# Engine readiness snapshot — Pass 171

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-31

## Read-only heads inspected

AutoPTU-Java main: `54feddaa3d95ab75d1efb90ea062ef20234627a8`.
Head message: `Freeze shadow tag forced movement geometry (#310)`.

AutoPTU main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.
Head remains presentation-only and explicitly states that battle rules and outcomes do not change.

Neither engine repository was modified by this pass.

## Java evidence

PR #310 freezes Python-oracle evidence for `shadow_tag_anchor` setup and per-step geometry inside forced movement and adds that contract to CI. Recent earlier heads also provide production evidence for selected post-hit Push behavior, selected Ability modifiers/prevention and selected status/temporary-state prevention.

This remains representative evidence. It does not prove complete movement as a family.

Still unverified broadly:
- all Push and Pull cases;
- general Knockback;
- every Intercept ordering and interaction;
- arbitrary forced movement from all sources;
- full terrain/weather displacement;
- all Item/Ability/Trainer Feature movement interactions;
- escort/rescue semantics;
- protected-object carrying;
- crowd routing;
- vehicles/platforms;
- generalized reactions;
- objective-aware tactical policy.

No permanent category is promoted.

## Permanent capability map

VERIFIED
- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL
- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING
- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Pass 171 encounter dependency review

### Mobile Library Route Interruption

FULL: BLOCKED.

Potential dependency families:
- complete movement for escort, route breakthrough, Intercept or displacement;
- full lifecycle for sustained protection/withdrawal objectives;
- terrain/weather/hazards/zones/reactions if road/weather conditions alter tactical state;
- exact Move/Ability/Item/Feature parity for selected combatants;
- AI tactical policy for protect/escort/breakthrough behavior;
- adapter/playback for semantic vehicle and route-state presentation.

REDUCED: READY at narrative-contract level after individual combat-content audit. The vehicle, driver, patrons and book crates remain outside BattleSpec. Allowed tactical-world output: `IMMEDIATE_MOBILE_LIBRARY_ROUTE_CLEAR`.

### Interlibrary Transfer Chokepoint

FULL: BLOCKED.

Requires protected-object carrying or escort semantics if the shipment is tactical, complete movement, potentially lifecycle/reactions, objective-aware AI and semantic adapter/playback.

REDUCED: READY at narrative-contract level after audit. Shipment and library copies remain outside BattleSpec. Allowed output: `IMMEDIATE_INTERLIBRARY_TRANSFER_ROUTE_CLEAR`. This cannot mark dispatch, receipt, check-in, patron collection, ownership transfer or successful service fulfillment.

### Flooded Return Room Access

FULL: BLOCKED.

A rich implementation may need dynamic terrain, water/hazard zones, timed access, object recovery and reaction support plus tactical objective policy and playback.

REDUCED: READY at narrative-contract level after audit. Returned books remain world-state objects. AutoPTU can only establish `IMMEDIATE_RETURN_PROCESSING_ACCESS_CLEAR`. Deposited, received, checked-in, condition-assessed and available remain separate Narrative/Archives facts.

### Reading Room Evacuation

FULL: BLOCKED.

Civilian escort/protection, crowd movement, full lifecycle, reactions, objective-aware AI and semantic playback are not fully verified.

REDUCED: READY at narrative-contract level after audit. Civilians and fragile holdings leave BattleSpec before initiative. AutoPTU may only establish `IMMEDIATE_READING_ROOM_PERIMETER_CLEAR`.

## Library mechanics boundary

No reviewed project evidence establishes a universal PTU/Caelo mechanic for:
- library membership;
- checkout eligibility;
- holds or renewals;
- overdue penalties;
- interlibrary requests;
- research bonuses from possession of a book;
- automatic Skill Rank, Edge or Feature gain from reading;
- automatic Move/Tutor effects from manuals;
- knowledge acquisition merely because an item was borrowed.

These remain narrative/institutional state unless exact governing PTU/Caelo material is verified.

If a text is also a mechanical Item, the exact Item must be audited before it can affect battle.

## Knowledge boundary

The circulation layer must preserve:
- CHECKED_OUT != READ
- READ != UNDERSTOOD
- UNDERSTOOD != BELIEVED
- BELIEVED != TRUE
- BORROWING_HISTORY != ACTOR_KNOWLEDGE

Knowledge state must come from authored observation/knowledge provenance rather than inventory or circulation inference.

## Adapter boundary

Minecraft/Cobblemon may render libraries, shelves, books, librarians, reading rooms, mobile-library vehicles, return chutes, pickup shelves and transfer crates.

Presentation cannot establish:
- canonical checkout;
- patron identity;
- ownership;
- due dates;
- successful return;
- reading;
- comprehension;
- truth of book contents;
- mechanical benefits.

A Minecraft book item in an inventory is not automatically a circulating library copy. A chest is not the catalog. An NPC near a shelf is not a borrower.

Cobblemon/Minecraft battle-state authority remains excluded. AutoPTU decides tactical facts. Narrative and institutional rules decide circulation consequences.

## Promotion rule

A capability category changes only when live tests/contracts demonstrate broad family coverage. Selected Push integration, selected prevention rules and a Shadow Tag geometry oracle remain important but insufficient evidence to promote complete movement, abilities, statuses or any other permanent category.