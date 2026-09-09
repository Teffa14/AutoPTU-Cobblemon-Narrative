# Delivery / replan provenance runtime scan — Pass 373

Status: RESEARCH / NON-CANON
Date: 2026-09-09
Canon effect: NONE

## Repository inspection

The recursive repository tree at narrative head `68b92f7bb91951b53697277a4c348e142d8abde4` was inspected before writing. `CURRENT_FOCUS.md`, canon governance, Pass 372, the existing delivery coordinator, replan queue, world checkpoint, V14 resource/notice wrapper and relevant tests were checked before selecting this slice.

The concrete gap remains the one documented in Pass 372: after a replan trigger is consumed, `NpcReplanQueue` retains the completed trigger ID but no longer retains the trigger's full agent/reason/source/due/priority provenance. The coordinator separately retains only the set of delivery-event IDs already materialized. Those states are sufficient for idempotency but insufficient to prove the exact historical chain after restart.

This pass implements a standalone provenance owner. It deliberately does not yet alter the coherent V14 world checkpoint.

## Duplicate-source control

Repository search was used before external research. Repeated comparison sources including Pokémon Rollout!, Putuland, Pokémon Living World, Pokémon World Tour material and Pokémon Pokopia were not reprocessed as primary evidence. `Pokémon Mystère Exploration` had no prior repository hit by name and was selected as a new fan-game reference.

## New operational source — FAA acknowledgement / readback discipline

Sources inspected 2026-09-09:

- Federal Aviation Administration, Air Traffic Control, 2-4-3 Pilot Acknowledgment/Read Back: https://www.faa.gov/air_traffic/publications/atpubs/atc_html/chap2_section_4.html
- Federal Aviation Administration, Aeronautical Information Manual, 4-4-7 Pilot Responsibility upon Clearance Issuance: https://www.faa.gov/Air_traffic/publications/atpubs/aim_html/chap4_section_4.html

The FAA material separates issuance from acknowledgement and verification. The ATC manual explicitly notes that before acknowledgement the controller cannot know whether the pilot will comply or remain on the previous clearance. The AIM also treats acceptance/refusal as the pilot's responsibility and uses readback as mutual verification.

Reusable Ouros abstraction:

A communication can be validly authored and delivered without proving that its receiver acknowledged it, understood it correctly, accepted it, selected the requested plan or began the requested action. Each transition should remain independently queryable when a story depends on misunderstanding, delayed confirmation or competing obligations.

No aviation rule or phraseology becomes Ouros canon. The source supports only the high-level causal separation.

## New fan-game source — Pokémon Mystère Exploration

Source inspected 2026-09-09:

- Pokémon Mystère Exploration public project site: https://pmexploration.net/

The project publicly presents changing dungeon layouts, traps, hidden shops, dynamic combat and an expedition loop where dungeon failure can remove carried items while a separate persistent resource survives and can be used in town to prepare for another attempt.

Reusable Ouros abstraction:

A failed field attempt does not need to reset every form of progress. Route intelligence, mapped hazards, established contacts, verified communications, environmental observations or institutional permissions can survive while perishable supplies, a time window or temporary field position are lost. This supports retryable expeditions whose second attempt is informed by the first without copying the fan game's resource names, town, dungeons, characters, combat rules or progression system.

## PTU / Caelo cross-check

Internal project authority remains PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and the Caelo Region Location & Encounter List where available. Public campaign/fan-game/operations sources are literary and systems-design evidence only.

Pass 373 adds no PTU move, Ability, Item, Trainer Feature, status, terrain or combat rule. A world-agent delivery can wake planning without granting any battle mechanic. Any structured battle consequence still requires explicit AutoPTU handoff and exact capability admission.

## Live engine evidence

Read-only AutoPTU-Java head inspected: `a0e7a0089f3cb3dce1f8b82fd92c6b99f64a2207`, merge #413, `Add generic round-start ability lifecycle hook`.

The new lifecycle hook executes the Python-parity round-start Ability dispatch plan from the authoritative lifecycle. Its own implementation states that unsupported families remain explicit unhandled invocations until their Python behavior is frozen and implemented. This strengthens evidence for generic round-start orchestration but does not verify all Abilities or the complete turn/round lifecycle.

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, still presentation-only viewport synchronization with no battle rule/outcome change.

Neither engine repository was modified.

## Resulting design lesson

For long-form Ouros continuity, the durable historical chain should be able to answer all of these independently:

`AUTHORED -> DELIVERED -> MATERIALIZED_AS_EVIDENCE -> REPLAN_TRIGGER_CREATED -> REPLAN_TRIGGER_CONSUMED -> PLAN_SELECTED -> ACTION_STARTED -> ACKNOWLEDGED`

The ordering of acknowledgement may differ by workflow and should not be silently inferred from another state. Pass 373 only closes the materialization and consumed-trigger provenance seam. Plan selection, action commencement and explicit acknowledgement remain separate owners.