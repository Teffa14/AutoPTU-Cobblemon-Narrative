# Ouros Credentials, Permissions & Eligibility Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

Ouros already models authority, regional recognition, education, conservation access, cases, workplaces, research programs, archives, battle institutions and infiltration. Those systems all need bounded access decisions, but they should not each invent a different meaning for rank, certification, permission or admission.

This layer provides a common record model for proving qualifications and granting scoped access while avoiding a universal modern bureaucracy that Ouros has not established.

It does not create passports, citizenship, visas, professional licensing law, a universal Trainer license, universal police powers or a single rank ladder for the region.

## Core separation

Keep these facts independent:

qualification evidence → what the actor has demonstrated;

credential → what an issuer has formally recognized;

eligibility assessment → whether a specific rule set currently accepts that evidence;

permission grant → what action/location/resource the holder may access;

admission token → a bounded proof of permission for a visit/event;

authority/mandate → what an institution or actor is responsible for;

ownership/custody → who owns or holds an object/Pokémon;

public reputation → what people think about the actor;

mechanical PTU state → what rules the character/Pokémon can actually perform.

None of these implies the others automatically.

## Qualification record

```yaml
qualification_record:
  qualification_id: null
  actor_id: null
  qualification_kind: null
  demonstrated_scope: []
  evidence_refs: []
  evaluator_ids: []
  evaluation_method_ref: null
  completed_time: null
  review_or_expiry_time: null
  status: demonstrated
  provenance_refs: []
  canon_status: proposed
```

A qualification record says that evidence exists. It does not grant access by itself.

Examples can eventually include completion of an authored field course, a documented prior assignment, a validated skill requirement, a supervised practical assessment or a public competitive result.

Do not invent Skill ranks, Features or mechanical competencies from a narrative certificate.

## Credential

```yaml
credential:
  credential_id: null
  holder_id: null
  issuer_id: null
  credential_type: null
  qualification_refs: []
  recognized_scope: []
  issued_time: null
  nominal_expiry_time: null
  status: ACTIVE
  physical_token_refs: []
  digital_record_refs: []
  recognition_links: []
  suspension_events: []
  revocation_events: []
  provenance_refs: []
```

Suggested status values:

- PENDING
- ACTIVE
- EXPIRED
- SUSPENDED
- REVOKED
- SUPERSEDED
- HISTORICAL
- DISPUTED

Expiry or revocation changes current validity. It does not erase that the credential once existed.

## Eligibility rule

Eligibility must be versioned because institutions can change their criteria.

```yaml
eligibility_rule:
  rule_id: null
  issuer_or_activity_id: null
  rule_version: null
  effective_from: null
  effective_until: null
  required_qualification_refs: []
  accepted_credential_types: []
  required_world_state: []
  required_record_refs: []
  disqualifying_state_refs: []
  supervision_options: []
  alternative_evidence_routes: []
  mechanics_review_required: false
  canon_status: proposed
```

The generator must never invent a hidden prerequisite after the player has already committed to an activity. Requirements should be discoverable unless secrecy is itself authored content.

## Eligibility assessment

```yaml
eligibility_assessment:
  assessment_id: null
  actor_id: null
  target_activity_or_access_id: null
  rule_id: null
  rule_version: null
  assessed_time: null
  assessor_id: null
  evidence_considered: []
  result: ELIGIBLE
  unmet_requirements: []
  accepted_conditions: []
  review_needed: false
```

Other possible results:

- INELIGIBLE
- PROVISIONALLY_ELIGIBLE
- PENDING_VERIFICATION
- ELIGIBLE_WITH_SUPERVISION
- NOT_APPLICABLE

An assessment records a decision made under one rule version. It should not be silently recomputed into history when criteria later change.

## Permission grant

```yaml
permission_grant:
  permission_id: null
  holder_ids: []
  grantor_id: null
  mandate_ref: null
  basis_refs: []
  action_scope: []
  location_scope_ids: []
  resource_scope_ids: []
  record_scope_ids: []
  start_time: null
  end_time: null
  use_limit: null
  supervision_requirement: null
  escort_or_host_ids: []
  conditions: []
  emergency_override: false
  status: ACTIVE
  suspension_events: []
  revocation_events: []
  provenance_refs: []
```

A permission grant should be narrow enough that the server can answer a concrete question.

Examples:

- may enter Survey Sector C until sunset;
- may inspect archive collection X while accompanied by curator Y;
- may access one tournament warm-up area during this event;
- may collect a named sample under a specific research project;
- may enter an infrastructure site during one emergency response.

Avoid `can_access_everything=true`.

## Admission token

Physical or digital tokens can represent an existing permission.

```yaml
admission_token:
  token_id: null
  permission_id: null
  holder_id: null
  issuer_id: null
  presentation_type: card|ticket|badge|wristband|key|digital_record|other
  valid_from: null
  valid_until: null
  remaining_uses: null
  transferability: nontransferable
  token_status: valid
```

