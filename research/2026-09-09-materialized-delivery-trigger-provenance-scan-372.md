# Materialized delivery and replan provenance scan — Pass 372

Status: RESEARCH / NON-CANON
Date: 2026-09-09
Canon effect: NONE

Repository inspection completed before writing. The current world checkpoint V14 already preserves notice obligations, their real communication envelopes, transport status, managed-agent state, private evidence ledgers, the replan queue and the coordinator materialized-delivery idempotency set. Pass 287 materializes a successful private delivery into receiver knowledge and schedules a `KNOWLEDGE_DELIVERED` replan trigger.

The remaining recovery gap is provenance after the replan trigger has been consumed. `NpcReplanQueue` preserves the full trigger while pending, but after processing it retains only the completed trigger ID. The coordinator separately preserves only the materialized delivery event ID. Therefore a restart can preserve both facts while lacking durable structured evidence that proves which receiver, delivery event, materialized claim and replan trigger belonged to the same causal transition.

This pass does not alter PTU rules, Caelo setting facts or established Ouros canon.

## New external source 1 — HowlOps incident lifecycle

Source: https://howlops.com/docs/concepts/incident-response
Inspected: 2026-09-09.

Public documentation describes one incident timeline shared across several interfaces. Acknowledgement, assignment and later actions enter a single server-side lifecycle rather than becoming disconnected parallel records.

Reusable Ouros structure: world-agent communication consequences should retain one durable causal timeline across transport, receiver materialization, replanning and later action. A delivery receipt, a completed replan trigger and a changed route should remain cross-referenceable after restart instead of being inferred from final state.

No incident-management product behavior, UI, terminology or implementation is imported as canon.

## New external source 2 — PTU Night Rangers: Hollow Underdeep

Source: https://startplaying.games/adventure/cmtrrpyqw00d7jl04r0mm82kx
Inspected: 2026-09-09.

Repository search found no previous processing of `Hollow Underdeep` by name. The public PTU listing describes an expedition through an underground region where the party reconnects separated communities, traverses old routes and carries a concrete delivery responsibility.

Reusable structure: a courier or expedition objective can remain meaningful across a long route, and successful delivery can create a later obligation to verify that the receiving side incorporated the information or cargo into its own plan.

Ouros transformation: use route-separated institutions, couriers and field teams whose knowledge and decisions remain individually persistent. No Night Rangers, Bellow, eggs, setting history, encounter text or homebrew mechanics are imported.

## New external source 3 — Pokémon Nova

Source: https://pokemonnova.com/
Inspected: 2026-09-09.

The public project presents open exploration, puzzles, secrets, rank progression and a long-form mystery across multiple locations. Repository search found prior references to Pokémon Terra Nova and Pokémon Supernova, but not this project as a processed source.

Reusable structure: environmental discoveries can unlock interpretation progressively. A player may encounter a consequence first, then reconstruct which prior message, decision or missed action caused it.

Ouros transformation: place the visible consequence in the world before exposing the full provenance trail. The quest can begin with a team on the wrong route, a missed observation window or a duplicated field task, then let the player trace transport, receipt and decision history backward. No Ultra Megalopolis plot, Necrozma story, Rank Leaders, locations or custom content are imported.

## PTU / Caelo cross-check

Project authority remains unchanged: PTU Core/Pokédex and indexed Caelo material govern mechanics and approved regional facts where applicable. No source inspected here creates a PTU combat rule or establishes a Caelo location, institution or technology.

World-agent delivery, evidence materialization and replanning are Ouros simulation semantics. They must not grant Trainer Features, Items, Abilities, movement options or combat reactions that are absent from authoritative PTU/Caelo evidence.

## Read-only engine cross-check

AutoPTU-Java head inspected: `c5713b41c99a1b969c7d934fc38d35acd0295d6a`, merge #412. The change registers the already parity-gated Intimidate round-start effect in the generic round-start Ability registry. This strengthens the exact Intimidate runtime path. It does not verify the Ability family, all round-start effects or all reactions.

AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change remains presentation-only and contributes no new rules evidence.

## Durable causal pattern proposed for later implementation

A materialized delivery receipt should be able to preserve at least:

- delivery event ID;
- receiver actor ID;
- delivered claim/evidence reference;
- provenance root;
- materialization semantic minute;
- wake result;
- replan trigger ID when one was created.

A consumed replan should separately preserve enough trigger provenance to prove:

- trigger ID;
- agent ID;
- reason;
- source delivery/event reference;
- due minute;
- processed minute or batch identity.

The essential invariant is:

`DELIVERED -> MATERIALIZED_AS_EVIDENCE -> REPLAN_TRIGGER_CREATED -> REPLAN_TRIGGER_CONSUMED`

Each arrow needs evidence. A later route change or agenda decision must never be used to reconstruct a missing earlier arrow.

## Capability implications

Reduced investigation and communication version has no AutoPTU dependency.

Mechanically rich interception version remains gated as follows: targeting/footprints/range/LoS VERIFIED within ordinary audited scope; base movement legality VERIFIED; complete movement PARTIAL; core calculations VERIFIED within audited deterministic scope; action economy/initiative VERIFIED for audited primitives; full turn/round lifecycle PARTIAL; full stateful damage pipeline PARTIAL; status lifecycle PARTIAL; terrain/weather/hazards/zones/reactions MIXED/PARTIAL/BLOCKING by exact mechanism; move-specific behavior, Abilities, Items and Trainer Features individually gated; AI legal-action infrastructure VERIFIED for ordinary audited actions; AI tactical policy BLOCKING for intercept-to-inform, escort, preserve-cargo, reroute and disengage-after-objective; Minecraft/Cobblemon/Craftics PARTIAL/BLOCKING for authoritative objective acknowledgement and end-to-end playback.

## Open questions

1. Whether materialization receipts belong directly to the coordinator or to a dedicated append-only world-event provenance owner.
2. Whether completed replan triggers should retain structured rows rather than only IDs.
3. Whether acknowledgement should remain a communication event semantic type or become a first-class owner.
4. Which approved Ouros institutions and routes should first bind this pattern once the persistence seam exists.