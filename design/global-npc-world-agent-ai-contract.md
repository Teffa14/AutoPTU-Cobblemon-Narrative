# Global NPC / World-Agent AI Contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-05
Scope: ALL persistent and recurring Ouros NPCs, independent of country, region, settlement or faction.

## Purpose

Ouros needs one world-agent architecture for NPCs everywhere.

Marea, Sendero, Puerto Bruma and any later location are content bindings and regression sites. They are not allowed to define the global NPC decision model.

The global NPC layer owns world-level intent selection. It does not duplicate AutoPTU tactical AI.

```text
persistent NPC state
+ NPC knowledge and memory
+ goals and needs
+ obligations and schedules
+ relationships and institutional roles
+ permissions and resources
+ current world context the NPC can actually know
= candidate world intents
-> deterministic world-intent selection
-> overworld action OR explicit AutoPTU handoff
```

## 1. Global invariant

Every persistent/recurring NPC may use the same core agent schema and planner regardless of region.

Region-specific code may provide content, observations, jobs, schedules, relationships, permissions, routes and goals. It may not fork the meaning of NPC memory, knowledge, intent selection or tactical handoff.

`LOCAL_CONTENT != NPC_AI_ARCHITECTURE`

A core NPC-AI module must not import or special-case Marea, Sendero or any other authored location.

## 2. Persistent agent state

A persistent NPC agent may contain:

- `agent_id`;
- identity/profile reference;
- current world-agent mode;
- current semantic location and travel state;
- needs and maintenance pressures;
- long-term and short-term goals;
- scheduled commitments;
- contractual/professional obligations;
- relationships and faction/institution references;
- permissions, jurisdiction and delegated authority references;
- private knowledge/claims with provenance;
- memory references;
- risk tolerance and other authored decision traits;
- resource/inventory references owned by the appropriate subsystem;
- companion/party Pokémon references;
- active dialogue/interaction locks;
- active AutoPTU binding when structured mechanics own resolution.

The NPC's Minecraft entity UUID is never the persistent identity.

## 3. Agent modes

Initial global modes:

- `OFFSCREEN_NAMED` — persistent NPC exists and plans without a loaded Minecraft entity;
- `LOCAL_DORMANT` — local/present but not currently running high-frequency behaviour;
- `LOCAL_ACTIVE` — local world behaviour can be selected/projected;
- `CONVERSATION_LOCKED` — another interaction currently owns immediate behaviour;
- `AUTOPTU_BOUND` — structured mechanics own the conflict/action sequence;
- `SUSPENDED` — planner intentionally disabled by a higher-level world-state reason.

Mode changes are explicit state transitions. Chunk load/unload alone does not create or delete the NPC.

## 4. Knowledge boundary

NPC AI is non-omniscient.

The planner may consume only information available to that NPC through:

- direct observation;
- remembered observation;
- communication from another actor;
- accessible institutional records;
- public/local facts actually available to the NPC;
- explicit authored starting knowledge;
- inferences already recorded in the NPC knowledge system.

It may not read hidden ecology truth, hidden quest truth, another NPC's private memory, hidden player state or the global simulation ledger merely because Ouros knows those facts.

`WORLD_TRUTH != NPC_KNOWLEDGE`

A new message or observation may change an NPC decision without changing world truth.

## 5. World intents

The global planner can rank intents such as:

- work;
- travel;
- wait;
- rest/sleep/eat;
- observe;
- investigate;
- communicate/report;
- trade;
- maintain/repair;
- train;
- patrol;
- socialize;
- negotiate;
- assist;
- escort;
- seek a resource;
- respond to an emergency;
- avoid;
- flee;
- confront;
- pursue;
- request structured resolution.

This list is extensible. Intents are world-level purposes, not PTU Actions.

## 6. Decision inputs

The initial deterministic planner may evaluate:

- base goal priority;
- urgency;
- obligation/commitment strength;
- risk versus the NPC's risk tolerance;
- travel/resource cost;
- relationship weight;
- required knowledge;
- required permission;
- whether local Minecraft projection is required;
- whether structured mechanics are required.

Exact weights are Ouros world-AI policy and must be versioned/tested. They are not PTU rules.

Stable tie-breaking is required so identical state replays produce identical decisions.

## 7. Off-screen simulation

A named NPC does not need a Minecraft entity to exist or decide.

Off-screen NPCs may perform low-frequency/event-driven world planning for actions whose outcome does not depend on unresolved local geometry or tactical mechanics, for example:

- travel planning;
- scheduled work progression;
- communication;
- reporting;
- waiting/resting;
- institutional/relationship state transitions;
- other explicitly modeled world-level actions.

A local animation, gesture, collision-sensitive interaction or other presentation-only action can require local projection and be ineligible while off-screen.

Generic crowds do not need full persistent agents. The project may represent non-persistent crowds statistically/aggregately and promote individuals only when persistence is required.

## 8. Ecology integration

Ecology is a global input subsystem, not the owner of NPC AI.

Ecology may publish observations, evidence, resource pressure, hazards-as-world-facts, animal activity and world events. An NPC reacts only if that information enters their knowledge/context through a legal channel.

The same NPC architecture must also operate for goals unrelated to ecology: work, travel, social relationships, commerce, training, rivalry, faction obligations, exploration, investigations, logistics and emergencies.

Marea ecology fixtures can test this integration. They do not define it.

## 9. AutoPTU boundary

World-agent AI and AutoPTU tactical AI are separate systems.

The Ouros NPC planner may decide that an NPC intends to confront, defend, escape, pursue or otherwise enter a structured interaction.

If the selected intent requires PTU mechanics, the world planner emits:

`REQUEST_AUTOPTU`

It does not choose squares, legal Moves, damage, statuses, reactions, initiative order or tactical target legality.

When an NPC is `AUTOPTU_BOUND`, the world planner holds and does not compete with the tactical engine. After semantic results return, Ouros releases the binding and resumes world planning.

`WORLD_NPC_AI != AUTOPTU_TACTICAL_AI`

The permanent engine capability category `AI tactical policy` refers to tactical policy inside structured AutoPTU resolution. It must not be used to block ordinary off-screen/world-agent choices that do not require tactical adjudication.

## 10. Minecraft/Cobblemon boundary

Minecraft/Cobblemon projects the chosen local behaviour where possible.

It does not decide persistent NPC identity, knowledge, goals, relationships, permissions, risk policy or tactical outcomes.

A Minecraft entity can disappear while the agent continues off-screen.

`MINECRAFT_ENTITY != NPC_AGENT`

## 11. Dialogue boundary

Future generative or authored dialogue must be conditioned by the same agent state.

Dialogue may express:

- beliefs the NPC has;
- uncertainty the NPC has;
- relationships;
- goals and current intent;
- remembered experiences;
- institutional/faction information the NPC can access.

Dialogue must not author new world truth simply because a language model generated it.

## 12. Scaling tiers

Recommended execution tiers:

1. aggregate population/crowd simulation for non-persistent background actors;
2. low-frequency/event-driven planning for off-screen named NPCs;
3. higher-frequency local planning for nearby persistent NPCs;
4. explicit interaction/dialogue ownership when engaged by the player;
5. explicit AutoPTU ownership during structured tactical resolution.

Promotion between tiers must preserve identity and durable state.

## 13. Region-neutral validation requirements

A global NPC-AI implementation is not accepted if it only works in one authored area.

Minimum regression expectations:

- same planner produces valid decisions in at least two unrelated fixture regions;
- core code contains no special case for Marea/Sendero or another authored location;
- hidden world truth cannot trigger an NPC intent without knowledge provenance;
- communicated information can change an NPC decision without changing world truth;
- obligations and emergencies can compete deterministically;
- risk tolerance can produce different choices from the same evidence;
- off-screen planning works without Minecraft projection;
- local-only intents are rejected off-screen;
- structured conflict emits AutoPTU handoff rather than resolving tactics;
- restart/replay with identical state is deterministic.

## 14. Current implementation seam

Initial executable slice:

- `tools/global_npc_ai.py`
- `implementation/global-npc-ai-agent-fixture-v1.json`
- `tests/test_global_npc_ai.py`

This is a foundation, not the complete NPC simulation.

The next implementation layers should add, in order:

1. durable goals/needs and schedule state;
2. relationship/faction/institution input adapters;
3. world travel planning over the global route graph;
4. memory/claim confidence and forgetting/revision policies;
5. resource/inventory-aware intents;
6. dialogue/context projection;
7. local Minecraft behaviour adapter;
8. NPC-to-NPC communication and social propagation;
9. escalation/handoff integration with battle-subject bindings;
10. scalable tick/event scheduling for thousands of named agents.

No local NPC fixture may replace these global layers with region-specific logic.
