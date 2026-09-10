# The Leads Do Not Wait — Pass 413

Status: PROPOSED / NON-CANON
Date: 2026-09-10

## Premise

One field incident creates several attributed leads at the same time. They may concern a route condition, a missing resource, a wildlife disturbance, a delayed traveler, a damaged service point or another bounded world problem. The proposal does not establish which incident exists in canon and does not assume crime, sabotage or one hidden culprit.

The important pressure is time. Pursuing one lead consumes semantic time while other parts of the world continue to change.

## Existing-world binding

A future canonized version can bind naturally to `ouros.faction.marea_field_office`, because the existing institution already coordinates route observations, wildlife incidents, missing-person searches and practical assistance. Mara Veyra is already a field-report coordinator. These facts make the Field Office a possible coordination surface without assigning this proposed incident to Mara or changing her canon schedule.

The concept can also be reused outside Marea because its core loop depends on the global NPC/world-agent architecture rather than a local special case.

## Lead state

A lead is an attributed reason to investigate a place, person, record or world object. It is not a global quest truth flag.

Each lead should retain:

- source/provenance;
- who currently knows it;
- semantic time when it became available;
- destination or subject if known;
- access/permission prerequisites where applicable;
- current investigation status;
- observations actually produced by a visit;
- later communications carrying those observations.

A lead that nobody knows cannot be selected merely because the server knows it exists.

## Parallel agency

The player may pursue one lead while a persistent named NPC pursues another if that NPC actually receives the assignment, knows enough to act, has time, can travel there and has the required access.

An off-screen NPC does not generate a cinematic or invisible tactical battle. Existing world-level travel and investigation state resolve only the facts that belong to the persistent world. If structured mechanics become necessary, the action must stop at an explicit AutoPTU handoff.

If no one pursues a lead, no observation is fabricated later to fill the gap.

## Time-sensitive consequences

A lead may remain useful, become stale, produce a different observation after conditions change, be resolved by another actor, or require a new visit after a site revision. Exact transformations must come from authored/world-system transitions rather than arbitrary timeout failure.

This allows several valid histories from the same starting incident:

- the player returns early with enough evidence to support a safe next step;
- another agent returns with an independent observation;
- two reports conflict because they describe different semantic windows;
- one lead becomes inaccessible before anyone reaches it;
- an initially weak clue becomes important only after a later communication connects it to another record.

No branch automatically creates omniscient knowledge of what happened on every unvisited lead.

## Return-and-review loop

A coordination point can act as the convergence surface. Participants compare evidence they actually possess, decide whether another sortie is justified, communicate missing context and update obligations.

Returning before every lead is exhausted can be a rational success state. The world can value sufficient evidence, safety, resource conservation and timely reporting rather than requiring map clearing.

## Reduced implementation

The reduced version requires no AutoPTU encounter.

It can run through current global systems for semantic time, schedules, obligations, travel, permissions, private knowledge, durable memory, explicit communication, evidence provenance, site revisions and event-driven replanning.

Environmental pressure is represented through authoritative world revisions between observations. Minecraft may display the current site state and authored inspectables, but it does not decide hidden causes or PTU checks.

Narrative premise preserved: simultaneous leads compete for attention while the world continues moving.

## Full encounter version

A later mechanically rich sortie may place one lead behind immediate tactical pressure. Example objectives could include obtaining an observation, retrieving one tracked object, protecting an observer, escorting a traveler to an exit or withdrawing after evidence is secured.

Combat elimination is not automatically the victory condition.

The full version must bind every requested interaction to verified AutoPTU capabilities. If a capability remains partial or blocking, the reduced investigative version remains valid instead of duplicating the missing rule in Minecraft.

## Engine capability dependencies

Targeting / footprints / range / LoS: VERIFIED only in previously audited scopes. Required if tactical observation, protection or attacks use spatial targeting.

Base movement legality: VERIFIED only in audited scopes. Ordinary tactical path/Shift legality can use only those proven paths.

Complete movement including push / pull / knockback / interception / forced movement: PARTIAL. Any rescue reposition, interception, dragging, forced retreat or environmental displacement depends on this family explicitly.

Core calculations: VERIFIED only in audited scopes. No new calculation is inferred by this proposal.

Action economy / initiative: PARTIAL. Multi-step interact-and-withdraw objectives or initiative-sensitive extraction require the exact contracts.

Full turn / round lifecycle: PARTIAL. Timed observation windows, escalating pursuit phases, delayed closure or round-bound extraction depend on full lifecycle support.

Full stateful damage pipeline: PARTIAL. Persistent tactical damage/injury consequences cannot be authored from presentation state.

Status lifecycle: PARTIAL. Complex or delayed conditions remain unavailable unless their lifecycle is verified.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING by mechanic. Moving debris, flood pressure, reactive terrain, weather phases, visibility changes or triggered zones need exact support.

Move-specific behavior: GATED PER MOVE. A Move cannot solve a lead obstacle merely because its fiction seems appropriate.

Abilities: PARTIAL / GATED PER ABILITY. Current Ball Fetch/switch approach evidence does not establish the family.

Items: GATED INDIVIDUALLY. Retrieval targets can be narrative WorldResources without granting unsupported PTU Item effects.

Trainer Features / perks: GATED INDIVIDUALLY. Observation, interception or command interrupts require exact verification.

AI legal-action infrastructure: VERIFIED only for ordinary audited scopes. Investigate, retrieve, escort, protect, interact, extract and specialized withdrawal actions require their own admission if represented tactically.

AI tactical policy: BLOCKING for evidence-first, protect-observer, escort-first, extraction, conserve-resource, objective-aware withdrawal and disengage-after-objective policy unless a verified policy contract exists.

Minecraft / Cobblemon / Craftics adapter / playback: PARTIAL / BLOCKING for authoritative tactical objective state, non-KO completion, specialized interactables and in-flight battle recovery. It may present the reduced investigation without inventing those mechanics.

## Long-term arc use

Repeated moving-lead incidents can develop institutional competence and relationships without using one global reputation meter. A player may become trusted because specific NPCs remember timely reports, careful evidence handling, abandoned obligations or unnecessary risk. Those consequences should flow through existing relationship, knowledge and provenance systems.

A region-wide arc can also let apparently unrelated field calls converge only after enough independent evidence accumulates. Convergence must emerge from recorded claims and world state rather than retroactively making every earlier irregularity part of one conspiracy.

## Canon questions left open

No incident, culprit, route revision, missing person, damaged structure, faction dispute or reward is canonized here.

A future content packet must decide the initiating event, exact existing IDs involved, which lead transformations are authoritative world changes, what evidence survives each window and whether any branch ever needs AutoPTU.
