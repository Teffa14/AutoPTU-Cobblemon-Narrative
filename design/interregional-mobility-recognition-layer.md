# Interregional Mobility, Recognition & Exchange Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already models travel networks, transport, education, housing, public memory, cases, conservation, science, battle institutions, media and workplaces. This layer connects those systems when actors, Pokémon, records, institutions and obligations move between regions.

The design goal is to preserve regional identity without inventing a modern nation-state model that the setting has not established.

This layer models:

- home-region and host-region context;
- visits and temporary stays;
- arrival/departure state;
- visitor purpose;
- institutional invitations;
- reciprocal recognition;
- regional record portability;
- host-region orientation;
- cross-region referrals and handoffs;
- event-driven visitor influx;
- interregional cooperation;
- mixed-permission multiplayer groups;
- return visits;
- long-term regional continuity.

It does not establish passports, visas, citizenship, customs law, tariffs, immigration law, national borders or extradition.

## 1. Core separation

Keep these concepts distinct:

- physical geography;
- cultural region;
- League service/jurisdiction area;
- civic authority area;
- conservation-management area;
- transport-network coverage;
- institutional service area;
- an actor's home association;
- an actor's current location;
- an actor's temporary access permissions;
- what records the host recognizes.

A region may contain several authorities. One authority may span several regions. None of those relationships should be inferred automatically.

## 2. Region profile

```yaml
region_profile:
  region_id: null
  name: null
  geographic_scope_refs: []
  settlement_ids: []
  transport_network_ids: []
  cultural_reference_ids: []
  league_framework_ids: []
  civic_body_ids: []
  conservation_area_ids: []
  major_institution_ids: []
  public_information_channels: []
  interregional_connection_ids: []
  status: proposed
```

`region_profile` is a world organization object, not proof of sovereignty.

## 3. Actor regional association

```yaml
actor_regional_association:
  actor_id: null
  region_id: null
  association_kind: home|former_home|resident|temporary_resident|visitor|institutional_assignment|unknown
  start_time: null
  end_time: null
  source_refs: []
  visibility: private_or_authored
```

Do not infer nationality, citizenship or birthplace from a current residence.

A character may have several meaningful regional associations over time.

## 4. Visit record

```yaml
visit_record:
  visit_id: null
  actor_id: null
  host_region_id: null
  origin_region_id: null
  purpose: tourism|competition|education|research|employment|social|expedition|medical_referral|performance|crisis_response|delegation|other
  invitation_ref: null
  arrival_connection_ref: null
  arrival_time: null
  expected_departure_time: null
  actual_departure_time: null
  lodging_ref: null
  host_contact_ids: []
  granted_access_scope_ids: []
  status: planned
  provenance_refs: []
```

Purpose is contextual, not legal status.

## 5. Arrival state

An arrival should update world state only once.

Possible arrival facts:

- reached host region;
- arrived at a specific port/station/route;
- met host contact;
- checked into lodging;
- received orientation packet;
- registered for a specific event;
- began a placement or assignment.

Do not make every arrival a playable checkpoint. Routine known arrivals should compress.

## 6. Host contact

A host contact can be:

- friend;
- institution liaison;
- event organizer;
- employer;
- researcher;
- guide;
- accommodation provider;
- club member;
- family contact;
- public service desk.

A host contact can provide information and navigation without becoming a universal authority.

## 7. Regional orientation

```yaml
orientation_record:
  orientation_id: null
  actor_id: null
  region_id: null
  provider_id: null
  topics_shared: []
  map_refs: []
  service_refs: []
  access_warnings: []
  cultural_notes: []
  ecological_notes: []
  misinformation_flags: []
  time: null
```

Orientation is information delivery. It does not alter canonical facts.

A host may be wrong, out of date or biased.

## 8. Local knowledge asymmetry

Being experienced elsewhere does not imply local knowledge.

Possible knowledge that may remain region-local:

- route hazards;
- recent closures;
- local species behavior;
- seasonal timing;
- informal service customs;
- local faction relationships;
- minor landmarks;
- regional terminology;
- active cases;
- current rumors.

This creates meaningful newcomer play without making visitors incompetent.

## 9. Institutional invitation

```yaml
institutional_invitation:
  invitation_id: null
  issuer_institution_id: null
  invited_actor_ids: []
  host_region_id: null
  purpose: null
  start_time: null
  end_time: null
  access_scope_ids: []
  resource_scope_ids: []
  sponsor_contact_ids: []
  revocation_conditions_ref: null
  status: offered
```

