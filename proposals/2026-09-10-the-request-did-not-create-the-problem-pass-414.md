# The Request Did Not Create the Problem — Pass 414

Status: PROPOSED / NON-CANON
Date: 2026-09-10

## Premise

A practical problem already exists before anyone offers the player a quest.

A route fixture is damaged, a delivery is overdue, an observation instrument is missing from its expected holder, a traveler has not reached a scheduled stop, a wild-population disturbance has been reported, or another bounded world condition has changed. The proposal does not choose one of these as canon.

One or more NPCs may notice the condition. Another person may learn about it later through ordinary communication. A request for help is a response to that knowledge. Accepting the request records the player's involvement; it does not create the underlying condition.

`WORLD CONDITION -> OBSERVATION -> COMMUNICATION -> REQUEST -> COMMITMENT`

The chain can branch and some links can be absent.

## Existing-world binding

A future Marea implementation can reuse existing owners instead of creating a new quest island.

Marea Field Office already coordinates route observations, wildlife incidents, missing-person searches and practical assistance. Loma Clara Producers Cooperative already handles shared deliveries and storage. Tideglass Archive already preserves records and attributed claims. Estación Mirador already produces route, weather and ecological observations. These are possible surfaces only; this proposal does not assign a new incident to any one institution.

Named residents retain their own schedules and goals. An NPC does not wait motionless because the player has not accepted a journal entry.

## Separate persistent facts

A robust implementation should distinguish at least these facts:

- `condition_ref`: what world state changed and when;
- `observation_ref`: what a specific actor actually observed;
- `knowledge/provenance`: who knows which claim and from what source;
- `request_ref`: who asked whom to do what, when, and on what evidence;
- `commitment_ref`: whether the recipient accepted, declined or left the request unanswered;
- `resolution_ref`: what later world transition actually changed the condition.

A request can become obsolete while its historical existence remains true. A world condition can be resolved even if the player never accepted a quest.

## Player choices

The player can encounter several histories without hidden omniscient correction.

The player may discover the condition before anyone asks for help. They may accept immediately. They may decline. They may postpone and return later. Another persistent NPC may accept the same or a related obligation if that NPC knows about it and has the time, permissions and route access to act.

A delayed return can therefore find:

- the same unresolved condition;
- a partially changed condition;
- another actor already investigating it;
- a safe temporary workaround;
- a completed world-level resolution with provenance;
- a new request because the original one no longer matches the current facts.

No branch is selected merely to punish delay. State changes must come from authored or simulated world transitions.

## Independent NPC arcs

The requesting NPC does not become a quest marker with no other life.

They may continue ordinary work, communicate with other relevant actors, replan after receiving new evidence, withdraw the request, delegate it, or decide that the issue no longer justifies intervention. These actions must follow the global NPC agenda, travel, knowledge, permissions and communication systems.

This also allows later reconvergence. An NPC can leave on unrelated work and return with information that changes how both parties understand the original condition, provided the world simulation actually supported that information path.

## Reduced implementation

The reduced form requires no new AutoPTU mechanics.

It uses:

- semantic time;
- persistent world facts/site revisions;
- NPC goals, schedules and obligations;
- private knowledge and provenance;
- communication queues;
- travel and permissions;
- event-triggered replanning;
- explicit request/commitment history;
- ordinary world-level resolution where no structured mechanic is required.

If an off-screen action crosses into structured combat or another PTU-governed resolution, the world agent stops at the normal AutoPTU handoff rather than simulating an invisible battle.

## Mechanically rich version

A future incident can culminate in rescue, escort, retrieval, inspection under pressure, protected withdrawal or another non-KO objective.

That richer form preserves the same narrative premise: the problem predates the quest offer and can continue changing independently of the player's journal.

### Capability dependencies

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Any dragging, interception, forced slide, knockback or rescue reposition depends on this family.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL.

Full turn/round lifecycle: PARTIAL. Timed protection, staged extraction, delayed collapse or objective windows depend on it.

Full stateful damage pipeline: PARTIAL. Persistent consequences from tactical damage require this family.

Status lifecycle: PARTIAL. Complex or delayed statuses remain gated.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism. Reactive debris, flooding, visibility changes, weather phases and triggered zones need exact verified behavior.

Move-specific behavior: individually gated.

Abilities: PARTIAL / individually gated.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for audited ordinary scopes. Rescue, escort, retrieve, inspect, carry and specialized interaction need explicit legal-action admission.

AI tactical policy: BLOCKING for rescue-first, escort-first, preserve-evidence, objective-aware withdrawal and disengage-after-objective unless separately verified.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for authoritative objective state, specialized interactables, non-KO completion and in-flight tactical recovery.

## Minecraft presentation boundary

Minecraft may show the changed site, the requesting person, a notice, a missing object location, repair work or other authored projection.

Loading the chunk cannot create the incident. Removing an entity cannot resolve it. A visual animation cannot prove a PTU outcome. The quest UI may present known objectives and commitment state, but it cannot own the underlying world truth.

## Narrative consequences

This structure turns refusal and delay into ordinary world history rather than binary quest failure. It also gives NPC agency observable consequences without making them omniscient.

The player can learn that someone else solved a problem, that a request was withdrawn for a good reason, that two people acted from different information, or that the situation worsened because nobody with sufficient access was available. Those outcomes become useful relationship and faction material because they have explicit provenance.

## Canon questions before promotion

A future canon binding must decide the exact incident, owner, affected WorldResource or site, initial observer, request policy, eligible alternate actors, possible world-level transitions and any administrative consequences.

No such choice is made here.
