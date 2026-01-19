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
| 5 | GBP 213,449 | GBP 258,913 | GBP 296,598 | GBP 338,539 | GBP 416,937 |
| 10 | GBP 393,522 | GBP 502,432 | GBP 601,366 | GBP 723,320 | GBP 952,426 |
| 15 | GBP 635,559 | GBP 826,351 | GBP 1,023,372 | GBP 1,273,122 | GBP 1,780,259 |
| 20 | GBP 950,500 | GBP 1,289,551 | GBP 1,627,059 | GBP 2,085,461 | GBP 3,045,901 |
| 25 | GBP 1,363,873 | GBP 1,921,661 | GBP 2,486,254 | GBP 3,234,121 | GBP 4,967,989 |
| 30 | GBP 1,590,798 | GBP 2,410,833 | GBP 3,282,150 | GBP 4,516,485 | GBP 7,312,158 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 19,279 | GBP 26,695 | GBP 34,401 | GBP 45,611 | GBP 72,658 |
| 21 | GBP 20,839 | GBP 29,090 | GBP 37,866 | GBP 50,871 | GBP 83,085 |
| 22 | GBP 22,341 | GBP 31,756 | GBP 41,623 | GBP 56,725 | GBP 95,130 |
| 23 | GBP 24,036 | GBP 34,513 | GBP 45,829 | GBP 63,112 | GBP 108,317 |
| 24 | GBP 25,800 | GBP 37,454 | GBP 50,165 | GBP 70,210 | GBP 124,140 |
| 25 | GBP 27,507 | GBP 40,294 | GBP 54,377 | GBP 76,620 | GBP 137,425 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 17,487 | GBP 25,765 | GBP 34,725 | GBP 49,381 | GBP 89,854 |
| 27 | GBP 18,481 | GBP 27,327 | GBP 37,126 | GBP 52,956 | GBP 97,642 |
| 28 | GBP 19,546 | GBP 29,023 | GBP 39,700 | GBP 56,924 | GBP 106,076 |
| 29 | GBP 20,628 | GBP 30,931 | GBP 42,331 | GBP 61,429 | GBP 115,331 |
| 30 | GBP 21,845 | GBP 32,818 | GBP 45,294 | GBP 65,764 | GBP 125,293 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 29,144 | GBP 42,942 | GBP 57,876 | GBP 82,301 | GBP 149,756 |
| 27 | GBP 30,802 | GBP 45,545 | GBP 61,877 | GBP 88,259 | GBP 162,737 |
| 28 | GBP 32,577 | GBP 48,372 | GBP 66,167 | GBP 94,874 | GBP 176,794 |
| 29 | GBP 34,380 | GBP 51,551 | GBP 70,551 | GBP 102,381 | GBP 192,218 |
| 30 | GBP 36,408 | GBP 54,697 | GBP 75,490 | GBP 109,607 | GBP 208,822 |

## Income Growth (Years 26-30)

- **Median CAGR**: 6.8%
- **5th percentile CAGR**: 3.4%
- **95th percentile CAGR**: 11.1%

## Dividend Stress Analysis

*Analysis of dividend cuts during market stress periods across all simulations*

### Frequency of Dividend Cuts

- **Simulations experiencing cuts**: 9,822 (98.2%)
- **Simulations with no cuts**: 178 (1.8%)

### Dividend Cut Statistics

| Metric | Value |
|--------|-------|
| Mean cuts per simulation | 6.41 |
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
- **Mean deployment events**: 35.6
- **Median deployment events**: 36
- **Maximum deployment events**: 47

### Capital Deployed

- **Mean total deployed**: GBP 141,136
- **Median total deployed**: GBP 141,000
- **95th percentile deployed**: GBP 183,000

## Scenario Analysis

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 24,613,438
- **Year 30 Total Dividends**: GBP 40,759
- **Year 30 Income Withdrawn**: GBP 24,456
- **Dividend cuts experienced**: 1

### Median Case Path
- **Final NAV (Year 30)**: GBP 3,478,448
- **Year 30 Total Dividends**: GBP 63,772
- **Year 30 Income Withdrawn**: GBP 38,263
- **Dividend cuts experienced**: 5

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 787,507
- **Year 30 Total Dividends**: GBP 86,997
- **Year 30 Income Withdrawn**: GBP 52,198
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