# Ouros Supporter, Fandom & Community Identity Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Date: 2026-08-31
Research basis: `research/2026-08-31-supporter-fandom-community-identity-scan-160.md`

## Purpose

This extension preserves durable supporter communities around Trainers, Gyms, teams, performers, researchers, public institutions and other authored public subjects without turning popularity into a universal reputation score or granting mechanical effects from narrative applause.

Existing owners remain authoritative. Public Memory owns what communities remember. Media/Communications owns publication and delivery. Battle Institutions owns formal competition. Performance Production owns productions and performance episodes. Social Bonds owns interpersonal relationships. Material Culture owns physical artifacts. Travel owns movement between places. Civic Governance owns collective decision procedures. This extension records supporter-group identity and supporter participation between those systems.

## Authority boundary

A supporter relationship requires evidence in world state. The generator may propose a group, but cannot silently create one for a famous NPC, winner or player character.

A supported subject does not automatically control supporters. A supporter group does not automatically become a faction. Crowd behavior is never inferred from Minecraft entity behavior.

## Core invariants

`ATTENDED_EVENT != SUPPORTER_MEMBER`

`SUPPORTER_MEMBER != EMPLOYEE`

`SUPPORTER_GROUP != FACTION_BY_DEFAULT`

`GROUP_ACTION != SUBJECT_ORDER`

`CHEERING != PTU_BUFF`

`APPLAUSE != MECHANICAL_REPUTATION_GAIN`

`POPULAR_LOCAL != POPULAR_REGION_WIDE`

`PUBLIC_ATTENTION != TRUST`

`PUBLIC_ATTENTION != COMPETITIVE_RANK`

`MERCHANDISE_OWNED != SUPPORT_PROVEN`

`COLORS_WORN != MEMBERSHIP_PROVEN`

`FAN_ARTIFACT != OFFICIAL_STATEMENT`

`SUPPORTER_CLAIM != CANONICAL_TRUTH`

`ONE_LOUD_GROUP != COMMUNITY_CONSENSUS`

`BOYCOTT_ANNOUNCED != BOYCOTT_OCCURRED`

`FOLLOWING_SPLIT != SUBJECT_FACTION_SPLIT`

`OFFICE_ENDED != FOLLOWING_ENDED`

`BATTLE_WON != SUPPORTER_LOYALTY_GAINED`

## 1. Supporter community

```yaml
supporter_community:
  supporter_community_id: null
  public_name: null
  subject_refs: []
  origin_event_refs: []
  origin_claim_refs: []
  home_location_refs: []
  membership_model: informal
  current_identity_state: active
  liaison_refs: []
  practice_refs: []
  artifact_refs: []
  internal_group_refs: []
  public_memory_refs: []
  media_channel_refs: []
  history_event_refs: []
  canon_basis_refs: []
```

Candidate identity states:

- EMERGING
- ACTIVE
- QUIET
- SPLIT
- MERGED_INTO_SUCCESSOR
- DISSOLVED
- HISTORICAL_ONLY
- UNCERTAIN

No state carries a mechanical modifier.

## 2. Supported subject

A group can support more than one subject and a subject can have several groups.

```yaml
supporter_subject_link:
  link_id: null
  supporter_community_id: null
  subject_ref: null
  subject_type: authored
  began_at: null
  basis_event_refs: []
  current_relation: supportive
  public_claim_refs: []
  subject_acknowledgement_state: unknown
  subject_contact_refs: []
  ended_at: null
  end_reason_refs: []
```

Candidate relation labels are descriptive only:

- SUPPORTIVE
- CRITICAL_SUPPORT
- NOSTALGIC
- PROTESTING_CURRENT_DIRECTION
- FORMER_SUPPORT
- MEMORIAL
- UNCERTAIN

A group can support a Gym while criticizing its current Leader. It can admire a former performer while disliking a revival production. It can support a town's team without supporting every sponsor.

## 3. Membership evidence

