# Global NPC AI Readiness Snapshot — Pass 283

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

## Narrative repository evidence

Pass 283 adds a region-neutral event-driven information transport layer on top of the Pass 282 per-agent memory/belief ledger.

Executable evidence:
- `tools/global_npc_information_network.py`
- `implementation/global-npc-information-propagation-fixture-v1.json`
- `tests/test_global_npc_information_network.py`

Covered contracts include semantic latency, due-only processing, deterministic ordering, unavailable channels, local-projection acknowledgement, provenance-root preservation, same-root deduplication, independent-source preservation and idempotent in-process replay.

Durable queue persistence across a real server restart is still an integration gap; the in-memory executable contract must not be reported as storage-complete.

## Read-only AutoPTU-Java evidence

Live main inspected at:
`d6c42c2d7c6750a71f10614d2db7525757cc4dca`

Head commit: `Extract declarative temporary-effect lifecycle cleanup hook (#362)`.

The evidence is narrow: a reusable temporary-effect cleanup hook is routed through round-start lifecycle infrastructure and tested for its defined cleanup scope. This supports the existence of that seam. It does not prove full lifecycle or full status-family coverage and does not change the readiness categories below.

## Read-only AutoPTU Python evidence

Live main inspected at:
`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Head commit remains explicitly presentation-only (`Career: keep battle coordinates synced after viewport resize (#237)`) and states that battle rules/outcomes do not change.

No category promotion follows from this evidence.

## Permanent capability-category audit

- targeting / footprints / range / LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy / initiative: VERIFIED within audited contracts;
- full turn / round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING depending on behavior;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features / perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for autonomous structured tactical choice;
- Minecraft / Cobblemon / Craftics adapter and playback support: PARTIAL / BLOCKING end-to-end.

One representative implementation or hook must never promote an entire capability family.

## Pass 283 dependency interpretation

Ordinary message scheduling, remote delivery, provenance preservation and belief updates require no AutoPTU tactical capability.

A local face-to-face communication can remain world-level if it only requires adapter acknowledgement. If the scene becomes a mechanically structured confrontation, chase or battle, Ouros must hand off to AutoPTU and gate the scene by the exact families it uses.

Examples:
- pursuit/interception requires complete movement;
- tactical weather/hazard effects require terrain/weather/hazards/zones/reactions;
- temporary or delayed battle effects require the relevant lifecycle/status/move/ability/item/feature contracts;
- autonomous combat tactics require AI tactical policy;
- faithful visible reproduction requires adapter/playback support.

The reduced information-network mystery loop therefore remains implementable even while those richer families are partial/blocking.

## PTU/Caelo/Kairos authority

No PTU, Caelo or Kairos rule is adopted by Pass 283. Event queues, message latency, channel state and communication delivery are Ouros simulation policy.

`SOURCE_HAS_RULE != OUROS_USES_RULE` remains binding.

## Open implementation risks

- persistent storage of pending/delivered event IDs across real server lifecycle;
- scalable audience resolution without faction-wide hidden knowledge;
- selective forwarding policy based on social/role state;
- event-triggered agenda replanning integration;
- local adapter acknowledgement plumbing;
- channel congestion/retries/interception if later desired;
- deception, source confusion, forgetting and claim mutation;
- performance validation at thousands of named agents/events.
