# The Message That Woke the Wrong Plan — Pass 372

Status: PROPOSED / NON-CANON
Date: 2026-09-09
Canon effect: NONE

## Premise

A field team receives a legitimate route update while already travelling. The delivery reaches the correct leader and becomes durable receiver evidence. That event also creates a replanning wake-up. Before the group commits to a new route, another higher-priority obligation enters the same planning batch and wins.

Hours later an observer sees three facts that appear contradictory: the message was delivered, the team can prove it received the update, and the team still travelled somewhere else.

The contradiction disappears when provenance survives at the correct granularity. Delivery caused a replan opportunity. It did not dictate the decision produced by that planning cycle.

## Narrative use

The player first encounters the consequence: a survey crew is present at an unexpected location while another institution believes the crew ignored a direct instruction.

Investigation can recover the authored route update, its real delivery, the receiver evidence, the wake-up that entered the planner and the competing obligation that won the resulting agenda decision.

No actor needs to lie. The sender can correctly say the message was delivered. The leader can correctly say it was considered. Another official can correctly say the requested route was never selected.

## Full version

The competing obligation is an urgent field hazard or welfare duty encountered during travel. The player may help complete that duty quickly enough to preserve part of the original observation window, escort a courier carrying replacement instructions, recover equipment or divide responsibilities between teams.

Wild Pokémon can create pressure without becoming the mission's mandatory elimination objective. The encounter can end through safe passage, rescue, rerouting, delivery, protection or successful observation.

## Reduced version

Run entirely through semantic world simulation. The update is delivered, materialized into the leader's evidence, a `KNOWLEDGE_DELIVERED` trigger enters the replan queue, and the agenda planner selects a different lawful obligation. The player later reconstructs the provenance through records and conversations.

This version preserves the complete narrative premise without structured combat.

## Required persistent facts

The case needs the authored communication envelope, delivery status, receiver identity, durable receiver evidence, materialization receipt, replan trigger provenance, planning batch or consumed-trigger provenance, the chosen agenda result and the active travel plan.

Final position must never be used to infer which information was delivered or which trigger caused a planning cycle.

## Mechanical dependency classification

Targeting/footprints/range/LoS: VERIFIED within ordinary audited scope if tactical play occurs.

Base movement legality: VERIFIED within ordinary audited scope.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Required only if the full encounter uses physical interception, forced displacement, carrier movement or similar interactions.

Core calculations: VERIFIED within audited deterministic scope.

Action economy/initiative: VERIFIED for audited primitives.

Full turn/round lifecycle: PARTIAL. Required for strict timed escort, rescue or observation windows.

Full stateful damage pipeline: PARTIAL. Required if battle injury changes later world outcomes.

Status lifecycle: PARTIAL. Required if a condition alters travel, communication or objective execution.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact mechanism. Reduced play should model static obstruction or semantic travel cost instead of unverified reactive weather/hazard behavior.

Move-specific behavior: individually gated.

Abilities: individually gated. Java merge #412 verifies registration of the exact Intimidate round-start path after its parity gates; it does not verify Abilities generally.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED for ordinary audited actions.

AI tactical policy: BLOCKING for intercept-to-inform, escort, preserve-cargo, rescue-first, reroute-after-objective and disengage-after-objective policies.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for objective acknowledgement, persistent cargo/resource identity and authoritative end-to-end playback.

## Canon questions

The institutions, route, hazard, observation objective, communication medium and involved species are placeholders. A canon binding must reuse approved geography and organizations rather than creating an isolated institution for this quest.

No rule here assumes universal radio or electronic messaging. The same causal structure can use courier, terminal, ranger station, messenger Pokémon or another medium already approved for the chosen location.