# Pass 290 research — publication revision delivery

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-05
Canon authority: NONE

## Question

How should Ouros distribute a correction, update or retraction after a public claim has already reached some NPCs, while preserving the historical fact that different actors knew different versions at different times?

## Public research reviewed

### Friggeri, Adamic, Eckles and Cheng — Rumor Cascades (ICWSM 2014)

Public paper page: https://ojs.aaai.org/index.php/ICWSM/article/view/14559

Reusable lesson: corrective information can change behavior around a rumor, yet a large cascade may continue spreading while corrective links already exist. A correction therefore cannot be modeled as instantaneous global deletion of the earlier version. Exposure to the correction is its own propagation fact.

Ouros transformation: each publication revision performs its own audience expansion and creates its own per-agent receipt events. An NPC who received the original can miss the correction. Another NPC can receive only the correction. Receipt history stays queryable.

No Facebook-specific mechanics, probability values or social-network data are imported.

### Martin Fowler — Domain Event / event-driven architecture

Public pages:
- https://martinfowler.com/eaaDev/DomainEvent.html
- https://martinfowler.com/articles/201701-event-driven.html

Reusable lesson: record an interesting change as an event so later state and reactions can be traced back to what happened. Event-sourced state is derived from a history of changes rather than requiring past entries to be overwritten.

Ouros transformation: a correction/retraction remains a later publication event with explicit lineage. Earlier publication, delivery and NPC decision records remain historical facts. The current editorial version is a projection over that lineage.

No enterprise implementation framework is imported.

### Super Pokémon Online — PTU Living World RPG

Public community post: https://www.reddit.com/r/PokemonTabletop/comments/1mkct0y/super_pok%C3%A9mon_online_ptu_living_world_rpg/

Reusable lesson: the advertised living-world model emphasizes asynchronous play and a world that remembers player actions, including changes to reputation, economy and discovered locations. Persistent consequences must therefore survive differences in who was present at a given moment.

Ouros transformation: public information can affect named NPCs asynchronously. Receipt timing becomes part of persistent causality rather than session-local exposition.

No setting, characters, guilds, locations, rules or story material are imported.

## Project-source cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` records Kairos as living-world evidence with persistent interaction outside quests, downtime, player-created factions and parallel progression. It explicitly warns that the supplied Kairos material contains homebrew and is a reference rather than automatic Ouros acceptance.

`design/ouros-source-authority-and-species-policy.md` is authoritative for this pass. It states that Ouros project invariants outrank external material, PTU-derived mechanics remain under the active rules profile, Caelo/Kairos are evidence rather than automatic rules authority, and Minecraft presentation cannot silently author PTU outcomes.

Pass 290 adds no PTU, Caelo or Kairos rule. Publication revision semantics are an Ouros persistent-world adaptation.

## Resulting design constraints

1. Every revision has its own publication identity and remains linked to its predecessor.
2. Audience eligibility is recomputed for the revision at its actual expansion time.
3. Receiving an original never guarantees receiving its successor.
4. Receiving a successor does not require having received the original.
5. Delivery is required before the NPC ledger or agenda can react.
6. A retraction records withdrawal of a claim; it does not infer the opposite world fact.
7. Historical receipts and decisions remain intact after later editorial changes.
8. Publication lineage, receipt lineage and belief state remain separate concepts.
9. Bounded audience expansion and delivery budgets remain authoritative under load.
10. No region, faction or publication medium becomes core-AI special-case logic.

## Novel Ouros hook generated from the research

A correction race can become an investigation structure. The player may discover that one group acted from the first bulletin, another had already received a correction, and a third never received either. Responsibility can then depend on publication time, coverage, actual receipt, trust and subsequent action instead of a single global quest flag.

This is proposed structure, not canon.
