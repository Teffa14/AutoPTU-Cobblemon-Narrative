# Ouros Contest, Performance Culture & Creative Circuit Layer

Status: proposed systems architecture. Not established Ouros canon.

## Purpose

Ouros needs a durable path for Pokémon-centered performance that can matter as much as combat, exploration, research or crafting without replacing PTU Contest mechanics.

This layer models the world around performance: venues, schedules, careers, audiences, rehearsals, productions, professional relationships, public reception, awards and long-term creative identity.

The rules engine remains authoritative for actual Contest resolution.

## Core separation

Keep these states distinct:

1. Performance world state — what event exists, where, when and under which institution.
2. Participant state — who entered, who performs, who supports and who withdrew.
3. Routine/production state — what the participants plan to present.
4. Mechanical Contest state — PTU Contest Stats, dice, Appeal, Fumble, Effects and legal Moves.
5. Formal result — placements, advancement, ribbons or institutional records.
6. Public reception — what audiences, peers and critics thought.
7. Career memory — how this performance changes future opportunities and relationships.

Narrative generation may create layers 1–3, 6 and 7. It must not fabricate layer 4 or rule-derived parts of layer 5.

## Performance event object

Suggested structure:

```yaml
event_id: null
event_type: CONTEST
status: ANNOUNCED
edition: 1
venue_id: null
circuit_id: null
host_institution_id: null
start_window: null
registration_state: OPEN
participant_ids: []
support_role_ids: []
judge_role_ids: []
host_role_ids: []
audience_profile_id: null
format_ref: null
ruleset_ref: PTU_CAEL0_REQUIRED
phases: []
formal_results: []
public_reception_refs: []
world_state_dependencies: []
source_refs: []
```

Possible event types can include CONTEST, EXHIBITION, RECITAL, FILM_PRODUCTION, FESTIVAL_SHOW, CLUB_SHOWCASE or other future Ouros traditions. Only CONTEST is assumed to use the PTU Contest subsystem unless another format is explicitly authored and validated.

## Event lifecycle

A performance event may move through:

ANNOUNCED → REGISTRATION → PREPARATION → REHEARSAL → LIVE → JUDGING → AFTERSHOW → ARCHIVED

Optional outcomes include POSTPONED, RELOCATED and CANCELLED when world state supports them.

The lifecycle gives other systems time to interact with the event before the result exists.

## Venue object

A venue should have persistent identity.

```yaml
venue_id: null
settlement_id: null
venue_type: null
operator_id: null
capacity_class: null
stage_profile: null
backstage_capabilities: []
public_access: null
calendar_refs: []
local_traditions: []
known_constraints: []
prestige_state: null
maintenance_state: null
history_refs: []
```

Capacity is narrative unless an implementation needs a concrete number. Do not spawn one Minecraft entity per audience member.

A venue can change over time:
- repaired;
- expanded;
- damaged;
- renovated;
- rebranded;
- repurposed;
- temporarily closed;
- used as an emergency shelter;
- moved to an outdoor temporary stage.

## Circuit object

A circuit connects events into a career path.

```yaml
circuit_id: null
name: null
season_id: null
host_regions: []
event_ids: []
qualification_policy_ref: null
final_event_id: null
public_calendar_state: null
travel_impacts: []
historical_champions: []
```

Qualification mechanics must reference PTU/Caelo or authored Ouros rules. Narrative generation may arrange dates and host locations, but it cannot invent Ribbon thresholds or mechanical eligibility.

## Performer profile

A performer profile describes public career history without replacing a Trainer sheet.

```yaml
performer_profile_id: null
trainer_id: null
pokemon_partner_ids: []
known_specialties: []
public_aliases: []
venue_history: []
event_history: []
formal_awards: []
peer_relationship_refs: []
audience_recognition: {}
professional_standing: {}
creative_identity_notes: []
```

Do not turn subjective labels into mechanics. “Known for dramatic fire-themed finales” can be a public description. It does not grant a Beauty bonus.

## Routine / act object

A routine is a plan, not a guaranteed result.

