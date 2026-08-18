# Ouros Public Memory, Event & Legacy Layer

Status: Proposed systems design. Not established canon.

## Purpose

Ouros already models Chronicle facts, NPC memory, factions, knowledge, settlements, clocks and persistent locations. This layer adds a missing distinction: what the world publicly remembers and how recurring civic events turn that memory into playable content.

The goal is to let player actions become history without giving the narrative system permission to invent a retired character's later life.

## 1. Historical state has three layers

```yaml
historical_event:
  event_id: null
  canonical_fact_ids: []
  public_record_ids: []
  living_memory_ids: []
  affected_locations: []
  affected_institutions: []
  affected_factions: []
  participant_ids: []
  witness_ids: []
```

Canonical facts come from validated Chronicle state.

Public records are claims preserved by institutions, archives, plaques, newspapers, tournament records, reports or civic announcements.

Living memory includes rumors, family stories, commemorations, songs, local legends, propaganda and popular misunderstandings.

The second and third layers may be incomplete or wrong without modifying canonical truth.

## 2. Witness graph

Public consequences should spread from plausible observation.

```yaml
witness_report:
  report_id: null
  source_event_id: null
  witness_id: null
  observed_fact_ids: []
  inferred_claim_ids: []
  confidence: null
  audience_ids: []
  propagation_scope: local
  distortion_tags: []
```

Rules:
- a witness cannot report facts they had no plausible access to;
- actors may omit information intentionally;
- later retellings may summarize or distort;
- private Chronicle state does not automatically become public;
- public fame and blame should be attributable to reports, recordings, institutions or visible events.

## 3. Public standing

Public standing is separate from NPC relationships and faction reputation.

```yaml
public_standing:
  subject_id: null
  community_id: null
  recognition: 0
  prestige: 0
  controversy: 0
  trust: 0
  fear: 0
  known_for_tags: []
  source_event_ids: []
  last_updated: null
```

These values can be ordinal bands.

A character can simultaneously be:
- famous but distrusted;
- respected but obscure;
- controversial but admired by a subcommunity;
- feared without being respected;
- trusted locally but unknown elsewhere.

No public-standing value grants direct PTU bonuses unless separately reviewed.

## 4. Public memory object

```yaml
public_memory:
  memory_id: null
  community_id: null
  subject_ids: []
  source_event_ids: []
  memory_type: null
  dominant_claims: []
  minority_claims: []
  commemorated_at: []
  institutional_backers: []
  contested_by: []
  confidence: null
  visibility: public
```

Candidate memory types:
- victory;
- disaster;
- rescue;
- scandal;
- discovery;
- founding;
- migration;
- rivalry;
- championship;
- disappearance;
- reconstruction;
- protest;
- expedition;
- unresolved mystery.

## 5. Institution identity

Institutions need continuity beyond one NPC.

```yaml
institution_identity:
  institution_id: null
  location_ids: []
  institution_type: null
  public_role: null
  traditions: []
  operating_principles: []
  signature_spaces: []
  signature_event_ids: []
  current_leadership_ids: []
  former_leadership_ids: []
  prestige_sources: []
  controversies: []
  reform_history: []
```

Examples of institution types:
- Gym;
- contest hall;
- academy;
- research institute;
- rescue organization;
- ranger-like service;
- league office;
- guild;
- transport association;
- museum;
- tournament committee;
- civic council.

Leadership can change without erasing traditions, public expectations or institutional scars.

## 6. Event lifecycle

Major public events should be state machines.

```yaml
public_event:
  event_id: null
  event_type: null
  host_location_ids: []
  sponsor_ids: []
  edition: null
  lifecycle_state: announced
  schedule_blocks: []
  activity_lanes: []
  invited_actor_ids: []
  public_access: true
  temporary_world_changes: []
  incident_slots: []
  closing_outputs: []
  historical_record_policy: null
```

Suggested lifecycle states:
- PROPOSED
- ANNOUNCED
- PREPARING
- ACTIVE
- CLOSING
- CLEANUP
- AFTERMATH
- ARCHIVED

Minecraft can visibly express each state through construction, temporary NPCs, route restrictions, decorations, stalls, crowds and teardown.

## 7. Event schedule blocks

```yaml
event_schedule_block:
  block_id: null
  event_id: null
  time_window: null
  location_id: null
  activity_type: null
  participation_policy: open
  participant_limit: null
  spectator_access: true
  plot_critical: false
  mechanics_review_required: false
```

Candidate activity types:
- SOCIAL;
- CEREMONY;
- EXHIBITION;
- TOURNAMENT;
- CONTEST;
- CAPTURE_EVENT;
- EXPEDITION;
- MARKET;
- PERFORMANCE;
- WORKSHOP;
- PUBLIC_DEBATE;
- INVESTIGATION;
- RAID_RESPONSE;
- AWARD;
- PARADE.

Public events should leave substantial unscheduled space for player-directed interaction.

## 8. Incident budget

High-density events can become exhausting if every schedule block contains a crisis.

