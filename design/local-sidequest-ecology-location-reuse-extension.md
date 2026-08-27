# Local Sidequest Ecology & Location Reuse Extension

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already knows how to generate missions from world state. The missing problem is orchestration when one neighborhood, settlement or route contains many simultaneously valid hooks.

This extension controls density, selection, merging, revisits and repetition. It sits above existing systems and never replaces them.

Mission Grammar still owns mission shape. World Agency still owns actors and causal state. Public Notices still owns public projection. Downtime still owns quiet voluntary activity. Every domain-specific system keeps authority over its own facts.

The goal is to make a small place feel deep rather than noisy.

## 1. Core rule

A valid hook does not automatically become an active quest.

The system must distinguish:

- a world condition exists;
- someone could plausibly care about it;
- the player could discover it;
- it deserves foreground attention now;
- it should become a formal mission;
- it should remain ambient;
- it should wait;
- it should merge with another thread;
- it should retire.

This separation is mandatory.

## 2. Local content cell

A `local_content_cell` is an orchestration view over existing places and actors. It does not create a new geography object.

```yaml
local_content_cell:
  cell_id: null
  location_refs: []
  resident_actor_refs: []
  service_refs: []
  institution_refs: []
  route_refs: []
  recurring_pokemon_refs: []
  active_world_state_refs: []
  foreground_thread_refs: []
  ambient_opportunity_refs: []
  latent_hook_refs: []
  recent_scene_refs: []
  last_evaluated_at: null
```

A cell may represent:

- one street;
- a public square plus adjacent shops;
- a village and immediate outskirts;
- a campus wing;
- a route junction;
- a waterfront block;
- a research station and nearby field site.

The cell exists only to decide what becomes legible to players.

## 3. Hook candidate

```yaml
hook_candidate:
  hook_id: null
  source_system: null
  source_state_refs: []
  causal_actor_refs: []
  affected_actor_refs: []
  location_refs: []
  activity_tags: []
  urgency: low|medium|high|critical
  discoverability: direct|public|ambient|conditional|hidden
  time_window: null
  player_commitment_refs: []
  related_thread_refs: []
  mechanical_risk_tags: []
  status: candidate
```

A candidate must come from real state.

Examples:

- a storefront has a recurring supplier problem;
- a resident's routine changed;
- a repaired path reopened but a public notice is stale;
- a researcher has enough observations to request a field check;
- a volunteer call has more helpers than qualified roles;
- a recurring wild Pokémon begins using a different local path;
- a library copy has returned with a relevant insert;
- an old puzzle mechanism has changed after maintenance.

## 4. Foreground thread

A `foreground_thread` is optional content that the game deliberately surfaces as worth attention now.

```yaml
foreground_thread:
  thread_id: null
  source_hook_refs: []
  current_premise: null
  location_refs: []
  participant_refs: []
  activity_profile: []
  surfaced_via: []
  opened_at: null
  last_meaningful_change_at: null
  revisit_delta_refs: []
  current_state: available|accepted|active|waiting|paused|resolved|failed_forward|retired
  world_state_writeback_refs: []
  mechanics_review_ref: null
```

A thread may contain more than one hook if they share a causal root.

Example:

A shop closes early, a courier delivery is delayed and a repair crew is waiting for a component.

If all three facts trace to the same disrupted transport leg, prefer one coherent local thread with several stakeholders over three unrelated quest markers.

## 5. Ambient opportunity

Some world facts deserve interaction without becoming formal missions.

```yaml
ambient_opportunity:
  opportunity_id: null
  source_state_refs: []
  location_refs: []
  actor_refs: []
  available_interactions: []
  persistence_window: null
  can_escalate: false
  escalation_conditions: []
```

Examples:

- an NPC wants to compare field notes;
- a shop has a new display after a prior event;
- a familiar Pokémon is resting somewhere unusual;
- a local board has a corrected notice;
- a resident is practicing a hobby in a public space;
- an old construction detour has become a shortcut.

These can deepen the world with no quest log entry.

## 6. Latent hook

A `latent_hook` is valid but intentionally not surfaced.

Reasons may include:

