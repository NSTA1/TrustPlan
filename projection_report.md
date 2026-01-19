# Portfolio NAV and Income Projection Report

## Simulation Parameters

- **Number of simulations**: 10,000
- **Simulation period**: 30 years (January 2026 - December 2055)
- **Accumulation phase**: Years 0-25 (100% dividend reinvestment)
- **Post-accumulation phase**: Years 26-30 (60% dividend withdrawal)
- **NAV expected return**: 5.0% real annual
- **NAV volatility**: 18.0% annual
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
| 5 | GBP 212,247 | GBP 257,581 | GBP 297,187 | GBP 344,361 | GBP 427,930 |
| 10 | GBP 389,180 | GBP 502,323 | GBP 604,552 | GBP 733,230 | GBP 986,386 |
| 15 | GBP 615,739 | GBP 828,651 | GBP 1,034,280 | GBP 1,287,818 | GBP 1,858,163 |
| 20 | GBP 924,622 | GBP 1,275,699 | GBP 1,639,640 | GBP 2,108,882 | GBP 3,144,205 |
| 25 | GBP 1,353,612 | GBP 1,921,361 | GBP 2,495,802 | GBP 3,306,390 | GBP 5,122,162 |
| 30 | GBP 1,566,584 | GBP 2,416,000 | GBP 3,305,945 | GBP 4,650,741 | GBP 7,622,186 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 19,283 | GBP 27,383 | GBP 35,871 | GBP 48,613 | GBP 81,159 |
| 21 | GBP 20,827 | GBP 29,904 | GBP 39,559 | GBP 54,058 | GBP 92,427 |
| 22 | GBP 22,538 | GBP 32,626 | GBP 43,709 | GBP 60,256 | GBP 106,573 |
| 23 | GBP 24,159 | GBP 35,622 | GBP 48,241 | GBP 67,038 | GBP 123,291 |
| 24 | GBP 26,154 | GBP 38,840 | GBP 53,154 | GBP 74,672 | GBP 141,575 |
| 25 | GBP 27,953 | GBP 41,789 | GBP 57,971 | GBP 82,107 | GBP 158,629 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 17,807 | GBP 26,661 | GBP 37,224 | GBP 52,853 | GBP 103,536 |
| 27 | GBP 18,847 | GBP 28,357 | GBP 39,751 | GBP 56,826 | GBP 114,357 |
| 28 | GBP 19,907 | GBP 30,123 | GBP 42,553 | GBP 61,197 | GBP 124,845 |
| 29 | GBP 21,145 | GBP 32,012 | GBP 45,366 | GBP 66,023 | GBP 135,678 |
| 30 | GBP 22,395 | GBP 34,164 | GBP 48,523 | GBP 70,934 | GBP 148,479 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 29,679 | GBP 44,435 | GBP 62,040 | GBP 88,088 | GBP 172,560 |
| 27 | GBP 31,411 | GBP 47,262 | GBP 66,252 | GBP 94,710 | GBP 190,595 |
| 28 | GBP 33,179 | GBP 50,204 | GBP 70,922 | GBP 101,994 | GBP 208,076 |
| 29 | GBP 35,242 | GBP 53,353 | GBP 75,611 | GBP 110,039 | GBP 226,130 |
| 30 | GBP 37,325 | GBP 56,939 | GBP 80,871 | GBP 118,223 | GBP 247,465 |

## Income Growth (Years 26-30)

- **Median CAGR**: 7.0%
- **5th percentile CAGR**: 3.5%
- **95th percentile CAGR**: 11.6%

## Dividend Stress Analysis

*Analysis of dividend cuts during market stress periods across all simulations*

### Frequency of Dividend Cuts

- **Simulations experiencing cuts**: 9,834 (98.3%)
- **Simulations with no cuts**: 166 (1.7%)

### Dividend Cut Statistics

| Metric | Value |
|--------|-------|
| Mean cuts per simulation | 6.85 |
| Median cuts per simulation | 7 |
| 5th percentile | 1 |
| 95th percentile | 14 |
| Maximum cuts (worst path) | 28 |
| Mean cuts (paths with cuts) | 7.0 |

*Note: Cuts are applied probabilistically when market drawdowns exceed the threshold.*
*High-resilience dividend aristocrats have significantly lower cut probability.*

## Downturn Strategy Analysis

*Analysis of the mechanical downturn fund deployment strategy*

### Deployment Frequency

- **Simulations with deployments**: 10,000 (100.0%)
- **Mean deployment events**: 36.5
- **Median deployment events**: 37
- **Maximum deployment events**: 47

### Capital Deployed

- **Mean total deployed**: GBP 147,397
- **Median total deployed**: GBP 147,000
- **95th percentile deployed**: GBP 186,000

## Scenario Analysis

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 24,456,504
- **Year 30 Total Dividends**: GBP 46,049
- **Year 30 Income Withdrawn**: GBP 27,629
- **Dividend cuts experienced**: 5

### Median Case Path
- **Final NAV (Year 30)**: GBP 3,512,470
- **Year 30 Total Dividends**: GBP 76,336
- **Year 30 Income Withdrawn**: GBP 45,802
- **Dividend cuts experienced**: 11

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 755,999
- **Year 30 Total Dividends**: GBP 60,154
- **Year 30 Income Withdrawn**: GBP 36,093
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