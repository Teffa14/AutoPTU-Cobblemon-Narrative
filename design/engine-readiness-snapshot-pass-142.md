# Engine Readiness Snapshot — Pass 142

Status: IMPLEMENTATION EVIDENCE SNAPSHOT. Not canon.
Date: 2026-08-23

## Purpose

This snapshot records live AutoPTU-Java and AutoPTU evidence relevant to Pass 142 oral-history, interview and witness-memory concepts. Both engine repositories remain read-only for this task.

A representative implemented mechanic never promotes an entire permanent capability family.

## Inspected heads

AutoPTU-Java:

`4f16e07862008b8fb00ee405a9cbc160ae8fbcec`

Latest inspected commit:

`Execute authoritative multi-target area moves (#170)`

The latest Java slice executes area/multi-target Moves once per declaration while deriving authoritative area anchors/targets and allowing the supported pre-damage reaction path to interact with that execution. This strengthens targeting, action ownership, Move execution and reaction ordering for the covered contract.

It does not create interview state, witness memory, social truth detection, testimony, civilian evacuation policy or dialogue AI.

AutoPTU Python:

`0b9da120608343e286e93fa38daa8ecaaf4b5893`

Latest inspected commit:

`Career: fail over when browser bundle is missing (#80)`

This is Career browser/deployment resilience and does not alter the tactical capability map.

## Repository-level Java boundary

The current AutoPTU-Java README still explicitly leaves unfinished:

- complete combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- complete status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Recent authoritative multi-target and reaction work does not override those blockers.

## Pass 142 world-state boundary

The following belongs outside AutoPTU:

- interview identity;
- narrator/interviewer identity;
- recording provenance;
- transcript/translation revisions;
- interview permissions and embargoes;
- recollection claims;
- narrator certainty as expressed;
- memory-access states such as PARTIAL or DOES_NOT_RECALL;
- source dependency between retellings;
- corroboration assessments;
- oral-tradition variants;
- archival access state;
- witness-route reconstruction history;
- public/private release decisions.

AutoPTU becomes authoritative only when a distinct battle opens.

## Permanent capability map

### targeting/footprints/range/LoS — VERIFIED

Java has parity-backed range, area, footprints, tile anchors and LoS. The new area-move slice strengthens authoritative target derivation.

This does not model conversational attention, microphone range, interview-room acoustics, who heard a statement or whether a witness could visually perceive an old event.

### base movement legality — VERIFIED

Ordinary Shift/Jump legality remains verified for the ported scope.

This can move combatants inside a frozen arena. It does not model a witness walkthrough, civilian evacuation or archivists carrying equipment as narrative objectives.

### complete movement including push/pull/knockback/interception/forced movement — BLOCKING

Narrow reaction movement and Push/Pull instruction contracts exist, but complete forced/interception movement remains unfinished according to the README.

Pass 142 FULL evacuation/walkthrough scenarios depend on this family when noncombatants must cross threatened space or actors can be intercepted.

### core calculations — VERIFIED

Core stat/type/damage-table primitives remain verified.

Memory confidence, statement consistency, age, emotion, interview skill or archival status must never modify combat stats without exact PTU rules.

### action economy/initiative — VERIFIED

Action budgets and initiative are verified for the ported scope. The new multi-target area-move contract further protects once-per-declaration cost ownership.

Answering a question, pausing an interview, making a correction or granting archive permission is not automatically a combat action.

### full turn/round lifecycle — PARTIAL

Round flow, selected temporary/delayed effects and selected reaction paths have parity-backed slices. Full lifecycle remains unfinished.

### full stateful damage pipeline — PARTIAL

Area execution and pre-damage reaction ordering continue to improve the pipeline, but the README still marks full damage incomplete.

Interview equipment, falling shelves, panicked crowds or broken recorders cannot create custom damage from narrative description.

### status lifecycle — PARTIAL

Selected application, prevention, stacking, suppression and timing behavior exists.

A narrator being confused about a date is not mechanically Confused. Memory loss is not a Status. Stress, hesitation, silence or emotional speech do not become Flinched, Suppressed, Enraged or other Status conditions.

### terrain/weather/hazards/zones/reactions — BLOCKING

Reaction support has concrete slices, but the permanent combined family remains incomplete.

An interview room, archive stacks, crowd barrier, rain during a walkthrough or dark corridor does not become tactical Terrain/Hazard/Zone without an exact validated rule.

