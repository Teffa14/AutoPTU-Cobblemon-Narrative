# Ouros Extreme Heat & Cooling Access Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Date: 2026-08-29

## Purpose

This extension preserves the operational continuity of unusual or prolonged heat when a canonized region experiences it.

It connects weather evidence to decisions about route use, public activity, cooling/shade access, temporary support and staged recovery without becoming a second Weather, Care, Electric Grid, Drinking Water, Public Space, Workplace, Travel or Crisis system.

The central design rule is that heat-related evidence, operational response, health state and tactical mechanics remain separate authorities.

## Existing owners

Weather owns observations, forecasts, notices and forecast revision.

Seasonality owns expected climate and phenology.

Care owns individual health observations, diagnosis, treatment and recovery.

Community Health owns aggregate health signals and investigations.

Electric Grid owns electrical service and restoration evidence.

Drinking Water owns potable-water service state.

Facility Maintenance owns faults, repair and technical verification.

Travel owns journey and route-use decisions.

Public Space, Education, Workplace, Hospitality, Temporary Event and Commercial layers own their own operating states.

Crisis/Rescue owns emergency activation, rescue and stabilization.

This extension records the heat episode and the lineage between those systems. It does not steal their decisions.

## 1. Heat episode

```yaml
heat_episode:
  episode_id: null
  geographic_scope_ids: []
  opened_at: null
  closed_at: null
  source_weather_observation_ids: []
  source_forecast_ids: []
  assessment_ids: []
  response_handoff_ids: []
  cooling_access_site_ids: []
  temporary_measure_ids: []
  health_signal_ref_ids: []
  recovery_checkpoint_ids: []
  history_event_ids: []
  canon_status: proposed
```

An episode is a continuity container, not a tactical Weather state.

`HEAT_EPISODE_OPEN != BATTLE_WEATHER_ACTIVE`.

## 2. Heat-condition observation bundle

Do not collapse all conditions into one hidden number.

```yaml
heat_condition_bundle:
  bundle_id: null
  scope_ids: []
  time_window: null
  weather_observation_ids: []
  data_gap_intervals: []
  local_context_claim_ids: []
  provenance_refs: []
```

Local context may include authored shade, elevation, built form or other observed factors, but those claims require evidence.

No bundle creates health damage.

## 3. Heat-impact assessment

A region may later canonize an institution or method that interprets observations for operational use.

```yaml
heat_impact_assessment:
  assessment_id: null
  issuer_id: null
  authority_or_method_ref: null
  issued_at: null
  valid_window: null
  spatial_scope_ids: []
  source_bundle_ids: []
  impact_categories: []
  uncertainty_state: null
  supersedes_assessment_id: null
  superseded_by_assessment_id: null
  response_recommendation_refs: []
  provenance_refs: []
  canon_status: proposed
```

The model does not define universal tiers or thresholds.

A later revision never mutates the earlier assessment silently.

## 4. Cooling-access site

A cooling-access site is any canonized place temporarily or routinely used to reduce exposure or support rest during a heat episode.

It is not automatically a clinic.

```yaml
cooling_access_site:
  site_id: null
  location_id: null
  owning_system_ref: null
  operator_id: null
  normal_function_ref: null
  heat_episode_role: null
  access_state: unknown
  cooling_function_state: unknown
  power_dependency_ref: null
  water_dependency_ref: null
  staffing_dependency_refs: []
  accessibility_ref: null
  capacity_claim_ids: []
  operating_window_ids: []
  verification_ids: []
  notice_ids: []
  history_event_ids: []
  canon_status: proposed
```

Possible descriptive roles may include shaded rest point, indoor cooler space, temporary support hall, staffed welfare point or overnight relief site if canon approves them.

No role label creates medical capability.

## 5. Critical state separations

Always preserve:

`BUILDING_OPEN != COOLING_FUNCTION_AVAILABLE`

`POWER_RESTORED != COOLING_FUNCTION_VERIFIED`

`COOLING_FUNCTION_VERIFIED != SITE_OPEN_TO_PUBLIC`

`SITE_OPEN != CAPACITY_AVAILABLE`

`WATER_SERVICE_AVAILABLE != DRINKING_POINT_VERIFIED`

