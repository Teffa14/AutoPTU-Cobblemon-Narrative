# Engine Readiness Snapshot — Pass 131

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-23
Narrative topic: Climate Baselines, Long-Term Change & Adaptation

This snapshot records read-only live evidence used to classify the encounter dependencies introduced in Pass 131. It does not modify AutoPTU-Java or AutoPTU.

## Inspected revisions

### AutoPTU-Java

Repository: `Teffa14/AutoPTU-Java`
Inspected `main`: `3ede4a8493738ddc70b2f0eb3959973488f78db9`
Latest inspected commit: `Freeze area-escape reaction movement contract (#161)`
Commit date: 2026-08-23

Immediately preceding relevant evidence:

- `7de79dcd30b241d439724050fb24ee893a7c5c63` freezes PUSH/PULL forced-movement instruction parsing but explicitly does not execute displacement.
- `3ede4a8493738ddc70b2f0eb3959973488f78db9` adds a parity-backed destination-selection contract for specific area-escape reaction patterns derived from Python Perception/Telepathy hooks.

What the new area-escape contract actually proves:

- given an origin;
- given externally supplied reachable legal tiles;
- given threatened tiles;
- optionally given a maximum displacement distance;
- Java can choose the same safe destination as the pinned Python hook pattern for the tested cases.

What it does not prove:

- generic reaction dispatch;
- spending/eligibility for every reaction;
- movement execution inside authoritative battle state;
- interception;
- Push/Pull execution;
- knockback/collision chains;
- obstacle/fall resolution;
- movement-triggered hazards;
- dynamic objective movement;
- complete Perception/Telepathy Feature/Ability behavior;
- broad terrain/weather/hazard/reaction support.

Interpretation:

This is meaningful progress inside the blocked `complete movement` and `reactions` space. It is too narrow to promote either permanent capability category.

### AutoPTU Python

Repository: `Teffa14/AutoPTU`
Inspected latest visible `main`: `99ba07ea47b8896d96bd37f6c06cffb8695f69bb`
Latest inspected commit: `test(career): lock capture overflow to PC (#68)`
Commit date: 2026-08-23

Observed evidence:

- the latest visible Python change is Career/persistence regression coverage for seventh-Pokémon overflow to PC;
- it verifies capture-resource/event behavior in Career state;
- it does not change the tactical capability classification used by this narrative task.

## Java README boundary

The live Java README still explicitly lists as incomplete:

- core combatant/grid battle state expansion;
- full damage resolution;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec → BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Therefore representative parity contracts must not be generalized to whole categories.

## Permanent capability map

### VERIFIED

#### targeting / footprints / range / LoS

Static battle targeting geometry remains sufficiently evidenced.

Climate non-inference:

Geometric LoS does not prove visibility through smoke, fog, heat shimmer, snowfall or other environmental presentation. Those require their own validated mechanics.

#### base movement legality

Ordinary static Shift/jump legality remains sufficiently evidenced for the project’s VERIFIED classification.

Climate non-inference:

Legal movement on a frozen snapshot does not prove escort, evacuation, crossing objectives, wind displacement or moving hazard fronts.

#### core calculations

Existing calculation primitives remain VERIFIED.

No climate baseline, anomaly, trend or scenario creates a new combat calculation.

#### action economy / initiative

Existing initiative/action-budget foundations remain VERIFIED.

Long-term climate exposure does not alter initiative.

#### AI legal-action infrastructure

The engine can constrain choices to legal actions.

It does not prove policy goals such as `WITHDRAW`, `REACH_SITE`, `PROTECT_EQUIPMENT`, `EVACUATE`, `CLEAR_ROUTE` or `AVOID_HAZARD`.

### PARTIAL

#### full turn / round lifecycle

Many lifecycle slices are parity-backed, but the complete lifecycle remains unproven.

Pass 131 rule:

Climate itself never owns battle phase progression. A current environmental encounter may depend on lifecycle only when its real PTU mechanics require timed effects.

#### full stateful damage pipeline

Substantial behavior exists, but the full family is not verified.

Climate trend, baseline or adaptation state never creates damage. Current fire, heat, flood or other hazards require separate validated mechanics.

#### status lifecycle

Multiple status application/prevention/removal slices exist, but the controller remains incomplete.

Pass 131 does not add:

- heat-exposure Status;
- cold-exposure Status;
- smoke Status;
- climate fatigue;
- climate sickness;
- long-term environmental debuffs.

#### move-specific behavior

Many Move slices exist, including forced-movement instruction parsing and delayed-hit work, but catalog completeness remains unproven.

No weather Move changes long-term climate state.

#### abilities

Many Ability families have parity evidence. Catalog completeness remains unproven.

Weather-related or environmental Ability flavor does not grant climate-control authority.

#### items

Item support remains partial.

A sensor, climate archive, monitoring station or adaptation material is not a PTU Item unless explicitly mapped.

#### Trainer Features / perks

Generic gates/effects have progressed substantially in prior passes, but the Feature catalogue remains partial.

Climate research employment or adaptation work does not grant Researcher, Survivalist or other Features.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

Status: BLOCKING.

New evidence:

Java can now choose a safe area-escape destination for a narrow parity-backed Perception/Telepathy reaction pattern when legal reachable tiles are already supplied.

Why still blocked:

- destination selection is not generic movement execution;
- Push/Pull parsing is not displacement;
- interception is not proven;
- dynamic route/escort behavior is not proven;
- obstacle/collision/falling/occupied-space rules for forced movement are not proven.

Pass 131 full encounters that move technicians, responders, wildlife or objective actors still depend on this BLOCKING family.

#### terrain / weather / hazards / zones / reactions

