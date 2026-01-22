"""
Portfolio Asset Definitions.

Creates the portfolio assets with all required parameters including
yields, dividend growth rates, payment schedules, and tax treatment.

Asset data is based on the SDG portfolio specification with:
- 27 holdings across 8 asset sleeves
- Forward yields and withholding taxes from Forward Yield (2026) table
- 5-year dividend growth rates from Asset 5-Year Average Dividend Growth table
"""

from typing import Dict

from .models import Asset


def create_assets() -> Dict[str, Asset]:
    """
    Create the portfolio assets with all required parameters.
    
    Returns:
        Dictionary of Asset objects keyed by ticker symbol
        
    Note:
        Forward yields are from the SDG Forward Yield (2026) table.
        Portfolio-weighted yield after withholding should be ~1.40%.
        
        Dividend resilience scores (0-1):
        - 0.9+: Dividend aristocrats, 25+ years of increases
        - 0.8-0.9: Strong dividend growers, consistent history
        - 0.7-0.8: Good dividend history, some variability
        - 0.6-0.7: Moderate dividend stability
        - 0.5-0.6: Higher risk of cuts during stress
    """
    # Format: (name, ticker, allocation, forward_yield, withholding_tax, 
    #          dividend_growth_5yr, payment_frequency, payment_months, is_adr, resilience)
    assets_data = [
        # US Quality / Moat (24%)
        ("Microsoft", "MSFT", 0.07, 0.0075, 0.15, 0.102, "Quarterly", [3, 6, 9, 12], False, 0.95),  # 20+ years of increases
        ("S&P Global", "SPGI", 0.04, 0.0078, 0.15, 0.099, "Quarterly", [3, 6, 9, 12], False, 0.90),  # 50+ years
        ("Waste Management", "WM", 0.05, 0.0144, 0.15, 0.083, "Quarterly", [3, 6, 9, 12], False, 0.90),  # 20+ years
        ("ADP", "ADP", 0.03, 0.0201, 0.15, 0.128, "Quarterly", [1, 4, 7, 10], False, 0.95),  # 49+ years
        ("Accenture", "ACN", 0.02, 0.0216, 0.15, 0.12, "Quarterly", [2, 5, 8, 11], False, 0.85),  # Strong growth
        ("Stryker", "SYK", 0.03, 0.0092, 0.15, 0.088, "Quarterly", [1, 4, 7, 10], False, 0.85),  # 30+ years
        
        # US Payments & Platforms (12%)
        ("Mastercard", "MA", 0.07, 0.0052, 0.15, 0.142, "Quarterly", [2, 5, 8, 11], False, 0.85),  # Strong but newer
        ("JP Morgan", "JPM", 0.05, 0.019, 0.15, 0.1188, "Quarterly", [1, 4, 7, 10], False, 0.70),  # Banks cut in 2008-09
        
        # European Luxury & IP (27%)
        ("LVMH", "MC", 0.03, 0.02, 0.25, 0.23, "Semi-Annual", [4, 12], False, 0.75),  # Strong but cyclical
        ("EssilorLuxottica", "EL", 0.03, 0.0187, 0.25, 0.23, "Annual", [5], False, 0.80),
        ("RELX", "REL", 0.04, 0.0208, 0.0, 0.068, "Semi-Annual", [6, 9], False, 0.90),  # Very consistent
        ("London Stock Exchange Group", "LSEG", 0.02, 0.0153, 0.0, 0.145, "Semi-Annual", [5, 9], False, 0.85),
        ("L'Oreal", "OR", 0.03, 0.0189, 0.25, 0.128, "Annual", [5], False, 0.90),  # 40+ years
        ("Wolters Kluwer", "WKL", 0.05, 0.014, 0.15, 0.1096, "Semi-Annual", [5, 9], False, 0.90),  # Very consistent
        ("Hermes International", "RMS", 0.03, 0.008, 0.25, 0.16, "Annual", [5], False, 0.85),  # Luxury resilience
        ("Judges Scientific", "JDG", 0.04, 0.0215, 0.0, 0.1515, "Semi-Annual", [6, 10], False, 0.80),  # 20 years paying, scientific instruments
        
        # Global Semis & Healthcare (18%)
        ("ASML", "ASML", 0.04, 0.01, 0.15, 0.208, "Semi-Annual", [5, 11], False, 0.80),  # Cyclical but strong
        ("Novo Nordisk", "NVO", 0.04, 0.0164, 0.27, 0.191, "Annual", [3], False, 0.90),  # Healthcare stability
        ("Coloplast", "CLPBY", 0.05, 0.033, 0.27, 0.056, "Annual", [12], True, 0.85),  # Healthcare
        ("Hoya", "HOCPY", 0.05, 0.0043, 0.15, 0.053, "Semi-Annual", [6, 12], True, 0.80),
        
        # Global Financials (7%)
        ("Japan Exchange", "JPXGY", 0.05, 0.018, 0.15, 0.125, "Semi-Annual", [6, 12], True, 0.75),
        ("SMFG", "SMFG", 0.02, 0.0271, 0.15, 0.136, "Semi-Annual", [6, 12], True, 0.65),  # Banks more volatile
        
        # Defence & Strategic Platforms (6%)
        ("Lockheed Martin", "LMT", 0.03, 0.027, 0.15, 0.0722, "Quarterly", [3, 6, 9, 12], False, 0.90),  # 20+ years
        ("BAE Systems", "BA", 0.02, 0.029, 0.0, 0.065, "Semi-Annual", [6, 12], False, 0.85),  # Consistent
        ("General Dynamics", "GD", 0.01, 0.021, 0.15, 0.068, "Quarterly", [2, 5, 8, 11], False, 0.90),  # 30+ years
        
        # Transport & Infrastructure (3%)
        ("Canadian National Railway", "CNR", 0.03, 0.0261, 0.25, 0.102, "Quarterly", [3, 6, 9, 12], False, 0.85),  # 28+ years
        
        # US Real Estate (3%)
        ("Essex Property Trust", "ESS", 0.03, 0.035, 0.15, 0.055, "Quarterly", [1, 4, 7, 10], False, 0.75),  # REITs can cut
    ]
    
    assets = {}
    for data in assets_data:
        name, ticker, alloc, fwd_yield, wht, div_growth, freq, months, is_adr, resilience = data
        assets[ticker] = Asset(
            name=name, 
            ticker=ticker, 
            allocation=alloc,
            forward_yield=fwd_yield, 
            withholding_tax=wht,
            dividend_growth_5yr=div_growth, 
            payment_frequency=freq,
            payment_months=months, 
            is_adr=is_adr,
            dividend_resilience=resilience
        )
    
    return assets


