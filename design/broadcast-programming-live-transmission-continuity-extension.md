# Broadcast Programming & Live Transmission Continuity Extension

Status: PROPOSED ARCHITECTURE
Canon effect: NONE until individually approved
Pass: 161
Date: 2026-08-31

## Purpose

Ouros already knows how information exists, how it is published, how communication networks carry it, how public memory forms, how performances occur and how recordings can enter archives. This extension preserves the missing continuity of recurring broadcasts themselves: programs, editions, presenter tenures, scheduled slots, live and prerecorded components, concrete transmissions, regional variants, interruptions, overrides, rebroadcasts and archive links.

The design supports radio, television, public video, institutional broadcast, livestream-like channels and future authored equivalents without deciding which technologies exist in every Ouros region.

## Authority boundaries

Media/Communications retains authority over information packets, claims, publication framing, correction lineage, audience receipt and actor knowledge.

Communications Network retains authority over physical/logical distribution topology, service sectors, relay paths, reroutes, endpoint readiness and restoration.

Archives retains authority over preserved recording objects, custody, catalog, condition and access.

Performance continuity retains authority over artistic works and staged performances being covered by a broadcast.

Battle Institutions and AutoPTU retain authority over formal battle contracts and tactical results.

Public Memory retains authority over what communities later remember.

This extension owns only the continuity of the broadcast product and its transmission history.

## Core principle

A program, an episode, a transmission and a received viewing/listening event are different persistent facts.

`PROGRAM_EXISTS != EPISODE_PRODUCED`

`EPISODE_PRODUCED != TRANSMISSION_OCCURRED`

`TRANSMISSION_OCCURRED != AUDIENCE_RECEIVED`

`AUDIENCE_RECEIVED != AUDIENCE_BELIEVED`

## Broadcast program

```yaml
broadcast_program:
  program_id: null
  public_title: null
  operator_institution_ref: null
  program_kind: null
  primary_channel_refs: []
  recurring_format_ref: null
  started_at: null
  ended_at: null
  active_version_ref: null
  presenter_tenure_refs: []
  regular_slot_refs: []
  archive_collection_ref: null
  public_identity_refs: []
  canon_reference_ids: []
```

Possible descriptive kinds include NEWS, WEATHER, BATTLE_COVERAGE, INTERVIEW, CULTURE, EDUCATION, ENTERTAINMENT, SERIAL, RESEARCH, COMMUNITY, PUBLIC_SERVICE, MIXED and OTHER.

Kinds do not grant truth authority or mechanical effects.

## Program version

A recurring program can change format without becoming a new historical object.

```yaml
broadcast_program_version:
  program_version_id: null
  program_id: null
  valid_from: null
  valid_until: null
  format_summary: null
  segment_template_refs: []
  regular_presenter_role_refs: []
  production_location_refs: []
  intended_region_refs: []
  predecessor_version_ref: null
  revision_reason_refs: []
```

`FORMAT_CHANGED != PROGRAM_RETCONNED`

`PROGRAM_RENAMED != PROGRAM_HISTORY_ERASED`

Whether a rename creates a new program identity or a version is authored case by case.

## Presenter and crew tenure

```yaml
broadcast_role_tenure:
  tenure_id: null
  program_id: null
  actor_ref: null
  role_label: null
  started_at: null
  ended_at: null
  scope_refs: []
  source_refs: []
  replacement_or_successor_ref: null
```

Possible roles are presenter, reporter, commentator, producer, field correspondent, technical operator, editor, researcher or authored local equivalents.

Role presence does not imply ownership, editorial control, institutional leadership or mechanical social authority.

`HOST_OF_PROGRAM != OWNER_OF_CHANNEL`

`COMMENTATOR != BATTLE_OFFICIAL`

## Scheduled slot

```yaml
broadcast_slot:
  slot_id: null
  program_id: null
  channel_ref: null
  intended_start: null
  intended_end: null
  recurrence_ref: null
  intended_region_refs: []
  priority_or_override_ref: null
  status: SCHEDULED
```

Suggested states:

- TENTATIVE
- SCHEDULED
- CONFIRMED
- DELAYED
- PREEMPTED
- CANCELLED
- COMPLETED
- SUPERSEDED

A slot is a plan.

`PROGRAM_SCHEDULED != PROGRAM_TRANSMITTED`

## Episode / edition production

```yaml
broadcast_episode:
  episode_id: null
  program_id: null
  program_version_ref: null
  edition_label: null
  production_started_at: null
  production_completed_at: null
  planned_slot_ref: null
  segment_refs: []
  production_state: PLANNED
  source_event_refs: []
  publication_info_refs: []
  recording_refs: []
```

