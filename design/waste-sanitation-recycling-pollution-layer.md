# Ouros Waste, Sanitation, Recycling & Pollution Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

Ouros already models infrastructure, conservation, crises, workplaces, material provenance, food systems, care, ecology and public works. This layer owns the end-of-material-life and sanitation state that connects those systems: waste generation, collection, transfer, treatment, recycling/reuse, residues, wastewater, contamination observations, cleanup and waste-associated Pokémon activity.

It does not define environmental damage, poison exposure, sanitation law or universal waste-processing Pokémon abilities.

## 1. Keep the important truths separate

Ouros should maintain separate state for:

- physical material or waste stream;
- provenance/source history;
- custody and ownership claims;
- collection/service status;
- treatment/process status;
- output/residue stream;
- contamination observation;
- causal diagnosis;
- ecological response;
- public belief/media framing;
- policy/authorization claims;
- PTU mechanical state.

Visible garbage does not prove toxic exposure. A clean-looking stream does not prove safe water. A Grimer near a drain does not prove that Grimer caused contamination. A cleanup operation does not remove a PTU status from a combatant.

## 2. Waste stream

A meaningful disposed material should remain traceable when it matters.

```yaml
waste_stream:
  waste_stream_id: null
  material_class: null
  source_actor_ids: []
  source_institution_ids: []
  source_event_ids: []
  provenance_batch_ids: []
  generated_at: null
  current_location_id: null
  current_container_or_asset_id: null
  custody_claim_ids: []
  ownership_claim_ids: []
  quantity_band: unknown
  containment_state: unknown
  segregation_state: unknown
  recoverable_material_claims: []
  hazard_claim_ids: []
  downstream_process_ids: []
  public_visibility: unknown
  canon_status: proposed
```

Candidate descriptive material classes:

- household refuse;
- food-service organics;
- agricultural residue;
- construction/demolition material;
- workshop scrap;
- research/laboratory discard;
- medical-service discard;
- event/festival refuse;
- packaging;
- wastewater/sludge;
- industrial residue;
- mixed unknown material;
- recovered/reusable material.

These are narrative categories. They do not create legal or PTU hazard classes.

## 3. Sanitation service

Collection is a service, not a cleanliness meter.

```yaml
sanitation_service:
  sanitation_service_id: null
  operator_institution_id: null
  service_area_ids: []
  accepted_stream_classes: []
  excluded_or_special_handling_claims: []
  collection_route_ids: []
  schedule_band: null
  normal_capacity_band: null
  current_capacity_band: null
  backlog_state: none
  vehicle_or_asset_ids: []
  staff_role_ids: []
  supporting_pokemon_ids: []
  transfer_site_ids: []
  treatment_destination_ids: []
  disruption_ids: []
  public_information_packet_ids: []
```

Capacity can degrade because of route closure, staffing, equipment, event surge, treatment failure or other explicit causes.

Do not assume a strike, sabotage or negligence when a backlog exists.

## 4. Transfer and treatment sites

Treatment changes material state and creates outputs.

```yaml
treatment_site:
  treatment_site_id: null
  site_type: null
  location_id: null
  operator_id: null
  input_stream_ids: []
  process_claim_ids: []
  output_stream_ids: []
  residue_stream_ids: []
  operational_state: unknown
  capacity_band: unknown
  monitoring_record_ids: []
  maintenance_asset_ids: []
  bypass_or_overflow_event_ids: []
  ecological_interface_ids: []
  worker_role_ids: []
```

Possible descriptive site types:

- transfer station;
- sorting facility;
- reuse/recycling workshop;
- composting site;
- wastewater treatment facility;
- industrial treatment plant;
- contained disposal site;
- legacy closed disposal site;
- temporary crisis collection point.

Exact engineering process is authored per site. The generator must not invent treatment chemistry or efficiency.

## 5. Material transformation and recycling

Processing should preserve lineage.

```yaml
material_transformation:
  transformation_id: null
  input_batch_ids: []
  process_site_id: null
  process_event_id: null
  operator_ids: []
  output_batch_ids: []
  residue_batch_ids: []
  rejected_input_ids: []
  quality_claim_ids: []
  evidence_ids: []
  mechanical_crafting_refs: []
```

This connects to the existing Material Culture/Crafting layer.

A recovered steel batch may later become a crafted object. The crafting system still owns legal recipes, quantities and effects.

## 6. Wastewater and sanitation networks

Wastewater should remain separate from drinking-water supply even when both share infrastructure dependencies.

```yaml
wastewater_flow_state:
  flow_state_id: null
  source_zone_ids: []
  network_id: null
  treatment_site_id: null
  normal_destination_ids: []
  current_destination_ids: []
  flow_state: normal
  bypass_active: false
  overflow_event_ids: []
  monitoring_ids: []
  downstream_location_ids: []
```

