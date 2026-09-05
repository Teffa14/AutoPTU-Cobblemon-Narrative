# Global NPC AI / engine readiness snapshot — Pass 281

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05
Narrative repo baseline before this pass: `ce7ce10a257824a0345caba740f039f4275dc1fa`

## Read-only engine evidence

AutoPTU-Java live main inspected at:
`d6c42c2d7c6750a71f10614d2db7525757cc4dca`

Head is PR #362, `Extract declarative temporary-effect lifecycle cleanup hook`. The change creates a reusable `TemporaryEffectCleanupLifecycleHook`, routes round-start cleanup through it, and adds tests for all-combatant versus actor-scoped cleanup plus preservation of unrelated temporary effects.

This is positive narrow evidence for lifecycle/status infrastructure. It does not prove the full turn/round lifecycle or full status lifecycle complete. It also does not verify travel, world-agent AI, complete movement or Minecraft/Cobblemon playback.

AutoPTU Python live main inspected at:
`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Its head remains presentation-only coordinate synchronization and explicitly states that battle rules/outcomes do not change.

Neither engine repository was modified by Pass 281.

## Permanent capability classification

No family is promoted by Pass 281.

- targeting / footprints / range / LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy / initiative: VERIFIED within audited contracts;
- full turn / round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING;
- move-specific behavior: PARTIAL;
- Abilities: PARTIAL;
- Items: PARTIAL;
- Trainer Features / perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING;
- Minecraft / Cobblemon / Craftics adapter / playback: PARTIAL / BLOCKING end-to-end.

## Travel-specific distinction

Global NPC travel is an Ouros world-agent capability. The ordinary world-only version does not depend on `AI tactical policy` and does not claim PTU movement support.

Semantic graph travel can answer:
- where the NPC is at the world-node level;
- which known/permitted route it chose;
- when it must depart;
- its expected arrival;
- whether a route became unavailable;
- whether it needs a replan;
- whether it is late or blocked.

It cannot answer tactical movement questions.

`SEMANTIC_TRAVEL_DURATION != PTU_OVERLAND_MOVEMENT`

## Encounter dependency examples

World-only trip to a social commitment:
- global agenda;
- social relationship/faction input;
- route graph and semantic time;
- no AutoPTU dependency unless structured resolution occurs.

Locally visible arrival:
- global travel state remains authoritative for semantic location;
- Minecraft/Cobblemon/Craftics adapter/playback is required to project the local traversal and acknowledge its result;
- adapter remains PARTIAL/BLOCKING end-to-end, so the reduced version can keep that leg abstract.

Structured road confrontation, full intended version:
- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL if damage occurs;
- status lifecycle: PARTIAL if statuses occur;
- complete movement: PARTIAL if interception/forced movement/knockback occurs;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING when used;
- exact Move/Ability/Item/Trainer Feature families: PARTIAL and must be audited per encounter;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for autonomous tactical choice;
- adapter/playback: PARTIAL/BLOCKING end-to-end.

Reduced version:
- travel reaches an interruption node;
- Ouros records delay/blockage or requests a supported structured encounter;
- unsupported tactical gimmicks are omitted without changing the premise that the journey was interrupted.

## Canon/mechanics questions left open

- No universal Ouros travel speeds are canonized by Pass 281.
- No transport network, road, shortcut, border or settlement is canonized by fixture data.
- Whether semantic edge durations later derive partly from Trainer/Pokémon capabilities remains open and must not be assumed from this planner.
- Local adapter acknowledgement semantics for a projected travel edge still need a dedicated contract.
- Travel events can later feed memory and communication, but Pass 281 does not create those downstream beliefs automatically.
