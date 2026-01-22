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
| 5 | GBP 228,597 | GBP 271,652 | GBP 306,599 | GBP 347,622 | GBP 418,124 |
| 10 | GBP 440,196 | GBP 550,813 | GBP 647,422 | GBP 763,506 | GBP 981,482 |
| 15 | GBP 727,518 | GBP 950,123 | GBP 1,154,017 | GBP 1,418,133 | GBP 1,919,905 |
| 20 | GBP 1,125,283 | GBP 1,527,105 | GBP 1,911,637 | GBP 2,403,199 | GBP 3,385,403 |
| 25 | GBP 1,698,782 | GBP 2,365,053 | GBP 3,043,765 | GBP 3,950,882 | GBP 5,872,960 |
| 30 | GBP 2,134,129 | GBP 3,227,152 | GBP 4,337,558 | GBP 5,877,696 | GBP 9,297,683 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 16,780 | GBP 21,902 | GBP 26,918 | GBP 33,555 | GBP 48,467 |
| 21 | GBP 17,959 | GBP 23,633 | GBP 29,167 | GBP 36,806 | GBP 53,685 |
| 22 | GBP 19,118 | GBP 25,460 | GBP 31,686 | GBP 40,235 | GBP 60,003 |
| 23 | GBP 20,447 | GBP 27,320 | GBP 34,300 | GBP 43,774 | GBP 66,183 |
| 24 | GBP 21,903 | GBP 29,428 | GBP 37,024 | GBP 47,665 | GBP 72,605 |
| 25 | GBP 23,148 | GBP 31,436 | GBP 39,859 | GBP 51,206 | GBP 79,239 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 14,605 | GBP 19,917 | GBP 25,269 | GBP 32,683 | GBP 50,818 |
| 27 | GBP 15,362 | GBP 21,007 | GBP 26,736 | GBP 34,718 | GBP 54,114 |
| 28 | GBP 16,189 | GBP 22,184 | GBP 28,304 | GBP 36,884 | GBP 57,931 |
| 29 | GBP 17,033 | GBP 23,454 | GBP 30,012 | GBP 39,286 | GBP 62,230 |
| 30 | GBP 17,882 | GBP 24,751 | GBP 31,694 | GBP 41,794 | GBP 66,512 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 24,342 | GBP 33,195 | GBP 42,115 | GBP 54,471 | GBP 84,697 |
| 27 | GBP 25,603 | GBP 35,011 | GBP 44,560 | GBP 57,863 | GBP 90,190 |
| 28 | GBP 26,981 | GBP 36,974 | GBP 47,174 | GBP 61,474 | GBP 96,552 |
| 29 | GBP 28,389 | GBP 39,090 | GBP 50,020 | GBP 65,476 | GBP 103,717 |
| 30 | GBP 29,803 | GBP 41,251 | GBP 52,823 | GBP 69,657 | GBP 110,853 |

## Income Growth (Years 26-30)

- **Median CAGR**: 5.9%
- **5th percentile CAGR**: 2.9%
- **95th percentile CAGR**: 9.3%

## Dividend Stress Analysis

*Analysis of dividend cuts during market stress periods across all simulations*

### Frequency of Dividend Cuts

- **Simulations experiencing cuts**: 9,651 (96.5%)
- **Simulations with no cuts**: 349 (3.5%)

### Dividend Cut Statistics

| Metric | Value |
|--------|-------|
| Mean cuts per simulation | 5.09 |
| Median cuts per simulation | 5 |
| 5th percentile | 1 |
| 95th percentile | 11 |
| Maximum cuts (worst path) | 19 |
| Mean cuts (paths with cuts) | 5.3 |

*Note: Cuts are applied probabilistically when market drawdowns exceed the threshold.*
*High-resilience dividend aristocrats have significantly lower cut probability.*

## Downturn Strategy Analysis

*Analysis of the mechanical downturn fund deployment strategy*

### Deployment Frequency

- **Simulations with deployments**: 10,000 (100.0%)
- **Mean deployment events**: 11.7
- **Median deployment events**: 12
- **Maximum deployment events**: 21

### Capital Deployed

- **Mean total deployed**: GBP 45,855
- **Median total deployed**: GBP 45,000
- **95th percentile deployed**: GBP 63,000

## Scenario Analysis

*Each scenario shows a specific simulation path selected by final NAV percentile.*
*Dividend and income figures are from that specific path, not percentiles of dividends.*

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 9,299,076
- **Year 30 Total Dividends**: GBP 44,350
- **Year 30 Income Withdrawn**: GBP 26,610
- **Dividend cuts experienced**: 7

### Median Case Path (50th percentile NAV)
- **Final NAV (Year 30)**: GBP 4,337,743
- **Year 30 Total Dividends**: GBP 39,842
- **Year 30 Income Withdrawn**: GBP 23,905
- **Dividend cuts experienced**: 3

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 2,134,130
- **Year 30 Total Dividends**: GBP 71,725
- **Year 30 Income Withdrawn**: GBP 43,035
- **Dividend cuts experienced**: 11

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