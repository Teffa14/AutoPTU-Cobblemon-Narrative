# Engine Readiness Snapshot — Pass 132

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-29

This file records the live engine evidence checked while adding the severe-wind, windthrow, debris-impact and recovery continuity material.

AutoPTU-Java and AutoPTU were inspected read-only. This pass writes only to `AutoPTU-Cobblemon-Narrative`.

## Narrative head before this pass

Pass 131 head inspected before writing:

`a3ac4749ac7b561ee77ddca05b1e4f16f71ef50f`

The complete recursive narrative tree was inspected before selecting the topic. The returned tree was not truncated.

The adjacent Weather, Crisis/Rescue, Building Safety, Grid, Forestry/Public Space, Roads/Travel, Maintenance and prior readiness material were checked to avoid duplicating owner authority.

## AutoPTU-Java live head

Current head checked during Pass 132:

`80f08b5d66f3451f70743ac0d4717f3a3dd21a0b`

Commit:
`Derive intercept Justified bonus from server state (#275)`

No newer Java commit was present during this run.

### Local evidence still verified

The recent Intercept sequence supports a concrete authoritative route with:

- PRE-target integration;
- successful interceptor movement for the implemented case;
- effective-defender replacement for the implemented case;
- Acrobatics/Athletics ranks derived from server-owned `CombatantRuleContent`;
- Coaching automatic-success state derived from server-owned temporary effects;
- exact `Justified [Errata]` presence derived from server-owned Ability state;
- Python-authority bonus for `Justified [Errata]` pinned to +4 in regression coverage.

This strengthens one Intercept path.

It does not prove the complete movement family.

### Evidence not established by this head

Do not generalize the current Intercept evidence to:

- broad Push;
- broad Pull;
- broad Knockback;
- every forced-movement source;
- generic gust displacement;
- environmental movement;
- all Intercept timing windows;
- generalized reaction ordering;
- multiple competing reaction windows;
- protected-civilian reaction contracts;
- flying-debris reactions;
- broad terrain authority;
- broad Weather authority;
- all Abilities;
- all Trainer Features/perks;
- objective-aware tactical policy;
- semantic Minecraft/Cobblemon/Craftics playback.

One representative mechanic remains representative evidence only.

## AutoPTU live head

Current head checked during Pass 132:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:
`Career: keep battle coordinates synced after viewport resize (#237)`

The commit synchronizes cached Pixi screen dimensions after viewport resizing so tactical sprite destinations use current renderer geometry. Its commit description explicitly states that rules and outcomes do not change.

### Consequence for this pass

This is useful presentation hardening.

It does not establish:

- semantic wind playback;
- falling/debris animation contracts tied to rules;
- world-weather-to-PTU Weather mapping;
- combatant authority;
- legality authority;
- HP/status authority;
- tactical position authority beyond rendering existing engine state;
- post-storm impact authority;
- owner-system handoff authority.

Minecraft/Cobblemon/Craftics adapter/playback therefore remains BLOCKING.

## Permanent capability map — Pass 132

No family receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

The established baseline remains sufficient for reduced static encounters. This does not imply every unusual target shape, cover interaction or bespoke Move exists.

`base movement legality`

Basic legal movement remains verified for conventional BattleSpecs.

`core calculations`

Existing parity-backed calculation infrastructure remains sufficient at the previously established category baseline.

`action economy/initiative`

Baseline action economy and initiative remain verified.

`AI legal-action infrastructure`

The engine can enumerate and validate legal options at the established baseline. This does not provide objective-aware tactical selection.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

Concrete Intercept work exists. The family remains broader than that route. Generic wind displacement would depend on forced movement and environmental interaction that are not comprehensively verified.

`full turn/round lifecycle`

Ordinary battle flow exists, but rich staged withdrawal, timed hazard windows and delayed environmental transitions remain incomplete as a family.

`full stateful damage pipeline`

Substantial damage behavior exists. The complete stateful pipeline remains partial under the permanent engine classification.

`status lifecycle`

Existing statuses do not authorize invented wind, airborne, debris, exposure or shelter statuses.

`move-specific behavior`

Representative implementations do not prove complete Move coverage.

