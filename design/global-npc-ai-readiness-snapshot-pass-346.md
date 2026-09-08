# Global NPC AI readiness snapshot — Pass 346

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-09-07

Narrative repository evidence

Pass 346 adds an executable handoff-reschedule successor layer after Pass 345 appointment coordination.

New evidence:

- `tools/global_npc_resource_handoff_rescheduling.py`;
- `tests/test_global_npc_resource_handoff_rescheduling.py`;
- `implementation/global-npc-resource-handoff-reschedule-regression-v1.json`;
- `design/global-npc-resource-handoff-reschedule-successor-contract-pass-346.md`;
- `research/2026-09-07-handoff-reschedule-successor-authorization-scan-346.md`;
- `proposals/2026-09-07-the-window-that-moved-case-346.md`.

The first Global NPC AI run for the new suite exposed two regression-fixture constructor errors: the tests used `capability_tags` while the live `WorldResource` contract uses `capability_refs`. No production logic was relaxed. After correcting the test inputs, Global NPC AI Regressions run #205 completed successfully, including the existing fixture replays and the complete `tests/test_global_npc_*.py` pytest suite.

The workflow path filter was then extended so future edits to `tools/global_npc_resource_handoff_rescheduling.py` trigger the same regression suite directly.

Pass 346 world-state scope

The layer can now preserve an original handoff authorization, bind a proposed replacement to an actual Pass 345 RESCHEDULE_REQUEST, require real message delivery before the named responder can decide, record ACCEPT/REJECT, create a distinct successor authorization after acceptance, mark the older authorization operationally superseded, resolve the current authorization through a deterministic replacement chain, and reject a physical transfer that still cites stale authority.

No reschedule event changes resource custody. The existing Pass 343 physical handoff owner still performs that mutation.

PTU / Caelo source boundary

The project README continues to identify the supplied PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List as the governing source set for mechanical claims.

Pass 346 creates no PTU Skill Check, Item effect, Trainer Feature, movement permission, combat action or battle timing rule. The successor-authorization layer is world-state scheduling/provenance only. If a future tactical scene turns pickup, delivery, guarding, interception or timed transfer into combat mechanics, exact PTU/Caelo and AutoPTU evidence remains required.

Read-only engine heads inspected

AutoPTU-Java:

- head: `30ff159abafbef6d14ef4a776789e9077dd26bc4`;
- merge of PR #398, `Preserve numeric Burrow speed in movement profiles`;
- evidence: numeric Burrow speed is preserved in the movement-profile representation instead of collapsing all Burrow capability into one boolean;
- limitation: this does not prove carrying, interception, push/pull, knockback, rescue, forced movement or the complete movement family.

AutoPTU Python:

- head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`;
- latest commit states that its viewport-coordinate change is presentation-only and changes no battle rules or outcomes.

Permanent capability classification

Targeting / footprints / range / LoS: VERIFIED for previously audited ordinary targeting contracts. Pass 346 does not add new evidence for the whole family.

Base movement legality: VERIFIED for previously audited ordinary movement contracts. Numeric Burrow representation in Java is additional narrow evidence, not a promotion of complete movement.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Rich courier/interception versions remain gated.

Core calculations: VERIFIED for previously audited deterministic arithmetic.

Action economy / initiative: VERIFIED for current audited primitives. A new tactical handoff action would still require explicit legal-action and timing evidence.

Full turn / round lifecycle: PARTIAL. Round-bound delivery windows, delayed pickup effects or objective phase transitions remain gated.

Full stateful damage pipeline: PARTIAL. Any authoritative damage to courier, opponents or carried equipment needs this family.

Status lifecycle: PARTIAL. Persistent conditions affecting a courier or escort remain gated.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING. Any route obstruction or battle-site effect must declare the exact family used.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL and individually gated.

Items: PARTIAL and individually gated. A world resource being physically present does not prove its PTU Item effect is implemented.

Trainer Features/perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED for its current ordinary audited scope. New objective interactions such as tactical pickup/drop/handoff still require their own legal-action contract.

AI tactical policy: BLOCKING for rich objectives where an agent must protect a carrier, prioritize delivery over defeat, avoid interception, retreat with equipment, or stop fighting after the logistical objective succeeds.

Minecraft / Cobblemon / Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end. Presentation can show a meeting place, courier, item and dialogue. It cannot author message receipt, accept a reschedule, supersede an authorization, change custody or infer character knowledge.

Reduced encounter readiness

`The Window That Moved` can run without AutoPTU using semantic time, communication delivery, Pass 343 handoff state, Pass 345 appointment notice state, Pass 346 successor authorization, travel, memory/belief and replanning.

Mechanically rich encounter readiness

A post-pickup interruption that preserves the same narrative premise can use ordinary verified targeting/base movement/arithmetic/action primitives where applicable. It remains blocked or partial for complete movement, full lifecycle, full damage, status, rich terrain/weather/hazards/reactions, exact Moves/Abilities/Items/Trainer Features, objective-aware tactical AI and full Minecraft adapter integration.

Unresolved world-state questions

- delivering the ACCEPT/REJECT response back through the durable communication runtime;
- actor-specific replanning only after each actor learns the successor authorization;
- checking reservation conflicts before accepting a proposed new window;
- whether an accepted successor must explicitly cancel the old appointment or supersession alone is sufficient;
- institutional authority for changing provider, resource, receiving actor or handoff mode;
- arrival/departure evidence sourced from travel rather than authored assumptions;
- chained reschedules and conflict resolution;
- persistence of request/handoff/attempt/appointment/reschedule ledgers in the atomic world checkpoint;
- player inventory and Minecraft projection bindings;
- canon review for whether Teo, Ema and Nerea may alter this class of handoff without additional approval.
