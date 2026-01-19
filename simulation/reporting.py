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
        dividends, income, and scenario analysis.
    """
    config = results['config']
    all_nav = results['all_nav']
    all_annual_income = results['all_annual_income']
    all_annual_dividends = results['all_annual_dividends']
    
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
    
    # Scenario analysis
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
    report.append("5. **Dividend Calculation**: `dividend = units × base_dividend × excess_growth_factor`")
    report.append("")
    
    report.append("---")
    report.append("")
    report.append("*Report generated using Monte Carlo simulation based on SDG portfolio specifications.*")
    report.append("*All values in GBP real terms (inflation-adjusted).*")
    
    return "\n".join(report)


def print_summary(stats: Dict, config: SimulationConfig) -> None:
    """Print a summary of simulation results to console."""
    print("=" * 60)
    print("SUMMARY (Realistic Model)")
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
