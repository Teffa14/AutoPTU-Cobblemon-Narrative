# Engine readiness snapshot — Pass 273

Status: evidence snapshot for narrative dependency gating. AutoPTU-Java and AutoPTU were inspected read-only; this pass changes only the narrative repository.

Read-only heads inspected: AutoPTU-Java `820ef88acbb982243588dc7efd3bc21e79f2177b`, merge PR #353 “Bridge POST_DAMAGE into move-special target transport”; AutoPTU Python `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, presentation-only viewport synchronization.

Conservative classification remains unchanged: targeting/footprints/range/LoS VERIFIED within audited contracts; base movement legality VERIFIED; complete movement PARTIAL; core calculations VERIFIED; action economy/initiative VERIFIED; full turn/round lifecycle PARTIAL; full stateful damage pipeline PARTIAL; status lifecycle PARTIAL; terrain/weather/hazards/zones/reactions MIXED/PARTIAL/BLOCKING; move-specific behavior PARTIAL; abilities PARTIAL; items PARTIAL; Trainer Features/perks PARTIAL; AI legal-action infrastructure VERIFIED; AI tactical policy BLOCKING; Minecraft/Cobblemon/Craftics adapter/playback support PARTIAL/BLOCKING end-to-end.

Java PR #353 adds a package-private bridge from resolved `RuntimeMoveSpecialPostDamageApplication.Result` into the canonical `MoveSpecialTargetResult`, preserving the action result, immutable post-damage result snapshot and damage dealt. Its regression checks that later mutation of the original snapshot does not alter the transported target result. This is useful narrow evidence for POST_DAMAGE move-special target transport. It does not verify the full stateful damage pipeline, full turn/round lifecycle, all move-specific behavior, status lifecycle, complete movement, terrain/weather/hazards/zones/reactions, tactical AI, or a public typed AutoPTU-to-Ouros semantic-result export API.

AutoPTU Python has no newer mechanical evidence. Its current head explicitly states that its viewport synchronization change is presentation-only and changes no battle rules or outcomes.

Pass 273’s reduced regime-transition investigation requires no tactical AutoPTU capability. It depends on Ouros persistence, Pass 261 semantic horizons, Pass 271 controlled comparison/detectability, Pass 272 recovery trajectories, evidence provenance and an adapter that preserves the difference between world presentation and ecological authority.

For a mechanically rich version, dependencies remain exact. Tactical detection/selection uses targeting/footprints/range/LoS. Ordinary traversal uses base movement legality. Push/pull/knockback/interception/forced movement uses complete movement. Adopted PTU arithmetic uses core calculations. Structured sequencing uses action economy/initiative and full turn/round lifecycle where state spans phases. Persistent damage requires full stateful damage pipeline. Persistent statuses require status lifecycle. Admitted tactical environmental effects use terrain/weather/hazards/zones/reactions. Exact Moves, Abilities, Items and Trainer Features/perks require their own verified paths. AI legal-action infrastructure can enumerate legal choices; autonomous avoidance, contest, reroute or intervention behavior requires AI tactical policy. Minecraft/Cobblemon/Craftics adapter/playback support is required for live projection and semantic feedback.

No ecological threshold, feedback, regime-transition or hysteresis evidence can promote a Minecraft block pattern into cover, hazard, zone, reaction, forced movement, weather phase, delayed effect, damage, status, Ability trigger, Item effect or Trainer Feature interrupt.

Caelo/Kairos remain comparative sources under existing source-authority policy. No new Caelo rule was found or adopted in Pass 273.
