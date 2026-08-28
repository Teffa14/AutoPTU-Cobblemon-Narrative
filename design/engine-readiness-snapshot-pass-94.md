# Engine Readiness Snapshot — Pass 94

Status: implementation-readiness evidence for Narrative authoring. This file does not establish Ouros canon or claim complete engine support beyond cited live evidence.

Date: 2026-08-28

## Evidence inspected

Narrative baseline before Pass 94:
- `Teffa14/AutoPTU-Cobblemon-Narrative` main at `2de7fe08d0d61b9872512c6e833ce7bbfde2b117`.
- Recursive repository tree inspected with `truncated=false` before choosing the new research gap.
- Directly overlapping Pokémon Agency, Care/Recovery/Welfare, Conservation, Breeding/Nursery and Pass 93 readiness documents reviewed.

Read-only engine repositories:
- `Teffa14/AutoPTU-Java` main at `8eca19e141568efa2b0e5e0307f6e0b7627e39a4`.
- `Teffa14/AutoPTU` main at `a7e7cbbd65febbed4a1f23c97e56f5f2d83594a6`.

Neither engine repository was modified by Pass 94.

## Live Java delta since Pass 93

AutoPTU-Java advanced from `538b0ed5e81e427e94397382f5a33a763a776bab` to `8eca19e141568efa2b0e5e0307f6e0b7627e39a4` through #254, `Apply intercept resources authoritatively`.

The new runtime slice applies server-owned resource mutations after a successful Intercept candidate has already been selected and the Intercept check has succeeded.

Current covered behavior in that slice includes:

- prepared Intercept consumption of one `intercept_ready` temporary effect;
- one-shot consumption of `coaching_intercept` after a successful Intercept;
- Sentinel Stance consumption of the base or extra SHIFT resource;
- retention of Sentinel Stance where Python retains it;
- Sentinel Stance damage-reduction output in the resource result;
- Weaponize source classification without consuming ordinary movement action;
- pre-mutation validation so stale candidates fail before unrelated resources are consumed;
- pinned Python-oracle parity tests.

The implementation boundary explicitly states that this component does not choose an interceptor, roll RNG, move combatants or resolve damage. Minecraft/Cobblemon therefore never decides which PTU resources are spent.

This is meaningful progress in the Intercept chain and action/lifecycle integration. It does not prove the complete movement family or the complete reaction system.

## Current Java architectural status

The live README still states the target boundary:

AutoPTU-Java decides legal actions and battle results. Minecraft/Cobblemon/Craftics adapt world state and render resulting events.

The broad pending checklist still includes:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement and reactions as broad families;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- semantic event emission and full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Recent slices can be more advanced than the broad checklist wording for one behavior. That does not justify marking the whole family complete.

## Python AutoPTU delta

Python AutoPTU advanced from `2de71fb314ca573806b96c538d4fc2b34c755b78` to `a7e7cbbd65febbed4a1f23c97e56f5f2d83594a6`.

The latest merged work defers Career run-API loading until a route requests it. This improves browser/application startup behavior. It does not add evidence for a tactical capability family and causes no readiness promotion.

## PTU mechanical evidence relevant to Pass 94

PTU 1.05 already defines Loyalty and Command behavior.

The source material includes low-Loyalty Command checks and examples involving rescued or mistreated Pokémon. It leaves Loyalty changes under GM determination.

Therefore the shelter/sanctuary design may store provenance such as care events, observed cooperation, refusals and placement history, but narrative code must not:

- assign Loyalty ranks;
- modify Loyalty;
- calculate Command DCs;
- alter movement or Ability state to represent rehabilitation;
- fabricate trauma/status mechanics;
- infer battle commandability from successful foster/placement.

No new Caelo-specific shelter/placement mechanic was established from searchable project evidence in this pass. That remains unresolved rather than being replaced with a narrative rule.

## Permanent capability map

```yaml
capabilities:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: PARTIAL
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: PARTIAL
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

No family is promoted in Pass 94.

## Why complete movement remains PARTIAL

Evidence now includes substantial slices:

- Shift and Jump legality;
- Push/Pull forced displacement;
- collision and partial-stop behavior;
- authoritative position mutation;
- Intercept candidate discovery and materialization;
- eligibility and attempt gates;
- check resolution;
- geometry and candidate positioning;
- committed interceptor movement;
- one melee Intercept plus Push 1 composition;
- temporary-effect cleanup;
- resource mutation/consumption contract;
- authoritative application of successful Intercept resources.

Still insufficiently general or missing:

- complete reaction lifecycle across all trigger sources;
- competing reaction ordering/conflicts;
- broad knockback coverage;
- all forced-displacement sources;
- broad Move integration;
- broad Ability integration;
- broad Item integration;
- broad Trainer Feature/perk integration;
- environment-driven displacement;
- objective-aware tactical AI;
- complete semantic transcript and Minecraft playback.

The Intercept path is increasingly mature, but one mature path cannot stand in for the complete family.

## Shelter-specific implementation consequences

The following remain narrative/world-state concerns unless authoritative mechanics exist:

- shelter intake and placement status;
- custody/ownership/registration transitions;
- foster or sanctuary residence;
- willingness to interact with a prospective caretaker;
- release readiness;
- trauma or behavioral diagnoses;
- enclosure safety effects;
- crowding effects;
- quarantine effects;
- gate or barrier combat effects;
- evacuation/protection objectives;
- resident Pokémon behavior during a crisis.

A Pokémon appearing in a Cobblemon shelter yard must remain an overworld resident until Ouros explicitly selects it for a BattleSpec.

## Encounter readiness — Shelter Yard Withdrawal

Full version requirements:

```yaml
encounter: Shelter Yard Withdrawal
requirements:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: PARTIAL
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: PARTIAL
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

