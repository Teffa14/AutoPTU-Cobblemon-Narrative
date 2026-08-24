# Wild nesting, parental care & juvenile dispersal layer

Status: PROPOSED SYSTEMS DESIGN. NON-CANON until reviewed.

## Purpose

Ouros needs an authority for wild reproductive ecology that is separate from Trainer-directed breeding, institutional nurseries and mechanical Egg resolution.

This layer records persistent reproductive sites, seasonal nesting episodes, eggs/young observations, parental-care behavior, colony structure, dependency assessments, post-nest association and natal dispersal. It preserves uncertainty and does not invent PTU breeding mechanics.

## Authority boundary

Breeding/Egg/Nursery remains authoritative once an Egg enters legitimate human/institutional custody or an authoritative PTU breeding/hatching transaction is required.

Wild Collective Agency remains authoritative for persistent groups and population-level agency.

Pokémon Agency remains authoritative for persistent individual identity, custody, partnership and release.

Seasonality owns recurring calendar/phenology windows. Migration owns regional movement episodes/corridors. Conservation owns stewardship/protection decisions. Research Ethics owns intrusive monitoring and subject/site protection. Photography owns camera records. Minecraft/Cobblemon only projects current visible state.

This layer owns the reproductive-ecology history between those systems.

## Core separation

```text
species-grounded / observed context
    -> reproductive site identity
    -> nesting or breeding episode
    -> egg / young observation
    -> caregiver-behavior observation
    -> dependency assessment
    -> nest departure / emergence
    -> post-natal association
    -> natal dispersal
    -> later settlement / recruitment evidence
```

No arrow is automatic.

## Primary objects

### WILD_REPRODUCTIVE_SITE

```yaml
wild_reproductive_site_id: null
location_geometry_ref: null
site_type: NEST | DEN | BURROW | COLONY | ROOST_NURSERY | SHORE_SITE | CAVE_SITE | UNKNOWN
first_observed_at: null
last_observed_at: null
known_species_claims: []
site_revision_ids: []
episode_ids: []
access_state_ref: null
protection_state_ref: null
confidence: null
```

The site persists across seasons. `inactive_this_year` does not delete it.

### REPRODUCTIVE_SITE_REVISION

Tracks physical change without changing site identity.

```yaml
revision_id: null
site_id: null
valid_from: null
geometry_ref: null
substrate_or_structure_refs: []
condition_observations: []
change_event_refs: []
source_refs: []
```

A storm, fallen tree, new building, river shift or Pokémon construction may revise the physical site.

### NESTING_EPISODE

```yaml
nesting_episode_id: null
site_id: null
season_ref: null
start_state: UNKNOWN
observation_ids: []
egg_observation_ids: []
young_observation_ids: []
care_observation_ids: []
disturbance_ids: []
monitoring_effort_ids: []
status: POSSIBLE | ACTIVE_OBSERVED | ENDED_OBSERVED | INACTIVE_OBSERVED | UNKNOWN
confidence: null
```

Do not fabricate courtship, mating, conception or parentage when they were not observed or mechanically established.

### EGG_OR_YOUNG_OBSERVATION

```yaml
observation_id: null
episode_id: null
observed_at: null
observer_or_device_id: null
observation_type: EGG | HATCHED_YOUNG | JUVENILE | UNKNOWN_YOUNG_STAGE
count_type: EXACT | MINIMUM | ESTIMATE | UNKNOWN
count_value: null
persistent_entity_ids: []
position_ref: null
method: DIRECT | CAMERA | ACOUSTIC | TRACK | OTHER
confidence: null
disturbance_context_ref: null
```

An Egg observation is not an inventory object. It becomes an `egg_id` under the Breeding/Egg layer only after an authored custody handoff that is legally/narratively valid and mechanically safe.

### PARENTAL_CARE_OBSERVATION

```yaml
care_observation_id: null
episode_id: null
actor_pokemon_entity_id: null
target_young_refs: []
behavior: PROVISION | SHELTER | GUARD | TRANSPORT | GROOM | WARM | GUIDE | FEED | OTHER
observed_at: null
source_ref: null
confidence: null
```

The name describes an observed behavior category, not confirmed parentage.

A Pokémon feeding or guarding young can be recorded without adding `PARENT_OF`.

### DEPENDENCY_ASSESSMENT

```yaml
assessment_id: null
juvenile_ref: null
as_of: null
state: DEPENDENT_OBSERVED | PARTIALLY_INDEPENDENT | INDEPENDENT_OBSERVED | UNKNOWN
basis_observation_ids: []
author_id: null
confidence: null
```

This is ecological/narrative state, not PTU Level, age, Loyalty or Evolution state.

### NEST_DEPARTURE_OR_EMERGENCE_EVENT

```yaml
event_id: null
juvenile_ref: null
site_id: null
observed_at: null
event_type: LEFT_NEST | EMERGED_FROM_DEN | FIRST_FLIGHT_OBSERVED | FIRST_SOLO_FORAGING_OBSERVED | OTHER
source_refs: []
```

A nest departure does not mean independent.

### NATAL_DISPERSAL_CASE

```yaml
natal_dispersal_case_id: null
subject_ref: null
natal_site_id: null
post_natal_use_area_refs: []
dispersal_start_claim: null
movement_observation_ids: []
temporary_range_refs: []
settlement_claim_ref: null
status: NOT_STARTED | POSSIBLE | ACTIVE | SETTLED_POSSIBLE | UNKNOWN
confidence: null
```

This can link to Migration if the movement becomes a population/seasonal movement pattern, but ordinary natal dispersal is not automatically migration.

### BREEDING_COLONY_PROFILE

For colonial species or persistent multi-nest sites.

