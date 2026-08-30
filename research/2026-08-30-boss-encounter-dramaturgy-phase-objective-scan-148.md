# Boss Encounter Dramaturgy, Phase Logic & Objective Persistence — Research Pass 148

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file creates Ouros canon.

Date: 2026-08-30

## Why this pass exists

Pass 16 established encounter implementation contracts, capability gates, full/reduced variants and a technical `phase boss` footprint. `mission-dungeon-grammar.md` already owns route structure and terminal set pieces. Those layers answer whether a mechanically ambitious encounter can run and where it sits in an adventure.

A different design problem remained under-specified: what makes a boss encounter narratively legible, memorable and persistent across scenes without hiding missing mechanics behind scripted prose.

This pass researches that missing layer. It focuses on readable escalation, objective change, openings, non-KO resolution, recurring antagonists or guardians, aftermath, fail-forward consequences and the boundary between a narrative beat and an engine-authoritative battle phase.

## Existing Ouros material inspected before writing

The repository tree was inspected recursively from `main` at `ca90128f2b339e22f08bc7f4256376f210e1f7ff`; the Git tree response was not truncated. Relevant existing owners were then checked directly.

`design/encounter-implementation-contracts.md` already owns implementation feasibility, capability dependencies and full/reduced encounter contracts. It should remain the authority for whether a runtime mechanic is available.

`design/mission-dungeon-grammar.md` already owns adventure routing, safe/danger/reward nodes and terminal set pieces. This pass must not create a second dungeon graph system.

`research/2026-08-18-encounter-contracts-boss-objectives-scan-16.md` already researched boss templates, raids, objective clocks and the danger of assuming that more turns or one representative mechanic means a boss system exists. Pass 148 therefore avoids repeating raid/barrier/timer research and concentrates on encounter dramaturgy.

## Pokémon Legends: Arceus — quelling as a different success grammar

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Walkthrough%3APok%C3%A9mon_Legends%3A_Arceus/Part_4
- https://bulbapedia.bulbagarden.net/wiki/Walkthrough%3APok%C3%A9mon_Legends%3A_Arceus/Part_7
- https://bulbapedia.bulbagarden.net/wiki/Walkthrough%3APok%C3%A9mon_Legends%3A_Arceus/Part_13

The frenzied Noble encounters are useful because ordinary Pokémon battle is not always the terminal objective. The player reads attack patterns, avoids pressure, creates or receives an opening and may use a normal Pokémon battle to create a better opportunity to continue the real calming objective. Later encounters increase arena pressure and alter the available safe space.

Reusable high-level lessons:

- boss success can be CALM, CONTAIN, INTERRUPT, ESCAPE or PROTECT rather than only KO;
- ordinary battle can be one tool inside a larger encounter instead of the sole narrative resolver;
- an opening should be readable before it is mechanically exploitable;
- escalation can change pressure and available space while preserving the same core objective;
- a later boss can test a grammar the player already learned instead of inventing an unrelated gimmick every time.

Ouros must not copy balms, frenzy gauges, specific attack sequences, named Nobles, plates or Hisui plot structure.

Implementation warning:

Real-time dodging, free-aim projectiles, moving area hazards and live arena transformation are not implied by PTU or by current AutoPTU-Java readiness. A reduced Ouros encounter must represent the same premise through separate world-state beats and ordinary verified battles unless exact lifecycle/hazard/reaction support is proven.

## Alola Totem encounters — boss identity can be relational

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Brooklet_Hill
- https://bulbapedia.bulbagarden.net/wiki/SOS_Battle
- https://bulbapedia.bulbagarden.net/wiki/Appendix%3ASun_and_Moon_walkthrough/Section_4

Totem encounters create identity through pre-battle conditions and ally pressure. Brooklet Hill in particular demonstrates a boss whose reinforcement behavior changes with battle state.

Reusable lessons:

- a memorable boss does not need only inflated durability;
- allies, arena context and a pre-established rule can make the encounter read differently from an ordinary wild battle;
- reinforcement pressure is most legible when the player understands why another actor can enter and what role it serves;
- phase-like escalation can be relational: new combatants, changed priority or protection demand rather than a literal transformation.

