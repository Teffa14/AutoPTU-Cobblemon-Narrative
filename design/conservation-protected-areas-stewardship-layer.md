# Ouros Conservation, Protected Areas & Stewardship Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

Ouros already models ecology, wild collectives, science, care, travel, settlements, factions, cases and civic decisions. This layer adds persistent stewardship state so the world can represent habitats that people intentionally manage, restore, monitor or protect without assuming every wild Pokémon problem should end in capture or combat.

The core distinction is between ecology and policy.

A habitat can be ecologically important without being legally or culturally protected. A place can be declared protected while still being degraded. A local tradition can restrict use even when no formal institution does. A temporary closure can exist without changing the underlying habitat. None of these states automatically changes PTU legality unless the governing rules and implementation explicitly support it.

## 1. Separate the important truths

Ouros should keep these layers distinct:

- ecological state: what is physically happening in the habitat;
- observed evidence: what has actually been documented;
- stewardship claim: why someone believes the area or population needs care;
- management designation: what an institution/community has decided to do;
- visitor policy: what activities are requested, restricted, scheduled or supervised;
- enforcement capacity: whether anyone can realistically maintain that policy;
- public belief: what visitors think the rules or ecological situation are;
- mechanical state: what AutoPTU actually allows in a battle/capture scene.

A policy never rewrites ecological truth. A rumor never becomes policy. A sign never creates a PTU mechanic by itself.

## 2. Protected-area schema

```yaml
stewardship_area:
  stewardship_area_id: null
  location_ids: []
  status: PROPOSED
  designation_type: null
  stewardship_actor_ids: []
  management_body_ids: []
  local_custodian_claim_ids: []
  ecological_value_claim_ids: []
  cultural_value_claim_ids: []
  management_objectives: []
  visitor_use_zones: []
  access_policy_ids: []
  active_monitoring_program_ids: []
  restoration_project_ids: []
  threat_ids: []
  corridor_ids: []
  public_information_packet_ids: []
  last_management_review_event_id: null
  unresolved_questions: []
  canon_status: proposed
```

Candidate designation types are descriptive only:

- COMMUNITY_STEWARDSHIP_AREA
- RESEARCH_RESERVE
- HABITAT_REFUGE
- MIGRATION_CORRIDOR
- NESTING_OR_ROOST_PROTECTION
- URBAN_COEXISTENCE_ZONE
- RESTORATION_SITE
- CULTURAL_ECOLOGICAL_SITE
- MANAGED_USE_AREA
- TEMPORARY_PROTECTION
- OTHER_AUTHORED_DESIGNATION

The generator must not create legal powers from the label.

## 3. Zoning instead of one global rule

Large areas can contain different use zones.

```yaml
visitor_use_zone:
  zone_id: null
  stewardship_area_id: null
  location_ids: []
  purpose: null
  permitted_activity_claims: []
  restricted_activity_claims: []
  supervision_requirements: []
  season_conditions: []
  time_conditions: []
  ecological_trigger_conditions: []
  source_policy_id: null
  implementation_status: proposed
```

Possible uses:

- public trail;
- research-only sector;
- seasonal nesting buffer;
- supervised training area;
- no-entry restoration patch;
- observation blind;
- visitor center;
- emergency access corridor;
- managed harvest zone;
- transit-only route.

Do not assume "protected" means nobody may enter, battle or catch. Those are authored policy choices that require separate canon and mechanic review.

## 4. Stewardship actors

Stewardship can come from multiple actor types:

- local residents;
- long-standing custodians;
- researchers;
- Ranger-like field teams;
- municipal institutions;
- clubs;
- conservation organizations;
- Gym/Dojo institutions with a local role;
- transport operators;
- farmers or fishers using the landscape;
- mixed management boards;
- temporary crisis teams.

```yaml
stewardship_actor_role:
  actor_id: null
  stewardship_area_id: null
  role_type: null
  mandate_source_id: null
  knowledge_scope_ids: []
  operational_capabilities: []
  current_tasks: []
  conflicts_of_interest_ids: []
  public_contact_channels: []
```

Knowledge authority and decision authority must remain separate. A researcher may know more about a migration route without having authority to close it. A local steward may have authority over access without controlling PTU capture mechanics globally.

## 5. Management objectives

Each stewardship area should have explicit goals rather than a generic conservation score.

Examples:

- maintain seasonal nesting access;
- restore water quality;
- reduce disturbance at a roost;
- keep a wildlife corridor open;
- monitor a newly arrived population;
- prevent spread of a confirmed harmful organism;
- repair habitat after a fire;
- protect a culturally significant site while allowing public visits;
- reduce conflict between a settlement and a wild collective;
- maintain a mixed-use wetland for both residents and wild Pokémon.

```yaml
management_objective:
  objective_id: null
  stewardship_area_id: null
  statement: null
  evidence_basis_ids: []
  success_indicators: []
  failure_or_risk_indicators: []
  review_date_or_clock_id: null
  responsible_actor_ids: []
  tradeoff_ids: []
```

