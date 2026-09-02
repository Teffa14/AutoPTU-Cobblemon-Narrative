# Engine Readiness Snapshot — Pass 211

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-09-02

## Live evidence checked

Read-only engine repositories were inspected for this pass.

AutoPTU-Java main: `ee794c04014f87740703bc73d5929c15360e0840` — `Freeze forced-movement prevention traces for area and delayed hits (#327)`. This adds evidence for blocked forced-movement traces in delayed and area-hit cases. It does not prove the full complete-movement family, including all push/pull/knockback/interception/forced-movement interactions.

AutoPTU main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`. The commit explicitly states that it is presentation-only and changes no battle rules or outcomes.

No capability family is promoted relative to pass 210.

## Permanent capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited contracts.
2. base movement legality — VERIFIED within audited contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL. Current forced-movement prevention traces are meaningful subcase evidence only.
4. core calculations — VERIFIED within audited contracts.
5. action economy/initiative — VERIFIED within audited contracts.
6. full turn/round lifecycle — PARTIAL.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — BLOCKING for the rich shared-site encounter as a complete family.
10. move-specific behavior — PARTIAL.
11. abilities — PARTIAL.
12. items — PARTIAL.
13. Trainer Features/perks — PARTIAL.
14. AI legal-action infrastructure — VERIFIED within audited contracts.
15. AI tactical policy — BLOCKING for autonomous parallel actors making tactical field-objective decisions.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for the full end-to-end rich encounter.

`VERIFIED` here means verified only inside the audited contracts already evidenced by the engine project. It does not mean every PTU interaction in that family is implemented.

## Pass 211 encounter dependency

`Shared Window at the Crossing` has two implementation tiers.

The full version uses spatial objectives, multiple actors with different task intents, optional wild/battle pressure, possible interception/repositioning, environmental state and autonomous tactical choices. If all of those elements are enabled, it touches all 16 permanent categories. Categories 3, 6-8, 10-13 and 16 remain partial; 9 and 15 are blocking. Therefore the full version is not implementation-ready as specified.

The reduced `Two Visits, One Site` version does not require a tactical rival expedition. It can use existing Minecraft locomotion as presentation, server-authored access windows, visit records, task intents, explicit handoffs and scheduled/authored NPC state transitions. Optional battles stay separate and may use only audited BattleSpec paths. This reduced version preserves the narrative premise while avoiding rule duplication in the adapter.

## Authority boundaries

Minecraft/Cobblemon must not decide access-window success, observation truth, professional credit, handoff provenance, task completion, battle legality or battle results from local entity/block state.

A document carried as a Minecraft item is presentation/correlation unless an authoritative Ouros object record backs it. Inventory transfer cannot silently mutate authorship or source provenance.

A competing or cooperating NPC party cannot be advanced through hidden Cobblemon combat AI and then have invented results written back into canon. Until a verified world-simulation/tactical-policy contract exists, off-screen progress must use explicit authored/scheduled transitions with defined writes.

The canonical lower-shelf Fletchling remains its own persistent world/battle identity. Pass 211 does not authorize cloning it, moving it to the seasonal crossing by convenience, changing its frozen blueprint or using its battle outcome as evidence for unrelated fieldwork.

## Mechanical questions still open

The project still needs exact PTU/Caelo/Kairos validation for which Skills, Edges, Features, Moves, capabilities or equipment can mechanically perform field measurement, safe-route assessment, equipment assistance or courier protection. Narrative competence cannot substitute for that rules check.

A server-authoritative contract is needed for access windows and site visits if they are to affect eligibility across sessions. The contract should distinguish authored schedule state from weather or terrain mechanics so a narrative window does not accidentally claim implementation of capability family 9.

If a future encounter lets two parties contest custody or spatial objectives during battle, BattleSpec needs audited semantic-objective/custody support. Until then, such objects remain narrative/world-state records outside battle authority.

If NPCs eventually choose between assistance, disengagement, protection and objective play tactically, AI legal-action enumeration alone is insufficient. AI tactical policy must be verified for the required decision family.

## Canon effect

None. This file records implementation evidence and constraints for proposed material. It does not alter rules authority, existing world facts or encounter canon.