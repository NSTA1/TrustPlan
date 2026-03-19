# Portfolio Allocation Change Procedure

When the user requests an allocation change (adding, removing, or reweighting assets), apply **all** of the following steps in order. Do not skip any step.

## Trigger

Any instruction that changes the portfolio composition, such as:
- Adding a new holding
- Removing an existing holding
- Changing an asset's allocation percentage
- Replacing one asset with another

## Data Retrieval

- Always use `curl.exe` with a browser User-Agent header for HTTP requests:
  ```
  curl.exe -s -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
  ```
- Yahoo Finance dividend history (v8 chart API):
  ```
  https://query1.finance.yahoo.com/v8/finance/chart/{TICKER}?range=10y&interval=3mo&events=div
  ```
- Yahoo Finance price data:
  ```
  https://query1.finance.yahoo.com/v8/finance/chart/{TICKER}?range=5d&interval=1d
  ```
- finviz (US-listed stocks, payout ratios):
  ```
  https://finviz.com/quote.ashx?t={TICKER}
  ```

For any new asset, fetch and calculate:
1. **Forward yield**: forward annual dividend ÷ current price
2. **5-year dividend growth CAGR**: from dividend history
3. **Withholding tax rate**: based on country of domicile (US 15%, UK 0%, FR 25%, NL 15%, DK 27%, JP 15%, CA 25%, DE 26%)
4. **Payment months**: from dividend payment dates
5. **ADR status**: if trading on OTC markets

## Step-by-Step Changes Required

### 1. `sdg.md` — Asset Allocations table
- Add/remove/update the asset row
- Verify allocations still sum to 100%
- Keep table sorted by allocation descending, then alphabetically within equal allocations

### 2. `sdg.md` — Asset Sleeves table
- Update the relevant sleeve's asset list and weight
- All sleeve weights must sum to 100%
- If a new sleeve is needed, add it; if a sleeve becomes empty, remove it

### 3. `sdg.md` — Forward Yield table
- Add/remove/update the asset row with: Country, Withholding Tax, Forward Yield, Effective Yield After Withholding
- Effective Yield = Forward Yield × (1 − Withholding Tax)
- Recalculate and update the blended forward yield (gross): `Σ(allocation × forward_yield)`

### 4. `sdg.md` — 5-Year Dividend Growth table
- Add/remove/update the asset row
- Recalculate and update the blended dividend growth: `Σ(allocation × growth_rate)`

### 5. `sdg.md` — Portfolio-Weighted Fundamentals table
- Recalculate and update:
  - Forward Yield (after withholding): `Σ(allocation × effective_yield)`
  - Dividend Growth (5-yr): `Σ(allocation × growth_rate)`
- Review whether ROIC, Payout Ratio, and Expected Return ranges still hold; update if clearly outside range

### 6. `modelling.md` — Payment Schedule (§2.1)
- Add/remove/update the asset row with payment frequency and months
- Keep table alphabetically sorted

### 7. `modelling.md` — Asset Identifiers (§9.4.2)
- Add/remove/update the asset row with: Ticker, Exchange, Currency, Notes (ADR if applicable)
- Keep table alphabetically sorted

### 8. `modelling.md` — ADR references (§9.4.2 notes, §9.4.3)
- If adding/removing an ADR, update the ADR Notes, ADR Ratio Verification, and ADR Fee sections
- Only ADR holdings should appear in these sections

### 9. `modelling.md` — §9.4.7 Rationale
- Update the portfolio dividend growth figure cited in the rationale text

### 10. `simulation/assets.py`
- Add/remove/update the asset in the `assets_data` list
- Parameters: name, ticker, allocation, forward_yield, withholding_tax, dividend_growth_5yr, payment_frequency, payment_months, is_adr, dividend_resilience
- Update sleeve comments (names and weights)
- Update expected metrics in `verify_portfolio_metrics()`: `expected_yield_net`, `expected_yield_gross`, `expected_growth`
- Update the docstring yield reference

### 11. `simulation/correlation.py` — **Sole source of correlation data**
- `correlation.py` is the **authoritative and only** location for the dividend growth correlation matrix
- There is no correlation matrix in `sdg.md` — do not add one
- When adding a new asset: add its ticker to the `tickers` list and add all pairwise correlations to the `correlations` dict
- When removing an asset: remove its ticker from the `tickers` list and remove all correlation entries referencing it
- Estimate correlations for new assets based on sector, geography, and business model similarity to existing holdings
- After changes, verify the matrix is:
  - Correct size (n×n where n = number of assets)
  - Symmetric
  - Positive semi-definite (minimum eigenvalue ≥ 0)

### 12. Verification
- Run `verify_portfolio_metrics()` from `simulation/assets.py` and confirm no warnings
- Run a small Monte Carlo simulation (5 paths) to confirm no runtime errors
- Check that no stale references to removed assets remain in any modified file

## Correlation Estimation Guidelines

When estimating correlations for a new asset, use these ranges:
- **Same sector, same geography**: 0.45–0.55
- **Same sector, different geography**: 0.30–0.40
- **Related sectors** (e.g., tech/data, luxury/consumer): 0.25–0.35
- **Unrelated sectors** (e.g., defence/healthcare): 0.15–0.25
- **Small-cap / niche vs large-cap**: reduce by 0.05–0.10
- Default for unspecified pairs: 0.25 (set in `correlation.py`)

## Dividend Resilience Guidelines

When setting `dividend_resilience` for a new asset:
- **0.90+**: Dividend aristocrats, 25+ years of consecutive increases
- **0.80–0.89**: Strong dividend growers with consistent history
- **0.70–0.79**: Good dividend history but some variability or cyclicality
- **0.60–0.69**: Moderate stability, may cut in severe downturns
- **0.50–0.59**: Higher risk of cuts during stress (banks, cyclicals)