An invitation grants only its authored scope.

An academy invitation does not grant League authority. A research invitation does not grant unrestricted protected-area access. A tournament invitation does not grant permanent residence.

## 10. Recognition claim

```yaml
recognition_claim:
  recognition_id: null
  subject_actor_id: null
  source_record_ref: null
  source_institution_id: null
  host_institution_id: null
  requested_scope: null
  host_result: full|limited|provisional|pending_verification|not_recognized|irrelevant
  accepted_scope: []
  conditions_refs: []
  reviewed_by_ids: []
  review_time: null
```

Recognition is an institutional decision, not universal truth.

## 11. Portable records

Potentially portable public records:

- published tournament placements;
- verified public battle records;
- public research publications;
- public awards;
- public event participation;
- authored institutional credentials;
- public service records when canon allows it.

Potentially nonportable/private records:

- clinic files;
- private academic assessments;
- unpublished case evidence;
- private NPC relationships;
- secret faction state;
- protected research locations;
- mental/psychic information;
- private housing records.

Use existing privacy layers.

## 12. Recognition does not equal equivalency

Two institutions can agree that a record is authentic while disagreeing about what it means locally.

Example:

A field institute may recognize that a visitor completed an ecological practicum elsewhere but still require local orientation before entering a sensitive habitat.

This avoids both total reset and universal credential portability.

## 13. Battle records across regions

A formal battle result may travel as a fact.

It does not automatically grant:

- a local Badge;
- local qualification;
- local ranking;
- a rematch right;
- seeded tournament placement;
- local reputation;
- opponent knowledge beyond what was actually public.

Battle-institution state owns formal competitive consequences.

## 14. Local reputation versus imported reputation

Separate:

- globally/publicly known achievement;
- host-region awareness;
- local NPC trust;
- institutional standing;
- media framing.

A famous visitor may arrive somewhere that barely follows their circuit. A little-known researcher may be highly respected by one host laboratory.

## 15. Interregional connection

```yaml
interregional_connection:
  connection_id: null
  region_a_id: null
  region_b_id: null
  physical_route_refs: []
  transport_service_refs: []
  arrival_hub_ids: []
  normal_operating_state: null
  current_state: null
  schedule_refs: []
  access_condition_refs: []
  information_channel_refs: []
```

The travel layer owns movement and service state.

This layer only adds the regional transition context.

## 16. No universal border checkpoint

Do not generate a checkpoint merely because two regions meet.

A transition may be:

- an open road;
- a mountain pass;
- a ferry;
- a train;
- a flight;
- a ship;
- a research vessel;
- a guided trail;
- a portal only if canon establishes one;
- a seamless geographic boundary.

Formal inspection exists only when authored.

## 17. Biosecurity boundary

Conservation may require temporary ecological restrictions.

Examples:

- cleaning equipment before entering a fragile area;
- temporary closure after disease concern;
- limiting access to nesting habitat;
- sample-handling rules.

Those are conservation/science policies, not automatic customs law.

Any Pokémon quarantine, disease mechanic or item confiscation requires explicit canon/rules support.

## 18. Cross-region case handoff

Cases may move between institutions when:

- the incident crosses a service area;
- evidence is held elsewhere;
- a person/Pokémon of interest travels;
- specialist capability is required;
- local authority ends.

The case layer owns custody/evidence. This layer records the regional transition.

A handoff does not imply extradition, arrest powers or criminal law.

## 19. Research collaboration

Cross-region research can create:

- shared field sites;
- reciprocal visiting programs;
- sample exchange;
- dataset replication;
- joint expeditions;
- equipment loans;
- conference events;
- specialist visits.

Science layer owns evidence and claims.

Access to a partner institution's lab does not grant access to every site it studies.

## 20. Interregional event influx

```yaml
visitor_influx_event:
  event_id: null
  host_region_id: null
  source_region_ids: []
  event_ref: null
  expected_scale: low|moderate|high|unknown
  active_window: null
  transport_impacts: []
  lodging_impacts: []
  service_impacts: []
  media_impacts: []
  market_impacts: []
  clinic_impacts: []
  security_impacts: []
  status: planned
```

Do not simulate every visitor as a persistent NPC.

Use representative actors plus aggregated demand state.

## 21. Host settlement pressure

A major interregional event may change:

- room availability;
- ferry/train frequency;
- restaurant demand;
- clinic queue;
- media presence;
- temporary stalls;
- police/security workload if such institutions exist;
- volunteer staffing;
- public signage;
- translation support;
- route crowding.

These changes must be causally linked to the influx event.

## 22. Visitor economy without automatic tourism simulation

A host region can benefit from visitors without creating a full tourism economy simulator.

Track coarse states such as:

- normal demand;
- elevated visitor demand;
- capacity strain;
- special-event service;
- post-event recovery.

Economy/hospitality layers own detailed venue state.

## 23. Cultural exchange

Cross-region content may involve:

- food;
- performance;
- battle styles;
- research methods;
- crafts;
- festivals;
- language;
- ecological knowledge;
- historical interpretation;
- training customs.

Do not flatten a region into one stereotype.

A cultural practice belongs to specific people, institutions or communities, not automatically every resident.

## 24. Translation and terminology

Visitors may encounter:

- different technical vocabulary;
- regional names for the same practice;
- multiple living languages if canon establishes them;
- local signs;
- inherited terms from older institutions.

Use the language/translation layer rather than inventing comprehension checks.

## 25. Reciprocal access agreements

```yaml
reciprocal_access_agreement:
  agreement_id: null
  party_institution_ids: []
  recognized_record_types: []
  shared_access_scopes: []
  excluded_scopes: []
  start_time: null
  review_time: null
  status: proposed|active|suspended|expired
  public_summary_ref: null
```

This can exist between institutions without implying diplomatic relations between sovereign states.

Examples:

- two research institutes share archive access;
- two conservation programs recognize training records;
- two battle circuits exchange public results;
- two academies accept certain coursework;
- clinics use a referral network.

## 26. Disputed recognition

Recognition disputes can generate playable content without making either side evil.

Possible causes:

- outdated records;
- different standards;
- unclear provenance;
- changed policy;
- missing verification;
- incompatible scopes;
- a record that is genuine but irrelevant.

Resolution options include verification, supervised demonstration, temporary access, alternate evidence or refusal.

## 27. Return visits

A return visit should read previous state.

Potential callbacks:

- host contacts remember prior events;
- old lodging changed ownership;
- regional reputation shifted;
- transport changed;
- local ecology changed;
- previous temporary project became permanent;
- former exchange cohort members moved on;
- an institution now recognizes a record it previously rejected.

Return should not reset the region to first-visit state.

## 28. Long-term stay versus residence

Do not automatically convert a long visit into residence.

Possible states:

- repeatedly visiting;
- seasonal presence;
- temporary assignment;
- long-term guest;
- formal resident if canon/player state establishes it.

Housing layer owns actual residence.

## 29. Multiplayer mixed-access groups

A party may contain members with different permissions.

Do not silently upgrade everyone to the broadest access level.

Possible resolutions:

- group uses public route;
- authorized member enters alone;
- host institution issues temporary group scope;
- party splits;
- activity is moved to an accessible location;
- access is denied.

The generator should surface the difference before committing the party to a blocked objective.

## 30. Regional continuity graph

Useful edges:

- visited_region;
- hosted_by;
- invited_by;
- recognized_by;
- referred_to;
- transferred_record_to;
- competed_in;
- studied_at;
- worked_with;
- returned_to;
- traveled_via;
- collaborated_with;
- unresolved_handoff_to.

This supports long campaigns spanning several regions without merging all regional state.

## 31. Minecraft representation

Possible overworld representations:

- arrival boards;
- ferry/train terminals;
- visiting NPC groups;
- temporary event banners;
- multilingual or regional signage where canon supports it;
- exchange dorm/guest housing;
- visitor desks;
- research delegations;
- temporary vendor stalls;
- packed or quiet transport hubs depending on event state;
- returning NPC visitors during recurring events.

Avoid spawning hundreds of visitor entities.

## 32. Encounter implementation contracts

### Port Arrival Disturbance

Narrative premise:

A crowded arrival period is disrupted by a wild or hostile encounter near the terminal. The goal is to restore safe movement without treating visitors as disposable tactical units.

FULL version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if crowd lanes/interception are tactical
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if terminal hazards or dynamic crowd zones matter
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING
- CLEAR_ROUTE/PROTECT objective semantics: not verified

Reduced version:

Visitors evacuate through overworld state before battle instantiation. AutoPTU receives a static legal terminal-side arena. Safe reopening is a world-state consequence after authoritative combat resolution.

