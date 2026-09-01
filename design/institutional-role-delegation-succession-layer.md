# Institutional Role, Delegation, and Succession Layer

Status: DESIGN CANDIDATE — NOT CANON
Date: 2026-09-01
Research basis: `research/2026-09-01-institutional-succession-apprenticeship-handover-scan-179.md`

## Design objective

Give Ouros institutions durable responsibility that can continue when individual NPCs train, travel, transfer duties, become unavailable or eventually leave a role.

This layer is intentionally separate from relationship affinity, PTU Trainer Classes, service dispatch, schedules and quest completion. It composes with those systems rather than replacing them.

Core sequence:

```text
INSTITUTION
  -> ROLE / MANDATE
  -> CURRENT HOLDER
  -> DUTIES
  -> SUPERVISED PRACTICE
  -> BOUNDED DELEGATION
  -> INDEPENDENT DUTY
  -> ABSENCE / TRANSFER / VACANCY
  -> HANDOVER
  -> RETURN / NEW HOLDER / ROLE CHANGE
```

The sequence is not mandatory and is not one-way. A character can remain an assistant indefinitely, refuse advancement, lose one delegated scope while retaining another, return to supervision, or leave without naming a successor.

## Non-negotiable semantic boundaries

```text
MENTORSHIP != SUCCESSION
RELATIONSHIP != INSTITUTIONAL_AUTHORITY
PTU_MENTOR_CLASS != SOCIAL_MENTORSHIP
WORKSITE_PRESENCE != ROLE_HOLDING
SCHEDULE_ENTRY != MANDATE
DELEGATION != FULL_ROLE_TRANSFER
ACTING_ROLE != PERMANENT_SUCCESSION
TRAINING_COMPLETE != PROMOTION
BATTLE_VICTORY != PROMOTION
PUBLIC_BELIEF != CANONICAL_AUTHORITY
NPC_ENTITY_DESPAWN != ABSENCE_OR_VACANCY
SAME_SURNAME != INHERITANCE
QUEST_COMPLETE != OFFICE_GAINED
```

These distinctions are especially important in Marea because several canon relationships already use mentor/supervisor language while PTU also has a mechanical Mentor class.

## Canonical role record

A future runtime representation should preserve at minimum:

```yaml
role_id: ouros.role.example
institution_id: ouros.institution.example
display_name: Example role
status: ACTIVE
mandate:
  - receive_reports
  - schedule_field_checks
current_holder_actor_id: ouros.npc.example
acting_holder_actor_id: null
holder_since_world_time: ...
public_contact_actor_id: ouros.npc.example
work_site_ids: []
qualification_claims: []
restricted_actions: []
```

`role_id` is stable even when the holder changes.

An institution may have multiple roles. A role may have no current holder. One actor may hold several compatible roles only when canon explicitly says so.

## Mandate verbs

Authority should be represented through specific verbs instead of a single scalar rank.

Candidate verbs include:

- RECEIVE
- PREPARE
- RECORD
- VERIFY
- REVIEW
- APPROVE
- SCHEDULE
- ASSIGN
- ESCALATE
- PUBLISH
- ISSUE
- RELEASE
- CUSTODY_ACCEPT
- CUSTODY_TRANSFER
- OPEN_FACILITY
- CLOSE_FACILITY
- DECLARE_RESTRICTION
- REQUEST_ASSISTANCE
- AUTHORIZE_MATCH
- CERTIFY_RESULT

These verbs are narrative/world authority only until a matching gameplay system explicitly consumes them.

A role can own one verb without owning adjacent verbs. For example, an observation technician may PREPARE a field packet while a project lead REVIEWs it. A dock worker may RECEIVE cargo while the dock coordinator SCHEDULEs berth priority.

## Delegation record

Delegation should be explicit and auditable.

```yaml
delegation_id: ...
role_id: ...
principal_actor_id: ...
delegate_actor_id: ...
allowed_verbs:
  - PREPARE
  - RECORD
scope_refs:
  - ouros.site.example
starts_at_world_time: ...
expires_at_world_time: ...
supervision_mode: REVIEW_REQUIRED
revocation_state: ACTIVE
reason_claim_id: ...
created_by_authority_ref: ...
```

A delegation never copies the entire role implicitly.

### Delegation states

- PROPOSED
- ACTIVE_SUPERVISED
- ACTIVE_INDEPENDENT
- SUSPENDED
- EXPIRED
- REVOKED
- COMPLETED

