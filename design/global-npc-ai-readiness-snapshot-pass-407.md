# Global NPC AI Readiness Snapshot — Pass 407

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE

Pass 407 upgrades persistent-world generation selection to `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V4`.

V4 selects one exact generation of five owners at one semantic minute: global NPC state, persistent-world evidence, current `WorldResource` catalog, resource-holder transition history, and persisted holder-history coverage baselines. The manifest verifies each owner digest and its own SHA-256. A valid baseline checkpoint from the wrong generation is rejected even when its semantic minute matches.

Legacy V1, V2 and V3 manifests remain readable. None fabricates newer owners. A V3 recovery path rejects an independently supplied baseline checkpoint because V3 never selected that evidence.

The bounded-history authority rule remains unchanged. A restored baseline certifies only its recorded starting cut and can support continuity after that cut. V4 selection does not make pre-baseline history complete and does not allow a baseline to prove the catalog generation that caused its original issuance.

Research added two source anchors not previously present in the repository: the 2026 Pokémon Resonance development brief describing community notice-board jobs as local worldbuilding, and the public Pokémon Last Chance listing describing side quests and choices across competing factions. Their structures were transformed into the proposed `The Job Everyone Needs Done`, where several institutions share a practical local problem but later consequences follow from actual work, evidence, custody, access and communications instead of an omniscient faction score.

PTU/Caelo/Kairos remains reference-only. No Skill, Edge, Feature, Move, Ability, Item, faction bonus, reputation mechanic, hazard, terrain or weather rule is granted by this pass.

Live engine evidence inspected on 2026-09-10: AutoPTU-Java `main` is `0b03b2716141fe94c2fbf85fdca1ba4548d080a2`, merge PR #430, `Add reusable Ball Fetch approach Shift resolver`. The new resolver applies the pinned Ball Fetch approach policy over ordinary legal Shift destinations and deterministic tie-breaking. This strengthens one narrow movement/Ability interaction. It does not complete movement, forced movement, interception, switching, the abilities family, action economy, lifecycle or AI tactical policy. AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7` with presentation-only latest changes.

Capability status for the new encounter concept remains conservative. Targeting/footprints/range/LoS: VERIFIED only in audited scopes. Base movement legality: VERIFIED only in audited scopes. Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Core calculations: VERIFIED only in audited scopes. Action economy/initiative: PARTIAL. Full turn/round lifecycle: PARTIAL. Full stateful damage pipeline: PARTIAL. Status lifecycle: PARTIAL. Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact mechanism. Move-specific behavior: individually gated. Abilities: individually gated. Items: individually gated. Trainer Features/perks: individually gated. AI legal-action infrastructure: verified only for audited ordinary scopes. AI tactical policy: BLOCKING for objective-aware repair/rescue/preservation behavior. Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative job objective state, resource interaction and non-KO completion.

Next recovery seam: restore the V4-selected baseline owner and feed those certificates into bounded holder-history reconciliation only after each certificate cut, with explicit cross-owner chronology against the restored transition journal.

Independent high-impact blocker: stable AutoPTU battle/session identity and authoritative recovery of an in-flight tactical resolution after crash/restart.
