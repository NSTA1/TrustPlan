"""
Portfolio NAV and Income Projection Monte Carlo Simulation

This script implements a 30-year Monte Carlo simulation for portfolio-level 
dividend income projection based on the SDG and modelling specifications.

REVISED: Uses realistic dividend growth model that avoids double-counting
NAV appreciation and dividend growth.
"""

import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Tuple
from datetime import date
import warnings
warnings.filterwarnings('ignore')


@dataclass
class Asset:
    """Represents a single asset in the portfolio."""
    name: str
    ticker: str
    allocation: float
    forward_yield: float
    withholding_tax: float
    dividend_growth_5yr: float
    payment_frequency: str
    payment_months: List[int]
    is_adr: bool = False
    
    @property
    def effective_yield(self) -> float:
        return self.forward_yield * (1 - self.withholding_tax)
    
    @property
    def payments_per_year(self) -> int:
        return len(self.payment_months)


@dataclass
class SimulationConfig:
    """Configuration parameters for the simulation."""
    start_date: date = date(2025, 12, 9)
    accumulation_years: int = 25
    post_accumulation_years: int = 5
    
    # REVISED: More conservative NAV assumptions
    nav_mean_annual: float = 0.05  # 5% real (was 7%)
    nav_volatility_annual: float = 0.18  # 18% (was 20%)
    nav_correlation: float = 0.60  # 0.6 (was 0.7)
    
    # Dividend modelling
    dividend_growth_volatility: float = 0.05
    excess_growth_decay: float = 0.95  # High-growth assets decay toward mean
    
    num_simulations: int = 10000  # Increased for better statistics
    random_seed: int = 42
    
    lump_sum: float = 55500.0
    weekly_contribution: float = 2300.0
    weekly_contribution_weeks: int = 20
    monthly_contribution: float = 1666.0
    monthly_contribution_months: int = 300
    
    dividend_reinvestment_rate_post: float = 0.40
    dividend_withdrawal_rate_post: float = 0.60
    
    adr_fee_rate: float = 0.005
    
    @property
    def nav_mean_monthly(self) -> float:
        return self.nav_mean_annual / 12
    
    @property
    def nav_volatility_monthly(self) -> float:
        return self.nav_volatility_annual / np.sqrt(12)
    
    @property
    def total_months(self) -> int:
        return (self.accumulation_years + self.post_accumulation_years + 1) * 12


