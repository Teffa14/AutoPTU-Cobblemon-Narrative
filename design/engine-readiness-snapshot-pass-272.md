# Engine readiness snapshot — Pass 272

Status: evidence snapshot for narrative dependency gating. This document does not modify AutoPTU-Java or AutoPTU and does not promote a capability family from representative mechanics.

Read-only heads inspected: AutoPTU-Java `2de76ca7f804b3b52f74bfe01aa09c816bbefd91` (merge PR #352, preserve move-special target transport across event composition). AutoPTU Python `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

Conservative classification remains: targeting/footprints/range/LoS VERIFIED within audited contracts; base movement legality VERIFIED; complete movement PARTIAL; core calculations VERIFIED; action economy/initiative VERIFIED; full turn/round lifecycle PARTIAL; full stateful damage pipeline PARTIAL; status lifecycle PARTIAL; terrain/weather/hazards/zones/reactions MIXED/PARTIAL/BLOCKING; move-specific behavior PARTIAL; abilities PARTIAL; items PARTIAL; Trainer Features/perks PARTIAL; AI legal-action infrastructure VERIFIED; AI tactical policy BLOCKING; Minecraft/Cobblemon/Craftics adapter/playback support PARTIAL/BLOCKING end-to-end.

Java PR #352 is narrow evidence that `MoveSpecialTargetResult` can replace its adapter-facing `AppliedActionResult` while preserving post-damage snapshot and damage bookkeeping through later event composition, with a regression covering that recomposition path. This strengthens move-special target transport/event composition only. It does not establish full turn/round lifecycle, complete move-specific behavior, complete movement, status lifecycle, terrain/weather/hazards/zones/reactions, tactical AI, or a public typed AutoPTU-to-Ouros semantic-result export API.

AutoPTU Python has no new mechanical evidence in this pass; its current head explicitly describes its change as presentation only.

Pass 272 reduced recovery investigation requires no AutoPTU tactical family. It requires Ouros persistence, semantic time/horizons, controlled-comparison and observation provenance, and an adapter that does not confuse Minecraft visibility/runtime lifecycle with ecological state.

For a mechanically rich recovery scene the dependency mapping remains exact: targeting/footprints/range/LoS for active tactical detection; base movement legality for ordinary movement; complete movement for push/pull/knockback/interception/forced movement; core calculations for adopted PTU arithmetic; action economy/initiative and full turn/round lifecycle for structured sequencing; full stateful damage pipeline for persistent damage; status lifecycle for persistent statuses; terrain/weather/hazards/zones/reactions for admitted tactical environmental effects; move-specific behavior, abilities, items, and Trainer Features/perks only when those exact mechanisms participate; AI legal-action infrastructure for legal autonomous actions; AI tactical policy for autonomous return/avoidance/contest/reroute decisions; Minecraft/Cobblemon/Craftics adapter/playback support for live projection and semantic feedback.

No recovery observation can be used to infer reaction, interception, forced movement, weather phase, delayed effect, damage, status, Ability trigger, Item effect, Trainer Feature interrupt, or another unverified mechanic.

Caelo/Kairos remain comparative sources under existing source-authority policy. No new Caelo rule was found or adopted in Pass 272.