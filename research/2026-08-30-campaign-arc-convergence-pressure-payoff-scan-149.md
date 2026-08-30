# Ouros Narrative Research — Campaign Arc Convergence, Pressure & Payoff — Pass 149

Status: RESEARCH ONLY. Provenance and design evidence. Nothing in this file establishes Ouros canon.

Date: 2026-08-30

## Research question

How can Ouros sustain months of play in which local quests, rivals, factions, mysteries, expeditions and personal goals remain independently meaningful, then sometimes converge into larger arcs without turning the world into a fixed quest chain or a global doomsday clock?

This pass follows Pass 148's boss-dramaturgy work. Pass 148 owns the shape of a major confrontation. Pass 149 studies what must happen before and after that confrontation so a finale is earned by prior world state rather than inserted because an author wants a boss scene.

## Internal repository cross-check

The complete repository tree was inspected before writing and was returned with `truncated: false` at narrative head `ea85f0a3b4b16f5cbc11769b4b9fb1284b6184a6`.

Relevant existing owners:

- `design/ouros-narrative-architecture.md` already owns local closure/global consequence, quiet/pressure pacing, Chronicle callbacks and the principle that major authored arcs remain human-controlled.
- `design/world-agency-layer.md` already owns autonomous actor activity, faction fronts, actor knowledge and world-pulse budgets.
- `design/mission-dungeon-grammar.md` already owns individual mission assembly, activity blocks and failure-forward mission outcomes.
- `design/antagonist-agency-defection-escalation-layer.md` already owns adversarial plans, escalation, attention, defections and successor behavior.
- `design/boss-encounter-dramaturgy-phase-objective-extension.md` already owns major-confrontation beats and full/reduced tactical forms.
- `design/rivalry-recurring-peer-progression-extension.md`, `design/public-memory-event-legacy-layer.md`, `design/organization-faction-identity-lineage-continuity-extension.md` and other continuity layers already preserve their own histories.

The missing layer is therefore not another quest generator and not another faction simulator. It is the connective grammar that tracks several long-lived threads, recognizes when their current states legitimately intersect, manages pressure without forcing every front to advance, and records which earlier setups have earned callbacks or payoffs.

## PTU / Caelo guardrails

The project's internal source scan records that the PTU Core Rulebook explicitly supports central plots, character-centric arcs and sandbox activity. It also recommends alternating calmer periods with larger-plot pressure and connecting different player interests while allowing sessions to provide local satisfaction.

That supports an Ouros campaign in which a main arc is one pressure source among several rather than a permanent override of every other activity.

No internal PTU/Caelo evidence found for this pass establishes:

- a universal campaign clock;
- mandatory advancement of a villain whenever players perform side content;
- a universal three-act structure;
- a generic `finale` mechanical state;
- mandatory Gym participation as the only narrative spine;
- a rule that a major reveal invalidates previously observed facts;
- a mechanical bonus for recognizing a callback or foreshadowed event.

Those remain narrative design concerns unless a specific governing rule says otherwise.

## Public Pokémon structure: Mystery Dungeon — parallel work and earned convergence

Sources:

- Pokémon Mystery Dungeon: Explorers of Time and Explorers of Darkness overview: https://en.wikipedia.org/wiki/Pok%C3%A9mon_Mystery_Dungeon%3A_Explorers_of_Time_and_Explorers_of_Darkness
- Grovyle reference: https://bulbapedia.bulbagarden.net/wiki/Grovyle_the_Thief
- Supplemental plot reference used only to cross-check the parallel-objective sequence: https://pokemon.fandom.com/wiki/The_Future_(Mystery_Dungeon)

Reusable high-level pattern:

A long arc can recontextualize earlier incidents without deleting them. The local effects of removed Time Gears were real observations; the later revelation changes their interpretation and the understood motive behind them. After the reversal, important allies do not simply teleport into agreement because the plot says so. Prior observations and relationships make the new account assessable. The protagonists and Grovyle then perform different jobs in parallel: one side gathers needed objects while another investigates access to the destination. Those independent efforts later converge.

Ouros lesson:

- store observed event, interpretation and canonical explanation separately;
- permit a reveal to change `belief_about_event` without rewriting `event_fact`;
- allow major arcs to split into parallel threads owned by different actors;
- converge those threads only when their current outputs create compatible world-state conditions;
- let old relationship/evidence state affect whether a recontextualization is believed.

No characters, locations, artifacts, dialogue or distinctive plot events are imported.

## Pokémon Tabletop community: long campaigns expose lane and pacing mismatch

Source:

- Reddit /r/PokemonTabletop, “Campaign pacing help,” 2025-03-31: https://www.reddit.com/r/PokemonTabletop/comments/1jo8d4i

A GM describes a campaign running roughly two and a half to three years where players spend substantial time exploring towns and preparing before Gyms. Responses ask what each player wants from the game and suggest that obvious conflicts or prerequisites work best when tied to those interests.

