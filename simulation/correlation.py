"""
Dividend Growth Correlation Matrix.

Defines the correlation structure for dividend growth shocks
between portfolio assets based on the SDG correlation matrix.
"""

import numpy as np
from typing import Dict, List, Tuple

from .models import Asset


def create_dividend_correlation_matrix(assets: Dict[str, Asset]) -> Tuple[np.ndarray, List[str]]:
    """
    Create the dividend growth correlation matrix.
    
    The correlations are based on the SDG document's dividend growth
    correlation matrix, reflecting how assets' dividend changes
    tend to move together.
    
    Args:
        assets: Dictionary of Asset objects keyed by ticker
        
    Returns:
        Tuple of (correlation matrix, list of tickers in matrix order)
    """
    # Tickers in matrix order (matches SDG document)
    tickers = [
        'MSFT', 'SPGI', 'CB', 'WM', 'ADP', 'ACN', 'SYK', 'MA', 'ASML', 'NVO', 
        'CLPBY', 'MC', 'EL', 'RMS', 'REL', 'LSEG', 'OR', 'WKL', 'JPM', 'CNR',
        'HOCPY', 'JPXGY', 'SMFG', 'LMT', 'BA', 'ESS', 'GD'
    ]
    
    n = len(tickers)
    corr = np.eye(n)
    
    # Explicit correlations from SDG correlation matrix
    correlations = {
        # US Quality / Moat correlations
        ('MSFT', 'SPGI'): 0.55, ('MSFT', 'ACN'): 0.55, ('MSFT', 'ADP'): 0.50,
        ('SPGI', 'ACN'): 0.55, ('SPGI', 'ADP'): 0.50, ('SPGI', 'JPXGY'): 0.45,
        ('CB', 'JPM'): 0.55, ('CB', 'SMFG'): 0.45,
        ('ADP', 'ACN'): 0.55, ('ADP', 'SYK'): 0.45,
        ('ACN', 'SYK'): 0.45, ('ACN', 'ASML'): 0.45,
        
        # Global Semis & Healthcare correlations
        ('ASML', 'NVO'): 0.50, ('ASML', 'CLPBY'): 0.45,
        ('NVO', 'CLPBY'): 0.50,
        
        # European Luxury & IP correlations
        ('MC', 'EL'): 0.55, ('MC', 'RMS'): 0.60, ('MC', 'OR'): 0.55,
        ('EL', 'RMS'): 0.55, ('EL', 'OR'): 0.55,
        ('RMS', 'OR'): 0.55,
        ('REL', 'LSEG'): 0.50, ('REL', 'WKL'): 0.40,
        ('LSEG', 'JPXGY'): 0.50, ('LSEG', 'WKL'): 0.40,
        
        # Financial correlations
        ('JPM', 'SMFG'): 0.50, ('JPM', 'ESS'): 0.40,
        
        # Defence correlations
        ('LMT', 'BA'): 0.50,
        
        # General Dynamics correlations (from sdg.md correlation matrix)
        ('GD', 'LMT'): 0.55,  # High correlation with Lockheed Martin
        ('GD', 'BA'): 0.50,   # High correlation with BAE Systems
        ('GD', 'CNR'): 0.35,  # Moderate with Canadian National Railway
        ('GD', 'CB'): 0.30,   # Moderate with Chubb
        ('GD', 'JPM'): 0.30,  # Moderate with JP Morgan
        ('GD', 'SMFG'): 0.30, # Moderate with SMFG
        ('GD', 'WM'): 0.30,   # Moderate with Waste Management
        ('GD', 'ACN'): 0.30,  # Moderate with Accenture
    }
    
    ticker_idx = {t: i for i, t in enumerate(tickers)}
    
    # Apply explicit correlations (symmetric)
    for (t1, t2), rho in correlations.items():
        if t1 in ticker_idx and t2 in ticker_idx:
            i, j = ticker_idx[t1], ticker_idx[t2]
            corr[i, j] = rho
            corr[j, i] = rho
    
    # Fill remaining with default correlation
    default_correlation = 0.25
    for i in range(n):
        for j in range(n):
            if i != j and corr[i, j] == 0:
                corr[i, j] = default_correlation
    
    return corr, tickers
