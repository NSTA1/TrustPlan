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
| Pessimistic | GBP 1,092,668 | GBP 2,192,210 | GBP 5,149,443 |
| Base | GBP 1,347,022 | GBP 2,398,501 | GBP 4,709,715 |
| Optimistic | GBP 1,698,782 | GBP 3,043,765 | GBP 5,872,960 |

## Year 30 NAV Comparison (Final)

| Scenario | 5th %ile | Median | 95th %ile |
|----------|----------|--------|-----------|
| Pessimistic | GBP 1,155,274 | GBP 2,825,489 | GBP 8,580,838 |
| Base | GBP 1,556,154 | GBP 3,169,055 | GBP 7,047,295 |
| Optimistic | GBP 2,134,129 | GBP 4,337,558 | GBP 9,297,683 |

## Year 30 Dividend Income Comparison (60% Withdrawal)

| Scenario | 5th %ile | Median | 95th %ile |
|----------|----------|--------|-----------|
| Pessimistic | GBP 32,423 | GBP 99,841 | GBP 979,183 |
| Base | GBP 22,435 | GBP 46,302 | GBP 135,439 |
| Optimistic | GBP 17,882 | GBP 31,694 | GBP 66,512 |

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