# Recurring Companion, Guide & Mentor Continuity Extension

Status: DESIGN PROPOSAL. New NPCs, events, roles, institutions and story content introduced here are NON-CANON unless separately approved. Existing project authority boundaries remain governing architecture.

Date: 2026-08-30

## Purpose

Ouros already models relationships, mentorship, actor agency, journeys, expeditions, rivalry and campaign convergence. This extension adds a narrow missing continuity layer for recurring non-rival NPC participation.

It answers one question: when a persistent NPC accompanies the player for a bounded part of an activity, how does Ouros remember that episode, its scope, its role, its departure and any later return without turning the NPC into a permanent party member?

This layer does not own affection, mentorship progression, travel routing, actor goals, faction authority, battle legality or campaign convergence. It links those authoritative states.

## 1. Authority boundaries

Relationship state remains in `social-bonds-mentorship-clubs-layer.md`.

Actor goals, knowledge, resources and autonomous action remain in `world-agency-layer.md`.

Journey and expedition participation remain in `travel-transport-expedition-layer.md`.

Competitive peer history remains in `rivalry-recurring-peer-progression-extension.md`.

Campaign-scale arrival and convergence checks remain in `campaign-arc-convergence-pressure-payoff-extension.md`.

Battle participation and tactical facts remain authoritative only when an explicit reviewed BattleSpec includes that actor.

The companion layer stores the history and scope of participation episodes. It must reference, not duplicate, these other states.

## 2. Companion episode

A companion episode is a bounded period in which one persistent NPC participates alongside the player or player group for a defined reason.

```yaml
companion_episode:
  companion_episode_id: null
  npc_id: null
  status: planned
  episode_kind: null
  role_at_start: null
  role_history: []
  scope_type: null
  scope_ref: null
  start_event_id: null
  end_event_id: null
  shared_objective_refs: []
  journey_or_expedition_refs: []
  location_refs: []
  relationship_ref: null
  world_agenda_ref: null
  knowledge_snapshot_refs: []
  presence_records: []
  departure_reason_ref: null
  return_candidate_refs: []
  provenance_refs: []
  canon_status: proposed
```

Candidate `episode_kind` values:

- LOCAL_GUIDE
- TEMPORARY_TRAVEL_COMPANION
- FIELD_SPECIALIST
- MENTOR_FIELD_EPISODE
- RESEARCH_PARTICIPANT
- INSTITUTIONAL_ESCORT
- CRISIS_SUPPORT
- TEMPORARY_ALLY
- WITNESS_OR_OBSERVER
- HOST_OR_LIAISON

These labels describe narrative function only. They grant no PTU statistics, authority or action economy.

## 3. Scope is mandatory

Every companion episode should have an intelligible scope.

Candidate scope forms:

- one scene;
- one route segment;
- one settlement visit;
- one dungeon section;
- one expedition leg;
- one field task;
- one institutional appointment;
- one crisis operation;
- one investigation node;
- one explicitly authored multi-scene objective.

A scope may be open-ended in time while still bounded by purpose.

Examples:

- guide until the ridge where their local knowledge ends;
- researcher until samples are secured;
- mentor through one supervised field exercise;
- liaison until the group reaches the host institution;
- witness through one hearing day;
- rescue specialist until evacuation staging is complete.

`JOINED_FOR_ONE_SCOPE != PERMANENT_PARTY_MEMBER`.

## 4. Presence has separate lanes

One boolean such as `with_party` is too coarse.

```yaml
companion_presence:
  episode_id: null
  npc_id: null
  scene_presence: false
  journey_participation: false
  field_support_presence: false
  social_presence: false
  battle_eligibility_ref: null
  battlespec_participant_ref: null
  effective_from_event: null
  effective_until_event: null
```

Important boundaries:

- an NPC can travel with the group and remain outside combat;
- an NPC can be at a campsite but not join the next field segment;
- an NPC can participate in a battle without being a long-term travel companion;
- a mentor can observe an exercise without becoming a tactical controller;
- a guide can leave before a dangerous zone while remaining socially friendly.

`TRAVELS_WITH_PARTY != COMBATANT`.

`PRESENT_IN_SCENE != PRESENT_IN_BATTLESPEC`.

## 5. Role-at-the-time

A persistent NPC should not be frozen into one narrative function.

```yaml
companion_role_episode:
  role_episode_id: null
  companion_episode_id: null
  role_type: null
  begins_at_event_id: null
  ends_at_event_id: null
  authority_ref: null
  competency_ref: null
  obligation_refs: []
  notes: []
```

A character may first appear as a guide, later become a colleague, return as a witness, then eventually become a mentor or cease mentoring while remaining a friend.

Role transitions must not rewrite earlier history.

`RETURNED != SAME_ROLE`.

`MENTOR != AUTHORITY`.

A mentor only has institutional or procedural authority when another governing system establishes it.

## 6. Joining an episode

A join event should have a cause.

```yaml
companion_join_event:
  event_id: null
  npc_id: null
  companion_episode_id: null
  invitation_source: npc|player|institution|shared_event|other
  stated_reason_refs: []
  world_reason_refs: []
  scope_acknowledged: null
  current_location_ref: null
  travel_viability_ref: null
  relationship_context_ref: null
  authored_constraints: []
  outcome: joined|declined|delayed|unable|unknown
```

Possible causes:

- overlapping destination;
- local-guide contract or favor;
- shared investigation;
- mentor field exercise;
- research objective;
- rescue deployment;
- institutional assignment;
- personal request;
- temporary alignment during a crisis;
- mutual need for access or information.

Friendship by itself is not a join condition.

## 7. Availability decomposition

Companion availability should be composed from existing authoritative facts rather than one hidden loyalty score.

Candidate questions:

- does the NPC know about the opportunity?
- where are they currently located?
- can they reach the start point?
- do they have time?
- do their current goals support participation?
- are institutional or personal obligations blocking them?
- are they willing under authored relationship/personality state?
- does the requested role fit what they can actually do?
- is the route currently viable?

Possible evaluated outcomes:

- AVAILABLE
- AVAILABLE_LATER
- WILLING_BUT_UNREACHABLE
- REACHABLE_BUT_UNWILLING
- OBLIGATION_CONFLICT
- ROLE_MISMATCH
- INFORMATION_MISSING
- DECLINED
- UNKNOWN

These are orchestration results, not emotional labels.

`FRIEND != AVAILABLE`.

`AVAILABLE != WILLING`.

`WILLING != ABLE_TO_REACH`.

## 8. Departure is an event, not deletion

```yaml
companion_departure_event:
  event_id: null
  companion_episode_id: null
  npc_id: null
  departure_type: scope_complete
  cause_refs: []
  departure_location_ref: null
  known_next_intent_refs: []
  unresolved_commitment_refs: []
  relationship_effect_ref: null
  next_contact_candidate_refs: []
  provenance_refs: []
```

Candidate departure types:

- SCOPE_COMPLETE
- PERSONAL_GOAL_COMPLETE
- ROUTE_BOUNDARY
- ROLE_NO_LONGER_NEEDED
- INSTITUTIONAL_RECALL
- SCHEDULE_OR_OBLIGATION
- VOLUNTARY_DIVERGENCE
- SAFETY_WITHDRAWAL
- ACCESS_LIMIT
- DISAGREEMENT_WITHOUT_RUPTURE
- RELATIONSHIP_RUPTURE if explicitly established elsewhere
- SEPARATED_BY_EVENT
- UNKNOWN

Departure does not itself establish rejection, betrayal, death, disappearance or relationship break.

`LEFT_PARTY != RELATIONSHIP_BROKEN`.

`DEPARTURE_EVENT != DISAPPEARANCE`.

