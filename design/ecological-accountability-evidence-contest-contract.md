# Ecological accountability evidence-contest contract

Status: PROPOSED IMPLEMENTATION CONTRACT. No canon effect.
Pass: 278

Purpose

Define how Ouros records disagreement about the evidence used to evaluate a delegated ecological obligation without duplicating ecological truth, inventing bad faith or creating a second adjudication system.

This contract sits between Pass 277 accountability observations and the existing generic adjudication/review layer. It can produce a structured evidence-review packet. It does not itself create appeal rights, stays, hearings, remedies or jurisdiction.

Core record

```yaml
ECOLOGICAL_ACCOUNTABILITY_EVIDENCE_CONTEST_V1:
  contest_id: null
  delegation_ref: null
  accountability_observation_ref: null
  challenged_interpretation_ref: null
  challenger_ref: null
  reviewer_ref: null
  obligation_ref: null
  ecological_claim_refs: []
  process_claim_refs: []
  evidence_refs: []
  disputed_evidence_refs: []
  missing_expected_evidence_refs: []
  method_profile_refs: []
  semantic_window_refs: []
  provenance_chain_refs: []
  comparability_assessment: UNKNOWN
  independence_assessment: UNKNOWN
  detectability_or_visibility_refs: []
  confounder_refs: []
  alternative_interpretation_refs: []
  requested_followup_refs: []
  review_disposition: REVIEW_PENDING
  downstream_decision_matter_ref: null
  canon_status: proposed
```

Interpretation record

```yaml
ECOLOGICAL_ACCOUNTABILITY_INTERPRETATION_V1:
  interpretation_id: null
  contest_ref: null
  author_ref: null
  evidence_scope_refs: []
  method_scope_refs: []
  claim_scope: null
  confidence_class: UNKNOWN
  supports_process_compliance: UNKNOWN
  supports_ecological_outcome: UNKNOWN
  limitations: []
  supersedes_interpretation_ref: null
  superseded_by_interpretation_ref: null
  provenance_refs: []
```

Permitted review dispositions

`REVIEW_PENDING`: evidence has been challenged but no review disposition exists.

`EVIDENCE_SUFFICIENT_FOR_NARROW_PROCESS_FINDING`: the surviving record is adequate for the exact process obligation under review. This does not prove ecological success.

`EVIDENCE_INSUFFICIENT_FOR_PROCESS_FINDING`: available evidence cannot support the requested process conclusion. This does not prove noncompliance.

`METHODS_NOT_COMPARABLE`: observations use materially different method, effort, semantic window, visibility/detectability context or scope.

`INDEPENDENCE_NOT_ESTABLISHED`: apparently separate evidence is not sufficiently independent to count as corroboration.

`ALTERNATIVE_INTERPRETATIONS_REMAIN_PLAUSIBLE`: more than one interpretation remains compatible with the record.

`EVIDENCE_REMAINS_INCONCLUSIVE`: review cannot resolve the issue from surviving evidence.

`FOLLOWUP_OBSERVATION_AUTHORIZED`: the governing authority has validly authorized a bounded new observation. The contest itself cannot create that authority.

`INTERPRETATION_SUPERSEDED_BY_STRONGER_RECORD`: a later interpretation has stronger evidence and becomes current for its scope while the old interpretation remains historical.

Hard invariants

`EVIDENCE_CONTEST != ECOLOGICAL_TRUTH_DUPLICATION`

`DISAGREEMENT != BAD_FAITH`

`CHALLENGE_FILED != ORIGINAL_FINDING_INVALID`

`REVIEW_OPENED != DELEGATION_STAYED`

`MISSING_EVIDENCE != NONCOMPLIANCE_PROVEN`

`PROCESS_COMPLIANCE != ECOLOGICAL_SUCCESS`

`ECOLOGICAL_SUCCESS != PROCESS_COMPLIANCE`

`METHOD_DIFFERENCE != OBSERVER_ERROR`

`LATER_BETTER_EVIDENCE != EARLIER_MISCONDUCT`

`REPEATED_OBSERVATION != INDEPENDENT_CORROBORATION`

`REVIEWER_INTERPRETATION != CANONICAL_WORLD_TRUTH`

`INCONCLUSIVE != TIE_BROKEN_BY_AUTHORITY`

`APPEAL_OR_REVIEW_RIGHT != IMPLIED_BY_THIS_CONTRACT`

