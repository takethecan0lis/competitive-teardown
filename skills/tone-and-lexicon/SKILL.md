---
name: tone-and-lexicon
description: Analyzes a product's copy for tonality, intention, and stance, and builds a glossary, taxonomy, and lexical study of its vocabulary. Use during a teardown, or when the user asks to "analyze the tone", "study the word choice", "build a glossary of the app's terms", "what is the voice of this product", or "how does the language make users feel".
---

# Tone and Lexicon Analysis

Study the words a product uses and what they do to the person reading them. Work from captured screens, help articles, store copy, notifications, and any public brand or voice guidelines the company has published. Quote at most once per source, under 15 words; paraphrase everything else.

## Objective and benefit

- **Objective:** This skill aims to show what a product's words do to the people who read them, surface by surface.
- **Benefit:** You get the stance of the copy, its recurring patterns, the places where the voice breaks, and a glossary, each tied to a captured source.
- **Why it is worth having:** Voice is usually argued from taste. Here it is judged on evidence, so a team can decide what to match, avoid or improve.

Adopted, not measured: no result has been measured yet.

## Ask first

Ask the user who the audience is (who reads this product's copy and who the analysis is for) before step 1. There is no default; an audience guessed wrongly changes the findings.

## 1. Collect
Gather copy by surface: onboarding, home, empty states, create and edit forms, confirmations, errors, lapsed plans and renewals (missed deadlines, expired trials), paywalls and upsells, notifications, settings, support screens, help center. Note who is speaking on each (brand, product, system).

## 2. Find the stance
For each surface answer: What does the copy assume about the reader's state? What does it ask of them? What does it promise? What does it confirm after an action? How does it handle errors, empty states, and expired plans? Classify the stance (for example: guide, tool, authority, salesperson).

## 3. Map the patterns
Identify 6 to 12 recurring language patterns with one short example each, for example: questions instead of orders; progress shown as counts; jargon defined on first use; plain verbs instead of nouns; second person instead of passive voice.

## 4. Find where the voice breaks
List places where system, sales, or analytics vocabulary leaks into the user's view (for example "Churn risk", "Segment B", sale banners, error codes). Each break is a finding with its location.

## 5. Build the glossary and taxonomy
Write `analysis/lexicon-and-taxonomy.md`:
- A taxonomy as a mermaid mindmap grouped by domain (core objects, sharing, commerce, settings, company and community).
- A glossary table per domain: term, register (UI, brand voice, product voice, internal jargon, data-model name), meaning, source.
- Retired terms and what replaced them.

## 6. Write the lexical study
Explain in prose what the vocabulary is doing and why it matters for the product's goals: which metaphors anchor it, how many voices it uses and what each is for, how it lowers or raises stakes, how internal jargon reveals the operating model, and who the voice may not reach (for example expert users who find it simplistic).

## 7. Tie it to intention
Close with how the language supports or undercuts the product's core promise (for a banking app: trust; for a productivity app: momentum). Cite the company's own voice guidelines if published.

Stay neutral. Do not compare to the user's own product here.

## What this does not verify

- How readers actually feel; it reads the copy, not the readers, so a stance is an interpretation.
- That the captured copy is complete or current; copy changes by release, region and test group.
- Whether the company's stated voice matches what it ships; both are recorded, and any gap is a finding, not a verdict.
