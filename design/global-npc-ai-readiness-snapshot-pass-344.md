# Global NPC AI readiness snapshot — Pass 344

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

Narrative repository

Head validated before this snapshot: `6c4e7d986307e21aea23a9aafe8eb534914ad340`.

`Global NPC AI Regressions` run #192 completed successfully on that head after adding the Pass 344 handoff-attempt module, tests, workflow trigger, research, contract, proposal and fixture.

Pass 344 executable seam

The narrative runtime can now preserve a failed authorized handoff attempt as append-only world state and schedule deterministic `EXTERNAL_EVENT` replans for the provider, physical recipient and accountable requester.

No-show, resource absence and site blockage do not fabricate custody. Explicit provider/recipient refusal closes the current authorization semantically without deleting it or moving the resource.

Read-only AutoPTU evidence

AutoPTU-Java head inspected: `b85fe17319d16e54402a5a45fb6acccd6b388553`, merge of PR #397 `Freeze Python Arena Trap target eligibility`.

The GitHub Actions query for that head reported 77 workflow runs. The retrieved current page showed completed successful runs and no failure or in-progress conclusion. This is CI evidence for that Java head, not evidence that every PTU capability family is complete.

The PR #397 slice freezes Python parity for Arena Trap target eligibility. It does not by itself prove Arena Trap stateful application, Slowed lifecycle, complete movement or the full Ability family.

AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its latest commit is explicitly presentation-only and states that battle rules/outcomes do not change.

Permanent capability assessment

Targeting / footprints / range / LoS: VERIFIED for previously audited ordinary contracts. Arena Trap has additional narrow target-eligibility evidence.

Base movement legality: VERIFIED for previously audited ordinary contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED for previously audited deterministic arithmetic.

Action economy / initiative: VERIFIED for current audited primitives.

Full turn / round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL and individually gated. Arena Trap target eligibility and the earlier Air Lock round-start work do not establish family completeness.

Items: PARTIAL and individually gated.

Trainer Features/perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED for its current ordinary scope.

AI tactical policy: BLOCKING for objective choices such as protect carrier, finish delivery, retreat with equipment, abandon equipment to rescue an actor, or stop fighting when the logistical objective is already satisfied.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end. Presentation cannot authoritatively create an attempt, refusal, arrival, custody transfer or Item effect.

Pass 344 encounter dependency map

Reduced `The Empty Counter` case: no structured battle dependency. Uses semantic time, request/handoff records, attempt provenance, communication, travel and world-agent replanning.

Rich blocked-pickup continuation: targeting VERIFIED within ordinary scope; base movement VERIFIED; complete movement PARTIAL; calculations VERIFIED; action economy/initiative VERIFIED for current primitives; lifecycle PARTIAL; damage PARTIAL; statuses PARTIAL; terrain/weather/hazards/zones/reactions MIXED/PARTIAL/BLOCKING; Moves/Abilities/Items/Trainer Features individually gated; AI tactical policy BLOCKING for protection/delivery/retreat objectives; adapter PARTIAL/BLOCKING.

Open questions

- whether no-show expiry should automatically schedule a second replan or remain a general semantic-time wake-up;
- how appointment confirmation/cancellation should flow through the communication runtime;
- when repeated failed handoffs may affect directional trust, without assuming fault from a single event;
- how travel completion supplies evidence that an actor actually reached the authored meeting point;
- checkpoint persistence for request, handoff and attempt ledgers;
- return/overdue integration with the older shared-equipment owner instead of duplicating it;
- player inventory and Minecraft acknowledgement boundaries;
- exact PTU/Caelo behavior for any mechanically active loaned Item.
