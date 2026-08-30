# Campaign Arc Convergence, Pressure & Payoff Extension

Status: DESIGN PROPOSAL. New arc structures, NPCs, factions, locations and events in this file are NON-CANON unless separately approved. Existing authority boundaries remain CANON-APPROVED project architecture.

Date: 2026-08-30

## Purpose

This layer owns campaign-scale connective state between locally complete adventures.

It does not own individual mission assembly, faction decision-making, antagonist planning, boss mechanics, actor knowledge, institutional procedures or tactical battle execution. Those remain with their existing owners.

The problem this layer solves is narrower: several independent threads can remain alive for weeks or months, change state separately, become more or less salient, intersect when their facts genuinely align, and leave consequences after a major arc resolves.

## 1. Arc thread

An arc thread is a persistent question, pressure, relationship or unresolved consequence that can generate future situations.

```yaml
arc_thread:
  thread_id: null
  arc_id: null
  source_refs: []
  question: null
  stake_refs: []
  actor_ids: []
  location_ids: []
  faction_ids: []
  current_state: active
  current_stage: null
  visibility: low
  urgency: low
  player_knowledge_refs: []
  world_fact_refs: []
  unresolved_outputs: []
  advancement_conditions: []
  stall_conditions: []
  retreat_conditions: []
  transformation_conditions: []
  collision_tags: []
  payoff_candidates: []
  last_meaningful_event_id: null
```

Candidate states:

- ACTIVE
- DORMANT
- PRESSING
- STALLED
- TRANSFORMED
- CONVERGED
- LOCALLY_RESOLVED
- RESOLVED
- ABANDONED_BY_ACTORS
- ACCEPTED_AMBIGUITY

`DORMANT` means the thread remains true but currently produces little player-facing pressure.

## 2. Pressure is salience, not automatic progression

World Agency remains responsible for whether actors actually advance a plan or front.

This layer may increase or decrease how prominently an existing development is surfaced to players.

```yaml
pressure_signal:
  signal_id: null
  thread_id: null
  source_event_id: null
  signal_type: null
  audience_ids: []
  visibility: null
  urgency_claimed: null
  urgency_verified: null
  expires_at: null
```

Signals may include:

- a recurring absence;
- changed route conditions;
- a rival arriving early;
- a faction moving visible assets;
- a public notice;
- a witness seeking contact;
- an ecological shift;
- a deadline that actually exists in the owning system;
- an NPC changing plans because of a verified event.

No hidden global timer is created merely because a thread is important.

## 3. Campaign pressure budget

A region should not present every active thread as an emergency simultaneously.

```yaml
campaign_pressure_budget:
  region_id: null
  max_pressing_threads: null
  protected_quiet_capacity: null
  current_pressing_thread_ids: []
  next_review_event: null
```

Exact numerical defaults remain implementation choices.

Selection should prefer:

- real urgency;
- direct player consequence;
- recent actor action;
- strong evidence visibility;
- unresolved commitments;
- novelty against recent play;
- lane diversity;
- causal proximity.

A pressure budget must never suppress an actual crisis fact. It controls narrative salience and hook density, not world truth.

## 4. Convergence eligibility

A convergence is a new situation created by two or more threads whose current states now share meaningful actors, locations, resources, evidence, goals or consequences.

```yaml
arc_convergence:
  convergence_id: null
  contributing_thread_ids: []
  eligibility_conditions: []
  disqualifying_conditions: []
  shared_actor_ids: []
  shared_location_ids: []
  shared_resource_refs: []
  shared_evidence_refs: []
  conflict_edges: []
  player_visible_signals: []
  available_activity_lanes: []
  candidate_outcomes: []
  aftermath_outputs: []
  status: candidate
```

Hard rule:

`CONVERGENCE_ELIGIBLE != CONVERGENCE_FORCED`.

The campaign can offer the convergent situation. Players may approach another thread, decline, arrive late where that is plausible, or change the conditions enough that the convergence transforms.

## 5. No convergence teleportation

Every participant in a large scene must independently pass normal world-state checks:

