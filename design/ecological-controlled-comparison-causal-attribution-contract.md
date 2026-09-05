# Ecological controlled comparison and causal-attribution contract

Status: PROPOSED IMPLEMENTATION CONTRACT. No canon effect.
Pass: 271

## Purpose

Add an ecology-specific protocol for testing causal interpretations of patterns already represented by Pass 270 and related ecology contracts. This layer complements, rather than replaces, the generic observation/evidence and investigation ledgers.

## Record

```yaml
ECOLOGICAL_CONTROLLED_COMPARISON_V1:
  comparison_id: null
  hypothesis_ref: null
  response_scope:
    process_ref: null
    species_or_source_refs: []
    response_variable: null
    partition_axis_ref: null
  focal_scope:
    site_ref: null
    before_windows: []
    after_windows: []
  comparator_scopes: []
  exposure:
    event_ref: null
    exposure_type: null
    started_at: null
    ended_at: null
    provenance_refs: []
  observation_protocol:
    method: null
    observer_refs: []
    effort_descriptor: null
    detectability_covariates: []
    known_method_limits: []
  evidence_refs: []
  confounder_refs: []
  comparator_validity: UNASSESSED
  detectability_assessment: UNASSESSED
  causal_disposition: DESCRIPTIVE_ONLY
  uncertainty_notes: []
  canon_status: proposed
```

## Dispositions

`DESCRIPTIVE_ONLY`: observations describe a pattern but do not test cause.

`REPEATED_PATTERN`: the pattern recurred under recorded observation conditions. Repetition alone does not establish a cause.

`COMPARATOR_INSUFFICIENT`: a causal comparison was attempted but comparator scope, baseline, detectability, exposure contrast or provenance is inadequate.

`CONTROLLED_COMPARISON_SUPPORTED`: focal and comparator evidence provide a materially stronger test of the hypothesis, while residual uncertainty remains explicit.

`CAUSAL_ATTRIBUTION_SUPPORTED_NARROWLY`: evidence supports the declared causal relation for the tested response, scope, exposure and time window. It does not globalize to the species, ecosystem or every outcome.

`CONFOUNDED`: a material alternative explanation cannot currently be separated from the proposed cause.

`INCONCLUSIVE`: the comparison is usable evidence but does not resolve the hypothesis.

## Detectability record

Each survey window that relies on detection/nondetection must retain enough context to judge whether absence is informative:

```yaml
detection_context:
  survey_window: null
  method: null
  effort_descriptor: null
  visibility_or_sensory_conditions: []
  observer_state_refs: []
  prior_detection_known_to_observer: false
  target_expected_detectability: null
  method_limitations: []
```

A nondetection is evidence about the survey result. It becomes evidence about ecological absence only through a supported inference that explicitly accounts for detection conditions.

Prior knowledge matters. If an observer has already located a source or learned its routine, later redetection can become easier. The evidence ledger must therefore preserve observer/source lineage rather than counting every sighting as independent corroboration.

## Comparator validity

A comparator does not need to be physically identical to the focal site. It does need a documented reason why it can inform the tested question.

Assess at least:

- comparable time/season window;
- relevant habitat/resource context;
- observation method and effort;
- exposure contrast;
- major disturbance/weather/context differences;
- source lineage and observer dependence;
- whether another active process plausibly changes the same response.

Possible states: `UNASSESSED`, `PLAUSIBLE`, `MATERIAL_MISMATCH`, `INVALID_FOR_QUESTION`.

## Before/after rule

A focal before/after change can be recorded immediately as a change. It does not become a causal result merely because an intervention happened between the two observations.

When feasible, strengthen inference by comparing the focal change with one or more valid comparator scopes observed across corresponding windows.

Multiple response variables remain independent. An intervention may alter temporal use while leaving abundance, spatial use or habitat condition unchanged.

## Hard invariants

`REPEATED_DETECTION != INDEPENDENT_CORROBORATION`

`NONDETECTION != ABSENCE`

`BEFORE_AFTER_CHANGE != INTERVENTION_CAUSED_CHANGE`

`COMPARATOR_UNCHANGED != AUTOMATIC_CAUSAL_PROOF`

`MATCHED_TIME != MATCHED_DETECTABILITY`

`VISIBLE_COUNT != POPULATION_SIZE`

`ONE_RESPONSE_CHANGED != ALL_RESPONSES_CHANGED`

`LOCAL_CAUSAL_SUPPORT != SPECIES_GLOBAL_RULE`

`PLAYER_EXPECTATION != DETECTION_INDEPENDENCE`

`MINECRAFT_ENTITY_NOT_VISIBLE != ECOLOGICAL_SOURCE_ABSENT`

## Integration with existing contracts

`observation-evidence-npc-knowledge-contract.md` owns observations, evidence, source chains and holder knowledge.

`investigation-inference-hypothesis-revision-continuity-extension.md` owns hypotheses, assumptions, inference edges and revision history.

`ecology-observation-intervention-contract.md` owns ecological interventions and delayed verification.

Pass 270 owns the independent spatial/temporal/resource partition axes.

This contract owns the comparison design and causal-disposition gate linking those records.

## Reduced encounter profile

A field-research version can run with Ouros persistence, semantic time, observation provenance and Minecraft/Cobblemon presentation of already-authorized sources. It requires no AutoPTU tactical family.

## Mechanically rich profile

Use the permanent capability categories only when the scene actually consumes them:

- targeting/footprints/range/LoS: active tactical detection/target selection;
- base movement legality: ordinary approach/rerouting;
- complete movement: push/pull/knockback/interception/forced movement;
- core calculations: mapped PTU arithmetic/checks;
- action economy/initiative: structured sequencing;
- full turn/round lifecycle: timed tactical state transitions;
- full stateful damage pipeline: persistent damage outcomes;
- status lifecycle: persistent status outcomes;
- terrain/weather/hazards/zones/reactions: admitted tactical environmental effects;
- move-specific behavior, abilities, items, Trainer Features/perks: only when those exact mechanisms drive the exposure or response;
- AI legal-action infrastructure: generating legal autonomous actions;
- AI tactical policy: choosing whether/when wildlife avoids, waits, contests, follows or changes route;
- Minecraft/Cobblemon/Craftics adapter/playback support: live projection, interaction and semantic feedback.

No observed schedule shift can substitute for verification of interception, reactions, weather phases, delayed effects or any other engine family.

## Canon effect

None. This contract defines evidence handling only. It does not establish a Marea disturbance, comparator site, species response, avoidance relation, competition relation, population change, PTU mechanic or Caelo rule.
