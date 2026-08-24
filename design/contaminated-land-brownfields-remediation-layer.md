# Ouros Contaminated Land, Brownfields & Remediation Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Date: 2026-08-24

## Purpose

This layer gives Ouros persistent state for contaminated or potentially contaminated land across investigation, cleanup, restricted use, long-term monitoring and redevelopment.

It coordinates existing Soil, Groundwater, Freshwater, Air Quality, Toxicology, Waste/Sanitation, Manufacturing, Architecture, Land Tenure, Conservation, Cases and Public Memory systems without replacing them.

It does not create PTU terrain, Poisoned, environmental damage, cleanup DCs, contaminant chemistry, legal liability or Minecraft physics.

## Core separation

Keep these records distinct:

```yaml
contaminated_site_boundary:
  site_id: null
  historical_use_refs: []
  suspected_source_refs: []
  medium_observation_refs: []
  conceptual_model_revision_ids: []
  investigation_area_ids: []
  remediation_project_ids: []
  residual_condition_ids: []
  land_use_control_ids: []
  monitoring_program_ids: []
  reuse_project_ids: []
  exposure_case_refs: []
  responsibility_case_refs: []
  battle_projection_id: null
```

A site can be suspected without being confirmed.

A contaminant can be confirmed in one medium without proving exposure.

A cleanup project can be complete while monitoring continues.

A site can be reused while historical restrictions remain.

A battle result never determines cleanup success or causal responsibility.

## 1. Persistent site identity

```yaml
contaminated_site:
  site_id: null
  location_id: null
  geometry_ref: null
  current_site_revision_id: null
  former_name_refs: []
  historical_use_refs: []
  structure_refs: []
  land_tenure_refs: []
  source_hypothesis_ids: []
  conceptual_model_revision_ids: []
  investigation_program_ids: []
  remediation_project_ids: []
  monitoring_program_ids: []
  current_use_state: null
  current_access_state: null
  public_information_refs: []
  archive_refs: []
  status: SUSPECTED|UNDER_INVESTIGATION|CONFIRMED|REMEDIATING|CONTROLLED|MONITORING|REUSED|ARCHIVED
```

`REUSED` does not erase `CONFIRMED` history.

The same site can move from factory -> abandoned parcel -> investigation -> cleanup -> park/research campus/housing/workshop district while retaining one `site_id`.

## 2. Historical use and source candidates

```yaml
site_historical_use:
  historical_use_id: null
  site_id: null
  use_type: null
  starts_at: null
  ends_at: null
  operator_or_actor_refs: []
  process_refs: []
  storage_asset_refs: []
  waste_stream_refs: []
  known_incident_refs: []
  evidence_refs: []
  confidence: null
```

Historical use is context, not proof of contamination.

```yaml
site_source_hypothesis:
  hypothesis_id: null
  site_id: null
  candidate_source_ref: null
  candidate_source_kind: PROCESS|TANK|PIPE|DRAIN|FILL|WASTE_AREA|POKEMON|OFFSITE_SOURCE|UNKNOWN
  candidate_agent_refs: []
  pathway_claims: []
  supporting_evidence_refs: []
  contradicting_evidence_refs: []
  status: OPEN|SUPPORTED|WEAKENED|REJECTED|UNRESOLVED
  last_reviewed_at: null
```

A Poison-type Pokémon can appear in `candidate_source_ref` only when there is actual evidence tying that individual/event to material found at the site.

## 3. Investigation areas

Do not treat an entire parcel as homogeneous.

```yaml
site_investigation_area:
  area_id: null
  site_id: null
  geometry_ref: null
  reason_for_scope: null
  medium_refs: []
  sample_location_refs: []
  source_hypothesis_refs: []
  current_assessment_state: UNKNOWN|CLEAN_SIGNAL|CONTAMINATION_SIGNAL|CONFIRMED_CONTAMINATION|MIXED
  data_gap_refs: []
  access_restriction_refs: []
```

Possible area scopes:

- former tank field;
- loading yard;
- drain line;
- fill zone;
- warehouse slab;
- rail siding;
- shoreline reach;
- downwind deposition area;
- groundwater monitoring transect;
- neighboring parcel potentially affected by migration.

One clean sample cannot clear an unobserved area.

## 4. Conceptual site model

This is a versioned hypothesis graph, not a deterministic contaminant simulator.

```yaml
site_conceptual_model_revision:
  revision_id: null
  site_id: null
  effective_at: null
  suspected_source_refs: []
  confirmed_source_refs: []
  medium_state_refs:
    soil: []
    groundwater: []
    surface_water: []
    air: []
    sediment: []
    building_material: []
  pathway_hypotheses: []
  receptor_scope_refs: []
  uncertainty_notes: []
  data_gap_refs: []
  supersedes_revision_id: null
  evidence_refs: []
  prepared_by: []
```

Examples of pathway hypotheses:

- leaking tank -> soil -> groundwater;
- former drain -> sediment -> river reach;
- contaminated fill -> dust during excavation;
- offsite plume -> groundwater beneath site;
- historical process residue -> enclosed building surfaces.

The graph may change after new samples without rewriting old observations.

## 5. Medium-specific observations

This layer references observations owned elsewhere.

```yaml
site_medium_observation_link:
  link_id: null
  site_id: null
  area_id: null
  medium: SOIL|GROUNDWATER|SURFACE_WATER|AIR|SEDIMENT|BUILDING_MATERIAL
  observation_ref: null
  sample_ref: null
  observed_at: null
  interpretation_state: SIGNAL|NO_SIGNAL|INCONCLUSIVE|PENDING
  relevant_agent_refs: []
```

Authoritative owners:

- Soil owns soil observations and condition.
- Groundwater owns well/plume observations.
- Freshwater owns surface water.
- Air Quality owns atmospheric state.
- Material Culture/Architecture own building materials where relevant.
- Toxicology owns samples only when used for exposure assessment.

## 6. Remediation project

```yaml
remediation_project:
  remediation_project_id: null
  site_id: null
  objective_refs: []
  target_area_ids: []
  target_agent_refs: []
  planned_reuse_ref: null
  action_type: EXCAVATION|REMOVAL|CAP|CONTAINMENT|STABILIZATION|IN_SITU_TREATMENT|DEWATERING|BUILDING_ABATEMENT|ACCESS_CONTROL|MONITORING_ONLY|OTHER
  project_revision: 1
  authorized_by_refs: []
  starts_at: null
  ends_at: null
  work_event_ids: []
  temporary_impact_refs: []
  verification_program_ref: null
  status: PROPOSED|AUTHORIZED|ACTIVE|PAUSED|COMPLETED|ABANDONED
```

Completion means the planned action was carried out. It does not mean the site is cleared for every use.

Temporary impacts can hand off to:

- Soil for compaction/erosion;
- Air Quality for dust;
- Road/Transit for truck traffic;
- Noise/Soundscapes for construction disturbance;
- Conservation/Wildlife for habitat displacement;
- Groundwater for pumping/dewatering;
- Public Space for access closures.

## 7. Residual conditions and land-use controls

Some cleanups can intentionally leave contamination isolated or controlled.

```yaml
residual_condition:
  residual_condition_id: null
  site_id: null
  area_id: null
  condition_kind: BURIED_RESIDUAL|CAPPED_AREA|STABILIZED_MATERIAL|MONITORING_REQUIRED|EXCAVATION_RESTRICTED|GROUNDWATER_USE_RESTRICTED|UNKNOWN
  effective_at: null
  basis_refs: []
  verification_refs: []
  review_due_at: null
  active: true
```

```yaml
site_use_control:
  control_id: null
  site_id: null
  geometry_ref: null
  prohibited_or_limited_activity: null
  reason_ref: null
  starts_at: null
  ends_at: null
  authority_ref: null
  public_notice_ref: null
  review_due_at: null
```

