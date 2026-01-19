"""
Downturn Strategy Implementation.

Implements the mechanical downturn deployment protocol from Downturn.md.
Tracks a benchmark index and deploys capital from a downturn fund
when drawdowns reach 10%, 20%, or 30%.
"""

from .models import SimulationConfig


class DownturnStrategy:
    """
    Implements the mechanical downturn deployment strategy.
    
    Tracks a benchmark index (simulated FTSE All-World proxy) and deploys
    capital from a downturn fund when drawdowns reach 10%, 20%, or 30%.
    
    Key features:
    - Tranche A: 20% of fund at 10% drawdown
    - Tranche B: 40% of fund at 20% drawdown  
    - Tranche C: 40% of fund at 30% drawdown
    - Rebuild at 3.5% of target per month after deployment
    - No new deployments during rebuild phase
    - Tranche flags only reset when a new peak is reached (new drawdown cycle)
    """
    
    def __init__(self, config: SimulationConfig):
        self.config = config
        self.reset()
    
    def reset(self):
        """Reset state for a new simulation run."""
        self.fund_balance = self.config.downturn_fund_initial
        self.target_fund_size = self.config.downturn_fund_initial
        self.peak_benchmark = 100.0  # Starting benchmark value
        self.current_benchmark = 100.0
        
        # Track which tranches have been deployed in current drawdown event
        self.tranche_a_deployed = False
        self.tranche_b_deployed = False
        self.tranche_c_deployed = False
        
        # Rebuilding state
        self.is_rebuilding = False
        self.rebuild_monthly_amount = self.target_fund_size * self.config.downturn_rebuild_rate
        
        # Track total deployed for statistics
        self.total_deployed = 0.0
        self.deployment_events = []
    
    def update_benchmark(self, monthly_return: float) -> None:
        """
        Update benchmark value with monthly return.
        
        Args:
            monthly_return: The monthly return for the benchmark
        """
        self.current_benchmark *= (1 + monthly_return)
        if self.current_benchmark > self.peak_benchmark:
            self.peak_benchmark = self.current_benchmark
            # Reset tranche flags when new peak is reached (new drawdown cycle)
            # This happens regardless of rebuild status - a new peak means a new cycle
            self.tranche_a_deployed = False
            self.tranche_b_deployed = False
            self.tranche_c_deployed = False
    
    def get_drawdown(self) -> float:
        """
        Calculate current drawdown from peak.
        
        Returns:
            The drawdown as a decimal (e.g., 0.15 for 15% drawdown)
        """
        if self.peak_benchmark <= 0:
            return 0.0
        return (self.peak_benchmark - self.current_benchmark) / self.peak_benchmark
    
    def check_and_deploy(self, month_idx: int) -> float:
        """
        Check if a deployment should occur and return the amount to deploy.
        
        Args:
            month_idx: The current month index in the simulation
            
        Returns:
            The amount to invest in the portfolio (0 if no deployment)
        """
        if self.is_rebuilding:
            # No deployments during rebuild phase
            return 0.0
        
        if self.fund_balance <= 0:
            return 0.0
        
        drawdown = self.get_drawdown()
        deployment = 0.0
        
        # Check tranches in order (C first if multiple thresholds crossed)
        if drawdown >= self.config.downturn_tranche_c_threshold and not self.tranche_c_deployed:
            # Deploy Tranche C (40% of initial fund)
            amount = self.target_fund_size * self.config.downturn_tranche_c_pct
            deployment += min(amount, self.fund_balance)
            self.fund_balance -= deployment
            self.tranche_c_deployed = True
            self.deployment_events.append(('C', month_idx, deployment, drawdown))
            
            # Also deploy B and A if not yet deployed
            if not self.tranche_b_deployed:
                amount_b = self.target_fund_size * self.config.downturn_tranche_b_pct
                deploy_b = min(amount_b, self.fund_balance)
                deployment += deploy_b
                self.fund_balance -= deploy_b
                self.tranche_b_deployed = True
                self.deployment_events.append(('B', month_idx, deploy_b, drawdown))
            
            if not self.tranche_a_deployed:
                amount_a = self.target_fund_size * self.config.downturn_tranche_a_pct
                deploy_a = min(amount_a, self.fund_balance)
                deployment += deploy_a
                self.fund_balance -= deploy_a
                self.tranche_a_deployed = True
                self.deployment_events.append(('A', month_idx, deploy_a, drawdown))
        
        elif drawdown >= self.config.downturn_tranche_b_threshold and not self.tranche_b_deployed:
            # Deploy Tranche B (40% of initial fund)
            amount = self.target_fund_size * self.config.downturn_tranche_b_pct
            deployment += min(amount, self.fund_balance)
            self.fund_balance -= deployment
            self.tranche_b_deployed = True
            self.deployment_events.append(('B', month_idx, deployment, drawdown))
            
            # Also deploy A if not yet deployed
            if not self.tranche_a_deployed:
                amount_a = self.target_fund_size * self.config.downturn_tranche_a_pct
                deploy_a = min(amount_a, self.fund_balance)
                deployment += deploy_a
                self.fund_balance -= deploy_a
                self.tranche_a_deployed = True
                self.deployment_events.append(('A', month_idx, deploy_a, drawdown))
        
        elif drawdown >= self.config.downturn_tranche_a_threshold and not self.tranche_a_deployed:
            # Deploy Tranche A (20% of initial fund)
            amount = self.target_fund_size * self.config.downturn_tranche_a_pct
            deployment = min(amount, self.fund_balance)
            self.fund_balance -= deployment
            self.tranche_a_deployed = True
            self.deployment_events.append(('A', month_idx, deployment, drawdown))
        
        if deployment > 0:
            self.total_deployed += deployment
            # Start rebuilding after any deployment
            self.is_rebuilding = True
        
        return deployment
    
    def process_monthly_rebuild(self) -> None:
        """Process monthly rebuilding of the downturn fund."""
        if not self.is_rebuilding:
            return
        
        # Add rebuild amount to fund
        self.fund_balance += self.rebuild_monthly_amount
        
        # Check if fully rebuilt
        if self.fund_balance >= self.target_fund_size:
            self.fund_balance = self.target_fund_size
            self.is_rebuilding = False
            # Note: Tranche flags are NOT reset here. They are only reset when
            # a new peak is reached in update_benchmark(), which indicates
            # the start of a new drawdown cycle. This ensures:
            # "One downturn → one sequence of tranches → full rebuild → next downturn"