`HEAT_CONDITIONS_IMPROVED != EVERY_RESPONSE_RETIRED`

`EPISODE_CLOSED != EVERY_DOWNSTREAM_SYSTEM_RECOVERED`

`OUTDOOR_ACTIVITY_PAUSED != LOCATION_PHYSICALLY_CLOSED`

`ROUTE_EXISTS != ROUTE_SELECTED_FOR_THIS_JOURNEY`

These distinctions are necessary for persistent world history.

## 6. Site operating window

```yaml
cooling_site_operating_window:
  window_id: null
  site_id: null
  effective_from: null
  effective_until: null
  planned_or_actual: actual
  trigger_assessment_ids: []
  operator_decision_ref: null
  actual_opened_at: null
  actual_closed_at: null
  interruption_ids: []
  capacity_observation_ids: []
  provenance_refs: []
```

A public notice may advertise a planned window while an equipment fault later changes actual service.

Both records remain queryable.

## 7. Access and capacity observations

```yaml
cooling_access_observation:
  observation_id: null
  site_id: null
  observed_at: null
  observer_id: null
  access_state_observed: null
  cooling_function_observed: null
  capacity_band_observed: null
  limitation_notes: []
  interpretation_claim_ids: []
  provenance_refs: []
```

Suggested capacity bands remain qualitative unless canon supports exact capacity data:

- AVAILABLE
- BUSY
- LIMITED
- AT_DECLARED_CAPACITY
- NOT_ASSESSED
- UNKNOWN

An observation of a crowd does not itself prove capacity was exceeded.

## 8. Temporary heat-response measure

```yaml
temporary_heat_measure:
  measure_id: null
  episode_id: null
  owner_system_ref: null
  subject_id: null
  measure_type: authored
  trigger_assessment_ids: []
  authorized_by_ref: null
  started_at: null
  expected_review_at: null
  ended_at: null
  successor_measure_id: null
  outcome_refs: []
  legacy_ref_ids: []
```

Possible measures are authored by their owner systems, such as changed hours, moved activity, a temporary shaded waiting area, additional welfare checks, an alternate travel plan or a temporary indoor venue.

This layer stores the relationship; it does not grant authority for the measure.

## 9. Activity-timing changes

Heat can change when an activity happens without cancelling the activity.

```yaml
heat_timing_adjustment_ref:
  adjustment_id: null
  owner_system_ref: null
  subject_id: null
  prior_window_ref: null
  replacement_window_ref: null
  heat_evidence_ids: []
  decision_ref: null
  review_condition_refs: []
```

Examples may include a market opening earlier, a worksite pausing during one period, a field survey moving to another window or a public event shifting indoors.

The owner system remains authoritative.

## 10. Welfare-check campaign

A canonized institution may choose to contact residents, workers, travelers or other groups during a heat episode.

```yaml
heat_welfare_check_campaign:
  campaign_id: null
  owner_institution_id: null
  mandate_ref: null
  scope_definition_ref: null
  started_at: null
  ended_at: null
  contact_attempt_ids: []
  aggregate_outcome_ref: null
  care_referral_ids: []
  privacy_policy_ref: null
```

This object is allowed only when canon establishes the institution, mandate and scope.

No individual health diagnosis is copied into public world state.

## 11. Cross-system health handoff

```yaml
heat_health_handoff:
  handoff_id: null
  episode_id: null
  source_observation_or_aggregate_id: null
  destination_care_or_health_system_ref: null
  created_at: null
  scope: aggregate_or_case_ref
  accepted_at: null
  outcome_ref: null
```

The heat layer never diagnoses heat illness.

Care may receive an individual case.

Community Health may receive an aggregate signal.

## 12. Power and cooling dependency

A heat episode may coincide with high electrical demand or an unrelated outage, but the causal relationship remains a claim until supported.

```yaml
heat_power_dependency_event:
  dependency_event_id: null
  cooling_site_id: null
  power_sector_ref: null
  observed_dependency_state: null
  outage_or_restoration_ref: null
  cooling_function_impact_claim_id: null
  verification_ids: []
```

`POWER_OUTAGE_DURING_HEAT != HEAT_CAUSED_OUTAGE`.

The Electric Grid owner controls technical causality and restoration.

## 13. Water dependency

