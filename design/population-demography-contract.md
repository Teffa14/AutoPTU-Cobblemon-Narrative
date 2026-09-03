# Ouros population and demography contract

Status: PROPOSED DESIGN CONTRACT
Date: 2026-09-03
Pass: 238

## Purpose

Define how local wild Pokémon populations gain, lose and redistribute members without allowing Minecraft/Cobblemon visibility, habitat recovery or random encounter generation to author population truth.

This contract consumes ecology from Passes 227–237 and prepares the persistent-individual reconciliation work in Pass 239.

## Authority invariants

1. Ouros owns canonical population identity, abundance, life-stage structure and demographic events.
2. Minecraft/Cobblemon entity spawn, despawn, chunk load, chunk unload, vanilla death and entity count are presentation facts only.
3. AutoPTU owns structured battle mechanics after explicit handoff, but battle participation alone does not imply capture, death, emigration or population removal.
4. Every canonical abundance change must have a typed demographic event with provenance.
5. Habitat recovery changes demographic context; it never automatically refills abundance.
6. Local extirpation preserves the population record and history.
7. Recolonization requires a valid demographic source and connectivity path.
8. Named persistent Pokémon outside a wild population are never silently counted into it.

## Population record

Recommended minimum state:

```text
population_id
species_id
form_id
site_id
regional_group_id_or_null
status
stage_counts
known_persistent_member_ids
unresolved_member_pool
reference_abundance_range_or_null
effective_capacity_context
resource_pressure
shelter_pressure
predation_pressure
competition_pressure
disturbance_pressure
connectivity_state
last_demographic_tick
recent_demographic_event_ids
```

`unresolved_member_pool` represents canonical members that do not need individual identity yet. It is population truth, not a spawn budget.

## Population status

```text
RESIDENT
SEASONAL_RESIDENT
TRANSIENT
DECLINING
RECOVERING
LOCALLY_EXTIRPATED
RECOLONIZING
RELOCATED
```

Status is descriptive state derived from authored evidence. It does not independently add or remove members.

## Stage structure

Default semantic stages:

```text
DEPENDENT_JUVENILE
INDEPENDENT_JUVENILE
SUBADULT_OR_PREBREEDER
BREEDING_ADULT
NONBREEDING_ADULT
```

Species profiles may collapse, rename or extend these stages when official behaviour, life history or Ouros-approved ecology requires it.

Eggs and active nests remain separate persistent reproductive records until a successful recruitment event moves offspring into a population stage.

## Demographic event ledger

Every change in canonical abundance must be represented by one or more events.

```text
demographic_event_id
population_id
tick
event_type
count
from_stage_or_null
to_stage_or_null
source_population_id_or_null
destination_population_id_or_null
cause_code
provenance
confidence
related_world_event_id_or_null
related_battle_id_or_null
member_ids_if_resolved
```

Allowed event families:

```text
LOCAL_RECRUITMENT
STAGE_TRANSITION
IMMIGRATION
EMIGRATION
ECOLOGICAL_MORTALITY
CAPTURE_REMOVAL
RELEASE_RETURN
RELOCATION_OUT
RELOCATION_IN
MIGRATION_SETTLEMENT
MIGRATION_DEPARTURE
CORRECTION_WITH_AUDIT_PROVENANCE
```

A correction event exists only for explicit data repair. It must never be used as routine ecology logic.

## Arithmetic invariant

For a bounded demographic window:

```text
ending_count = starting_count
  + local_recruitment
  + immigration
  + release_return
  + relocation_in
  + migration_settlement
  - ecological_mortality
  - emigration
  - capture_removal
  - relocation_out
  - migration_departure
```

Stage transitions do not change total abundance.

Every delta must reconcile exactly to the event ledger.

## Recruitment

Local recruitment means members entered the population through in-situ reproduction and survived to the project-defined counted stage.

It is not equivalent to:
- an egg existing;
- a nest existing;
- mating behaviour;
- a juvenile being visually spawned;
- an outbreak occurring.

Recruitment eligibility can consume:

```text
breeding-capable stage counts
+ nesting/reproduction records
+ seasonal window
+ food/resource state
+ shelter/nest availability
+ disturbance state
+ density pressure
+ species-specific provenance
```

The resolver must emit a typed event rather than simply forcing abundance toward capacity.

## Survival and ecological mortality

Mortality pressure from Pass 237 and predation pressure from earlier ecology passes are risk/context. They do not remove members by themselves.

Canonical ecological mortality requires an authored demographic resolution event. The model may later use deterministic or seeded stochastic resolution, but the cause and count must be recorded.

Minecraft vanilla death cannot write this event.

## Immigration and emigration

Movement between local populations is paired when both source and destination are known.

```text
source: EMIGRATION count=N destination=X
destination: IMMIGRATION count=N source=Y
```

The transaction must conserve member count across the regional group unless mortality, capture, release or an external boundary event is also present.