```yaml
supporter_membership_record:
  membership_record_id: null
  supporter_community_id: null
  actor_id: null
  membership_claim_state: claimed
  membership_basis_refs: []
  joined_at: null
  left_at: null
  current_state: unknown
  role_refs: []
  source_refs: []
```

Suggested states:

- CLAIMED
- CONFIRMED_BY_GROUP_RECORD
- OBSERVED_PARTICIPATION_ONLY
- FORMER_MEMBER
- DISPUTED
- UNKNOWN

Observed attendance or colors are insufficient to promote a person to confirmed membership.

## 4. Informal participation

Many supporters never join a formal organization.

```yaml
supporter_participation_event:
  participation_event_id: null
  actor_ids: []
  supporter_community_id: null
  event_ref: null
  participation_type: null
  occurred_at: null
  location_ref: null
  evidence_refs: []
  public_visibility: null
  consequence_refs: []
```

Candidate participation types:

- ATTENDANCE
- CHEERING
- VOLUNTEERING
- TRAVEL
- ARTIFACT_CREATION
- FUNDRAISING_WHERE_CANON_SUPPORTS_IT
- PUBLIC_COMMENT
- PETITION_OR_CAMPAIGN
- BOYCOTT_PARTICIPATION
- WATCH_PARTY
- ARCHIVE_CONTRIBUTION
- WELCOME_OR_FAREWELL

These labels do not imply legality, authority, money flow or mechanical effects.

## 5. Supporter practice

```yaml
supporter_practice:
  practice_id: null
  supporter_community_id: null
  practice_type: null
  first_observed_at: null
  location_scope_refs: []
  event_scope_refs: []
  participant_refs: []
  material_artifact_refs: []
  media_refs: []
  variation_refs: []
  current_state: active
  tradition_promotion_ref: null
```

Examples can include colors, meeting points, banners, songs, signs, pre-event meals, away-travel customs, post-event cleanup, autograph queues or fan archives.

A practice remains a supporter practice until Ritual/Tradition explicitly accepts it as a durable tradition. Repetition alone does not promote it.

## 6. Supporter-created artifact meaning

Material Culture remains owner of the object.

```yaml
supporter_artifact_link:
  supporter_artifact_link_id: null
  material_instance_ref: null
  supporter_community_id: null
  creator_refs: []
  subject_refs: []
  creation_event_ref: null
  supporter_meaning_claims: []
  official_status: unofficial
  subject_approval_state: unknown
  circulation_refs: []
```

`UNOFFICIAL` can coexist with wide circulation.

Official merchandise, licensed publications or institution-produced objects require the appropriate owner system and canon basis.

## 7. Supporter-made media

Media/Communications owns the publication packet and circulation. This extension only links supporter authorship and group context.

```yaml
supporter_media_link:
  supporter_media_link_id: null
  info_or_publication_ref: null
  supporter_community_id: null
  creator_refs: []
  subject_refs: []
  publication_relationship: independent
  editorial_position_claims: []
  correction_refs: []
```

Possible relationships:

- INDEPENDENT
- GROUP_OFFICIAL
- SUBJECT_AUTHORIZED
- SUBJECT_UNAUTHORIZED
- HISTORICAL_ARCHIVE
- PARODY_OR_SATIRE_WHERE_CANON_ESTABLISHES_IT

The subject's silence is not approval.

## 8. Attention episode

Public attention should have provenance and scope.

```yaml
public_attention_episode:
  attention_episode_id: null
  subject_refs: []
  triggering_event_refs: []
  triggering_publication_refs: []
  affected_region_refs: []
  affected_community_refs: []
  observed_attention_types: []
  began_at: null
  peak_claim_refs: []
  ended_at: null
  successor_episode_refs: []
```

Safe attention types include increased attendance, interview requests, supporter artifact circulation, public commentary, event invitations or local recognition when supported by evidence.

Do not infer universal fame from one episode.

## 9. Locality and reach

```yaml
supporter_reach_record:
  supporter_community_id: null
  location_ref: null
  reach_state: unknown
  evidence_refs: []
  valid_from: null
  valid_until: null
```

