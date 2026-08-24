# Pokémon training, practice and coaching scan — pass 144

Status: research/provenance only. Nothing in this file is established Ouros canon.

Date: 2026-08-24

## Why this pass exists

The repository already has strong authorities for formal education, Trainer-to-Trainer mentorship, Pokémon agency/welfare, battle institutions, social learning, working Pokémon and tactical battle resolution.

The current gap is narrower and more central to day-to-day Trainer life: repeated practical training between a Trainer and an individual Pokémon.

The missing questions include:

- what was the training objective;
- what cue or setup was used;
- what the Pokémon actually attempted;
- what feedback or adjustment followed;
- whether the exercise was repeated under the same or different conditions;
- whether a successful practice result generalized outside the original setup;
- whether the Pokémon voluntarily participated or disengaged;
- whether the session was stopped because of care, fatigue, frustration, injury, schedule or environment;
- whether the practice produced any authoritative PTU progression at all.

The central research goal is to support training scenes that matter narratively without inventing levels, Tutor Moves, Poke Edges, Skill increases, stats, Loyalty, combat bonuses or obedience mechanics.

## Internal repository review before research

The branch inventory was reviewed before choosing this gap.

Relevant existing boundaries:

- `design/social-bonds-mentorship-clubs-layer.md` owns mentorship relationships and competency opportunities but explicitly refuses to grant PTU progression from narrative practice.
- `design/education-academies-field-practice-layer.md` owns formal instruction, curricula, supervised practice and institutional assessment.
- `design/care-recovery-welfare-layer.md` owns welfare observations, recovery and care boundaries.
- `design/pokemon-social-learning-behavioral-traditions-layer.md` owns transmission of behavior between Pokémon populations/individuals when there is evidence of social learning.
- `design/pokemon-cognition-problem-solving-tool-use-layer.md` owns individual problem solving and object manipulation.
- `design/battle-institutions-challenge-circuits-layer.md` owns formal challenge history and battle contracts.
- `design/working-pokemon-institutional-roles-layer.md` owns recurring task assignments in institutions.
- AutoPTU/PTU data remains authority for actual mechanical progression.

No existing layer owns a persistent Trainer-Pokémon practice record with goals, cues, attempts, feedback, progression claims and transfer/generalization evidence.

## Source 1 — Pokémon Horizons: Special Training Time!

Source: Pokémon.com animation page, `Special Training Time!`, Pokémon Horizons season 1 episode 17.

URL: https://www.pokemon.com/us/animation/horizons/1/special-training-time

Reusable structure:

Roy does not begin with an abstract stat problem. He observes that Fuecoco and Wattrel are not coordinating well, watches another pair battle, creates a training setup intended to force cooperation, sees partial success and continued failure, then continues training.

Design lessons for Ouros:

1. Training can begin from a specific observed problem rather than a generic desire to become stronger.
2. A sparring partner can be used as a controlled training environment without making the spar an official match.
3. A session can produce mixed evidence: a new behavior may appear while the larger objective remains unresolved.
4. Team coordination should not become a binary unlocked flag from one successful drill.
5. Training can generate future practice goals even when the immediate exercise ends in defeat.

Do not copy the episode's characters, battle sequence or exact training method.

## Source 2 — Kabu's Battle Training!

Source: Pokémon.com animation page, `Kabu's Battle Training!`, Pokémon Horizons season 1 episode 20.

URL: https://www.pokemon.com/us/animation/horizons/1/kabus-battle-training

Reusable structure:

An experienced Gym Leader first runs an exercise, then places the learners into a battle context that tests what they have been working on. Several learners participate at different experience levels.

Design lessons:

- demonstration, drill and test can be different events;
- the same coach can challenge different learners for different reasons;
- a training session can include peer observation;
- an institution can host practice without every session becoming a Badge challenge;
- a learner's result can be useful evidence even if the coach is overwhelmingly stronger.

This fits Ouros especially well for clubs, schools, Gyms and recurring coaches.

## Source 3 — Rematch at the Nacrene Gym!

Source: Pokémon.com animation page, `Rematch at the Nacrene Gym!`.

URL: https://www.pokemon.com/us/animation/seasons/14/episode-16-rematch-at-the-nacrene-gym

Reusable structure:

A previous loss identifies concrete problems. Ash uses a Battle Club and specialist equipment for focused preparation before attempting the rematch again.

Design lessons:

- battle transcript/history can create a practice objective;
- training facilities can provide controlled repetitions or equipment that the overworld normally cannot;
- practice should record what weakness was being addressed;
- the later rematch is the actual test of transfer, not the drill itself;
- repeated preparation can become part of a local institution's history.

