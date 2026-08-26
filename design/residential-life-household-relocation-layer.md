# Ouros Residential Life, Household & Relocation Layer

Status: Proposed systems design. Not established canon.

## Purpose

Ouros already models settlements, services, social bonds, care, hospitality, economy, public works, travel, communication and public memory. This layer gives residential places enough persistent state to support daily life, relocation, renovation, household change and neighborhood continuity without turning the project into a property simulator.

The goal is to make homes matter because people and Pokémon actually live around them, not because ownership grants passive bonuses.

## 1. Residence record

```yaml
residence:
  residence_id: null
  location_id: null
  settlement_id: null
  residence_type: null
  current_condition: stable
  occupant_ids: []
  household_id: null
  access_records: []
  room_or_zone_refs: []
  service_dependency_ids: []
  environmental_context_ids: []
  maintenance_state_ids: []
  accommodation_ids: []
  history_event_ids: []
  public_visibility: private_location
  canon_refs: []
```

Candidate residence types may include a private dwelling, apartment, room, shared house, staff lodging, institutional quarters, dormitory or another authored type. No type implies a legal ownership model.

## 2. Household record

```yaml
household:
  household_id: null
  residence_id: null
  resident_actor_ids: []
  resident_pokemon_entity_ids: []
  temporary_guest_ids: []
  shared_resource_refs: []
  shared_routine_refs: []
  known_constraints: []
  move_history_ids: []
  active_household_projects: []
  privacy_state: private
```

A household is an occupancy grouping. It does not establish family, romance, friendship, ownership or legal dependency.

## 3. Occupancy and ownership stay separate

```yaml
residential_interest:
  residence_id: null
  actor_id: null
  interest_type: occupant
  authority_source_id: null
  effective_from: null
  effective_until: null
  confidence: confirmed
```

Possible authored interest types might include occupant, guest, caretaker, operator or owner where canon explicitly establishes the concept.

The generator must never infer ownership because someone sleeps there, pays for repairs, stores belongings there or has lived there for a long time.

## 4. Residential suitability

Suitability is a set of explicit constraints rather than one score.

```yaml
residential_suitability:
  residence_id: null
  household_id: null
  constraint_checks:
    access: unknown
    space: unknown
    noise: unknown
    weather_exposure: unknown
    nearby_services: unknown
    transport_access: unknown
    care_access: unknown
    work_or_study_access: unknown
    pokemon_accommodation: unknown
    habitat_conflict: unknown
  evidence_refs: []
  unresolved_questions: []
  reviewed_at: null
```

The system should preserve why a location works or fails.

## 5. Pokémon accommodation

```yaml
pokemon_accommodation:
  accommodation_id: null
  residence_id: null
  pokemon_entity_id: null
  observed_need_refs: []
  species_information_refs: []
  authoritative_capability_refs: []
  physical_adjustments: []
  routine_adjustments: []
  conflict_refs: []
  status: proposed
```

Rules:
- species identity alone should not generate a custom mechanical requirement;
- observed behavior may justify narrative preferences;
- authoritative movement or capability data may constrain physical access when actually relevant;
- accommodation does not grant combat, breeding, healing or loyalty bonuses;
- wild Pokémon near a residence remain wild unless another authoritative system changes that state.

## 6. Residential routines

```yaml
residential_routine:
  routine_id: null
  household_id: null
  actor_ids: []
  location_refs: []
  time_window: null
  activity_tag: null
  dependency_ids: []
  compression_default: true
  interruption_hooks: []
```

Candidate routine tags:
- leave_for_work;
- return_home;
- meal;
- maintenance;
- study;
- care;
- social_visit;
- errands;
- Pokémon exercise;
- delivery;
- quiet_time.

Routine should usually compress. It becomes a scene only when a meaningful decision, interruption or consequence exists.

## 7. Neighborhood continuity

```yaml
neighborhood_state:
  neighborhood_id: null
  settlement_id: null
  residence_ids: []
  public_space_ids: []
  service_ids: []
  recurring_actor_ids: []
  route_refs: []
  environmental_state_refs: []
  shared_issue_ids: []
  public_memory_refs: []
```

A neighborhood is useful because repeated routes and people create callbacks. It should not become a universal social reputation meter.

## 8. Neighbor relationship edge

```yaml
neighbor_edge:
  actor_a_id: null
  actor_b_id: null
  basis: residential_proximity
  shared_event_ids: []
  known_promises: []
  known_conflicts: []
  assistance_events: []
  private_label: none
```

Residential proximity allows encounter opportunities. It does not infer friendship, trust or hostility.

## 9. Residential problem

```yaml
residential_problem:
  problem_id: null
  residence_id: null
  household_id: null
  problem_type: null
  observation_refs: []
  affected_actor_ids: []
  affected_service_ids: []
  current_impacts: []
  suspected_causes: []
  confirmed_causes: []
  candidate_resolutions: []
  urgency: low
  escalation_trigger_ids: []
```

