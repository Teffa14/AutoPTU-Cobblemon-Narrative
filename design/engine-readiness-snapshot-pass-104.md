# Engine Readiness Snapshot — Pass 104

Status: implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Live evidence inspected

AutoPTU-Java head observed during this pass:

`cd8def8fa0530c1897610ee8cfa81251c71065ec`

Latest relevant commit:

`Port generic Trainer Feature frequency gates (#139)`

This slice adds Python-parity infrastructure for Trainer Feature frequency/cooldown eligibility. It handles:

- frequency tokens such as Daily, Scene, Encounter, EOT, Round and Turn;
- explicit per-round and total-use limits;
- usage counts from authoritative Trainer state;
- cooldown-until checks;
- Python-compatible coercion behavior represented in parity fixtures.

The Java contract explicitly excludes prerequisite checks, context checks, resource/AP spending, usage mutation, target scopes and effect application. Prerequisite and context-gate slices exist in the two immediately preceding commits, but those independent primitives still do not equal complete Feature execution.

The parity workflow pins Python AutoPTU commit `16d228efa63aabecb67fa788959a359aac7f8f03` for this specific frequency contract.

Current AutoPTU repository head observed separately during this pass:

`13093e718dd9343ed4418178946607ea0cd6beec`

Its newest visible commits are Career-oriented, including recurring-rival rematch memory and battle-loading recovery. Those changes do not justify promoting any tactical engine family in this narrative snapshot.

The Java README continues to state that Python remains authoritative while the port is incomplete. It continues to list major incomplete work including full combat state, full damage, status controller, terrain/hazards/forced movement/reactions, complete hook registries/transcript parity, tactical AI and Minecraft/Cobblemon integration.

## Permanent capability map

### VERIFIED

`targeting / footprints / range / LoS`

Static geometry, target anchors, footprints, range and geometric LoS remain verified.

Pass 104 non-inference:

- a hearing room is not a protected tactical zone;
- a reviewer is not mechanically untargetable because of institutional role;
- an evidence table is not a targetable combat object unless explicitly represented in BattleSpec;
- privacy/access restrictions do not change LoS;
- institutional authority does not extend attack range.

`base movement legality`

Established Shift/Jump and known movement-mode legality remain verified.

Pass 104 non-inference:

- a restricted area does not mechanically prevent Shift unless represented by valid geometry/state;
- a security line does not create interception;
- a hearing aisle does not create special movement cost;
- an evacuation route does not grant extra movement;
- institutional permission does not change Overland/Swim/Sky capability.

`core calculations`

Established PTU calculation primitives remain verified.

Pass 104 adds no:

- guilt score;
- credibility score;
- sanction severity formula;
- evidence weight formula;
- appeal modifier;
- reviewer authority bonus;
- confession threshold;
- institutional reputation calculation.

`action economy / initiative`

Established action economy and initiative remain verified.

Pass 104 non-inference:

- judge/reviewer role does not grant initiative priority;
- emergency authority does not grant free actions;
- a ruling is not a battle interrupt;
- a sanction does not consume battle actions;
- a protest does not rewind an already resolved battle.

`AI legal-action infrastructure`

Legal-action generation remains verified.

It does not prove policy goals such as:

- PROTECT_REVIEWER;
- PRESERVE_EVIDENCE;
- CLEAR_EXIT;
- WITHDRAW_WITHOUT_ESCALATION;
- AVOID_CIVILIANS;
- HOLD_CORRIDOR;
- ESCORT_PARTICIPANT;
- SECURE_RECORDS;
- DEESCALATE.

### PARTIAL

`full turn / round lifecycle`

Representative phase ordering, cleanup, delayed-hit behavior, initiative rebuilding, temporary effects, Trainer AP/action reset, declared-action cleanup and Trainer Feature ordering slices exist.

Still PARTIAL because complete START/END behavior, all Status/Ability/Feature timing, interrupts/reactions, durations and full transcript parity are not proven.

Pass 104 distinction:

An institutional proceeding timeline is world state. It is not battle-round lifecycle.

`full stateful damage pipeline`

