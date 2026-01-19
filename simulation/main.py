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

Usage:
    python -m simulation                     # Default: 5% return, 17% volatility
    python -m simulation --nav-return 0.06   # 6% return
    python -m simulation --nav-volatility 0.15  # 15% volatility
    python -m simulation --nav-return 0.07 --nav-volatility 0.15  # Both
"""

import argparse
import os
import warnings
warnings.filterwarnings('ignore')

from .models import SimulationConfig
from .assets import create_assets, verify_portfolio_metrics
from .simulator import PortfolioSimulator
from .reporting import analyze_results, generate_report, print_summary


def parse_args():
    """Parse command line arguments for NAV parameters."""
    parser = argparse.ArgumentParser(
        description='Run SDG Portfolio Monte Carlo Simulation',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--nav-return', 
        type=float, 
        default=0.05,
        help='Expected annual real NAV return (e.g., 0.05 for 5%%)'
    )
    parser.add_argument(
        '--nav-volatility', 
        type=float, 
        default=0.17,
        help='Annual NAV volatility (e.g., 0.17 for 17%%)'
    )
    parser.add_argument(
        '--num-simulations',
        type=int,
        default=10000,
        help='Number of Monte Carlo simulations to run'
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=42,
        help='Random seed for reproducibility'
    )
    parser.add_argument(
        '--output',
        type=str,
        default=None,
        help='Output report filename (default: projection_report.md)'
    )
    return parser.parse_args()


def main():
    """Main entry point for the simulation."""
    args = parse_args()
    
    print("=" * 60)
    print("Portfolio NAV and Income Projection Simulation")
    print("(SDG Portfolio - Modular Architecture)")
    print("=" * 60)
    print()
    
    # Create configuration with CLI parameters
    config = SimulationConfig(
        nav_mean_annual=args.nav_return,
        nav_volatility_annual=args.nav_volatility,
        num_simulations=args.num_simulations,
        random_seed=args.seed
    )
    
    print(f"NAV Parameters:")
    print(f"  Expected Return: {config.nav_mean_annual:.1%}")
    print(f"  Volatility: {config.nav_volatility_annual:.1%}")
    print(f"  Excess Growth Baseline: {config.excess_growth_nav_baseline:.1%}")
    print()
    
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
    
    # Determine output filename
    if args.output:
        report_path = os.path.join(project_root, args.output)
    else:
        report_path = os.path.join(project_root, "projection_report.md")
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"\nReport saved to {os.path.basename(report_path)}")
    print()
    
    # Print summary
    print_summary(stats, config)


if __name__ == "__main__":
    main()
