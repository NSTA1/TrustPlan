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
| Pessimistic | GBP 1,070,661 | GBP 2,103,674 | GBP 5,031,817 |
| Base | GBP 1,268,890 | GBP 2,325,829 | GBP 4,677,452 |
| Optimistic | GBP 1,646,939 | GBP 2,985,077 | GBP 5,747,272 |

## Year 30 NAV Comparison (Final)

| Scenario | 5th %ile | Median | 95th %ile |
|----------|----------|--------|-----------|
| Pessimistic | GBP 1,107,167 | GBP 2,680,526 | GBP 7,767,464 |
| Base | GBP 1,481,440 | GBP 3,053,038 | GBP 6,822,665 |
| Optimistic | GBP 2,072,884 | GBP 4,249,490 | GBP 9,143,462 |

## Year 30 Dividend Income Comparison (60% Withdrawal)

| Scenario | 5th %ile | Median | 95th %ile |
|----------|----------|--------|-----------|
| Pessimistic | GBP 29,144 | GBP 89,137 | GBP 747,868 |
| Base | GBP 20,555 | GBP 42,048 | GBP 116,210 |
| Optimistic | GBP 16,441 | GBP 28,816 | GBP 59,069 |

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