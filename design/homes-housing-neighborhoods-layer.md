# Ouros Homes, Housing & Neighborhoods Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already models settlements, travel, public works, workshops, clubs, clinics, nurseries, media, crises, social bonds and public memory. This layer adds persistent personal places without turning housing into a parallel economy or progression tree.

A home can be:
- a residence;
- a shared household;
- a temporary lodging;
- a personal base;
- a team base;
- an inherited or former residence;
- a room inside an institution;
- a mobile or expedition home base;
- a place a character considers home even without ownership.

The system should answer who lives where, who may enter, what changed there, what history the place accumulated and how it connects to the neighborhood.

It must not infer property law, private relationships or mechanical bonuses.

## Core separation

Keep these states distinct:

```text
physical_place
  -> residence permission / occupancy
  -> household membership
  -> access permissions
  -> personal modifications / stored provenance
  -> resident routines
  -> neighborhood relationships
  -> public address / known location
  -> subjective home attachment
```

Ownership is a separate claim.

Residence does not prove ownership.
Co-residence does not prove friendship or family.
A public address does not imply unrestricted access.
A character can move without erasing prior history.

## 1. Residence

```yaml
residence:
  residence_id: null
  location_id: null
  structure_id: null
  unit_id: null
  residence_type: null
  current_occupant_ids: []
  household_id: null
  permission_source_refs: []
  ownership_claim_ids: []
  access_policy_id: null
  public_address_status: private
  operational_state: usable
  established_at: null
  vacated_at: null
  prior_residence_ids: []
  source_refs: []
```

Suggested residence types:
- private_home;
- shared_home;
- rented_room;
- dormitory;
- institutional_quarters;
- team_base;
- temporary_lodging;
- field_cabin;
- mobile_base;
- guest_room;
- caretaker_residence;
- other_authored.

These are narrative categories only.

## 2. Household

A household represents shared use of a residence.

```yaml
household:
  household_id: null
  residence_ids: []
  member_ids: []
  shared_access_ids: []
  shared_storage_refs: []
  shared_project_refs: []
  household_rules_refs: []
  start_event_id: null
  end_event_id: null
  status: active
```

A household does not automatically encode:
- romance;
- family relation;
- friendship;
- financial dependence;
- ownership shares;
- caretaker authority;
- Pokémon ownership.

Those facts require their own evidence and systems.

## 3. Home Attachment

The system may track whether a character explicitly treats a place as home only when the state is authored or evidenced.

```yaml
home_attachment:
  actor_id: null
  residence_or_location_id: null
  status: unknown
  evidence_refs: []
  since: null
  former_status: false
```

Allowed statuses should remain qualitative:
- unknown;
- stated_home;
- former_home;
- temporary_home;
- base_of_operations;
- not_home.

Do not compute a hidden emotional score from time spent inside a building.

## 4. Access Policy

Minecraft needs explicit access state.

```yaml
residence_access_policy:
  policy_id: null
  owner_or_steward_ids: []
  resident_ids: []
  invited_actor_ids: []
  invited_group_ids: []
  public_rooms: []
  restricted_rooms: []
  guest_rules: []
  emergency_access_refs: []
  active_from: null
  active_until: null
```

Narrative access and Minecraft permissions should be related but not identical.

The adapter must not infer social permission solely because a player can physically open a door.

## 5. Rooms and Functional Areas

A residence may have authored areas such as:
- bedroom;
- kitchen;
- workshop;
- study;
- storage;
- guest room;
- common room;
- garden;
- stable or habitat area;
- training room;
- clinic room;
- nursery area;
- office;
- archive.

A label describes purpose. It does not grant a mechanical benefit.

Example:

```yaml
residence_area:
  area_id: null
  residence_id: null
  area_type: workshop
  world_structure_refs: []
  steward_ids: []
  equipment_refs: []
  stored_item_refs: []
  operational_state: usable
  service_refs: []
  capability_dependencies: []
```

If a workshop produces items, use the material-culture layer and governing PTU rules.
If a clinic heals, use the care layer.
If a nursery breeds or boards Pokémon, use the breeding layer.

## 6. Personalization and Provenance

Decoration should create identity and memory without automatically creating buffs.

```yaml
home_feature:
  feature_id: null
  residence_id: null
  feature_type: decoration
  item_or_structure_refs: []
  creator_ids: []
  installation_event_id: null
  meaning_claim_refs: []
  mechanical_effect_ref: null
```

Possible feature types:
- decoration;
- memorial;
- display;
- trophy;
- practical_furniture;
- garden_feature;
- storage_feature;
- structural_modification;
- sign;
- artwork;
- habitat_feature.

`mechanical_effect_ref` must remain null unless an authoritative system explicitly defines one.

## 7. Home Chronicle

Residences can accumulate events.

```yaml
home_chronicle_event:
  event_id: null
  residence_id: null
  timestamp: null
  event_type: null
  actor_ids: []
  world_state_changes: []
  physical_change_refs: []
  witness_ids: []
  public_memory_refs: []
  private_memory_refs: []
  source_refs: []
```