`ACTIVE_INDEPENDENT` means independent within the declared scope, not institution-wide autonomy.

## Supervision modes

- DIRECT_PRESENT: principal is physically present.
- REVIEW_REQUIRED: delegate acts, principal must review before finalization.
- SAMPLE_AUDIT: delegate can finalize ordinary work; selected work is audited.
- ESCALATION_ONLY: delegate works independently but defined exceptions must be escalated.
- NONE_WITHIN_SCOPE: mature delegation with no routine review requirement.

These are institutional states. They do not provide PTU bonuses.

## Handover record

Handovers should preserve continuity rather than silently replacing one actor ID.

```yaml
handover_id: ...
role_id: ...
outgoing_holder_actor_id: ...
incoming_holder_actor_id: ...
acting_or_permanent: ACTING
started_at_world_time: ...
completed_at_world_time: ...
open_items: []
physical_custody_transfers: []
knowledge_packet_refs: []
public_notice_ref: ...
accepted_by_incoming: true
```

Open work remains tied to its actual state. Changing the role holder does not complete, cancel or recreate outstanding tasks.

## Vacancy and absence are different

Suggested role availability states:

- STAFFED
- HOLDER_TEMPORARILY_OFFSITE
- HOLDER_UNAVAILABLE
- ACTING_COVER
- VACANT
- HANDOVER_IN_PROGRESS
- ROLE_SUSPENDED
- ROLE_ABOLISHED

A scheduled trip or field inspection normally produces `HOLDER_TEMPORARILY_OFFSITE`, not `VACANT`.

A Minecraft actor unloading produces no role-state transition at all.

## Apprenticeship / supervised development

Ouros should represent development through real work history rather than a generic apprenticeship XP bar.

A development record can track:

```yaml
actor_id: ...
institution_id: ...
target_role_id: null
observed_duties: []
supervised_duties: []
independent_duties: []
review_history: []
known_limits: []
interest_posture: UNDECLARED
```

`target_role_id` may be null. Learning a job does not mean intending to inherit it.

### Development events

- OBSERVED_DUTY
- ASSISTED_DUTY
- COMPLETED_SUPERVISED_DUTY
- COMPLETED_REVIEWED_INDEPENDENT_DUTY
- RECEIVED_CORRECTION
- ESCALATED_CORRECTLY
- EXCEEDED_SCOPE
- DECLINED_DELEGATION
- REQUESTED_MORE_RESPONSIBILITY
- DECLINED_ROLE_PATH

A correct escalation can count as evidence of competence. Knowing when not to act is part of institutional reliability.

## Relationship integration

Existing relationships can explain why two actors spend time together, trust each other or enter a training scene. They do not grant mandate.

Examples:

- Taro/Pia professional mentorship can produce archive-learning scenes.
- Sela/Jace mentor/student can produce supervised Battle Yard work.
- Nerea/Ema project supervision can produce reviewed observation packets.

A relationship system may remember reactions to a delegation, failure or promotion. Authority still comes from the role/delegation record.

## Schedule integration

Schedules answer where an actor is expected to be.

Roles answer what the actor is authorized or responsible to do.

When a regular holder is off-site, a schedule event can trigger evaluation of coverage. It must not automatically appoint the nearest coworker.

Useful schedule-linked events:

- DUTY_SHIFT_START
- DUTY_SHIFT_END
- FIELD_ASSIGNMENT_START
- EXPECTED_RETURN
- HANDOVER_WINDOW
- PUBLIC_OFFICE_HOURS

## Service dispatch integration

The service dispatch layer can ask an institution for the current valid contact for a request type.

A temporary delegation may change who receives or prepares a request without changing who has final approval.

Example:

```text
REQUEST_ARRIVES
  -> ROLE_LOOKUP(RECEIVE)
  -> CURRENT AUTHORIZED ACTOR
  -> WORK
  -> ROLE_LOOKUP(APPROVE)
  -> POSSIBLY DIFFERENT ACTOR
```

This prevents every service request from hard-coding an NPC name.

## Communications and local knowledge integration

A public notice can say that an actor is covering a desk today. That notice is an information packet.

Canonical authority remains the role state.

A resident can miss the notice and still believe the regular holder is responsible. Another can overinterpret an acting assignment as a permanent promotion. Existing claim propagation handles that divergence.

## Public memory integration

Meaningful role changes can become public-memory events:

- first independently handled ferry shift;
- a long-serving role holder retiring;
- an institution changing procedure after a failed handover;
- an acting appointment during a major disruption;
- a former holder returning after another post ends.

