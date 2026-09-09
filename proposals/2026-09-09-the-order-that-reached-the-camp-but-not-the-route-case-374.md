# The Order That Reached the Camp but Not the Route — Pass 374

Status: PROPOSED / NON-CANON
Date: 2026-09-09
Canon effect: NONE

## Premise

A field team receives a legitimate route-change message before departing from a temporary camp. The delivery becomes part of the leader's usable evidence and wakes the planner. The corresponding replan trigger is processed.

Another obligation wins the same planning cycle. The team leaves on a different urgent task instead of taking the requested route.

Hours later, an administrator sees that the reroute message was delivered and assumes the field team ignored it. The field leader can truthfully say that the message was received and considered. A third worker can truthfully say that the route change was never issued as the team's final plan.

The contradiction is causal, not deceptive.

## World-state chain

Required preserved facts:

communication authored;
communication delivered;
delivery materialized as receiver evidence;
knowledge-delivered wake trigger created;
wake trigger consumed;
selected plan still unresolved by Pass 374 provenance;
actual action still resolved by its own owner.

The scenario depends on the explicit boundary:

`DELIVERED != MATERIALIZED != REPLAN_CONSUMED != PLAN_SELECTED != ACTION_STARTED`

## Investigation hooks

The player may encounter the discrepancy while checking a routine field site rather than through a dedicated quest summons.

Evidence can include message records, travel traces, shift notes, resource reservations, witness knowledge and the team's later location.

The mystery can resolve into ordinary prioritization, incomplete authority, an emergency, conflicting obligations or deliberate misconduct. The first discovery must not preselect the cause.

## Reduced implementation

The reduced version requires no AutoPTU battle resolution.

Required world-agent capabilities:

semantic time and travel;
Communications delivery provenance;
private knowledge and memory references;
DeliveryReplanProvenanceLedger;
coherent V15 recovery;
ordinary agenda/replan processing.

The player can reconstruct the chain, interview participants, carry updated information and choose whom to inform.

## Mechanically rich implementation

The downstream consequence occurs at an active field location where the unexpected assignment has placed the team in danger or caused a second objective to become time-sensitive.

Possible objectives include reaching the team, preserving a sample case, escorting a worker, withdrawing safely, carrying a replacement message or keeping a route open long enough for evacuation.

Combat is optional pressure. The narrative premise does not require defeating every Pokémon.

## AutoPTU dependency classification

Targeting/footprints/range/LoS: VERIFIED for ordinary audited use. Required only if the full encounter uses tactical targeting or visibility.

Base movement legality: VERIFIED for ordinary audited use. Required for normal tactical approach/retreat.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. The reduced encounter excludes these mechanics. Any full version using forced displacement or interception remains gated.

Core calculations: VERIFIED within audited deterministic contracts when ordinary battle arithmetic is needed.

Action economy/initiative: VERIFIED for audited primitives. Required for the full tactical version.

Full turn/round lifecycle: PARTIAL. Required if the encounter depends on complete phase/round behavior rather than simple audited actions.

Full stateful damage pipeline: PARTIAL. Required for a combat-heavy full version.

Status lifecycle: PARTIAL. Complex status-based objectives are excluded from the reduced version.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact mechanism. Environmental phases, reaction zones or hazard-dependent objectives must be individually verified before use.

Move-specific behavior: INDIVIDUALLY GATED.

Abilities: INDIVIDUALLY GATED. Current Java evidence for the round-start registry does not verify the whole family.

Items: INDIVIDUALLY GATED.

Trainer Features/perks: INDIVIDUALLY GATED.

AI legal-action infrastructure: VERIFIED for ordinary audited actions.

AI tactical policy: BLOCKING for escort, preserve-cargo, intercept-to-inform, rescue-first, objective-aware withdrawal and disengage-after-objective policies.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING for persistent objective/cargo identity, acknowledgement and authoritative end-to-end playback.

## Canon questions

No location, institution, field profession, route, species population or recurring NPC is canonized by this proposal.

Before promotion, bind the scenario to approved Ouros geography and institutions and verify any Pokémon population against established regional ecology.

Any battle-specific implementation must use current PTU/Caelo authority and explicit AutoPTU capability evidence rather than this narrative file.