Representative authoritative damage slices exist.

Still PARTIAL.

Pass 104 non-inference:

- sanction -> HP loss;
- damaged evidence -> damage roll;
- crowd disorder -> automatic damage;
- institutional suspension -> combat debuff;
- unsafe venue finding -> environmental damage.

`status lifecycle`

Representative Status slices exist.

Still PARTIAL.

No institutional outcome creates:

- Confused;
- Fear;
- Asleep;
- Vulnerable;
- Tripped;
- Poisoned;
- Burned;
- any other PTU Status.

`move-specific behavior`

Representative Move slices exist.

Still PARTIAL.

A Move or battle transcript may be evidence only to the extent the exact behavior is implemented authoritatively. A review cannot infer unimplemented Move semantics from narration or Minecraft animation.

`abilities`

Representative Ability hooks exist.

Still PARTIAL.

An Ability cannot be used as testimony, intent evidence, truth detection or institutional authority unless exact PTU/Caelo behavior and Java implementation support that narrow use.

`items`

Representative held-item behavior exists.

Still PARTIAL.

Credentials, evidence bags, badges, permits, files, seals and hearing records are world/material objects unless an exact mechanical Item definition exists.

`Trainer Features / perks`

Still PARTIAL, with stronger generic infrastructure evidence in Pass 104.

Recent Java sequence:

- #137 — generic prerequisite gates;
- #138 — generic context gates;
- #139 — generic frequency/cooldown eligibility.

The newest slice freezes frequency-limit and cooldown/usage checks against Python and requires usage observations to come from authoritative Trainer state rather than Minecraft/Cobblemon.

The family remains PARTIAL because complete generic execution still requires separate contracts for resource/AP spending, usage mutation, target scopes, effect application and concrete Feature implementations. The three generic gate primitives do not prove the catalog.

Pass 104 non-inference:

- institutional role = Trainer Feature;
- inspector = Skill rank;
- hearing participant = ally scope;
- testimony = Feature use;
- decision = Feature effect;
- prior warning = cooldown;
- institutional review window = battle frequency token;
- social/professional credential = mechanical prerequisite.

### BLOCKING

`complete movement including push / pull / knockback / interception / forced movement`

Still BLOCKING as a complete family.

Pass 104 impact:

- no true in-grid evacuation through moving crowds;
- no escort/interception around reviewers or evidence;
- no pursuit through a disrupted hearing venue;
- no protected-corridor movement objective;
- no forced removal from an arena as an institutional sanction.

`terrain / weather / hazards / zones / reactions`

Still BLOCKING as a complete family.

Pass 104 impact:

- a security perimeter does not create a tactical zone;
- a restricted area does not create terrain;
- an unsafe-building finding does not create a hazard;
- an interim order does not create a reaction trigger;
- an institution cannot script Minecraft regions to imitate missing PTU mechanics.

`AI tactical policy`

Still BLOCKING.

Legal actions alone do not make actors preserve evidence, avoid civilians, protect a reviewer, withdraw, obey an institutional order, surrender or pursue a non-KO objective.

`Minecraft / Cobblemon / Craftics adapter and playback`

Still BLOCKING.

No verified end-to-end contract yet exists for:

- world institutional state -> Minecraft access/venue presentation;
- authenticated credential/permission projection;
- evidence/object custody presentation;
- hearing/inspection scene projection;
- battle-safe venue snapshots;
- semantic battle events -> persistent institutional evidence records;
- reinstatement/access changes -> Minecraft permissions;
- preventing client-side state from becoming institutional or PTU authority.

## Pass 104 specific overworld blockers

`INSTITUTIONAL_REVIEW_CASE_STATE`
Persistent bounded review identity linked to cases/disputes without creating a universal judiciary.

`RULE_VERSION_AND_EFFECTIVE_DATE_STATE`
Stable authored rules and the version actually applicable to an event.

`REVIEW_MANDATE_CHECK`
Explicit institution/body/scope validation before a decision can be authoritative.

`REVIEW_NOTICE_AND_PARTICIPATION_STATE`
Who was notified, what was delivered, and what response opportunity existed.

