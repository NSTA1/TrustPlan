# Portfolio NAV and Income Projection Report

## Simulation Parameters

- **Number of simulations**: 10,000
- **Simulation period**: 30 years (January 2026 - December 2055)
- **Accumulation phase**: Years 0-25 (100% dividend reinvestment)
- **Post-accumulation phase**: Years 26-30 (60% dividend withdrawal)
- **NAV expected return**: 5.0% real annual
- **NAV volatility**: 17.0% annual
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
| 5 | GBP 208,383 | GBP 251,463 | GBP 288,898 | GBP 332,170 | GBP 410,789 |
| 10 | GBP 378,630 | GBP 484,202 | GBP 578,583 | GBP 694,584 | GBP 917,728 |
| 15 | GBP 601,388 | GBP 792,655 | GBP 977,421 | GBP 1,211,464 | GBP 1,694,893 |
| 20 | GBP 899,202 | GBP 1,230,919 | GBP 1,540,897 | GBP 1,977,629 | GBP 2,861,023 |
| 25 | GBP 1,325,371 | GBP 1,848,967 | GBP 2,373,563 | GBP 3,092,015 | GBP 4,662,631 |
| 30 | GBP 1,535,279 | GBP 2,325,162 | GBP 3,139,583 | GBP 4,319,277 | GBP 6,980,963 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 19,620 | GBP 26,923 | GBP 34,712 | GBP 46,186 | GBP 74,155 |
| 21 | GBP 21,281 | GBP 29,454 | GBP 38,441 | GBP 51,659 | GBP 85,226 |
| 22 | GBP 22,921 | GBP 32,122 | GBP 42,441 | GBP 57,473 | GBP 97,716 |
| 23 | GBP 24,768 | GBP 35,019 | GBP 46,646 | GBP 64,145 | GBP 112,261 |
| 24 | GBP 26,606 | GBP 38,201 | GBP 51,284 | GBP 71,363 | GBP 129,072 |
| 25 | GBP 28,486 | GBP 41,315 | GBP 55,946 | GBP 78,182 | GBP 145,560 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 18,103 | GBP 26,383 | GBP 35,902 | GBP 50,539 | GBP 94,379 |
| 27 | GBP 19,199 | GBP 28,036 | GBP 38,349 | GBP 54,284 | GBP 103,127 |
| 28 | GBP 20,219 | GBP 29,858 | GBP 41,062 | GBP 58,410 | GBP 112,488 |
| 29 | GBP 21,501 | GBP 31,701 | GBP 43,789 | GBP 62,972 | GBP 123,007 |
| 30 | GBP 22,761 | GBP 33,734 | GBP 46,885 | GBP 67,747 | GBP 132,744 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 30,171 | GBP 43,971 | GBP 59,837 | GBP 84,231 | GBP 157,299 |
| 27 | GBP 31,998 | GBP 46,727 | GBP 63,914 | GBP 90,473 | GBP 171,878 |
| 28 | GBP 33,698 | GBP 49,763 | GBP 68,436 | GBP 97,350 | GBP 187,479 |
| 29 | GBP 35,835 | GBP 52,835 | GBP 72,982 | GBP 104,953 | GBP 205,012 |
| 30 | GBP 37,935 | GBP 56,223 | GBP 78,142 | GBP 112,911 | GBP 221,240 |

## Income Growth (Years 26-30)

- **Median CAGR**: 6.9%
- **5th percentile CAGR**: 3.5%
- **95th percentile CAGR**: 11.1%

## Dividend Stress Analysis

*Analysis of dividend cuts during market stress periods across all simulations*

### Frequency of Dividend Cuts

- **Simulations experiencing cuts**: 9,853 (98.5%)
- **Simulations with no cuts**: 147 (1.5%)

### Dividend Cut Statistics

| Metric | Value |
|--------|-------|
| Mean cuts per simulation | 6.42 |
| Median cuts per simulation | 6 |
| 5th percentile | 1 |
| 95th percentile | 13 |
| Maximum cuts (worst path) | 24 |
| Mean cuts (paths with cuts) | 6.5 |

*Note: Cuts are applied probabilistically when market drawdowns exceed the threshold.*
*High-resilience dividend aristocrats have significantly lower cut probability.*

## Downturn Strategy Analysis

*Analysis of the mechanical downturn fund deployment strategy*

### Deployment Frequency

- **Simulations with deployments**: 10,000 (100.0%)
- **Mean deployment events**: 11.9
- **Median deployment events**: 12
- **Maximum deployment events**: 24

### Capital Deployed

- **Mean total deployed**: GBP 49,890
- **Median total deployed**: GBP 51,000
- **95th percentile deployed**: GBP 72,000

## Scenario Analysis

*Each scenario shows a specific simulation path selected by final NAV percentile.*
*Dividend and income figures are from that specific path, not percentiles of dividends.*

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 6,986,111
- **Year 30 Total Dividends**: GBP 79,314
- **Year 30 Income Withdrawn**: GBP 47,588
- **Dividend cuts experienced**: 9

### Median Case Path (50th percentile NAV)
- **Final NAV (Year 30)**: GBP 3,139,693
- **Year 30 Total Dividends**: GBP 93,911
- **Year 30 Income Withdrawn**: GBP 56,347
- **Dividend cuts experienced**: 7

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 1,535,289
- **Year 30 Total Dividends**: GBP 58,097
- **Year 30 Income Withdrawn**: GBP 34,858
- **Dividend cuts experienced**: 6

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