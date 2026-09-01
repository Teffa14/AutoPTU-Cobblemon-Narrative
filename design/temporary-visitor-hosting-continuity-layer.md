# Temporary Visitor and Hosting Continuity Layer

Status: DESIGN / PROPOSED ARCHITECTURE
Date: 2026-09-01
Canon effect: NONE until explicit promotion.
Research basis: `research/2026-09-01-temporary-visitors-lodging-hosting-scan-193.md`

## Purpose

Represent temporary visitors, repeat travelers, short stays, guest Pokémon, lodging assignments, local hosts, delayed departures, and narrow institutional access without turning every arrival into permanent residency or creating an unsupported hotel/immigration subsystem.

This layer reuses existing Ouros authority:

- ferry arrival/departure evidence remains with Lia/Mina and transport records;
- correspondence remains in the correspondence continuity layer;
- found property remains in salvage/found-property continuity;
- provisioning remains in stock/provisioning continuity;
- searches remain in field-search continuity;
- institutional access remains owned by the institution involved;
- relationships remain persistent relationship history;
- PTU mechanics remain authoritative outside Narrative.

It owns only temporary-presence continuity and the links between those systems.

## Canon anchors

Current canon already establishes:

- boarding rooms around Puerto Bruma Market Street;
- Mara's boarding room near the Field Office;
- Sela's home in the north boarding row;
- ferry landing traffic connecting Puerto Bruma outward;
- Lia recording arrivals/departures;
- Mina operating short ferry runs;
- Ivo as a future bridge into hospitality arcs;
- no canonized external ferry destination yet.

This architecture must not invent a hotel, room count, proprietor, rates, lodging law, border authority, or external settlement.

## Core records

### `temporary_presence_case`

```yaml
temporary_presence_case:
  case_id: null
  person_or_group_refs: []
  pokemon_refs: []
  stated_origin_claim_ref: null
  stated_purpose_claim_ref: null
  host_contact_ref: null
  expected_arrival_ref: null
  observed_arrival_ref: null
  expected_departure_ref: null
  observed_departure_ref: null
  current_presence_state: EXPECTED | PRESENT_CONFIRMED | DEPARTED_CONFIRMED | UNKNOWN | CANCELLED
  stay_refs: []
  access_grant_refs: []
  open_errand_refs: []
  provenance_refs: []
```

A stated origin or purpose is initially an attributed claim unless canon or evidence independently validates it.

### `stay_assignment`

```yaml
stay_assignment:
  stay_id: null
  guest_refs: []
  space_ref: null
  assignment_window:
    begins_at: null
    ends_at_expected: null
    ends_at_actual: null
  assignment_state: HELD | ACTIVE | EXTENDED | COMPLETED | CANCELLED | NO_SHOW
  assigning_authority_ref: null
  occupancy_evidence_refs: []
  companion_accommodation_notes: []
  resource_allocation_refs: []
  custody_refs: []
```

`HELD` means capacity was reserved. It does not prove arrival.

### `temporary_access_grant`

```yaml
temporary_access_grant:
  grant_id: null
  subject_ref: null
  institution_ref: null
  scope: []
  granted_by_ref: null
  effective_from: null
  effective_until: null
  conditions: []
  revocation_or_expiry_ref: null
  provenance_refs: []
```

This record expresses narrow local permission only. It does not create a PTU Feature, government credential, membership, employment, or ownership.

### `visit_contact_event`

```yaml
visit_contact_event:
  contact_id: null
  visitor_ref: null
  local_actor_refs: []
  location_ref: null
  occurred_at: null
  observations: []
  claims_received: []
  commitments_created: []
  relationship_history_refs: []
```

Repeated contacts can accumulate history across separate visits.

## Hard boundaries

`EXPECTED_ARRIVAL != ARRIVED`

`FERRY_ARRIVED != PERSON_CONFIRMED_PRESENT`

`ROOM_HELD != ROOM_OCCUPIED`

`ROOM_OCCUPIED != RESIDENCY`

`REPEAT_VISITOR != RESIDENT`

`TEMPORARY_ACCESS != INSTITUTIONAL_MEMBERSHIP`

`HOST_CONTACT != LEGAL_GUARDIAN`

`VISITOR_CLAIM != REGIONAL_TRUTH`

`DEPARTURE_DELAYED != MISSING_PERSON`

`OVERSTAY != WRONGDOING`

`GUEST_POKEMON_PRESENT != HOST_OWNS_POKEMON`

`TRAINER_REQUEST != POKEMON_PREFERENCE`

`MINECRAFT_BED_BINDING != CANONICAL_LODGING_ASSIGNMENT`

`ENTITY_UNLOAD != DEPARTURE`

## Arrival sequence

A robust visit can progress through:

1. expected arrival or informal notice;
2. transport evidence becomes available;
3. physical presence is confirmed separately;
4. stay assignment activates if one exists;
5. host/contact or institution records narrow permissions;
6. ordinary visit activity occurs;
7. plans may change;
8. actual departure is observed or remains uncertain;
9. unresolved property, correspondence, promises, or records persist after departure.

