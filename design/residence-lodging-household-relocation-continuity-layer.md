# Residence, Lodging, Household and Relocation Continuity Layer

Status: DESIGN / NON-CANON ARCHITECTURE
Pass: 204
Date: 2026-09-02

## Purpose

Represent where persistent actors live, stay temporarily, receive residential access, move between accommodations and retain residential history without inventing Ouros property law, rent, family relations or PTU rest mechanics.

This layer extends existing canon facts about Marea homes and boarding rooms. It does not change any canonical residence established in `canon/`.

## Authority boundaries

Narrative owns:
- residence and lodging history;
- descriptive room/space identity;
- assignment provenance;
- temporary accommodation windows;
- observed occupancy;
- relocation workflow state;
- residential notices and forwarding references;
- physical room usability as a world fact when established by authored events;
- household/co-residence claims only when explicitly evidenced.

Narrative does not own:
- legal ownership;
- tenancy law;
- rent/prices;
- eviction rights;
- inheritance;
- family/romantic inference;
- healing/rest outcomes;
- inventory capacity;
- Minecraft respawn point authority;
- battle legality.

## Core distinction set

`RESIDENCE != CURRENT_POSITION`

`ROOM_ASSIGNMENT != OWNERSHIP`

`LODGING_ACCESS != PERMANENT_RESIDENCE`

`CO_RESIDENCE != FAMILY_RELATION`

`CO_RESIDENCE != SHARED_FINANCES`

`GUEST != HOUSEHOLD_MEMBER`

`KEY_OR_ACCESS_TOKEN != UNIVERSAL_ACCESS_RIGHT`

`BED_PRESENT != PTU_REST_COMPLETED`

`SLEEP_ANIMATION != PTU_SLEEP_STATUS`

`MINECRAFT_RESPAWN_POINT != CANONICAL_HOME`

`ENTITY_UNLOAD != RESIDENT_MOVED_OUT`

`ROOM_EMPTY_NOW != ROOM_UNASSIGNED`

`PERSONAL_EFFECT_PRESENT != PERSON_CURRENTLY_PRESENT`

`MOVE_PLANNED != MOVE_COMPLETED`

`MOVE_COMPLETED != OLD_ADDRESS_INSTANTLY_FORGOTTEN`

`TEMPORARY_DISPLACEMENT != PERMANENT_RELOCATION`

## Data model

### `residential_site`

```yaml
residential_site:
  residential_site_id: null
  location_id: null
  descriptive_type: null
  parent_building_or_site_ref: null
  room_or_space_refs: []
  current_world_state: AVAILABLE | LIMITED | UNAVAILABLE | UNKNOWN
  world_state_evidence_refs: []
  notes: []
```

`descriptive_type` is narrative metadata such as boarding room, staff quarter, private home, guest room or field bunk. It has no legal effect by itself.

### `residence_record`

```yaml
residence_record:
  residence_record_id: null
  actor_id: null
  residential_site_id: null
  room_or_space_ref: null
  residence_role: ORDINARY | INSTITUTIONAL | TEMPORARY | FIELD | DISPLACEMENT | OTHER
  status: PLANNED | ACTIVE | PAUSED | ENDED | CANCELLED | UNKNOWN
  valid_from: null
  valid_until: null
  assignment_source_ref: null
  authority_or_host_ref: null
  access_grant_refs: []
  possession_custody_refs: []
  notice_refs: []
  provenance_refs: []
```

An actor can have more than one active record when the roles genuinely coexist.

### `occupancy_observation`

```yaml
occupancy_observation:
  observation_id: null
  residential_site_id: null
  actor_ids_observed: []
  observed_at: null
  observer_ref: null
  method: null
  confidence: null
  provenance_ref: null
```

This records a bounded observation. It cannot promote itself into residence status.

### `residential_access_event`

```yaml
residential_access_event:
  access_event_id: null
  actor_id: null
  residential_site_id: null
  purpose: null
  access_scope: null
  valid_from: null
  valid_until: null
  issuer_or_host_ref: null
  source_ref: null
  status: OFFERED | ACTIVE | USED | EXPIRED | REVOKED | DECLINED | UNKNOWN
```

Use the identity/credential/delegated-authority layer for verification where needed. This record only preserves residential-purpose scope.

### `relocation_case`

```yaml
relocation_case:
  relocation_case_id: null
  actor_ids: []
  from_residence_refs: []
  to_residence_refs: []
  reason_claim_refs: []
  state: PROPOSED | PREPARING | IN_TRANSIT | ARRIVED | HANDED_OVER | COMPLETED | PAUSED | CANCELLED
  possession_transfer_refs: []
  service_request_refs: []
  transport_refs: []
  old_address_forwarding_refs: []
  event_history: []
  provenance_refs: []
```

No reason claim automatically becomes canonical motive. A move can be delayed, partial or cancelled.

### `household_claim`

```yaml
household_claim:
  household_claim_id: null
  actor_ids: []
  claimed_relationship_type: null
  source_ref: null
  status: REPORTED | CORROBORATED | DISPUTED | WITHDRAWN | UNKNOWN
  evidence_refs: []
```

Only create when household identity itself matters. Do not synthesize it from shared coordinates.

## Integration with current layers

### Rest/sleep/duty cycle

A residence may provide the narrative location for a rest attempt. The rest layer records intervals. PTU/AutoPTU decides mechanical recovery when an implemented resolver exists.

### Identity and delegated authority

A room assignment should reference persistent actor IDs. Display name, Minecraft username or visual skin cannot substitute for identity verification when access matters.

### Service request / capacity

Boarding rooms can use capacity slots if a future service owns reservations. Residence history must not duplicate the queue/service system.

### Market / transaction

If lodging later has a price, the transaction layer and authoritative economy own payment. `residence_record` only references the transaction.

