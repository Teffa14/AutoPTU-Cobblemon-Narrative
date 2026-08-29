# Engine Readiness Snapshot — Pass 131

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-29

This file records the battle-engine evidence checked while adding the food-service safety assessment, correction and reopening continuity layer.

It does not modify AutoPTU-Java or AutoPTU. Both repositories were inspected read-only.

## Narrative head before this pass

Pass 130 head inspected before writing:

`9010671c856da49fa980bff49a941e69ede41078`

The complete recursive narrative tree was inspected and was not truncated.

## AutoPTU-Java live head

Current head checked during Pass 131:

`80f08b5d66f3451f70743ac0d4717f3a3dd21a0b`

Commit:
`Derive intercept Justified bonus from server state (#275)`

No newer Java commit was present than the one already documented in Pass 130.

### What this live evidence verifies locally

The inspected commit and preceding Intercept work support a concrete server-owned Intercept route with:

- PRE-target integration in the authoritative runtime path;
- successful interceptor movement in the implemented case;
- effective defender replacement in the implemented case;
- Acrobatics/Athletics ranks derived from server-owned `CombatantRuleContent`;
- Coaching automatic-success state derived from server-owned temporary effects;
- exact `Justified [Errata]` detection derived from server-owned Ability state;
- the Python-authority `Justified [Errata]` Intercept bonus pinned to +4 in regression coverage.

The current factory comment keeps terrain as an explicit internal input until its authoritative environment contract is frozen independently against Python.

### What this evidence does not verify

Do not generalize this implementation to:

- every Intercept timing window;
- broad Push;
- broad Pull;
- broad Knockback;
- every forced-movement source;
- environmental displacement;
- generalized reaction ordering;
- multiple competing reaction windows;
- generalized protected-civilian reactions;
- broad terrain authority;
- broad weather authority;
- all Abilities;
- all Trainer Features/perks;
- tactical objective selection;
- Minecraft/Cobblemon/Craftics semantic playback.

One representative mechanic remains representative evidence only.

## AutoPTU live head

Current head checked during Pass 131:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:
`Career: keep battle coordinates synced after viewport resize (#237)`

The commit synchronizes cached Pixi screen dimensions after viewport resize so visual tactical sprite destinations use current renderer geometry. Its commit description explicitly states that battle rules and outcomes do not change.

### Classification consequence

This is useful presentation hardening.

It does not verify:

- battle authority in the Minecraft adapter;
- semantic playback of environmental states;
- combatant selection authority;
- legality authority;
- HP/status authority;
- tactical position authority beyond rendering of existing transcript state;
- service-closure or evacuation semantics;
- food-service world-state authority.

The adapter/playback family remains BLOCKING.

## Permanent capability map — Pass 131

No family receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

Evidence remains sufficient for the established baseline used by reduced static encounters. This does not imply every unusual target shape or bespoke Move behavior exists.

`base movement legality`

Basic legal movement remains available for conventional BattleSpecs.

`core calculations`

Existing parity-backed calculation infrastructure remains sufficient at the category baseline previously established by the engine project.

`action economy/initiative`

Baseline action-economy and initiative handling remain verified.

`AI legal-action infrastructure`

The engine can enumerate/validate legal options at the established baseline. This must not be confused with objective-aware tactical selection.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

The Intercept path has concrete implementation evidence, but the family is broader than Intercept. Push/Pull/Knockback and all forced-movement/reaction combinations are not comprehensively verified.

`full turn/round lifecycle`

Enough lifecycle exists for ordinary battle flow, but mechanically rich timed evacuation/withdrawal windows and every delayed effect contract remain incomplete.

`full stateful damage pipeline`

Substantial damage behavior exists, but the permanent family remains partial until the complete stateful pipeline and edge cases are parity-backed.

`status lifecycle`

Existing statuses do not imply support for invented food-safety or environmental statuses. The family remains partial.

`move-specific behavior`

Representative Move implementations do not prove complete move coverage.

`abilities`

Exact `Justified [Errata]` evidence strengthens one Intercept dependency only. It does not promote the Ability family.

`items`

Items remain partial. No food-service safety item behavior is inferred.

`Trainer Features/perks`

Coaching on the Intercept route is concrete evidence for one Feature interaction, not family completion.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

Food-service full encounters would need this family for protected corridors, active heat/steam/spill/fire areas, changing unsafe cells and generalized reaction windows. No such generalized contract is verified.

`AI tactical policy`

Full versions need objective-aware policies such as `PROTECT`, `WITHDRAW` and `CLEAR_ROUTE`. Legal-action infrastructure alone does not choose those objectives correctly.

`Minecraft/Cobblemon/Craftics adapter/playback support`

The live AutoPTU change improves visual coordinate synchronization only. Semantic projection and authority boundaries required by the full encounters remain unverified.

## Pass 131 encounter review

### Kitchen Service Withdrawal

Intended full version requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including Intercept/forced displacement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL if attacks/damage occur;
- status lifecycle — PARTIAL if status effects occur;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

