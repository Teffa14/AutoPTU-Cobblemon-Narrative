# Ouros Festivals, Ceremonies, Observances & Rites Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already has `PUBLIC_EVENT` lifecycle, calendar/seasonality, public memory, traditions, myths, performance, food, tourism, civic institutions, public spaces and media. This layer adds the missing persistent cultural object that survives across editions: the observance itself.

The goal is to let a community repeat, reinterpret and sometimes abandon meaningful practices over years without turning those practices into automatic mechanics or copying the entire event every cycle.

## 1. Core separation

Use this chain:

```text
cultural observance identity
    ↓
calendar / ecological / historical trigger
    ↓
edition
    ↓
public-event execution
    ↓
practices + participation + nested activities
    ↓
archive / memory / changed tradition
```

Keep these concepts separate:

- `CULTURAL_OBSERVANCE`: persistent identity across years;
- `OBSERVANCE_EDITION`: one occurrence;
- `PUBLIC_EVENT`: scheduling and physical execution;
- `TRADITION`: broader cultural system that may contain many observances;
- `MYTHIC_CLAIM`: what a tradition says;
- `RITUAL_PRACTICE`: repeated symbolic/social act;
- `NESTED_ACTIVITY`: Contest, battle, sport, market, feast, performance, survey, procession, etc.;
- `PUBLIC_MEMORY`: what later generations remember;
- `MECHANICAL_EFFECT`: only when an exact PTU/Caelo/AutoPTU rule validates one.

## 2. Cultural observance

```yaml
cultural_observance:
  observance_id: null
  public_names: []
  tradition_ids: []
  community_ids: []
  region_ids: []
  origin_claim_ids: []
  earliest_confirmed_record_id: null
  recurrence_policy_id: null
  core_practice_ids: []
  optional_practice_ids: []
  steward_actor_ids: []
  steward_institution_ids: []
  signature_location_ids: []
  participation_policy_id: null
  archival_policy_id: null
  continuity_state: ACTIVE
  latest_edition_id: null
  unresolved_questions: []
```

Candidate continuity states:

- ACTIVE
- REVIVING
- REFORMING
- SPLIT
- DORMANT
- DISCONTINUED
- HISTORICAL_ONLY
- UNKNOWN

A discontinued observance remains part of Chronicle.

## 3. Recurrence policy

Do not assume every observance follows a fixed Gregorian-like date.

```yaml
observance_recurrence_policy:
  recurrence_policy_id: null
  anchor_type: null
  calendar_rule: null
  phenology_pattern_ids: []
  ecological_state_requirements: []
  institutional_trigger_ids: []
  historical_anniversary_ref: null
  tolerance_window: null
  postponement_policy: null
  cancellation_policy: null
  rescheduling_authority_ids: []
```

Candidate `anchor_type` values:

- DATE_ANCHORED
- SEASON_PHASE_ANCHORED
- PHENOLOGY_ANCHORED
- CELESTIAL_ANCHORED
- INSTITUTIONAL_ANCHORED
- HISTORICAL_ANNIVERSARY
- RECOVERY_MILESTONE
- RESOURCE_PULSE_ANCHORED
- CONDITIONAL
- MIXED

A migration celebration can move with the migration if authored that way. A civic anniversary may remain fixed even when weather or ecology changes.

## 4. Edition state

Each recurrence gets a new edition object.

```yaml
observance_edition:
  edition_id: null
  observance_id: null
  edition_number_or_label: null
  planned_window: null
  actual_window: null
  public_event_id: null
  preparation_project_ids: []
  edition_theme: null
  changed_practice_ids: []
  suspended_practice_ids: []
  guest_actor_ids: []
  participant_record_ids: []
  temporary_space_ids: []
  nested_activity_ids: []
  incident_ids: []
  media_packet_ids: []
  cleanup_project_ids: []
  archive_record_ids: []
  outcome_summary: null
  continuity_review_id: null
```

Edition history is append-only. The current version must not rewrite earlier editions.

