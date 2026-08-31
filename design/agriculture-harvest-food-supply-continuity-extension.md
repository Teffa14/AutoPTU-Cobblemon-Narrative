# Ouros Agriculture, Harvest & Food-Supply Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This extension gives Ouros persistent continuity for farms, orchards, ranches, berry plots, harvests, storage and seasonal food supply without inventing a universal farming simulator, food law, domestication model or automatic Pokémon labor system.

It tracks what was planned, cultivated or raised, what was actually harvested, what happened afterward, what supply was released or lost, what temporary substitutions emerged, and how production later recovered.

## Existing authority boundaries

Material Culture owns physical item and batch identity, custody, ownership claims and provenance.

Ecology, wildlife, conservation, weather, water, soil or other environment layers own observed environmental facts and scientific interpretation inside their established scopes.

Infrastructure owns authored irrigation assets, pumps, roads, storage-support equipment and service interruptions.

Workplace systems own workers, assignments and ordinary job continuity.

Markets and shops own offers, sales and commercial transactions.

Travel, freight and transport layers own movement between locations.

Care owns health and treatment facts for people and Pokémon.

Investigation owns evidence, hypotheses and causal claims.

AutoPTU owns tactical state and outcomes covered by BattleSpec and verified mechanics.

Minecraft/Cobblemon/Craftics owns presentation and playback only.

This extension owns longitudinal production and food-supply continuity between those systems.

## Production site record

```yaml
production_site:
  site_id: null
  canonical_name: null
  site_type: null
  location_ref: null
  operator_or_caretaker_refs: []
  workplace_refs: []
  infrastructure_dependency_refs: []
  environment_dependency_refs: []
  material_input_refs: []
  ordinary_output_category_refs: []
  current_activity_state: UNKNOWN
  provenance_refs: []
  chronicle_event_ids: []
  canon_status: proposed
```

Candidate descriptive site types include FARM, ORCHARD, BERRY_PLOT, RANCH, GREENHOUSE, GARDEN, FORAGE_MANAGEMENT_SITE, PROCESSING_SITE, STORAGE_SITE and OTHER_AUTHORED_PRODUCTION_SITE.

A type does not grant mechanics, yields, legal status or Pokémon ownership.

## Production cycle

```yaml
production_cycle:
  cycle_id: null
  site_ref: null
  product_or_output_refs: []
  planned_start: null
  observed_start: null
  expected_window_ref: null
  actual_harvest_window_ref: null
  participant_refs: []
  pokemon_work_participation_refs: []
  dependency_refs: []
  intervention_refs: []
  observation_refs: []
  yield_estimate_claim_refs: []
  status: PLANNED
  provenance_refs: []
```

Candidate states:

PLANNED
PREPARATION
ACTIVE
DELAYED
PARTIALLY_HARVESTED
HARVESTED
ABANDONED
FAILED_WITH_SCOPE
CLOSED
UNKNOWN

`CYCLE_ACTIVE != HARVEST_GUARANTEED`

`DELAYED != FAILED`

`YIELD_ESTIMATE != HARVESTED_AMOUNT`

The system does not calculate growth time or output quantity. Those values must come from authored facts, approved mechanics or explicit observations.

## Work participation by Pokémon

```yaml
pokemon_work_participation:
  participation_id: null
  pokemon_ref: null
  site_ref: null
  cycle_ref: null
  authored_role_ref: null
  relationship_or_custody_ref: null
  capability_evidence_refs: []
  start_time: null
  end_time: null
  participation_status: null
  provenance_refs: []
```

Work participation must be individual and explicit.

`POKEMON_PRESENT != WORKING`

`POKEMON_WORKING != OWNED_BY_SITE`

`ONE_GROUND_TYPE_PLOWS != ALL_GROUND_TYPES_CAN_PLOW`

`SPECIES_ASSOCIATED_WITH_FARMING != UNIVERSAL_DOMESTICATION`

If an exact Move, Ability, Feature or Skill matters mechanically, it requires individual PTU/Caelo and engine verification.

## Harvest episode