- can they know about it?
- can they reach it?
- do they have a reason to go?
- do they have the required resources?
- are they free to act?
- does their current plan still support attendance?

A recurring rival, old mentor or faction leader cannot appear merely because a finale needs recognizable faces.

## 6. Parallel objective model

Large arcs should often permit actors to work on different problems at the same time.

```yaml
parallel_objective:
  objective_id: null
  owner_ids: []
  parent_arc_id: null
  required_inputs: []
  independent_progress_state: null
  outputs: []
  dependency_edges: []
  convergence_hooks: []
```

One group may research access while another secures supplies. A rival may independently pursue the same location. A faction may move an asset for a different reason. These lines become one scene only if their states meet.

The player is not required to personally perform every objective for the arc to progress.

## 7. Recontextualization contract

Long campaigns need reveals that change meaning without corrupting provenance.

```yaml
recontextualization_event:
  event_id: null
  affected_fact_refs: []
  affected_claim_refs: []
  new_evidence_refs: []
  prior_interpretations: []
  supported_interpretations: []
  rejected_interpretations: []
  facts_unchanged: []
```

Hard boundaries:

- `REVEAL != RETCON`
- `NEW_CAUSE_DISCOVERED != OLD_EVENT_ERASED`
- `CLAIM_DISPROVED != CLAIMANT_KNEW_IT_WAS_FALSE`
- `PUBLIC_BELIEF_CHANGED != WORLD_TRUTH_CHANGED`

## 8. Setup and payoff ledger

Not every detail is foreshadowing.

A deliberate setup can be recorded when the campaign intentionally creates an unresolved expectation, question or affordance.

```yaml
payoff_ledger_entry:
  setup_id: null
  source_event_id: null
  setup_type: null
  signaled_to: []
  related_thread_ids: []
  promised_question: null
  guaranteed_event: false
  callback_eligible: true
  transformation_required: true
  payoff_state: open
  payoff_event_ids: []
  retirement_reason: null
```

Candidate setup types:

- unresolved_question
- visible_cost
- promise_or_debt
- recurring_object
- unexplained_behavior
- relationship_change
- incomplete_record
- closed_route
- rival_goal
- faction_claim
- ecological anomaly

A callback should normally add changed context, new consequence or new understanding. Repeating the same NPC, object or joke without transformation is continuity, not payoff.

## 9. Payoff retirement

Setups may become invalid.

Valid retirement reasons include:

- actor died or permanently left through governed state;
- location destroyed or inaccessible through established state;
- mystery resolved elsewhere;
- player decision removed the premise;
- source claim disproved;
- importance decayed and no meaningful future use remains.

Retiring a setup is preferable to forcing an implausible callback.

## 10. Finale eligibility

A finale is a campaign-scale concentration of stakes. It is not a mechanical status.

```yaml
finale_candidate:
  arc_id: null
  unresolved_core_threads: []
  resolved_support_threads: []
  convergence_id: null
  pressure_signals: []
  personal_stake_refs: []
  world_stake_refs: []
  likely_activity_lanes: []
  aftermath_owners: []
  mechanics_review_required: true
```

A finale becomes eligible when enough causal material exists for a major resolution. No fixed act count or universal threshold is proposed.

Strong finale candidates usually have:

- a question the players already understand;
- visible consequences from earlier play;
- at least one changed relationship or actor state;
- a location or objective grounded in prior information;
- more than one plausible approach before commitment;
- an aftermath that matters after the battle or decision.

## 11. Finale runway

Major convergence should normally have player-facing runway unless surprise is itself causally justified.

Possible runway signals:

- several threads begin mentioning the same place;
- a rival changes route;
- an institution changes posture;
- ordinary services react to pressure;
- an antagonist reallocates resources;
- an ecological pattern becomes visible;
- a previously minor clue becomes independently corroborated.

Runway is not a countdown. It is evidence that the world is moving toward a shared situation.

## 12. Participation lanes

World Agency already defines participation profiles. A major arc should query those profiles and current world state when exposing hooks.

Potential lanes:

