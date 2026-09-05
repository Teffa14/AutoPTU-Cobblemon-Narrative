# Ecological management decision-governance contract

Status: PROPOSED IMPLEMENTATION CONTRACT. No canon effect.
Pass: 275

## Purpose

Convert ecological evidence, including Pass 274 early-warning signals, into transparent and revisable management choices without treating ecological knowledge as an automatic policy command.

## Record

```yaml
ECOLOGICAL_MANAGEMENT_DECISION_V1:
  decision_id: null
  focal_scope_ref: null
  evidence_refs: []
  evidence_disposition_refs: []
  decision_owner_ref: null
  objective_profile_ref: null
  risk_posture_ref: null
  available_action_refs: []
  selected_action_ref: null
  decision_threshold_ref: null
  ecological_threshold_ref: null
  utility_threshold_ref: null
  critical_uncertainty_refs: []
  value_of_information_notes: []
  monitoring_plan_ref: null
  action_cost_notes: []
  reversibility_class: null
  semantic_review_horizon_ref: null
  rollback_conditions: []
  reassessment_conditions: []
  provenance_refs: []
  disposition: EVIDENCE_REVIEW_PENDING
  uncertainty_notes: []
  canon_status: proposed
```

## Dispositions

`EVIDENCE_REVIEW_PENDING`: evidence exists but has not yet been translated into a decision context.

`OBJECTIVES_DECLARED`: the decision owner and objectives are explicit.

`ALTERNATIVES_DECLARED`: feasible actions and known costs/tradeoffs are explicit.

`MONITORING_BEFORE_ACTION`: a decision-critical uncertainty is judged reducible within the relevant horizon and monitoring is selected before intervention.

`PRECAUTIONARY_ACTION_SELECTED`: a bounded action is selected despite residual uncertainty because the stated objective/risk posture gives greater weight to plausible downside from delay.

`ACTION_SELECTED`: a non-precautionary management action is selected under the declared objective and evidence.

`DEFERRED_WITH_REVIEW`: no immediate intervention is selected, but a semantic review horizon and trigger are explicit.

`REASSESSMENT_REQUIRED`: evidence, objectives, costs or world state changed enough that the current choice must be re-evaluated.

`ACTION_REVERSED_OR_EXPIRED`: a temporary action was rolled back, expired or replaced; history remains queryable.

`INCONCLUSIVE_DECISION_CONTEXT`: evidence may be adequate but objectives, authority or feasible alternatives are not sufficiently specified.

## Hard invariants

`ECOLOGICAL_SIGNAL != POLICY_COMMAND`

`ECOLOGICAL_THRESHOLD != DECISION_THRESHOLD`

`DECISION_THRESHOLD != UTILITY_THRESHOLD`

`UNCERTAINTY != AUTOMATIC_INACTION`

`UNCERTAINTY != AUTOMATIC_RESTRICTION`

`RISK_POSTURE != ECOLOGICAL_TRUTH`

`STAKEHOLDER_DISAGREEMENT != DATA_CONTRADICTION`

`MORE_MONITORING != BETTER_DECISION`

`LOW_VALUE_INFORMATION != REQUIRED_PROGRESS`

`TEMPORARY_ACTION != PERMANENT_CANON_STATE`

`MINECRAFT_BARRIER != PTU_TERRAIN_RULE`

`MINECRAFT_SIGNAGE != TRAINER_FEATURE`

`RESTART != REVIEW_HORIZON_ADVANCE`

## Decision-threshold separation

An ecological threshold describes a property or transition in the ecological system when supported by the relevant ecological contract.

A utility threshold describes a value judgement embedded in an objective.

A decision threshold describes when a selected action changes under the current objectives, alternatives, models, uncertainty and risk posture.

They may reference the same measured variable but must remain separately identified and separately sourced.

## Objective and risk profiles

Two authorized decision owners may consume the same evidence and select different actions if their objectives, legal responsibilities, costs or risk postures differ. Ouros records the disagreement as governance state. It does not duplicate ecological truth.

A risk posture must be scoped to a decision context. It cannot become a species trait, PTU stat or universal personality label.

## Monitoring gate

Monitoring before action should identify at least one `critical_uncertainty_ref` and explain how resolving it could change the selected action.

A monitoring plan should declare:

- measurement or observation target;
- semantic window;
- method and detectability assumptions where applicable;
- cost or opportunity cost;
- expected decision impact;
- stop/review condition.

If the information cannot plausibly change the decision before the decision horizon closes, it may still be archived as research but must not be treated as mandatory gating work.

## Precautionary action gate

`PRECAUTIONARY_ACTION_SELECTED` requires:

- a declared decision owner with authority for the proposed action;
- explicit objective and risk posture;
- at least one source-backed evidence record establishing a plausible scoped concern;
- explicit acknowledgement of unresolved uncertainty;
- bounded action scope;
- known or estimated costs/tradeoffs;
- reversibility class;
- semantic review horizon;
- rollback or reassessment condition.

The gate does not require Pass 274 `RESILIENCE_LOSS_SIGNAL_SUPPORTED_NARROWLY` specifically. Other authorized evidence may justify precaution. Conversely, a supported warning does not force precaution.

## Reversibility classes

`EASILY_REVERSIBLE`: expected rollback is routine and does not itself create persistent ecological state.

`REVERSIBLE_WITH_COST`: rollback is available but has meaningful social, logistical or ecological cost.

`PARTIALLY_REVERSIBLE`: some consequences may persist after rollback.

`IRREVERSIBLE_OR_UNKNOWN`: the action cannot confidently be restored to baseline; stronger approval and evidence should be expected by downstream governance systems.

These classes describe decision planning and do not author ecological recovery outcomes. Passes 272–273 remain authoritative for recovery, regime transition and hysteresis evidence.

## Reduced encounter profile

Needs Ouros persistence, semantic horizons, provenance, observation/knowledge state, existing ecological evidence contracts and Minecraft/Cobblemon presentation. No AutoPTU tactical family is required.

## Mechanically rich profile

Targeting/footprints/range/LoS applies if an intervention needs tactical detection or selection. Base movement legality covers ordinary traversal. Push/pull/knockback/interception/forced movement require complete movement. PTU calculations require core calculations. Structured action sequencing uses action economy/initiative and full turn/round lifecycle as applicable. Damage-bearing interventions require full stateful damage pipeline; persistent conditions require status lifecycle. Mechanical environmental effects require terrain/weather/hazards/zones/reactions. Exact Moves, Abilities, Items and Trainer Features/perks require their own verified paths. AI legal-action infrastructure can enumerate legal actions. Autonomous tactical choice requires AI tactical policy. Live representation requires Minecraft/Cobblemon/Craftics adapter/playback support.

A governance decision can authorize a future tactical encounter but cannot synthesize missing battle semantics.

## Canon effect

None. No Sendero institution, access restriction, law, ecological decline, stakeholder objective, risk posture or intervention is established as canon by this contract.
