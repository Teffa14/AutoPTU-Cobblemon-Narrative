# Ouros Volcanic Monitoring, Eruption & Ashfall Recovery Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This extension preserves persistent world state around volcanic monitoring, unrest observations, eruption observations, ashfall observations, notices, access decisions and post-event reassessment.

It does not create a generic volcano simulator. It does not define where active volcanoes exist in Ouros. It does not create tactical lava, ash, gas, heat, lahar, collapse or eruption rules.

Existing authorities remain intact:

- Geology owns volcanic sites, formations, geological context and site disturbance.
- Weather owns meteorological observations and forecasts.
- Seismic Monitoring owns earthquake/seismic observation records.
- Crisis/Rescue owns evacuations, rescue operations and casualty-response workflows.
- Public Notices / Communications own dissemination channels and receipt evidence.
- Roads, Rail, Aviation, Maritime and Travel own their service/access state.
- Power, Water, Agriculture, Care, Pollution, Facilities and other downstream systems own their consequences and restoration.
- AutoPTU owns tactical legality and resolution.
- Ouros owns world facts and combatant selection.

## 1. Volcanic system identity

```yaml
volcanic_system:
  volcanic_system_id: null
  geological_site_ids: []
  region_ids: []
  authored_activity_class_ref: null
  monitoring_network_ids: []
  known_historical_episode_ids: []
  public_name_ids: []
  scientific_name_ids: []
  stewardship_or_access_actor_ids: []
  current_assessment_id: null
  canon_status: proposed
```

`authored_activity_class_ref` must point to an approved setting classification if one exists. Narrative generation cannot decide that a mountain is active, dormant, extinct or dangerous from visual appearance.

## 2. Monitoring node

```yaml
volcanic_monitoring_node:
  node_id: null
  volcanic_system_id: null
  location_id: null
  operator_actor_ids: []
  observation_method_refs: []
  operational_state: UNKNOWN
  coverage_claim_ids: []
  last_observation_ids: []
  maintenance_ref_ids: []
  communications_ref_ids: []
  provenance_refs: []
```

Candidate operational states:

- OPERATING
- DEGRADED
- OFFLINE
- ACCESS_BLOCKED
- DATA_DELAYED
- STATUS_UNKNOWN

An operating node proves only that the authored node is operational. It does not prove complete monitoring coverage.

## 3. Volcanic observation

```yaml
volcanic_observation:
  observation_id: null
  volcanic_system_id: null
  node_or_observer_id: null
  location_id: null
  observed_at: null
  observation_type_ref: null
  observed_value_or_band_ref: null
  confidence_or_quality_ref: null
  raw_evidence_ids: []
  interpreted_by_assessment_ids: []
  provenance_refs: []
```

Observation types must be authored. Possible descriptive examples, only when supported by setting technology and evidence, include visible plume, unusual sound, ground change, thermal observation, gas observation, ash observation, water-system change or instrument reading.

An observation is evidence. It is not automatically a cause, prediction or hazard declaration.

## 4. Activity assessment

```yaml
volcanic_activity_assessment:
  assessment_id: null
  volcanic_system_id: null
  issuer_actor_or_institution_id: null
  issued_at: null
  source_observation_ids: []
  assessed_activity_band_ref: null
  uncertainty_band: null
  interpretation_claim_ids: []
  consequence_claim_ids: []
  supersedes_assessment_id: null
  superseded_by_assessment_id: null
  provenance_refs: []
```

Suggested generic uncertainty states:

- LOW
- MODERATE
- HIGH
- CONFLICTING_EVIDENCE
- INSUFFICIENT_DATA
- NOT_ASSESSED

Do not import real-world alert labels or thresholds unless canon explicitly chooses them.

Old assessments remain queryable. Later evidence should supersede, not silently rewrite, what an institution believed earlier.

## 5. Volcanic episode

```yaml
volcanic_episode:
  episode_id: null
  volcanic_system_id: null
  start_observation_ref: null
  end_or_transition_observation_ref: null
  episode_type_ref: null
  confirmed_event_state: UNCONFIRMED
  observation_ids: []
  assessment_ids: []
  affected_area_claim_ids: []
  ashfall_observation_ids: []
  downstream_handoff_ids: []
  access_decision_ids: []
  recovery_review_ids: []
  public_memory_ids: []
  provenance_refs: []
```