Candidate states:

- HOME_BASE
- ESTABLISHED_LOCAL
- OCCASIONAL
- EVENT_ONLY
- ONLINE_OR_MEDIA_ONLY_IF_TECHNOLOGY_CANON_SUPPORTS_IT
- HISTORICAL
- UNKNOWN

Reach is evidence-based, not a radius.

## 10. Internal diversity

A supporter community may contain subgroups with different preferences.

```yaml
supporter_internal_group:
  internal_group_id: null
  parent_supporter_community_id: null
  public_name: null
  origin_event_refs: []
  distinctive_practice_refs: []
  preference_claims: []
  spokesperson_refs: []
  current_state: active
```

This prevents a single supporter group object from becoming a hive mind.

## 11. Supporter position

```yaml
supporter_position_record:
  position_record_id: null
  supporter_community_or_internal_group_ref: null
  subject_ref: null
  issue_ref: null
  position_claims: []
  adopted_at: null
  adoption_basis_refs: []
  dissent_refs: []
  supersedes_position_ref: null
```

A supporter position can concern a retirement, venue, sponsorship, format, leadership change, public statement or institutional proposal.

The extension records the position. Civic Governance, Battle Institutions or another owner decides whether it has formal effect.

## 12. Supporter liaison

```yaml
supporter_liaison_relationship:
  liaison_ref: null
  supporter_community_id: null
  counterpart_actor_or_institution_ref: null
  liaison_actor_refs: []
  communication_channel_refs: []
  scope: null
  established_at: null
  current_state: active
```

A liaison route provides communication. It does not grant governance authority, confidential access or command over either side.

## 13. Subject acknowledgement

```yaml
supporter_acknowledgement_event:
  acknowledgement_event_id: null
  subject_ref: null
  supporter_community_id: null
  occurred_at: null
  acknowledgement_type: null
  communication_ref: null
  event_ref: null
  scope_notes: null
```

Possible types:

- THANKED
- MET_WITH
- RECOGNIZED_PUBLICLY
- DISTANCED_FROM_ACTION
- REQUESTED_BEHAVIOR_CHANGE
- DECLINED_FORMAL_RELATIONSHIP
- ENDORSED_SPECIFIC_PROJECT

One acknowledgement must not be generalized into permanent approval.

## 14. Split and succession

```yaml
supporter_group_transition:
  transition_id: null
  predecessor_group_refs: []
  successor_group_refs: []
  transition_type: null
  occurred_at: null
  triggering_event_refs: []
  member_transfer_claim_refs: []
  artifact_custody_refs: []
  inherited_practice_refs: []
  disputed_identity_claims: []
```

Candidate transitions:

- SPLIT
- MERGER
- RENAMING
- FORMALIZATION
- INFORMALIZATION
- DISSOLUTION
- REVIVAL

A successor does not automatically inherit every member, artifact, position or reputation claim.

## 15. Support through role transitions

When a subject retires, transfers office or changes institution, ask which link actually persists.

Examples:

- support follows the person;
- support remains with the Gym;
- support splits between person and successor;
- support becomes nostalgic/historical;
- support fades;
- a new group forms around the successor.

No option is automatic.

## 16. Public disagreement and controversy

Public Memory owns the remembered controversy. Media owns published claims. This extension may record supporter reaction events with provenance.

```yaml
supporter_reaction_episode:
  reaction_episode_id: null
  supporter_group_refs: []
  trigger_refs: []
  observed_action_refs: []
  published_claim_refs: []
  attendance_change_claim_refs: []
  internal_dissent_refs: []
  current_state: active
```

Do not create a numerical outrage meter.

## 17. Boycotts and attendance campaigns

A declared campaign needs separate execution evidence.

```yaml
supporter_campaign:
  campaign_id: null
  supporter_group_refs: []
  target_refs: []
  stated_goal_claims: []
  announced_at: null
  announcement_refs: []
  participation_event_refs: []
  outcome_claim_refs: []
  ended_at: null
```

