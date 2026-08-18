# Ouros Material Culture, Crafting & Economy Layer

Status: Proposed systems design. Not established canon.

## Purpose

The existing Ouros architecture already models missions, settlements, factions, public events, cases, persistent Pokémon and world state. This layer adds the material side of that world: where useful things come from, who can make or repair them, how services depend on people and routes, and how objects can accumulate history.

The goal is narrative economy, not a full market simulator. Production and scarcity should create choices, relationships and world consequences without turning ordinary play into repetitive gathering or price optimization.

## 1. Mechanical item type versus physical item instance

Most consumables do not need unique narrative identity. Story-significant objects do.

```yaml
item_instance:
  item_instance_id: null
  mechanical_item_ref: null
  current_owner_id: null
  current_custodian_id: null
  maker_id: null
  source_material_batch_ids: []
  origin_event_id: null
  origin_location_id: null
  acquired_event_id: null
  condition_state: null
  cosmetic_descriptor_ids: []
  linked_event_ids: []
  repair_record_ids: []
  public_memory_ids: []
  evidence_id: null
  significance: ordinary
```

Suggested significance bands:
- ORDINARY
- PERSONAL
- COMMISSIONED
- TROPHY
- INSTITUTIONAL
- HISTORICAL
- EVIDENCE
- RELIC_CANDIDATE

The significance band affects narrative persistence only. It cannot create an unreviewed PTU bonus.

## 2. Tracking threshold

Do not create a database row for every disposable object if the game does not need it.

Create a persistent item instance when at least one of these conditions applies:
- a player explicitly marks the object as personally important;
- the item was crafted or commissioned by a named character;
- the object is unique in current world state;
- it is evidence in a case;
- it is tied to a public event or historical record;
- it was recovered from a meaningful expedition or dungeon state;
- damage, repair or transfer is part of a story;
- another actor is actively interested in this exact object.

Bulk supplies can remain aggregate inventory until something makes an individual instance narratively relevant.

## 3. Material provenance

A material batch can remember where it came from without redefining its mechanical properties.

```yaml
material_batch:
  batch_id: null
  mechanical_material_ref: null
  source_location_id: null
  source_event_id: null
  finder_or_harvester_ids: []
  acquisition_method: null
  world_time: null
  ecological_context_ids: []
  institutional_context_ids: []
  restriction_claim_ids: []
  current_holder_id: null
  transformed_into_ids: []
  rules_validation_required: true
```

Potential acquisition methods:
- gathered;
- harvested;
- excavated;
- salvaged;
- produced by a legal Pokémon capability;
- purchased;
- traded;
- institution-issued;
- dungeon recovery;
- event recovery;
- donated.

Exact yields, item values and harvesting rules come from PTU/Caelo or authored implementation data, never from narrative inference.

## 4. Provenance chain

An object may transform several times.

```yaml
provenance_event:
  provenance_event_id: null
  object_or_batch_id: null
  event_type: null
  actor_ids: []
  location_id: null
  source_ids: []
  output_ids: []
  timestamp: null
  notes_claim_ids: []
```

Candidate event types:
- FOUND
- HARVESTED
- EXCAVATED
- ISSUED
- TRADED
- SOLD
- GIFTED
- CRAFTED
- MODIFIED
- REPAIRED
- DISPLAYED
- STORED
- STOLEN
- RECOVERED
- RETURNED
- DESTROYED

This connects directly to Chronicle events and, where relevant, the evidence-custody system.

## 5. Recipe knowledge

Recipe access is knowledge state, not a universal unlock flag.

```yaml
recipe_knowledge:
  holder_id: null
  recipe_ref: null
  source_type: null
  source_actor_id: null
  source_institution_id: null
  source_event_id: null
  governing_rule_refs: []
  current_access: true
```

Candidate source types:
- governed PTU/Caelo character feature;
- formal instruction;
- apprenticeship;
- institution training;
- authored book/manual;
- discovered record;
- approved cultural tradition.

The narrative generator may propose how knowledge is learned. It may not invent a recipe or waive actual PTU prerequisites.

