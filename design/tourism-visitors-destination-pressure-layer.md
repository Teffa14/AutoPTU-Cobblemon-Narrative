# Ouros Tourism, Visitors & Destination Pressure Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already models routes, transport, food/hospitality, housing, events, media, conservation, museums, sacred sites, settlements and interregional movement. This layer connects them through temporary visitors and destination pressure.

The goal is to let places become popular, crowded, quiet, fashionable, overlooked, restored or overextended for traceable reasons without turning Ouros into a tourism-economy simulator.

## 1. Separate destination truth from visitor perception

```yaml
destination_profile:
  destination_id: null
  location_ids: []
  attraction_ids: []
  accommodation_ids: []
  transport_access_refs: []
  public_information_refs: []
  resident_service_refs: []
  ecological_sensitivity_refs: []
  heritage_or_sacred_refs: []
  current_visitor_pressure: NORMAL
  current_capacity_state: NORMAL
  active_event_refs: []
  current_disruption_refs: []
```

A destination can be safe but rumored dangerous, famous but currently inaccessible, or popular for a reason locals consider misleading.

## 2. Visitor relationship to place

```yaml
visitor_presence:
  actor_id: null
  destination_id: null
  presence_type: null
  arrival_event_id: null
  intended_departure_window: null
  accommodation_ref: null
  host_or_institution_ref: null
  purpose_refs: []
  known_information_refs: []
  itinerary_ref: null
  current_state: PRESENT
```

Candidate `presence_type` values:
- FIRST_TIME_VISITOR
- RETURNING_VISITOR
- EVENT_ATTENDEE
- COMPETITOR
- RESEARCH_VISITOR
- TEMPORARY_WORKER
- GUEST_OF_INSTITUTION
- HERITAGE_VISITOR
- PILGRIM only when an authored tradition supports it
- STRANDED_TRAVELLER

Visitor status does not imply citizenship, legal status, wealth, naivety or social class.

## 3. Accommodation is not residence

```yaml
accommodation_site:
  accommodation_id: null
  location_id: null
  operator_ids: []
  site_type: null
  capacity_band: null
  current_occupancy_band: null
  staff_capacity_ref: null
  service_dependency_refs: []
  accessibility_refs: []
  guest_policy_refs: []
  event_block_refs: []
  outage_or_disruption_refs: []
```

Candidate types:
- HOTEL
- INN
- HOSTEL
- LODGE
- RESORT
- CAMPGROUND
- DORM_GUEST_WING
- RESEARCH_STATION_GUEST_QUARTERS
- TEAM_BASE_GUEST_ROOM

A temporary stay must not create household membership, residency, property rights or social relationships.

## 4. Attraction object

```yaml
visitor_attraction:
  attraction_id: null
  location_id: null
  attraction_type: null
  operator_or_steward_ids: []
  access_state: OPEN
  visitor_information_refs: []
  capacity_band: null
  ecological_or_heritage_sensitivity_refs: []
  seasonal_window_refs: []
  event_refs: []
  reputation_refs: []
  current_pressure_band: LOW
  management_action_refs: []
```

Possible types include scenic site, museum, market district, competition venue, wildlife-viewing area, historic place, public works landmark, resort, festival district or guided trail.

The label does not create mechanical bonuses.

## 5. Visitor flow is causal

Visitor demand should be derived from actual world state.

```yaml
visitor_flow_driver:
  driver_id: null
  destination_id: null
  cause_type: null
  source_event_or_record_id: null
  audience_scope: null
  start_time: null
  decay_or_end_rule: null
  estimated_strength_band: null
```

Drivers may include:
- tournament or Contest;
- festival;
- media coverage;
- research publication;
- famous battle;
- restoration milestone;
- seasonal wildlife event;
- new route or transport service;
- newly opened ruin;
- famous trainer appearance;
- rumor or viral image.

No spontaneous crowd generation without a cause.

## 6. Pressure is multidimensional

Do not store one universal `tourism = 80` number.

```yaml
visitor_pressure_state:
  zone_id: null
  visitor_volume_band: null
  accommodation_pressure: null
  transport_pressure: null
  staff_pressure: null
  waste_or_maintenance_pressure: null
  habitat_disturbance_pressure: null
  resident_space_pressure: null
  queue_or_access_pressure: null
  safety_pressure: null
  evidence_refs: []
  last_reviewed_at: null
```

Pressure should be zone-specific. A busy town can coexist with a quiet protected valley.

## 7. Resident response is not one mood meter

```yaml
resident_response_record:
  actor_or_group_id: null
  destination_id: null
  observed_statement_or_action_refs: []
  issue_refs: []
  benefit_refs: []
  burden_refs: []
  policy_preference_refs: []
```

Do not infer that residents “hate tourists” or “love growth” from one event. Different businesses, households, conservation staff and institutions can hold different positions.

## 8. Visitor guide and itinerary

```yaml
visitor_guide_record:
  guide_id: null
  publisher_id: null
  destination_scope: []
  edition_date: null
  intended_audience: null
  attraction_refs: []
  route_refs: []
  warning_refs: []
  promotional_claim_refs: []
  omitted_or_redacted_refs: []
```

```yaml
itinerary:
  itinerary_id: null
  actor_or_group_ids: []
  planned_stop_ids: []
  reservation_or_booking_refs: []
  transport_refs: []
  fallback_refs: []
  current_state: PLANNED
```

A guide can be stale or promotional. An itinerary can fail without the geography changing.

## 9. Guide services

Local guides can be institutions, professionals, volunteers or informal contacts.

