# Pass 375 research — plan-selection alternative provenance

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-09
Canon impact: NONE

## Repository boundary inspected

This pass follows Pass 374. V15 can prove delivery, evidence materialization, replan-trigger creation and trigger consumption. The current planner can select an AgendaDecision from goals, needs, commitments and situational intents, but the winning result alone does not preserve the complete decision-time alternative set.

Existing canon governance remains unchanged: research is evidence, proposals are candidates, design files define architecture, and only canon/ establishes approved Ouros world facts.

Internal mechanical source priority remains PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and the Caelo Region Location & Encounter List. Public narrative references have no PTU/Caelo mechanical authority.

## Duplicate avoidance

Repository search was performed before selecting sources. Recent heavily processed references such as Pokémon Burning Scales and Pokémon: Adventures in the Millennium were not reused. No repository match was found for Pokémon Rejuvenation, Pokémon Project Vanguard or Pokémon Odyssey by those names at selection time.

## New source 1 — decision records preserving rejected alternatives

Source: Decision Log, public product documentation, accessed 2026-09-09.
https://www.decisionlog.ai/

Useful high-level pattern:

A durable decision record preserves what was selected, why it was selected, actor/provenance evidence and supersession history rather than allowing later state to silently rewrite the meaning of the earlier choice. Its public description also separates proposed candidates from active decisions.

Ouros transformation:

World-agent replanning should be reconstructable from the decision-time evidence set. A later route, position or successful outcome must not be treated as proof of which alternatives existed when the NPC chose. Candidate inputs and the selected AgendaDecision can be persisted as replayable provenance without making the provenance owner responsible for the planning policy itself.

Nothing from the product's implementation or commercial workflow becomes Ouros canon.

## New source 2 — Pokémon Rejuvenation

Source: public Pokémon Rejuvenation V14 project information, accessed 2026-09-09.
https://pokemonrejuvenation.com/

Useful high-level patterns:

- long-form regional progression can combine chapter structure with side content;
- choices can alter later route access and encounter sequencing;
- major encounters can use environmental/field context to change how a location plays.

Ouros transformation:

A regional problem can expose multiple legitimate objectives at once. An NPC expedition may have an institutional instruction, a personal obligation, a local emergency and an environmental constraint competing in one replanning window. Persisting the competing inputs makes later consequences intelligible without copying route plots, named characters, factions, locations, field systems or boss designs.

## New source 3 — Pokémon Project Vanguard

Source: public project overview dated 2026-07-03, accessed 2026-09-09.
https://t.co/WAxgkGSShE

Useful high-level patterns:

- progression can be organized around institutional duties instead of a conventional badge circuit;
- rank, regional protection work and mysteries can provide recurring reasons to revisit places;
- missions can define a character's role in the world without making every task part of one central villain plot.

Ouros transformation:

Institutional commitments can be first-class plan candidates alongside needs and situational emergencies. A field researcher, ranger, courier, technician or local authority can rationally abandon an instruction when a harder obligation wins the same deterministic agenda arbitration.

Academy names, characters, mysteries, regional forms and plot material are excluded.

## Additional comparison — Pokémon Odyssey

Source: public project overview, accessed 2026-09-09.
https://romhaven.com/games/pokemon-odyssey/

Useful high-level pattern:

A dungeon/exploration loop can combine deeper traversal, gathering, sidequests, preparation and optional objectives. The reusable lesson is that one expedition can carry several concurrent reasons to continue, retreat, divert or spend resources.

Ouros transformation:

Dungeon or field-site encounters should expose explicit objective competition. A route instruction may lose to rescue, specimen preservation, evacuation or survival without invalidating the original instruction.

Names, labyrinth structure, characters, progression systems, layouts and story material are excluded.

## Design synthesis

The reusable structure is a decision-time alternative set:

trigger batch -> actor state -> goals / needs / commitments / situational intents -> deterministic agenda selection -> selected intent

The provenance owner should preserve enough input state to replay the existing planner and confirm the stored winner. It should not introduce a second scoring policy. It should also link every selection back to the consumed replan batch that caused the decision.

This produces useful narrative ambiguity without arbitrary NPC behavior. Different observers may know different triggers or outcomes, but recovery can still prove what the planner actually considered.

## PTU / Caelo and engine boundary

Plan selection belongs to Ouros world-agent policy, not PTU battle arithmetic. No PTU rule is changed by this pass.

A proposed field consequence can remain battle-free. If expanded into a structured encounter, each mechanic must still be admitted separately through the permanent engine capability categories. Weather phases, forced movement, reactions, delayed hazards, special statuses, ability-triggered terrain or Trainer Feature interrupts remain gated unless live tests/contracts verify those exact families.

## Proposed narrative direction

Use a field expedition where a valid reroute message, a scheduled survey obligation, fatigue pressure and an emergency habitat-protection commitment become simultaneous candidates. The emergency wins. Later observers can incorrectly infer that the reroute was ignored unless they can inspect the decision-time alternative set.

This direction remains PROPOSED / NON-CANON.
