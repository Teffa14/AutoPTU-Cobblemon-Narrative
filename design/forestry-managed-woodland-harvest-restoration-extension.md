# Forestry, Managed Woodland, Harvest & Restoration Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This extension gives Ouros a persistent operational model for forests and other managed woodlands that can simultaneously function as habitat, travel space, workplace, material source, restoration site and cultural landscape.

It fills the gap between Conservation, Material Culture, Workplaces, Worksite Safety, Travel, Weather/Crisis, Pokémon Work and Wild Ecology without replacing any of those systems.

The extension owns woodland-use history, intervention records, patch/stand continuity, forest-product provenance handoffs and post-disturbance forestry review.

It does not define universal logging law, ownership, harvest rights, forestry economics, tree growth math, PTU terrain effects, falling-tree damage, wildfire rules, Cut/Strength behavior or species-based work capability.

## Authority boundaries

Conservation owns ecological interpretation, managed-use designation, restoration objectives, protected-area decisions and stewardship policy.

Material Culture owns physical material batches, item instances, transformation and provenance after woodland material enters the material economy.

Workplaces owns workers, roles, shifts, assignments and staffing capacity.

Pokémon Work owns individual Pokémon work assignments and capability-evidence review.

Worksite Safety owns preventive work restrictions, near misses, corrective actions and return-to-work review.

Weather/Crisis owns active storms, fire emergencies, evacuations and crisis recovery.

Travel owns route/service state and ordinary traveler access.

Wild Collective/Interspecies Ecology owns wild group state, observed habitat use, territory and ecological relationships.

This extension owns the persistent woodland structure that connects those handoffs.

## 1. Managed woodland site

```yaml
managed_woodland_site:
  woodland_id: null
  location_ids: []
  woodland_type_claims: []
  zone_ids: []
  stewardship_area_refs: []
  operator_or_workplace_refs: []
  travel_route_refs: []
  ecological_context_refs: []
  wild_collective_refs: []
  material_source_refs: []
  intervention_ids: []
  disturbance_refs: []
  restoration_project_refs: []
  public_information_refs: []
  historical_use_claim_refs: []
  current_access_summary: null
  unresolved_questions: []
  canon_status: proposed
```

`woodland_type_claims` may describe local usage such as old growth, coppice, plantation, mixed woodland, post-fire regrowth or community woodlot, but the label is descriptive. It creates no mechanical effect or ownership rule.

## 2. Woodland zones

```yaml
woodland_zone:
  zone_id: null
  woodland_id: null
  location_refs: []
  current_use_claims: []
  ecological_role_claims: []
  access_state_ref: null
  route_refs: []
  work_area_refs: []
  restoration_refs: []
  habitat_overlap_refs: []
  intervention_history_ids: []
  current_condition_claims: []
```

Possible authored uses include:

- public trail corridor;
- managed material-use patch;
- restoration patch;
- habitat-retention patch;
- post-storm assessment zone;
- post-fire assessment zone;
- research plot;
- charcoal/fuelwood source area where canonically appropriate;
- cultural-use area;
- temporary closure area;
- mixed-use woodland.

These are orchestration labels, not universal legal categories.

## 3. Woodland observation

```yaml
woodland_observation:
  observation_id: null
  woodland_id: null
  zone_id: null
  observer_ids: []
  observed_at: null
  observation_type: null
  description_claim_ref: null
  evidence_refs: []
  related_intervention_ids: []
  related_disturbance_refs: []
  interpretation_claim_refs: []
  status: RECORDED
```

Candidate observations:

- fresh or old stumps;
- fallen timber;
- blocked trail;
- canopy opening;
- sap/bark removal signs;
- scorch/fire evidence;
- storm damage;
- new regrowth;
- reduced regrowth;
- nest/den use;
- deadwood use;
- erosion near a work route;
- changed wild-Pokémon route;
- equipment or survey markers;
- material stockpile.

An observation records what was seen. It does not establish who caused it or why.

## 4. Forest intervention

```yaml
forest_intervention:
  intervention_id: null
  woodland_id: null
  zone_ids: []
  intervention_type: authored
  objective_refs: []
  authority_or_mandate_refs: []
  operator_refs: []
  work_assignment_refs: []
  pokemon_work_assignment_refs: []
  equipment_refs: []
  planned_start: null
  actual_start: null
  completed_at: null
  source_condition_refs: []
  output_batch_refs: []
  visible_world_change_refs: []
  ecological_followup_refs: []
  safety_refs: []
  status: PLANNED
```

Possible intervention types:

- survey;
- selective removal;
- fallen-tree clearance;
- trail clearance;
- deadwood retention;
- restoration planting;
- access closure;
- material collection;
- sap/bark collection where canonically supported;
- vegetation management;
- route rerouting;
- post-disturbance stabilization;
- monitoring installation.

The label never establishes a yield, Skill check, Move requirement or legality.

## 5. Forest-product provenance handoff

