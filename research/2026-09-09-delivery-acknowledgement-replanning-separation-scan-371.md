# Delivery, acknowledgement and replanning separation scan — Pass 371

Status: RESEARCH / NON-CANON
Date: 2026-09-09
Canon effect: NONE

## Repository inspection

Pass 370 already places allocation-notice obligations, notice links and the real Communications envelope/status under one coherent world checkpoint. `CURRENT_FOCUS.md` and the Pass 287 coordinator keep private delivery, knowledge materialization and selective replanning as separate owners. Existing world snapshots persist agent knowledge refs, private KnowledgeLedgers, the replan queue and the coordinator materialization guard.

This pass does not change PTU rules or established Ouros geography.

## New external source 1 — AHA TeamSTEPPS closed-loop communication

Source: https://www.aha.org/center/project-firstline/teamstepps-video-toolkit/closed-loop-communication
Inspected: 2026-09-09.

Reusable structure: receiving a message does not prove correct understanding or execution. Closed-loop communication adds an explicit receiver check-back and sender verification. The useful Ouros abstraction is a causal ladder with independently queryable states: transmitted, delivered, materialized as receiver evidence, acknowledged/checked back, and acted upon.

No healthcare procedure or protected prose is imported.

## New external source 2 — AHRQ TeamSTEPPS communication definitions

Source: https://www.ahrq.gov/hai/cauti-tools/phys-championsgd/appa.html
Inspected: 2026-09-09.

Reusable structure: a check-back verifies exchanged information, while a handoff can transfer information together with authority/responsibility. Ouros can therefore model a field instruction that arrived but still requires clarification, acceptance or later replanning without treating communication receipt as plan execution.

No medical setting is imported.

## New external source 3 — Pokémon Origins fan game

Source: https://originsproject.eu/
Inspected: 2026-09-09.

Repository search found no prior processing of this project by name. Public material presents a region shaped by several competing organizations and a protagonist moving through a conflict whose meaning depends on relationships among those groups. The reusable structure is multi-faction interpretation: the same observed event can acquire different operational meaning because actors have different duties, loyalties and prior information.

Ouros transformation: a relay instruction can be correctly delivered to one expedition member while another institution interprets the same route change differently because its mandate, authority and evidence differ. No Elenos geography, confraternities, characters, plot, dialogue or custom mechanics are imported.

## New external source 4 — Pokémon Z fan game

Source: https://pokemonzfangame.com/
Inspected: 2026-09-09.

Public material describes a completed fan adventure that places optional activities beside a larger historical conflict. The reusable structure is layered obligation: a local task can continue to matter while the main story moves elsewhere. Ouros can use this for field instructions and unfinished acknowledgements that persist across travel and later become the reason two parties arrive with incompatible plans.

No characters, ancient-Kalos plot, regional forms, villains, gyms or custom mechanics are imported.

## PTU / Caelo cross-check

The project source hierarchy remains unchanged. PTU Core/Pokédex and the indexed Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Region Location & Encounter List remain authoritative when they address a mechanic or setting fact.

No inspected PTU/Caelo evidence was found that requires a delivered world-agent message to become remembered knowledge, accepted instruction or changed agenda automatically. Those are Ouros world-simulation semantics, not new PTU combat rules.

## Engine evidence cross-check

Read-only AutoPTU-Java head inspected: `50879211895641d740bb0e389ada075c98f366af` (merge #411). The change adds/fixes differential parity around combat-stage reaction handling including `Minus [SwSh]` and nested stage-event provenance. It is specific evidence for those reaction paths and does not establish complete Ability or reaction-family coverage.

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head remains presentation-only and supplies no new battle-rule promotion.

## Reusable Ouros pattern

A robust field communication chain should be able to represent all of these states without collapsing them:

`AUTHORED -> DELIVERED -> MATERIALIZED_AS_EVIDENCE -> ACKNOWLEDGED -> REPLAN_TRIGGERED -> PLAN_SELECTED -> ACTION_STARTED`

A later state may be absent while every earlier state remains historically true. Current recall is also separate: materialized evidence may exist in a durable ledger while retrieval is temporarily inaccessible.

## Narrative consequences

This permits errors without omniscience or contrived deception. A ranger can receive an instruction during a hazardous crossing, fail to check it back, retain the claim in durable evidence, continue the old route because no planning window occurred, and later sincerely state that the instruction arrived. Another actor can reasonably infer that delivery should have changed the plan and be wrong about that inference.

It also creates investigable provenance. Players can ask who authored the change, which recipient received it, whether the receiver acknowledged it, whether a replan trigger existed, and what decision followed.

## Capability implications

Reduced communication/investigation version: no AutoPTU dependency.

Mechanically rich interception version:
- targeting/footprints/range/LoS — VERIFIED within audited ordinary scope;
- base movement legality — VERIFIED within audited ordinary scope;
- complete movement including interception/forced movement — PARTIAL and required if physical interception matters;
- core calculations — VERIFIED within audited contracts;
- action economy/initiative — VERIFIED for audited primitives;
- full turn/round lifecycle — PARTIAL if the encounter uses timed multi-round objectives;
- full stateful damage pipeline — PARTIAL if combat damage can persist into the objective state;
- status lifecycle — PARTIAL if statuses affect courier/relay operation;
- terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism;
- move-specific behavior — gated per move;
- abilities — gated per Ability; merge #411 does not promote the family;
- items — gated per Item;
- Trainer Features/perks — gated per Feature;
- AI legal-action infrastructure — VERIFIED for ordinary audited actions;
- AI tactical policy — BLOCKING for intercept-to-inform, preserve-cargo, acknowledge-objective and disengage-after-objective policy;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL/BLOCKING for authoritative communication/objective acknowledgement and cargo/relay playback.

## Open questions

1. Should acknowledgement be a first-class owner, or only a new communication event with a semantic type such as CHECK_BACK?
2. Should every delivered allocation notice schedule a replan trigger, or can policy legitimately defer low-urgency information until a later planning window?
3. How should current recall gates interact with an already scheduled replan trigger when the underlying evidence remains durable but temporarily inaccessible?
4. Which Ouros regions, institutions and relay technologies are canon-approved enough to bind this pattern to named places? Until answered, all locations below remain placeholders.
