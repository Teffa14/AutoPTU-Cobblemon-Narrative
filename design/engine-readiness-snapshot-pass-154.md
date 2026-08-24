# Engine Readiness Snapshot — Pass 154

Status: evidence snapshot for narrative dependency planning. AutoPTU-Java and AutoPTU are read-only inputs.
Date: 2026-08-24

## Live revisions inspected

AutoPTU-Java `main`: `7be3c4d3a4edc3324a5953fa371c033a8acabab5` — `Preserve mutable move-special result state (#184)`.

The current Java head preserves Python-compatible shared mutable result state across move-special handlers. The dispatch context retains a shared mutable mapping while also preserving the dispatch-start `hit` snapshot. Immediately preceding work adds a generic move-special registry contract (`971699af`) and authoritative zero-damage Status Move execution (`1f9b721e`).

These are meaningful implementation slices for move-special behavior and Status-category execution. They do not prove catalog parity, complete Status lifecycle, generic environmental behavior or complete reaction handling.

AutoPTU Python `main`: `a3ff5cc71adb080973522abd604b0248b4447e06` — Career club-loan return preview/history behavior. Recent Python changes remain Career/persistence/presentation oriented and do not promote battle capability families.

Java still states that Python AutoPTU remains authoritative while the port is incomplete. The live README continues to list core combatant/grid state, full damage, status controller, terrain, hazards, forced movement, reactions, move/ability/item/perk/Trainer Feature registries, transcript parity, AI scoring/policy and Minecraft/Cobblemon adapter work as incomplete.

## Permanent capability map

| Capability family | Pass 154 status | Live evidence boundary |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Java README documents areas, footprints, anchors, ranges and LoS as implemented. |
| base movement legality | VERIFIED | Shift/Jump legality, movement modes, terrain costs, blockers and fit are documented as ported. |
| complete movement including push/pull/knockback/interception/forced movement | BLOCKING | Narrow reaction/push contracts exist, but forced movement remains explicitly incomplete. |
| core calculations | VERIFIED | Damage Base/type/stage/accuracy/weather/crit/Burn/modifier primitives are documented as implemented. |
| action economy / initiative | VERIFIED | Typed budgets and deterministic initiative/order variants are implemented. |
| full turn / round lifecycle | PARTIAL | Many lifecycle slices exist; complete battle-state/transcript parity does not. |
| full stateful damage pipeline | PARTIAL | Representative normal/delayed/multi-target/reaction paths exist; full damage remains incomplete. |
| status lifecycle | PARTIAL | Zero-damage Status-category execution and selected prevention/application slices exist; full controller/effect catalog is incomplete. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Exact PRE-damage reactions exist; the family remains explicitly incomplete. |
| move-specific behavior | PARTIAL | Generic move-special registry/result contracts now exist; move catalog/effect parity is incomplete. |
| abilities | PARTIAL | Selected Ability/reaction contracts have parity evidence; complete registry parity does not. |
| items | PARTIAL | Selected item paths exist; complete registry/hook parity does not. |
| Trainer Features / perks | PARTIAL | Generic gates/effects and selected interactions exist; catalog parity remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal `BattleChoice` action space is documented as implemented. |
| AI tactical policy | BLOCKING | Java README still lists scoring/policy over legal choices as pending. |
| Minecraft / Cobblemon / Craftics adapter / playback | BLOCKING | Java remains a standalone rules library; adapter integration is pending. |

## New Java evidence — move-special registry does not promote move-specific behavior

The recent Java sequence establishes more of the generic plumbing around Move special-effect dispatch:

- authoritative zero-damage Status-category execution;
- generic move-special registry dispatch ordering;
- shared mutable result state compatible with Python’s handler model;
- preserved dispatch-start hit snapshot while later handlers may mutate result fields.

It still does not verify:

- every Move handler;
- every Status effect;
- environmental Move effects;
- all Ability/Item/Feature hooks;
- generic interrupt/reaction ordering for the full catalog;
- all target scopes;
- complete semantic battle-event/transcript parity.

Therefore `move-specific behavior` and `status lifecycle` remain PARTIAL, while the combined `terrain/weather/hazards/zones/reactions` family remains BLOCKING.

## Pass 154 encounter dependency mapping

### Lock Chamber Evacuation — FULL

Required:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING if noncombatants, protected routes, chamber-edge displacement, interception or changing exits are represented tactically;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL as invoked;
- terrain/weather/hazards/zones/reactions — BLOCKING if water level, lock gates, chamber edges or generic reactions produce tactical effects;
- move-specific behavior — PARTIAL, exact Moves require evidence;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for `EVACUATE`, `PROTECT_ROUTE`, `WITHDRAW`, `CLEAR_EXIT`;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED: Navigation halts chamber movement and secures water/gates outside AutoPTU. Workers/passengers are evacuated in world state. A static safe arena receives actual combatants only. No moving water, vessel, crushing gate, civilian HP or lock physics is invented.

