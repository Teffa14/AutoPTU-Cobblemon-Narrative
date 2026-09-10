# Global NPC AI Readiness Snapshot — Pass 398

Status: IMPLEMENTED ON PASS BRANCH
Date: 2026-09-10
Canon changes: NONE

## Slice completed

Pass 398 upgrades persistent-world generation selection to `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V3`.

The new generation binds four independently validated owners at one semantic minute: global NPC state, persistent world evidence, current world-resource catalog and the Pass 397 holder-transition checkpoint.

Legacy V1 and V2 manifests remain readable. Neither legacy path fabricates resource or holder-history state that its original generation did not select.

Files changed by the executable seam:

`tools/persistent_world_recovery_manifest.py`
`tests/test_persistent_world_recovery_manifest.py`
`design/persistent-world-recovery-manifest-v3-contract-pass-398.md`

Research and narrative candidate:

`research/2026-09-10-four-owner-recovery-courier-escalation-scan-398.md`
`proposals/2026-09-10-the-delivery-that-changed-hands-pass-398.md`

## Recovery boundary after Pass 398

Generation selection now has a stable digest for the holder-history owner. The manifest still does not merge owner payloads or assert that the holder journal is complete for mutation paths that have not been audited.

Pass 395 post-restore gating therefore must not yet convert every current-holder disagreement into a hard conflict. The next executable seam should pass a successfully restored `ResourceHolderTransitionLedger` into the Pass 394 reconciliation layer and strengthen only cases the journal can genuinely prove.

## Engine capability evidence

Read-only AutoPTU-Java head inspected: `ca235409e6d317055ae4afd9008bd82156b739f7`, merge #423.

That merge adds/fixes a narrow authoritative switch-transition plan with parity coverage. It does not complete switching, complete movement, action economy, lifecycle or Abilities as families.

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The newest commit remains presentation-only.

Capability posture remains conservative: targeting/footprints/range/LoS, base movement legality and core calculations are VERIFIED only in audited scopes; action economy/initiative has verified primitives but remains incomplete as a family; complete movement, full turn/round lifecycle, full stateful damage pipeline and status lifecycle remain PARTIAL; terrain/weather/hazards/zones/reactions remains MIXED/PARTIAL/BLOCKING by mechanism; move behavior, Abilities, Items and Trainer Features remain individually gated; ordinary AI legal-action infrastructure has audited verified scopes; AI tactical policy remains BLOCKING for objective-aware rescue/custody tactics; Minecraft/Cobblemon/Craftics remains PARTIAL/BLOCKING for authoritative world-object handoff and non-KO objective playback.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked as a router only. No delivery, custody, rescue, weather, Item or Trainer Feature rule is granted by this pass.

## Next highest-value seam

Use the restored holder-transition ledger as optional evidence in `world_resource_history_reconciliation.py` and the Pass 395 post-restore activation gate. Add regressions proving that complete journal evidence can produce `CONFIRMED` or `CONFLICT`, while missing or unaudited history remains `INDETERMINATE`.

Stable AutoPTU battle/session identity and crash recovery remain a separate unresolved integration problem.