```yaml
routine_id: null
creator_ids: []
performer_ids: []
participating_pokemon_ids: []
intended_theme: null
segment_plan: []
prop_refs: []
venue_requirements: []
rehearsal_notes: []
known_risks: []
mechanics_review_required: true
```

The generator may propose an intended theme or dramatic structure. If a routine depends on specific Moves, Abilities, Skills, Contest Effects or capabilities, every one must be validated before implementation.

## Rehearsal state

Rehearsal should generate information rather than free power.

A rehearsal can reveal:
- timing problems;
- stage-space conflicts;
- prop failures;
- Pokémon discomfort;
- communication issues;
- venue limitations;
- schedule conflicts;
- uncertainty about a planned transition.

It must not silently award PTU bonuses unless rules explicitly provide them.

## Formal result versus public reception

Store formal outcome separately from reception.

Formal result can include:
- official placement;
- advancement;
- disqualification;
- judge ruling;
- rule-derived award.

Public reception can include:
- local enthusiasm;
- peer respect;
- controversy;
- fan interest;
- press attention;
- divided opinion;
- strong reaction to one Pokémon or one segment.

A player may place second while becoming the crowd favorite. Another may win while becoming controversial. Neither state changes PTU mechanics automatically.

## Audience model

Represent audiences as aggregate state plus representative actors.

```yaml
audience_profile_id: null
expected_scale: SMALL
local_share: null
visitor_share: null
interest_tags: []
known_fan_groups: []
media_presence: []
faction_presence: []
sentiment_refs: []
representative_npc_ids: []
```

Avoid total-population simulation.

Audience state can affect world presentation:
- fuller stands;
- banners;
- temporary vendors;
- traffic;
- transport demand;
- hotel demand;
- public chatter;
- photographers;
- fan clubs;
- empty seats after a controversy or crisis.

These are causal world effects, not Contest modifiers.

## Professional relationships

Performance creates relationship types not covered by simple friendship.

Possible edges:
- recurring_competitor;
- creative_partner;
- mentor_of;
- former_partner;
- troupe_member;
- sponsor_of;
- venue_favorite;
- judge_history;
- critic_history;
- fan_of;
- professional_debt;
- collaboration_invite;

Player-controlled emotional states remain consent-sensitive under the existing social-bond rules.

## Rival performer memory

A professional rival may remember:
- prior official placements;
- routines they witnessed;
- themes the player repeats;
- public praise or criticism;
- collaborations;
- promises;
- scheduling conflicts;
- moments of sportsmanship;
- shared mentors.

The system should not infer jealousy, romance, hatred or friendship unless authored.

## Creative evolution

A performer should change over time through authored state rather than numeric grind alone.

Possible observable evolution:
- tries a new theme;
- changes partner Pokémon;
- abandons an overused routine;
- begins collaborative shows;
- becomes a mentor;
- tours smaller venues;
- returns after a hiatus;
- shifts from competition into production, judging or teaching;
- uses previous public criticism as a design constraint.

No mechanical benefit is implied.

## Show production roles

Performance content should remain valuable for non-performers.

Possible roles:
- performer;
- coordinator;
- stage manager;
- announcer;
- judge;
- photographer;
- costume/prop artisan;
- venue technician;
- researcher;
- security responder;
- medic;
- organizer;
- vendor;
- transport operator;
- chronicler.

Each role should connect to existing Skills, professions or world-state systems only after rules review.

## Staged scenario mode

Pokéstar Studios demonstrates that Pokémon mechanics can support scenario objectives. Ouros can use the same high-level principle for film, theater or exhibition encounters.

A staged scenario may specify narrative goals such as:
- hold a position until a cue;
- protect a prop;
- deliberately lose at the correct moment;
- trigger a visual effect;
- deliver dialogue before an action;
- complete a sequence under time pressure.

These are design intents only. AutoPTU must explicitly support a safe/staged encounter mode before any battle-state effects, injury assumptions, AI constraints or win conditions are implemented.

## Production artifact

A completed performance can become a persistent public-memory artifact.

```yaml
production_record_id: null
event_id: null
performer_ids: []
result_ref: null
public_summary: null
venue_id: null
recorded_at: null
archive_location_id: null
rights_state: null
source_event_refs: []
```