Status: BLOCKING.

The new area-escape reaction contract is one narrow reaction-movement selection primitive. The Java README still lists terrain, hazards and reactions as incomplete.

Climate-specific rule:

A long-term warm trend, drought trend or revised baseline cannot produce battle Weather. Even a current heatwave/fire/flood must go through the owning world layer and a validated PTU/AutoPTU environmental contract.

#### AI tactical policy

Status: BLOCKING.

Legal choices do not prove purpose-aware behavior.

Pass 131 full versions may need:

- `PROTECT_EQUIPMENT`
- `REACH_SITE`
- `CLEAR_ROUTE`
- `WITHDRAW`
- `REACH_GROUP`
- `AVOID_CIVILIANS`

Those goals remain unverified.

#### Minecraft / Cobblemon / Craftics adapter and playback

Status: BLOCKING.

Pass 131 adds a specific authority guard:

Minecraft biome values, snow blocks, rain particles, vegetation, loaded Pokémon counts and local clocks cannot become climate observations or climate truth automatically. They are projections/sensors only when a server-authoritative contract explicitly records them.

## Pass 131 overworld blockers

These are world-state systems, not AutoPTU-Java responsibilities:

- `CLIMATE_REGION_STATE`
- `CLIMATE_INDICATOR_SERIES`
- `CLIMATE_BASELINE_VERSIONING`
- `CLIMATE_ANOMALY_RECORDS`
- `CLIMATE_TREND_ASSESSMENTS`
- `CLIMATE_ATTRIBUTION_CLAIMS`
- `CLIMATE_REGIME_SHIFT_CASES`
- `CLIMATE_VULNERABILITY_PROFILES`
- `CLIMATE_SCENARIO_SETS`
- `CLIMATE_ADAPTATION_PLANS`
- `CLIMATE_ADAPTATION_REVIEWS`
- `CLIMATE_TO_METEOROLOGY_HANDOFF`
- `CLIMATE_TO_PHENOLOGY_HANDOFF`
- `CLIMATE_TO_CRYOSPHERE_HANDOFF`
- `CLIMATE_TO_FRESHWATER_GROUNDWATER_HANDOFF`
- `CLIMATE_TO_WILDFIRE_ARIDITY_HANDOFF`
- `CLIMATE_TO_COASTAL_MARINE_HANDOFF`
- `CLIMATE_TO_MIGRATION_ECOLOGY_HANDOFF`
- `CLIMATE_TO_INFRASTRUCTURE_GOVERNANCE_HANDOFF`
- `CLIMATE_TO_COBBLEMON_REVIEW_HANDOFF`
- `CLIMATE_TO_MINECRAFT_PROJECTION`

## Encounter dependency matrix

### `CLIM-131-A — High Pass Sensor Retrofit`

FULL dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if current weather is tactical
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

REDUCED readiness:

Implementable as overworld travel/weather/sensor work plus a static legal battle if conflict remains.

### `CLIM-131-B — Early Fire-Season Relay`

FULL dependencies:

- complete movement — BLOCKING
- terrain/weather/hazards/zones/reactions — BLOCKING if current fire/smoke/wind is tactical
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING
- ordinary static battle foundations — usable under existing VERIFIED/PARTIAL categories

REDUCED readiness:

Keep responders, fire perimeter and relay deployment in world state. Use a static battle only on a safe fixed access segment.

### `CLIM-131-C — Heat-Night Monitoring Walk`

FULL dependencies:

- complete movement — BLOCKING for mobile route objectives
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING
- terrain/weather/hazards/zones/reactions — BLOCKING only if current heat becomes tactical through validated rules

REDUCED readiness:

Run the monitoring transect as world state. Evacuate surveyors/civilians before any battle. Use one fixed arena for unavoidable conflict.

### `CLIM-131-D — The Baseline Dispute`

Battle dependency: NONE.

This is a Science/Metrology/Archives problem. A battle outcome has no evidentiary value for choosing a climate baseline.

## Specific non-inferences added by Pass 131

Do not infer:

- weather event → climate trend;
- several unusual years → confirmed trend without an assessment;
- trend → cause;
- new baseline → old observations invalid;
- anomaly relative to one baseline → same anomaly relative to every baseline;
- scenario → forecast;
- forecast → future fact;
- historical baseline → mandatory management target;
- long-term climate state → battle Weather;
- drought trend → Sandstorm;
- warming trend → Sunny Day/Harsh Sunlight;
- cooling trend → Hail/Snow Weather;
- climate change → Status or damage;
- climate change → regional form/evolution/Type/Ability/stat/Move;
- climate change → extinction/local extirpation;
- climate change → migration without ecological evidence;
- loaded Cobblemon count → population trend;
- Minecraft biome temperature → authoritative climate record;
- weather-linked Pokémon → climate cause;
- Legendary presence → climate cause;
- area-escape destination-selection contract → complete reactions;
- forced-movement instruction parsing → forced movement execution.

## PTU/Caelo validation status

The full named Caelo corpus was not available as a reliable invocable source during this run. Super PTU Online Helper was not exposed as an invocable capability.

No new PTU/Caelo rule is asserted for:

- long-term climate exposure;
- heat/cold exposure;
- climate-driven migration;
- climate-driven evolution;
- environmental adaptation bonuses;
- climate Weather;
- climate-related Skills/Features;
- scenario prediction.

## Capability conclusion

Pass 131 does not justify a permanent-category promotion.

Correct live classification:

VERIFIED:

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

PARTIAL:

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

BLOCKING:

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter / playback

The new area-escape reaction destination-selection contract is useful narrow evidence. It does not change that classification.