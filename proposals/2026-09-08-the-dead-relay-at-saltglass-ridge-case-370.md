# The Dead Relay at Saltglass Ridge — Pass 370

Status: PROPOSED / NON-CANON
Date: 2026-09-08
Canon effect: NONE

## Premise

A field office reallocates a calibrated survey instrument away from one expedition because another observation window has become more urgent. The displaced holder receives a proper notice obligation. An office worker authors the correct message to the correct person and sends it through a remote relay serving the ridge route.

The relay is unavailable when delivery comes due. Communications records a terminal failed attempt and retains the envelope provenance. The field team never receives the new claim and continues toward the old rendezvous using the last schedule it actually knows.

After restart, the office can truthfully prove that a message was authored and attempted. The expedition can truthfully say that no update arrived. The transport archive can prove both statements simultaneously.

The cause of the relay failure remains open. Ordinary equipment failure, damage, environmental interference, Pokémon activity, negligence or deliberate action are separate hypotheses that require evidence. The proposal does not canonize sabotage.

## Player-facing investigation loop

The incident can surface when the player notices that the displaced team is missing from the new allocation plan, encounters them on the obsolete route, or is asked to reconcile conflicting accounts at the field office.

Useful evidence includes the resource application record, the notice obligation, the linked communication event, its intended recipient, terminal delivery status, relay maintenance evidence and what each NPC actually knew before leaving.

Consequences can remain small or grow. The team may lose an observation window, carry the wrong equipment into another site, require a manual courier, distrust office scheduling, or discover that other failed notices share the same relay path.

## Reduced implementation version

This version requires no AutoPTU battle.

The relay failure is a semantic world event. The player can inspect records, travel to intercept the team, carry the update manually or restore communication through a non-combat interaction. Success means getting the correct information to the affected holder soon enough for a useful replan.

Required living-world capabilities are semantic time, resource reservation/allocation persistence, notice obligations, real communication status/provenance, private knowledge, travel and selective replanning.

## Full field version

The failed relay becomes a physical field objective. The player reaches the ridge and must inspect or restore the station while wild Pokémon and difficult terrain complicate movement. The objective can be completed by restoring the relay, protecting equipment long enough to transmit, or carrying the update onward. Defeating every opponent is optional unless a later encounter design explicitly requires it.

If weather phases, hazardous zones, forced movement, persistent statuses, Ability-driven terrain or Trainer Feature interrupts are added later, each mechanic must remain separately gated by engine evidence.

## Permanent engine capability dependencies

targeting/footprints/range/LoS: VERIFIED within ordinary audited contracts; needed for rich encounter geometry.

base movement legality: VERIFIED within ordinary audited contracts; needed for basic approach and positioning.

complete movement including push/pull/knockback/interception/forced movement: PARTIAL; needed only if the encounter uses physical interception, forced displacement or carrying interactions.

core calculations: VERIFIED within audited deterministic scope; needed for ordinary resolved combat arithmetic.

action economy/initiative: VERIFIED for audited primitives; richer objective interactions remain individually gated.

full turn/round lifecycle: PARTIAL; required for a sustained tactical battle with phase-sensitive effects.

full stateful damage pipeline: PARTIAL; required for the complete combat version.

status lifecycle: PARTIAL; required if persistent conditions are introduced.

terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism; required only for explicit environmental pressure or reaction mechanics.

move-specific behavior: PARTIAL and individually gated.

abilities: PARTIAL and individually gated. Existing Intimidate reaction parity evidence does not establish complete Ability support.

items: PARTIAL and individually gated.

Trainer Features/perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED within ordinary audited action-generation scope.

AI tactical policy: BLOCKING for protect-relay, preserve-equipment, intercept-to-inform, reroute and disengage-after-objective policies.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for authoritative relay interaction, objective acknowledgement, carried-equipment identity and end-to-end playback.

## Canon questions deliberately left open

Saltglass Ridge is a placeholder working name and has no canon geography status.

No institution, relay network, survey program, named employee or field expedition is approved by this proposal.

The existence and technical form of long-range communications in a specific Ouros location must remain consistent with established regional canon before promotion.

Any Pokémon species used at the relay site must be checked against approved regional ecology and supplied PTU/Caelo material.
