# Ouros Digital Systems, Cyberspace & Data Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already models physical technology, communications, archives, visual evidence, identity, cases and persistent Pokémon. This layer defines the digital state that sits between those systems: software, records, versions, access, logs, backups, digital identities, service incidents and possible virtual spaces.

It does not define a universal technology level for Ouros. It does not create hacking rules. It does not make every computer network a dungeon.

The central rule is that digital representation and world truth remain separate.

## 1. Boundary with existing layers

The Technology/Energy layer owns physical machines, power, servers as assets, terminals, maintenance and technical faults.

The Media/Communications layer owns transmission, delivery, channels, coverage and publication.

The Archives layer owns institutional preservation, cataloging and retention of holdings.

The Photography layer owns visual-record semantics and visual evidence interpretation.

The Infiltration layer owns physical/social covert access.

The Pokémon Agency layer owns Pokémon identity, custody and partnership continuity.

This layer owns digital storage, software state, record versions, authorization, access events, virtual-space state and digital incident history.

## 2. Digital system

A digital system is a persistent logical service, not merely a physical machine.

```yaml
digital_system:
  system_id: null
  system_type: null
  operator_institution_id: null
  hosting_asset_ids: []
  service_role_ids: []
  current_release_id: null
  data_store_ids: []
  access_policy_ids: []
  external_interface_ids: []
  dependency_ids: []
  current_service_state: unknown
  incident_ids: []
  mechanical_rule_refs: []
  canon_reference_ids: []
```

Possible types include registry, scheduling service, research repository, public information system, battle archive, logistics service, access-control service, simulation service, library catalogue or local control network.

A system may move between physical hosts without changing its identity if canon says that architecture is supported.

## 3. Digital record

A record stores information. It does not establish truth by itself.

```yaml
digital_record:
  record_id: null
  semantic_type: null
  source_fact_ids: []
  claim_ids: []
  created_by_actor_id: null
  created_by_system_id: null
  created_at: null
  current_version_id: null
  storage_location_ids: []
  sensitivity: internal
  retention_state: active
  provenance_refs: []
  access_policy_id: null
  canonical_truth_authority: false
```

Examples:
- route record;
- patient scheduling entry;
- research measurement;
- tournament result mirror;
- maintenance log;
- staff roster;
- map edition;
- custody record;
- public notice draft;
- battle transcript copy.

When another layer already owns the semantic object, the digital record points to it instead of replacing it.

## 4. Version history

Edits create versions instead of silently rewriting history.

```yaml
record_version:
  version_id: null
  record_id: null
  parent_version_id: null
  created_at: null
  created_by_actor_id: null
  created_by_system_id: null
  change_summary: null
  source_refs: []
  superseded: false
  restored_from_snapshot_id: null
  integrity_claim_ids: []
```

A later correction can supersede an earlier value while the earlier version remains part of history.

This connects directly to Ouros public memory. A public institution may have once published an incorrect value even after its database is corrected.

## 5. Data store

```yaml
data_store:
  store_id: null
  system_id: null
  host_asset_ids: []
  record_ids: []
  replication_mode: unknown
  authoritative_scope: []
  backup_policy_id: null
  service_state: unknown
  last_verified_at: null
```

“Authoritative” is scoped. A tournament database may be authoritative for registrations while AutoPTU remains authoritative for battle resolution.

## 6. Access policy and grants

Possessing an account does not prove authorization for every action.

```yaml
access_policy:
  policy_id: null
  system_id: null
  resource_scope: []
  recognized_role_ids: []
  permitted_operation_types: []
  approval_requirements: []
  expiry_rules: []
  authored_authority_refs: []
```

```yaml
access_grant:
  grant_id: null
  subject_actor_id: null
  subject_institution_id: null
  digital_identity_id: null
  policy_id: null
  resource_scope: []
  granted_by_id: null
  granted_at: null
  valid_until: null
  revoked_at: null
  grant_reason_id: null
```

Narrative generation must not invent administrator rights because a character has high Technology Education, belongs to an institution, owns the physical terminal or controls a Rotom/Porygon.

