# Rivalry, Recurring Peers & Competitive Continuity — Research Scan 59

Status: research/provenance only. Nothing in this file is Ouros canon.
Date: 2026-08-26

## Research question

How can Ouros support recurring peers and rivals who grow, change goals, remember prior encounters and remain relevant outside formal boss battles, without reducing rivalry to one affection meter or forcing every recurring opponent into enemy status?

This pass intentionally extends rather than replaces:
- `design/social-bonds-mentorship-clubs-layer.md`
- `design/battle-institutions-challenge-circuits-layer.md`
- `design/antagonist-agency-defection-escalation-layer.md`
- `design/public-memory-event-legacy-layer.md`
- `design/world-agency-layer.md`

The existing social layer already allows rivalry as one relationship shape. The gap is operational continuity: when a recurring competitive peer appears, what they know, why they are there, what changed since last contact, what competition domain is active, and how an authoritative result feeds later scenes.

## Sources reviewed

### Pokémon Animation’s Ten Greatest Rivalries
Source: Pokémon.com, 13 September 2023
https://www.pokemon.com/us/news/pokemon-animations-ten-greatest-rivalries

The official retrospective explicitly frames Pokémon rivalries as ranging from friendly competition to hostile opposition. Several examples also change function over time: some rivals teach, train together, help prepare for later challenges, cooperate during crises or continue to matter after a decisive competitive result.

Reusable structures:
- rivalry is a relationship mode, not a synonym for enemy;
- competitive tension can coexist with assistance, mentorship, respect or ideological disagreement;
- a rival’s function may change between meetings without erasing prior competitive history;
- the same recurring person can test different dimensions of a protagonist over time;
- later cooperation has more weight when it preserves, rather than deletes, earlier friction.

Do not copy named character arcs, dialogue, team compositions or episode sequences.

### Rival archetype across the core series
Source: Bulbapedia — Rival
https://bulbapedia.bulbagarden.net/wiki/Rival

The recurring game pattern is structurally useful: a peer often appears early, reappears at intervals, travels independently, carries a progressively changing team and creates repeated comparison points across the journey.

Reusable structures:
- introduce a peer before the player’s identity is fully established;
- let the peer operate on an independent route rather than wait in fixed boss rooms;
- use recurring meetings as longitudinal snapshots of both actors’ development;
- allow team or approach changes to come from visible history, not hidden scaling;
- not every meeting needs to be mandatory or combat-centered.

This source is used for broad franchise structure only.

### Pokémon Scarlet/Violet retrospective — Nemona as a recurring battling peer
Source: Pokémon.com, 22 September 2025
https://www.pokemon.com/uk/pokemon-news/reminisce-on-pokemon-scarlet-and-pokemon-violet-with-the-pokemon-tcg

The official retrospective identifies Nemona as the player’s battling peer from the beginning and ties early rivalry to shared physical places, including the first battle court and academy context.

Reusable structures:
- rivalry can be anchored to ordinary recurring locations rather than special arenas only;
- an experienced peer can deliberately meet the player at their current stage without implying hidden stat normalization;
- shared institutions create plausible repeat contact;
- a rival can remain socially legible even when not directly obstructing progress.

### Pokémon Legends: Arceus — peer competition inside shared work
Sources:
https://legends.arceus.pokemon.com/en-ca/story/
https://bulbapedia.bulbagarden.net/wiki/Rei_%28game%29

Akari/Rei is framed officially as a fellow Survey Corps member close to the player’s age. Public battle records show that at least one early battle can be lost without blocking story progression.

Reusable structures:
- peers can compete while sharing a workplace, expedition mandate or research goal;
- losing a peer battle does not always need to stop the story;
- rivalry can emerge from repeated comparison inside ordinary work rather than from a dedicated League track;
- cooperation during larger problems can continue regardless of prior battle result.

Do not copy the Survey Corps, character identities or specific battle teams into Ouros.

### Pokémon Reborn — relationship-sensitive recurring characters
Source: Pokémon Reborn Wiki — Relationship Points
https://pokemon-reborn.fandom.com/wiki/Relationship_Points

This fan game tracks hidden relationship state and allows some later battles, events and cutscenes to vary based on prior choices. The same source warns, implicitly through its design, against equating one number with a complete relationship.

Reusable structures:
- prior choices can change later scene availability or framing;
- relationship consequences can persist into postgame or later arcs;
- not every interaction needs to change relationship state;
- rivalry state should remain multidimensional and event-backed rather than become a single score.

