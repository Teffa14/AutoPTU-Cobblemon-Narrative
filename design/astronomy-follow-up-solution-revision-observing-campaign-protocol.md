# Astronomy Follow-Up, Solution Revision & Observing Campaign Protocol

Status: PROPOSED PROTOCOL. Not canon.
Pass: 170
Authority: subordinate extension of Pass 63 `astronomy-celestial-observation-layer.md`.

## Scope

Pass 63 remains the sole astronomy authority. This protocol deepens four areas without replacing its objects: multi-site observing campaigns, candidate/transient follow-up, versioned solution/ephemeris revision, and explicit coverage/non-detection provenance.

It does not own celestial events, observatories, instruments, meteor recovery, Pokémon behavior, clocks, weather, light pollution, calibration, science publications or cultural meaning; those remain with Pass 63 and the authorities it already names.

## Evidence chain

`Pass-63 CELESTIAL_EVENT / target claim -> observing campaign -> session coverage -> raw observation -> candidate linkage -> follow-up request -> additional observations -> SOLUTION_REVISION -> visibility/prediction revision -> Science/public handoff`

No step implies the next automatically.

## OBSERVING_CAMPAIGN_REVISION

```yaml
observing_campaign_revision:
  campaign_id: null
  predecessor_revision_ref: null
  target_or_event_refs: []
  participating_observatory_ids: []
  method_revision_refs: []
  requested_windows: []
  priority_reason_ref: null
  coverage_goal_ref: null
  public_participation_policy_ref: null
  created_at: null
```

A campaign may add or remove sites without creating a new celestial event.

## SESSION_COVERAGE_RECORD

```yaml
session_coverage_record:
  session_or_observation_ref: null
  planned_window_ref: null
  achieved_time_coverage_ref: null
  achieved_sky_coverage_ref: null
  weather_limit_refs: []
  lightscape_limit_refs: []
  instrument_limit_refs: []
  timekeeping_quality_ref: null
  completeness_state: null
```

Allowed states include COMPLETE_FOR_SCOPE, PARTIAL, WEATHER_BLOCKED, LIGHT_LIMITED, EQUIPMENT_FAILURE, TIME_REFERENCE_PROBLEM, NOT_ATTEMPTED and UNKNOWN.

`NOT_DETECTED` is interpretable only together with this record.

## CANDIDATE_LINKAGE_ASSESSMENT

```yaml
candidate_linkage_assessment:
  assessment_id: null
  source_observation_ids: []
  candidate_target_ref: null
  comparison_target_refs: []
  source_dependency_refs: []
  assessment_state: UNRESOLVED
  rationale_ref: null
  supersedes_assessment_ref: null
```

Possible outcomes: CORROBORATED, EXISTING_TARGET, ARTIFACT_POSSIBLE, DUPLICATE_REPORT, SPLIT_REQUIRED, MERGE_REQUIRED, INSUFFICIENT_EVIDENCE, UNRESOLVED.

Several reports derived from the same photograph or alert are not independent corroboration.

## FOLLOW_UP_REQUEST

```yaml
astronomy_follow_up_request:
  request_id: null
  celestial_or_candidate_ref: null
  issued_at: null
  requested_window_ref: null
  requested_method_ref: null
  requested_precision_or_quality_ref: null
  destination_site_ids: []
  response_observation_ids: []
  result_state: OPEN
```

A failed follow-up can mean cloud, target faintness, equipment failure, bad prediction, insufficient coverage or true non-recovery. Do not collapse them.

## SOLUTION_REVISION

```yaml
astronomy_solution_revision:
  solution_revision_id: null
  pass63_target_or_event_ref: null
  predecessor_revision_ref: null
  included_observation_ids: []
  excluded_observation_ids: []
  method_revision_ref: null
  reference_epoch_ref: null
  derived_parameters_ref: null
  uncertainty_summary_ref: null
  valid_scope_ref: null
  supersedes_for_current_use: []
  created_at: null
```

The project may keep `derived_parameters_ref` qualitative. Exact orbital simulation is not required for narrative value.

A later solution can substantially change a prediction without making the earlier publication fraudulent or retroactively impossible.

## VISIBILITY_OUTCOME

Tie a Pass-63 prediction to a local outcome:

```yaml
visibility_outcome:
  prediction_ref: null
  site_ref: null
  session_ref: null
  outcome: null
  observation_refs: []
  explanation_refs: []
```

Candidate outcomes: OBSERVED_AS_PREDICTED, OBSERVED_WITH_DIFFERENCE, NOT_DETECTED_GOOD_COVERAGE, COVERAGE_INCOMPLETE, WEATHER_BLOCKED, LIGHTSCAPE_LIMITED, EQUIPMENT_FAILURE, TIME_REFERENCE_PROBLEM, NOT_ATTEMPTED.

Prediction accuracy and local visibility remain separate.

## Multi-observatory disagreement

When sites disagree, preserve each raw record and inspect:

- Timekeeping correction;
- Metrology/calibration state;
- local weather/cloud;
- Lightscapes/horizon obstruction;
- instrument/method differences;
- coverage overlap;
- source dependence;
- target-linkage hypothesis.

Valid outcomes include one site being wrong, both being correct about different targets, both being incomplete, or UNRESOLVED.

## Meteor versus meteorite

Pass 63 already owns the astronomy-side meteor/fall record. This protocol adds only a linkage assessment between an observed fall solution and a later terrestrial candidate. Geology/Material Culture/Museums determine the physical object. Location inside a predicted search area never authenticates it automatically.

## Public/cultural handoff

A revised scientific prediction may trigger updates in Media, Public Events, Sacred Sites or Public Memory. Those systems preserve what people were told and believed at each time. Astronomy revisions do not rewrite earlier public behavior.

## Pokémon guardrails

Official Minior lore supports authored falling/high-altitude observations. Official Lunatone lore supports a possible authored lunar-phase behavioral study. Neither creates a global celestial mechanic.

Never infer:

- meteor = Minior;
- full moon = Lunatone spawn or stat modifier;
- celestial prediction = Pokémon appearance;
- Psychic/Occult Education = astronomy expertise;
- `Gravity`, `Moonlight`, `Meteor Mash`, `Comet Punch` or similarly named mechanics = world astronomy.

## Minecraft boundary

Pass 63 remains authoritative over sky-event state. Minecraft may render a scheduled presentation. Vanilla moon phase, shader state, particles, tick time or client sky texture cannot create, confirm or measure an Ouros celestial event.

## Long-term Chronicle use

Prefer revision and baseline over spectacle:

- the same shower observed for twenty years;
- an observatory whose time reference was later reconstructed;
- a candidate object merged into an older catalog identity;
- a community station filling a flagship-site weather gap;
- a quiet season later useful as baseline;
- a public alert revised after follow-up;
- an old plate becoming valuable under a newer solution.

## Mechanical boundary

This protocol creates no Weather, Terrain, Gravity, Moonlight healing, eclipse Status, meteor damage, cosmic buffs, evolution triggers, Legendary spawns, telescope Item effects, Accuracy/Initiative modifiers or capture modifiers.

Battle dependencies remain encounter-specific and are documented in the Pass 170 engine snapshot.