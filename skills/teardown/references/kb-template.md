# Knowledge base template (Claude Code docs structure)

```
<product>-teardown/
  CLAUDE.md                 # how agents should use this KB; CLAUDE.md imports only conventions.md and 00-index.md, never evidence or analysis files
  README.md                 # what is here, headline findings, reading order
  CHANGELOG.md              # versioned increments
  docs/<product>/
    00-index.md             # every file with status
    conventions.md          # copy of the conventions reference
    01-charter.md
    02-product-map.md       # MAP tree
    03-journeys.md          # JRN
    04-capability-inventory.md   # rendered from data/capabilities.csv
    05-gap-analysis.md      # rendered from data/gap-scores.csv
    06-synthesis.md         # THM, vision, positioning, what it will not do
    07-candidate-capabilities.md # OPP with WSJF, rendered from data/backlog.csv
    08-risks-and-validation.md   # RSK
    open-questions.md       # Q with method, owner, status
    analysis/
      core-model-and-language.md
      lexicon-and-taxonomy.md
      team-questions.md
      architecture.md        # full depth
      data-model.md          # full depth
      company-and-history.md # standard and full
    data/
      capabilities.csv  gap-scores.csv  competitor-comparison.csv  backlog.csv
    evidence/
      sources.md             # MLA Works Cited
      help-center-notes.md   review-themes.md   privacy-policy-notes.md   competitors.md
      sessions/session-plan.md  sessions/session-NN-notes.md  sessions/participant-notes.md
  implications/             # written only after research is confirmed complete
    <product>-implications.md
```

## CSV schemas (keep column names identical across teardowns so the roll-up can merge them)
- capabilities.csv: `id,area,capability,description,layer,kano,free_or_paid,evidence_tag,confidence,source,map_ids,jrn_ids,notes`
- gap-scores.csv: `id,capability_or_job,this_product_score,peer,peer_score,evidence_tag,confidence,notes` (scores 0 to 5)
- competitor-comparison.csv: `dimension,this_product,peer_1,peer_2,peer_3,source`
- backlog.csv: `id,epic,title,user_story,acceptance_criteria,bv,tc,rr,js,wsjf,cap_ids,thm_ids,rsk_ids`

## CLAUDE.md template
State: the KB's purpose and audience; that evidence is neutral; the evidence tags and ID rules; "do not re-research answered questions, check open-questions.md first"; reading order; writing standard. CLAUDE.md imports only conventions.md and 00-index.md, never evidence or analysis files.

## Rendering
Generate markdown tables from CSVs with a small script so data stays the single source of truth. Re-render after every CSV change.