## 7. Digital identity

```yaml
digital_identity:
  digital_identity_id: null
  handle_or_account_label: null
  claimed_actor_id: null
  verified_actor_link_state: unknown
  institution_id: null
  credential_ref_ids: []
  active_session_ids: []
  compromise_claim_ids: []
  public_profile_info_ids: []
  created_at: null
  retired_at: null
```

A handle is not a person.

An action performed through an account supports an attribution hypothesis. It does not automatically establish who physically used the account.

## 8. Digital event log

Logs are produced observations.

```yaml
digital_event_log_entry:
  log_entry_id: null
  system_id: null
  event_type: null
  recorded_at: null
  reported_actor_or_identity_id: null
  resource_ids: []
  operation_summary: null
  source_component_id: null
  collection_state: complete
  provenance_refs: []
```

Possible collection states:
- COMPLETE_FOR_SCOPE
- PARTIAL
- DELAYED
- GAPPED
- RECOVERED
- UNKNOWN

Absence from a log cannot automatically prove that an event did not happen.

## 9. Software release

```yaml
software_release:
  release_id: null
  system_id: null
  version_label: null
  authored_by_ids: []
  approved_by_ids: []
  deployed_at: null
  intended_changes: []
  actual_observed_changes: []
  known_issue_ids: []
  configuration_ref_ids: []
  rollback_target_release_id: null
  deployment_scope_ids: []
```

A release can work correctly in one environment and fail in another.

Unexpected Pokémon behavior near a software update is not enough to assign cause.

## 10. Backup and restore

```yaml
backup_snapshot:
  snapshot_id: null
  system_id: null
  captured_at: null
  record_version_refs: []
  software_release_id: null
  configuration_refs: []
  storage_location_ids: []
  verification_state: unknown
  retention_state: active
```

```yaml
restore_event:
  restore_id: null
  system_id: null
  snapshot_id: null
  initiated_by_ids: []
  started_at: null
  completed_at: null
  restored_scope: []
  records_lost_from_current_view: []
  reconciliation_required_ids: []
  resulting_service_state: null
```

Critical rule: restore changes current digital state. It does not erase Chronicle events, memories, publications, deliveries, physical consequences or facts that occurred after the snapshot.

## 11. Digital incident

```yaml
digital_incident:
  incident_id: null
  affected_system_ids: []
  first_observed_at: null
  observed_symptoms: []
  service_effect_ids: []
  suspected_cause_claim_ids: []
  confirmed_cause_ids: []
  evidence_ids: []
  containment_state: null
  recovery_state: null
  case_id: null
  technical_fault_ids: []
  public_information_ids: []
```

Potential causes may include configuration error, stale data, failed update, hardware fault, replication delay, operator mistake, Pokémon interaction, deliberate interference or unknown cause.

No cause is selected only because it creates a better mystery.

## 12. Virtual space

A virtual space requires explicit persistence and embodiment rules.

```yaml
virtual_space:
  virtual_space_id: null
  hosting_system_ids: []
  physical_dependency_ids: []
  access_interface_ids: []
  persistence_mode: null
  active_instance_ids: []
  actor_projection_rules_ref: null
  pokemon_interaction_rules_ref: null
  state_store_ids: []
  exit_or_recovery_paths: []
  access_policy_id: null
  current_incident_ids: []
  canon_reference_ids: []
```

Suggested persistence descriptions:
- EPHEMERAL_INSTANCE
- RESETTABLE_INSTANCE
- SNAPSHOT_PERSISTENT
- ACTOR_PERSISTENT
- WORLD_STATE_PERSISTENT

These labels describe architecture, not metaphysics.

Before a virtual space becomes canon, authors must answer:
- What physically happens to the participant?
- What remains in the physical world?
- What persists after disconnect?
- Can multiple actors share the same state?
- What happens if the host fails?
- How does the actor exit?
- Which injuries or battle states cross the boundary?
- Which PTU rules govern Pokémon interaction there?

