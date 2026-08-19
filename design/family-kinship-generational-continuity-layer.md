# Ouros Family, Kinship & Generational Continuity Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already models homes, households, social bonds, public memory, breeding/eggs, education, workplaces and institutional succession. This layer adds explicit human kinship and generational continuity without turning family into a faction, a morality system or a source of automatic mechanics.

The system should answer:
- who is explicitly related to whom;
- what kind of relationship is confirmed;
- what obligations, permissions or expectations are actually authored;
- what public reputation is attached to a family name;
- what passes between generations as records, objects, history or expectations;
- what remains unresolved or private.

It must never infer family relations from co-residence, surnames, age, appearance or repeated caregiving.

## Core separation

```text
kinship_fact
  -> household/residence state
  -> guardianship/care claim
  -> ownership/custody claim
  -> social relationship state
  -> public family reputation
  -> inherited records/provenance
  -> personal response to legacy
```

These are distinct systems.

## 1. Kinship facts

```yaml
kinship_relation:
  relation_id: null
  actor_a_id: null
  actor_b_id: null
  relation_type: null
  relation_status: confirmed
  start_event_id: null
  end_event_id: null
  source_refs: []
  consent_refs: []
  visibility: private
```

Suggested relation types are descriptive only:
- parent_child;
- sibling;
- grandparent_grandchild;
- extended_family;
- spouse_or_partner;
- adoptive_relation;
- guardian_dependent;
- authored_other.

Do not derive one relation from another unless the graph rule is explicitly safe. For example, two people sharing a parent may suggest a sibling relation, but the system should preserve uncertainty around half-siblings, adoption and unknown parentage rather than silently collapsing them.

## 2. Player-consent boundary

Family links involving a player-controlled character require explicit authoring by that player.

A relation involving two PCs requires consent from both players.

The generator may propose a blank hook such as:
- "an older relative contacts the character";
- "a family archive may exist";
- "someone claims to know the character's family".

It may not assign the relative's identity or make the claim true without authorized canon.

Forbidden automatic additions to a PC:
- parents;
- siblings;
- children;
- spouse/partner;
- adoption;
- guardians;
- ancestry;
- estrangement;
- death in the family;
- pregnancy;
- inheritance;
- family trauma.

## 3. Family group

A family group is an indexing convenience, not a hive mind.

```yaml
family_group:
  family_group_id: null
  member_ids: []
  confirmed_relation_refs: []
  shared_name_refs: []
  public_history_refs: []
  archive_refs: []
  associated_property_claim_ids: []
  associated_institution_ids: []
  public_reputation_refs: []
```

A family group has no automatic:
- alignment;
- faction membership;
- shared knowledge;
- shared money;
- shared Pokémon;
- shared access;
- loyalty score.

## 4. Public family reputation

Some names become publicly associated with achievements, scandals, institutions or historical events.

```yaml
family_public_reputation:
  family_group_id: null
  claim_ids: []
  region_ids: []
  audience_ids: []
  current_public_associations: []
  counterclaims: []
  source_refs: []
```

This is a media/public-memory object.

It can cause recognition or expectations. It does not modify personal reputation automatically.

Example:
A famous Gym family may be respected in one town. A younger member arriving there may be recognized by name while still having zero personal battle record.

## 5. Legacy pressure

Characters can explicitly react to inherited expectations.

```yaml
legacy_pressure:
  actor_id: null
  source_family_group_id: null
  expectation_claims: []
  actor_response_status: unknown
  response_evidence_refs: []
```

Allowed actor response states should remain authored and qualitative:
- unknown;
- embraces;
- rejects;
- negotiates;
- indifferent;
- conflicted;
- reframes.

Do not infer a response from behavior alone.

## 6. Generational records

A campaign can progress across generations without resetting the world.

```yaml
generational_record:
  generation_id: null
  era_start: null
  era_end: null
  active_pc_ids: []
  major_world_state_refs: []
  inherited_archive_refs: []
  unresolved_arc_refs: []
  institution_state_refs: []
  public_memory_refs: []
```

When time advances:
- locations retain validated changes;
- institutions retain history;
- items retain provenance;
- public records age and may become incomplete;
- ecological systems continue;
- old rumors can mutate;
- descendants or later PCs encounter consequences rather than a reset setting.

## 7. What can pass between generations

The following may pass when canon and ownership rules allow it:
- documents;
- photographs;
- journals;
- trophies;
- tools;
- heirlooms;
- property claims;
- institutional membership history;
- invitations;
- public recognition;
- unresolved cases;
- research archives;
- stories and rumors.

The following do not pass automatically:
- Trainer Classes;
- Skill Ranks;
- Edges;
- Features;
- Pokémon ownership;
- Pokémon Loyalty;
- faction allegiance;
- political office;
- debt;
- guilt;
- trust;
- combat knowledge.

Any mechanical inheritance requires explicit PTU/Caelo authority.

## 8. Pokémon across generations

Long-lived Pokémon can connect eras, but they remain independent entities.

A Pokémon may remember earlier Trainers or places if persistent memory is canonically represented. A later family member does not automatically own, command or understand that Pokémon.

Possible safe structures:
- an old Pokémon still lives near a former family home;
- a Pokémon recognizes a familiar object or place;
- a retired partner is cared for by an institution;
- a later character investigates the provenance of an old Poké Ball or ribbon;
- a family claims historical association with a species, but the claim may be incomplete or mythologized.

Never convert this into automatic Loyalty or obedience.

## 9. Guardianship and dependency

Guardianship is a civic/legal concept and must remain unresolved until Ouros defines its institutions.