Ouros should not import Reborn’s point values, thresholds, characters, scenes or branching routes.

### Public PTU campaign log — recurring player-vs-peer competition inside a tournament
Source: r/PokemonTabletop campaign log #14
https://www.reddit.com/r/PokemonTabletop/comments/o98jgt

The session report includes recurring trainers who meet again inside a competitive event, with player choices such as withdrawing to protect a Pokémon and multiple peer-vs-peer outcomes contributing to the event rather than existing only as isolated duels.

Reusable structures:
- a tournament can create several intersecting rivalries at once;
- withdrawal can be a meaningful authored choice without treating the participant as narratively defeated forever;
- recurring peers can return through event structure rather than coincidence;
- competitive history can accumulate through several formats and contexts.

Only the abstract structure is retained. No campaign characters, dialogue or event rules are copied.

### Pokémon Horizons — rival/mentor assistance around a failed challenge
Sources:
https://www.pokemon.com/us/animation/horizons/2/a-new-song-for-fuecoco
https://www.pokemon.com/us/news/pokemon-horizons-season-2-the-search-for-laqua-part-2-recap-quiz

Official episode summaries show a stronger peer helping another Trainer prepare after a failed challenge and before a rematch.

Reusable structures:
- a rival can become a preparation partner without ending the rivalry;
- failure can create a concrete training or reflection hook rather than a generic power-up;
- a rematch feels stronger when something observable changed between attempts;
- support does not require the two Trainers to become identical in method or goal.

## Cross-check against existing Ouros research

Pass 09 already established that rivalry belongs inside a multidimensional social model and noted that Caelo has a Rivalry framework. Pass 15 already established formal battle records, rematches, scouting boundaries and challenge contracts. Pass 21 already established persistent opposition and adversary replanning.

This pass therefore does not create:
- a universal relationship score;
- a second formal battle-record system;
- a second antagonist planner;
- an automatic friendship/enmity label;
- hidden adaptive stat scaling.

The new design target is a continuity coordinator that links those existing records across repeated peer encounters.

## PTU / Caelo mechanical boundary

The project’s existing source review states that Caelo defines a Rivalry framework with prerequisites. This pass does not import those exact mechanics because the intended Caelo carry-over remains undecided.

A live code search in `Teffa14/AutoPTU` for `Rivalry` found a PTR2e ability file and unrelated references, but no evidence that the Caelo Rivalry framework is currently an authoritative AutoPTU runtime mechanic. PTR2e material is not a governing source for this project.

Therefore:
- rivalry is narrative state only in this pass;
- no combat modifier, XP modifier, Loyalty change, Feature, Edge, perk or reward is granted by rivalry state;
- any future mechanical Rivalry effect must be validated against the supplied PTU/Caelo source set and then against AutoPTU implementation evidence.

## Design conclusions

1. Recurring rivals need independent goals and schedules. They should not appear merely because the player crossed a checkpoint.
2. Competitive history should point to authoritative results and observed events, not invented summaries.
3. A rival should remember only information they plausibly observed, were told or could access publicly.
4. Rivalry can change domain. Two Trainers may battle, cooperate on research and later compete for an institutional opportunity without collapsing all of those interactions into one label.
5. Losing to a rival need not block story progression unless a reviewed challenge contract requires it.
6. Rematches should change because participants, goals, public knowledge, venue state or legal rosters changed.
7. A recurring peer can temporarily become ally, mentor, teammate, witness or opposing stakeholder while retaining competitive history.
8. Rival arcs should permit divergence. A peer can change career, leave a circuit, become unavailable, reject competition or pursue another goal.
9. Public attention and private rivalry state must remain separate.
10. Multiple rivals should be able to interact with each other, creating a peer network rather than a player-centered queue of boss fights.

## Copyright / provenance boundary

Only high-level structures, publicly described mechanics and campaign-design lessons are retained. No protected dialogue, distinctive plot sequence, character identity, team composition or fan-game route is copied into Ouros.

## Open research gaps

- Which Caelo Rivalry rules, if any, should become Ouros mechanics?
- Does the intended PTU/Caelo ruleset distinguish formal Rival mechanically from ordinary recurring opponent?
- Should rivalry state ever be visible numerically to players, or only through records and callbacks?
- What privacy rules govern a rival’s knowledge of public battle footage, team reveals and private training?
- How often can recurring peers appear before continuity becomes repetition?
- Should supporting rivals resolve off-screen battles through authored records, a future simulation policy or only externally supplied authoritative results?
