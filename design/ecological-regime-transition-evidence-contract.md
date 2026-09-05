# Ecological regime-transition evidence contract

Status: PROPOSED IMPLEMENTATION CONTRACT. No canon effect.
Pass: 273

## Purpose

Extend Pass 272 with an evidence gate for persistent ecological state change. This contract prevents slow recovery, continuing pressure, poor detectability, or a visually altered Minecraft site from being promoted automatically into an alternative stable state, regime transition, or hysteresis claim.

## Record

```yaml
ECOLOGICAL_REGIME_TRANSITION_EVIDENCE_V1:
  transition_case_id: null
  recovery_trajectory_ref: null
  focal_scope_ref: null
  response_dimensions: []
  reference_state_ref: null
  departure_path:
    driver_refs: []
    assessment_windows: []
    threshold_evidence_refs: []
  cessation_refs: []
  shifted_state:
    evidence_refs: []
    persistence_windows: []
    comparison_refs: []
  feedback_candidates: []
  return_path:
    intervention_refs: []
    assessment_windows: []
    asymmetry_evidence_refs: []
  secondary_pressure_refs: []
  confounder_refs: []
  detectability_refs: []
  evidence_refs: []
  regime_disposition: PERSISTENT_SHIFT_OBSERVED
  uncertainty_notes: []
  canon_status: proposed
```

## Dispositions

`PERSISTENT_SHIFT_OBSERVED`: a response remains outside its declared reference after verified cessation. This is descriptive evidence only.

`ALTERNATE_STATE_HYPOTHESIS`: a contrasting configuration persists across valid semantic windows and comparison quality is adequate, but maintaining mechanisms or return-path behavior remain unresolved.

`FEEDBACK_MECHANISM_SUPPORTED`: evidence supports a specific process capable of reinforcing the shifted configuration. This does not itself prove a regime transition.

`RETURN_PATH_ASYMMETRY_SUPPORTED`: comparable evidence shows that reversal/recovery does not retrace the departure path or requires materially different driver conditions/intervention.

`REGIME_TRANSITION_SUPPORTED_NARROWLY`: evidence supports a persistent contrasting configuration for the declared process/scope while ordinary lag and known continuing pressure are insufficient explanations. Scope remains local and dimension-specific.

`HYSTERESIS_SUPPORTED_NARROWLY`: the regime-transition gate is met and the case additionally has supported return-path asymmetry plus a plausible maintaining feedback. It remains bounded to the tested site/process/window.

`SECONDARY_PRESSURE_SUSPECTED`: another active process plausibly maintains the response.

`CONFOUNDED`: material alternatives cannot be separated.

`INCONCLUSIVE`: valid evidence exists but the stronger claim is not supported.

`CLOSED_HISTORICAL`: active assessment ended; evidence and inference history remain queryable.

## Promotion gates

A case cannot reach `REGIME_TRANSITION_SUPPORTED_NARROWLY` unless all of the following are true:

- the Pass 272 initiating-pressure cessation is authoritative;
- the relevant response dimension has a declared evidence-backed reference;
- multiple valid semantic assessment windows support persistence of a contrasting configuration;
- Pass 271 comparison/detectability quality is adequate for the claim;
- known secondary pressures and confounders are recorded and materially assessed;
- the claim is scoped to the tested process/location/window and does not globalize to a species or ecosystem.

A case cannot reach `HYSTERESIS_SUPPORTED_NARROWLY` unless the regime-transition gate is already met and both of these are supported:

- a specific maintaining feedback with provenance;
- return-path asymmetry under comparable driver conditions or asymmetric forward/reversal thresholds.

## Hard invariants

`SLOW_RECOVERY != HYSTERESIS`

`PERSISTENCE_AFTER_CESSATION != ALTERNATE_STABLE_STATE_CONFIRMED`

`ABRUPT_VISIBLE_CHANGE != CRITICAL_THRESHOLD_CONFIRMED`

`FEEDBACK_PLAUSIBLE != FEEDBACK_CAUSALITY_PROVED`

`RETURN_PATH_DIFFERENT != HYSTERESIS` without adequate comparison and feedback evidence.

`ONE_DIMENSION_SHIFTED != WHOLE_ECOSYSTEM_REGIME_SHIFT`

`LOCAL_REGIME_SUPPORT != SPECIES_GLOBAL_RULE`

`SUCCESSFUL_INTERVENTION != RETROSPECTIVE_PROOF_OF_ALL_CAUSES`

`VISIBLE_COUNT != POPULATION_SIZE`

`BLOCK_STATE != ECOLOGICAL_STATE`

`ECOLOGICAL_STATE != PTU_TERRAIN_SEMANTICS`

`RESTART != SEMANTIC_TIME_ADVANCE`

## Feedback evidence

Each feedback candidate records mechanism, affected response dimension, expected direction, source/provenance, observations consistent and inconsistent with it, competing explanations, and current support state.

Allowed support states are `PROPOSED`, `OBSERVATION_CONSISTENT`, `CONTROLLED_COMPARISON_SUPPORTED`, `SUPPORTED_NARROWLY`, `REJECTED`.

A positive feedback may be biotic, abiotic, or biotic-abiotic. The project must name the process. Generic labels such as `ecosystem stuck` or `habitat bad` are not mechanisms.

## Return-path evidence

The return path is evaluated with semantic windows, not runtime duration. A restoration or intervention must declare what driver or feedback it changes. Evidence that a stronger or qualitatively different intervention is needed for recovery can support asymmetry only when the departure and return conditions are sufficiently comparable under Pass 271.

If a second pressure remains active, prefer `SECONDARY_PRESSURE_SUSPECTED` or `CONFOUNDED` rather than hysteresis promotion.

## Integration

Pass 271 owns controlled comparison, detectability and narrow causal attribution. Pass 272 owns cessation, reference dimensions and recovery trajectory. Pass 261 semantic horizons own assessment eligibility. Population/demography contracts own abundance. Passes 262–264 own AutoPTU semantic aftermath and quarantine.

This contract may consume evidence from habitat engineering, resource pulses, cue-quality divergence, facilitation cascades, branch competition or resource partitioning, but it cannot rewrite those relations into a regime claim without its own gate.

## Reduced encounter profile

The reduced field-investigation version needs Ouros persistence, semantic horizons, observation/provenance, controlled comparison and Minecraft/Cobblemon presentation of already-authorized sources. It requires no AutoPTU tactical family.

## Mechanically rich profile

Dependencies apply only when the scene consumes them. Targeting/footprints/range/LoS covers tactical detection and target selection. Base movement legality covers ordinary traversal. Push/pull/knockback/interception/forced movement require complete movement. Adopted PTU arithmetic uses core calculations. Structured sequences require action economy/initiative and, when state spans phases, full turn/round lifecycle. Persistent damage needs full stateful damage pipeline; persistent conditions need status lifecycle. Tactical environmental effects require terrain/weather/hazards/zones/reactions. Exact Moves, Abilities, Items and Trainer Features/perks require their own verified paths. AI legal-action infrastructure can generate legal options; autonomous decisions about avoidance, contest, intervention or rerouting require AI tactical policy. Live world execution and feedback require Minecraft/Cobblemon/Craftics adapter/playback support.

No ecological regime claim may be used to synthesize an unverified PTU hazard, reaction, terrain modifier, weather phase, delayed effect, movement interaction, damage result or status.

## Canon effect

None. This contract defines an evidentiary gate only. It creates no Marea/Sendero regime transition, feedback, threshold, intervention, species behavior, population change, PTU mechanic or Caelo rule.
