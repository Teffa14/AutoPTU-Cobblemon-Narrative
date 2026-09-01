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

## Current canon maturity

The repository has extensive researched systems and proposed content but only now begins explicit region-canon promotion. Initial canon files should establish a small connected playable foundation before attempting to freeze the entire region at once.
