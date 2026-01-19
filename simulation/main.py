"""
Portfolio NAV and Income Projection Monte Carlo Simulation

Main entry point for running the SDG portfolio simulation.
Uses a realistic dividend growth model that avoids double-counting
NAV appreciation and dividend growth.

Modules:
- models.py: Asset and SimulationConfig dataclasses
- assets.py: Portfolio asset definitions
- correlation.py: Dividend growth correlation matrix
- downturn_strategy.py: Downturn fund deployment strategy
- simulator.py: Monte Carlo simulation engine
- reporting.py: Results analysis and report generation
"""

import os
import warnings
warnings.filterwarnings('ignore')

from .models import SimulationConfig
from .assets import create_assets, verify_portfolio_metrics
from .simulator import PortfolioSimulator
from .reporting import analyze_results, generate_report, print_summary


def main():
    """Main entry point for the simulation."""
    print("=" * 60)
    print("Portfolio NAV and Income Projection Simulation")
    print("(SDG Portfolio - Modular Architecture)")
    print("=" * 60)
    print()
    
    # Create configuration
    config = SimulationConfig(
        num_simulations=10000,
        random_seed=42
    )
    
    # Load assets
    assets = create_assets()
    print(f"Loaded {len(assets)} assets")
    
    # Verify portfolio metrics
    verify_portfolio_metrics(assets)
    
    # Calculate excess growth
    weighted_excess = sum(
        a.allocation * max(0, a.dividend_growth_5yr - config.nav_mean_annual) 
        for a in assets.values()
    )
    print(f"Portfolio weighted excess dividend growth: {weighted_excess:.2%}")
    print(f"NAV growth assumption: {config.nav_mean_annual:.1%}")
    print()
    
    # Run simulation
    simulator = PortfolioSimulator(config, assets)
    results = simulator.run_simulation()
    
    # Analyze results
    print("\nAnalyzing results...")
    stats = analyze_results(results)
    
    # Generate and save report (in parent directory)
    report = generate_report(stats, config)
    
    # Get the parent directory (project root)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    report_path = os.path.join(project_root, "projection_report.md")
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"\nReport saved to projection_report.md")
    print()
    
    # Print summary
    print_summary(stats, config)


if __name__ == "__main__":
    main()
