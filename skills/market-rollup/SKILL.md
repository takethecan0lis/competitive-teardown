---
name: market-rollup
description: Merges several completed competitive teardowns into a market view and finds the user's differentiator and product-market fit, producing a comparison sheet (feature matrix and scores), a one-page differentiator brief, and an optional slide deck. Use when the user says "roll up the teardowns", "compare these competitors", "market map", "where's the gap", "what's our differentiator", or "write the differentiator brief".
---

# Market Roll-up

Combine neutral teardowns into one market view, then, and only then, bring in the user's own product to find the differentiator.

## Objective and benefit

- **Objective:** This skill aims to help you see where a market is crowded and where a differentiator may exist.
- **Benefit:** You get a comparison sheet, a market view, and a one-page brief with options, each traceable to a teardown, and a stated test for the riskiest assumption.
- **Why it is worth having:** One teardown shows one product. Side by side, gaps and crowding become visible, so a differentiator is chosen against evidence and a test, not a hunch.

Adopted, not measured: no result has been measured yet.

## Ask first

Before step 4, ask the user, one at a time:
1. Where do your persona, empathy map and vision files live? No default; the skill reads only the paths you give.
2. What scoring weights should the white-space scoring use? Default: equal weights across the criteria; say so and offer to change them.

## Preconditions
- At least two teardowns at any depth, written to the shared schema (capabilities.csv, gap-scores.csv, competitor-comparison.csv).
- The user has confirmed research is complete for each included teardown.
- The user's own product materials (persona, empathy map, vision) are available. If not, run the market view (steps 1 to 3) and stop before step 4.

## 1. Normalize
Load every teardown's CSVs. Map capabilities to a shared capability list (merge synonyms; keep each source CAP ID). Record each teardown's depth and confidence so a quick scan is not mistaken for a full teardown.

## 2. Build the comparison sheet
Columns: capability or job, category, then one column per competitor with a 0 to 5 score and evidence tag, plus a "best in market" column. Add sheets for pricing and packaging, tone and stance, privacy and safety, platforms, and scale. Make it from the Sheets artifact type when available; otherwise write an .xlsx with the xlsx skill or a CSV. Use `references/comparison-sheet.md`.

## 3. Read the market
Write `rollup/market-view.md`: table stakes (what everyone has), where products differentiate, white space (jobs no one serves well), shared complaint themes, segment gaps (for example by age or accessibility needs), and a positioning map on two axes chosen from the evidence (for example simple to powerful, solo to team). Draw the map as a simple chart or mermaid quadrant.

## 4. Find the differentiator (user's lens enters here)
Read the user's persona, empathy map, and vision. Score the white space against them. Produce 2 to 3 differentiation options, each with: the unmet need, evidence for it, who it serves, why incumbents will not follow quickly, the riskiest assumption, and a test to run. Recommend one, and say what would change the recommendation.

## 5. One-page differentiator brief
Write it for the enterprise product manager using `references/differentiator-brief.md`. Make it from the Docs artifact type when available. One page, plain language, every claim traceable to a teardown ID.

## 6. Optional deck
Only when the user needs to present. Use `references/deck-outline.md`; make it from the Slides artifact type when available, otherwise follow the pptx skill.

## 7. Deliver
Package `rollup/` with the sheet, brief, market view, and deck (if any). Summarize the recommendation in the reply in a few sentences.

## What this does not verify

- That the market is fully covered; it sees only the teardowns you give it, at the depth each was done.
- That a recommended differentiator will work; it proposes a test, and the test is yours to run.
- That scores are comparable across teardowns of different depth; confidence is carried along, and a quick scan is not a full teardown.