## 9. Temporary separation

A companion episode can remain open while participants temporarily separate.

```yaml
companion_separation:
  episode_id: null
  starts_at_event_id: null
  reason_ref: null
  expected_rejoin_condition: null
  actual_rejoin_event_id: null
  current_state: separated
```

Useful cases:

- player temporarily exits the intended route;
- guide waits at a known landmark;
- specialist remains at base camp while player scouts ahead;
- group splits to handle parallel objectives;
- NPC cannot cross one access boundary;
- evacuation separates participants before a rendezvous.

A predicted rejoin is a plan, not a guaranteed future fact.

## 10. Reunion eligibility

A past companion can become a reunion candidate when current state creates a plausible new overlap.

This extension must reuse the campaign convergence principle rather than teleporting familiar characters into scenes.

Before a reunion, check:

- knowledge;
- current location and route;
- ability to reach;
- current motive;
- current obligations;
- resources;
- relationship constraints;
- relevance of the proposed role;
- whether the callback adds changed context.

```yaml
companion_return_candidate:
  candidate_id: null
  npc_id: null
  prior_episode_ids: []
  current_trigger_refs: []
  knowledge_ok: null
  reach_ok: null
  motive_ok: null
  availability_ok: null
  role_candidate: null
  changed_context_refs: []
  status: candidate
```

`REUNION_EXPECTED != REUNION_GUARANTEED`.

## 11. Returning with changed context

A reunion should usually reveal that time has passed.

Possible changes:

- different professional role;
- changed institution;
- new project;
- changed knowledge;
- new obligations;
- different route familiarity;
- improved or reduced access;
- altered social relationship established elsewhere;
- changed opinion explicitly authored by the NPC;
- changed public reputation;
- another companion or organization now depends on them.

The system should prefer a changed callback over identical repetition.

`SAME_NPC_RETURNED != SAME_KNOWLEDGE_STATE`.

## 12. Independent life while absent

`ABSENT != INACTIVE`.

When an NPC is no longer in a companion episode, World Agency may continue evaluating their goals and actions according to ordinary rules.

The companion layer may reference outputs such as:

- relocated;
- completed another job;
- failed to complete another job;
- joined another expedition;
- entered a new institution;
- became unavailable;
- learned a public fact;
- encountered a blocker;
- changed schedule.

It must not simulate these outcomes itself.

## 13. Knowledge boundary

Traveling together creates opportunities to share information, not automatic omniscience.

A companion only knows:

- what they directly observed;
- what another actor communicated to them;
- what public or institutional sources they legitimately accessed;
- what their own prior knowledge state already contained.

A player similarly does not automatically receive every private fact the companion knows.

Conversation, reports, explicit warnings and observed actions create evidence of information transfer.

## 14. Advice without railroading

A guide or mentor may offer advice when it follows from authored personality, current knowledge and role.

Advice should be represented as an actor claim, recommendation or warning. It is not privileged narration.

The NPC may be:

- correct;
- partially correct;
- cautious;
- mistaken because information is stale;
- unwilling to advise;
- knowledgeable only within a local domain.

A companion must not become a hidden `correct route` flag.

## 15. Shared goal and loyalty remain separate

Two actors can cooperate because their goals overlap temporarily.

Examples:

- both need the same road reopened;
- both want civilians evacuated;
- both need access to the same archive;
- both oppose one immediate threat;
- both need the same scientific observation;
- both need to reach the same settlement.

This does not imply permanent alliance, obedience or social intimacy.

`SHARED_GOAL != SHARED_LOYALTY`.

`SUPPORTS_PLAYER != OBEYS_PLAYER`.

## 16. Mentor-specific boundary

Mentorship state and learning milestones remain in Social Bonds and governing PTU/Caelo progression rules.

A `MENTOR_FIELD_EPISODE` can record:

- the mentor accompanied this exercise;
- the learner attempted a task;
- the mentor observed a battle;
- feedback was later given;
- the mentor left when the supervised scope ended.