```yaml
harvest_episode:
  harvest_id: null
  cycle_ref: null
  start_time: null
  completion_time: null
  harvested_batch_refs: []
  observed_quantity_claim_refs: []
  quality_claim_refs: []
  incomplete_area_refs: []
  participant_refs: []
  interruption_refs: []
  resulting_status: null
  provenance_refs: []
```

Material Culture owns the identity of any actual batch. This record owns the event that produced or gathered it.

`HARVEST_RECORDED != ALL_OUTPUT_RECOVERED`

`HARVESTED != SAFE_OR_USABLE`

`HARVESTED != SOLD`

## Post-harvest handling episode

```yaml
post_harvest_episode:
  episode_id: null
  source_harvest_refs: []
  material_batch_refs: []
  stage_type: null
  location_ref: null
  handler_refs: []
  start_time: null
  end_time: null
  storage_or_processing_asset_refs: []
  condition_observation_refs: []
  loss_event_refs: []
  resulting_batch_refs: []
  provenance_refs: []
```

Candidate stage types are descriptive: SORTING, CLEANING, PACKING, PROCESSING, ON_SITE_STORAGE, TRANSFER_TO_STORAGE, STORAGE_RELEASE and OTHER_AUTHORED_STAGE.

The layer records transitions; it does not invent technical food-safety standards or shelf-life calculations.

## Production loss event

```yaml
production_loss_event:
  loss_id: null
  affected_cycle_or_batch_refs: []
  stage_ref: null
  discovered_at: null
  observed_scope_refs: []
  suspected_cause_refs: []
  confirmed_cause_refs: []
  affected_availability_refs: []
  status: OBSERVED
  provenance_refs: []
```

Candidate states:

REPORTED
OBSERVED
SCOPE_ESTIMATED
SCOPE_CONFIRMED
CAUSE_UNDER_INVESTIGATION
CAUSE_PARTLY_RESOLVED
CLOSED

`LOSS_OBSERVED != CAUSE_KNOWN`

`POST_HARVEST_LOSS != CROP_FAILURE`

`ONE_BATCH_LOST != SITE_PRODUCTION_FAILED`

`SITE_PRODUCTION_FAILED != REGIONAL_SHORTAGE`

## Supply availability record

```yaml
food_supply_availability:
  availability_id: null
  product_or_category_ref: null
  location_or_market_ref: null
  observation_time: null
  availability_scope: null
  source_batch_or_supply_refs: []
  reservation_or_restriction_refs: []
  substitution_refs: []
  observation_or_claim_refs: []
  provenance_refs: []
```

Candidate scopes can include NONE_OBSERVED, LIMITED, ORDINARY, SURPLUS_REPORTED and UNKNOWN. They are observations or authored states, not a universal economic index.

`STORED != AVAILABLE_TO_PUBLIC`

`AVAILABLE_REGIONALLY != AVAILABLE_LOCALLY`

`MARKET_EMPTY != REGION_OUT_OF_SUPPLY`

`SHORTAGE != FAMINE`

## Production dependency

```yaml
production_dependency:
  dependency_id: null
  production_site_or_cycle_ref: null
  dependency_type: null
  source_ref: null
  authored_scope_ref: null
  alternate_source_refs: []
  active_from: null
  active_until: null
  evidence_refs: []
  canon_status: proposed
```

Examples may reference irrigation service, seasonal labor, a storage asset, a particular input, a transport route, an individual Pokémon work relationship or an ecological interaction when those facts have already been established by the owning system.

Proximity never creates a dependency.

`NEAR_WATER != IRRIGATION_DEPENDENCY_PROVEN`

`POKEMON_VISITS_ORCHARD != POLLINATION_DEPENDENCY_PROVEN`

## Temporary substitution

```yaml
temporary_food_substitution:
  substitution_id: null
  affected_location_ref: null
  unavailable_or_limited_product_refs: []
  substitute_product_refs: []
  start_time: null
  expected_end_time: null
  actual_end_time: null
  adoption_context_refs: []
  market_or_cultural_effect_refs: []
  provenance_refs: []
```

A temporary substitute can later become culturally important, but the historical transition must be recorded.