```yaml
event_incident_budget:
  max_major_incidents_per_phase: 1
  max_minor_incidents_per_phase: 3
  max_mandatory_scenes_per_phase: 2
```

Values are placeholders.

The event generator should prioritize social density and contrast. A quiet banquet can make a later disappearance matter more than nonstop emergencies.

## 9. Event edition history

Recurring events accumulate history.

```yaml
event_edition_record:
  recurring_event_id: null
  edition: null
  host_locations: []
  format_version: null
  participant_ids: []
  winner_ids: []
  finalist_ids: []
  records_set: []
  public_incidents: []
  controversies: []
  rule_changes_proposed: []
  relationship_outputs: []
  faction_outputs: []
  settlement_outputs: []
```

A new edition should query earlier editions for:
- defending champions;
- old records;
- unresolved rivalries;
- retired participants;
- disputed outcomes;
- prior safety failures;
- traditions;
- sponsors;
- format changes.

## 10. Ceremony and commemoration

Ceremonies turn state into public meaning.

```yaml
commemoration:
  commemoration_id: null
  source_event_ids: []
  host_ids: []
  location_id: null
  form: null
  public_claims: []
  omitted_claims: []
  contested_claims: []
  recurring: false
```

Possible forms:
- plaque;
- memorial;
- annual ceremony;
- named tournament round;
- museum exhibit;
- route name;
- scholarship;
- public holiday;
- mural;
- statue;
- preserved battlefield.

Commemoration is not proof that its public interpretation is accurate.

## 11. Retired character boundary

The system must protect player authorship.

For a retired PC, Ouros may reuse:
- validated past actions;
- publicly recorded achievements;
- confirmed relationships at retirement;
- items, organizations or institutions the player explicitly left behind;
- approved future-state notes supplied by the player or human canon editor.

Ouros must not autonomously decide:
- whom the retired PC married;
- where they moved;
- what ideology they later adopted;
- whether they died;
- what major choices they made after retirement;
- what their current team became.

If later content needs such a fact, mark it unresolved or request human canon input outside automated generation.

## 12. Legacy handoff

```yaml
legacy_handoff:
  legacy_id: null
  source_actor_ids: []
  source_event_ids: []
  inheriting_entity_ids: []
  inherited_assets: []
  inherited_obligations: []
  inherited_reputation_context: []
  inherited_mysteries: []
  consent_or_canon_refs: []
```

Possible inheritors:
- faction;
- settlement;
- institution;
- NPC;
- later player group;
- family only when canonically established;
- research archive;
- rival organization;
- successor tournament team.

A legacy may be beneficial, harmful or ambiguous.

## 13. Historical dispute generator

Older events can seed investigations without retconning canonical truth.

Candidate triggers:
- two public records conflict;
- a monument omits a participant;
- physical evidence contradicts the accepted story;
- an institution sealed part of an archive;
- a witness later retracts a claim;
- a recurring festival celebrates an event whose cause remains uncertain;
- a faction's current legitimacy depends on one historical interpretation.

The generator creates a present-day conflict around history. It does not rewrite the original Chronicle fact.

## 14. Audience and spectator state

Public battles and competitions may have spectators whose reactions become social evidence.

```yaml
audience_state:
  event_id: null
  audience_groups: []
  known_participants: []
  witnessed_moments: []
  dominant_reactions: []
  faction_presence: []
  media_or_recording_presence: []
```

This enables consequences such as recognition, controversy, sponsorship interest or rival attention.

Exact Contest or battle scoring remains outside this layer.

## 15. Event-world integration

A public event should affect the surrounding settlement.

Potential temporary changes:
- lodging demand;
- vendor population;
- transport frequency;
- security presence;
- visitor factions;
- crowd density;
- public-space access;
- wild-Pokémon disturbance;
- cleanup needs;
- temporary jobs;
- price or supply pressure where economically modeled.

Potential aftermath:
- damaged infrastructure;
- new relationships;
- sponsorship agreements;
- faction influence;
- tourism reputation;
- permanent venue improvements;
- new regulations;
- rumors;
- historical records;
- recurring rivalries.

## 16. PTU / Caelo boundary

This layer orchestrates narrative state only.

Caelo already supports Social, Wild Encounter, PvP, Job, Raid, Contest, Gym and Dojo as distinct activity categories. A public event may combine several of these categories, but it does not replace their rules.

Before executable competition content is authored, validate:
- Contest rules;
- League/Gym restrictions;
- battle format;
- trainer participation rules;
- capture mechanics;
- Skill Checks;
- rewards and experience;
- environmental interactions;
- any Caelo-specific homebrew intentionally retained;
- AutoPTU objective and arena support.

## 17. Implementation priority

Recommended order:
1. witness reports;
2. public standing;
3. public memory objects;
4. event lifecycle;
5. edition history;
6. institution identity;
7. retired-character boundary enforcement;
8. commemoration;
9. audience state;
10. historical dispute generation.

This layer turns past player action into public culture while preserving provenance and player authorship.