## 13. Virtual-space anti-sequence-break rule

Digital entry cannot automatically bypass:
- physical route requirements;
- custody;
- ownership;
- Gym/League qualification;
- protected-site access;
- faction authorization;
- medical/privacy restrictions;
- item possession;
- world consequences.

A virtual representation of a locked archive is not permission to read the physical archive.

## 14. Porygon as digital actor

Official Pokémon material supports Porygon moving through cyberspace. Ouros may use that fact as a species-grounded narrative capability only at a high level until PTU/Caelo mechanics are validated.

```yaml
digital_pokemon_interaction:
  interaction_id: null
  pokemon_entity_id: null
  system_id: null
  observed_entry_event_id: null
  observed_exit_event_id: null
  authorized_scope_ids: []
  observed_actions: []
  inferred_actions: []
  mechanical_rule_refs: []
```

Entering a system never creates universal read/write/admin rights.

Porygon remains a persistent Pokémon entity. It cannot be duplicated because a database was copied.

## 15. Porygon2 and autonomous interpretation

A digital Pokémon can act outside an institution’s expectations without the system immediately classifying that event as malfunction.

Allowed states include:
- expected operation;
- unexpected but harmless behavior;
- adaptive behavior under review;
- mechanical malfunction confirmed by evidence;
- external interference confirmed by evidence;
- unresolved.

Private thoughts or motives are not generated from system logs alone.

## 16. Rotom boundary

The Technology layer may record a Rotom interacting with a physical device.

The Digital layer records only observed consequences to services/data.

Rotom presence does not imply:
- credential bypass;
- data comprehension;
- remote network reach;
- access to every connected device;
- ability to edit any record.

Exact mechanics require PTU/Caelo validation.

## 17. Pokémon storage guardrail

Official Pokémon games contain digital-style Box interfaces. Ouros must decide its own storage technology and metaphysics in canon.

Until then:
- a Pokémon is never treated as a file;
- a backup cannot restore a lost Pokémon;
- copying a database cannot clone a Pokémon;
- deleting a record cannot delete the Pokémon;
- party/custody changes remain authoritative Pokémon-state events;
- digital records may point to a Pokémon entity without owning that identity.

## 18. Data conflict and reconciliation

Distributed institutions may hold different legitimate versions of a record.

```yaml
data_reconciliation:
  reconciliation_id: null
  subject_record_ids: []
  conflicting_version_ids: []
  shared_ancestor_version_id: null
  factual_conflict_ids: []
  formatting_only_conflicts: []
  adjudicating_actor_ids: []
  merged_version_id: null
  unresolved_claim_ids: []
  completed_at: null
```

A merge should not fabricate certainty when the underlying facts remain disputed.

## 19. Privacy and multiplayer

Digital information uses the project’s actor-knowledge boundary.

Private player communications, medical data, unreleased research, private notes, coverage locations and hidden character facts cannot become globally visible because another player accesses the same terminal.

Access logs may record that a player opened a resource when canon says logging exists. They do not expose what the player privately thought about it.

## 20. Digital evidence and cases

Digital evidence follows the Case/Custody layer.

Important distinctions:
- original record;
- copied record;
- export;
- screenshot;
- restored version;
- reconstructed log;
- analyst interpretation.

A copied file can be authentic while incomplete.

A manipulated export does not imply the source database was manipulated.

## 21. Cybersecurity abstraction rule

Ouros narrative generation should use abstract operations such as:
- REQUEST_ACCESS
- VERIFY_CREDENTIAL
- ISOLATE_SYSTEM
- RESTORE_SNAPSHOT
- COMPARE_VERSIONS
- REVIEW_LOGS
- REVOKE_ACCESS
- SWITCH_TO_FALLBACK
- EXPORT_RECORD

Do not generate real exploit instructions, passwords, brute-force procedures, malware recipes or practical intrusion techniques.

If PTU/Caelo later defines relevant checks, those checks govern resolution.

## 22. Digital dungeons

