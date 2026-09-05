# Ecological recovery trajectory contract

Status: PROPOSED IMPLEMENTATION CONTRACT. No canon effect.
Pass: 272

## Purpose

Represent what happens after an ecologically relevant pressure ends without treating cessation, apparent normality, or elapsed runtime as recovery. This contract extends Pass 271 controlled comparison and remains separate from population authority and PTU state.

## Record

```yaml
ECOLOGICAL_RECOVERY_TRAJECTORY_V1:
  trajectory_id: null
  causal_claim_ref: null
  disturbance_ref: null
  focal_scope_ref: null
  cessation:
    event_ref: null
    semantic_epoch: null
    authority_ref: null
    verified: false
  reference_state:
    reference_id: null
    provenance_refs: []
    comparison_method_ref: null
    dimensions: []
  assessment_windows: []
  response_dimensions: []
  secondary_pressure_refs: []
  evidence_refs: []
  confounder_refs: []
  recovery_disposition: RECOVERY_ASSESSMENT_PENDING
  uncertainty_notes: []
  canon_status: proposed
```

Each `response_dimension` records its own variable, reference band or qualitative reference class, current evidence, detectability context, trajectory disposition, and semantic assessment horizon. Population size is never reconstructed from these dimensions.

## Dispositions

`DISTURBANCE_ACTIVE`: authoritative evidence says the focal pressure has not ceased.

`CESSATION_CONFIRMED`: the pressure ended through an authoritative event; no recovery claim follows automatically.

`RECOVERY_ASSESSMENT_PENDING`: the next valid semantic assessment window has not supplied enough evidence.

`RECOVERY_LAG_OBSERVED`: a response remains outside its reference band after verified cessation, without evidence sufficient to diagnose a persistent alternative state.

`RECOVERING_TOWARD_REFERENCE`: repeated comparable evidence supports movement toward the declared reference for that dimension.

`RECOVERED_WITHIN_REFERENCE_BAND`: the dimension meets its predeclared recovery criterion across the required assessment evidence. This does not recover other dimensions.

`PERSISTENT_SHIFT_HYPOTHESIS`: the response remains materially shifted after cessation and ordinary lag remains an insufficient explanation, but hysteresis has not been demonstrated.

`HYSTERESIS_HYPOTHESIS`: evidence supports history-dependent or asymmetric reversal as a plausible mechanism. This remains a hypothesis unless the project adopts a stronger evidentiary gate.

`SECONDARY_PRESSURE_SUSPECTED`: another active pressure plausibly explains delayed or altered return.

`CONFOUNDED`: the available comparison cannot separate material explanations.

`INCONCLUSIVE`: evidence is valid but does not resolve trajectory state.

`CLOSED_HISTORICAL`: active assessment ended while history and provenance remain queryable.

## Reference-state rule

A reference state is an evidence-backed comparison target, not a metaphysical pristine state. It may come from matched pre-disturbance observations or a justified comparator under Pass 271. Store ranges/classes and observation conditions where possible. Never invent a single perfect baseline value merely to make recovery computable.

## Cessation rule

`DISTURBANCE_ENDED != ECOLOGY_RECOVERED`.

A cessation event must identify what pressure ended, who/what had authority to assert that fact, and the semantic epoch. Minecraft entity disappearance, block unload, restart, day/night rollover, or missing particles cannot create cessation.

## Dimension independence

Activity timing, site use, resource fraction, habitat structure, cue response, observable behavior, and any later adopted ecological function recover independently. One recovered dimension cannot promote the whole trajectory.

Hard invariant: `ONE_DIMENSION_RECOVERED != SYSTEM_RECOVERED`.

## Lag and hysteresis gate

Persistence after cessation first supports lag or persistent-shift reasoning. Do not label hysteresis merely because the response has not returned yet.

A `HYSTERESIS_HYPOTHESIS` needs evidence beyond elapsed time, such as a different return path under comparable driver conditions, history dependence, plausible feedback maintaining the shifted state, or asymmetric forward/reversal thresholds. Multiple lines of evidence are preferred because similar patterns can arise from continuing pressures, slow demographic/ecological processes, poor detectability, or an invalid reference.

Hard invariants:

`PERSISTENCE_AFTER_CESSATION != HYSTERESIS_CONFIRMED`

`SOURCE_REMOVED != PRESSURE_ENDED` unless the source was itself the authoritative pressure representation.

`ONE_NORMAL_SIGHTING != RECOVERY`

`NONDETECTION != RECOVERY`

`VISIBLE_COUNT != POPULATION_SIZE`

`RUNTIME_TICKS != SEMANTIC_RECOVERY_TIME`

`RESTART != ASSESSMENT_ADVANCE`

## Secondary pressures

When a response fails to return, preserve competing explanations. A newly documented second pressure may move the trajectory to `SECONDARY_PRESSURE_SUSPECTED` or `CONFOUNDED`. Removing that second pressure still requires a new cessation event and new assessment windows; it does not retroactively prove the original explanation.

## Integration

Pass 271 owns comparison quality and narrow causal attribution. This contract consumes those records rather than weakening them.

Semantic-time/horizon contracts own when an assessment window becomes eligible. Chunk lifecycle and wall-clock runtime do not substitute.

Passes 262–264 own AutoPTU semantic aftermath and quarantine. Ecological observation of limping, resting, avoidance, or apparent injury cannot create HP loss, Injury, status, or another PTU fact.

Population ledgers remain authoritative for demography. Recovery evidence cannot add/remove individuals.

## Reduced encounter profile

A longitudinal field-research version requires Ouros persistence, semantic time, observation/provenance, controlled comparison, and Minecraft/Cobblemon presentation of already-authorized sources. No AutoPTU tactical family is required.

## Mechanically rich profile

Dependencies apply only when consumed: targeting/footprints/range/LoS for tactical detection/targeting; base movement legality for ordinary traversal; complete movement for push/pull/knockback/interception/forced movement; core calculations for adopted PTU arithmetic; action economy/initiative and full turn/round lifecycle for structured tactical sequencing; full stateful damage pipeline for persistent damage; status lifecycle for persistent status; terrain/weather/hazards/zones/reactions for admitted tactical environmental effects; move-specific behavior, abilities, items, and Trainer Features/perks only for exact mechanisms involved; AI legal-action infrastructure for legal autonomous options; AI tactical policy for choosing return/avoidance/contest strategies; Minecraft/Cobblemon/Craftics adapter/playback support for live representation and feedback.

## Canon effect

None. No Marea disturbance, recovery outcome, secondary pressure, reference site, species behavior, PTU mechanic, or Caelo rule becomes canon through this contract.