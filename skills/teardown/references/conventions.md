# Conventions

## Evidence tags
| Tag | Meaning | Example |
|---|---|---|
| OBSERVED | Seen first-hand in the product during a session | The project editor has a Due date field |
| DOCUMENTED | Stated by the company (help center, policy, store listing, job post, public docs) | Help article says plan changes take effect in 3 days (illustrative) |
| REPORTED | Stated by third parties (reviews, press, forums, aggregators) | 21 to 32 percent of reviews cite bugs (illustrative) |
| INFERRED | Reasoned from other evidence; say what it rests on | Personal data is local-first because it is absent from synced models (illustrative) |

Confidence: High (direct, recent, corroborated), Medium (single source or slightly dated), Low (weak, modeled, or conflicting). Revenue and user counts from aggregators are Low unless the company states them.

Every row in a CSV and every factual line in prose carries a tag, a confidence, and a source pointer (file, URL, session and step).

## Stable IDs (never renumber; add, do not delete; mark retired items "Retired")
| Prefix | Object |
|---|---|
| PER- | Persona |
| H | Hypothesis |
| MAP- | Screen or node in the product map |
| JRN- | User journey |
| CAP- | Capability |
| GAP- | Gap versus peers |
| THM- | Synthesis theme |
| OPP- | Candidate capability or opportunity |
| RSK- | Risk or riskiest assumption |
| Q- | Open question |

## Layers and classes
- Whole product layers: Generic, Expected, Augmented, Potential.
- Kano: Must-be, Performance, Attractive, Indifferent, Reverse.
- Prioritization: WSJF = (Business Value + Time Criticality + Risk Reduction) / Job Size, each on 1, 2, 3, 5, 8, 13, 20.

## Jargon key
MAP = a screen or node in the product map. JRN = a user journey. CAP = a capability the product offers. Kano = a model that sorts features into Must-be, Performance, Attractive, Indifferent or Reverse (see Layers and classes).

## Contradictions
When two sources disagree, record both, date both, state which governs and why (usually the newer, more formal source), and add the contradiction as a finding.

## Privacy and personal data
Record structure, never personal content: field names not values, counts not contents, UI copy not the tester's entries. Never record the tester's notifications, contacts, messages, or document text. If a file contains personal data, read only keys and types.

## Copyright
Paraphrase. Quote a source at most once, under 15 words. Never reproduce a product's long copy, art, or prompts wholesale. Describe structure and principles instead.

## Writing standard (default; the user may override)
Plain, active voice. No em dashes in prose. No filler summaries. MLA 9 for the Works Cited in `evidence/sources.md`. Dates as YYYY-MM-DD in tables.