It cannot grant a Skill Rank, Edge, Feature, Tutor Move, stat increase or other mechanical benefit without explicit governing authority.

## 17. Specialist-specific boundary

A specialist can make an expedition more plausible without becoming a universal solution.

Examples:

- local route guide;
- researcher;
- conservator;
- technician;
- medic;
- interpreter;
- historian;
- infrastructure operator;
- liaison.

Their participation may unlock access to work they are actually authorized and equipped to perform. It does not automatically establish the truth of their conclusions or solve another owner's problem.

Science still owns scientific claims. Case systems own evidence/custody. Infrastructure systems own service state. Credentials own formal authorization where applicable.

## 18. BattleSpec admission boundary

An NPC enters AutoPTU only when an explicit reviewed combat contract includes that actor as a combatant.

The following facts are insufficient by themselves:

- walking beside the player in Minecraft;
- being part of the same journey;
- being a friend;
- being a mentor;
- being armed or owning Pokémon;
- having fought previously;
- being endangered;
- being visible when hostilities begin.

Ouros decides the combatant set before handoff. Cobblemon/Minecraft BattleState, entity proximity or follower logic never decides this.

## 19. Full companion-protection pattern

A mechanically rich companion battle may eventually support:

- companion and player moving toward an extraction point;
- body positioning and Intercept;
- Push/Pull/Knockback affecting route safety;
- reactions protecting the companion;
- hazards or zones changing the safe path;
- objective-aware allied and hostile AI;
- timed withdrawal or reinforcement;
- authoritative playback of departure.

This exact pattern depends on capability families that are not all complete.

It must remain blocked until each required family is verified for the authored contract.

## 20. Reduced companion-protection pattern

A safe current reduction is:

1. Ouros establishes the companion's current episode, location and departure intent.
2. The NPC exits the tactical footprint before initiative, or remains a semantic noncombatant outside BattleSpec.
3. AutoPTU receives only explicit combatants and static legal geometry.
4. The battle resolves a narrow physical fact such as an approach or withdrawal corridor being cleared.
5. Ouros evaluates the companion's actual movement, reunion or departure using world/travel state after the battle.

A tactical victory must not automatically mean:

- the NPC survived an unmodeled event;
- the NPC reached a destination;
- the NPC remains with the player;
- the NPC changed relationship state;
- the NPC will return later.

## 21. Encounter contract — Companion Extraction Corridor

Narrative premise:

A temporary companion needs to leave a threatened site while hostile combatants control the immediate route.

Full intended version:

- explicit protect/extract objective;
- moving companion or allied actor;
- legal Intercept and displacement interactions;
- opponents choose between pressure, blocking and withdrawal denial;
- possible reaction windows around route protection;
- extraction state ends the encounter only through an authoritative contract.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if reaction/protection zones are used
- move-specific behavior — PARTIAL as used
- abilities — PARTIAL as used
- items — PARTIAL as used
- Trainer Features/perks — PARTIAL as used
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full version: BLOCKED.

Reduced version: READY.

The companion leaves BattleSpec before initiative. Use one static combat encounter whose reviewed output can be only `IMMEDIATE_WITHDRAWAL_ROUTE_CLEAR` or an equivalent narrow fact. Travel/World Agency then determine the NPC's subsequent location and episode state.

## 22. Encounter contract — Separated Expedition Reunion Perimeter

Narrative premise:

A temporary expedition group split for parallel work. The player reaches a planned rendezvous while hostile pressure affects the perimeter.

Full intended version:

- companion arrivals can occur during the encounter;
- arrival timing depends on world-state progress;
- multiple groups may hold different tactical priorities;
- player decisions can affect who safely reaches the rendezvous;
- aftermath updates expedition participation.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including forced movement/interception — PARTIAL if used
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for timed arrivals
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if dynamic perimeter pressure is used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for multi-objective arrival/holding behavior
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full version: BLOCKED.

