# Ouros Wild Collective Agency Layer

Status: Proposed systems design. Not established Ouros canon.

## Purpose

Ouros already models ecological causality, behavior observations, persistent individual Pokémon, route ecology, dungeon occupation and World Pulse. This layer adds persistent state for meaningful groups of wild Pokémon without turning every spawn into a simulated citizen or every group into a human-style faction.

The key distinction is scale. A region can contain a population. A particular pack, colony, herd, flock, school, roost, nesting cluster or mixed-species association may become a persistent collective. A player usually sees only a subgroup. AutoPTU then receives only the specific encounter participants.

## 1. Four ecological scales

Ouros should keep these objects separate.

### Population

A statistical/ecological presence such as `species X is common in this wetland during autumn`.

Population state belongs primarily to encounter ecology and observation systems.

### Persistent collective

A recurring, locally meaningful group whose identity matters across scenes.

Examples:
- a pack repeatedly using one valley;
- a nesting colony occupying the same cliff system;
- a herd following a known seasonal corridor;
- a group displaced into an abandoned industrial site;
- a mixed-species association repeatedly sharing one resource.

### Visible subgroup

The portion currently observed by a player.

A hunting party, scouting subset, foraging cluster or small group at a water source may represent only part of the larger collective.

### Tactical encounter group

The exact Pokémon entities instantiated for an AutoPTU scene.

A tactical encounter must never imply that every member of the ecological collective was present unless world state explicitly says so.

## 2. Wild collective schema

```yaml
wild_collective:
  collective_id: null
  status: ACTIVE
  collective_type: null
  primary_species_refs: []
  associated_species_refs: []
  persistent_member_entity_ids: []
  estimated_size_band: unknown
  home_range_location_ids: []
  core_site_ids: []
  seasonal_route_ids: []
  current_location_band: null
  current_behavioral_drivers: []
  cohesion_state: unknown
  leadership_state: unknown
  leadership_model: unknown
  known_leader_entity_ids: []
  communication_observation_ids: []
  resource_dependency_ids: []
  nesting_or_roost_state: null
  vulnerable_member_context: null
  rival_collective_ids: []
  association_ids: []
  disturbance_history_ids: []
  human_contact_history_ids: []
  observed_fact_ids: []
  unresolved_questions: []
  last_confirmed_event_id: null
  persistence_policy: narrative_relevance
```

Candidate collective types:
- PACK
- HERD
- FLOCK
- SCHOOL
- COLONY
- ROOST
- NESTING_CLUSTER
- FAMILY_GROUP only when actually established
- TEMPORARY_AGGREGATION
- FORAGING_PARTY
- MIGRATION_GROUP
- MIXED_SPECIES_ASSOCIATION
- OTHER_OBSERVED_STRUCTURE

Type labels describe observed organization. They do not grant mechanics.

## 3. Persistence threshold

Do not assign an ID to every group spawned by Cobblemon.

A collective becomes persistent when at least one condition applies:
- repeated player interaction makes the same group narratively meaningful;
- a persistent Pokémon entity anchors the group;
- the group repeatedly uses an important location or route;
- its movement changes settlement, travel or ecology state;
- an institution, faction or community actively monitors it;
- its nesting, territory or resource use creates an ongoing arc;
- a previous encounter created consequences that should survive despawn;
- the group is deliberately authored as a regional feature.

Otherwise, ordinary wild groups can remain transient encounter ecology.

## 4. Group identity is not exact membership

Many collectives should persist even if their exact roster is unknown or changes naturally.

```yaml
collective_membership_snapshot:
  collective_id: null
  observed_at_event_id: null
  exact_known_member_ids: []
  estimated_species_counts: {}
  unknown_member_count_band: null
  confidence: null
```

Only story-significant individuals require persistent Pokémon entity IDs.

Do not create thousands of permanent entity records merely to represent a flock.

## 5. Leadership must be evidence-based

