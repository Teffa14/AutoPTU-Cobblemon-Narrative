# Engine Readiness Snapshot — Pass 25

Status: implementation evidence snapshot for narrative authoring. Not canon. AutoPTU-Java and AutoPTU are read-only inputs for this task.

Inspected date: 2026-08-19

## Live revisions inspected

Latest inspected AutoPTU-Java commit:

`de0ab9f6224c76dc232071881f4a88435262d7e1` — Port authoritative turn-end lifecycle boundary (#52).

New Java evidence since Pass 24:

- `de0ab9f6224c76dc232071881f4a88435262d7e1` adds a semantic turn-end battle event, permits turn-end events in the event model, performs authoritative turn-end temporary cleanup through the lifecycle registry, freezes the Python turn-end lifecycle contract and tests parity against Python.

Relevant immediately prior evidence remains:

- `a735d66c8bf19c5fdda712b4fce4773e6f0ee3d4` — ordinary Move resolution writes actual HP loss into authoritative round damage history.
- `28d49949b63f2e675680356e650ac5b04e0c5c6b` — round injury-history rotation with lifecycle hooks and Python parity.
- `53d9a7b521fb398e28984334e9aa2a9a33d98db0` — round damage-history rotation with lifecycle hooks and Python parity.
- `62e6bef9e45b2e30febb48b4b6b73927c36328c0` — delayed hits bound to canonical attacker/move/target inputs.
- `6111b6c5bcda851a1015ddc3ac4d5b578edc2c10` — authoritative delayed-hit scheduling and due/future partitioning.
- `6c357d59061be2eae7bbbb85f401750acd7cf686` — payload-bearing temporary-effect state.
- `b71a0c1887cd303b78099eed846293a9dd60ef2f` — round-start temporary-effect cleanup.
- `6570d95ac874bc26bc6bcc8ffe64d007bba37e34` — authoritative lifecycle hook registry.
- `046cc9f97ed8893e97674222f80789afcdf2cc7f` — pre-damage Move hooks with parity-backed Mega Launcher slice.
- `1757163fe793335e24a17769ee0fdfb78e87c754` — authoritative held-item state and parity-backed Pink Pearl damage hook.
- `7b0fac33d139d8bd72b265aa00bb939e895d5a9a` — ordered damage-hook registry with representative Burn behavior.

Latest inspected Python AutoPTU commit:

`54e4fa8ccbe0e555afef8b4b3713e7568608e5d3` — merge of stateless casual Career/serverless persistence work.

Recent Python commits inspected are Career/runtime persistence changes. They do not establish additional battle-family readiness for this pass.

The Python battle oracle itself contains much broader battle behavior than Java. Relevant to Pass 25, `battle_state.py` contains Trainer Feature actions for Telepath, Thought Detection, Suggestion, release of Suggestion and Psionic Analysis, with temporary psychic-residue state and Mindlock-aware blocking. This is Python-oracle evidence only. It does not establish Java support.

## Permanent capability classification

### VERIFIED

#### targeting/footprints/range/LoS

Canonical target anchors, target modes, footprints, range and line of sight have explicit action-space/test evidence.

#### base movement legality

Verified for the ported Shift/Jump legality slice, supported movement modes, static terrain costs/blockers and landing-fit behavior.

This excludes push/pull, knockback, interception and forced movement.

#### core calculations

Verified for explicitly ported primitives including Damage Base tables, type-effectiveness steps, stages, selected accuracy/crit/weather calculations, Burn calculation slices, modifiers and rounding points.

Calculation helpers that mention Weather do not establish authoritative battlefield Weather state.

#### action economy/initiative

Typed phases, action budget and deterministic initiative/League/Trick Room/declaration ordering have direct evidence.

#### AI legal-action infrastructure

The engine can enumerate deterministic legal choices for supported movement and target modes with action-budget filtering.

This proves legality infrastructure only, not tactical choice quality.

### PARTIAL

#### full turn/round lifecycle

This category is stronger than Pass 24 because Java now has an explicit authoritative turn-end boundary as well as round-start behavior and several server-owned lifecycle state stores.

Verified slices now include:
- authoritative round controller;
- lifecycle hook registry;
- round-start temporary-effect cleanup;
- payload-bearing temporary-effect state;
- semantic turn-end battle event;
- authoritative turn-end temporary cleanup;
- delayed-hit scheduling and canonical binding;
- round damage-history rotation;
- round injury-history rotation;
- ordinary Move resolution writing into authoritative damage history.

It remains PARTIAL because complete effect execution, all duration semantics, all trigger families, turn-start/turn-end behavior for the full rules corpus and full BattleSpec -> BattleTranscript parity are not established.

#### full stateful damage pipeline

Calculation primitives, ordered hooks, representative Burn/Mega Launcher/Pink Pearl paths and authoritative damage-history writeback exist.

It remains PARTIAL because full end-to-end resolution and all modifier/trigger sources are not verified.

#### status lifecycle

Burn plus lifecycle/injury infrastructure provide real slices.

Still PARTIAL because the complete status controller, saves, durations and cross-status interactions are not ported.

This matters for dream/sleep content: do not assume Sleep, Bad Sleep, Drowsy or nightmare-related status interactions are complete merely because lifecycle cleanup exists.

#### move-specific behavior

Canonical Move state, selected hooks, delayed-hit scheduling/binding and damage-history integration exist.

Still PARTIAL. Representative Move behavior does not establish the complete Move library. Dream Eater, Hypnosis or another dream-related Move must be checked individually before use.

#### abilities

Mega Launcher has parity-backed authoritative hook evidence.

Still PARTIAL because the complete Ability registry and behavior set are not established. Dream-related abilities such as Bad Dreams, Insomnia, Forewarn or others cannot be assumed present without direct evidence.

#### items

Held-item state and Pink Pearl provide an authoritative representative item path.

Still PARTIAL because the complete item library and item hook families remain unverified.

### BLOCKING

#### complete movement including push/pull/knockback/interception/forced movement

The current Java README still lists forced movement/reactions among unfinished work. No inspected live evidence verifies this family.

#### terrain/weather/hazards/zones/reactions

Generic lifecycle infrastructure does not establish dynamic dream terrain, psychic zones, shifting geometry, hazards or reactions.

Remain BLOCKING.

#### Trainer Features/perks

This is the principal blocker for Pass 25 mechanics.

Python AutoPTU contains concrete Telepath/Thought Detection/Suggestion/Psionic Analysis behavior. The Java README still lists perk and Trainer Feature hook registries among unfinished work, and code search found no Java implementation of those actions.

Generic temporary-effect payloads and lifecycle hooks are useful future infrastructure. They do not prove Telepath, Suggestion, Mindlock interaction, Psionic Analysis or any other Trainer Feature behavior.

Remain BLOCKING.

#### AI tactical policy

Legal action generation exists. Tactical scoring/policy over legal choices remains unfinished.

This blocks encounters where opponents should escape, protect a dream anchor, defend equipment, pursue a non-DEFEAT objective or react strategically to supernatural information.

#### Minecraft/Cobblemon/Craftics adapter/playback support

AutoPTU-Java remains a standalone Java rules core. The current README explicitly places Minecraft/Cobblemon/Craftics consumption later and lists the adapter as unfinished.

This is especially relevant for private dream views, psychic/Aura visualization, dream-space transitions and participant-specific information presentation.

## Pass 25 dream/psychic implications

The following narrative/world-state structures can advance now without Java psychic mechanics:

- subjective-event records;
- player-authored dream reports;
- private perception packets;
- research hypotheses about dream phenomena;
- dream anchors and persistent dream-region topology as narrative state;
- public rumors and corrections;
- case evidence records that clearly identify source type;
- mental-privacy and consent policy;
- care-facility aggregate sleep signals;
- archaeology/public-memory links to dream motifs;
- Minecraft presentation requirements as future adapter contracts.

The following must not be promoted to implemented tactical mechanics yet:

- Java Telepath/Thought Detection/Suggestion/Psionic Analysis;
- psychic Feature AP/use limits;
- Mindlock interactions in Java;
- dream-reading mechanics;
- forced Sleep/Bad Sleep behavior unless individually verified;
- dream terrain with changing zones;
- telepathic battle commands beyond validated PTU mechanics;
- psychic residue created locally by Minecraft scripts;
- AI using private thoughts or unobserved information;
- private/shared dream rendering as if the adapter already supported it.

## Pass 25 encounter dependency table

| Encounter | Full-version key dependencies | Current readiness | Reduced version |
|---|---|---|---|
| Dreamyard Containment | lifecycle; status lifecycle; move-specific behavior; abilities; optional Trainer Features; terrain/hazards/zones if machinery changes battlefield; tactical AI; adapter | BLOCKING overall | world-state disturbance + reviewed static arena + ordinary legal combat + equipment resolution outside grid |
| Shared Nightmare Exit | lifecycle; status lifecycle; Trainer Features for dream/telepath mechanics; dynamic terrain/zones; non-DEFEAT AI; adapter/private views | BLOCKING overall | narrative/Minecraft dream exploration + static legal battle + exit resolution outside grid |
| Aura Trail Interception | Trainer Features/perks or exact validated capability; ordinary verified battle families; adapter for Aura visualization | BLOCKING for Java supernatural sensing, VERIFIED for reduced combat core | sensing resolved outside battle from authoritative source; ordinary static encounter |
| Psychic Residue Dispute | Trainer Features/perks; lifecycle; source-specific moves/abilities/items; adapter | BLOCKING overall | residue as previously validated evidence record; ordinary investigation + standard battle if needed |

## New turn-end evidence and non-inference

The latest Java commit is important because many PTU effects eventually need a precise turn-end boundary.

It does not prove the downstream mechanics that may use that boundary.

Do not infer:
- complete status durations from turn-end cleanup;
- Telepath/Suggestion behavior from generic temporary effects;
- Trainer Features from lifecycle registry existence;
- reactions from semantic battle events;
- dream/sleep mechanics from turn-end support;
- AI policy from more complete server state;
- Minecraft playback from event emission.

## Current source-of-truth boundary

Python `Teffa14/AutoPTU` remains the behavioral oracle while Java parity is incomplete.

The narrative repository may author subjective-information state, dream-world structures, privacy rules, desired encounters and reduced implementations. It must not recreate missing PTU psychic, sleep, Aura, Trainer Feature or environmental mechanics in Minecraft scripts, Cobblemon hooks or narrative code.