Event examples:
- move_in;
- move_out;
- renovation;
- repair;
- visitor_arrival;
- gathering;
- household_change;
- stored_item_added;
- stored_item_removed;
- damage;
- recovery;
- public_opening;
- temporary_closure;
- later_occupant_arrival.

Routine sleeping and storage actions should not flood the Chronicle.

## 8. Moving and Former Homes

Moving should create a transition, not delete state.

```yaml
move_event:
  move_id: null
  actor_ids: []
  from_residence_ids: []
  to_residence_ids: []
  effective_time: null
  carried_item_refs: []
  left_item_refs: []
  custody_changes: []
  access_changes: []
  public_address_changes: []
  reason_claim_refs: []
```

A reason can be unknown. The generator must not invent eviction, breakup, poverty, inheritance or family conflict merely because someone moved.

Former homes can later become:
- another NPC's residence;
- abandoned space;
- public building;
- workshop;
- historical site;
- damaged structure;
- temporary shelter;
- ordinary private residence with no further plot.

## 9. Neighborhood

A neighborhood is a local social/infrastructure graph below settlement scale.

```yaml
neighborhood:
  neighborhood_id: null
  settlement_id: null
  residence_ids: []
  business_ids: []
  institution_ids: []
  public_space_ids: []
  transit_refs: []
  habitat_refs: []
  infrastructure_refs: []
  recurring_actor_ids: []
  local_event_ids: []
  public_issue_ids: []
  reputation_or_identity_claims: []
```

Neighborhood state should support low-intensity callbacks:
- a shop changes hands;
- a familiar Pokémon population shifts;
- construction changes foot traffic;
- a neighbor starts a new service;
- an old resident returns;
- a public garden opens;
- transport changes who passes through;
- a crisis temporarily changes occupancy.

Not every change becomes a quest.

## 10. Resident Routine

Supporting residents should have coarse schedules rather than fixed coordinates.

```yaml
resident_routine:
  actor_id: null
  home_residence_id: null
  recurring_location_windows: []
  work_refs: []
  club_refs: []
  travel_refs: []
  exception_state: null
  last_authoritative_update: null
```

Use coarse states:
- home;
- work;
- traveling;
- visiting;
- unavailable;
- event;
- unknown.

Do not simulate every minute of every NPC.

## 11. Guests and Visitors

Visiting can generate social scenes without changing household membership.

```yaml
visit_event:
  visit_id: null
  residence_id: null
  host_ids: []
  visitor_ids: []
  invited: null
  start_time: null
  end_time: null
  purpose_claim_refs: []
  public_visibility: private
  source_refs: []
```

A visit does not prove friendship, romance, employment or alliance.

## 12. Pokémon and Home Space

Pokémon may occupy or visit a residence only when world state supports it.

Keep separate:
- Trainer ownership;
- custody;
- temporary presence;
- habitat suitability;
- nursery/daycare state;
- wild visitation;
- persistent individual identity.

A Pokémon appearing near a home must not automatically become a resident or owned Pokémon.

Home/habitat features cannot grant movement, Ability, healing, training or encounter-rate bonuses unless governing mechanics explicitly support them.

## 13. Shared and Team Bases

A team base is a residence/institution hybrid.

```yaml
team_base:
  base_id: null
  organization_id: null
  residence_id: null
  headquarters_status: null
  member_access_refs: []
  public_access_refs: []
  facility_refs: []
  archive_refs: []
  meeting_space_refs: []
  active_project_refs: []
```

Organization membership can grant access if canon says so. It does not grant ownership of every object in the base.

## 14. Temporary Lodging

Hotels, inns, hostels, dorms, camps and guest rooms need lighter state than permanent homes.

```yaml
temporary_lodging:
  lodging_id: null
  actor_ids: []
  location_id: null
  provider_id: null
  start_time: null
  expected_end_time: null
  room_or_space_ref: null
  access_ref: null
  status: active
```

Routine lodging should compress unless another system intersects it.

## 15. Home Damage, Displacement and Recovery

Housing state can interact with crisis and public works.

Possible operational states:
- usable;
- partially_usable;
- inaccessible;
- damaged;
- under_repair;
- temporarily_vacant;
- condemned_or_restricted_only_if_canon_defined;
- destroyed_only_by_authoritative_event.

High-impact state changes need explicit causal events.

A procedural generator should not randomly destroy a player home to create drama.

Displacement does not imply homelessness if alternate lodging exists.

Recovery may create:
- temporary housing;
- repair projects;
- relocation choices;
- neighborhood rebuilding;
- memorialization;
- changed transport or services.

## 16. Storage and Provenance

A home can physically store items, but storage state must remain compatible with item authority.

```yaml
storage_location:
  storage_id: null
  residence_id: null
  container_world_ref: null
  custody_actor_ids: []
  access_policy_id: null
  item_instance_refs: []
  last_sync: null
```

The narrative layer must not duplicate inventory quantities maintained by AutoPTU/Cobblemon. It stores provenance/reference links only when useful.

## 17. Home as Quest Source

Homes can generate content when real state changes.

