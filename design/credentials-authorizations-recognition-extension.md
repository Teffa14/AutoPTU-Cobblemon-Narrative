# Credentials, Authorizations & Recognition Extension

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already tracks qualifications, roles, enrollment, invitations, recognition claims, service access, issued equipment and public records. This extension adds a common lifecycle for credentials and scoped authorizations without inventing universal licenses, passports, permits or legal systems.

The layer owns evidence that an institution issued, recognized, suspended, expired, replaced or revoked a scoped authorization. The specialist system still owns the underlying right or qualification.

## Core separation

Keep these concepts distinct:

- actor identity;
- qualification evidence;
- institutional role;
- authorization scope;
- credential representation;
- recognition by another institution;
- physical possession of a credential;
- current validity;
- public display fields;
- PTU mechanical state.

A valid-looking card is not enough. A current issuer record is not automatically a PTU Feature. A completed course is not automatically legal authority.

## Credential record

```yaml
credential_record:
  credential_id: null
  subject_actor_id: null
  issuer_institution_id: null
  credential_type_ref: null
  issued_time: null
  effective_from: null
  effective_until: null
  status: issued
  authorization_scope_ids: []
  qualification_refs: []
  role_refs: []
  public_projection_ref: null
  supersedes_credential_id: null
  superseded_by_credential_id: null
  source_refs: []
  visibility: private_or_authored
```

Suggested lifecycle states:

- DRAFT
- PENDING_VERIFICATION
- ISSUED
- ACTIVE
- SUSPENDED
- EXPIRED
- REVOKED
- SUPERSEDED
- LOST_REPORTED
- REPLACED
- ARCHIVED

Do not use REVOKED merely because an actor failed a scene. Revocation requires an authored policy, decision and provenance.

## Authorization scope

```yaml
authorization_scope:
  scope_id: null
  issuer_institution_id: null
  subject_actor_id: null
  resource_or_activity_refs: []
  location_scope_refs: []
  action_scope: []
  supervision_requirement: null
  valid_window: null
  dependency_refs: []
  exclusions: []
  status: active
  decision_ref: null
```

A scope can authorize one narrow task without granting broad institutional power.

Examples, only when canon supports the underlying institutions:

- enter one protected survey site;
- use one laboratory room;
- conduct one supervised practicum;
- participate in one formal battle event;
- access one staff-only work area;
- borrow one equipment class;
- act in one temporary crisis role.

## Credential representation

```yaml
credential_representation:
  representation_id: null
  credential_id: null
  medium: card|badge|paper|token|device|registry_entry|other
  serial_or_instance_ref: null
  issued_time: null
  replaced_time: null
  physical_item_ref: null
  display_fields: []
  current_representation: true
```

The physical object belongs to Material Culture or Shared Equipment when relevant. This layer only connects it to the authorization record.

Destroying a card does not automatically revoke the authorization. Finding an old card does not reactivate it.

## Public projection

```yaml
public_credential_projection:
  projection_id: null
  credential_id: null
  publishable_identity_fields: []
  publishable_qualification_fields: []
  publishable_status_fields: []
  generated_time: null
  revision: null
```

Never expose private clinic, academic, case, roster, inventory, housing or relationship data through a credential unless an explicit policy says that exact field is public.

## Verification event

```yaml
credential_verification_event:
  verification_id: null
  credential_id: null
  presented_representation_id: null
  verifier_actor_or_system_id: null
  requested_scope_ref: null
  issuer_record_checked: true
  result: valid_for_scope|valid_but_insufficient|expired|suspended|revoked|superseded|unverified|mismatch
  evidence_refs: []
  time: null
```

`valid_but_insufficient` is important. A genuine credential can be irrelevant to the requested action.

## Recognition by another institution

Use the existing interregional recognition system as authority. This extension adds a credential-specific projection:

```yaml
credential_recognition:
  recognition_id: null
  credential_id: null
  receiving_institution_id: null
  authenticity_result: confirmed|pending|not_confirmed
  local_scope_result: full|limited|provisional|not_sufficient|irrelevant
  additional_requirement_refs: []
  review_time: null
  decision_ref: null
```

Authentication and local equivalency are separate decisions.

## Temporary authorization

```yaml
temporary_authorization:
  authorization_id: null
  issuer_institution_id: null
  subject_actor_ids: []
  purpose_ref: null
  location_scope_refs: []
  action_scope: []
  start_time: null
  end_time: null
  supervision_ref: null
  automatic_end_condition_ref: null
  status: offered
```

Temporary access should end explicitly. It must not silently become permanent because the actor used it successfully.

## Emergency scope

A crisis may justify a temporary scope only if the owning institution or an authored emergency policy grants it.

Possible state sequence:

`requested -> reviewed -> issued -> active -> ended -> archived`

The narrative generator cannot create emergency authority merely because a scene would be easier with it.

## Suspension and review

Suspension is a temporary status, not a finding of guilt.

```yaml
credential_status_change:
  change_id: null
  credential_id: null
  from_status: null
  to_status: null
  reason_claim_refs: []
  authority_decision_ref: null
  effective_time: null
  review_due: null
  notification_refs: []
```

Case allegations, rumors and public controversy cannot alter status unless the responsible system records an actual decision.

## Expiry and renewal