Suggested production states:

- PLANNED
- GATHERING_MATERIAL
- RECORDING
- EDITING
- READY
- PARTIAL
- ABANDONED
- SUPERSEDED
- TRANSMITTED

An episode can be complete and never air. A transmission can use a partially prepared edition because a live event changed the plan.

## Broadcast segment

```yaml
broadcast_segment:
  segment_id: null
  episode_id: null
  segment_kind: null
  source_info_refs: []
  source_event_refs: []
  presenter_refs: []
  recorded_at: null
  intended_live_state: RECORDED
  editorial_transform_refs: []
  runtime_order_hint: null
  archive_object_refs: []
```

Possible states for `intended_live_state`:

- LIVE
- RECORDED
- DELAYED_LIVE
- REPLAY
- UNKNOWN

The label describes production/transmission relationship. It does not create a gameplay clock.

`LIVE != UNEDITED`

`LIVE != UNIVERSALLY_RECEIVED`

`RECORDED != ARCHIVED`

## Concrete transmission

```yaml
broadcast_transmission:
  transmission_id: null
  episode_ref: null
  channel_ref: null
  service_ref: null
  feed_variant_ref: null
  actual_start: null
  actual_end: null
  transmission_state: STARTED
  segment_order_refs: []
  interruption_refs: []
  network_service_observation_refs: []
  publication_refs: []
  archive_capture_refs: []
```

Suggested transmission states:

- STARTED
- COMPLETE
- PARTIAL
- INTERRUPTED
- ABORTED
- FAILED_BEFORE_START
- UNKNOWN

A transmission can be COMPLETE even if a particular settlement lacked coverage. Coverage belongs to Communications Network and audience receipt belongs to Media.

## Feed variant

```yaml
broadcast_feed_variant:
  feed_variant_id: null
  transmission_or_episode_ref: null
  intended_region_refs: []
  language_or_presentation_ref: null
  local_insert_segment_refs: []
  omitted_segment_refs: []
  delay_ref: null
  provenance_refs: []
```

Hard safeguards:

`REGIONAL_FEED_DIFFERS != ONE_FEED_FALSE`

`LOCAL_INSERT != WORLD_EVENT_CHANGED`

`FEED_OMISSION != EVENT_DID_NOT_OCCUR`

## Live event linkage

A broadcast may cover a battle, performance, civic meeting, festival, field event, expedition return or other persistent event.

```yaml
broadcast_event_link:
  link_id: null
  transmission_id: null
  underlying_event_ref: null
  observation_scope_refs: []
  authoritative_owner_system: null
  camera_or_reporter_observation_refs: []
  commentary_info_refs: []
```

The owner system remains authoritative.

For AutoPTU battles:

`CAMERA_FEED != TARGETING_LOS`

`COMMENTARY != BATTLE_EVENT`

`REPLAY_EDIT != BATTLE_REWIND`

`SIGNAL_LOSS != BATTLE_INTERRUPTED`

`VIEWER_POLL != BATTLE_RESULT`

`REMOTE_VIEWER != COMBATANT`

## Interruption and override

```yaml
broadcast_interruption:
  interruption_id: null
  transmission_id: null
  started_at: null
  ended_at: null
  interruption_kind: null
  cause_claim_refs: []
  verified_cause_refs: []
  replacement_segment_refs: []
  network_incident_ref: null
  resumed: false
```

Possible descriptive kinds:

- NETWORK_LOSS
- STUDIO_INCIDENT
- FIELD_FEED_LOSS
- SCHEDULE_OVERRIDE
- EMERGENCY_BULLETIN
- TECHNICAL_FAILURE
- EDITORIAL_CUTAWAY
- UNKNOWN

No universal emergency-broadcast priority is implied. Any override policy must be authored locally.

`INTERRUPTION != PROGRAM_CANCELLED`

`CUTAWAY != UNDERLYING_EVENT_STOPPED`

`TECHNICAL_FAILURE_CLAIM != VERIFIED_CAUSE`

## Resumption

```yaml
broadcast_resumption:
  resumption_id: null
  interruption_ref: null
  resumed_at: null
  resumed_segment_ref: null
  skipped_segment_refs: []
  catchup_or_summary_info_refs: []
  resulting_transmission_state: null
```

A resumption can summarize missed material, continue from the current live moment or use a recorded replacement. Which occurs is authored.

## Rebroadcast

```yaml
broadcast_rebroadcast:
  rebroadcast_id: null
  source_episode_ref: null
  source_transmission_ref: null
  new_transmission_ref: null
  edit_or_version_refs: []
  reason_refs: []
```

