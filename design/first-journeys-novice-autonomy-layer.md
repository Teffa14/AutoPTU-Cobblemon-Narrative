# Ouros First Journeys, Novice Autonomy & Supported Independence Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already models education, credentials, family/kinship, travel, Pokémon partnership, clubs, workplaces, care, housing, battle institutions and public memory. This layer models the transition from supported novice activity into increasingly independent field participation.

It does not define a universal starting age, adulthood threshold, Trainer license, family permission model or League law.

It must answer:
- what kind of first journey or novice track an actor is currently undertaking;
- what support is available;
- which activities are independently permitted;
- which activities still require supervision, a check-in or a separate credential;
- what milestones have actually occurred;
- what happened during departure, return, failure, interruption and resumption;
- how the actor's first Pokémon partnership develops without inventing Loyalty.

## Core separation

```text
chronological_age
  != novice_status
  != Trainer_Level
  != education_status
  != credential_scope
  != travel_permission
  != battle_capability
  != social_independence
```

An adult can be a first-time Trainer.
A young character can be highly experienced in one domain.
A high Trainer Level does not grant institutional permission.
Completing school does not prove a specific PTU Skill Rank.

## 1. First-journey record

```yaml
first_journey:
  journey_id: null
  actor_id: null
  sponsor_institution_ids: []
  mentor_actor_ids: []
  partner_pokemon_ids: []
  home_anchor_ids: []
  departure_event_id: null
  intended_scope_ref: null
  current_scope_ref: null
  milestone_ids: []
  support_contact_ids: []
  checkin_plan_ref: null
  return_event_ids: []
  status: proposed
  provenance_refs: []
```

Suggested states:
- planned;
- preparing;
- departed;
- active;
- temporarily_returned;
- interrupted;
- redirected;
- completed;
- withdrawn;
- superseded.

`completed` means the authored journey contract ended. It does not mean the character stopped travelling or became an expert.

## 2. Autonomy scope

Autonomy should be scoped instead of represented as one number.

```yaml
novice_autonomy_scope:
  scope_id: null
  actor_id: null
  geographic_scope_refs: []
  permitted_activity_refs: []
  supervision_requirements: []
  overnight_permission: unknown
  solo_travel_permission: unknown
  battle_responsibility_scope: []
  pokemon_custody_scope: []
  emergency_action_scope: []
  communication_requirements: []
  valid_from: null
  valid_until: null
  authority_refs: []
```

This object references Credentials/Permissions where formal authority exists.

Do not invent permissions because a route is technically reachable.

## 3. Support network

```yaml
journey_support_network:
  journey_id: null
  mentor_ids: []
  institution_ids: []
  clinic_ids: []
  transport_contact_ids: []
  lodging_refs: []
  emergency_contact_refs: []
  known_safe_location_ids: []
  supply_service_ids: []
  communication_channel_refs: []
```

A support network is available infrastructure, not a guarantee that someone will solve a problem for the player.

If a mentor is geographically distant or communications fail, support may be delayed.

## 4. First-partner transition

Receiving or choosing a first Pokémon can be a major world event without defining the relationship automatically.

```yaml
first_partner_event:
  event_id: null
  trainer_actor_id: null
  pokemon_entity_id: null
  transfer_or_association_type: null
  previous_custody_ref: null
  new_custody_ref: null
  ownership_claim_ref: null
  partnership_event_ref: null
  observed_initial_interactions: []
  mechanics_state_ref: null
  provenance_refs: []
```

Possible association types are narrative only until canon defines them:
- institutional_assignment;
- family_transfer;
- voluntary_partnership;
- rescue_followup;
- capture;
- preexisting_companion;
- authored_other.

The event does not automatically create:
- Loyalty;
- obedience;
- friendship;
- affection;
- ownership;
- mechanical bonuses.

## 5. Journey leg

```yaml
journey_leg:
  leg_id: null
  journey_id: null
  origin_location_id: null
  destination_location_id: null
  route_ref: null
  intended_departure_time: null
  actual_departure_time: null
  intended_return_or_checkin: null
  actual_return_or_checkin: null
  support_state_snapshot_ref: null
  world_state_snapshot_refs: []
  incident_ids: []
  outcome: null
```

A journey may consist of many small legs. Each leg can have a satisfying end without ending the entire campaign.

## 6. Milestones

Milestones describe lived experience, not automatic progression.

Examples:
- first overnight stay away from home;
- first independent route completed;
- first field report submitted;
- first wild encounter resolved without capture;
- first voluntary retreat;
- first emergency check-in;
- first return after an unsuccessful objective;
- first solo navigation leg;
- first time helping another novice;
- first institutional review after fieldwork.

```yaml
journey_milestone:
  milestone_id: null
  actor_id: null
  journey_id: null
  milestone_type: null
  event_refs: []
  witness_refs: []
  public_visibility: private
  mechanical_result_refs: []
```

No XP, stat, Skill, Edge or Feature reward is implied.

## 7. Check-ins and missed check-ins

```yaml
journey_checkin:
  checkin_id: null
  journey_id: null
  due_window: null
  actual_time: null
  channel_ref: null
  status: due|received|missed|delayed|impossible|waived
  reason_claim_refs: []
  escalation_event_refs: []
```

A missed check-in is an observation.
It does not prove injury, disappearance, disobedience or criminal activity.

The response should use Communications, Cases and Crisis state as appropriate.

## 8. Departure event

A departure should read the current world instead of existing as a canned ceremony.

Possible inputs:
- route condition;
- weather forecast;
- transport schedule;
- housing/home state;
- school or institution schedule;
- partner Pokémon state;
- current care status;
- active local events;
- existing relationships;
- equipment provenance and availability.

