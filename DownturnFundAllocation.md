# Downturn Fund Allocation

## Purpose
The Downturn Fund is a permanent, multi‑generational resilience mechanism designed to:
- provide dry powder for −10%, −20%, and −30% market drawdowns  
- increase long‑run share count through convex deployment  
- reduce sequence‑of‑returns risk across successive stewards  
- preserve operational clarity and mechanical execution  

The Downturn Fund is **not** part of the strategic asset allocation and must never be used for lifestyle spending, discretionary timing, or rebalancing.

---

## 1. Funding Structure

### 1.1 Initial Allocation
- Establish the Downturn Fund at **£15,000 (real, 2025 GBP)** at inception.

### 1.2 Ten‑Year Ramp‑Up Rule
For the first ten years after inception:
- Increase the Downturn Fund target by **£1,000 per year (real terms)**.
- These increases are additive and cumulative.
- Example:  
  - Year 1 target: £16,000  
  - Year 2 target: £17,000  
  - …  
  - Year 10 target: £25,000  

This ramp‑up ensures meaningful convexity during the highest‑impact compounding years.

---

## 2. Multi‑Generational Scaling Rule (Post‑Ramp)

After Year 10, the Downturn Fund target is determined mechanically as:

> **Downturn Fund Target = max( Real Floor , Percentage of NAV )**

Where:

### 2.1 Real Floor
- The real floor is the inflation‑linked value of **£15,000 (2025 GBP)**.
- This ensures the fund never becomes trivial in real terms.

### 2.2 Percentage of NAV
- Target percentage = **1.5% of total portfolio NAV** (real).
- This ensures the fund scales appropriately as the portfolio grows across generations.

### 2.3 Final Target
- Each year, compute both values and select the larger:
  - **Real Floor**  
  - **1.5% of NAV**

This rule ensures:
- the fund remains small relative to total capital  
- convexity remains meaningful even at multi‑million‑pound scale  
- drag remains minimal  
- the system remains simple and trustee‑ready  

---

## 3. Trustee Notes

- The Downturn Fund is a **permanent structural feature** of the portfolio’s resilience architecture.  
- The ramp‑up ensures early convexity; the scaling rule ensures multi‑generational relevance.  
- The fund must remain segregated, explicit, and mechanically governed.  
- **These rules are immutable. No steward, trustee, or successor may alter, reinterpret, override, or amend them under any circumstances. The Downturn Fund Allocation is a fixed and permanent component of the Strategy Document.**

  ---

# Downturn Fund Funding

## 1. Funding Sources

### 1.1 Ramp‑Up Period (Years 1–10)

During the ten‑year ramp‑up period defined in the Downturn Fund Allocation section:

- The Downturn Fund target increases by **£1,000 per year (real terms)**.
- These increases are funded from **dedicated contributions**, not from dividends.
- The ramp‑up establishes the permanent minimum convexity capacity for all future stewards.

**Real‑terms formula (Unicode):**

Let  
• DF₀ = £15,000 (real, 2025)  
• t = year number (1–10)

Then:  
**DFᵣₑₐₗ(t) = DF₀ + 1,000 × t**

Nominal target:  
**DFₙₒₘ(t) = DFᵣₑₐₗ(t) × (1 + π)ᵗ**  
where π = annual inflation rate.

---

### 1.2 Post‑Ramp Period (Year 11 Onward)

After Year 10, the Downturn Fund target is determined mechanically each year by a **monotonic, non‑decreasing rule**.

**Definitions (Unicode):**

• NAVₜ = nominal portfolio NAV in year t  
• π = inflation rate  
• DF_floor_real = £15,000 (2025 real floor)  
• DF_floorₜ = DF_floor_real × (1 + π)ᵗ  
• DF_NAVₜ = 0.015 × NAVₜ  
• DFₜ₋₁ = previous year’s nominal target

**Monotonic target rule:**

**DFₜ = max( DFₜ₋₁ , DF_floorₜ , DF_NAVₜ )**

This ensures:

- The target **never decreases**.  
- The target always keeps pace with inflation.  
- The target scales with NAV once 1.5% of NAV exceeds the floor and ramp‑up level.

From Year 11 onward:

- The Downturn Fund is funded **exclusively from dividends**.  
- No external contributions, reallocations, or sales may be used.

---

## 2. Funding Priority

### 2.1 Priority Over Reinvestment

Dividend flows must be allocated in the following strict order:

1. **First:**  
   Allocate dividends to bring the Downturn Fund up to its required target DFₜ.  
   This applies whenever:
   - DF_floorₜ increases due to inflation,  
   - DF_NAVₜ increases due to NAV growth, or  
   - the fund is being replenished after deployment.

2. **Second:**  
   Only after DF_balanceₜ = DFₜ may any remaining dividends be reinvested.

This preserves the Downturn Fund’s resilience function across generations.

---

## 3. Insufficient Dividends

If dividends in a given year are insufficient to reach DFₜ:

- The fund remains temporarily below target.  
- All future dividends are allocated **entirely** to the Downturn Fund until DF_balanceₜ = DFₜ.  
- No dividend reinvestment may occur until the target is fully restored.  
- DFₜ itself **never decreases**.

---

## 4. Trustee Notes

- The Downturn Fund must remain fully funded at its target level whenever possible.  
- Funding from dividends ensures the mechanism is self‑sustaining across generations.  
- Prioritising the Downturn Fund over reinvestment preserves its role as a permanent convexity and resilience buffer.  
- These funding rules are **immutable** and must be executed exactly as written.
