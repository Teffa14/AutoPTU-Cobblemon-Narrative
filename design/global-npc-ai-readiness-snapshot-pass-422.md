# Global NPC AI readiness snapshot — Pass 422

Status: IMPLEMENTED NARRATIVE-REPO SLICE / NON-CANON CONTENT

Repository baseline

Pass 422 starts from narrative main `ab17c2ad3109d7c31a76ff954793cf5cf8c8f916` after Pass 421. The recursive repository tree was inventoried before writing. Current focus, canon governance, Marea resident/institution bindings, the Pass 418–421 consequence/observation/delivery/replanning chain, global planner state, recent research/proposals and the PTU/Caelo/Kairos source router were reviewed. Canon files remain unchanged. AutoPTU-Java and AutoPTU were inspected read-only.

Implemented seam

`tools/global_npc_world_action_intent.py` adds `OUROS_WORLD_ACTION_INTENT_LEDGER_V1`.

A completed world-agent replan can now be recorded as a durable `PLANNED` world-action intent while preserving the deciding actor, selected intent, target, semantic minute, causal replan triggers, coordinator reasons and agenda source.

The ledger does not execute the action. It cannot mutate another NPC, create a commitment, deliver a message, grant a permission or resolve PTU mechanics.

Decisions with AutoPTU ownership do not enter this owner. Exact replay is idempotent; conflicting reuse of an action ID fails closed. Snapshot/restore preserves the causal record.

Regression

`tests/test_global_npc_world_action_intent.py` covers ordinary recording, exact replay, conflicting replay, AutoPTU rejection, idle rejection, trigger requirement, identity mismatch and snapshot round-trip.

Research and proposal

Research: `research/2026-09-11-independent-specialist-request-scan-422.md`

Proposal: `proposals/2026-09-11-the-person-you-ask-still-has-a-choice-422.md`

Both remain outside canon.

New public sources

Unavowed, Wadjet Eye Games, 2018. Reusable high-level structure: mission composition can change the available approach because companions contribute different capabilities, without changing the broad problem being investigated.

Invisible, Inc., Klei Entertainment, 2015. Reusable high-level structure: personnel assignment interacts with travel and finite time, so selecting one person for one mission carries opportunity cost elsewhere.

No characters, plots, dialogue, settings, companion powers, mission maps, tactical rules or distinctive puzzles were imported.

Live AutoPTU-Java evidence

Inspected main: `494430a5e602652e21cf90dc3ae6f3e8ffef2cf6`, merge PR #441, `Freeze replacement initiative insertion oracle`, committed September 11, 2026 UTC.

The oracle strengthens one bounded replacement-initiative seam. Action economy/initiative remains PARTIAL because the evidence does not establish the complete category.

Live AutoPTU evidence

Inspected main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit remains presentation-only viewport coordinate synchronization and explicitly states that battle rules and outcomes do not change.

Capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.
Base movement legality: VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
Core calculations: VERIFIED only in audited paths.
Action economy/initiative: PARTIAL.
Full turn/round lifecycle: PARTIAL.
Full stateful damage pipeline: PARTIAL.
Status lifecycle: PARTIAL.
Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact behavior.
Move-specific behavior: individually gated.
Abilities: PARTIAL and individually gated.
Items: individually gated.
Trainer Features/perks: individually gated.
AI legal-action infrastructure: VERIFIED only for audited ordinary actions.
AI tactical policy: BLOCKING for specialized rescue, escort, extraction, protect-carrier and objective-aware withdrawal policies.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative tactical objective state, specialized non-KO completion and in-flight recovery.

PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing aid to combat, movement/terrain, status, hazards/weather, encounter construction, Items, Trainer capabilities and living-world structure. Its references do not grant Ouros mechanics. Pass 422 adds no PTU/Caelo rule.

Next implementation seam

Turn a `PLANNED` world-action intent whose semantic kind is a request for assistance into an explicit communication intent/envelope without changing the proposed recipient's schedule. Only successful delivery should make the recipient eligible to reconsider the request. Acceptance should then create its own durable decision/commitment rather than retroactively treating the request as an assignment.

Separate unresolved paths

The V1 world-action intent ledger is not yet part of the coherent persistent-world checkpoint generation.

Engine authority `UNKNOWN` and `EXPLICITLY_ABANDONED` still require separate durable policies. Persistent Injury and Status consequences remain deferred until their producing AutoPTU paths are sufficiently verified.
