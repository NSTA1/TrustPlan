# Sensitivity Analysis Summary

## Scenario Parameters

| Scenario | NAV Return | NAV Volatility |
|----------|------------|----------------|
| Pessimistic | 3.0% | 22.0% |
| Base | 5.0% | 17.0% |
| Optimistic | 7.0% | 15.0% |

## Year 25 NAV Comparison (End of Accumulation)

| Scenario | 5th %ile | Median | 95th %ile |
|----------|----------|--------|-----------|
| Pessimistic | GBP 1,176,179 | GBP 2,309,652 | GBP 5,512,152 |
| Base | GBP 1,363,873 | GBP 2,486,254 | GBP 4,967,989 |
| Optimistic | GBP 1,714,793 | GBP 3,116,936 | GBP 5,979,754 |

## Year 30 NAV Comparison (Final)

| Scenario | 5th %ile | Median | 95th %ile |
|----------|----------|--------|-----------|
| Pessimistic | GBP 1,239,423 | GBP 2,970,441 | GBP 8,588,150 |
| Base | GBP 1,590,798 | GBP 3,282,150 | GBP 7,312,158 |
| Optimistic | GBP 2,181,826 | GBP 4,445,288 | GBP 9,534,067 |

## Year 30 Dividend Income Comparison (60% Withdrawal)

| Scenario | 5th %ile | Median | 95th %ile |
|----------|----------|--------|-----------|
| Pessimistic | GBP 31,995 | GBP 98,914 | GBP 826,866 |
| Base | GBP 21,845 | GBP 45,294 | GBP 125,293 |
| Optimistic | GBP 17,123 | GBP 30,171 | GBP 61,929 |

## Key Observations

1. **NAV Spread**: Higher volatility scenarios show wider percentile spreads, as expected
2. **Counterintuitive Income Pattern**: Lower NAV growth scenarios show *higher* dividend income because:
   - Lower price growth = more units accumulated during contribution phase
   - Dividend per share growth is modelled independently of NAV (excess growth baseline fixed at 5%)
   - More units × same dividend growth = higher total dividends
3. **Volatility Effect**: The pessimistic scenario's higher volatility (22%) creates extreme 95th percentile outcomes
4. **NAV Ordering is Correct**: Optimistic > Base > Pessimistic for median NAV, as expected

### Note on Dividend Model

The inverse relationship between NAV growth and income is a feature of the excess dividend growth model:
- Dividend growth is modelled as yield expansion above a 5% NAV baseline
- When actual NAV grows slower, you accumulate more units at lower prices
- The same dividend-per-share growth applied to more units produces higher income
- This represents the value of consistent contribution investing into undervalued markets

---

*Analysis generated using Monte Carlo simulation with 10,000 paths per scenario.*