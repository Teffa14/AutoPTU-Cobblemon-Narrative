# Evacuation Shelter, Reunification & Departure Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Pass: 128

## Purpose

Crisis/Rescue already owns evacuation, staging, shelter sites, missing-actor cases and immediate life-safety response. Residential already owns normal residence, displacement and return-to-home continuity. Family/Kinship owns explicit relationship facts. Pokémon Agency owns persistent Pokémon identity, association and custody.

This extension fills the operational gap between those owners. It preserves who was recorded where and when, who became separated, what search or contact evidence exists, which reunifications actually occurred, and how actors left temporary sheltering.

It does not invent shelter law, guardianship, custody, emergency powers, family relationships, medical authority or Pokémon ownership.

## 1. Authority boundaries

Crisis/Rescue owns:

- hazard truth;
- evacuation scope;
- shelter/staging activation;
- rescue/search priorities;
- immediate life-safety decisions.

Residential owns:

- normal residence;
- household state;
- displacement;
- permanent or temporary relocation;
- return-to-home review.

Family/Kinship owns:

- confirmed human relationship facts;
- player-consent boundaries;
- authored guardianship claims where a governing system exists.

Pokémon Agency owns:

- persistent Pokémon identity;
- association;
- current custodian;
- residence;
- active Trainer;
- transfer/release/rehoming events.

Pokémon Shelter/Sanctuary owns:

- its own Pokémon placement-program intake;
- shelter-program reunification/rehoming/release workflows.

Care owns health/treatment truth.

Travel owns journeys and route use.

Communications/Public Notices own message delivery and publication.

Community Aid owns volunteer/helper workflow.

AutoPTU owns battle mechanics.

This extension stores continuity among those systems.

## 2. Core separations

These states must remain distinct:

`EVACUATION_INSTRUCTION != ACTUAL_DEPARTURE`

`ACTUAL_DEPARTURE != SHELTER_ARRIVAL`

`SHELTER_REGISTRATION != CURRENT_PRESENCE`

`CURRENT_PRESENCE != SAFE_TO_DISCLOSE_LOCATION`

`SEARCH_LEAD != LOCATION_VERIFIED`

`LOCATION_VERIFIED != CONTACT_ESTABLISHED`

`CONTACT_ESTABLISHED != PHYSICAL_REUNIFICATION`

`PHYSICAL_REUNIFICATION != CUSTODY_TRANSFER`

`SHELTER_DEPARTURE != DESTINATION_ARRIVAL`

`DESTINATION_ARRIVAL != RETURN_HOME`

`SAME_SPECIES != SAME_POKEMON`

`KNOWN_COMPANION != OWNER`

`HOUSEHOLD_MEMBER != FAMILY_RELATION`

## 3. Shelter population episode

Use the Crisis shelter as the physical/operational owner and attach time-scoped presence history.

```yaml
shelter_population_episode:
  population_episode_id: null
  crisis_shelter_ref: null
  actor_or_pokemon_id: null
  entity_kind: human|pokemon
  arrival_time_claims: []
  verified_arrival_event_ref: null
  registration_event_refs: []
  current_presence_state: UNKNOWN
  last_presence_observation_ref: null
  accommodation_zone_ref: null
  care_transfer_refs: []
  departure_event_refs: []
  visibility_scope_ref: null
  history_event_refs: []
```

Suggested presence states:

- UNKNOWN
- REPORTED_EN_ROUTE
- ARRIVAL_REPORTED
- PRESENT_VERIFIED
- TEMPORARILY_OFFSITE
- TRANSFERRED
- DEPARTED
- PRESENCE_UNCONFIRMED_AFTER_GAP

A printed roster is a historical record. It must not overwrite later observed departure.

## 4. Registration event

```yaml
shelter_registration_event:
  registration_event_id: null
  shelter_ref: null
  subject_id: null
  timestamp: null
  registrar_actor_or_system_ref: null
  information_received_refs: []
  identity_evidence_refs: []
  relationship_claim_refs: []
  stated_origin_ref: null
  intended_contact_refs: []
  privacy_scope_ref: null
  registration_status: RECORDED
```

Registration records what was supplied at that time.

It does not prove:

- current physical presence forever;
- legal identity beyond supporting evidence;
- family relationship;
- guardianship;
- ownership of a Pokémon;
- residence;
- health state;
- permission to disclose location.

## 5. Separation record