- prerequisite information is missing;
- another thread already owns the same causal problem;
- local saturation is too high;
- the affected actor has not yet observed the issue;
- the player has no plausible access path;
- the condition is still too routine to justify foreground play;
- the exact mechanic required is not ready and no acceptable reduced version exists;
- the hook would reveal hidden state unfairly;
- the timing window has not opened.

Latent does not mean nonexistent.

World Pulse may continue changing its source state.

## 7. Local saturation budget

The system should bound simultaneous foreground content.

```yaml
local_saturation_budget:
  cell_id: null
  max_foreground_threads: null
  max_high_urgency_threads: null
  preferred_activity_mix: []
  current_foreground_count: 0
  suppressed_hook_refs: []
  rationale_refs: []
```

Exact numbers are implementation tuning, not canon.

Selection should consider:

- urgency;
- existing player promises;
- unresolved consequences;
- whether the player recently interacted with the same actors/place;
- activity novelty;
- causal overlap with other hooks;
- whether the state change is legible in Minecraft;
- whether a meaningful choice exists;
- whether the opportunity can wait without contradiction.

The budget prevents a single district from exposing every valid condition at once.

## 8. Hook merge

```yaml
hook_merge:
  merge_id: null
  source_hook_refs: []
  shared_cause_refs: []
  shared_location_refs: []
  shared_actor_refs: []
  merged_thread_ref: null
  preserved_independent_outputs: []
```

Merge when multiple hooks are different views of one problem.

Do not merge merely because they occur nearby.

Good merge:

A storm damaged a footbridge, delayed deliveries and moved pedestrian traffic past a nesting site.

Possible single thread:

Inspect the route, understand the ecological conflict and coordinate reopening.

Bad merge:

A missing library book and a restaurant staffing shortage happen on the same street but have no causal relationship.

## 9. Revisit delta

A recurring place or actor should not reappear as unchanged content.

```yaml
revisit_delta:
  delta_id: null
  thread_id: null
  since_event_ref: null
  changed_world_state_refs: []
  changed_actor_state_refs: []
  changed_location_state_refs: []
  new_information_refs: []
  changed_access_refs: []
  changed_mechanical_contract_refs: []
  materially_different: false
```

A revisit becomes foreground-worthy when the delta creates a new decision.

Examples:

- the former blocker is gone but a new stakeholder objects;
- the same Pokémon group now uses another route;
- the shop reopened with limited service rather than full service;
- a witness corrected their statement;
- an old puzzle bypass now affects maintenance;
- a rival returns with legitimately changed public preparation.

## 10. Repeatability guard

```yaml
repeatability_guard:
  thread_id: null
  prior_encounter_refs: []
  prior_activity_signature: []
  current_activity_signature: []
  meaningful_delta_refs: []
  identical_replay_rejected: true
  replacement_options: []
```

The generator should reject exact repetition unless repetition itself is the authored point and the player knowingly chooses it.

If a prior optional battle failed, valid next states include:

- opponent left;
- another actor intervened;
- location access changed;
- preparation changed;
- negotiation became possible;
- the opportunity expired;
- a different route opened;
- the battle remains available but is summarized as an explicit player choice only if governing progression policy allows it;
- a new encounter replaces the old one because world state advanced.

Do not respawn an identical battle because the quest flag is still incomplete.

## 11. Activity diversity

Use Mission Grammar's activity blocks and recent experience vector.

A local cell should avoid making every visible thread use the same lane.

Possible mix:

- one investigation;
- one social/service thread;
- one exploration opportunity;
- one combat-capable thread;
- several ambient interactions.

This is a selection preference, not a quota.

Causality overrides variety when the world strongly demands one type of response.

## 12. Player commitment priority

Existing promises, accepted jobs and direct requests should usually outrank newly generated optional noise.

```yaml
commitment_priority:
  commitment_ref: null
  affected_thread_refs: []
  deadline_ref: null
  blocker_refs: []
  player_deferred: false
```

A new generic task must not crowd out a promise the player already made unless the player explicitly chooses to defer it or world state makes the promise impossible.

## 13. Quiet content compression

Many valid hooks should resolve as ambient continuity instead of scenes.

Compress when:

- outcome is routine and already authorized;
- no meaningful choice exists;
- no new participant or information appears;
- no scarce resource decision exists;
- no irreversible state changes;
- the player did not choose to focus on it;
- repetition would add no new information.

Example:

A courier route has returned to normal and three routine deliveries arrive.

Preferred:

Update shipment/storefront state and show visual evidence.

Avoid:

Three separate delivery quests.

## 14. Thread retirement

```yaml
thread_retirement:
  thread_id: null
  retired_at: null
  retirement_reason: resolved|expired|absorbed|superseded|no_longer_relevant|player_declined|world_changed
  final_state_refs: []
  chronicle_refs: []
  future_callback_refs: []
```

Retirement does not erase history.

A retired thread may later create a new hook if world state genuinely changes.

## 15. Declining and ignoring optional content

Optional content must tolerate nonparticipation.

If the player ignores a thread:

- the world may resolve it through other actors;
- it may remain unresolved;
- it may worsen only if causal state supports that;
- it may expire;
- it may transform;
- another faction may act;
- a service may adapt;
- nothing may happen.

Ignoring cannot automatically produce punishment merely to force engagement.

## 16. NPC instantiation budget

Narrative density should not require complete PTU builds for every local actor.

Local NPC tiers:

`AMBIENT`
- identity or role only when needed;
- schedule/location projection;
- no tactical stat block.

`PERSISTENT_SOCIAL`
- stable actor ID;
- knowledge, role, relationships, routines, commitments;
- no battle build unless needed.

`MECHANICALLY_RELEVANT`
- authoritative PTU/AutoPTU combatant data when the actor actually participates in battle or another rules-bearing subsystem.

A promotion between tiers must be explicit.

Cobblemon entity presence does not define the tier.

## 17. Location reuse contract

Every frequently used local location should support multiple layers of meaning over time.

```yaml
location_reuse_profile:
  location_ref: null
  baseline_functions: []
  prior_thread_refs: []
  persistent_changes: []
  current_users: []
  current_access_state: null
  ecological_state_refs: []
  institution_state_refs: []
  visual_delta_refs: []
  overuse_guard: null
```

A market lane may host:

- routine commerce;
- an event overlay;
- a delivery problem;
- a rumor scene;
- a public correction;
- an ecological conflict;
- a recurring rival encounter;
- a later memorial or historical callback.

The location remains itself throughout.

## 18. Overuse guard

A location can become narratively implausible if every important event happens there.

Suppress or redirect new foreground content when:

- recent major scenes repeatedly used the same exact spot;
- another plausible nearby location better fits the actors;
- the area is already occupied by an active event/crisis;
- the accumulated density would break ordinary-life baseline;
- the player has had no opportunity to see the location in a normal state.

Ouros should establish ordinary baselines between disruptions whenever possible.

## 19. Public surface policy

A foreground thread may be surfaced through:

- direct NPC approach;
- conversation;
- public board;
- sign/notice;
- message;
- observed event;
- rumor;
- institution desk;
- environmental evidence;
- recurring schedule deviation.

The surface must be owned by the correct subsystem.

A public notice never proves the underlying claim. A quest icon never creates a need.

## 20. World Pulse integration

World Pulse may create hook candidates.

It should not directly create foreground missions.

Proposed flow:

1. source system changes world state;
2. World Pulse records actor action/consequence;
3. valid hook candidates are derived;
4. local ecology evaluates saturation, overlap, timing and player commitments;
5. selected thread becomes foreground or ambient;
6. discovery surface is created by the relevant presentation system;
7. player interaction creates/updates mission state if needed.

## 21. Cobblemon reuse

Use as much safe Cobblemon/Minecraft functionality as possible for presentation:

- NPC and Pokémon overworld entities;
- species models/forms/textures;
- animations, cries, sounds and particles;
- signs, books, lecterns, containers and display blocks;
- map markers and UI surfaces;
- interaction callbacks;
- schedules and entity tracking where useful;
- client/server synchronization;
- networking;
- persistence hooks;
- world geometry and loaded-location observations.

Ouros remains authoritative for:

- whether a hook exists;
- who knows it;
- whether it is foreground/ambient/latent;
- which actors are narratively involved;
- thread history;
- state changes and consequences.

When battle begins:

`Ouros world/thread state -> explicit AutoPTU BattleSpec -> AutoPTU state/result -> adapter -> Cobblemon/Minecraft presentation`

Cobblemon battle participant selection, internal BattleState, HP, status, target legality, outcome or tactical AI cannot become authority.

## 22. Encounter implementation contract

Every mechanically rich foreground thread uses the permanent capability categories.

A sidequest selector must not hide missing mechanics by calling a concept “small”.

Even an optional local encounter may depend on:

- complete movement including interception;
- lifecycle;
- full damage;
- statuses;
- terrain/weather/hazards/zones/reactions;
- exact Moves/Abilities/Items/Trainer Features;
- tactical AI;
- adapter/playback.

The full/reduced pattern remains mandatory when the premise can survive simplification.

## 23. Example full/reduced encounter — Market-Lane Clear Route

Narrative premise:

A normal market lane becomes blocked after a local Pokémon group reacts to a temporary change in pedestrian traffic.

Full version:

- civilians withdraw through several exits;
- the party may need CLEAR_ROUTE or WITHDRAW rather than defeat-all;
- interception/forced displacement may matter in narrow geometry;
- stalls and protected fixtures affect space;
- wild AI may prefer territorial retreat;
- current local environmental state may matter if supported.

Dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle where roster requires it;
- terrain/weather/hazards/zones/reactions if environment becomes tactical;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

Reduced version:

Civilians leave first through world state. Market goods are outside battle authority. Ouros freezes a reviewed static arena. AutoPTU resolves only explicitly selected combatants. Route reopening is decided afterward by public-space/ecology state. No scripted knockback, escort bonus or destructible stall mechanics are invented in Minecraft.

## 24. Example full/reduced encounter — Revisit at the Footbridge

Narrative premise:

A previously solved repair thread returns because the footbridge is open again but altered pedestrian flow now intersects a recurring Pokémon route.

Full version:

- route usage changes during encounter;
- protected crossing zones;
- possible intercept/reaction behavior;
- territorial/withdrawal AI;
- environment-aware positions.

Reduced version:

The bridge state and pedestrian rerouting are resolved before battle. Noncombatants remain outside the grid. AutoPTU receives a static approved encounter nearby. The revisit remains narratively distinct because the cause and decision differ from the original repair thread.

## 25. Noncombat example — Three Problems, One Cause

A cafe closes early, a workshop waits on a component and a resident says the afternoon street is unusually quiet.

The system traces all three to one suspended transport service.

Instead of generating three missions:

- storefront remains LIMITED;
- maintenance order remains WAITING;
- public-space activity changes;
- one foreground investigation/travel-service thread is surfaced;
- the other facts become stakeholders and evidence.

No battle capability is required.

## 26. Acceptance tests

Future orchestration implementation should prove:

1. Ten valid hooks in one cell do not automatically create ten active quests.
2. Two hooks with one causal root can merge while preserving separate downstream outputs.
3. Two unrelated nearby hooks remain separate.
4. A player promise outranks new low-urgency procedural content.
5. An ambient interaction can remain discoverable without a quest-log entry.
6. A latent hook can change off-screen through World Pulse.
7. Identical failed combat cannot respawn without a meaningful delta unless explicitly authored.
8. A retired thread preserves Chronicle/history.
9. A location can be reused without erasing baseline functions.
10. An incidental NPC does not receive a full PTU build until rules-bearing participation requires it.
11. A Cobblemon entity spawning does not create a hook.
12. A Cobblemon battle object cannot choose participants or resolve the thread.
13. A reduced encounter remains valid when adapter, tactical AI and reactions are absent.

## 27. Canon boundary

This extension establishes no actual settlement, resident, institution, quest board, technology or sidequest as canon.

Exact tuning values for saturation budgets remain implementation decisions.

Any future concrete content still requires canon review for:

- location existence;
- actor identity;
- institution authority;
- public/private access;
- species ecology;
- technology;
- cultural norms;
- PTU/Caelo legality;
- AutoPTU support.

## 28. Design conclusion

Ouros should produce more continuity, not more markers.

The sidequest ecology is successful when a player can return to one familiar place and discover that several people, services, Pokémon and prior choices have changed in connected ways while most ordinary life continues around them.
