# Layered Field Jobs + Resource Reconciliation Scan — Pass 394

Status: RESEARCH / PROVENANCE. Not canon.
Date: 2026-09-09

## Repository-first deduplication

The current repository tree, canon directory, current focus, Pass 393 readiness snapshot, resource owners, recent research anchors and source index were inspected before selecting sources.

Frequently reused material was excluded, including Tales of Visiwa, Pokémon Unbound, Gaia, Wastelands, Rejuvenation, Desolation, Infinity, Bushido, Odyssey, Prisme, Valoryn, Stalactite, Clockwork, Tectonic, Empyrean, Xenoverse, Altair/Sirius, Historic England, CIfA, Collections Trust, FEMA/NIMS, CIDOC and Apache Flink.

This pass uses a newer public PTU actual-play episode description plus Pokémon sources that add a different mission-structure angle. It does not import protected characters, dialogue, maps, plots, custom species or bespoke mechanics.

## Source 1 — The Reckless Rollers, current PTU actual play

Source:
https://podcastaddict.com/podcast/the-reckless-rollers/2836264

Public episode metadata inspected on 2026-09-09 includes `FTTC 13: The Freeing of Connor Lezinsky` (2026-06-01) and `FTTC 14: Let's Solve A Moidah` (2026-06-15). The descriptions present two useful high-level patterns: a crew can have one explicit job while unrelated obligations continue in parallel, and a social location such as a hotel can become an investigation site without ceasing to be an ordinary place.

Reusable Ouros lesson:

A field assignment does not need to suspend personal errands, relationship obligations, institutional messages or local incidents. The world-agent layer can let several objectives coexist, with actors choosing what they can actually pursue from current knowledge, schedule and resources.

Do not copy the campaign crew, murder, hotel case, names, dialogue, science-fiction setting or episode plots.

## Source 2 — Pokémon Mystery Dungeon mission-board taxonomy

Sources:
https://strategywiki.org/wiki/Pok%C3%A9mon_Mystery_Dungeon%3A_Explorers_of_Time_and_Explorers_of_Darkness/Chapter_2%3A_The_New_Guild_Recruits
https://bulbapedia.bulbagarden.net/wiki/Mystery_dungeon

Public guides distinguish rescue, escort, delivery, outlaw capture and item-retrieval jobs while reusing dungeon exploration as a common activity space. Dungeons may also impose special floor conditions such as weather or reduced sight.

Reusable Ouros lesson:

One route or site can support multiple objective families. The objective should be explicit and can change what counts as success even when the physical map is the same. A rescue, delivery and evidence-gathering trip should not collapse into the same KO condition.

Ouros should not import guild characters, badges, randomized floor rules, rescue teleportation, dungeon layouts or specific Mystery Dungeon story material.

## Source 3 — Pokémon Coral Version

Sources:
https://www.pokemoncoders.com/pokemon-coral/
https://www.pokeharbor.com/2021/05/pokemon-coral-version/

The public descriptions emphasize an explorable region with optional areas and events around a comparatively simple main progression. That separation is useful because environmental curiosity can remain worthwhile without every cave, side path or local event becoming a main-story gate.

Reusable Ouros lesson:

Author optional field jobs as consequences of places and people rather than as mandatory detours. A player can discover a side assignment while already travelling for another purpose. The assignment can remain unresolved, be delegated to an NPC team, or be revisited later if the world state still permits it.

Do not import Onwa, its antagonist group, locations, characters, custom art, species availability, plot or ROM mechanics.

## Source 4 — Pokémon Reborn field-effect structure, used only as a dependency warning

Source:
https://pokemon-reborn.fandom.com/wiki/Field_Effects

Reborn uses location-sensitive battle environments whose fields can modify move behavior and can sometimes transform into other fields. The useful lesson is not the specific mechanics. It is that environment can be mechanically meaningful enough to change tactical assumptions.

For Ouros this source is primarily a warning: a rich encounter that changes terrain, weather, zones or Move behavior cannot be implemented as narrative flavor and then assumed to work tactically. Every exact environmental mechanism must be gated against current AutoPTU contracts.

