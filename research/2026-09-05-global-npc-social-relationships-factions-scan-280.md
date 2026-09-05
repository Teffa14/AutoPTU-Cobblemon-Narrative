# Global NPC social relationships and factions research scan — Pass 280

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-05
Canon effect: NONE by itself
Scope: reusable social/world-agent structures for all Ouros NPCs

## Why this scan exists

Pass 279 gave persistent NPCs durable goals, needs and commitments. The next gap is social causation: why an NPC helps one person, avoids another, keeps a promise, challenges a rival, reports to an institution or refuses a request without reducing every relationship to a single reputation number.

This research is region-neutral. Marea, Sendero and other authored places are not used as architectural assumptions.

## New public sources

### Comme il Faut / Prom Week

Joshua McCoy et al., “Comme il Faut: A System for Authoring Playable Social Models,” AIIDE 2011.
DOI: https://doi.org/10.1609/aiide.v7i1.12454
Source page: https://ojs.aaai.org/index.php/AIIDE/article/view/12454

Reusable lesson:
- represent social state separately from authored dialogue;
- use reusable social considerations rather than writing a bespoke script for every pair of characters;
- let history and current relationship state affect which social actions are attractive or appropriate;
- preserve enough state that social consequences can recombine into later interactions.

Ouros transformation:
- directional relationship vectors are persistent world state;
- relationship dimensions influence world-intent utility;
- dialogue later renders the underlying state but cannot create it;
- no Prom Week characters, setting, dialogue or plots are copied.

### Prom Week as playable social state

McCoy et al., “Prom Week,” AIIDE 2013.
DOI: https://doi.org/10.1609/aiide.v9i1.12662
Source page: https://ojs.aaai.org/index.php/AIIDE/article/view/12662

Reusable lesson:
- relationships can be game state that changes through repeated actions;
- the same social goal can have multiple viable approaches;
- a social simulation becomes more useful when consequences persist instead of resetting after a scene.

Ouros transformation:
- assistance, avoidance, rivalry, reporting and socializing are candidate purposes, not fixed dialogue branches;
- one interaction can update only the dimensions justified by its semantic result;
- NPC A’s state toward NPC B does not imply NPC B has the same state toward A.

### PTU community: recurring rivals tied to character goals

Public discussion: “New to Ptu,” r/PokemonTabletop, 27 January 2026.
https://www.reddit.com/r/PokemonTabletop/comments/1qo26uy/new_to_ptu/

Reusable lesson from community advice:
- recurring characters are more engaging when they connect to player interests and goals;
- rivals benefit from an opposing philosophy and repeated appearances;
- shorter arcs allow relationships to evolve rather than depending on a single endgame reveal.

Ouros transformation:
- rivalry is one relationship dimension and can motivate training, investigation, communication or a challenge;
- rivalry never means automatic combat;
- philosophy/goal conflict belongs in authored motives and knowledge, not in a universal PTU rule.

### PTU community: avoid over-authoring future rival battle sheets

Public discussion: “Rival Team for Kanto based PTU Campaign,” r/PokemonTabletop, 4 April 2026.
https://www.reddit.com/r/PokemonTabletop/comments/1sbx3kf/rival_team_for_kanto_based_ptu_campaign/

Reusable lesson from replies:
- building detailed future NPC battle teams before the campaign state is known wastes authoring effort;
- recurring rivals should be prepared around role and near-term set pieces rather than fixed late-game sheets.

Ouros transformation:
- social identity and relationship history persist;
- battle-ready state continues to use the existing dynamic NPC Pokémon progression and AutoPTU validation contracts;
- relationship AI does not own battle sheets.

### Official Pokémon: faction support can coexist with individual action

The Pokémon Company, “Stop Chairman Rose with Leon and Gloria in Pokémon Masters EX,” 2 August 2023.
https://www.pokemon.com/us/news/stop-chairman-rose-with-leon-and-gloria-in-pokemon-masters-ex

Reusable high-level pattern only:
- a conflict can contain supporters, opponents and individuals who act from their own goals within a broader factional dispute;
- membership/alignment is useful context without requiring every member to behave identically.

Ouros transformation:
- faction membership contributes obligations, permissions and social context;
- membership does not create hive-mind knowledge or automatic obedience;
- no Masters EX plot, characters or dialogue are imported.

## Design conclusions

A single scalar reputation cannot safely own social AI. Minimum useful persistent relationship state should keep separable dimensions such as affinity, trust, respect, fear, rivalry and reciprocal obligation/debt.

Directional state is mandatory:

`RELATIONSHIP(A -> B) != RELATIONSHIP(B -> A)`

Faction membership is a distinct state family. It may grant explicit role obligations or permissions when the relevant content contract says so. It does not grant private knowledge, shared emotions or unconditional compliance.

Useful safeguards:
- affinity does not imply trust;
- trust does not imply agreement;
- rivalry does not imply hostility;
- fear does not imply hatred;
- shared faction does not imply shared knowledge;
- institutional duty does not erase needs, relationships or individual goals;
- a social event must carry provenance before it can mutate a persistent relationship;
- relationship effects must remain bounded so one dimension cannot permanently override every other agenda pressure.

## PTU / Caelo / Kairos cross-check

No PTU rule was found that should become a global social-simulation equation. PTU Trainer Skills, Features, Edges and combat mechanics remain mechanical inputs only where the active Ouros rules profile adopts them.

The project source-authority policy already requires `SOURCE_HAS_RULE != OUROS_USES_RULE` and keeps Caelo/Kairos campaign semantics from becoming Ouros defaults. This pass follows that boundary.

Existing `canon/npc-pokemon-dynamic-progression-v1.md` remains owner of recurring NPC Pokémon battle-ready progression. Social state can motivate an encounter; it cannot select illegal Moves, generate combat stats or bypass AutoPTU.

## Canon boundary

PROPOSED:
- region-neutral directional relationship vectors;
- explicit faction membership/role state;
- social modifiers feeding the existing global agenda utility layer;
- provenance-gated relationship changes.

UNCERTAIN / CONTENT-DEFINED:
- exact relationship dimension ranges and rates of change;
- which factions exist;
- faction role obligations and permissions;
- which authored events should change trust, respect, fear, rivalry, affinity or debt;
- whether any relationship dimension becomes visible numerically to players.

CANON-APPROVED FOUNDATIONS CONSUMED, NOT CHANGED:
- global persistent NPC identity;
- non-omniscient NPC knowledge;
- dynamic recurring NPC Pokémon progression;
- Ouros/AutoPTU/Minecraft authority boundaries.

No new NPC, faction, relationship, region or social rule is canonized by this research note.
