# Engine Readiness Snapshot — Pass 154

Status: LIVE EVIDENCE SNAPSHOT
Narrative head before pass: `ca30a1ebf38711fad6894a12ec9efaeb6504233e`
Date: 2026-08-30

## Read-only engine heads inspected

AutoPTU-Java:

`9edd7287d7af09df39fadeae8a44c8df37e88642` — `Internalize Intercept position at spatial sequence boundary (#289)`

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`

No files in either engine repository were modified by Pass 154.

## Live Java evidence added since Pass 153

The latest inspected Java change advances server-owned Intercept sequencing.

The spatial sequence boundary now receives:

- attack-line cells;
- ordered candidate identity and canonical rule content;
- authoritative battle state.

The runtime then:

1. preserves the pinned Python behavior of selecting the first sorted Intercept candidate;
2. derives that selected candidate's legal intercept position from server-owned Shift legality;
3. aborts Intercept before check/RNG/resource consumption when the selected candidate cannot reach a legal attack-line tile;
4. does not fall through to later candidates in that case;
5. materializes the Intercept check only after a legal position exists;
6. commits movement only after a successful Intercept;
7. reuses the shared melee Intercept movement path for Push 1, collisions, and partial stops.

This is meaningful evidence for a bounded Intercept sequence and strengthens the adapter-authority boundary: callers do not provide an arbitrary final intercept position.

It remains insufficient to claim complete movement.

## Conservative interpretation

Do not extrapolate the latest Intercept evidence to:

- every Push source;
- Pull;
- general Knockback;
- every Intercept form and ordering interaction;
- arbitrary forced movement;
- environmental displacement;
- escort movement;
- protect/rescue movement;
- object carrying;
- moving platforms;
- generalized reactions;
- dynamic hazards;
- semantic objective ownership;
- tactical retreat/capture/protect policy.

The AutoPTU head remains presentation-side evidence. Its latest commit explicitly states that battle rules and outcomes are unchanged.

## Death/loss authority evidence

Pass 154 introduces narrative architecture around death and loss, but no inspected engine evidence justifies a new death-authority claim.

A code search for `death` in the current AutoPTU-Java repository returned no indexed implementation result during this pass. This absence must be interpreted narrowly:

- it does not prove PTU/Caelo lacks death rules;
- it does not prove AutoPTU-Java can never represent lethal state;
- it does mean Pass 154 cannot claim a verified end-to-end runtime `DEATH_CONFIRMED` contract from inspected evidence.

Therefore:

`KO_OR_FAINTED -> DEATH_CONFIRMED` remains FORBIDDEN as a narrative inference.

Any future promotion requires explicit PTU/Caelo rule evidence plus a tested runtime contract.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No category is promoted by Pass 154.

## Pass 154 encounter matrix

### Memorial Relocation Access Corridor — full version

Required families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when damaged terrain, crowd lanes, or reaction windows are tactical
- move-specific behavior — PARTIAL, individual audit required
- abilities — PARTIAL, individual audit required
- items — PARTIAL, individual audit required
- Trainer Features/perks — PARTIAL, individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Overall: BLOCKED for intended rich form.

Reduced form: READY at narrative-contract level if only individually audited combat content is used.

Reduced constraints:

- memorial objects outside BattleSpec;
- remains/custody state outside BattleSpec if such canon state exists;
- workers and visitors outside BattleSpec;
- static geometry;
- explicit roster;
- no semantic carry/protect objective;
- permitted result: `IMMEDIATE_MEMORIAL_ACCESS_ROUTE_CLEAR` only.

Ouros decides whether relocation proceeds afterward.

### Cemetery Visitor Withdrawal Perimeter — full version

Required families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- lifecycle — PARTIAL
- damage/status as content requires — PARTIAL
- reactions/zones/hazards — BLOCKING when active
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

Overall: BLOCKED for true live escort/withdrawal play.

Reduced form: READY only when Ouros can validly resolve visitor extraction before initiative from existing world facts. The tactical slice then contains remaining combatants only.

Permitted result: `IMMEDIATE_CEMETERY_PERIMETER_CLEAR`.

The battle cannot establish survival of people/Pokémon from unmodeled earlier events.

### Memorial Archive Recovery Chokepoint — full version

Primary blockers:

- semantic object carry/protection/steal behavior is not globally verified;
- complete movement is PARTIAL;
- reactions may be required;
- AI tactical policy is BLOCKING;
- adapter/playback is BLOCKING.

Overall: BLOCKED.

Reduced form: READY.

Archive objects and records remain outside BattleSpec. AutoPTU may return only `IMMEDIATE_ARCHIVE_APPROACH_CLEAR`.

Investigation/Archives then determines custody, authenticity, provenance, and meaning.

`BATTLE_WON != DEATH_RECORD_AUTHENTICATED`

### Survivor Rescue From Memorial-Site Incident — full version

Primary blockers:

- escort/rescue objective semantics;
- complete movement;
- dynamic hazards;
- reactions;
- lifecycle interactions;
- AI tactical policy;
- adapter/playback.

Overall: BLOCKED.

Reduced form: CONDITIONAL READY.

Use the reduced form only when Ouros can establish a safe pre-battle extraction from already verified facts. If the rescue itself requires tactical simulation that current contracts cannot express, the encounter remains blocked.

This encounter receives an additional Pass 154 safety invariant:

`TACTICAL_FAILURE_WITHOUT_DEATH_CONTRACT != DEATH_CONFIRMED`

Narrative cannot translate a failed rescue objective into death unless the authoritative mechanical/world-state contract explicitly resolves that outcome.

## Narrative authority implications

Pass 154 gives Narrative authority over continuity records around loss and memorialization, not over lethal mechanics.

Ouros may decide or preserve, when backed by appropriate canon authority:

- missing reports;
- attributed presumed-alive/presumed-dead statements;
- public/private knowledge;
- memorial creation;
- memorial subject intent;
- memorial relocation;
- marker damage/repair;
- observance participation;
- survivor reevaluation hooks;
- personal-effect memory associations;
- historical correction events;
- unresolved status.

Ouros may record canonical death only after an approved authority source already establishes it.

AutoPTU remains authoritative for tactical facts actually covered by BattleSpec and verified mechanics.

Minecraft/Cobblemon/Craftics remains presentation/playback only and cannot decide:

- death;
- identity;
- cause;
- responsibility;
- grief;
- inheritance;
- Pokémon ownership transfer;
- afterlife;
- spirit identity;
- memorial authenticity;
- combatant roster;
- PTU HP/status.

Minecraft entity removal/despawn must never become canonical death by default.

## PTU/Caelo unresolved mechanics

Keep UNKNOWN until project-approved source evidence and current implementation contracts verify them:

- exact death threshold/trigger approved for Ouros;
- whether lethal combat is enabled generally or only in authored contexts;
- any death-save/stabilization procedure;
- timing between lethal mechanical state and narrative death confirmation;
- handling of death during a battle lifecycle;
- effect of Injuries on death semantics;
- legal restorative/revival effects, if any;
- resurrection mechanics;
- afterlife mechanics;
- generic spirit communication;
- universal funeral/burial mechanics;
- grief penalties or bonuses;
- memorial-derived bonuses;
- ownership/custody transfer after Trainer death;
- inheritance of Pokémon, Poké Balls, items, money, credentials, offices, housing, or businesses;
- automatic faction/reputation consequences from a death;
- escort/rescue objective mechanics;
- generic object-carrying mechanics;
- tactical civilian withdrawal semantics.

## Canon questions opened by Pass 154

- What death mechanics from PTU/Caelo are actually approved for Ouros?
- Can Trainers die mechanically, can Pokémon die mechanically, and under what campaign conditions?
- Which engine event becomes the authoritative death fact?
- How are death, cause, time, identity, and public announcement represented separately?
- Which care institutions can confirm death?
- Which regions use which memorial/funerary practices?
- Do people and Pokémon share memorial institutions in any Ouros communities?
- What authority governs relocation of memorial sites?
- What happens to surviving Pokémon after their Trainer dies?
- Which ownership/custody questions require a future dedicated legal/property layer?
- Are Ghost-type Pokémon ever canonical evidence of deceased spirits in Ouros?
- Which historical losses should remain permanently unresolved?
- Which recurring NPCs/Pokémon should have authored survivor continuity rather than generic grief behavior?
- How should player-character death, if enabled, preserve Chronicle state without silently authoring the player's legacy?

## Pass conclusion

Pass 154 can support memorial sites, missing-person continuity, survivor stories, archive work, relocation, mourning participation, long-term NPC callbacks, and noncombat investigations immediately.

Rich rescue, escort, dynamic memorial-site danger, semantic object protection, and objective-aware tactical encounters remain gated by their real capability families.

Canonical death remains gated by a dedicated authoritative source. No narrative subsystem, Cobblemon battle state, Minecraft entity lifecycle, or presentation event may manufacture it.