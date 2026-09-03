# Pass 243 — executable ecology regression research

Status: RESEARCH / PROVENANCE, NOT CANON
Date: 2026-09-03

## Scope

This pass starts the 243+ gap-closure phase defined by `design/ecology-development-program.md`. The immediate question is how to turn the ecology contracts from passes 227–242 into executable regressions without moving PTU authority into the narrative repository.

The repository already contains deterministic JSON fixtures for demography, persistent-individual projection, observation, ecology-driven events and AutoPTU handoff. The missing layer was an executable harness able to fail when those fixtures contradict their own authority and conservation rules.

## New public-source scan

### PTU wilderness information remains observation-scoped

Source: Pokemon Tabletop United community rules reference, Skills / Survival.
https://pturpg.wikidot.com/skills

The Survival description explicitly supports scouting an area to learn basic information such as common Pokémon and resources. The reusable Ouros lesson is that field investigation can expose bounded ecological information without handing the player the hidden population ledger. This is consistent with Pass 240 and should remain a regression invariant.

Ouros use: transformed structural lesson only. The wiki is a PTU reference, not new Ouros canon.

### Pokémon Reborn treats environment as explicit state with transitions

Sources:
https://pokemon-reborn.fandom.com/wiki/Field_Effects
https://pokemon-reborn.fandom.com/wiki/Corrosive_Field
https://pokemon-reborn.fandom.com/wiki/Burning_Field

Reborn's field system demonstrates a useful game-design pattern: environmental state has named states, explicit transition causes and mechanical consequences. Some fields can replace or terminate others, and specific actions trigger the transition.

Ouros use: adopt only the high-level state-machine lesson. Do not import Reborn field names, numerical modifiers, move interactions or battle rules. For Ouros ecology, disturbance/event states must have explicit causes and observable consequences, while any PTU tactical terrain effect still requires an AutoPTU capability contract.

### Mystery Dungeon separates world trouble from the request surface

Sources:
https://mysterydungeon.pokemon.com/fr-ca/world/
https://mysterydungeonwiki.com/wiki/Pkmn%3ANatural_Disasters

Rescue Team uses requests and a bulletin-board surface to expose problems occurring in the world, while broader natural-disaster pressure exists independently of an individual accepted request.

Ouros use: this reinforces Pass 241. A quest or notice may point at an ecology event but cannot create, resolve or rewrite the event's hidden state. The ecology event must survive without an accepted quest.

## Repository finding

Pass 239 contained a lifecycle contradiction that was easy to miss in prose review. `lease.pool.002` was promoted from an unresolved slot to a persistent member and remained active. A later capture window attempted to reserve that same persistent member again. That violated the fixture's own one-active-lease-per-member invariant.

Pass 243 corrects the trace by releasing the research-session lease before the later capture lease is reserved. This does not change population truth or canon. It makes the fixture internally consistent with the existing lease contract.

## Implementation consequence

The new validator should enforce contracts that can be checked without PTU adjudication:

- population conservation and explicit demographic deltas;
- presentation events never author population changes;
- stage transitions conserve abundance;
- persistent member and unresolved-slot leases are unique while active;
- Minecraft UUIDs cannot become canonical identity;
- capture removal requires an AutoPTU semantic capture result plus demographic writeback;
- no-detection does not prove absence;
- ecology event thresholds and hysteresis remain deterministic;
- ordinary visibility, warning and unopposed flight stay in overworld;
- unsupported tactical pursuit uses a reduced version rather than Cobblemon inventing missing PTU rules.

The validator must not calculate PTU attacks, damage, statuses, terrain effects, forced movement or AI choices. Those remain AutoPTU responsibilities.

## Capability implications

The regression harness itself does not promote any engine category.

Verified from the prior audited contract set: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

Partial: complete movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

Mixed/partial/blocking: terrain/weather/hazards/zones/reactions.

Blocking as a complete family: AI tactical policy.

Partial/blocking end-to-end: Minecraft/Cobblemon/Craftics adapter/playback.

AutoPTU-Java live evidence at review time is `c5ca00d22cc234d0ec8dc0429e60f8ee42381dec`, which freezes the terrain-trap semantic event payload against the Python oracle. This strengthens that narrow tile-entry/trap seam only. AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its latest commit is presentation-only.

## Next implementation gap

Once this regression harness is green, the next high-value slice is a cross-fixture integration trace that carries one persistent Fletchling through population state -> projection lease -> observation -> ecology event -> optional AutoPTU handoff -> semantic result -> post-battle ecology reevaluation. The trace must use real fixture identifiers and must never duplicate hidden PTU rules in the narrative runner.