Do not invent legal powers. `authority_ref` must point to an institution already established by canon.

A Minecraft fence or sign can present a control, but cannot create one.

## 8. Verification and long-term monitoring

```yaml
site_verification_program:
  verification_program_id: null
  site_id: null
  remediation_project_ref: null
  objective_refs: []
  required_observation_refs: []
  schedule_refs: []
  result_revision_ids: []
  completion_state: ACTIVE|SATISFIED|UNSATISFIED|INCONCLUSIVE|SUPERSEDED
```

```yaml
site_monitoring_program:
  monitoring_program_id: null
  site_id: null
  monitor_asset_refs: []
  target_medium_refs: []
  target_agent_refs: []
  schedule_refs: []
  observation_refs: []
  maintenance_refs: []
  data_gap_refs: []
  status: ACTIVE|PAUSED|ENDED
```

A monitoring well that is dry, damaged or inaccessible creates a data gap rather than a false clean result.

## 9. Reuse and redevelopment

```yaml
site_reuse_project:
  reuse_project_id: null
  site_id: null
  proposed_use: null
  proponent_refs: []
  architecture_project_refs: []
  land_tenure_refs: []
  access_refs: []
  required_control_refs: []
  monitoring_dependency_refs: []
  current_phase: CONCEPT|REVIEW|CONSTRUCTION|OCCUPIED|ADAPTED|ENDED
  public_memory_refs: []
```

Candidate reuse categories:

- park/open space;
- ecological restoration;
- workshop/light industry;
- housing;
- transit/public works;
- research campus;
- market/community hall;
- shelter/emergency facility;
- museum/memorial/heritage reuse;
- mixed use.

Do not encode any category as automatically safe or unsafe.

## 10. Ecological occupation of contaminated sites

Abandoned industrial land may develop habitat value before cleanup.

```yaml
site_ecological_use_observation:
  observation_id: null
  site_id: null
  observed_at: null
  species_or_collective_refs: []
  habitat_use_type: ROOST|NEST|FORAGE|PASSAGE|REFUGE|UNKNOWN
  evidence_refs: []
  disturbance_context_refs: []
  interpretation_ref: null
```

Ecological use does not prove safety for humans.

Contamination does not prove absence of wildlife.

A cleanup project may need a Conservation/Wildlife handoff if remediation would disturb established habitat.

## 11. Pokémon-specific guardrails

Species such as Grimer, Muk, Trubbish, Garbodor, Koffing or Weezing may have authored relationships with waste or polluted places.

Do not infer from species alone:

- contamination source;
- cleanup capacity;
- cleanup rate;
- immunity to every site agent;
- ability to detect contamination;
- ownership by a facility;
- willingness to work;
- automatic spawn preference;
- population increase after contamination;
- PTU Status on nearby actors.

Any institutional Pokémon role must use Working Pokémon + Pokémon Agency.

Any actual toxic exposure must use Toxicology.

## 12. Minecraft/Cobblemon projection

Allowed presentation:

- fenced investigation area;
- capped mound;
- monitoring wells;
- excavated zone;
- temporary truck route;
- old foundations;
- stained or replaced surfaces;
- remediation equipment;
- redevelopment construction;
- signage and public information;
- habitat returning over time.

Forbidden authority direction:

- loaded block palette -> contamination truth;
- particle effect -> exposure;
- visible sludge -> Poisoned;
- removed barrels -> remediation complete;
- chunk reload -> old site revision restored;
- spawned Poison-types -> source attribution;
- player block placement -> cleanup verification.

World state projects into Minecraft, never the reverse without a validated world-state action.

## 13. Encounter contracts

### Brownfield Survey Perimeter — FULL

Premise: investigators are sampling a former industrial parcel while wild Pokémon use a partially reclaimed edge. A confrontation occurs when activity overlaps a restricted section.

