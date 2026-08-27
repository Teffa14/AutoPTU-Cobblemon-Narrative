# Engine Readiness Snapshot — Pass 71

Status: implementation evidence snapshot. Not canon.

## Read-only sources inspected

AutoPTU-Java head: `87ee4652b8d1d123f6b1180bf4f652053d40cb73`

AutoPTU Python head: `1aec183155fcf6d66f710339708bf74e6575a5c2`

Narrative repo pre-pass head: `a06465f4599c4d85e5166c514500f6fc0af3f72f`

## New Java evidence since Pass 70

Commit `87ee4652` wires the shared `StatusControllerPhaseEnvelopeDispatcher` into live `TURN_START` and `PHASE_CHANGE` lifecycle hooks. Tests verify that both hooks use the shared envelope and that a Flinch-derived pending status skip still propagates through the live lifecycle path.

This is meaningful progress for lifecycle/status orchestration because the phase-envelope work is no longer only a detached policy/dispatcher contract.

It does not prove the entire StatusController family, all status effects, full battle state, damage resolution, move hooks, item hooks, reactions or tactical AI.

The live Java README still lists these work families as pending:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move, ability, item, perk and Trainer Feature hook registries;
- semantic battle-event emission and full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Python evidence

AutoPTU Python head `1aec1831` merges work restoring visible battle replay and the selected Trainer in Career. Recent adjacent commits lock selected-Trainer recovery in replay and keep backend persistence unchanged.

This improves presentation/persistence behavior. It is not evidence of a newly implemented tactical rules family in Java.

## Permanent capability map

### targeting / footprints / range / LoS

Status: VERIFIED

Evidence remains the Java targeting contracts, areas, footprints, target anchors and LoS implementation plus the legal action-space integration.

### base movement legality

Status: VERIFIED

Evidence remains Shift/Jump legality, Overland/Swim/Sky handling, terrain costs, blockers, Wallrunner, sprint and landing-fit predicates.

This category does not include forced movement or interception.

### complete movement including push / pull / knockback / interception / forced movement

Status: BLOCKING

The Java README still explicitly lists forced movement as pending. Do not model tactical evacuation, knockback-sensitive hazards or interception objectives as implemented.

### core calculations

Status: VERIFIED

Damage Base table, type-effectiveness steps, combat stages, accuracy stages, weather DB primitive, critical-hit probability, Burn and modifier/rounding primitives remain present.

A calculation primitive does not imply full battle-system lifecycle support.

### action economy / initiative

Status: VERIFIED

Typed turn flow, action budget, deterministic initiative, Trick Room ordering, League ordering and declared-action ordering remain implemented.

### full turn / round lifecycle

Status: PARTIAL

Pass 71 strengthens this category. The StatusController phase envelope is now wired into live lifecycle hooks instead of existing only as an isolated dispatcher contract.

Still not promoted because the README continues to list core battle state, full StatusController work and semantic BattleTranscript parity as incomplete.

### full stateful damage pipeline

Status: PARTIAL

Calculation primitives exist, but the README still explicitly marks the full damage pipeline as pending.

### status lifecycle

Status: PARTIAL

The live phase envelope and Flinch skip propagation are concrete progress. The full controller and complete registry of status behavior remain unfinished.

### terrain / weather / hazards / zones / reactions

Status: BLOCKING

A `weather DB` calculation primitive exists, but the README still names terrain, hazards and reactions as pending. No general tactical environment controller is verified.

### move-specific behavior

Status: PARTIAL

Representative and supporting infrastructure exists, but the complete move hook registry is still pending.

### abilities

Status: PARTIAL

Do not infer category completion from representative calculations or individual effects. Full registry remains pending.

### items

Status: PARTIAL

The StatusController ordering work anticipates held-item hooks, but full item hook coverage remains pending.

### Trainer Features / perks

Status: PARTIAL

Focused Training / Chronicler Accuracy slices and authoritative runtime-state work provide concrete representative support. The Java README still lists perk and Trainer Feature hook registries as incomplete.

### AI legal-action infrastructure

Status: VERIFIED

The deterministic action-space contract remains implemented for Shift, direct targets, SELF/FIELD, tile-AoE, footprints, LoS and action-budget filtering.

### AI tactical policy

Status: BLOCKING

The README still explicitly lists AI scoring/policy as pending.

### Minecraft / Cobblemon / Craftics adapter and playback

Status: BLOCKING

The Java repository explicitly states it is not a Minecraft mod yet and that the adapter comes after a parity-safe vertical slice.

## Pass 71 encounter consequences

### Restricted Facility Evacuation

Full version requires BLOCKING complete movement, environmental zones/hazards, objective-aware tactical AI and adapter/playback. Lifecycle/status is PARTIAL.

Reduced version can use verified targeting, base movement, calculations, action economy and legal-action generation only after all civilians and access-door dynamics are resolved in overworld state before battle instantiation.

### Field Authorization Interrupted

Full version becomes blocked if retreat/interception, active field weather/terrain or objective-aware territorial AI matters.

Reduced version keeps authorization, supervision, site boundaries and field conditions as narrative/world state and uses a static conventional battle when needed.

## Credential-system mechanical boundary

The new Pass 71 credential layer does not require new battle mechanics by itself.

Credentials may reference:

- authoritative battle results;
- education completion records;
- workplace roles;
- conservation/science access decisions;
- equipment eligibility;
- service prerequisites.

They must not create:

- PTU Skill ranks;
- Edges or Features;
- Moves;
- Trainer interrupts;
- combat bonuses;
- initiative changes;
- action-budget changes;
- item permissions inside battle;
- terrain/weather immunity;
- AI behavior modifiers.

Any future credential that claims a mechanical effect must be reviewed against PTU/Caelo and live AutoPTU evidence as a separate mechanic.

## Promotion decision

No permanent capability category is promoted in Pass 71.

The only readiness change is qualitative: full turn/round lifecycle and status lifecycle have stronger PARTIAL evidence because the shared StatusController phase envelope now participates in the live lifecycle path.

## Open mechanical questions

- When will the complete StatusController move from pending to parity-complete?
- Which concrete held-item and food hooks will populate the currently ordered envelope?
- Which Move/Ability/Item/Trainer Feature registries will be ported next?
- When will forced movement/interception become authoritative?
- What objective semantics will exist for PROTECT, ESCAPE, WITHDRAW, CLEAR_ROUTE or ACCESS?
- What is the first parity-safe adapter vertical slice?
- Which world-state events will be included in BattleTranscript/playback versus remain outside AutoPTU?

Until tests/contracts answer them, narrative designs must continue to use reduced encounter versions where necessary.