Do not turn these into numeric buffs by default.

## 6. Monitoring and management review

Protected areas should change because people observe and respond.

```yaml
management_review:
  review_id: null
  stewardship_area_id: null
  observation_window: null
  evidence_ids: []
  ecological_changes: []
  visitor_pressure_changes: []
  management_actions_reviewed: []
  unintended_consequences: []
  proposed_changes: []
  adopted_changes: []
  unresolved_disagreements: []
```

A failed intervention is valid content. The system should preserve what was attempted and why instead of rewriting history as if the correct plan had always been obvious.

## 7. Habitat restoration projects

Restoration is a project, not a one-click state reset.

Potential project phases:

- assess;
- stabilize;
- remove or reduce an identified pressure;
- repair habitat structure;
- re-establish access/corridors;
- monitor recovery;
- adapt the plan;
- hand off to routine stewardship.

Restoration can create world-state changes in Minecraft:

- repaired waterways;
- reopened passages;
- vegetation or terrain variants;
- temporary fencing/signage;
- relocated services;
- observation stations;
- reduced or altered spawn opportunities;
- different NPC presence.

Exact Pokémon encounter changes must be generated from ecological state and validated against Cobblemon spawn implementation, not hardcoded as narrative rewards.

## 8. Corridors and connectivity

A protected area does not exist in isolation.

```yaml
habitat_corridor:
  corridor_id: null
  endpoint_location_ids: []
  traversed_location_ids: []
  target_population_or_collective_ids: []
  seasonal_conditions: []
  known_barriers: []
  disturbance_sources: []
  monitoring_points: []
  status: unknown
  evidence_ids: []
```

Corridor stories can intersect transport, public works, agriculture and settlement growth. A new road may improve human travel while fragmenting movement for a wild collective. That is a tradeoff state, not automatic villainy.

## 9. Coexistence incidents

Human–Pokémon conflict should record causes before assigning blame.

```yaml
coexistence_incident:
  incident_id: null
  location_id: null
  affected_actor_ids: []
  affected_population_or_collective_ids: []
  observed_behaviors: []
  human_activity_context: []
  suspected_drivers: []
  evidence_ids: []
  immediate_response_ids: []
  long_term_management_candidate_ids: []
```

Examples:

- wild Pokémon repeatedly entering a market because waste is accessible;
- a migration route crossing a newly expanded road;
- a nesting colony reacting to festival noise;
- farmers losing crops after another food source disappeared;
- a territorial group using a restored water source.

Never assign hatred, revenge or moral guilt to wild Pokémon without authored evidence.

## 10. Biosecurity and newly arrived species

A species being newly observed does not automatically make it invasive.

Ouros should separate:

- NEWLY_RECORDED
- RANGE_EXPANSION_SUSPECTED
- HUMAN_INTRODUCTION_SUSPECTED
- ESTABLISHED_NEW_POPULATION
- ECOLOGICAL_IMPACT_UNCONFIRMED
- ECOLOGICAL_IMPACT_CONFIRMED
- MANAGEMENT_ACTION_AUTHORIZED

The word "invasive" should require canonized ecological evidence and management context. Narrative generators must not turn rarity or unfamiliarity into a kill/capture order.

## 11. Rescue, rehabilitation, release and relocation

These states must remain separate from ownership.

```yaml
wild_care_transition:
  transition_id: null
  pokemon_entity_id: null
  origin_location_id: null
  care_case_id: null
  custody_state: null
  release_candidate: false
  release_location_candidates: []
  relocation_reason_claim_ids: []
  readiness_evidence_ids: []
  authorization_state: unresolved
  actual_release_event_id: null
  post_release_monitoring_ids: []
```

Hard rules:

- treatment does not imply capture/ownership;
- temporary custody does not imply ownership;
- relocation is not automatically beneficial;
- a release should not silently erase a persistent Pokémon's identity;
- mechanical capture/release legality must come from governing PTU/Caelo and adapter rules;
- wild collectives may react to the return/removal of an individual only when collective state supports it.

## 12. Visitor behavior and education

Visitor rules can be communicated through:

- signs;
- rangers/guides;
- permit or booking systems if canonized;
- visitor centers;
- briefings;
- public media;
- local guides;
- seasonal notices;
- trail markers;
- observation reports.

The system should prefer understandable causal explanations over arbitrary invisible restrictions.

If a trail closes because a nesting site is active, players should be able to learn that reason unless secrecy itself is an authored story state.

## 13. Sustainable use

Not every protected landscape must be a no-use wilderness.

Ouros can model managed use such as:

- berry gathering;
- fishing;
- research sampling;
- grazing;
- tourism;
- transport corridors;
- cultural ceremonies;
- educational events;
- limited material collection.

