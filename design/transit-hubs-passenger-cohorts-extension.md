# Ouros Transit Hubs, Passenger Cohorts & In-Transit Scene Extension

Status: Proposed systems design extension. Not established Ouros canon.

Parent systems:
- `design/travel-transport-expedition-layer.md`
- `design/interregional-mobility-recognition-layer.md`
- `design/observation-settlement-time-layer.md`
- `design/crisis-rescue-recovery-layer.md`
- `design/case-authority-custody-layer.md`

## Purpose

Ouros already models physical connections, route state, transport services, journeys, expeditions, regional arrival context and visitor influx. This extension defines what happens when a transport hub or vehicle becomes socially important enough to expand into a playable scene.

The design target is selective persistence. A ferry can feel occupied without storing every passenger forever. A train can create a recurring cast without forcing conversation every trip. A terminal can respond to delays, events and ecology without becoming a border checkpoint.

## Ownership boundary

Travel owns route viability, journey state, schedules and transport-service operation.

Interregional Mobility owns regional transition context, host-region recognition and visitor state.

Crisis owns emergency state and recovery.

Case owns evidence, testimony and custody.

Care owns medical treatment and welfare state.

Material Culture owns cargo/item provenance and supply chains.

This extension owns only temporary co-presence, scene expansion and journey-contact persistence.

It does not establish ticket prices, legal authority, immigration, customs, vehicle capacity math, combat evacuation rules or PTU modifiers.

## Transit hub state

```yaml
transit_hub_state:
  hub_id: null
  location_id: null
  service_ids: []
  current_operating_band: normal|busy|delayed|disrupted|limited|closed|restoring
  active_arrival_ids: []
  active_departure_ids: []
  aggregate_passenger_pressure: low|normal|high|severe|unknown
  representative_actor_ids: []
  crew_or_staff_ids: []
  active_information_ids: []
  active_disruption_ids: []
  current_scene_refs: []
  last_state_event_id: null
```

Passenger pressure is an aggregate world-state signal. It is not a literal entity count and does not create combat crowd mechanics.

## Passenger cohort

```yaml
passenger_cohort:
  cohort_id: null
  journey_id: null
  service_id: null
  boarding_hub_id: null
  destination_hub_ids: []
  aggregate_size_band: small|moderate|large|unknown
  representative_actor_ids: []
  recurring_actor_ids: []
  relevant_profession_tags: []
  relevant_commitment_ids: []
  known_shared_context_ids: []
  current_pressure_state: normal
  promoted_contact_ids: []
  expires_after_journey: true
```

A cohort is a scene abstraction. Most members disappear from active state after the journey because nothing made their exact identity important.

## Actor promotion threshold

A passenger becomes a persistent actor/contact when at least one authored condition applies:

- the player deliberately forms a relationship or commitment;
- the passenger becomes a witness or case participant;
- their professional capability matters to an event;
- they provide or receive a meaningful service;
- they are a recurring worker or regular traveler;
- they become a rival, collaborator, client, guide or specialist through actual events;
- a Chronicle-worthy consequence refers to this exact person.

Incidental small talk alone should not create permanent graph noise.

## Recurring journey contact

```yaml
journey_contact:
  contact_id: null
  actor_id: null
  route_or_service_ids: []
  first_met_journey_id: null
  subsequent_journey_ids: []
  shared_event_ids: []
  public_role_tags: []
  current_commitment_ids: []
  current_availability: unknown
  last_seen_location_id: null
  relationship_claim_refs: []
```

`relationship_claim_refs` must follow the existing social-bond consent/evidence rules. Co-travel does not prove friendship, trust, romance or rivalry.

## In-transit scene

```yaml
in_transit_scene:
  scene_id: null
  journey_id: null
  service_id: null
  vehicle_or_hub_location_ref: null
  participant_actor_ids: []
  passenger_cohort_id: null
  trigger_state_ids: []
  scene_type: social|investigation|care|coordination|disruption|optional_hook|observation|combat_handoff
  player_decision_refs: []
  active_clock_ids: []
  persistent_output_refs: []
  mechanics_review_required: false
  resolved: false
```

The scene is expanded only if a meaningful decision exists.

## Scene expansion test

Expand transit when one or more of these are materially true:

```yaml
transit_scene_significance:
  player_chosen_engagement: false
  schedule_or_deadline_intersection: false
  case_or_testimony_intersection: false
  care_or_welfare_intersection: false
  relationship_callback: false
  specialist_or_mobile_service_present: false
  disruption_requires_choice: false
  route_ecology_revealed: false
  optional_followup_possible: false
  hub_or_service_state_can_change: false
```

If all values are false, use Travel compression.

## Temporary community rule

A vehicle can briefly operate like a tiny settlement, but only at the scene level.

Possible roles include:
- crew/operator;
- maintenance staff;
- regular commuter;
- visiting researcher;
- nursery/care worker;
- courier;
- traveling artisan;
- performer;
- merchant;
- student;
- event participant;
- tourist;
- local resident using routine transport.

The generator should pick only roles supported by actual route, institution, event or actor state. It should not populate every sailing with a random dramatic ensemble.

## Mobile profession pattern

Some services plausibly move with a route instead of belonging to one settlement.

Candidate narrative patterns:
- traveling repair specialist;
- mobile exhibit or performance worker;
- rotating field researcher;
- courier or document carrier;
- seasonal vendor;
- relief or care worker moving between facilities;
- survey crew;
- transport-employed guide.