`REBROADCAST != NEW_UNDERLYING_EVENT`

`REBROADCAST_AT_NEW_TIME != EVENT_OCCURRED_AT_NEW_TIME`

A later rebroadcast can still create a new publication and new audience receipt.

## Archive linkage

This extension stores links only.

```yaml
broadcast_archive_link:
  archive_link_id: null
  episode_or_transmission_ref: null
  archive_object_ref: null
  capture_kind: null
  completeness_claim_ref: null
  source_refs: []
```

Possible capture kinds:

- STUDIO_MASTER
- AIR_FEED_CAPTURE
- REGIONAL_FEED_CAPTURE
- SEGMENT_RECORDING
- EDITED_REPLAY
- TRANSCRIPT
- UNKNOWN

Archives owns the actual object.

Hard safeguards:

`AIRED != RECORDED`

`RECORDED != PRESERVED`

`PRESERVED != PUBLICLY_ACCESSIBLE`

`ARCHIVE_COPY_EXISTS != COMPLETE_AIR_FEED`

`NO_ARCHIVE_COPY != NEVER_AIRED`

## Correction linkage

Corrections remain Media information revisions.

This extension may record where they appeared:

```yaml
broadcast_correction_appearance:
  correction_appearance_id: null
  information_revision_ref: null
  episode_ref: null
  segment_ref: null
  transmission_ref: null
  aired_at: null
```

A later correction does not alter the historical contents of an earlier air capture.

`CORRECTION_AIRED != EARLIER_TRANSMISSION_OVERWRITTEN`

## Serialized fictional or dramatized content

Programs may contain fiction, documentary reconstruction or dramatized retelling if canon creates them.

The Broadcast layer stores the program and transmission. Performance may own the produced dramatic work. Claims/Investigation govern historical assertions.

`PROGRAM_DEPICTS_EVENT != EVENT_PROVEN`

`DRAMATIZATION != ARCHIVAL_FOOTAGE`

`ACTOR_PORTRAYS_NPC != NPC_PRESENT`

## Audience and metrics boundary

This extension does not create universal ratings, viewer counts, follower counts or popularity math.

If a canon system later records measured audience state, provenance and measurement scope are mandatory.

`TRANSMISSION_OCCURRED != EVERYONE_WATCHED`

`VIEWER_COMMENT != REGION_OPINION`

`TRENDING != TRUSTED`

`HIGH_AUDIENCE != MECHANICAL_REPUTATION_GAIN`

## Pokémon participation boundary

A Pokémon may be a presenter partner, field assistant, performer, mascot, camera subject or battle participant only when that role is authored and mechanically legal where relevant.

Species, Type or flavor never creates media capabilities automatically.

`POKEMON_IN_STUDIO != BROADCAST_EQUIPMENT`

`ELECTRIC_TYPE_PRESENT != SIGNAL_POWERED`

`PSYCHIC_TYPE_PRESENT != TELEPATHIC_BROADCAST`

`ROTOM_LIKE_PRESENTATION != DEVICE_AUTHORITY`

## Battle observer contract

A broadcast that covers an AutoPTU battle consumes authoritative outputs after or as they are published by the battle runtime boundary. It never supplies tactical inputs.

Permitted Narrative observations may include:

- battle started/ended when exposed authoritatively;
- named combatants already established by BattleSpec;
- authoritative positions/events exposed to playback;
- final formal result;
- interruption of the broadcast feed itself.

Forbidden derivations include:

- selecting combatants from Minecraft entities in camera range;
- creating target legality from camera visibility;
- declaring hit/miss from animation;
- creating HP/status from spectator UI;
- changing initiative because the broadcast schedule is late;
- granting extra actions for an encore, replay or viewer request.

## Encounter contract A — Studio Evacuation Access Corridor

Premise: a hostile or wild-Pokémon incident blocks immediate access around an occupied studio during a scheduled transmission.

Full intended version requires:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement for contested withdrawal and protection;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle for staged evacuation timing;
- full stateful damage pipeline and status lifecycle as selected content requires;
- terrain/weather/hazards/zones/reactions if equipment, smoke, live electrical danger or moving zones matter;
- move-specific behavior, abilities, items and Trainer Features/perks by individual audit;
- AI legal-action infrastructure;
- AI tactical policy for protect/withdraw/route-control behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support for authoritative semantic playback.

Full status at Pass 161: BLOCKED.

Reduced version:

- studio crew, guests and noncombatant Pokémon are moved to a safe authored state before initiative;
- broadcast transmission becomes INTERRUPTED before battle begins;
- equipment and studio hazards stay outside BattleSpec;
- arena geometry is static;
- explicit combatants only;
- permitted tactical output: `IMMEDIATE_STUDIO_ACCESS_ROUTE_CLEAR`.

`IMMEDIATE_STUDIO_ACCESS_ROUTE_CLEAR != STUDIO_EVACUATED`

`BATTLE_WON != BROADCAST_RESUMED`

## Encounter contract B — Relay Rooftop Perimeter

Premise: access to a communications relay or rooftop broadcast position is contested during an incident.

Full intended version can require height/fall semantics, weather, forced movement near edges, reactions and objective-aware AI.

Full status: BLOCKED.

Reduced version:

- use a bounded safe static platform with dangerous edge/fall mechanics excluded;
- weather effects are frozen out unless individually verified;
- relay technical state remains outside BattleSpec;
- permitted output: `IMMEDIATE_RELAY_APPROACH_CLEAR`.

`IMMEDIATE_RELAY_APPROACH_CLEAR != SIGNAL_RESTORED`

`BATTLE_WON != NETWORK_PATH_VERIFIED`

## Encounter contract C — Field Crew Withdrawal Corridor

Premise: a field reporter/crew must leave an area while a separate tactical threat remains.

Full version requires escort/withdrawal semantics, object carrying if equipment matters, complete movement, lifecycle and tactical policy.

Full status: BLOCKED.

Reduced version:

- field crew and equipment are removed from the tactical slice before initiative;
- their departure destination is authored externally;
- battle resolves only a fixed corridor among explicit combatants;
- permitted output: `IMMEDIATE_FIELD_EXIT_CORRIDOR_CLEAR`.

`CORRIDOR_CLEAR != CREW_DEPARTURE_COMPLETED`

`CREW_SAFE != FOOTAGE_PRESERVED`

## Encounter contract D — Broadcast Battle Coverage

Premise: a formally valid battle is being broadcast.

Reduced baseline version can run whenever the selected battle content itself is legal and audited. Broadcast state remains observational and imposes no tactical objective.

Narrative sequence:

1. Ouros authors the event and BattleSpec.
2. AutoPTU resolves the battle.
3. A broadcast transmission links to authoritative battle events/results exposed through supported integration.
4. Media produces commentary/publication packets separately.
5. Audience receipt occurs through Media/Communications.

The mechanically richer synchronized spectator/playback version remains BLOCKED on Minecraft/Cobblemon/Craftics adapter/playback support.

`BROADCAST_BATTLE != SPECIAL_BATTLE_RULESET`

`CAMERA_PRESENT != BATTLE_PARTICIPANT`

## Persistence writeback

After a broadcast-related scene, write back only demonstrated facts:

- episode production state;
- actual transmission times;
- feed variant used;
- interruption/resumption events;
- presenter/crew participation;
- information packets actually published;
- network service observations supplied by their owner system;
- archive links actually created;
- underlying event references and authoritative owner.

Do not write inferred audience belief, reputation, mechanical progression, technical causes, battle facts or canonical truth beyond their owning systems.

## Minecraft/Cobblemon/Craftics boundary

Minecraft/Cobblemon/Craftics may present studios, cameras, screens, antennae, presenters, field crews, broadcast vehicles, spectators and archived playback after Ouros has established those states.

It may not decide:

- which program is actually live from loaded chunks;
- which nearby entities are combatants;
- whether a camera sees a legal PTU target;
- whether a signal outage changes battle state;
- whether a Pokémon powers equipment;
- whether an animation proves a hit, status or Move use;
- whether a recording is authentic;
- whether a transmission was received region-wide;
- whether a broadcast changes reputation;
- any PTU/Caelo rule outcome.

## Canon approval queue

Remain unresolved until reviewed:

- which broadcast technologies exist by region;
- which operators/stations/programs are established canon;
- whether particular programs are public, commercial, institutional or community-run;
- which battles, performances or civic events are regularly broadcast;
- presenter identities and employment relationships;
- archive practices and access;
- local override priorities;
- region/feed boundaries;
- player-character consent and quotation boundaries;
- any fame, sponsorship, revenue or audience metric system;
- any mechanically relevant broadcast equipment or Pokémon capability.

## Pass 161 architecture conclusion

Broadcast continuity can now sit cleanly between Media, Communications Network, Archives, Performance and AutoPTU. The world may remember exactly what program was planned, what was produced, what actually aired, where it reached, what later survived in an archive and how the program changed over years without turning a television screen or livestream into a second source of tactical authority.