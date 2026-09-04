# Ecology pressure to Cobblemon projection envelope contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Pass: 248
Canon effect: NONE

## Purpose

Translate persistent ecological state into conditional Cobblemon presentation eligibility without letting visibility mutate population truth.

## Authority flow

persistent population/member state
→ local ecological pressures and context
→ projection envelope evaluation
→ selection from already-counted sources
→ Pass 239 lease reservation
→ Cobblemon materialization
→ visible behavior/observation

The projection layer never creates or removes a population member.

## Projection envelope

Minimum proposed fields:

population_id
species_id
eligible_microhabitats
activity_windows
search_radius_band
visibility_band
candidate_limit
context_revision
reason_codes

The envelope is a presentation eligibility result. It is not a spawn table and it is not a demographic forecast.

## Inputs

A policy evaluator may consume:

resource_pressure
disturbance_pressure
habituation state
time and season
weather/light context
microhabitat condition
nesting/parental role
migration state
individual temperament/history
current lease locks
adapter capacity

Every input must already belong to Ouros persistent state or an explicitly accepted environmental observation. Minecraft entity count is not an ecological input.

## Required separations

Population total changes only through the Pass 238 demographic ledger.

Visibility changes only presentation eligibility. A larger eligible area or longer activity window cannot increment abundance.

Short displacement caused by disturbance remains behavior/projection unless an explicit ecological event establishes emigration or relocation.

Search-radius expansion is not migration.

A lower candidate limit is not mortality.

An absent projection candidate is not evidence that the population is absent.

## Pressure responses

Resource scarcity may propose wider search, different activity windows, alternate eligible microhabitats or lower concentration at one patch.

Disturbance may propose sheltered microhabitats, quieter activity windows, reduced exposure or temporary withdrawal from a presentation surface.

These are species-policy outputs, not universal constants. Fixture thresholds must never be promoted to canon automatically.

## Candidate selection

Every candidate must bind to an already-counted source class from Pass 239:

PERSISTENT_MEMBER
UNRESOLVED_POOL_SLOT
TRANSIENT_COHORT_MEMBER
EXTERNAL_ASSOCIATED_INDIVIDUAL

For resident wild population projection, a candidate reservation must reference either a persistent member or one unresolved pool slot already included in population total.

candidate_limit constrains simultaneous presentation only.

## Existing actor continuity

If policy changes while a valid actor is materialized, Ouros may let that same actor move into a newly eligible microhabitat or become less exposed. The persistent member ID and lease source remain unchanged.

Minecraft UUID remains correlation data only.

## Observation boundary

Pass 240 receives sightings and observable behavior. It does not receive projection thresholds, hidden pressure values, unresolved slot tokens or population totals unless another authorized measurement surface exposes them.

A failure to sight an actor under a REDUCED visibility band does not prove absence.

## Reduced version

The Pass 248 fixture keeps the canon Sendero Fletchling population at 12. Resource pressure expands eligible search space and activity windows. A later disturbance spike reduces exposure and rejects a previously eligible edge presentation. Recovery restores the baseline envelope. No battle is required.

Dependencies:

Minecraft/Cobblemon/Craftics adapter/playback: REQUIRED for actual materialization and visible behavior; PARTIAL/BLOCKING end-to-end.

All battle capability families: NOT REQUIRED for the reduced version.

## Rich version

If a player actively follows, corners, blocks or intercepts a pressure-displaced Pokémon, the encounter may cross the Pass 242 handoff boundary.

Dependency classification when those mechanics are authored:

targeting/footprints/range/LoS: REQUIRED for structured target geometry; VERIFIED within audited contracts.
base movement legality: REQUIRED; VERIFIED within audited contracts.
complete movement including push/pull/knockback/interception/forced movement: REQUIRED for interception/forced access; PARTIAL.
core calculations: REQUIRED for adopted tactical checks/damage; VERIFIED within audited contracts.
action economy/initiative: REQUIRED for structured turns; VERIFIED within audited contracts.
full turn/round lifecycle: REQUIRED for timed pursuit or phase objectives; PARTIAL.
full stateful damage pipeline: REQUIRED only if damaging attacks occur; PARTIAL.
status lifecycle: REQUIRED only if statuses occur; PARTIAL.
terrain/weather/hazards/zones/reactions: REQUIRED if those mechanics alter pursuit/access; MIXED/PARTIAL/BLOCKING outside verified slices.
move-specific behavior: validate each Move; family PARTIAL.
abilities: validate each Ability; family PARTIAL.
items: validate each Item; family PARTIAL.
Trainer Features/perks: validate each Feature; family PARTIAL.
AI legal-action infrastructure: REQUIRED for tactical wildlife; VERIFIED within audited contracts.
AI tactical policy: REQUIRED for flee/search/guard/yield priorities; BLOCKING as a complete family.
Minecraft/Cobblemon/Craftics adapter/playback: REQUIRED end-to-end; PARTIAL/BLOCKING.

## Acceptance gates

1. Pressure changes can alter projection envelope without changing population total.
2. Every projected resident source is already counted.
3. Candidate limits never become abundance.
4. Existing persistent identity survives envelope changes.
5. Current microhabitat/activity policy gates new reservations.
6. Despawn/unload only changes lease/presentation state.
7. Server restart preserves ecology truth and invalidates unsafe entity correlations without deleting members.
8. Observation does not expose hidden pressure or projection internals.
9. Fixture-only thresholds remain non-canon.

## Canon status

PROPOSED.

This contract changes no species availability, actual abundance, physical resource identity, PTU rule or approved encounter outcome.
