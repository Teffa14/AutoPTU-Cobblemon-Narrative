# Ouros Questline Taxonomy v2

Status: CANON-APPROVED SYSTEM TAXONOMY
Date: 2026-09-01

Ouros uses one questline graph with composable types. A playable episode may advance several questlines at once. Questline type is metadata and indexing, not a separate runtime engine.

## Canonical questline families

The current complete top-level family set is:

1. `MAIN` — central campaign progression and major world-arc convergence.
2. `CLASS` — PTU Trainer-class identity arcs. All 69 current classes require eventual coverage.
3. `SECONDARY` — authored local stories that do not need a stronger owner.
4. `REGION` — district, province, settlement-chain or regional-history arcs.
5. `FACTION` — organization goals, internal disputes, membership, reputation and consequences.
6. `POKEMON` — persistent individual Pokémon, species, populations, ecology and Pokémon-centered stories.
7. `DUNGEON` — discovery, access, exploration, internal change, bosses, revisits and aftermath of persistent dungeons.
8. `EQUIPMENT` — significant equipment construction, restoration, provenance, upgrades and ownership history.
9. `ITEM` — significant item, document, ingredient, relic, fossil, tool or other object-centered stories.
10. `RELATIONSHIP` — persistent interpersonal history with NPCs. This is not a generic friendship meter.
11. `RIVAL` — recurring Trainer/rival competitive and personal progression independent of the player's current build.
12. `SERVER_EVENT` — shared, scheduled or condition-driven server-wide events.
13. `CHARACTER` — a person's own life arc when the central question is not reducible to their relationship with the player.
14. `EXPLORATION` — routes, mapping, ruins, hidden spaces, expeditions, discoveries and access change.
15. `COMPETITIVE` — battle circuits, contests, tournaments, ladders, exhibitions and institutional competitive seasons.
16. `SETTLEMENT` — community projects, reconstruction, services, local growth, decline, migration and civic continuity.

No separate `LEGENDARY` family is needed. A Legendary or mythic thread can be tagged `POKEMON`, `REGION`, `EXPLORATION`, `MAIN`, `FACTION` or another combination as appropriate.

No separate `PROFESSION` family is needed. Profession stories use `CLASS`, `FACTION`, `CHARACTER`, `ITEM`, `EQUIPMENT`, `SETTLEMENT` and other existing families. If later evidence shows that profession identity cannot be represented cleanly with these tags, this decision may be revised explicitly.

## Multi-type rule

A questline can have more than one family.

Example:

```yaml
questline_id: ouros.marea.thin_delivery.route_evidence
questline_types:
  - REGION
  - EXPLORATION
  - CLASS
  - FACTION
class_refs:
  - Survivalist
  - Backpacker
faction_refs:
  - ouros.faction.marea_field_office
```

A quest episode can advance multiple questlines without duplicating the underlying world event.

## Runtime graph

Canonical hierarchy:

`WORLD ARC -> QUESTLINES -> QUEST EPISODES -> OBJECTIVES / CHOICES -> WORLD WRITES`

Every questline record must be able to reference:

```yaml
questline:
  questline_id: null
  title: null
  types: []
  parent_arc_ids: []
  parent_questline_ids: []
  quest_episode_ids: []
  location_ids: []
  npc_ids: []
  faction_ids: []
  pokemon_ids: []
  item_ids: []
  dungeon_ids: []
  class_refs: []
  world_fact_reads: []
  world_fact_writes: []
  character_history_reads: []
  relationship_reads: []
  eligibility_rules: []
  completion_rules: []
  failure_or_transformation_rules: []
  aftermath_outputs: []
  battle_contract_refs: []
```

## Replication rule

Every new district must eventually provide the following minimum graph:

- at least one Region Questline;
- at least one Settlement Questline for each major settlement;
- one or more Faction Questlines for persistent institutions;
- Relationship and Character threads for recurring NPC anchors;
- Pokémon Questlines grounded in the district ecology;
- Exploration content for routes or spaces that can change through play;
- Secondary Questlines that make ordinary residents matter;
- Class intersections selected from the actual PTU class catalogue;
- Competitive content where the district has a battle/contest institution;
- Server Event hooks where calendar or world-state events can affect the district.

This is a coverage floor, not a quota for every episode.

## Correlation rule

New content must reuse existing IDs and world facts when it touches established people, places, institutions or events.

Before creating a new NPC, location, faction, Pokémon identity, dungeon, item or questline, implementation must ask whether an existing entity already owns the role.

`NEW_CONTENT != NEW_ISLAND`

Every substantial addition should add at least one edge to the existing world graph unless isolation is itself a deliberate canonical fact.

## Multiclass and respec boundary

Current build, historical identity and narrative progress remain separate.

- Current classes can expose choices or mechanically gated solutions.
- Class history can support authored recognition only where canon records it.
- Completed class-thread history survives respec.
- Removed classes do not retain current Feature, Edge, Skill or other PTU permissions.
- Up to four simultaneous classes must not require duplicate copies of the same shared event.

## External structural references

Research references for implementation structure:

- Heracles: tree-style quest graph and explicit dependencies. MIT. Structural inspiration only unless a reviewed compatible dependency is adopted.
- FTB Quests: mature chapters, dependency visualization and 1.21.1 availability. Candidate projection/UI integration only; it must not own Ouros truth.
- MCA: Quests: data-driven quest files, server authority, validation, NPC offers and shared community projects. GPL-3.0 and Forge 1.20.1; no code is copied into Ouros. Its data-authoring patterns are useful research input.

Ouros keeps its existing canonical services as authority. External quest systems may become adapters or UI surfaces but may not decide canonical completion, PTU legality, battle outcomes or world truth.
