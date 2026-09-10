# Global NPC AI Readiness Snapshot — Pass 399

Status: IMPLEMENTED ON PASS BRANCH
Date: 2026-09-10
Canon changes: NONE

## Slice completed

Pass 399 connects the holder-transition owner selected by `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V3` to post-restore resource reconciliation.

`tools/world_resource_history_reconciliation.py` now accepts restored holder-transition evidence and an explicit set of resource ids whose holder history has been audited complete. Complete evidence can confirm a current holder relationship or prove a contradiction. Unverified coverage remains `INDETERMINATE`.

`tools/global_npc_persistent_world_post_restore.py` now requires the holder-transition owner when a V3 manifest selected one, checks its semantic minute and rejects an unselected holder owner on legacy recovery.

`tools/resource_holder_transition_checkpoint.py` now rejects transition records later than the checkpoint semantic cut.

Executable regressions were added to:

`tests/test_world_resource_history_reconciliation.py`
`tests/test_global_npc_persistent_world_post_restore.py`
`tests/test_global_npc_resource_holder_transition_checkpoint.py`

Contract:

`design/holder-journal-post-restore-reconciliation-contract-pass-399.md`

Research and narrative candidate:

`research/2026-09-10-holder-journal-optional-route-continuity-scan-399.md`
`proposals/2026-09-10-the-survey-trail-nobody-took-pass-399.md`

## Holder-history readiness boundary

Repository call-site audit found ordinary checkout and return routed through dedicated holder-aware wrappers, plus a holder-aware authorized-handoff wrapper.

One current production path still prevents a universal completeness claim: `tools/global_npc_resource_handoff_rescheduling.py::execute_current_authorized_handoff()` calls the lower-level `execute_authorized_handoff()` directly after authorization-state checks.

Pass 399 therefore does not infer completeness from the mere existence of a holder checkpoint. `complete_holder_history_resource_ids` must represent separately audited coverage. This keeps a valid but incomplete event journal from turning legitimate uncertainty into false corruption.

## Recovery boundary after Pass 399

V3 now has a coherent path from generation selection to holder-aware post-restore validation:

manifest selection -> independent owner restore -> semantic-minute check -> cross-owner reconciliation -> activation gate.

A demonstrated holder contradiction blocks activation only when the relevant resource history is explicitly audited complete. Missing coverage remains visible and activatable as `INDETERMINATE`.

The holder-transition checkpoint also enforces `transition.at_tick <= checkpoint.semantic_minute`.

## Live engine evidence

Read-only AutoPTU-Java head inspected: `d809490e15ef77afeaf3fd6ed32ac6d70638f166`, merge PR #424, `Freeze switch entry state prefix`.

The new Java seam freezes pre-entry temporary-effect state for a successful switch, including release/joined-round markers before later Feature or Ability hooks. Its source explicitly leaves field presence and active-affiliation mutation outside the new plan until a first-class off-field placement store exists.

This strengthens only that switch-entry prefix. It does not verify complete switching, complete movement, the full action economy, the full turn/round lifecycle, Abilities or Trainer Features as families.

Read-only AutoPTU Python remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its newest commit remains presentation-only viewport-coordinate synchronization, with no battle-rule or outcome change.

## Permanent capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL as a family; audited primitives remain verified.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: individually gated.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only in ordinary audited scopes.

AI tactical policy: BLOCKING for survey-first, rescue-first, protect-object, escort, objective-aware withdrawal and disengage-after-objective policies.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for stable world-resource interaction, environmental objective state, authoritative acknowledgement and non-KO completion.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked as a routing aid only. This pass grants no survey Skill check, utility-class Feature, weather rule, terrain effect, Item effect, carrying rule or reaction.

## Narrative progress

`The Survey Trail Nobody Took` demonstrates a persistent optional hook that can remain causally real after the player ignores it. A named NPC expedition may attempt it, an environmental revision may alter the route, and an old observation may later become valuable. The reduced form runs without AutoPTU; the rich form exposes every tactical dependency instead of pushing missing rules into Minecraft.

## Next highest-value seams

First, close or journal-wrap the rescheduled-handoff mutation path and continue the holder mutation audit. Only then can broader resource classes receive automatic completeness guarantees.

Second, stable AutoPTU battle/session identity and crash recovery remain unresolved. The persistent world still needs a way to recover an in-flight tactical session without inferring its result from Minecraft presentation or later world state.