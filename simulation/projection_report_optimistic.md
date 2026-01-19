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
| 5 | GBP 226,832 | GBP 270,758 | GBP 305,394 | GBP 346,982 | GBP 414,727 |
| 10 | GBP 435,944 | GBP 547,945 | GBP 648,865 | GBP 766,278 | GBP 986,509 |
| 15 | GBP 710,380 | GBP 934,527 | GBP 1,148,333 | GBP 1,407,933 | GBP 1,905,537 |
| 20 | GBP 1,091,566 | GBP 1,497,090 | GBP 1,881,273 | GBP 2,375,997 | GBP 3,385,013 |
| 25 | GBP 1,646,939 | GBP 2,309,127 | GBP 2,985,077 | GBP 3,862,620 | GBP 5,747,272 |
| 30 | GBP 2,072,884 | GBP 3,135,791 | GBP 4,249,490 | GBP 5,739,972 | GBP 9,143,462 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 15,482 | GBP 20,172 | GBP 24,695 | GBP 30,820 | GBP 43,961 |
| 21 | GBP 16,583 | GBP 21,789 | GBP 26,796 | GBP 33,709 | GBP 48,453 |
| 22 | GBP 17,656 | GBP 23,442 | GBP 29,054 | GBP 36,693 | GBP 53,765 |
| 23 | GBP 18,851 | GBP 25,149 | GBP 31,396 | GBP 39,823 | GBP 59,537 |
| 24 | GBP 20,009 | GBP 27,028 | GBP 33,887 | GBP 43,220 | GBP 65,610 |
| 25 | GBP 21,227 | GBP 28,801 | GBP 36,320 | GBP 46,628 | GBP 71,382 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 13,409 | GBP 18,231 | GBP 23,019 | GBP 29,702 | GBP 45,811 |
| 27 | GBP 14,078 | GBP 19,273 | GBP 24,387 | GBP 31,478 | GBP 48,789 |
| 28 | GBP 14,784 | GBP 20,416 | GBP 25,831 | GBP 33,497 | GBP 51,972 |
| 29 | GBP 15,582 | GBP 21,461 | GBP 27,260 | GBP 35,672 | GBP 55,309 |
| 30 | GBP 16,441 | GBP 22,679 | GBP 28,816 | GBP 37,737 | GBP 59,069 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 22,349 | GBP 30,385 | GBP 38,365 | GBP 49,503 | GBP 76,352 |
| 27 | GBP 23,463 | GBP 32,121 | GBP 40,644 | GBP 52,464 | GBP 81,314 |
| 28 | GBP 24,639 | GBP 34,026 | GBP 43,052 | GBP 55,829 | GBP 86,620 |
| 29 | GBP 25,970 | GBP 35,769 | GBP 45,433 | GBP 59,453 | GBP 92,182 |
| 30 | GBP 27,401 | GBP 37,798 | GBP 48,027 | GBP 62,895 | GBP 98,449 |

## Income Growth (Years 26-30)

- **Median CAGR**: 5.9%
- **5th percentile CAGR**: 2.8%
- **95th percentile CAGR**: 9.1%

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
- **Mean deployment events**: 11.6
- **Median deployment events**: 12
- **Maximum deployment events**: 21

### Capital Deployed

- **Mean total deployed**: GBP 45,754
- **Median total deployed**: GBP 45,000
- **95th percentile deployed**: GBP 63,000

## Scenario Analysis

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 32,820,725
- **Year 30 Total Dividends**: GBP 45,747
- **Year 30 Income Withdrawn**: GBP 27,448
- **Dividend cuts experienced**: 5

### Median Case Path
- **Final NAV (Year 30)**: GBP 4,534,287
- **Year 30 Total Dividends**: GBP 18,954
- **Year 30 Income Withdrawn**: GBP 11,373
- **Dividend cuts experienced**: 8

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 823,394
- **Year 30 Total Dividends**: GBP 48,209
- **Year 30 Income Withdrawn**: GBP 28,925
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