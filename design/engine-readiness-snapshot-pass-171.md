# Engine Readiness Snapshot — Pass 171

Status: evidence snapshot for narrative dependency planning. Not a rules source and not canon.
Date: 2026-08-25
Narrative focus: seasonal dormancy, torpor, hibernation, emergence and protected winter sites.

## Read-only engine evidence inspected

AutoPTU-Java main head inspected: `d64d6417dc89c1aca878d0a8fd6b526921b8e193` — `Route move-special secondary statuses through canonical prevention (#205)`.

The newest slice composes a generic move-special secondary-status request with canonical status-application prevention. This is concrete progress for a narrow path through move-specific behavior and status application.

It does not demonstrate:

- the full Status controller;
- every secondary Status;
- every Move/Ability/Item/Trainer Feature interaction;
- environmental status application;
- overworld physiological inactivity;
- hibernation or torpor;
- noncombat wake/sleep cycles.

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

AutoPTU Python main head inspected: `54edaa5377589d8d182f91260845389ae694300c` — Career persistence hardening for legacy trainer appearance. It provides no battle-readiness promotion.

## Permanent capability map

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions as a complete family;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

No permanent category is promoted in Pass 171.

## Dormancy is not PTU Sleep

The narrative layer may store:

- long inactivity intervals;
- torpor-like observations;
- arousal observations;
- den/hibernaculum use;
- seasonal entry/exit estimates;
- monitoring gaps;
- emergence timing revisions.

None of these facts can write PTU `Sleep` or `Asleep` automatically.

Sleep-related Abilities and Moves remain mechanical contracts requiring exact rules/engine evidence.

Do not infer:

- Insomnia/Vital Spirit -> inability to rest or enter ecological dormancy;
- Early Bird -> early seasonal emergence;
- Sleep immunity -> immunity to torpor;
- PTU Sleep -> hibernation;
- waking from Sleep -> biological emergence;
- species label 'Hibernator' -> a mechanical state.

## Encounter dependency matrix

### Hibernaculum Access Interruption — FULL

Targeting/footprints/range/LoS: VERIFIED for ordinary combat.

Base movement legality: VERIFIED for ordinary legal shifts.

Complete movement: BLOCKING. Required when researchers, threats or wildlife must withdraw, traverse contested spaces, respect protected cells or interact with interception.

Core calculations: VERIFIED for supported ordinary calculations.

Action economy/initiative: VERIFIED.

Full turn/round lifecycle: PARTIAL when complete lifecycle state matters.

Full stateful damage pipeline: PARTIAL when damage occurs.

Status lifecycle: PARTIAL for exact statuses. Dormancy itself never supplies a Status.

Terrain/weather/hazards/zones/reactions: BLOCKING if cave constraints, unstable ground, protected chambers, snow/ice or other environment modifies tactical legality.

Move-specific behavior: PARTIAL whenever a specific Move is essential.

Abilities: PARTIAL.

Items: PARTIAL.

Trainer Features/perks: PARTIAL.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING for `WITHDRAW`, `PROTECT_RESEARCHER`, `AVOID_PROTECTED_ZONE`, `REACH_EXIT`.

Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED: world state handles equipment retrieval and sensitive-site access. Researchers leave the dormancy chamber. Any independent battle occurs in a static arena outside the protected area. Dormant occupants do not enter combat automatically.

### Early Emergence Road Closure — FULL

Ordinary VERIFIED/PARTIAL battle categories remain as above.

Complete movement: BLOCKING for wildlife crossing/withdrawal and traffic/responders moving dynamically.

Terrain/weather/hazards/zones/reactions: BLOCKING only if snow, ice, barriers or roadside conditions have actual tactical effects.

AI tactical policy: BLOCKING for `CROSS`, `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT_RESPONDER`.

Adapter/playback: BLOCKING.

REDUCED: Road Ecology/Wayfinding resolves closure and wildlife movement before battle. AutoPTU receives a static confrontation only if an unrelated threat remains.

### Den-Site Reconstruction After Storm — FULL

Complete movement: BLOCKING for evacuation, moving debris routes, withdrawal or interception.

Terrain/weather/hazards/zones/reactions: BLOCKING if unstable ground, snow, water, debris or collapse changes tactical legality.

AI tactical policy: BLOCKING for `EVACUATE`, `WITHDRAW`, `PROTECT_WORKER`, `REACH_EXIT`.

Adapter/playback: BLOCKING.

REDUCED: Architecture/Crisis/Cryosphere resolves the site revision. Dormancy monitoring records the coverage gap. Battle, if any, occurs afterward on stable terrain.

### Midwinter Arousal Review — NON-COMBAT

No battle capability is required.

Diel Activity, Dormancy, Timekeeping, Photography/Acoustics/Telemetry and Science may reconcile the observations or leave the case `UNRESOLVED`.

## Recent Java evidence must not be over-generalized

`d64d6417...` routes a move-special secondary Status through canonical prevention.

It does not prove:

- full status lifecycle;
- all secondary effects;
- all status prevention;
- all sleep-related mechanics;
- environmental Status application;
- hibernation mechanics;
- fatigue;
- noncombat sleep/rest rules;
- complete reactions;
- complete movement;
- objective-aware AI;
- adapter playback.

## Pass 171 world-state blockers

Outside current battle parity:

- dormancy-profile persistence;
- episode history;
- entry/exit intervals;
- torpor/arousal observation ledger;
- den/hibernaculum identity;
- disturbance-sensitive survey effort;
- dormancy timing revisions;
- protected-site policy;
- population projection from dormant state;
- Dormancy -> Cobblemon projection;
- Dormancy -> battle snapshot guardrail.

## Mechanical guardrails

Do not create:

- automatic Sleep/Asleep;
- fatigue/exhaustion;
- helpless/vulnerable state;
- Speed/Evasion reduction;
- capture bonuses;
- waking checks;
- seasonal initiative modifiers;
- dormancy healing;
- HP/AP regeneration;
- winter spawn suppression formulas;
- temperature-triggered battle statuses;
- den Terrain;
- disturbance damage;
- automatic aggression on emergence.

## Promotion decision

No permanent capability category changes state in Pass 171.