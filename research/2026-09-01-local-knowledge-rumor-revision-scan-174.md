# Ouros Narrative Research — Local Knowledge, Rumor Revision & Environmental Recontextualization — Pass 174

Status: RESEARCH ONLY / NON-CANON
Date: 2026-09-01

This pass extends the existing investigation, communications, public-memory and service-dispatch work. It does not replace the evidence graph from pass 03 or the communications layer. The specific gap is how incomplete local observations become claims, how claims move between actors, how culturally meaningful explanations can coexist with uncertain causality, and how later evidence revises knowledge without erasing the fact that an earlier belief circulated.

## Existing-repository boundary

Repository review before research showed that Ouros already separates canonical facts, claims, evidence, actor knowledge, public memory, message delivery and player-private state. It also already has non-linear investigation, communication-channel state, archives, public memory, service dispatch and fixed Marea residents. This pass therefore avoids creating a second investigation system.

The new contribution is a propagation model between those layers:

`OBSERVATION -> SOURCE INTERPRETATION -> CLAIM PACKET -> TRANSMISSION -> RECIPIENT BELIEF/DOUBT -> CORROBORATION/CONTRADICTION -> REVISION`

A claim can be useful even when incomplete. A later correction changes current belief but does not delete that the older version was once known or acted upon.

## Source 1 — PTU campaign log #22: ritual practice, drought and a hidden ecological cause

Source: https://www.reddit.com/r/PokemonTabletop/comments/ug8b7t/

A public PTU session recap describes a town festival tied to a story about a Mankey saving the settlement from starvation. Festival-goers leave peanuts as offerings. The party later learns that a large tree associated with the local practice is diseased and drawing unusually large amounts of water, contributing to drought. The problem is resolved by treating the ecological cause rather than by treating the festival participants as foolish or hostile.

Reusable structure:
- a local practice can have social meaning independent of whether the community's causal explanation is scientifically complete;
- ritual, ecology and current crisis can intersect without one automatically invalidating the others;
- residents can accurately report symptoms while misidentifying cause;
- the investigative payoff comes from recontextualization, not from revealing that every local story was a lie.

Ouros translation:
A Marea resident may say that a route has become unsafe "since the bell stopped sounding" because that temporal association is true from their perspective. Field evidence may later show that the bell and the route change share a third cause. The resident's statement remains a valid provenance record even after the causal model changes.

## Source 2 — PTU campaign log #24: player-caused disturbance, Pokémon territorial response and non-combat repair

Source: https://www.reddit.com/r/PokemonTabletop/comments/wudfhz/

A public PTU recap describes players knocking down a tree while travelling. A large Pokémon appears because the disturbance threatens nearby eggs. The group uses communication and restorative action—planting replacement trees—to de-escalate rather than treating the encounter as mandatory combat.

Reusable structure:
- wild Pokémon behavior can be a response to a recent world event rather than a permanent hostility flag;
- players can be the cause of the problem they are investigating;
- resolution may require changing the environment or behavior that produced the conflict;
- discovering motive changes the meaning of the same visible encounter.

Ouros translation:
A report such as "the upper Sendero group has become aggressive" should not become canonical species temperament. The claim packet should preserve observer, time, position and triggering context. Later evidence may identify nest protection, food pressure, route works, noise, smoke or another supported cause.

Mechanical guardrail:
Communication, Channeler effects or Pokémon capabilities from the source session are not imported as mechanics. Any Ouros equivalent must use actual PTU/Caelo and AutoPTU-supported capabilities.

## Source 3 — Pokémon Legends: Arceus, Back-Alley Mr. Mime: suspicion recontextualized as civic function

Source: https://www.serebii.net/legendsarceus/requests/back-alleymr.mime.shtml

The request begins from a villager's suspicion about a Mr. Mime behaving strangely. Following the Pokémon through invisible barriers eventually reveals a mundane civic explanation: the behavior helps a gate guard. The quest structure converts a suspicious interpretation into a more accurate understanding through direct observation.

Reusable structure:
- the initiating NPC does not need to be malicious or stupid to be wrong;
- a quest can begin from an interpretation rather than from confirmed danger;
- following behavior across several locations can reveal function;
- the resolution can update the source actor's knowledge rather than simply award loot.

Ouros translation:
Residents should be allowed to post "please check this" requests whose authoritative state is `UNVERIFIED_CONCERN`, not `THREAT_CONFIRMED`. Completion can write `EXPLANATION_ESTABLISHED`, `CONCERN_REDUCED`, or `NEW_QUESTION` depending on evidence.

## Source 4 — Pokémon Legends: Arceus, The Sea's Legend: archival clue + composition + time + place