### move-specific behavior — PARTIAL

Move execution coverage is growing, including authoritative area/multi-target execution.

Any Move used during a Pass 142 battle still depends on exact parity for its effects.

### abilities — PARTIAL

Selected Ability families have parity-backed behavior.

No Ability should be inferred to detect lies, restore memory, verify testimony, translate speech or identify historical truth unless an exact rule explicitly does so.

### items — PARTIAL

Item coverage remains incomplete.

Recorders, notebooks, microphones, archival boxes, tapes and ordinary interview equipment remain narrative objects unless mapped to validated PTU Items.

### Trainer Features/perks — PARTIAL

Generic Trainer Feature infrastructure and selected effects exist.

Charm, Guile, Command, Intuition, Researcher, Chronicler or Psychic-themed Features must not be promoted into generic interview, lie-detection or memory mechanics without exact source text and parity-backed implementation.

### AI legal-action infrastructure — VERIFIED

The legal BattleChoice contract is verified for the ported scope.

It does not reason about testimony, source dependency, narrator permission, evacuation priorities or preserving an interview recording.

### AI tactical policy — BLOCKING

No complete policy exists for Pass 142 objectives such as:

- `EVACUATE_NARRATOR`;
- `PROTECT_ARCHIVIST`;
- `CLEAR_ROUTE`;
- `REACH_INTERVIEW_EXIT`;
- `PROTECT_RECORDING_EQUIPMENT`;
- `ESCORT_WITNESS`;
- `WITHDRAW`;
- `REACH_OBSERVATION_POINT`.

A legal-action list is not objective-aware interview or escort behavior.

### Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

No parity-safe adapter exists.

Minecraft must not infer authoritative testimony state from:

- chat bubbles;
- NPC proximity;
- subtitles;
- voice chat;
- a recorder item;
- a book-and-quill;
- player-written signs;
- an NPC repeating the same line;
- two NPCs standing together;
- a successful battle;
- a client-side transcript.

The adapter must not decide whether a narrator is truthful, accurate, consenting, corroborated or legally/institutionally authoritative.

## Pass 142 encounter dependencies

### Evacuation During Community History Recording — FULL

Requires:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL if exact supported effects are invoked;
- terrain/weather/hazards/zones/reactions — BLOCKING only if a validated environmental/reaction mechanic becomes tactical;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED:
Pause the interview at the last completed claim boundary. Move narrators, archivists and equipment to safety in world state. Open a static battle only if a separate confrontation remains. Resume or reschedule afterward. Battle outcome does not complete or validate testimony.

### Witness Route Reconstruction — FULL

Primary blockers:
- complete movement for a witness/escort moving between observation points;
- AI tactical policy for `ESCORT_WITNESS`, `REACH_OBSERVATION_POINT`, `WITHDRAW`, `CLEAR_ROUTE`;
- adapter/playback;
- environmental family only if an exact validated hazard becomes tactical.

REDUCED:
Resolve the route as overworld navigation. Create versioned claims at fixed locations. Freeze any independent battle into a static arena and resume the walkthrough afterward.

### Archive Interview Handoff

Non-combat by design.

Archives, Research Ethics, Languages, Identity and Pass 142 state govern the handoff. No battle capability is required.

## Key non-inferences

- confidence != accuracy;
- inconsistency != lie;
- age != unreliable memory;
- emotion != falsehood;
- calmness != truth;
- matching stories != independent corroboration;
- interview != permission to publish;
- transcript != original recording;
- translation != original wording;
- oral tradition != literal world truth;
- Telepathy reaction support != mind-reading system;
- battle LoS != historical witness visibility;
- battle victory != reliable testimony.

## Unresolved mechanics/canon

- exact PTU/Caelo treatment of Charm, Guile, Command, Intuition, Perception and any interrogation/social-information mechanics;
- whether any Psychic/Telepathy Feature permits propositional communication or memory access in the project's authoritative rules;
- which Ouros institutions can take witness statements versus oral histories;
- access and privacy policy for interview archives;
- whether narrators can revise publication permissions after deposit;
- which oral traditions exist at campaign start;
- which historical claims intentionally remain unresolved.

The complete Caelo primary corpus was not reliably available during this run. Super PTU Online Helper was not exposed as an invocable capability. No result was invented for either.