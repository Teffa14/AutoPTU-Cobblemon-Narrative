# Engine Readiness Snapshot — Pass 124

Status: EVIDENCE SNAPSHOT. This file records current evidence and does not promote capability families from isolated representative mechanics.
Date: 2026-08-29

## Read-only heads inspected

AutoPTU-Java current head: `82b9dd92ac8fd0cc47a6e53e24017fc20ebd04f6` — `Derive intercept Coaching from server-owned state (#273)`.

Compared with the Pass 123 head `91a61de675a08f8144849eb80b41f10648a81907`, the current slice further tightens the authority boundary for one Intercept check path. `RuntimeInterceptCheckInputFactory` now derives Coaching automatic-success state from server-owned runtime temporary effects while Acrobatics/Athletics remain derived from server-owned `CombatantRuleContent`. Tests verify present/absent Coaching behavior, authoritative Skill inputs, unknown-interceptor rejection and that the factory remains core-only rather than public adapter API.

The implementation itself documents an important limitation: Justified and terrain remain explicit internal inputs until their authoritative source families are frozen independently. Therefore this evidence does not promote complete movement, terrain/reactions or Trainer Features/perks as whole capability families.

AutoPTU current head: `d97c45e76647642105fee3ff1b9b80a38e092778` — `Career: preserve clean roster normalization identity`.

The current AutoPTU slice makes clean Career roster normalization referentially stable while preserving duplicate/invalid-record repair behavior. This is Career persistence/browser-state hardening and adds no tactical battle capability.

## Permanent capability map

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

No family is promoted in Pass 124.

## Intercept evidence update

Current concrete evidence supports a bounded route in which:
- a real interception sequence can enter the PRE-target registry;
- the effective defender is propagated into the authoritative Move pipeline;
- successful Intercept movement uses the resolved interceptor position for that route;
- Acrobatics/Athletics inputs are derived from server-owned combatant content;
- Coaching automatic-success state is derived from server-owned temporary effects;
- the builder remains core-only;
- Justified and terrain modifiers remain explicitly unfrozen authority families.

This is materially stronger than adapter-supplied Intercept conclusions. It still does not verify:
- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- every Intercept timing/window;
- environmental displacement;
- generalized competing reactions;
- generalized reaction ordering;
- broad terrain modifier authority;
- every Coaching or Trainer Feature pathway;
- every Move, Ability or Item registration;
- objective-aware AI tactical policy;
- semantic adapter playback.

## Pass 124 narrative readiness

The interregional arrival/inspection continuity model is primarily world-state and provenance data. It requires no new battle capability for:
- inspection gateways whose institution/mandate already exists in canon;
- requirement references;
- scoped intake episodes;
- document review records;
- identity checks based on existing persistent IDs;
- condition observations separated from interpretation;
- findings bounded by scope;
- temporary holds;
- referrals to owner systems;
- release-from-inspection events;
- historical gateway relocation and alias state;
- archive/provenance mysteries.

`Three Manifests, One Crate`, `Six Arrivals, Two Releases`, `The Correct Form for the Wrong Door` and `The Old Gate Still Has the New Number` are READY using current narrative infrastructure.

`The Receiving Hall Beneath the New Platform` is READY when all traversed geometry is static, already assessed/authorized and free of active machinery or controlled live subjects.

## Encounter readiness — Arrival Hall Perimeter

Targeting/footprints/range/LoS — VERIFIED.

Base movement legality — VERIFIED.

Complete movement including push/pull/knockback/interception/forced movement — PARTIAL if staff withdrawal, Intercept, escort movement or forced displacement happens during combat.

Core calculations — VERIFIED.

Action economy/initiative — VERIFIED.

Full turn/round lifecycle — PARTIAL if the encounter has staged withdrawal or timed closure windows.

Full stateful damage pipeline — PARTIAL for selected governed combat effects.

Status lifecycle — PARTIAL when selected legal effects apply status.

Terrain/weather/hazards/zones/reactions — BLOCKING if a protected corridor, changing inspection boundary or generalized crossing reaction is tactical.

Move-specific behavior — PARTIAL.

Abilities — PARTIAL.

Items — PARTIAL.

Trainer Features/perks — PARTIAL. Current Coaching evidence applies only to a concrete Intercept path and cannot promote the whole family.

AI legal-action infrastructure — VERIFIED.

AI tactical policy — BLOCKING for WITHDRAW/PROTECT/CLEAR_ROUTE behavior.

Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING for authoritative semantic evacuation, inspection shutdown or boundary-state playback.

Reduced form: READY. Close the inspection operation in Ouros world state first. Move staff, visitors, noncombatant Pokémon, documents and controlled subjects outside BattleSpec. Resolve a static conventional battle on the exterior apron. Victory can secure immediate access only.

## Encounter readiness — Sealed Consignment Diversion

Full-form pressure:
- complete movement — PARTIAL for escort/Intercept/forced displacement;
- lifecycle — PARTIAL for a timed handoff or departure;
- terrain/weather/hazards/zones/reactions — BLOCKING if a protected crossing is represented as a zone or generalized reactions trigger on movement;
- full stateful damage pipeline — PARTIAL if a governed combat effect can damage actors;
- object-specific damage/movement remains UNKNOWN unless a separate exact contract exists;
- AI tactical policy — BLOCKING for PROTECT/CLEAR_ROUTE;
- adapter/playback — BLOCKING for semantic custody/handoff presentation.

