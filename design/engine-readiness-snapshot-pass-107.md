# Engine Readiness Snapshot — Pass 107

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU are read-only from this task.

## Live heads inspected

AutoPTU-Java `main`: `1ac0eab794f2179297c5d32575e9c82746556a9f`

Latest inspected slice: generic Trainer Feature usage bookkeeping with Python parity. The recent sequence now covers generic prerequisite gates, context gates, frequency/cooldown gates, resource gates and usage bookkeeping as separate primitives. This still does not prove execution of the Trainer Feature catalog or any specific supporter/crowd mechanic.

AutoPTU `main`: `2aa09d7ac741353fff27382b412bf0e1bf5ab161`

Recent Python changes visible during this run are deployment/Career oriented and do not justify promoting a tactical capability family.

## Permanent capability categories

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

## Evidence discipline

The Java README still states that full combat state, full damage, status controller, terrain, hazards, forced movement, reactions, hook registries, transcript parity, tactical AI and Minecraft integration remain incomplete. Representative implemented slices must not be generalized into full-family support.

In particular:
- generic Trainer Feature gates/bookkeeping do not prove Charm-like crowd influence, Musician, Commander, Cheerleader-like behavior, interrupts or any other concrete Feature;
- verified LoS does not imply crowd visibility, privacy, or overworld attention;
- AI legal-action generation does not imply the AI understands PROTECT, EVACUATE, WITHDRAW or CLEAR_ROUTE goals;
- static movement legality does not imply moving crowds, escorts, interception lanes or civilian avoidance;
- semantic field-state infrastructure does not authorize custom morale, cheering or audience zones.

## Pass 107 encounter dependency map

### Supporter Section Evacuation — FULL

Requires:
- complete movement including interception / forced movement: BLOCKING
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics playback: BLOCKING
- terrain/weather/hazards/zones/reactions: BLOCKING only if the authored incident includes a validated tactical hazard

Reduced implementation:
- evacuate supporters through world/public-space state;
- freeze a legal static arena;
- use VERIFIED targeting, base movement, core calculations, action economy and legal-action infrastructure;
- any move/status/ability/item/Feature used by combatants remains individually gated by its PARTIAL family evidence.

### Fan Archive Retrieval — FULL

No battle dependency by default.

If authored as protected-cargo combat:
- complete movement including interception / forced movement: BLOCKING
- AI tactical policy: BLOCKING
- playback: BLOCKING

Reduced implementation:
- investigation, archive access, provenance and transport remain overworld systems;
- optional unrelated combat uses a static legal arena.

### Public Appearance Chokepoint — FULL

Requires:
- complete movement including interception / forced movement: BLOCKING
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics playback: BLOCKING
- terrain/weather/hazards/zones/reactions: only if a real validated environment effect exists

Reduced implementation:
- redirect crowd before combat;
- resolve wild withdrawal outside the grid;
- open AutoPTU only for remaining combatants.

## New overworld blockers introduced by Pass 107

These belong outside AutoPTU-Java:

- `PUBLIC_FIGURE_PROFILE`
- `AUDIENCE_SEGMENT_STATE`
- `SUPPORTER_GROUP_STATE`
- `ATTENTION_EVENT_GRAPH`
- `PUBLIC_PERSONA_REVISION_HISTORY`
- `FAN_ARTIFACT_PROVENANCE`
- `SUPPORTER_ACTIVITY_SCHEDULE`
- `EVENT_AUDIENCE_STATE`
- `PUBLIC_FIGURE_PRIVACY_POLICY`
- Fandom -> Media handoff
- Fandom -> Tourism/Public Space pressure handoff
- Fandom -> Markets/Sponsorship handoff
- Fandom -> Minecraft presentation projection

## Hard non-inferences for this pass

Do not infer:
- crowd support -> morale or damage;
- booing -> Accuracy or initiative penalty;
- popularity -> Charm or Command rank;
- supporter club -> faction combat unit;
- public fame -> AI access to private movesets;
- famous Pokémon -> higher Loyalty or obedience;
- fan-made stats -> authoritative battle record;
- merchandise -> ownership/custody rights;
- visible supporter cosmetics -> actual membership;
- media reach -> world truth.

## Mechanical/canon questions still unresolved

- Does PTU/Caelo contain any crowd, morale, cheering, fame or audience mechanic that Ouros should preserve?
- Which specific Trainer Features could interact with public performance or supporters, and are any implemented in Java?
- How should public battle transcripts expose information without granting future AI omniscience?
- Should Minecraft ever render noncombatants inside a live tactical arena, or should crowd evacuation always precede combat?
- What privacy controls exist for public PCs and persistent Pokémon?
- Which supporter institutions and famous figures exist before campaign start?

The full Caelo corpus was not reliably accessible during this run. Super PTU Online Helper was not exposed as an invokable capability. No rule claims were invented from either source.