`TEMPORARY_SUBSTITUTE != PERMANENT_TRADITION`

`ONE_SEASON_OF_USE != ANCIENT_PRACTICE`

## Recovery episode

```yaml
production_recovery_episode:
  recovery_id: null
  affected_site_or_supply_refs: []
  recovery_start: null
  intervention_refs: []
  restored_capacity_claim_refs: []
  first_new_harvest_refs: []
  distribution_normalization_refs: []
  remaining_limitation_refs: []
  status: IN_PROGRESS
  provenance_refs: []
```

Recovery can be partial.

`PRODUCTION_RESUMED != ORDINARY_OUTPUT_RESTORED`

`ORDINARY_OUTPUT_RESTORED != INVENTORY_REPLENISHED`

`INVENTORY_REPLENISHED != PRICE_NORMALIZED`

## Player-facing presentation

Player-facing panels may show only discovered or public facts such as active fields, expected harvest windows when published, observed shortages, announced substitutions, visible damage, known closures, market availability and recovery notices.

Do not expose hidden yield rolls, secret contamination, undiscovered dependencies, culprit flags or canonical causal conclusions.

## Chronicle events

Candidate events include:

`PRODUCTION_CYCLE_STARTED`

`PRODUCTION_CAPACITY_CHANGED`

`POKEMON_WORK_PARTICIPATION_STARTED`

`HARVEST_STARTED`

`HARVEST_RECORDED`

`POST_HARVEST_STAGE_RECORDED`

`PRODUCTION_LOSS_REPORTED`

`PRODUCTION_LOSS_CONFIRMED`

`SUPPLY_LIMITATION_OBSERVED`

`TEMPORARY_SUBSTITUTION_STARTED`

`PRODUCTION_RECOVERY_STARTED`

`PRODUCTION_RESUMED`

Each event retains provenance and time. Corrections append rather than overwrite.

## Narrative invariants

`YIELD_ESTIMATE != HARVESTED_AMOUNT`

`HARVESTED != DISTRIBUTED`

`STORED != AVAILABLE_TO_PUBLIC`

`CROP_FAILURE != SHORTAGE`

`SHORTAGE != FAMINE`

`WEATHER_EVENT != CROP_FAILURE`

`POKEMON_PRESENT_ON_FARM != FARM_OWNED`

`POKEMON_WORK_ROLE != UNIVERSAL_SPECIES_CAPABILITY`

`PROCESSING_COMPLETE != DISTRIBUTION_COMPLETE`

`ONE_BAD_SEASON != PERMANENT_ECOLOGICAL_CHANGE`

`PRODUCTION_RESTORED != PRICE_NORMALIZED`

`BATTLE_WON != HARVEST_SAVED`

`MINECRAFT_CROP_GROWTH != OUROS_PRODUCTION_EVENT`

## Battle boundary

Crops, produce, workers, carts, gates, irrigation controls and semantic livestock/work Pokémon remain outside BattleSpec unless an exact verified AutoPTU contract models the relevant entity and role.

Ouros decides the pre-battle production state and explicit combatant roster.

AutoPTU may return bounded tactical facts such as `IMMEDIATE_ORCHARD_APPROACH_CLEAR`, `IMMEDIATE_IRRIGATION_GATE_ACCESS_CLEAR`, `IMMEDIATE_HARVEST_STAGING_APPROACH_CLEAR` or `IMMEDIATE_RANCH_PERIMETER_CLEAR`.

Those outcomes do not determine harvest quantity, food safety, distribution, ownership, ecological cause or recovery.

Minecraft/Cobblemon/Craftics may show fields, orchards, paddocks, weathered crops, crates, storehouses, workers and seasonal visual change after Ouros has established those facts. Minecraft crop ticks, redstone, entity breeding, pathfinding or Cobblemon BattleState cannot decide Ouros production, Pokémon ownership, harvest outcome, shortage or tactical authority.

## Canon-status rule

All schemas and examples here remain PROPOSED until canon review adopts specific sites, products, practices, institutions, work relationships or histories.

Research citations remain in the paired research scan. Canon files should reference approved facts rather than external research prose.