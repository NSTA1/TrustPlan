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
        'MSFT', 'SPGI', 'WM', 'ROP', 'ADP', 'ACN', 'SYK', 'MA', 'ASML', 'NVO',
        'CLPBY', 'MC', 'EL', 'RMS', 'REL', 'LSEG', 'OR', 'WKL', 'JDG', 'JPM', 'CNR',
        'HOCPY', 'LMT', 'BA', 'BMI', 'DSY', 'SU', 'MUV2'
    ]

    n = len(tickers)
    corr = np.eye(n)

    # Explicit correlations from SDG correlation matrix
    correlations = {
        # US Quality / Moat correlations
        ('MSFT', 'SPGI'): 0.55, ('MSFT', 'ACN'): 0.55, ('MSFT', 'ADP'): 0.50,
        ('MSFT', 'ROP'): 0.45, ('MSFT', 'DSY'): 0.45,
        ('MSFT', 'WM'): 0.40, ('MSFT', 'SYK'): 0.40, ('MSFT', 'ASML'): 0.45,
        ('MSFT', 'NVO'): 0.40, ('MSFT', 'CLPBY'): 0.40,
        ('MSFT', 'BMI'): 0.35, ('MSFT', 'SU'): 0.40, ('MSFT', 'MUV2'): 0.25,
        ('SPGI', 'ACN'): 0.55, ('SPGI', 'ADP'): 0.50, ('SPGI', 'ROP'): 0.50,
        ('SPGI', 'WM'): 0.40, ('SPGI', 'DSY'): 0.40,
        ('SPGI', 'BMI'): 0.30, ('SPGI', 'SU'): 0.35, ('SPGI', 'MUV2'): 0.30,
        ('WM', 'BMI'): 0.50, ('WM', 'SU'): 0.45, ('WM', 'CNR'): 0.40,
        ('WM', 'ROP'): 0.40, ('WM', 'DSY'): 0.30, ('WM', 'MUV2'): 0.25,
        ('ROP', 'ACN'): 0.50, ('ROP', 'ADP'): 0.45, ('ROP', 'SYK'): 0.40,
        ('ROP', 'DSY'): 0.40, ('ROP', 'SU'): 0.40, ('ROP', 'BMI'): 0.35,
        ('ROP', 'ASML'): 0.40, ('ROP', 'NVO'): 0.35, ('ROP', 'CLPBY'): 0.30,
        ('ROP', 'REL'): 0.35, ('ROP', 'LSEG'): 0.35, ('ROP', 'WKL'): 0.35,
        ('ROP', 'MA'): 0.30, ('ROP', 'JPM'): 0.30, ('ROP', 'CNR'): 0.35,
        ('ROP', 'HOCPY'): 0.30, ('ROP', 'MC'): 0.30, ('ROP', 'EL'): 0.30,
        ('ROP', 'OR'): 0.30, ('ROP', 'RMS'): 0.25, ('ROP', 'LMT'): 0.25,
        ('ROP', 'BA'): 0.20, ('ROP', 'JDG'): 0.20, ('ROP', 'MUV2'): 0.25,
        ('ADP', 'ACN'): 0.55, ('ADP', 'SYK'): 0.45, ('ADP', 'BMI'): 0.30,
        ('ADP', 'SU'): 0.35, ('ADP', 'DSY'): 0.35, ('ADP', 'MUV2'): 0.25,
        ('ACN', 'SYK'): 0.45, ('ACN', 'ASML'): 0.45, ('ACN', 'BMI'): 0.35,
        ('ACN', 'SU'): 0.45, ('ACN', 'DSY'): 0.45, ('ACN', 'MUV2'): 0.30,
        ('SYK', 'BMI'): 0.30, ('SYK', 'SU'): 0.35,
        ('SYK', 'DSY'): 0.30, ('SYK', 'MUV2'): 0.20,

        # Payments correlations
        ('MA', 'JPM'): 0.25, ('MA', 'BMI'): 0.20, ('MA', 'SU'): 0.25,
        ('MA', 'DSY'): 0.25, ('MA', 'MUV2'): 0.25,

        # Global Semis & Healthcare correlations
        ('ASML', 'NVO'): 0.50, ('ASML', 'CLPBY'): 0.45, ('ASML', 'HOCPY'): 0.35,
        ('ASML', 'SU'): 0.55, ('ASML', 'DSY'): 0.45,
        ('ASML', 'BMI'): 0.30, ('ASML', 'MUV2'): 0.20,
        ('NVO', 'CLPBY'): 0.50, ('NVO', 'BMI'): 0.25, ('NVO', 'SU'): 0.35,
        ('NVO', 'DSY'): 0.30, ('NVO', 'MUV2'): 0.20,
        ('CLPBY', 'BMI'): 0.25, ('CLPBY', 'SU'): 0.30,
        ('CLPBY', 'DSY'): 0.25, ('CLPBY', 'MUV2'): 0.20,
        ('HOCPY', 'BMI'): 0.25, ('HOCPY', 'SU'): 0.30,
        ('HOCPY', 'DSY'): 0.30, ('HOCPY', 'MUV2'): 0.20,

        # European Luxury & IP correlations
        ('MC', 'EL'): 0.55, ('MC', 'RMS'): 0.60, ('MC', 'OR'): 0.55,
        ('MC', 'BMI'): 0.20, ('MC', 'SU'): 0.35,
        ('MC', 'DSY'): 0.35, ('MC', 'MUV2'): 0.25,
        ('EL', 'RMS'): 0.55, ('EL', 'OR'): 0.55,
        ('EL', 'BMI'): 0.20, ('EL', 'SU'): 0.35,
        ('EL', 'DSY'): 0.35, ('EL', 'MUV2'): 0.25,
        ('RMS', 'OR'): 0.55, ('RMS', 'BMI'): 0.15, ('RMS', 'SU'): 0.30,
        ('RMS', 'DSY'): 0.30, ('RMS', 'MUV2'): 0.20,
        ('REL', 'LSEG'): 0.50, ('REL', 'WKL'): 0.40,
        ('REL', 'BMI'): 0.20, ('REL', 'SU'): 0.30, ('REL', 'BA'): 0.35,
        ('REL', 'DSY'): 0.35, ('REL', 'MUV2'): 0.25,
        ('LSEG', 'WKL'): 0.40, ('LSEG', 'BA'): 0.35,
        ('LSEG', 'BMI'): 0.20, ('LSEG', 'SU'): 0.30,
        ('LSEG', 'DSY'): 0.35, ('LSEG', 'MUV2'): 0.30,
        ('OR', 'BMI'): 0.20, ('OR', 'SU'): 0.35,
        ('OR', 'DSY'): 0.35, ('OR', 'MUV2'): 0.25,
        ('WKL', 'SU'): 0.40, ('WKL', 'BMI'): 0.20,
        ('WKL', 'DSY'): 0.40, ('WKL', 'MUV2'): 0.25,
        ('JDG', 'BMI'): 0.35,
        ('JDG', 'SU'): 0.20, ('JDG', 'DSY'): 0.20, ('JDG', 'MUV2'): 0.15,

        # Financial correlations
        ('JPM', 'MUV2'): 0.40,
        ('JPM', 'BMI'): 0.20, ('JPM', 'SU'): 0.25, ('JPM', 'DSY'): 0.25,

        # Defence correlations
        ('LMT', 'BA'): 0.50,
        ('LMT', 'BMI'): 0.30, ('LMT', 'SU'): 0.30,
        ('LMT', 'DSY'): 0.25, ('LMT', 'MUV2'): 0.25,
        ('BA', 'BMI'): 0.25, ('BA', 'SU'): 0.30,
        ('BA', 'DSY'): 0.25, ('BA', 'MUV2'): 0.25,

        # Transport & Infrastructure correlations
        ('CNR', 'BMI'): 0.45,
        ('CNR', 'SU'): 0.40, ('CNR', 'DSY'): 0.30, ('CNR', 'MUV2'): 0.25,
        ('CNR', 'LMT'): 0.35,

        # European Industrial Technology correlations
        ('DSY', 'SU'): 0.55,  # Same sleeve, both French industrial tech
        ('DSY', 'MUV2'): 0.25,
        ('BMI', 'SU'): 0.40,
        ('BMI', 'MUV2'): 0.20,

        # European Financials
        ('SU', 'MUV2'): 0.30,
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
