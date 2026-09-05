# Global NPC / engine readiness snapshot — Pass 279

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

## Narrative repository

Pass 279 adds an executable region-neutral agenda layer for persistent NPCs:
- durable goals;
- need pressure thresholds;
- semantic-time scheduled commitments;
- missed-commitment follow-up rather than teleportation;
- finite intent continuity;
- situational interruption through legal NPC knowledge;
- explicit structured-mechanics handoff.

Executable evidence:
- `tools/global_npc_ai.py`;
- `implementation/global-npc-goal-need-schedule-fixture-v1.json`;
- `tests/test_global_npc_goals_needs_schedules.py`;
- `.github/workflows/global-npc-ai.yml`.

The global NPC AI remains a world-agent planner. It does not satisfy the separate AutoPTU `AI tactical policy` category.

## AutoPTU-Java live evidence

Live head inspected: `b4d46423ba657417f987f7432b49a5f81a268062`.

Head is merge PR #357, `Add PTU/Kairos rulebook conformance baseline`.

The change strengthens the migration protocol by adding rulebook/profile conformance as an independent acceptance gate, documenting profile differences and requiring source-backed rule validation. This is valuable evidence-quality infrastructure. It does not by itself demonstrate broader tactical implementation in any permanent capability family.

Therefore Pass 279 makes no capability promotion from this commit alone.

## AutoPTU Python live evidence

Live head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

The head commit explicitly states its change is presentation-only and does not alter battle rules or outcomes. No new mechanical promotion follows.

## Permanent capability categories

Conservative status carried from the last audited narrative snapshot because no new live evidence proves a whole-family promotion:

- targeting/footprints/range/LoS — VERIFIED within audited contracts;
- base movement legality — VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED within audited contracts;
- action economy/initiative — VERIFIED within audited contracts;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED within audited contracts;
- AI tactical policy — BLOCKING for autonomous tactical choice;
- Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING end-to-end.

## Pass 279 dependency interpretation

Pure world scheduling, needs, long-term goals, reporting, ordinary off-screen work and non-mechanical rescheduling do not require AutoPTU capability families.

If a selected agenda action only needs visible overworld presentation, it depends on Minecraft/Cobblemon projection but not on tactical mechanics.

If an agenda action crosses into structured PTU resolution, Ouros emits `REQUEST_AUTOPTU`. The encounter must then declare every permanent capability family it actually uses; verified representative seams cannot be generalized to whole families.

## Source/canon boundary

No Pass 279 fixture NPC, region, job, need value, schedule or relationship is canon.

No PTU/Caelo/Kairos rule was silently adopted. The global agenda score and thresholds remain Ouros MMO/world-agent policy.
