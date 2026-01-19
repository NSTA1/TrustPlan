"""
Data models for the portfolio simulation.

Contains the Asset and SimulationConfig dataclasses that define
the structure of portfolio assets and simulation parameters.
"""

import numpy as np
from dataclasses import dataclass
from typing import List
from datetime import date


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
    dividend_resilience: float = 0.7  # 0-1 scale, higher = more resistant to cuts
    
    @property
    def effective_yield(self) -> float:
        """Calculate yield after withholding tax."""
        return self.forward_yield * (1 - self.withholding_tax)
    
    @property
    def payments_per_year(self) -> int:
        """Number of dividend payments per year."""
        return len(self.payment_months)
    
    @property
    def cut_probability_modifier(self) -> float:
        """
        Modifier for dividend cut probability based on resilience.
        
        High resilience (0.9) -> 0.1x base probability (very unlikely to cut)
        Low resilience (0.3) -> 1.7x base probability (more likely to cut)
        """
        return 2.0 - (2.0 * self.dividend_resilience)


@dataclass
class SimulationConfig:
    """Configuration parameters for the simulation."""
    start_date: date = date(2026, 1, 1)
    accumulation_years: int = 25
    post_accumulation_years: int = 5
    
    # NAV assumptions (conservative)
    nav_mean_annual: float = 0.05  # 5% real
    nav_volatility_annual: float = 0.18  # 18%
    nav_correlation: float = 0.60
    
    # Dividend modelling
    dividend_growth_volatility: float = 0.05
    excess_growth_decay: float = 0.95  # High-growth assets decay toward mean
    
    # Dividend cut parameters (stress realism)
    dividend_cut_drawdown_threshold: float = 0.20  # 20% drawdown triggers cut risk
    dividend_cut_base_probability: float = 0.15  # Base probability of cut per asset per stress period
    dividend_cut_severity_min: float = 0.10  # Minimum cut: 10% reduction
    dividend_cut_severity_max: float = 0.50  # Maximum cut: 50% reduction
    dividend_recovery_rate: float = 0.25  # 25% recovery per year after stress ends
    
    num_simulations: int = 10000
    random_seed: int = 42
    
    # Contribution schedule (January 2026)
    lump_sum: float = 86000.0
    monthly_contribution: float = 2500.0
    monthly_contribution_months: int = 300  # 25 years from May 2026
    
    dividend_reinvestment_rate_post: float = 0.40
    dividend_withdrawal_rate_post: float = 0.60
    
    adr_fee_rate: float = 0.005
    
    # Downturn fund parameters
    downturn_fund_initial: float = 15000.0
    downturn_rebuild_rate: float = 0.035  # 3.5% of target per month (~£525)
    downturn_tranche_a_threshold: float = 0.10  # 10% drawdown
    downturn_tranche_b_threshold: float = 0.20  # 20% drawdown
    downturn_tranche_c_threshold: float = 0.30  # 30% drawdown
    downturn_tranche_a_pct: float = 0.20  # 20% of fund
    downturn_tranche_b_pct: float = 0.40  # 40% of fund
    downturn_tranche_c_pct: float = 0.40  # 40% of fund
    
    @property
    def nav_mean_monthly(self) -> float:
        """Monthly NAV return mean."""
        return self.nav_mean_annual / 12
    
    @property
    def nav_volatility_monthly(self) -> float:
        """Monthly NAV return volatility."""
        return self.nav_volatility_annual / np.sqrt(12)
    
    @property
    def total_months(self) -> int:
        """Total simulation months."""
        return (self.accumulation_years + self.post_accumulation_years + 1) * 12