This allows posters, photos, programs, trophies, statues, newspaper references or museum exhibits without storing copyrighted external media.

## Performance economy

Events may create causal demand for:
- lodging;
- transport;
- food;
- costumes;
- props;
- flowers;
- photography;
- stage repair;
- souvenirs;
- security;
- rehearsal rooms.

Use the existing material-culture and settlement systems. Do not introduce dynamic economic simulation solely for performance.

## Calendar and travel integration

Circuit events create time-sensitive but predictable travel.

The travel layer should know:
- event dates;
- registration windows;
- venue changes;
- transport disruptions;
- expected visitor pressure;
- whether routine travel can be compressed.

A missed event can become career history, but the system should not punish an absent/offline multiplayer participant through hidden scheduling assumptions.

## Festivals versus Contests

A public festival may contain a Contest, but they are different objects.

Festival = broader civic/cultural event.
Contest = PTU-governed competitive activity.

A festival can contain exhibitions, food, craft markets, club booths, performances, ceremonies, research demonstrations and a Contest in parallel.

This distinction prevents every public celebration from becoming a tournament.

## Cooperative performance

Not every show needs a winner.

Ouros should support collaborative exhibitions where success is based on completing the event, satisfying an institution, entertaining an audience, revealing a story or participating in a tradition. If a mechanical resolution is needed, it must be authored separately rather than borrowing Contest scoring automatically.

## Failure-forward career logic

When a participant fails to advance or loses a Contest, the narrative layer can still generate:
- critique;
- peer conversation;
- new practice objective;
- invitation to collaborate;
- fan recognition;
- sponsor withdrawal;
- sponsor interest;
- changed venue opportunity;
- return-match hook;
- public-memory entry.

Avoid “win or content disappears.”

## Minecraft representation

Possible overworld expression:
- venue buildings;
- temporary outdoor stages;
- rehearsal rooms;
- backstage areas;
- posters and schedules;
- crowd proxies;
- fan NPCs;
- decorators;
- vendor stalls;
- winner portraits;
- trophy cases;
- banners;
- transport congestion;
- changed lighting or stage layouts;
- archived memorabilia.

Physical representation must remain performance-conscious. Large audiences should use sparse representative NPCs and environmental dressing rather than thousands of entities.

## AutoPTU interface proposal

Narrative layer should eventually request a Contest or staged scenario with structured inputs, not calculate it itself.

Example future request:

```yaml
activity_type: CONTEST
ruleset_ref: PTU_CAEL0
participant_refs: []
contest_type: null
variant_ref: null
venue_ref: null
```

AutoPTU or a dedicated Contest module returns authoritative mechanical outcome data. Narrative then records the result and derives public/career consequences.

For film/theater scenarios, use a separate activity type until explicit mechanics exist.

## Required mechanical extraction before implementation

A dedicated engineering pass should extract from supplied PTU/Caelo material:
- Contest Stat derivation;
- Introduction Stage rules;
- Performance Stage order;
- Appeal scoring;
- Center of Attention;
- Voltage;
- Fumble;
- Contest Types and allied/opposed relationships;
- every Contest Effect;
- Contest variants;
- Poffins and Contest Stats;
- Coordinator and Style Expert interactions;
- Caelo Contest Hall Circuit modifications;
- Caelo rewards and limits;
- any errata affecting Contests.

Do not implement from public mirrors when the supplied project corpus is available.

## Generation guardrails

The generator must not:
- convert fame into PTU bonuses;
- assume a Contest winner before resolution;
- fabricate Ribbon requirements;
- invent judge scores;
- assign Contest Stats from personality;
- infer that a beautiful Pokémon has Beauty dice;
- assume a Move is good for a category without its legal Contest Type/Effect;
- create new Contest Effects through narrative prose;
- make every festival a Contest;
- make every performer a Coordinator class Trainer;
- treat public criticism as objective truth;
- force emotional rivalry between player characters;
- simulate mass audiences as thousands of Minecraft entities;
- use battle KO as the default performance objective.

## Success criteria

This layer succeeds when a player can build a recognizable creative career whose venues, peers, audiences, travel, public history and opportunities persist between events while every mechanical Contest result still comes from validated PTU/Caelo rules.