Possible readable states:

- NORMAL
- DEGRADED
- CAPACITY_LIMITED
- BYPASS_CONTROLLED
- OVERFLOW_UNCONTROLLED
- ISOLATED
- UNDER_REPAIR
- UNKNOWN

These states do not define battle hazards.

## 7. Contamination observation

Observation and diagnosis must remain separate.

```yaml
contamination_observation:
  observation_id: null
  location_id: null
  medium: null
  observed_at: null
  observer_ids: []
  indicator_type: null
  indicator_description: null
  sample_ids: []
  instrument_record_ids: []
  visual_record_ids: []
  comparison_baseline_ids: []
  confidence_band: null
  possible_cause_claim_ids: []
  confirmed_cause_ids: []
  health_case_refs: []
  ecology_observation_refs: []
```

Candidate media:

- water;
- soil/sediment;
- air;
- built surface;
- food-contact area;
- habitat substrate;
- unknown/mixed.

Do not convert an odor, discoloration, dead vegetation, Pokémon absence or illness report directly into a confirmed contaminant.

## 8. Pollution source claims

Use the existing evidence/case architecture.

```yaml
pollution_source_claim:
  claim_id: null
  affected_location_ids: []
  suspected_source_ids: []
  pathway_claim_ids: []
  evidence_for_ids: []
  evidence_against_ids: []
  alternative_claim_ids: []
  status: hypothesis
  confirmed_event_id: null
```

A discarded item with a clinic logo does not prove that the clinic dumped it. It may have been lost in transit, stolen, reused or moved later.

## 9. Cleanup project

Cleanup is a project with verification.

```yaml
cleanup_project:
  cleanup_project_id: null
  affected_location_ids: []
  confirmed_pressure_ids: []
  responsible_actor_ids: []
  source_control_steps: []
  removal_or_containment_steps: []
  recovered_material_ids: []
  residue_destination_ids: []
  habitat_restoration_project_ids: []
  monitoring_window_ids: []
  verification_observation_ids: []
  current_phase: assess
  status: proposed
  unresolved_risks: []
```

Candidate phases:

- assess;
- identify/source-control;
- contain;
- remove/recover;
- treat;
- restore;
- monitor;
- verify;
- handoff to routine service.

Removing visible waste may complete removal while verification remains open.

## 10. Sanitation incidents and backlogs

```yaml
sanitation_incident:
  incident_id: null
  service_or_site_ids: []
  first_observed_at: null
  incident_type: null
  observed_effect_ids: []
  confirmed_cause_ids: []
  affected_route_ids: []
  affected_service_ids: []
  ecological_response_ids: []
  public_information_ids: []
  response_action_ids: []
  recovery_project_ids: []
```

Candidate incident types:

- missed collection;
- route interruption;
- transfer-site congestion;
- sorting contamination;
- treatment outage;
- controlled bypass;
- overflow;
- containment failure;
- illegal/unknown dumping claim;
- storm-distributed debris;
- legacy-site exposure;
- unknown.

## 11. Urban scavenger and waste-associated Pokémon

Waste can become an ecological resource.

```yaml
waste_pokemon_interaction:
  interaction_id: null
  pokemon_entity_ids: []
  collective_ids: []
  waste_stream_ids: []
  location_id: null
  observed_behavior: null
  observed_at: null
  repeated_observation_ids: []
  ecological_effect_claim_ids: []
  service_effect_claim_ids: []
  intervention_ids: []
  authoritative_species_refs: []
```

Possible observed behaviors:

- feeding/foraging;
- nesting nearby;
- carrying material;
- avoiding a stream;
- repeated visitation;
- blocking access;
- cooperating with staff;
- unknown association.

Do not infer disease, hostility, willingness to work, ownership, ecological benefit or contamination source from species identity.

## 12. Pokémon integrated into sanitation work

Official Pokémon material provides a precedent for Alolan Grimer being used at garbage-disposal facilities. Ouros may author comparable institutional relationships only where canon explicitly supports them.

A supporting Pokémon record should connect to the existing workplace and Pokémon-agency layers:

```yaml
sanitation_pokemon_role:
  pokemon_entity_id: null
  institution_id: null
  role_description: null
  observed_tasks: []
  residence_state_id: null
  custody_or_registration_refs: []
  cooperation_history_ids: []
  refusal_or_change_events: []
  PTU_capability_refs: []
  canon_basis_ids: []
```

No mechanical processing amount, immunity, productivity or disposal bonus may be generated from flavor alone.

## 13. Event and tourism surges

Festivals, tournaments, tourism or crises can temporarily change waste composition and volume.

The event layer owns attendance. This layer may derive sanitation pressure from:

- venue capacity;
- service plan;
- observed material volume bands;
- collection schedule;
- treatment capacity;
- transport disruption.

