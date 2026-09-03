# Ecosystem conflict, strength and world-feedback simulation v1

Status: PROPOSED ARCHITECTURE
Date: 2026-09-03
Pass: 223

## Intent

Extend pass 221 finite populations and pass 222 demography with an abstract world simulation that lets wild populations become stronger through repeated conflict, lose or redistribute members through capture and predation, and visibly reshape the ecosystem over time.

Most off-screen wild-vs-wild interactions are not AutoPTU battles. They are population/world simulation. Their aggregate consequences become canonical world state. Any real on-screen battle still belongs to AutoPTU.

## 1. Four authorities, not one number

For each ecosystem population keep separate state for:

1. abundance and demography — how many members exist and their life stages;
2. strength distribution — how combat-capable the population has become;
3. ecological pressure — predation, competition, capture, resources, disturbance and habitat use;
4. management/risk state — what local institutions are doing to keep human-use areas within an acceptable danger envelope.

Do not collapse these into `area_level` or `spawn_difficulty`.

A low-population ecosystem can contain a few very strong survivors. A high-population ecosystem can contain many weak juveniles. A starter area can have many battles without being allowed to accumulate unmanaged high-danger outliers.

## 2. Population conflict-pressure state

Candidate `ECOSYSTEM_CONFLICT_PRESSURE_STATE`:

```text
population_id
ecosystem_id
window_id
resolved_trainer_battle_count
resolved_trainer_battle_severity
capture_count
capture_pressure
wild_conflict_pressure
predation_pressure_outgoing
predation_pressure_incoming
resource_competition_pressure
territorial_pressure
human_disturbance_pressure
combat_exposure_pressure
recent_management_pressure
confidence/provenance
revision
```

`resolved_trainer_battle_count` is sourced only from battles that actually occurred and were authoritatively resolved.

`wild_conflict_pressure` is an ecological estimate. It does not imply hidden battle logs.

## 3. Abstract ecological conflict resolver

Candidate window resolver:

```text
for each interacting population pair or within-population conflict class:
    overlap = spatial_overlap * temporal_overlap
    opportunity = abundance_available * activity_factor
    motive = competition + predation + territorial/social drivers
    context = resources + season + disturbance + behavior_priors

    expected_conflict_pressure = f(overlap, opportunity, motive, context)

    resolve_seeded_bounded_aggregate_outcomes()
    persist_result_once()
```

Outputs may include:

```text
conflict_exposure_delta
predation_consumption_count
displacement_pressure_delta
resource_pressure_delta
habitat_disturbance_delta
behavior_pressure_delta
background_injury_or_mortality_transition only if an approved world rule exists
```

Forbidden outputs:

```text
fake Move use
fake initiative
fake damage numbers
fake Status Afflictions
fake Ability/Item/Feature triggers
fake AutoPTU battle result
```

An abstract predation result can remove one prey membership through a demographic mortality/consumption event. It cannot narrate the nonexistent tactical fight as if AutoPTU resolved it.

## 4. Strength distribution

Wild populations need persistent strength state independent of recurring NPC scaling.

Candidate `WILD_POPULATION_STRENGTH_PROFILE`:

```text
population_id
strength_cohort_ids[]
combat_exposure_index
recent_strength_drift
upper_tail_risk
last_progression_resolution
revision
```

Candidate `WILD_STRENGTH_COHORT`:

```text
cohort_id
life_stage
count
progression_band
combat_exposure_memory
survivor_pressure
projection_level_policy_ref
```

`progression_band` is Ouros world state. Its conversion to an exact legal PTU Level must be handled by an audited projection/progression policy and validated by AutoPTU before battle assembly.

Do not reuse `canon/npc-pokemon-dynamic-progression-v1.md` for wild populations. That canon rule intentionally derives recurring NPC partner level from the player's party reference. Wild strength must instead come from its ecosystem/population history.

## 5. Strength update algorithm

Resolve progression in persisted world windows rather than after every abstract conflict.

Conceptual function:

```text
raw_exposure =
    trainer_battle_weight * resolved_trainer_battle_pressure
  + wild_conflict_weight * wild_conflict_pressure
  + predation_conflict_weight * predator_or_prey_conflict_pressure

opportunity_modifier = f(resources, health_survival, life_stage, season)
selection_modifier = f(capture_pattern, predation_pattern, mortality, emigration)
management_modifier = f(relocation_or_deterrence_affecting_exposed_members)

progression_pressure = bounded(raw_exposure * opportunity_modifier)

new_strength_distribution =
    resolve_strength_transition(
        old_distribution,
        progression_pressure,
        selection_modifier,
        recruitment_and_immigration,
        departures_and_captures,
        seeded_window_state
    )
```

Important rules:

- more battles can push the surviving population stronger;
- battle count alone cannot instantly grant arbitrary Levels;
- new juveniles/recruits can pull the distribution downward even while veterans grow stronger;
- capture can remove members from particular exposure/strength bands;
- predation can reduce prey abundance and selectively change survivor composition;
- immigration/emigration can change the distribution without local battles;
- no automatic normalization returns the population to a target level.

## 6. Persistent individuals

A persistent wild individual can keep exact historical state rather than being regenerated from the population distribution every appearance.

Candidate additions:

```text
persistent_wild_progression:
  ecological_exposure_refs[]
  actual_battle_refs[]
  progression_state
  last_strength_resolution
  population_origin
```

Actual battle results may update that individual only through approved progression/result contracts.

Abstract ecological exposure can contribute to a world progression policy without fabricating a battle transcript.

Once a generic projected member is promoted to persistent identity, its generated legal combat state becomes part of that identity according to the governing persistence policy; reloading cannot reroll it merely to fit a new local average.

## 7. Starter and child-development zones

Starter zones are not naturally weak forever. They are actively managed high-encounter, low-unmanaged-danger landscapes.

Candidate `MANAGED_DEVELOPMENT_ZONE_POLICY`:

```text
zone_id
ecosystem_id
high_encounter_availability_target
beginner_access_context
risk_observation_thresholds[]
dangerous_outlier_policy_ref
monitoring_effort
patrol_or_response_refs[]
closure_or_escalation_policy_ref
relocation_destination_policy_ref?
public_warning_policy_ref?
revision
```

Desired equilibrium is causal, not magical:

```text
many beginners/trainers
-> many legitimate battles
-> wild survivor exposure rises

but also
-> captures remove members
-> recruitment/immigration supplies new lower-exposure members
-> ordinary dispersal exports some members
-> authorities identify dangerous outliers
-> targeted management prevents those outliers from remaining unmanaged near children
```

There is no `if level > threshold then despawn()` rule.

A dangerous wild Pokémon can enter or emerge in a starting zone. That is a real world event. Authorities can respond by monitoring, restricting access, deterrence, containment/escort, relocation or another canon-approved action. If relocation occurs, the member transfers to a destination ecosystem and can affect that ecosystem instead of disappearing.

The exact institution, danger thresholds and legal intervention toolkit are unresolved until canonized.

## 8. Actual Trainer battles feed the ecology

When an actual wild battle happens:

```text
Ouros selected/projected participant
-> AutoPTU authoritative battle
-> semantic authoritative result
-> world writeback
```

Potential world writeback, only when supported by the battle/result contract:

```text
battle_exposure
capture_removal
persistent_injury_or_state
death if the rules/world explicitly support it
participant displacement/location consequence
relationship/behavior evidence
```

The ecosystem simulator never reconstructs missing battle details from visual playback.

## 9. Wild-vs-wild conflicts stay abstract unless observed as real encounters

Off-screen:

```text
population simulation -> aggregate pressure/outcome
```

If players physically witness or intervene in a specific wild-vs-wild confrontation, that encounter may be promoted to explicit participants and a real AutoPTU BattleSpec when the necessary engine families are supported.

Do not run invisible AutoPTU battles merely to update a seasonal ledger.

