# Performance, Production, Ensemble, and Reception Continuity Extension

Status: PROPOSED ARCHITECTURE
Canon effect: NONE until individually approved
Pass: 159

## Purpose

Ouros needs to remember artistic and staged activity across time without turning applause, reviews, rehearsal, or stage spectacle into invented PTU mechanics.

This extension tracks works, production versions, ensembles, roles, rehearsal episodes, scheduled events, actual performances, cancellations, tours, attributed reception, revisions, recasts, revivals, and retirement.

## Authority boundaries

This extension owns:

- persistent identity for a work and a production version;
- ensemble membership for a specific production period;
- role assignment and recasting history;
- rehearsal and production-preparation episodes as narrative facts;
- scheduled performance records;
- actual performance episodes;
- cancellation, postponement, relocation, interruption, resumption, and completion records;
- attributed audience response and reviews;
- production revision/version lineage;
- tour legs as production-level references;
- retirement, revival, and archival-performance links.

Existing systems retain authority over:

Training/Coaching:
- practice goals, coaching, demonstrations, mechanical progression gates.

Ritual/Tradition:
- living inherited practices, observances, transmission, variants, community meaning.

Travel/Expedition:
- actual movement between venues and route outcomes.

Material Culture / Archives:
- props, costumes, instruments, recordings, posters, programs, physical provenance and custody.

Organizations / Workplaces / Contracts:
- employment, ownership, organizational membership, formal authority, commercial terms.

Public Memory / Claims / Investigation:
- public narratives, historical claims, source lineage, truth status, evidence.

Battle Institutions / PTU Contest mechanics:
- formal contest legality, Appeal Rolls, Contest effects, judging mechanics, rewards, ranks and official result authority when such systems are actually approved and verified.

AutoPTU:
- authoritative tactical facts inside BattleSpec only.

Minecraft/Cobblemon/Craftics:
- visual presentation and playback of already-decided state.

## Core records

### `performance_work_ref`

Persistent identity of the authored or inherited work/practice being staged.

Suggested fields:

```yaml
work_ref: work:...
title: ...
work_kind: MUSIC | DANCE | DRAMA | MIXED | CONTEST_ROUTINE | STORYTELLING | OTHER
authorship_claim_refs: []
tradition_ref: null
canon_status: PROPOSED
```

A work identity does not prove authorship claims.

### `production_version`

One staged interpretation or organized version of a work.

```yaml
production_id: production:...
work_ref: work:...
version_label: ...
lead_organization_ref: ...
active_from: ...
active_until: null
parent_production_id: null
revision_notes: []
```

`PRODUCTION_REVISED != PRIOR_VERSION_ERASED`.

### `ensemble_period`

Tracks who belonged to the active production ensemble during a bounded interval.

Roles may include performer, Trainer-performer, Pokémon-performer, musician, stage manager, director, technical operator, understudy, narrator, host, judge, or other authored role.

Membership never implies employment or organizational membership unless linked to those systems.

### `role_assignment`

```yaml
role_assignment_id: role:...
production_id: ...
role_label: ...
actor_ref: ...
start_time: ...
end_time: null
reason_for_change: ...
source_refs: []
```

A recast creates history. It does not replace old records.

### `rehearsal_episode`

Records that preparation occurred.

May include:

- participants;
- location;
- production version;
- goals;
- observed problems;
- changes proposed;
- interruptions;
- linked Training records;
- linked battle demonstrations.

Hard boundary:

`REHEARSAL_COMPLETED != MECHANICAL_PROGRESSION`.

### `scheduled_performance`

A plan, booking, announcement, or calendar commitment.

Possible states:

- ANNOUNCED
- TENTATIVE
- CONFIRMED
- POSTPONED
- RELOCATED
- CANCELLED
- SUPERSEDED
- OCCURRED

The schedule record is not the performance itself.

### `performance_episode`

A concrete occurrence.

```yaml
performance_id: perf:...
production_id: ...
scheduled_ref: ...
venue_ref: ...
start_time: ...
end_time: ...
participant_refs: []
completion_state: COMPLETE | INTERRUPTED | PARTIAL | ABORTED
formal_result_ref: null
recording_refs: []
```

### `reception_record`

Attribution-preserving reception evidence.

Kinds:

- AUDIENCE_APPLAUSE_OBSERVATION
- FORMAL_REVIEW
- INFORMAL_COMMENT
- PRESS_REVIEW
- JUDGE_COMMENT
- SALES_OR_ATTENDANCE_OBSERVATION
- VOTE_RESULT
- ORGANIZER_ASSESSMENT

Suggested fields include observer/source, scope, date, quoted-or-paraphrased claim, confidence, and evidence references.

There is no global quality scalar.

### `production_change_event`

Examples:

- RECAST
- DIRECTOR_CHANGE
- ROUTINE_REVISION
- PROP_CHANGE
- VENUE_ADAPTATION
- FORMAT_CHANGE
- TOUR_CUT
- TOUR_EXTENSION
- REVIVAL
- RETIREMENT

Each change references the version it affected.

## Required semantic separations

- `PERFORMANCE_SCHEDULED != PERFORMANCE_OCCURRED`
- `PERFORMANCE_STARTED != PERFORMANCE_COMPLETED`
- `PERFORMANCE_CANCELLED != PRODUCTION_ENDED`
- `PRODUCTION_ENDED != WORK_FORGOTTEN`
- `ROLE_RECAST != PREVIOUS_CAST_RETCONNED`
- `AUDIENCE_REACTION != CANONICAL_QUALITY`
- `REVIEW_PUBLISHED != REVIEW_TRUE`
- `FORMAL_RESULT != UNIVERSAL_QUALITY`
- `POPULAR != CANON_APPROVED`
- `POKEMON_ON_STAGE != COMBATANT`
- `TRAINER_ON_STAGE != TRAINER_IN_BATTLESPEC`
- `MOVE_USED_AS_PERFORMANCE != MOVE_RESOLVED_AS_ATTACK`
- `STAGE_EFFECT != TERRAIN`
- `STAGE_WEATHER_EFFECT != PTU_WEATHER`
- `PROP != PTU_ITEM`
- `COSTUME != ARMOR_OR_HELD_ITEM`
- `PERFORMANCE_INJURY_RUMOR != DAMAGE_EVENT`
- `REHEARSAL_BATTLE != PERFORMANCE_RESULT`
- `REHEARSAL_SUCCESS != FEATURE_GRANTED`
- `APPLAUSE != REPUTATION_GAIN`
- `DEPICTION_OF_HISTORY != HISTORICAL_EVIDENCE`

## Contest bridge

A production can be linked to a formal Contest only through an explicit governing contract.

Required fields:

```yaml
formal_performance_contract:
  governing_source: PTU_OR_CAELO_REFERENCE
  rules_version: ...
  event_format: ...
  runtime_support_status: VERIFIED | PARTIAL | BLOCKED | UNKNOWN
  result_ref: ...
```

If runtime support is UNKNOWN or BLOCKED, Narrative may still stage a nonmechanical performance event but may not invent Appeal scores, Contest effects, official ranks, or mechanical rewards.

## Audience model

Audience state is sampled and attributed.

A performance may have:

- mixed applause;
- different reactions by section;
- reviews published later;
- regional differences across tour stops;
- contradictory memories months later;
- a formal vote whose scope is narrower than general popularity.

No reaction automatically propagates globally. Communications/Public Memory controls later spread.

## Touring model

A tour is a sequence of intended performance stops linked to Travel.

A stop can be:

- completed;
- delayed;
- relocated;
- cancelled;
- replaced by a smaller event;
- converted to workshop/rehearsal;
- skipped.

The next stop does not inherit physical or tactical state automatically.

## Pokémon agency

A Pokémon performer has its own participation record.

Narrative must not infer:

- consent from ownership alone;
- ownership from performance participation;
- combatant status from being on stage;
- learned Moves from rehearsal;
- mechanical Contest readiness from popularity;
- willingness to continue a tour from prior participation.

Any mechanically meaningful Pokémon capability must be cross-checked against PTU/Caelo and current engine contracts.

## Stage effects

Stage lighting, projected rain, smoke machines, pyrotechnic-looking visual effects, moving scenery, sound cues, trapdoors, and choreography are presentation facts unless separately promoted into tactical state through an explicit verified contract.

Minecraft may render these effects after Ouros establishes them.

Minecraft physics, fire, particles, redstone, block updates, entity pathing, or Cobblemon battle-state logic cannot create PTU hazards or damage by themselves.

## Interruption and incident handling

A performance can be interrupted by:

- infrastructure failure;
- medical event;
- travel delay;
- protest or civic restriction;
- weather;
- missing participant;
- equipment/prop problem;
- hostile incident;
- voluntary withdrawal.

The causal system owns the cause. This layer records the production consequence.

## Long-term story support

This layer enables:

- recurring performers who age into directors or teachers;
- local venues with decades of production history;
- rival artists whose competition is not automatically battle rivalry;
- works adapted differently by different towns;
- contested revivals;
- touring careers;
- famous cancellations;
- props and recordings with provenance;
- characters returning after years in a new production role;
- artistic depictions that shape public memory while remaining historically disputable.

## Canon policy

Everything created through this extension remains PROPOSED unless an existing canon source or explicit approval promotes it.

Research provenance remains in `research/`.

Worldbuilding candidates remain in `proposals/`.

No source-inspired institution, performer, title, work, or event becomes Ouros canon automatically.