# Recurring wild individual recognition scan — Pass 253

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Date: 2026-09-04

## Research question

How can Ouros let players and NPCs become familiar with a recurring wild Pokemon while keeping observer knowledge fallible and preventing accidental identity merges?

## New source patterns

### Wildlife mark-resight uncertainty

McClintock et al., "Mark-resight abundance estimation under incomplete identification of marked individuals" (Methods in Ecology and Evolution, 2014) treats uncertain identification of already marked animals as a real observation-error problem. Movement, behaviour, visual obstruction and environmental conditions can prevent confident identity assignment. Reusable lesson: an observation system should preserve unresolved identity rather than silently choosing the most convenient match.

Source: https://doi.org/10.1111/2041-210X.12140

Yoshizaki et al., "Modeling misidentification errors in capture-recapture studies using photographic identification of evolving marks" (Ecology, 2009) shows that individual identification from natural marks can create consequential false matches when marks change or evidence quality is poor. Reusable lesson: apparent similarity is evidence, not identity authority.

Source: https://doi.org/10.1890/08-0304.1

USGS Bird Banding Laboratory material documents colored leg bands as a way to identify individual birds from a distance. Reusable lesson: a deliberately assigned, externally observable marker can support stronger identity claims than ordinary appearance or behaviour. Ouros has no such marker approved for the Sendero Fletchling in this pass.

Source: https://www.usgs.gov/media/images/semipalmated-plover

### Behaviour is useful but probabilistic

Hardman and Dalesman, "To be so bold: boldness is repeatable and related to within individual behavioural variability in North Island robins" (2018 publication record) found high repeatability alongside meaningful within-individual variability. Reusable lesson: repeated retreat timing, tolerance or boldness can strengthen a longitudinal hypothesis but cannot function as a unique key.

Source: https://pubmed.ncbi.nlm.nih.gov/28454917/

Senar et al./Plaza et al. work on passerine social traits reports repeatable between-individual differences across contexts while also showing that repeatability depends on timescale and acclimation context. Reusable lesson: behavioural consistency is contextual evidence whose weight can decay or conflict.

Source: https://onlinelibrary.wiley.com/doi/full/10.1111/jeb.13703

### Investigation structure

Robin D. Laws' GUMSHOE scenario-structure guidance recommends multiple routes and core clues so a mystery does not depend on one fragile discovery. Reusable Ouros lesson: recurring-individual recognition should accumulate from independent observation roots, while relays of one root must not become artificial corroboration.

Source: https://pelgranepress.com/2018/01/03/see-page-xx-improv-and-gumshoe-scenario-structure/

A 2023 Pokemon Tabletop community resource discussion recommends using habitat/lore information and Pokemon intelligence when preparing wild encounters rather than treating encounters as stat blocks alone. Reusable lesson: observed ecology and behavioural context can carry encounter identity and meaning before combat begins.

Source: https://www.reddit.com/r/PokemonTabletop/comments/11j2p3l

## Transformed design lessons for Ouros

1. Internal actor continuity and diegetic identity confidence are separate records.
2. Repeated behaviour can add evidence but cannot reveal `persistent_actor_id`.
3. Independent observations may increase confidence; copies, rumours and relays sharing one provenance root do not.
4. Contradictory evidence must be preserved. It can reduce confidence or create a competing hypothesis instead of forcing a merge.
5. Ordinary visual similarity among same-species wild Pokemon is insufficient for certainty.
6. A future canon-approved band, tag or uniquely observable stable marker could support a stronger identity state, but Pass 253 does not create one.
7. Observer uncertainty must never mutate population totals, projection leases, capture truth, combatants or demographic history.

## Project cross-check

Pass 252 already establishes a proposed recurring-Fletchling loop, states that `persistent_actor_id` must not become player knowledge, and leaves the recognition threshold unresolved. Pass 253 addresses that specific unresolved question without changing the existing population or actor canon.

The lower-Sendero Fletchling population remains 12. The established actor `ouros.marea.encounter.sendero_lower_shelf.fletchling.0` is used only as hidden fixture truth. No second persistent actor is canonized; competing same-species evidence uses a fixture-only unresolved population source.

PTU/Caelo/Kairos material remains source evidence under existing repository authority policy. No external campaign character, plot, dialogue, location or mechanics are imported as Ouros canon.

## Status boundaries

CANON-ALIGNED: observer knowledge is imperfect; hidden persistent identity remains authoritative inside Ouros; population changes require explicit demographic authority.

PROPOSED: identity-hypothesis states `UNRESOLVED`, `POSSIBLE_SAME_INDIVIDUAL`, `PROBABLE_SAME_INDIVIDUAL`, contradiction handling and provenance-weighted promotion.

FIXTURE-ONLY: the exact perch class, retreat vector, observation timestamps, confidence values and competing unresolved source used in the Pass 253 trace.

UNCERTAIN: which future physical or social markers can ever justify player-facing confirmation of individual identity; whether specific Trainer Features or research tools should modify evidence quality.
