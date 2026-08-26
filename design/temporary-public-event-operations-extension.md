# Ouros Temporary Public Event Operations Extension

Status: Proposed systems design. Not established canon.

## Purpose

Ouros already has systems for recurrence, public memory, tourism, staffing, economy, accessibility, sanitation, transit, communications, performance and battle institutions. Those layers describe the ingredients of a public event, but they do not yet provide one operational record that says what is active at this edition, what the site currently looks like, which dependencies are failing and what needs to persist after closure.

This extension coordinates those systems for a bounded event instance. It does not replace them.

## 1. Ownership boundary

The extension owns:
- event-instance phase;
- temporary site overlay;
- active service/activity roster;
- dependency readiness;
- aggregate visitor/crowd state;
- operational incidents;
- setup and teardown state;
- handoff records back to permanent systems.

Existing layers remain authoritative for their domains:
- Seasonality/Calendar: recurrence and date windows;
- Public Memory: remembered editions and legacy;
- Tourism: destination pressure and visitor effects;
- Workplaces: staffing;
- Material Culture/Economy: vendors, supply routes, commissions, markets;
- Accessibility: accommodations and participation barriers;
- Waste/Sanitation: refuse, cleanup and pollution;
- Travel/Transit: routes and service capacity;
- Media/Communications: announcements and corrections;
- Civic Governance: public works and institutional decisions;
- Contest/Performance and Battle Institutions: formal event mechanics.

## 2. Event instance

A recurring festival can have many event instances. A one-time fair has one.

```yaml
event_instance:
  event_instance_id: null
  recurring_event_ref: null
  edition_id: null
  public_name: null
  host_actor_ids: []
  host_institution_ids: []
  site_overlay_ids: []
  announced_window_ref: null
  actual_opened_at: null
  actual_closed_at: null
  phase: SETUP
  activity_ids: []
  temporary_service_ids: []
  dependency_ids: []
  visitor_cohort_ids: []
  operational_incident_ids: []
  prior_edition_refs: []
  chronicle_refs: []
  closure_handoff_id: null
```

Candidate phases:
- PLANNED
- SETUP
- READY
- OPENING
- OPERATING
- LIMITED
- PAUSED
- EVACUATING
- CLOSED
- TEARDOWN
- AFTERMATH
- CANCELLED

Phase changes need causal events. The clock alone does not silently move an event from OPERATING to EVACUATING.

## 3. Temporary site overlay

The event modifies an existing location for a limited period.

```yaml
event_site_overlay:
  overlay_id: null
  event_instance_id: null
  base_location_id: null
  active_from: null
  active_until: null
  public_zone_refs: []
  staff_zone_refs: []
  vendor_slot_refs: []
  activity_slot_refs: []
  rest_quiet_zone_refs: []
  temporary_access_change_refs: []
  temporary_signage_refs: []
  closure_segment_refs: []
  overworld_variant_ref: null
  mechanics_review_required: true
```

The overlay must not create a duplicate settlement record. When removed, the base location persists with any approved damage, cleanup, memory or infrastructure changes written back.

## 4. Operational dependency

A public event depends on other world systems.

```yaml
event_operational_dependency:
  dependency_id: null
  event_instance_id: null
  dependency_type: null
  owning_layer: null
  owning_state_ref: null
  required_state: null
  current_state: UNKNOWN
  checked_at: null
  consequence_if_unavailable: null
  workaround_refs: []
```

Candidate dependency types:
- STAFFING
- SUPPLY_DELIVERY
- TRANSPORT_ACCESS
- POWER_OR_INFRASTRUCTURE
- COMMUNICATION
- ACCESSIBILITY
- SANITATION
- WEATHER_PLAN
- ECOLOGICAL_ACCESS
- MEDICAL_OR_CARE_SUPPORT
- SITE_CONDITION
- PERFORMER_OR_OPERATOR
- EQUIPMENT_CUSTODY
- OTHER_AUTHORED_DEPENDENCY

The extension stores dependency status. The owning layer decides the real underlying state.

## 5. Readiness gate

Before opening, the event can derive a legible readiness summary.

```yaml
event_readiness:
  event_instance_id: null
  blocking_dependency_ids: []
  degraded_dependency_ids: []
  ready_dependency_ids: []
  decision_state: REVIEW_REQUIRED
  decision_actor_ids: []
  decision_event_id: null
```

Candidate decisions:
- OPEN_AS_PLANNED
- OPEN_LIMITED
- DELAY_OPENING
- RELOCATE_PART
- PAUSE_ACTIVITY
- CANCEL_EVENT

Do not automate governance choices unless an explicit institution policy exists. A failed dependency should surface a decision, not invent authority.

## 6. Event activity

An activity is a scheduled or continuous public interaction.

