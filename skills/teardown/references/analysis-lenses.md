# Analysis lenses

Apply each lens the depth calls for. Each lens names its output file and the questions it must answer. Go below the screens: explain why a feature works, not only that it exists.

## 1. Object and relationship model (standard, full)
File: `analysis/core-model-and-language.md` section 1 and 2.
- What are the core objects (for example Project, Task, Comment, Label)? Draw a mermaid diagram with cardinality.
- How do objects relate to the user's time (day, week, billing cycle) and to limits?
- Which objects can be created, edited, archived, deleted? Which fields are required? (From create-and-cancel and edit passes.)

## 2. Tone, intention, and lexicon (standard, full)
Files: `analysis/core-model-and-language.md` section 3 onward and `analysis/lexicon-and-taxonomy.md`. Use the tone-and-lexicon skill.
- What stance does the copy take toward the user? Where does the voice break (system vocabulary leaking into UI, sales language, failure framing)?
- Glossary of every product-specific term with register (UI, brand voice, product voice, internal, data).
- Taxonomy (mermaid mindmap). Lexical study: what the vocabulary is doing and why it matters.

## 3. Signature mechanic deep dive (standard: one; full: all that matter)
Pick the feature that makes the product feel different (for example a one-click import or a trial). Document it step by step: what each step asks, the move it makes, what shifts for the user, where it comes from (research, method), what it omits. Cite sources for the method.

## 4. Feedback design (standard, full)
Every way an upgrade, a downgrade, and a renewal is acknowledged: visual effects, copy, benefits, trial handling, grace periods, notifications. Note what is configurable.

## 5. Monetization and packaging (all depths)
Free versus paid matrix, price points by platform, trial mechanics, upsell placement and tone, gift or family plans, cancellation and refund paths, complaint themes about billing.

## 6. Ethics, privacy, and safety (standard, full)
Data collected versus needed, where it lives, encryption, third-party sharing, contacts and permissions, deletion path, store label versus policy versus observed behavior, abuse reporting, dark patterns. Rank serious findings in the opportunity backlog; do not footnote them.

## 7. Company and strategy (standard, full)
File: `analysis/company-and-history.md`. Entity, founders, size, funding and profitability (as stated), scale, ratings, trademarks, operating model, release cadence, product timeline with major changes and the reasons given, strategic signals for a competitor. Exclude name collisions explicitly.

## 8. Architecture and data model (full)
Files: `analysis/architecture.md`, `analysis/data-model.md`. Tech stack from job posts and store metadata; what lives on device versus server (from export structure and policy); content pipeline; release model; system context, module map, and core-loop sequence diagrams in mermaid; entity dictionary and ERD from the export (structure only). Mark every diagram as INFERRED where it is.

## 9. Frameworks for synthesis (standard, full)
Whole product layers, Kano, jobs to be done, story mapping for journeys, WSJF for opportunities. State what the product deliberately will not do.

## 10. Team question bank (standard, full)
File: `analysis/team-questions.md`. For each role (PO/PM, UX research, interaction design, content design, visual, mobile, platform/backend, data, domain expert, QA, security/privacy/legal, growth/community): what it needs, depth needed, and its questions marked answered (with file) or open (with Q-ID).