Reduced version: READY.

Ouros resolves which actors actually reached the rendezvous before BattleSpec. The tactical roster is fixed. Semantic companions who are not explicit combatants remain outside the battle. A win may establish `IMMEDIATE_REUNION_PERIMETER_CLEAR`; it cannot invent who arrived.

## 23. Encounter contract — Mentor Withdrawal Chokepoint

Narrative premise:

A mentor or specialist decides their role in the current operation is complete and needs to withdraw through a contested chokepoint while the player remains behind.

Full intended version:

- authoritative withdrawal objective;
- Intercept can matter;
- reactions may protect or obstruct movement;
- hostile AI values the withdrawal objective;
- the mentor acts according to their own legal tactical policy rather than player puppet control.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if generalized reactions or zones are used
- move-specific behavior — PARTIAL as used
- abilities — PARTIAL as used
- items — PARTIAL as used
- Trainer Features/perks — PARTIAL as used
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full version: BLOCKED.

Reduced version: READY.

Ouros removes the mentor from the tactical scene before initiative and records the intended withdrawal separately. AutoPTU resolves only the remaining static fight. The result may clear the immediate approach; it never proves the mentor survived, reached the next settlement, retained mentorship status or will return.

## 24. Minecraft/Cobblemon representation

Minecraft may present companion state after Ouros has established it:

- NPC walking alongside the player on an approved route;
- NPC waiting at a camp or landmark;
- temporary camp equipment;
- role-specific animations;
- departure dialogue;
- a visible route split;
- later reunion at a causally valid location;
- changed clothing, equipment or workplace reflecting another owner system;
- post-battle presence after authoritative handoff.

Minecraft/Cobblemon must not infer:

- companion membership;
- willingness;
- relationship state;
- route completion;
- joining or leaving;
- battle participation;
- survival;
- reunion eligibility;
- mentor authority;
- tactical withdrawal.

An entity despawning is a rendering/runtime event unless Ouros separately records a departure. `DESPAWN != DEPARTURE` and `DESPAWN != DEATH`.

## 25. Provenance and canon promotion

Every authored recurring companion should record:

- first established identity;
- relationship references;
- world-agenda references;
- each participation episode;
- join/departure/reunion event provenance;
- role changes;
- information-transfer evidence where important;
- current availability derived from live state;
- canon status for proposed material.

Before promotion, verify:

- NPC fits established region and institutions;
- participation has a causal reason and scope;
- no relationship label was inferred improperly;
- no authority or progression reward was invented;
- reunion passes normal reach/knowledge/motive checks;
- tactical scenes declare exact engine dependencies;
- reduced contract exists when rich support is incomplete;
- Minecraft remains presentation/playback rather than authority.

## 26. Open canon and implementation questions

- Which recurring non-rival NPCs already exist in approved Ouros canon?
- Which regions routinely employ guides or expedition specialists?
- Are any formal guide credentials or institutions canon-approved?
- Which Caelo social or party practices, if any, should carry forward?
- Can a non-player Trainer ever be directly player-controlled in AutoPTU, and under what contract?
- What is the authoritative rule for allied Trainer/Pokémon participation when several Trainers share one side?
- How should temporary NPC inventory/cargo exchange be represented without duplicating Material Culture?
- Which information-transfer events should be automatic from direct observation and which require explicit conversation?
- How should a companion episode be surfaced in Minecraft UI without implying a permanent RPG party roster?
- What engine contracts will eventually support escort, protect and tactical withdrawal objectives?

## Conclusion

The useful unit is a bounded participation episode around a persistent actor. It lets the same person travel with the player, leave, live independently and later return under changed circumstances while every substantive authority remains in its existing owner.

That structure supports memorable companions without converting Ouros into a fixed party RPG and without making the Minecraft adapter duplicate missing PTU battle rules.