Routine shift coverage should normally remain operational history, not civic legend.

## Physical object integration

Handovers can have physical evidence without creating magical authority tokens.

Potential objects:

- duty roster;
- custody ledger;
- key ring;
- stamped packet;
- archive checkout register;
- equipment issue sheet;
- match schedule;
- field notebook bundle.

Holding the object does not itself grant the role unless canon explicitly establishes such a custom.

## Pokémon partner integration

An NPC's partner Pokémon can accompany work and become part of the visible continuity of a role.

However:

```text
PARTNER_PRESENT != ACTOR_AUTHORIZED
PARTNER_ABSENT != ROLE_SUSPENDED
PARTNER_BATTLE_RESULT != HOLDER_PROMOTED
```

If an institution eventually assigns duties to Pokémon directly, those duties require their own canon record rather than being inferred from the Trainer's role.

## Institutional resilience

A persistent world should expose single points of failure.

Possible institution-level metrics are qualitative, not numeric buffs:

- DOCUMENTED_PROCEDURE
- SHARED_KNOWLEDGE
- TRAINED_BACKUP
- SINGLE_HOLDER_DEPENDENCY
- OPEN_HANDOVER
- CUSTODY_AMBIGUITY
- PUBLIC_CONTACT_CLEAR

An arc can improve resilience by documenting a process or training a backup without replacing anyone.

## Conflict without villainy

Institutional stories can generate meaningful conflict through normal constraints:

- two people believe different handover times are in effect;
- a delegate correctly refuses work outside scope, frustrating a resident;
- an acting holder changes a routine within their mandate and the regular holder dislikes it;
- a talented trainee does not want the senior post;
- a former holder returns to find the institution has improved without them;
- a public notice lags behind canonical role state;
- a procedure depends on undocumented personal knowledge;
- two duties conflict while only one actor is authorized for both.

None requires corruption or conspiracy.

## Battle handoff rule

Institutional authority must stay outside BattleSpec.

A battle can provide an audited event such as:

- MATCH_COMPLETED
- SESSION_SAFELY_CONCLUDED
- TRAINER_RECORD_UPDATED
- SPECIFIC_COMPETENCY_OBSERVED

The institution then decides whether that event matters under an existing policy.

Battle code must never directly emit `PROMOTED`, `ROLE_ASSIGNED`, `DELEGATION_GRANTED` or `SUCCESSOR_CHOSEN`.

## Mechanically rich example: supervised Battle Yard shift

Intended full version:

Jace receives a bounded delegation from Sela to run one scheduled local training session. He handles participant check-in, ordinary fixture inspection and one audited Trainer battle. Sela is not required to stand beside him throughout the whole event, but remains the escalation contact for exceptions outside Jace's scope.

Potential mechanical needs depend on the exact participants and battlefield package:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement if selected Moves or Features use Push, Pull, Knockback, Interception or forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle if selected content applies statuses;
- terrain/weather/hazards/zones/reactions if the selected battlefield or content requires them;
- exact move-specific behavior;
- exact Abilities;
- exact Items;
- exact Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy for autonomous opponents;
- Minecraft/Cobblemon/Craftics adapter/playback support for the full visible version.

Institutional evaluation remains separate from combat mechanics.

### Reduced version

Use a parity-audited basic matchup that avoids forced movement, hazard/zone/weather dependencies, complex statuses, unsupported Items and unsupported Trainer Features.

Sela's delegation and Jace's responsibilities remain canonical world-state facts outside BattleSpec.

The battle may emit only its audited result plus a narrow event such as `YARD_SESSION_MATCH_COMPLETE`.

Jace's institutional review can then consider whether he stayed within scope, completed records and escalated exceptions correctly. Winning is neither necessary nor sufficient for promotion.

## Long-term story value

This layer supports character growth without making every arc a friendship meter or power increase.

A resident can become more trusted, more independent, less interested in leadership, better at documentation, more willing to delegate, or more replaceable in a healthy organizational sense.

Institutions themselves can mature. Marea can move from personality-dependent operations toward documented shared practices while retaining the individuality of its residents.

## Canon gate

Promotion to canon requires explicit decisions for:

- institution IDs and mandates;
- role IDs;
- current holders;
- actual delegation scopes;
- any succession or vacancy;
- public titles;
- certification customs;
- relationship changes;
- any PTU Trainer Class assignment.

Until those decisions are approved, this file remains architecture only.
