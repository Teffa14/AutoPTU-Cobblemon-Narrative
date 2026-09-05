# Ecological resilience early-warning contract

Status: PROPOSED IMPLEMENTATION CONTRACT. No canon effect.
Pass: 274

## Purpose

Extend Pass 273 from retrospective regime-transition evidence into prospective but explicitly uncertain resilience monitoring.

## Record

```yaml
ECOLOGICAL_RESILIENCE_EARLY_WARNING_V1:
  case_id: null
  focal_scope_ref: null
  response_dimension: null
  reference_state_ref: null
  semantic_windows: []
  comparison_refs: []
  detectability_refs: []
  disturbance_refs: []
  candidate_signals: []
  noise_model_notes: []
  false_positive_checks: []
  confounder_refs: []
  evidence_refs: []
  disposition: DESCRIPTIVE_VARIABILITY_ONLY
  uncertainty_notes: []
  canon_status: proposed
```

## Dispositions

`DESCRIPTIVE_VARIABILITY_ONLY`: a response varies but there is no supported resilience inference.

`EARLY_WARNING_PATTERN_CANDIDATE`: one or more candidate warning metrics change across valid semantic windows.

`FALSE_POSITIVE_RISK_HIGH`: method, noise, detectability, sampling, seasonality, or comparison quality can plausibly create the pattern.

`RESILIENCE_LOSS_SIGNAL_SUPPORTED_NARROWLY`: repeated, comparable observations support a local warning signal after material false-positive checks. This remains probabilistic evidence.

`SIGNAL_NOT_SUPPORTED`: adequate comparison fails to reproduce the candidate pattern.

`INCONCLUSIVE`: evidence exists but cannot separate the candidate signal from alternatives.

`CLOSED_HISTORICAL`: monitoring ended; history remains queryable.

## Hard invariants

`RISING_VARIANCE != COLLAPSE_PREDICTION`

`RISING_AUTOCORRELATION != CRITICAL_THRESHOLD_CONFIRMED`

`SLOWER_RECOVERY != HYSTERESIS`

`EARLY_WARNING_SIGNAL != FUTURE_REGIME_TRANSITION`

`NO_SIGNAL != SYSTEM_SAFE`

`ONE_METRIC != RESILIENCE_STATE`

`VISIBLE_PATCHINESS != ECOLOGICAL_THRESHOLD`

`LOCAL_SIGNAL != SPECIES_GLOBAL_RULE`

`MINECRAFT_PRESENTATION != ECOLOGICAL_AUTHORITY`

`RESTART != SEMANTIC_TIME_ADVANCE`

## Promotion gate

`RESILIENCE_LOSS_SIGNAL_SUPPORTED_NARROWLY` requires multiple valid semantic windows, a declared reference, adequate Pass 271 comparison/detectability quality, explicit handling of known seasonality and disturbance, at least one false-positive check, and scope limited to the tested response/location/window.

A warning disposition can never directly promote Pass 273 `REGIME_TRANSITION_SUPPORTED_NARROWLY` or `HYSTERESIS_SUPPORTED_NARROWLY`. Those require their own retrospective evidence gates.

## Candidate signals

Candidate signals may include slower recovery after comparable small perturbations, changing variance, changing temporal autocorrelation, changing spatial structure, or other source-backed metrics. Each metric must declare method and assumptions. No metric is globally privileged.

## Player-facing rule

Presentation should communicate graded concern and uncertainty. UI/NPC language may say evidence suggests reduced resilience or warrants closer monitoring. It must not claim a collapse is certain or scheduled.

## Reduced encounter profile

Needs Ouros persistence, semantic horizons, Pass 271 controlled comparison/detectability, Pass 272 recovery trajectories where used, observation provenance, and Minecraft/Cobblemon presentation of authorized sources. No AutoPTU tactical family is required.

## Mechanically rich profile

Targeting/footprints/range/LoS applies only to tactical detection/selection. Base movement legality covers ordinary traversal. Push/pull/knockback/interception/forced movement require complete movement. Adopted PTU arithmetic uses core calculations. Structured sequences use action economy/initiative and full turn/round lifecycle where phase-spanning state exists. Persistent damage requires full stateful damage pipeline; persistent conditions require status lifecycle. Tactical environment effects require terrain/weather/hazards/zones/reactions. Exact Moves, Abilities, Items, and Trainer Features/perks require their own verified paths. AI legal-action infrastructure can enumerate legal choices; autonomous risk response requires AI tactical policy. Live execution requires Minecraft/Cobblemon/Craftics adapter/playback support.

No warning signal may synthesize a PTU hazard, reaction, terrain modifier, delayed effect, forced movement, damage, status, Ability trigger, Item effect, or Trainer Feature interrupt.

## Canon effect

None. No Marea/Sendero resilience decline, threshold, collapse, species behavior, or PTU mechanic is established by this contract.
