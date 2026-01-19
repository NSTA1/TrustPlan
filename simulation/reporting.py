"""
Simulation Results Analysis and Reporting.

Contains functions to analyze simulation results and generate
markdown reports with statistics and projections.
"""

import numpy as np
from typing import Dict

from .models import SimulationConfig


def analyze_results(results: Dict) -> Dict:
    """
    Analyze simulation results and compute statistics.
    
    Args:
        results: Dictionary from PortfolioSimulator.run_simulation()
        
    Returns:
        Dictionary of statistics including percentiles for NAV,
        dividends, income, scenario analysis, and dividend stress metrics.
    """
    config = results['config']
    all_nav = results['all_nav']
    all_annual_income = results['all_annual_income']
    all_annual_dividends = results['all_annual_dividends']
    all_dividend_cuts = results.get('all_dividend_cuts', np.zeros(all_nav.shape[0]))
    all_downturn_events = results.get('all_downturn_events', np.zeros(all_nav.shape[0]))
    all_downturn_deployed = results.get('all_downturn_deployed', np.zeros(all_nav.shape[0]))
    
    total_years = config.accumulation_years + config.post_accumulation_years + 1
    
    stats = {}
    
    # NAV statistics at key years
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
    
    # Annual dividend statistics
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
    
    # Annual income statistics (post-accumulation)
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
    
    # Income CAGR (years 26-30)
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
    
    # Dividend stress statistics
    stats['dividend_stress'] = {
        'simulations_with_cuts': np.sum(all_dividend_cuts > 0),
        'simulations_with_cuts_pct': np.mean(all_dividend_cuts > 0) * 100,
        'total_cuts_mean': np.mean(all_dividend_cuts),
        'total_cuts_median': np.median(all_dividend_cuts),
        'total_cuts_max': np.max(all_dividend_cuts),
        'total_cuts_p5': np.percentile(all_dividend_cuts, 5),
        'total_cuts_p95': np.percentile(all_dividend_cuts, 95),
        'cuts_per_sim_nonzero_mean': np.mean(all_dividend_cuts[all_dividend_cuts > 0]) if np.sum(all_dividend_cuts > 0) > 0 else 0,
    }
    
    # Downturn strategy statistics
    stats['downturn_strategy'] = {
        'simulations_with_deployments': np.sum(all_downturn_events > 0),
        'simulations_with_deployments_pct': np.mean(all_downturn_events > 0) * 100,
        'events_mean': np.mean(all_downturn_events),
        'events_median': np.median(all_downturn_events),
        'events_max': np.max(all_downturn_events),
        'total_deployed_mean': np.mean(all_downturn_deployed),
        'total_deployed_median': np.median(all_downturn_deployed),
        'total_deployed_p95': np.percentile(all_downturn_deployed, 95),
    }
    
    # Scenario analysis (best, worst, median paths)
    final_nav = all_nav[:, -1]
    best_idx = np.argmax(final_nav)
    worst_idx = np.argmin(final_nav)
    median_idx = np.argsort(final_nav)[len(final_nav)//2]
    
    year_30_idx = min(30, all_annual_income.shape[1] - 1)
    
    stats['best_case'] = {
        'final_nav': final_nav[best_idx],
        'year_30_income': all_annual_income[best_idx, year_30_idx],
        'year_30_dividends': all_annual_dividends[best_idx, year_30_idx],
        'dividend_cuts': all_dividend_cuts[best_idx],
    }
    stats['worst_case'] = {
        'final_nav': final_nav[worst_idx],
        'year_30_income': all_annual_income[worst_idx, year_30_idx],
        'year_30_dividends': all_annual_dividends[worst_idx, year_30_idx],
        'dividend_cuts': all_dividend_cuts[worst_idx],
    }
    stats['median_case'] = {
        'final_nav': final_nav[median_idx],
        'year_30_income': all_annual_income[median_idx, year_30_idx],
        'year_30_dividends': all_annual_dividends[median_idx, year_30_idx],
        'dividend_cuts': all_dividend_cuts[median_idx],
    }
    
    return stats


def generate_report(stats: Dict, config: SimulationConfig) -> str:
    """
    Generate a markdown report of the simulation results.
    
    Args:
        stats: Dictionary from analyze_results()
        config: SimulationConfig used for the simulation
        
    Returns:
        Markdown-formatted report string
    """
    report = []
    report.append("# Portfolio NAV and Income Projection Report")
    report.append("")
    report.append("## Simulation Parameters")
    report.append("")
    report.append(f"- **Number of simulations**: {config.num_simulations:,}")
    report.append("- **Simulation period**: 30 years (January 2026 - December 2055)")
    report.append("- **Accumulation phase**: Years 0-25 (100% dividend reinvestment)")
    report.append("- **Post-accumulation phase**: Years 26-30 (60% dividend withdrawal)")
    report.append(f"- **NAV expected return**: {config.nav_mean_annual:.1%} real annual")
    report.append(f"- **NAV volatility**: {config.nav_volatility_annual:.1%} annual")
    report.append(f"- **Dividend growth volatility**: {config.dividend_growth_volatility:.1%}")
    report.append(f"- **Excess growth decay factor**: {config.excess_growth_decay}")
    report.append(f"- **Downturn fund**: GBP {config.downturn_fund_initial:,.0f}")
    report.append("")
    
    # Dividend stress parameters
    report.append("### Dividend Stress Modelling")
    report.append("")
    report.append(f"- **Cut trigger threshold**: {config.dividend_cut_drawdown_threshold:.0%} market drawdown")
    report.append(f"- **Base cut probability**: {config.dividend_cut_base_probability:.0%} per asset per stress event")
    report.append(f"- **Cut severity range**: {config.dividend_cut_severity_min:.0%} - {config.dividend_cut_severity_max:.0%}")
    report.append(f"- **Recovery rate**: {config.dividend_recovery_rate:.0%} per year after stress ends")
    report.append("")
    
    # Contributions summary
    total_monthly = config.monthly_contribution * config.monthly_contribution_months
    total_contributions = config.lump_sum + total_monthly
    report.append("## Total Contributions")
    report.append("")
    report.append(f"- **Lump sum**: GBP {config.lump_sum:,.0f}")
    report.append(f"- **Monthly contributions**: GBP {total_monthly:,.0f} (25 years)")
    report.append(f"- **Total contributions**: GBP {total_contributions:,.0f}")
    report.append("")
    
    # NAV projections
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
    
    # Annual dividends (accumulation phase)
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
    
    # Annual income (post-accumulation)
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
    
    # Total dividends (post-accumulation)
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
    
    # Income growth
    if 'income_cagr_26_30' in stats:
        cagr = stats['income_cagr_26_30']
        report.append("## Income Growth (Years 26-30)")
        report.append("")
        report.append(f"- **Median CAGR**: {cagr['median']:.1%}")
        report.append(f"- **5th percentile CAGR**: {cagr['p5']:.1%}")
        report.append(f"- **95th percentile CAGR**: {cagr['p95']:.1%}")
        report.append("")
    
    # Dividend Stress Analysis (NEW SECTION)
    if 'dividend_stress' in stats:
        ds = stats['dividend_stress']
        report.append("## Dividend Stress Analysis")
        report.append("")
        report.append("*Analysis of dividend cuts during market stress periods across all simulations*")
        report.append("")
        report.append("### Frequency of Dividend Cuts")
        report.append("")
        report.append(f"- **Simulations experiencing cuts**: {ds['simulations_with_cuts']:,.0f} ({ds['simulations_with_cuts_pct']:.1f}%)")
        report.append(f"- **Simulations with no cuts**: {config.num_simulations - ds['simulations_with_cuts']:,.0f} ({100 - ds['simulations_with_cuts_pct']:.1f}%)")
        report.append("")
        report.append("### Dividend Cut Statistics")
        report.append("")
        report.append("| Metric | Value |")
        report.append("|--------|-------|")
        report.append(f"| Mean cuts per simulation | {ds['total_cuts_mean']:.2f} |")
        report.append(f"| Median cuts per simulation | {ds['total_cuts_median']:.0f} |")
        report.append(f"| 5th percentile | {ds['total_cuts_p5']:.0f} |")
        report.append(f"| 95th percentile | {ds['total_cuts_p95']:.0f} |")
        report.append(f"| Maximum cuts (worst path) | {ds['total_cuts_max']:.0f} |")
        if ds['cuts_per_sim_nonzero_mean'] > 0:
            report.append(f"| Mean cuts (paths with cuts) | {ds['cuts_per_sim_nonzero_mean']:.1f} |")
        report.append("")
        report.append("*Note: Cuts are applied probabilistically when market drawdowns exceed the threshold.*")
        report.append("*High-resilience dividend aristocrats have significantly lower cut probability.*")
        report.append("")
    
    # Downturn Strategy Analysis (NEW SECTION)
    if 'downturn_strategy' in stats:
        dt = stats['downturn_strategy']
        report.append("## Downturn Strategy Analysis")
        report.append("")
        report.append("*Analysis of the mechanical downturn fund deployment strategy*")
        report.append("")
        report.append("### Deployment Frequency")
        report.append("")
        report.append(f"- **Simulations with deployments**: {dt['simulations_with_deployments']:,.0f} ({dt['simulations_with_deployments_pct']:.1f}%)")
        report.append(f"- **Mean deployment events**: {dt['events_mean']:.1f}")
        report.append(f"- **Median deployment events**: {dt['events_median']:.0f}")
        report.append(f"- **Maximum deployment events**: {dt['events_max']:.0f}")
        report.append("")
        report.append("### Capital Deployed")
        report.append("")
        report.append(f"- **Mean total deployed**: GBP {dt['total_deployed_mean']:,.0f}")
        report.append(f"- **Median total deployed**: GBP {dt['total_deployed_median']:,.0f}")
        report.append(f"- **95th percentile deployed**: GBP {dt['total_deployed_p95']:,.0f}")
        report.append("")
    
    # Scenario analysis
    report.append("## Scenario Analysis")
    report.append("")
    report.append("### Best Case Path (95th percentile NAV)")
    report.append(f"- **Final NAV (Year 30)**: GBP {stats['best_case']['final_nav']:,.0f}")
    report.append(f"- **Year 30 Total Dividends**: GBP {stats['best_case']['year_30_dividends']:,.0f}")
    report.append(f"- **Year 30 Income Withdrawn**: GBP {stats['best_case']['year_30_income']:,.0f}")
    report.append(f"- **Dividend cuts experienced**: {stats['best_case']['dividend_cuts']:.0f}")
    report.append("")
    report.append("### Median Case Path")
    report.append(f"- **Final NAV (Year 30)**: GBP {stats['median_case']['final_nav']:,.0f}")
    report.append(f"- **Year 30 Total Dividends**: GBP {stats['median_case']['year_30_dividends']:,.0f}")
    report.append(f"- **Year 30 Income Withdrawn**: GBP {stats['median_case']['year_30_income']:,.0f}")
    report.append(f"- **Dividend cuts experienced**: {stats['median_case']['dividend_cuts']:.0f}")
    report.append("")
    report.append("### Worst Case Path (5th percentile NAV)")
    report.append(f"- **Final NAV (Year 30)**: GBP {stats['worst_case']['final_nav']:,.0f}")
    report.append(f"- **Year 30 Total Dividends**: GBP {stats['worst_case']['year_30_dividends']:,.0f}")
    report.append(f"- **Year 30 Income Withdrawn**: GBP {stats['worst_case']['year_30_income']:,.0f}")
    report.append(f"- **Dividend cuts experienced**: {stats['worst_case']['dividend_cuts']:.0f}")
    report.append("")
    
    # Model notes
    report.append("## Model Notes")
    report.append("")
    report.append("This simulation uses a **realistic dividend growth model**:")
    report.append("")
    report.append("1. **NAV Growth**: 5% real annual return (conservative)")
    report.append("2. **Dividend Growth**: Modelled as excess growth above NAV growth")
    report.append("   - Historical 5-year dividend growth includes underlying earnings growth")
    report.append("   - Only 'excess' portion (dividend growth minus NAV growth) applied additionally")
    report.append("   - Prevents double-counting of growth")
    report.append("3. **Growth Decay**: High excess growth rates decay toward sustainable levels")
    report.append("4. **Downturn Strategy**: Mechanical deployment at 10%/20%/30% drawdowns")
    report.append("5. **Dividend Cuts**: Probabilistic cuts during market stress (>20% drawdown)")
    report.append("   - Cut probability scaled by asset resilience score (0-1)")
    report.append("   - Higher resilience = lower cut probability")
    report.append("   - Cuts recover gradually after market stabilization")
    report.append("6. **Dividend Calculation**: `dividend = units × base_dividend × excess_growth_factor × cut_factor`")
    report.append("")
    
    report.append("---")
    report.append("")
    report.append("*Report generated using Monte Carlo simulation based on SDG portfolio specifications.*")
    report.append("*All values in GBP real terms (inflation-adjusted).*")
    
    return "\n".join(report)


def print_summary(stats: Dict, config: SimulationConfig) -> None:
    """Print a summary of simulation results to console."""
    print("=" * 60)
    print("SUMMARY (Realistic Model with Dividend Stress)")
    print("=" * 60)
    print()
    
    total_contributions = config.lump_sum + config.monthly_contribution * config.monthly_contribution_months
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
    print()
    
    # Dividend stress summary
    if 'dividend_stress' in stats:
        ds = stats['dividend_stress']
        print("Dividend Stress Analysis:")
        print(f"  Simulations with cuts: {ds['simulations_with_cuts_pct']:.1f}%")
        print(f"  Mean cuts per simulation: {ds['total_cuts_mean']:.2f}")
        print(f"  Median cuts per simulation: {ds['total_cuts_median']:.0f}")
        print(f"  95th percentile cuts: {ds['total_cuts_p95']:.0f}")
        print()
    
    # Downturn strategy summary
    if 'downturn_strategy' in stats:
        dt = stats['downturn_strategy']
        print("Downturn Strategy Analysis:")
        print(f"  Simulations with deployments: {dt['simulations_with_deployments_pct']:.1f}%")
        print(f"  Mean deployment events: {dt['events_mean']:.1f}")
        print(f"  Mean capital deployed: GBP {dt['total_deployed_mean']:,.0f}")
        print()
