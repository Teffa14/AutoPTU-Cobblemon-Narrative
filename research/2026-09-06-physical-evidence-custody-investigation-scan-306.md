# Physical evidence custody / investigation scan — Pass 306

Status: RESEARCH / PROVENANCE, NOT CANON
Date: 2026-09-06

## Existing-repository check

The recursive repository tree was inspected before this pass and targeted code/research searches found no existing `custody` implementation. Passes 303–305 already cover infrastructure-failure attribution, durable findings and concurrent causes, so Pass 306 deliberately addresses handling integrity instead of adding another causal-attribution system.

Canon remains governed by `canon/README.md`: research is evidence, proposals are candidates, design defines architecture, and only `canon/` establishes world facts.

## New public sources

### National Institute of Justice — Chain of Custody

Source: https://nij.ojp.gov/nij-hosted-online-training-courses/law-101-legal-guide-forensic-expert/pretrial/pretrial-motions/chain-custody

NIJ describes chain of custody as a recorded way to account for where evidence travelled and who handled it, intended to protect identity, authenticity and integrity. The source also distinguishes consequences of an incomplete chain from a finding that evidence was necessarily falsified or altered.

Reusable Ouros lesson: preserve handling history as its own evidence layer. A missing handoff should reduce confidence in continuity without becoming an omniscient tampering flag.

No legal admissibility rule, real-world procedure or numeric standard is imported into Ouros.

### National Institute of Justice — Preservation of Evidence

Source: https://nij.ojp.gov/nij-hosted-online-training-courses/crime-scene-and-dna-basics-forensic-analysts/evidence-crime-scene/preservation-evidence

The NIJ material emphasizes documented transfers, identification of handlers, packaging/labeling and disposition records.

Reusable Ouros lesson: collection, transfer, storage, examination and release can be separate durable handling events. Investigators may know only a subset of those events.

No forensic protocol is made a PTU rule.

### NIST — Digital Evidence Preservation

Source: https://www.nist.gov/publications/digital-evidence-preservation-considerations-evidence-handlers

NIST treats preservation and acquisition/handling as distinct evidence-management concerns, particularly when evidence can be changed by the act of handling it.

Reusable Ouros lesson: provenance of an observation and integrity of the object that produced it are separate questions. The same architecture can later support physical records, machine logs and digital artifacts without claiming they share identical preservation mechanics.

### Detective Pikachu / Detective Pikachu Returns

Sources:
- https://www.nintendo.com/au/games/nintendo-switch/detective-pikachu-returns/
- https://www.nintendo.com/en-gb/Games/Nintendo-3DS-games/Detective-Pikachu-1329566.html

Nintendo describes a loop of examining scenes, gathering evidence, interviewing human and Pokémon witnesses, recording clues and later combining testimony/evidence during deduction.

Reusable Ouros lesson: environmental evidence, witness knowledge and later deduction can remain distinct data sources. Pokémon may contribute different observational perspectives without automatically making their statements mechanically true.

No Ryme City characters, cases, dialogue, locations or plot structure are copied.

### PTU community campaign — Pokémon Undercover

Source: https://www.reddit.com/r/PokemonTabletop/comments/z24ni1/

The public PTU campaign pitch centers on undercover work, heists and the need to accumulate enough information to identify an organization while managing consequences during infiltration.

Reusable Ouros lesson: an investigation can create tension from what evidence can safely be obtained, preserved and communicated, rather than from a single clue-gated reveal.

The campaign's organization, story and characters are not imported.

### Contemporary investigation-GM discussion

Source: https://www.reddit.com/r/rpg/comments/1t94pra/how_do_you_prep_for_investigative_campaigns/

A 2026 GM discussion describes clue graphs connecting NPCs, locations, factions and events, with multiple avenues available to players.

Reusable Ouros lesson: evidence custody should generate additional investigation nodes instead of merely invalidating a clue. A missing transfer can lead to a handler, storage site, registry or witness while keeping the main case playable.

Community advice is treated as design inspiration, not authority.

## Original structures derived for Ouros

A durable evidence item can create a second investigation after the initial discovery: who collected it, who moved it, where it was stored, who examined it and whether every handoff can be supported by evidence available to the current investigator.

This supports disputed samples, recovered machine parts, damaged Poké Balls or equipment, archived physical records, ecological specimens, intercepted cargo and infrastructure components. Concrete item types remain proposal-level until their local canon and PTU/Caelo mechanics are validated.

The critical world-model distinction is:

`HANDLING_CONTINUITY != EVIDENCE_TRUTH`

An NPC can reasonably believe that an item was handled continuously while disagreeing with an expert interpretation. Another NPC can accept the interpretation but distrust the custody history. Those disagreements can persist because each actor receives different records.

## Canon / mechanics classification

Nothing in this research note is canon-approved automatically.

The evidence-custody runtime is a world-simulation architecture proposal with executable regression coverage. Specific inspection skills, forensic techniques, Pokémon senses, Moves, Abilities, Items, Trainer Features, laboratory procedures and institutional rules remain uncertain until validated against PTU/Caelo and local canon.
