# Engine Readiness Snapshot — Pass 68

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.
Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live Java evidence

Newest inspected AutoPTU-Java commit:

`57c7c2a9751cf02facf5d176b9d0f95b996a9bd1` — Use effective Accuracy in authoritative move preparation (#230).

This is the same Java head inspected by Pass 67. It strengthens one concrete Accuracy path by using effective Accuracy during authoritative move preparation. It does not establish a complete Trainer Feature registry, a complete move-specific runtime, a complete battle lifecycle, objective-aware tactical AI or a Minecraft/Cobblemon adapter.

The current README still reports implemented slices for:

- targeting, areas, footprints, target anchors and LoS;
- Shift and jump movement legality;
- Damage Base/type tables and calculation primitives;
- stages and accuracy-stage primitives;
- weather DB as a calculation primitive;
- invariant d20 accuracy resolution;
- combat-stat resolution;
- typed turn flow and action budget;
- deterministic initiative;
- legal autobattler action-space generation.

The same README still explicitly leaves unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

No capability category is promoted by Pass 68.

## Live Python evidence

Newest inspected AutoPTU commit:

`6be09cdf3fb26a5a36fc9cf4dc02633c77b8c0f7` — Career: harden current rival season authority.

Immediately preceding commits fail closed on malformed current rival season state and narrow validated values before arithmetic. These are persistence/career-authority changes. They do not add PTU tactical capabilities or Minecraft adapter behavior.

## Permanent capability map

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

## Physical-information authority boundary

Pass 68 can determine:

- which information surface exists in narrative/world state;
- where the surface is located;
- which posted notice instance is displayed;
- which source information/state object it references;
- when the notice was posted, superseded, removed or archived;
- observed physical condition/readability;
- which actor saw which readable claims;
- whether a surface carries a specific map edition or schedule projection;
- whether the physical display is stale relative to current authoritative state.

Pass 68 cannot determine:

- canonical truth merely from displayed text;
- ownership or legal authority without an established mandate;
- route openness merely because a sign was removed;
- service operation merely because a timetable says so;
- map truth merely because a map is visible;
- PTU combat modifiers;
- tactical terrain/weather/hazards;
- forced movement or reactions;
- battle objective legality;
- AI tactical priorities;
- mechanical Skills, Edges, Moves, Abilities, Items or Trainer Features.

## Minecraft projection caution

Physical signage is especially prone to accidental dual-authority bugs.

Unsafe architecture:

Minecraft sign exists -> world state is edited to match sign.

Required architecture:

authoritative narrative/system state -> posted_notice projection -> Minecraft object/UI.

World interactions with the physical object may create observations or authorized update requests. They must not bypass the owning system.

Examples:

- breaking a closure sign cannot reopen a route;
- replacing a timetable panel cannot restore a suspended service;
- editing sign text cannot change an institutional request;
- copying a map texture cannot reveal undiscovered geography in actor knowledge;
- an NPC quest icon cannot create a request record if the source request does not exist.

## Encounter review — Trailhead Update Under Pressure

Narrative premise:

A trail restriction changes and an authorized team needs to replace visible guidance while a local battle-capable threat makes the immediate area unsafe.

Intended full version may require:

- noncombatants withdrawing through legal routes;
- a protected work position or CLEAR_ROUTE/PROTECT objective;
- changing access lanes;
- interception or forced displacement;
- terrain/weather/hazard mapping where governing PTU/Caelo rules establish it;
- territorial, denial or withdrawal-aware tactical AI;
- semantic objective events;
- adapter playback that preserves the exact route state and exact notice revision.

Dependency state:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when active
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback support — BLOCKING

Reduced version:

Evacuate workers in world state before battle. Keep the restriction authoritative outside tactical state. Run a static reviewed encounter near the trailhead using only supported mechanics. After the authoritative AutoPTU result, the owning route/ecology/maintenance system decides access state and Pass 68 projects the resulting notice revision.

Battle victory cannot reopen the trail by itself.

## Encounter review — Station Notice Replacement

Narrative premise:

A timetable or service-status panel contains stale information during a transport/service interruption. Replacing it requires access to an area currently unsafe because of a battle-capable threat.

Intended full version may require:

- civilian withdrawal;
- protect/access objective state;
- dynamic doors, barriers or access lanes;
- interception/forced movement;
- non-KO tactical priorities;
- semantic objective events;
- synchronized adapter writeback separating service state from display state.

Dependency state:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING if active
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback support — BLOCKING

Reduced version:

Clear civilians first. Freeze the service in the authoritative state owned by Travel/Transit. Resolve a static legal encounter away from operational controls. After AutoPTU returns its result, update the information panel as a separate world-state action.

A battle result cannot prove the previous schedule fraudulent, repair transport infrastructure or restore service.

## Noncombat readiness — Three Boards, Two Updates

This mystery can run before new tactical capabilities.

Required narrative state:

- stable notice IDs;
- source information/state refs;
- posting times;
- effective windows;
- supersession/revision edges;
- physical readability observations;
- actor knowledge created from observed notice versions.

No battle engine rule is needed to reconstruct the discrepancy.

Actual physical materialization inside Minecraft still depends on the BLOCKING adapter/playback family.

A text/UI prototype outside the final adapter can represent the same state earlier, provided it does not become a parallel authority layer.

## Noncombat readiness — request-board projection

A public request board can function with existing narrative state if:

- the request already exists;
- visibility is authorized/plausible;
- the board projects a limited summary;
- acceptance/completion remains owned by the request system;
- removal from display does not mutate completion.

This feature does not need new PTU combat mechanics.

Minecraft interaction and persistent physical rendering still require adapter work.

## Why signage does not change the tactical capability map

A sign, map board, timetable or poster is overworld information presentation.

No current Pass 68 concept needs to create:

- Accuracy modifiers;
- damage modifiers;
- movement penalties;
- initiative changes;
- status effects;
- terrain effects;
- weather effects;
- reactions;
- Trainer Feature triggers.

Therefore the narrative layer can advance independently while rich battle scenes continue to expose their exact missing families.

## Adapter implications

Safe future adapter behavior:

- each displayed object references a stable narrative notice/surface ID;
- text/texture is derived from current display state, not treated as authority;
- stale notices may intentionally persist when narrative state says so;
- interacting records an observation of what was readable;
- map boards reference a specific map edition;
- schedule panels reference a specific service schedule version;
- destroyed/damaged props update physical display state only unless another authorized system responds;
- corrections may propagate to different surfaces at different times;
- quest icons project existing request state rather than inventing it.

Unsafe shortcuts:

- direct Minecraft block state controls canonical route/service state;
- every board is globally synchronized regardless of location/update cadence;
- old notice text disappears from actor history when replaced;
- sign damage is automatically classified as vandalism;
- a missing notice proves sabotage;
- a public poster grants institutional authority;
- displayed route safety suppresses ecology or encounters;
- a board reveals hidden/private requests for convenience.

## Promotion gates for full encounter versions

Before Trailhead Update Under Pressure or Station Notice Replacement can run in their intended rich form, current evidence is still needed for the exact mechanics actually selected, including where applicable:

- objective lifecycle for CLEAR_ROUTE/PROTECT/ACCESS/WITHDRAW;
- complete forced movement/interception;
- terrain/weather/hazard mapping;
- full lifecycle timing;
- complete Move/Ability/Item/Feature interactions used by participants;
- tactical AI scoring non-KO objectives;
- semantic transcript events for objective changes;
- adapter playback that keeps service/restriction/notice state distinct.

Representative helpers remain insufficient.

## Unresolved mechanical questions

- Which non-DEFEAT objective family will AutoPTU port first?
- How will noncombatants or protected work positions be represented without creating a second combat engine in Minecraft?
- Which semantic transcript events will represent route access, withdrawal and protected-objective state?
- How will adapter playback distinguish an overworld barrier/notice from tactical terrain or a battle objective?
- Can a future battle interact with a sign physically without allowing destruction of the prop to alter underlying policy?
- How should authoritative battle aftermath request a world-state notice update without writing directly into Media/Travel/Public Space owners?

## Unresolved canon questions

- Which Ouros settlements use public boards or fixed information surfaces?
- Which institutions can issue official notices in each region?
- Are physical posting practices standardized, local or mixed?
- Which places use static paper/signage versus dynamic panels?
- What accessibility conventions exist for notices and maps?
- What privacy constraints govern publicly posted requests?
- Who maintains surfaces and removes expired notices?
- Which superseded notices are archived or preserved in Public Memory?
- How much content should be directly legible in-world versus opened through an interaction UI?

Until reviewed, all Pass 68 material remains proposed/non-canon.
