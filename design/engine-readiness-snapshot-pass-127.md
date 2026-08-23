# Engine Readiness Snapshot — Pass 127

Status: IMPLEMENTATION EVIDENCE SNAPSHOT. Read-only inspection of AutoPTU-Java / AutoPTU. No engine files changed by this task.

## Inspected heads

AutoPTU-Java main: `967b16237c6ea93a939bd4acbbe67da979885a60`

Recent Java slices inspected:
- `967b1623` — Mirror Armor combat-stage reflection; recursive prevention/reflection context; parity gate.
- `ba4d489c` — target-owned Combat Stage Ability prevention family; declarative resolver; parity gate.
- `554b97e4` — Flower Veil / Flower Veil [Errata] Combat Stage prevention.

AutoPTU Python main: `9df36aeae4bcbef49fd5edb658b51d68bd45fa71`

Recent Python activity remains Career-oriented and does not justify a tactical capability promotion for this snapshot.

## Live README boundary

AutoPTU-Java still describes itself as a Java 21 battle library, not a Minecraft mod. Python AutoPTU remains the authoritative oracle while the port is incomplete.

The Java README marks as complete targeting/range/areas/footprints/LoS, base Shift/Jump legality, core calculations, typed turn/action budget, deterministic initiative and legal autobattler action-space infrastructure.

It still marks as unfinished:
- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Permanent capability categories

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

These categories have broad enough contracts and parity evidence to support reduced static encounters, subject to exact Move/Ability/Feature caveats.

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

Recent Combat Stage prevention/reflection work strengthens Abilities and Combat Stage mutation ordering, but one family such as Flower Veil or Mirror Armor does not prove all Abilities or all recursive reactions.

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

## Pass 127 language-layer implications

Language, translation, writing systems and actor comprehension are overworld/information-state systems. They do not belong inside the battle engine unless an exact PTU/Caelo mechanic explicitly invokes them.

No evidence was found for a generic Java or Python runtime subsystem that models:
- spoken-language competence;
- literacy;
- translation;
- interpretation confidence;
- script deciphering;
- multilingual signage;
- machine translation;
- actor comprehension after message delivery.

Therefore these remain narrative/world-state blockers rather than battle categories:
- `LANGUAGE_SYSTEM_STATE`
- `WRITING_SYSTEM_STATE`
- `ACTOR_LANGUAGE_PROFILE`
- `TEXT_AND_TRANSLATION_PROVENANCE`
- `TERMINOLOGY_STANDARD_VERSIONING`
- `MULTILINGUAL_SIGNAGE_STATE`
- `ACTOR_COMPREHENSION_STATE`
- `LANGUAGE_TO_COMMUNICATION_HANDOFF`
- `LANGUAGE_TO_ARCHIVE_HANDOFF`
- `LANGUAGE_TO_MINECRAFT_PRESENTATION`

## New encounter dependency mapping

### Archive Script Dispute

Reduced version can run now because translation and investigation remain outside AutoPTU and any combat is static.

FULL version requires moving expedition objectives:
- complete movement/interception/forced movement — BLOCKING
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

### Station Signage Failure

Reduced version can run after crowds are resolved in world state.

FULL version requires:
- complete movement/interception — BLOCKING
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

### Unown Survey Chamber

Reduced observational version can run now with no mechanical symbol effect.

A future version where symbols alter battlefield state would require:
- terrain/weather/hazards/zones/reactions — BLOCKING
- exact Move-specific behavior if a Move is involved — PARTIAL and must be individually verified
- exact Ability behavior if an Ability is involved — PARTIAL and must be individually verified
- adapter/playback — BLOCKING

## Guardrails

Do not infer:
- battle LoS -> language comprehension;
- Psychic type -> translation;
- Telepathy flavor -> universal language access;
- Chatot mimicry -> semantic understanding;
- Unown glyph resemblance -> deciphered text;
- Pokémon Education -> fluency;
- Trainer Feature generic execution -> Translator capability;
- Minecraft book/sign text -> authoritative interpretation;
- a static battle victory -> correct historical reading.

## Unresolved mechanical questions

- Does the project PTU/Caelo corpus define languages or literacy at all?
- Are there exact rules for telepathic communication that distinguish communication from translation?
- Do any Edges, Features or Capabilities govern deciphering, linguistics or written codes?
- How should player language preferences interact with character knowledge without reducing accessibility?
- If a future Unown encounter has mechanical text/symbol behavior, which exact PTU rule authorizes it?

The complete primary Caelo source set was not reliably available in this runtime. Super PTU Online Helper was not exposed as an invocable capability. No rules were invented to fill those gaps.