Possible outputs:
- journey starts as planned;
- departure delayed;
- route changed;
- group composition changed;
- scope reduced;
- support plan revised.

## 9. Return and debrief

Returning should create durable consequences.

```yaml
journey_debrief:
  debrief_id: null
  journey_id: null
  participant_ids: []
  event_summary_refs: []
  unresolved_question_refs: []
  damaged_or_consumed_asset_refs: []
  pokemon_state_refs: []
  route_information_refs: []
  new_contact_refs: []
  institution_feedback_refs: []
  next_scope_proposal_ref: null
```

Debrief does not rewrite the actor's memories or decide their emotions.

## 10. Failure-forward policy

Early journeys need meaningful failure without producing arbitrary career-ending punishment.

Valid consequences can include:
- returning early;
- asking for help;
- losing time;
- spending supplies;
- discovering a route was unsuitable;
- failing to complete a report;
- needing a supervised repeat;
- changing a planned destination;
- gaining a new unresolved question;
- having an institution keep the same autonomy scope rather than expanding it.

Do not invent Injury, death, confiscation, expulsion or loss of a Pokémon because the generator wants stakes.

## 11. Novice-risk budget

The narrative generator should consider actual support/capability state when selecting content.

Inputs may include:
- number of available Pokémon;
- known travel routes;
- access to clinics or safe lodging;
- communication reliability;
- current weather/hazard information;
- whether a mentor/supervisor is present;
- verified battle capability families;
- player-selected tone.

This is a content-selection heuristic, not PTU combat math.

The PTU first-session guidance is especially relevant: early Trainers may have only one Pokémon and therefore less redundancy than established teams.

## 12. Multiplayer parties with mixed scopes

Each PC keeps separate autonomy, credential and permission state.

A party leader cannot automatically lend another PC:
- route permission;
- institutional authorization;
- custody rights;
- battle credentials;
- private information;
- family consent;
- overnight permission.

The party may choose a route valid for everyone, split temporarily, or obtain the missing permissions.

## 13. Older first-time Trainers

Never write novice content as child-coded by default.

An older first-time Trainer may already have:
- employment;
- family responsibilities;
- travel experience;
- advanced academic expertise;
- professional credentials;
- established housing;
- social standing.

They may still be novice specifically in Pokémon battling, capture, League participation, fieldwork or partnership management.

## 14. Long-term transition

A first journey should naturally hand off into existing systems.

Possible transitions:
- novice → club member;
- novice → field researcher;
- novice → League challenger;
- novice → Ranger-like regional role if canon supports it;
- novice → apprentice/workplace trainee;
- novice → performer;
- novice → expedition participant;
- novice → mentor to a later character.

There is no universal success path.

## 15. Encounter contract — First Night Route Incident

Narrative premise:
A novice party is making its first planned overnight leg when a normal route becomes temporarily unusable. The problem is to decide whether to wait, return, reroute or resolve a local Pokémon conflict.

FULL version dependencies:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: BLOCKING if the encounter uses a moving escape corridor;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full lifecycle: PARTIAL;
- full stateful damage: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING if weather or route danger enters the grid;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for WITHDRAW/PROTECT/REACH_SAFE_TILE goals;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version:
Resolve route closure and weather entirely in overworld state. Freeze one safe static encounter arena. If combat happens, use ordinary legal combatants and basic objectives. After combat, return to the travel decision: wait, reroute or go home.

## 16. Encounter contract — Starter Partnership Field Test

Narrative premise:
An institution arranges a supervised field exercise where a Trainer and newly associated partner must complete a real task such as locating a marker, returning an item or assisting a local survey.

FULL version dependencies:
- standard verified geometry/movement/calculations/action economy;
- PARTIAL move/Ability/Item/Feature families only when exact content is implemented;
- BLOCKING tactical AI if the partner must act autonomously toward a non-KO objective;
- BLOCKING adapter/playback for synchronized world objectives.

REDUCED version:
Keep the field objective outside battle. If a static wild encounter occurs, run it normally. The debrief records observed cooperation and choices without generating Loyalty.

## 17. Encounter contract — Return Before Dark

Narrative premise:
A day trip runs late because an earlier objective took longer than expected. The party must choose between a known longer route, waiting at a safe site, or using a poorly surveyed shortcut.

FULL version dependencies:
- complete movement: BLOCKING for dynamic pursuit/escape;
- terrain/weather/hazards/zones/reactions: BLOCKING if darkness/weather changes tactical rules;
- AI tactical policy: BLOCKING for REACH_EXIT/WITHDRAW;
- adapter/playback: BLOCKING.

REDUCED version:
Resolve time, visibility, route feasibility and shelter in the overworld. Any combat uses a frozen arena with no invented darkness penalties.

## 18. Engine boundary

AutoPTU-Java owns battle legality and resolution.
The narrative/world server owns journey state, support, permissions, check-ins and route decisions.
Minecraft presents the current world and requests actions.

The adapter must not implement:
- novice combat bonuses;
- hidden safety modifiers;
- starter obedience rules;
- automatic capture assistance;
- guardian interrupts;
- route permission;
- evacuation AI;
- dynamic weather penalties.

## 19. Canon gates

Before promotion to canon, define or explicitly leave unresolved:
- whether Ouros has a general Trainer registration system;
- whether any minimum age exists, and where;
- which institutions sponsor first journeys;
- how guardianship works for authored minor NPCs;
- what permissions are needed for overnight or interregional travel;
- how first Pokémon are normally obtained in each region;
- whether starter traditions differ by culture/institution;
- whether the League has any authority over ordinary Trainers;
- what emergency support exists outside settlements.

No default answer should be imported from one Pokémon region and treated as universal Ouros law.