### Mutual aid / relief

Temporary displacement accommodation can be offered through mutual-aid state. Receiving a room does not create debt, reputation or ownership.

### Building safety / reentry

A room can become temporarily unusable because a separately governed building-safety event established that state. This layer consumes the decision; it does not invent engineering conclusions.

### Material custody

Moving possessions uses existing item/custody provenance. Residence does not infer ownership from location alone.

### Information circulation

An old directory or notice may still list an ended residence. Publication state and actor knowledge remain separate from the canonical residential record.

## Canon application to Marea

Existing canon residence facts are consumed as initial records, not rewritten:
- Mara Veyra: Puerto Bruma boarding room near Field Office;
- Ivo Serrat: Puerto Bruma market street home;
- Dr. Nerea Sol: quarters at Estación Mirador;
- Taro Min: Puerto Bruma archive residence room;
- Sela Orrin: Puerto Bruma north boarding row.

Exact room numbers, legal tenure, payment, building ownership and household composition remain unresolved.

Secondary residents have settlement membership and workplaces in canon, but the canon file does not specify exact homes for all of them. Pass 204 does not invent those addresses.

## Minecraft/Cobblemon projection rules

Minecraft may render:
- doors;
- beds;
- rooms;
- storage props;
- nameplates;
- occupied/unoccupied visual states;
- resident actors;
- temporary repair state.

Minecraft may not decide:
- who legally or canonically lives there;
- whether an actor moved out;
- whether a guest became a household member;
- whether an item belongs to the resident;
- whether sleep produced PTU recovery;
- whether setting a spawn point creates residence;
- whether a destroyed/duplicated bed ends or creates a residential record.

Persist canonical state outside volatile block/entity state. Projection reconciles from Narrative authority.

## Residential continuity events

Useful events include:
- `RESIDENCE_ASSIGNED`
- `TEMPORARY_LODGING_OFFERED`
- `TEMPORARY_LODGING_ACCEPTED`
- `ROOM_BECAME_UNAVAILABLE`
- `ROOM_RETURNED_TO_SERVICE`
- `MOVE_PREPARATION_STARTED`
- `MOVE_DELAYED`
- `MOVE_ARRIVED`
- `OLD_ROOM_HANDED_OVER`
- `RESIDENCE_ENDED`
- `DIRECTORY_ENTRY_CORRECTED`
- `FORWARDING_REFERENCE_CREATED`

Every event should cite the source that established it.

## Quest grammar

Residence works best as continuity pressure, not a property-management minigame.

Good objective forms:
- verify which room assignment is current;
- deliver a notice to the actual current resident or forwarding location;
- help move a bounded item set after custody is established;
- resolve a temporary room conflict through existing service/authority rules;
- document an old residence before a building changes;
- prepare temporary accommodation after a verified disruption;
- compare a stale public directory with current records;
- revisit a former home and surface history without forcing emotional interpretation.

Avoid:
- arbitrary rent countdowns;
- hidden eviction meters;
- universal housing quality buffs;
- relationship gains for entering someone's room;
- automatic family inference;
- mandatory decorating grind;
- using a bed as quest-completion authority.

## Mechanically rich encounter pattern

### `Return Route to the Boarding Row`

Premise:
A resident has legitimate temporary accommodation in Puerto Bruma after a separately established route/service disruption. A bounded trip to recover personal field equipment from an accessible prior location encounters a localized wild threat on Sendero del Vidrio.

The residential premise remains outside BattleSpec.

### Full intended version dependencies

- targeting/footprints/range/LoS: required
- base movement legality: required
- complete movement including push/pull/knockback/interception/forced movement: required if protected withdrawal, escort spacing or displacement matters
- core calculations: required
- action economy/initiative: required
- full turn/round lifecycle: required for sustained objective behavior
- full stateful damage pipeline: required
- status lifecycle: required when selected content uses statuses
- terrain/weather/hazards/zones/reactions: required if route conditions materially affect tactics
- move-specific behavior: required
- abilities: required when selected actors use them
- items: required if battle Items participate
- Trainer Features/perks: required when selected Trainers use them
- AI legal-action infrastructure: required
- AI tactical policy: required if wild actors must prioritize territory/withdrawal or NPCs must protect an exit rather than maximize damage
- Minecraft/Cobblemon/Craftics adapter/playback support: required for full overworld-to-battle-to-world presentation

Disposition: FULL RICH VERSION BLOCKED under pass-204 live evidence.

### Reduced version

Narrative resolves before battle:
- current residence and temporary lodging records;
- reason and provenance for the recovery trip;
- identity of the equipment/custody holder;
- noncombatant safety state;
- current route context;
- destination after withdrawal.

Battle uses:
- one ordinary audited confrontation;
- stable geometry;
- audited combatants/content;
- no tactical weather/hazards unless independently verified;
- no forced-movement objective unless every selected interaction is contract-verified.

Allowed narrow handoffs:
- `IMMEDIATE_RECOVERY_ROUTE_CLEAR`
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_RESIDENT_CAN_WITHDRAW`

Battle output cannot determine:
- who owns a room;
- whether accommodation continues;
- household membership;
- property ownership;
- rent/payment;
- why a resident relocated;
- whether an old address remains valid for mail;
- entitlement to future lodging;
- emotional meaning of a home;
- PTU rest/healing.

## Implementation recommendation

Prototype `Room Assigned, Room Empty` first.

Use one existing canonical resident whose quarters are already established. Record that the room remains assigned while the resident is at work elsewhere. A delivery/notice can arrive at the residential site and later be received through a plausible handoff. The slice requires no battle, no new NPC, no new address, no price, no lease rule and no family inference.

This proves the central invariant: persistent residence survives absence and Minecraft entity unload.