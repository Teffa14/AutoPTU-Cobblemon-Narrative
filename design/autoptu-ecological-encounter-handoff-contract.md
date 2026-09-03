# AutoPTU ecological encounter handoff contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Pass: 242
Canon effect: NONE

## Purpose

Define the exact transition from persistent ecological behavior in Ouros to structured AutoPTU mechanics and back again.

The contract exists to prevent three failures:

- converting every wild contact into combat;
- letting Minecraft/Cobblemon decide tactical truth;
- letting AutoPTU results silently become ecological conclusions.

## Authority sequence

`persistent ecology state -> observable behavior -> encounter-intent evaluation -> optional BattleSpec assembly -> AutoPTU -> semantic tactical result -> Ouros world-state evaluation -> Minecraft/Cobblemon projection`

Only Ouros may open the encounter boundary.

## Encounter-intent evaluator

Required inputs:

`interaction_id`
`world_context_ref`
`actor_refs`
`player_intents`
`wild_behavioral_intents`
`ecology_event_ref nullable`
`requested_mechanical_question`
`active_rules_profile`
`required_capability_families`
`fallback_profile`

Required output:

`STAY_OVERWORLD`
`OPEN_AUTOPTU`
`USE_REDUCED_VERSION`
`BLOCK_UNSUPPORTED`

The evaluator must fail closed when a requested tactical mechanic lacks verified support.

## Handoff matrix

### Stay in overworld

Use `STAY_OVERWORLD` when the interaction can be represented without PTU mechanical adjudication.

Typical cases:

- observation;
- tolerance;
- warning display;
- hiding;
- ordinary foraging/resting;
- social signaling;
- unopposed departure;
- player backs away;
- ordinary route avoidance;
- noncombat world-service intervention.

Minecraft can animate these states only from Ouros-authorized behavior.

### Open AutoPTU

Use `OPEN_AUTOPTU` when the answer depends on structured PTU legality or state.

Trigger families:

`DIRECT_HOSTILE_ENGAGEMENT`
Requires attacks, targets, range, initiative, damage or other tactical facts.

`PLAYER_STRUCTURED_ENGAGEMENT`
The player requests a mechanically meaningful PTU action whose legality belongs to AutoPTU.

`TACTICAL_PURSUIT_OR_ESCAPE`
Success depends on exact movement, footprints, distance, interception, forced movement or turn order.

`DEFENSE_OR_ESCORT_OBJECTIVE`
The encounter requires protecting an actor/area under tactical timing or target pressure.

`TACTICAL_HAZARD_CONFLICT`
Terrain/weather/hazard/zone rules become mechanically consequential.

`CONTESTED_CAPTURE`
Only when the adopted Ouros rules profile assigns the contested capture sequence to AutoPTU.

## Explicit non-triggers

None of the following may open AutoPTU by itself:

- distance threshold;
- player enters chunk;
- Minecraft collision;
- Cobblemon aggression flag;
- entity targets player;
- visible attack animation;
- vanilla damage event;
- Poké Ball animation;
- entity despawn;
- nearby Pokémon count;
- ecology event entering `ESCALATING`;
- quest acceptance.

## Combatant freeze

Before BattleSpec creation, Ouros must freeze a manifest.

Each participant requires:

`persistent_actor_ref`
`projection_lease_ref nullable`
`mechanical_profile_ref`
`side`
`role`
`initial_position_source`
`initial_position`
`footprint_profile`
`entry_reason`

Nearby actors not in the manifest remain overworld actors.

A later reinforcement cannot be inferred from a spawned entity. It requires a separate legal entry transition.

## BattleSpec mapping

World facts become tactical facts only through reviewed mappings.

Allowed candidates:

- world position -> initial tactical position;
- static block geometry -> reviewed battlefield geometry;
- visible weather -> tactical Weather only when the corresponding rules/capability mapping is explicitly enabled;
- route barrier -> tactical impassable geometry only when mapped;
- persistent actor state -> frozen battle mechanical profile.

Unmapped world facts remain presentational.

## Freeze point

At `OPEN_AUTOPTU`, the following become AutoPTU-owned for the battle instance:

- combatant roster;
- tactical positions;
- HP/status/combat-stage state used by the encounter;
- initiative/action economy;
- targets and legality;
- movement legality;
- damage/healing/status resolution;
- tactical terrain/weather/hazards that were explicitly mapped;
- encounter-end tactical conditions.

Ouros continues to own ecological state but must not independently simulate those tactical facts during the active battle.

## Ecology during battle

Noncombatant ecological state may continue evolving only where doing so cannot mutate the active BattleSpec implicitly.

Examples that may continue:

- remote population processes;
- unrelated migration elsewhere;
- NPC knowledge propagation;
- clocks and event timers that do not alter battle mechanics.

Examples requiring a declared seam before affecting the current battle:

- reinforcement arrives;
- weather changes tactically;
- route closes inside the arena;
- nest actor enters combat;
- hazard activates;
- third party intervenes.

Without a verified seam, defer the effect until battle completion or use a linked BattleSpec.

## Semantic result envelope

AutoPTU returns a narrow result envelope.

Required fields:

`battle_instance_id`
`source_interaction_id`
`participant_final_states`
`objective_results`
`capture_results`
`withdrawal_results`
`semantic_events`
`engine_rules_profile`
`completion_reason`

Ouros may consume only fields verified by the current engine contract.

## World-state conversion

Examples:

`TACTICAL_KO_CONFIRMED` -> may update encounter history and condition; does not mean ecological death.

`TACTICAL_WITHDRAWAL_FORCED` -> may permit Ouros to evaluate displacement if a valid route exists; does not automatically mean emigration.

`ESCAPE_ROUTE_CLEARED` -> may lower immediate conflict pressure; does not resolve the ecology event automatically.

`CAPTURE_MECHANIC_SUCCEEDED` -> only after capture authority is verified may Ouros emit the corresponding demographic `CAPTURE_REMOVAL`.

`OBJECTIVE_AREA_HELD` -> may permit a world intervention to proceed; does not mean the habitat is restored.

## Re-entry to overworld

After writeback, each surviving persistent participant returns through a projection decision:

`REMATERIALIZE`
`KEEP_EXISTING_PROJECTION`
`SUSPEND_PROJECTION`
`RELOCATE_PROJECTION`
`REMOVE_FROM_WILD_POPULATION_AFTER_AUTHORIZED_DEMOGRAPHIC_EVENT`

A missing Minecraft entity does not block persistence. Ouros reconstructs presentation from authoritative state.

## Reduced-version rule

If an encounter premise requires unsupported mechanics, preserve the narrative premise with a reduced form.

Examples:

- tactical chase -> unopposed overworld escape plus later observation consequence;
- reinforcement -> second linked BattleSpec;
- dynamic weather phase -> static presentation-only weather;
- reaction-based nest defense -> ordinary explicit combatants from battle start;
- forced movement corridor -> static blocked/open geometry;
- complex calming mechanic -> tactical `CALMING_WINDOW_CREATED` followed by Ouros world evaluation.

## Capability dependency matrix

Targeting/footprints/range/LoS: REQUIRED for most structured engagement. Current state: VERIFIED within audited contracts.

Base movement legality: REQUIRED for structured movement. Current state: VERIFIED within audited contracts.

Complete movement: REQUIRED only for push/pull/knockback/interception/forced movement or equivalent. Current state: PARTIAL.

Core calculations: REQUIRED when checks/damage consume PTU arithmetic. Current state: VERIFIED within audited contracts.

Action economy/initiative: REQUIRED for ordinary structured combat. Current state: VERIFIED within audited contracts.

Full turn/round lifecycle: REQUIRED for timed objectives, phase timing, delayed effects and round-sensitive logic. Current state: PARTIAL.

Full stateful damage pipeline: REQUIRED for damaging combat. Current state: PARTIAL.

Status lifecycle: REQUIRED when statuses are permitted. Current state: PARTIAL.

Terrain/weather/hazards/zones/reactions: REQUIRED only when those facts are tactical. Current state: MIXED/PARTIAL/BLOCKING outside verified slices.

Move-specific behavior: validate every Move. Family state: PARTIAL.

Abilities: validate every Ability. Family state: PARTIAL.

Items: validate every tactical Item. Family state: PARTIAL.

Trainer Features/perks: validate every Feature/Edge. Family state: PARTIAL.

AI legal-action infrastructure: REQUIRED for AI combatants. Current state: VERIFIED within audited contracts.

AI tactical policy: REQUIRED when wildlife must prioritize flee/guard/escort/separation/objectives. Current state: BLOCKING as a complete family.

Minecraft/Cobblemon/Craftics adapter/playback: REQUIRED end-to-end for visible production handoff. Current state: PARTIAL/BLOCKING.

## Regression invariants

1. Overworld contact never automatically creates a BattleSpec.
2. Every tactical participant is explicitly frozen before battle creation.
3. Nearby spawned actors cannot join implicitly.
4. Minecraft cannot author HP, status, initiative, legality or outcomes.
5. Unmapped weather/terrain remains presentation-only.
6. Unsupported rich mechanics select a reduced version or block; Cobblemon never fills the gap.
7. AutoPTU result vocabulary remains narrower than ecological consequence vocabulary.
8. KO never means death automatically.
9. Capture changes abundance only through an authorized demographic event.
10. Battle completion cannot resolve an ecology event without post-result ecological evaluation.
11. Missing/despawned renderer entities do not remove persistent actors.
12. Reconnect/chunk reload reconstructs presentation from Ouros/AutoPTU truth.

## Status

PROPOSED. No new PTU rule, species, event, geography or engine capability is canonized by this contract.
