# Downturn Strategy

## 1. Purpose
A mechanical, trustee‑ready downturn deployment protocol designed to enhance long‑term expected returns by allocating a small, convex pool of capital during major global equity drawdowns. This strategy applies to the SDG Portfolio and is intended to operate without discretion, emotion, or subjective judgement.

---

## 2. Downturn Fund
- **Target Size:** £15,000 initially - grows over time according to [these rules](DownturnFundAllocation.md).
- **Cash Yield Assumption:** 3% real  
- **Portfolio Real Return Assumption:** 10%  
- **Location:** Held in cash or an instant‑access savings vehicle  
- **Usage:** Only deployed according to the rules below; never used for rebalancing or contributions

---

## 3. Benchmark for Measuring Drawdowns

### **Formal Benchmark**
**FTSE All‑World Net Total Return Index (GBP)**  
This is the official benchmark for defining downturns.

### **Operational Proxy**
**VWRP — Vanguard FTSE All‑World UCITS ETF (GBP‑listed)**  
VWRP may be used for daily monitoring because:
- It tracks the same underlying FTSE All‑World universe  
- It is priced daily in GBP  
- Its drawdowns closely mirror the Net TR benchmark  

**If the formal benchmark and VWRP diverge, the formal benchmark takes precedence.**

---

## 4. Definition of Peak and Drawdown
- **Peak Value:** The highest *daily closing price* ever recorded for the benchmark index  
- **Current Value:** The latest *daily closing price*  
- **Drawdown Formula:**

\[
\text{Drawdown} = \frac{\text{Peak Value} - \text{Current Value}}{\text{Peak Value}}
\]

- **Measurement Frequency:** Daily closing prices only  
- **Trigger Confirmation:** A single daily close at or below the threshold is sufficient (no smoothing, no multi‑day confirmation)

---

## 5. Deployment Tranches

### **Tranche A**
- **Size:** 20% of downturn fund
- **Trigger:** Index down **10%** from peak  
- **Deployment Timing:** Within 5 trading days  

### **Tranche B**
- **Size:** 40% of downturn fund
- **Trigger:** Index down **20%** from peak  
- **Deployment Timing:** Within 5 trading days  

### **Tranche C**
- **Size:** 40% of downturn fund
- **Trigger:** Index down **30%** from peak  
- **Deployment Timing:** Within 5 trading days  

---

## 6. Deployment Method (Self‑Balancing)
Downturn deployments follow the same self‑balancing rules as contributions and dividends:

- All deployed capital is invested **pro‑rata to target weights**  
- No discretionary tilting toward “cheap” assets  
- No overriding of the annual rebalance  
- Deployed capital is treated as a normal contribution for rebalancing purposes  

This preserves the portfolio’s intended structure and maintains long‑term compounding integrity.

---

## 7. Rebuild Rules (Clarified)

### **7.1 When Rebuilding Begins**
Rebuilding begins **immediately after the final tranche deployed in that downturn event**, whether that is:
- Only Tranche A  
- Tranche A + B  
- Tranche A + B + C  

There is **no requirement** for all three tranches to deploy before rebuilding starts.

### **7.2 Rebuilding Cashflow**
- Rebuild at **3-4% of target per month** until the downturn fund reaches the target again  
- Rebuilding **does not reduce or replace** ISA contributions during the contribution period
- Rebuilding is a **separate, parallel cashflow**  
- Cash yield during rebuild remains part of the fund

### **7.3 No New Deployments During Rebuild**
Once rebuilding has begun:
- **No new downturn deployments** may occur  
- Even if a new 10% drawdown happens  
- The system remains “locked” until the fund is fully rebuilt  

This ensures:
- One downturn → one sequence of tranches  
- Then a full rebuild  
- Then the next downturn event

---

## 8. Interaction with Portfolio Rules
- Annual January rebalancing continues as normal  
- All dividends remain reinvested during the accumulation phase  
- Downturn deployments do **not** override rebalancing rules  
- No selling of assets is permitted except for annual rebalancing

---

## 9. Trustee Execution Summary
A downturn deployment occurs when:

1. The FTSE All‑World Net Total Return Index (GBP) — or its proxy VWRP (GBP) — closes at or below **90%**, **80%**, or **70%** of its most recent all‑time high  
2. The corresponding tranche is deployed within 5 trading days  
3. All deployed capital is allocated **pro‑rata to target weights**  
4. After the **last** deployed tranche in that downturn, the fund begins rebuilding at £500/month  
5. **No further downturn deployments** may occur until the fund is fully rebuilt to £15,000  

This system is fully mechanical, requiring no judgement or forecasting.