## 6. Production action

Every executable crafting action must be mechanically validated before it reaches the player.

```yaml
production_action:
  production_id: null
  crafter_id: null
  recipe_ref: null
  workshop_id: null
  required_tool_refs: []
  input_batch_ids: []
  output_item_refs: []
  output_item_instance_ids: []
  rules_reference_ids: []
  validation_state: pending
  source_event_id: null
```

Validation questions:
1. Does this actor actually meet the PTU/Caelo prerequisite?
2. Are required tools or facilities present?
3. Are the actual material inputs available?
4. Is the action/frequency/time requirement legal?
5. Is the resulting item implemented by AutoPTU or the Minecraft bridge?

If any answer is unresolved, the production action remains a proposal.

## 7. Workshop state

A workshop is a world actor/service node rather than a generic menu.

```yaml
workshop:
  workshop_id: null
  location_id: null
  operator_ids: []
  apprentice_ids: []
  institution_id: null
  service_ids: []
  tool_refs: []
  facility_dependencies: []
  supply_route_ids: []
  local_material_refs: []
  specialist_material_refs: []
  public_access: null
  availability_state: OPEN
  current_backlog: []
  current_problems: []
  style_tags: []
```

Suggested states:
- OPEN
- LIMITED
- COMMISSIONS_ONLY
- TEMPORARILY_CLOSED
- RELOCATING
- DAMAGED
- UNSTAFFED

Closure should have a reason in world state, such as a missing specialist, damaged facility, disrupted supply or public event.

## 8. Service offer

```yaml
service_offer:
  service_id: null
  provider_id: null
  workshop_id: null
  service_type: null
  mechanical_service_ref: null
  access_requirements: []
  material_requirements: []
  current_availability: true
  limitation_reasons: []
  mechanics_review_required: true
```

Potential narrative service categories:
- CRAFT
- REPAIR
- COOK
- REFINE
- IDENTIFY
- RESTORE
- COMMISSION
- CUSTOMIZE_COSMETIC
- PACKAGE
- STORE
- APPRAISE

These categories are orchestration labels. They do not define new mechanics.

## 9. Commission state

Commissioning allows non-crafters to participate through relationships, logistics and materials.

```yaml
commission:
  commission_id: null
  requester_id: null
  maker_id: null
  requested_mechanical_item_ref: null
  requested_cosmetic_tags: []
  material_source_plan: []
  accepted_material_batch_ids: []
  workshop_id: null
  status: DISCUSSING
  dependency_ids: []
  completion_event_id: null
  relationship_outputs: []
  provenance_outputs: []
```

Suggested states:
- DISCUSSING
- ACCEPTED
- WAITING_FOR_MATERIALS
- IN_PROGRESS
- BLOCKED
- READY
- DELIVERED
- CANCELLED

Do not simulate arbitrary real-time queues unless the authored scenario benefits from them.

## 10. Repair and continuity

Repair exists primarily to preserve meaningful object continuity.

```yaml
repair_record:
  repair_id: null
  item_instance_id: null
  repairer_id: null
  workshop_id: null
  cause_event_id: null
  input_material_batch_ids: []
  restored_state: null
  cosmetic_changes: []
  rules_reference_ids: []
  mechanics_review_required: true
```

A repaired item may gain a scar, replaced component, maker's mark or story association as cosmetic/narrative metadata. It receives no improved statistics unless a governing rule explicitly grants them.

## 11. Artisan identity

Specialists need character state beyond the services they sell.

```yaml
artisan_identity:
  actor_id: null
  profession_tags: []
  workshop_ids: []
  specialties: []
  training_lineage_ids: []
  apprentices: []
  mentors: []
  regular_client_ids: []
  supplier_ids: []
  professional_rival_ids: []
  values: []
  current_goal: null
  current_constraints: []
  signature_style_tags: []
```

Style tags should normally be cosmetic or cultural. Mechanical specialization must reference real PTU/Caelo options.

## 12. Apprenticeship and professional continuity

