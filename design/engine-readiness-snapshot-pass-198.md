# Engine Readiness Snapshot — Pass 198

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-02
Narrative head before pass: `7fedc197a80eba832b84de49bbd6774ba11abb8d`

Read-only engines inspected:

- AutoPTU-Java head: `dd8097910da62f98d07047cd0603fa8d858f4c67`
- AutoPTU head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

## Live engine delta

AutoPTU-Java advanced one commit beyond pass 197.

New commit:

`dd8097910da62f98d07047cd0603fa8d858f4c67` — `Add forced movement prevention semantic event adapter (#322)`.

Changed evidence inspected from the commit:

- new `RuntimeForcedMovementPreventionSemanticEvents.java`;
- new semantic-event tests;
- additional precedence-test coverage.

The new adapter maps an already-resolved forced-movement prevention result to a semantic `TrainerFeatureEvent` for the pinned Insectoid Utility / Wallclimber case.

The class explicitly states that it never decides whether forced movement is legal or prevented. The governing conclusion belongs to `ForcedMovementPreventionResolution`; this adapter translates winning provenance into an observable event contract.

This is meaningful progress in parity and observability for one exact prevention path.

It does not verify the complete movement family, complete Trainer Feature behavior or all semantic-event combinations.

No permanent capability category is promoted by this delta.

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head remains a presentation-only viewport-resize coordinate synchronization change and explicitly does not alter battle rules or outcomes.

## Permanent capability classification

### VERIFIED within currently audited contracts

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

`VERIFIED` remains scoped to audited contracts. It does not assert exhaustive combinatorial coverage.

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING when the complete family is required

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Why complete movement remains PARTIAL

Java #322 covers semantic projection for an already-resolved prevention path. It does not close the full matrix across:

- Push;
- Pull;
- Knockback;
- Interception;
- collisions;
- partial stops;
- chained displacement;
- footprint interactions during displacement;
- reaction ordering;
- terrain-mediated displacement;
- all combinations with Moves;
- all combinations with Abilities;
- all combinations with Items;
- all combinations with Trainer Features;
- statuses and temporary effects;
- full semantic-event parity for every path.

The new code is therefore evidence for a narrower statement:

`ONE TRAINER-FEATURE PREVENTION EVENT PATH HAS BETTER JAVA OBSERVABILITY`.

It is not evidence for:

`COMPLETE_FORCED_MOVEMENT_IMPLEMENTED`.

## Why Trainer Features remain PARTIAL

The new event payload contains an exact Trainer Feature case and controller provenance. That proves an integration point for that Feature interaction.

It does not prove:

- every Trainer Feature is parsed;
- every Feature trigger timing is implemented;
- every Feature interrupt/reaction is implemented;
- every movement interaction is supported;
- every Feature has semantic-event parity;
- every Feature can be projected faithfully through Minecraft/Cobblemon/Craftics.

Trainer Features/perks therefore remain PARTIAL.

## Pass 198 narrative-mechanics boundary

Pass 198 adds no new battle rule.

It adds proposed Narrative records for:

- service requests;
- routing;
- local triage/priority decisions;
- capacity slots;
- appointments;
- work orders;
- service-result provenance;
- schedule revisions;
- queue projections;
- delay dependencies;
- off-screen ordinary service progression.

These records must never substitute for authoritative mechanical resolution.

## PTU service cross-check

PTU 1.05 source material explicitly discusses NPC-provided services based on Features, including specialist/generalist Tutors and other service examples whose availability depends on the setting and provider capabilities.

Therefore the Narrative service layer may manage intake and scheduling while mechanical results remain governed.

Required distinction:

```text
NARRATIVE_SERVICE_COMPLETED
  !=
PTU_MECHANICAL_EFFECT_APPLIED
```

Examples:

- tutor appointment completed != Move learned;
- training session completed != XP/level/Feature gained;
- item work order closed != governed Item transformation;
- Battle Yard appointment completed != battle result;
- ordinary service history != provider's PTU build legality.

Narrative should store a `mechanical_resolution_ref` when an external authority actually resolves the effect.

## Pass 198 rich encounter

Encounter: `Battle Yard Double-Booked Drill`.

Narrative premise:

Two legitimate session histories point to the same Battle Yard window because an older schedule projection remained visible after a revision. The conflict is resolved through service continuity first. A battle occurs only if an authored solution legitimately calls for one.

### Full intended dependency matrix