Some Pokémon species have official descriptions or PTU mechanics involving leadership. Others do not.

```yaml
collective_leadership:
  collective_id: null
  model: unknown
  candidate_leader_ids: []
  evidence_ids: []
  succession_state: null
  observer_confidence: null
  mechanics_refs: []
```

Possible narrative models:
- UNKNOWN
- NONE_OBSERVED
- SINGLE_COORDINATOR
- MULTIPLE_COORDINATORS
- ROLE_BASED
- TEMPORARY_COORDINATOR
- DISTRIBUTED
- FORMATION_ENTITY

Hard rules:
1. Never generate an `alpha` because the group visually resembles wolves.
2. Never assume the largest or highest-level Pokémon is the leader.
3. Do not infer sex, kinship or breeding role from leadership.
4. PTU `Pack Mon` is a mechanical capability and remains separate from narrative leadership unless governing rules explicitly connect them.
5. Leadership can remain unresolved indefinitely.

## 6. Collective knowledge boundary

Players should know only what they observed, learned or were told.

```yaml
wild_collective_knowledge:
  holder_id: null
  collective_id: null
  known_species_refs: []
  known_size_band: null
  known_core_sites: []
  known_routes: []
  known_behavioral_patterns: []
  suspected_leadership_claim_ids: []
  known_disturbance_responses: []
  source_ids: []
  last_confirmed_event_id: null
  freshness_band: null
  confidence: null
```

A researcher may know a migration route that a traveler does not. A settlement may incorrectly believe a group has one permanent den. A rumor can misidentify one individual as the leader.

The UI must not expose global collective state as omniscient fact.

## 7. Home range instead of political territory

Wild groups use space differently from factions.

```yaml
collective_range_use:
  collective_id: null
  location_ids: []
  use_type: null
  season_or_time_conditions: []
  resource_ids: []
  overlap_collective_ids: []
  observed_conflict_ids: []
  tolerance_state: unknown
  confidence: null
```

Candidate use types:
- CORE_SHELTER
- NESTING
- ROOSTING
- FEEDING
- WATERING
- HUNTING
- TRAVEL_CORRIDOR
- DISPLAY_OR_COURTSHIP only when supported
- REFUGE
- TEMPORARY_OCCUPATION

Do not model every home range as exclusive ownership. Multiple collectives or species can use the same place at different times or for different resources.

## 8. Resource dependency

A persistent group should usually have ecological reasons for being where it is.

```yaml
collective_resource_dependency:
  collective_id: null
  dependency_type: null
  source_location_ids: []
  seasonal_conditions: []
  current_state: stable
  pressure_ids: []
  observation_refs: []
```

Potential dependency types:
- food source;
- water;
- shelter;
- nesting substrate;
- temperature refuge;
- migration corridor;
- mineral/resource lick;
- human refuse or crops;
- another species relationship;
- artificial infrastructure.

A dependency may create a quest when its state changes.

## 9. Group lifecycle

```yaml
collective_lifecycle:
  collective_id: null
  state: STABLE
  state_started_event_id: null
  cause_state_ids: []
  expected_next_states: []
  visible_signs: []
```

Suggested states:
- FORMING
- STABLE
- GATHERING
- DISPERSING
- MIGRATING
- RELOCATING
- DISPLACED
- FRAGMENTED
- REFORMING
- MERGING
- TEMPORARY_AGGREGATION
- DORMANT_OR_ABSENT
- LOST_TRACK

These states are narrative/ecological. They do not define battle modifiers.

## 10. Fragmentation and merge

A group can change identity without being destroyed.

```yaml
collective_transition:
  transition_id: null
  source_collective_ids: []
  output_collective_ids: []
  transition_type: null
  cause_event_ids: []
  member_entity_transfers: []
  estimated_population_changes: []
  range_changes: []
  unresolved_membership: true
```