### Debris Boom Recovery at Navigation Reach — FULL

Required:

- targeting/base movement/core/action economy — VERIFIED foundations;
- complete movement — BLOCKING for protected technicians, moving retrieval objectives, withdrawal/interception or debris displacement;
- lifecycle/damage/status/move/ability/item/Feature categories — PARTIAL as invoked;
- terrain/weather/hazards/zones/reactions — BLOCKING if current, moving debris, water depth or unstable access affects tactics;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for `PROTECT_TECHNICIAN`, `RETRIEVE`, `WITHDRAW`, `CLEAR_ROUTE`;
- adapter/playback — BLOCKING.

REDUCED: Freshwater/Navigation isolate the work site. Technicians and debris handling stay outside the grid. A battle, if still necessary, occurs on a static bank/platform arena. Combat victory does not complete debris removal or certify navigation reopening.

### Wildlife Crossing During Lockage — FULL

Required:

- targeting/base movement/core/action economy — VERIFIED foundations if combat occurs;
- complete movement — BLOCKING for `CROSS`, `WITHDRAW`, `REACH_GROUP`, route protection or interception;
- lifecycle/damage/status/move/ability/item/Feature families — PARTIAL as invoked;
- terrain/weather/hazards/zones/reactions — BLOCKING if approach water/lock state changes tactically;
- AI legal-action infrastructure — VERIFIED only as legal-choice generation;
- AI tactical policy — BLOCKING for non-hostile ecological objectives;
- adapter/playback — BLOCKING.

REDUCED: lockage is suspended and wildlife movement resolves in world state. If an independent hostile encounter remains afterward, AutoPTU receives a conventional static arena. Crossing success never changes capture eligibility, ownership, population truth or migration truth by itself.

### Lock Queue Dispute

No battle capability is inherently required.

Navigation, Travel, Public Information and Institutional Review resolve queue records, priority claims and stale estimates. A battle result cannot decide operational priority unless an authored institution explicitly defines such a procedure.

## Pass 154 world-state blockers

These belong outside AutoPTU-Java:

- inland-waterway network identity;
- navigation-reach state;
- maintained-channel revisions;
- navigation-clearance assessments;
- lock-complex identity and operating state;
- lockage-event history;
- lock queues and public wait estimates;
- vessel/service asset identity;
- inland passenger/cargo service state;
- navigation restrictions;
- water-use/navigation decisions;
- alternate-route handoffs;
- navigation public information and actor knowledge;
- navigation state -> Travel journey handoff;
- navigation state -> Supply Chains/Postal delay handoff;
- wildlife/ecology -> temporary navigation restriction;
- navigation state -> Minecraft presentation;
- frozen navigation incident -> battle-contract selection.

## Mechanical non-inferences

Pass 154 does not authorize:

- visible current as forced movement;
- water blocks as Water Terrain;
- low water as movement penalty;
- lock gates as crushing-damage hazards;
- vessel movement as moving-platform rules;
- ferry/barge collision damage;
- drowning or falling rules;
- boat/vessel initiative;
- cargo as cover;
- Sailor/Fisherman occupation as PTU qualification;
- Water type as current resistance;
- Electric type as lock-control access;
- Strength as towing/cargo capacity;
- large body size as passenger/cargo capacity;
- wildlife blockage as hostility/capture authorization;
- completed battle as completed lockage;
- Minecraft gate/piston state as authoritative navigation state;
- recent generic Move-special plumbing as proof of any environmental Move effect.

## PTU / project evidence

The narrative layer has no authority to invent navigation or vessel mechanics.

Any FULL encounter requiring currents, dynamic water, moving vessels, drowning, falls, forced movement, reactions, environmental zones or objective-aware AI must stay behind the corresponding capability categories until exact PTU/Caelo plus engine evidence exists.

The current project evidence does not justify promoting those families.

Super PTU Online Helper was not exposed as an invocable capability in this run. No output is invented or attributed to it.

No reliable primary Caelo rule defining inland navigation locks, vessel operation, currents or canal-specific environmental combat was recovered in this run.

## Open mechanical/canon questions

- Does Ouros have engineered canal/lock systems at campaign start?
- Which waterways are navigable by passenger craft, cargo vessels or research/rescue craft?
- Who operates locks, navigation notices and maintenance programs?
- Are navigation clearances qualitative or numerically modeled?
- Which ecological movements can create temporary navigation holds?
- How does navigation interact with water-supply, habitat, flood-control or power decisions in authored regions?
- Can players or player organizations own/operate inland vessels or services?
- Which Pokémon participate voluntarily in inland navigation institutions?
- What PTU/Caelo rules, if any, govern vessels, currents, moving platforms, drowning, Swim, towing/carrying and environmental water?
- If a battle occurs on a vessel, must Ouros freeze the vessel before AutoPTU handoff until moving-platform support exists?
