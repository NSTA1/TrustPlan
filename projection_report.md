# Portfolio NAV and Income Projection Report

## Simulation Parameters

- **Number of simulations**: 10,000
- **Simulation period**: 30 years (December 2025 - December 2055)
- **Accumulation phase**: Years 0-25 (100% dividend reinvestment)
- **Post-accumulation phase**: Years 26-30 (60% dividend withdrawal)
- **NAV expected return**: 5.0% real annual
- **NAV volatility**: 18.0% annual
- **Dividend growth volatility**: 5.0%
- **Excess growth decay factor**: 0.95

## Total Contributions

- **Lump sum**: GBP 55,500
- **Weekly contributions**: GBP 46,000 (20 weeks)
- **Monthly contributions**: GBP 499,800 (25 years)
- **Total contributions**: GBP 601,300

## NAV Projections (GBP Real Terms)

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 5 | GBP 159,611 | GBP 197,964 | GBP 230,729 | GBP 272,412 | GBP 344,814 |
| 10 | GBP 268,811 | GBP 352,266 | GBP 430,727 | GBP 528,821 | GBP 721,427 |
| 15 | GBP 417,346 | GBP 557,016 | GBP 700,862 | GBP 896,567 | GBP 1,275,040 |
| 20 | GBP 618,902 | GBP 855,610 | GBP 1,096,873 | GBP 1,438,928 | GBP 2,167,713 |
| 25 | GBP 902,201 | GBP 1,289,104 | GBP 1,674,897 | GBP 2,237,523 | GBP 3,556,374 |
| 30 | GBP 1,029,282 | GBP 1,600,160 | GBP 2,213,797 | GBP 3,113,473 | GBP 5,243,892 |

## Annual Net Dividends (Years 20-25, Accumulation Phase)

*All dividends reinvested during accumulation phase*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 20 | GBP 13,952 | GBP 19,339 | GBP 24,908 | GBP 33,214 | GBP 55,008 |
| 21 | GBP 14,991 | GBP 21,132 | GBP 27,487 | GBP 37,179 | GBP 63,753 |
| 22 | GBP 16,154 | GBP 23,048 | GBP 30,251 | GBP 41,462 | GBP 72,941 |
| 23 | GBP 17,468 | GBP 24,984 | GBP 33,324 | GBP 46,269 | GBP 84,093 |
| 24 | GBP 18,835 | GBP 27,152 | GBP 36,634 | GBP 51,471 | GBP 96,892 |
| 25 | GBP 20,051 | GBP 29,257 | GBP 39,672 | GBP 56,565 | GBP 109,177 |

## Annual Dividend Income Withdrawn (Years 26-30, Post-Accumulation)

*Income represents 60% of net dividends withdrawn*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 12,772 | GBP 18,679 | GBP 25,416 | GBP 36,535 | GBP 71,444 |
| 27 | GBP 13,515 | GBP 19,854 | GBP 27,152 | GBP 39,288 | GBP 78,386 |
| 28 | GBP 14,252 | GBP 21,023 | GBP 28,957 | GBP 42,317 | GBP 86,087 |
| 29 | GBP 15,112 | GBP 22,422 | GBP 30,971 | GBP 45,298 | GBP 93,898 |
| 30 | GBP 15,894 | GBP 23,943 | GBP 32,948 | GBP 48,821 | GBP 103,381 |

## Total Annual Dividends (Years 26-30)

*Total dividends before 60/40 split*

| Year | 5th %ile | 25th %ile | Median | 75th %ile | 95th %ile |
|------|----------|-----------|--------|-----------|-----------|
| 26 | GBP 21,287 | GBP 31,132 | GBP 42,360 | GBP 60,892 | GBP 119,074 |
| 27 | GBP 22,525 | GBP 33,091 | GBP 45,254 | GBP 65,480 | GBP 130,643 |
| 28 | GBP 23,754 | GBP 35,039 | GBP 48,261 | GBP 70,529 | GBP 143,479 |
| 29 | GBP 25,187 | GBP 37,371 | GBP 51,619 | GBP 75,496 | GBP 156,496 |
| 30 | GBP 26,490 | GBP 39,905 | GBP 54,914 | GBP 81,368 | GBP 172,302 |

## Income Growth (Years 26-30)

- **Median CAGR**: 6.9%
- **5th percentile CAGR**: 3.4%
- **95th percentile CAGR**: 11.5%

## Scenario Analysis

### Best Case Path (95th percentile NAV)
- **Final NAV (Year 30)**: GBP 71,862,725
- **Year 30 Total Dividends**: GBP 73,218,603
- **Year 30 Income Withdrawn**: GBP 43,931,162

### Median Case Path
- **Final NAV (Year 30)**: GBP 2,327,381
- **Year 30 Total Dividends**: GBP 221,058
- **Year 30 Income Withdrawn**: GBP 132,635

### Worst Case Path (5th percentile NAV)
- **Final NAV (Year 30)**: GBP 470,302
- **Year 30 Total Dividends**: GBP 66,815
- **Year 30 Income Withdrawn**: GBP 40,089

## Model Notes (Revised)

This simulation uses a **realistic dividend growth model**:

1. **NAV Growth**: 5% real annual return (conservative)
2. **Dividend Growth**: Modelled as excess growth above NAV growth
   - Historical 5-year dividend growth already includes underlying earnings growth
   - Only the 'excess' portion (dividend growth minus NAV growth) is applied additionally
   - This prevents double-counting of growth
3. **Growth Decay**: High excess growth rates decay toward sustainable levels over time
4. **Dividend Calculation**: `dividend = units x base_dividend x excess_growth_factor`
   - Base dividend fixed at start (initial_price x yield)
   - Growth in units (via reinvestment) captures NAV appreciation
   - Excess growth factor captures yield expansion

---

*Report generated using Monte Carlo simulation based on SDG portfolio specifications.*
*All values in GBP real terms (inflation-adjusted).*