Candidate transition types:
- SPLIT
- MERGE
- ABSORB only when species/world facts support it
- DISPERSE
- REFORM
- RELOCATE
- TEMPORARY_JOIN

A conflict that causes a group to split is a consequence even when no Pokémon faints.

## 11. Temporary aggregation object

A mass gathering need not become a persistent social unit.

```yaml
wild_aggregation_event:
  aggregation_id: null
  location_ids: []
  species_refs: []
  cause_state_ids: []
  start_event_id: null
  expected_end_conditions: []
  estimated_size_band: null
  behavior_tags: []
  risk_state: null
  linked_collective_ids: []
```

Possible causes:
- migration stop;
- seasonal food abundance;
- refuge from weather;
- spawning/nesting season if canon supports it;
- disturbance elsewhere;
- temporary defensive gathering;
- authored outbreak event.

The system must not label an outbreak as an invasion without evidence.

## 12. Mixed-species association

Co-location is not friendship.

```yaml
wild_association:
  association_id: null
  collective_or_population_ids: []
  observed_interaction_type: null
  evidence_ids: []
  persistence: unknown
  benefit_claims: []
  cost_claims: []
  confidence: null
```

Candidate observed relationships:
- COMPETITION
- PREDATION
- SCAVENGING_AFTER
- SHARED_RESOURCE
- SHARED_REFUGE
- MUTUAL_WARNING only when observed
- CLEANING_OR_MAINTENANCE only when supported
- COMMENSAL_ASSOCIATION
- MUTUALISM_CANDIDATE
- AVOIDANCE
- UNKNOWN

Do not generate symbiosis merely because two species share an encounter table.

## 13. Disturbance history

Collectives can react to repeated player or world pressure.

```yaml
collective_disturbance_event:
  collective_id: null
  source_actor_ids: []
  source_event_id: null
  disturbance_type: null
  intensity_band: null
  immediate_response: null
  later_observed_change_ids: []
```

Potential disturbance types:
- close approach;
- battle;
- capture attempt;
- food provisioning;
- construction;
- habitat damage;
- loud event;
- predator appearance;
- resource removal;
- repeated observation pressure;
- transport traffic.

Group-scale memory should be recorded as observed adaptation:
- avoids one trail;
- relocates feeding time;
- becomes easier/harder to approach;
- gathers earlier;
- sends fewer visible members into an area;
- returns after pressure disappears.

Do not automatically generate human-like revenge, gratitude, political alliance or moral judgment.

## 14. Human feeding and conditioning

Repeated feeding can change behavior without creating friendship.

Possible consequences:
- group waits near a settlement;
- scavenging increases;
- animals approach people more closely;
- conflict rises when food is absent;
- another species is displaced;
- residents disagree about continuing the practice.

Any mechanical bait or item effects must use PTU/Caelo rules. This layer only stores ecological/social consequences.

## 15. Nest, den and roost state

```yaml
collective_core_site:
  site_id: null
  collective_id: null
  location_id: null
  site_type: null
  occupancy_state: null
  access_risk_state: null
  vulnerable_period_tags: []
  disturbance_ids: []
  stewardship_ids: []
  observed_member_roles: []
```

Possible site types:
- nest;
- den;
- roost;
- cave shelter;
- spawning/aggregation site;
- temporary refuge;
- artificial structure.

The existence of a nest does not automatically create eggs, babies or captureable resources. Reproductive detail should be authored only when needed.

## 16. Collective response model

A group confronting pressure should select from plausible responses instead of defaulting to aggression.

Candidate responses:
- IGNORE
- WATCH
- WARN
- WITHDRAW
- SCATTER
- CLUSTER
- MOVE_VULNERABLE_MEMBERS
- BLOCK_ROUTE
- PURSUE
- DEFEND_SITE
- ABANDON_SITE
- RELOCATE
- CALL_OR_SIGNAL others only when supported
- SEEK_RESOURCE
- COMPETE_WITH_OTHER_GROUP