Reduced form: READY. Complete the consignment custody transfer and move the physical package off-grid before BattleSpec creation. Run a static chokepoint battle. Courier and the inspection owner decide subsequent delivery/release state.

## Encounter readiness — Wildlife Transfer Gate

Full-form pressure:
- complete movement — PARTIAL for withdrawal or Intercept;
- lifecycle — PARTIAL for staged intake or withdrawal windows;
- terrain/weather/hazards/zones/reactions — BLOCKING if protected enclosures, crossing reactions or environmental exposure are tactical;
- damage/status — PARTIAL only for exact governed combat effects; health screening, sedation, restraint or exposure mechanics remain UNKNOWN unless separately sourced and implemented;
- move-specific behavior/abilities/items/Trainer Features — PARTIAL and must be selected from actual covered mechanics;
- AI tactical policy — BLOCKING for PROTECT/WITHDRAW;
- adapter/playback — BLOCKING for semantic transfer/placement playback.

Reduced form: READY. Finish or safely pause the transfer under Ouros world state before combat. Keep the transferred Pokémon outside BattleSpec unless Ouros independently selects it as a legal combatant. Use a static exterior perimeter. Battle outcome cannot grant ownership, ecological release or inspection clearance.

## PTU/Caelo boundary

The internal PTU/Caelo source scan supports campaign structures, exploration, standard Skills, species capabilities and exact authored environmental mechanics. It does not establish a universal customs, border-control, immigration, quarantine-at-entry or biosecurity subsystem.

Remain UNKNOWN without exact governing evidence:
- universal inspection/search authority over Trainers, Pokémon, bags, cargo or vehicles;
- generic border checkpoints or permit requirements;
- universal ecological screening of transferred Pokémon;
- automatic quarantine duration;
- automatic disease/exposure screening;
- inspection-specific Skill DCs;
- contraband detection mechanics;
- Type-derived or species-derived ecological risk;
- species-derived detection of disease, prohibited materials or false documents;
- Move/Ability/Item/Trainer Feature effects that automatically clear or fail an inspection;
- carrying or restraint rules for a live inspection subject beyond exact implemented PTU mechanics;
- battle victory as release, authorization or proof.

Regional origin and species identity may be evidence inputs. They do not create a mechanical or ecological conclusion by themselves.

## Boundary with existing narrative systems

Interregional Mobility continues to own visits and record recognition.

Port/Travel/Rail/Road/Aviation/Transit systems continue to own physical arrival and service state.

Courier/Storage/Procurement/Material Culture continue to own goods movement, custody and provenance.

Credentials continues to own scoped authorization.

Conservation/Wildlife/Science/Interspecies Ecology continue to own ecological interpretation.

Care continues to own health and treatment.

Batch Traceability continues to own post-distribution recall/containment/correction.

Case Authority continues to own allegations and investigations.

Pass 124 stores an inspection episode only when an authored requirement and mandate already exist. It does not create the requirement or authority.

## Minecraft/Cobblemon boundary

Minecraft/Cobblemon may render gateways, desks, receiving rooms, queues, sealed containers, signs, temporary sites, staff, visiting Pokémon and doors opening after an Ouros decision.

Entity proximity does not trigger inspection. A chest does not prove contents. A sign does not establish authority. A Poké Ball model does not establish ownership. A Pokémon from another biome/region is not automatically invasive or diseased. Minecraft inventory state does not replace custody/provenance. Cobblemon healing/status display does not perform screening. Cobblemon BattleState remains outside combatant selection, legality, HP/status, tactical positions, inspection findings, hold/release and destination admission.

## Readiness result

Narrative/world-state inspection continuity: READY, but only when canon supplies the institution, mandate, trigger and scope.

Document/identity/provenance mysteries: READY.

Reduced Arrival Hall Perimeter: READY.

Reduced Sealed Consignment Diversion: READY.

Reduced Wildlife Transfer Gate: READY.

Full versions: PARTIAL/BLOCKING where complete movement, staged lifecycle, generalized reactions/zones, object interaction, objective-aware AI or semantic playback are required.

## Unresolved mechanical and canon questions

- Does any Ouros region use routine or event-specific arrival inspection?
- Which institutions, if any, have that mandate and for which subjects?
- Are there conservation-transfer receiving sites for Pokémon moving between regions?
- What privacy and record-access rules apply to inspection episodes?
- Can a hold be reviewed, and by whom, if canon establishes that process?
- Which PTU/Caelo Skills or exact species capabilities are relevant to particular observation tasks?
- Are any live-subject transport, restraint or welfare mechanics needed beyond existing systems?
- What object-interaction contracts would be required if a consignment remains on the tactical grid?
- How should AI represent WITHDRAW, PROTECT and CLEAR_ROUTE when those tactical policies exist?
- Which adapter semantic events are required for intake, hold, release and evacuation playback without granting the adapter authority?

Until exact canon or mechanical contracts answer those questions, the reduced forms and provenance-first state model are the implementation-safe path.