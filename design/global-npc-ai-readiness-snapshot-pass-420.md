# Global NPC AI readiness snapshot — Pass 420

Status: IMPLEMENTED NARRATIVE-REPO SLICE / NON-CANON CONTENT

Repository baseline

Pass 420 starts from narrative main `d2a27beb27bd11e1ad0133f21bba33424e3dd11a` after Pass 419. The recursive repository tree was inventoried before writing. Current focus, canon governance, the Pass 418–419 consequence/observation chain, existing private information delivery and knowledge ledgers, disclosure-access coverage, recent research/proposals and the PTU/Caelo/Kairos source router were reviewed. Canon files were left unchanged. AutoPTU-Java and AutoPTU were inspected read-only.

Implemented seam

`tools/autoptu_world_observation_delivery.py` connects one committed `WorldObservationRecord` to the existing global NPC information queue.

The seam requires an explicit custodian, explicit recipient, explicit channel, explicit source/receiver claim identities, explicit delivery event and message identities, and a semantic creation minute. It materializes the observation as an `INSTITUTIONAL_RECORD` in the custodian's private knowledge ledger and schedules an ordinary information envelope to the one named recipient.

The source claim uses the observation transaction ID as its provenance root. Successful ordinary delivery preserves that root in the recipient's `REPORT` claim. The returned scheduling record also retains the observation's upstream provenance reference.

Shared faction or institutional membership does not expand the audience. Before the event is due, the recipient remains uninformed. Channel failure or unacknowledged local projection does not create knowledge.

Exact replay is idempotent before and after terminal delivery. Reusing an event identity with different envelope content fails closed. Reusing the source claim identity for another observation fails through the existing claim collision guard.

Regression

`tests/test_global_npc_autoptu_world_observation_delivery.py` covers one-custodian/one-recipient transfer, latency, recipient isolation, replay before and after delivery, conflicting event reuse, missing identities and conflicting observation claim reuse.

Research and proposal

Research: `research/2026-09-11-explicit-observation-delivery-stale-team-scan-420.md`

Proposal: `proposals/2026-09-11-the-second-team-left-before-the-warning-arrived-420.md`

Both remain outside canon.

New public sources

Pokémon Space Pog Jam, itch.io project page by BoogerFace. Reusable high-level structure: an exploration assignment can become an escape problem, and information discovered during the incident can matter to people outside the immediate scene.

Antura Discover Quest Design developer documentation. Reusable high-level structure: separate content/knowledge units, quest logic and scene implementation so displayed world state does not imply universal character knowledge.

No characters, plots, dialogue, locations, puzzles, layouts or distinctive content were imported.

Live AutoPTU-Java evidence

Inspected main: `494430a5e602652e21cf90dc3ae6f3e8ffef2cf6`, merge PR #441, `Freeze replacement initiative insertion oracle`, committed September 11, 2026 UTC.

This strengthens one bounded replacement-initiative seam. Action economy/initiative remains PARTIAL because the oracle does not establish the entire family.

Live AutoPTU evidence

Inspected main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its newest change remains explicitly presentation-only viewport-coordinate synchronization with no battle-rule or outcome change.

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
AI tactical policy: BLOCKING for specialized rescue, warning-aware withdrawal, protect-observer and objective-aware disengagement policies.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative tactical objectives and in-flight recovery.

PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing aid toward combat, movement/terrain, status, hazards/weather, encounter construction, Items and related source material. Its page references are not Ouros acceptance. Pass 420 adds no PTU/Caelo mechanic.

Next implementation seam

Connect the successful AutoPTU-derived observation delivery into the existing delivery-to-replanning coordinator and prove that only the explicit receiver can wake and reconsider an agenda. Failed, queued or unacknowledged delivery must not wake the actor. The integration must keep the same provenance root and must not re-read the original tactical payload.

Separate unresolved paths

Engine authority `UNKNOWN` and `EXPLICITLY_ABANDONED` still require separate durable policies. Persistent Injury/status consequences remain deferred until their producing AutoPTU paths are sufficiently verified.