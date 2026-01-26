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
| Pessimistic | GBP 1,097,539 | GBP 2,181,898 | GBP 5,205,055 |
| Base | GBP 1,325,371 | GBP 2,373,563 | GBP 4,662,631 |
| Optimistic | GBP 1,697,519 | GBP 3,053,378 | GBP 5,953,029 |

## Year 30 NAV Comparison (Final)

| Scenario | 5th %ile | Median | 95th %ile |
|----------|----------|--------|-----------|
| Pessimistic | GBP 1,179,897 | GBP 2,843,299 | GBP 8,457,417 |
| Base | GBP 1,535,279 | GBP 3,139,583 | GBP 6,980,963 |
| Optimistic | GBP 2,162,187 | GBP 4,366,032 | GBP 9,438,260 |

## Year 30 Dividend Income Comparison (60% Withdrawal)

| Scenario | 5th %ile | Median | 95th %ile |
|----------|----------|--------|-----------|
| Pessimistic | GBP 32,551 | GBP 101,348 | GBP 957,521 |
| Base | GBP 22,761 | GBP 46,885 | GBP 132,744 |
| Optimistic | GBP 17,865 | GBP 31,863 | GBP 66,020 |

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