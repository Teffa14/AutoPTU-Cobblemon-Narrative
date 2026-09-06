# The Cut Relay Inquiry — Pass 303

Status: PROPOSED / NON-CANON
Date: 2026-09-06

## Narrative premise

A warning fails to reach a small travel corridor after a relay goes offline. The dispatcher attempted the message, so Pass 302 prevents the story from treating the missed warning as willful silence. The new question is what happened to the relay.

The first visit provides no guaranteed villain. The installation can show ordinary wear, storm damage, signs of deliberate interference, or evidence too ambiguous to resolve. Different NPCs may already have incompatible explanations because they saw different parts of the history.

## Investigation structure

The failure can be approached through several independent evidence routes rather than one mandatory clue. A maintenance worker has service history. A traveler saw who used the access trail. Physical inspection can reveal wear or deliberate alteration. Dispatch records establish when the relay stopped responding. A later statement may connect an actor to a deliberate act.

The important conclusions are staged. `The relay failed` comes first. `The relay was tampered with` is a stronger finding. `This person was linked to the tampering` is stronger again. `This person acted deliberately` requires its own evidence. Access, rivalry, faction membership or benefit from the outage never substitute for those steps.

An accident remains a valid resolution. Mixed evidence can remain contested. A saboteur may also exploit equipment that was already failing, which allows institutional negligence and deliberate interference to coexist without flattening the story into one cause.

## Consequences and arcs

If ordinary failure is corroborated, suspicion toward a worker or dispatcher can be challenged by evidence rather than author fiat. If tampering is proven without an actor, the corridor gains an unresolved security problem. If an actor is linked but intent remains unproven, factions can disagree about negligence, accident and sabotage. If intent is eventually attributable, relationships, permissions, patrol routes and future communication policy can change through their existing systems.

The repair itself can create later continuity. Restoring the relay changes which routes and warnings can function, while the investigation record remains available for future disputes.

## Reduced implementation version

This version needs no AutoPTU battle implementation.

The relay failure is represented by Pass 302 access/delivery evidence. NPCs gather authored world evidence through travel, conversations, records and simple interaction gates. Pass 303 produces causal findings from each investigator's actual ledger. Repair changes world connectivity through existing world-state authoring. Any confrontation can remain narrative or be deferred until a verified tactical handoff exists.

This preserves the premise: the missed warning becomes an evidence-driven inquiry whose outcome can be accident, ambiguity or sabotage.

## Intended mechanically rich version

The relay sits above a storm-damaged ravine. Access requires traversal while unstable debris and electrical/weather hazards change the safe approach. A stranded technician may need rescue before the installation can be inspected. If an opposing actor intervenes, the scene can escalate to AutoPTU while preserving the investigation state outside tactical authority.

Intended dependencies:

- targeting/footprints/range/LoS: VERIFIED within audited contracts, required if the scene becomes structured positioning/combat;
- base movement legality: VERIFIED within audited contracts, required for ordinary traversal;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL, required only for wind/debris forced displacement or interception rescue;
- core calculations: VERIFIED within audited contracts for ordinary deterministic calculations;
- action economy/initiative: VERIFIED within audited contracts for structured resolution;
- full turn/round lifecycle: PARTIAL, required for timed collapses, surges or phase changes;
- full stateful damage pipeline: PARTIAL, required for authoritative environmental damage;
- status lifecycle: PARTIAL, required for persistent mechanical conditions;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING, required for mechanically active storm, exposed cables, collapsing zones or reaction rescues;
- move-specific behavior: PARTIAL when authored Moves are used;
- abilities: PARTIAL when Abilities alter the scene;
- items: PARTIAL when Items mechanically alter resolution;
- Trainer Features/perks: PARTIAL when Trainer Features alter investigation or tactical resolution;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for general autonomous rescue/combat choice;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end for authoritative visible playback.

## Reduced tactical fallback

Keep the storm visually and narratively present but mechanically static. Represent the approach as connected safe/blocked traversal nodes using verified base movement. Remove wind knockback, reaction rescues, delayed collapse phases, persistent status effects and dynamic hazard zones. If a battle occurs, restrict it to capabilities already verified by the engine evidence rather than reimplementing missing mechanics in Minecraft.

The evidence graph, culprit uncertainty and downstream narrative consequences remain unchanged between reduced and full versions.

## Canon questions

No relay location, faction, saboteur, maintenance institution, corridor or outage is canon-approved by this proposal. A future location binding must use established Ouros geography and infrastructure canon.

PTU/Caelo checks remain necessary before assigning mechanical Skill checks, Trainer Features, Pokémon capabilities or battle effects to clue acquisition and repair.
