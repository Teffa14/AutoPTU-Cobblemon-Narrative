# Ranch, Managed Pokémon Group & Pasture Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

Research basis: `research/2026-08-27-ranch-managed-groups-pasture-scan-85.md`

## Purpose

Ouros already models agricultural sites, food batches, Pokémon work assignments, Eggs and nurseries, conservation, seasonality, travel, care and persistent Pokémon identity. This extension connects those systems around one rural site that maintains a managed group of Pokémon across time.

The objective is continuity: who is expected to be present, which zones the group uses, when the group moves, which individuals require special attention, how wild ecology overlaps the site, and what history persists after each visit.

This layer does not create livestock ownership law, breeding rules, productivity math, rancher Trainer mechanics, hunger simulation or battle authority.

## Scope boundary

This extension owns:

- rural managed-site identity;
- persistent managed-group identity;
- membership observations and reconciliation;
- paddock/pasture/use-zone state;
- planned and observed group movement between zones;
- broad managed-group availability/location state;
- individual exception references;
- temporary refuge/relocation episodes;
- wild-overlap observations;
- history of group/site use;
- explicit handoffs to Care, Food, Material Culture, Workplaces, Pokémon Work, Conservation, Travel and Crisis.

It does not own:

- Pokémon ownership or custody law;
- breeding eligibility, parentage, Eggs or inheritance;
- individual medical state;
- individual work assignments;
- food/item mechanics, production yields or prices;
- route ownership or access authority;
- conservation designation authority;
- Skills, Moves, Abilities, Trainer Features or Loyalty;
- tactical battle participants, state or results.

## Core separation

Keep these facts distinct:

```text
rural site identity
        ↓
managed group identity
        ↓
expected membership / current observations
        ↓
zone-use and movement plan
        ↓
observed movement / exception events
        ↓
other systems produce care, work, production or policy outcomes
        ↓
managed-group history
```

A Pokémon can be observed with a managed group without proving ownership, breeding relation or permanent membership.

A Pokémon can belong to the managed group without being assigned to work.

A working Pokémon can supervise or guide the group without becoming its leader as a biological or social fact.

## 1. Rural managed site

```yaml
rural_managed_site:
  site_id: null
  location_ids: []
  site_label: null
  operator_actor_ids: []
  institution_ids: []
  managed_group_ids: []
  managed_zone_ids: []
  route_connection_ids: []
  service_refs: []
  storage_or_shelter_refs: []
  nursery_refs: []
  care_referral_refs: []
  stewardship_overlap_refs: []
  current_operating_state: NORMAL
  active_problem_refs: []
  history_refs: []
  canon_status: proposed
```

Candidate operating states:

- NORMAL
- LIMITED
- PARTIAL_ZONE_USE
- MOVEMENT_WINDOW
- TEMPORARY_REFUGE
- RELOCATED
- RECOVERING
- CLOSED_TO_VISITORS
- SUSPENDED

These labels describe operational world state. They do not imply legal authority or PTU effects.

## 2. Managed Pokémon group

A managed group is a persistent world-state entity that can contain exact individuals and aggregate background membership.

```yaml
managed_pokemon_group:
  group_id: null
  site_id: null
  public_label: null
  species_claim_refs: []
  exact_member_ids: []
  aggregate_member_estimate: null
  current_zone_ref: null
  current_location_confidence: null
  expected_presence_window_ref: null
  group_management_context_ref: null
  individual_exception_refs: []
  production_dependency_refs: []
  current_status: PRESENT
  history_refs: []
```

Candidate status values:

- PRESENT
- PARTIALLY_OBSERVED
- MOVING
- SPLIT_BETWEEN_ZONES
- TEMPORARILY_OFF_SITE
- SHELTERED
- COUNT_UNRESOLVED
- RETURNING
- RELOCATED

`aggregate_member_estimate` is deliberately not a hidden exact truth. Large background groups do not need every member materialized or individually named.

## 3. Membership observations

Membership is evidence-based.

```yaml
group_membership_observation:
  observation_id: null
  group_id: null
  pokemon_id: null
  observed_at: null
  observed_zone_id: null
  observer_ids: []
  observation_type: null
  claimed_membership_state: null
  confidence: null
  source_refs: []
```

Possible observation types:

- VISUAL_COUNT
- IDENTIFIED_INDIVIDUAL
- CHECK_IN
- CHECK_OUT
- MOVEMENT_HANDOFF
- RETURN_OBSERVED
- TEMPORARY_GUEST
- UNKNOWN_INDIVIDUAL_WITH_GROUP

A single co-location observation must not establish permanent membership.

## 4. Count reconciliation

The system needs to tolerate uncertainty without spawning missing Pokémon to satisfy paperwork.

```yaml
managed_group_count_reconciliation:
  reconciliation_id: null
  group_id: null
  expected_count_claim: null
  direct_observed_count: null
  exact_identified_ids: []
  known_off_site_ids: []
  temporary_guest_ids: []
  duplicate_or_stale_record_refs: []
  unresolved_count: null
  status: OPEN
  reviewed_at: null
  provenance_refs: []
```

Suggested statuses:

- OPEN
- CONSISTENT
- PARTIALLY_RECONCILED
- DISCREPANCY_REMAINS
- SUPERSEDED

An unresolved count does not prove theft, escape, death, capture or clerical misconduct.

## 5. Managed zones

```yaml
managed_zone:
  zone_id: null
  site_id: null
  location_refs: []
  zone_type: null
  current_use_state: ACTIVE
  expected_group_ids: []
  access_state_ref: null
  shelter_refs: []
  water_or_feed_dependency_refs: []
  maintenance_refs: []
  ecology_overlap_refs: []
  seasonal_condition_refs: []
  public_access_state: null
  history_refs: []
```

Possible zone types:

- PADDOCK
- PASTURE
- SHELTER
- HANDLING_OR_STAGING_AREA
- WATERING_AREA
- MOVEMENT_CORRIDOR
- TEMPORARY_REFUGE_AREA
- RESTING_OR_RECOVERY_PASTURE
- PUBLIC_EDGE
- WILD_OVERLAP_EDGE

A zone can change use without changing identity.

## 6. Pasture use windows

Pasture rotation is authored from explicit land, calendar and ecology state.

```yaml
pasture_use_window:
  window_id: null
  zone_id: null
  group_ids: []
  planned_start: null
  planned_end: null
  season_phase_ref: null
  access_dependency_refs: []
  maintenance_dependency_refs: []
  ecological_observation_refs: []
  reason_refs: []
  status: PLANNED
```

This is not a simulation of optimal grazing, carrying capacity or nutrition.

A pasture may rest because of authored ecological recovery, maintenance, water access, nesting overlap, public works or another documented reason.

## 7. Group movement plan

```yaml
group_movement_plan:
  plan_id: null
  group_id: null
  from_zone_id: null
  to_zone_id: null
  route_ref: null
  planned_window: null
  supervisor_actor_ids: []
  working_pokemon_assignment_refs: []
  access_dependency_refs: []
  weather_or_calendar_refs: []
  wildlife_overlap_refs: []
  fallback_zone_ids: []
  status: PLANNED
```

The plan references Travel/route state where appropriate.

A movement plan does not give any Pokémon a traversal capability. Individual working partners use `pokemon-work-role-participation-extension.md` and authoritative mechanics when needed.

## 8. Group movement event

```yaml
group_movement_event:
  event_id: null
  plan_id: null
  group_id: null
  started_at: null
  completed_at: null
  observed_route_ref: null
  exact_member_ids_observed: []
  aggregate_count_observed: null
  deviation_refs: []
  interruption_refs: []
  final_zone_id: null
  result: COMPLETE
  provenance_refs: []
```

Possible results:

- COMPLETE
- PARTIAL
- PAUSED
- RETURNED_TO_ORIGIN
- REROUTED
- SPLIT
- COUNT_UNRESOLVED

No result itself causes a tactical battle.

## 9. Boundary and escape events

A Pokémon outside the expected zone creates an observation first.

```yaml
managed_boundary_event:
  event_id: null
  group_id: null
  pokemon_ids: []
  expected_zone_id: null
  observed_location_id: null
  observed_at: null
  boundary_condition_refs: []
  working_assignment_refs: []
  immediate_response_refs: []
  cause_claim_ids: []
  resolution_refs: []
```

Possible causes may include an open gate, damaged fence, changed route, interrupted supervision, wildlife pressure or unknown cause. These remain claims until evidence supports them.