A virtual/digital dungeon can use:
- access segments;
- versioned environments;
- broken references;
- archived sectors;
- isolated processes;
- service dependencies;
- conflicting simulations;
- historical snapshots;
- corrupted presentation layers;
- Porygon-specific traversal opportunities when mechanically validated.

Every digital dungeon should define:
- persistence mode;
- physical host/dependencies;
- exit/recovery route;
- player-access boundary;
- what world changes can legally write back;
- what is only simulation;
- exact AutoPTU dependencies.

Do not use endless “glitch” visuals as a substitute for navigable logic.

## 23. Minecraft representation

Minecraft/Cobblemon can present:
- terminals;
- server rooms;
- screens;
- public kiosks;
- data archives;
- maintenance consoles;
- virtual-space instances or dimensions if implemented;
- service-state indicators;
- access doors;
- backup/restore visualizations;
- Porygon/Rotom presence.

The adapter must not become authority for PTU effects, access legality, Pokémon identity or battle outcomes.

## 24. Encounter contract — Server Room Failover

Narrative premise: a critical service is unstable while a physical disturbance makes the operators switch to a fallback host.

FULL version:
- operators and combatants share a constrained technical space;
- terminals have explicit objective state;
- some zones can become unsafe if governing rules support them;
- opponents understand PROTECT/REACH/ACTIVATE-style objectives;
- world state receives authoritative service and battle results.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED version:
The failover decision and terminal interaction happen in overworld/world state. If a battle occurs, AutoPTU receives a static legal arena. The service outcome is written after both operations resolve.

## 25. Encounter contract — Porygon Diagnostic Dive

Narrative premise: a persistent Porygon enters a damaged digital environment to trace inconsistent records while Trainers coordinate from outside or through an authored virtual interface.

FULL version:
- digital space is an actual playable instance;
- Porygon has validated cyberspace movement/interactions;
- access gates change with data state;
- legal Move/Ability effects operate inside the instance only where PTU rules support them;
- exit and failure behavior are deterministic.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED if combat occurs;
- base movement legality — VERIFIED for ordinary battle movement only;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- full turn/round lifecycle — PARTIAL;
- AI tactical policy — BLOCKING for diagnostic/objective behavior;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- exact PTU/Caelo Porygon digital interaction — UNRESOLVED SOURCE GATE.

REDUCED version:
Cyberspace investigation is resolved as world-state research with explicit source gates. Any combat happens in a separate static legal arena. Porygon receives no invented movement or access bonus.

## 26. Encounter contract — Archive Restore Conflict

Narrative premise: two valid data branches exist and a failing institution must decide what to restore while a physical confrontation threatens the archive.

FULL version:
- protect/activate objectives;
- interactable restoration nodes;
- objective-aware opponents;
- possible zone/hazard behavior if mechanically supported;
- battle result and restore result remain separate authoritative outputs.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- action economy/initiative — VERIFIED;
- terrain/weather/hazards/zones/reactions — BLOCKING when used;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED version:
Players choose and document the restoration outside the grid. A conventional battle may secure the room. The chosen backup then changes current digital state without deleting post-snapshot Chronicle events.

## 27. Rules guardrails

Narrative generation must not invent:
- hacking DCs;
- passwords;
- intrusion bonuses;
- digital damage;
- cyberspace movement speeds;
- Porygon admin powers;
- Rotom network powers;
- virtual-world injury rules;
- Pokémon duplication/storage metaphysics;
- data-transfer speeds;
- cybernetic Features;
- software-derived combat modifiers.

Required rules sources remain PTU/Caelo plus current AutoPTU implementation evidence.

## 28. Canon promotion checklist

Before promoting any digital system or virtual space:

1. Define its regional technology assumptions.
2. Identify operator and physical dependencies.
3. Define persistence mode.
4. Define access and privacy rules.
5. Define Pokémon interaction rules from PTU/Caelo.
6. Define backup/restore consequences.
7. Define which records are authoritative for which scope.
8. Define Minecraft representation.
9. Record exact battle capability dependencies.
10. Verify that no digital mechanic silently bypasses existing world-state systems.