`CAMPAIGN_ANNOUNCED != PARTICIPATION_PROVEN`.

`LOW_ATTENDANCE != BOYCOTT_CAUSED` unless evidence establishes causation.

## 18. Away support and travel

Travel owns route legality and actual journeys.

```yaml
supporter_travel_episode:
  supporter_travel_episode_id: null
  supporter_group_refs: []
  destination_event_ref: null
  intended_travel_refs: []
  actual_travel_refs: []
  meeting_point_refs: []
  lodging_refs: []
  liaison_refs: []
  disruption_refs: []
  arrival_evidence_refs: []
```

A group announcement that hundreds will travel does not establish that hundreds arrived.

## 19. Fan archives and historical continuity

Public Library/Archives and Public Memory remain owners of archival records. This extension can link supporter provenance.

A long-lived group may preserve:

- tickets or programs;
- photos;
- homemade publications;
- banners;
- recordings where technology permits;
- lists of trips or events;
- oral histories;
- correspondence.

The archive can be incomplete, curated or disputed without changing Chronicle truth.

## 20. Player characters and authorship protection

Do not create a fan club around a PC merely because the PC wins public battles.

If a supporter community does emerge from validated public events, preserve player boundaries:

- do not fabricate PC quotes;
- do not infer consent to endorsements;
- do not assign the PC ownership of supporter actions;
- do not force the PC to maintain a public persona;
- do not invent post-retirement supporter relations without canon support.

## 21. PTU/Caelo mechanics gate

Narrative supporter state has no automatic PTU effect.

Any mechanical use requires an exact rule review for the actor and moment. Relevant possibilities may include Charm, Command, Intimidate, Cheerleader, Coordinator or other Features depending on approved source material, but names alone are insufficient.

A mechanics gate should record:

```yaml
supporter_mechanics_gate:
  gate_id: null
  narrative_event_ref: null
  requested_mechanical_effect: null
  governing_source_ref: null
  prerequisite_refs: []
  engine_contract_refs: []
  approval_state: unresolved
```

Until approved, cheering remains narrative observation only.

## 22. Minecraft/Cobblemon boundary

Minecraft/Cobblemon/Craftics may render supporter state after Ouros establishes it:

- clothing colors;
- banners and signs;
- crowd placement;
- queues;
- meeting points;
- fan-made displays;
- arrival/departure visuals;
- venue sections;
- post-event cleanup;
- archived memorabilia.

The adapter may not decide:

- who is a supporter;
- what a crowd believes;
- whether a group is hostile;
- who becomes a combatant;
- whether cheering grants a bonus;
- whether a boycott succeeded;
- whether a public figure authorized supporter behavior;
- whether a supporter group becomes a faction.

## 23. Encounter contract A — Away Support Arrival Chokepoint

Narrative premise: a visiting supporter group reaches a congested access area while a separate hostile or wild-Pokémon incident blocks the route.

Full intended version:

- supporters and staff move through bounded evacuation/access lanes;
- combatants can protect or open routes;
- displacement and reactions matter around chokepoints;
- tactical AI can distinguish attack, delay, withdraw and route control;
- crowd state changes only from Ouros-authored events.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full status: BLOCKED.

Reduced version:

Ouros places supporters, staff and noncombatant Pokémon in a safe holding area before initiative. BattleSpec contains only audited combatants on static geometry. AutoPTU may establish `IMMEDIATE_ARRIVAL_ACCESS_CLEAR`. Travel/Event state decides later who actually enters the venue.

Reduced status: READY subject to per-content move/ability/item/Feature audit.

## 24. Encounter contract B — Supporter Archive Recovery Perimeter

Narrative premise: a fan archive or club room is threatened during a separate incident and the immediate approach must be cleared before custodians can recover records.

Full intended version may involve smoke, unstable shelving, changing access, rescue, object carrying and timed deterioration.

