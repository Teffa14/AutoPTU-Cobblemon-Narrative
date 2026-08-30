# Investigation Inference, Hypothesis & Revision Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

Date introduced: 2026-08-30, Pass 152.

## Purpose

Ouros already preserves cases, evidence, observations, testimony, rumors, scientific work, archaeological interpretation, photography and puzzle clues. This extension preserves the reasoning history that connects those materials during a cross-domain investigation.

Its job is to answer:

1. What exact question is being investigated?
2. Which explanations have actually been proposed?
3. What discovered material supports, conflicts with or does not bear on each explanation?
4. Which assumptions connect evidence to a deduction?
5. How did a theory change when new information appeared?
6. Which part of the question was actually resolved, and which part remains open?

It does not calculate truth.

## Ownership boundaries

Case/Authority owns case identity, incident linkage, mandate, formal participation, evidence custody and institutional handling.

Rumor/Testimony owns informal claims, witness provenance, retellings, local knowledge and claim lineage.

Observation owns direct observations and actor knowledge records.

Science owns scientific research questions, measurements, scientific hypotheses and scientific claims.

Archaeology/Myth owns archaeological interpretation and sacred-site provenance.

Puzzle Persistent State owns puzzle mechanisms, puzzle state and clues that belong to those mechanisms.

Campaign Convergence owns long-arc pressure, convergence and payoff scheduling.

This extension owns cross-domain investigative reasoning records. It links existing objects. It does not replace their authority.

## 1. Investigation question

```yaml
investigation_question:
  question_id: null
  case_ref: null
  parent_question_id: null
  wording: null
  subject_refs: []
  scope_tags: []
  opened_at: null
  opened_by_actor_ids: []
  status: OPEN
  hypothesis_ids: []
  relevant_material_refs: []
  resolution_ids: []
  canon_status: proposed
```

Candidate statuses:

- OPEN
- PARTIALLY_ANSWERED
- ANSWERED_NARROWLY
- STALLED
- SUPERSEDED_BY_NARROWER_QUESTIONS
- CLOSED_INSUFFICIENT_EVIDENCE
- CLOSED_ACCEPTED_AMBIGUITY

A question should be narrow enough that an answer has meaning.

`Who was responsible for everything?` is usually a poor single question.

Better child questions can include:

- who was physically present;
- what happened first;
- which mechanism produced the observed effect;
- who knew about the event at a particular time;
- what motive an identified actor actually had;
- whether two incidents share a cause.

Splitting a question does not imply that the answers are related.

## 2. Hypothesis record

```yaml
investigation_hypothesis:
  hypothesis_id: null
  question_id: null
  proposition: null
  proposed_by_actor_ids: []
  created_at: null
  status: ACTIVE
  confidence_band: uncertain
  support_edge_ids: []
  conflict_edge_ids: []
  neutral_material_refs: []
  assumption_ids: []
  alternative_hypothesis_ids: []
  predecessor_hypothesis_ids: []
  successor_hypothesis_ids: []
  revision_event_ids: []
  does_not_establish: []
```

Suggested statuses:

- ACTIVE
- WEAKENED
- STRENGTHENED
- SPLIT
- MERGED
- REVISED
- DISPROVEN_NARROWLY
- WITHDRAWN_BY_PROPONENT
- SUPERSEDED
- UNRESOLVED

A hypothesis can be reasonable and still be wrong.

A hypothesis can also be partly right at one scope and wrong at another.

## 3. Inference edge

An inference edge records why an investigator thinks some material bears on a proposition.

```yaml
inference_edge:
  inference_id: null
  source_refs: []
  target_hypothesis_id: null
  relation: SUPPORTS
  scope: null
  reasoning_note: null
  assumption_ids: []
  authored_by_actor_ids: []
  created_at: null
  reviewed_state: UNREVIEWED
  provenance_refs: []
```

Candidate relations:

- SUPPORTS
- CONFLICTS_WITH
- NARROWS
- EXCLUDES_NARROWLY
- REQUIRES_CONTEXT
- EXPLAINS_PART
- IRRELEVANT_TO_THIS_PROPOSITION
- DUPLICATES_SOURCE_LINEAGE

The relation belongs to the reasoning record. It does not rewrite the underlying evidence or claim.

## 4. Assumption record

Many bad mystery systems hide assumptions inside an automatic deduction. Ouros should expose them.

```yaml
investigation_assumption:
  assumption_id: null
  statement: null
  introduced_by_actor_ids: []
  basis_refs: []
  status: UNTESTED
  challenged_by_refs: []
  tested_by_event_ids: []
```

Candidate statuses:

- UNTESTED
- SUPPORTED_NARROWLY
- CHALLENGED
- REJECTED
- ACCEPTED_FOR_WORKING_MODEL
- UNKNOWN

Examples:

- the clock was synchronized;
- the witness could see the entrance from that position;
- the trail had not been disturbed before observation;
- the badge was still assigned to the same holder;
- the map reflected current route conditions.

The system must never hide these assumptions behind a confidence number.

## 5. Investigative lead

A lead is a possible next action grounded in discovered information.

```yaml
investigative_lead:
  lead_id: null
  source_refs: []
  target_type: null
  target_ref: null
  proposed_action: null
  created_at: null
  known_by_actor_ids: []
  freshness_state: CURRENT
  accessibility_state: UNKNOWN
  status: OPEN
  dependency_refs: []
  alternative_lead_ids: []
```

Suggested statuses:

- OPEN
- PURSUED
- EXHAUSTED
- STALE
- INVALIDATED_BY_WORLD_CHANGE
- MERGED_WITH_OTHER_LEAD
- DECLINED
- UNREACHABLE_CURRENTLY

A lead is not a quest marker from an omniscient narrator. It exists because an actor has enough discovered information to consider that action useful.

## 6. Lead redundancy for critical connections

For an authored campaign connection whose total loss would stall the adventure, prefer several causally independent access routes where the world state permits them.

Possible routes:

- direct observation;
- witness testimony;
- a record or archive;
- a physical trace;
- a communication packet;
- ecological behavior;
- an earlier sidequest consequence;
- a map or route record;
- a public notice;
- a research result;
- an organization relationship;
- a changed location state.

Do not spawn a new clue merely because an arbitrary numeric quota has not been met.

Redundancy belongs to authored situation design, not to a hidden rescue mechanic.

## 7. Hypothesis revision event

```yaml
hypothesis_revision_event:
  revision_id: null
  trigger_refs: []
  previous_hypothesis_ids: []
  resulting_hypothesis_ids: []
  revision_type: null
  actor_ids: []
  timestamp: null
  rationale_ref: null
  preserved_disagreements: []
```

Candidate revision types:

- STRENGTHEN
- WEAKEN
- NARROW
- BROADEN_WITH_CAUTION
- SPLIT
- MERGE
- REPLACE
- WITHDRAW
- DISPROVE_NARROWLY
- REOPEN

Old hypotheses remain historical records. Do not delete them after revision.

## 8. Recontextualization event

New information often changes the interpretation of an earlier observation without changing the observation itself.

```yaml
investigation_recontextualization:
  recontextualization_id: null
  original_material_refs: []
  previous_interpretation_refs: []
  new_context_refs: []
  resulting_inference_ids: []
  occurred_at: null
  actor_ids: []
  canonical_fact_write: false
```

Examples:

- tracks once interpreted as one traveler are later understood as overlapping events;
- a map thought inaccurate is discovered to have been correct for an earlier season;
- a witness's phrase gains significance after another record shows the phrase was circulated publicly;
- an instrument blamed for an outlier is later shown to have passed calibration at the relevant time.

The event preserves both the source and the earlier interpretation.

## 9. Narrow resolution

```yaml
investigation_resolution:
  resolution_id: null
  question_id: null
  status: null
  supported_answer: null
  scope: null
  basis_refs: []
  unresolved_subquestions: []
  alternative_explanations_remaining: []
  authority_owner_ref: null
  canonical_fact_refs: []
  timestamp: null
```

Candidate statuses:

- ANSWERED_NARROWLY
- PARTIALLY_ANSWERED
- CANDIDATE_DISPROVEN_NARROWLY
- INSUFFICIENT_EVIDENCE
- ACCEPTED_AMBIGUITY
- REOPENED_BY_NEW_EVIDENCE

Only the authority that owns the relevant world fact may connect a resolution to canonical fact refs.

An investigator can personally believe a conclusion without the server promoting it to canonical truth.

## 10. Hard invariants

The following distinctions are permanent design guardrails:

`CLUE_FOUND != CONCLUSION_PROVEN`

`EVIDENCE_SUPPORTS != EVIDENCE_CONFIRMS`

`EVIDENCE_CONFLICTS != ENTIRE_HYPOTHESIS_FALSE`

`HYPOTHESIS_PLAUSIBLE != CANONICAL_TRUTH`

`THEORY_REJECTED != SOURCE_WAS_FALSE`

`ABSENCE_OF_EVIDENCE != EVIDENCE_OF_ABSENCE`

`CORRELATION != CAUSE`

`ACTOR_LIED_ON_ONE_CLAIM != ENTIRE_TESTIMONY_FALSE`

`ONE_CLUE != ONE_REQUIRED_PATH`