Ouros must not import Totem auras, SOS formulas, scripted HP thresholds or exact ally-call behavior unless PTU/AutoPTU contracts explicitly support the required mechanics.

## PTU campaign log — complexity and duration are encounter costs

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/xtwhxv

A public PTU campaign log describes a Gym fight that became sufficiently long and arduous that the group later retconned the repeated fight rather than play it again. The author notes that the party entered after training with Pokémon already worn down and that the encounter was taking a long time.

This is community experience, not a PTU rules source.

Reusable lessons:

- a boss encounter that is memorable in design can still fail at the table through excessive duration;
- replaying an unchanged long boss after defeat is especially costly;
- persistence should allow the fiction to remember a failed attempt and change the next approach instead of forcing an identical reset;
- encounter authors should budget active combatants, phase count and repeated turns as pacing costs.

## PTU campaign log — staged roster pressure can create identity

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/njlkdr

Another public PTU campaign log describes a Fire Gym structured as three separate 4-on-4 battles, with restrictions on reusing selected Pokémon across stages. The important reusable pattern is not the exact Gym or roster numbers. It is that a major challenge can obtain identity through linked discrete battles and persistent resource decisions between them.

Reusable lessons:

- a multi-stage boss or institution challenge does not require one continuous runtime battle;
- separate BattleSpecs with explicit inter-scene state can be safer and easier to reason about than a giant scripted combat;
- decisions from an earlier stage can shape a later one without requiring dynamic terrain or bespoke boss turns;
- this pattern is especially useful while full lifecycle, status carryover and adapter playback remain incomplete.

## Contemporary PTU community — boss versions are commonly treated as bespoke table contracts

Source:
- https://startplaying.games/adventure/cmt7oxvn6002gl6044hl8ppx5

A current public PTU campaign advertisement describes Gym challenges where individual fights lead into a group fight against a boss version of the leader's ace, alongside explicit house rules for weather and boss immunities.

This is community homebrew, not PTU canon and not evidence that those mechanics exist in AutoPTU.

Reusable lesson:

Tables often make boss status explicit through local contracts. Ouros should be stricter: every bespoke boss rule must have a named authority, implementation dependency and fallback. “Boss” cannot silently grant immunities, extra turns, weather, damage reduction or action exceptions.

## General encounter-design inference

Across these sources, the strongest reusable pattern is a sequence of readable promises rather than a pile of exceptions.

A boss should communicate what kind of problem it is before asking the player to solve the hardest form of that problem. The dungeon, prior scene, NPC behavior, damaged environment, recurring move pattern or earlier confrontation can teach a safe version of the encounter's central pressure.

A phase transition is valuable only when it changes the player's decision. More HP, more damage or a different animation without a changed decision does not need to be represented as a narrative phase.

A defeat or retreat should leave a world fact. Repeating the identical encounter from an untouched checkpoint weakens Ouros's persistent-world premise.

## PTU/Caelo boundary

No source inspected in this pass establishes a universal PTU boss subsystem that grants extra actions, phase thresholds, immunity packages, stagger gauges, scripted reinforcements, destructible objectives, dynamic arenas or non-KO victory procedures.

Pass 16 already records PTU development commentary warning that multi-turn boss templates interact strongly with status timing and round semantics. That warning remains controlling.

Caelo/Ouros may author a narrative objective such as calm, rescue, protect, contain, interrupt or force withdrawal. The tactical engine may establish only the combat facts it is explicitly contracted to resolve. Ouros converts those facts into a world-state consequence through the owning narrative/world system.

## Research conclusion

The new layer should define boss-scene dramaturgy, not new combat rules.

The safest reusable grammar is:

1. establish the threat and what matters;
2. telegraph the boss's characteristic pressure;
3. let the player commit to an approach;
4. create an observable opening or changed priority;
5. escalate only when the decision space changes;
6. resolve through an explicit objective contract;
7. persist the aftermath, including failure, retreat or ambiguity.

That grammar can support a future rich runtime version while also compiling into multiple ordinary BattleSpecs today. The reduction is structural rather than cosmetic: missing hazards, reactions, moving platforms or tactical AI are removed from engine authority, while the narrative premise survives in Ouros state before and after each battle.