Whether these are permitted, restricted or seasonal is world-specific canon. Do not import real-world laws or assume modern environmental regulations.

## 14. Stewardship reputation

Avoid a single "conservation score".

Relevant relationship dimensions may include:

- trust from local stewards;
- reliability in field work;
- respect from researchers;
- public confidence;
- history of following access agreements;
- competence in crisis response;
- unresolved disputes.

These are social/institutional state only. They must not grant PTU Features or capture bonuses unless explicit mechanics exist.

## 15. Minecraft/Cobblemon representation

Potential visible states:

- gates or trail signs;
- seasonal barriers;
- observation platforms;
- ranger/research stations;
- restoration structures;
- habitat variants;
- temporary camps;
- visitor centers;
- altered path routing;
- wildlife corridor markers;
- damaged/restored infrastructure;
- different aggregate spawn context when adapter support exists.

Do not despawn all Pokémon merely because a zone closes to visitors. Visitor access and ecological presence are different states.

## 16. AutoPTU boundary

This layer can create narrative reasons for encounters, but it does not alter PTU legality.

Potential encounter dependencies must use the permanent capability categories:

- targeting/footprints/range/LoS
- base movement legality
- complete movement including push/pull/knockback/interception/forced movement
- core calculations
- action economy/initiative
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- terrain/weather/hazards/zones/reactions
- move-specific behavior
- abilities
- items
- Trainer Features/perks
- AI legal-action infrastructure
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

A habitat-management encounter may be narratively simple while mechanically depending on blocked families. Mark the exact dependency.

## 17. Encounter contract A — Corridor Crossing

Narrative premise:

A known seasonal movement route intersects a human transit corridor during an unusually dense migration window. Players need to keep both travelers and wild Pokémon moving safely while identifying the cause of the changed timing.

FULL version:

- moving groups cross the tactical map;
- temporary protected lanes matter;
- opponents or panicked actors may block passages;
- success can be REACH_TILE / PROTECT / CLEAR_ROUTE rather than KO;
- AI understands corridor movement;
- world state writes back whether the migration passed safely.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if dynamic lane hazards are used
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING if used
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

REDUCED version:

Migration movement remains overworld/world-state. AutoPTU runs one or more static legal encounters only when conflict actually occurs. Players clear a fixed chokepoint or defend themselves, then the migration outcome is resolved from explicit world-state choices rather than invented escort mechanics.

## 18. Encounter contract B — Restoration Site Disturbance

Narrative premise:

A habitat-restoration site is attracting Pokémon earlier than expected. Workers need space to stabilize equipment while the players determine whether the Pokémon are curious, displaced or reacting to a resource change.

FULL version:

- interactable restoration equipment;
- zones that change as work proceeds;
- optional non-KO objective;
- AI responds to objective state;
- terrain/hazard state can change during the scene.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/forced movement: BLOCKING if physical repositioning matters
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING if used
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

REDUCED version:

Equipment stabilization happens in overworld state before or after the fight. The tactical map is static. The encounter uses legal standard battle/capture/withdrawal rules only, and the restoration project's response is written back after the battle.

## 19. Encounter contract C — Ranger Survey Interrupted

Narrative premise:

A survey team is collecting evidence in a managed habitat when a separate disturbance creates danger nearby. The important objective is to preserve people and survey provenance, not necessarily defeat every wild Pokémon.

FULL version dependencies:

- protect/withdraw objective support;
- objective-aware AI;
- complete movement/interception if extraction lanes matter;
- adapter support for survey gear and NPC positioning;
- lifecycle/status/damage categories as required by actual encounter participants.

REDUCED version:

Survey NPCs and equipment remain outside the grid. Players handle a static legal encounter while the world layer records whether they evacuated, abandoned samples, completed the survey later or changed the management plan.

## 20. Design guardrails

- Never create an automatic capture ban from rarity alone.
- Never label a newly observed species invasive without evidence.
- Never use conservation as an excuse to remove player agency without visible world-state reasons.
- Never convert treatment or temporary custody into ownership.
- Never grant spawn buffs, capture modifiers or Pokémon capabilities through stewardship reputation.
- Never assume relocation is the correct answer.
- Never assume local communities and scientific institutions agree.
- Never treat cultural stewardship as decorative flavor for an external institution.
- Never create a Legendary boss because a protected site has a mythic association.
- Never duplicate PTU mechanics in Minecraft scripts to make a conservation scenario work.

## 21. Integration with existing layers

Wild collective agency supplies group identity and movement.

Observation/science supplies evidence.

Civic governance supplies prospective public decisions.

Case/custody handles incidents and evidence when wrongdoing is alleged.

Care handles rehabilitation and recovery.

Travel/public works supply route and infrastructure conflicts.

Seasonality supplies migration/nesting windows.

Media supplies public notices and misinformation.

Conservation stewardship connects those systems through management intent, review and habitat-scale consequences.