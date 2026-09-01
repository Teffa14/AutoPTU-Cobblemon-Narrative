# Ouros Canon

Status: CANON GOVERNANCE / IMPLEMENTATION BASELINE
Date established: 2026-09-01

This directory is the authoritative home for reviewed Ouros world facts that game content may implement directly.

## Promotion rule

Research is evidence. Proposals are candidates. Design files define architecture. Files in `canon/` define the actual Ouros world unless a later canon revision explicitly supersedes them.

A canon entry must preserve provenance and distinguish:
- established world fact;
- implementation detail;
- unresolved field that still requires a decision;
- mechanical behavior delegated to PTU/Caelo/AutoPTU.

No Minecraft/Cobblemon presentation state may silently create or revise canon.

## Canon precedence

Later explicit canon rules may resolve fields that an earlier foundation file left unresolved without requiring the older file to be rewritten immediately.

Current explicit supersession:
- `npc-pokemon-dynamic-progression-v1.md` resolves the general level/moveset-generation policy for persistent NPC Pokémon that `ouros-playable-foundation-v1.md` originally left unresolved.
- Species identity and narrative companionship established in the playable foundation remain canon.
- AutoPTU still owns legality and derived battle state.

Where two canon files genuinely conflict beyond an explicit supersession note, implementation must stop and open a canon migration rather than silently choose one.

## Natural-growth rule

Once a canon fact exists, future content should derive from it instead of reopening the same foundational question without cause. New settlements, NPCs, factions, schedules, quests and events should reuse established geography, institutions, relationships and history wherever possible.

Canon can grow through consequences. It should not oscillate through arbitrary rewrites.

## Implementation completeness

Important canon content should converge toward implementation packets containing:
- stable IDs;
- locations and spatial relationships;
- NPC identity and schedule;
- current PTU classes and relevant class history;
- Pokémon roster identity and battle audit state;
- faction memberships and relationships;
- knowledge/provenance state;
- quest and event participation;
- triggers and prerequisites;
- persistent variables;
- state transitions and branches;
- battle handoff contracts;
- reduced implementations when engine capabilities are incomplete;
- cleanup and aftermath behavior;
- assets/adapters still required.

## Player build boundary

World history is independent of the player's current class loadout.

`HAS_CLASS_NOW != HAS_CLASS_HISTORY`

Changing or removing a class does not erase completed events, learned world facts, faction relationships or prior decisions. Mechanical permissions are always revalidated against the current authoritative PTU build.

## Persistent NPC Pokémon boundary

A persistent NPC Pokémon has durable identity but does not require a static battle sheet.

`PERSISTENT_POKEMON_IDENTITY != STATIC_BATTLE_SHEET`

Default recurring NPC Pokémon level is derived from the player's battle-eligible active-party median plus the NPC encounter profile. Legal level-up moves are regenerated from authoritative learnset data at that effective level. Optional TM knowledge is resolved from a persistent deterministic roll and legal TM compatibility, so reloads and rematches do not reroll the individual.

## Current canon maturity

The repository now has a first connected playable foundation plus a global recurring-NPC progression rule. Future canon should continue outward from those facts and progressively replace unresolved implementation fields with explicit reusable rules.