Selection inputs:
- known species behavior;
- group lifecycle state;
- resource dependency;
- current pressure;
- prior observed response;
- terrain and available routes;
- presence of vulnerable members where actually established.

## 17. Encounter derivation

The encounter generator should request a subgroup from ecology.

```yaml
collective_encounter_request:
  collective_id: null
  location_id: null
  encounter_reason: null
  visible_subgroup_estimate: null
  persistent_member_candidates: []
  anonymous_member_species_refs: []
  collective_response_intent: null
  escape_or_retreat_routes: []
  protected_site_ids: []
  mechanics_review_required: true
```

Pipeline:
1. Read current collective state.
2. Determine why the player intersects it.
3. Determine which portion is physically present.
4. Select persistent individuals only when their presence makes sense.
5. Pass species/forms/levels/legal mechanics to the authoritative encounter builder.
6. Resolve AutoPTU battle or noncombat interaction.
7. Write back only the consequences supported by the result.

## 18. Post-encounter writeback

Possible outputs:
- specific member captured;
- persistent member injured/fled/relocated where battle state supports it;
- group retreats;
- group remains but avoids one area;
- nesting site abandoned;
- rival group gains access to resource;
- temporary aggregation disperses;
- player gains observation evidence;
- no durable ecological change.

Important rule:
Most ordinary wild encounters should produce little or no collective-level state change.

A single capture should not automatically collapse a pack, herd or colony.

## 19. Important member removal

If a known persistent member appears to hold an important role, removing it may create consequences. The consequence must not be assumed in advance.

Possible observed outcomes:
- another coordinator takes over;
- group fragments;
- behavior becomes less coordinated;
- group leaves;
- no major change;
- previous leadership assumption proves wrong.

This is an ideal source of follow-up observation rather than an automatic script.

## 20. Collective-to-settlement relationships

Settlements can develop recurring interactions with nearby groups.

Possible relationships:
- tolerated neighbor;
- crop conflict;
- waste scavenger;
- culturally protected group;
- research subject;
- seasonal tourism draw;
- route hazard;
- service dependency;
- mutually avoidant coexistence;
- unresolved fear/rumor.

These are public/social states, not Pokémon relationship emotions.

The same group may be valued by one community and considered disruptive by another.

## 21. Collective-to-route relationships

Route ecology can reference persistent groups directly.

Examples:
- herd crossing window;
- flock roost beside a station;
- pack hunting range overlaps a trail;
- school gathers near ferry infrastructure under certain conditions;
- abandoned road becomes a nesting corridor.

Travel consumes validated collective state; it does not invent ecology to force an incident.

## 22. Dungeon occupation

A dungeon may be occupied by one or more collectives.

Persistent state can record:
- which chambers are core sites;
- whether occupation began after a previous expedition;
- competition with another group/faction;
- changed routes caused by nesting or shelter use;
- whether the group leaves when hazards return;
- whether clearing one chamber simply relocates activity elsewhere.

Avoid treating wild occupation as a set of respawning room guards.

## 23. Research and observation integration

The Observation layer should be able to ask collective-scale questions:
- Is this group stable or temporary?
- Which individuals leave to forage?
- Does it use the same route at different times?
- Is the apparent leader actually coordinating others?
- Which resource anchors the group here?
- Does the group split under pressure?
- Are two species cooperating or only sharing space?
- Did player disturbance change behavior?

Answers remain knowledge records with provenance.

## 24. World Pulse integration

Do not simulate every collective every pulse.

Eligibility for background change can consider:
- active regional clock;
- major resource state change;
- migration timing;
- direct player disturbance;
- faction/infrastructure intervention;
- nearby predator/competitor state;
- authored lifecycle transition;
- high narrative relevance.

Safe background transitions:
- move along known migration corridor;
- leave a depleted resource site;
- return after temporary disturbance;
- fragment after an established event;
- occupy an available shelter;
- join a known seasonal aggregation.

