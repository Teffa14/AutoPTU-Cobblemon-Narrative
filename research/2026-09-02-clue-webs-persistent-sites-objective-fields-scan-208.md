# Pass 208 Research — clue webs, persistent sites and objective-shaped battlefields

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-02

## Scope

This pass looks for structures that can make an Ouros investigation, route or dungeon replayable without turning it into a linear quest chain or creating a new isolated location for every objective.

The focus is three reusable ideas:

1. redundant clue webs that preserve player route choice;
2. persistent spaces that support different jobs on different visits;
3. battlefields whose physical identity matters, while keeping tactical environmental rules behind AutoPTU capability gates.

No external plot, named character, dialogue, faction, dungeon, reward or combat rule is imported into Ouros canon.

## Internal project evidence inspected

Before writing this pass, the repository recursive tree and current internal layers were inspected, with targeted reads of the canon and implementation-facing files that own this subject:

- `README.md`;
- `canon/README.md` and current canon file inventory;
- `canon/ouros-playable-foundation-v1.md`;
- `canon/marea-interior-map-resident-network-v2.md`;
- `canon/marea-interior-first-wild-population-v1.md`;
- `canon/questline-taxonomy-v2.md`;
- `research/2026-09-02-wildlife-signs-observation-telegraphing-scan-207.md`;
- `design/engine-readiness-snapshot-pass-207.md`;
- `sources/kairos/KAIROS_SOURCE_INDEX.md` and current source inventory.

Searches across the narrative repository for `Alexandrian`, `Mystery Dungeon` and `Conquest` returned no prior indexed material. This pass therefore adds new provenance rather than repeating the wildlife-observation work in pass 207.

Current narrative head before this write: `e6204de10d4878137f2983ed80042c1be37225f1`.

## Public research

### The Alexandrian — node-based scenario design and clue redundancy

Sources:

- https://thealexandrian.net/creations/misc/node-design/node-design.html
- https://www.thealexandrian.net/creations/misc/node-design/node-design2.html

Reusable structure:

A linear sequence creates chokepoints when one missed conclusion blocks the only next scene. Node-based design instead prepares situations/locations/actors and places multiple links between them. The Three Clue Rule supplies redundancy: an important conclusion should have multiple independent ways to reach it. The inverted form suggests that several clues pointing toward several nodes make it likely that players can choose at least one productive direction without the GM prescribing order.

Ouros transformation:

- a world investigation should store evidence edges between existing world entities instead of one `quest_step_next` chain;
- mandatory world facts should not depend on one successful Skill check or one NPC conversation;
- evidence can point to more than one next site;
- visiting a node can produce new evidence, contradict an existing hypothesis, or strengthen provenance without requiring a predetermined sequence;
- class/Skill advantages should improve interpretation, efficiency, safety or extra context where PTU/Kairos rules support them, rather than hiding the only continuation behind a roll.

This fits the canon Thin Delivery Season especially well because its cause is intentionally unresolved and already has several evidence owners.

### Pokémon Mystery Dungeon — one persistent dungeon, many job objectives

Sources:

- https://bulbapedia.bulbagarden.net/wiki/Job_(Mystery_Dungeon)
- https://bulbapedia.bulbagarden.net/wiki/Tiny_Meadow
- https://bulbapedia.bulbagarden.net/wiki/Normal_Maze

Reusable structures:

Mystery Dungeon repeatedly sends players into known spaces for different objective families: rescue a target, deliver or find an item, defeat an outlaw, escort, reach a destination, train, or progress through a short maze. The same named space can therefore gain new purpose without being replaced by a one-use set piece. Short training dungeons can also establish a simple escalation grammar: ordinary traversal, altered visibility/terrain, then a culminating opponent.

Ouros transformation:

