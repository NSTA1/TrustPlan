# Additional Portfolio Modelling Information

*This section provides the additional assumptions required to run approximate long‑horizon Monte Carlo simulations of portfolio‑level dividend income. These assumptions are intended solely for modelling convenience and internal scenario analysis. They do not alter the investment mandate, portfolio construction rules, or operational instructions defined elsewhere in the SDG documentation.*

## 1. Dividend Growth Modelling

### 1.1 Correlation Matrix
- The **Dividend Correlation** table in the main SDG document is defined as the **dividend‑growth correlation matrix** for all assets.
- These correlations apply exclusively to **annual dividend‑growth shocks**.

### 1.2 Dividend Growth Volatility
- All assets use a **uniform annual dividend‑growth volatility of 5%**, applied to the 5‑year average dividend‑growth rates listed in the main document.
- Annual dividend‑growth shocks follow a **lognormal distribution**.

### 1.3 Dividend Growth Interpretation
- **Dividend growth represents the increase in dividend per share**, independent of NAV appreciation.
- The 5-year average dividend growth rates reflect historical DPS growth, which typically **includes** underlying earnings/NAV growth.
- To avoid double-counting, the simulation uses **excess dividend growth** = dividend growth rate - NAV growth rate (floored at 0).
- This represents the portion of dividend growth attributable to payout ratio expansion or yield enhancement.

### 1.4 Zero‑Dividend Assets
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
  - Mean: **5%** (conservative estimate for real total return less dividends).
  - Volatility: **18%** (slightly reduced from 20% to reflect quality portfolio).
- For monthly simulation, annual returns are converted to monthly returns:
  - Monthly mean: **0.417%** (≈ 5% ÷ 12)
  - Monthly volatility: **5.20%** (≈ 18% ÷ √12)

### 3.2 NAV Correlation Structure
- All assets share a **uniform pairwise NAV return correlation of 0.6**.
- This correlation applies only to NAV returns.

### 3.3 Relationship Between NAV and Dividend Growth
- Dividend per share growth is modelled as: **NAV growth + excess dividend growth + shock**
- Where excess dividend growth = max(0, historical_dividend_growth - expected_NAV_growth)
- This ensures dividends grow at least as fast as NAV, with additional growth from yield expansion

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

## 9. Implementation Parameters

This section provides the additional parameters required to implement the simulation.

### 9.1 Simulation Timeline

| Parameter | Value |
|-----------|-------|
| Simulation Start Date | **9th December 2025** |
| Year 0 | December 2025 – December 2026 |
| Accumulation Phase | Years 0–25 (December 2025 – December 2050) |
| Post-Accumulation Phase | Years 26–30 (January 2051 – December 2055) |

### 9.2 Initial Portfolio Value

- **Initial portfolio value**: £0 (no existing holdings)
- The portfolio is funded entirely through the contribution schedule
- First investment: £55,500 lump sum on 9th December 2025

### 9.3 Contribution Schedule

| Phase | Amount | Frequency | Start Date | End Date |
|-------|--------|-----------|------------|----------|
| Lump Sum | £55,500 | One-time | 9th December 2025 | 9th December 2025 |
| Weekly Contributions | £2,300 | Weekly | 16th December 2025 | 30th April 2026 |
| Monthly Contributions | £1,666 | Monthly (1st of month) | 1st May 2026 | 1st April 2051 |

**Note**: Weekly contributions span approximately 20 weeks (£46,000 total). Monthly contributions span 25 years (300 payments, £499,800 total).

### 9.4 Asset Pricing Model

The simulation uses actual asset prices at the simulation start date to calculate initial holdings and dividend amounts.

#### 9.4.1 FX Rates

FX rates as of January 2026 (source: FT Markets Data):

| Currency Pair | Rate |
|---------------|------|
| GBP/USD | **1.3381** |
| GBP/EUR | **1.1534** |
| GBP/JPY | **211.54** |
| GBP/CAD | **1.87** |
| GBP/DKK | **8.60** |

**Note**: Rates should be updated to actual values on the simulation start date (9th December 2025).

#### 9.4.2 Asset Identifiers

The following identifiers should be used to fetch current prices from market data sources:

| Asset                        | Ticker    | Exchange  | Currency | Notes |
|------------------------------|-----------|-----------|----------|-------|
| Accenture                    | ACN       | NYSE      | USD      | |
| ADP                          | ADP       | NASDAQ    | USD      | |
| ASML                         | ASML      | AEX       | EUR      | |
| BAE Systems                  | BA.       | LSE       | GBP      | |
| Canadian National Railway    | CNR       | TSX       | CAD      | |
| Chubb                        | CB        | NYSE      | USD      | |
| Coloplast                    | CLPBY     | OTC       | USD      | ADR |
| Essex Property Trust         | ESS       | NYSE      | USD      | |
| EssilorLuxottica             | EL        | PAR       | EUR      | |
| Hermès International         | RMS       | PAR       | EUR      | |
| Hoya                         | HOCPY     | OTC       | USD      | ADR |
| Japan Exchange               | JPXGY     | OTC       | USD      | ADR |
| JP Morgan                    | JPM       | NYSE      | USD      | |
| L'Oréal                      | OR        | PAR       | EUR      | |
| Lockheed Martin              | LMT       | NYSE      | USD      | |
| London Stock Exchange Group  | LSEG      | LSE       | GBP      | |
| LVMH                         | MC        | PAR       | EUR      | |
| Mastercard                   | MA        | NYSE      | USD      | |
| Microsoft                    | MSFT      | NASDAQ    | USD      | |
| Novo Nordisk                 | NOVC      | XETR      | EUR      | |
| RELX                         | REL       | LSE       | GBP      | |
| S&P Global                   | SPGI      | NYSE      | USD      | |
| SMFG                         | SMFG      | NYSE      | USD      | ADR |
| Stryker                      | SYK       | NYSE      | USD      | |
| Waste Management             | WM        | NYSE      | USD      | |
| Wolters Kluwer               | WKL       | AEX       | EUR      | |