Reusable lesson:

Long campaign pacing cannot assume that the presence of a Gym or main objective automatically creates urgency for every character. Different players may be pursuing preparation, money, capture, exploration or other goals. Artificial pressure can move play, but constant timers risk turning optional lanes into fake choices.

Ouros use:

Major arcs should expose several legitimate participation surfaces where the fiction permits them. A faction problem might also generate a research question, expedition lead, professional assignment, rival opportunity or ecological consequence. Those surfaces must come from actual world state; they must not be fabricated merely to force every character into the same scene.

This community discussion is design inspiration only, not PTU rules authority.

## Node-based scenario design: convergence conditions are safer than plotted arrows

Sources:

- The Alexandrian, Node-Based Scenario Design: https://www.thealexandrian.net/creations/misc/node-design/node-design.html
- Node-based campaign-scale “cloud” discussion: https://www.thealexandrian.net/creations/misc/node-design/node-design6.html

Reusable lesson:

A rigid plotted sequence creates chokepoints because the PCs must follow authored arrows. Node-based design instead prepares situations, entities and links. Campaign-scale complexity can emerge from modular nodes without pre-authoring every possible path. Nodes can even move or be recombined when the underlying actors plausibly adapt.

Ouros translation:

Do not store a long arc primarily as `scene_1 -> scene_2 -> scene_3 -> finale`. Store active questions, actors, fronts, evidence, locations, dependencies and possible convergence states. A planned scene becomes invalid when its actors, resources or premise no longer exist. The system should preserve the unresolved pressure and re-evaluate it rather than resurrecting the old scene.

## Slow-burning fronts: pressure without false urgency

Source:

- Sly Flourish, “Custom Fronts of Storm King's Thunder”: https://slyflourish.com/fronts_of_skt.html

Reusable lesson:

Multiple threats can move slowly enough that players retain meaningful freedom. A front represents one possible future and can shift as the world changes. Choosing to address one threat should not automatically force every other threat to jump forward merely to punish the players.

Ouros translation:

World Agency already owns faction-front advancement. Pass 149 should add a campaign-facing pressure budget that chooses which existing developments become highly salient at the same time. A dormant or low-pressure thread can remain real without advancing. Urgency must have a cause and a player-facing signal.

## Existing Ouros lesson reinforced: local closure can feed a larger whole

The early source scan already records episodic fanfiction and Pokémon Tabletop side-quest discussions as evidence that local stories can close while contributing outward edges. Pass 149 does not replace that principle. It adds a ledger for those outbound edges so a later callback is earned and causally attributable.

## Derived campaign invariants

The following distinctions are proposed design invariants, not canon facts:

`THREAD_ACTIVE != THREAD_URGENT`

`THREAD_DORMANT != THREAD_ABANDONED`

`FRONT_ADVANCED != PLAYER_FAILED`

`SETUP_RECORDED != PAYOFF_PROMISED`

`FORESHADOWED != GUARANTEED_TO_HAPPEN`

`CALLBACK != REPETITION`

`CONVERGENCE_ELIGIBLE != CONVERGENCE_FORCED`

`SAME_LOCATION != SAME_GOAL`

`ALLY_PRESENT != ALLY_CONTROLLED`

`REVEAL != RETCON`

`RECONTEXTUALIZED != PRIOR_OBSERVATION_ERASED`

`LOCAL_VICTORY != GLOBAL_ARC_RESOLVED`

`BOSS_DEFEATED != OPPOSITION_ENDED`

`FINALE_AVAILABLE != FINALE_MANDATORY_NOW`

`ARC_RESOLVED != CONSEQUENCES_COMPLETE`

## Design risks identified

### The permanent emergency

If every major thread advances whenever the players train, shop, explore or pursue a personal goal, the campaign says “freedom” while mechanically punishing freedom.

### The prophecy ledger

If every incidental detail is marked as future setup, callbacks become forced and the world feels authored backward from a predetermined finale.

### The convergence teleport

Actors who have unrelated goals must not suddenly appear together because the finale needs a cast. Presence requires reach, knowledge, motivation and timing.

### The revelation overwrite

A later explanation must not delete earlier events that were directly observed. It may invalidate an inference, expose deception or add a hidden cause.

### The compulsory ensemble

Not every faction, rival, mentor and NPC needs to appear in a final scene. A payoff can occur earlier, later or in a separate lane.

### The boss-room preservation rule

If players make a planned confrontation irrational or impossible, the confrontation changes or disappears. The campaign may preserve consequences but never preserve an invalid scene only because content was authored for it.

## Research conclusion

Ouros already has strong local state, actors, fronts, mission grammar and confrontation contracts. The next useful layer is a campaign-scale connective model: independent threads, pressure salience, convergence eligibility, deliberate setup/payoff tracking and aftermath residue.

The target is not a generated novel. It is a stateful campaign fabric where several locally complete stories can later become one larger situation because their world facts actually intersect.