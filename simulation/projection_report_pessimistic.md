# Portfolio NAV and Income Projection Report

## Simulation Parameters

- **Number of simulations**: 10,000
- **Simulation period**: 30 years (January 2026 - December 2055)
- **Accumulation phase**: Years 0-25 (100% dividend reinvestment)
- **Post-accumulation phase**: Years 26-30 (60% dividend withdrawal)
- **NAV expected return**: 3.0% real annual
- **NAV volatility**: 22.0% annual
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
| 5 | GBP 181,500 | GBP 228,274 | GBP 271,472 | GBP 323,533 | GBP 422,321 |
| 10 | GBP 309,185 | GBP 409,921 | GBP 507,753 | GBP 641,042 | GBP 910,863 |
| 15 | GBP 472,936 | GBP 650,686 | GBP 830,908 | GBP 1,085,031 | GBP 1,613,946 |
| 20 | GBP 706,184 | GBP 1,020,509 | GBP 1,324,095 | GBP 1,735,388 | GBP 2,710,079 |
| 25 | GBP 1,070,661 | GBP 1,561,083 | GBP 2,103,674 | GBP 2,909,583 | GBP 5,031,817 |
| 30 | GBP 1,107,167 | GBP 1,855,034 | GBP 2,680,526 | GBP 4,037,084 | GBP 7,767,464 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 22,808 | GBP 35,700 | GBP 51,494 | GBP 79,848 | GBP 177,823 |
| 21 | GBP 25,078 | GBP 39,705 | GBP 58,748 | GBP 92,961 | GBP 224,651 |
| 22 | GBP 27,357 | GBP 44,240 | GBP 66,775 | GBP 108,448 | GBP 282,919 |
| 23 | GBP 29,782 | GBP 49,214 | GBP 76,141 | GBP 128,375 | GBP 359,658 |
| 24 | GBP 32,408 | GBP 54,907 | GBP 86,292 | GBP 151,810 | GBP 465,666 |
| 25 | GBP 35,458 | GBP 60,274 | GBP 96,575 | GBP 173,472 | GBP 570,279 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 22,586 | GBP 38,799 | GBP 63,075 | GBP 115,665 | GBP 397,118 |
| 27 | GBP 24,238 | GBP 41,748 | GBP 68,574 | GBP 128,254 | GBP 460,847 |
| 28 | GBP 25,733 | GBP 45,098 | GBP 74,908 | GBP 141,853 | GBP 537,482 |
| 29 | GBP 27,313 | GBP 48,524 | GBP 81,741 | GBP 157,450 | GBP 627,768 |
| 30 | GBP 29,144 | GBP 52,235 | GBP 89,137 | GBP 175,710 | GBP 747,868 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 37,644 | GBP 64,664 | GBP 105,125 | GBP 192,774 | GBP 661,863 |
| 27 | GBP 40,397 | GBP 69,581 | GBP 114,290 | GBP 213,756 | GBP 768,079 |
| 28 | GBP 42,889 | GBP 75,164 | GBP 124,846 | GBP 236,421 | GBP 895,803 |
| 29 | GBP 45,521 | GBP 80,874 | GBP 136,236 | GBP 262,416 | GBP 1,046,280 |
| 30 | GBP 48,573 | GBP 87,059 | GBP 148,562 | GBP 292,850 | GBP 1,246,447 |

## Income Growth (Years 26-30)

- **Median CAGR**: 9.1%
- **5th percentile CAGR**: 4.4%
- **95th percentile CAGR**: 19.6%

## Dividend Stress Analysis

*Analysis of dividend cuts during market stress periods across all simulations*

### Frequency of Dividend Cuts

- **Simulations experiencing cuts**: 9,638 (96.4%)
- **Simulations with no cuts**: 362 (3.6%)

### Dividend Cut Statistics

| Metric | Value |
|--------|-------|
| Mean cuts per simulation | 6.86 |
| Median cuts per simulation | 6 |
| 5th percentile | 1 |
| 95th percentile | 15 |
| Maximum cuts (worst path) | 31 |
| Mean cuts (paths with cuts) | 7.1 |

*Note: Cuts are applied probabilistically when market drawdowns exceed the threshold.*
*High-resilience dividend aristocrats have significantly lower cut probability.*

## Downturn Strategy Analysis

*Analysis of the mechanical downturn fund deployment strategy*

### Deployment Frequency

- **Simulations with deployments**: 10,000 (100.0%)
- **Mean deployment events**: 10.8
- **Median deployment events**: 10
- **Maximum deployment events**: 30

### Capital Deployed

- **Mean total deployed**: GBP 47,329
- **Median total deployed**: GBP 45,000
- **95th percentile deployed**: GBP 84,000

## Scenario Analysis

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 5,057,706,666
- **Year 30 Total Dividends**: GBP 1,861,827,509
- **Year 30 Income Withdrawn**: GBP 1,117,096,505
- **Dividend cuts experienced**: 10

### Median Case Path
- **Final NAV (Year 30)**: GBP 2,830,672
- **Year 30 Total Dividends**: GBP 97,865
- **Year 30 Income Withdrawn**: GBP 58,719
- **Dividend cuts experienced**: 0

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 269,338
- **Year 30 Total Dividends**: GBP 75,746
- **Year 30 Income Withdrawn**: GBP 45,447
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