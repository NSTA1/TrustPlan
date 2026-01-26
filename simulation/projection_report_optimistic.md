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
| 5 | GBP 229,417 | GBP 270,703 | GBP 306,010 | GBP 347,393 | GBP 417,879 |
| 10 | GBP 438,938 | GBP 549,805 | GBP 647,610 | GBP 766,285 | GBP 985,953 |
| 15 | GBP 722,777 | GBP 949,993 | GBP 1,155,168 | GBP 1,414,558 | GBP 1,913,951 |
| 20 | GBP 1,120,357 | GBP 1,532,970 | GBP 1,914,892 | GBP 2,419,558 | GBP 3,460,135 |
| 25 | GBP 1,697,519 | GBP 2,379,983 | GBP 3,053,378 | GBP 3,940,554 | GBP 5,953,029 |
| 30 | GBP 2,162,187 | GBP 3,245,681 | GBP 4,366,032 | GBP 5,908,575 | GBP 9,438,260 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 16,527 | GBP 21,696 | GBP 26,777 | GBP 33,658 | GBP 47,117 |
| 21 | GBP 17,682 | GBP 23,454 | GBP 29,098 | GBP 36,906 | GBP 52,482 |
| 22 | GBP 18,958 | GBP 25,321 | GBP 31,658 | GBP 40,303 | GBP 58,381 |
| 23 | GBP 20,207 | GBP 27,257 | GBP 34,258 | GBP 44,008 | GBP 64,597 |
| 24 | GBP 21,491 | GBP 29,280 | GBP 36,968 | GBP 47,871 | GBP 71,658 |
| 25 | GBP 22,953 | GBP 31,344 | GBP 39,791 | GBP 51,620 | GBP 78,198 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 14,465 | GBP 19,907 | GBP 25,296 | GBP 32,962 | GBP 50,009 |
| 27 | GBP 15,225 | GBP 21,070 | GBP 26,803 | GBP 35,074 | GBP 53,699 |
| 28 | GBP 16,083 | GBP 22,232 | GBP 28,332 | GBP 37,234 | GBP 57,601 |
| 29 | GBP 16,922 | GBP 23,462 | GBP 30,073 | GBP 39,609 | GBP 61,756 |
| 30 | GBP 17,865 | GBP 24,801 | GBP 31,863 | GBP 42,085 | GBP 66,020 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 24,108 | GBP 33,178 | GBP 42,159 | GBP 54,936 | GBP 83,348 |
| 27 | GBP 25,375 | GBP 35,116 | GBP 44,671 | GBP 58,456 | GBP 89,499 |
| 28 | GBP 26,806 | GBP 37,053 | GBP 47,220 | GBP 62,056 | GBP 96,002 |
| 29 | GBP 28,203 | GBP 39,103 | GBP 50,122 | GBP 66,015 | GBP 102,926 |
| 30 | GBP 29,775 | GBP 41,335 | GBP 53,105 | GBP 70,141 | GBP 110,034 |

## Income Growth (Years 26-30)

- **Median CAGR**: 6.1%
- **5th percentile CAGR**: 2.9%
- **95th percentile CAGR**: 9.3%

## Dividend Stress Analysis

*Analysis of dividend cuts during market stress periods across all simulations*

### Frequency of Dividend Cuts

- **Simulations experiencing cuts**: 9,655 (96.5%)
- **Simulations with no cuts**: 345 (3.5%)

### Dividend Cut Statistics

| Metric | Value |
|--------|-------|
| Mean cuts per simulation | 5.04 |
| Median cuts per simulation | 5 |
| 5th percentile | 1 |
| 95th percentile | 11 |
| Maximum cuts (worst path) | 22 |
| Mean cuts (paths with cuts) | 5.2 |

*Note: Cuts are applied probabilistically when market drawdowns exceed the threshold.*
*High-resilience dividend aristocrats have significantly lower cut probability.*

## Downturn Strategy Analysis

*Analysis of the mechanical downturn fund deployment strategy*

### Deployment Frequency

- **Simulations with deployments**: 10,000 (100.0%)
- **Mean deployment events**: 11.6
- **Median deployment events**: 12
- **Maximum deployment events**: 22

### Capital Deployed

- **Mean total deployed**: GBP 45,634
- **Median total deployed**: GBP 45,000
- **95th percentile deployed**: GBP 63,000

## Scenario Analysis

*Each scenario shows a specific simulation path selected by final NAV percentile.*
*Dividend and income figures are from that specific path, not percentiles of dividends.*

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 9,438,636
- **Year 30 Total Dividends**: GBP 42,267
- **Year 30 Income Withdrawn**: GBP 25,360
- **Dividend cuts experienced**: 8

### Median Case Path (50th percentile NAV)
- **Final NAV (Year 30)**: GBP 4,367,016
- **Year 30 Total Dividends**: GBP 43,876
- **Year 30 Income Withdrawn**: GBP 26,326
- **Dividend cuts experienced**: 8

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 2,162,291
- **Year 30 Total Dividends**: GBP 41,189
- **Year 30 Income Withdrawn**: GBP 24,713
- **Dividend cuts experienced**: 7

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