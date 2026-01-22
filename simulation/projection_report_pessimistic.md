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
| 5 | GBP 180,228 | GBP 228,250 | GBP 270,755 | GBP 322,733 | GBP 423,260 |
| 10 | GBP 306,652 | GBP 413,173 | GBP 512,904 | GBP 642,752 | GBP 908,528 |
| 15 | GBP 481,661 | GBP 658,281 | GBP 843,050 | GBP 1,091,152 | GBP 1,630,397 |
| 20 | GBP 726,714 | GBP 1,034,794 | GBP 1,347,048 | GBP 1,780,744 | GBP 2,797,774 |
| 25 | GBP 1,092,668 | GBP 1,629,744 | GBP 2,192,210 | GBP 3,023,951 | GBP 5,149,443 |
| 30 | GBP 1,155,274 | GBP 1,959,615 | GBP 2,825,489 | GBP 4,226,399 | GBP 8,580,838 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 24,666 | GBP 38,907 | GBP 56,556 | GBP 89,001 | GBP 207,685 |
| 21 | GBP 27,091 | GBP 43,492 | GBP 64,767 | GBP 104,764 | GBP 263,673 |
| 22 | GBP 29,704 | GBP 48,695 | GBP 73,642 | GBP 123,298 | GBP 338,567 |
| 23 | GBP 32,561 | GBP 54,322 | GBP 83,725 | GBP 145,661 | GBP 440,333 |
| 24 | GBP 35,658 | GBP 60,808 | GBP 95,290 | GBP 172,268 | GBP 573,684 |
| 25 | GBP 38,523 | GBP 66,777 | GBP 107,331 | GBP 198,530 | GBP 709,039 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 24,793 | GBP 43,298 | GBP 70,551 | GBP 132,142 | GBP 497,892 |
| 27 | GBP 26,428 | GBP 46,629 | GBP 76,868 | GBP 146,917 | GBP 580,532 |
| 28 | GBP 28,194 | GBP 50,038 | GBP 83,825 | GBP 163,573 | GBP 681,239 |
| 29 | GBP 30,281 | GBP 54,161 | GBP 91,222 | GBP 182,390 | GBP 825,468 |
| 30 | GBP 32,423 | GBP 58,513 | GBP 99,841 | GBP 203,238 | GBP 979,183 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 41,321 | GBP 72,163 | GBP 117,585 | GBP 220,237 | GBP 829,820 |
| 27 | GBP 44,046 | GBP 77,715 | GBP 128,113 | GBP 244,862 | GBP 967,553 |
| 28 | GBP 46,989 | GBP 83,397 | GBP 139,709 | GBP 272,621 | GBP 1,135,398 |
| 29 | GBP 50,468 | GBP 90,269 | GBP 152,037 | GBP 303,984 | GBP 1,375,780 |
| 30 | GBP 54,038 | GBP 97,522 | GBP 166,401 | GBP 338,729 | GBP 1,631,971 |

## Income Growth (Years 26-30)

- **Median CAGR**: 9.4%
- **5th percentile CAGR**: 4.6%
- **95th percentile CAGR**: 20.4%

## Dividend Stress Analysis

*Analysis of dividend cuts during market stress periods across all simulations*

### Frequency of Dividend Cuts

- **Simulations experiencing cuts**: 9,641 (96.4%)
- **Simulations with no cuts**: 359 (3.6%)

### Dividend Cut Statistics

| Metric | Value |
|--------|-------|
| Mean cuts per simulation | 6.85 |
| Median cuts per simulation | 6 |
| 5th percentile | 1 |
| 95th percentile | 15 |
| Maximum cuts (worst path) | 28 |
| Mean cuts (paths with cuts) | 7.1 |

*Note: Cuts are applied probabilistically when market drawdowns exceed the threshold.*
*High-resilience dividend aristocrats have significantly lower cut probability.*

## Downturn Strategy Analysis

*Analysis of the mechanical downturn fund deployment strategy*

### Deployment Frequency

- **Simulations with deployments**: 10,000 (100.0%)
- **Mean deployment events**: 10.6
- **Median deployment events**: 10
- **Maximum deployment events**: 28

### Capital Deployed

- **Mean total deployed**: GBP 46,619
- **Median total deployed**: GBP 45,000
- **95th percentile deployed**: GBP 84,000

## Scenario Analysis

*Each scenario shows a specific simulation path selected by final NAV percentile.*
*Dividend and income figures are from that specific path, not percentiles of dividends.*

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 8,620,715
- **Year 30 Total Dividends**: GBP 253,745
- **Year 30 Income Withdrawn**: GBP 152,247
- **Dividend cuts experienced**: 11

### Median Case Path (50th percentile NAV)
- **Final NAV (Year 30)**: GBP 2,825,982
- **Year 30 Total Dividends**: GBP 145,128
- **Year 30 Income Withdrawn**: GBP 87,077
- **Dividend cuts experienced**: 9

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 1,155,284
- **Year 30 Total Dividends**: GBP 105,883
- **Year 30 Income Withdrawn**: GBP 63,530
- **Dividend cuts experienced**: 0

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