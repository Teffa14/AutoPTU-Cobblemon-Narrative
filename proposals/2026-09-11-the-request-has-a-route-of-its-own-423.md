# The Request Has a Route of Its Own — Pass 423

Status: PROPOSED / NON-CANON

This file proposes a reusable Ouros quest and world-event pattern. It does not establish a new incident, character relationship, duty, route condition, battle, faction rule or historical fact.

## Premise

A world agent can decide that another named person would be useful. That decision creates an intent owned by the requester. It does not teleport knowledge to the proposed helper and it does not reserve that person's time.

The request must travel.

The requested person can react only after receiving it. Their response depends on what they know at that moment, where they are, what obligations already exist, whether travel is possible, whether they have authority to help and whether a structured mechanic requires AutoPTU.

This supports a world where people coordinate without becoming a hive mind.

## Candidate Marea regression surface

Marea already has enough canon to test the pattern without creating new world facts.

Mara Veyra coordinates field reports, route checks, wildlife incidents and practical assistance from the Marea Field Office. Teo Lark maintains ordinary equipment and field instruments. Oren Vale handles care work. Nerea Sol owns longitudinal observation responsibilities. Lia Morn coordinates docks and unloading windows.

A future authored incident may therefore give Mara a legitimate reason to request one of them. The recipient still owns their decision. The proposal does not canonize any particular incident or request.

## Reduced version

The reduced form needs no AutoPTU battle.

A world event changes Mara's private knowledge. She replans and selects a `REQUEST_ASSISTANCE` intent toward one explicit person. The action intent is recorded durably. A message is then authored from that action and placed on an ordinary communication channel.

Until delivery, the target remains unchanged.

After delivery, the target may receive a `KNOWLEDGE_DELIVERED` wake-up through the existing global coordinator. Their planner can then accept, defer, reject, ask for clarification, recommend another person, or continue a higher-priority obligation.

Any acceptance should become the target's own durable action or commitment. The requester's ledger must never edit the target's schedule directly.

This version uses existing semantic-time, private-knowledge, communication, schedule, obligation, permission, travel and event-driven replanning architecture.

## Full encounter version

A richer authored episode can make the request itself part of field pressure.

Example structure: a first team reaches an existing site and learns that a second skill set or piece of equipment would materially improve the situation. A request is sent while the current team continues a bounded objective. The helper may arrive later, decline, or redirect support. The original group can still reach a narratively valid reduced resolution before the helper arrives.

Possible tactical objectives include protecting an observer, holding access long enough to retrieve evidence, escorting an injured or vulnerable actor, extracting after a bounded observation, or withdrawing once enough information has been secured.

The narrative premise does not require those tactical behaviors. If the needed engine families are incomplete, the same episode can resolve through the reduced version: the team exits safely, sends the request, and the world consequence continues through schedules, travel and later investigation.

## Encounter dependency contract

Targeting/footprints/range/LoS: VERIFIED only in audited scopes. Required for any full encounter whose protect, escort or extraction objective depends on actual spatial targeting.

Base movement legality: VERIFIED only in audited scopes. Required for ordinary tactical movement in the full version.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Required if the encounter uses dragging, interception, forced displacement, knockback or movement caused by hazards. The reduced version does not require it.

Core calculations: VERIFIED only in audited paths. Required when the full encounter resolves combat calculations.

Action economy/initiative: PARTIAL. AutoPTU-Java now has concrete parity evidence and a production mutation for replacement initiative insertion, but that bounded seam does not verify the category as a whole.

Full turn/round lifecycle: PARTIAL. Required for timed protection windows, staged evacuation or multi-round environmental progression.

Full stateful damage pipeline: PARTIAL. Required if damage, healing or injury-producing state must survive and matter beyond a bounded representative action.

Status lifecycle: PARTIAL. Required for encounters whose objective depends on complex or persistent status behavior.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact behavior. Required for unstable terrain, reactive debris, flooding, weather phases, triggered zones or reaction windows.

Move-specific behavior: individually gated. Any authored move-dependent objective must name and verify the exact behaviors it needs.

Abilities: PARTIAL and individually gated. Ability-triggered rescue, terrain, switching or reaction behavior cannot be assumed from representative implementations.

Items: individually gated. Equipment or consumables that affect tactical resolution require exact support.

Trainer Features/perks: individually gated. Narrative profession or class concepts never imply that an interrupt, command or Feature exists in AutoPTU.

AI legal-action infrastructure: VERIFIED only for audited ordinary actions. Specialized escort, protect, retrieve, carry, interact, brace, rescue or extract actions need explicit admission.

AI tactical policy: BLOCKING for specialized protect-carrier, rescue-first, escort-first, objective-aware withdrawal and disengage-after-objective policies.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING for authoritative tactical objective state, specialized non-KO completion and in-flight recovery. Minecraft may present the scene, but it must not invent the battle result or the helper's decision.

## Consequence patterns

A delivered request can arrive while the target is still free, after the target has departed, while another duty is in progress, or after the original problem has changed. Each branch preserves the same causal history.

A failed channel means the target did not receive the request through that event.

A queued message means only that a message is pending.

A local-projection message waiting for acknowledgement means delivery has not yet completed.

A successful receipt makes reconsideration possible. It does not equal acceptance.

A rejection or deferral should remain a legitimate authored outcome. The quest can adapt by finding another person, reducing scope, changing timing or accepting a partial result.

## Longer arc use

Repeated coordination episodes can build character arcs without scripted omniscience. One person may become known for reliably answering certain kinds of calls. Another may set clearer boundaries after being over-requested. Institutions may learn which channels, handoff practices or staffing patterns work under pressure.

Those reputational or relationship changes require their own provenance-backed world events. This proposal does not grant them automatically.

## Canon questions left open

No default communication channel is canonized for Marea requests.

No response-time expectation is canonized between the Field Office and any resident.

No resident gains a new duty merely because their existing role makes them a plausible candidate.

No assistance-request acceptance policy is canonized.

No tactical objective above becomes canon until a later content package chooses it and verifies its required engine capabilities.
