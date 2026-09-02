# Identity, Credential and Delegated Authority Continuity Layer

Status: DESIGN / PROPOSED ARCHITECTURE
Pass: 201
Date: 2026-09-02
Canon effect: NONE until explicit promotion.
Research basis: `research/2026-09-02-identity-credential-delegated-authority-scan-201.md`

## Purpose

Preserve who an actor is understood to be, what evidence supports that identification, what role or credential they present, and what bounded authority currently follows from it. This layer exists so visitors, institutions, pickups, field work, archive access and service handoffs can use durable identity without inventing a regional civil-ID or licensing system.

It reuses existing owners:

- canonical NPC identity remains in `canon/`;
- visitor presence and `temporary_access_grant` remain in the visitor layer;
- claims and their social circulation remain in pass 200;
- document/copy provenance remains in archive/provenance systems;
- service requests and work orders remain in pass 198;
- custody/ownership remain in their own layers;
- PTU/Caelo/AutoPTU remain authoritative for contested Guile, Perception, Features, Skills and other mechanics.

Pass 201 owns identity resolution references and bounded authority continuity between those systems.

## Canon anchors

Current canon already establishes:

- stable `npc_id` values for recurring residents;
- exact family relationships cannot be inferred from shared surnames;
- institutions have bounded ordinary responsibilities;
- Marea Field Office is not a police force;
- Bruma Battle Yard is not yet a Gym and grants no invented badge;
- mechanical permissions must be revalidated against the current PTU build;
- Minecraft actors project world state and cannot author identity/history through unload, death, duplication or pathing behavior.

These facts justify stable identity and narrow authority records. They do not authorize civil registries, passports, licenses or government structures.

## Core records

### `actor_identity_record`

```yaml
actor_identity_record:
  actor_id: null
  actor_kind: PERSON | POKEMON | INSTITUTION | GROUP
  canonical_name_ref: null
  display_name_history: []
  alias_claim_refs: []
  stable_world_refs: []
  provenance_refs: []
  canon_status: CANON_APPROVED | PROPOSED | UNRESOLVED
```

The stable actor ID survives presentation changes.

### `identity_assertion`

```yaml
identity_assertion:
  assertion_id: null
  claimant_actor_ref: null
  claimed_identity_ref: null
  asserted_name: null
  asserted_role: null
  asserted_at: null
  purpose_ref: null
  evidence_refs: []
  verification_refs: []
  current_state: SELF_ASSERTED | SUPPORTED | DISPUTED | UNRESOLVED
```

An assertion can be sincere and still unresolved.

### `identity_verification_event`

```yaml
identity_verification_event:
  verification_id: null
  subject_actor_ref: null
  verifier_actor_or_institution_ref: null
  purpose_ref: null
  checked_at: null
  evidence_refs: []
  result: SUFFICIENT_FOR_PURPOSE | INSUFFICIENT | CONFLICTING | NOT_REQUIRED
  scope_limits: []
  expiry_or_recheck_at: null
  notes: []
```

`SUFFICIENT_FOR_PURPOSE` must always name a purpose. It is not universal truth authority.

### `credential_record`

```yaml
credential_record:
  credential_id: null
  subject_actor_ref: null
  issuer_ref: null
  credential_type_key: null
  issued_at: null
  effective_from: null
  effective_until: null
  status: CLAIMED | ACTIVE | EXPIRED | REVOKED | SUPERSEDED | UNVERIFIED
  scope_refs: []
  artifact_refs: []
  provenance_refs: []
```

The repository must not invent credential types unless a slice actually establishes them.

### `authority_grant`

```yaml
authority_grant:
  grant_id: null
  subject_actor_ref: null
  granting_actor_or_institution_ref: null
  authority_domain_ref: null
  action_scope: []
  object_or_location_scope: []
  begins_at: null
  ends_at: null
  conditions: []
  source_credential_refs: []
  source_assignment_refs: []
  status: PROPOSED | ACTIVE | EXPIRED | REVOKED | COMPLETED
  provenance_refs: []
```

A visitor-layer `temporary_access_grant` can reference or specialize this structure instead of being duplicated.

### `delegation_record`

```yaml
delegation_record:
  delegation_id: null
  delegator_ref: null
  delegate_ref: null
  task_or_case_ref: null
  delegated_actions: []
  excluded_actions: []
  effective_from: null
  effective_until: null
  revocable: true
  status: OFFERED | ACTIVE | COMPLETED | EXPIRED | REVOKED
  evidence_refs: []
```