Do not automatically classify the Pokémon as escaped, disobedient, hostile or lost.

## 10. Individual exception record

Important individuals can be singled out without turning the group into a stat spreadsheet.

```yaml
managed_group_individual_exception:
  exception_id: null
  group_id: null
  pokemon_id: null
  exception_type: null
  care_case_ref: null
  work_assignment_ref: null
  temporary_location_ref: null
  production_dependency_ref: null
  restriction_refs: []
  started_at: null
  ended_at: null
  status: ACTIVE
```

Examples:

- under Care review;
- temporarily separated from the group;
- assigned to a service route;
- new arrival under observation;
- equipment compatibility review;
- temporarily housed elsewhere.

The exact medical or work decision belongs to the owner system.

## 11. Production handoff

The ranch layer can explain where a product/service originates, but it does not calculate output.

```yaml
rural_production_dependency_handoff:
  handoff_id: null
  site_id: null
  group_id: null
  product_or_service_ref: null
  source_condition_refs: []
  individual_exception_refs: []
  operating_effect_claim: null
  destination_system: FOOD | MATERIAL_CULTURE | STOREFRONT | TRAVEL | OTHER
  authoritative_output_ref: null
```

Examples:

- an individual Care case causes a service to become LIMITED;
- a route closure delays a physical batch;
- a temporary relocation changes source provenance;
- a resting pasture changes where a batch was produced.

Never invent yield or item power here.

## 12. Wild overlap

Managed and wild Pokémon can share the same broad landscape.

```yaml
ranch_wild_overlap_observation:
  observation_id: null
  site_id: null
  zone_id: null
  wild_subject_refs: []
  managed_group_refs: []
  observed_at: null
  behavior_observed: null
  evidence_refs: []
  conflict_claim_ids: []
  conservation_or_science_handoff_refs: []
```

Co-presence does not prove conflict, predation, competition, habituation, domestication or ownership.

If the overlap becomes a persistent ecological issue, Conservation or Science owns the interpretation and management response.

## 13. Temporary refuge and relocation

```yaml
managed_group_temporary_refuge:
  refuge_event_id: null
  group_id: null
  origin_zone_id: null
  refuge_location_id: null
  reason_refs: []
  crisis_or_weather_refs: []
  host_actor_or_institution_ids: []
  movement_event_refs: []
  expected_return_window: null
  returned_at: null
  status: ACTIVE
```

Temporary shelter elsewhere does not transfer ownership or permanent membership.

## 14. Pokémon work boundary

Exact work belongs to `pokemon-work-role-participation-extension.md`.

Examples:

- guiding a managed group through a gate;
- carrying supplies between paddocks;
- checking a known route;
- performing a validated signaling routine;
- providing a reviewed traversal or service capability.

The ranch layer stores only references to those assignments.

Species and Type never establish task eligibility.

## 15. Breeding and nursery boundary

A ranch may coexist with a nursery or breeding service, but group co-location does not prove breeding.

The ranch layer may record:

- an adult group uses a zone;
- an Egg or juvenile is temporarily present under an existing nursery/custody record;
- a nursery service shares the site.

It may not decide:

- reproductive eligibility;
- parentage;
- offspring species;
- Egg creation;
- inheritance;
- hatch timing;
- ownership after hatching.

## 16. Care and welfare boundary

Observable conditions may create a Care referral.

Examples:

- one individual stops joining the normal route;
- reduced activity is observed repeatedly;
- an individual remains separated;
- a worker reports a physical symptom;
- a scheduled service becomes limited while a Care case is open.

The ranch layer does not diagnose or create PTU statuses.

## 17. Seasonality and phenology

Seasonal movement references the shared calendar.

Potential authored consequences:

- a zone is normally unused during a nesting window;
- a high pasture opens after a route becomes accessible;
- a water-dependent paddock closes during maintenance;
- a group stays near shelter during an observed weather event;
- a public path temporarily shares a movement corridor.

None of these automatically create tactical Weather or Terrain.

## 18. Compression policy

Routine rural work should compress.

Do not generate a quest for:

- opening and closing normal gates;
- moving a group through a routine safe route;
- ordinary feeding/watering when no meaningful choice exists;
- normal product collection;
- a count that reconciles immediately;
- routine sheltering during expected conditions;
- ordinary staff handoffs.