A token is presentation state. The authoritative permission remains server-owned.

Hard rules:

- a stolen token does not create permission;
- a counterfeit token may fool an observer but does not create permission;
- losing a token does not necessarily erase the underlying grant;
- a stale token may look valid after the grant has expired;
- possession of a uniform does not prove membership or access.

This connects directly to the fashion and infiltration layers.

## Access checkpoint

Minecraft can present doors, gates, terminals, desks, rope lines, trailheads or NPC checks. The world authority should make the access decision.

```yaml
access_checkpoint:
  checkpoint_id: null
  location_id: null
  controlled_scope_id: null
  accepted_permission_types: []
  active_rule_ref: null
  verification_method: server_authoritative
  failure_routes: []
  supervised_entry_route: null
  emergency_route: null
  presentation_refs: []
```

Possible failure routes should be diegetic and recoverable when appropriate:

- request verification;
- obtain the missing qualification;
- contact host/issuer;
- use a public route instead;
- schedule a supervised visit;
- wait until a timed restriction ends;
- leave and return later.

Do not default to invisible walls for every failed check.

## Temporary access

Temporary permission is first-class world state.

Common scopes:

- one shift;
- one expedition;
- one event;
- one research window;
- one archive session;
- one maintenance job;
- one crisis response;
- one guided visit;
- one seasonal survey;
- one promotion challenge.

A temporary grant can expire naturally without anyone being punished or accused of wrongdoing.

## Supervised access

Some activities may be valid only while another actor is present.

```yaml
supervision_requirement:
  requirement_id: null
  permission_id: null
  supervisor_role_requirement: null
  accepted_supervisor_ids: []
  must_be_co_present: true
  valid_activity_scope: []
  handoff_allowed: false
```

Supervision should be authored because the institution has a reason for it. Do not add escort NPCs merely to slow the player down.

## Suspension and revocation

Suspension and revocation need causes and provenance.

Possible authored causes can include:

- qualification expired;
- required equipment unavailable;
- protected-area conditions changed;
- institution suspended a whole activity category;
- record verification failed;
- temporary role ended;
- emergency conditions changed;
- misconduct was established through an authored process;
- holder voluntarily surrendered the credential.

Do not infer misconduct simply because a credential became inactive.

A revocation event should store who acted, under which mandate, what scope changed and which source records support it.

## Emergency override

```yaml
emergency_access_grant:
  permission_id: null
  crisis_id: null
  holder_ids: []
  grantor_id: null
  emergency_scope: []
  location_scope_ids: []
  start_time: null
  termination_condition: null
  after_action_review_required: true
```

An emergency grant ends when its condition ends unless separately renewed. It does not become a permanent credential by repetition.

## Reciprocal recognition

Use the existing interregional layer rather than duplicating it.

A credential may be:

- fully recognized;
- recognized only for a narrow activity;
- accepted provisionally;
- accepted only with supervision;
- pending verification;
- not relevant to the host institution.

Example: a field-survey qualification from Region A may satisfy the safety-training component in Region B without granting automatic access to Region B's protected sites.

## Institutional roles

Employment, membership and access remain separate.

An employee may have no access to a restricted laboratory.

A visiting researcher may have lab access without employment.

A Gym Trainer may have arena access without authority over League policy.

A medic may have clinical competence without access to private case files outside their assignment.

A reporter may have press-area access without clinic-record access.

## Pokémon and institutional access

Do not treat Pokémon as equipment attached to a Trainer credential.

If Ouros later authors institutional Pokémon roles, keep separate:

- Pokémon identity;
- partnership/custody state;
- institutional role;
- access grant;
- mechanical Loyalty/Command state;
- observed cooperation.

A Trainer's credential must not silently transfer command authority over another institution's Pokémon.

## Privacy

Credentials can contain information with different visibility.

Potentially public:

- public tournament qualification;
- public institutional title;
- authored public award;
- public event admission status where appropriate.

Potentially restricted:

- clinic qualification review;
- private employment records;
- security clearance scope;
- protected-site access details;
- confidential research permissions;
- revocation evidence under active review.

The media layer may report a credential claim. Reporting does not determine validity.

## Integration with existing layers

Interregional mobility supplies recognition relationships.

Education supplies training and assessment evidence.

Workplaces supply occupational assignment and staffing state.

Conservation supplies visitor policy and protected-area scope.

Science supplies project/sample permissions.

Geology and archaeology supply excavation/site access needs.

Archives supply reading-room, restricted-record and collection access.

Cases supply per-case roles and evidence access.

Battle institutions supply event eligibility and challenge contracts.

Crisis supplies emergency override context.

Digital systems supply versioned records, audit logs and outage handling.