Do not import Reborn field names, modifiers, transformations, formulas or location mappings.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked as a router only. Relevant routes include campaign/session structure, encounter creation, movement/terrain, status, hazards, terrain/weather, recurring rivals, boss encounters, Items/Gear and utility classes. The index explicitly does not grant Ouros acceptance.

This pass therefore defines no new Skill check, Edge, Trainer Feature, Item effect, mission reward formula, environmental modifier, weather rule or tactical interrupt.

## Read-only engine evidence

AutoPTU-Java main advanced to `19dd2d9b99d81f8479c73e6ef4709a30f0794474`, merge #421, after Pass 393. The merge freezes additional Impostor negative-guard parity and touches lifecycle-hook registration. This is stronger evidence for those exact tested seams only. It does not verify the complete Abilities family or complete turn/round lifecycle.

AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its latest commit is presentation-only viewport-coordinate synchronization.

Neither engine is modified by this pass.

## New implementation lesson — reconciliation must preserve uncertainty

The current `WorldResource` catalog is a present-state owner. Reservation and handoff ledgers are historical owners, but they do not journal every legal resource mutation. Therefore recovery should distinguish three outcomes:

- confirmed compatibility when present state agrees with a directly comparable historical fact;
- proven conflict only when explicit claims cannot both be true;
- indeterminate when history is insufficient to derive present state.

This avoids converting an incomplete log into false omniscience.

## New narrative structure

Candidate: `Three Jobs on the Same Road`.

A travelling group begins with one assigned field task. At an intermediate settlement it learns about a small delivery that shares most of the route. A later message reports a stranded surveyor near the destination. The three objectives overlap geographically but have different deadlines, resource needs and success conditions.

NPC teams can pursue tasks the player declines. Resource history can create believable friction: a field kit may have a valid reservation record while the current catalog has not projected it, or a custody record may show an earlier holder while the item has since been legally returned. The reconciliation layer exposes uncertainty instead of rewriting the world to make the records agree.

This proposal should remain region-neutral until canon binds it to a place or institution.

## Reduced encounter version

The reduced version needs no AutoPTU battle.

It uses world travel, semantic time, explicit knowledge delivery, schedules, resource readiness, reservations, current resource catalog, reconciliation findings and ordinary quest state. Each objective can complete through arrival, delivery, contact or evidence state.

## Rich encounter version and permanent capability dependencies

If a local confrontation occurs on stable geometry with ordinary attacks only, targeting/footprints/range/LoS, base movement legality, core calculations, audited action economy/initiative and ordinary AI legal-action infrastructure can use their currently verified scopes.

Escort movement, body-blocking, push/pull, knockback, interception or forced rescue reposition require complete movement and remain PARTIAL.

Timed rescue windows, environmental phase changes or delayed collapse require full turn/round lifecycle and remain PARTIAL.

Persistent objective damage or injury consequences require the full stateful damage pipeline and remain PARTIAL.

Complex conditions require status lifecycle and remain PARTIAL.

Weather changes, visibility zones, hazards, reactions, unstable surfaces or field transformations require terrain/weather/hazards/zones/reactions and remain mechanism-specific MIXED / PARTIAL / BLOCKING.

Any special Move, Ability, Item or Trainer Feature used to manipulate those conditions remains individually gated.

AI legal-action infrastructure is verified only within audited ordinary scopes. AI tactical policy remains BLOCKING for escort-first, rescue-first, protect-cargo, deliver-objective, split-task coordination, objective-aware withdrawal and disengage-after-objective.

Minecraft/Cobblemon/Craftics adapter/playback remains PARTIAL / BLOCKING for authoritative objective acknowledgement, persistent resource projection, escort/rescue state and non-KO completion playback.

## Canon questions deliberately left open

No settlement, road, institution, delivery object, stranded surveyor, faction, species, hazard, reward or PTU class is established here.

No assumption is made that the player must accept all objectives, that an NPC team succeeds off-screen, or that a resource-history mismatch implies theft or deception.
