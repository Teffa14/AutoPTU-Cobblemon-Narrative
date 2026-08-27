# Competitive Scouting, Battle Replays & Legitimate Preparation — Research Scan 81

Status: research/provenance only. Nothing in this file is Ouros canon.

Date: 2026-08-27

## Research question

How can Ouros support recurring competitive preparation, public battle footage, opponent analysis, post-battle study and rematch planning without giving NPCs or AI omniscient access to private battle state?

This pass was selected only after inspecting the current repository inventory. Closely related systems already exist for battle institutions, recurring rivals, photography/visual evidence, media, public memory and personal records. The useful gap is narrower: a provenance-aware layer that turns legally available observations and recordings into bounded scouting knowledge that can later inform narrative preparation or, once implemented, an approved tactical AI policy.

## Existing Ouros boundaries this pass must preserve

`design/battle-institutions-challenge-circuits-layer.md` already establishes that formal preparation may use public and legally observed information. It already prohibits battle AI from reading world truth or private opponent loadouts merely because those facts exist in persistent state.

`design/rivalry-recurring-peer-progression-extension.md` already permits a recurring peer to adapt to observed history while forbidding hidden-moveset reading, private-inventory counterpicks, arbitrary difficulty scaling and unapproved AI-weight changes.

`design/photography-visual-evidence-layer.md` already distinguishes a primary visual record from later classification and interpretation.

`design/cobblemon-runtime-authority-boundary.md` makes the runtime rule binding: Cobblemon may present battle footage and entities, but its battle-state code cannot decide what tactical facts are true or which combat information an analyst legally knows.

Pass 81 therefore adds no second battle record, rival system, visual-record system or media system.

## Source 1 — Vs. Recorder and Battle Videos

Source: Bulbapedia, “Vs. Recorder” / “Battle Video.”

URLs:
- https://bulbapedia.bulbagarden.net/wiki/Vs._Recorder
- https://bulbapedia.bulbagarden.net/wiki/Battle_Video

Relevant structure:

Pokémon games have explicitly represented battles as records that can be viewed later, shared and, in some generations, downloaded from other players. Generation VI also allowed a saved Battle Video to seed a Mock Battle against an AI representation of the Trainer and team shown in the recording.

Reusable lessons for Ouros:

- a battle can create a replay object separate from the authoritative battle result;
- replay availability is a disclosure/publication state, not an automatic property of every battle;
- recordings can become unavailable or obsolete while the historical battle still exists;
- a replay can be used for practice without turning the practice simulation into a new fact about the original opponent;
- an AI reconstruction based on old footage should be understood as a training model, not as the current real Trainer.

Transformation boundary:

Ouros should not copy the Vs. Recorder device, storage limits, codes or exact Mock Battle mechanics. The reusable structure is battle record -> replay publication -> later review or training simulation.

## Source 2 — Lenora observes challengers, Ash trains for a rematch

Sources:
- Bulbapedia, “The Battle According to Lenora!”
- Bulbapedia, “Rematch at the Nacrene Gym!”

URLs:
- https://bulbapedia.bulbagarden.net/wiki/The_Battle_According_to_Lenora%21
- https://bulbapedia.bulbagarden.net/wiki/Rematch_at_the_Nacrene_Gym%21

Relevant structure:

Lenora is shown watching potential challengers closely and forming an initial judgment from observation. After Ash loses, he goes to a Battle Club for focused preparation before returning. The rematch then reflects both remembered information from the first match and genuine changes made during training.

Reusable lessons for Ouros:

- legitimate observation can happen before a formal match starts;
- defeat can generate a concrete preparation window rather than a hidden numerical buff;
- a rematch can preserve known patterns from an earlier fight while still allowing both sides to change;
- the old encounter should remain evidence of what happened then, not a frozen guarantee of what the opponent will do next.

Transformation boundary:

Ouros must not infer that watching a match grants a PTU bonus. Any actual training gains still require governing PTU/Caelo rules and authoritative progression state.

## Source 3 — Barry watches Ash vs. Fantina

Source: Bulbapedia, “Shield with a Twist!”

URL: https://bulbapedia.bulbagarden.net/wiki/Shield_with_a_Twist

Relevant structure:

Barry watches a Gym rematch in which Ash uses a recognizable counter strategy and Fantina then adapts against it. The scene demonstrates that spectators can learn something real from a public battle while also seeing that a visible tactic can be countered once it becomes legible.

Reusable lessons for Ouros:

- public tactics may become part of another Trainer's legal knowledge;
- a visible strategy can create future expectations without guaranteeing repetition;
- scouting should record evidence and uncertainty, not convert an observed tactic into a permanent personality rule;
- opponents can adapt to public information while remaining bounded by their own legal roster and current state.

## Source 4 — Nemona as recurring observer and analyst

Source: Bulbapedia, “Nemona (anime).”

URL: https://bulbapedia.bulbagarden.net/wiki/Nemona_%28anime%29

Relevant structure:

Nemona repeatedly watches battles involving recurring peers, later battles them herself, and in another scene analyzes a battle between other Trainers. Her role shows how an experienced recurring competitor can accumulate legitimately witnessed information across multiple events without needing to be present inside every private training session.

Reusable lessons for Ouros:

- recurring peers can maintain a growing observation history;
- witnessed battles, public reports and direct encounters should be distinguishable sources;
- a peer can recognize progression from repeated evidence without gaining access to private build data;
- third-party battles can matter to the competitive world even when the player is not a participant.

