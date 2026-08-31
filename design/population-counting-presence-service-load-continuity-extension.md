# Population Counting, Presence & Service-Load Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This extension gives Ouros a conservative way to preserve aggregate population claims across time.

It answers questions such as:

- how many people an institution estimated usually lived in a settlement at a given time;
- how many people were physically present during a festival, crisis or tournament;
- how many people a service was effectively supporting;
- what geographic boundary a figure used;
- whether a figure came from enumeration, estimation, projection or revision;
- why two historically valid figures may differ.

It does not create a universal census authority, civil registry, citizenship system or realistic demographic simulator.

## Authority boundary

Residential/Household owns individual residence and household links.

Human Identity owns actor/name/record linkage.

Settlement owns capabilities and service state.

Travel, Hospitality and Transport own visitors and temporary movement when explicitly recorded.

Employment owns work relationships.

Education owns enrollment.

Health/Care owns service cases.

Electoral Selection owns electorate definitions and voting state.

Wild Collective and Scientific Research own wild Pokémon abundance and ecological surveys.

Media/Broadcast own publication of figures.

Archives/Public Memory own preservation and later social interpretation.

This extension owns only aggregate population-measure definitions, snapshots, coverage, revisions and cross-source comparison.

## 1. Population measure definition

```yaml
population_measure_definition:
  measure_id: null
  label: null
  subject_scope: humans
  population_concept: usual_residence|present_at_reference_time|service_population|working_population|institutional_population|authored_other
  geographic_scope_ref: null
  reference_rule_ref: null
  inclusion_rule_refs: []
  exclusion_rule_refs: []
  source_institution_ref: null
  status: PROPOSED
```

No measure exists merely because a settlement exists.

A measure must be authored or produced by a known institution/process.

## 2. Enumeration episode

```yaml
population_enumeration_episode:
  enumeration_id: null
  measure_id: null
  geographic_scope_ref: null
  reference_time_or_period: null
  collection_window: null
  collection_method_ref: null
  coverage_state: unknown
  source_institution_ref: null
  raw_count_ref: protected_or_aggregate
  adjustment_method_ref: null
  result_snapshot_id: null
  provenance_refs: []
```

Coverage states may include COMPLETE_BY_AUTHORED_METHOD, PARTIAL, INTERRUPTED, ESTIMATED_FROM_PARTIAL, DISPUTED and UNKNOWN.

`ENUMERATION_COMPLETED != EVERY_PERSON_REACHED` unless the governing method explicitly establishes that fact.

## 3. Population snapshot

```yaml
population_snapshot:
  snapshot_id: null
  measure_id: null
  settlement_or_area_ref: null
  reference_time: null
  value_kind: exact|range|band|estimate|unknown
  value_ref: null
  confidence_or_quality_ref: null
  source_episode_refs: []
  revision_state: current_for_series
  supersedes_snapshot_ref: null
  published_record_refs: []
  canon_status: proposed
```

Precision must follow evidence.

A source that supports only a coarse band cannot become an exact integer because the renderer currently has 37 NPC entities loaded.

## 4. Presence snapshot

```yaml
presence_snapshot:
  presence_snapshot_id: null
  area_ref: null
  reference_time: null
  present_population_ref: null
  usual_resident_present_ref: null
  usual_resident_temporarily_absent_ref: null
  temporary_visitor_present_ref: null
  unknown_classification_ref: null
  source_refs: []
```

These fields may be ranges or bands.

The model does not require an individual-level list.

## 5. Service-population signal

```yaml
service_population_signal:
  signal_id: null
  service_or_facility_ref: null
  catchment_area_refs: []
  reference_period: null
  demand_band: null
  observed_usage_refs: []
  resident_population_snapshot_refs: []
  visitor_or_commuter_refs: []
  confidence: null
  provenance_refs: []
```

This exists to model pressure without fabricating permanent residents.

A Pokémon Center, ferry terminal, school, market or Gym may serve people from outside its settlement.

`SERVICE_DEMAND_RISE != RESIDENT_POPULATION_RISE`.

## 6. Seasonal and event presence

```yaml
temporary_population_pressure:
  pressure_id: null
  area_ref: null
  cause_ref: festival|tournament|harvest|pilgrimage|seasonal_work|tourism|crisis_displacement|transport_disruption|authored_other
  start_time: null
  end_time: null
  normal_presence_band_ref: null
  active_presence_band_ref: null
  lodging_pressure_ref: null
  transport_pressure_ref: null
  care_pressure_ref: null
  food_supply_pressure_ref: null
  source_refs: []
```

