# Sports, Racing & Athletic Culture Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon.

## Purpose

Ouros needs persistent physical competition outside Pokémon battles and Contests. This layer covers races, relays, obstacle courses, endurance events, mounted competition, navigation sport, community athletic meets and mixed-discipline festivals.

It does not create a new PTU rules subsystem. Mechanical resolution must use governing PTU/Caelo Skills, capabilities, movement rules and any later approved sport-specific rules.

## Core separation

Keep these states independent:

1. SPORT_DEFINITION — what kind of activity this institution recognizes.
2. EVENT_INSTANCE — one scheduled occurrence.
3. COURSE_VERSION — the physical route or arena used for that occurrence.
4. ENTRY — participant/team registration and eligibility state.
5. MECHANICAL_RESOLUTION — authoritative PTU/Caelo/AutoPTU result when applicable.
6. OFFICIAL_RESULT — placement, time, score or completion status accepted by the organizer.
7. PUBLIC_RECEPTION — how spectators/media react.
8. CAREER_RECORD — persistent history for athlete, Trainer, Pokémon, team and institution.

A popular performance is not automatically an official win. An official win is not automatically a PTU progression reward.

## Data model

### SPORT_DEFINITION

```yaml
sport_id: null
name: null
status: proposed
activity_family: null
institution_ids: []
participant_model: null
allowed_course_types: []
mechanical_authority: null
ruleset_version_ids: []
required_capability_families: []
prohibited_assumptions: []
source_inspiration_refs: []
```

Possible activity families are descriptive only:
- FOOT_RACE
- RELAY
- OBSTACLE
- MOUNTED_RACE
- SURF_OR_WATER_RACE
- AERIAL_COURSE
- NAVIGATION
- ENDURANCE
- PRECISION
- TEAM_POSITIONAL
- MIXED_DISCIPLINE

Do not assign mechanical meaning to these labels by themselves.

### ATHLETIC_INSTITUTION

```yaml
institution_id: null
name: null
location_ids: []
recognized_sports: []
venue_ids: []
organizer_ids: []
medical_support_refs: []
record_archive_ref: null
public_standing: null
season_schedule_refs: []
```

An institution may be a local club, school league, town association, racing stable, surf organization, regional circuit or annual festival committee.

### COURSE_VERSION

```yaml
course_version_id: null
sport_id: null
base_location_ids: []
world_state_snapshot_ref: null
start_ref: null
finish_ref: null
checkpoints: []
route_segments: []
temporary_event_objects: []
restricted_zones: []
known_hazards: []
weather_policy_ref: null
conservation_constraints: []
accessibility_notes: []
version_reason: null
valid_from: null
valid_until: null
```

Course versions are important because roads, bridges, trails and waterfronts change over time.

### EVENT_INSTANCE

```yaml
event_id: null
sport_id: null
institution_id: null
course_version_id: null
status: scheduled
ruleset_version_id: null
entry_window: null
scheduled_time_ref: null
weather_decision_state: null
participant_entries: []
officials: []
service_dependencies: []
result_ref: null
public_event_ref: null
```

Suggested event states:
- PROPOSED
- SCHEDULED
- REGISTRATION_OPEN
- READY
- DELAYED
- ACTIVE
- SUSPENDED
- COMPLETED
- CANCELLED
- UNDER_REVIEW

### ATHLETE_ENTRY

```yaml
entry_id: null
trainer_ids: []
pokemon_ids: []
team_id: null
entry_class: null
eligibility_checks: []
verified_capabilities: []
verified_mechanical_refs: []
withdrawal_state: null
```

Eligibility must be derived from approved rules and current Pokémon/Trainer state. Narrative generation cannot create Mountable eligibility, movement capability, Skill Rank or Feature access.

### SPORT_RULESET_VERSION

```yaml
ruleset_version_id: null
sport_id: null
effective_date: null
mechanical_source_refs: []
scoring_model_ref: null
contact_policy: null
interference_policy: null
substitution_policy: null
course_policy: null
withdrawal_policy: null
safety_policy: null
```

