# Field observation disturbance budget contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Pass: 255
Canon effect: NONE

## Purpose

Make field research capable of changing local behavioral pressure without letting observation invent population truth, identity, battle state or canon permissions.

## Authority flow

player/NPC field action
→ observation method declaration
→ evidence capture
→ observation-impact evaluation
→ explicit ecology pressure write when warranted
→ Pass 248 projection-envelope reevaluation
→ later observation of changed visibility/behavior

Knowledge and ecological impact are separate outputs of the same field action.

## Observation impact record

Minimum fields:

observation_id
provenance_root
method_class
target_scope
evidence_quality
disturbance_impact
impact_reason
population_delta
autoptu_handoff

Proposed method classes:

PASSIVE_REMOTE
DISTANT_VISUAL
CLOSE_APPROACH
PHYSICAL_HANDLING

These labels describe implementation semantics only. They are not canon field-protocol names.

## Required separations

A successful observation may produce strong evidence and zero pressure change.

A poor observation may still disturb the subject.

Repeated close approaches may accumulate disturbance pressure even when each observation yields little information.

A disturbance-pressure write cannot create mortality, emigration, capture, recruitment, relocation or a new persistent Pokemon.

Disturbance changes projection only after Pass 248 evaluates the resulting ecology state.

Absence after disturbance is not proof of population absence.

## Provenance and idempotency

Every observation-impact write requires a stable provenance root and unique impact transaction ID.

Replaying or relaying the same observation cannot apply the impact twice.

NPC retellings can alter knowledge distribution but cannot re-disturb the Pokemon retroactively.

## Handling and marking gate

PHYSICAL_HANDLING is fail-closed unless a separate canon-approved authority/welfare policy exists and the runtime can prove that the actor is permitted to perform the action.

Pass 254's fixture-only marker does not satisfy this gate.

Denied handling may still create an attempted-interaction record, but it must not mutate the Pokemon, marker registry or population.

## Recovery

Disturbance pressure may recover only through an explicit ecology recovery event with provenance and a valid quiet/recovery condition.

Fixture-only cooldown values must not become species canon.

Recovery changes behavioral pressure. It does not undo observation history.

## Reduced version

A passive observation gives low/medium-quality evidence with zero pressure delta. Two close approaches add fixture-only pressure through explicit impact transactions. Pass 248 then shifts the projection envelope to reduced visibility. A later quiet-period recovery returns pressure toward baseline. Population remains 12 and no battle opens.

Dependencies: Minecraft/Cobblemon/Craftics adapter/playback is required for actual observation surfaces and behavioral presentation; PARTIAL/BLOCKING end-to-end. No battle capability family is required.

## Rich version

If a player shadows, corners or intercepts a subject to improve evidence:

targeting/footprints/range/LoS: REQUIRED for structured observation geometry; VERIFIED within audited contracts.
base movement legality: REQUIRED; VERIFIED within audited contracts.
complete movement including push/pull/knockback/interception/forced movement: REQUIRED if interception/forced movement occurs; PARTIAL.
core calculations: REQUIRED for adopted deterministic tactical checks; VERIFIED within audited contracts.
action economy/initiative: REQUIRED if the pursuit becomes structured; VERIFIED within audited contracts.
full turn/round lifecycle: REQUIRED for timed pursuit/observation windows; PARTIAL.
full stateful damage pipeline: NOT REQUIRED unless damaging actions occur; PARTIAL as a family.
status lifecycle: NOT REQUIRED unless statuses occur; PARTIAL as a family.
terrain/weather/hazards/zones/reactions: REQUIRED only when they mechanically alter approach, visibility or risk; MIXED/PARTIAL/BLOCKING outside verified slices.
move-specific behavior: validate each Move; family PARTIAL.
abilities: validate each Ability; family PARTIAL.
items: validate each Item; family PARTIAL.
Trainer Features/perks: REQUIRED only if a Feature modifies observation/tracking; PARTIAL and unverified for the Pass 254/255 identity-study use.
AI legal-action infrastructure: REQUIRED for structured wildlife choices; VERIFIED within audited contracts.
AI tactical policy: REQUIRED for flee/avoid/tolerate/search priorities; BLOCKING as a complete family.
Minecraft/Cobblemon/Craftics adapter/playback: REQUIRED; PARTIAL/BLOCKING end-to-end.

## Acceptance gates

1. Evidence quality and disturbance impact are independent fields.
2. Pressure changes require explicit idempotent impact transactions.
3. Relays cannot duplicate impact.
4. Pressure changes cannot alter abundance.
5. Projection changes consume pressure through the existing Pass 248 boundary.
6. Handling/marking fails closed without separate authorization.
7. Recovery is explicit and preserves observation history.
8. No observation event opens AutoPTU by itself.
9. Fixture thresholds remain non-canon.

## Canon status

PROPOSED. No field-research institution, physical marker programme, sensitivity threshold or wildlife-handling permission is approved by this contract.