`abilities`

Exact `Justified [Errata]` evidence is local to the Intercept contract. No broad wind-related Ability authority is inferred.

`items`

Items remain partial. No generic brace, shelter, tether or debris-protection item behavior is inferred.

`Trainer Features/perks`

Coaching provides concrete evidence on the Intercept path only. It does not provide storm-response, evacuation or assessment authority.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

The intended full wind encounters would require this family for active gust areas, flying debris, unsafe/hanging-object zones, protected retreat corridors, changing hazard cells and generalized reactions.

No generalized contract is verified.

`AI tactical policy`

Full versions need objective-aware behavior such as `WITHDRAW`, `PROTECT`, `CLEAR_ROUTE`, avoid-hazard and possibly hold-position behavior.

Legal-action infrastructure cannot choose those objectives reliably by itself.

`Minecraft/Cobblemon/Craftics adapter/playback support`

Visual coordinate synchronization does not provide semantic projection of wind, owner decisions, hazard state or environmental consequences.

This family remains BLOCKING.

## Encounter review: Assessment Team Withdrawal

### Full intended version

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL if attacks occur;
- status lifecycle — PARTIAL if ordinary statuses occur;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Full version status: BLOCKED FOR RICH SEMANTICS.

The full version would need active withdrawal, escort/Intercept, possible environmental displacement, changing safe areas and semantic playback.

### Reduced version

Status: READY.

Contract:

- Ouros ends or suspends the assessment activity first;
- assessors, private records, equipment and other noncombatants are removed from BattleSpec through world state;
- active wind/debris mechanics are not represented;
- the battle uses static geometry that has already been selected as safe enough for combat presentation;
- Ouros selects explicit combatants;
- victory records immediate access/perimeter outcome only;
- the authorized owner decides whether assessment resumes.

Forbidden automatic transitions:

- victory => `ASSESSMENT_COMPLETE`;
- victory => `SAFE_ACCESS_CONFIRMED`;
- victory => `WIND_CAUSE_CONFIRMED`;
- victory => route reopened;
- victory => building reentry authorized.

## Encounter review: Debris-Origin Chokepoint

### Full intended version

The rich version would require:

- controlled evidence/custody representation while combat is active;
- Intercept/protection behavior;
- potential forced movement;
- active debris or hazard zones;
- generalized reactions;
- objective-aware AI;
- semantic adapter playback.

No generalized battle contract exists for evidence-object custody, wind-blown debris or post-event provenance resolution.

Full version status: BLOCKED FOR RICH SEMANTICS.

### Reduced version

Status: READY.

Contract:

- the displaced object has already been documented and moved to safe custody by the appropriate owner;
- investigators/noncombatants withdraw before battle;
- the evidence object remains outside BattleSpec;
- static combat resolves only the independent threat at the chokepoint;
- post-battle investigation resumes through narrative state.

Combat cannot:

- identify the object;
- prove its origin;
- establish ownership;
- prove wind causation;
- authenticate evidence;
- decide liability;
- close the impact case.

## Encounter review: Displaced Pokémon Perimeter

### Full intended version

Rich semantics would want:

- explicit distinction between observation subjects and combatants;
- active observer withdrawal;
- Intercept/protection;
- generalized reaction windows;
- potentially changing environmental cells;
- objective-aware AI;
- semantic playback of wildlife observation state.

Full version status: BLOCKED FOR RICH SEMANTICS.

### Reduced version

Status: READY.

Contract:

- observation staff withdraw before BattleSpec;
- Pokémon under observation remain outside BattleSpec unless Ouros independently selects specific individuals as legitimate combatants;
- active wind remains narrative context only;
- combat occurs on static geometry;
- afterward Coexistence/Ecology/Wildlife Monitoring resume their own investigation.

Combat cannot prove:

- storm displacement;
- aggression;
- ecological risk;
- individual identity;
- ownership;
- custody;
- capture legality;
- relocation authority.

## Mechanical assumptions deliberately rejected

Pass 132 found no governing evidence sufficient to create universal mechanics for:

