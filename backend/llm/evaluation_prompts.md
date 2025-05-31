# LLM Investment Profiling Prompts by Horizon

This document provides input prompts tailored to different investment horizons. Use these to feed user responses into an LLM agent for evaluation and conversion into a consistent risk and behavior profile in JSON format.

---

## Shared JSON Schema

```json
{
  "horizon_category": "6_month | 12_month | 1_3_years | 3_10_years | 10_plus_years",
  "target_amount_eur": null,
  "liquidity_need_rating": 0,
  "risk_capacity_score": 0,
  "risk_tolerance_score": 0,
  "max_drawdown_comfort_pct": null,
  "crypto_max_pct": null,
  "illiquidity_max_pct": null,
  "esg_preference_level": "none | low | moderate | high",
  "decision_style": "execution_only | collaborative | discretionary",
  "behavioural_flags": [],
  "overall_profile": "Capital Preservation | Cautious Balanced | Balanced Growth | Growth | Aggressive",
  "notes": ""
}
```

---

### Grading Guidance

- Map qualitative answers onto 0-100 scales using quartiles.
- “Any drop worries me” ⇒ liquidity_need_rating ≥ 90, risk_tolerance_score ≤ 20.
- Checking account daily ⇒ behavioural_flags += “overtrading”.
- Convert fee/drawdown choices directly into `max_drawdown_comfort_pct`.
- If a question is missing, leave the related field `null` and explain in `notes`.

---

## 1. 6-Month Horizon

```
SYSTEM / TOOL
You are an investment-profiling analyst. Use the “Shared JSON schema”.

TASK
Evaluate the following answers from a client who needs money in **6 months**.

INPUT
```json
{QUESTIONS_AND_ANSWERS_ARRAY}
```

OUTPUT
Return exactly one JSON object matching the schema.
• `horizon_category` must be `"6_month"`.
• Treat any willingness to accept >2 % drop as above-average risk tolerance for this horizon.
• `illiquidity_max_pct` should default to 0 (six-month money must stay liquid).
• Highlight panic-selling tendencies in `behavioural_flags`.
No extra text.
```

---

## 2. 12-Month Horizon

```
SYSTEM / TOOL
[same preamble]

TASK
Evaluate the client answers for a **12-month** goal.

INPUT
```json
{QUESTIONS_AND_ANSWERS_ARRAY}
```

OUTPUT
JSON only.
• `horizon_category`: `"12_month"`.
• If client allows up to 5 % loss, set `max_drawdown_comfort_pct` = 5, etc.
• `illiquidity_max_pct`: ≤10 % only if the client is “very comfortable” locking funds for a year.
• Apply the grading rules; flag high inflation concern as `behavioural_flags += "inflation_sensitive"`.
```

---

## 3. 1–3 Year Horizon

```
SYSTEM / TOOL
[same preamble]

TASK
Profile a client saving for **1-3 years**.

INPUT
```json
{QUESTIONS_AND_ANSWERS_ARRAY}
```

OUTPUT
JSON only.
• `horizon_category`: `"1_3_years"`.
• Use their “Grow it a bit / Grow it a lot” choice to tilt `risk_capacity_score` and `risk_tolerance_score`.
• Derive `crypto_max_pct` from the direct crypto question; if “None”, set 0.
• Frequent checking **and** willingness to sell after a 10 % drop ⇒ `behavioural_flags` include `"loss_aversion_high"` and `"overtrading"`.
• Populate all other fields per schema.
```

---

## 4. 3–10 Year Horizon

```
SYSTEM / TOOL
[same preamble]

TASK
Analyse answers for a **3-10 year** plan.

INPUT
```json
{QUESTIONS_AND_ANSWERS_ARRAY}
```

OUTPUT
JSON only.
• `horizon_category`: `"3_10_years"`.
• Map 20 % volatility comfort to higher `risk_tolerance_score`.
• Set `illiquidity_max_pct` from their “things you can’t sell quickly” answer.
• If they tend to “Sell right away” on bad news, add `"panic_sell_bias"` to `behavioural_flags`.
• Follow the master grading guidance.
```

---

## 5. 10+ Year Horizon

```
SYSTEM / TOOL
[same preamble]

TASK
Evaluate a **10 + year** investor profile.

INPUT
```json
{QUESTIONS_AND_ANSWERS_ARRAY}
```

OUTPUT
JSON only.
• `horizon_category`: `"10_plus_years"`.
• High comfort with 30 % draw-down ⇒ risk_tolerance_score ≥ 70.
• Use their “lock money 5–10 yrs” answer for `illiquidity_max_pct`.
• Crypto ceiling maps directly to `crypto_max_pct`.
• If “I’d see it as a chance to buy more” on a 35 % crash, add `"contrarian"` flag.
• Conform strictly to the schema—no commentary.
```