A cooling site or public activity may depend on potable water.

The Drinking Water owner controls availability, treatment and verification.

This extension may store the dependency and resulting operating decision only.

A visible Minecraft water source never proves potable supply.

## 14. Public-space and event integration

Heat can produce socially visible but scoped changes:
- benches moved into shade;
- temporary shade structures;
- indoor venue substitutions;
- queues relocated;
- later opening times or earlier closing times;
- reduced outdoor programming;
- temporary rest points;
- signage linking to a canonized notice.

These changes should persist as world history when meaningful.

A temporary shade structure may later become permanent through Civic/Public Works. The heat layer records the origin story, not the construction authority.

## 15. Travel integration

Travel receives evidence and makes journey decisions.

Possible narrative consequences:
- a walking segment is delayed;
- a departure moves to a cooler window;
- an already-authored alternate mode is selected;
- a rest stop becomes part of the journey;
- one expedition proceeds while another does not because their capabilities and support differ.

Do not mark the base route destroyed or mechanically impassable merely because one journey did not use it.

## 16. Workplaces and professions

Workplace owners may record schedule changes, temporary indoor relocation, staffing changes or suspended tasks.

This extension does not create occupational heat thresholds, labor law or work-rest formulas.

Historical consequences can persist: an early-morning market or evening maintenance shift may remain popular after the episode.

## 17. Pokémon behavior observations

```yaml
heat_pokemon_observation:
  observation_id: null
  pokemon_id_or_population_ref: null
  location_id: null
  observed_at: null
  behavior_description: null
  environmental_context_ids: []
  interpretation_claim_ids: []
  species_lore_refs: []
  mechanical_rule_refs: []
  provenance_refs: []
```

Record only observable behavior first.

Examples:
- an individual repeatedly rests beneath one structure;
- a group shifts activity toward evening;
- a familiar Pokémon visits a water-adjacent area more often;
- another remains active during the same period.

Do not infer heat stress, immunity, forecasting or ecological causality automatically.

## 18. Episode recovery checkpoints

Recovery is multi-owner and staged.

```yaml
heat_recovery_checkpoint:
  checkpoint_id: null
  episode_id: null
  checkpoint_type: authored
  observed_at: null
  evidence_ids: []
  owner_system_ref: null
  downstream_review_refs: []
  status: complete
```

Possible checkpoints can include observed condition improvement, revised forecast, cooling-site stand-down, restoration of a related power service, return of an event, return of a work schedule or closure of a health-monitoring period.

They are not interchangeable.

## 19. Closure

An episode can close while consequences remain.

Possible closure state:

```yaml
heat_episode_closure:
  episode_id: null
  closed_at: null
  closure_basis_ids: []
  open_downstream_ref_ids: []
  legacy_measure_ids: []
  unresolved_cause_or_impact_claim_ids: []
```

A temporary site can remain useful.

A route schedule may stay changed.

A health investigation can remain open.

A public-works proposal can continue.

## 20. Provenance mysteries

This architecture supports mysteries without hidden truth scores.

Example: five residents say “the heat ended” on different dates.

One may mean the last hot afternoon.
Another may mean overnight relief returned.
Another may mean a public site closed.
Another may mean an event resumed outdoors.
Another may mean a clinic stopped special monitoring.

All statements can be accurate within scope.

## 21. Long-term memory

An episode can leave:
- renamed informal meeting spots;
- a shade structure later made permanent;
- changed market hours;
- revised expedition habits;
- a remembered power failure;
- institutional links between Weather and Care;
- repeated Pokémon behavior observations;
- a public archive of notices and revisions.

Future stories should query those facts rather than inventing a fresh town every season.

## 22. Minecraft/Cobblemon boundary

Minecraft/Cobblemon may present:
- harsh-light or heat-haze visuals;
- shade structures;
- altered NPC schedules;
- temporary indoor gathering spaces;
- water stations if canonized;
- closed outdoor activities;
- public notices;
- fans, vents or cooling equipment appropriate to regional technology;
- Pokémon resting or changing routine based on Ouros state.

Presentation has no mechanical authority.

Sunlight rendering does not apply PTU damage.

A Fire-type model does not grant immunity.

Water particles do not heal dehydration.

Minecraft daytime does not activate Sunny Day.