Do not create a sanitation crisis merely because an event exists.

## 14. Circular material economy

Reuse can connect waste streams back to material culture.

Possible loops:

- bottle/container return;
- repair and resale;
- construction-material salvage;
- workshop scrap recovery;
- compost/organic reuse where authored;
- packaging reuse;
- textile repair;
- decommissioned machinery parts;
- reclaimed exhibit/building material.

Economic prices and crafting yields remain under their authoritative systems.

## 15. Minecraft representation

Minecraft can show sanitation state through coarse, causally grounded changes:

- bins/collection points;
- temporary piles or containers;
- collection vehicles/NPC crews;
- transfer/treatment facilities;
- blocked drains;
- booms/barriers;
- changed water appearance where safe to represent;
- cleanup scaffolding/signage;
- sorting/reuse workshops;
- closed legacy disposal sites;
- wildlife presence changes when supported by ecology state.

Avoid representing every unit of waste as a persistent item entity.

World visuals must not become the PTU hazard authority.

## 16. Offline advancement

Routine collection can compress while players are offline.

Offline simulation should use coarse state transitions such as:

NORMAL → DELAYED → BACKLOG → RECOVERY

or

TREATING → MONITORING → VERIFIED

It should not simulate every truck, item, microbial process or Pokémon feeding event.

Major irreversible discoveries, accusations or PC-owned item disposal should require appropriate authored/player authority.

## 17. Encounter contract — Overflow at Southworks

Narrative premise:

A treatment-site overflow changes downstream world state while staff attempt to isolate one channel. Displaced wild Pokémon appear near the maintenance access route.

Reduced version:

Resolve the overflow, flow routing and contamination as overworld/world state. Use a dry, static maintenance platform for any unavoidable battle. Only the immediate hostile subgroup enters the grid. Do not apply environmental Poison automatically.

Full version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if evacuation, displacement or current effects occur in-grid;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if an exact validated status is used;
- terrain/weather/hazards/zones/reactions — BLOCKING for contaminated-water zones, toxic areas or changing flow;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for WITHDRAW/PROTECT/ISOLATE objectives;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

## 18. Encounter contract — Transfer Station Jam

Narrative premise:

A collection backlog blocks service access while waste-associated wild Pokémon forage around the transfer yard. Workers need the vehicle route restored.

Reduced version:

Represent containers and waste piles as static nonhazardous blockers on a legal arena. Keep workers, sorting activity and collection routing outside the battle grid. Run a conventional encounter only if a subgroup becomes aggressive.

Full version adds:

- dynamic route-clearing objective;
- workers/vehicles moving through the site;
- Pokémon approach/withdrawal behavior;
- movable material or gates;
- possible validated hazards if the source rules support them.

The full version remains blocked mainly by complete movement, broad terrain/hazard/reaction support, tactical AI and adapter/playback.

## 19. Encounter contract — River Boom Recovery

Narrative premise:

A storm damages a debris-containment boom and floating material starts entering a habitat corridor. Players assist recovery while wildlife responds to the disturbance.

Reduced version:

Resolve currents, debris collection and boom repair in overworld state. If combat occurs, use a stable bank/dock arena. Never use current or debris damage unless authoritative mechanics exist.

Full version dependencies add:

- terrain/weather/hazards/zones/reactions — BLOCKING for current/debris zones;
- complete movement — BLOCKING for forced drift/interception;
- AI tactical policy — BLOCKING for CROSS/WITHDRAW/PROTECT behavior;
- adapter/playback — BLOCKING for live debris and water-state synchronization.

## 20. Critical non-inference gates

Never infer any of the following:

- pollution applies Poison status;
- Garbodor/Grimer can delete arbitrary waste;
- a Poison-type Pokémon is safe in every contaminant;
- a sanitation worker profession grants Technology Education, Medicine, Survival or Features;
- a visible cleanup means environmental recovery is complete;
- absence of visible litter proves safe water/soil;
- presence of Trubbish/Grimer/Garbodor proves illegal dumping;
- a waste backlog proves negligence or sabotage;
- recycling creates a mechanically legal crafting ingredient without validation;
- wastewater treatment creates potable water automatically;
- a cleanup changes Cobblemon spawns until the ecology/adapter systems support that writeback.

## 21. Canon promotion questions

Before any sanitation proposal becomes canon, decide:

- which settlements have collection, sewer and treatment systems;
- what technology level each region uses;
- which waste streams require special handling;
- who operates sanitation services;
- what kinds of dumping/ownership/access rules exist, if any;
- whether and how Pokémon participate in sanitation work;
- how water-quality observations are represented;
- how service capacity advances offline;
- which cleanup projects can change ecology/spawns;
- what PTU/Caelo rules govern actual environmental exposure;
- what Minecraft/Cobblemon hooks can show the state without duplicating PTU mechanics.