```yaml
separation_record:
  separation_id: null
  subject_a_id: null
  subject_b_id: null
  established_relation_ref: null
  relation_claim_ref: null
  last_verified_together_event_ref: null
  separation_trigger_ref: null
  expected_meeting_point_ref: null
  expected_destination_refs: []
  opened_at: null
  status: OPEN
  inquiry_refs: []
  resolution_ref: null
```

Possible status values:

- OPEN
- CONTACT_ESTABLISHED
- LOCATION_ESTABLISHED
- REUNIFICATION_PENDING
- REUNITED
- CLOSED_WITHOUT_REUNION
- SUPERSEDED

The system may track separation between actors whose relationship is unknown. It must not fabricate a family label to make the record easier to display.

## 6. Reunification inquiry

```yaml
reunification_inquiry:
  inquiry_id: null
  separation_id: null
  requester_id: null
  requested_subject_id_or_description_ref: null
  requester_relationship_claim_ref: null
  requester_authority_ref: null
  submitted_at: null
  search_scope_refs: []
  disclosure_scope_ref: null
  current_state: OPEN
  lead_refs: []
  verified_contact_ref: null
  closure_ref: null
```

Suggested states:

- OPEN
- INFORMATION_REQUIRED
- SEARCHING
- CANDIDATE_FOUND
- LOCATION_VERIFIED_RESTRICTED
- CONTACT_PENDING
- CONTACT_ESTABLISHED
- CLOSED
- WITHDRAWN

A requester can legitimately know that contact occurred without receiving the other actor's exact current location if privacy/authority state does not permit disclosure.

## 7. Location and contact evidence

```yaml
reunification_evidence:
  evidence_id: null
  subject_id: null
  evidence_kind: shelter_record|transport_record|message|direct_observation|camera_detection|witness_report|care_transfer|pokemon_identity_record|other
  observed_or_recorded_time: null
  location_ref: null
  source_ref: null
  identity_confidence: unresolved
  current_location_confidence: unresolved
  disclosure_scope_ref: null
  superseded_by_refs: []
```

Old evidence stays valid for what it proved at its timestamp.

A 14:00 shelter check-in does not become false because the actor departed at 15:00.

## 8. Contact event

```yaml
verified_contact_event:
  contact_event_id: null
  actor_a_id: null
  actor_b_id: null
  contact_kind: message_delivered|two_way_message|voice_contact|visual_contact|physical_contact|authorized_intermediary_contact|other
  timestamp: null
  location_refs: []
  verification_refs: []
  information_shared_scope_ref: null
  physical_reunion_created: false
```

A delivered message is not two-way communication.

Two-way communication is not physical reunion.

Visual contact across a restricted area is not permission to cross it.

## 9. Physical reunification event

```yaml
physical_reunification_event:
  reunification_event_id: null
  subject_ids: []
  timestamp: null
  location_id: null
  separation_refs: []
  verification_refs: []
  movement_or_handoff_refs: []
  custody_change_ref: null
  residence_change_ref: null
  followup_destination_refs: []
```

Physical reunion records co-location after separation.

It does not automatically create:

- guardianship;
- custody transfer;
- residential relocation;
- Pokémon ownership;
- active Trainer state;
- medical discharge;
- permission to leave a shelter;
- emotional interpretation.

## 10. Pokémon-specific reunification boundary

Pokémon use the persistent `pokemon_id` from Pokémon Agency.

Useful evidence may include:

- authoritative capture/ball record when accessible;
- established association record;
- shelter/sanctuary intake identifier;
- prior care record;
- distinctive documented physical observation;
- photograph;
- wildlife-monitoring identity;
- direct observed interaction;
- testimony.

None individually receives universal force from this layer.

Forbidden inference:

- same species means same individual;
- same nickname proves identity;
- a Poké Ball in someone's inventory proves ownership;
- a Pokémon approaching someone proves ownership or consent;
- a Pokémon found with a child proves guardianship or family;
- successful reunion changes Loyalty;
- temporary sheltering changes active Trainer.

If a Pokémon has been transferred to the Pokémon Shelter/Sanctuary program, its placement/reunification workflow remains authoritative there.

## 11. Household continuity

A displaced household can be distributed among multiple places.

```yaml
household_displacement_distribution:
  household_id: null
  crisis_or_displacement_ref: null
  member_presence_refs: []
  known_contact_refs: []
  current_distribution_state: UNKNOWN
  planned_reunion_ref: null
  residential_followup_ref: null
```