Current authoring profile: REDUCED.

Reduced form:

- complete staff/resident evacuation staging through world state before battle;
- keep shelter residents outside the tactical grid unless explicitly selected by Ouros;
- use a static reviewed arena outside the protected residential spaces;
- make gates, pens, carriers and care equipment non-targetable scenery;
- keep any crowding/environmental presentation mechanically neutral;
- resolve return-to-yard state after the authoritative result.

## Encounter readiness — Transfer Handoff Interruption

Full version particularly depends on:

- complete movement: PARTIAL;
- reaction behavior: BLOCKING as part of the broad terrain/weather/hazards/zones/reactions family;
- objective-aware AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING;
- applicable lifecycle/damage/status/Move/Ability/Item/Feature behavior: PARTIAL by family.

Current authoring profile: REDUCED.

The placement subject, records and staff remain outside the tactical grid. A static encounter can establish that an access route is clear. It cannot complete custody transfer, decide ownership or create a new Trainer association.

## Encounter readiness — Release-Site Boundary Conflict

The premise already works as world-state content because Agency, Conservation and shelter continuity can review a release without tactical support.

A richer tactical version would need objective-aware AI and potentially complete movement plus terrain/zones/reactions.

Current authoring profile: REDUCED.

The release target waits outside combat. Ouros selects actual combatants, AutoPTU resolves the fixed battle, and Conservation/Agency then determine whether release still proceeds.

## Cobblemon authority boundary

Pass 94 preserves the binding direction:

`Ouros shelter/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Likely reusable overworld/presentation surfaces include:

- Pokémon entities and models;
- forms/cosmetic state;
- poses and movement animations;
- cries, sounds and particles;
- buildings, pens, gates and doors;
- signs/books/displays;
- UI;
- networking and synchronization;
- entity tracking and persistence hooks;
- world coordinates and residence anchors.

Adapter review is required for stable mapping between persistent Ouros Pokémon identity and loaded/unloaded Minecraft entity representation.

Battle-authority-forbidden behavior includes:

- selecting every nearby shelter Pokémon as a battle participant;
- using Cobblemon party/battle controller state to decide custody or placement;
- deriving AutoPTU HP/status/position from Cobblemon battle state;
- resolving shelter evacuation through Minecraft physics;
- applying damage/status from a pen, gate or facility hazard outside AutoPTU.

## Promotion gate for shelter-rich encounters

Do not promote full versions because Minecraft can visually render an evacuation or because Intercept has many verified slices.

A full objective-driven shelter encounter still needs current evidence for the exact families it uses.

At minimum:

- dynamic safe zones, gates, hazards or reaction spaces require `terrain/weather/hazards/zones/reactions` above BLOCKING for the exact behavior;
- autonomous attackers/defenders pursuing evacuation or protection goals require `AI tactical policy` above BLOCKING;
- in-world authoritative rendering requires adapter/playback support above BLOCKING;
- any Intercept/knockback/forced-movement reliance needs the exact behavior verified rather than inferred from neighboring slices.

## Unresolved implementation and canon questions

- What Ouros institutions, if any, operate shelters or sanctuaries?
- What terms and legal distinctions exist for ownership, custody, guardianship, surrender and abandonment?
- What evidence can authorize reunification?
- Is foster care an established Pokémon practice anywhere in Ouros?
- Who may approve release or relocation?
- Which case details are visible to prospective caretakers or the public?
- How does multiplayer authority handle irreversible Pokémon transfers?
- Which exact PTU/Caelo rules govern transfer, release, Loyalty and Command in the chosen Ouros rules interpretation?
- Does Caelo alter any of those rules?
- How should stable Pokémon identity survive Minecraft chunk unload/reload and server restarts?
- Which Cobblemon entity/persistence APIs are SAFE_REUSE versus ADAPTER_REQUIRED?
- How should a shelter keep many visible resident Pokémon without allowing nearby-entity presence to become BattleSpec composition?

These questions remain open rather than receiving invented answers.
