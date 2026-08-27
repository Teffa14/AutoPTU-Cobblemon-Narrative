# Ouros Hot Springs, Bathhouses & Thermal Leisure Continuity Extension

Status: Proposed systems design. Not established canon.
Date: 2026-08-28

## Purpose

Ouros already models geology, infrastructure, hospitality, tourism, public space, care, maintenance, seasonality, local knowledge and ecological occupancy. This extension connects those systems around persistent thermal places without creating a parallel healing system or a generic resort simulator.

It models the continuity between:

`thermal source -> delivery/distribution -> bath facility -> access/service -> repeated use -> observation/incident -> inspection/intervention -> reopening -> persistent callback`

The same thermal place should remain useful across ordinary leisure, local routines, tourism, investigation, maintenance, environmental observation and occasional tactical encounters.

## 1. Authority split

Geology owns:
- geothermal source/context;
- source-location observations;
- geological interpretation;
- subsurface connection claims.

Infrastructure and Facility Maintenance own:
- pipes, pumps, channels, tanks, valves, structural condition and faults;
- repair work;
- inspection and reopening of technical assets.

Hospitality/Tourism own:
- guest-facing service;
- visitor pressure;
- accommodation/venue relationships;
- ordinary commercial operation.

Public Space owns:
- shared-space use when the bath or surrounding spring is genuinely public/communal.

Care owns:
- medical assessment/treatment;
- authoritative health-state handoffs.

Conservation/Wild Ecology own:
- habitat interpretation;
- recurring wild use;
- ecological management decisions.

Rumor/Public Memory own:
- public stories, advertised benefits, superstition and later corrections.

This extension owns the cross-system continuity of the thermal place and its use history. It does not override any owner above.

## 2. Thermal site

```yaml
thermal_site:
  thermal_site_id: null
  location_id: null
  geological_site_ref: null
  source_zone_ids: []
  source_observation_ids: []
  water_or_heat_delivery_link_ids: []
  facility_ids: []
  natural_access_zone_ids: []
  ecological_overlap_ids: []
  cultural_claim_ids: []
  historical_event_ids: []
  current_source_state: UNKNOWN
  disclosure_scope: null
```

Suggested source states:
- UNKNOWN
- OBSERVED_ACTIVE
- OBSERVED_REDUCED
- OBSERVED_INTERRUPTED
- OBSERVED_CHANGED
- UNDER_REVIEW

These are observation-oriented states. They do not declare the geological cause.

“Hotter than usual”, “cooler than last month” or “flow stopped” should remain sourced observations until a qualified system records interpretation.

## 3. Bathing facility

```yaml
bathing_facility:
  facility_id: null
  thermal_site_id: null
  location_id: null
  operator_or_steward_ids: []
  facility_type: null
  bath_zone_ids: []
  service_dependency_ids: []
  staff_dependency_ids: []
  maintenance_asset_ids: []
  access_rule_refs: []
  accessibility_refs: []
  public_information_refs: []
  visitor_destination_ref: null
  current_operational_state: UNKNOWN
  closure_reason_refs: []
  reopening_review_refs: []
```

Candidate descriptive facility types:
- NATURAL_SPRING_ACCESS
- COMMUNAL_BATH
- BATHHOUSE
- INN_OR_LODGE_BATH
- PUBLIC_THERMAL_POOL
- SMALL_NEIGHBORHOOD_BATH
- RESEARCH_OR_INSTITUTIONAL_THERMAL_SITE

These labels grant no legal authority, healing effect or cultural practice by themselves.

Suggested operational states:
- OPEN
- LIMITED
- PARTIALLY_CLOSED
- CLOSED
- UNDER_INSPECTION
- RESTORING
- SEASONAL

## 4. Bath zones and pool identity

Do not flatten a multi-pool site into `bathhouse_open=true`.

```yaml
bath_zone:
  bath_zone_id: null
  facility_id: null
  zone_type: null
  supply_link_ids: []
  access_state: null
  capacity_band: null
  observed_temperature_band: null
  condition_observation_ids: []
  maintenance_refs: []
  ecological_use_refs: []
  ordinary_use_window_refs: []
```