Delegation transfers only named actions for the stated purpose/window.

### `authority_check`

```yaml
authority_check:
  check_id: null
  actor_ref: null
  requested_action_ref: null
  target_ref: null
  checked_at: null
  applicable_grant_refs: []
  result: AUTHORIZED | NOT_AUTHORIZED | NEEDS_VERIFICATION | AMBIGUOUS
  decision_actor_or_system_ref: null
  provenance_refs: []
```

This record answers a world-facing permission question. It cannot grant a PTU Feature or bypass mechanically governed prerequisites.

## Hard boundaries

`SAME_DISPLAY_NAME != SAME_ACTOR`

`SAME_SURNAME != FAMILY_RELATIONSHIP`

`FAMILIAR_FACE != CURRENT_AUTHORITY`

`IDENTITY_ASSERTION != VERIFIED_IDENTITY_FOR_PURPOSE`

`CREDENTIAL_PRESENT != CREDENTIAL_VALID`

`CREDENTIAL_VALID != AUTHORIZED_FOR_EVERY_ACTION`

`ROLE_TITLE != UNIVERSAL_AUTHORITY`

`MEMBERSHIP != TASK_AUTHORITY`

`PRIOR_ACCESS != CURRENT_ACCESS`

`DELEGATION != TRANSFER_OF_OFFICE`

`DELEGATION != OWNERSHIP_TRANSFER`

`COPY_OF_AUTHORIZATION != CURRENT_AUTHORIZATION`

`SIGNATURE_OR_SEAL_PRESENT != AUTHENTICITY_PROVEN`

`EXTERNAL_CREDENTIAL != LOCAL_EQUIVALENCE_PROVEN`

`TRAINER_ID_OR_OT_DATA != CAELO_CIVIL_IDENTITY`

`MINECRAFT_USERNAME != CANONICAL_CHARACTER_IDENTITY`

`MINECRAFT_ENTITY_UUID != SOCIAL_OR_LEGAL_IDENTITY`

`MINECRAFT_SKIN_OR_UNIFORM != AUTHORITY`

`BATTLE_VICTORY != LICENSE_OR_OFFICE`

## Verification proportionality

Do not require maximum verification for every interaction.

Examples:

- ordinary introduction: self-asserted name may be enough;
- returning a low-stakes note to a known contact: contextual recognition may be enough;
- collecting a reserved or repaired object for another person: explicit delegation may matter;
- viewing bounded archive material: current access scope may matter;
- representing an institution in a consequential decision: issuer and scope should be inspectable.

The actual Caelo standard remains unresolved. This architecture only preserves the reasoning path once a local rule exists.

## Identity conflicts

When evidence conflicts, keep both records and open an identity-resolution case. Do not merge or split actors silently.

Useful conflict dimensions:

- same name, different provenance;
- changed name with continuity evidence;
- duplicate Minecraft actor for one canonical NPC;
- one physical artifact copied from another;
- outdated role title;
- visitor recognized from a previous trip but current purpose differs;
- external credential whose meaning is unknown locally.

## Delegation examples using existing canon

### Lia at the ferry landing

Lia can plausibly assign a bounded unloading or record-check action within her ordinary dock coordination responsibilities. This does not make the delegate the dock coordinator or grant authority over all ferry operations.

### Nerea and Ema

Ema can perform observation tasks under Nerea's project protocols. Observation work, review authority and publication authority should remain separable.

### Taro and Pia

Pia can circulate copies and retrieve sources. A courier assignment does not automatically grant Taro's archive-custody or interpretive authority.

### Sela and Jace

Jace can assist sessions and maintenance. That does not automatically make him manager of the Battle Yard or grant external League authority.

### Teo pickup

A work order can permit a named delegate to collect an item. The pickup permission does not itself settle ownership, payment or mechanical Item effects.

## Visitor integration

A repeat visitor retains stable identity history when evidence supports it, but every new visit can have a new purpose and access window.

The existing `temporary_access_grant` remains authoritative for the visit-specific permission. Pass 201 supplies identity and verification references that the grant may point to.

A previous successful visit can reduce uncertainty narratively, but expired access does not renew itself.

## Information-circulation integration