```yaml
colony_profile_id: null
collective_id: null
site_ids: []
seasonal_episode_ids: []
monitoring_method_history: []
known_disturbance_history: []
occupancy_assessments: []
```

Do not derive `Pack Mon`, shared initiative or combat coordination from colony membership.

## Parentage and kinship guardrail

Possible evidence of care is not enough to establish genetic parentage.

Never infer `PARENT_OF` from:
- proximity;
- feeding;
- guarding;
- two adults sharing a nest;
- species stereotype;
- a juvenile following an adult;
- a camera sequence without sufficient identity evidence.

If PTU/Caelo breeding resolution or authored canon establishes parentage, the lineage layer may record it. Otherwise use `caregiver_observation` or `association_claim` with confidence.

## Abandonment guardrail

Adult absence during one visit does not mean abandonment.

Possible reasons include:
- foraging;
- shift in caregiver attendance;
- observer timing;
- concealment;
- disturbance avoidance;
- incomplete detection;
- mortality or permanent departure, if separately evidenced.

`ABANDONED` should require an authored assessment with time, monitoring effort and species/context evidence.

## Juvenile progression

Keep these separate:

```text
egg/young first observed
nest departure
post-nest dependence
independent foraging or movement
natal dispersal
temporary range
later settlement/recruitment
mechanical Evolution/Level progression
```

The last line remains entirely under PTU/AutoPTU authority.

## Monitoring and observer effects

Every serious nesting assessment should retain monitoring effort:

```yaml
monitoring_effort:
  method: DIRECT | REMOTE_CAMERA | ACOUSTIC | DISTANT_SCOPE | TRACK_SURVEY
  start_at: null
  end_at: null
  coverage: null
  visit_count: null
  known_blind_spots: []
  disturbance_risk: null
```

A blank camera interval can mean device failure. No tracks can mean poor substrate. A missing adult can mean detection failure. A single successful observation can prove presence but not long-term occupancy.

Research Ethics should be consulted for close handling, tagging, baiting, repeated entry, nest cameras or Egg/juvenile sampling.

## Disturbance and access

Potential disturbances may be recorded from existing world state:
- trail or road traffic;
- tourism pressure;
- construction;
- logging;
- water-level change;
- wildfire;
- storm damage;
- light/noise change;
- introduced species;
- predators/competitors;
- researcher visits.

A temporal association is not automatically causation.

Access closures belong to Conservation/Land Tenure/Governance authority. This layer records the nesting evidence that may motivate them.

## Wild Egg emergency handoff

A storm, fire, collapse or other crisis may create a legitimate rescue situation.

The handoff must be explicit:

```text
wild reproductive observation
 -> crisis/welfare assessment
 -> intervention authority + ethics check
 -> custody event
 -> Breeding/Egg/Nursery `egg_id`
 -> care / authoritative hatching mechanics
 -> release/placement decision later
```

Rescue never grants capture rights or ownership by default.

## Minecraft/Cobblemon projection

Minecraft is a renderer, not reproductive truth.

Rules:
- loaded baby entities never define brood size;
- a despawn never means mortality;
- an unloaded adult never means abandonment;
- breaking/replacing a decorative nest block cannot erase the reproductive-site record;
- chunk reload cannot reset an episode;
- visual Eggs cannot be collectible unless an authoritative handoff exposes an interaction;
- player-placed nests do not create breeding state or rare spawns.

Large broods/colonies may use aggregate world-state cohorts and only project a limited visible subset.

## Cross-layer handoffs

Breeding/Egg/Nursery: custody and authoritative hatching.
Pokémon Agency: persistent individual identity, wild/captured/released state.
Wild Collectives: group identity and population-scale behavior.
Seasonality: expected nesting windows.
Migration: seasonal arrival/departure around breeding grounds when supported.
Conservation: protection, closures, habitat management.
Research Ethics: intrusive monitoring and handling.
Photography: nest-camera/image provenance.
Field Signs: tracks, feathers, nesting material and spoor.
Canopy/Caves/Intertidal/Urban Wildlife/etc.: physical habitat context.
Road Ecology/Travel/Tourism: disturbance and access.
Care: injured or compromised wild young.

## Battle boundary

A reproductive site is not automatically a battle objective or hazard.

Do not infer:
- guardian bonuses;
- Rage or Loyalty mechanics;
- Accuracy/Defense buffs near young;
- custom Reaction interrupts;
- nest cover;
- Egg HP;
- juvenile capture modifiers;
- swarm AI;
- protected-zone movement rules;
- automatic hostility.

If confrontation occurs, narrative state determines why actors are present. AutoPTU determines legal combat.

## Implementation blockers for rich encounters

FULL nest/juvenile encounters commonly require:
- complete movement including interception/forced movement when actors must cross, withdraw or protect routes;
- terrain/weather/hazards/zones/reactions if the physical site changes tactical legality;
- AI tactical policy for `WITHDRAW`, `PROTECT_NEST`, `CROSS`, `REACH_GROUP`, `CLEAR_ROUTE` or de-escalation goals;
- Minecraft/Cobblemon/Craftics adapter/playback for civilians, young, site exclusions and semantic objectives.

REDUCED encounters should resolve young/civilians/ecological movement in world state first, exclude nests/Eggs from the tactical grid, then open a conventional static battle only for actual combatants if conflict remains.

## Canon decisions still required

Ouros has not yet established:
- which species/populations have authored reproductive behavior;
- region-specific breeding seasons;
- how much wild Egg/juvenile state is simulated offline;
- which institutions may close or monitor nesting sites;
- thresholds for declaring abandonment;
- how persistent young are identified before individualization;
- Caelo-specific changes to breeding/hatching rules;
- whether any PTU Feature or Capability modifies wild reproductive monitoring.

Until reviewed, all examples and schemas here remain proposed architecture rather than canon.
