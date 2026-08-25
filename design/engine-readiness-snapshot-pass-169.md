# Engine Readiness Snapshot — Pass 169

Status: evidence snapshot for narrative dependency planning. Not a rules source and not canon.

Date: 2026-08-25

Narrative focus: structural inspection, load/capacity assessment, operational restriction, repair verification and condition monitoring.

## Read-only engine evidence inspected

AutoPTU-Java main head inspected: `3825f32490c405a3d541c5eddf4b04097b4d1e69` — `Carry canonical move effects text (#199)`.

The new Java slice carries canonical Move effects text inside `MoveSpec`, adds a server/runtime-owned fallback path and freezes parity against a pinned Python oracle. This is useful evidence for canonical Move content ownership and `move-specific behavior` infrastructure.

It does not demonstrate that the effects text is fully executed, that the complete Move catalog has parity, or that structural/environmental rules exist.

AutoPTU-Java README still explicitly leaves these major families incomplete:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- remaining move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

AutoPTU Python main head inspected: `e6aa730a77e25142f5308eaa3a738dc66ba34bbb` — Career presentation hardening for malformed winner tokens. The commit explicitly does not change combat mechanics.

## Permanent capability map

`VERIFIED`

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

`PARTIAL`

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

`BLOCKING`

- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions as a complete family;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

No category is promoted in Pass 169.

## Why structural inspection is primarily world state

Inspection, load/capacity assessment, restrictions and repair verification belong outside the PTU battle engine.

AutoPTU may authoritatively resolve a separate confrontation near an inspection site. Its transcript can support claims such as `combatants were defeated`, `the party withdrew` or `the static route was cleared` when the encounter contract allows it.

It cannot determine:

- whether a crack is structural;
- whether deterioration progressed;
- bridge load capacity;
- whether a restriction is necessary;
- scour depth;
- whether a foundation is stable;
- whether a repair restored capacity;
- whether a structure should reopen;
- engineering causation;
- inspection completeness.

## Encounter dependency matrix

### After-Flood Foundation Survey — FULL

Targeting/footprints/range/LoS: VERIFIED for ordinary combat.

Base movement legality: VERIFIED for ordinary legal shifts.

Complete movement: BLOCKING. Required if researchers or wildlife must cross/withdraw through threatened space, if interception matters, or if a safe-route objective is tactical.

Core calculations: VERIFIED for supported ordinary calculations.

Action economy/initiative: VERIFIED.

Full turn/round lifecycle: PARTIAL when complete lifecycle state matters.

Full stateful damage pipeline: PARTIAL when damage is used.

Status lifecycle: PARTIAL for any actual Status.

Terrain/weather/hazards/zones/reactions: BLOCKING if current, unstable banks, falling, debris, protected work zones or reaction movement alter tactical legality.

Move-specific behavior: PARTIAL whenever a particular Move beyond verified generic behavior is essential.

Abilities: PARTIAL.

Items: PARTIAL.

Trainer Features/perks: PARTIAL.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING for `PROTECT_RESEARCHER`, `REACH_OBSERVATION_POINT`, `WITHDRAW`, `CROSS` or `CLEAR_ROUTE` behavior.

Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version: resolve flood/scour state and move researchers to a stable approach in world state. Use an ordinary static arena only if an independent confrontation remains. No current, collapse, falling or inspection-device mechanics are created.

### Emergency Shoring Access — FULL

The ordinary battle-facing VERIFIED/PARTIAL categories remain unchanged.

Complete movement: BLOCKING for technicians/custodians reaching a work point, withdrawal or interception.

Terrain/weather/hazards/zones/reactions: BLOCKING if moving/falling structural pieces, unstable surfaces, gaps or temporary shoring have tactical effects.

AI tactical policy: BLOCKING for `REACH_WORK_POINT`, `PROTECT_TECHNICIAN`, `WITHDRAW` or `CLEAR_ROUTE`.

Adapter/playback: BLOCKING.

Items remain PARTIAL if safety/shoring equipment is expected to have tactical effects.

REDUCED version: evacuate the work zone, freeze structural state and use a stable adjacent battle arena. Public Works resumes only after combat.

### Heritage Bridge Inspection Disturbance — FULL

Complete movement: BLOCKING for civilians, inspectors and wildlife moving through restricted/narrow space.

Terrain/weather/hazards/zones/reactions: BLOCKING if height, scaffolding, falling or temporary platforms matter tactically.

AI tactical policy: BLOCKING for `EVACUATE`, `PROTECT_INSPECTOR`, `WITHDRAW` and `CLEAR_ROUTE`.

Adapter/playback: BLOCKING.

Any exact Status, Ability, Item, Trainer Feature or Move interaction remains PARTIAL unless a current contract verifies that mechanic.

REDUCED version: terminate the inspection and evacuate everyone through world state. Preserve `PARTIAL`/`ACCESS_BLOCKED` inspection state. Run any independent fight on a static plaza or approach.

### Condition Review Board — NON-COMBAT

No battle capability is required. Architecture, Public Works, Metrology, Travel and Institutional Review can decide or leave the assessment `UNRESOLVED` using world state.

## Recent Java evidence must not be over-generalized

`3825f324...` ensures canonical Move effects text is carried in the Java model and supplies a runtime-owned fallback. It does not prove:

- that every text effect is parsed or executed;
- that every Move special exists;
- full Status behavior;
- full Ability/Item/Trainer Feature registries;
- generic environmental effects;
- structural collapse mechanics;
- forced movement;
- tactical objectives;
- Minecraft structural integration.

Likewise:

- verified battle LoS cannot be reused for structural inspection visibility;
- base movement legality cannot model evacuation/escort objectives by itself;
- PTU terrain costs cannot become bridge-condition ratings;
- canonical Move effects text cannot become an engineering rules source.

## PTU cross-check guardrails

Public PTU 1.05 material describes Technology Education as covering machines, engineering-related technology and examples such as vehicle/machinery repair. This does not define bridge-inspection certification, structural capacity, load ratings or a universal repair DC.

Groundshaper/Mold the Earth has specific PTU terrain/hazard semantics. It cannot be repurposed as foundation stabilization, scour repair, shoring or bridge reconstruction.

Do not infer Power, Weight Class, Strength-like Moves or Pokémon typing into structure capacity.

## Pass 169 world-state blockers

These are implementation questions outside AutoPTU parity:

- structural inspection-program persistence;
- zone/element references at narrative scale;
- defect/anomaly histories;
- engineering-assessment revisions;
- load/capacity assessment scopes;
- operational-restriction lifecycle;
- special-inspection triggers;
- structural monitoring links to Metrology/Timekeeping;
- scour/foundation handoff from Freshwater/Fluvial layers;
- repair-verification workflow;
- transport rerouting and reopening handoffs;
- Minecraft projection without block-based structural authority.

## Mechanical guardrails

Do not create:

- structural HP;
- collapse rolls or percentages;
- block-hardness capacity;
- entity-weight bridge loading;
- automatic Rough Terrain from cracks;
- automatic falls from visible damage;
- custom `unsafe structure` Status;
- Technology Education inspection bonuses without exact rules;
- Groundshaper repairs;
- shoring Cover/DR without a verified battle contract;
- victory-based repairs or reopening.

Caelo-specific structural/engineering rules were not recovered reliably in this pass. Super PTU Online Helper was not available as an invocable capability. No output from either is invented.

## Promotion decision

No permanent capability category changes state in Pass 169.