`REVIEW_EVIDENCE_PACKAGE`
Frozen provenance-aware record of evidence actually considered in each review level.

`REVIEWER_ASSIGNMENT_AND_RECUSAL`
Reviewer role, mandate and conflict/recusal history without automatic corruption inference.

`INSTITUTIONAL_FINDING_STATE`
Scoped findings such as CONFIRMED / NOT_ESTABLISHED / UNRESOLVED / OUTSIDE_SCOPE without rewriting world truth.

`RULE_INTERPRETATION_VERSIONING`
Interpretations, dissents and supersession across rule changes.

`INSTITUTIONAL_DECISION_STATE`
Formal disposition with reasons, findings, effective dates and review routes.

`REMEDY_ORDER_HANDOFF`
Decision -> Credentials / Battle Institutions / Contests / Finance / Conservation / other owner system without duplicated state.

`REVIEW_APPEAL_REHEARING_GRAPH`
Append-only challenge, affirmation, amendment, overturn and remand history.

`REINSTATEMENT_AND_RESTORATION`
Explicit end/overturn of suspensions or restrictions so stale downstream state does not become permanent.

`INSTITUTIONAL_PRIVACY_AND_PUBLIC_SUMMARY`
Private evidence and redacted public decision state.

`BATTLE_TRANSCRIPT_TO_REVIEW_EVIDENCE`
Battle events can enter an evidence package only through verified semantic contracts; Minecraft presentation is not evidence authority.

`INSTITUTIONAL_STATE_TO_MINECRAFT`
Access/venue presentation without the client deciding mandates, sanctions or PTU mechanics.

## Encounter dependency summary

### Inspection Day Interruption — FULL

VERIFIED foundations:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL if exact mechanics are invoked:

- lifecycle;
- damage;
- statuses;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:

- complete movement/interception/forced movement for live evacuation;
- terrain/hazards/zones/reactions if venue hazards are tactical;
- AI tactical policy for protect/evacuate/withdraw goals;
- Minecraft/Cobblemon/Craftics adapter/playback.

REDUCED viability:

High. Evacuate civilians in world state, freeze a safe arena, run a conventional static confrontation, then review pre-incident evidence and authoritative battle events separately.

### Protested Exhibition Result — FULL

Predominantly overworld/institutional.

Combat dependency is scoped to the exact protested mechanic.

If the protest concerns:

- Move legality/behavior -> `move-specific behavior` PARTIAL and exact Move parity required;
- Ability -> `abilities` PARTIAL and exact Ability parity required;
- Item -> `items` PARTIAL and exact Item parity required;
- Trainer Feature -> `Trainer Features / perks` PARTIAL and exact Feature parity required;
- targeting/range/LoS -> VERIFIED foundation;
- ordinary initiative -> VERIFIED foundation.

No full-family claim follows from a representative implementation.

REDUCED viability:

Very high. Use the recorded event/result plus registration and evidence. Do not replay the battle unless the authored competition process explicitly orders a new match.

### Credential Review Under Evacuation — FULL

Predominantly world state until a crisis becomes tactical.

BLOCKING for the intended live rescue version:

- complete movement/interception/forced movement;
- terrain/weather/hazards/zones/reactions if environmental hazards matter;
- AI tactical policy;
- adapter/playback.

REDUCED viability:

High. Pause review, issue an explicit emergency permission through the existing Credentials/Authority system, resolve evacuation in world state and use static conventional combat only if separately required. Resume the review afterward.

## Promotion decision

No permanent category is promoted in Pass 104.

The latest Java slice materially strengthens generic `Trainer Features / perks` infrastructure by adding Python-parity frequency/cooldown eligibility on top of prerequisite and context gates. The family remains PARTIAL because gate evaluation is not complete execution and the implementation explicitly excludes resources/AP, usage mutation, target scopes and effect application.

Pass 104 itself is primarily an overworld/institutional architecture. It can advance extensively without waiting for battle parity, provided battles remain authoritative evidence sources only within their verified/partial implementation boundaries and Minecraft never becomes the authority for institutional findings or PTU rules.