Possible descriptive zone types:
- INDOOR_POOL
- OUTDOOR_POOL
- NATURAL_POOL
- FOOTBATH
- COOLING_OR_REST_AREA
- WASHING_AREA
- SOURCE_VIEWING_AREA
- SERVICE_ONLY_ZONE
- OUTFLOW_CHANNEL

Exact bathing customs, dress/privacy rules, segregation practices and etiquette require culture-specific canon. Do not infer them from real-world or Pokémon references.

## 5. Source, delivery and service are separate facts

A useful dependency graph is:

```yaml
thermal_service_dependency:
  dependency_id: null
  upstream_ref: null
  downstream_ref: null
  dependency_type: null
  observation_refs: []
  current_state: UNKNOWN
```

Examples:
- source -> collection point;
- collection point -> pipe/channel;
- pipe -> holding tank;
- tank -> specific bath zone;
- electrical utility -> pump;
- staffing -> opening window;
- access route -> visitor service.

A source may be active while one pool is cold because its line is blocked.

A bath may be closed while water is fine because inspection, staffing, access or structural condition is unresolved.

A town may retain ordinary life while one visitor-facing thermal venue is unavailable.

## 6. Thermal observation event

```yaml
thermal_observation:
  observation_id: null
  observed_at: null
  observer_ids: []
  site_or_zone_id: null
  observation_type: null
  qualitative_value: null
  instrument_or_method_ref: null
  comparison_ref: null
  confidence: null
  evidence_refs: []
```

Candidate observations:
- FLOW_PRESENT
- FLOW_REDUCED
- FLOW_ABSENT
- TEMPERATURE_HIGHER
- TEMPERATURE_LOWER
- STEAM_PRESENT
- ODOR_OR_COLOR_CHANGE
- UNUSUAL_NOISE
- POOL_LEVEL_CHANGE
- PIPE_OR_CHANNEL_LEAK
- WILDLIFE_USE
- CROWDING

An observation never creates a diagnosis or tactical hazard automatically.

## 7. Therapeutic claims boundary

Thermal places can accumulate claims such as:
- “good after a long hike”;
- “helps sore muscles”;
- “the old pool is stronger”;
- “visitors recover faster here”;
- “this spring is sacred/protective”.

Store those as claims with provenance.

```yaml
thermal_claim:
  claim_id: null
  claimant_or_publisher_id: null
  thermal_site_id: null
  claim_type: CULTURAL | PERSONAL | COMMERCIAL | HISTORICAL | MEDICAL_HYPOTHESIS | OTHER
  statement_summary: null
  source_refs: []
  current_review_state: UNREVIEWED
  public_scope: null
```

No claim may directly:
- heal HP;
- remove Injury;
- cure status;
- restore AP;
- refresh Move frequency;
- change Combat Stages;
- grant temporary HP;
- increase Loyalty/Friendship;
- create a custom Digestion/Food Buff;
- reduce PTU recovery time.

PTU already owns Rest, Extended Rest and Pokémon Center healing. A soak can only benefit mechanically through an existing validated rule path, not through this layer.

## 8. Ordinary leisure and social use

A bathhouse can be a recurring social location without turning every visit into an event.

```yaml
thermal_use_event:
  event_id: null
  facility_id: null
  zone_ids: []
  actor_or_cohort_ids: []
  use_type: LEISURE | LOCAL_ROUTINE | VISITOR_STOP | POST_ACTIVITY_REST | MEETING | OBSERVATION
  start_window: null
  end_window: null
  conversation_or_information_refs: []
  notable_observation_refs: []
  mechanical_rest_ref: null
```

Routine use should normally compress.

Expand when:
- a recurring NPC matters;
- new information appears;
- access or capacity changes;
- an ecological overlap becomes visible;
- the player deliberately chooses social/leisure time;
- a maintenance or service anomaly occurs;
- the location carries historical/cultural significance.

`mechanical_rest_ref` remains null unless the authoritative PTU time/rest service actually records qualifying rest.

## 9. Recurring local knowledge

Regular users can know patterns without knowing causes.

Examples:
- a morning regular knows one pool usually warms first;
- a cleaner knows which drain normally runs louder;
- an inn worker knows when visitor pressure rises;
- a maintenance worker remembers a previous pipe repair;
- a local Pokémon repeatedly appears near the warm outflow at dusk.