## 5. Preparation is durable world state

Recurring events require work.

```yaml
observance_preparation_project:
  project_id: null
  edition_id: null
  workstream_type: null
  responsible_actor_ids: []
  responsible_institution_ids: []
  volunteer_pool_ids: []
  location_ids: []
  dependency_ids: []
  required_asset_ids: []
  status: PLANNED
  handoff_records: []
  backlog_ids: []
```

Candidate workstreams:

- decoration;
- food/service;
- route setup;
- stage/venue preparation;
- accessibility review;
- visitor information;
- transport coordination;
- stewardship/security;
- archive/exhibit preparation;
- ceremonial-object custody;
- cleanup;
- ecological protection;
- lighting/sound;
- temporary market setup.

Do not create a quest for every routine task. Most preparation compresses unless capacity, dependency, conflict or player intent makes it meaningful.

## 6. Ritual practice

A ritual is a repeated practice, not proof that its stated supernatural meaning is true.

```yaml
ritual_practice:
  ritual_practice_id: null
  observance_ids: []
  tradition_ids: []
  practice_type: null
  public_description: null
  participant_role_requirements: []
  object_refs: []
  location_refs: []
  sequence_refs: []
  stated_meaning_claim_ids: []
  known_historical_changes: []
  access_policy_id: null
  mechanical_effect_ref: null
```

Candidate practice types:

- procession;
- offering;
- communal meal;
- bell/ringing/signal;
- lighting/extinguishing;
- mask/costume practice;
- dance/performance;
- oath or pledge;
- naming/recognition;
- memorial act;
- blessing claim;
- symbolic journey;
- temporary opening of a site;
- stewardship action;
- distribution/sharing;
- public reading or storytelling.

`mechanical_effect_ref` stays null unless exact rules authorize one.

## 7. Participation record

Attendance alone does not prove cultural membership, belief or relationship.

```yaml
observance_participation_record:
  participation_id: null
  edition_id: null
  actor_id: null
  role: OBSERVER
  invited_by_id: null
  registered_activity_ids: []
  volunteer_shift_ids: []
  formal_action_ids: []
  consent_refs: []
  public_visibility: null
```

Candidate roles:

- OBSERVER
- GUEST
- LOCAL_PARTICIPANT
- VOLUNTEER
- ORGANIZER
- STEWARD
- PERFORMER
- COMPETITOR
- VENDOR
- OFFICIAL
- INVITED_DELEGATE
- MEDIA
- RESEARCHER
- SUPPORT_ROLE

The generator must not infer ethnicity, religion, ideology, family membership, sincerity or friendship from a participation record.

## 8. Participation permissions

Some practices may be public, some invited, some role-specific and some closed.

```yaml
observance_participation_policy:
  policy_id: null
  observance_id: null
  general_public_access: null
  visitor_access: null
  role_requirements: []
  invitation_rules: []
  stewardship_rules: []
  sacred_access_refs: []
  media_rules: []
  photography_rules: []
  change_history: []
```

Do not invent protected/sacred restrictions from aesthetic cues. They require authored tradition state.

## 9. Nested activities

A festival can contain many activities without owning their mechanics.

```yaml
observance_nested_activity:
  nested_activity_id: null
  edition_id: null
  activity_type: null
  subsystem_ref: null
  event_slot_id: null
  location_id: null
  eligibility_ref: null
  result_ref: null
  cultural_role: null
```

Examples:

- Contest → Contest layer;
- battle exhibition → Battle Institution layer;
- race → Sports layer;
- market → Economy/Food layer;
- archaeological open day → Archaeology layer;
- fishing contest → Fisheries layer;
- public survey → Science layer;
- memorial → Loss/Memorial layer.

The observance layer records why the activity is part of this edition and how the result enters public memory. It does not duplicate the rules.

## 10. Ceremonies of transition

Ceremonies may recognize a status change established by another authority.