Possible problem types:
- maintenance;
- access;
- recurring noise;
- environmental exposure;
- service interruption;
- crowding;
- habitat overlap;
- route disruption;
- accommodation mismatch;
- relocation pressure;
- safety concern;
- disputed responsibility.

These are narrative categories, not legal classifications.

## 10. Relocation case

```yaml
relocation_case:
  relocation_id: null
  moving_actor_ids: []
  moving_pokemon_entity_ids: []
  origin_residence_id: null
  candidate_residence_ids: []
  reason_refs: []
  constraint_refs: []
  dependency_ids: []
  decision_owner_ids: []
  selected_residence_id: null
  move_status: evaluating
  move_event_id: null
  followup_review_trigger: null
```

Suggested statuses:
- EVALUATING
- WAITING_ON_INFORMATION
- WAITING_ON_DEPENDENCY
- OPTION_SELECTED
- PREPARING
- MOVING
- SETTLED
- RECONSIDERING
- CANCELLED

A relocation should not occur instantly because a quest completed. It should emit a move event and update connected state.

## 11. Candidate residence comparison

```yaml
residence_option_review:
  relocation_id: null
  residence_id: null
  positive_factors: []
  negative_factors: []
  unknowns: []
  evidence_refs: []
  dependency_refs: []
  rejected_reason: null
  review_status: pending
```

The useful gameplay is often discovering why an apparently good option fails.

## 12. Move event

```yaml
move_event:
  move_event_id: null
  relocation_id: null
  effective_time: null
  origin_residence_id: null
  destination_residence_id: null
  actor_ids: []
  pokemon_entity_ids: []
  belongings_or_asset_refs: []
  route_ref: null
  support_actor_ids: []
  completed_steps: []
  outstanding_steps: []
  emitted_state_changes: []
```

The move updates:
- residence occupancy;
- household membership where applicable;
- recurring routes;
- nearby service access;
- neighbor surfaces;
- delivery/contact address where modeled;
- public or institutional records only where an authored system requires them.

## 13. Former-home persistence

The origin should not vanish after relocation.

```yaml
former_residence_link:
  actor_id: null
  residence_id: null
  occupied_from: null
  occupied_until: null
  remembered_event_ids: []
  remaining_asset_refs: []
  unresolved_issue_ids: []
  neighbor_contact_ids: []
```

This supports later callbacks, investigations, sentimental returns or unresolved maintenance without assigning private emotions automatically.

## 14. Residential project

```yaml
residential_project:
  project_id: null
  residence_id: null
  sponsor_actor_ids: []
  objective: null
  prerequisites: []
  material_refs: []
  labor_refs: []
  service_dependencies: []
  environmental_constraints: []
  phases: []
  current_phase: planned
  completion_outputs: []
  visual_change_refs: []
  future_maintenance_ids: []
```

Examples:
- repair a damaged roof;
- create an accessible entrance;
- convert a room into an authored workspace;
- improve safe storage;
- add a non-mechanical Pokémon accommodation;
- repair drainage;
- restore a courtyard;
- prepare temporary guest space.

Exact prices, build times, legal permissions, material requirements and mechanical effects require separate authority.

## 15. Residence-service dependency graph

A household can be affected by external systems.

Example:

```text
residence
  -> water/service connection
  -> local route access
  -> care access
  -> food/market access
  -> communications coverage
  -> waste/remediation service
  -> nearby habitat condition
```

A residential quest should derive from an actual dependency rather than inventing a random chore.

## 16. Temporary displacement

```yaml
temporary_displacement:
  displacement_id: null
  affected_household_ids: []
  source_problem_id: null
  start_event_id: null
  temporary_residence_ids: []
  support_service_ids: []
  return_conditions: []
  permanent_relocation_option_ids: []
  current_state: active
```

This connects to crisis, care, hospitality and public works without defining shelter law or entitlement policy.

## 17. Residential ecology overlap

```yaml
residential_ecology_overlap:
  overlap_id: null
  residence_id: null
  observed_pokemon_refs: []
  observation_event_ids: []
  habitat_state_ids: []
  recurring_pattern: unknown
  disturbance_sources: []
  household_response_state: observing
  stewardship_refs: []
```

Potential outcomes:
- coexistence with a non-mechanical accommodation;
- stewardship consultation;
- route or maintenance adjustment;
- temporary closure;
- relocation of human activity;
- further observation;
- battle only when actual encounter state supports it.

## 18. Privacy and information

Residential state is private by default.

The generator should separate:
- canonical occupancy truth;
- what neighbors know;
- what institutions know;
- what public records contain;
- what media has published;
- what the player has personally observed.

A visible light, parked vehicle or Pokémon outside does not prove who is home.

## 19. Domestic evidence

A residence may become relevant to a case without becoming freely searchable.

Domestic observations should be recorded through the evidence/case systems and only when the player has a legitimate authored reason to obtain them.