- Sendero del Vidrio, Estación Mirador transects, Tideglass Archive, Bruma Battle Yard and future dungeons should support multiple authored objective contracts over time;
- a visit reason belongs to the quest episode, while the physical site's history and state remain persistent;
- an objective should reference a specific target/world object when one exists instead of spawning an unrelated replacement;
- repeated visits should be justified by changed world state, different stakeholders, new access or a different objective, not by resetting the place to a generic dungeon instance.

No Mystery Dungeon floor generation, rescue rank, recruit rate, item table, trap probability, turn limit or job reward is imported.

### Pokémon Conquest — battlefield identity through physical rules

Sources:

- https://bulbapedia.bulbagarden.net/wiki/Aurora
- https://bulbapedia.bulbagarden.net/wiki/Pugilis
- https://bulbapedia.bulbagarden.net/wiki/Valora
- https://bulbapedia.bulbagarden.net/wiki/Viperia_Kingdom
- https://bulbapedia.bulbagarden.net/wiki/Spectra_Kingdom

Reusable structures:

Conquest battlefields are memorable because the location participates in the encounter: movable logs, edge drops, bells, moving machinery, fences, secret passages, condition-causing tiles, moving hazards and explicit turn/victory conditions. The important narrative lesson is not the exact gimmick. It is that a battlefield can express where the battle is taking place and what that place normally does.

Ouros transformation:

- a tactical map may eventually expose location-authored interactables whose effects are resolved by AutoPTU, not Minecraft;
- route crossings, work yards, archives, stations and ruins can have objective geometry tied to their normal world function;
- tactical terrain should be authored as semantic encounter data with clear engine dependencies and playback projection;
- Minecraft blocks may visually represent a bridge, gate, shelf, cart, machine or flooded patch, but block presence alone must never create PTU damage, forced movement, status or legality.

No Conquest stat-stage bells, poison tiles, crane displacement, turn limits, status fireballs or kingdom-control rules are imported.

### PokémonTabletop community — campaign premise can constrain encounter cadence

Source:

- https://www.reddit.com/r/PokemonTabletop/comments/z24ni1

This public PTU campaign advertisement describes an undercover/heist campaign where catching everything is explicitly not the intended loop. It is weak evidence about rules, but useful evidence that PTU campaign identity can be built around investigation, infiltration and selective battles rather than continuous capture.

Ouros transformation:

Quest identity determines what information or decision matters. A wild Pokémon or battle can be important without automatically becoming the objective or reward.

## PTU / Kairos cross-check

The current project index routes the authoritative mechanics relevant to this design to the supplied Kairos/PTU material: Skills/Features in chapters 3–4, movement/terrain in the combat chapter, status/hazards/terrain/weather in the combat rules, campaign structure in the GM chapter, encounter creation around p. 470, recurring rivals/villains around p. 477 and boss encounters around p. 485.

This pass does not invent any DC, Skill substitution, movement rule, terrain effect, hazard damage, reaction, boss action, turn limit or reward. Those details require exact source-page verification and then current engine-contract verification before implementation.

The Kairos living-world evidence also supports persistent characters and one-shot quest sessions in a shared world. Ouros can use that structural lesson while keeping its own canonical world-state authority and avoiding Kairos-specific homebrew content.

## Derived design candidate: evidence graph, not quest staircase

Proposed non-canon schema:

```text
EvidenceNode
  evidence_id
  subject_arc_id
  source_entity_id
  observation_or_record_ref
  provenance_class
  supports_hypothesis_ids[]
  weakens_hypothesis_ids[]
  reveals_node_ids[]
  interpretation_contract_ref?
  published_to_ids[]
  acquired_at_world_time
```

The quest system should distinguish:

- `ACCESS`: the player can reach or speak to a source;
- `OBSERVATION`: a direct fact is available;
- `INTERPRETATION`: an authoritative rules check or expert conclusion adds meaning;
- `LINK`: evidence reveals another productive node;
- `PUBLICATION`: private findings become available to an institution/group;
- `CONCLUSION`: the arc has enough evidence for a canonical world update.