Dependencies add terrain/weather/hazards/zones/reactions, complete movement, lifecycle, tactical policy and playback support. Full status: BLOCKED.

Reduced version removes archive objects and custodians from BattleSpec. Geometry and hazard state are frozen before initiative. AutoPTU may return `IMMEDIATE_ARCHIVE_APPROACH_CLEAR`. Material Culture/Archive systems resolve actual custody afterward.

Reduced status: READY.

`BATTLE_WON != ARCHIVE_RECOVERED`.

## 25. Encounter contract C — Venue Exit Separation Perimeter

Narrative premise: two supporter groups need separate exit routes after a public event while an unrelated tactical threat occupies one perimeter.

Full intended version requires crowd routing, multiple protected objectives, reactions, complete withdrawal semantics and objective-aware AI. Full status: BLOCKED.

Reduced version keeps both supporter groups outside BattleSpec and fixes their routes before combat. Battle result may only establish `IMMEDIATE_EXIT_PERIMETER_CLEAR`.

Reduced status: READY.

`PERIMETER_CLEAR != GROUPS_RECONCILED`.

## 26. Encounter contract D — Public Figure Departure Corridor

Narrative premise: a retiring or transferring public figure needs a physically clear departure route while supporters remain nearby.

Full intended version may require escort, interception, contested withdrawal, reactions and tactical protect policy. Full status: BLOCKED.

Reduced version moves the subject and supporters outside BattleSpec before initiative. AutoPTU resolves a static chokepoint among verified combatants. It can establish `IMMEDIATE_DEPARTURE_CORRIDOR_CLEAR` only.

Reduced status: READY.

`CORRIDOR_CLEAR != DEPARTURE_COMPLETED`.

`DEPARTURE_COMPLETED != FOLLOWING_ENDED`.

## 27. Engine evidence interpretation

Live AutoPTU-Java head inspected for this pass: `e8bbd584cd55654b72d52117ee410d7e738f93b6`, merged PR #297, “Revalidate forced-movement target before displacement”.

The inspected diff shows the runtime now resolves canonical move metadata and revalidates the actor/target/move choice against current battle state before generic Push/Pull displacement mutates position. Tests cover out-of-range targets, stale target anchors, ownership of the move and server-owned movesets.

This is meaningful evidence for a broader forced-movement slice than the earlier Intercept-only work. It still does not verify the entire permanent movement family. The inspected evidence does not establish every Push/Pull move, general Knockback, all Intercept variants/orderings, escort, rescue, object carrying, crowd routing, moving vehicles, generalized reactions or tactical withdrawal/protection policy.

Therefore `complete movement including push/pull/knockback/interception/forced movement` remains PARTIAL.

AutoPTU head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit explicitly describes viewport/Pixi coordinate synchronization as presentation-only and says no battle rules or outcomes change.

No capability promotion is justified by that repository.

## 28. Integration outputs

Possible outputs to other systems:

- Public Memory: durable public interpretation or commemorated supporter event;
- Media/Communications: supporter publication, correction, interview or announcement;
- Travel: actual away journey;
- Hospitality: lodging demand when real arrivals exist;
- Event/Performance/Battle Institutions: attendance and liaison inputs;
- Material Culture: artifact provenance/custody;
- Civic Governance: petition, consultation input or stakeholder claim;
- Social Bonds: individual relationships formed through supporter activity;
- Chronicle: validated supporter events only.

## 29. Promotion gate

Before promoting any supporter concept to canon, require:

1. a specific supported subject already established in canon;
2. a plausible origin event or social basis;
3. scope and locality evidence;
4. group identity distinct from faction/employee status;
5. explicit ownership for artifacts and communication channels;
6. no inferred mechanical benefit;
7. exact PTU/Caelo review when a Feature or Skill effect is requested;
8. engine support for any tactical encounter behavior;
9. Minecraft presentation that reads server-owned state rather than inventing it.

This extension gives Ouros social continuity around public figures while preserving the difference between being watched, being liked, being organized around and being mechanically empowered.