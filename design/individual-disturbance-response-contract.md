# Individual disturbance response contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Pass: 256
Canon effect: NONE

## Purpose

Convert shared ecological disturbance plus persistent individual history into a bounded projection response without changing demographics, PTU state or tactical battle policy.

## Authority flow

Pass 255 observation impact
→ local disturbance pressure
→ persistent individual response profile
→ context-specific response evaluation
→ response history write
→ Pass 248 projection-envelope contribution
→ Cobblemon presentation

AutoPTU does not adjudicate this reduced ecology path.

## Minimum individual response profile

persistent_actor_id
species_policy_revision
baseline_wariness_band
exposure_history_by_stimulus_class
response_trend_by_stimulus_class
last_response_context
response_revision

The internal actor ID never becomes player-facing knowledge.

## Required separations

Population disturbance pressure describes shared local conditions. Individual response state describes one member's history.

Species policy constrains plausible behavior but cannot force all individuals to have the same response.

A lower avoidance response is not population growth, domestication, capture ownership, friendship, obedience or proof of welfare.

A higher avoidance response is not emigration, mortality or permanent removal from the area.

Habituation to one stimulus class does not imply habituation to physical handling, attacks, capture attempts, loud noise or other stimulus classes.

No ecology response state may alter PTU stats, Accuracy, Evasion, movement capabilities, Moves, Ability, status, injuries or damage.

## Proposed evaluation inputs

local_disturbance_pressure
stimulus_class
stimulus_intensity
species_policy_revision
individual_baseline_wariness
prior_exposure_count
prior_response_trend
current_activity_context
resource_pressure
nesting_or_parental_context when canonically available

Unknown inputs remain unknown. The evaluator must not infer them from Minecraft entity behavior after the fact.

## Proposed outputs

MAINTAIN_BASELINE_EXPOSURE
REDUCE_EXPOSURE
EARLY_WITHDRAWAL
EXPANDED_STANDOFF
CONTEXT_TOLERANCE

These outputs affect future ecology/projection eligibility only. They are not battle actions.

## History and reversibility

Each evaluation writes a response-history event with provenance and policy revision.

Later observations may change the trend. The system must preserve prior observations rather than rewriting history to fit the newest classification.

A response trend can differ by stimulus class. Repeated low-intensity approaches may trend toward tolerance while physical handling remains unknown or strongly avoidant.

## Reduced version

Two already-counted Fletchling sources experience the same fixture-only shared disturbance pressure. Actor A has a fixture-only lower baseline wariness and repeated benign approach history, so its future projection remains eligible in a quieter edge window. Actor B has a fixture-only higher baseline wariness and an avoidance trend, so its projection is reduced earlier. Both remain members of the population of 12. No tactical movement or AutoPTU handoff occurs.

Dependencies: Minecraft/Cobblemon/Craftics adapter/playback is REQUIRED to present different exposure outcomes; PARTIAL/BLOCKING end-to-end. Battle capability families are NOT REQUIRED.

## Rich version

If the player actively pursues, blocks or corners the individual and the response becomes tactical:

targeting/footprints/range/LoS: REQUIRED; VERIFIED within audited contracts.
base movement legality: REQUIRED; VERIFIED within audited contracts.
complete movement including interception/forced movement: REQUIRED when those interactions occur; PARTIAL.
core calculations: REQUIRED for adopted deterministic checks; VERIFIED within audited contracts.
action economy/initiative: REQUIRED once structured turns begin; VERIFIED within audited contracts.
full turn/round lifecycle: REQUIRED for timed pursuit; PARTIAL.
full stateful damage pipeline: REQUIRED only for damaging actions; PARTIAL.
status lifecycle: REQUIRED only for statuses; PARTIAL.
terrain/weather/hazards/zones/reactions: REQUIRED only when mechanically relevant; MIXED/PARTIAL/BLOCKING outside verified slices.
move-specific behavior: validate each Move; family PARTIAL.
abilities: validate each Ability; family PARTIAL.
items: validate each Item; family PARTIAL.
Trainer Features/perks: validate each Feature; family PARTIAL.
AI legal-action infrastructure: REQUIRED; VERIFIED within audited contracts.
AI tactical policy: REQUIRED to choose flee/tolerate/route priorities; BLOCKING as a complete family.
Minecraft/Cobblemon/Craftics adapter/playback: REQUIRED; PARTIAL/BLOCKING.

## Acceptance gates

1. Two individuals under the same shared pressure may produce different projection responses.
2. The difference must come from explicit individual/history/context inputs, never random hidden improvisation.
3. Response state is stimulus-specific.
4. Population total remains unchanged without a demographic event.
5. Ecology response state cannot modify PTU combat state.
6. Projection outcomes consume already-counted sources only.
7. Restart preserves response history and policy revision.
8. Player-facing observations do not expose persistent_actor_id or hidden response coefficients.
9. Fixture thresholds and temperament values remain non-canon.

## Canon status

PROPOSED. No Fletchling temperament, habituation rate, sensitization rate, stimulus threshold or long-term welfare rule is approved by this contract.