**ADR Notes**:
- ADRs trade in USD regardless of the underlying company's home currency.
- ADR ratios (how many underlying shares each ADR represents) should be verified from the depositary bank (typically BNY Mellon or JPMorgan) before simulation.
- Dividends are paid in USD after conversion from local currency by the depositary bank.
- ADR fees (typically $0.01–0.05 per share per dividend) are deducted from dividend payments.
- Withholding tax is still applied based on the company's country of domicile (as listed in the Forward Yield table).

**ADR Ratio Verification Required**:
Before running the simulation, verify the ADR ratios for:
- Coloplast (CLPBY) - depositary: BNY Mellon
- Hoya (HOCPY) - depositary: BNY Mellon
- Japan Exchange (JPXGY) - depositary: BNY Mellon
- SMFG (SMFG) - depositary: JPMorgan

ADR ratios and pricing can be verified at:
- [Morningstar](https://global.morningstar.com) - search by ticker (e.g., CLPBY, HOCPY, JPXGY, SMFG)
- [adr.com](https://www.adr.com) - BNY Mellon's official ADR portal
- [JPMorgan ADR](https://www.adr.com/DRSearch) - for JPMorgan-sponsored ADRs

#### 9.4.3 ADR Fee Assumption

For simulation purposes, apply an **ADR fee of $0.02 per share per dividend payment** for all ADR holdings:
- Coloplast (CLPBY)
- Hoya (HOCPY)
- Japan Exchange (JPXGY)
- SMFG (SMFG)

This fee is deducted after withholding tax but before reinvestment.

#### 9.4.4 Price Fetching Instructions

At simulation initialisation:

1. **Fetch closing prices** for each asset on the simulation start date (or most recent trading day prior).
2. **Convert to GBP** using the FX rates from Section 9.4.1.
3. **Calculate annual dividend** = GBP Price × Forward Yield (from sdg.md Forward Yield table).
4. **For ADRs**: Deduct estimated ADR fees from dividend calculations (see Section 9.4.3).
5. **Store both local currency and GBP prices** for reference.

#### 9.4.5 Initial Unit Calculation

For the initial £55,500 lump sum investment on 9th December 2025:

1. **Calculate target allocation**: For each asset, target_value = £55,500 × target_weight
2. **Calculate units**: units = target_value ÷ GBP_price
3. **Store fractional units**: The simulation permits fractional unit holdings

**Example** (using hypothetical prices):
- Microsoft closes at $450.00 on 9th December 2025
- GBP price = $450.00 ÷ 1.3381 = £336.30
- Microsoft target: £55,500 × 7% = £3,885
- Microsoft units: £3,885 ÷ £336.30 = 11.55 units
- Annual dividend (gross): £336.30 × 0.75% = £2.52 per unit
- Total annual dividend: 11.55 × £2.52 = £29.11 gross

#### 9.4.6 NAV Growth Application

Unit prices grow according to the NAV return model (Section 3):

```
new_price = previous_price × (1 + monthly_return)
```

Where monthly_return is the correlated lognormal shock for that asset.

#### 9.4.7 Dividend Yield Stability (REVISED)

**Key Principle**: Dividend per share growth is modelled independently of NAV growth to avoid double-counting.

The simulation uses the following approach:

1. **Base dividend per unit** is fixed at simulation start based on initial price × forward yield
2. **Each year**, the base dividend grows by the **excess dividend growth rate** plus a random shock
3. **Excess dividend growth** = max(0, historical_5yr_growth - expected_NAV_growth)
4. This represents yield expansion (dividends growing faster than stock price)

```
dividend_per_unit[year] = base_dividend × cumulative_excess_growth_factor[year]
```

Where:
- base_dividend = initial_price × forward_yield (fixed at start)
- cumulative_excess_growth_factor compounds the excess growth each year

**Rationale**: 
- Historical dividend growth rates (e.g., 11.5% for portfolio) typically include underlying earnings growth
- NAV already captures earnings growth via the 5% real return assumption
- Only the "excess" portion (dividend growth above NAV growth) should be applied additionally
- This prevents the unrealistic scenario of 18%+ annual dividend growth

#### 9.4.8 Dividend Growth Mean Reversion

To reflect that exceptionally high dividend growth rates tend to moderate over time:

- Assets with excess dividend growth > 5% apply a **decay factor of 0.95** per year
- This gradually brings extreme growers toward a sustainable long-term rate
- Minimum excess growth rate is **0%** (dividends grow at least with NAV)
