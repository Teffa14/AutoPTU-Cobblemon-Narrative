# Research scan 293 — memory retrieval, forgetting and source monitoring

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-05
Canon effect: NONE

## Question

How can Ouros support witnesses who forget details or lose source attribution without deleting history, fabricating psychology or turning later uncertainty into a retroactive rewrite?

## Public sources reviewed

### APA memory teaching material

Source: https://www.apa.org/ed/precollege/topss/lessons/memory.pdf

Reusable structure: forgetting is not constant over time, and interference can disrupt retrieval. This supports treating recall accessibility as distinct from whether information was ever encoded.

Not adopted: Ebbinghaus curves, classroom examples, human-rate constants or any real-world psychological calibration.

### Protecting memory from misinformation

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC7502729/

Reusable structure: source-monitoring failures can occur when misleading details are retrieved without correct source/context attribution. This supports separating content accessibility from source accessibility.

Not adopted: neural mechanisms, experimental parameters or probabilities.

### Recalling fake news during corrections

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC9481799/

Reusable structure: correction, familiarity and recollection can coexist, and successful updating can depend on retrieving relationships between earlier and later information. This supports preserving contradictory historical claims instead of overwriting them.

Not adopted: news-specific framing or behavioral effect sizes.

### Memory failure after misinformation correction

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10710738/

Reusable structure: remembering that information was corrected matters separately from having encountered the correction. This supports later cue/rehearsal work without treating publication receipt as permanent perfect recall.

Not adopted: political/news domains or human belief probabilities.

### PTU campaign-log scan

Source: https://www.reddit.com/r/PokemonTabletop/comments/xtwhxv

Reusable structure: campaign play can intentionally move past repeated tactical resolution when replaying the same fight does not add value. For Ouros this reinforces maintaining reduced semantic consequences for investigation/witness loops rather than forcing every memory-driven consequence into battle.

No characters, events, dialogue or plot are reused.

## Transformation into Ouros

The implementation keeps the durable KnowledgeLedger intact and creates a temporary recall projection at a semantic minute.

Three states are enough for the first seam: content plus source recalled; content recalled without source; content inaccessible.

Source loss does not create a new source. Forgetting does not erase provenance. Historical audit and current testimony can therefore disagree without data corruption.

## PTU / Caelo / Kairos cross-check

No PTU mechanic is introduced. No Caelo or Kairos rule is adopted. The system is world-agent simulation policy only.

`SOURCE_HAS_PATTERN != OUROS_USES_RULE`

## Open questions

Future work should define explicit memory cues and rehearsal, archival lookup versus unaided recall, deliberate deception, false source attribution, and whether high-salience authored events need per-claim retention tags instead of a global age policy.
