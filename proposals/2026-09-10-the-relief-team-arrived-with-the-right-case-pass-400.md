# The Relief Team Arrived With the Right Case — Pass 400

Status: PROPOSED / NON-CANON
Canon approval: REQUIRED before naming any region, institution, route, NPC, species, item, emergency, historic event or PTU/Caelo mechanic.

## Premise

A field team is scheduled to transfer a shared equipment case to another crew at a known meeting point. Before the handoff, an unrelated local emergency forces both sides to change route and time. The reschedule is legitimate and reaches the necessary actors. The successor authorization is used and the physical transfer occurs.

Hours later, another coordinator sees the old appointment record, knows the original team departed with the case, and concludes that the delivery probably failed. That conclusion is reasonable from incomplete information but can be wrong.

The investigation asks separate questions:

- which authorization was operational at the moment of transfer;
- which actor physically held the case before and after the handoff;
- which actors received the reschedule;
- which world obligation caused the route change;
- whether a later record refers to the original appointment, the successor appointment or the actual custody event.

No contradiction automatically implies theft, deception or negligence.

## Persistent-world value

This scenario gives routine logistics narrative weight without forcing combat. It also validates a critical world invariant: a rescheduled physical handoff that changes current holder must leave both custody history and holder-transition history.

A stale appointment remains historically real. It simply stops being operational authority after an accepted successor replaces it.

## Reduced playable version

The entire premise can run without AutoPTU.

Required world capabilities:

- semantic time;
- persistent NPC knowledge and explicit communication;
- schedules, obligations and replanning;
- `WorldResource` identity and current holder state;
- resource request/reservation state where applicable;
- handoff authorization plus reschedule lineage;
- `ResourceCustodyTransfer` history;
- `ResourceHolderTransition` history;
- travel and route changes;
- post-event investigation through records and testimony.

The emergency can resolve off-screen or between scenes. The player may reconstruct what happened, contact either crew, verify current custody or continue another objective.

## Rich encounter version

The rescheduled meeting point can sit near an active rescue, damaged path or wild-Pokémon pressure. The narrative objective remains delivery, rescue, escort, preservation of the case or safe withdrawal. Defeating every opponent is not required.

### Capability dependencies

Targeting / footprints / range / LoS: required if threats, protection or ranged interaction depend on exact geometry. Current evidence is VERIFIED only for previously audited scopes.

Base movement legality: required for ordinary tactical navigation. Current evidence is VERIFIED only for audited ordinary movement scopes.

Complete movement including push/pull/knockback/interception/forced movement: required for body interception, dragging, forced carrier displacement, knockback from the route or rescue reposition. Current evidence remains PARTIAL.

Core calculations: required for ordinary combat calculations. Current evidence is VERIFIED only for audited scopes.

Action economy / initiative: required for ordered tactical actions. Audited primitives exist, but the complete family remains PARTIAL.

Full turn / round lifecycle: required for timed rendezvous windows, delayed collapse, staged evacuation or round-bound emergency changes. PARTIAL.

Full stateful damage pipeline: required when damage consequences persist across the objective or affect the rescued actor/cargo state. PARTIAL.

Status lifecycle: required for complex persistent conditions. PARTIAL.

Terrain / weather / hazards / zones / reactions: required for unstable paths, visibility loss, flooding, environmental zones, reactive hazards or delayed environmental effects. MIXED / PARTIAL / BLOCKING by exact mechanic.

Move-specific behavior: individually gated.

Abilities: individually gated. Current AutoPTU-Java evidence for specific Ability hooks does not verify the family.

Items: individually gated. The field case remains a world resource unless an exact PTU Item implementation is separately verified.

Trainer Features / perks: individually gated.

AI legal-action infrastructure: VERIFIED only within existing audited ordinary scopes.

AI tactical policy: BLOCKING for rescue-first, protect-case, escort-carrier, transfer-object, abandon-cargo-to-save-person, objective-aware withdrawal and disengage-after-objective.

Minecraft / Cobblemon / Craftics adapter and playback: PARTIAL / BLOCKING for stable resource projection, pickup/handoff acknowledgement, emergency objective state and authoritative non-KO completion.

## AutoPTU-Java evidence at proposal time

Read-only head inspected: `16352837e09c9fe07e0d38f8942d1dec96c095bb`, merge #425.

The new field-presence store materially improves the narrow switch transition seam by explicitly removing the outgoing combatant from field presence and placing the replacement at the resolved destination. It does not prove complete movement, general forced movement, complete switching semantics, turn lifecycle, tactical objective policy or adapter playback.

AutoPTU Python remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its latest change is presentation-only.

## Canon questions

The following remain unresolved and must not be inferred from this proposal:

- which Ouros institution owns or administers shared field equipment;
- whether this exact equipment case exists;
- who can authorize a reschedule or emergency reassignment;
- what local emergency creates the route change;
- what location hosts the original and successor meetings;
- which Pokémon or environmental hazards are present;
- whether the incident later connects to a larger arc;
- which PTU/Caelo Skills, Edges, Features or Items apply.