## Source 5 — Pokémon Tabletop community discussion: rival design should stay reactive

Source: Reddit /r/PokemonTabletop, “Rival Team for Kanto based PTU Campaign” (2026).

URL: https://www.reddit.com/r/PokemonTabletop/

Research note:

The public discussion warns against fully scripting a rival's distant end-state team too early and suggests letting rival construction respond to what actually develops in play. For larger parties, commenters also discuss the value of a rival group rather than making one NPC mirror every player need.

Reusable lesson:

A recurring rival is stronger when preparation responds to actual observed campaign history. Ouros should avoid generating exhaustive counterteams against hidden player state simply to maintain difficulty.

Provenance caution:

This is community advice, not PTU rules authority. It supports narrative design only.

## Source 6 — PTU play-by-post tournament cadence

Source: Reddit /r/PokemonTabletop, “Battle Island - Play by Post” (2021).

URL: https://www.reddit.com/r/PokemonTabletop/

Research note:

The public campaign pitch used a repeating weekly structure leading into a tournament and gave characters recurring rivals. The useful structure is not the homebrew mechanics; it is the existence of a predictable preparation window in which teams, relationships and public knowledge can change before competition.

Reusable lesson:

Competitive arcs benefit from explicit time between events. Scouting, training, travel, roster changes, interviews and public discussion can become meaningful world state before the next official match.

## Cross-source synthesis

The strongest reusable structure is not “Trainer knows opponent weakness.” It is a chain with provenance:

battle or observation occurs
-> an authoritative result/reveal exists
-> a witness, replay, report or publication makes some portion available
-> an observer actually receives or views that source
-> the observer creates an analysis claim
-> the claim may be correct, incomplete, stale or overfit
-> preparation changes only through legal existing systems
-> a later battle tests the preparation
-> new reveals become part of future history

This creates competitive intelligence without omniscience.

## Design lessons for Ouros

### 1. Observed effect and confirmed mechanic must be separate

A spectator may see a projectile, switch, status-like behavior or positioning pattern without knowing the exact Move, Ability, Item or Trainer Feature responsible.

The record should support states such as:
- effect observed, mechanic unknown;
- Move publicly announced/confirmed;
- Ability revealed through an authoritative battle event;
- Item revealed through an authoritative event;
- analyst hypothesis only.

Visual similarity alone cannot establish a mechanical identity.

### 2. Public result is weaker than full replay

A public result can establish winner, participants and whatever the institution officially publishes. It should not imply turn-by-turn access.

A replay can reveal more, but still only what the replay contains.

A commentary summary may omit turns, mislabel a tactic or emphasize a narrative angle.

### 3. Old footage must become stale naturally

A replay proves what a Trainer brought and revealed during that historical match. It does not prove:
- current roster;
- current Moves;
- current held items;
- current Trainer Features;
- current AI priorities;
- current injury/status state;
- current private strategy.

Staleness is a property of the information relationship, not a reason to delete the old record.

### 4. Analysis itself is a claim

A coach or rival may conclude that a Trainer “always opens aggressively” after two matches. That conclusion can later fail.

Store the source matches and analysis separately so Ouros can tell the difference between observation and interpretation.

### 5. Practice simulations need a hard identity boundary

A mock opponent built from a public battle record is a training artifact. It must not:
- write changes into the real opponent;
- reveal newer private data;
- count as a formal battle against that person;
- create public competitive history for the real person;
- be treated as proof of how the real opponent will act next time.

### 6. Opponent AI eventually needs an explicit knowledge packet

When tactical AI is implemented, an NPC should not query the complete persistent player object. It should receive only an approved scouting packet derived from:
- direct observed battles;
- public replays;
- official results;
- legally received reports;
- current encounter-visible facts;
- explicit scenario disclosures.

This should become testable.

## PTU/Caelo mechanical boundary

This research does not create a Scouting skill, replay bonus, rematch modifier, prediction roll, hidden counterpick rule or automatic training benefit.

If a proposed scene asks for mechanical benefits from analysis, coaching, recalling a Move, changing a roster, learning a Feature, tutoring a Move or preparing an Item, the exact effect must be validated against the project's governing PTU/Caelo source set and the current AutoPTU implementation.

The narrative layer may always store that an actor watched a battle and formed a conclusion. It may not convert that fact into combat math without source support.

## Current engine relevance

AutoPTU-Java was inspected read-only during this pass.

Current head inspected:

`3177594f92df4c5a86023ba0cb5fbac3da195e4e`

The newest commit adds a parity-gated Intercept eligibility contract. It proves candidate guards for prepared Intercept/Weaponize/Sentinel-style eligibility, including status, trapped state, coaching and Loyalty checks. The implementation explicitly states that runtime status/coaching/controller truth comes from AutoPTU `BattleRuntimeState`; Minecraft/Cobblemon must not supply those values.

This strengthens the existing PARTIAL classification for complete movement/interception. It does not prove full interception execution, all reactions, tactical AI or Minecraft playback.

AutoPTU Python was also inspected read-only. Current head:

`95899537a72fb8c85330d7488c530316a8883884`

Its recent work concerns truthful Career retirement ownership summaries and temporary-loan accounting. No new tactical family is established by those changes.

## Canon status

No institution, replay technology, broadcast policy, analyst profession, rival practice, public-record rule or scouting mechanic in this scan is canon.

The only binding statements referenced here are existing project architecture and source-priority rules already present in the narrative repository.