def create_assets() -> Dict[str, Asset]:
    """Create the portfolio assets with all required parameters."""
    assets_data = [
        ("Microsoft", "MSFT", 0.07, 0.0075, 0.15, 0.102, "Quarterly", [3, 6, 9, 12], False),
        ("Mastercard", "MA", 0.07, 0.0052, 0.15, 0.142, "Quarterly", [2, 5, 8, 11], False),
        ("JP Morgan", "JPM", 0.06, 0.019, 0.15, 0.1188, "Quarterly", [1, 4, 7, 10], False),
        ("Coloplast", "CLPBY", 0.05, 0.033, 0.27, 0.056, "Annual", [12], True),
        ("Hoya", "HOCPY", 0.05, 0.0043, 0.15, 0.053, "Semi-Annual", [6, 12], True),
        ("Japan Exchange", "JPXGY", 0.05, 0.018, 0.15, 0.125, "Semi-Annual", [6, 12], True),
        ("Waste Management", "WM", 0.05, 0.0144, 0.15, 0.083, "Quarterly", [3, 6, 9, 12], False),
        ("Wolters Kluwer", "WKL", 0.05, 0.014, 0.15, 0.1096, "Semi-Annual", [5, 9], False),
        ("ASML", "ASML", 0.04, 0.01, 0.15, 0.208, "Semi-Annual", [5, 11], False),
        ("Chubb", "CB", 0.04, 0.0131, 0.15, 0.0447, "Quarterly", [1, 4, 7, 10], False),
        ("Novo Nordisk", "NVO", 0.04, 0.0164, 0.27, 0.191, "Annual", [3], False),
        ("RELX", "REL", 0.04, 0.0208, 0.0, 0.068, "Semi-Annual", [6, 9], False),
        ("S&P Global", "SPGI", 0.04, 0.0078, 0.15, 0.099, "Quarterly", [3, 6, 9, 12], False),
        ("ADP", "ADP", 0.03, 0.0201, 0.15, 0.128, "Quarterly", [1, 4, 7, 10], False),
        ("Canadian National Railway", "CNR", 0.03, 0.0261, 0.25, 0.102, "Quarterly", [3, 6, 9, 12], False),
        ("EssilorLuxottica", "EL", 0.03, 0.0187, 0.25, 0.23, "Annual", [5], False),
        ("Essex Property Trust", "ESS", 0.03, 0.035, 0.15, 0.055, "Quarterly", [1, 4, 7, 10], False),
        ("Hermes International", "RMS", 0.03, 0.008, 0.25, 0.16, "Annual", [5], False),
        ("Lockheed Martin", "LMT", 0.03, 0.027, 0.15, 0.0722, "Quarterly", [3, 6, 9, 12], False),
        ("LOreal", "OR", 0.03, 0.0189, 0.25, 0.128, "Annual", [5], False),
        ("LVMH", "MC", 0.03, 0.02, 0.25, 0.23, "Semi-Annual", [4, 12], False),
        ("Stryker", "SYK", 0.03, 0.0092, 0.15, 0.088, "Quarterly", [1, 4, 7, 10], False),
        ("Accenture", "ACN", 0.02, 0.0216, 0.15, 0.12, "Quarterly", [2, 5, 8, 11], False),
        ("BAE Systems", "BA", 0.02, 0.029, 0.0, 0.065, "Semi-Annual", [6, 12], False),
        ("London Stock Exchange Group", "LSEG", 0.02, 0.0153, 0.0, 0.145, "Semi-Annual", [5, 9], False),
        ("SMFG", "SMFG", 0.02, 0.0271, 0.15, 0.136, "Semi-Annual", [6, 12], True),
    ]
    
    assets = {}
    for data in assets_data:
        name, ticker, alloc, fwd_yield, wht, div_growth, freq, months, is_adr = data
        assets[ticker] = Asset(
            name=name, ticker=ticker, allocation=alloc,
            forward_yield=fwd_yield, withholding_tax=wht,
            dividend_growth_5yr=div_growth, payment_frequency=freq,
            payment_months=months, is_adr=is_adr
        )
    return assets


def create_dividend_correlation_matrix(assets: Dict[str, Asset]) -> Tuple[np.ndarray, List[str]]:
    """Create the dividend growth correlation matrix."""
    tickers = ['MSFT', 'SPGI', 'CB', 'WM', 'ADP', 'ACN', 'SYK', 'MA', 'ASML', 'NVO', 
               'CLPBY', 'MC', 'EL', 'RMS', 'REL', 'LSEG', 'OR', 'WKL', 'JPM', 'CNR',
               'HOCPY', 'JPXGY', 'SMFG', 'LMT', 'BA', 'ESS']
    
    n = len(tickers)
    corr = np.eye(n)
    
    correlations = {
        ('MSFT', 'SPGI'): 0.55, ('MSFT', 'ACN'): 0.55, ('MSFT', 'ADP'): 0.50,
        ('SPGI', 'ACN'): 0.55, ('SPGI', 'ADP'): 0.50, ('SPGI', 'JPXGY'): 0.45,
        ('CB', 'JPM'): 0.55, ('CB', 'SMFG'): 0.45,
        ('ADP', 'ACN'): 0.55, ('ADP', 'SYK'): 0.45,
        ('ACN', 'SYK'): 0.45, ('ACN', 'ASML'): 0.45,
        ('ASML', 'NVO'): 0.50, ('ASML', 'CLPBY'): 0.45,
        ('NVO', 'CLPBY'): 0.50,
        ('MC', 'EL'): 0.55, ('MC', 'RMS'): 0.60, ('MC', 'OR'): 0.55,
        ('EL', 'RMS'): 0.55, ('EL', 'OR'): 0.55,
        ('RMS', 'OR'): 0.55,
        ('REL', 'LSEG'): 0.50, ('REL', 'WKL'): 0.40,
        ('LSEG', 'JPXGY'): 0.50, ('LSEG', 'WKL'): 0.40,
        ('JPM', 'SMFG'): 0.50, ('JPM', 'ESS'): 0.40,
        ('LMT', 'BA'): 0.50,
    }
    
    ticker_idx = {t: i for i, t in enumerate(tickers)}
    
    for (t1, t2), rho in correlations.items():
        if t1 in ticker_idx and t2 in ticker_idx:
            i, j = ticker_idx[t1], ticker_idx[t2]
            corr[i, j] = rho
            corr[j, i] = rho
    
    for i in range(n):
        for j in range(n):
            if i != j and corr[i, j] == 0:
                corr[i, j] = 0.30
    
    return corr, tickers