Not every visit needs every phase.

## Repeat-visitor continuity

A repeat visitor retains:

- stable identity when known;
- previous contact history;
- what they legitimately learned;
- promises and unresolved errands;
- prior institutional access history;
- observed companion relationships;
- previous disputes or cooperation;
- previous stated claims with dates and provenance.

A new visit does not automatically reuse expired access or assume unchanged purpose.

## Guest Pokémon

Visiting Pokémon are persistent actors when individually identified.

Narrative may store:

- observed comfort/discomfort;
- known relationship to a Trainer or other person;
- authored accommodation needs;
- observed routine;
- explicitly established food/care constraints;
- temporary separation incidents.

Narrative may not infer mechanical needs from species alone or grant PTU recovery/bonuses from lodging without source and engine support.

If a Trainer and Pokémon become separated near expected departure, the field-search layer decides whether verification escalates to a search. The hosting layer merely supplies expected-presence and last-confirmed-contact evidence.

## Institutional visitors

### Tideglass

A visiting historian/researcher can receive access only to material Taro or another authorized actor may legitimately expose. Temporary presence never unlocks protected records.

### Estación Mirador

A visiting observer can be allowed to attend or assist a specific activity without acquiring project authority, raw-data access, or permanent station membership.

### Bruma Battle Yard

A visiting Trainer can watch, request a session, or receive a challenge contract. Presence does not guarantee a battle, ranking, reward, or rival status.

### Marea Field Office

A visitor can request practical assistance. The Field Office does not become immigration enforcement or a universal registration authority.

### Loma Clara Cooperative

A visitor can meet producers or observe approved activity without representing the cooperative or gaining access to private holdings.

## Capacity and service consequences

The layer should support small persistent effects without inventing economy rules:

- a held room remains unavailable during the actual hold window;
- an extension can conflict with another proposed assignment;
- meal planning can reference confirmed guest count without creating a new food buff;
- delayed ferry service can extend a stay;
- a cancelled arrival can release capacity;
- property left behind opens custody handling;
- a returned visitor can recognize changed procedures or spaces.

No global `hospitality_score` is required.

## Information from outsiders

Visitors are useful for expanding Ouros gradually, but their dialogue must not canonize unseen places accidentally.

Example:

A traveler says a coastal route was rough last week.

Store:

```yaml
claim:
  speaker_ref: visitor_id
  claim_type: TRAVEL_CONDITION
  target_ref: unresolved_external_route_claim
  observed_or_heard: SPEAKER_ASSERTION
  timestamp: null
```

Do not create a named external route, exact geography, or verified weather event until canon review establishes it.

## Minecraft/Cobblemon projection

Minecraft actors project authoritative presence records.

Rules:

- spawning an NPC in a room cannot create a stay assignment;
- sleeping in a bed cannot create residency;
- chunk unload cannot close a visit;
- entity death cannot author departure or death;
- duplicate actors must collapse to the same persistent identity or be rejected;
- a visual suitcase/crate does not create inventory ownership;
- a Pokémon following a visitor does not by itself prove ownership, only observable association unless canon says more;
- room doors, signs, beds, and containers are presentation surfaces, not authority.

## Battle integration

Most visitor content should remain noncombat.

If a visit intersects a threat, the visitor, luggage, accommodation state, access grant, and social consequences should remain Narrative-owned unless a verified BattleSpec contract explicitly supports them.

### Full concept contract

A route scene protecting a visitor may depend on:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including interception and forced displacement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions;
- exact move behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics playback.

Do not call that runnable while required families remain partial/blocking.

### Reduced contract

Keep visitor position semantics, baggage, escort, route purpose, and departure plan in Narrative. Move the visitor to a safe Narrative state before battle assembly. Compile only the remaining immediate wild threat into an ordinary audited BattleSpec on stable geometry.

Allowed narrow handoffs can include:

- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_PASSAGE_CLEAR`

Battle output must not decide:

- whether the visitor stays or leaves;
- residence;
- lodging rights;
- institutional access;
- relationship gain;
- truth of outsider claims;
- ownership of possessions;
- whether a guest Pokémon prefers the host or Trainer;
- whether a visitor becomes a rival, member, employee, or citizen.

## Relationship use

Temporary visitors can generate durable social history without forcing permanent settlement.

Good persistence signals:

- remembering a previous conversation;
- noticing a changed procedure on a later visit;
- following up on an unresolved promise;
- bringing back a corrected record;
- choosing a different local contact because of earlier experience;
- a Pokémon showing familiar behavior toward a known local actor, when authored/observed rather than inferred.

## Canon promotion gate

Before any visitor concept becomes canon, resolve only what that slice needs. Do not globally decide:

- who owns Puerto Bruma boarding rooms;
- how many rooms exist;
- exact rates or payment;
- Caelo residency law;
- identification requirements;
- visitor taxes;
- border authority;
- external ferry destinations;
- universal institutional guest policy.

The layer can operate with local, attributed, scoped facts while those questions remain open.