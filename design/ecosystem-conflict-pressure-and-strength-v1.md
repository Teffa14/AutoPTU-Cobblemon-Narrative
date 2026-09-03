# Ecosystem conflict pressure and wild strength — v1

Status: PROPOSED SYSTEM CONTRACT / NON-CANON UNTIL APPROVED
Date: 2026-09-03
Depends on: `design/ecosystem-population-authority-v1.md`, `design/ecosystem-demographic-cycle-v1.md`, `design/wild-pokemon-behavior-tolerance-tactical-policy.md`
Research provenance: `research/2026-09-03-ecosystem-conflict-strength-management-scan-223.md`

## Purpose

Define an authoritative off-screen ecosystem process that can make wild populations change through repeated battles, predation, capture, migration, resource pressure, and management without running invisible PTU battles.

The system must create persistent consequences in population composition, future encounter strength, species behavior, NPC knowledge, and environmental evidence while preserving finite-population accounting.

## Authority rule

Ouros owns ecosystem truth.

AutoPTU owns real tactical battles when they occur.

Cobblemon/Minecraft owns presentation, entities, native spawn eligibility inputs, and world playback, but it must not decide hidden battle outcomes or manufacture population members.

An off-screen ecosystem conflict result is not a compressed AutoPTU transcript. It is an ecological state transition.

## Simulation cadence

Run conflict/demography in persisted windows rather than per tick.

A window may be daily, weekly, seasonal, or event-driven depending on scale. The exact cadence is configuration and must be stored with provenance so replay/debugging can reproduce a result.

Each window reads a frozen start snapshot and produces an atomic result ledger.

Suggested processing order:

```text
1. read ecosystem membership/cohorts
2. read season, resources, habitat patches, dependent sites, migration state
3. ingest actual player battle/capture/release events since previous window
4. estimate species-to-species contact pressure
5. estimate competition / territorial / predator-prey pressure
6. resolve aggregate behavioral and demographic consequences
7. update combat-profile distributions
8. apply institutional policy and interventions
9. emit environmental traces and observation opportunities
10. persist end snapshot and provenance
```

Order matters. Results must not depend on which chunks happened to be loaded.

## Conservation

All membership changes must continue to obey the demographic ledger.

Off-screen conflict may cause a death only through an explicitly configured ecological mortality function. If it does, that death is a real decrement and must appear in the demographic event ledger.

Conflict may instead produce displacement, avoidance, temporary injury pressure, altered habitat use, or no demographic change.

No result may be represented as despawn/respawn replacement.

## Core structures

### `ECOSYSTEM_CONFLICT_PRESSURE_WINDOW`

Candidate fields:

```text
window_id
ecosystem_id
opened_at
closed_at
season_context
population_snapshot_ref
resource_snapshot_ref
human_activity_summary
trainer_battle_events_ref
capture_release_events_ref
species_contact_matrix
predation_pressure_matrix
competition_pressure_matrix
territorial_pressure_matrix
management_policy_ref
random_seed_or_deterministic_inputs
result_ledger_ref
provenance
```

The matrices represent opportunity/pressure, not observed tactical battles.

### `POPULATION_COMBAT_PROFILE`

Candidate fields:

```text
ecosystem_id
species_or_population_id
cohort_scope
window_id
battle_exposure_index
wild_conflict_exposure_index
trainer_conflict_exposure_index
avoidance_tendency
escalation_tendency
confidence_or_contest_memory_state
competence_distribution
strength_materialization_policy
verified_ptu_mapping_ref|null
dangerous_outlier_tail
last_updated
```

The profile is a distribution. Do not store only `average_level`.

`competence_distribution` must remain an ecology/world variable until an accepted PTU/Caelo/Kairos rule maps it to mechanical Level, Experience, Moves, Stats, or other battle properties.

### `OFFSCREEN_CONFLICT_LEDGER`

Candidate result types:

```text
behavior_shift
habitat_displacement
resource_access_shift
territory_shift
injury_pressure
predation_attempt_pressure
confirmed_predation_loss
dominance_or_access_shift
contact_avoidance_shift
competence_pressure_change
management_trigger
no_material_change
```

Each result records evidence strength and the inputs/functions that produced it.

Never emit move names, HP deltas, Status, Initiative, exact attack rolls, or Item use from this ledger.

### `MANAGED_DEVELOPMENT_ZONE_POLICY`

A development zone is an administrative overlay on one or more habitat patches. It does not define an ecosystem and does not create weaker Pokémon.

