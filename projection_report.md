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
| 5 | GBP 207,369 | GBP 250,756 | GBP 287,087 | GBP 328,777 | GBP 405,317 |
| 10 | GBP 372,995 | GBP 477,623 | GBP 573,561 | GBP 690,097 | GBP 911,485 |
| 15 | GBP 597,410 | GBP 780,485 | GBP 966,108 | GBP 1,204,138 | GBP 1,686,905 |
| 20 | GBP 887,041 | GBP 1,210,271 | GBP 1,526,032 | GBP 1,959,889 | GBP 2,875,130 |
| 25 | GBP 1,268,890 | GBP 1,796,805 | GBP 2,325,829 | GBP 3,030,665 | GBP 4,677,452 |
| 30 | GBP 1,481,440 | GBP 2,241,673 | GBP 3,053,038 | GBP 4,213,860 | GBP 6,822,665 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 18,235 | GBP 25,197 | GBP 32,300 | GBP 42,697 | GBP 67,962 |
| 21 | GBP 19,691 | GBP 27,409 | GBP 35,469 | GBP 47,525 | GBP 77,217 |
| 22 | GBP 21,101 | GBP 29,916 | GBP 39,013 | GBP 52,954 | GBP 87,956 |
| 23 | GBP 22,699 | GBP 32,517 | GBP 42,810 | GBP 58,658 | GBP 101,106 |
| 24 | GBP 24,432 | GBP 35,251 | GBP 46,934 | GBP 65,130 | GBP 115,089 |
| 25 | GBP 25,953 | GBP 37,933 | GBP 50,878 | GBP 71,267 | GBP 127,823 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 16,484 | GBP 24,166 | GBP 32,437 | GBP 45,811 | GBP 83,515 |
| 27 | GBP 17,413 | GBP 25,652 | GBP 34,670 | GBP 49,184 | GBP 90,260 |
| 28 | GBP 18,356 | GBP 27,112 | GBP 36,980 | GBP 52,854 | GBP 98,292 |
| 29 | GBP 19,411 | GBP 28,837 | GBP 39,489 | GBP 56,783 | GBP 106,836 |
| 30 | GBP 20,555 | GBP 30,554 | GBP 42,048 | GBP 60,965 | GBP 116,210 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 27,474 | GBP 40,277 | GBP 54,062 | GBP 76,351 | GBP 139,191 |
| 27 | GBP 29,022 | GBP 42,754 | GBP 57,784 | GBP 81,974 | GBP 150,433 |
| 28 | GBP 30,593 | GBP 45,187 | GBP 61,633 | GBP 88,089 | GBP 163,820 |
| 29 | GBP 32,351 | GBP 48,061 | GBP 65,816 | GBP 94,638 | GBP 178,060 |
| 30 | GBP 34,259 | GBP 50,923 | GBP 70,080 | GBP 101,608 | GBP 193,684 |

## Income Growth (Years 26-30)

- **Median CAGR**: 6.7%
- **5th percentile CAGR**: 3.2%
- **95th percentile CAGR**: 10.9%

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
- **Mean deployment events**: 11.9
- **Median deployment events**: 12
- **Maximum deployment events**: 24

### Capital Deployed

- **Mean total deployed**: GBP 49,616
- **Median total deployed**: GBP 51,000
- **95th percentile deployed**: GBP 72,000

## Scenario Analysis

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 23,558,478
- **Year 30 Total Dividends**: GBP 29,182
- **Year 30 Income Withdrawn**: GBP 17,509
- **Dividend cuts experienced**: 8

### Median Case Path
- **Final NAV (Year 30)**: GBP 3,233,797
- **Year 30 Total Dividends**: GBP 69,318
- **Year 30 Income Withdrawn**: GBP 41,591
- **Dividend cuts experienced**: 14

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 691,964
- **Year 30 Total Dividends**: GBP 76,464
- **Year 30 Income Withdrawn**: GBP 45,879
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