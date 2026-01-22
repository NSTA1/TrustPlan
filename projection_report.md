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
| 5 | GBP 208,185 | GBP 251,473 | GBP 287,501 | GBP 330,878 | GBP 409,804 |
| 10 | GBP 378,060 | GBP 481,604 | GBP 572,852 | GBP 691,519 | GBP 921,659 |
| 15 | GBP 597,063 | GBP 795,609 | GBP 981,772 | GBP 1,221,034 | GBP 1,690,223 |
| 20 | GBP 913,333 | GBP 1,246,595 | GBP 1,564,857 | GBP 1,998,123 | GBP 2,893,883 |
| 25 | GBP 1,347,022 | GBP 1,869,156 | GBP 2,398,501 | GBP 3,127,753 | GBP 4,709,715 |
| 30 | GBP 1,556,154 | GBP 2,340,506 | GBP 3,169,055 | GBP 4,350,781 | GBP 7,047,295 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 19,653 | GBP 27,268 | GBP 35,136 | GBP 46,731 | GBP 75,790 |
| 21 | GBP 21,216 | GBP 29,714 | GBP 38,758 | GBP 52,340 | GBP 87,342 |
| 22 | GBP 22,814 | GBP 32,417 | GBP 42,610 | GBP 58,319 | GBP 99,840 |
| 23 | GBP 24,506 | GBP 35,331 | GBP 46,724 | GBP 64,753 | GBP 114,650 |
| 24 | GBP 26,411 | GBP 38,378 | GBP 51,255 | GBP 71,973 | GBP 131,815 |
| 25 | GBP 28,262 | GBP 41,321 | GBP 55,427 | GBP 78,767 | GBP 147,230 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 17,905 | GBP 26,299 | GBP 35,554 | GBP 50,662 | GBP 95,833 |
| 27 | GBP 18,960 | GBP 27,988 | GBP 38,024 | GBP 54,351 | GBP 103,719 |
| 28 | GBP 20,069 | GBP 29,742 | GBP 40,584 | GBP 58,476 | GBP 112,930 |
| 29 | GBP 21,216 | GBP 31,562 | GBP 43,362 | GBP 62,878 | GBP 122,804 |
| 30 | GBP 22,435 | GBP 33,537 | GBP 46,302 | GBP 67,923 | GBP 135,439 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 29,842 | GBP 43,831 | GBP 59,256 | GBP 84,437 | GBP 159,722 |
| 27 | GBP 31,600 | GBP 46,647 | GBP 63,373 | GBP 90,585 | GBP 172,864 |
| 28 | GBP 33,448 | GBP 49,571 | GBP 67,639 | GBP 97,460 | GBP 188,217 |
| 29 | GBP 35,360 | GBP 52,603 | GBP 72,270 | GBP 104,797 | GBP 204,674 |
| 30 | GBP 37,392 | GBP 55,896 | GBP 77,171 | GBP 113,205 | GBP 225,732 |

## Income Growth (Years 26-30)

- **Median CAGR**: 6.9%
- **5th percentile CAGR**: 3.4%
- **95th percentile CAGR**: 11.1%

## Dividend Stress Analysis

*Analysis of dividend cuts during market stress periods across all simulations*

### Frequency of Dividend Cuts

- **Simulations experiencing cuts**: 9,848 (98.5%)
- **Simulations with no cuts**: 152 (1.5%)

### Dividend Cut Statistics

| Metric | Value |
|--------|-------|
| Mean cuts per simulation | 6.43 |
| Median cuts per simulation | 6 |
| 5th percentile | 1 |
| 95th percentile | 13 |
| Maximum cuts (worst path) | 25 |
| Mean cuts (paths with cuts) | 6.5 |

*Note: Cuts are applied probabilistically when market drawdowns exceed the threshold.*
*High-resilience dividend aristocrats have significantly lower cut probability.*

## Downturn Strategy Analysis

*Analysis of the mechanical downturn fund deployment strategy*

### Deployment Frequency

- **Simulations with deployments**: 10,000 (100.0%)
- **Mean deployment events**: 11.9
- **Median deployment events**: 12
- **Maximum deployment events**: 23

### Capital Deployed

- **Mean total deployed**: GBP 49,658
- **Median total deployed**: GBP 51,000
- **95th percentile deployed**: GBP 72,000

## Scenario Analysis

*Each scenario shows a specific simulation path selected by final NAV percentile.*
*Dividend and income figures are from that specific path, not percentiles of dividends.*

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 7,048,007
- **Year 30 Total Dividends**: GBP 42,674
- **Year 30 Income Withdrawn**: GBP 25,605
- **Dividend cuts experienced**: 9

### Median Case Path (50th percentile NAV)
- **Final NAV (Year 30)**: GBP 3,169,322
- **Year 30 Total Dividends**: GBP 48,605
- **Year 30 Income Withdrawn**: GBP 29,163
- **Dividend cuts experienced**: 7

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 1,556,161
- **Year 30 Total Dividends**: GBP 28,965
- **Year 30 Income Withdrawn**: GBP 17,379
- **Dividend cuts experienced**: 4

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