Candidate fields:

```text
policy_id
jurisdiction_ref
covered_patches
purpose
intended_user_groups
risk_thresholds
monitoring_inputs
permitted_interventions
restricted_interventions
seasonal_overrides
review_interval
active_from
active_until|null
```

Possible purposes include allowing children/new Trainers to gain experience in an ecologically real area while maintaining a controlled risk envelope.

### `AUTHORITY_WILDLIFE_INTERVENTION`

Candidate intervention types:

```text
observe_more
warning_signage
trainer_or_public_advisory
patrol_increase
temporary_route_closure
temporary_access_window
attractant_removal
habitat_steering
deterrence
managed_capture
relocation
cross-ecosystem_transfer
specialist_response
```

The exact legal/institutional owner remains a canon question.

Relocation/cross-ecosystem transfer must use real membership transfer semantics. It cannot delete the actor.

### `ECOLOGICAL_TRACE_EVENT`

Candidate fields:

```text
trace_id
ecosystem_id
patch_id
created_at
decay_profile
trace_category
possible_causes
server_cause_ref|null
character_visible_evidence
confidence_if_interpreted
source_population_refs
world_projection_ref|null
```

Examples of safe generic trace categories:

- disturbed vegetation
- trampled ground
- feeding remains
- shed material
- damaged bark/branches
- abandoned use site
- changed trail intensity
- displaced nesting/roosting evidence
- unusual absence/presence pattern

Do not label a trace as caused by Flamethrower, Knockback, Poison, etc. unless a witnessed/source-authoritative event actually established that cause.

## Battle pressure from actual Trainer encounters

Actual Trainer-vs-wild battles are especially valuable because they are known events rather than statistical inference.

For each completed battle, the ecosystem layer may store high-level evidence such as:

```text
population member involved
outcome class
whether capture occurred
whether the member remained in ecosystem
whether the member fled/withdrew
approximate conflict intensity derived from verified transcript facts
location/time/context
```

The ecology layer may use this evidence to increase `trainer_conflict_exposure_index` and, if species-specific policy allows, alter later avoidance/escalation/competence state.

It must not award additional hidden XP on top of whatever AutoPTU already resolved.

## Wild-vs-wild conflict

### Contact opportunity

Estimate contact from ecology rather than arbitrary dice alone:

```text
shared patch use
x temporal overlap
x resource overlap
x territoriality
x reproductive/seasonal pressure
x predator-prey relationship
x density/contact opportunity
x species behavior profile
x recent disturbance
```

### Resolution

A contact does not imply a fight.

Possible abstract outcomes include avoidance, displacement, display, contest, predation attempt, successful predation, resource loss, or no change.

The algorithm records outcome class only at the ecological resolution it can justify.

### No invisible tactical authority

Even if a successful predation event is confirmed, the simulation does not fabricate a hidden battle to explain it. It records an ecological loss and later world evidence appropriate to the authored model.

## Strength and competence

### Keep three meanings separate

`biological_maturity` = age/life stage.

`combat_experience` = history of encounters/conflict exposure.

`PTU_strength` = source-authorized mechanical properties such as Level, Stats, Moves, Features, etc.

These variables may correlate but must never alias one another.

### Distribution-first representation

For population balancing, track at least a center and upper tail. A starter route can have a safe median while one unusually capable adult is still dangerous.

Suggested reporting:

```text
competence P25 / P50 / P75 / P90 / P99
outlier memberships when persistent/identified
sample confidence
last materialized PTU evidence
```

Exact quantiles are implementation choices, not canon.

### Strength-pressure algorithm

Until PTU mapping is audited, use a dimensionless `competence_pressure` rather than silently adding Levels.

Candidate update shape:

```text
competence_pressure_delta =
    successful_conflict_exposure
  + repeated_survival_exposure
  + species_learning_factor
  + selective_survival_pressure
  - injury_or_exhaustion_pressure
  - long_decay_without_relevant_exposure
```

All coefficients are species/context data and need calibration.

Critically, losing may change future behavior without making an individual stronger. Winning may increase confidence while also creating costs. The algorithm must support both.

## Managed starter/development zones

### Safety is an institutional feedback loop

A development zone may have many Trainer battles. This is desirable if the route exists to help children/new Trainers develop.

The zone remains suitable through monitoring and intervention:

```text
frequent battles
-> population exposure changes
-> surveys / battle records / incident reports update risk model
-> dangerous upper tail or inappropriate species movement detected
-> authority chooses intervention
-> actual population/world state changes
-> route remains open, restricted, or temporarily closed based on evidence
```