`CASE_STALLED != WORLD_FROZEN`

`NEW_EVIDENCE != RETCON`

`REVEAL != OVERWRITE`

`BATTLE_WON != MYSTERY_SOLVED`

`POKEMON_CAPABILITY_USED != AUTOMATIC_DEDUCTION`

`SKILL_CHECK_SUCCEEDED != CANONICAL_CAUSATION_REVEALED`

`SAME_PHRASE != SAME_ORIGIN_CONFIRMED`

`FOUND_AT_LOCATION != PLACED_BY_SUSPECT`

`CREDENTIAL_PRESENT != HOLDER_PRESENT`

## 11. Absence evidence rule

An absence becomes meaningful evidence only if the observation conditions make the missing thing reasonably detectable.

Before creating an absence-based inference, record:

- what was expected;
- why it was expected;
- the observation window;
- the detection method;
- whether the method was capable of detecting the expected signal;
- relevant environmental or operational blockers;
- uncertainty.

This avoids automatic deductions such as “no footprints means nobody came through.”

## 12. Source independence

Two materials that derive from the same origin are not independent corroboration merely because they appear in two places.

Example:

A newspaper repeats a witness statement. A later resident repeats the newspaper. These are three records but one root information lineage unless the resident had independent first-hand knowledge.

Use existing claim lineage and provenance refs to expose this relationship.

## 13. Contradiction handling

When two materials conflict, first test scope before declaring one false.

Possible causes include:

- different time windows;
- different observation positions;
- terminology mismatch;
- memory compression;
- stale records;
- changed site conditions;
- distinct entities with similar identifiers;
- transmission distortion;
- deliberate deception;
- incomplete access;
- measurement uncertainty.

The investigation ledger can store several candidates simultaneously.

## 14. Player-facing caseboard

A safe caseboard may display:

- discovered questions;
- evidence and claim cards already known to the player;
- provenance labels that the player actually knows;
- hypothesis cards proposed by player characters or NPCs;
- support/conflict/inference edges;
- open leads;
- stale leads;
- unresolved contradictions;
- previous theories and revision history.

It must not display:

- hidden canonical truth;
- secret reliability percentages;
- undiscovered source lineage;
- hidden NPC intent;
- culprit flags;
- invisible “correct theory” markers;
- server-only world facts.

## 15. NPC reasoning

NPCs may maintain their own hypothesis records when useful.

Their reasoning is limited by their knowledge state. An NPC cannot infer from evidence they have not received.

Different actors can rationally hold different working theories because they know different things or weight assumptions differently.

AI tactical policy has no authority over this reasoning layer.

## 16. Pokémon-assisted investigation

Pokémon can contribute through mechanically and narratively grounded capabilities.

Possible roles include:

- accessing a location that the party could not otherwise inspect;
- perceiving a signal supported by a verified capability;
- carrying or retrieving an object when the rules and world state permit it;
- communicating a perspective when the setting provides a legitimate communication route;
- performing a Move or Ability whose verified mechanics create an observable state.

The system must not infer forensic superpowers from species flavor text alone.

Each capability-assisted evidence route must preserve:

- exact PTU/Caelo source reference where applicable;
- capability or mechanic used;
- what was directly observed;
- what remains inference;
- engine dependency family if tactical execution is required.

## 17. Battle handoff

Before BattleSpec:

- Ouros freezes the investigation question and known-material state for the tactical slice;
- explicit combatants are selected by Ouros;
- semantic evidence, records, witnesses and noncombatants stay outside BattleSpec unless independently valid combatants;
- static geometry and battle inputs are built from verified capabilities.

After BattleSpec:

- AutoPTU returns only tactical facts supported by the battle contract;
- Ouros records those facts as new material if relevant;
- investigators may create new inferences from them;
- the battle result never directly flips a hypothesis to TRUE.

## 18. Minecraft/Cobblemon/Craftics boundary

The adapter may present:

- a caseboard;
- known clue markers;
- documents and objects already established in world state;
- witness positioning;
- environmental traces;
- hypothesis and lead UI;
- visual callbacks when earlier evidence is recontextualized.

It may not:

- reveal hidden truth;
- choose the correct theory;
- invent evidence;
- decide that a witness is lying;
- mark a clue as conclusive;
- select BattleSpec participants;
- decide PTU legality, HP, status or tactical outcomes;
- convert a Minecraft collision or animation into forensic evidence without an Ouros-authored event.

## 19. Canon status

This file defines proposed infrastructure only.

No named investigator, investigative institution, forensic profession, evidence standard, deduction procedure, legal rule, regional case practice or Pokémon investigative role becomes canon through this document.

Those require separate canon approval.