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
    # Updated: Removed ESS and GD, added BMI and SU
    tickers = [
        'MSFT', 'SPGI', 'WM', 'ADP', 'ACN', 'SYK', 'MA', 'ASML', 'NVO', 
        'CLPBY', 'MC', 'EL', 'RMS', 'REL', 'LSEG', 'OR', 'WKL', 'JDG', 'JPM', 'CNR',
        'HOCPY', 'JPXGY', 'SMFG', 'LMT', 'BA', 'BMI', 'SU'
    ]
    
    n = len(tickers)
    corr = np.eye(n)
    
    # Explicit correlations from SDG correlation matrix
    correlations = {
        # US Quality / Moat correlations
        ('MSFT', 'SPGI'): 0.55, ('MSFT', 'ACN'): 0.55, ('MSFT', 'ADP'): 0.50,
        ('MSFT', 'WM'): 0.40, ('MSFT', 'SYK'): 0.40, ('MSFT', 'ASML'): 0.45,
        ('MSFT', 'BMI'): 0.35, ('MSFT', 'SU'): 0.40,
        ('SPGI', 'ACN'): 0.55, ('SPGI', 'ADP'): 0.50, ('SPGI', 'JPXGY'): 0.45,
        ('SPGI', 'WM'): 0.40, ('SPGI', 'BMI'): 0.30, ('SPGI', 'SU'): 0.35,
        ('WM', 'BMI'): 0.50, ('WM', 'SU'): 0.45, ('WM', 'CNR'): 0.40,
        ('ADP', 'ACN'): 0.55, ('ADP', 'SYK'): 0.45, ('ADP', 'BMI'): 0.30, ('ADP', 'SU'): 0.35,
        ('ACN', 'SYK'): 0.45, ('ACN', 'ASML'): 0.45, ('ACN', 'BMI'): 0.35, ('ACN', 'SU'): 0.45,
        ('SYK', 'BMI'): 0.30, ('SYK', 'SU'): 0.35,
        
        # Payments correlations
        ('MA', 'JPM'): 0.25, ('MA', 'BMI'): 0.20, ('MA', 'SU'): 0.25,
        
        # Global Semis & Healthcare correlations
        ('ASML', 'NVO'): 0.50, ('ASML', 'CLPBY'): 0.45, ('ASML', 'HOCPY'): 0.35,
        ('ASML', 'SU'): 0.55,  # Both European tech/industrial
        ('ASML', 'BMI'): 0.30,
        ('NVO', 'CLPBY'): 0.50, ('NVO', 'BMI'): 0.25, ('NVO', 'SU'): 0.35,
        ('CLPBY', 'BMI'): 0.25, ('CLPBY', 'SU'): 0.30,
        ('HOCPY', 'BMI'): 0.25, ('HOCPY', 'SU'): 0.30,
        
        # European Luxury & IP correlations
        ('MC', 'EL'): 0.55, ('MC', 'RMS'): 0.60, ('MC', 'OR'): 0.55,
        ('MC', 'BMI'): 0.20, ('MC', 'SU'): 0.35,
        ('EL', 'RMS'): 0.55, ('EL', 'OR'): 0.55,
        ('EL', 'BMI'): 0.20, ('EL', 'SU'): 0.35,
        ('RMS', 'OR'): 0.55, ('RMS', 'BMI'): 0.15, ('RMS', 'SU'): 0.30,
        ('REL', 'LSEG'): 0.50, ('REL', 'WKL'): 0.40,
        ('REL', 'BMI'): 0.20, ('REL', 'SU'): 0.30,
        ('LSEG', 'JPXGY'): 0.50, ('LSEG', 'WKL'): 0.40,
        ('LSEG', 'BMI'): 0.20, ('LSEG', 'SU'): 0.30,
        ('OR', 'BMI'): 0.20, ('OR', 'SU'): 0.35,
        ('WKL', 'SU'): 0.40, ('WKL', 'BMI'): 0.20,
        ('JDG', 'BMI'): 0.35,  # Both small-cap industrial/scientific instruments
        ('JDG', 'SU'): 0.20,
        
        # Financial correlations
        ('JPM', 'SMFG'): 0.50, ('JPM', 'JPXGY'): 0.35,
        ('JPM', 'BMI'): 0.20, ('JPM', 'SU'): 0.25,
        ('SMFG', 'BMI'): 0.15, ('SMFG', 'SU'): 0.20,
        ('JPXGY', 'BMI'): 0.20, ('JPXGY', 'SU'): 0.25,
        
        # Defence correlations
        ('LMT', 'BA'): 0.50,
        ('LMT', 'BMI'): 0.30, ('LMT', 'SU'): 0.30,
        ('BA', 'BMI'): 0.25, ('BA', 'SU'): 0.30,
        
        # Transport & Infrastructure correlations
        ('CNR', 'BMI'): 0.45,  # Both infrastructure
        ('CNR', 'SU'): 0.40,
        ('CNR', 'LMT'): 0.35,
        
        # BMI and SU correlation
        ('BMI', 'SU'): 0.40,  # Industrial infrastructure overlap
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