Required capability families:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including interception/forced movement if technicians or wildlife need dynamic withdrawal/crossing;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle only if exact supported status effects occur;
- terrain/weather/hazards/zones/reactions if contamination, debris, dust or protected lanes become tactical mechanics;
- move-specific behavior as used;
- abilities as used;
- items if PPE/equipment becomes mechanical;
- Trainer Features/perks if invoked;
- AI legal-action infrastructure;
- AI tactical policy for WITHDRAW, PROTECT_TECHNICIAN, CLEAR_ROUTE;
- Minecraft/Cobblemon/Craftics adapter/playback.

REDUCED:

Resolve sampling, restricted access and wildlife withdrawal in world state. Freeze a clean static arena outside the contaminated work zone. AutoPTU resolves only the independent confrontation. No contamination mechanics are introduced.

### Cap Inspection After Storm — FULL

Premise: a storm exposes damage near a capped legacy site while maintenance workers inspect the perimeter.

Additional dependencies if retained tactically:

- terrain/weather/hazards/zones/reactions for dynamic rain, damaged cap, mud or restricted zones;
- complete movement for evacuation/route changes;
- AI tactical policy for PROTECT_WORKER, WITHDRAW, REACH_EXIT.

REDUCED:

The world-state layer closes the affected sector and establishes a safe staging area. Any battle occurs there with no storm, mud, cap-failure or toxic effects in the grid.

### Redevelopment Utility Trench — FULL

Premise: construction on a reused site uncovers unexpected buried material and a confrontation interrupts the shutdown.

Required rich dependencies:

- complete movement for workers/actors leaving the trench;
- terrain/weather/hazards/zones/reactions only if trench geometry or material has tactical effects;
- AI tactical policy for EVACUATE and CLEAR_ROUTE;
- adapter/playback.

REDUCED:

Stop excavation, evacuate workers and secure the material in world state. Battle, if any, occurs on a dry static surface away from the discovery. Investigation continues afterward.

### Site Reuse Review

Primarily non-combat.

Inputs can include contamination observations, verification state, community proposals, land-use controls, habitat observations and access needs.

Valid outcome: `REUSE_DECISION_DEFERRED_PENDING_DATA`.

## 14. Long-term Chronicle behavior

A contaminated site can produce meaningful history without repeated combat:

- old industrial records discovered years later;
- monitoring networks gain or lose coverage;
- cleanup methods change as new evidence appears;
- habitat colonizes vacant land;
- a cap requires routine maintenance;
- an old access restriction becomes unnecessary and is retired;
- redevelopment changes traffic and public space;
- a new trench reveals a previously unknown source area;
- historical responsibility remains disputed while cleanup proceeds;
- a former industrial parcel becomes a civic landmark whose earlier history remains visible.

Routine monitoring should compress unless a threshold, anomaly, outage, new observation or decision occurs.

## 15. Non-inferences

This layer does not authorize:

- Poisoned/Badly Poisoned from environmental description;
- custom contamination damage;
- contamination immunity by Type;
- Factory/Rough Terrain from site identity;
- movement penalties from debris or sludge;
- accuracy penalties from dust;
- automatic Gas Mask/PPE effects;
- purification by Grimer/Weezing or other species;
- cleanup progress from KO/capture;
- criminal liability from contamination;
- safe reuse from visual redevelopment;
- rare-spawn changes from contamination or cleanup;
- player-created toxic sites through arbitrary block placement.

## 16. Canon questions to resolve later

- Which Ouros settlements have legacy industrial parcels at campaign start?
- Which historical industries and waste practices are canon?
- Which institutions can investigate, restrict access, approve remediation or certify reuse?
- Are any contaminated sites linked to existing factions, or should many remain mundane historical problems?
- Which sites already have ecological value despite their industrial history?
- What level of public disclosure exists for monitoring data?
- How much contaminant detail should remain qualitative?
- Which Pokémon have authored waste/pollution relationships in specific regions?
- Does Caelo define any environmental protection equipment or toxic-environment rules beyond base PTU material?
- How should player-owned businesses interact with redevelopment without inventing liability law?