The cause must come from existing world state.

The generator may not create a festival or migration merely to justify a population spike.

## 7. Geographic scope version

```yaml
population_geography_version:
  geography_version_id: null
  area_ref: null
  effective_from: null
  effective_until: null
  included_location_refs: []
  excluded_location_refs: []
  boundary_source_ref: null
  supersedes_ref: null
```

A historical series must preserve boundary changes.

If a nearby beach, station district or new suburb enters the counted area, a changed total does not automatically mean people moved.

`COUNT_CHANGED != POPULATION_MOVED`.

## 8. Revision record

```yaml
population_revision:
  revision_id: null
  prior_snapshot_ref: null
  revised_snapshot_ref: null
  revision_reason: coverage_update|method_change|boundary_change|duplicate_removal|late_records|correction|authored_other
  evidence_refs: []
  issued_by_ref: null
  issued_at: null
  propagation_refs: []
```

Historical values remain queryable.

A revision changes the current interpretation of the series. It does not erase what institutions previously believed or published.

## 9. Cross-source comparison

```yaml
population_comparison:
  comparison_id: null
  snapshot_refs: []
  compatible_measure_refs: []
  incompatibility_reasons: []
  interpretation_refs: []
  unresolved_questions: []
```

Typical incompatibilities:

- different reference dates;
- usual residence versus physical presence;
- different geographic boundaries;
- different inclusion rules;
- partial coverage;
- estimate versus direct count;
- institutional population included in one figure but excluded in another.

The system should explain these differences before creating a mystery or fraud allegation.

## 10. Relationship to individual records

Aggregates should not require storage of a hidden universal resident list.

When exact individual links already exist for important persistent actors, the aggregate layer may reference them as supporting evidence. It must not infer unrecorded identities to make totals balance.

`AGGREGATE_COUNT != LIST_OF_IDENTITIES`.

`COUNTED_PERSON != CIVIC_REGISTRATION_CREATED`.

`RESIDENT_LINK_EXISTS != INCLUDED_IN_EVERY_POPULATION_MEASURE`.

## 11. Core continuity boundaries

`USUAL_RESIDENT != PRESENT_NOW`

`PRESENT_NOW != USUAL_RESIDENT`

`VISITOR != RESIDENT`

`TEMPORARILY_ABSENT != MOVED_AWAY`

`ENUMERATED != CIVICALLY_REGISTERED`

`POPULATION_ESTIMATE != EXACT_WORLD_HEADCOUNT`

`CENSUS_SNAPSHOT != CURRENT_POPULATION`

`COUNT_REVISED != PRIOR_REPORT_NEVER_EXISTED`

`BOUNDARY_CHANGED != PEOPLE_MOVED`

`SERVICE_LOAD != RESIDENT_COUNT`

`WORKING_HERE != LIVING_HERE`

`STUDENT_HERE != RESIDENT_HERE`

`VOTER != RESIDENT_BY_DEFAULT`

`SUPPORTER_PRESENT != LOCAL_RESIDENT`

`MINECRAFT_NPC_ENTITY_COUNT != CANONICAL_POPULATION`

`COBBLEMON_ENTITY_COUNT != SETTLEMENT_DEMOGRAPHY`

## 12. Population change attribution

A changed aggregate may be explained only through evidence.

Possible authored contributors include residential relocation, births/deaths if a governing life-event layer establishes them, boundary changes, institutional opening/closure, temporary visitor flows, crisis displacement, seasonal work, data revision or changed methodology.

Do not reverse-engineer causal life events from arithmetic alone.

If one snapshot is 1,000 and the next is 980, Narrative cannot silently create twenty deaths or departures.

## 13. Privacy and disclosure

Default outputs are aggregate.

Small groups can create re-identification risk inside the fiction. The generator should avoid turning a tiny category into a named-person list unless existing authority and access rules permit it.

A public demographic table does not expose private residence records.

## 14. Population-aware settlement planning

Settlement systems may consume aggregate signals for authored planning decisions.

Examples:

- clinic demand exceeds normal capacity;
- temporary lodging pressure rises during a tournament;
- ferry demand grows during a seasonal work period;
- a school catchment changes over years;
- food distribution plans use a revised service-population estimate.

The population layer only supplies evidence. Civic Governance, institutions and world actors decide what to do with it.

## 15. Mystery discipline

Disagreeing population figures are not automatically evidence of corruption.

Before generating a case, check method, scope, date, visitors, absences, geography and revision lineage.

Useful mysteries arise when those explanations fail or when an existing authored motive intersects the discrepancy.

## 16. Minecraft/Cobblemon boundary

Minecraft/Cobblemon may render:

- a visibly busier settlement during a canon event;
- queues or crowds after Ouros establishes pressure state;
- empty houses after authored relocation;
- changed settlement density over long timescales;
- census workers or survey stations after the relevant episode exists.

It may not decide:

- canonical population from loaded entities;
- who is a resident from spawn location;
- who moved because an NPC unloaded;
- that a missing NPC died;
- that a crowd size equals votes, supporters or service users;
- that a Pokémon entity belongs in a human demographic count.

## 17. PTU/Caelo boundary

This extension creates no mechanical population effects.

Do not invent:

- population-based Trainer bonuses;
- crowd bonuses;
- settlement-size Skill modifiers;
- enumeration Skill DCs;
- Features that alter demographic facts;
- Badge or League eligibility from residence;
- citizenship/residency permissions;
- Pokémon loyalty/capture effects from household or town population.

Any future mechanic must be validated against exact PTU/Caelo authority and current engine implementation.

## 18. Encounter contract A — Enumeration Team Withdrawal

Full premise: a field enumeration team is cut off during an unrelated tactical incident and must withdraw safely while preserving its equipment and partial records.

Full dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL; escort/withdrawal remains unverified as a complete family
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL as selected content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING if environmental danger is tactical
- move-specific behavior — PARTIAL; individual audit
- abilities — PARTIAL; individual audit
- items — PARTIAL; individual audit
- Trainer Features/perks — PARTIAL; individual audit
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for protect/withdraw semantics
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic escort playback

Full status: BLOCKED.

Reduced version: the team exits the tactical slice before initiative. Static ordinary combat may return only `IMMEDIATE_ENUMERATION_SITE_APPROACH_CLEAR`.

That result does not complete the count, recover missing forms, establish coverage or validate a population total.

## 19. Encounter contract B — Archive Count-Sheet Recovery Perimeter

Full premise: historical count material is threatened during a facility incident.

Full version requires protected-object handling, complete movement when carrying matters, lifecycle, relevant hazards/reactions, tactical policy and adapter playback.

Full status: BLOCKED.

Reduced version: records remain outside BattleSpec in secured narrative state. AutoPTU may establish only `IMMEDIATE_RECORD_STORAGE_APPROACH_CLEAR`.

No result proves records intact, authentic, complete or interpreted correctly.

## 20. Encounter contract C — Festival Service Chokepoint

Full premise: temporary population pressure produces congestion during a separate hostile incident near a service route.

A rich version requires crowd routing, complete movement, zones/reactions, lifecycle, objective-aware AI and adapter support.

Full status: BLOCKED.

Reduced version: civilians are removed from BattleSpec before initiative and geometry is frozen. AutoPTU may return `IMMEDIATE_SERVICE_ROUTE_CLEAR` only.

That does not reduce the festival population, restore service capacity or determine public reaction.

## 21. Encounter contract D — Remote Count Station Perimeter

Full premise: a temporary field station must remain reachable during an ecological or faction incident.

Full dependencies vary with authored threat but commonly include complete movement, lifecycle, hazards/weather/zones/reactions and tactical policy.

Full status: BLOCKED when those families are required.

Reduced status: READY at narrative-contract level after individual battle-content audit. The station and staff remain outside BattleSpec. AutoPTU may return only `IMMEDIATE_COUNT_STATION_ACCESS_CLEAR`.

## 22. Implementation order

Recommended implementation sequence:

1. population measure definition;
2. snapshots with provenance;
3. geographic scope versions;
4. revision lineage;
5. presence versus usual-residence distinction;
6. service-load signals;
7. event/seasonal pressure links;
8. cross-source comparison;
9. public reporting integration;
10. reduced encounter hooks.

The layer can function without battle mechanics. Tactical incidents remain optional consumers of already-authored population context.