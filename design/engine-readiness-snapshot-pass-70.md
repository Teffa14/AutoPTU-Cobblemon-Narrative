# Engine Readiness Snapshot — Pass 70

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.
Date inspected: 2026-08-27

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live Java evidence

Newest inspected AutoPTU-Java commit:

`b1dc29e3beae24f56d1106129cb1fa61db55b069` — Add StatusController phase envelope dispatcher (#232).

Its parent `84505214d4bca41610f36f0a178e675ef0ab26ba` froze the Python-oracle phase-envelope ordering. The new commit adds an executable dispatcher around that ordering.

Observed contract from the commit and tests:

- START executes held-item start -> food regen -> food-buff start -> combatant phase effects;
- END executes combatant phase effects -> held-item end;
- COMMAND and ACTION execute combatant phase effects only within this envelope;
- events from each registered lifecycle hook are preserved in sequence;
- `PendingStatusSkipRequest` is accepted from the combatant-phase-effects step and is not replaced by a skip returned from surrounding held-item/food envelope hooks.

This is real progress for cross-family lifecycle orchestration. It establishes more than a static ordering table because the dispatcher now executes registered hooks and returns ordered events/pending skip state.

It still does not establish a complete StatusController or complete turn/round lifecycle. The dispatcher documentation explicitly says concrete held-item, food and combatant phase behavior remains in separate lifecycle hooks.

The current Java README still reports implemented slices for:

- targeting, areas, footprints, target anchors and LoS;
- Shift and jump movement legality;
- Damage Base/type tables and calculation primitives;
- stages, Accuracy stages and weather DB primitives;
- invariant d20 accuracy resolution;
- combat-stat resolution;
- typed turn flow and action budget;
- deterministic initiative;
- deterministic legal autobattler action-space generation.

The same README still explicitly leaves unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful Accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic event/full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

No permanent capability category is promoted by Pass 70.

## Why the new dispatcher does not promote lifecycle/status

For `full turn / round lifecycle`, category completion still needs complete battle-state ownership, complete phase semantics for real combatants, all relevant hook families, transition behavior, authoritative event emission and full BattleTranscript parity.

For `status lifecycle`, an envelope can call combatant-phase effects but does not prove complete application, persistence, phase behavior, skip behavior, expiry, removal and interactions across the complete governed status set.

For `items`, held-item START/END slots and an executable dispatcher prove integration points, not complete Item registry coverage or individual item semantics.

For `move-specific behavior`, `abilities` and `Trainer Features/perks`, the dispatcher supplies no evidence that their complete registries or timing contracts are implemented.

## Live Python evidence

Newest inspected AutoPTU commit:

`b5d39de8448b1f47b106418268e6376aa64c9a30` — merge of Career PR #174, “move battle trainers onto arena-edge pads.”

The adjacent commits are Career UX/presentation staging and cleanup. This is useful for visual battle presentation but does not establish a new authoritative PTU rules family or the Minecraft/Cobblemon/Craftics adapter required by this project.

No permanent capability category changes because of this Python evidence.

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

## Pass 70 authority boundary

Service-access state is primarily narrative/world state.

Pass 70 can determine or persist:

- which existing service access channel a request uses;
- request submission time;
- eligibility result references supplied by the owning system;
- slot/allocation references;
- queue membership;
- check-in and call timestamps;
- wait estimates and their revision history;
- cancellation/reschedule/no-show observations;
- explicit priority decision provenance;
- referral/callback access handoffs;
- completion of the access lifecycle after the owning service says the service completed.

Pass 70 cannot determine:

- medical urgency or treatment legality;
- challenge/battle eligibility;
- transport capacity or legal boarding;
- event participation mechanics;
- professional qualification;
- prices or fees;
- item/equipment availability beyond a referenced specialized record;
- PTU battle rules from appointment data;
- tactical objective rules;
- forced movement, terrain, weather, hazards or reactions;
- tactical AI priorities;
- Minecraft entity/interaction authority.

## Noncombat readiness

The core Pass 70 loop can be implemented in narrative state before new tactical capabilities exist:

`request -> owning eligibility result -> slot or queue -> check-in -> called -> owning service starts -> owning service completes -> access history`

Additional world-time behaviors can also work now where the existing narrative clock is authoritative:

- waiting advances world time;
- schedules can change through their owning layers;
- estimates can be superseded;
- an actor can miss a window;
- cancellation/rescheduling can preserve history.

The visual representation of exact desks, waiting actors and physical call/check-in state remains dependent on adapter work if Minecraft is expected to be authoritative for those visuals.

## Encounter review — Registration Hall Evacuation

Narrative premise:

Several actors are checked in for a formal service/challenge when a battle-capable threat makes the public registration area unsafe.

Intended full version may require:

- civilian/participant movement during battle;
- multiple evacuation exits;
- PROTECT/WITHDRAW/CLEAR_ROUTE objectives;
- interception or forced displacement;
- changing safe zones;
- terrain/hazards/reactions where governing rules exist;
- AI that values access denial, territorial behavior or evacuation instead of KO only;
- synchronized adapter playback preserving queue/check-in state.

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

Evacuate all queued noncombatants through world state before tactical initialization. Preserve requests, allocations and check-ins outside battle state. Freeze a static reviewed arena away from service desks. Resolve a standard encounter with only individually supported mechanics. The owning service/institution determines reopening. Pass 70 then applies reschedule/cancellation/restoration events supplied by that state.

Battle victory cannot automatically:

- complete appointments;
- establish eligibility;
- reorder the queue;
- grant priority;
- reopen the venue;
- restore a cancelled slot.

## Encounter review — Mobile Service Stop Interrupted

Narrative premise:

A recurring mobile service has confirmed appointments plus a small walk-in cohort when a threat interrupts the stop.

Intended full version may require:

- withdrawing clients and staff;
- a service point/vehicle that matters spatially;
- PROTECT/WITHDRAW/CLEAR_ROUTE objectives;
- terrain/weather where PTU/Caelo mapping exists;
- interception or forced movement;
- reactions;
- objective-aware opponents;
- adapter playback preserving IN_SERVICE versus CHECKED_IN versus WAITING actors.

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

Remove all clients/staff from tactical state first. Preserve access records in world state. Resolve a static battle. The owning service then decides whether interrupted sessions resume, refer, cancel or reschedule.

For a care-service variant, AutoPTU cannot infer clinical priority or treatment state from the battle result.

## Noncombat review — Two Names, One Slot

This can run now using narrative persistence only.

Required state:

- stable request IDs;
- stable slot/allocation IDs;
- access channel identity;
- timestamps;
- reschedule/cancellation events;
- communication/notice refs;
- group/proxy refs only where canon supports them;
- provenance-aware observations.

No PTU combat mechanic is required.

## Battle-institution handoff caution

A confirmed challenge slot is not a BattleSpec.

Required safe handoff:

1. Pass 70 confirms that the actor reached the relevant access state.
2. Battle Institution checks its own eligibility/format/roster rules.
3. The authoritative battle layer creates a legal BattleSpec.
4. AutoPTU resolves the battle.
5. The BattleTranscript returns to the owning institution.
6. The institution updates challenge state.
7. Pass 70 records whether the service instance completed and what access state follows.

This prevents booking metadata from becoming a second source of PTU legality.

## Care handoff caution

A queue layer must never implement hidden medical triage.

Care may supply a priority/access decision with provenance. Pass 70 can honor and record it. Observers may know only that another actor was called first, not the private reason.

The access history and the medical record therefore remain separate.

## Minecraft population caution

A persistent queue does not require one Minecraft entity for every queued actor.

Recommended representation:

- exact persistent NPCs for story-relevant actors;
- aggregate cohort/count state for background demand;
- only materialize additional temporary actors when performance and gameplay justify it;
- never derive queue order from entity coordinates;
- never use physical proximity to the desk as authoritative check-in.

This is especially important for locations that may otherwise accumulate dozens of idle entities.

## Current implementation recommendation

Build Pass 70 as a narrative coordination slice before adapter work:

1. one existing service owned by another layer;
2. one `service_access_channel`;
3. request submission;
4. owning eligibility/capacity result reference;
5. appointment allocation or queue entry;
6. check-in;
7. call/start handoff;
8. completion event from owning service;
9. preserved history for cancellation/reschedule/no-show.

A second useful slice is the noncombat `Two Names, One Slot` provenance mystery.

## Unresolved mechanical questions

- How will a checked-in formal challenge transition into BattleSpec creation without duplicating Battle Institution authority?
- Which semantic events should connect a battle transcript to a service-access completion record?
- If battle interrupts an active service, what component owns pause/resume ordering?
- Can a persistent overworld service desk remain near a battle while being excluded from tactical targeting?
- How will the adapter materialize and despawn aggregate waiting cohorts?
- How will multiplayer or group check-in map to a battle with multiple legal participants?
- How should world time advance while AutoPTU/Cobblemon playback is active?
- How will an owning service publish a capacity change atomically with queue effects?

Until those contracts exist, Pass 70 should keep service-access state outside tactical resolution and use reduced encounter forms.