### No magical level ceiling

Never implement:

```text
if zone == starter:
    wild_level <= 5
```

unless a separate PTU generation rule intentionally creates a bounded encounter and the world can explain why those members are present.

The ecological system should instead make overly dangerous individuals uncommon through management consequences:

- deterrence from high-use corridors;
- attractant/resource management;
- managed capture;
- relocation with real destination membership;
- temporary closure until an outlier moves naturally;
- specialist intervention;
- habitat steering;
- seasonal schedule changes.

### Strong outliers are content

When a dangerous member appears, do not normalize it away.

That event can generate:

- NPC warnings;
- route signs;
- patrol changes;
- school/parent concern;
- research interest;
- temporary rerouting;
- a supervised response quest;
- evidence of why it entered the corridor.

A safe region becomes credible because people maintain it, not because ecology stops working there.

## Capture and selection pressure

A capture is a demographic subtraction plus possible selection effect.

If players disproportionately catch bold, visible, attractive, rare, or high-competence individuals, remaining behavior/strength distributions may shift even before total abundance becomes critical.

Do not universalize the direction. Different species and encounter systems can produce different selection effects.

## Predators and trophic cascades

Predator pressure can:

- remove prey members;
- displace prey into different patches/times;
- alter detectability;
- alter resource use;
- indirectly change vegetation/resource pressure;
- attract management attention when predators approach development corridors.

Removing many predators can therefore raise prey pressure later. Removing many prey can reduce predator support later.

These effects should pass through diet/resource/ecosystem profiles and demographic windows rather than immediate spawn-weight edits.

## World manifestation

Every material ecosystem change should have one or more possible player-facing channels.

### NPC knowledge

NPCs consume evidence, not server omniscience:

```text
patrol logs
battle reports
capture records
survey counts
tracks/traces
injury/remains observations
route incidents
historic comparison
```

Their conclusions have confidence and can be wrong.

### Habitat presentation

Persistent pressure may gradually change:

- trail use;
- vegetation damage/recovery;
- feeding-site use;
- nesting/roosting placement;
- avoidance corridors;
- resource depletion;
- visible remains/traces;
- ambient species composition projected from the real ledger.

Changes should age/decay. One abstract contest should not permanently scar a forest.

### Species behavior

Population or individual behavior profiles may change tolerance, withdrawal distance, approach strategy, group spacing, resource defense, or likelihood of escalation when source/context supports it.

That behavior feeds the existing wild tactical policy when a real encounter begins.

## Determinism and auditability

Every window must retain enough inputs to answer:

- why did population X get stronger/weaker/more avoidant?
- why did abundance change?
- why did authorities intervene?
- why does this trace exist?
- was the effect caused by actual player battles, an abstract ecological window, migration, capture, or a scripted world event?

Use deterministic seeds or persisted random draws. Never reroll history when a chunk reloads.

## Reduced implementation path

A first runnable implementation does not need off-screen PTU combat.

It can support:

1. finite population ledger;
2. actual player battle counters by population;
3. one `competence_pressure` distribution with no PTU Level mapping;
4. one predator-prey pressure matrix producing only displacement or demographic loss;
5. one managed development-zone risk threshold;
6. one authority response that changes access or relocates a real member;
7. one trace event projected into the world;
8. one NPC report derived from that trace/incident.

This proves the ecosystem feedback loop without faking missing battle mechanics.

## Rules/source gates before PTU strength materialization

Before `competence_pressure` can alter Level/XP/Stats/Moves/Evolution, audit the supplied PTU/Caelo/Kairos material for:

- Pokémon leveling/training rules;
- XP awards and recipients;
- wild Pokémon generation/encounter-level guidance;
- whether wild-vs-wild conflict awards mechanical progression;
- injury/death consequences;
- evolution triggers;
- encounter creation constraints.

Until then, strength pressure can influence encounter selection only by selecting among already legal/source-backed mechanical profiles, not by inventing new ones.

## Permanent battle capability dependencies

This world-simulation contract itself requires no AutoPTU battle category and proves none.

A live capture/relocation/containment encounter may require:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Only activate the families actually used by a concrete encounter.

## Canon boundary

This file does not yet canonize:

- a named starter route;
- an authority with relocation powers;
- numerical safety thresholds;
- a universal species learning rate;
- any mapping from conflict exposure to PTU Level;
- any specific predator/prey relationship in Marea;
- a specific dangerous wild individual.