```yaml
transition_ceremony:
  ceremony_id: null
  edition_id: null
  subject_actor_ids: []
  recognized_transition_type: null
  source_decision_ref: null
  public_witness_scope: null
  symbolic_actions: []
  archive_refs: []
```

Examples of possible authored transitions:

- graduation;
- appointment;
- retirement;
- reopening;
- reconstruction milestone;
- accession to a club role;
- recognition of a research achievement;
- first journey departure;
- return from expedition.

The ceremony cannot create eligibility, ownership, office, guardianship or authority unless the governing subsystem has already produced the valid state transition.

## 11. Rites of passage and player agency

A `rite_of_passage` can exist culturally without forcing a PC to participate.

```yaml
rite_of_passage:
  rite_id: null
  tradition_id: null
  eligible_role_description: null
  participation_mode: OPTIONAL
  prerequisite_refs: []
  recognized_output_ref: null
  refusal_or_alternative_policy: null
  historical_variants: []
```

Rules:

- never infer a PC's age, family permission, belief or desire to participate;
- never force irreversible identity changes through generated ritual;
- participation must not grant unsupported Skills, Features, Loyalty or stat changes;
- alternatives may exist if canon says they do;
- nonparticipation can be socially visible only when plausible actors know about it.

## 12. Ceremony objects and custody

Objects may accumulate cultural significance without gaining mechanics.

```yaml
ceremonial_object_use:
  use_id: null
  object_instance_id: null
  edition_id: null
  custodian_before_id: null
  custodian_during_id: null
  custodian_after_id: null
  practice_id: null
  condition_before: null
  condition_after: null
  public_claim_ids: []
```

A bell, mask, banner, cup, lantern, flute, stone, book or garment can have provenance and custody independent of its symbolic meaning.

## 13. Local meaning versus public brand

Tourism/media can reshape how outsiders know an observance.

```yaml
observance_public_profile:
  observance_id: null
  local_meaning_claim_ids: []
  tourism_brand_claim_ids: []
  media_frame_ids: []
  disputed_claim_ids: []
  attendance_trend_refs: []
  pressure_state_ids: []
```

A festival may become famous for masks while locals care more about harvest, remembrance or stewardship. Both can be true social facts.

## 14. Change across editions

```yaml
observance_change_record:
  change_id: null
  observance_id: null
  effective_edition_id: null
  changed_component: null
  old_ref: null
  new_ref: null
  proposed_by_ids: []
  decision_ref: null
  reason_claim_ids: []
  contested_by_ids: []
```

Possible causes:

- ecology changed;
- route changed;
- organizer succession;
- new safety/accessibility requirement;
- recovery after crisis;
- migration of community members;
- sponsorship/funding change;
- reinterpretation of history;
- new research;
- tourism pressure;
- infrastructure change;
- voluntary reform.

Change does not automatically mean decline. Continuity can include reform.

## 15. Cancellation, postponement and partial editions

An edition can fail to occur without deleting the observance.

```yaml
edition_disruption:
  disruption_id: null
  edition_id: null
  disruption_type: null
  cause_ref_ids: []
  decision_ref: null
  public_notice_ids: []
  replacement_activity_ids: []
  next_review_date: null
```

Candidate disruption types:

- POSTPONED
- CANCELED
- PARTIALLY_HELD
- RELOCATED
- REMOTE_OR_DISTRIBUTED
- CEREMONY_ONLY
- ACTIVITIES_ONLY

Chronicle should remember skipped years.

## 16. Phenology-linked observances

When an observance depends on ecology, the trigger must come from the relevant world-state layer.

Examples:

- migration arrival → Wild Collectives/Seasonality;
- flowering window → Flora/Phenology;
- first thaw → Cryosphere;
- harvest completion → Agriculture;
- fishing season → Fisheries;
- astronomical event → Astronomy;
- river reopening → Freshwater/Travel.

The observance layer consumes the fact. It does not manufacture it.

## 17. Multiplayer / anti-FOMO policy

Recurring events must not punish players for real-life absence.

Policy principles:

- central progression must remain available outside one narrow live window;
- missed editions leave archive records, aftermath and future editions;
- one-time unique mechanical power should not depend on being online at a specific real-world hour;
- personal ceremonies involving a PC require that player's participation or explicit consent;
- public world events may advance while offline, but private character commitments do not.

## 18. Minecraft projection

Minecraft may render:

- temporary decoration;
- stalls;
- stages;
- banners;
- seating;
- procession routes;
- temporary road closures;
- lights;
- festival clothing;
- crowds as coarse representative cohorts;
- ceremonial objects;
- teardown and cleanup.

Minecraft must not infer:

- who belongs to the tradition;
- whether a ritual worked;
- whether an attendee believes a claim;
- whether a symbolic object grants a buff;
- whether a ceremony created authority;
- whether a Pokémon voluntarily participates.

## 19. Battle handoff

If combat occurs during an observance:

1. world state identifies the incident;
2. civilians/noncombatants are removed or represented only through a validated objective system;
3. ceremonial assets remain overworld objects unless battle object-target rules support them;
4. AutoPTU receives the legal combatants and a frozen arena snapshot;
5. AutoPTU returns authoritative combat results;
6. the observance edition records aftermath, schedule disruption and public memory.

No festival script may create custom damage, statuses, weather, buffs, crowd morale or forced movement.

## 20. Encounter dependency policy

Mechanically rich observance encounters must name permanent capability dependencies.

Common FULL dependencies:

- `complete movement including push/pull/knockback/interception/forced movement` for processions, escorts, crowd corridors or pursuit;
- `terrain/weather/hazards/zones/reactions` for changing festival grounds or environmental phases;
- `AI tactical policy` for PROTECT, WITHDRAW, HOLD_ROUTE, ESCORT or AVOID_CIVILIANS goals;
- `Minecraft/Cobblemon/Craftics adapter/playback` for live crowds, temporary structures and semantic objectives.

Most REDUCED versions can preserve the premise by resolving festival logistics first and then using a normal static battle.

## 21. Mechanical guardrails

The narrative system must not invent:

- blessings;
- luck bonuses;
- Accuracy/Evasion changes;
- Initiative bonuses;
- healing;
- Loyalty/friendship changes;
- capture modifiers;
- evolution triggers;
- weather control;
- Contest bonuses;
- Skill bonuses;
- status immunity;
- masks/costumes as equipment effects;
- food buffs;
- ceremonial item powers;
- crowd bonuses;
- rite-of-passage Features;
- supernatural effects from songs, bells, lanterns, offerings or dances.

An authored supernatural phenomenon can exist as world truth, but any combat effect still needs a validated PTU/Caelo/AutoPTU contract.

## 22. Suggested cross-layer handoffs

- Calendar/Seasonality → recurrence eligibility.
- Public Memory → edition history and commemorations.
- Myth/Archaeology → origin claims and sacred practices.
- Civic Governance → permits, closures and official decisions.
- Workplaces → staffing and volunteer coordination.
- Food/Hospitality → feasts, stalls and supply.
- Performance/Sports/Battle Institutions → nested activities.
- Tourism → visitor surge and pressure.
- Media → public framing.
- Material Culture/Fashion → ceremonial objects and clothing.
- Accessibility → participation design.
- Travel/Rail/Air/Maritime → arrival capacity.
- Waste/Sanitation → cleanup and temporary service load.
- Conservation/Ecology → sensitive windows and stewardship.
- Archive/Museums → edition records and historic objects.

## 23. Canon promotion gate

Before promoting an observance to canon, review:

- community and location identity;
- origin claims versus confirmed history;
- recurrence rule;
- mandatory versus optional practices;
- participation/access policy;
- any sacred/private components;
- organizer/steward authority;
- nested activity mechanics;
- ceremonial object provenance;
- accessibility policy;
- offline/multiplayer handling;
- whether any claimed supernatural effect is actually canon;
- PTU/Caelo legality of any mechanical element.
