# Death, Bereavement, Funerary and Memorial Continuity Extension

Status: PROPOSED ARCHITECTURE — NON-CANON UNTIL APPROVED
Pass: 165

## Purpose

This extension gives Ouros a persistent, provenance-aware way to represent mortality reports, confirmed death, remains status, funerary activity, resting places and bereavement-related acts without conflating them with battle defeat, public reputation, spiritual truth or physical presentation.

It fills the lifecycle gap between care before death and the already-existing layers that preserve family consequences, rituals, memorial objects, archives and public memory afterward.

## Authority boundary

Ouros owns authored world facts and continuity.

AutoPTU owns tactical battle state and verified PTU resolution.

Minecraft, Cobblemon and Craftics display already-established facts and play back authoritative results. They do not decide mortality.

This extension owns only the mortality/funerary continuity surface. It links outward instead of duplicating adjacent systems.

Public Memory owns collective remembrance, public narratives and event legacy.

Ritual / Tradition owns inherited observances and their transmission.

Myth / Archaeology / Sacred Sites owns sacred claims, archaeology and uncertain supernatural interpretations.

Family / Kinship owns relationship status and family structure.

Material Culture owns the physical history of markers, urns, monuments, keepsakes and funerary objects.

Archives owns later preservation and access to records.

Health / Care owns injury, treatment and stabilization before a canonical death is established.

## Core invariants

`DEFEATED != DEAD`

`FAINTED != DEAD`

`DEATH_REPORTED != DEATH_CONFIRMED`

`MISSING != DEAD`

`PRESUMED_DEAD != CONFIRMED_DEAD`

`REMAINS_UNRECOVERED != SURVIVED`

`GRAVE_EXISTS != REMAINS_PRESENT`

`MEMORIAL_EXISTS != DEATH_PROVEN`

`FUNERAL_HELD != PUBLIC_MEMORY_UNIFORM`

`MOURNING_PRACTICE != INNER_EMOTION`

`MEMORIALIZED != CANONICAL_HEROISM`

`SPIRITUAL_CLAIM != WORLD_FACT`

`GHOST_TYPE != IDENTIFIED_DECEASED_ENTITY`

`GHOST_LIKE_APPEARANCE != IDENTIFIED_DECEASED_ENTITY`

`BATTLE_WON != KILL`

`BATTLE_DEFEAT != DEATH`

`REVIVE_USED != RESURRECTION`

`MINECRAFT_ENTITY_DESPAWN != DEATH`

`COBBLEMON_FAINT != DEATH`

`TOMBSTONE_BLOCK != CANONICAL_GRAVE`

## Proposed records

### mortality_status_assertion

Fields:

- `subject_ref`
- `asserted_status`
- `asserted_at`
- `effective_time_if_known`
- `source_ref`
- `source_role`
- `authority_basis`
- `confidence`
- `supersedes_assertion_ref`
- `privacy_scope`
- `notes`

Allowed status vocabulary should remain small and explicit:

- `ALIVE`
- `MISSING`
- `PRESUMED_DEAD`
- `CONFIRMED_DEAD`
- `UNKNOWN`

A status assertion records what an authorized or cited source asserted. Only a canon-approved assertion may promote Chronicle mortality state.

### death_report

Preserves a report independently of whether the report later proves correct.

Fields:

- `report_ref`
- `subject_ref`
- `reporting_actor_or_institution_ref`
- `reported_at`
- `claimed_death_time`
- `claimed_cause_if_stated`
- `evidence_refs`
- `distribution_scope`
- `current_report_status`
- `correction_ref`

Suggested statuses:

- `UNVERIFIED`
- `CORROBORATED`
- `CONFIRMED`
- `DISPUTED`
- `RETRACTED`
- `SUPERSEDED`

A retracted report remains historical evidence that the report existed.

### death_event

Created only when authored canon or an approved authoritative process establishes that a death occurred.

Fields:

- `death_event_ref`
- `subject_ref`
- `time_or_range`
- `place_ref_if_known`
- `confirmation_basis_refs`
- `cause_statement_ref_if_any`
- `cause_certainty`
- `visibility_scope`
- `chronicle_event_ref`

Cause may remain unknown even when death is confirmed.

### remains_status_record

Fields:

- `subject_ref`
- `status`
- `recorded_at`
- `evidence_refs`
- `location_ref_if_known`
- `identity_confidence`
- `supersedes_ref`

Possible statuses:

- `NOT_APPLICABLE_OR_NOT_RECORDED`
- `UNRECOVERED`
- `RECOVERED_IDENTITY_UNCONFIRMED`
- `RECOVERED_IDENTITY_CONFIRMED`
- `TRANSFERRED`
- `DISPOSED_ACCORDING_TO_AUTHORED_PRACTICE`
- `LOCATION_UNKNOWN`

Do not force all cultures or species into one physical-remains model.

### remains_custody_episode

Fields:

- `remains_or_container_ref`
- `custodian_ref`
- `custody_started_at`
- `custody_ended_at`
- `handoff_ref`
- `purpose`
- `documentation_refs`

Custody records responsibility for a period. It does not assert ownership.

### funerary_intent

Preserves a stated preference, family request, institutional plan or community proposal before execution.

Fields:

- `intent_ref`
- `subject_ref`
- `stated_by_ref`
- `stated_at`
- `requested_practice_ref`
- `requested_site_ref`
- `authority_or_relationship_basis`
- `current_status`

`FUNERARY_INTENT != FUNERARY_EPISODE_OCCURRED`

### funerary_episode

Records an observed or canon-approved funerary event.

Fields:

- `episode_ref`
- `subject_ref`
- `episode_type`
- `time_range`
- `site_ref`
- `participant_refs_or_aggregates`
- `practice_refs`
- `remains_status_ref_if_relevant`
- `source_refs`
- `public_visibility`

The episode records what happened. Ritual meaning belongs to the ritual/sacred authorities.

### resting_place_record

Fields:

- `resting_place_ref`
- `subject_ref`
- `site_ref`
- `marker_object_ref_if_any`
- `remains_presence_status`
- `established_at`
- `relocation_history_refs`
- `access_scope`
- `source_refs`

`resting_place_record` can represent a grave, tomb, niche, cenotaph, symbolic marker or other authored form without assuming every culture uses burial.

### bereavement_observation

Records observable mourning-related behavior without inventing internal emotional truth.

Fields:

- `actor_ref`
- `subject_or_event_ref`
- `observed_action`
- `time_range`
- `place_ref`
- `source_ref`
- `visibility_scope`

Examples include visiting, maintaining a marker, carrying an object, attending a ceremony, declining an invitation, making a public statement or performing an authored observance.

Do not generate a numeric grief score.

### memorial_link

Links mortality continuity outward to Public Memory and Material Culture.

Fields:

- `subject_or_death_event_ref`
- `public_memory_record_ref`
- `material_object_ref_if_any`
- `established_at`
- `link_basis`

The memorial layer decides collective interpretation. This record only maintains referential continuity.

### mortality_record_revision

Fields:

- `revision_ref`
- `target_record_ref`
- `revision_type`
- `reason`
- `evidence_refs`
- `effective_at`
- `authoritative_actor_ref`

Examples:

- correction of identity;
- correction of date;
- retraction of a premature report;
- changed cause confidence;
- location update for remains;
- marker relocation.

Earlier records remain visible with superseded status.

## State progression

A safe default progression is:

`ALIVE -> MISSING -> PRESUMED_DEAD -> CONFIRMED_DEAD`

but no step is automatic and intermediate states may be skipped when authoritative evidence warrants it.

A false report can produce:

`ALIVE + DEATH_REPORT(UNVERIFIED) -> DEATH_REPORT(RETRACTED)`

without ever changing Chronicle mortality state.

A confirmed death can have:

`CONFIRMED_DEAD + REMAINS_UNRECOVERED`

for an indefinite period.

A memorial can be established while status remains `MISSING` or `PRESUMED_DEAD` if canon says the community created one. The memorial itself cannot upgrade mortality status.

## Battle integration

Battle events can supply evidence only within their contract.

A normal AutoPTU result may establish HP, Fainted state, injuries or other implemented tactical outcomes. Narrative must not translate those into death unless an exact PTU/Caelo mortality rule has been verified and executed by the authoritative engine path.

Until then:

`AUTOPTU_FAINTED -> narrative subject remains alive/unknown according to existing canon`

No adapter-side death inference is permitted.

If future engine work implements mortality, the interface should return an explicit authoritative mortality event or rule result, not require Narrative to reverse-engineer death from HP numbers.

## Pokémon-specific boundary

Ghost-type Pokémon are creatures with their own canonical biological/world status. Type never proves that an encountered Pokémon is a deceased person or deceased Pokémon.

If canon establishes a specific spirit, apparition or returned deceased entity, represent that through an authored identity / supernatural-world fact with provenance. Do not infer it from species, particles, model, nameplate or location.

Revive-like items and Fainted recovery remain battle/recovery mechanics. Their existence does not imply resurrection from canonical death.

## Physical-site boundary

Minecraft blocks and entities can present graves, markers, urns, flowers, bells, paths and cemetery vegetation after Ouros establishes those objects and states.

A changed block layout can be evidence only when the authoritative world-event pipeline records the change. Client rendering alone cannot relocate a grave, destroy a memorial or disturb remains.

Cemetery maintenance can use Infrastructure / Material Culture / Workplaces as appropriate. This extension stores the mortality/resting-place relationships, not maintenance simulation.

## Privacy

Death records can contain sensitive personal information. Access should be field- or record-scoped.

Public marker text may be public while identity evidence, remains location, family requests or disputed cause information remains restricted.

An archive becoming accessible later does not retroactively make every earlier private record public at the time it was created.

## Generator guardrails

The generator may propose a death only when authoring policy for that subject permits it.

The generator must not kill a persistent NPC or Pokémon merely to create drama, motivate another character, explain absence or produce a quest hook.

Prefer nonfatal loss, separation, retirement, relocation, missing status, institutional change or ordinary aging when those satisfy the narrative purpose.

For existing canon entities, any mortality transition requires explicit canon authority.

Do not generate afterlife doctrine from generic funeral scenes.

Do not make every cemetery haunted.

Do not make every bereaved character seek revenge.

Do not make every memorial flattering or accurate.

## Integration examples

A former Gym Leader dies years after retirement. Civic Office already records the end of office; Employment/Workplaces already record career history. This extension records the death and funeral. Public Memory later records competing narratives about the Leader's legacy.

A Trainer disappears during a remote expedition. Travel/Exploration records last known movement; this extension records `MISSING`. A memorial service can occur while the subject remains missing. Search results do not promote to confirmed death without evidence.

A Pokémon companion dies through an authored non-battle event. Family/Social Bonds retains relationship history. Material Culture can preserve a collar or ribbon. Public Memory may never know. A private resting place can still persist for decades.

A cemetery is moved during redevelopment. Infrastructure/Urban Planning owns the project; Material Culture owns marker relocation; this extension updates resting-place and remains-location links with provenance. Public Memory may later debate the decision.

## Canon status

This architecture is proposed. It creates no deaths, cemeteries, funerals, religions or memorial customs by itself.