A claim that someone is an inspector, courier, researcher, owner or delegate remains an `information_claim` while circulating socially.

An `authority_check` may use direct evidence and conclude whether the actor may perform one action. That conclusion does not retroactively rewrite every rumor or every NPC's knowledge.

## PTU social-mechanics boundary

PTU 1.05 explicitly uses Guile for deception, posing and disguise, with Perception potentially opposing Guile to see through a disguise.

Therefore:

- contested impersonation cannot be solved by comparing Narrative confidence numbers;
- a convincing disguise does not rewrite `actor_id`;
- successful Guile can affect what an observer believes without changing underlying authority records;
- successful Perception can expose a discrepancy without automatically proving the actor's true identity;
- Features/Edges that modify these interactions remain PTU/Caelo/AutoPTU concerns.

## Pokémon identity/provenance boundary

Pokémon game OT/Trainer-ID structures demonstrate that visible name alone need not determine originating identity. For Ouros:

- persistent Pokémon keep stable Narrative identity when individually established;
- capture/ownership mechanics remain PTU/Caelo/AutoPTU governed;
- OT-like data may be referenced if the authoritative engine exposes it;
- Narrative must not invent a transfer of ownership from following behavior, party presentation or Minecraft tethering.

## Minecraft/Cobblemon projection

The adapter may display names, uniforms, badges, books, tags or access markers. It must read authoritative records rather than create them.

Required safeguards:

- duplicate NPC entities resolve to one persistent actor or are rejected;
- changing a skin does not change identity;
- changing a username/display name does not rewrite character history;
- carrying a visual badge item does not create an active credential;
- a stale sign/card can remain evidence of an old state while current authority differs;
- entity death/unload cannot expire or revoke authority unless the world clock/record independently does so;
- client localization cannot alter names, scope or permission state.

## Rich encounter pattern

### Authorized Recovery at Mirador Perimeter

Premise:
A bounded piece of field equipment or record package must be recovered from a route-side observation site. Nerea authorizes one person to retrieve it and another to carry it back. Wild activity complicates immediate withdrawal. The story tests scope: the recovery team may handle the named package without gaining general Mirador access or ownership.

Full intended dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement if protected withdrawal and displacement matter;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle where selected content needs it;
- terrain/weather/hazards/zones/reactions if terrain, weather or protected space is tactical;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy if wild actors must defend territory, withdraw or ignore the package;
- Minecraft/Cobblemon/Craftics adapter/playback support.

The authority record stays outside BattleSpec.

### Reduced version

Narrative resolves identity, delegation, package custody and the noncombatants before battle. Move the package and designated carriers into a safe semantic state if necessary. If one immediate wild actor still blocks withdrawal, compile one ordinary audited battle on stable geometry with verified content.

Allowed narrow handoffs:

- `IMMEDIATE_RECOVERY_ROUTE_CLEAR`
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_TEAM_CAN_WITHDRAW`

Battle output cannot determine:

- whether a credential is valid;
- whether a delegation exists;
- who owns the package;
- whether a carrier exceeded authority;
- permanent Mirador access;
- employment or membership;
- identity truth;
- whether an external credential is recognized;
- later relationship or disciplinary consequences.

## Generation rules

1. Use stable actor IDs for durable people/Pokémon/institutions.
2. Treat visible names/titles as presentation linked to identity.
3. Record verification purpose and scope.
4. Prefer narrow grants over generic `authorized=true` flags.
5. Preserve expiry, revocation and supersession history.
6. Reuse visitor access rather than duplicating it.
7. Keep delegation tied to a task/case.
8. Never infer family from surname.
9. Never infer ownership from custody, following behavior or visual proximity.
10. Defer contested disguise/deception to PTU mechanics.
11. Keep artifacts separate from the authority they claim to represent.
12. Do not invent regional credentials merely to make a quest work.
13. Keep Minecraft identity/presentation subordinate to authoritative Narrative IDs.
14. Keep battle outcomes out of civic/institutional authority.

## Canon promotion gate

Before promoting a specific use, resolve only what that slice needs. Open questions include:

- Caelo legal/civil identity rules;
- legal names and aliases;
- Trainer licensing;
- age/guardianship requirements;
- institutional credential formats;
- external credential recognition;
- signature/seal validity;
- delegation formality;
- revocation/appeal procedures;
- employment/agency law;
- proxy pickup standards.

None of those are established by this design.