# Persistent resource history across restart — research scan 353

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-08
Canon authority: NONE

## Question

How can Ouros preserve long-running resource commitments across session/runtime boundaries without flattening history into only the latest state, and how can that persistence become useful narrative material rather than invisible infrastructure?

## Internal duplicate check

The repository already covers resource identity and readiness, reservations, requests, handoffs, failed attempts, appointment notices, rescheduling, admission conflicts, allocation decisions, displacement application, notice obligations, recipient binding and terminal communication provenance in Passes 338–352. The atomic world checkpoint predates those layers. Its V5 payload protects core world-agent, information, evidence and decision-chain state, while the recent resource ledgers remain outside that durability boundary.

Searches for `West Marches`, `Pokémon Living World`, `PokeLiving` and `event sourcing` returned no prior research entries in the repository before this pass.

## New public sources

### West Marches persistent-world structure

Role-playing Games Stack Exchange, “What defines a West Marches campaign?”
https://rpg.stackexchange.com/questions/120770/what-defines-a-west-marches-campaign/120776

Reusable structure: several groups act in one shared world, discoveries persist, and shared records can be incomplete or mistaken. The useful Ouros lesson is persistence with provenance: later actors encounter the consequences and records produced by earlier activity rather than a reset version of the location.

Do not import the specific map, monsters, treasure structure or competitive assumptions.

### Pokémon Living World public project description

Pokémon Living World
https://www.pokeliving.com/

The public project describes persistent NPC memories, relationships and a world that continues while a player is absent. This is useful only as contemporary fan-design evidence that persistence itself is part of the player-facing fantasy in Pokémon-derived projects. Ouros should retain its own deterministic world-agent architecture and authored canon; no characters, dialogue, Johto continuity or implementation claims are imported.

### Event-sourced history and snapshots

Blueprint, “Event Sourcing”
https://blueprint-hld.vercel.app/patterns/event-sourcing

Reusable structure: immutable changes can remain authoritative while current state is projected from them; snapshots accelerate restoration without rewriting historical events. This matches Ouros resource owners such as request events and allocation applications, where historical records must survive even after operational state changes.

The architecture is inspiration, not a requirement to convert Ouros into a general event-sourced database. Pass 353 preserves the existing dataclass ledgers and adds a serialization boundary only.

## Transformed Ouros design lessons

1. Restart should preserve commitments that still have consequences. An active reservation, an accepted request and their provenance must not vanish because the simulation crossed a process or session boundary.
2. Historical and operational truth can coexist. A closed or displaced booking may remain in history while projections decide what currently blocks a resource.
3. Persistence should retain actor identity and time. Restoring an event without its requester/provider/actor or semantic tick destroys the causal explanation that later investigations need.
4. Checkpoint data should fail closed when it cannot reconstruct a valid causal chain. An event referring to a missing request or a non-participant actor is not safe to silently accept.
5. The resource owner remains authoritative. The checkpoint codec serializes and reconstructs the existing reservation/request records; it does not decide availability, acceptance, cancellation or allocation.

## PTU / Caelo cross-check

No new PTU combat rule is introduced by this persistence slice. Existing project source scans identify PTU Core, the Caelo Player's Guide, Caelo Region Location & Encounter List, character-creation material, errata/extras and Pokédex material as the governing mechanical/setting references. Pass 353 treats reservations and requests as world-simulation state outside PTU battle resolution.

Any future encounter spawned from a restored resource obligation must still use the permanent engine capability gates recorded in the live readiness snapshot. Persistence does not grant missing combat mechanics.

## Canon boundary

Research findings are not canon. The proposed case accompanying this pass is PROPOSED / NON-CANON. Existing Marea people and places remain unchanged. No public source establishes Ouros lore.