Ouros should avoid copying the episode's mechanical claim that training literally raises power/speed unless PTU progression independently authorizes a change.

## Source 4 — Battling on Thin Ice!

Source: Pokémon.com animation page, `Battling on Thin Ice!`.

URL: https://www.pokemon.com/us/animation/seasons/17/episode-6-battling-on-thin-ice

Reusable structure:

The Trainer studies two problems from a previous Gym battle and constructs simulations of those problems before the rematch. One machine fails, so the group substitutes a Pokémon-generated analogue for the exercise.

Design lessons:

- practice can use simulation rather than replaying the exact opponent;
- the fidelity of a training setup should be recorded;
- a failed training device can change the method without invalidating the objective;
- an improvised substitute can be useful while remaining mechanically different from the original threat;
- a rehearsal environment is not automatically a tactical Terrain or hazard.

This source strongly supports a `training_setup` object with `target_problem`, `simulation_method` and `fidelity_claim` instead of a generic `training_complete=true`.

## Source 5 — Facing Fear with Eyes Wide Open!

Source: Pokémon.com animation page, `Facing Fear with Eyes Wide Open!`.

URL: https://www.pokemon.com/us/animation/seasons/14/episode-32-facing-fear-with-eyes-wide-open

Reusable structure:

Ash works with Oshawott on a specific difficulty: opening its eyes underwater. The practice becomes relevant later in an uncontrolled situation.

Design lessons:

- the useful training state is a narrowly defined behavior under conditions;
- success in a controlled session and success in a field situation are different observations;
- the same objective can matter for exploration and battle without becoming a universal stat;
- field generalization may occur under pressure, but the world should record what actually happened rather than assume permanent mastery.

Ouros must not infer fear diagnoses or impose private emotional states from a single behavior.

## Source 6 — Short and to the Punch!

Source: Pokémon.com animation page, `Short and to the Punch!`.

URL: https://www.pokemon.com/us/animation/seasons/13/episode-2-short-and-to-the-punch

Reusable structure:

A specialist demonstrates a technique. Ash and Buizel fail to reproduce it immediately, practice with a moving target, then later use the learned technique in a battle.

Design lessons:

- demonstrations do not equal acquisition;
- drills can isolate one component of a larger Move or tactic;
- repeated failed attempts are valid history rather than filler;
- transfer should be evidenced by later use;
- a learned Move remains a PTU mechanical fact and must only be written by the rules authority.

The narrative layer may record `practice_target: Ice Punch` only as a practice target. It may not add Ice Punch to the move list.

## Source 7 — A Call for Brotherly Love!

Source: Pokémon.com animation page, `A Call for Brotherly Love!`.

URL: https://www.pokemon.com/us/animation/seasons/15/episode-10-a-call-for-brotherly-love

Reusable structure:

A losing streak is interpreted as a training problem. Another Trainer evaluates the pair and suggests a more balanced option. The training proposal reflects both team history and a concrete tactical gap.

Design lessons:

- a losing streak should not produce an automatic diagnosis;
- coaching advice is a claim, not truth;
- compatibility, temperament or frustration should not be system-inferred unless explicitly observed/authored;
- practice plans can be recommendations that the Trainer accepts, modifies or rejects;
- learning a Move is still gated by PTU mechanics.

## Source 8 — Top-Down Training

Source: Pokémon.com animation page, `Top-Down Training`.

URL: https://www.pokemon.com/us/animation/seasons/10/episode-40-top-down-training

Reusable structure:

The episode contrasts harsh performance-first training with care and a broader Trainer-Pokémon relationship.

Design lesson for Ouros:

Training effectiveness and welfare should remain separate dimensions. A session can produce performance evidence and still trigger a welfare concern. Conversely, a welfare-focused session may intentionally produce no combat progression.

The generator should never equate intensity, harshness or repeated failure with superior progression.

## Source 9 — Pokémon Champions training state

Source: Pokémon.com, `Pokémon Champions Is Coming to Nintendo Switch in April 2026`, published 2026.

URL: https://www.pokemon.com/us/pokemon-news/pokemon-champions-is-coming-to-nintendo-switch-in-april-2026

Reusable structure:

The official game treats training results as state that can persist when a visiting Pokémon leaves and later returns to the same game context, while move availability can depend on the destination ruleset.

Design lessons:

- training/progression state can have provenance and ruleset context;
- a Pokémon's persistent identity should survive transfers between systems;
- not every learned/available action is legal in every rules environment;
- the narrative layer should reference authoritative mechanical state instead of duplicating it.

Do not import Pokémon Champions' training system, values or move rules into PTU.

## Source 10 — public PTU campaign log #24