```yaml
guardianship_claim:
  claim_id: null
  guardian_actor_ids: []
  dependent_actor_ids: []
  authority_scope: []
  source_refs: []
  jurisdiction_refs: []
  status: proposed_or_confirmed
```

The narrative system may track a confirmed caregiver without assuming formal guardianship.

## 10. Family-linked institutions

A workshop, Gym, farm, clinic, ferry company or archive may involve several relatives across time.

Institutional succession must remain separate from kinship.

```text
relative of founder
!=
automatic successor
```

A successor needs the institution's own governance, ownership, staffing or appointment state.

This creates useful stories:
- a child declines to inherit a workshop;
- a non-relative apprentice becomes the best successor;
- siblings divide institutional roles;
- a famous family retains ceremonial prestige but no operational control;
- an institution outgrows its founding household.

## 11. Family archives

Private archives integrate with the media, language, archaeology and public-memory layers.

```yaml
family_archive:
  archive_id: null
  steward_ids: []
  access_policy_ref: null
  item_refs: []
  document_refs: []
  provenance_quality: mixed
  public_catalog_refs: []
  restricted_record_refs: []
```

A family archive may be incomplete, biased or wrong. It is evidence, not truth.

## 12. Ordinary family life as content

Family content should not require tragedy.

Low-pressure hooks can include:
- reunion travel;
- helping prepare a shop for a busy season;
- transporting old records;
- resolving scheduling conflicts;
- introducing a new partner Pokémon to relatives;
- attending a ceremony;
- comparing two versions of a family story;
- helping an older relative document local ecology;
- moving between homes;
- deciding whether to accept an institutional role.

## 13. Generational arcs

Long-form structures supported by this layer:

### Inherited World
Generation A changes a town. Years later, Generation B deals with the benefits, mistakes and myths that grew around those decisions.

### Name Before Person
A character enters a region where their family name is known. The arc is about defining a personal identity rather than proving or disproving the ancestor's worth.

### The Missing Middle
Two eras have strong records but the generation between them is poorly documented. Players investigate why institutional memory became fragmented without assuming conspiracy.

### Succession Without Destiny
A long-running family institution faces transition. Several relatives, apprentices and outsiders have legitimate claims or qualifications. The story is about process and choice, not bloodline entitlement.

## 14. Minecraft representation

Safe visible state:
- family photographs or portraits when canon-approved;
- surnames on signs or public records;
- heirlooms with provenance IDs;
- old rooms preserved or repurposed;
- family archives;
- memorials;
- NPC schedules around reunions/events;
- multiple generations living in or visiting one settlement.

Do not expose private family data merely because an NPC exists in a loaded chunk.

## 15. Encounter implementation contracts

Family narratives usually do not require special combat mechanics. When they do, battle dependencies must remain explicit.

### Full concept: Archive Evacuation
Premise: during a crisis, players protect people and irreplaceable records while leaving a damaged ancestral building.

Full dependencies:
- targeting/footprints/range/LoS: VERIFIED baseline;
- base movement legality: VERIFIED baseline;
- complete movement including interception/forced movement: required for true escort/chokepoint behavior — BLOCKING;
- core calculations: VERIFIED baseline;
- action economy/initiative: VERIFIED baseline;
- full turn/round lifecycle: PARTIAL;
- status lifecycle: PARTIAL if hazards cause status effects;
- terrain/weather/hazards/zones/reactions: required for dynamic building hazards — BLOCKING;
- AI legal-action infrastructure: VERIFIED baseline;
- AI tactical policy: required for objective-aware opposition — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: required for physical evacuation — BLOCKING.

Reduced version:
The evacuation and record selection occur in overworld/world-state scenes. AutoPTU receives one stable arena encounter with civilians and archives outside the tactical grid.

### Full concept: Reunion Route Breakdown
Premise: a routine family journey is interrupted by a route problem and a wild encounter.

Full dependencies:
Only baseline combat families are needed if the route problem is resolved before battle. If the route itself shifts during combat, terrain/hazards become BLOCKING.

Reduced version:
Resolve route repair/exploration first, then launch an ordinary static encounter if one remains justified.

### Full concept: Legacy Challenge Exhibition
Premise: two relatives participate in a voluntary public exhibition where spectators compare their styles.

Full dependencies:
- targeting/range/LoS: VERIFIED;
- base movement: VERIFIED;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- lifecycle/status/move/ability/item families: only as required by the selected legal combatants; currently PARTIAL at family level;
- AI tactical policy: BLOCKING if an AI-controlled rival needs adaptive strategy;
- playback: BLOCKING for Minecraft spectacle.

Reduced version:
Run a legal standard battle and record official result separately from audience/public-memory reactions.

## 16. PTU/Caelo boundary

Family state is narrative unless a governing source explicitly defines a mechanic.

Never invent:
- family stat bonuses;
- inheritance of Trainer Features;
- sibling combo attacks;
- automatic Command bonuses;
- guardian interrupts;
- inherited Pokémon obedience;
- shared inventories;
- legacy move access;
- automatic rivalry mechanics.

Character backgrounds can mention family facts, but Skill Ranks, Edges, Features, combat stats and Pokémon state remain governed by PTU/Caelo and AutoPTU.

## 17. Promotion checklist

Before family-related proposals become canon:
1. every PC-linked family relation has player consent;
2. provenance for NPC kinship is explicit;
3. guardianship/ownership claims do not rely on assumed real-world law;
4. housing and household state agree with the housing layer;
5. inheritance agrees with ownership/custody systems;
6. public family reputation is stored as public memory, not truth;
7. former PCs receive no invented life events;
8. Pokémon ownership/Loyalty is not inferred from family association;
9. any combat dependency uses the permanent engine categories;
10. copyrighted source characters or plots were not transplanted.
