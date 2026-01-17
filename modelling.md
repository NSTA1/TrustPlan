# Additional Portfolio Modelling Information

*This section provides the additional assumptions required to run approximate long‑horizon Monte Carlo simulations of portfolio‑level dividend income. These assumptions are intended solely for modelling convenience and internal scenario analysis. They do not alter the investment mandate, portfolio construction rules, or operational instructions defined elsewhere in the SDG documentation.*

## 1. Dividend Growth Modelling

### 1.1 Correlation Matrix
- The **Dividend Correlation** table in the main SDG document is defined as the **dividend‑growth correlation matrix** for all assets.
- These correlations apply exclusively to **annual dividend‑growth shocks**.

### 1.2 Dividend Growth Volatility
- All assets use a **uniform annual dividend‑growth volatility of 5%**, applied to the 5‑year average dividend‑growth rates listed in the main document.
- Annual dividend‑growth shocks follow a **lognormal distribution**.

### 1.3 Zero‑Dividend Assets
- Assets with zero forward yield are assumed to:
  - Never initiate a dividend.
  - Grow NAV normally.
  - Influence income only indirectly through rebalancing flows.

## 2. Dividend Payment Mechanics

### 2.1 Payment Schedule

Each asset pays dividends according to its historical payment schedule. Dividends are reinvested immediately upon receipt.

| Asset                        | Frequency   | Payment Months              |
|------------------------------|-------------|------------------------------|
| Accenture                    | Quarterly   | Feb, May, Aug, Nov           |
| ADP                          | Quarterly   | Jan, Apr, Jul, Oct           |
| ASML                         | Semi-Annual | May, Nov                     |
| BAE Systems                  | Semi-Annual | Jun, Dec                     |
| Canadian National Railway    | Quarterly   | Mar, Jun, Sep, Dec           |
| Chubb                        | Quarterly   | Jan, Apr, Jul, Oct           |
| Coloplast                    | Annual      | Dec                          |
| Essex Property Trust         | Quarterly   | Jan, Apr, Jul, Oct           |
| EssilorLuxottica             | Annual      | May                          |
| Hermès International         | Annual      | May                          |
| Hoya                         | Semi-Annual | Jun, Dec                     |
| Japan Exchange               | Semi-Annual | Jun, Dec                     |
| JP Morgan                    | Quarterly   | Jan, Apr, Jul, Oct           |
| L'Oréal                      | Annual      | May                          |
| Lockheed Martin              | Quarterly   | Mar, Jun, Sep, Dec           |
| London Stock Exchange Group  | Semi-Annual | May, Sep                     |
| LVMH                         | Semi-Annual | Apr, Dec                     |
| Mastercard                   | Quarterly   | Feb, May, Aug, Nov           |
| Microsoft                    | Quarterly   | Mar, Jun, Sep, Dec           |
| Novo Nordisk                 | Annual      | Mar                          |
| RELX                         | Semi-Annual | Jun, Sep                     |
| S&P Global                   | Quarterly   | Mar, Jun, Sep, Dec           |
| SMFG                         | Semi-Annual | Jun, Dec                     |
| Stryker                      | Quarterly   | Jan, Apr, Jul, Oct           |
| Waste Management             | Quarterly   | Mar, Jun, Sep, Dec           |
| Wolters Kluwer               | Semi-Annual | May, Sep                     |

### 2.2 Reinvestment Timing
- Dividends are **reinvested immediately upon receipt** in the month they are paid.
- Each dividend is allocated in a **self-balancing fashion** to bring the portfolio closer to target weights.
- During the accumulation phase (Years 0–25), **100% of dividends** are reinvested.
- During the post-accumulation phase (Years 26–30), **40% of dividends** are reinvested and **60%** are withdrawn as income.

### 2.3 Modelling Simplification
- For simulation purposes, monthly time steps are used to capture dividend timing accurately.
- Annual dividend growth shocks are applied at the start of each calendar year.
- Each payment is calculated as:
  - **Annual dividend ÷ number of payments per year** (adjusted for growth)

## 3. NAV Return Modelling

### 3.1 Return Distribution
- Annual NAV returns follow a **lognormal distribution**.
- Real NAV growth assumptions:
  - Mean: **7%** (midpoint of the 6–8% range).
  - Volatility: **20%**.
- For monthly simulation, annual returns are converted to monthly returns:
  - Monthly mean: **0.565%** (≈ 7% ÷ 12)
  - Monthly volatility: **5.77%** (≈ 20% ÷ √12)

### 3.2 NAV Correlation Structure
- All assets share a **uniform pairwise NAV return correlation of 0.7**.
- This correlation applies only to NAV returns.

### 3.3 Independence of NAV and Dividend Growth
- Annual NAV shocks and annual dividend‑growth shocks are assumed to be **independent**.

## 4. Currency Treatment

### 4.1 Base Currency
- All modelling is performed in **GBP real terms**.

### 4.2 FX Assumptions
- FX volatility and FX correlations are **ignored**.
- All dividends and NAV returns are treated as if already expressed in GBP real terms.

## 5. Tax Treatment

### 5.1 Withholding Tax Stability
- Withholding tax rates listed in the **Forward Yield (2026)** table remain **constant for all 30 years**.
- No additional tax drag applies inside the ISA wrapper during the first 25 years.

## 6. Rebalancing Rules

### 6.1 Accumulation Phase (Years 0–25)
- Annual rebalancing to target weights each January.
- All contributions and dividends are invested in a self-balancing fashion upon receipt.

### 6.2 Post‑Accumulation Phase (Years 26–30)
- Annual rebalancing continues each January.
- 40% of dividends are reinvested in a self-balancing fashion upon receipt.
- 60% of dividends are withdrawn as income in the month received.

## 7. Simulation Structure

### 7.1 Time Step
- **Monthly time steps** for dividend receipt and reinvestment.
- Annual dividend growth shocks applied each January.
- NAV returns modelled monthly (derived from annual parameters).

### 7.2 Number of Trials
- Recommended minimum: **10,000 Monte Carlo paths**.

### 7.3 Output Requirements
- Probability distribution of **annual dividend income** for Years **20–30**, in **GBP real terms**, including:
  - Median income  
  - 5th, 25th, 75th, and 95th percentiles  
  - Worst‑case and best‑case paths  
  - Expected CAGR of income over Years 20‑30

## 8. Sequence‑of‑Returns Rules

### 8.1 Monthly Order of Operations
1. Apply monthly NAV return to all holdings.
2. For each asset with a dividend payment in the current month:
   - Calculate dividend (annual dividend ÷ payment frequency, adjusted for year's growth).
   - Apply withholding tax.
   - Reinvest net dividend immediately in a self-balancing fashion (100% during accumulation, 40% post-accumulation).
3. Apply any contributions scheduled for the month in a self-balancing fashion.
4. In January: apply annual dividend growth shock, perform annual rebalancing to target weights.