`MINECRAFT_PRESENTATION != EVIDENCE_AUTHORITY`

`BATTLE_OUTCOME != ACCOUNTABILITY_FINDING`

Creation gate

A contest requires:

- a valid Pass 277 delegation/accountability reference;
- an exact interpretation or accountability conclusion being challenged;
- identified evidence or an explicitly missing expected record;
- a bounded obligation and semantic window;
- provenance sufficient to determine what the evidence actually represents;
- no assumption that the challenger, reviewer or delegate has powers not granted elsewhere.

Evidence dimensions

Review must preserve at least these dimensions when relevant:

- who collected the observation;
- who interpreted it;
- whether the same observer or source was reused;
- collection method;
- effort or duration;
- semantic time/window;
- site and geographic scope;
- visibility/detectability context;
- instrument or data-source version;
- chain of provenance;
- whether a required record is absent or merely unavailable to the reviewer;
- whether later evidence is genuinely comparable;
- whether ecological conditions changed between observations.

Process and ecology separation

The contest can conclude that a required inspection log exists and satisfies the authored reporting standard while the ecological effect remains unknown.

It can also conclude that the ecological observation is credible while a process obligation was missed.

These states must remain separate and feed their owning contracts independently.

Interpretation lineage

Do not edit a historical interpretation in place when a later review reaches a different conclusion. Create a new interpretation and link it with `supersedes_interpretation_ref` / `superseded_by_interpretation_ref`.

The historical record must still show what evidence was available at the time and why the earlier interpretation was reasonable, unreasonable or unresolved according to the later review.

Escalation boundary

If a canon institution permits a formal review, stay, hearing, appeal, remand, reversal or remedy, create or link a `decision_matter` in `design/adjudication-hearing-decision-review-continuity-extension.md`.

This contract supplies the evidence packet only.

It must never infer:

- that review permission exists;
- that the challenged action is stayed;
- that a reviewer outranks the original decision-maker;
- that the delegate must be suspended;
- that a remedy is owed;
- that a finding is reversed.

Pass 277 integration

A supported process finding may update a Pass 277 accountability observation only through the Pass 277 state machine and its valid authority source.

For example:

- `EVIDENCE_SUFFICIENT_FOR_NARROW_PROCESS_FINDING` may support returning a corrected record to `ACTIVE_WITH_OBLIGATIONS` when the governing instrument permits it;
- `EVIDENCE_INSUFFICIENT_FOR_PROCESS_FINDING` may keep the matter in review rather than automatically producing `REVOKED`;
- `EVIDENCE_REMAINS_INCONCLUSIVE` cannot fabricate either compliance or noncompliance.

Ecology integration

Ecological claims remain owned by the relevant observation, population, recovery, disturbance or interaction contract. A governance reviewer cannot turn a field report into abundance truth, disappearance, recovery, avoidance, competition or habitat quality by institutional fiat.

Minecraft/Cobblemon projection

The adapter may display already-authorized review state through notices, report books, inspection markers, NPC dialogue or UI. It cannot infer evidence validity from entity presence, block state, inventory, scoreboard, chat text or visible completion of a quest objective.

Reduced encounter profile

Requires persistent Ouros evidence/provenance records, semantic time, Pass 277 accountability state and Minecraft/Cobblemon presentation. No AutoPTU handoff is required.

Mechanically rich profile

If a dispute escalates into a structured encounter, the permanent capability gates apply exactly:

- targeting/footprints/range/LoS for tactical selection;
- base movement legality for ordinary traversal;
- complete movement for push/pull/knockback/interception/forced movement;
- core calculations for adopted deterministic PTU arithmetic;
- action economy/initiative for structured sequencing;
- full turn/round lifecycle for phase-spanning interactions;
- full stateful damage pipeline for persistent damage;
- status lifecycle for persistent conditions;
- terrain/weather/hazards/zones/reactions for corresponding mechanics;
- move-specific behavior, abilities, items and Trainer Features/perks only through verified paths;
- AI legal-action infrastructure for legal option generation;
- AI tactical policy for autonomous confrontation/withdrawal/enforcement choices;
- Minecraft/Cobblemon/Craftics adapter/playback for live projection.

An audit, complaint, evidence challenge or adverse finding creates none of those mechanics.

Canon effect

None. No canon appeal body, reviewer, steward, institution, right, sanction, Fletchling behavior, ecological result or Marea/Sendero governance rule is created.