Cobblemon BattleState does not decide combatants, legality, HP/status, positions, heat exposure or encounter outcomes.

## 23. PTU/Caelo mechanical boundary

Remain UNKNOWN unless exact rules and tests establish them:
- generic extreme-heat damage;
- dehydration;
- exhaustion/fatigue tracks;
- hot-ground penalties;
- heat-driven status effects;
- temperature-derived LoS/accuracy changes;
- heat exposure accumulation;
- cooling-zone mechanical effects;
- Type-derived climate immunity;
- species-derived weather sensing;
- Moves/Abilities/Items/Trainer Features used as general civic cooling;
- overworld heat mapping automatically into PTU Weather.

A named Move or Ability that contains sun, fire, water, ice or weather language does not authorize an overworld rule by analogy.

## 24. Encounter A — Cooling Hall Access Withdrawal

Narrative premise:
A temporary cooler public space is ending or changing service while unrelated hostile or territorial contact develops near the entrance.

Full intended version:
- staff and civilians withdraw during combat;
- protected access corridors can matter;
- Intercept and forced displacement may affect the withdrawal;
- AI understands PROTECT/WITHDRAW;
- a heat or exposure zone exists only if exact PTU/Caelo mechanics support it;
- semantic playback shows the same authoritative evacuation and site state.

Permanent capability dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for live heat/exposure or protected-zone mechanics;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version:
Close or pause public service first. Move civilians, staff and sensitive equipment outside BattleSpec. Freeze the heat episode as world context only. AutoPTU receives a reviewed static exterior arena with no heat modifier and no escort objective. Victory can secure the entrance area; the owning institution decides reopening afterward.

## 25. Encounter B — Early-Morning Market Diversion

Narrative premise:
A market has shifted operating hours during a heat episode. A conflict develops at a junction used by vendors moving between the old and temporary schedule/location.

Full intended version:
- vendor withdrawal or route-clearing objective;
- timed departure window;
- Intercept/forced movement;
- objective-aware AI;
- possible environmental heat effects only with exact rules;
- semantic market shutdown/playback.

Dependencies:
The same permanent categories apply. Timed departure additionally pressures full turn/round lifecycle. Dynamic shade or exposure pressures terrain/weather/hazards/zones/reactions.

Reduced version:
Complete vendor movement before BattleSpec creation. Goods and noncombatants remain off-grid. Fight on a static junction after the logistical handoff. Battle outcome can clear immediate access but does not set market hours or conclude the heat episode.

## 26. Encounter C — Observation Roof Perimeter

Narrative premise:
A weather or research team needs a bounded rooftop/yard site after an unusual reading while wild or hostile activity affects access.

Full intended version:
- staff withdrawal/protection;
- equipment protection without treating instruments as ordinary combatants;
- possible live environmental zones;
- reactions/forced movement;
- tactical AI;
- semantic playback.

Reduced version:
Finish observation and secure instruments first. Staff leave the tactical space. Fight on a static reviewed access area. Winning never validates the observation, proves heat causality or changes the forecast.

## 27. Immediate readiness

Usable now without new battle mechanics:
- persistent heat-episode history;
- source-linked observation bundles;
- versioned assessments if canon supplies an issuer/method;
- cooling-access site identity;
- planned versus actual operating windows;
- power/water/staffing dependencies;
- cross-system response handoffs;
- schedule changes preserved as history;
- health handoffs without diagnosis leakage;
- Pokémon behavior observations;
- staged recovery checkpoints;
- archive/provenance mysteries;
- reduced encounter forms on static reviewed geometry.

## 28. Canon questions

Keep unresolved until approved:
- which Ouros regions experience these events;
- what counts locally as unusual heat;
- whether any formal heat-specific assessment exists;
- who can open temporary public support sites;
- regional cooling/ventilation technology;
- operating and access norms;
- privacy rules for welfare checks;
- known historical episodes;
- permanent public-space changes linked to past episodes;
- documented trained roles for individual Pokémon.

## 29. Design outcome

Heat becomes a persistent world event with uneven institutional and social consequences instead of a generic damage aura.

Worldbuilding can advance now while tactical heat, exposure, weather effects and environmental reactions remain gated behind exact PTU/Caelo and AutoPTU contracts.