```yaml
event_activity:
  activity_id: null
  event_instance_id: null
  operator_actor_ids: []
  operator_institution_ids: []
  site_slot_ref: null
  public_label: null
  schedule_ref: null
  availability_state: PLANNED
  access_policy_ref: null
  participant_state_ref: null
  mechanics_ref: null
  dependency_ids: []
  result_event_refs: []
```

Candidate availability states:
- PLANNED
- OPEN
- DELAYED
- LIMITED
- FULL
- PAUSED
- COMPLETED
- CANCELLED

`mechanics_ref` must point to an approved system when the activity has formal rules. The narrative layer cannot invent a catching contest, racing format, performance scoring, battle bracket or reward table.

## 7. Temporary service

Vendors, information desks, mobile clinics, repair stands or other temporary services can be present only during the event.

```yaml
event_temporary_service:
  temporary_service_id: null
  event_instance_id: null
  provider_ref: null
  base_service_ref: null
  site_slot_ref: null
  operating_window_ref: null
  availability_state: PLANNED
  stock_or_capacity_ref: null
  dependency_ids: []
```

Actual prices, stock, healing, crafting, food effects and service rules stay with their governing systems.

## 8. Visitor cohort

Reuse the abstraction discipline established for transit passenger cohorts.

```yaml
event_visitor_cohort:
  cohort_id: null
  event_instance_id: null
  origin_context_refs: []
  size_band: null
  visitor_tags: []
  arrival_window_ref: null
  departure_window_ref: null
  current_presence_state: EXPECTED
  notable_actor_ids: []
  pressure_effect_refs: []
```

Candidate presence states:
- EXPECTED
- ARRIVING
- PRESENT
- DEPARTING
- DEPARTED
- DISPLACED
- UNKNOWN

Visitor tags describe authored context such as local residents, visiting performers, students, researchers or spectators. They do not grant private beliefs or mechanical abilities.

## 9. Crowd pressure without crowd combat rules

An event may track ordinal crowd pressure for world operations.

```yaml
crowd_pressure_state:
  event_instance_id: null
  zone_ref: null
  band: LIGHT
  observation_refs: []
  operational_effect_refs: []
  last_updated_at: null
```

Candidate bands:
- LIGHT
- NORMAL
- BUSY
- CONGESTED
- ACCESS_RESTRICTED

This state may justify more staff, queue redirection, service limitation or a temporary closure when the authored world system supports it.

It must not automatically become:
- difficult terrain;
- forced movement;
- interception;
- Accuracy modifiers;
- damage;
- initiative changes;
- reaction windows.

## 10. Queue and access state

Queues can matter operationally without requiring individual NPC simulation.

```yaml
event_access_flow:
  flow_id: null
  activity_or_service_ref: null
  entry_zone_ref: null
  exit_zone_ref: null
  pressure_band: null
  accessibility_conflict_refs: []
  route_conflict_refs: []
  current_response: null
```

Possible responses:
- REDIRECT
- ADD_SIGNAGE
- LIMIT_ENTRY
- TEMPORARY_PAUSE
- MOVE_QUEUE
- OPEN_ALTERNATE_ACCESS

Any response must be feasible in actual site state.

## 11. Operational incident

An incident is a change that threatens event operation or creates a meaningful choice.

```yaml
event_operational_incident:
  incident_id: null
  event_instance_id: null
  detected_at: null
  cause_state_refs: []
  observed_impact_refs: []
  affected_dependency_ids: []
  affected_activity_ids: []
  affected_service_ids: []
  response_option_refs: []
  current_state: OPEN
  battle_handoff_ref: null
  resolution_event_id: null
  persistent_output_refs: []
```

Candidate incident sources:
- delayed supply;
- absent operator;
- damaged site component;
- unexpected visitor pressure;
- actual weather observation;
- route disruption;
- ecological restriction;
- misinformation;
- lost property;
- equipment custody problem;
- sanitation backlog;
- conflict between simultaneous activities.

Do not generate arbitrary emergencies merely because an event is active.

## 12. Event information surface

Players should know why an event is limited or changing.

Possible surfaces:
- schedule board;
- temporary signs;
- announcements;
- staff dialogue;
- queue changes;
- visibly closed stalls;
- route notices;
- updated event program;
- physical setup or teardown state.

The Media/Communications layer owns publication and delivery. This extension only links current event operations to the relevant information records.

## 13. Setup gameplay

Setup deserves expansion when the player has a meaningful choice.

Examples:
- decide which activity opens late after a delivery fails;
- help verify alternate accessible routing;
- trace why a temporary service lacks materials;
- identify conflicting site uses before doors open;
- locate borrowed equipment before an operator arrives;
- respond to an ecological observation that changes one zone's access.

Routine setup should compress.

## 14. Teardown and closure handoff