Most values may remain unresolved until authored. The system must not fill them using assumptions from Pokéathlon, Rhyhorn racing or real-world sport.

### OFFICIAL_ATHLETIC_RESULT

```yaml
result_id: null
event_id: null
status: provisional
placements: []
completion_records: []
disqualifications: []
withdrawals: []
mechanical_resolution_refs: []
review_notes: []
record_changes: []
```

Possible statuses:
- PROVISIONAL
- OFFICIAL
- AMENDED
- VOID

## Athletic careers

An athletic career can remember:
- participation history;
- best official placements;
- course-specific records;
- rivals encountered;
- club affiliation;
- coaching relationships;
- injuries only when authoritative health state supports them;
- public reputation;
- sponsorship relationships if those systems become canon;
- transitions from athlete to coach, organizer, steward or official.

Do not infer retirement, burnout, injury, family pressure or ambition without authored evidence.

## Records and course history

Records should be contextual, not global numbers detached from history.

```yaml
record_id: null
sport_id: null
course_version_id: null
ruleset_version_id: null
holder_ids: []
result_ref: null
set_at: null
conditions_ref: null
status: current
superseded_by: null
```

A route rebuilt after a landslide may create a new course version rather than pretending the old record is directly comparable.

## Rivalries

Athletic rivalries use the existing social-bond and public-memory layers.

A rival may remember:
- prior placements;
- observed strategies;
- public interviews;
- shared clubs;
- course preferences;
- sportsmanship incidents.

The system cannot infer hatred, friendship or obsession from repeated competition.

## Training and practice

Practice may update narrative state:
- route familiarity;
- coach relationship;
- institutional access;
- recorded practice attempts;
- public anticipation;
- equipment readiness;
- team routine familiarity.

Practice does not create unsupported Speed, Athletics, Acrobatics, Jump, Combat Stage or capability bonuses.

When a PTU Feature, Edge or approved training rule changes mechanics, the authoritative mechanical layer owns that change.

## Course-world integration

Sport should reuse the existing world rather than spawn disconnected arenas whenever possible.

Examples:
- a harbor hosts a paddling event;
- an old road becomes a relay route;
- a mountain pass hosts a seasonal endurance challenge;
- a restored bridge returns to an annual race;
- a surf route doubles as normal inter-island transport;
- a school field hosts short local events;
- a conservation area allows a controlled race only outside nesting season.

The event must read current route, crisis, construction, ecological and calendar state.

## Event interruption and recovery

Events can react to world state:
- severe weather;
- infrastructure failure;
- wildlife movement;
- emergency response;
- route closure;
- medical capacity;
- public-safety decision.

Cancellation should not require a villain.

Rescheduling preserves the event object and its history rather than deleting it.

## Multiplayer participation

A multiplayer event can support different roles:
- competitor;
- teammate;
- coach;
- route scout;
- volunteer;
- medic/support staff;
- journalist;
- spectator;
- organizer.

Players should not be forced into direct competition to participate meaningfully.

Private training plans remain private unless shared or observed.

## Minecraft presentation

Possible overworld manifestations:
- temporary start/finish structures;
- banners and route markers;
- spectator clusters;
- participant staging zones;
- scoreboards or record plaques;
- clubhouses;
- training tracks;
- stable or mount-care areas;
- course marshals;
- changed transport schedules during a major event.

Do not persist hundreds of spectators as full simulated NPCs. Use representative crowds and event-state presentation.

## PTU/Caelo mechanical boundary

Public PTU material confirms that Acrobatics and Athletics can govern physical competition contexts. PTU also has explicit mounted play and Rider mechanics.

This layer does not define:
- race DCs;
- opposed-check formulas;
- mount eligibility;
- collision rules;
- drafting;
- stamina meters;
- fatigue;
- sport injuries;
- course speed conversion;
- scoring math;
- event rewards;
- Trainer progression;
- Pokémon progression.