```yaml
guide_service:
  service_id: null
  provider_ids: []
  coverage_area_ids: []
  speciality_refs: []
  access_policy_refs: []
  schedule_refs: []
  current_capacity_band: null
  required_rules_refs: []
```

Narrative expertise does not grant PTU Skill bonuses. If a guide mechanically assists a Skill Check, use validated PTU/Caelo rules.

## 10. Visitor management actions

Possible narrative actions:
- timed entry;
- temporary closure;
- route redistribution;
- alternate viewing point;
- shuttle service;
- guided-only access;
- quiet window;
- seasonal closure;
- additional staff deployment;
- temporary accommodation expansion;
- information campaign;
- reservation system;
- emergency-only access.

These exist only when an authorized institution and canon policy support them. Do not invent legal powers.

## 11. Conservation bridge

Visitor pressure can interact with protected-area state, wild collectives and ecological observations.

Examples:
- repeated crowding near a nesting site;
- trail erosion near a migration corridor;
- wildlife changing time-of-day use around busy routes;
- visitors feeding Pokémon despite warnings;
- successful restoration making a previously quiet area famous.

Observed behavioral change does not automatically prove causation. Record the hypothesis and evidence separately.

## 12. Heritage and sacred-site bridge

A sacred or archaeological place can also attract visitors.

Keep separate:
- sacred meaning;
- archaeological evidence;
- local stewardship;
- tourism promotion;
- visitor behavior;
- public interpretation.

A visitor brochure must never become canonical theology or historical truth.

## 13. Event surge

Large events can temporarily change destination state.

```yaml
event_visitor_surge:
  event_id: null
  destination_id: null
  expected_arrival_band: null
  accommodation_effect_refs: []
  transport_effect_refs: []
  staffing_effect_refs: []
  vendor_effect_refs: []
  conservation_effect_refs: []
  post_event_cleanup_refs: []
```

This connects directly to Contest, battle-institution, festival, sports and public-memory layers.

## 14. Compression rule

Compress:
- ordinary check-in;
- routine meals already supported by hospitality;
- normal sightseeing with no meaningful choice;
- standard ticketing when policy and capacity are stable;
- routine checkout and departure.

Expand when:
- capacity becomes meaningful;
- a route or service fails;
- visitor activity intersects sensitive ecology;
- the player has a professional role in the destination;
- different visitor/resident interests collide;
- a public event changes normal operations;
- an attraction contains unresolved history or mystery;
- a recurring visitor relationship matters;
- a player deliberately chooses leisure or cultural participation.

## 15. Minecraft representation

Potential world-facing state:
- temporary visitor NPC density bands;
- queues represented by a small sample, not thousands of entities;
- event decorations;
- full/available accommodation signage;
- shuttle or ferry changes;
- temporary trail barriers;
- visitor-centre notices;
- changed shop hours;
- guided-tour meeting points;
- wildlife-viewing zones;
- crowd-noise ambience;
- post-event cleanup state.

The adapter must not decide mechanical rules.

## 16. PTU/Caelo boundary

This layer never invents:
- lodging/rest healing;
- hotel buffs;
- attraction bonuses;
- travel speed;
- crowd penalties;
- encounter-rate modifiers;
- Friendship/Loyalty gains;
- guide bonuses;
- Charm/Guile/Survival DCs;
- prices, taxes or tourism income formulas;
- pilgrimage blessings;
- weather or hazard effects.

Any exact mechanical interaction must use validated PTU/Caelo/AutoPTU behavior.

## 17. Encounter implementation contracts

### Scenic Ridge Closure

Narrative premise: a popular overlook must be cleared after route damage while visitors are redirected.

FULL version dependencies:
- complete movement including interception/forced movement if actors dynamically block routes;
- terrain/weather/hazards/zones/reactions for unstable terrain;
- AI tactical policy for retreat/protection behavior;
- Minecraft/Cobblemon/Craftics playback for physical barriers and visitor movement.

REDUCED version:
Visitors remain outside the tactical grid. Route closure and redirection resolve in overworld state. If hostile or wild Pokémon create a battle, AutoPTU receives a static legal arena.

### Resort Wildlife Disturbance

Narrative premise: unusual wild activity reaches the edge of a resort during peak occupancy.

FULL version dependencies:
- AI tactical policy for wildlife retreat/avoidance and staff protection priorities;
- complete movement/interception for evacuation lanes;
- terrain/weather/hazards if the environment changes;
- adapter/playback for guests and resort state.

REDUCED version:
Guests evacuate through world-state actions. A conventional battle occurs only if needed. Wildlife motive remains an investigation question, not a forced aggression label.

### Heritage Trail Bottleneck

Narrative premise: a famous trail becomes overcrowded during a seasonal event while a sensitive adjacent site must remain protected.

FULL version dependencies:
- complete movement/interception;
- terrain/zones/reactions for protected-space boundaries inside combat;
- AI tactical policy for route-aware actors;
- adapter/playback.

REDUCED version:
Visitor management, closures and rerouting occur outside combat. Any tactical encounter uses fixed blockers and a standard objective-neutral battle.

## 18. Canon questions

- Which Ouros regions deliberately promote tourism?
- Which locations are famous before the player arrives?
- What kinds of lodging exist by region?
- Do pilgrimages exist, and if so which authored traditions define them?
- Who can close or limit access to public/protected places?
- How much visitor data is private in multiplayer?
- Which destinations rely economically on visitors?
- How does tourism interact with wild Pokémon spawning without becoming an exploit system?
- How should offline visitor pressure advance?
- Which tourism states deserve numeric simulation versus qualitative bands?
