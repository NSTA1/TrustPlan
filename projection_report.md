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
- **Weekly contributions**: GBP 614/week for 25 years (GBP 798,200 total)
- **Total contributions**: GBP 884,200

## NAV Projections (GBP Real Terms)

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 5 | GBP 219,461 | GBP 265,910 | GBP 303,380 | GBP 348,818 | GBP 429,603 |
| 10 | GBP 400,426 | GBP 508,321 | GBP 605,444 | GBP 728,011 | GBP 950,142 |
| 15 | GBP 634,443 | GBP 835,538 | GBP 1,025,488 | GBP 1,270,682 | GBP 1,759,373 |
| 20 | GBP 959,867 | GBP 1,295,620 | GBP 1,630,136 | GBP 2,079,004 | GBP 3,031,154 |
| 25 | GBP 1,416,537 | GBP 1,958,363 | GBP 2,524,245 | GBP 3,308,057 | GBP 4,912,268 |
| 30 | GBP 1,631,641 | GBP 2,463,845 | GBP 3,327,241 | GBP 4,557,936 | GBP 7,429,806 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 21,312 | GBP 29,504 | GBP 38,089 | GBP 50,825 | GBP 83,401 |
| 21 | GBP 23,099 | GBP 32,161 | GBP 42,208 | GBP 56,681 | GBP 95,846 |
| 22 | GBP 24,871 | GBP 35,178 | GBP 46,497 | GBP 63,383 | GBP 110,261 |
| 23 | GBP 26,870 | GBP 38,337 | GBP 51,143 | GBP 70,655 | GBP 126,348 |
| 24 | GBP 28,892 | GBP 41,839 | GBP 56,304 | GBP 79,119 | GBP 143,782 |
| 25 | GBP 30,800 | GBP 45,150 | GBP 61,208 | GBP 86,505 | GBP 162,234 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 19,530 | GBP 28,875 | GBP 39,212 | GBP 55,742 | GBP 106,703 |
| 27 | GBP 20,810 | GBP 30,698 | GBP 41,860 | GBP 59,867 | GBP 115,717 |
| 28 | GBP 21,900 | GBP 32,685 | GBP 44,633 | GBP 64,481 | GBP 125,786 |
| 29 | GBP 23,214 | GBP 34,694 | GBP 47,883 | GBP 69,389 | GBP 137,040 |
| 30 | GBP 24,549 | GBP 36,924 | GBP 51,047 | GBP 74,616 | GBP 147,888 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 32,550 | GBP 48,125 | GBP 65,353 | GBP 92,904 | GBP 177,839 |
| 27 | GBP 34,683 | GBP 51,163 | GBP 69,767 | GBP 99,779 | GBP 192,862 |
| 28 | GBP 36,500 | GBP 54,474 | GBP 74,389 | GBP 107,469 | GBP 209,644 |
| 29 | GBP 38,689 | GBP 57,824 | GBP 79,805 | GBP 115,649 | GBP 228,400 |
| 30 | GBP 40,915 | GBP 61,540 | GBP 85,078 | GBP 124,360 | GBP 246,481 |

## Income Growth (Years 26-30)

- **Median CAGR**: 7.0%
- **5th percentile CAGR**: 3.5%
- **95th percentile CAGR**: 11.1%

## Dividend Stress Analysis

*Analysis of dividend cuts during market stress periods across all simulations*

### Frequency of Dividend Cuts

- **Simulations experiencing cuts**: 9,799 (98.0%)
- **Simulations with no cuts**: 201 (2.0%)

### Dividend Cut Statistics

| Metric | Value |
|--------|-------|
| Mean cuts per simulation | 6.47 |
| Median cuts per simulation | 6 |
| 5th percentile | 1 |
| 95th percentile | 13 |
| Maximum cuts (worst path) | 23 |
| Mean cuts (paths with cuts) | 6.6 |

*Note: Cuts are applied probabilistically when market drawdowns exceed the threshold.*
*High-resilience dividend aristocrats have significantly lower cut probability.*

## Downturn Strategy Analysis

*Analysis of the mechanical downturn fund deployment strategy*

### Deployment Frequency

- **Simulations with deployments**: 10,000 (100.0%)
- **Mean deployment events**: 11.9
- **Median deployment events**: 12
- **Maximum deployment events**: 22

### Capital Deployed

- **Mean total deployed**: GBP 49,707
- **Median total deployed**: GBP 51,000
- **95th percentile deployed**: GBP 72,000

## Scenario Analysis

*Each scenario shows a specific simulation path selected by final NAV percentile.*
*Dividend and income figures are from that specific path, not percentiles of dividends.*

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 7,431,010
- **Year 30 Total Dividends**: GBP 46,879
- **Year 30 Income Withdrawn**: GBP 28,127
- **Dividend cuts experienced**: 1

### Median Case Path (50th percentile NAV)
- **Final NAV (Year 30)**: GBP 3,327,316
- **Year 30 Total Dividends**: GBP 85,854
- **Year 30 Income Withdrawn**: GBP 51,512
- **Dividend cuts experienced**: 5

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 1,631,645
- **Year 30 Total Dividends**: GBP 74,430
- **Year 30 Income Withdrawn**: GBP 44,658
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