Those require source validation and, where tactical execution occurs, AutoPTU support.

## Engine-capability mapping

The permanent engine categories apply to any event entering AutoPTU.

### Can often stay outside battle engine

Pure overworld timing, registration, course knowledge, public results and career history can remain narrative/world-state systems.

### Basic tactical athletic encounter

A bounded obstacle or checkpoint encounter may depend on:
- targeting/footprints/range/LoS: only if target selection matters;
- base movement legality: REQUIRED;
- core calculations: MAY BE REQUIRED if rules call for them;
- action economy/initiative: REQUIRED if resolved in rounds;
- AI legal-action infrastructure: REQUIRED for autonomous participants.

### Rich race/obstacle version

May additionally require:
- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

Do not mark a sport implementable merely because ordinary Shift movement exists.

## Encounter contracts

### Cliffside Relay

Narrative premise:
A regional relay uses a maintained cliff road. A recent repair changed one segment, creating a new official course version.

FULL VERSION:
- multiple autonomous competitors;
- route choice;
- terrain-cost decisions;
- safe overtaking/interception rules if the sport permits them;
- objective-aware AI pursuing checkpoints rather than enemies;
- live event playback in Minecraft.

Dependencies:
- base movement legality: VERIFIED;
- complete movement incl. interception/forced movement: BLOCKING for rich interaction;
- action economy/initiative: VERIFIED foundation;
- full turn/round lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- Trainer Features/perks: PARTIAL INFRASTRUCTURE ONLY, not enough for full rules;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED VERSION:
Resolve route traversal through validated PTU Skill checks/world-state logic outside AutoPTU. If a separate battle happens because of an actual incident, open a normal static encounter. Preserve official race result separately.

### Harbor Sprint Festival

Narrative premise:
A harbor district runs a short athletic festival combining foot travel and legal Pokémon-assisted traversal through public waterfront space.

FULL VERSION:
- timed checkpoint course;
- route blockers;
- participant collision rules only if governing sport rules define them;
- weather-dependent course decision;
- spectators and service closures in Minecraft.

Dependencies:
- base movement legality: VERIFIED;
- complete movement: BLOCKING for collision/interception-rich version;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- abilities/items/Trainer Features: PARTIAL/PARTIAL/PARTIAL-INFRASTRUCTURE and require exact mechanic support;
- AI tactical policy: BLOCKING;
- playback: BLOCKING.

REDUCED VERSION:
Keep festival and route state in overworld. Use opposed/team Skill checks validated from PTU/Caelo for the competition. AutoPTU is not invoked unless a legal battle occurs.

### Ridge Rescue Race

Narrative premise:
An established endurance event is interrupted when a nonparticipant becomes stranded near the course. Competitors may continue, stop to help or withdraw according to event policy and player choice.

FULL VERSION:
- active race state plus rescue objective;
- dynamic objective priorities;
- route hazards;
- movement and protection decisions;
- objective-aware AI.

Dependencies:
- complete movement: BLOCKING;
- full lifecycle: PARTIAL;
- hazards/zones/reactions: BLOCKING;
- AI tactical policy: BLOCKING;
- playback: BLOCKING.

REDUCED VERSION:
Suspend the official event state. Resolve rescue as overworld/crisis content. Resume, amend or cancel the race according to institutional policy. No tactical rescue mechanic is invented.

## Promotion checklist

Before a sport or event becomes canon:
1. Confirm regional and institutional fit.
2. Confirm activity does not duplicate an existing Contest or battle institution.
3. Validate all Skill/capability/mount rules against PTU/Caelo.
4. Define ruleset version and official-result authority.
5. Verify engine dependencies if tactical simulation is required.
6. Provide a reduced implementation if full dependencies remain blocked.
7. Confirm welfare, route and conservation interactions.
8. Keep external-source inspiration transformed and attributed in research only.
