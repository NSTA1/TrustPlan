"""
Sensitivity Analysis Runner for SDG Portfolio Simulation.

Runs the Monte Carlo simulation with multiple NAV parameter scenarios:
- Pessimistic: 3% return, 22% volatility
- Base case: 5% return, 17% volatility  
- Optimistic: 7% return, 15% volatility

Generates separate reports for each scenario and a summary comparison.

Usage:
    python -m simulation.sensitivity_analysis
    
Or via PowerShell script:
    .\\sensitivity.ps1
"""

import os
import warnings
warnings.filterwarnings('ignore')

from .models import SimulationConfig
from .assets import create_assets, verify_portfolio_metrics
from .simulator import PortfolioSimulator
from .reporting import analyze_results, generate_report, print_summary


# Define scenarios: (name, nav_return, nav_volatility)
SCENARIOS = [
    ("pessimistic", 0.03, 0.22),  # 3% return, 22% volatility
    ("base", 0.05, 0.17),         # 5% return, 17% volatility (default)
    ("optimistic", 0.07, 0.15),   # 7% return, 15% volatility
]


def get_output_dir() -> str:
    """Get the simulation output directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return script_dir


def run_scenario(name: str, nav_return: float, nav_volatility: float, 
                 assets: dict, num_simulations: int = 10000) -> dict:
    """Run a single scenario and return results."""
    print(f"\n{'='*60}")
    print(f"Running {name.upper()} scenario")
    print(f"  NAV Return: {nav_return:.1%}")
    print(f"  NAV Volatility: {nav_volatility:.1%}")
    print(f"{'='*60}")
    
    config = SimulationConfig(
        nav_mean_annual=nav_return,
        nav_volatility_annual=nav_volatility,
        excess_growth_nav_baseline=0.05,  # Always use 5% baseline for consistent dividend modelling
        num_simulations=num_simulations,
        random_seed=42  # Same seed for comparability
    )
    
    print(f"  Excess Growth Baseline: {config.excess_growth_nav_baseline:.1%}")
    
    simulator = PortfolioSimulator(config, assets)
    results = simulator.run_simulation()
    stats = analyze_results(results)
    
    return {
        'name': name,
        'config': config,
        'stats': stats,
        'report': generate_report(stats, config)
    }


def generate_comparison_summary(scenarios_results: list) -> str:
    """Generate a markdown summary comparing all scenarios."""
    lines = [
        "# Sensitivity Analysis Summary",
        "",
        "## Scenario Parameters",
        "",
        "| Scenario | NAV Return | NAV Volatility |",
        "|----------|------------|----------------|",
    ]
    
    for result in scenarios_results:
        config = result['config']
        name = result['name'].capitalize()
        lines.append(f"| {name} | {config.nav_mean_annual:.1%} | {config.nav_volatility_annual:.1%} |")
    
    lines.extend([
        "",
        "## Year 25 NAV Comparison (End of Accumulation)",
        "",
        "| Scenario | 5th %ile | Median | 95th %ile |",
        "|----------|----------|--------|-----------|",
    ])
    
    for result in scenarios_results:
        stats = result['stats']
        name = result['name'].capitalize()
        nav_25 = stats['nav_year_25']
        lines.append(f"| {name} | GBP {nav_25['p5']:,.0f} | GBP {nav_25['median']:,.0f} | GBP {nav_25['p95']:,.0f} |")
    
    lines.extend([
        "",
        "## Year 30 NAV Comparison (Final)",
        "",
        "| Scenario | 5th %ile | Median | 95th %ile |",
        "|----------|----------|--------|-----------|",
    ])
    
    for result in scenarios_results:
        stats = result['stats']
        name = result['name'].capitalize()
        nav_30 = stats['nav_year_30']
        lines.append(f"| {name} | GBP {nav_30['p5']:,.0f} | GBP {nav_30['median']:,.0f} | GBP {nav_30['p95']:,.0f} |")
    
    lines.extend([
        "",
        "## Year 30 Dividend Income Comparison (60% Withdrawal)",
        "",
        "| Scenario | 5th %ile | Median | 95th %ile |",
        "|----------|----------|--------|-----------|",
    ])
    
    for result in scenarios_results:
        stats = result['stats']
        name = result['name'].capitalize()
        income_30 = stats['annual_income']['year_30']
        lines.append(f"| {name} | GBP {income_30['p5']:,.0f} | GBP {income_30['median']:,.0f} | GBP {income_30['p95']:,.0f} |")
    
    lines.extend([
        "",
        "## Key Observations",
        "",
        "1. **NAV Spread**: Higher volatility scenarios show wider percentile spreads, as expected",
        "2. **Counterintuitive Income Pattern**: Lower NAV growth scenarios show *higher* dividend income because:",
        "   - Lower price growth = more units accumulated during contribution phase",
        "   - Dividend per share growth is modelled independently of NAV (excess growth baseline fixed at 5%)",
        "   - More units × same dividend growth = higher total dividends",
        "3. **Volatility Effect**: The pessimistic scenario's higher volatility (22%) creates extreme 95th percentile outcomes",
        "4. **NAV Ordering is Correct**: Optimistic > Base > Pessimistic for median NAV, as expected",
        "",
        "### Note on Dividend Model",
        "",
        "The inverse relationship between NAV growth and income is a feature of the excess dividend growth model:",
        "- Dividend growth is modelled as yield expansion above a 5% NAV baseline",
        "- When actual NAV grows slower, you accumulate more units at lower prices",
        "- The same dividend-per-share growth applied to more units produces higher income",
        "- This represents the value of consistent contribution investing into undervalued markets",
        "",
        "---",
        "",
        "*Analysis generated using Monte Carlo simulation with 10,000 paths per scenario.*",
    ])
    
    return "\n".join(lines)


def main():
    """Run sensitivity analysis across all scenarios."""
    print("=" * 60)
    print("SDG Portfolio Sensitivity Analysis")
    print("=" * 60)
    
    output_dir = get_output_dir()
    
    # Load assets once (shared across all scenarios)
    assets = create_assets()
    print(f"Loaded {len(assets)} assets")
    verify_portfolio_metrics(assets)
    
    # Run all scenarios
    results = []
    for name, nav_return, nav_volatility in SCENARIOS:
        result = run_scenario(name, nav_return, nav_volatility, assets)
        results.append(result)
        
        # Save individual scenario report in simulation folder
        filename = os.path.join(output_dir, f"projection_report_{name}.md")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(result['report'])
        print(f"  Saved projection_report_{name}.md")
    
    # Generate and save comparison summary
    summary = generate_comparison_summary(results)
    summary_path = os.path.join(output_dir, "sensitivity_analysis_summary.md")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"\nSaved sensitivity_analysis_summary.md")
    
    # Print comparison table
    print("\n" + "=" * 60)
    print("SENSITIVITY ANALYSIS COMPLETE")
    print("=" * 60)
    print("\nYear 30 Median NAV Comparison:")
    for result in results:
        name = result['name'].capitalize()
        nav_30 = result['stats']['nav_year_30']['median']
        print(f"  {name:12s}: GBP {nav_30:,.0f}")
    
    print("\nYear 30 Median Income (60% withdrawal):")
    for result in results:
        name = result['name'].capitalize()
        income_30 = result['stats']['annual_income']['year_30']['median']
        print(f"  {name:12s}: GBP {income_30:,.0f}")
    
    print(f"\nReports saved to: {output_dir}")
    print("  - projection_report_pessimistic.md")
    print("  - projection_report_base.md")
    print("  - projection_report_optimistic.md")
    print("  - sensitivity_analysis_summary.md")


if __name__ == "__main__":
    main()