Mechanical services remain governed by their parent systems. A traveling craftsperson does not gain invented recipes; a care worker does not create healing effects.

## Transit testimony window

A bounded trip can support an investigation without becoming a detective minigame.

```yaml
transit_testimony_window:
  scene_id: null
  case_id: null
  departure_time: null
  expected_arrival_time: null
  witness_actor_ids: []
  available_observation_refs: []
  conflicting_claim_refs: []
  privacy_constraints: []
  followup_contact_refs: []
```

Important separation:
- observation;
- interpretation;
- rumor;
- deliberate claim;
- canonical truth.

Arrival ending the immediate interview window does not erase unresolved leads.

## Disruption-to-discovery pattern

Transport failure should not default to waiting or combat.

```text
service disruption
-> reveal existing alternate location / ecology / infrastructure / actor dependency
-> offer reroute, delay, assistance, investigation or optional exploration
-> update service state based on actual resolution
```

Examples of safe narrative outputs:
- discover a maintenance access route;
- learn why a harbor is blocked;
- meet a small alternate operator;
- observe seasonal Pokémon behavior at an unscheduled stop;
- find a stranded worker or researcher;
- expose a supply-chain dependency;
- create a deadline choice about waiting versus rerouting.

## First-trip / repeat-trip asymmetry

A route can expand on first use because the player is learning its spatial and social grammar.

Later travel should compress unless something changed.

Persistent callbacks can include:
- familiar crew greeting the party;
- a regular passenger no longer appearing;
- a repaired cabin or platform;
- a previously delayed service returning to normal;
- a recurring mobile specialist now serving another stop;
- an old journey contact boarding again;
- a route notice referencing a prior disruption.

Do not replay the same onboard scene verbatim.

## Vehicle spatial grammar

Large transport assets can contain authored sublocations when useful:
- boarding area;
- passenger cabin/deck;
- observation area;
- crew workspace;
- service/storage space;
- maintenance access;
- cargo area;
- restricted operational space when authored.

These are world locations. They do not imply tactical zones or movement penalties.

## Minecraft / Cobblemon representation

Prefer a representative population instead of hundreds of entities.

Useful representations:
- named crew on schedules;
- a small changing passenger sample;
- aggregate crowd ambience/visuals where supported;
- arrival/departure boards;
- visibly delayed or cancelled services;
- staged luggage/cargo tied to actual state;
- barriers or closed access only when world state supports them;
- repeated route workers with persistent identity;
- changed signage after a resolved disruption;
- alternate operator NPCs appearing only when their service is active.

Minecraft presentation must reflect server-owned narrative state. It must not independently decide PTU battle consequences.

## Encounter contract — Broken-Deck Containment

Status: proposed encounter pattern, not canon.

Narrative premise:
A transport incident leaves a bounded deck or platform unsafe while a frightened or hostile Pokémon subgroup remains nearby. The party's broader goal is to make the service area safe and prevent escalation around civilians and cargo.

Full intended version dependencies:
- targeting / footprints / range / LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push / pull / knockback / interception / forced movement — BLOCKING if shifting cargo, falls or protective interception matter tactically;
- core calculations — VERIFIED;
- action economy / initiative — VERIFIED;
- full turn / round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain / weather / hazards / zones / reactions — BLOCKING for damaged-floor zones, moving hazards or reactive protection;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features / perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for withdrawal, territorial defense or civilian-aware priorities;
- Minecraft / Cobblemon / Craftics adapter and playback — BLOCKING.

Reduced executable form:
Evacuate passengers and secure loose cargo through overworld/world-state resolution before battle begins. Instantiate only the immediate opposing subgroup on a static legal deck/platform arena. No sliding cargo, forced displacement, collapse, environmental damage, civilian units or custom protection reactions. After authoritative combat resolution, update the transport service to `limited`, `restoring` or `operating` through narrative state.

## Encounter contract — Last-Leg Witness Window

Status: proposed noncombat scene pattern, not canon.

Narrative premise:
Several passengers witnessed different fragments of an event before boarding. The journey provides a limited period to compare testimony before everyone separates at arrival.

Battle dependencies:
None required by premise.

Implementation dependencies:
- Case layer evidence/claim separation;
- journey clock / arrival state;
- persistent actor/contact promotion for relevant witnesses;
- Minecraft/adapter presentation for onboard actors remains BLOCKING for full in-world execution.

Reduced form:
The same scene can run through text/state orchestration without spatial passenger AI. Present only the authored witnesses and the departure-to-arrival clock. Store statements as claims, never canonical truth.

## Generation guardrails

1. Do not expand routine travel only to create content volume.
2. Do not persist every passenger.
3. Do not create a border checkpoint because a route crosses regions.
4. Do not infer criminal suspicion from travel status.
5. Do not turn crowd descriptions into combat terrain without engine support.
6. Do not make civilians tactical tokens merely to raise stakes.
7. Do not invent ticket costs, vehicle capacity, safety checks or legal authority.
8. Do not guarantee friendship because actors shared a trip.
9. A disruption needs a causal world-state source.
10. Later journeys should remember prior service and contact history without replaying old scenes.

## Canon boundary

This extension defines reusable data and narrative grammar only. It establishes no Ouros ferry company, railway, aircraft, port, region boundary, law, named route or vehicle. Concrete services remain proposals until canon review.