Suggested descriptive states:

- UNKNOWN
- DISTRIBUTED
- PARTIALLY_LOCATED
- ALL_LOCATED
- CONTACT_RESTORED
- PARTIALLY_REUNITED
- REUNITED_FOR_NOW
- RESIDENTIAL_TRANSITION_PENDING

Do not create household membership here. Reference Residential's explicit household graph.

## 12. Departure event

```yaml
shelter_departure_event:
  departure_event_id: null
  shelter_ref: null
  subject_ids: []
  timestamp: null
  departure_kind: planned|self_departure_observed|transfer|return_route|temporary_offsite|unknown
  destination_claim_ref: null
  transport_ref: null
  receiving_handoff_ref: null
  departure_observation_refs: []
  followup_contact_ref: null
  residential_transition_ref: null
```

Possible downstream outcomes include:

- arrived at another shelter;
- moved to temporary accommodation;
- transferred to Care;
- returned home after Residential review;
- departed to an independently chosen location;
- destination remains unknown.

This layer must tolerate `DEPARTED_DESTINATION_UNKNOWN` without fabricating a destination.

## 13. Roster revisions

```yaml
shelter_roster_snapshot:
  roster_snapshot_id: null
  shelter_ref: null
  generated_at: null
  source_presence_event_refs: []
  included_subject_ids: []
  unresolved_entries: []
  intended_use: operational
  visibility_scope_ref: null
  supersedes_snapshot_ref: null
```

A roster is a versioned product.

Never mutate an old roster to make it match the future.

This enables fair chronology mysteries and preserves who knew what when.

## 14. Privacy and disclosure

Shelter and reunification state can be sensitive.

Exact location should not become public merely because:

- an NPC entity is loaded in Minecraft;
- a shelter roster exists;
- a requester claims a relationship;
- a volunteer saw a registration card;
- a Pokémon is physically rendered at a site.

Public-facing summaries can expose aggregate occupancy, capacity or service availability when the owning system allows it.

Actor-level location, care transfers, relationship claims and Pokémon custody/placement records require the visibility policy already established by the relevant owner systems.

## 15. Communication gaps

A useful record distinguishes:

- message attempted;
- message accepted by network/service;
- message delivered;
- message read/acknowledged if actually observed;
- reply received;
- physical meeting occurred.

Communications owns network truth. This layer only references the resulting evidence.

## 16. Shelter closure

Shelter closure is not equivalent to every resident having returned home.

```yaml
shelter_population_closure:
  shelter_ref: null
  intake_closed_at: null
  last_verified_population_departure_at: null
  unresolved_presence_refs: []
  unresolved_inquiry_refs: []
  transferred_case_refs: []
  archived_roster_refs: []
  ordinary_use_handoff_ref: null
```

Possible long-tail states:

- household still temporarily relocated;
- actor in Care;
- Pokémon in temporary placement;
- inquiry open but actor independently safe;
- home still under repair;
- return route still blocked;
- former shelter already back to ordinary use.

## 17. Persistent place callbacks

Former emergency shelter sites can retain visible history:

- tape or mounting marks from temporary partitions;
- archived floor maps;
- old public notices;
- storage spaces created during the crisis;
- a doorway widened during operations;
- an accessibility improvement retained afterward;
- a community board created during displacement and kept in use;
- a temporary Pokémon accommodation yard converted to another approved use;
- a route between two civic buildings that became locally familiar.

These callbacks require no combat mechanic.

## 18. Narrative patterns

### Five times someone was “found”

The same actor can be:

1. named in a witness report;
2. matched to a shelter registration;
3. located at another site from a later record;
4. contacted by message;
5. physically reunited with the searcher.

NPC accounts using “found” can all be locally reasonable while referring to different milestones.

### Three shelters, one household

A confirmed household is distributed across three sites because members used different evacuation routes. The quest reconstructs chronology and communication rather than forcing everyone into one dramatic rescue.

### Pokémon arrived first

A known partner Pokémon is registered at a temporary Pokémon-capable site before its Trainer's location is established. Pokémon Agency preserves the existing association. The temporary site does not become owner, and later reunion does not invent a Loyalty change.

## 19. Minecraft/Cobblemon projection

Safe presentation candidates:

- shelter beds/cots/partitions;
- registration desks;
- public information boards;
- queue lines already decided by world state;
- temporary signs and route markers;
- representative evacuee NPCs;
- authorized Pokémon entities in separated accommodation zones;
- message boards containing only public-safe information;
- archived former-shelter markings after ordinary use resumes.

Minecraft/Cobblemon must not decide:

- who counts as evacuated;
- family/household relation;
- guardianship;
- Pokémon ownership/custody;
- presence from chunk loading;
- reunification completion from proximity;
- shelter discharge;
- destination arrival;
- return-home authorization.

Entity proximity is presentation, not a reunification transaction.

## 20. Encounter contract — Shelter Loading Bay Withdrawal

Narrative premise:

A hostile encounter threatens the outer loading-bay area while the shelter is already being cleared or transferred.

Full intended version may require:

- evacuees withdrawing through a protected route;
- Intercept or forced movement;
- timed departure waves;
- protected/nonparticipant zones;
- reactions around route crossings;
- AI that understands PROTECT/WITHDRAW/CLEAR_ROUTE;
- semantic playback of departures.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED baseline;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL for exact governed effects;
- status lifecycle — PARTIAL for exact governed statuses;
- terrain/weather/hazards/zones/reactions — BLOCKING for protected corridors/changing zones/reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version: READY.

Before BattleSpec creation, Crisis completes or pauses the shelter transfer in world state. Evacuees, registration records, vehicles, belongings and noncombatant Pokémon leave the tactical grid. AutoPTU receives a static reviewed exterior arena with explicit combatants.

Victory can secure the immediate loading-bay perimeter. It cannot mark anyone reunited, discharge a resident, transfer custody, disclose a location or complete destination arrival.

## 21. Encounter contract — Reunification Route Chokepoint

Narrative premise:

Two already-located parties are expected to meet, but a separate encounter blocks the route between safe locations.

Full intended version may require:

- escort movement;
- Intercept;
- forced displacement;
- timed route availability;
- protected crossing zones;
- objective-aware AI;
- semantic movement playback.

Dependencies use the same map as Shelter Loading Bay Withdrawal: complete movement PARTIAL, lifecycle PARTIAL, environmental/zones/reactions BLOCKING, AI tactical policy BLOCKING and adapter/playback BLOCKING.

Reduced version: READY.

Contact and identity verification remain world-state facts. Keep both reunion subjects off-grid. AutoPTU resolves a conventional battle at a static chokepoint. If the route becomes safe afterward, Travel/Crisis may allow movement and this layer may later record physical reunion.

Battle victory itself is not reunification.

## 22. Encounter contract — Temporary Registration Site Diversion

Narrative premise:

A temporary registration/information point must suspend operation while a hostile encounter occurs nearby.

Full intended version may require staff withdrawal, protected records/equipment, dynamic service zones and objective-aware opposition.

Reduced version: READY.

The coordinator pauses intake, secures records, releases or relocates staff through world state and keeps every evacuee outside BattleSpec. The static perimeter encounter happens afterward. Reopening requires the owner system's operational decision.

Winning cannot authenticate a registration record, confirm identity or reveal private location.

## 23. PTU/Caelo boundary

Remain UNKNOWN unless exact governing project evidence is found:

- generic evacuation action;
- carrying/dragging evacuees;
- crowd/panic mechanics;
- shelter capacity mechanics;
- morale effects;
- human-family reunification mechanics;
- guardian release mechanics;
- generic rescue Skill DCs;
- generic protected-civilian escort reactions;
- communication through any Pokémon species without explicit capability;
- identity recognition by species/type;
- emergency Pokémon custody rules;
- Loyalty changes from separation or reunion;
- status effects from shelter crowding;
- Moves that automatically clear evacuation routes;
- Abilities that automatically locate missing actors;
- Trainer Features that create emergency authority.

A narrative need cannot promote an engine capability family.

## 24. Promotion questions

Before any specific shelter/reunification implementation becomes canon, confirm:

- which institution activates and operates the shelter;
- what information it records;
- what privacy/disclosure policy applies;
- who may submit or receive a reunification inquiry;
- whether any special rules exist for children/dependents and who defines them;
- what Pokémon accommodation model exists locally;
- which existing Pokémon Agency/custody records are accessible;
- how departure is recorded;
- how unresolved departures are handled;
- how shelter closure hands off to Residential, Care, Travel and Pokémon Shelter/Sanctuary;
- which former shelter sites and historical incidents are canon.

Until reviewed, this extension supplies data structures and narrative continuity only.