Sources:
- https://www.serebii.net/legendsarceus/requests/thesea%27slegend.shtml
- https://www.gamespot.com/articles/the-seas-legend-how-to-get-the-mythical-manaphy-in-pokemon-legends-arceus/1100-6500224/

The request uses a historical text as a clue to a current event. Progress depends on interpreting several conditions together: a specific group of Pokémon, time of day, a landmark and a route through that landmark. The information source and the physical solution are separated.

Reusable structure:
- archival information can describe a pattern without directly giving a map marker;
- a clue may require correlation across actor composition, timing and geography;
- world knowledge becomes actionable only when the player tests it in the environment;
- a successful test can reveal a new place or event.

Caution for Ouros:
The cross-game obscurity of this example is not a desirable usability target. Ouros should keep enough redundant evidence inside the playable world. The structural lesson is multi-variable correlation, not deliberately withholding essential information outside the game.

## Source 5 — Kairos Isles PTU living world: durable character and downtime state outside quests

Source: https://kairosptu.wiki.gg/

The publicly accessible search index describes Kairos Isles as a PTU living-world campaign with character records, NPC information, downtime and real-estate systems available outside active quests.

Reusable structure:
Knowledge propagation works better when actors continue to exist between adventures. A rumor or correction should be able to arrive during downtime, through a workplace, household, club, archive, market or other durable social location instead of requiring every information exchange to be a formal quest scene.

Ouros translation:
Use fixed homes, workplaces and institutional routes as possible delivery edges. An NPC does not automatically hear regional news because the global simulation knows it.

## Source 6 — Pokémon Unbound mission structure: mission availability can depend on state and time

Sources:
- https://unboundwiki.com/missions/
- https://pokemonunboundpokedex.com/wiki/missions/

Public mission documentation shows a large mission catalogue with prerequisites, locations, progression gates and some time-sensitive availability. The useful lesson is that a mission can become discoverable because world/player state changed rather than because every NPC permanently displays every possible request.

Ouros translation:
Rumor-linked requests should appear only when the relevant source actor currently has the claim, the posting channel is available, and the concern has not already been superseded. Later corrections can retire or rewrite the posting.

No Unbound mission reward, trigger or progression formula is imported.

## Cross-source design conclusions

1. Local knowledge needs provenance: observer, time, location, channel and confidence.
2. Reports should distinguish observation from interpretation.
3. Cultural explanation, professional hypothesis and canonical causality can coexist as separate records.
4. An NPC can be wrong without being deceptive.
5. A claim can become obsolete without being deleted from history.
6. Corrections should propagate through actual social/institutional edges rather than globally.
7. Wild Pokémon behavior should be contextualized by observed conditions before being generalized to species temperament.
8. Some investigation rewards should be knowledge-state changes, route reclassification or institutional decisions rather than items.
9. Repeated observations from different positions/times can legitimately conflict.
10. Player-caused disturbances must remain possible inputs to later reports.

## PTU / Caelo cross-check

The project source priority remains PTU Core, Pokédex material, Caelo Player's Guide, Caelo rules/errata, character-creation material, Caelo Region Location & Encounter List, AutoPTU Python and the current Java port.

This pass makes no new mechanical claims about Channeler communication, Pokémon speech, sensing range, Knowledge Skill checks, weather effects, movement, wild disposition, encounter rolls, status conditions or Trainer Features. When a narrative beat requires a mechanical ability to obtain information, the exact ability/Feature must be checked against the source set and current engine contracts.

The existing repository rule remains in force: allegation, hypothesis, evidence, public belief and canonical truth stay separate.

## Current engine evidence relevant to these concepts

Read-only AutoPTU-Java head inspected for this pass: `8e5204b19f4aa83d96c573635be52c6e0e9092a3`.

The newest slice adds Shadow Tag through generic forced-movement candidate-step constraints. This is meaningful evidence for one more forced-movement composition path, but it does not prove the whole complete-movement family.

Conservative capability classification for encounter design in this pass:
- targeting/footprints/range/LoS: VERIFIED for current covered contracts;
- base movement legality: VERIFIED for current covered contracts;
- complete movement incl. push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED for current covered contracts;
- action economy/initiative: VERIFIED for current covered contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING as a complete family;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED for current covered contracts;
- AI tactical policy: BLOCKING as a complete tactical policy layer;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING as a complete family despite substantial individual presentation surfaces.

## Copyright / transformation note

No source dialogue, named fan characters, distinctive plot sequences or prose are imported. The research extracts state architecture and quest-design patterns only. All proposed Ouros actors, claims, sites and events must remain original and consistent with existing canon.