## 10. Predator-prey effects

Predation operates through at least two paths.

Consumptive:

```text
predation event
-> prey membership removed through authoritative demographic transition
-> predator/resource state may improve according to species/world model
```

Non-consumptive:

```text
predation risk
-> prey activity/tolerance/distribution changes
-> foraging/resource pressure shifts
-> later habitat consequences change
```

Predator abundance can therefore change prey population and behavior even when only some interactions end in consumption.

Do not invent predator/prey relations without provenance.

## 11. Habitat and landscape feedback

Candidate `ECOSYSTEM_IMPACT_STATE`:

```text
ecosystem_id
habitat_patch_id
forage_depletion
browsing_pressure
sapling_recruitment_pressure
trampling_or_trail_pressure
nesting_or_structure_pressure
territorial_disturbance
soil_or_water_disturbance?
resource_regeneration_state
recovery_pressure
source_population_refs[]
last_resolution
revision
```

Not every field applies to every biome/species.

Population actions can accumulate into visible habitat state. Examples:

- abundant browsing species reduce successful sapling recruitment;
- repeated feeding depletes a resource patch;
- dense movement creates visible trails or disturbed ground;
- predator pressure shifts prey away from one patch, allowing local resources to recover;
- nesting/territorial use can concentrate activity around selected structures;
- migration can move the pressure somewhere else.

Minecraft/Cobblemon renders semantic habitat state through authored, reversible world changes. It must not infer ecology directly from random block breakage.

## 12. Trees and vegetation

Tree response should be slow and stateful.

Possible progression:

```text
healthy_regeneration
-> repeated_browsing_or_trampling_pressure
-> fewer_successful_seedlings_or_saplings
-> changed_understorey_or_open_patches
-> long_term_altered_tree_recruitment
```

Recovery may also be visible when pressure falls.

Do not make a single abstract battle knock down a mature tree unless an actual world event authoritatively did so. Aggregate ecology changes the landscape through accumulated pressure windows.

## 13. NPC inference layer

NPC knowledge remains separate from world truth.

Candidate observations:

```text
more_or_fewer_sightings
known_marked_individuals
unusual_strength_during_actual_battles
fresh_predation_evidence
missing_juveniles
browse_lines_or_damaged_saplings
resource_depletion
changed_calls_or_activity_times
tracks_or_trails
patrol_reports
capture_records
relocation_records
```

NPCs form beliefs from those observations. Ordinary residents do not read `combat_exposure_index` or canonical population totals.

Institutions may have better records, but still only within their legitimate monitoring coverage.

This allows ecology to generate rumors, research, policy debates and quests without making NPCs omniscient.

## 14. Behavior feedback

The wild behavior policy receives ecosystem pressures as context.

Examples:

- repeated Trainer battle/capture exposure can increase wariness in a population if a species/context model supports learning/habituation;
- heavy predator pressure can shift activity or escape priorities;
- depleted resources can increase competition or dispersal pressure;
- dense safe human exposure can still increase tolerance where established;
- strong individuals do not automatically become aggressive.

Behavioral pressure changes priors/context. It does not grant unverified Moves, Status or Features.

## 15. Prevent runaway simulations

Use:

- explicit time windows;
- seeded/persisted resolution;
- bounded per-window strength transitions;
- delayed ecological feedback;
- stage-specific recruitment;
- conservation-preserving transfers;
- source-backed interaction graphs;
- hysteresis/recovery so vegetation does not flicker between states;
- confidence/provenance for inferred inputs.

Never use hidden rubber-banding that silently recreates population or lowers Levels because the player is new.

## 16. Example causal chains

### High-battle starter route

```text
high Trainer traffic
-> high battle exposure
-> survivor strength drifts upward
-> capture turnover + recruitment continue
-> upper-tail outlier detected
-> authority response
-> outlier relocates or access temporarily changes
-> route stays battle-rich without static weak spawns
```

### Predator loss