Unknown external movement is allowed only when the world model explicitly defines an external population boundary. It must not be used to hide unexplained arithmetic.

## Density dependence and effective capacity

Ouros should represent density pressure without turning carrying capacity into an automatic thermostat.

Suggested context:

```text
base_habitat_suitability
resource_availability
shelter_and_nesting_availability
seasonal_context
competition_pressure
predator_pressure
disturbance_recovery_state
human_disturbance_state
route_connectivity
```

Possible outputs:
- recruitment suppression;
- increased dispersal pressure;
- reduced breeding participation;
- increased competition pressure;
- increased mortality risk.

Forbidden output:
- `count = capacity`.

## Local extirpation

When total canonical count reaches zero:

```text
status = LOCALLY_EXTIRPATED
```

The population identity, site history, causes, former stage structure and relationships remain persisted.

`LOCALLY_EXTIRPATED != DELETE_POPULATION_RECORD`

## Recolonization

A locally extirpated population can enter `RECOLONIZING` only through an explicit source event such as:
- immigration from a connected source population;
- migration settlement;
- return of known emigrants;
- authorized conservation relocation/release.

A generic Cobblemon spawn cannot recolonize a site.

## Persistent members versus unresolved pool

Known persistent individuals consume one canonical member each from the population total unless the population contract explicitly marks them as associated but external.

Target invariant for Pass 239:

```text
population_total
= known_persistent_members_count
+ unresolved_member_pool_count
```

A projected generic actor may represent an unresolved member temporarily, but the projection system must lease/bind that representation rather than manufacture a new member.

## Interaction with migration Pass 235

Migration cohorts and resident populations must use demographic settlement/departure events when membership changes.

Transit through a site does not automatically make a cohort resident.

A cohort can increase visible abundance without changing the resident local population if its members remain classified as transient.

## Interaction with disturbance/recovery Pass 237

Pass 237 provides habitat/resource/connectivity context and mortality/displacement pressure.

Pass 238 resolves whether those pressures result in:
- mortality;
- emigration;
- reduced recruitment;
- no demographic change;
- later recolonization opportunity.

The same habitat recovery trajectory can therefore produce different population trajectories.

## Minecraft/Cobblemon projection

Allowed reads from population truth:
- species availability eligibility;
- maximum concurrent presentation leases;
- life-stage presentation eligibility when supported by assets;
- activity/exposure weighting from ecology;
- persistent-individual projection requests.

Forbidden writes:
- entity spawn increments population count;
- entity despawn decrements population count;
- vanilla breeding creates recruitment;
- vanilla death creates ecological mortality;
- chunk unload marks emigration;
- mass visible entities imply abundance estimate is exact.

## Observation boundary

Pass 240 should expose uncertain evidence rather than raw truth.

```text
population truth
-> activity/exposure/projection
-> sightings/tracks/nests/calls/captures
-> observer estimate + confidence
```

Field research can improve estimate quality but cannot rewrite ground truth merely because a survey missed individuals.

## Player consequences

Examples of later ecology-driven consequences:
- repeated captures lower local abundance through `CAPTURE_REMOVAL`;
- protecting nesting habitat improves recruitment conditions but does not guarantee births;
- opening a corridor permits immigration but does not create immigrants;
- disturbing a recovering site can increase emigration pressure;
- releasing a captured local Pokémon can create `RELEASE_RETURN` when provenance proves origin.

## Structured encounter handoff

### Reduced version

Population state chooses explicit combatant identities or leases members before battle. AutoPTU executes a conventional legal battle. After resolution, Ouros consumes only semantic outcomes that are actually supported by the encounter result and world policy.

No demographic change is assumed from KO alone.

### Intended rich version

Ecology encounters may involve protecting juveniles, intercepting a dispersal group, preventing capture pressure, defending a recolonization corridor or escorting relocated Pokémon.

Permanent dependency classification:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL, improved by AutoPTU-Java `2ca8552c640c582c98e7a2cc4667a29426b8173a` wiring forced movement into shared landing consequences, but not promoted to complete;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING outside verified slices;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING as a complete family;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING end-to-end.

## Implementation acceptance

A deterministic Pass 238 fixture must prove:

1. habitat recovery without a demographic event leaves abundance unchanged;
2. local recruitment and immigration produce the same numeric delta through different provenance;
3. ecological mortality and emigration produce the same numeric loss through different provenance;
4. stage transitions conserve total abundance;
5. local count can reach zero without deleting the population record;
6. a generic spawn cannot recolonize the site;
7. valid recolonization requires source/connectivity provenance;
8. paired immigration/emigration conserves regional abundance;
9. server restart/chunk unload preserve ledger and totals;
10. a battle KO alone does not change population count.

## Canon status

PROPOSED.

This contract does not set the actual abundance of the canon Sendero Fletchling population, does not invent a breeding rate, does not authorize additional Marea species and does not change the first deterministic encounter blueprint.