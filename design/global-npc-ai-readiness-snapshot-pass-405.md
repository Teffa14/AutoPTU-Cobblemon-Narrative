# Global NPC AI Readiness Snapshot — Pass 405

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE

Pass 405 moves holder-history baseline issuance to the correct side of the recovery boundary.

`validate_persistent_world_post_restore()` no longer accepts caller-authored bounded baseline objects. A V3 recovery caller may supply the exact raw WorldResource catalog checkpoint selected by the outer manifest. The activation stage validates its integrity, semantic cut, manifest digest and equality with the restored catalog. Historical reconciliation runs before new baselines are emitted.

The ordering matters. A baseline derived from the catalog at semantic minute T cannot be used to prove that same catalog at T. It begins a future bounded continuity interval only after the current recovery cut has passed existing cross-owner validation.

`PersistentWorldPostRestoreValidation` now returns any newly issued baselines explicitly. If the caller lacks the raw selected checkpoint, conservative V3 reconciliation still works and returns no new certificates.

The new regression file tests exact-generation binding, same-minute generation mismatch, outer-manifest digest mismatch, non-retroactive treatment of older holder events and conservative operation without raw checkpoint retention.

Narrative research added two source anchors not previously processed in these exact forms: the public Pokémon Rejuvenation `Prince from the Sands` quest page and Pokémon Sacred Phoenix's public project page. The extracted pattern is that earlier known conduct can change later friction and available responses without erasing the later physical problem.

`The Detour They Offer If They Trust You` is PROPOSED / NON-CANON. A legitimate route closure can produce waiting, supervised access, a disclosed provisional detour or extra verification depending on provenance-backed information actually available to the responsible NPC. No global morality flag or omniscient reputation state is required.

PTU/Caelo/Kairos remains a reference boundary only. The source index points toward Skills/Edges/Features, Researcher, Chronicler, Survivalist, Topographer, movement/terrain, hazards, encounter design, rivals and Items/Gear, but Pass 405 grants none of those mechanics.

Live AutoPTU-Java evidence advanced to `a27a27cb542f1b979b19abae4138261f322ca10e`, merge #428, `Freeze pinned switch post-entry call contract`. The pinned post-entry family order is now represented for Ball Fetch, Curious Medicine, replacement initiative insertion, First Blood and Quick Switch. This is evidence for that exact call-order contract, not proof that switching, Abilities, Trainer Features, initiative or lifecycle are complete.

AutoPTU Python remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its latest change is presentation-only.

Capability status for the full proposal remains conservative. Targeting/footprints/range/LoS, base movement legality and core calculations are verified only in previously audited scopes. Action economy/initiative is partial overall. Complete movement is partial. Full turn/round lifecycle, full stateful damage pipeline and status lifecycle are partial. Terrain/weather/hazards/zones/reactions is mixed/partial/blocking by exact mechanism. Move-specific behavior, Abilities, Items and Trainer Features/perks remain individually gated. AI legal-action infrastructure is verified only in ordinary audited scopes. AI tactical policy is blocking for traversal-first, protect-inspector, rescue-first, preserve-infrastructure, escort, objective-aware withdrawal and disengage-after-objective. Minecraft/Cobblemon/Craftics remains partial/blocking for authoritative closure state, conditional route disclosure, persistent objectives and non-KO completion playback.

The next holder-history seam is persisting the newly issued recovery baseline as the start of a future demonstrably covered interval across later checkpoints. Stable AutoPTU battle/session identity and authoritative recovery of in-flight tactical resolution remain the larger independent blocker.