Ouros has not established which credentials expire. Therefore expiry must be data, never default behavior.

If a credential does expire, renewal may require:

- updated record verification;
- current role assignment;
- new supervised practice;
- local orientation;
- refreshed equipment training;
- no additional requirement at all.

The exact rule belongs to the issuing institution.

## Replacement

Replacement should preserve history.

```yaml
credential_replacement:
  replacement_id: null
  old_credential_or_representation_ref: null
  new_credential_or_representation_ref: null
  trigger: lost|damaged|administrative_update|scope_change|format_change|other
  old_status_after_replacement: superseded
  decision_ref: null
  time: null
```

Found Property can later recover the old representation without reactivating it.

## Role and credential boundary

A workplace role may require a credential, but possessing the credential does not prove current employment.

A staff member can leave a role while retaining a historical qualification. A temporary worker can hold an active role scope without a permanent professional title.

## Education boundary

Completion records remain owned by Education. This layer can issue a credential that references such evidence only when the institution actually has an authored credential policy.

No diploma or certificate grants PTU Skills, Edges, Features or mechanical competence by itself.

## Battle institution boundary

Battle Institutions own qualification nodes, challenge eligibility, formats and progression effects.

This layer may represent a public credential or entry authorization referencing those records. It cannot invent Badge thresholds, ranking points, roster legality or participation rules.

## Conservation and science boundary

Protected-site or sample-handling authorization must reference Conservation/Science state. A research credential cannot imply universal access to every ecological site.

## Service access boundary

Service Access owns queue/appointment allocation. A credential may satisfy one prerequisite but does not reserve a slot, skip a queue or establish priority.

## Shared equipment boundary

A credential can prove eligibility for a lending pool if policy says so. Actual checkout, custody and return remain owned by Shared Equipment.

## Minecraft representation

Possible visible forms:

- card or badge item;
- staff lanyard analog if canon supports it;
- temporary wrist/token analog for an event;
- desk verification interaction;
- gate reader or registry terminal if technology supports it;
- wall display of publicly recognized qualifications;
- replaced credential returned as historical/found property;
- visitor authorization attached to an existing institutional visit.

Minecraft item possession must never be the sole authority check.

## Narrative patterns

### Authentic but obsolete

A recovered credential is genuine but superseded. The holder may be acting in good faith because they never received the replacement notice.

### Valid elsewhere, limited here

A host confirms an external qualification but grants only supervised local access until orientation is complete.

### Temporary scope ends mid-project

A project runs longer than expected. The team must renew, change supervision or hand off the work instead of silently extending access.

### Emergency authorization audit

After a crisis, temporary scopes are reviewed. Some end, some are archived, and any permanent staffing decision goes through the owning workplace/institution system.

### Public credential, private record

A public profile proves participation or qualification while detailed assessment evidence remains private.

## Encounter: Restricted Facility Evacuation

Narrative premise:

An incident occurs inside an area where different actors have different access scopes. The scene should preserve evacuation and authorization boundaries without making credentials tactical buffs.

FULL dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING when evacuation lanes are tactical
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL, strengthened by live StatusController envelope wiring
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if facility hazards matter mechanically
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL and mechanic-specific; credential state never substitutes for them
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING
- tactical EVACUATE/PROTECT/ACCESS objective semantics: not verified

Reduced version:

The overworld layer verifies who was present and evacuates all noncombatants before battle instantiation. AutoPTU receives a static legal arena. Access decisions remain world state and are not combat modifiers.

## Encounter: Field Authorization Interrupted

Narrative premise:

A supervised field team with valid temporary access encounters wild activity while performing an approved task.

FULL dependencies:

- targeting/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: BLOCKING if retreat/interception is tactical
- calculations and action economy: VERIFIED
- lifecycle/damage/status: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if field conditions enter tactical state
- move/ability/item/Trainer Feature families: PARTIAL per exact content
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

Reduced version:

Authorization, supervision and site boundaries remain overworld state. If battle is necessary, it occurs in a reviewed static arena using only supported mechanics. The result does not expand the authorization scope.

## Engine readiness note — Pass 71

AutoPTU-Java head inspected: `87ee4652b8d1d123f6b1180bf4f652053d40cb73`.

New live evidence wires the shared StatusController phase envelope into TURN_START and PHASE_CHANGE lifecycle hooks and tests status-skip propagation. This is meaningful lifecycle/status progress.

The Java README still marks as pending:

- core combatant/grid battle state;
- full damage resolution;
- full status controller, terrain, hazards, forced movement and reactions;
- move/ability/item/perk/Trainer Feature registries;
- semantic BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

No permanent capability category is promoted in this pass.

## Promotion checklist

Before any credential becomes canon:

1. Confirm issuer exists.
2. Confirm issuer has authority for that exact scope.
3. Confirm subject and identity provenance.
4. Confirm underlying qualification/role/access evidence.
5. Define public and private fields.
6. Define expiry, if any.
7. Define replacement/suspension/revocation policy, if any.
8. Define recognition by other institutions only where authored.
9. Keep physical representation separate from current validity.
10. Validate any combat-facing effect against PTU/Caelo and current engine support.

## Open questions

Ouros still has no established universal Trainer license, professional licensing regime, permit system, credential technology standard or cross-region equivalency framework. These remain canon decisions rather than defaults.
