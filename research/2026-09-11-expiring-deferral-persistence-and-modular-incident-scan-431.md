# Expiring deferral persistence and modular incident scan — Pass 431

Status: RESEARCH / NON-CANON
Date: 2026-09-11

## Purpose

Find new reusable structures for preserving a deferred assistance window through save/restart without turning the saved record into a promise, completed action or retroactive quest result.

Repository search was performed before source selection. Recent recurring anchors such as Six Ages, Majora's Mask, Pokémon RAMP, Trouble on the Farm, Pokémon Keishou and Pokémon Burning Scales were not reused as primary sources. No prior repository match was found for Unsighted or FanaticRat's Premade Module Repository.

## Source 1 — Unsighted: meaningful consequences under persistent time pressure

Public source: Game Developer, “Designing for meaningful consequences in Unsighted,” 2022-03-16.
https://www.gamedeveloper.com/design/exploring-meaningful-consequences-unsighted

Related developer interview: Game Developer, “UNSIGHTED embraces the catharsis of Metroidvanias through player agency.”
https://www.gamedeveloper.com/design/unsighted-embraces-the-catharsis-of-metroidvanias-though-player-agency

High-level observation: Unsighted connects character availability and consequences to a world-facing time resource. Time pressure forces prioritization; replay or improved knowledge can change later outcomes, while the original consequence still mattered in its own run. The developers also provide an accessibility mode that can relax the timer, showing that narrative premise and exact pressure implementation can be separated.

Reusable Ouros lesson: a deadline or expiry must be durable world state if the story relies on it. Saving and restoring cannot refresh the clock, forget that the window existed or silently convert an expired opportunity into success. At the same time, the exact pressure policy belongs to Ouros design, not to the inspiration source.

Excluded: characters, setting, resource names, plot, combat, dungeon layouts, dialogue and exact timer mechanics.

## Source 2 — PTU FanaticRat's Premade Module Repository

Public source: Pokémon Tabletop forum, “[PTU] FanaticRat's Premade Module Repository,” first posted 2015-03-12.
https://www.tapatalk.com/groups/pokemon_tabletop/ptu-fanaticrat-39-s-premade-module-repository-t3195.html

High-level observation: the repository was explicitly built around short, reusable PTU modules and one-shots that could introduce PTU, give a GM bounded material when preparation time was limited, or act as a break inside a longer campaign. The modules vary in expected length, level and genre rather than requiring every incident to become a permanent main arc.

Reusable Ouros lesson: a persistent world can support bounded incidents with clean entry and exit conditions. An assistance request can be a small episode attached to a larger living world. Its state still needs durable provenance and timing because the surrounding campaign continues before and after that episode.

The forum feedback also notes value in creative and communicative solutions rather than reducing every module to repeated attacks. For Ouros, this supports reduced noncombat implementations when the narrative premise does not require unverified tactical families.

Excluded: module names as Ouros content, towns, NPCs, deities, factions, exact encounters, rewards, maps, homebrew mechanics and authored plots.

## Synthesis

A deferred request has two independent continuities.

The first is causal continuity: who asked, who deferred, which response action owns the decision and which future wake belongs to it.

The second is temporal continuity: whether the reconsideration point is still pending, already processed or outside an optional expiry window.

A restart between the response and the future wake must restore both continuities from one coherent generation. Reconstructing the deferral from conversation history alone risks changing identity, losing expiry or duplicating the wake. Restoring the replan trigger without the deferral record loses the explanation and expiry context that make the trigger meaningful.

## Mechanical boundary

This persistence pattern itself exercises no PTU battle capability. If the later reconsideration selects a tactical incident, capability admission still occurs at that later boundary. A saved DEFER record grants no movement, status, weather, Move, Ability, Item, Trainer Feature or AI tactical capability.

## Unresolved design question

Pass 430 made expiry descriptive. This research does not choose what a runtime should do when it resumes after the optional expiry while the scheduled reconsideration trigger was never processed. Valid future policies include consuming the stale wake without assistance, waking only to record closure, or another explicitly authored expiration transition. The project should choose one policy before claiming expiry has executable consequences.

## Canon boundary

No source above adds facts to Ouros canon. This note provides transformed structural evidence only. Canon remains governed by `canon/` and PTU/Caelo legality remains delegated to authoritative sources and AutoPTU where structured mechanics are required.