A conclusion must not be silently written because the player collected a fixed number of clues. The conclusion rule must name the required evidence relationships or an explicit adjudication/decision process.

## Derived design candidate: persistent-site objective contract

Proposed non-canon fields:

```text
SiteObjectiveContract
  contract_id
  site_id
  quest_episode_id
  world_state_preconditions[]
  objective_type
  target_entity_refs[]
  success_world_writes[]
  failure_or_transform_writes[]
  battle_contract_ref?
  capability_requirements[]
  reduced_contract_ref?
```

Candidate objective types are descriptive only until implementation review: inspect, retrieve, deliver, escort, protect, reach, document, repair, negotiate, contain, train, challenge, evacuate, pursue.

These labels do not define PTU mechanics by themselves.

## Mechanically rich encounter concept

### Full intended version — Seasonal Crossing Evidence Race

Premise: Thin Delivery Season has produced conflicting claims about Sendero. Two or more evidence owners need a same-day verification at the seasonal crossing before weather/traffic changes the observable state. The players can approach through different evidence nodes first, so they arrive with different context. At the crossing, a localized confrontation may occur only if current ecology or actor state supports one.

The full tactical version makes the crossing itself legible: safe shelf, unstable edge, blocked route object, observation point and one or more interactable environmental anchors. An objective may require holding access to an observation point, protecting a recorder, reaching a route object or disengaging safely rather than defeating every opponent.

Required capability families:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement if edges, shoves or interception matter;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle for timed/multi-stage objectives;
- full stateful damage pipeline;
- status lifecycle if any legal move/status participates;
- terrain/weather/hazards/zones/reactions for crossing effects or reactive environmental rules;
- move-specific behavior;
- abilities;
- items if field tools become mechanically active;
- Trainer Features/perks for mechanical field actions or interrupts;
- AI legal-action infrastructure;
- AI tactical policy for objective-aware opponents/protectors;
- Minecraft/Cobblemon/Craftics adapter/playback support.

### Reduced implementation — Same investigation, ordinary battle optional

The same narrative premise can run now with:

- static crossing geometry as presentation only;
- several evidence nodes reachable in any order;
- direct observations that do not require a roll;
- optional authoritative interpretation only where a verified Skill service exists;
- no tactical weather, hazard cell, forced movement, reaction, delayed effect or environmental damage;
- one ordinary audited battle only if current world state produces a legal confrontation;
- success based on collecting/publishing the required evidence relationships, not on battle victory.

If the canon lower-shelf Fletchling appears, it must remain the existing server-owned individual/blueprint and cannot be repurposed as the cause of Thin Delivery Season or as a mandatory opponent.

## Capability state inherited from live evidence

AutoPTU-Java head remains `496f7e15dbc4bb547449727cd60cd397d8d9005a`. AutoPTU head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Neither repository has advanced since pass 207, so no capability family is promoted.

Current classification for this concept:

- targeting/footprints/range/LoS — VERIFIED within audited contracts;
- base movement legality — VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED within audited contracts;
- action economy/initiative — VERIFIED within audited contracts;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING as a complete family;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED within audited contracts;
- AI tactical policy — BLOCKING for complete objective-aware behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for the complete end-to-end target.

## Rejected imports

Do not import:

- a literal three-clue counter that auto-solves mysteries;
- Alexandrian sample plots, locations or characters;
- Mystery Dungeon floor generation, rescue ranks, recruit math, traps or reward tables;
- Conquest battlefield stat buffs, status tiles, crane rules, turn caps or territorial conquest system;
- mandatory Skill rolls for clues required to continue;
- Minecraft-owned terrain damage/displacement/status rules;
- a battle victory as proof of a noncombat hypothesis;
- new NPCs or factions where Marea's existing network already owns the evidence role.

## Product criterion

This research succeeds when one persistent Ouros location can support several different future episodes, while an investigation can continue through multiple evidence routes even if the player ignores one source, fails one optional interpretation or chooses not to fight.