### Joint Boundary Survey

Narrative premise:

Two regional institutions conduct a shared survey at a geographic transition zone while each side brings different assumptions and records.

FULL version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: only required if tactical rescue/interception occurs
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle: PARTIAL
- damage/status/move/ability/item families: PARTIAL when used
- terrain/weather/hazards/zones/reactions: BLOCKING if environmental transition becomes tactical
- Trainer Features/perks: BLOCKING when used
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

Reduced version:

Survey comparison and access negotiation remain overworld/research state. Any encounter uses a fixed arena whose legal mechanics are already supported. The survey can still produce conflicting observations and a future collaboration hook.

### Tournament Transfer Chokepoint

Narrative premise:

Competitors traveling between a transport hub and event venue encounter a route disruption. The event itself remains separate from the incident.

FULL version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING if escort/breakthrough is tactical
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle: PARTIAL
- stateful damage/status/move/ability/item families: PARTIAL when relied upon
- terrain/weather/hazards/zones/reactions: BLOCKING if route state enters combat
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING
- ESCORT/BREAK_THROUGH objective semantics: not verified

Reduced version:

Transport disruption and competitor movement resolve outside the battle grid. A static encounter blocks the route. Event registration/attendance updates only after the route is cleared or an alternate connection is selected.

## 33. Engine capability relevance

Interregional state can be implemented independently of battle readiness:

- visit records;
- arrival/departure;
- institutional invitations;
- recognition claims;
- reciprocal agreements;
- event influx;
- host contacts;
- orientation;
- regional record visibility;
- cross-region referrals;
- return-visit callbacks.

Do not use battle lifecycle as regional travel time.

## 34. Current engine boundary

Latest inspected AutoPTU-Java evidence includes a reusable ordered status-phase registry and Python parity for its bounded contract.

This strengthens lifecycle/status infrastructure but does not establish complete status behavior.

Permanent classification remains:

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items.

BLOCKING:
- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- Trainer Features/perks;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

## 35. PTU/Caelo boundary

The supplied Caelo material supports explicit location access requirements and inter-island travel constraints. That is enough to justify explicit access state.

It is not enough to establish:

- passport mechanics;
- visas;
- customs inspection;
- border detention;
- tariffs;
- immigration categories;
- extradition;
- interregional criminal law;
- universal League-recognition rules.

Any such system requires deliberate Ouros canon plus rules review.

## 36. Integration with existing layers

This layer references:

- travel/transport: physical movement and schedules;
- education: exchanges and transfers;
- housing: lodging/residence;
- battle institutions: competition records and local qualification;
- science: joint research and replication;
- conservation: protected-area access;
- cases: referrals/handoffs;
- care: specialist referrals;
- media: cross-region information movement;
- public memory: portable public achievements;
- language: terminology/translation;
- workplaces: visiting specialists;
- food/hospitality: visitor demand;
- crisis: mutual aid and emergency arrivals;
- civic governance: host-region public service state.

It should never duplicate those systems.

## 37. Promotion checklist

Before interregional content becomes canon:

1. Confirm the relevant regions exist.
2. Confirm the physical connection between them.
3. Confirm which institutions operate on each side.
4. Confirm whether any formal access requirement exists.
5. Do not infer sovereignty or citizenship.
6. Define what records can be recognized and by whom.
7. Define privacy/visibility of transferred information.
8. Validate Pokémon-assisted traversal against PTU/Caelo and engine state.
9. Add encounter contracts for mechanically rich crossings.
10. Confirm Minecraft representation is feasible.
11. Preserve source provenance.
12. Keep proposed institutional rules outside canon until reviewed.

## Open questions

- How many distinct regions will Ouros launch with?
- Are regions political units, cultural/geographic units, League areas or a mixture?
- Do any regions share a League framework?
- Which credentials have reciprocal recognition?
- Are public battle records globally available?
- Can a host conservation program recognize training completed elsewhere?
- How are medical referrals transferred privately?
- Are Pokémon ownership/custody records shared across regions?
- What distinguishes a long-term visitor from a resident?
- What host services appear automatically for major events?
- How should mixed-access multiplayer parties be handled in UI?
- Which cross-region connections are physical at launch?
- How do regional NPCs travel while chunks are unloaded?
- How much visitor demand should affect shops/clinics/transport before it becomes simulation noise?
