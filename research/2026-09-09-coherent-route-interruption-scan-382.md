# Coherent route interruption scan — Pass 382

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Date: 2026-09-09

## Repository-first deduplication

Before selecting new material, the repository was checked for recent and frequently reused anchors. PokeWilds, Pokémon Undercover, Tales of Visiwa, Hollow Underdeep, Pokémon Odyssey, Pokémon Bushido, Pokémon Infinity, Pokémon Golurk Rising, Pokémon Wastelands-adjacent recent scan themes and other recent pass sources were reviewed by title or source where applicable. PokeWilds and Pokémon Undercover were explicitly excluded because the repository already contains multiple prior uses.

`Pokémon Wastelands` itself had no repository match before this pass. The 2024 PTU ancient-ruins recruitment post used below also had no repository match for its distinctive title/topic string before this pass.

## Public source 1 — PTU exploration campaign built around ancient ruins

Source:
https://www.reddit.com/r/PokemonTabletop/comments/1e9ob4g/

The public recruitment post describes a Pokémon Tabletop United campaign focused on exploration and roleplay around ancient ruins, with maps and additional homebrew material supporting that premise.

Reusable structure:
- the travel/exploration loop can carry the campaign rather than merely connect battles;
- a ruin route can be a persistent investigative space visited for different reasons;
- interruptions, access changes and new evidence can change what an expedition does without replacing the campaign premise;
- custom mechanics should remain visibly separate from base PTU capability claims.

Transformation for Ouros:
Use persistent field routes and sites whose accessibility and interpretation can change over time. Do not import the campaign's characters, maps, homebrew Pokémon, bespoke mechanics or any unpublished GM material.

## Public source 2 — Pokémon Wastelands

Primary public project page:
https://www.eeveeexpo.com/threads/8991/

The project presents a compact hostile exploration space with weather as part of the experience and dungeon progress that can be interrupted by blackout/reload rather than requiring the whole premise to reset.

Reusable structure:
- environmental conditions can make route continuity itself a meaningful gameplay question;
- interruption can preserve knowledge gained before the interruption even when physical progress is lost;
- short repeatable exploration can support different decisions after the player understands the space better.

Transformation for Ouros:
Preserve route knowledge, observation evidence and institutional consequences across an interruption while allowing physical access to change. Do not import Wastelands characters, forms, locations, morality structure, dungeon layouts, bosses, dialogue or progression rewards.

## Public source 3 — real-world trail closure and reopening as a state model

Source:
https://www.nps.gov/grca/learn/news/south-rim-corridor-trails-partially-reopened.htm

The U.S. National Park Service describes corridor trails changing from closed to partially reopened while other segments remain unavailable. The update distinguishes different route segments, specific causes, current safety state and later expected access changes.

Reusable structure:
- access is a time-varying property of individual route segments rather than a permanent property of an entire destination;
- a route can become invalid after a journey has begun while another path remains viable;
- reopening one segment does not imply every connected segment is open;
- the cause of a closure and the current access state are separate facts that can have different evidence owners.

Transformation for Ouros:
Represent a route interruption as evidence about the attempted route at that moment. Keep the underlying cause separately attributable. A later replan can choose a detour, wait, seek permission, investigate the closure or abandon the objective.

No real-world policy, agency, place or procedure is imported into canon.

## Design synthesis

The combined pattern is a persistent expedition network where route state can change independently of mission state.

Useful causal sequence:

`PLAN_SELECTED -> ACTION_STARTED -> ROUTE_STATE_CHANGED -> TRAVEL_REPLAN_REQUIRED -> NEW_INFORMATION/INVESTIGATION -> REPLAN`

The current executable world-agent layer can already prove the action start and the `TRAVEL_REPLAN_REQUIRED` transition when supplied with the interruption-time route state. It does not yet prove the external cause of the route change unless another owner records it.

## PTU/Caelo boundary

No new PTU mechanic is asserted by this research. The reduced concept uses semantic travel and world-agent state only.

Any later tactical implementation involving difficult terrain, weather, hazards, forced movement, reactions, delayed effects, complex statuses, move-specific route clearing, Abilities, Items or Trainer Features must be admitted against current engine evidence individually.

## Engine evidence inspected

Read-only AutoPTU-Java head: `3a6be5d6a70fbce05e693495d02300d6948100c2`, merge #416. The current evidence strengthens the specific production round-start Intimidate rollover seam. It does not establish blanket Ability or full lifecycle coverage.

Read-only AutoPTU Python head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The current head is presentation-only viewport synchronization.

No engine repository was modified.
