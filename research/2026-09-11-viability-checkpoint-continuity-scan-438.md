# Viability Checkpoint Continuity Research — Pass 438

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Date: 2026-09-11
Narrative baseline inspected before writing: `d85b52aa5aca40244ab32e90712c77cd2dcf6e3c`.

The recursive repository tree was inventoried before authoring. Current focus, canon inventory, design/proposal/research/source/test/tool surfaces relevant to global NPC assistance, Passes 422–437, the Kairos/PTU routing material and live read-only AutoPTU evidence were reviewed before selecting this slice.

Searches were also checked against repository history to avoid intentionally reprocessing recent anchors. The Last Express and the specific Pokémon Reborn mulch quest below were not found as existing research anchors by title.

## Source 1 — The Last Express: concurrent schedules continue without waiting for the player

Public source:
https://en.wikipedia.org/wiki/The_Last_Express

Supporting public description:
https://gamefaqs.gamespot.com/pc/198971-the-last-express/faqs/61183

Observed high-level structure:

The adventure runs primarily on an accelerated real-time clock. Events occur at specific times, while multiple NPCs move through their own schedules. The player can miss conversations or events because other people continue acting elsewhere.

Reusable lesson for Ouros:

Persistent named actors should not freeze because the player left the chunk or the server crossed a save boundary. An accepted appointment, a later blocker and the wake-up caused by that blocker must therefore survive together. Restoring only the appointment would create false ignorance; restoring only the blocker would lose why it matters.

Transformation boundary:

Ouros does not import the train, characters, chronology, conspiracies, scenes, rewind mechanic, dialogue or authored schedule. The reused abstraction is concurrent actor schedules plus time-dependent event continuity.

## Source 2 — Pokémon Reborn Mulch Sidequest: optional opportunity with a finite availability window

Public source:
https://pokemon-reborn.fandom.com/wiki/Mulch_Sidequest

Observed high-level structure:

The optional task becomes available after a progression threshold, asks the player to recover several distributed objects in the city, and is available only until a later progression boundary.

Reusable lesson for Ouros:

An ordinary local job can coexist with larger story progression and still possess a finite opportunity window. The world does not need to turn every missed or obstructed job into a battle or global failure. What matters is that availability is world state, not UI decoration.

Transformation boundary:

Ouros does not import the quest giver, items, reward, exact locations, badge gate or collection pattern. The reused abstraction is a small optional obligation whose opportunity can close while other stories continue.

## Project-local PTU/Caelo cross-check

The project-local Kairos/PTU routing material remains rules/source navigation rather than automatic Ouros authority. Pass 438 introduces no move, ability, Item, Trainer Feature, status, terrain modifier, weather effect, hazard, reaction, forced movement or combat objective.

The new checkpoint contract only preserves already-existing world-simulation facts. If a later scene becomes tactical, the exact mechanic must still be routed to its PTU/Caelo source and verified against live AutoPTU contracts/tests.

## Live engine evidence

AutoPTU-Java read-only head inspected: `d2b3c593d235f1c841ca936df91c42c4a881f000`, merge of PR #447.

That head adds a server-authoritative switch-trigger planning seam for Quick Switch with AP requirement/consumption, candidate replacements, trigger guards, optional interrupt metadata, switch policy and deduplication. This is concrete evidence for that narrow path. It does not verify action economy/initiative, reactions/interrupts or Trainer Features/perks as complete families.

AutoPTU Python read-only head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its head explicitly describes the change as presentation-only coordinate synchronization after viewport resize and states that battle rules and outcomes do not change. It provides no new mechanics authority for this pass.

## Capability posture

For any later mechanically rich encounter growing from the proposal attached to this research:

- targeting/footprints/range/LoS — VERIFIED only in audited scopes;
- base movement legality — VERIFIED only in audited scopes;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED only in audited scopes;
- action economy/initiative — PARTIAL;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING by exact behavior;
- move-specific behavior — individually gated;
- abilities — PARTIAL and individually gated;
- items — individually gated;
- Trainer Features/perks — individually gated; current Quick Switch evidence is narrow;
- AI legal-action infrastructure — VERIFIED only for ordinary audited actions; specialized inspect/escort/protect/retrieve/carry/brace/extract needs explicit admission;
- AI tactical policy — BLOCKING for specialized objective policies;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL / BLOCKING for specialized objective state, non-KO completion and in-flight recovery.

Pass 438 promotes none of these families.

## Derived Ouros design lesson

A persistent world should remember both sides of a contradiction in time: what was promised and what later made that promise difficult. Restart must not collapse them into one synthetic current fact.

A route can be blocked at 14:20 and restored at 14:50. If a server restart occurs at 14:35, the 14:20 observation must still exist afterward with the accepted appointment that gave it meaning. If access later returns, `RESTORED` is appended rather than replacing the closure history.

This supports accountability, investigation, believable schedules and knowledge asymmetry without requiring tactical simulation.
