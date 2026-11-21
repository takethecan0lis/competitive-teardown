---
name: teardown
description: Runs an evidence-based competitive teardown of an app, website, or desktop software and builds a neutral knowledge base plus a short summary doc. Use when the user says "tear down", "teardown", "analyze this competitor", "research this app", "competitive analysis of", "spider this product", "document everything about", or names a product to study for market research. Supports quick, standard (default), and full depth.
---

# Competitive Teardown (orchestrator)

Run a teardown of one product. Produce a neutral, evidence-tagged knowledge base that an agentic product team can build from, plus a short summary doc for humans. Keep the user's own product out of the evidence entirely until research is confirmed complete.

## Objective and benefit

- **Objective:** This skill aims to give a product team a neutral, evidence-tagged picture of one competitor, with every claim tied to a source and a confidence level.
- **Benefit:** The team can see what was observed, what the company states, what others report and what is only inferred, so each claim can be checked before anyone acts on it.
- **Why it is worth having:** Product decisions then rest on what was seen and sourced, not on memory or opinion, and the open questions are written down instead of guessed.

Adopted, not measured: no result has been measured yet.

Read `references/conventions.md` before writing any file. Read the other references when the step that needs them begins.

## Operating rules

- **Neutral first.** Describe the product on its own terms. Never compare it to the user's product, persona, or idea during research. The user's lens enters only in the separate implications file (Step 8) after the user confirms research is done.
- **Evidence or it did not happen.** Tag every claim OBSERVED, DOCUMENTED, REPORTED, or INFERRED with High, Medium, or Low confidence and a source. Surface contradictions as findings. Label weak data as weak.
- **Unknowns become open questions** with an ID, a method to resolve, and an owner. Never fill gaps with guesses.
- **Pause only for real decisions.** Ask when a choice is the user's, when a handoff is needed, or when scope is ambiguous and expensive. Otherwise keep working and keep the task list current.
- **Ship increments.** After each phase, rebuild the package, bump the changelog, and deliver it. The user should always hold a usable copy.
- **Context lives on disk.** Write findings to the knowledge base as you go so the work survives context compaction.
- **Safety protocol always applies** during exploration. See the product-explorer skill.

## Step 0: Charter (always first)

Ask, in one AskUserQuestion round, only what is not already known:
1. Product name, platform(s), and how to access it (URL, App Store link, installed desktop app, account or trial).
2. Audience for the output (agentic build team, executives, both).
3. Focus areas that deserve the deepest digging (for example onboarding, pricing, sharing).
4. Depth: quick, **standard (default)**, or full. Describe each in one line from `references/depth-presets.md`.
5. Deadlines and constraints (trial end dates, paywalls, devices available).
6. Hypotheses the user wants tested, if any.

Write `docs/<product>/01-charter.md`: inputs, focus, scope, personas (from public evidence only), research questions, hypotheses H1 to Hn, and constraints. Create the knowledge base skeleton from `references/kb-template.md` and a task list mirroring the phases for the chosen depth.

## Step 1: Desk research (parallel)

Launch the `desk-researcher` agent, one instance per source group when depth is standard or full (help center and docs; reviews and ratings; store listings, pricing, and privacy; company, jobs, trademarks, and public docs). Give each the charter path and the source checklist in `references/source-checklist.md`. Use the help-center-extractor skill for documentation sites. Continue Step 2 setup while they run.

## Step 2: Product exploration (main session, with the user)

Skip for quick depth. Load the product-explorer skill and follow it: build the coverage checklist (MAP tree), choose the access mode (web, desktop, iPhone Mirroring), apply create-and-cancel, and use guided handoffs for anything the user must do. Record session notes in `evidence/sessions/`. Log participant confusion and reactions as tagged evidence.

For full depth, ask the user whether they can export their own data from the product. If yes, load the export-structure-reader skill and read structure only.

## Step 3: Journeys and capability inventory

Launch the `teardown-analyst` agent with the evidence folder. It writes `03-journeys.md` (JRN IDs) and `data/capabilities.csv` rendered to `04-capability-inventory.md` (CAP IDs, layer, Kano class, evidence tag, confidence, source). Quick depth: inventory from desk evidence only, confidence capped at Medium.

## Step 4: Deep analysis (standard and full)

Have the analyst apply the lenses in `references/analysis-lenses.md`: object and relationship model, tone and lexicon (load the tone-and-lexicon skill), the signature mechanic deep dive, feedback design, ethics and privacy, company and strategy, and (full depth) architecture and data model.

## Step 5: Gaps, synthesis, opportunities (written as the product's own PO)

Write phases 5 to 7 as if a product owner at the studied company were documenting their own product: gap analysis against named peers in the same category, themes, the product's vision and positioning, what it deliberately does not do, and candidate capabilities scored with WSJF. This keeps the analysis neutral and useful to anyone.

## Step 6: Risks and validation

Write `08-risks-and-validation.md` (RSK IDs) and finalize `open-questions.md`. Build the role-by-role question bank (`analysis/team-questions.md`) mapping each role's questions to answering files or open-question IDs.

## Step 7: Verify, package, summarize

1. Launch the `teardown-verifier` agent with no prior context. Fix every failure it reports.
2. Write the summary doc from `references/summary-doc-template.md`. Make it from the Docs artifact type when the session offers one; otherwise write `summary.md`.
3. Package the knowledge base (zip), update `CHANGELOG.md`, and deliver it to the user's chosen folder.
4. Ask the user to confirm research is complete.

## Step 8: Implications for us (only after confirmation)

Only after the user confirms research is complete, write `implications/<product>-implications.md` from `references/implications-template.md`, kept outside `docs/<product>/`. Read the user's own product materials (persona, empathy map, vision) only now. Never edit evidence files in this step. For cross-competitor differentiation, point the user to the market-rollup skill.

## Finishing message

Tell the user in a few sentences what the teardown found, deliver the package and summary, list the open questions that need them, and suggest the next step (another competitor, a depth upgrade, or a market roll-up).

## What this does not verify

- Whether a competitor's own statements (help center, policy, store listing) are true; it records them as DOCUMENTED, not as fact.
- Whether the findings lead to a better product decision; nothing here measures outcomes.
- Whether the product's terms of service or robots.txt allow your research; you check that yourself.