- service pauses before combat;
- workers/customers/noncombatant Pokémon withdraw through Ouros world state;
- food, samples, private records and controlled equipment remain outside BattleSpec;
- static safe geometry is selected;
- explicit combatants are sent to AutoPTU;
- victory records immediate perimeter/access result only;
- operational assessment, correction and reopening resume afterward through narrative owners.

### Receiving Dock Diversion

Intended full version additionally wants controlled-object/custody representation during active combat.

No generalized battle contract for shipment custody or damage/acceptance of food-service cargo is established.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

- receiving operation stops before BattleSpec;
- shipment remains outside battle under existing custody state;
- workers withdraw;
- combat uses a static dock perimeter;
- afterward Food, Batch Traceability and/or Cold Chain decide their own state;
- combat cannot accept/reject product or prove chain integrity.

### Follow-Up Visit Perimeter

Intended full version wants assessor withdrawal, protected evidence zones, Intercept/reactions and objective-aware AI.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

- follow-up assessment is suspended first;
- assessors, samples, records and equipment are outside BattleSpec;
- static combat resolves the independent threat;
- the authorized narrative owner decides whether the visit resumes;
- battle result cannot create a verification record.

## Food-service mechanical assumptions deliberately rejected

Pass 131 found no governing PTU/Caelo evidence sufficient to create universal mechanics for:

- kitchen heat damage;
- steam damage;
- hot-liquid damage;
- grease/fire zones;
- slippery-floor movement changes;
- contamination statuses;
- foodborne disease;
- allergen reactions;
- spoilage timers;
- cooking-temperature checks;
- cooling-temperature checks;
- cleaning/sanitization checks;
- sanitation scores;
- inspection Skill DCs;
- generic food-handler certification;
- generic venue reopening mechanics;
- universal Chef Feature authority over venue safety;
- automatic Fire-type cooking safety;
- automatic Ice-type refrigeration;
- automatic Water-type potability;
- automatic Poison-type contamination;
- species-based detection of unsafe food;
- Moves, Abilities, Items or Trainer Features that universally verify a correction.

If a future PTU/Caelo source or engine contract verifies a specific mechanic, only that specific scope should be promoted.

## Narrative implementation rule

Food-service operational truth stays outside combat authority.

AutoPTU may resolve a conventional battle that happens near a food-service site. Ouros owns:

- venue service state;
- assessment scope;
- evidence and provenance;
- samples and owner handoffs;
- corrective actions;
- verification;
- reopening/service decisions;
- public consequences;
- Chronicle persistence.

The adapter may display those states after Ouros decides them. It may not infer them from blocks, entities, particles, inventories or battle victory.

## Minecraft/Cobblemon guardrails

Presentation can include:

- closed counters;
- barriers;
- changed menu boards;
- replacement equipment;
- revised storage layout;
- alternate serving windows;
- workers returning after an approved state change;
- regular Pokémon resuming authored routines.

Presentation cannot establish:

- cleanliness;
- contamination;
- potable water;
- refrigeration validity;
- food custody;
- worker competence;
- venue approval;
- service authorization;
- health causality.

Native Minecraft fire, water, ice, particles, item spoilage assumptions, mob proximity and pathfinding remain non-authoritative unless an explicit adapter contract later maps a governing PTU/Caelo rule.

## Cross-owner narrative safety

A battle near a venue must not silently mutate another owner's case.

Forbidden automatic transitions include:

- victory => `CORRECTION_VERIFIED`;
- victory => `SERVICE_RESUMED`;
- enemy defeated => `HEALTH_CLUSTER_CLOSED`;
- object recovered => `BATCH_RELEASED`;
- machine repaired visually => `COLD_CHAIN_VALID`;
- water block restored => `WATER_QUALITY_CONFIRMED`;
- Pokémon removed from scene => `CONTAMINATION_REMOVED`.

Every transition requires its proper owner and evidence.

## Live-evidence conclusion

Pass 131 adds no reason to change the permanent engine map.

The new narrative material is implementation-ready at the world-state level and through reduced static battles. Rich evacuation, protected-zone, active-kitchen-hazard and objective-aware versions remain future-facing until the exact capability families receive stronger contracts and tests.

## Unresolved engine questions

- When will generalized terrain authority become server-owned rather than explicit internal input in isolated paths?
- How will generalized reactions and competing reaction windows be ordered?
- What is the complete contract for Push/Pull/Knockback/forced movement?
- How will objective-aware AI represent civilian withdrawal, protected corridors and route clearing?
- What semantic event vocabulary will the Minecraft/Cobblemon/Craftics adapter consume?
- Which Food Buff/Chef/item mechanics from Python AutoPTU already have parity-backed Java coverage, and at what exact scope?
- Will any future environment contract support kitchen-like hazards, or should such scenes remain narrative-only unless a specific PTU source defines them?

Until those questions are answered by live code/tests/contracts, the classifications above remain conservative.