# Global NPC AI readiness snapshot — Pass 343

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

Scope

Pass 343 adds an executable physical handoff/custody seam after Pass 342 provider consent.

Only `Teffa14/AutoPTU-Cobblemon-Narrative` was modified. AutoPTU-Java and AutoPTU were inspected read-only.

Narrative evidence

Narrative main began at `1da1fec9fd54659ee0f3ecbe489083adf28a5dce`.

The recursive repository tree, current focus, canon governance, canonical Marea resident network, Pass 338–342 resource owners, request code/tests and CI workflow were inspected before writing.

Pass 342 explicitly deferred handoff, pickup, delivery, proxy pickup and custody transfer. No existing region-neutral executable owner covered this seam.

Pass 343 adds:

- `tools/global_npc_resource_handoffs.py`;
- `tests/test_global_npc_resource_handoffs.py`;
- `implementation/global-npc-resource-handoff-fixture-v1.json`;
- `design/global-npc-resource-handoff-custody-contract-pass-343.md`;
- `research/2026-09-07-resource-handoff-proxy-custody-scan-343.md`;
- `proposals/2026-09-07-the-proxy-between-two-places-case-343.md`.

The executable seam distinguishes accepted request, handoff authorization, accountable requester, physical recipient, resource location, current holder and completed custody transfer.

A named proxy may receive the item physically while the requester remains the accountable actor. The resource is not teleported to the requester.

CI evidence

`.github/workflows/global-npc-ai.yml` now includes `tools/global_npc_resource_handoffs.py` in push and pull-request path triggers.

Workflow run #187 for head `70d55bde14e8ab01ee95d442c90ba58099e588ea` executed the pytest-based global NPC suite. The `Run global NPC AI regressions` step completed successfully. At snapshot authoring time only workflow post-job cleanup remained in progress; therefore the test step itself is verified green while the overall run conclusion was not yet final.

Live read-only engine heads

AutoPTU-Java main remains `b85fe17319d16e54402a5a45fb6acccd6b388553`, merge of PR #397, `Freeze Python Arena Trap target eligibility`.

This is narrow evidence for Arena Trap target eligibility, including the verified 5-meter targeting contract and oracle-backed exclusions represented by that slice. It does not prove stateful status application, complete movement, the entire Ability family or full lifecycle behavior.

AutoPTU Python main remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit explicitly states that the change is presentation-only and does not alter battle rules or outcomes.

Permanent capability audit

Targeting / footprints / range / LoS: VERIFIED for previously audited ordinary contracts. Arena Trap adds narrow target-range evidence only.

Base movement legality: VERIFIED for previously audited ordinary contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Carrying constraints, interception and forced resource/carrier displacement remain gated.

Core calculations: VERIFIED for previously audited deterministic arithmetic.

Action economy / initiative: VERIFIED for current audited primitives. Exact tactical pickup/drop/handoff/equip actions remain separately unverified.

Full turn / round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL. Arena Trap target selection does not prove Slowed application/duration/cleanup.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING by subfamily.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL and individually gated. Air Lock and Arena Trap provide representative narrow evidence only.

Items: PARTIAL and individually gated. World-resource custody does not establish PTU Item legality or effects.

Trainer Features / perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED for its current ordinary audited scope. Tactical object-transfer actions are not promoted by the world-level handoff seam.

AI tactical policy: BLOCKING for rich delivery/protection/retreat objectives.

Minecraft / Cobblemon / Craftics adapter/playback: PARTIAL / BLOCKING end-to-end. Presentation cannot create authoritative custody, proxy authority, travel completion or Item effects.

Reduced-version readiness

Pass 343 is executable without AutoPTU.

A resource may move from provider to requester or named proxy only after explicit authorization and verified world facts. Holder/location history can then drive travel, schedules, dialogue, belief and replanning.

Rich encounter dependency map

The proposed `The Proxy Between Two Places` case has a reduced noncombat implementation.

If the carrier is interrupted during structured play, the rich form depends on:

- targeting/range/LoS for exact threat/protection geometry;
- base movement for ordinary tactical relocation;
- complete movement for carrying/interception/rescue/forced displacement;
- core calculations for exact PTU arithmetic;
- action economy/initiative for pickup/drop/handoff/guard actions;
- full lifecycle for timed delivery or delayed objectives;
- damage pipeline for actor/equipment damage;
- status lifecycle for persistent carrier conditions;
- terrain/weather/hazards/zones/reactions for changing route/site conditions;
- exact Move/Ability/Item/Trainer Feature families used by the encounter;
- AI legal-action infrastructure for any new object actions;
- AI tactical policy for protecting the carrier, retreating, delivering or de-escalating;
- adapter/playback for presentation only.

Unresolved mechanical questions

- exact tactical pickup/drop/handoff action contracts;
- carrying and object-interception semantics;
- equipment damage representation;
- courier/travel coordinator;
- accepted request to reservation/checkout integration;
- proxy delegation authority beyond one explicit authorization;
- partial/quantity fulfillment;
- return/overdue obligations;
- checkpoint persistence;
- expiry/no-show replanning;
- PTU/Caelo mapping for mechanically active Items.

Unresolved canon questions

- whether the proposed Teo/Nerea/Ema handoff occurs;
- exact instrument identity;
- institution-specific proxy rules;
- who can delegate pickup authority;
- whether delivery or pickup is normally expected;
- any permanent borrowing policy;
- any route interruption or battle tied to the proposal.
