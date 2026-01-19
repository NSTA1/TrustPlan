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
| 5 | GBP 189,557 | GBP 238,001 | GBP 283,065 | GBP 336,863 | GBP 438,555 |
| 10 | GBP 332,462 | GBP 439,247 | GBP 543,312 | GBP 681,585 | GBP 962,051 |
| 15 | GBP 515,155 | GBP 709,421 | GBP 901,543 | GBP 1,174,418 | GBP 1,738,969 |
| 20 | GBP 773,270 | GBP 1,115,192 | GBP 1,446,638 | GBP 1,889,635 | GBP 2,938,562 |
| 25 | GBP 1,176,179 | GBP 1,719,260 | GBP 2,309,652 | GBP 3,181,932 | GBP 5,512,152 |
| 30 | GBP 1,239,423 | GBP 2,061,620 | GBP 2,970,441 | GBP 4,455,819 | GBP 8,588,150 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 24,619 | GBP 38,756 | GBP 56,331 | GBP 87,876 | GBP 197,638 |
| 21 | GBP 27,168 | GBP 43,159 | GBP 64,355 | GBP 102,721 | GBP 246,147 |
| 22 | GBP 29,472 | GBP 48,157 | GBP 73,513 | GBP 120,088 | GBP 311,583 |
| 23 | GBP 32,360 | GBP 53,813 | GBP 83,671 | GBP 141,500 | GBP 398,775 |
| 24 | GBP 35,379 | GBP 60,002 | GBP 95,017 | GBP 167,636 | GBP 509,530 |
| 25 | GBP 38,353 | GBP 65,904 | GBP 106,510 | GBP 192,694 | GBP 631,993 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 24,488 | GBP 42,551 | GBP 69,432 | GBP 128,711 | GBP 432,926 |
| 27 | GBP 26,253 | GBP 45,895 | GBP 75,669 | GBP 142,999 | GBP 507,623 |
| 28 | GBP 28,082 | GBP 49,549 | GBP 82,728 | GBP 158,385 | GBP 595,113 |
| 29 | GBP 29,905 | GBP 53,511 | GBP 90,521 | GBP 176,103 | GBP 699,401 |
| 30 | GBP 31,995 | GBP 57,901 | GBP 98,914 | GBP 196,257 | GBP 826,866 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 40,813 | GBP 70,919 | GBP 115,720 | GBP 214,518 | GBP 721,543 |
| 27 | GBP 43,756 | GBP 76,491 | GBP 126,115 | GBP 238,332 | GBP 846,039 |
| 28 | GBP 46,804 | GBP 82,582 | GBP 137,880 | GBP 263,975 | GBP 991,855 |
| 29 | GBP 49,841 | GBP 89,185 | GBP 150,868 | GBP 293,504 | GBP 1,165,669 |
| 30 | GBP 53,325 | GBP 96,501 | GBP 164,857 | GBP 327,095 | GBP 1,378,110 |

## Income Growth (Years 26-30)

- **Median CAGR**: 9.4%
- **5th percentile CAGR**: 4.5%
- **95th percentile CAGR**: 19.8%

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
- **Mean deployment events**: 39.5
- **Median deployment events**: 40
- **Maximum deployment events**: 47

### Capital Deployed

- **Mean total deployed**: GBP 173,849
- **Median total deployed**: GBP 177,000
- **95th percentile deployed**: GBP 198,000

## Scenario Analysis

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 5,593,233,135
- **Year 30 Total Dividends**: GBP 2,058,963,474
- **Year 30 Income Withdrawn**: GBP 1,235,378,085
- **Dividend cuts experienced**: 10

### Median Case Path
- **Final NAV (Year 30)**: GBP 3,150,859
- **Year 30 Total Dividends**: GBP 212,169
- **Year 30 Income Withdrawn**: GBP 127,301
- **Dividend cuts experienced**: 0

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 317,992
- **Year 30 Total Dividends**: GBP 88,933
- **Year 30 Income Withdrawn**: GBP 53,360
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