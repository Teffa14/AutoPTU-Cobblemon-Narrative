# The Crate That Crossed the Save — case 356

Status: PROPOSED / NON-CANON
Date: 2026-09-08
Research provenance: `research/2026-09-08-atomic-handoff-world-recovery-scan-356.md`
Design dependency: `design/global-npc-world-handoff-checkpoint-integration-contract-pass-356.md`

## Premise

A field team receives authorization to collect a sealed instrument crate needed for a later observation. The pickup actually occurs. The courier leaves the workshop with the crate. Other world events then advance and the session ends before the instrument reaches its final destination.

When the world resumes, a second group needs the same instrument and claims that the first team never completed the pickup.

The interesting problem is not deciding which NPC is automatically correct. The player can reconstruct what the world can actually prove at the same recovery moment.

## Evidence chain

The case can expose:

- the original reservation;
- the request and provider response;
- the handoff authorization;
- the authorized receiver and location;
- the completed custody transfer;
- the semantic time of that transfer;
- the current knowledge held by the relevant NPCs;
- any later messages or scheduling changes.

A V7 save can preserve these records inside one coherent recovery unit.

An older V6 save may preserve the reservation and request while lacking provable handoff history. That missing history remains uncertainty. The current holder does not retroactively manufacture a transfer record.

## Possible resolutions

The player may verify that the first courier legitimately holds the crate and help the second group find another unit or window.

The player may discover that the handoff was authorized but never completed, leaving the resource still under provider custody.

The player may discover that the transfer occurred but a later communication failed, explaining why another team still believes the equipment is available.

The case can remain an ordinary logistics dispute or feed a longer institutional pattern if repeated scarcity, poor communication or weak procurement processes already exist in world history.

## Reduced playable version

The reduced version requires no AutoPTU battle.

It uses semantic time, reservations, resource requests, handoff authorization/custody history, coherent checkpoint restore, memory/belief, communication and ordinary world travel.

The player resolves the problem by investigating provenance, contacting participants and adjusting plans.

## Mechanically rich version

After the restart, the courier can still be moving toward the observation site when a wild interruption occurs. The narrative objective is to preserve the instrument and reach the destination before the useful observation window closes.

The encounter should support success through arrival, disengagement or safe rerouting rather than require elimination of every opponent.

Implementation dependencies:

Targeting/footprints/range/LoS is required for ordinary tactical reach and attack legality.

Base movement legality is required for ordinary route movement on the combat map.

Complete movement is required if the encounter uses interception, pushes, pulls, knockback, forced movement or displacement of the carrier.

Core calculations are required for ordinary PTU arithmetic.

Action economy/initiative is required if pickup, drop, handoff or protect interactions become tactical actions.

Full turn/round lifecycle is required if the observation deadline or interruption uses round-bounded timing.

Full stateful damage pipeline is required if damage to the courier or instrument has persistent battle consequences.

Status lifecycle is required for persistent combat conditions.

Terrain/weather/hazards/zones/reactions are required only when those specific mechanics are authored into the encounter.

Move-specific behavior, Abilities, Items and Trainer Features/perks remain individually gated.

AI legal-action infrastructure is required for any new cargo interaction action.

AI tactical policy is required for protect-carrier, delivery-first, reroute, intercept or disengage-after-objective decisions.

Minecraft/Cobblemon/Craftics adapter/playback is required for authoritative presentation and acknowledgement of any cargo/objective semantics.

## Canon boundary

The crate, observation, teams and dispute are design candidates only. They do not establish a new named NPC, institution, location or historical event in Ouros canon.

The scenario can later be bound to an established region only after continuity review.