```yaml
forest_product_handoff:
  handoff_id: null
  woodland_id: null
  source_zone_id: null
  intervention_id: null
  material_batch_ref: null
  material_identity_ref: null
  quantity_state: null
  collected_at: null
  collector_or_operator_refs: []
  custody_ref: null
  destination_ref: null
  transformation_pending: true
  provenance_evidence_refs: []
  unresolved_identity_claims: []
```

The handoff connects the woodland to Material Culture. Exact quantity, value, recipe suitability and mechanical effect remain outside this extension.

A batch may be narratively significant because of provenance without becoming mechanically superior.

## 6. Aggregate vegetation versus exact trees

Do not give every tree a persistent object identity.

Default representation:

```yaml
woodland_patch_state:
  zone_id: null
  broad_structure_claims: []
  canopy_state_claims: []
  understory_state_claims: []
  deadwood_state_claims: []
  regeneration_claims: []
  observation_refs: []
  last_reviewed_at: null
```

Create an exact persistent tree/log object only when authored significance requires it, for example:

- landmark or culturally important tree;
- evidence in a case;
- exact fallen log controlling access;
- research-tagged specimen;
- memorial/history object;
- central element of a restoration project.

Minecraft block identity alone must not force narrative identity for every tree.

## 7. Deadwood and fallen timber

A fallen tree can belong to several systems at once.

```yaml
fallen_timber_record:
  record_id: null
  woodland_id: null
  zone_id: null
  exact_object_ref: null
  first_observed_at: null
  cause_claim_refs: []
  route_effect_refs: []
  habitat_use_refs: []
  safety_refs: []
  recovery_candidate_refs: []
  retention_decision_refs: []
  current_state: OBSERVED
```

Possible states:

- OBSERVED
- ASSESSING
- RETAINED
- PARTIALLY_CLEARED
- CLEARED_FROM_ROUTE
- RECOVERED_AS_MATERIAL
- RELOCATED
- DECOMPOSING_IN_PLACE
- UNKNOWN

A route crew may clear only enough timber for passage while leaving the remainder in place. That can be a successful outcome.

## 8. Post-disturbance review

```yaml
woodland_disturbance_review:
  review_id: null
  woodland_id: null
  source_disturbance_ref: null
  affected_zone_ids: []
  field_observation_refs: []
  route_change_refs: []
  ecological_change_claim_refs: []
  worksite_change_refs: []
  material_opportunity_claim_refs: []
  safety_handoff_refs: []
  conservation_handoff_refs: []
  restoration_candidate_refs: []
  unresolved_questions: []
  status: OPEN
```

This is particularly useful after:

- storm/windthrow;
- confirmed fire;
- flood/erosion;
- major harvest intervention;
- route construction;
- infrastructure work;
- unknown disturbance.

The review does not create a PTU Hazard from the presence of damaged trees.

## 9. Regeneration and restoration evidence

```yaml
woodland_regeneration_observation:
  observation_id: null
  woodland_id: null
  zone_id: null
  observed_at: null
  method_ref: null
  regeneration_claims: []
  vegetation_evidence_refs: []
  wildlife_use_evidence_refs: []
  route_or_access_evidence_refs: []
  comparison_baseline_refs: []
  uncertainty_notes: []
```

One successful planting does not prove restoration. One absent species does not prove ecological failure.

Conservation owns the interpretation of whether management objectives are being met.

## 10. Woodland-use conflict

```yaml
woodland_use_conflict:
  conflict_id: null
  woodland_id: null
  zone_ids: []
  actor_or_group_refs: []
  observed_activity_refs: []
  ecological_evidence_refs: []
  route_refs: []
  material_use_refs: []
  public_claim_refs: []
  management_decision_refs: []
  status: OPEN
```

Possible conflicts include:

- work route versus wildlife corridor;
- public shortcut versus restoration patch;
- deadwood retention versus trail clearance;
- material collection versus cultural use;
- visitor pressure versus ordinary work;
- harvest schedule versus nesting/roosting observation;
- emergency access versus long-term restoration.

Do not create a hidden “correct side.” Preserve the actual objectives and evidence.

## 11. Pokémon work boundary

A Pokémon may participate in woodland work only through an individual Pokémon Work assignment with evidence for the exact required capability.

Examples that require review:

- moving timber;
- locating material or people;
- clearing vegetation;
- transporting equipment;
- fire response;
- planting or watering;
- path scouting.

Type or species is insufficient.

A Cobblemon animation of a Pokémon interacting with a log is presentation. It does not resolve the task.

## 12. PTU/Caelo mechanical boundary

The generator must not invent:

- Cut/Strength or other Move-based forestry rules;
- falling-tree or branch damage;
- smoke/fire statuses;
- difficult-terrain penalties;
- canopy Accuracy/LoS modifiers;
- entangling undergrowth effects;
- weather-driven displacement;
- harvest yields;
- growth timers;
- item quality bonuses;
- work Skill DCs;
- Trainer Feature bonuses;
- wild-Pokémon “forest buffs.”

