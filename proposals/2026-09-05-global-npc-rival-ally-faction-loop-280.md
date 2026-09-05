# Global rival / ally / faction social loop — Pass 280

Status: PROPOSED NARRATIVE / SYSTEM LOOP
Date: 2026-09-05
Canon effect: NONE until separately approved

## Premise

Recurring NPCs should accumulate social history that changes what they choose to do across the whole Ouros world.

The same architecture supports a friend, mentor, rival, coworker, investigator, merchant, faction member or opponent. No region owns the behavior model.

## Example loop

An NPC has ordinary work and a scheduled training goal. They learn through a legitimate message that a close friend needs help. Their directional affinity/trust/debt state makes assistance competitive with the normal agenda, so they leave the routine task and respond.

A second NPC belongs to an institution with an explicit reporting duty. That role can make filing a report important, but membership alone does not tell them the hidden content of another member's investigation. They must receive the information first.

A third NPC has a long-running rival. High rivalry and respect can make `ARRANGE_CHALLENGE`, training or observation attractive. The relationship can therefore create repeated encounters without a scripted “rival appears every third badge” rule.

If both participants later agree to a mechanically structured spar, the world-agent layer requests AutoPTU and holds while structured resolution owns the encounter.

## Persistent consequences

Useful social results can include:
- a kept promise increasing trust;
- help received creating reciprocal obligation;
- an unfair accusation reducing trust without necessarily reducing respect;
- repeated competition increasing rivalry;
- a dangerous incident increasing fear without creating hatred;
- faction promotion changing role permissions/obligations while leaving personal relationships untouched.

Every mutation needs a semantic event/provenance reference. Selection of an intent alone changes nothing.

## Full and reduced encounter forms

Reduced form:
- NPC decides to seek, message, avoid, assist, report, socialize, train or arrange a challenge;
- off-screen world state can progress without local entities when geometry is irrelevant;
- dialogue/presentation can be authored or deferred;
- no AutoPTU dependency.

Full rival encounter:
- world-agent intent selects a structured spar/confrontation;
- Ouros builds the encounter request;
- AutoPTU owns tactical legality and outcome;
- semantic results return to world state;
- a separately authored social consequence may update relationship dimensions with provenance.

Potential dependencies for the full version must be declared per encounter: targeting/footprints/range/LoS; base movement; complete movement for interception/forced movement; core calculations; action economy/initiative; full lifecycle; stateful damage; status lifecycle; terrain/weather/hazards/zones/reactions; move-specific behavior; Abilities; Items; Trainer Features/perks; AI legal-action infrastructure; AI tactical policy; and Minecraft/Cobblemon/Craftics adapter/playback.

The reduced narrative premise remains valid if any richer tactical family is unavailable.

## Long-term arc value

This architecture allows rivalries to cool or intensify through history, allies to disagree, faction members to defect or refuse a duty for explainable reasons, mentors to respect a character they do not like, and friends to lose trust without instantly becoming enemies.

It also supports NPC-to-NPC arcs happening away from the player once communication, travel and scalable event scheduling are connected.

## Unresolved content decisions

- player visibility of relationship dimensions;
- decay or persistence policy for each dimension;
- how belief-source reliability later interacts with interpersonal trust;
- when social consequences of battle results are authored versus inferred;
- faction hierarchy and conflict rules;
- whether debts can expire or be formally discharged;
- migration from aggregate background actors to persistent relationships.