Source: public r/PokemonTabletop campaign log, August 2022.

URL: https://www.reddit.com/r/PokemonTabletop/comments/wudfhz

Reusable structure:

After losing a Gym battle, the party seeks a battlefield specifically to train. The trip to the practice site also creates unrelated ecology, capture and roleplay content before the actual sparring session.

Design lessons:

- a training destination can be part of the travel graph;
- practice does not need to consume an entire session;
- field travel can interrupt or reshape the training plan;
- party members may use the same training opportunity differently;
- training can coexist with ecological consequences that remain independent of progression.

The log's characters, Pokémon, captures and plot are not reused.

## Source 11 — public PTU campaign log #25

Source: public r/PokemonTabletop campaign log, October 2022.

URL: https://www.reddit.com/r/PokemonTabletop/comments/xtwhxv

Reusable structure:

The players describe training immediately before a long battle and note that the Pokémon were already worn down. The GM later skips a repeated fight because replaying it did not sound fun.

Design lessons:

- practice can interact with resource/readiness state when the rules actually support it;
- pacing matters: repeating the same mechanical encounter can be worse than resolving the learning goal another way;
- training records can preserve what was practiced even if a later rematch is compressed;
- narrative training must not invent fatigue/HP loss if PTU did not actually produce it.

## Source 12 — AZA behavioral husbandry

Source: Association of Zoos & Aquariums, `Behavioral Husbandry`.

URL: https://www.aza.org/connect-stories/stories/behavioral-husbandry-wellbeing-collaboration-zoos-aquariums

Useful external design principle:

Real animal-care programs can train voluntary participation in medical procedures over months using incremental familiarization and positive reinforcement.

Ouros adaptation:

- training may take multiple sessions;
- each session can have a small criterion;
- voluntary participation can be recorded separately from task performance;
- care training can be useful even when it has no combat benefit;
- different individuals can require different timelines without assigning a hidden intelligence score.

Do not import real zoological procedures or treat Pokémon as real animals. The source is used only for training-process architecture.

## Source 13 — shaping and gradual approximation

Source: Merck Veterinary Manual, `Treatment of Behavior Problems in Animals`.

URL: https://www.merckvetmanual.com/behavior/behavioral-medicine-introduction/treatment-of-behavior-problems-in-animals

Useful design principle:

Shaping builds a behavior through successive approximations instead of requiring the finished behavior immediately.

Ouros adaptation:

A practice objective can have authored or dynamically chosen intermediate criteria. Examples:

- remain at starting marker;
- orient toward cue;
- perform first step of a sequence;
- hold position for longer;
- execute the full sequence;
- perform it under a changed setup.

These are observational milestones only. They never grant PTU mechanics by themselves.

## Source 14 — voluntary participation and choice

Source: Animal Welfare Institute summary of Brando & Norman 2023, handling and training of wild animals.

URL: https://awionline.org/lab-animal-search/brando-s-norman-m-2023-handling-and-training-wild-animals-evidence-and-ethics

Useful design principle:

Training programs can preserve choice and control, especially around husbandry/care participation.

Ouros adaptation:

A training session should support outcomes such as:

- participates;
- participates partially;
- disengages;
- refuses one step;
- leaves and returns;
- completes a different behavior;
- session ends because the Trainer stops it.

None of those outcomes should automatically change Loyalty.

## Source 15 — trainer-led sessions versus self-directed behavior

Source: Association of Zoos & Aquariums, `Freeing Up the Operant`.

URL: https://www.aza.org/connect-stories/stories/freeing-up-the-operant-supporting-animals-core-interests

Useful design principle:

Trainer-led discrete trials represent only one part of an individual's behavioral life. Self-directed behavior outside the session remains important.

Ouros adaptation:

The training layer must not absorb all Pokémon behavior into Trainer commands. A Pokémon may practice, play, explore, rest, problem-solve or interact socially outside formal sessions. Training records only the session and its observed transfer.

## PTU project-source cross-check

The current AutoPTU repository contains PTU-derived Pokémon Edge data. Relevant explicit mechanical examples include:

- `Accuracy Training`: permanently lowers the AC of one qualifying Move under its prerequisites;
- `Capability Training`: increases a specific Power or Jump capability under its prerequisites;
- `Advanced Mobility`: increases a selected Movement Capability under its prerequisites;
- `Skill Improvement`: raises a qualifying Pokémon Skill;
- `Underdog's Lessons`: grants a qualifying Move under its exact prerequisites;
- `Expand Horizons`: grants Tutor Points when the governing Mentor Feature applies.

Project evidence: `files/Copia de Fancy PTU 1.05 Sheet - Version Hisui - Poke Edges.csv` in AutoPTU.