```text
predator population falls
-> prey predation pressure falls
-> prey abundance/activity rises
-> browsing/foraging pressure rises
-> sapling recruitment declines
-> NPCs first notice damaged vegetation and more prey sightings
```

### Capture boom

```text
rare/high-value population gets heavily captured
-> abundance falls
-> strength/stage distribution changes according to who was removed
-> wild conflict frequency may fall
-> predator diet/territory pressure shifts
-> resource pressure changes
-> migration/authority response may follow
```

### Strong neighboring population enters starter area

```text
season/migration/disturbance moves strong members inward
-> starter-zone risk envelope exceeded
-> sightings/battle reports rise
-> authority warning/patrol/management event
-> children/beginners may face route restrictions
-> resolution changes destination population, not a despawn table
```

## 17. Implementation cadence

Recommended:

```text
EVENT WRITEBACK
actual battles, captures, explicit relocations, observed persistent events

SHORT ECOLOGY WINDOW
activity, distribution, resource use, conflict exposure, local disturbance

DEMOGRAPHIC/STRENGTH WINDOW
recruitment, mortality, migration, strength-distribution transitions

SEASONAL/LANDSCAPE WINDOW
vegetation recovery/change, migration regime, institutional planning
```

Cadences are configuration. Do not tie them directly to every Minecraft tick.

## 18. Engine capability boundary

`ABSTRACT_ECOLOGICAL_CONFLICT` is world simulation, not AutoPTU combat and not a seventeenth permanent capability family.

For the off-screen resolver itself:

- targeting/footprints/range/LoS: not required for hidden aggregate resolution;
- base movement legality: not required unless an exact movement event is promoted to world fact;
- complete movement: not required for aggregate conflict;
- core calculations: PTU combat calculations not required;
- action economy/initiative: not required;
- full turn/round lifecycle: not required;
- full stateful damage pipeline: not required;
- status lifecycle: not required;
- terrain/weather/hazards/zones/reactions: ecological weather/terrain context may be read as world data, but PTU tactical mechanics are not simulated;
- move-specific behavior: not required;
- abilities: not required unless a source-backed ecological behavior contract later explicitly consumes one without fabricating combat;
- items: not required;
- Trainer Features/perks: not required off-screen;
- AI legal-action infrastructure: not required;
- AI tactical policy: not required;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for complete visible world feedback.

When a specific encounter becomes a real battle, every mechanic actually used inherits the normal engine dependency classification.

## 19. Interaction with current engine state

AutoPTU-Java head inspected for this pass: `c62e59beb9472116e55f36d5814fa1ef1f95ced6`, adding an authoritative tile-trap state store. This improves one tactical state capability but does not affect the abstract ecology boundary or complete the relevant mechanic families globally.

Python AutoPTU head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its latest change is presentation coordinate synchronization and does not alter world ecology or combat rules.

## 20. Acceptance tests

1. Ten off-screen wild conflicts can increase population conflict exposure without creating ten BattleSpecs.
2. Re-running the same ecology window after restart produces no duplicate strength/predation result.
3. A high battle count can shift survivor strength upward over time but cannot directly fabricate exact PTU XP.
4. Capture of a strong persistent wild removes that exact member and does not regenerate a replacement.
5. Predation consumption removes prey membership exactly once.
6. Predator presence can alter prey habitat use without a prey death.
7. A starter zone can contain high encounter volume while management prevents persistent dangerous outliers from remaining unmanaged.
8. Relocating an outlier transfers it to a real destination instead of deleting it.
9. A vegetation-pressure state can reduce sapling projection/recruitment without pretending a hidden Move damaged every tree.
10. Lower ecological pressure allows authored recovery rather than instant biome reset.
11. NPCs react to observation/report records, not hidden simulator variables.
12. An actual witnessed battle still requires AutoPTU authority.

## 21. Canon status

PROPOSED until explicit promotion.

This architecture does not yet canonize numerical battle weights, predator/prey pairs, starter-zone boundaries, authority jurisdictions, danger thresholds, exact strength bands or vegetation response rates.