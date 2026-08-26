# Ouros Pilgrimage & Sacred Routes Layer

Status: Proposed systems design. Not established Ouros canon.

This layer extends, rather than replaces, the existing Myth/Archaeology, Travel, Seasonality, Conservation, Hospitality and Public Memory layers.

## Purpose

A culturally important journey should persist as more than a quest marker between two ruins. Ouros needs a route-level object that can connect several settlements, sites, stewards and seasonal states while keeping physical access, cultural meaning and supernatural claims separate.

## 1. Sacred route object

```yaml
sacred_route:
  route_id: null
  display_name: null
  tradition_ids: []
  community_ids: []
  connection_ids: []
  station_ids: []
  steward_ids: []
  route_claim_ids: []
  historical_claim_ids: []
  mythic_claim_ids: []
  customary_sequence_ids: []
  public_access_state: null
  seasonal_state_ids: []
  ecology_dependency_ids: []
  service_ids: []
  active_conflict_ids: []
  public_memory_ids: []
  provenance: []
```

The route does not prove that its traditional explanation is historically or metaphysically true.

## 2. Route station

```yaml
sacred_route_station:
  station_id: null
  route_id: null
  location_id: null
  station_type: null
  steward_ids: []
  local_tradition_ids: []
  archaeological_site_ids: []
  heritage_object_ids: []
  ecology_state_ids: []
  service_ids: []
  access_policy_ids: []
  customary_practice_ids: []
  observation_ids: []
  visit_state_ids: []
```

Candidate station types:
- WAYMARK
- SHRINE_OR_MEMORIAL if canon supports that identity
- COMMUNITY_HALL
- OVERLOOK
- SPRING_OR_WATER_SITE
- OLD_BRIDGE
- RUIN
- REST_HOUSE
- ARCHIVE_OR_MUSEUM
- CONSERVATION_GATE
- TERMINUS

A station can have ordinary civic functions in addition to cultural significance.

## 3. Physical route state stays authoritative in Travel

The Sacred Route layer references `travel_connection` and `route_state`; it does not create a second movement graph.

A segment may be:
- physically open but culturally restricted;
- physically blocked while the tradition remains active through an alternate route;
- seasonally closed for ecology or safety;
- open to residents but limited for large visitor groups;
- accessible only through a service that is currently suspended.

## 4. Cultural route state

```yaml
cultural_route_state:
  route_id: null
  participation_state: null
  active_period_id: null
  current_steward_notice_ids: []
  temporary_restriction_ids: []
  alternate_practice_ids: []
  active_public_event_ids: []
  last_changed_event_id: null
```

Suggested participation states:
- ORDINARY
- PREPARATION
- ACTIVE_SEASON
- LIMITED
- TEMPORARILY_SUSPENDED
- EMERGENCY_ACCESS_ONLY
- RECOVERY

These states are social scheduling data, not battle mechanics.

## 5. Journey participation record

Use the Travel layer's `journey` as the physical trip. Add a cultural participation record only when the journey matters to the route's social history.

```yaml
route_participation:
  participation_id: null
  route_id: null
  journey_id: null
  participant_ids: []
  declared_purpose: null
  station_visit_ids: []
  steward_interaction_ids: []
  customary_practice_event_ids: []
  assistance_event_ids: []
  restriction_encounter_ids: []
  completion_state: null
  public_record_state: null
```

Completion has no automatic PTU reward.

## 6. Station visits are revisitable state

```yaml
route_station_visit:
  visit_id: null
  station_id: null
  actor_ids: []
  timestamp: null
  route_state_snapshot_id: null
  observations_added: []
  knowledge_updates: []
  service_events: []
  stewardship_events: []
  public_memory_events: []
  unresolved_hooks: []
```

A later visit should be able to reveal changed ecology, repairs, new interpretations, new staff, altered access or consequences of earlier choices.

## 7. Customary sequences

Some traditions may expect stations to be visited in a particular order. Store that as cultural practice.

```yaml
customary_sequence:
  sequence_id: null
  route_id: null
  tradition_id: null
  station_order: []
  timing_conditions: []
  stated_meaning_claim_ids: []
  optional_variants: []
  access_dependencies: []
```

Following or breaking the sequence can have social consequences when supported by actor beliefs. It does not create hidden buffs or supernatural penalties.

## 8. Stewardship decisions

Route stewards can create persistent decisions:
- close a segment;
- redirect visitors;
- request maintenance;
- limit group size;
- open a public day;
- coordinate emergency passage;
- move an observance to an alternate location;
- request ecological monitoring;
- document damage;
- negotiate with public works or researchers.

Every change should cite an event or reason state.

## 9. Visitor pressure

Visitor interest can interact with existing Tourism, Hospitality and Conservation systems.

Track consequences through those systems rather than inventing a sacred-route economy.

Potential effects include:
- booked lodging;
- temporary vendors;
- trail wear;
- litter or sanitation demand;
- crowding;
- local employment;
- quieter alternate routes;
- resident complaints;
- public transport changes.

Exact prices, income and mechanical bonuses remain outside this layer.

## 10. Interpretation across stations

A route can be historically coherent, partly reconstructed or entirely modern in its current form.

Use existing `historical_claim`, `mythic_claim`, `archaeological_observation` and `public_memory` objects.

Never infer that two similar markers prove one ancient network.

## 11. Route-wide mystery grammar

Useful mystery structures:
- a marker appears to be out of sequence;
- two towns preserve different route orders;
- an older segment is found beneath a modern bypass;
- a station name survives after the physical structure is gone;
- a seasonal ecological event explains an old travel custom without proving its mythic explanation;
- a modern restoration accidentally erases useful context;
- a steward archive contradicts a popular tourist narrative.

The resolution may remain contested.

## 12. Encounter implementation contract

A route scene must declare whether its environmental description has tactical meaning.

For any mechanically rich route encounter, record:
- intended full version;
- reduced currently executable version;
- exact permanent capability categories required;
- engine evidence date;
- any PTU/Caelo rule citation needed before implementation.

Narrative facts such as wind, steep paths, floodwater, loose rock or a crowd do not become tactical effects automatically.

## 13. Default reduced encounter pattern

Until terrain/weather/hazards, forced movement and tactical AI are verified, route conflicts should prefer:
- static legal battle terrain;
- ordinary verified movement;
- no environmental damage inferred from description;
- no forced movement caused by wind/current/collapse;
- rescue, evacuation or route-clearing objectives resolved as overworld state or authored interactions outside the battle grid;
- battle participants restricted to the immediate hostile subgroup.

This keeps the narrative premise intact without duplicating missing PTU rules in Minecraft.

## 14. Canon boundary

This layer establishes only a reusable schema.

It does not establish:
- a religion for Ouros;
- a specific pilgrimage tradition;
- an ancient civilization;
- Legendary involvement;
- ritual efficacy;
- ownership of sacred sites;
- legal authority of stewards;
- route names;
- historical truth behind any proposed tradition.

All named examples remain proposals until explicit canon review.