This is an important hard boundary.

Narrative repetition, drills, coaching, equipment, praise, failure, sparring or time spent training do not reproduce these Poke Edge effects.

If a training event results in one of these mechanical changes, the narrative layer must link to the authoritative PTU transaction that actually paid costs, satisfied prerequisites and changed character state.

The training layer may then record why the characters describe that change as significant.

## Current engine evidence relevant to training encounters

AutoPTU-Java head inspected during this pass: `359c31638448f23b6da230679988e42f21777abc` — `Port Perception pre-damage reaction (#172)`.

The latest slice ports one specific Perception pre-damage reaction contract using authoritative temporary effects, optional out-of-turn decisions, movement to a safe tile and hit cancellation.

This is meaningful reaction/movement evidence for one mechanic.

It does not demonstrate:

- generic reactions;
- generic dodge drills;
- generic training transfer;
- sparring AI with learning objectives;
- Trainer-Pokémon cue systems;
- Push/Pull execution;
- interception;
- objective-aware AI;
- training equipment as hazards;
- progression from practice.

The AutoPTU-Java README still marks full combat state, full damage, status controller, terrain, hazards, forced movement, reactions, registries, full transcript parity, AI policy and Minecraft/Cobblemon integration as incomplete.

AutoPTU Python head inspected: `0d56ea7b5a2b99a96f7ac4ca40b405e0ffbf83b8`. Its newest visible work is Career persistence sanitization and does not change the tactical capability map.

## Reusable Ouros principles derived from the scan

1. Training begins from an objective, not a generic XP action.
2. Practice evidence and mechanical progression remain separate.
3. A demonstration is not acquisition.
4. Success in one setup is not proof of generalization.
5. A later battle, field task or care procedure can become transfer evidence.
6. Failed attempts remain useful Chronicle history.
7. Coaches can disagree about what the problem is.
8. Training equipment can fail or be replaced without creating fake mechanics.
9. Voluntary participation and session performance are distinct.
10. A Pokémon can disengage without losing Loyalty.
11. Training can be welfare-positive, welfare-neutral or raise a welfare concern; intensity alone proves nothing.
12. A drill should not damage HP or cause Fatigue unless authoritative PTU execution actually did so.
13. Trainer-led practice should not overwrite self-directed behavior.
14. The same objective can have several methods.
15. A long-running practice record can become character history even if no stat ever changes.
16. Routine practice can compress into a short world event.
17. A meaningful session should surface a decision, discovery, relationship fact, mechanical transaction or later callback.
18. The Minecraft adapter must render practice state; it must not decide PTU progression.

## High-value narrative structures

### Failure -> diagnosis -> focused practice -> retest

Useful for rematches and recurring rivals.

The key is that diagnosis can be wrong or incomplete.

### Demonstration -> imitation attempt -> adaptation

Useful when a coach shows a technique but the learner's body plan, Move set or style requires a different solution.

### Controlled drill -> field transfer

Useful for caves, water, crowds, weather, rescue work and institutional duties.

The transfer event should be recorded independently.

### Pair-coordination practice

Useful for multi-Pokémon teams, Doubles, rescue teams or work groups.

Do not infer shared initiative, Pack Mon or tactical coordination bonuses.

### Cooperative-care practice

Useful for clinic, sanctuary, transport, equipment fitting or examinations.

The goal can be voluntary participation rather than combat improvement.

### Practice culture

Gyms, clubs and towns may develop recurring drills, equipment, coaching traditions or philosophies.

These are cultural practices until a PTU rule independently grants a mechanical effect.

## Sources intentionally not converted into rules

External animal-training literature is used only to structure observations, gradual criteria, voluntary participation, generalization and welfare review.

Pokémon animation is used as narrative precedent only.

Public PTU logs are used as campaign-design evidence, not rules authority.

The only mechanical claims in this scan come from project PTU data or current engine evidence.

## Remaining research questions

- Which Caelo sources modify Mentor, Poke Edges, tutoring, training time or Pokémon progression?
- Does Caelo define downtime training, practice facilities or custom training restrictions?
- Which Trainer Features in the final ruleset can legally grant Tutor Points, Moves, Poke Edges or Skill changes?
- How much training history should be visible to other players in multiplayer?
- Should Ouros persist individual cues/signals as authored relationship history or keep them abstract?
- How should practice histories survive ownership/custody changes without implying that a new Trainer inherits command fluency automatically?
- Which practice observations are private welfare records versus public competitive information?

The complete Caelo corpus was not recoverable through the available repository tools during this run. Super PTU Online Helper was not exposed as an invocable capability. No output was invented from either source.