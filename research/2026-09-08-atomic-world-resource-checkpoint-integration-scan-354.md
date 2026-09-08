# Atomic world/resource checkpoint integration scan — Pass 354

Status: RESEARCH / PROVENANCE ONLY
Canon authority: NONE
Date: 2026-09-08

## Internal inspection before research

Pass 353 already created `OUROS_NPC_RESOURCE_CHECKPOINT_V1` for Pass 339 reservations and Pass 342 resource requests, with deterministic round-trip and fail-closed validation. Its contract explicitly left insertion into the global world checkpoint for the next bounded slice.

`tools/global_npc_world_checkpoint.py` currently owns `OUROS_NPC_WORLD_CHECKPOINT_V5` and restores coupled world-agent state atomically. `CURRENT_FOCUS.md` requires restart to preserve causal state rather than independently restoring components from unrelated moments.

The repository search also reconfirmed the governing project-source inventory: PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and the Caelo Region Location & Encounter List. This pass adds persistence infrastructure only and does not claim a new PTU or Caelo rule.

## New public sources

### FableImpact — campaign continuity tooling

Source: https://fableimpact.com/

Public material describes campaign state in terms of faction memory, clocks, session consequences and delayed fallout that must remain available after the originating session. Reusable lesson: session boundaries should not erase obligations that are still live in the fiction. A later scene can legitimately depend on an earlier decision without requiring the GM to restate it as new truth.

Adaptation for Ouros: reservations and accepted resource requests need to cross the same restart boundary as NPC memory, travel and communication when later world decisions depend on them.

No setting text, characters or proprietary scenario content is imported.

### Inkweave — confirmed events versus speculative table language

Source: https://www.inkweave.net/journal/session-notes-are-not-world-state/

The public article distinguishes plans, attempted actions and confirmed world outcomes. Reusable lesson: durable world state should preserve confirmed events rather than treating every statement or intention as an accomplished fact.

Adaptation for Ouros: checkpoint restore reconstructs existing reservation/request records. It must not re-execute reservation creation, re-accept a request or infer a missing handoff.

No prose is copied into canon.

### Pokémon Burning Scales — dense sidequest continuity in a small open world

Source: https://github.com/Benitex/Pokemon-Burning-Scales

The project's public README describes a compact Pokémon open world with many side quests, choices that affect later material, a quest system that tracks objectives/locations, multiple saves and autosave support.

Reusable lesson: a small geography can support long-form play when local obligations survive transitions and remain discoverable. Side content gains weight when the player can leave, pursue another thread and later return to a world that still remembers the earlier commitment.

Adaptation for Ouros: resource obligations can remain minor optional threads while persisting across travel, unrelated scenes and restart.

No Burning Scales characters, mystery, dialogue or plot are imported.

### Pokémon Tabletop United actual-play continuity check

Sources:
- https://podcasts.apple.com/us/podcast/pokemon-world-tour-united/id1154176782
- https://podcastaddict.com/podcast/the-reckless-rollers/2836264
- https://www.podchaser.com/podcasts/pokemon-adventures-in-the-mill-702825

Public catalogs confirm long-running PTU campaigns organized across many episodes, arcs, jobs, downtime and accumulated campaign history. `Pokemon World Tour: United` and `The Reckless Rollers` were already processed in recent Ouros passes, so Pass 354 does not mine their episode plots again. `Pokemon Adventures in the Millennium` is used only as another structural confirmation that PTU actual play supports long multi-act continuity.

Reusable lesson: PTU campaign structure can carry consequences across long gaps without every old obligation becoming main-plot content.

No distinctive character, episode plot, dialogue or protected prose is imported.

## Duplicate-source control

Pass 353 already used Pokémon Living World and West Marches-style persistent-world material, so those sources were not reprocessed. Recent passes already used `Pokemon World Tour: United` and `The Reckless Rollers`; they were checked for currency but not treated as new extraction targets.

Repository search found no prior use of FableImpact, Inkweave or Pokémon Burning Scales.

## Derived Ouros design lessons

A save boundary is a causal boundary only if all state needed to explain the next decision comes from the same logical moment.

A historical resource record survives restore as evidence. Restore does not replay its business operation.

Older saves that predate resource persistence cannot prove historical reservations or requests. Compatibility should therefore restore empty resource ledgers instead of fabricating inferred history.

Future reservations can legitimately exist in a checkpoint because booking is prospective. A request creation or request transition dated after the checkpoint's semantic time is contradictory and must fail closed.

Persistence should preserve side obligations without promoting them to main-plot status. A resource request can wait while the player explores, battles, travels or follows another questline.

## PTU/Caelo boundary

No new combat mechanic is claimed here. PTU/Caelo source material remains authoritative whenever an encounter uses movement, actions, statuses, Moves, Abilities, Items or Trainer Features.

The persistence layer may remember that a later encounter is owed or that a resource was reserved. It may not create a battle effect, invent a PTU action or cause a Minecraft entity to become the authoritative owner of the state.