This layer does not create search authority, warrants, trespass rules or property rights.

## 20. Home as preparation surface

A residence can support preparation scenes through stored narrative assets, contacts, maps, notes, equipment already owned or other established state.

It must not grant:
- free PTU items;
- healing bonuses;
- extra daily actions;
- combat stat bonuses;
- automatic move tutoring;
- training XP;
- breeding advantages;
- feature access;
- crafting discounts.

## 21. Dense-world preference

Before creating a new residence, check whether an existing building or room can support the needed story through changed occupancy or state.

Preferred order:
1. existing residence with a changed household;
2. existing empty or underused authored space;
3. existing building converted through a residential project;
4. genuinely new construction when the setting requires it.

## 22. Procedural residential hook generator

```yaml
residential_hook_candidate:
  source_residence_id: null
  source_household_id: null
  trigger_state_ids: []
  unresolved_constraint_ids: []
  candidate_actor_ids: []
  related_system_ids: []
  playable_decisions: []
  compression_allowed: true
  mechanics_review_required: false
```

Reject a generated hook when it has no real world-state cause or only asks the player to perform repetitive upkeep.

## 23. Boundary with existing systems

Use `observation-settlement-time-layer.md` for settlement-level housing capability and regional clocks.

Use `civic-governance-public-works-layer.md` when the central issue is a collective land-use, infrastructure or public decision.

Use `travel-transport-expedition-layer.md` for movement between locations and transport availability.

Use `food-agriculture-hospitality-layer.md` or hospitality extensions for commercial or temporary guest service rather than a stable household.

Use `social-bonds-mentorship-clubs-layer.md` for authored interpersonal bonds.

Use `care-recovery-welfare-layer.md` for treatment, recovery and medical privacy.

Use `case-authority-custody-layer.md` for investigations and evidence authority.

Use this layer when the persistent residential place, household composition, relocation or home adaptation is the central state object.

## 24. Minecraft representation

Preferred visible outputs:
- occupied versus vacant authored rooms;
- personal but privacy-safe decoration states;
- changed signage where appropriate;
- moved NPC home positions;
- recurring arrival/departure routes;
- repair scaffolding;
- accessible paths;
- environmental wear;
- Pokémon resting or shelter surfaces where authored;
- changed yards, balconies or shared courtyards;
- packed or unpacked move-state props;
- former-home continuity rather than deletion.

The Minecraft adapter renders authoritative state. It does not decide occupancy, ownership or relocation outcomes.

## 25. Encounter implementation contract — Stairwell Evacuation

Narrative premise: a residential building has an active incident while a hostile or panicked Pokémon encounter blocks the safest exit.

Full version:
- multiple occupants need to reach a safe zone;
- narrow-space movement matters;
- interception, forced displacement and blocked exits may matter;
- tactical AI may need to protect or pursue routes rather than simply maximize damage;
- environmental hazards may change usable tiles.

Capability dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING;
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

Reduced version:
Evacuate all noncombatant residents through narrative world state before battle begins. Run a fixed-map battle with only legal combatants. The authoritative result determines whether the route becomes safe, remains closed or requires a later noncombat solution.

## 26. Encounter implementation contract — Courtyard Habitat Conflict

Narrative premise: recurring wild Pokémon activity around a shared residential courtyard escalates into a confrontation while residents disagree about how to respond.

Full version:
- territorial space and withdrawal routes matter;
- residents may need protection without becoming combatants;
- environmental zones or changing obstacles may matter;
- AI should understand escape/territory rather than only KO logic.

Dependencies follow the same map as Stairwell Evacuation. Dynamic territory, forced displacement, environmental zones, objective-aware AI and embodied playback remain blocking.

Reduced version:
Clear residents from the courtyard first. If battle is necessary, instantiate only the active Pokémon and Trainers on a static legal arena. Resolve stewardship, coexistence, repair or relocation consequences afterward through narrative state.

## 27. Noncombat implementation contract — Three Homes Survey

Narrative premise: a household evaluates several possible residences for one persistent constraint.

This can run now as narrative state. It requires no PTU battle resolution when the survey uses observation, interviews and established world facts.

The scene may read:
- route access;
- service availability;
- observed noise/weather context;
- authored accessibility state;
- household routine constraints;
- Pokémon observations;
- maintenance history;
- public-works dependencies.

A fully embodied visit loop in Minecraft still depends on adapter/playback support, but server/UI state can represent the decision before that integration is complete.

## 28. Implementation priority

Recommended order:
1. residence and household records;
2. occupancy history;
3. suitability constraints;
4. relocation case and move event;
5. neighborhood continuity;
6. residential projects and maintenance handoff;
7. Pokémon accommodation records;
8. procedural hook generator;
9. Minecraft visual-state mapping.

This layer should increase attachment to existing places without creating a housing economy simulator or inventing unsupported PTU mechanics.