A service can survive beyond one NPC when skills are transferred.

```yaml
apprenticeship:
  apprenticeship_id: null
  mentor_id: null
  apprentice_id: null
  institution_id: null
  knowledge_targets: []
  current_stage: null
  milestone_event_ids: []
  blockers: []
  completion_outputs: []
```

Narrative milestones may include:
- trusted with customers;
- completes first supervised commission;
- handles repair intake;
- teaches a narrower technique to another worker;
- opens an independent workshop;
- remains with the existing shop as successor.

Actual Trainer Edges/Features are never granted by this narrative record alone.

## 13. Supply route state

```yaml
supply_route:
  supply_route_id: null
  origin_location_id: null
  destination_location_id: null
  carrier_actor_ids: []
  carrier_institution_ids: []
  material_refs: []
  route_ids: []
  operating_state: ACTIVE
  capacity_band: null
  blockers: []
  faction_interest_ids: []
  ecological_pressure_ids: []
  last_delivery_event_id: null
```

Suggested states:
- ACTIVE
- DELAYED
- REROUTED
- SUSPENDED
- DISRUPTED
- RESTORED

Supply routes connect material culture to existing infrastructure, factions, clocks and route safety.

## 14. Market state without full simulation

Ouros does not need continuous supply-and-demand pricing for every object.

```yaml
market_state:
  market_id: null
  location_id: null
  permanent_vendor_ids: []
  temporary_vendor_ids: []
  service_ids: []
  shortage_tags: []
  surplus_tags: []
  visitor_pressure: null
  event_ids: []
  supply_route_ids: []
  public_information_ids: []
```

Early implementation should use ordinal states and authored effects instead of volatile numerical prices.

Examples:
- normal supply;
- limited specialty stock;
- festival demand;
- emergency rationing;
- transport delay;
- unusual surplus after harvest;
- visiting specialist available this week/event phase.

If exact prices are surfaced, they must come from an approved economy/mechanics layer.

## 15. Scarcity event

Scarcity should be causal and legible.

```yaml
scarcity_event:
  scarcity_id: null
  affected_material_refs: []
  affected_location_ids: []
  cause_state_ids: []
  visible_evidence: []
  severity_band: null
  substitute_options: []
  alternate_supplier_ids: []
  resolution_paths: []
  escalation_clock_ids: []
  expected_end_state: null
```

Valid narrative causes may include:
- route disruption;
- ecological damage;
- seasonal availability;
- settlement crisis;
- festival demand;
- institutional requisition;
- faction purchasing;
- specialist absence;
- workshop damage.

Do not spawn random shortages simply to force grinding.

## 16. Regional material identity

A region can be recognizable through what people make and use.

```yaml
regional_material_identity:
  region_id: null
  common_material_refs: []
  scarce_material_refs: []
  heritage_craft_tags: []
  current_industry_tags: []
  artisan_ids: []
  institution_ids: []
  ecological_constraints: []
  trade_partner_ids: []
  visual_style_tags: []
  public_memory_ids: []
```

Potential narrative uses:
- architecture and workshop visuals;
- festival goods;
- uniforms or accessories;
- packaging and signage;
- commissions;
- apprenticeship traditions;
- debates over resource extraction;
- restoration of nearly lost techniques.

Cosmetic identity is safe to develop earlier than mechanical item variants.

## 17. Economic actor pressure

A service provider or trading faction can create both benefit and disruption.

```yaml
economic_actor_pressure:
  actor_or_faction_id: null
  affected_location_ids: []
  services_added: []
  services_displaced: []
  price_pressure_claims: []
  supplier_dependencies: []
  employment_outputs: []
  opposition_ids: []
  public_benefits: []
  public_costs: []
```

Economic conflict should be rooted in concrete effects.

Examples:
- a large supplier makes medical goods reliable but weakens small shops;
- an artisan cooperative protects local expertise but cannot meet emergency demand;
- a new road lowers delivery risk but increases extraction pressure;
- a conservation restriction protects habitat but constrains a workshop's traditional material source.

## 18. Production professions as social networks

