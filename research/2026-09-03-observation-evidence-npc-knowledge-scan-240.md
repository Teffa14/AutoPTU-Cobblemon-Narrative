# Pass 240 research — observation, evidence and NPC knowledge

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-03
Ouros canon effect: NONE BY ITSELF

## Question

How should Ouros let players and NPCs learn about a persistent Pokémon ecology without exposing hidden population truth, turning sightings into omniscience, or letting Minecraft entity state author canon?

## Existing Ouros constraints reviewed

This pass follows `design/ecology-development-program.md`, `design/ouros-source-authority-and-species-policy.md`, Pass 238 population/demography work, and Pass 239 persistent-individual/spawn reconciliation.

Existing invariants retained:

- Ouros owns persistent ecological truth.
- Minecraft/Cobblemon presents observable actors and events but does not author ecological or PTU truth.
- AutoPTU owns structured tactical adjudication when a battle handoff occurs.
- a visible spawn is not a population increment;
- a despawn is not death or emigration;
- an entity UUID is only temporary projection correlation;
- a player or NPC must not receive hidden population-ledger access merely because a Pokémon was seen.

## Public research scan

### PTU skill structure

Source: PTU community rules reference, Skills page, retrieved 2026-09-03.
URL: https://pturpg.wikidot.com/skills

Reusable structure:

- Perception covers noticing environmental details, hidden actors, evidence and active investigation.
- Survival can scout wilderness, learn common local Pokémon/resources, identify rarer signs with stronger success, and track targets.
- General Education and specialized Education skills help interpret information after it has been found.

Design lesson: Ouros should separate observation acquisition from interpretation. A character can notice evidence without automatically knowing what it means. PTU already supports that distinction; no new tactical rules are needed merely to store observations.

Authority note: this is PTU reference evidence. Any exact DC, Edge, Feature or class interaction remains subject to the active Ouros rules profile and engine verification.

### Detective Pikachu investigation structure

Source: Bulbapedia summary of `Detective Pikachu`, retrieved 2026-09-03.
URL: https://bulbapedia.bulbagarden.net/wiki/Detective_Pikachu_(video_game)

The game structures investigation around testimony plus collected evidence, followed by reasoning. Reusable pattern: claims from people/Pokémon and physical evidence should be distinct records that can support or contradict an inference.

Do not import characters, cases, dialogue or plot specifics.

### Pokémon Legends: Arceus research structure

Source: Bulbapedia research-task documentation and public game documentation, retrieved 2026-09-03.
URL: https://bulbapedia.bulbagarden.net/wiki/Research_task_(Legends:_Arceus)

Reusable structure: knowledge can accumulate from repeated kinds of field evidence rather than one encounter revealing a complete species profile. Research tasks include repeated observation of behavior and contextual interactions.

Ouros adaptation: repeated evidence can improve confidence or unlock a field conclusion, but gameplay task counters must not be interpreted as literal biology.

### Imperfect detection and observation error

Source: U.S. Geological Survey, Royle, Nichols & Kéry, `Modelling occurrence and abundance of species when detection is imperfect`, 2005.
URL: https://www.usgs.gov/publications/modelling-occurrence-and-abundance-species-when-detection-imperfect

Key lesson: observed counts are biased estimates of true abundance when detection is imperfect. Presence and abundance require explicit treatment of detectability.

Ouros adaptation: a sighting can prove a minimum observed presence. It cannot expose total local abundance. Absence of sightings does not prove ecological absence.

Source: U.S. Geological Survey, McClintock et al., `Unmodeled observation error induces bias when inferring patterns and dynamics of species occurrence via aural detections`, 2010.
URL: https://www.usgs.gov/publications/unmodeled-observation-error-induces-bias-when-inferring-patterns-and-dynamics-species

Key lesson: false positives as well as false negatives matter. Even expert observers can generate incorrect auditory identifications, and small false-positive rates can badly distort inferred occupancy/change.

Ouros adaptation: tracks, calls, silhouettes, testimony and indirect evidence need modality-specific uncertainty. Contradictory evidence should create a disputed claim rather than silently overwrite old information.

### Living-world references

Kairos remains useful as evidence that PTU play can persist across asynchronous activities and one-shot quests. Its supplied source index routes relevant questions to skills/classes, campaign structure and world/encounter guidance. Kairos homebrew is not imported automatically.

Caelo/Kairos campaign material may inspire who records observations, who trusts whom, and how information persists, but no campaign-specific NPC, rule or species mutation becomes Ouros canon through this pass.

## Reusable Ouros conclusions

1. Store observation separately from inference.
2. Store inference separately from hidden ecological truth.
3. Every non-direct claim should retain a source chain.
4. Confidence belongs to a claim held by an observer/knowledge-holder; it is not a truth probability exposed by the world service.
5. Freshness matters. A once-correct report can become stale without becoming retroactively false.
6. Contradiction should coexist until resolved; newest does not automatically mean correct.
7. A direct sighting proves at most what was actually observable: presence, an observed minimum count, behavior, location/time and visible traits.
8. Repeated sightings may support persistent-individual recognition, but Minecraft UUID must never be used as player-facing identity evidence.
9. Rumor propagation must preserve provenance and should lose certainty unless corroborated.
10. NPC knowledge must be local and historical. A hidden population change elsewhere does not instantaneously rewrite what every NPC believes.
11. Battle results may contribute semantic evidence only after authoritative AutoPTU resolution. A visible KO animation is not evidence of death.
12. Research rewards should derive from evidence quality/diversity/corroboration, not from leaking the hidden ecology ledger.

## Proposed terminology

These terms are candidates, not canon approval:

Observation modalities:
`DIRECT_VISUAL`, `DIRECT_AURAL`, `TRACK`, `REMAINS_OR_TRACE`, `INSTRUMENT`, `FIRSTHAND_TESTIMONY`, `SECONDHAND_REPORT`, `AUTHORIZED_RECORD`.

Claim states:
`OBSERVED`, `SUPPORTED`, `SUSPECTED`, `DISPUTED`, `STALE`, `RETRACTED`.

Subject resolution:
`KNOWN_PERSISTENT`, `PROBABLE_MATCH`, `UNRESOLVED_LOCAL_MEMBER`, `UNKNOWN_EXTERNAL`.

Knowledge-holder stance:
`KNOWS_FROM_EVIDENCE`, `BELIEVES`, `SUSPECTS`, `HEARD`, `DISPUTES`, `UNKNOWN`.

## Research-to-canon boundary

Nothing above changes Marea species availability, population counts, NPC identities, locations, PTU DCs or battle rules. Pass 240 design/fixtures may consume already established Marea/Sendero actors and places, but any new story-specific fact remains PROPOSED until separately approved.

## Next implementation requirement

Create an observation/evidence/knowledge contract and deterministic fixture where sightings, reports, contradictions, staleness and repeated recognition can be replayed without mutating hidden population truth.