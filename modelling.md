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

### 2.1 Payment Frequency
- All dividends are modelled as **annual payments** occurring at year‑end.

### 2.2 Reinvestment Timing
- During the accumulation phase (until the end of Year 25), dividends are:
  - Paid at year‑end.
  - Reinvested immediately at year‑end using target weights.

## 3. NAV Return Modelling

### 3.1 Return Distribution
- Annual NAV returns follow a **lognormal distribution**.
- Real NAV growth assumptions:
  - Mean: **7%** (midpoint of the 6–8% range).
  - Volatility: **20%**.

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
- All contributions and dividends are invested using target weights.

### 6.2 Post‑Accumulation Phase (Years 26–30)
- Annual rebalancing continues each January.
- 40% of dividends are reinvested using target weights.
- 60% of dividends are withdrawn as income.

## 7. Simulation Structure

### 7.1 Time Step
- Annual time steps for both NAV and dividend modelling.

### 7.2 Number of Trials
- Recommended minimum: **10,000 Monte Carlo paths**.

### 7.3 Output Requirements
- Probability distribution of **annual dividend income** for Years **20–30**, in **GBP real terms**, including:
  - Median income  
  - 5th, 25th, 75th, and 95th percentiles  
  - Worst‑case and best‑case paths  
  - Expected CAGR of income over Years 20–30

## 8. Sequence‑of‑Returns Rules

### 8.1 Annual Order of Operations
1. Apply NAV return.  
2. Apply dividend growth to previous year's dividend.  
3. Pay dividends at year‑end.  
4. Reinvest dividends (100% until Year 25; 40% thereafter).  
5. Apply contributions (until April 2026 weekly, then monthly until Year 25).  
6. Rebalance annually in January.