Crafting/economy-focused play should generate interactions.

A productive profession may create:
- supplier relationships;
- recurring customers;
- apprentices;
- professional rivals;
- quality disputes;
- commissions;
- institution contracts;
- event orders;
- emergency work;
- research collaboration;
- trade-route dependencies.

Currency can be an output, but it should rarely be the only output.

## 19. Pokémon participation in production

A Pokémon may contribute only through actual governed state.

Potential contribution classes:
- material production through a legal Capability;
- transport through legal movement/carrying capability;
- environmental access;
- search or detection;
- workshop assistance where fiction and rules support it.

Hard rules:
- verify the individual Pokémon's actual capability list;
- do not infer powers from flavor text alone;
- do not convert a capability into a new mechanical crafting bonus without rules support;
- persistent Pokémon entity memory can record social participation independently from mechanical effect.

## 20. Integration with existing Ouros layers

Chronicle:
Records significant creations, repairs, discoveries and transfers.

Settlement layer:
Workshops and residents contribute to settlement crafting/trade capability.

Faction layer:
Organizations can sponsor, control, disrupt or depend on supply routes and services.

Dungeon layer:
Recovered materials and artifacts preserve origin and extraction state.

Case layer:
An item can simultaneously be a trade good and evidence; evidence custody takes priority over ordinary transfer logic while the case requires it.

Public memory:
Historically important objects can become exhibits, awards, memorial pieces or disputed symbols.

Public events:
Festivals, tournaments and markets can create temporary commissions, vendors and demand state.

World Pulse:
Supply routes and workshops may change only when a causal actor/state supports the change and the result is legible to players.

## 21. Minecraft / Cobblemon mapping

Potential overworld representation:
- named workshop NPCs;
- physical workbench/facility locations;
- changing market stalls;
- storage rooms and delivery crates;
- signs showing temporary shortages or commissions;
- supplier caravans/transport NPCs where feasible;
- facility damage and repair variants;
- apprentice/worker schedule changes;
- regional visual craft motifs;
- displayed story-significant items;
- shipment arrivals that alter service availability.

The Minecraft layer should expose current state rather than run hidden economy math the player cannot understand.

## 22. Generation guardrails

1. Never invent a PTU recipe, item effect, crafting prerequisite, yield, repair effect or price.
2. Do not create arbitrary resource drops solely to feed a crafting loop.
3. Prefer materials already grounded in ecology, exploration, dungeons, jobs, settlement production or trade.
4. Track unique item instances only when their identity matters.
5. A missing service needs a causal reason.
6. Scarcity must be understandable and should usually have more than one response path.
7. Avoid making every workshop problem a fetch quest.
8. Artisans remain characters with motives, not vending machines.
9. Economic actors should usually provide real value as well as potential pressure.
10. Cosmetic craft identity must remain separate from mechanical bonuses.
11. A player without crafting expertise should still have valid routes through commissioning, trade, relationships or institutional services.
12. Do not use economy state to silently invalidate equipment a player already owns.

## 23. PTU / Caelo mechanical boundary

Before production, repair, gathering, item use or Pokémon-assisted work becomes executable, validate against the supplied project corpus and current AutoPTU implementation.

Validation can include:
- Trainer Classes, Features and Edges;
- Skill prerequisites;
- legal recipes;
- tool requirements;
- material requirements;
- action type and time;
- item effects and costs;
- Pokémon capabilities;
- repair behavior;
- inventory semantics;
- Caelo-specific homebrew intentionally retained;
- current AutoPTU item implementation.

This layer adds orchestration and provenance. It does not define a replacement crafting system.

## 24. Implementation priority

Recommended order:
1. item-instance tracking threshold;
2. provenance events;
3. workshop/service registry;
4. recipe-knowledge references;
5. production validation adapter;
6. commissions;
7. supply-route state;
8. scarcity events;
9. repair records;
10. artisan/apprenticeship state;
11. market-state summaries;
12. regional material identity.

This order adds narrative continuity around existing PTU items before attempting any deeper economic simulation.
