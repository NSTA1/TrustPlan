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
| 5 | GBP 181,751 | GBP 228,942 | GBP 270,853 | GBP 323,476 | GBP 425,163 |
| 10 | GBP 307,394 | GBP 412,332 | GBP 511,007 | GBP 641,158 | GBP 922,324 |
| 15 | GBP 474,987 | GBP 651,547 | GBP 833,624 | GBP 1,078,821 | GBP 1,626,352 |
| 20 | GBP 722,913 | GBP 1,035,463 | GBP 1,339,548 | GBP 1,787,780 | GBP 2,825,825 |
| 25 | GBP 1,097,539 | GBP 1,626,785 | GBP 2,181,898 | GBP 3,033,726 | GBP 5,205,055 |
| 30 | GBP 1,179,897 | GBP 1,955,806 | GBP 2,843,299 | GBP 4,258,400 | GBP 8,457,417 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 24,470 | GBP 38,945 | GBP 56,670 | GBP 88,519 | GBP 204,363 |
| 21 | GBP 26,704 | GBP 43,668 | GBP 64,536 | GBP 104,716 | GBP 258,491 |
| 22 | GBP 29,213 | GBP 48,892 | GBP 73,916 | GBP 124,245 | GBP 332,048 |
| 23 | GBP 32,260 | GBP 54,794 | GBP 84,653 | GBP 146,706 | GBP 432,873 |
| 24 | GBP 35,494 | GBP 61,087 | GBP 96,215 | GBP 174,641 | GBP 562,216 |
| 25 | GBP 38,980 | GBP 67,363 | GBP 108,401 | GBP 200,493 | GBP 705,860 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 24,965 | GBP 43,539 | GBP 70,713 | GBP 133,823 | GBP 497,092 |
| 27 | GBP 26,595 | GBP 47,142 | GBP 77,678 | GBP 148,453 | GBP 578,395 |
| 28 | GBP 28,654 | GBP 50,949 | GBP 84,550 | GBP 166,272 | GBP 672,890 |
| 29 | GBP 30,326 | GBP 54,880 | GBP 92,630 | GBP 185,638 | GBP 800,412 |
| 30 | GBP 32,551 | GBP 59,745 | GBP 101,348 | GBP 206,265 | GBP 957,521 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 41,608 | GBP 72,566 | GBP 117,855 | GBP 223,039 | GBP 828,487 |
| 27 | GBP 44,325 | GBP 78,570 | GBP 129,464 | GBP 247,421 | GBP 963,992 |
| 28 | GBP 47,757 | GBP 84,915 | GBP 140,917 | GBP 277,120 | GBP 1,121,484 |
| 29 | GBP 50,543 | GBP 91,467 | GBP 154,384 | GBP 309,396 | GBP 1,334,021 |
| 30 | GBP 54,252 | GBP 99,574 | GBP 168,913 | GBP 343,775 | GBP 1,595,869 |

## Income Growth (Years 26-30)

- **Median CAGR**: 9.5%
- **5th percentile CAGR**: 4.6%
- **95th percentile CAGR**: 20.6%

## Dividend Stress Analysis

*Analysis of dividend cuts during market stress periods across all simulations*

### Frequency of Dividend Cuts

- **Simulations experiencing cuts**: 9,694 (96.9%)
- **Simulations with no cuts**: 306 (3.1%)

### Dividend Cut Statistics

| Metric | Value |
|--------|-------|
| Mean cuts per simulation | 6.93 |
| Median cuts per simulation | 6 |
| 5th percentile | 1 |
| 95th percentile | 15 |
| Maximum cuts (worst path) | 29 |
| Mean cuts (paths with cuts) | 7.1 |

*Note: Cuts are applied probabilistically when market drawdowns exceed the threshold.*
*High-resilience dividend aristocrats have significantly lower cut probability.*

## Downturn Strategy Analysis

*Analysis of the mechanical downturn fund deployment strategy*

### Deployment Frequency

- **Simulations with deployments**: 10,000 (100.0%)
- **Mean deployment events**: 10.8
- **Median deployment events**: 10
- **Maximum deployment events**: 28

### Capital Deployed

- **Mean total deployed**: GBP 47,433
- **Median total deployed**: GBP 48,000
- **95th percentile deployed**: GBP 84,000

## Scenario Analysis

*Each scenario shows a specific simulation path selected by final NAV percentile.*
*Dividend and income figures are from that specific path, not percentiles of dividends.*

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 8,465,334
- **Year 30 Total Dividends**: GBP 332,808
- **Year 30 Income Withdrawn**: GBP 199,685
- **Dividend cuts experienced**: 1

### Median Case Path (50th percentile NAV)
- **Final NAV (Year 30)**: GBP 2,843,549
- **Year 30 Total Dividends**: GBP 110,002
- **Year 30 Income Withdrawn**: GBP 66,001
- **Dividend cuts experienced**: 7

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 1,179,952
- **Year 30 Total Dividends**: GBP 91,080
- **Year 30 Income Withdrawn**: GBP 54,648
- **Dividend cuts experienced**: 14

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