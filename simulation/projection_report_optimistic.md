# Portfolio NAV and Income Projection Report

## Simulation Parameters

- **Number of simulations**: 10,000
- **Simulation period**: 30 years (January 2026 - December 2055)
- **Accumulation phase**: Years 0-25 (100% dividend reinvestment)
- **Post-accumulation phase**: Years 26-30 (60% dividend withdrawal)
- **NAV expected return**: 7.0% real annual
- **NAV volatility**: 15.0% annual
- **Dividend growth volatility**: 5.0%
- **Excess growth decay factor**: 0.95
- **Downturn fund**: GBP 15,000

### Dividend Stress Modelling

- **Cut trigger threshold**: 20% market drawdown
- **Base cut probability**: 15% per asset per stress event
- **Cut severity range**: 10% - 50%
- **Recovery rate**: 25% per year after stress ends

## Total Contributions

- **Lump sum**: GBP 86,000
- **Monthly contributions**: GBP 750,000 (25 years)
- **Total contributions**: GBP 836,000

## NAV Projections (GBP Real Terms)

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 5 | GBP 232,550 | GBP 276,959 | GBP 312,115 | GBP 354,818 | GBP 425,805 |
| 10 | GBP 451,837 | GBP 566,279 | GBP 671,193 | GBP 792,092 | GBP 1,018,764 |
| 15 | GBP 739,606 | GBP 975,912 | GBP 1,193,943 | GBP 1,458,927 | GBP 1,977,670 |
| 20 | GBP 1,136,622 | GBP 1,566,862 | GBP 1,963,505 | GBP 2,481,393 | GBP 3,527,077 |
| 25 | GBP 1,714,793 | GBP 2,418,993 | GBP 3,116,936 | GBP 4,024,595 | GBP 5,979,754 |
| 30 | GBP 2,181,826 | GBP 3,292,719 | GBP 4,445,288 | GBP 5,997,286 | GBP 9,534,067 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 16,064 | GBP 20,999 | GBP 25,760 | GBP 32,261 | GBP 45,776 |
| 21 | GBP 17,187 | GBP 22,648 | GBP 27,967 | GBP 35,302 | GBP 50,898 |
| 22 | GBP 18,347 | GBP 24,366 | GBP 30,311 | GBP 38,518 | GBP 56,545 |
| 23 | GBP 19,622 | GBP 26,202 | GBP 32,719 | GBP 41,786 | GBP 62,434 |
| 24 | GBP 20,802 | GBP 28,104 | GBP 35,370 | GBP 45,347 | GBP 68,564 |
| 25 | GBP 22,052 | GBP 30,033 | GBP 37,875 | GBP 48,832 | GBP 74,512 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 13,979 | GBP 18,995 | GBP 24,059 | GBP 31,145 | GBP 48,010 |
| 27 | GBP 14,676 | GBP 20,135 | GBP 25,520 | GBP 33,094 | GBP 51,331 |
| 28 | GBP 15,388 | GBP 21,247 | GBP 27,001 | GBP 35,189 | GBP 54,829 |
| 29 | GBP 16,284 | GBP 22,420 | GBP 28,587 | GBP 37,369 | GBP 58,245 |
| 30 | GBP 17,123 | GBP 23,669 | GBP 30,171 | GBP 39,716 | GBP 61,929 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 23,298 | GBP 31,659 | GBP 40,098 | GBP 51,909 | GBP 80,016 |
| 27 | GBP 24,459 | GBP 33,559 | GBP 42,533 | GBP 55,156 | GBP 85,552 |
| 28 | GBP 25,647 | GBP 35,412 | GBP 45,001 | GBP 58,649 | GBP 91,382 |
| 29 | GBP 27,139 | GBP 37,366 | GBP 47,645 | GBP 62,282 | GBP 97,075 |
| 30 | GBP 28,538 | GBP 39,448 | GBP 50,285 | GBP 66,194 | GBP 103,215 |

## Income Growth (Years 26-30)

- **Median CAGR**: 5.9%
- **5th percentile CAGR**: 2.8%
- **95th percentile CAGR**: 9.2%

## Dividend Stress Analysis

*Analysis of dividend cuts during market stress periods across all simulations*

### Frequency of Dividend Cuts

- **Simulations experiencing cuts**: 9,665 (96.7%)
- **Simulations with no cuts**: 335 (3.3%)

### Dividend Cut Statistics

| Metric | Value |
|--------|-------|
| Mean cuts per simulation | 5.04 |
| Median cuts per simulation | 5 |
| 5th percentile | 1 |
| 95th percentile | 10 |
| Maximum cuts (worst path) | 19 |
| Mean cuts (paths with cuts) | 5.2 |

*Note: Cuts are applied probabilistically when market drawdowns exceed the threshold.*
*High-resilience dividend aristocrats have significantly lower cut probability.*

## Downturn Strategy Analysis

*Analysis of the mechanical downturn fund deployment strategy*

### Deployment Frequency

- **Simulations with deployments**: 10,000 (100.0%)
- **Mean deployment events**: 29.3
- **Median deployment events**: 29
- **Maximum deployment events**: 48

### Capital Deployed

- **Mean total deployed**: GBP 106,261
- **Median total deployed**: GBP 105,000
- **95th percentile deployed**: GBP 153,000

## Scenario Analysis

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 33,707,628
- **Year 30 Total Dividends**: GBP 46,986
- **Year 30 Income Withdrawn**: GBP 28,192
- **Dividend cuts experienced**: 5

### Median Case Path
- **Final NAV (Year 30)**: GBP 4,755,075
- **Year 30 Total Dividends**: GBP 44,012
- **Year 30 Income Withdrawn**: GBP 26,407
- **Dividend cuts experienced**: 4

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 875,869
- **Year 30 Total Dividends**: GBP 51,269
- **Year 30 Income Withdrawn**: GBP 30,761
- **Dividend cuts experienced**: 3

## Model Notes

This simulation uses a **realistic dividend growth model**:

1. **NAV Growth**: 5% real annual return (conservative)
2. **Dividend Growth**: Modelled as excess growth above NAV growth
   - Historical 5-year dividend growth includes underlying earnings growth
   - Only 'excess' portion (dividend growth minus NAV growth) applied additionally
   - Prevents double-counting of growth
3. **Growth Decay**: High excess growth rates decay toward sustainable levels
4. **Downturn Strategy**: Mechanical deployment at 10%/20%/30% drawdowns
5. **Dividend Cuts**: Probabilistic cuts during market stress (>20% drawdown)
   - Cut probability scaled by asset resilience score (0-1)
   - Higher resilience = lower cut probability
   - Cuts recover gradually after market stabilization
6. **Dividend Calculation**: `dividend = units × base_dividend × excess_growth_factor × cut_factor`

---

*Report generated using Monte Carlo simulation based on SDG portfolio specifications.*
*All values in GBP real terms (inflation-adjusted).*