These observations can be excellent investigative evidence.

They do not make the speaker a geologist, mechanic, doctor or ecologist.

## 10. Ecological overlap

Warm water, outflow, sheltered ground or quiet closed periods may overlap wild Pokémon activity.

```yaml
thermal_ecology_overlap:
  overlap_id: null
  thermal_site_id: null
  zone_id: null
  actor_or_collective_refs: []
  observation_window_refs: []
  behavior_observation_refs: []
  source_dependency_hypothesis_refs: []
  disturbance_refs: []
  conservation_handoff_refs: []
```

Rules:
- recurring use does not create ownership;
- bathing humans do not automatically displace wild Pokémon off-screen;
- a Pokémon near a spring failure is not automatically the cause;
- a spring reopening cannot erase a newly established habitat through a narrative flag;
- an ecological interpretation requires Conservation/Science evidence.

A useful temporal pattern is shared use by different windows: humans by day, wild Pokémon around outflow at night, maintenance staff before opening, etc.

## 11. Closure and reopening

A thermal venue can close for many reasons:
- source interruption;
- pipe/pump fault;
- structural work;
- staff shortage;
- access-route closure;
- water-condition review;
- utility outage;
- ecological restriction;
- public-event repurposing;
- crisis state.

```yaml
thermal_closure:
  closure_id: null
  facility_or_zone_id: null
  observed_trigger_refs: []
  authority_ref: null
  start_at: null
  public_notice_refs: []
  technical_handoff_refs: []
  visitor_handoff_refs: []
  reopening_criteria_refs: []
  current_state: ACTIVE
```

A source repair does not automatically close the closure record.

Reopening may require separate confirmation of:
- source/service flow;
- asset condition;
- safe access;
- facility readiness;
- staffing;
- any required ecological or operational review.

No specific inspection law or health regulation is assumed until canon defines it.

## 12. Thermal-service incident investigation

Recommended sequence:

1. Record user-facing symptom.
2. Compare affected bath zones.
3. Check shared and separate supply links.
4. Review source observations.
5. Review recent maintenance/outage/weather/ecology state.
6. Preserve public claims separately from evidence.
7. Establish a bounded cause hypothesis.
8. Hand technical work to the owning system.
9. Verify downstream service before reopening.
10. Record public correction when prior information changed materially.

This supports mysteries without manufacturing a villain.

## 13. Visitor pressure and ordinary residents

Thermal tourism should reuse the existing Tourism layer.

Possible consequences of increased popularity:
- accommodation pressure;
- queue/access pressure;
- longer service windows;
- waste/maintenance load;
- resident-space conflict;
- ecological disturbance near source/outflow;
- new shops/services;
- stale promotional claims spreading farther.

The thermal system does not own a “tourism score”. It only supplies traceable attraction/service state.

A neighborhood bath used mainly by residents should not become a tourist destination merely because the player discovered it.

## 14. Historical continuity

Thermal infrastructure can accumulate revisions:
- original natural pool;
- first channel/pipe;
- expanded bathhouse;
- old line abandoned;
- source-access route changed;
- pool repurposed;
- outflow restored;
- visitor interpretation changed.

Older maps, signs and memories can remain accurate for their own period.

A new building does not erase the previous use of the spring.

## 15. Minecraft/Cobblemon representation

Strong `SAFE_REUSE` candidates, subject to concrete API review:
- water blocks and fluid visuals;
- steam/smoke-like particles where appropriate;
- sounds;
- blocks, slabs, stairs, signs, doors and decorative materials;
- Pokémon overworld entities;
- Pokémon models, forms, poses, idle animations and cries;
- NPC/world entity placement;
- interaction hooks;
- UI and networking;
- entity tracking and synchronization;
- persistence hooks for stable Ouros references.

Likely `ADAPTER_REQUIRED` inputs:
- world block/fluid geometry mapped into a reviewed encounter arena;
- current visible weather/time;
- exact entity references;
- block/interactable state that projects a thermal facility condition;
- source/facility observations that become Ouros evidence.

`BATTLE_AUTHORITY_FORBIDDEN`:
- Cobblemon BattleState;
- participant/side/controller selection;
- nearby-entity auto-enrollment;
- Cobblemon HP/status/initiative/action legality as Ouros truth;
- battle completion or outcome callbacks used as authority.