Infiltration supplies presented identity and observer belief without changing the authoritative grant.

## PTU/Caelo boundary

Narrative permission must never replace PTU legality.

If a site says only certified climbers may enter, the certification may authorize the expedition. It does not give the character a Climb capability, Athletics rank, movement bonus or Feature.

If Caelo explicitly requires a level, item or capability for a location, that exact requirement remains authoritative once re-verified against the source document. Pass 57 does not convert those requirements into general licenses.

Badges, Trainer ranks, Skills, Edges, Features, classes, items and Pokémon capabilities need their governing PTU/Caelo rules before they can be used as mechanical predicates.

## Minecraft authority boundary

Minecraft may show:

- gate state;
- credential icon;
- badge/card model;
- sign or notice;
- staff response;
- temporary visitor wristband;
- locked/unlocked door presentation;
- supervised-route marker.

The client must not decide permission by reading its own inventory or cosmetic state alone.

Preferred flow:

player requests entry → server resolves identity + current permission + scope + world state → server accepts/denies/offers alternate route → Minecraft presents result.

A future persistence/adapter service needs to own this access state. AutoPTU-Java should remain authoritative only for battle legality and battle results.

## Encounter contract A — Survey Annex Checkpoint

Narrative premise:

A field team reaches a research annex while an access record outage has made local physical passes unreliable. Some entrants are valid, some are pending verification, and a wild disturbance outside the building can escalate before the records are reconciled.

Full version:

The party may need to protect a verification station, move through controlled corridors, withdraw civilians or hold access lanes while the system recovers.

Capability dependencies:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: BLOCKING if protection/escort lanes are tactical;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING if alarms/doors/zones act inside battle;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

Reduced version:

Resolve credential verification completely in world state before battle. Keep civilians and controlled doors outside the grid. If a battle occurs, use a static arena and normal legal combat. Afterward, continue access reconciliation as narrative/persistence state.

## Encounter contract B — Seasonal Corridor Permit

Narrative premise:

A research team has valid temporary access to a migration corridor during a narrow survey window. Conditions change while they are inside, and the stewardship body must decide whether to shorten, supervise or preserve the permission.

Full version:

A tactical scene could require reaching an exit while avoiding a moving wild collective and protecting survey equipment without treating the Pokémon as enemies.

Additional blocking dependencies:

- complete movement/interception/forced movement;
- terrain/zones/reactions if corridor state affects the grid;
- AI tactical policy for autonomous retreat/route behavior;
- adapter/playback for world-to-battle state.

Reduced version:

The access window and collective movement stay in world state. If contact becomes a battle, freeze a legal static encounter. Withdrawal and permit expiry resolve outside the grid.

## Encounter contract C — Promotion Challenge Gate

Narrative premise:

A candidate has met the institution's eligibility criteria and receives one promotion challenge. The challenge result and the candidate's access state must remain separate.

Full version:

Can eventually support authored challenge objectives beyond defeat-all if the institution's format requires them.

Reduced version:

Use a normal legal static battle. The server records eligibility before battle, battle outcome from AutoPTU-Java, and any rank/credential consequence afterward. Do not grant mechanical bonuses because the candidate is being evaluated.

## Non-combat content opportunities

This layer can produce useful stories with no combat at all:

- reconstructing a damaged credential registry;
- observing a supervised practical assessment;
- comparing two legitimate recognition standards;
- finding that a physical pass is stale but the underlying permission is valid;
- helping an institution create an emergency-access procedure after a crisis;
- resolving a record mismatch after a name change;
- creating a safe public route so fewer visitors need restricted access;
- documenting why a temporary permit should expire normally instead of becoming permanent.

## Canon promotion checklist

Before any credential becomes canon:

1. Confirm the issuing institution exists in canon.
2. Confirm it has a mandate to recognize the qualification or grant the access.
3. Confirm the credential's exact scope.
4. Confirm prerequisites against PTU/Caelo if mechanical.
5. Confirm duration/expiry behavior.
6. Confirm privacy/publicity state.
7. Confirm interregional recognition if relevant.
8. Confirm Minecraft presentation does not become rules authority.
9. Confirm no badge, uniform or item is being treated as automatic proof.
10. Confirm the system does not create a universal license that was never authored.

## Open questions

- Does Ouros have any region-wide Trainer registration at all?
- What do League Badges formally prove outside their challenge circuit?
- Which field activities require institutional qualification?
- Which credentials are permanent, renewable or temporary?
- Can clubs or player-founded institutions issue recognized credentials?
- How does multiplayer consent work when one player's permission covers a group activity?
- What records can be verified across regions?
- Can a Pokémon hold a role or access grant independently of a Trainer?
- Which PTU/Caelo Skills, Features or capabilities can legitimately serve as prerequisites?
- How should access checks survive server outages without turning physical tokens into authority?