When a battle needs any of these, the encounter contract must name the relevant permanent capability category and remain reduced until the exact behavior is verified.

## 13. Cobblemon/Minecraft integration

Reuse as much of Minecraft/Cobblemon as possible for world presentation and interaction.

Strong reuse candidates:

- logs/leaves/saplings/vines/mushrooms and ordinary blocks;
- paths, fences, gates, signs and worksite structures;
- ambient weather, particles and sound;
- Pokémon entities, models, forms, poses, animation and cries;
- item models and props where available;
- entity tracking and networking;
- persistence hooks;
- reviewed spawn/ecology observations;
- block updates used as presentation of an already-authorized world-state change.

Adapter-required surfaces:

- interpreting a block break as a forestry intervention;
- mapping aggregate woodland state to visible block changes;
- selecting which wild entities are narratively persistent;
- binding an encounter manifest to overworld actors;
- projecting AutoPTU battle events back into the forest.

Forbidden authority:

- Minecraft/Cobblemon BattleState deciding participants, teams, legality, HP, statuses, positions, effects or result;
- nearby/spawned Pokémon automatically becoming combatants;
- a block breaking automatically creating a legal material batch;
- presentation weather becoming a PTU weather/hazard rule;
- Cobblemon AI deciding tactical battle intent.

Required direction:

`Ouros woodland/world state -> explicit encounter manifest -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

## 14. Encounter A — Windthrow Route Withdrawal

Narrative premise:

A storm has left fallen timber across a mixed-use woodland route. A work crew is assessing what can be cleared while a wild group displaced by the changed structure begins using the same corridor.

Full intended version:

Workers withdraw through multiple safe exits while routes change around unstable timber. Combatants may use legal Intercept/forced movement, fixed and changing blockers, and territorial/withdrawal AI. If exact PTU rules exist later, unstable woodland conditions may become reviewed tactical hazards.

Permanent capability dependencies:

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

Reduced version:

The work crew leaves the tactical area first. The unstable section is closed in world state. Ouros selects explicit combatants in a stable clearing with fixed legal geometry. Fallen timber outside the arena remains a route/forestry problem. No branch fall, tree roll, wind gust or debris applies scripted damage or displacement. After the battle, forestry/safety/conservation decide whether assessment and clearance resume.

## 15. Encounter B — Restoration Crew Boundary Conflict

Narrative premise:

A restoration crew begins work in a patch that has also become part of a recently observed wild-Pokémon movement route.

Full intended version:

The battle or withdrawal scene protects temporary work zones while civilians/crew leave. Wild AI values exit, territory or route continuity rather than pure KO. Reviewed zones may alter access if AutoPTU eventually supports those exact rules.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL when protection/withdrawal depends on it;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for tactical restoration/vegetation zones;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:

Crew, seedlings, tools and noncombatant Pokémon leave the grid first. The scene becomes a fixed ordinary encounter or a noncombat observation sequence. The battle can make the immediate area safe enough to continue reviewing, but it never proves why the wild route changed or grants permission to remove habitat.

## 16. Noncombat encounter — The Missing Cut Mark

Premise:

A field note says a small intervention occurred in one zone, but the current visible marks seem to be somewhere else.

Playable evidence:

- old/new photographs;
- woodland observations;
- work assignments;
- material-batch provenance;
- route markers;
- testimony;
- weather/storm history;
- restoration records.

Possible outcomes include:

- the old map used a different boundary reference;
- the cut record was superseded;
- storm damage resembles work marks;
- material came from another patch;
- records remain insufficient.

No battle or hidden culprit is required.

## 17. Long-form arc — A Working Forest Learns Its Boundaries

Phase 1: establish ordinary forest use, work routes, public paths and ecological observations.

Phase 2: a minor discrepancy links use pressure to one patch without proving cause.

Phase 3: players compare work history, route state, wildlife observations and material provenance.

Phase 4: one route/intervention is changed.

Phase 5: after time passes, the patch shows intended and unintended effects.

Phase 6: a later storm, seasonal shift or visitor change tests the revised arrangement.

Phase 7: management is reviewed again and the resulting landscape becomes the next persistent baseline.

The arc has no hidden “forest health meter.” Changes remain visible as state, evidence, routes, work practices and ecology.

## 18. Canon gates

Before promotion, canon review must decide where relevant:

- what managed woodlands exist in Ouros;
- who uses or stewards them;
- what authority governs access/interventions;
- what forest products exist and where;
- whether charcoal, sap, fuelwood, construction timber or other practices are regionally important;
- whether any trees/sites have cultural or sacred status;
- what restoration practices and technologies exist;
- what occupational roles are common;
- how wild-Pokémon habitat and public use are balanced culturally;
- what data can be shown physically in Minecraft without over-simulating every tree.

Until then this extension remains proposed systems design.