Possible `confirmed_event_state` values:

- UNCONFIRMED
- OBSERVED
- UNDER_REVIEW
- CONFIRMED
- REVISED
- CLOSED_FOR_CURRENT_REVIEW

The episode object records the information and history around the event. It does not calculate volcanic physics.

## 6. Ashfall observation

```yaml
ashfall_observation:
  ashfall_observation_id: null
  episode_id: null
  location_id: null
  observed_at: null
  observer_id: null
  presence_state: UNKNOWN
  qualitative_band_ref: null
  sample_or_media_evidence_ids: []
  confidence_ref: null
  downstream_handoff_ids: []
  provenance_refs: []
```

Presence states:

- OBSERVED_PRESENT
- OBSERVED_ABSENT
- POSSIBLE
- UNKNOWN
- REPORT_DISPUTED

A report of no ash can be useful for reconstructing an observed footprint.

Never infer health effects, crop damage, water contamination, engine damage, route closure or visibility penalties solely from `OBSERVED_PRESENT`.

## 7. Airborne material claim

Airborne plume observations should remain distinct from ground deposition.

```yaml
airborne_material_claim:
  claim_id: null
  episode_id: null
  observation_time: null
  observed_from_location_ids: []
  claimed_area_or_direction_refs: []
  observation_evidence_ids: []
  issuer_id: null
  confidence_ref: null
  superseded_by_claim_id: null
```

This object is informational. Aviation or Weather may use the claim as evidence, but those systems own operational decisions.

## 8. Notice and receipt boundary

```yaml
volcanic_notice_handoff:
  handoff_id: null
  assessment_id: null
  notice_owner_system_ref: null
  notice_packet_id: null
  intended_recipient_ids: []
  transmitted_at: null
  receipt_evidence_ids: []
  acknowledgement_ids: []
```

Keep these facts separate:

```text
observation recorded
assessment issued
notice authorized
notice transmitted
notice received
notice acknowledged
recipient action taken
```

A scientific assessment does not close a road. A road authority may use it as evidence for its own decision.

## 9. Access sector

```yaml
volcanic_access_sector:
  sector_id: null
  volcanic_system_id: null
  location_ids: []
  route_refs: []
  owner_system_refs: []
  current_access_claim_ref: null
  inspection_ref_ids: []
  restriction_ref_ids: []
  last_verified_at: null
```

The volcanic layer may link to access decisions but should not overwrite route, tourism, facility or protected-area authority.

One summit sector can be restricted while a lower settlement remains open.

## 10. Downstream consequence handoff

```yaml
volcanic_downstream_handoff:
  handoff_id: null
  episode_id: null
  observation_or_assessment_ids: []
  receiving_system_ref: null
  receiving_subject_ids: []
  handoff_state: SENT
  received_at: null
  resulting_owner_event_ids: []
```

Potential receiving systems:

- roads/travel;
- aviation;
- maritime;
- rail;
- power;
- communications;
- drinking water;
- stormwater;
- agriculture/food;
- care/public health;
- pollution/environmental response;
- wildlife/conservation;
- tourism/events;
- schools/workplaces;
- housing;
- facility maintenance.

The receiving system decides its own state.

## 11. Post-event assessment

```yaml
volcanic_post_event_assessment:
  review_id: null
  episode_id: null
  location_or_sector_ids: []
  reviewer_ids: []
  inspected_at: null
  observation_ids: []
  unresolved_question_ids: []
  safe_access_claim_ids: []
  downstream_review_handoffs: []
  next_review_ref: null
  provenance_refs: []
```

The end of visible activity does not complete post-event assessment.

A sector can need reassessment even after the volcanic activity assessment has decreased.

## 12. Recovery sequence

```yaml
volcanic_recovery_sequence:
  recovery_sequence_id: null
  episode_id: null
  monitoring_state_refs: []
  access_review_refs: []
  owner_system_recovery_refs: []
  temporary_arrangement_ids: []
  public_notice_refs: []
  current_phase: OBSERVATION_CONTINUES
  completed_phase_ids: []
```

Candidate descriptive phases:

- OBSERVATION_CONTINUES
- INITIAL_ASSESSMENT
- LIMITED_ACCESS_REVIEW
- DOWNSTREAM_INSPECTIONS
- PARTIAL_REOPENING
- NORMALIZATION_REVIEW
- LONG_TERM_MONITORING
- HISTORICAL_CLOSEOUT

These phases organize narrative continuity. They do not grant authority or mechanically reopen anything.

## 13. Historical episode and legacy landscape

```yaml
volcanic_legacy_event:
  legacy_event_id: null
  volcanic_system_id: null
  episode_id: null
  historical_location_ids: []
  deposit_or_landscape_claim_ids: []
  route_change_ids: []
  settlement_change_ids: []
  habitat_change_ids: []
  institution_change_ids: []
  public_memory_ids: []
  archive_refs: []
```

Old eruptions can explain why a road bends, why a district ends at a ridge, why a monitoring post exists, why a farm uses a local practice or why a habitat shifted. Historical causation must come from authored records or approved canon, not procedural inference.

## 14. Pokémon behavior boundary

```yaml
pokemon_volcanic_behavior_observation:
  observation_id: null
  pokemon_entity_id: null
  species_ref: null
  location_id: null
  observed_at: null
  observed_behavior_ref: null
  observer_ids: []
  linked_episode_id: null
  interpretation_claim_ids: []
  provenance_refs: []
```

This can preserve a specific Absol leaving a ridge, a flock changing roosts or a Fire-type collective moving into a cooled field.

It does not grant species-wide eruption sensing, immunity, causation or forecasting.

## 15. Attribution discipline

Keep four layers distinct:

```text
what happened
what was observed
what an actor believed caused it
what current approved canon establishes as cause
```

Narrative generation must never collapse temporal correlation into blame.

This supports stories where residents, scientists, guides and players hold different evidence without forcing one side into bad faith.

## 16. Monitoring gaps

A missing observation is meaningful state.

```yaml
volcanic_monitoring_gap:
  gap_id: null
  volcanic_system_id: null
  affected_node_ids: []
  affected_time_window: null
  known_missing_observation_types: []
  cause_claim_ids: []
  restoration_refs: []
  interpretation_constraints: []
```

Do not backfill a gap with invented readings.

An offline station does not prove that nothing happened during the interval.

## 17. World-generation rules

Generate volcanic content only when the location graph or canon supports a volcanic/geothermal context.

Good generated situations:

- conflicting observations from separate locations;
- an old notice still posted after a newer assessment;
- a route reopened while a research sector remains restricted;
- a community comparing a current episode to older archive evidence;
- a Pokémon behavior report that becomes folklore before causation is understood;
- ash observations arriving after transport decisions were already made;
- a monitoring gap caused by ordinary maintenance or communications failure;
- a temporary observation post becoming a lasting community institution.

Avoid procedural eruption spam. Most visits to a volcanic region should support ordinary life, ecology, travel, work, science and social continuity.

## 18. Dungeon and exploration design

Volcanic exploration should expose persistent stages, not arbitrary lava puzzles.

Possible authored stages:

- settled lower slope;
- old flow or ash landscape;
- monitoring route;
- historical observation shelter;
- restricted upper sector;
- crater-adjacent observation area;
- abandoned route exposed by an older event.

Each stage can have access, knowledge, observation and archive state.

Dynamic hazards require exact mechanics. Until then, changing lava, ash clouds, unstable ledges and eruption phases remain outside the tactical simulation.

## 19. Encounter contract — Monitoring Ridge Withdrawal

Narrative premise:

A monitoring team is leaving a ridge after access is restricted. A hostile or distressed encounter threatens the final withdrawal route.

FULL intended dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL when Intercept, escort or forced displacement matters
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL for timed withdrawal
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING for generalized reactions, ash/heat/unstable-ground effects or changing restricted areas
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for withdrawal/protection behavior
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

Reduced version:

The volcanic condition stabilizes before BattleSpec creation. Monitoring staff leave the grid through overworld state. Active vents, ash, equipment and unstable terrain remain outside the tactical arena. AutoPTU receives a static reviewed ridge clearing and explicit combatants. Victory can establish `IMMEDIATE_RIDGE_ROUTE_SECURED`. Scientific assessment and access restrictions remain separate workflows.

## 20. Encounter contract — Ashfall Shelter Perimeter

Narrative premise:

After an ashfall observation, several actors are moving toward an already-authored shelter or service point while a separate encounter threatens the perimeter.

FULL intended dependencies:

- verified targeting/base movement/core/action economy remain usable;
- complete movement: PARTIAL for protection/Intercept/forced movement;
- turn lifecycle: PARTIAL if arrival windows matter;
- damage/status: PARTIAL when exact legal effects apply;
- terrain/weather/hazards/zones/reactions: BLOCKING for ash visibility, exposure, accumulation, reactions or changing zones;
- tactical policy: BLOCKING for protection/withdrawal objectives;
- adapter/playback: BLOCKING;
- move/ability/item/Trainer Feature families: PARTIAL and require exact registrations.

Reduced version:

Ashfall itself is overworld state and has already ceased or the tactical area is an inspected covered space. Civilians and controlled service operations remain outside BattleSpec. Combat occurs in a static perimeter. Victory secures access only; it does not determine medical safety, road status, ash cleanup or building occupancy.

## 21. Encounter contract — Old Flow Observation Route

Narrative premise:

Players investigate conflicting records along a hardened historic flow boundary. A wild or adversarial encounter occurs on a route that is currently stable.

FULL intended dependencies:

If the route includes collapsing crust, active heat, gas, moving magma or delayed environmental phases, it depends on the BLOCKING environmental family plus PARTIAL movement/damage/status/turn lifecycle as applicable.

Reduced version:

The old flow field is geologically stable and tactically inert. Use only verified static geometry and ordinary legal combat. Historic deposits, maps and observations remain investigation/world-state objects outside combat.

## 22. PTU/Caelo mechanical boundary

Current evidence does not verify a universal contract for:

- natural eruption timing;
- volcanic alert thresholds;
- ash visibility penalties;
- ash inhalation or respiratory statuses;
- lava or magma damage;
- proximity heat damage;
- volcanic-gas damage/status;
- lahar or flow forced movement;
- crater-edge collapse;
- falling ejecta or volcanic-bomb damage;
- ash accumulation changing movement;
- automatic Fire/Ground-type immunity or resistance to environmental hazards;
- eruption sensing by species;
- Move/Ability/Item/Trainer Feature-driven volcanic control without an exact rule;
- structural damage from eruption;
- evacuation/rescue objective semantics.

Keep these UNKNOWN until both governing rules and implementation evidence exist.

## 23. Minecraft/Cobblemon/Craftics boundary

Presentation can reuse:

- volcanic terrain and structures;
- authored ash/frost-like overlays or particles;
- smoke/steam visuals;
- monitoring huts and instruments;
- barriers and signs;
- old flow fields;
- NPC crews;
- Pokémon models/forms/poses/animations/cries;
- lighting, sounds and particles;
- UI, networking, tracking and persistence hooks.

Presentation cannot become rules authority.

- Lava blocks do not execute PTU damage by default.
- Fire blocks do not automatically inflict Burn.
- Smoke or ash particles do not create status or LoS penalties.
- Minecraft weather does not create volcanic ashfall.
- Falling blocks do not execute PTU damage/collapse rules.
- Native knockback does not execute PTU forced movement.
- A Pokémon standing in lava does not prove immunity under PTU/Caelo.
- Redstone does not establish monitoring truth or notice authority.
- Cobblemon BattleState/controller logic does not select combatants or decide legality, HP/status, positions or outcomes.

Ouros owns world facts and combatant selection. AutoPTU owns tactical legality and resolution. Minecraft/Cobblemon/Craftics presents authoritative outcomes.

## 24. Canon status

Everything in this extension is PROPOSED unless an existing approved canon record says otherwise.

This pass adds no volcano, eruption, institution, technology, historical disaster, settlement or Pokémon capability to canon.

## 25. Open canon questions

- Which volcanic systems exist in Ouros, and what is their approved activity history?
- Which settlements, routes, farms, resorts, sacred sites or habitats depend on them?
- What monitoring technologies exist by region?
- Who owns scientific assessment, public notice and access restriction authority?
- What historical episodes changed settlement or route geography?
- How are ash observations collected and archived?
- Are geothermal energy or hot-spring systems established anywhere?
- Which individual Pokémon have documented site relationships?
- Which folklore traditions exist around volcanic behavior, and what evidence supports or contradicts them?