- battle
- investigation
- social
- exploration
- research
- profession
- faction
- contest
- capture
- dungeon

A major arc should offer multiple lanes when the fiction genuinely supports them. It should not manufacture a research task or social scene solely to satisfy a quota.

A player who resolves a relevant side thread may create an asset, clue, relationship or route that changes the convergence. Optional content must not be retroactively declared mandatory.

## 13. Local victory and global state

After a major encounter, each owner evaluates its own consequences.

A tactical victory may resolve one confrontation while leaving:

- faction succession;
- displaced Pokémon;
- damaged infrastructure;
- public memory;
- unresolved evidence;
- rival relationships;
- financial obligations;
- institutional review;
- ecological recovery;
- surviving subordinate plans.

`BOSS_DEFEATED != ARC_RESOLVED`.

The arc resolves only when its core thread question has a governed outcome.

## 14. Aftermath window

A resolved major arc should normally expose an aftermath window before the next high-pressure convergence unless world state makes that impossible.

Aftermath activities may include:

- checking on affected NPCs;
- seeing repaired or abandoned places;
- hearing conflicting public accounts;
- receiving delayed correspondence;
- observing faction succession;
- revisiting a changed dungeon;
- training or recovering;
- following optional residue threads.

This gives consequence layers time to become visible rather than compressing them into one epilogue paragraph.

## 15. Thread transformation

Threads do not need binary completion.

Examples:

- an antagonist thread becomes a succession dispute;
- an ecological crisis becomes a restoration project;
- a mystery becomes public-memory conflict after the truth is known;
- a rival race becomes cooperation against a shared obstacle;
- a damaged route becomes a profession or civic-work thread;
- a boss confrontation becomes a recurring Pokémon bond arc.

Transformation must preserve provenance and emit a new owner when responsibility changes.

## 16. Anti-railroading contract

The system must invalidate planned convergence content when required world facts disappear.

If players expose a plan early, remove a required asset, reconcile two groups, evacuate the target, destroy access, convince a critical actor or cause a faction to split, then the campaign re-evaluates.

It may produce a different confrontation, no confrontation, a negotiation, a pursuit, a reconstruction problem or a quiet resolution.

Authored spectacle has no authority over world state.

## 17. Battle handoff

When a convergence creates combat, Ouros freezes the explicit pre-battle state and requests a BattleSpec.

The tactical layer receives only facts it owns:

- explicit combatants;
- positions and footprints;
- legal tactical state;
- reviewed geometry;
- reviewed objective contract where supported.

Noncombatant faction goals, archive custody, political authority, scientific truth, rescue completion and other semantic world facts remain outside BattleSpec unless an explicit owner contract says otherwise.

After battle, Ouros accepts only narrow authoritative outputs and lets relevant world systems derive consequences.

## 18. Reduced convergence pattern

A mechanically rich finale may safely compile as:

1. Ouros resolves which threads actually converge.
2. Social/investigative/exploration decisions occur in overworld state.
3. Neutral actors and semantic objects leave tactical state.
4. AutoPTU resolves one static battle with explicit combatants.
5. Ouros commits the narrow tactical result.
6. Remaining threads resolve, transform or stay open through their owning systems.
7. A second BattleSpec is created only if a later state independently requires one.

This pattern preserves campaign consequence without requiring tactical AI or Minecraft scripting to impersonate missing PTU rules.

## 19. Canon boundary

This file establishes no actual Ouros faction, Legendary, villain, war, disaster, League hierarchy or final campaign plot.

It proposes the connective data model that future reviewed canon can use.

## 20. Promotion checklist

Before a major authored arc becomes canon:

- its setup facts have provenance;
- required actors can plausibly know and reach relevant situations;
- faction/front behavior follows existing agency state;
- recontextualizations preserve prior observations;
- optional content remains optional;
- no invalid planned scene is protected from player consequence;
- every tactical scene has exact capability dependencies;
- reduced forms exist where rich mechanics are not ready;
- aftermath owners are identified;
- Minecraft/Cobblemon/Craftics remains presentation/playback only.