Create playable content when state intersects:

- unexplained count discrepancy;
- individual welfare;
- damaged or changed route;
- seasonal habitat overlap;
- service/production interruption;
- changed working-Pokémon suitability;
- infrastructure failure;
- crisis refuge;
- public-route conflict;
- a player-authored rural profession/project.

## 19. Minecraft/Cobblemon materialization

Maximize reuse of Cobblemon and Minecraft for presentation.

Useful targets include:

- Pokémon entities/models/forms/textures;
- idle/walk/swim/fly/look/cry presentation where available;
- entity tracking and client/server sync;
- fences, gates, barns, paths, water, vegetation and storage blocks;
- scheduled presentation of groups in different zones;
- sounds/particles for work and movement;
- UI for zone state, observed counts and service availability;
- persistence hooks for mapping Ouros persistent IDs to current overworld embodiments.

Binding rule:

`Ouros rural/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Cobblemon BattleState, participant selection, entity proximity, despawn and animation state never decide tactical participants or managed-group truth.

## 20. Encounter contract — Paddock Withdrawal

Narrative premise:
A managed group is being moved away from a disturbed paddock while a separate wild encounter blocks the safe exit area.

FULL version:

- managed Pokémon withdraw through a protected corridor;
- selected PCs/opponents can use Intercept where legal;
- forced movement/collision matters near fences and gates;
- AI can prefer withdrawal, protection or territorial behavior rather than KO;
- reviewed environment state may matter if authoritative Terrain/Weather support exists;
- playback keeps the moving group distinct from tactical participants.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED version:

- Ouros stops the group before the tactical area;
- all managed Pokémon not explicitly selected as combatants remain outside the battle grid;
- workers/noncombatants withdraw through world state;
- a reviewed static battle clears the gate/route segment;
- afterward the ranch layer resumes or reroutes the movement plan;
- no stampede, escort HP, scripted knockback or protected-target mechanic is invented.

## 21. Encounter contract — Grazing Route Wildlife Conflict

Narrative premise:
A planned movement corridor now overlaps a repeatedly observed wild-use area.

FULL version:

- the managed group remains a moving noncombat objective;
- wild opponents may prefer territorial withdrawal/denial behavior;
- CLEAR_ROUTE/WITHDRAW intents matter;
- Intercept and forced displacement can matter at chokepoints;
- terrain/weather only applies through reviewed AutoPTU state;
- Conservation and Travel receive the result but retain route-policy authority.

Dependencies are the same mixed VERIFIED/PARTIAL/BLOCKING profile as Paddock Withdrawal, with AI tactical policy and adapter/playback particularly important.

REDUCED version:

- the managed group stops outside the tactical area;
- Ouros selects explicit combatants only;
- AutoPTU resolves a static legal encounter;
- afterward Conservation/Travel/Ranch state chooses continue, delay, reroute or suspend;
- battle victory does not establish permanent route rights or erase wild habitat use.

## 22. Noncombat scenario — Morning Count Reconciliation

A morning record expects one number, the direct observation produces another, and several known individuals are already documented off-site for care, work or temporary housing.

Play can involve:

- inspecting yesterday's handoff;
- checking exact known individuals;
- reviewing movement events;
- discovering a stale duplicate record;
- observing an unregistered temporary guest;
- finding that the discrepancy remains unresolved.

This scenario can execute entirely in narrative/world state today.

## 23. Engine readiness policy

This extension uses the permanent capability categories defined by `design/encounter-implementation-contracts.md`.

Do not promote a category because one representative mechanic exists.

The live Pass 85 snapshot is recorded separately in `design/engine-readiness-snapshot-pass-85.md`.

## 24. Canon questions

- Which Ouros cultures use managed Pokémon groups in rural production or services?
- What terms do they use for ranch, paddock, pasture, herd/flock/group or stewardship?
- Which relationships are ownership, custody, partnership, communal stewardship or something else?
- Which products/services exist and which are mechanically relevant PTU items?
- Are seasonal grazing routes common anywhere?
- How do managed routes coexist with wild corridors and protected areas?
- Which institutions inspect or support welfare?
- How are temporary refuge and disaster relocation handled?
- Which exact working-Pokémon roles are culturally normal?
- How many background group members should Cobblemon materialize at one time?

No answer is promoted to canon by this extension.
