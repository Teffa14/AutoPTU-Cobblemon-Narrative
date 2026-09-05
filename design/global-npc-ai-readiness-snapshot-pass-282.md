# Global NPC AI / engine readiness snapshot — Pass 282

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05
Narrative baseline before this pass: `027d72c839a99dcb338ff46a3b531f79c8f25de7`

## Read-only engine evidence

AutoPTU-Java live main remains `d6c42c2d7c6750a71f10614d2db7525757cc4dca`, PR #362, `Extract declarative temporary-effect lifecycle cleanup hook`.

That commit provides narrow positive evidence for reusable temporary-effect cleanup at lifecycle hooks, including actor/all-combatant scope tests and preservation of unrelated temporary effects. It does not prove full lifecycle, full status behavior, tactical policy, world-agent memory or adapter playback.

AutoPTU Python remains at the previously audited `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its head is presentation-only and does not change battle rules/outcomes.

Neither engine repository is modified by Pass 282.

## Permanent capability classification

No capability family is promoted by this pass.

- targeting / footprints / range / LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy / initiative: VERIFIED within audited contracts;
- full turn / round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING;
- move-specific behavior: PARTIAL;
- Abilities: PARTIAL;
- Items: PARTIAL;
- Trainer Features / perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING;
- Minecraft / Cobblemon / Craftics adapter / playback: PARTIAL / BLOCKING end-to-end.

## Memory-specific distinction

Global NPC memory/belief/communication is Ouros world-agent state. Direct observation records, hearsay lineage, contradiction and report propagation do not depend on tactical AI.

Reduced investigation/rumor loop:
- persistent NPC knowledge ledgers;
- explicit communication events;
- semantic time;
- directional trust input where configured;
- deterministic belief assessment;
- no AutoPTU dependency.

Locally rendered interview or observation:
- Minecraft/Cobblemon/Craftics adapter/playback remains required to turn local presentation into an accepted semantic observation/communication result;
- adapter remains PARTIAL/BLOCKING end-to-end, so reduced content may record authored/world events without pretending local animation completed the semantic action.

Structured confrontation caused by a belief:
- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL for multi-turn behavior;
- full stateful damage pipeline: PARTIAL if damage occurs;
- status lifecycle: PARTIAL if statuses occur;
- complete movement: PARTIAL for interception/forced movement/knockback;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING when used;
- exact Move/Ability/Item/Trainer Feature behavior: PARTIAL and requires encounter-specific audit;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for autonomous tactical choice;
- adapter/playback: PARTIAL/BLOCKING end-to-end.

## Canon/mechanics questions left open

No synthetic fixture claim, route state, confidence score or NPC is canonized.

Memory decay/forgetting remains unimplemented. Deliberate lying and source confusion remain unimplemented. Institutional record access requires explicit authority/content bindings. Dialogue generation may only project the ledger and cannot create facts. Mass broadcast/rumor propagation needs a scalable event-scheduling contract before use across large populations.

PTU/Caelo/Kairos do not supply the confidence heuristic used here. It is versioned Ouros simulation policy and must remain separate from adopted tactical rules.