Required battle direction:

`Ouros thermal/world state -> explicit participant manifest -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

A Pokémon visually sitting beside a pool remains an overworld actor unless Ouros explicitly selects it for the encounter.

## 16. PTU/Caelo boundary

Pass 88 establishes no custom mechanics for:
- hot-water healing;
- mineral-water buffs;
- sauna fatigue removal;
- heat tolerance;
- slippery movement;
- steam concealment;
- scalding damage;
- geothermal hazards;
- bathing-related status removal;
- accelerated Injury recovery;
- relaxation-based Loyalty/Friendship;
- spring-based Move/Ability changes.

When a visit is genuinely restful, use authoritative PTU Rest/Extended Rest timing and restrictions. When clinical treatment occurs, use Care plus authoritative healing systems.

## 17. Encounter A — Thermal Source Access Withdrawal

Narrative premise:
A survey/maintenance team inspecting a reduced spring flow encounters territorial wild Pokémon near the access route. The technical source remains unresolved and workers need to withdraw before any intervention can continue.

Intended full version:
- workers withdraw through more than one route;
- pool edges, steam or unstable warm ground matter only if validated tactical mappings exist;
- Intercept/forced displacement can matter around narrow access;
- wild AI may prioritize territory/retreat rather than KO;
- AutoPTU events drive Minecraft playback.

Full capability dependencies:
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
- Ouros withdraws all workers before BattleSpec creation;
- source/pipes remain world-state objects outside the tactical grid;
- steam, heat and water are presentation only;
- a fixed dry/stable arena is selected nearby;
- Ouros explicitly selects combatants;
- AutoPTU resolves only the ordinary battle;
- investigation and technical intervention resume afterward.

Victory cannot prove the source cause or authorize reopening.

## 18. Encounter B — Bathhouse Evacuation Perimeter

Narrative premise:
An unexpected wild intrusion reaches a bathhouse service edge while visitors are present. Staff close affected zones and clear guests before the cause of the intrusion is known.

Intended full version:
- civilians move toward exits;
- multiple access routes and protected noncombatants matter;
- tactical zones could represent validated facility constraints;
- AI can distinguish retreat, territory and protection priorities;
- adapter preserves exact facility/closure state.

Full capability dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING when wet floors, steam or protected zones have tactical meaning;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version:
- visitors and staff evacuate in world state first;
- affected bath zones close;
- battle occurs only in a fixed service courtyard/access area;
- no wet-floor, steam, heat, pool-HP or civilian-protection rules are scripted;
- closure remains after combat until Maintenance/Ecology/Facility review completes.

## 19. Noncombat investigation — Three Pools, Two Supply Lines

Three baths show different temperature/flow changes. Player work consists of:
- comparing observations by time;
- tracing which pools share a line;
- checking source observations;
- reading recent maintenance history;
- interviewing regulars as local-knowledge sources;
- separating a popular explanation from technical evidence.

Possible conclusions include:
- one line fault;
- source-side change affecting only one intake;
- stale observation;
- a valve/configuration difference;
- more evidence required.

No combat or custom Skill subsystem is required.

## 20. Compression policy

Compress:
- routine bathing with no meaningful choice;
- ordinary opening/closing;
- stable maintenance rounds;
- uneventful visitor use;
- normal rest already resolved by PTU/time systems.

Expand:
- changed source/service state;
- competing observations;
- recurring NPC callback;
- visitor pressure colliding with resident use;
- ecology overlapping access/outflow;
- a reopening decision;
- an old repair becoming relevant;
- misinformation affecting action;
- player-authored leisure/social goals.

## 21. Canon questions

Pass 88 deliberately leaves unresolved:
- which Ouros regions have thermal springs;
- whether naturally heated, artificially heated and mixed facilities all exist;
- bathing etiquette and privacy norms;
- institution/operator types;
- technical standards and inspection authority;
- whether any source is sacred or historically protected;
- therapeutic beliefs and how communities frame them;
- visitor versus resident access;
- wild Pokémon use of thermal environments;
- pricing, reservations or membership;
- exact source ownership/stewardship.

None may be inferred from the Pokémon references or real-world bathing traditions.