Unsafe without authored support:
- spontaneous extinction;
- mass reproduction;
- sudden new intelligence;
- arbitrary interspecies war;
- unexplained hostility toward a player;
- teleportation between disconnected regions.

## 25. Minecraft / Cobblemon mapping

Potential overworld-facing state:
- spawn profile tied to a collective ID;
- persistent anchor Pokémon for important individuals;
- group clustering or spacing behavior where the mod bridge supports it;
- core-site markers such as nests/roosts only when authored;
- migration corridor presence windows;
- state-driven spawn suppression after relocation;
- route signs/research notices based on player knowledge;
- settlement dialogue reacting to a nearby group;
- visible absence after dispersal;
- recurring group reappearance without requiring the same anonymous entities to persist physically.

The bridge should not attempt to keep hundreds of wild entities loaded solely to preserve group identity. Metadata can persist while ordinary entities despawn.

## 26. AutoPTU boundary

Narrative collective state grants no combat mechanics by itself.

Before an encounter becomes executable, validate:
- legal species/forms;
- level selection and encounter balance;
- actual Moves;
- actual Abilities;
- actual Capabilities including Pack Mon where relevant;
- action economy;
- movement;
- terrain;
- encounter objectives;
- capture;
- retreat/escape implementation;
- swarm/boss rules if intentionally retained from Caelo;
- any individual persistent Pokémon battle state.

Do not add pack bonuses, flanking bonuses, shared initiative, morale modifiers, leader buffs or special capture rules unless the governing mechanical layer explicitly implements them.

## 27. Generation guardrails

1. Group organization must come from evidence, authored ecology or species references.
2. Do not call every collective a family.
3. Do not call every coordinator an alpha.
4. Do not infer sex or kinship from role.
5. Do not equate territory with political ownership.
6. Do not generate permanent hostility from one ordinary encounter.
7. Do not treat wild Pokémon as disposable enemies whose group exists only to populate combat.
8. Do not assume removing a leader solves a conflict.
9. Do not give narrative collectives unsupported combat bonuses.
10. Do not create offspring, eggs or breeding events merely because a nest exists.
11. Do not infer friendship or symbiosis from co-location.
12. Temporary outbreaks should have start/end causes where possible.
13. Persistent group memory should describe observable adaptation rather than invented human motives.
14. Ordinary encounter members do not all require persistent IDs.
15. A collective can remain unknown, partially observed or misunderstood for long periods.
16. Players should sometimes be able to resolve collective conflict by changing routes, resources, pressure or access rather than battling.

## 28. Implementation priority

Recommended order:
1. ecological scale separation: population / collective / subgroup / encounter;
2. persistent collective schema;
3. player-specific collective knowledge;
4. home-range/core-site state;
5. collective lifecycle;
6. encounter derivation and writeback;
7. disturbance history;
8. temporary aggregation events;
9. mixed-species associations;
10. World Pulse transitions;
11. Minecraft spawn-profile bridge;
12. collective-aware research opportunities.

## Open implementation questions

- Can Cobblemon expose enough spawn provenance to associate a visible wild Pokémon with a persistent collective without custom entity tags?
- Should persistent anchor Pokémon use stable UUID mappings across despawn/reload?
- Which PTU/Caelo swarm, Pack Mon, loyalty, intimidation and escape rules are intended to carry into Ouros?
- How should AutoPTU represent an encounter whose success condition is `drive the group away`, `escape the territory` or `protect a nest` rather than defeat-all?
- How should group size bands influence spawn selection without becoming a simulation-heavy population model?
- Which species require hand-authored collective profiles and which can safely use generic observed-state templates?
- How should seasonal group movement advance when relevant chunks are unloaded?
- How much group-state information belongs in player UI versus field reports and visual behavior?
- What safeguards prevent players from intentionally farming collective fragmentation/merge events for rare spawns?
