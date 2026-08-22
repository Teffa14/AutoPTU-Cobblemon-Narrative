# Ouros Fandom, Supporters, Celebrity & Public Attention Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already has public memory, media, battle institutions, Contests, sports, music, sponsorships, tourism and public events. This layer owns the social state created when people repeatedly follow, support, criticize, archive, imitate or organize around public figures, teams, Pokémon, institutions and recurring activities.

The goal is to make fame produce believable consequences without turning it into omniscience, authority, friendship or a combat modifier.

## 1. Core separation

```text
world truth
  -> public events / records / publications
  -> attention exposure
  -> audience interpretation
  -> supporter affiliation or criticism
  -> supporter activity
  -> public artifacts / attendance / demand
  -> consequences in existing systems
```

None of these steps implies the next automatically.

A famous person can be misunderstood.
A fan can know public facts without knowing the person.
A crowd can cheer without becoming a faction.
A public figure can dislike attention without losing mechanical status.

## 2. Public figure profile

```yaml
public_figure_profile:
  subject_id: null
  subject_type: ACTOR|POKEMON|TEAM|INSTITUTION|PAIR|ENSEMBLE
  public_roles: []
  first_public_attention_at: null
  attention_domains: []
  public_record_refs: []
  official_channel_refs: []
  known_public_appearance_refs: []
  private_information_refs: []
  current_attention_band: LOW|LOCAL|REGIONAL|MULTIREGIONAL|UNKNOWN
  privacy_policy_ref: null
```

`attention_band` is descriptive and coarse. It does not equal reputation, moral approval or power.

## 3. Audience segment

A public figure can have multiple audiences with different reasons for paying attention.

```yaml
audience_segment:
  audience_id: null
  subject_ids: []
  region_ids: []
  attention_reason_tags: []
  typical_channels: []
  attendance_patterns: []
  artifact_patterns: []
  knowledge_basis_refs: []
  attitude_distribution: null
  organization_level: NONE|LOOSE|CLUB|FORMAL
  active_window: null
```

Possible reasons:
- competitive results;
- local identity;
- performance;
- music;
- rescue/public service;
- research/public education;
- fashion;
- historical significance;
- Pokémon-specific interest;
- personal style;
- recurring media presence.

## 4. Supporter group

A supporter group is persistent only when there is repeated organization, not because several spectators reacted similarly once.

```yaml
supporter_group:
  group_id: null
  name: null
  supported_subject_ids: []
  founded_at: null
  home_location_ids: []
  member_count_band: null
  membership_policy: null
  organizer_ids: []
  recurring_activity_ids: []
  traditions: []
  artifact_collection_refs: []
  communication_channel_refs: []
  current_status: ACTIVE|DORMANT|DISSOLVED|UNKNOWN
  canon_status: proposed
```

A supporter group is not automatically a faction. It gains faction-like properties only if it develops independent goals, resources and coordinated action beyond support culture.

## 5. Attention event

```yaml
attention_event:
  event_id: null
  subject_ids: []
  trigger_refs: []
  occurred_at: null
  region_scope: []
  channel_refs: []
  estimated_reach_band: null
  observed_reaction_refs: []
  followup_refs: []
```

Triggers can include:
- a formal battle;
- Contest/performance;
- public rescue;
- publication;
- interview;
- photograph/video;
- scandal claim;
- correction;
- retirement;
- return after absence;
- regional event.

The event does not directly modify “fame points.” Systems may derive a coarse attention revision from accumulated evidence.

## 6. Public persona vs private actor

```yaml
public_persona_revision:
  subject_id: null
  valid_from: null
  public_claim_refs: []
  recurring_presentation_tags: []
  official_bio_refs: []
  audience_assumption_refs: []
  correction_refs: []
```

Hard boundaries:
- audience assumptions do not become actor traits;
- media framing does not become inner motivation;
- clothing does not prove ideology or personality;
- public friendliness does not establish private friendship;
- romantic speculation never becomes relationship state;
- public silence does not prove guilt, anger or approval.

## 7. Fan-made artifact

```yaml
fan_artifact:
  artifact_id: null
  artifact_type: POSTER|BANNER|ZINE|SCRAPBOOK|SONG|COSTUME|STAT_BOOK|PHOTOBOOK|MODEL|OTHER
  creator_claim_ids: []
  created_at: null
  subject_ids: []
  source_material_refs: []
  physical_instance_id: null
  publication_refs: []
  official_status: UNOFFICIAL|ENDORSED|COMMISSIONED|UNKNOWN
  accuracy_assessment_refs: []
  archive_refs: []
```

An unofficial stat book may contain excellent data and still be unofficial. An official poster may contain simplified or outdated claims.

## 8. Supporter activity

```yaml
supporter_activity:
  activity_id: null
  group_id: null
  event_type: WATCH_PARTY|TRAVEL|CHANT|BANNER_DISPLAY|ARCHIVE_WORK|FAN_MEET|CHARITY|PUBLICATION|OTHER
  location_id: null
  scheduled_at: null
  participant_count_band: null
  public_space_ref: null
  event_ref: null
  observed_outputs: []
```

No activity grants a battle modifier by default.

## 9. Crowd allegiance during events

Crowd support can be stored for presentation and public-memory consequences without affecting battle rules.

```yaml
event_audience_state:
  event_id: null
  attendance_band: null
  supporter_segment_refs: []
  neutral_attendance_band: null
  observed_reaction_events: []
  presentation_cues: []
```

Until PTU/Caelo explicitly validates a crowd mechanic and Java implements it, crowd state remains narrative/presentation only.

