"""
SDG Portfolio Simulation Package.

A Monte Carlo simulation engine for projecting portfolio NAV
and dividend income based on the SDG portfolio specifications.
"""

from simulation.models import Asset, SimulationConfig
from simulation.assets import create_assets
from simulation.correlation import create_dividend_correlation_matrix
from simulation.downturn_strategy import DownturnStrategy
from simulation.simulator import PortfolioSimulator
from simulation.reporting import analyze_results, generate_report, print_summary

__all__ = [
    'Asset',
    'SimulationConfig', 
    'create_assets',
    'create_dividend_correlation_matrix',
    'DownturnStrategy',
    'PortfolioSimulator',
    'analyze_results',
    'generate_report',
    'print_summary',
]
