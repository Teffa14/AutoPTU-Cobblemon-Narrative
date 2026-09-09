# World action-start recovery scan — Pass 378

Status: RESEARCH / PROVENANCE
Date: 2026-09-09
Canon effect: NONE

## Repository inspection and deduplication

The narrative repository tree was inspected recursively at `f0bdc38aebe5c26999ddb4ea4200aed55112781c` before writing. Current focus, canon governance, the recent world-agent checkpoint chain, Pass 377 action-start owner/tests, existing research/proposal naming and PTU/Caelo authority notes were checked before selecting this slice.

Recent sources already used by the project were not reused as primary inspiration. Search results that resurfaced Pokémon Rainbow Wing, Pokémon Prisme, Pokémon Odyssey, Pokémon Stalactite, Burning Scales, Valoryn and other recent references were rejected for this pass.

## Operational source — AWS Step Functions task/execution states

Source: AWS Step Functions documentation.

URLs:
- https://docs.aws.amazon.com/step-functions/latest/dg/state-task.html
- https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListExecutions.html

Public documentation distinguishes a task start event from the later success/failure response, and execution status can independently be RUNNING, SUCCEEDED, FAILED, TIMED_OUT or ABORTED.

Reusable structure for Ouros: starting work is durable history even when the terminal result has not happened. Recovery should preserve the start boundary instead of looking at a later result and guessing when execution began.

Not imported: AWS products, APIs, timeout rules, retry policy or infrastructure terminology as in-world technology.

## New public PTU source — Pokémon: Dust

Source: public StartPlaying campaign page for `Pokémon: Dust - A Pokemon Tabletop United Western Campaign`.

URL: https://startplaying.games/adventure/cm6b0nrze0084grdr2dlvfhca

The public campaign description presents wilderness exploration as requiring the trainer's own capabilities and relationships alongside Pokémon, with mysteries and discoveries distributed through a dangerous frontier rather than confined to battles.

Reusable structure for Ouros: a field journey can become narratively meaningful as soon as characters physically enter a risky route. The important world fact may be that the expedition left, even before arrival, battle or objective completion exists.

Not imported: Mojave setting, western styling, outlaws/lawbringers, cryptid Pokémon, gym structure, NPCs or campaign plot.

## New public fan-game source — Pokémon Recollection Quest

Source: public PokeHarbor project page summarizing the completed ROM hack by The Sylph is In and linking its original PokeCommunity release thread.

URL: https://www.pokeharbor.com/2024/10/pokemon-recollection-quest/

The published premise begins after a ranger is separated from their team by a flood. Progress then combines local problems, reconnection with the missing team and a small number of scripted battles rather than random combat.

Reusable structure for Ouros: an interrupted expedition can create a playable aftermath without requiring the interruption itself to be a boss encounter. Once departure or separation is proven, later clues can concern route, equipment, local help, missed rendezvous and reconnection.

Not imported: Amelia, Elthe City, the special Eevee, shards, scripted encounters, dialogue, maps, characters or plot sequence.

## Ouros synthesis

A useful investigation grammar follows from the three sources:

`PLAN_SELECTED -> ACTION_STARTED -> TRACE_EXISTS -> TERMINAL_STATE_UNKNOWN`

The player may encounter evidence that an action genuinely started while its completion remains unknown. That supports mysteries where nobody needs to lie and the scheduler does not need omniscience.

Examples of original evidence patterns:

- a camp inventory records which field cases were actually taken;
- a route checkpoint records a departure but no arrival;
- weather damage makes the expected path harder after departure;
- another team receives a delayed rendezvous request;
- a local NPC encountered the party on the route but cannot establish what happened afterward;
- an AutoPTU binding exists for a structured interruption while no result has yet ingressed into the world layer.

These are design patterns only. No new location, institution, species, technology or historical event becomes canon in this pass.

## PTU / Caelo cross-check

Internal project authority remains PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and the Caelo Region Location & Encounter List where available.

Pass 378 introduces no new battle rule, species placement, move, Ability, Item, Trainer Feature or Caelo geography claim. External sources are research provenance only.

The action-start checkpoint delegates all structured battle resolution to AutoPTU. World travel start remains a semantic world-agent transition and must not be confused with tactical PTU movement.

## Read-only engine evidence

AutoPTU-Java live head inspected: `6cc66d91d286fab06365cf37d88dd04038589195`, merge #415, `freeze authoritative round-start rollover state parity`. The change adds oracle-backed coverage for round rollover, initiative order/cursor and the first actor after rollover. This strengthens that exact lifecycle/initiative seam only.

AutoPTU Python live head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, presentation-only viewport synchronization. No battle-rule implication.

Neither engine repository was modified.

## Research consequence for Pass 378

The implementation target is therefore narrow: put the already replayable Pass 377 action-start ledger under coherent world recovery. Do not advance directly to action completion because current evidence supports preserving the transition boundary more strongly than inferring terminal outcomes.