```yaml
event_closure_handoff:
  handoff_id: null
  event_instance_id: null
  final_phase: AFTERMATH
  temporary_overlays_removed: []
  unresolved_incident_ids: []
  waste_state_refs: []
  damage_state_refs: []
  lost_property_refs: []
  custody_transfer_refs: []
  route_reopening_refs: []
  vendor_or_service_outputs: []
  public_memory_candidate_refs: []
  next_edition_change_refs: []
  chronicle_event_ids: []
```

Closure is incomplete if an operational consequence still needs an owning system.

## 15. Edition continuity

The next edition should be allowed to read prior operational state.

Useful carryover:
- activities that repeatedly overfill;
- access changes that worked;
- services that failed because of known dependencies;
- recurring ecological restrictions;
- staff or vendor relationships;
- safety or cleanup lessons;
- public controversy;
- popular new traditions;
- discontinued practices;
- borrowed equipment still tied to provenance or custody.

The Public Memory and Seasonality layers remain the permanent owners of remembered editions and recurrence. This extension supplies operational facts.

## 16. Generation rule

Expand an event operationally when at least one current fact intersects a player decision:
- an active dependency fails;
- the player has a role in setup/operation/cleanup;
- a named actor's goal conflicts with event constraints;
- visitor pressure affects an existing service or route;
- an ecological or infrastructure observation changes access;
- a prior edition creates a current expectation or controversy;
- an incident creates several legitimate response paths.

Otherwise summarize attendance and record only important outcomes.

## 17. Encounter contract A — Crowdline Breakout

Narrative premise:
A disturbance occurs beside an active public event. Staff need the public out of the affected zone while a small set of actual combatants remains.

Intended full version:
- civilians visibly occupy and leave zones during combat;
- combatants may block, shove or intercept movement;
- temporary barriers can change the available space;
- objective-aware opponents may prioritize escape, pursuit or protected targets;
- the encounter can transition from evacuation to combat containment.

Capability dependencies:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING if crowd/barrier zones have tactical effects;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

Reduced version:
Resolve evacuation in overworld/event state before battle instantiation. Close the affected zone, remove visitor cohorts from tactical participation and run a standard encounter on a static legal arena containing only actual combatants. No crowd tiles, escort NPCs, forced movement, barrier reactions or objective-aware pursuit are simulated.

## 18. Encounter contract B — Closing-Time Wildlife Return

Narrative premise:
After a temporary event begins teardown, wild Pokémon return to a space they normally use. Remaining equipment and people create a conflict over how quickly the site can be cleared.

Intended full version:
- dynamically shrinking occupied area;
- territorial/withdrawal-aware wild AI;
- changing equipment zones;
- possible weather or environmental interaction;
- noncombat withdrawal as a first-class tactical objective.

Capability dependencies:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if displacement matters;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING for dynamic equipment/environment zones;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for territorial withdrawal behavior;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

Reduced version:
Pause teardown and clear all staff/visitors from the relevant space. Represent the ecological conflict in world state first. If battle is unavoidable, instantiate only the legal combatants on a fixed perimeter map. Do not give wild actors invented territorial bonuses or custom withdrawal behavior. Continue teardown only after the authoritative result is returned.

## 19. Noncombat contract — Opening Gate Dependency Check

Narrative premise:
Shortly before opening, several event dependencies have unresolved state and only some can be addressed before the public arrives.

Execution:
- query current staffing, delivery, transit, accessibility, sanitation and site-condition refs;
- present only failures supported by real state;
- let authorized actors choose OPEN_AS_PLANNED, OPEN_LIMITED, DELAY_OPENING or a valid workaround;
- create Chronicle and handoff records;
- publish any schedule change through the Media/Communications layer.

No PTU battle capabilities are required.

## 20. PTU/Caelo and engine guardrails

This extension does not create:
- crowd combat modifiers;
- queue Skill checks;
- event-specific movement costs;
- panic status;
- weather damage;
- custom escort rules;
- temporary Trainer Features;
- contest scoring;
- tournament rules;
- item rewards;
- healing or food effects;
- capture modifiers;
- vendor prices.

Every tactical or mechanical effect must be validated by PTU/Caelo and supported by AutoPTU before use.

## 21. Minecraft mapping

Possible presentation:
- temporary stall structures;
- stage or activity overlays;
- changing signs/program boards;
- crowd cohorts represented by bounded NPC samples rather than thousands of entities;
- staff-only barriers;
- closed/open booth states;
- setup crates and teardown visuals;
- cleanup state;
- reopened base location after the event.

Minecraft should expose the server-owned event state. It must not become the authority for PTU rules or hidden operational simulation.

## 22. Promotion gate

Before any specific Ouros event becomes canon, review:
1. host institution and authority;
2. base location and temporary footprint;
3. recurrence/calendar ownership;
4. cultural/history claims;
5. activity mechanics;
6. vendor/service provenance;
7. accessibility and sanitation dependencies;
8. travel and visitor pressure assumptions;
9. ecology impact;
10. Minecraft presentation feasibility;
11. any combat dependency on currently PARTIAL or BLOCKING engine families.