Valid sources:
- resident absence;
- damaged infrastructure;
- new neighbor;
- visitor request;
- household project;
- old stored object with provenance;
- renovation discovery;
- neighborhood conflict;
- wild Pokémon interaction;
- public works;
- route/service disruption;
- move-out or return event;
- former resident callback.

Invalid source:
`the player has not had a home quest recently`.

## 18. Home as Quiet Content

Not every visit needs gameplay.

Useful quiet outputs:
- updated resident position;
- changed decorations;
- new mail or publication;
- NPC conversation topics;
- visible repair progress;
- Pokémon resting visually;
- stored trophies;
- neighborhood ambience;
- old Chronicle callbacks.

The home should support pacing between high-pressure arcs.

## 19. Minecraft representation

Potential adapter responsibilities:
- persist structure IDs and residence IDs;
- map doors/rooms to access policies;
- present residents according to coarse routine state;
- preserve approved decorations/build changes;
- show damaged/repaired variants;
- synchronize public/private visitor access;
- attach provenance to important displayed objects;
- prevent unloaded chunks from deleting narrative state.

The adapter must not own PTU rules.

## 20. Battle boundary

Housing content is mostly world-state logic. Combat near or inside homes still uses the permanent encounter capability categories.

A static legal fight in a courtyard can use currently verified/basic slices where the selected combat behavior is supported.

The following ideas remain implementation-dependent:
- breakable walls;
- moving fire/smoke zones;
- collapsing floors;
- knockback through doors/windows;
- interception around civilians;
- escorting residents across the grid;
- defending multiple rooms as objective zones;
- AI prioritizing property/objectives;
- Minecraft battle playback inside mutable homes.

Do not implement these through ad-hoc Minecraft damage or movement scripts.

## 21. Encounter contract — Courtyard Disturbance

Narrative premise:
A persistent wild group has begun using a home's courtyard after a neighborhood state change. The goal is to understand or resolve the conflict without assuming the Pokémon are hostile or owned.

Full version:
- terrain-aware courtyard;
- possible CLEAR_ROUTE or WITHDRAW outcomes;
- AI can choose retreat or territorial behavior;
- persistent wild-collective writeback;
- Minecraft reflects the post-encounter occupancy state.

Capability dependencies:
- targeting/footprints/range/LoS: VERIFIED family;
- base movement legality: VERIFIED family;
- core calculations: VERIFIED family;
- action economy/initiative: VERIFIED family;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL when used;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for territorial/withdrawal policy;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING;
- terrain/weather/hazards/zones/reactions: only required if courtyard terrain has tactical state; otherwise omit.

Reduced version:
Use a reviewed static arena and standard legal combat only if combat actually occurs. Retreat, negotiation, observation and occupancy changes remain overworld/world-state outcomes rather than invented battle mechanics.

## 22. Encounter contract — Moving Day Chokepoint

Narrative premise:
Residents are relocating through a route whose state has changed. A Pokémon encounter or faction disturbance blocks passage.

Full version:
- BREAK_THROUGH or PROTECT objective;
- moving noncombatant/cargo state;
- interception and forced movement where legal;
- tactical AI aware of route objective;
- adapter renders convoy and writeback.

Dependencies:
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING;
- full lifecycle/damage/status/move/ability/item families as applicable: PARTIAL;
- targeting/base movement/core calculations/action economy/AI legal-action infrastructure: VERIFIED families.

Reduced version:
Keep residents and belongings outside the tactical grid. Resolve a standard legal battle at the chokepoint. If the route becomes safe through authoritative resolution, continue the move in overworld state.

## 23. Encounter contract — Damaged Rowhouse Evacuation

Narrative premise:
A building has become unsafe because of an already-established crisis event. Players must help occupants leave while a hostile or panicked encounter complicates the area.

Full version:
- PROTECT/ESCAPE objectives;
- hazardous zones or changing structure state;
- reactions/interception;
- lifecycle-timed hazard changes;
- AI objective awareness;
- Minecraft mutable-structure playback.

Dependencies:
- terrain/weather/hazards/zones/reactions: BLOCKING;
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if displacement/interception matters;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING;
- lifecycle/damage/status/move/ability/item families: PARTIAL where used.

Reduced version:
Evacuation happens before or after a static legal encounter. Building hazards stay visual/world-state only. No scripted hazard damage, forced movement or fake escort logic.

## 24. Rules and canon guardrails

The generator must not invent:
- land ownership;
- tenancy law;
- rent;
- mortgages;
- taxes;
- inheritance;
- eviction authority;
- property prices;
- construction times;
- house levels;
- building bonuses;
- passive income;
- healing/training/crafting bonuses;
- Pokémon habitat buffs;
- fast-travel rights;
- storage capacity;
- destruction rules.

The social layer remains authoritative for private relationship inference.
The civic layer remains authoritative for public works/official decisions.
The material layer remains authoritative for item provenance and production.
The care/breeding layers remain authoritative for clinics/nurseries.
The crisis layer remains authoritative for displacement and recovery events.
The travel layer remains authoritative for route and transport state.
The wild-collective layer remains authoritative for persistent wild groups.

This housing layer coordinates those systems around personal places. It does not replace them.