def calculate_portfolio_metrics(assets: Dict[str, Asset]) -> Dict[str, float]:
    """
    Calculate portfolio-weighted metrics.
    
    Args:
        assets: Dictionary of Asset objects
        
    Returns:
        Dictionary containing:
        - total_allocation: Sum of allocations (should be 1.0)
        - weighted_yield_gross: Portfolio-weighted gross yield
        - weighted_yield_net: Portfolio-weighted yield after withholding
        - weighted_dividend_growth: Portfolio-weighted 5-year dividend growth
    """
    total_allocation = sum(a.allocation for a in assets.values())
    weighted_yield_gross = sum(a.allocation * a.forward_yield for a in assets.values())
    weighted_yield_net = sum(a.allocation * a.effective_yield for a in assets.values())
    weighted_dividend_growth = sum(a.allocation * a.dividend_growth_5yr for a in assets.values())
    
    return {
        'total_allocation': total_allocation,
        'weighted_yield_gross': weighted_yield_gross,
        'weighted_yield_net': weighted_yield_net,
        'weighted_dividend_growth': weighted_dividend_growth,
    }


def verify_portfolio_metrics(assets: Dict[str, Asset]) -> None:
    """
    Verify portfolio metrics match SDG document expectations.
    
    Prints warnings if metrics deviate from expected values.
    """
    metrics = calculate_portfolio_metrics(assets)
    
    print(f"Total allocation: {metrics['total_allocation']:.0%}")
    print(f"Portfolio weighted yield (gross): {metrics['weighted_yield_gross']:.2%}")
    print(f"Portfolio weighted yield (after withholding): {metrics['weighted_yield_net']:.2%}")
    print(f"Portfolio weighted dividend growth: {metrics['weighted_dividend_growth']:.2%}")
    
    # Expected values from SDG document
    expected_yield_net = 0.0140  # 1.40%
    expected_yield_gross = 0.0166  # 1.66%
    expected_growth = 0.1191  # 11.91%
    
    if abs(metrics['weighted_yield_net'] - expected_yield_net) > 0.002:
        print(f"WARNING: Net yield {metrics['weighted_yield_net']:.2%} differs from expected {expected_yield_net:.2%}")
    
    if abs(metrics['weighted_yield_gross'] - expected_yield_gross) > 0.002:
        print(f"WARNING: Gross yield {metrics['weighted_yield_gross']:.2%} differs from expected {expected_yield_gross:.2%}")