- generic wind push;
- generic gust Knockback;
- generic Pull or lift;
- forced movement based on character/Pokémon weight;
- forced movement based on size;
- forced movement based on Flying capability;
- flying-debris damage;
- falling-tree or branch damage;
- unstable-object reaction windows;
- hanging-sign hazards;
- roof-element collapse;
- wind-based accuracy penalties;
- ranged projectile deviation;
- movement penalties in strong wind;
- generic bracing;
- generic shelter bonuses;
- generic Acrobatics/Athletics checks against wind;
- repeated environmental checks each round;
- airborne status;
- environmental flinching;
- Type-derived wind resistance;
- Flying-type immunity to wind;
- Rock/Steel/Ground-type wind resistance;
- species-derived wind forecasting;
- species-derived structural hazard sensing;
- battle Weather inferred from world weather;
- world wind inferred from Rain Dance, Sunny Day, Sandstorm or Hail;
- Trainer Features that create emergency, forestry, utility or building-safety authority.

Specific PTU Weather, Move, Ability or Feature behavior may be used only when its exact governing rule and engine implementation are verified for the actual scenario.

## PTU/Caelo source boundary

The internal source scan establishes that Caelo locations may contain explicit environmental mechanics when a governing source defines them, such as the documented Toxic Ravine precedent.

That precedent is intentionally narrow.

It does not authorize generic wind mechanics elsewhere.

The public PTU community discussions checked this pass further illustrate why timing-sensitive Weather effects cannot be approximated: initiative/round timing materially changes behavior.

Community homebrew remains inspiration only and carries no rules authority.

## Narrative authority rule

Wind-impact operational truth stays outside battle authority.

Weather/Ouros owns:

- world weather observations;
- forecasts;
- actual episode occurrence;
- impact reports;
- evidence/provenance;
- impact scope;
- cause hypotheses;
- owner handoffs;
- residual conditions;
- Chronicle persistence.

Existing owner systems own:

- route closure/reopening;
- electrical state;
- structural assessment/reentry;
- tree/vegetation intervention;
- facility repair;
- public-space operation;
- ecological interpretation;
- Pokémon agency/custody.

AutoPTU owns tactical battle facts for explicit BattleSpecs.

Minecraft/Cobblemon/Craftics presents outcomes after those authoritative systems decide them.

## Minecraft/Cobblemon guardrails

Presentation may include:

- authored weather visuals;
- fallen trees already decided by Ouros;
- debris props;
- temporary barriers;
- boarded openings;
- repaired signs;
- changed NPC paths;
- temporary routes;
- service crews;
- altered vegetation;
- Pokémon appearing at authored observation locations.

Presentation cannot establish:

- damaging-wind threshold;
- cause of damage;
- tree health;
- live/dead electrical state;
- building safety;
- route authorization;
- debris ownership/origin;
- Pokémon displacement;
- capture legality;
- tactical forced movement.

Native Minecraft thunder, rain, particles, entity motion, block breakage, leaf decay, redstone state, collision and pathfinding remain non-authoritative unless an explicit adapter contract maps a governing rule.

Cobblemon BattleState remains outside combatant selection, legality, HP/status, tactical positions and narrative outcomes for Ouros.

## Cross-owner forbidden transitions

Never infer:

- wind observed => route closed;
- route obstructed => route legally closed;
- debris removed => route reopened;
- line observed down => outage confirmed;
- line repaired => service restored everywhere;
- building exterior damage => whole building unsafe;
- no visible damage => whole building safe;
- fallen tree => Forestry removal authorized;
- Pokémon present after storm => displaced by storm;
- battle victory => impact cause established;
- battle victory => assessment complete;
- battle victory => owner repair complete;
- battle victory => incident closed.

## Live-evidence conclusion

No capability-family promotion is justified in Pass 132.

The new narrative material can progress today through reduced static encounters and noncombat exploration because those designs deliberately keep active wind mechanics, noncombatant escort, owner decisions and environmental hazards outside BattleSpec.

The full versions remain blocked specifically where they require the still-PARTIAL complete-movement/lifecycle families and the still-BLOCKING terrain/weather/hazards/zones/reactions, tactical-policy and semantic adapter/playback families.

This distinction is intentional and should remain visible in future Ouros implementation work.
