"""
Portfolio Simulation Engine.

Contains the PortfolioSimulator class that runs Monte Carlo simulations
for portfolio NAV and dividend income projections.
"""

import numpy as np
from typing import Dict, Tuple, List

from .models import Asset, SimulationConfig
from .correlation import create_dividend_correlation_matrix
from .downturn_strategy import DownturnStrategy


class PortfolioSimulator:
    """
    Monte Carlo portfolio simulation engine with realistic dividend growth.
    
    Features:
    - Correlated NAV returns across assets
    - Correlated dividend growth shocks
    - Excess dividend growth modelling (above NAV growth)
    - Growth decay for high-growth assets
    - Self-balancing investment of contributions and dividends
    - Annual rebalancing to target weights
    - Downturn strategy integration
    - Dividend cuts during market stress with recovery
    """
    
    def __init__(self, config: SimulationConfig, assets: Dict[str, Asset]):
        self.config = config
        self.assets = assets
        self.asset_list = list(assets.keys())
        self.n_assets = len(self.asset_list)
        
        # Create correlation matrices
        self.div_corr, self.div_tickers = create_dividend_correlation_matrix(assets)
        self.nav_corr = self._create_nav_correlation_matrix()
        
        # Compute Cholesky decompositions for correlated sampling
        self.nav_chol = np.linalg.cholesky(self.nav_corr)
        self.div_chol = np.linalg.cholesky(self.div_corr)
        
        # Map tickers to correlation matrix indices
        self.ticker_to_div_idx = {t: i for i, t in enumerate(self.div_tickers)}
        
        # Base prices for simulation
        self.base_prices = np.ones(self.n_assets) * 100.0
        
        # Calculate excess dividend growth rates (above NAV growth)
        self.excess_growth_rates = self._calculate_excess_growth_rates()
        
        # Dividend resilience for cut probability
        self.dividend_resilience = np.array([
            self.assets[ticker].dividend_resilience for ticker in self.asset_list
        ])
        
    def _calculate_excess_growth_rates(self) -> np.ndarray:
        """
        Calculate excess dividend growth = dividend_growth - nav_growth.
        
        This represents yield expansion, floored at 0.
        """
        rates = np.zeros(self.n_assets)
        nav_growth = self.config.nav_mean_annual
        
        for i, ticker in enumerate(self.asset_list):
            asset = self.assets[ticker]
            excess = max(0, asset.dividend_growth_5yr - nav_growth)
            rates[i] = excess
        
        return rates
        
    def _create_nav_correlation_matrix(self) -> np.ndarray:
        """Create uniform NAV correlation matrix."""
        n = self.n_assets
        corr = np.full((n, n), self.config.nav_correlation)
        np.fill_diagonal(corr, 1.0)
        return corr    
    def _generate_benchmark_returns(self, rng: np.random.Generator, months: int) -> np.ndarray:
        """
        Generate monthly benchmark returns (FTSE All-World proxy).
        
        The benchmark has slightly lower volatility due to broader diversification.
        """
        mu = self.config.nav_mean_monthly
        sigma = self.config.nav_volatility_monthly * 0.95
        
        z = rng.standard_normal(months)
        log_returns = (mu - 0.5 * sigma**2) + sigma * z
        returns = np.exp(log_returns) - 1
        
        return returns
    
    def _generate_nav_returns(self, rng: np.random.Generator, months: int) -> np.ndarray:
        """Generate correlated monthly NAV returns for all assets."""
        z = rng.standard_normal((months, self.n_assets))
        corr_z = z @ self.nav_chol.T
        
        mu = self.config.nav_mean_monthly
        sigma = self.config.nav_volatility_monthly
        
        log_returns = (mu - 0.5 * sigma**2) + sigma * corr_z
        returns = np.exp(log_returns) - 1
        
        return returns
    
    def _generate_dividend_growth_shocks(self, rng: np.random.Generator, years: int) -> np.ndarray:
        """Generate correlated annual dividend growth shocks."""
        z = rng.standard_normal((years, len(self.div_tickers)))
        corr_z = z @ self.div_chol.T
        
        sigma = self.config.dividend_growth_volatility
        
        shocks = np.zeros((years, self.n_assets))
        
        for i, ticker in enumerate(self.asset_list):
            div_idx = self.ticker_to_div_idx.get(ticker, 0)
            asset_z = corr_z[:, div_idx]
            log_shock = -0.5 * sigma**2 + sigma * asset_z
            shocks[:, i] = np.exp(log_shock)
        
        return shocks
    
    def _get_contribution_schedule(self) -> Dict[Tuple[int, int], float]:
        """Build the contribution schedule from config."""
        contributions = {}
        
        # Lump sum in January 2026 (Year 0, Month 1)
        contributions[(0, 1)] = self.config.lump_sum
        
        # Monthly contributions from May 2026 (Year 0, Month 5) for 25 years
        month_counter = 0
        for year in range(26):
            start_month = 5 if year == 0 else 1
            for month in range(start_month, 13):
                if month_counter < self.config.monthly_contribution_months:
                    contributions[(year, month)] = contributions.get((year, month), 0) + self.config.monthly_contribution
                    month_counter += 1
        
        return contributions
    
    def _is_dividend_month(self, asset: Asset, month: int) -> bool:
        """Check if asset pays dividend in given month."""
        return month in asset.payment_months
    
    def _calculate_dividend(self, asset: Asset, units: float, base_div_per_unit: float,
                           excess_growth_factor: float) -> float:
        """
        Calculate net dividend payment.
        
        Uses realistic model where:
        - Base dividend is fixed at simulation start
        - Excess growth factor captures yield expansion above NAV growth
        - Withholding tax and ADR fees are applied
        """
        annual_div = units * base_div_per_unit * excess_growth_factor
        payment = annual_div / asset.payments_per_year
        
        # Apply withholding tax
        net_div = payment * (1 - asset.withholding_tax)
        
        if asset.is_adr:
            net_div *= (1 - self.config.adr_fee_rate)
        
        return net_div
    
    def _self_balance_investment(self, amount: float, units: np.ndarray, 
                                 prices: np.ndarray) -> np.ndarray:
        """
        Allocate investment to bring portfolio closer to target weights.
        
        Prioritizes underweight assets.
        """
        if amount <= 0:
            return np.zeros(self.n_assets)
        
        current_values = units * prices
        current_total = np.sum(current_values)
        new_total = current_total + amount
        
        target_weights = np.array([self.assets[t].allocation for t in self.asset_list])
        target_values = target_weights * new_total
        
        value_gaps = target_values - current_values
        value_gaps = np.maximum(value_gaps, 0)
        
        if np.sum(value_gaps) > 0:
            investment_allocation = value_gaps / np.sum(value_gaps) * amount
        else:
            investment_allocation = target_weights * amount
        
        additional_units = investment_allocation / prices
        
        return additional_units
    
    def _rebalance_portfolio(self, units: np.ndarray, prices: np.ndarray) -> np.ndarray:
        """Rebalance portfolio to target weights."""
        current_values = units * prices
        total_value = np.sum(current_values)
        
        target_weights = np.array([self.assets[t].allocation for t in self.asset_list])
        target_values = target_weights * total_value
        
        new_units = target_values / prices
        

        return new_units
    
    def _check_dividend_cuts(self, rng: np.random.Generator, drawdown: float,
                             dividend_cut_factors: np.ndarray, 
                             in_stress: bool) -> Tuple[np.ndarray, bool]:
        """
        Check and apply dividend cuts during market stress.
        
        Args:
            rng: Random number generator
            drawdown: Current benchmark drawdown (0-1)
            dividend_cut_factors: Current cut factors per asset (1.0 = no cut)
            in_stress: Whether we're currently in a stress period
            
        Returns:
            Tuple of (updated cut factors, updated stress state)
        """
        threshold = self.config.dividend_cut_drawdown_threshold
        
        # Check if entering stress period
        if drawdown >= threshold and not in_stress:
            # Entering stress - evaluate cuts for each asset
            in_stress = True
            base_prob = self.config.dividend_cut_base_probability
            
            # Scale probability by drawdown severity (deeper = more cuts)
            severity_scale = min(2.0, drawdown / threshold)
            
            for i, ticker in enumerate(self.asset_list):
                asset = self.assets[ticker]
                # Probability adjusted by asset resilience
                cut_prob = base_prob * asset.cut_probability_modifier * severity_scale
                
                if rng.random() < cut_prob:
                    # Apply a cut - severity is random within range
                    cut_severity = rng.uniform(
                        self.config.dividend_cut_severity_min,
                        self.config.dividend_cut_severity_max
                    )
                    # Factor is the remaining portion (e.g., 0.7 means 30% cut)
                    dividend_cut_factors[i] *= (1.0 - cut_severity)
        
        # Check if exiting stress period
        elif drawdown < threshold * 0.5 and in_stress:
            # Market recovered significantly - exit stress
            in_stress = False
        
        return dividend_cut_factors, in_stress
    
    def _apply_dividend_recovery(self, dividend_cut_factors: np.ndarray, 
                                  in_stress: bool) -> np.ndarray:
        """
        Apply gradual dividend recovery when not in stress.
        
        Args:
            dividend_cut_factors: Current cut factors per asset
            in_stress: Whether we're in a stress period
            
        Returns:
            Updated cut factors (moving toward 1.0)
        """
        if in_stress:
            return dividend_cut_factors
        
        # Annual recovery rate applied monthly
        monthly_recovery = self.config.dividend_recovery_rate / 12
        
        for i in range(self.n_assets):
            if dividend_cut_factors[i] < 1.0:
                # Recover toward 1.0
                gap = 1.0 - dividend_cut_factors[i]
                dividend_cut_factors[i] += gap * monthly_recovery
                dividend_cut_factors[i] = min(1.0, dividend_cut_factors[i])
        
        return dividend_cut_factors
    
    def run_single_simulation(self, rng: np.random.Generator) -> Dict:
        """
        Run a single Monte Carlo simulation path.
        
        Returns dictionary with monthly NAV, income, and annual statistics.
        """
        total_months = self.config.total_months
        total_years = self.config.accumulation_years + self.config.post_accumulation_years + 1
        
        # Generate random paths
        nav_returns = self._generate_nav_returns(rng, total_months)
        benchmark_returns = self._generate_benchmark_returns(rng, total_months)
        div_growth_shocks = self._generate_dividend_growth_shocks(rng, total_years + 1)
        
        contributions = self._get_contribution_schedule()
        
        # Initialize state
        units = np.zeros(self.n_assets)
        prices = self.base_prices.copy()
        
        # Base dividend per unit (fixed at simulation start)
        base_div_per_unit = np.array([
            self.base_prices[i] * self.assets[ticker].forward_yield 
            for i, ticker in enumerate(self.asset_list)
        ])
        
        excess_growth_factors = np.ones(self.n_assets)
        current_excess_rates = self.excess_growth_rates.copy()
        
        # Dividend cut tracking
        dividend_cut_factors = np.ones(self.n_assets)  # 1.0 = no cut
        in_dividend_stress = False
        benchmark_value = 100.0
        benchmark_peak = 100.0
        total_dividend_cuts = 0
        
        # Output arrays
        monthly_nav = []
        monthly_income = []
        annual_income = np.zeros(total_years + 1)
        annual_dividends_total = np.zeros(total_years + 1)
        
        # Initialize downturn strategy
        downturn_strategy = DownturnStrategy(self.config)
        total_downturn_deployed = 0.0
        
        for month_idx in range(total_months):
            year = month_idx // 12
            month = (month_idx % 12) + 1
            
            is_accumulation = year < self.config.accumulation_years
            
            # 1. Apply monthly NAV return to prices
            for i in range(self.n_assets):
                prices[i] *= (1 + nav_returns[month_idx, i])
            
            # Update benchmark tracking for dividend cuts
            benchmark_value *= (1 + benchmark_returns[month_idx])
            if benchmark_value > benchmark_peak:
                benchmark_peak = benchmark_value
            benchmark_drawdown = (benchmark_peak - benchmark_value) / benchmark_peak if benchmark_peak > 0 else 0
            
            # Check for dividend cuts
            prev_cut_factors = dividend_cut_factors.copy()
            dividend_cut_factors, in_dividend_stress = self._check_dividend_cuts(
                rng, benchmark_drawdown, dividend_cut_factors, in_dividend_stress
            )
            # Count new cuts
            total_dividend_cuts += np.sum(dividend_cut_factors < prev_cut_factors)
            
            # Apply dividend recovery when not in stress
            dividend_cut_factors = self._apply_dividend_recovery(dividend_cut_factors, in_dividend_stress)
            
            # 2. Process dividends (now including cut factors)
            monthly_div_income = 0
            monthly_div_reinvest = 0
            
            for i, ticker in enumerate(self.asset_list):
                asset = self.assets[ticker]
                
                if self._is_dividend_month(asset, month) and units[i] > 0:
                    div = self._calculate_dividend(
                        asset, units[i], base_div_per_unit[i], 
                        excess_growth_factors[i] * dividend_cut_factors[i]  # Apply cut factor
                    )
                    
                    annual_dividends_total[year] += div
                    
                    if is_accumulation:
                        monthly_div_reinvest += div
                    else:
                        reinvest = div * self.config.dividend_reinvestment_rate_post
                        withdraw = div * self.config.dividend_withdrawal_rate_post
                        monthly_div_reinvest += reinvest
                        monthly_div_income += withdraw
                        annual_income[year] += withdraw
            
            if monthly_div_reinvest > 0:
                additional_units = self._self_balance_investment(
                    monthly_div_reinvest, units, prices
                )
                units += additional_units
            
            monthly_income.append(monthly_div_income)
            
            # 3. Apply contributions
            contrib = contributions.get((year, month), 0)
            if contrib > 0:
                additional_units = self._self_balance_investment(contrib, units, prices)
                units += additional_units
            
            # 4. January: dividend growth shock + annual rebalancing
            if month == 1:
                for i in range(self.n_assets):
                    shock = div_growth_shocks[year, i]
                    excess_growth_factors[i] *= (1 + current_excess_rates[i]) * shock
                    
                    if current_excess_rates[i] > 0.05:
                        current_excess_rates[i] *= self.config.excess_growth_decay
                
                if year > 0:
                    units = self._rebalance_portfolio(units, prices)
            
            # 5. Downturn strategy processing
            downturn_strategy.update_benchmark(benchmark_returns[month_idx])
            
            deployment_amount = downturn_strategy.check_and_deploy(month_idx)
            if deployment_amount > 0:
                additional_units = self._self_balance_investment(deployment_amount, units, prices)
                units += additional_units
                total_downturn_deployed += deployment_amount
            
            downturn_strategy.process_monthly_rebuild()
            
            # Record NAV
            nav = np.sum(units * prices)
            monthly_nav.append(nav)
        
        return {
            'monthly_nav': np.array(monthly_nav),
            'monthly_income': np.array(monthly_income),
            'annual_income': annual_income,
            'annual_dividends_total': annual_dividends_total,
            'final_nav': monthly_nav[-1] if monthly_nav else 0,
            'downturn_deployed': total_downturn_deployed,
            'downturn_events': len(downturn_strategy.deployment_events),
            'dividend_cuts': total_dividend_cuts,
        }
    
    def run_simulation(self) -> Dict:
        """
        Run full Monte Carlo simulation.
        
        Returns dictionary with all simulation paths and config.
        """
        rng = np.random.default_rng(self.config.random_seed)
        
        n_sims = self.config.num_simulations
        total_months = self.config.total_months
        total_years = self.config.accumulation_years + self.config.post_accumulation_years + 1
        
        all_nav = np.zeros((n_sims, total_months))
        all_income = np.zeros((n_sims, total_months))
        all_annual_income = np.zeros((n_sims, total_years + 1))
        all_annual_dividends = np.zeros((n_sims, total_years + 1))
        all_dividend_cuts = np.zeros(n_sims)
        all_downturn_events = np.zeros(n_sims)
        all_downturn_deployed = np.zeros(n_sims)
        
        print(f"Running {n_sims:,} Monte Carlo simulations...")
        
        for sim in range(n_sims):
            if (sim + 1) % 2000 == 0:
                print(f"  Completed {sim + 1:,} simulations...")
            
            result = self.run_single_simulation(rng)
            all_nav[sim] = result['monthly_nav']
            all_income[sim] = result['monthly_income']
            all_dividend_cuts[sim] = result['dividend_cuts']
            all_downturn_events[sim] = result['downturn_events']
            all_downturn_deployed[sim] = result['downturn_deployed']
            
            income_len = min(len(result['annual_income']), all_annual_income.shape[1])
            all_annual_income[sim, :income_len] = result['annual_income'][:income_len]
            all_annual_dividends[sim, :income_len] = result['annual_dividends_total'][:income_len]
        
        print("Simulation complete.")
        
        return {
            'all_nav': all_nav,
            'all_income': all_income,
            'all_annual_income': all_annual_income,
            'all_annual_dividends': all_annual_dividends,
            'all_dividend_cuts': all_dividend_cuts,
            'all_downturn_events': all_downturn_events,
            'all_downturn_deployed': all_downturn_deployed,
            'config': self.config,
        }