## 10. Fame and Pokémon agency

A Pokémon can become famous while remaining an individual entity.

Examples:
- repeated Gym appearances;
- rescue work;
- performance career;
- public research sightings;
- a distinctive historical photograph;
- association with a public Trainer.

Hard rules:
- fame does not transfer ownership;
- fans cannot command the Pokémon;
- a former Trainer cannot reclaim authority because supporters expect a reunion;
- merchandise does not imply consent by the Pokémon unless authored policy says so;
- popularity never modifies Loyalty automatically.

## 11. Privacy and access pressure

Attention can create pressure through existing systems:
- visitors outside a home;
- crowding at a training venue;
- increased interview requests;
- unauthorized photography claims;
- demand for public appearances;
- rumors after missed appearances;
- mail volume;
- market demand for memorabilia.

These create cases, access decisions, schedules and public-space pressure. They do not override privacy or credentials.

## 12. Criticism, anti-fandom and former supporters

```yaml
public_critique_group:
  group_id: null
  subject_ids: []
  critique_claim_refs: []
  evidence_refs: []
  activity_refs: []
  hostility_state: NONE|RHETORICAL|DISRUPTIVE|UNKNOWN
```

Criticism is not hostility. Disagreement with a Gym Leader, Champion, musician or institution does not create an antagonist flag.

Former supporters should remain persistent actors. A person may stop following a public figure without becoming an enemy.

## 13. Attention decay and recurrence

Attention should not only rise.

Possible causes of decline:
- inactivity;
- retirement;
- new public figures;
- regional distance;
- channel changes;
- institutional collapse;
- a sport or Contest format becoming less popular.

Old fandom can still survive in archives, memorabilia, annual gatherings or family traditions.

## 14. Multiplayer policy

For PCs:
- do not create a fan club without sufficient in-world public exposure;
- do not invent private admirers or romantic interest;
- do not publish private home/location data automatically;
- allow players to choose visibility policies where the world reasonably permits it;
- player-created supporter groups need normal multiplayer moderation and consent rules;
- a PC cannot mechanically control supporters through a single social roll.

## 15. Integration with existing layers

Media owns publications and delivery.
Public Memory owns durable public narratives.
Battle Institutions own official competitive records.
Contest/Performance, Sports and Music own careers/events.
Tourism owns visitor pressure.
Markets own sales/listings.
Sponsorship owns commercial agreements.
Public Space owns crowd use of physical places.
Fandom owns persistent supporter identity, supporter activity, attention segments and fan artifacts.

## 16. Minecraft projection

Minecraft may render:
- banners;
- supporter sections;
- fan-club rooms;
- posters;
- queues;
- autograph/photo lines;
- memorabilia displays;
- watch parties;
- visitor clusters.

The renderer must not infer actual membership, private beliefs or mechanical morale from visible cosmetics.

## 17. Encounter implementation contracts

### A. Supporter Section Evacuation

Narrative premise: a stadium-side supporter area must be cleared after a noncombat infrastructure incident creates a separate Pokémon confrontation nearby.

FULL version dependencies:
- complete movement including interception/forced movement: moving civilian/supporter flows if inside tactical space;
- terrain/weather/hazards/zones/reactions: only if the incident creates validated tactical zones;
- AI tactical policy: EVACUATE/PROTECT/CLEAR_ROUTE behaviors;
- Minecraft/Cobblemon/Craftics adapter/playback: crowd evacuation and semantic objectives.

REDUCED version:
- public-space/world-state layer evacuates supporters first;
- AutoPTU receives a static arena containing only combatants;
- the result writes back to event schedule, attendance and public memory.

### B. Fan Archive Retrieval

Narrative premise: an old supporter archive contains posters, recordings and unofficial stat books useful to a historical investigation.

FULL version dependencies:
- no battle required by default;
- if conflict occurs around moving archive materials, complete movement and AI tactical policy may be needed for protected-cargo objectives.

REDUCED version:
- investigation remains entirely overworld/noncombat;
- any unrelated confrontation becomes a conventional static battle.

### C. Public Appearance Chokepoint

Narrative premise: a public figure’s scheduled appearance creates crowding exactly when wild Pokémon attempt to withdraw through the same district.

FULL version dependencies:
- complete movement including interception/forced movement;
- AI tactical policy for WITHDRAW/CLEAR_ROUTE/PROTECT;
- terrain/weather/hazards/zones/reactions only if a validated environmental effect exists;
- Minecraft/Cobblemon/Craftics adapter/playback.

REDUCED version:
- public-space system redirects attendees;
- wild movement resolves in overworld state;
- any remaining combat uses a frozen static arena.

## 18. Mechanical guardrails

Never infer:
- supporter count -> morale bonus;
- cheering -> Accuracy or damage bonus;
- boos -> penalty;
- fame -> Charm/Command rank;
- fan club -> faction combat support;
- celebrity -> Trainer Feature;
- public Pokémon -> higher Loyalty;
- media reach -> AI scouting omniscience;
- merchandise -> ownership rights;
- supporter banner -> terrain/zone effect.

## 19. Canon decisions still required

- Which competitive/performance scenes in Ouros already have organized supporter culture?
- Do any regional fan clubs predate the player campaign?
- Which public figures are famous at campaign start?
- How global are broadcasts and social channels?
- Which supporter artifacts can become collectible world objects?
- What privacy expectations exist for public Trainers?
- Can player clubs formally organize supporter groups?
- Are any crowd or morale mechanics actually present in PTU/Caelo?

Until answered, this layer stays proposed and mechanics-neutral.
