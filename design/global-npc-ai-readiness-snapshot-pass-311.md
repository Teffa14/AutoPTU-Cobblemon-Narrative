# Global NPC AI readiness snapshot — pass 311

Status: DESIGN EVIDENCE / NOT CANON
Date: 2026-09-06

Pass 311 adds a durable explicit review event for assessment-dependent decisions. The review runtime itself requires no AutoPTU combat capability.

Read-only engine evidence checked during this pass:

AutoPTU-Java main: `0dff216a145c15d0d74fbe970b1b3be55b2299c1`, commit `Wire Psionic Overload TURN_END tick (#382)`, dated 2026-09-06. The commit wires one Trainer Feature effect into the TURN_END registry, uses the existing Tick resolver and ordinary-damage ingress, emits a TrainerFeatureEvent, and gates that seam against a pinned Python oracle. This is meaningful evidence for one lifecycle/Trainer Feature/status interaction. It does not establish complete turn/round lifecycle, complete Trainer Feature coverage, complete status lifecycle, or the full stateful damage pipeline.

AutoPTU Python main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, commit `Career: keep battle coordinates synced after viewport resize (#237)`, dated 2026-08-29. The commit explicitly states presentation-only behavior with no battle-rule or outcome changes.

Capability classification from live evidence:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL; Psionic Overload adds one verified TURN_END representative seam only;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by subfamily;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL; Psionic Overload TURN_END is verified but not representative of the whole family;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for general autonomous tactical choice;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end.

No capability category is promoted in Pass 311.

`The Order Under Review` has a reduced version requiring no tactical battle capability. Its full damaged-span inspection depends specifically on complete movement for wind/forced movement/interception, lifecycle for timed structural events, stateful damage for environmental injury, status lifecycle for persistent conditions, and terrain/weather/hazards/zones/reactions for unstable surfaces and rescue. Move, Ability, Item and Trainer Feature dependencies apply only when authored explicitly. AI tactical policy remains blocking for general autonomous rescue behavior, and visible end-to-end execution remains constrained by adapter/playback support.

PTU/Caelo/Kairos authority remains unchanged. Public references contribute narrative and investigation structures only; no new rules overlay is activated.
