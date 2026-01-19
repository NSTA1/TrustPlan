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

## Total Contributions

- **Lump sum**: GBP 86,000
- **Monthly contributions**: GBP 750,000 (25 years)
- **Total contributions**: GBP 836,000

## NAV Projections (GBP Real Terms)

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 5 | GBP 211,329 | GBP 259,699 | GBP 298,616 | GBP 345,691 | GBP 432,289 |
| 10 | GBP 386,096 | GBP 501,033 | GBP 604,259 | GBP 730,634 | GBP 989,256 |
| 15 | GBP 620,139 | GBP 824,873 | GBP 1,028,373 | GBP 1,295,759 | GBP 1,829,122 |
| 20 | GBP 949,547 | GBP 1,290,379 | GBP 1,644,792 | GBP 2,101,230 | GBP 3,121,416 |
| 25 | GBP 1,383,085 | GBP 1,940,738 | GBP 2,540,719 | GBP 3,366,038 | GBP 5,132,294 |
| 30 | GBP 1,576,972 | GBP 2,473,004 | GBP 3,398,281 | GBP 4,674,852 | GBP 7,797,298 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 20,134 | GBP 28,187 | GBP 37,011 | GBP 50,079 | GBP 84,065 |
| 21 | GBP 21,796 | GBP 30,909 | GBP 40,749 | GBP 55,926 | GBP 96,128 |
| 22 | GBP 23,435 | GBP 33,704 | GBP 44,990 | GBP 62,853 | GBP 110,913 |
| 23 | GBP 25,354 | GBP 36,753 | GBP 49,432 | GBP 69,820 | GBP 127,879 |
| 24 | GBP 27,216 | GBP 40,079 | GBP 54,511 | GBP 77,928 | GBP 148,528 |
| 25 | GBP 29,109 | GBP 43,252 | GBP 59,497 | GBP 85,993 | GBP 168,991 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 18,514 | GBP 27,708 | GBP 38,053 | GBP 55,609 | GBP 110,581 |
| 27 | GBP 19,528 | GBP 29,415 | GBP 40,669 | GBP 59,786 | GBP 120,682 |
| 28 | GBP 20,646 | GBP 31,337 | GBP 43,555 | GBP 64,303 | GBP 130,611 |
| 29 | GBP 21,800 | GBP 33,489 | GBP 46,491 | GBP 69,297 | GBP 142,337 |
| 30 | GBP 23,160 | GBP 35,538 | GBP 49,756 | GBP 74,508 | GBP 155,373 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 30,857 | GBP 46,180 | GBP 63,421 | GBP 92,681 | GBP 184,302 |
| 27 | GBP 32,546 | GBP 49,025 | GBP 67,782 | GBP 99,643 | GBP 201,137 |
| 28 | GBP 34,410 | GBP 52,229 | GBP 72,592 | GBP 107,172 | GBP 217,684 |
| 29 | GBP 36,334 | GBP 55,815 | GBP 77,485 | GBP 115,495 | GBP 237,228 |
| 30 | GBP 38,600 | GBP 59,231 | GBP 82,926 | GBP 124,179 | GBP 258,954 |

## Income Growth (Years 26-30)

- **Median CAGR**: 7.1%
- **5th percentile CAGR**: 3.5%
- **95th percentile CAGR**: 11.5%

## Scenario Analysis

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 86,407,585
- **Year 30 Total Dividends**: GBP 25,803,324
- **Year 30 Income Withdrawn**: GBP 15,481,994

### Median Case Path
- **Final NAV (Year 30)**: GBP 3,590,845
- **Year 30 Total Dividends**: GBP 126,201
- **Year 30 Income Withdrawn**: GBP 75,721

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 618,903
- **Year 30 Total Dividends**: GBP 78,900
- **Year 30 Income Withdrawn**: GBP 47,340

## Model Notes

This simulation uses a **realistic dividend growth model**:

1. **NAV Growth**: 5% real annual return (conservative)
2. **Dividend Growth**: Modelled as excess growth above NAV growth
   - Historical 5-year dividend growth includes underlying earnings growth
   - Only 'excess' portion (dividend growth minus NAV growth) applied additionally
   - Prevents double-counting of growth
3. **Growth Decay**: High excess growth rates decay toward sustainable levels
4. **Downturn Strategy**: Mechanical deployment at 10%/20%/30% drawdowns
5. **Dividend Calculation**: `dividend = units × base_dividend × excess_growth_factor`

---

*Report generated using Monte Carlo simulation based on SDG portfolio specifications.*
*All values in GBP real terms (inflation-adjusted).*