class PortfolioSimulator:
    """Monte Carlo portfolio simulation engine with realistic dividend growth."""
    
    def __init__(self, config: SimulationConfig, assets: Dict[str, Asset]):
        self.config = config
        self.assets = assets
        self.asset_list = list(assets.keys())
        self.n_assets = len(self.asset_list)
        
        self.div_corr, self.div_tickers = create_dividend_correlation_matrix(assets)
        self.nav_corr = self._create_nav_correlation_matrix()
        
        self.nav_chol = np.linalg.cholesky(self.nav_corr)
        self.div_chol = np.linalg.cholesky(self.div_corr)
        
        self.ticker_to_div_idx = {t: i for i, t in enumerate(self.div_tickers)}
        self.base_prices = np.ones(self.n_assets) * 100.0
        
        # Calculate excess dividend growth rates (above NAV growth)
        self.excess_growth_rates = self._calculate_excess_growth_rates()
        
    def _calculate_excess_growth_rates(self) -> np.ndarray:
        """
        Calculate excess dividend growth = dividend_growth - nav_growth
        This represents yield expansion, floored at 0.
        """
        rates = np.zeros(self.n_assets)
        nav_growth = self.config.nav_mean_annual
        
        for i, ticker in enumerate(self.asset_list):
            asset = self.assets[ticker]
            # Excess growth is the portion above NAV growth
            excess = max(0, asset.dividend_growth_5yr - nav_growth)
            rates[i] = excess
        
        return rates
        
    def _create_nav_correlation_matrix(self) -> np.ndarray:
        n = self.n_assets
        corr = np.full((n, n), self.config.nav_correlation)
        np.fill_diagonal(corr, 1.0)
        return corr
    
    def _generate_nav_returns(self, rng: np.random.Generator, months: int) -> np.ndarray:
        z = rng.standard_normal((months, self.n_assets))
        corr_z = z @ self.nav_chol.T
        
        mu = self.config.nav_mean_monthly
        sigma = self.config.nav_volatility_monthly
        
        log_returns = (mu - 0.5 * sigma**2) + sigma * corr_z
        returns = np.exp(log_returns) - 1
        
        return returns
    
    def _generate_dividend_growth_shocks(self, rng: np.random.Generator, years: int) -> np.ndarray:
        """Generate shocks around 1.0 for excess dividend growth."""
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
        contributions = {}
        
        contributions[(0, 1)] = self.config.lump_sum
        
        weekly_months = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
        weekly_distribution = [2, 4, 4, 4, 4]
        
        for (y, m), weeks in zip(weekly_months, weekly_distribution):
            key = (y, m)
            contributions[key] = contributions.get(key, 0) + weeks * self.config.weekly_contribution
        
        month_counter = 0
        for year in range(26):
            start_month = 6 if year == 0 else 1
            for month in range(start_month, 13):
                if month_counter < self.config.monthly_contribution_months:
                    contributions[(year, month)] = contributions.get((year, month), 0) + self.config.monthly_contribution
                    month_counter += 1
        
        return contributions
    
    def _is_dividend_month(self, asset: Asset, month: int) -> bool:
        return month in asset.payment_months
    
    def _calculate_dividend(self, asset: Asset, units: float, base_div_per_unit: float,
                           excess_growth_factor: float) -> float:
        """
        Calculate dividend using the realistic model.
        
        Dividend = units * base_div_per_unit * excess_growth_factor
        
        Where:
        - base_div_per_unit is fixed at simulation start (initial_price * yield)
        - excess_growth_factor compounds only the excess growth above NAV
        - NAV growth is already captured in the number of units (via reinvestment)
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
        current_values = units * prices
        total_value = np.sum(current_values)
        
        target_weights = np.array([self.assets[t].allocation for t in self.asset_list])
        target_values = target_weights * total_value
        
        new_units = target_values / prices
        
        return new_units
    
    def run_single_simulation(self, rng: np.random.Generator) -> Dict:
        total_months = self.config.total_months
        total_years = self.config.accumulation_years + self.config.post_accumulation_years + 1
        
        nav_returns = self._generate_nav_returns(rng, total_months)
        div_growth_shocks = self._generate_dividend_growth_shocks(rng, total_years + 1)
        
        contributions = self._get_contribution_schedule()
        
        units = np.zeros(self.n_assets)
        prices = self.base_prices.copy()
        
        # Base dividend per unit = initial_price * forward_yield (fixed)
        base_div_per_unit = np.array([
            self.base_prices[i] * self.assets[ticker].forward_yield 
            for i, ticker in enumerate(self.asset_list)
        ])
        
        # Excess growth factors start at 1.0
        excess_growth_factors = np.ones(self.n_assets)
        
        # Current excess growth rates (may decay over time)
        current_excess_rates = self.excess_growth_rates.copy()
        
        monthly_nav = []
        monthly_income = []
        annual_income = np.zeros(total_years + 1)
        annual_dividends_total = np.zeros(total_years + 1)
        
        for month_idx in range(total_months):
            year = month_idx // 12
            month = (month_idx % 12) + 1
            
            is_accumulation = year < self.config.accumulation_years
            
            # 1. Apply monthly NAV return to prices
            for i in range(self.n_assets):
                prices[i] *= (1 + nav_returns[month_idx, i])
            
            # 2. Process dividends
            monthly_div_income = 0
            monthly_div_reinvest = 0
            
            for i, ticker in enumerate(self.asset_list):
                asset = self.assets[ticker]
                
                if self._is_dividend_month(asset, month) and units[i] > 0:
                    div = self._calculate_dividend(
                        asset, units[i], base_div_per_unit[i], excess_growth_factors[i]
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
                # Apply excess dividend growth for this year
                for i in range(self.n_assets):
                    shock = div_growth_shocks[year, i]
                    excess_growth_factors[i] *= (1 + current_excess_rates[i]) * shock
                    
                    # Apply decay to high excess growth rates
                    if current_excess_rates[i] > 0.05:
                        current_excess_rates[i] *= self.config.excess_growth_decay
                
                if year > 0:
                    units = self._rebalance_portfolio(units, prices)
            
            nav = np.sum(units * prices)
            monthly_nav.append(nav)
        
        return {
            'monthly_nav': np.array(monthly_nav),
            'monthly_income': np.array(monthly_income),
            'annual_income': annual_income,
            'annual_dividends_total': annual_dividends_total,
            'final_nav': monthly_nav[-1] if monthly_nav else 0,
        }
    
    def run_simulation(self) -> Dict:
        rng = np.random.default_rng(self.config.random_seed)
        
        n_sims = self.config.num_simulations
        total_months = self.config.total_months
        total_years = self.config.accumulation_years + self.config.post_accumulation_years + 1
        
        all_nav = np.zeros((n_sims, total_months))
        all_income = np.zeros((n_sims, total_months))
        all_annual_income = np.zeros((n_sims, total_years + 1))
        all_annual_dividends = np.zeros((n_sims, total_years + 1))
        
        print(f"Running {n_sims:,} Monte Carlo simulations...")
        
        for sim in range(n_sims):
            if (sim + 1) % 2000 == 0:
                print(f"  Completed {sim + 1:,} simulations...")
            
            result = self.run_single_simulation(rng)
            all_nav[sim] = result['monthly_nav']
            all_income[sim] = result['monthly_income']
            
            income_len = min(len(result['annual_income']), all_annual_income.shape[1])
            all_annual_income[sim, :income_len] = result['annual_income'][:income_len]
            all_annual_dividends[sim, :income_len] = result['annual_dividends_total'][:income_len]
        
        print("Simulation complete.")
        
        return {
            'all_nav': all_nav,
            'all_income': all_income,
            'all_annual_income': all_annual_income,
            'all_annual_dividends': all_annual_dividends,
            'config': self.config,
        }


def analyze_results(results: Dict) -> Dict:
    """Analyze simulation results and compute statistics."""
    config = results['config']
    all_nav = results['all_nav']
    all_annual_income = results['all_annual_income']
    all_annual_dividends = results['all_annual_dividends']
    
    total_years = config.accumulation_years + config.post_accumulation_years + 1
    
    stats = {}
    
    for year in [5, 10, 15, 20, 25, 30]:
        if year <= total_years:
            month_idx = min(year * 12 - 1, all_nav.shape[1] - 1)
            nav_at_year = all_nav[:, month_idx]
            stats[f'nav_year_{year}'] = {
                'median': np.median(nav_at_year),
                'p5': np.percentile(nav_at_year, 5),
                'p25': np.percentile(nav_at_year, 25),
                'p75': np.percentile(nav_at_year, 75),
                'p95': np.percentile(nav_at_year, 95),
                'mean': np.mean(nav_at_year),
            }
    
    dividend_stats = {}
    for year in range(20, min(total_years + 1, all_annual_dividends.shape[1])):
        dividends = all_annual_dividends[:, year]
        dividend_stats[f'year_{year}'] = {
            'median': np.median(dividends),
            'p5': np.percentile(dividends, 5),
            'p25': np.percentile(dividends, 25),
            'p75': np.percentile(dividends, 75),
            'p95': np.percentile(dividends, 95),
            'mean': np.mean(dividends),
            'min': np.min(dividends),
            'max': np.max(dividends),
        }
    stats['annual_dividends'] = dividend_stats
    
    income_stats = {}
    for year in range(26, min(total_years + 1, all_annual_income.shape[1])):
        income = all_annual_income[:, year]
        income_stats[f'year_{year}'] = {
            'median': np.median(income),
            'p5': np.percentile(income, 5),
            'p25': np.percentile(income, 25),
            'p75': np.percentile(income, 75),
            'p95': np.percentile(income, 95),
            'mean': np.mean(income),
            'min': np.min(income),
            'max': np.max(income),
        }
    stats['annual_income'] = income_stats
    
    if 26 < all_annual_income.shape[1] and 30 < all_annual_income.shape[1]:
        income_26 = all_annual_income[:, 26]
        income_30 = all_annual_income[:, 30]
        
        valid_mask = (income_26 > 0) & (income_30 > 0)
        if np.sum(valid_mask) > 0:
            cagr = (income_30[valid_mask] / income_26[valid_mask]) ** (1/4) - 1
            stats['income_cagr_26_30'] = {
                'median': np.median(cagr),
                'p5': np.percentile(cagr, 5),
                'p95': np.percentile(cagr, 95),
                'mean': np.mean(cagr),
            }
    
    final_nav = all_nav[:, -1]
    best_idx = np.argmax(final_nav)
    worst_idx = np.argmin(final_nav)
    median_idx = np.argsort(final_nav)[len(final_nav)//2]
    
    year_30_idx = min(30, all_annual_income.shape[1] - 1)
    
    stats['best_case'] = {
        'final_nav': final_nav[best_idx],
        'year_30_income': all_annual_income[best_idx, year_30_idx],
        'year_30_dividends': all_annual_dividends[best_idx, year_30_idx],
    }
    stats['worst_case'] = {
        'final_nav': final_nav[worst_idx],
        'year_30_income': all_annual_income[worst_idx, year_30_idx],
        'year_30_dividends': all_annual_dividends[worst_idx, year_30_idx],
    }
    stats['median_case'] = {
        'final_nav': final_nav[median_idx],
        'year_30_income': all_annual_income[median_idx, year_30_idx],
        'year_30_dividends': all_annual_dividends[median_idx, year_30_idx],
    }
    
    return stats


def generate_report(stats: Dict, config: SimulationConfig) -> str:
    """Generate a markdown report of the simulation results."""
    report = []
    report.append("# Portfolio NAV and Income Projection Report")
    report.append("")
    report.append("## Simulation Parameters")
    report.append("")
    report.append(f"- **Number of simulations**: {config.num_simulations:,}")
    report.append("- **Simulation period**: 30 years (December 2025 - December 2055)")
    report.append("- **Accumulation phase**: Years 0-25 (100% dividend reinvestment)")
    report.append("- **Post-accumulation phase**: Years 26-30 (60% dividend withdrawal)")
    report.append(f"- **NAV expected return**: {config.nav_mean_annual:.1%} real annual")
    report.append(f"- **NAV volatility**: {config.nav_volatility_annual:.1%} annual")
    report.append(f"- **Dividend growth volatility**: {config.dividend_growth_volatility:.1%}")
    report.append(f"- **Excess growth decay factor**: {config.excess_growth_decay}")
    report.append("")
    
    total_weekly = config.weekly_contribution * config.weekly_contribution_weeks
    total_monthly = config.monthly_contribution * config.monthly_contribution_months
    total_contributions = config.lump_sum + total_weekly + total_monthly
    report.append("## Total Contributions")
    report.append("")
    report.append(f"- **Lump sum**: GBP {config.lump_sum:,.0f}")
    report.append(f"- **Weekly contributions**: GBP {total_weekly:,.0f} ({config.weekly_contribution_weeks} weeks)")
    report.append(f"- **Monthly contributions**: GBP {total_monthly:,.0f} (25 years)")
    report.append(f"- **Total contributions**: GBP {total_contributions:,.0f}")
    report.append("")
    
    report.append("## NAV Projections (GBP Real Terms)")
    report.append("")
    report.append("| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |")
    report.append("|------|----------|-----------|--------|-----------|-----------|")
    
    for year in [5, 10, 15, 20, 25, 30]:
        key = f'nav_year_{year}'
        if key in stats:
            s = stats[key]
            report.append(f"| {year} | GBP {s['p5']:,.0f} | GBP {s['p25']:,.0f} | GBP {s['median']:,.0f} | GBP {s['p75']:,.0f} | GBP {s['p95']:,.0f} |")
    
    report.append("")
    
    report.append("## Annual Net Dividends (Years 20-25, Accumulation Phase)")
    report.append("")
    report.append("*All dividends reinvested during accumulation phase*")
    report.append("")
    report.append("| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |")
    report.append("|------|----------|-----------|--------|-----------|-----------|")
    
    for year in range(20, 26):
        key = f'year_{year}'
        if key in stats.get('annual_dividends', {}):
            s = stats['annual_dividends'][key]
            report.append(f"| {year} | GBP {s['p5']:,.0f} | GBP {s['p25']:,.0f} | GBP {s['median']:,.0f} | GBP {s['p75']:,.0f} | GBP {s['p95']:,.0f} |")
    
    report.append("")
    
    report.append("## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)")
    report.append("")
    report.append("*Income represents 60% of net dividends withdrawn*")
    report.append("")
    report.append("| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |")
    report.append("|------|----------|-----------|--------|-----------|-----------|")
    
    for year in range(26, 31):
        key = f'year_{year}'
        if key in stats.get('annual_income', {}):
            s = stats['annual_income'][key]
            report.append(f"| {year} | GBP {s['p5']:,.0f} | GBP {s['p25']:,.0f} | GBP {s['median']:,.0f} | GBP {s['p75']:,.0f} | GBP {s['p95']:,.0f} |")
    
    report.append("")
    
    report.append("## Total Annual Dividends (Years 26-30)")
    report.append("")
    report.append("*Total dividends before 60/40 split*")
    report.append("")
    report.append("| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |")
    report.append("|------|----------|-----------|--------|-----------|-----------|")
    
    for year in range(26, 31):
        key = f'year_{year}'
        if key in stats.get('annual_dividends', {}):
            s = stats['annual_dividends'][key]
            report.append(f"| {year} | GBP {s['p5']:,.0f} | GBP {s['p25']:,.0f} | GBP {s['median']:,.0f} | GBP {s['p75']:,.0f} | GBP {s['p95']:,.0f} |")
    
    report.append("")
    
    if 'income_cagr_26_30' in stats:
        cagr = stats['income_cagr_26_30']
        report.append("## Income Growth (Years 26-30)")
        report.append("")
        report.append(f"- **Median CAGR**: {cagr['median']:.1%}")
        report.append(f"- **5th percentile CAGR**: {cagr['p5']:.1%}")
        report.append(f"- **95th percentile CAGR**: {cagr['p95']:.1%}")
        report.append("")
    
    report.append("## Scenario Analysis")
    report.append("")
    report.append("### Best Case Path (95th percentile NAV)")
    report.append(f"- **Final NAV (Year 30)**: GBP {stats['best_case']['final_nav']:,.0f}")
    report.append(f"- **Year 30 Total Dividends**: GBP {stats['best_case']['year_30_dividends']:,.0f}")
    report.append(f"- **Year 30 Income Withdrawn**: GBP {stats['best_case']['year_30_income']:,.0f}")
    report.append("")
    report.append("### Median Case Path")
    report.append(f"- **Final NAV (Year 30)**: GBP {stats['median_case']['final_nav']:,.0f}")
    report.append(f"- **Year 30 Total Dividends**: GBP {stats['median_case']['year_30_dividends']:,.0f}")
    report.append(f"- **Year 30 Income Withdrawn**: GBP {stats['median_case']['year_30_income']:,.0f}")
    report.append("")
    report.append("### Worst Case Path (5th percentile NAV)")
    report.append(f"- **Final NAV (Year 30)**: GBP {stats['worst_case']['final_nav']:,.0f}")
    report.append(f"- **Year 30 Total Dividends**: GBP {stats['worst_case']['year_30_dividends']:,.0f}")
    report.append(f"- **Year 30 Income Withdrawn**: GBP {stats['worst_case']['year_30_income']:,.0f}")
    report.append("")
    
    report.append("## Model Notes (Revised)")
    report.append("")
    report.append("This simulation uses a **realistic dividend growth model**:")
    report.append("")
    report.append("1. **NAV Growth**: 5% real annual return (conservative)")
    report.append("2. **Dividend Growth**: Modelled as excess growth above NAV growth")
    report.append("   - Historical 5-year dividend growth already includes underlying earnings growth")
    report.append("   - Only the 'excess' portion (dividend growth minus NAV growth) is applied additionally")
    report.append("   - This prevents double-counting of growth")
    report.append("3. **Growth Decay**: High excess growth rates decay toward sustainable levels over time")
    report.append("4. **Dividend Calculation**: `dividend = units x base_dividend x excess_growth_factor`")
    report.append("   - Base dividend fixed at start (initial_price x yield)")
    report.append("   - Growth in units (via reinvestment) captures NAV appreciation")
    report.append("   - Excess growth factor captures yield expansion")
    report.append("")
    
    report.append("---")
    report.append("")
    report.append("*Report generated using Monte Carlo simulation based on SDG portfolio specifications.*")
    report.append("*All values in GBP real terms (inflation-adjusted).*")
    
    return "\n".join(report)


def main():
    """Main entry point for the simulation."""
    print("=" * 60)
    print("Portfolio NAV and Income Projection Simulation")
    print("(REVISED - Realistic Dividend Growth Model)")
    print("=" * 60)
    print()
    
    config = SimulationConfig(
        num_simulations=10000,
        random_seed=42
    )
    
    assets = create_assets()
    print(f"Loaded {len(assets)} assets")
    
    total_allocation = sum(a.allocation for a in assets.values())
    print(f"Total allocation: {total_allocation:.0%}")
    
    weighted_yield = sum(a.allocation * a.effective_yield for a in assets.values())
    print(f"Portfolio weighted yield (after tax): {weighted_yield:.2%}")
    
    weighted_growth = sum(a.allocation * a.dividend_growth_5yr for a in assets.values())
    print(f"Portfolio weighted dividend growth (historical): {weighted_growth:.2%}")
    
    # Calculate excess growth
    weighted_excess = sum(
        a.allocation * max(0, a.dividend_growth_5yr - config.nav_mean_annual) 
        for a in assets.values()
    )
    print(f"Portfolio weighted excess dividend growth: {weighted_excess:.2%}")
    print(f"NAV growth assumption: {config.nav_mean_annual:.1%}")
    print()
    
    simulator = PortfolioSimulator(config, assets)
    results = simulator.run_simulation()
    
    print("\nAnalyzing results...")
    stats = analyze_results(results)
    
    report = generate_report(stats, config)
    
    with open("projection_report.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    print("\nReport saved to projection_report.md")
    print()
    
    print("=" * 60)
    print("SUMMARY (Realistic Model)")
    print("=" * 60)
    print()
    
    total_contributions = config.lump_sum + config.weekly_contribution * config.weekly_contribution_weeks + config.monthly_contribution * config.monthly_contribution_months
    print(f"Total contributions: GBP {total_contributions:,.0f}")
    print()
    
    print("NAV Projections (Median):")
    for year in [5, 10, 15, 20, 25, 30]:
        key = f'nav_year_{year}'
        if key in stats:
            print(f"  Year {year}: GBP {stats[key]['median']:,.0f}")
    print()
    
    print("Annual Dividends (Median, Years 20-25, all reinvested):")
    for year in range(20, 26):
        key = f'year_{year}'
        if key in stats.get('annual_dividends', {}):
            print(f"  Year {year}: GBP {stats['annual_dividends'][key]['median']:,.0f}")
    print()
    
    print("Annual Income Withdrawn (Median, Years 26-30, 60% of dividends):")
    for year in range(26, 31):
        key = f'year_{year}'
        if key in stats.get('annual_income', {}):
            print(f"  Year {year}: GBP {stats['annual_income'][key]['median']:,.0f}")


if __name__ == "__main__":
    main()