- targeting/footprints/range/LoS: VERIFIED within audited contracts
- base movement legality: VERIFIED within audited contracts
- complete movement: PARTIAL; blocking when selected content or drill objectives depend on Interception, Push, Pull, Knockback, forced movement, collisions or displacement interactions
- core calculations: VERIFIED within audited contracts
- action economy/initiative: VERIFIED within audited contracts
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL when selected content uses statuses
- terrain/weather/hazards/zones/reactions: BLOCKING when marked safety zones, reactions, hazards or environment have mechanical consequences
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL when battle Items participate
- Trainer Features/perks: PARTIAL; #322 improves one exact Feature/prevention event path only
- AI legal-action infrastructure: VERIFIED within audited contracts
- AI tactical policy: BLOCKING when NPC-controlled actors must obey drill objectives, avoid a protected zone, prioritize non-KO goals or deliberately de-escalate
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for faithful simultaneous Yard projection and authoritative return

Disposition: FULL RICH VERSION BLOCKED unless a narrower selected BattleSpec avoids blocking families and every exact content dependency is separately verified.

## Reduced encounter contract

The scheduling story can run immediately.

Narrative retains:

- request IDs;
- appointment histories;
- authoritative schedule revision;
- stale visible schedule copy;
- participant check-in facts;
- Sela/Jace authority and availability;
- rescheduling decision;
- relationship/history consequences;
- any spectator state.

Before combat, resolve the double booking at the world layer.

If an audited battle remains part of the chosen solution:

- run one ordinary audited battle at a time;
- use stable Battle Yard geometry;
- omit unverified mechanical zones, hazards and reactions;
- select only audited combatants/content;
- avoid forced-movement objectives unless exact selected interactions have contracts;
- do not require AI to understand booking fairness or social consequences.

Allowed output:

- authoritative normal BattleSpec result;
- optionally `AUDITED_PRACTICE_BATTLE_COMPLETE` when integration supports that exact handoff.

Battle output cannot determine:

- which appointment deserved priority;
- whether a person was at fault;
- whether compensation exists;
- relationship gain/loss;
- rival status;
- future queue priority;
- Battle Yard ranking;
- badge or award;
- invented mechanical training benefit.

Disposition: REDUCIBLE USING AUDITED BASIC BATTLE CONTENT.

## AI policy caution

The pass does not upgrade tactical AI simply because legal-action infrastructure exists.

A simultaneous drill could require policy such as:

- preserve distance from another practice group;
- stop once the training objective is met;
- avoid a safety area;
- prioritize positioning over damage;
- deliberately avoid KO pressure;
- follow Sela's authored drill objective.

Those are tactical-policy requirements and remain blocking until live tests/contracts prove them.

## Adapter/playback caution

A complete Battle Yard scheduling story eventually needs the adapter to preserve a reliable world -> battle -> world loop.

The adapter must not author service state from presentation alone.

Required distinctions include:

- NPC standing in a waiting area != checked in;
- visible line order != authoritative queue order;
- chunk unload != cancelled appointment;
- entity pathing failure != provider unavailable;
- stale sign != current schedule authority;
- visual workbench occupancy != resource reservation unless linked to server state;
- battle start animation != accepted service request;
- battle playback result cannot revise appointment provenance;
- duplicate NPC entity cannot create duplicate provider capacity.

The complete Minecraft/Cobblemon/Craftics family remains BLOCKING.

## Caelo uncertainty

Literal `Caelo` search across Narrative, AutoPTU-Java and AutoPTU returned no indexed result during this pass.

No inspected evidence currently establishes:

- regional queue law;
- universal appointment etiquette;
- service cancellation penalties;
- professional service licensing;
- ferry reservation doctrine;
- service pricing rules;
- mandatory response times;
- compensation requirements;
- universal service hours;
- regional staffing standards.

All remain unresolved.

## Narrative repository state for this pass

Pass 198 writes only to Narrative and keeps canon untouched.

New files:

- `research/2026-09-02-service-request-queue-appointment-capacity-scan-198.md`
- `design/service-request-queue-appointment-capacity-continuity-layer.md`
- `proposals/2026-09-02-marea-service-request-queue-capacity-seeds-198.md`
- `design/engine-readiness-snapshot-pass-198.md`

No AutoPTU-Java or AutoPTU write is authorized by this task.

## Implementation recommendation

Prototype `Two Repairs, One Bench` first.

It requires no battle, no new institution, no regional service law, no price, no mechanical crafting rule and no new NPC.

It validates the core architecture using already-canon Teo/repair-row responsibilities and can later be reused by Mirador review, ferry windows, Tideglass requests and Battle Yard scheduling.