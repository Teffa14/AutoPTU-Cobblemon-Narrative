# Global NPC AI Readiness Snapshot — Pass 413

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE
Date: 2026-09-10

## Slice completed

Pass 413 adds one exact post-restore boundary between `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V5`, the global NPC checkpoint selected by that manifest, and `OUROS_AUTOPTU_SESSION_CHECKPOINT_V1`.

`tools/persistent_world_v5_autoptu_session_recovery.py` validates the complete V5 generation before agent/session content can affect recovery. Persistent agents are then reconstructed from the selected global NPC checkpoint and reconciled against the selected session ledger through the existing Pass 411 identity rules.

A valid same-minute global checkpoint or session checkpoint from another generation is rejected at the manifest boundary. V4 cannot enter this helper because V4 never selected a tactical-session owner.

Unresolved `ENGINE_BOUND` sessions remain explicit unresolved work. This pass does not infer battle completion, release agents, resume tactical state or treat presentation as battle authority.

## Research and narrative progress

New source anchors for this corpus are Lethalmon's public project material and Cryptochrome's Pokémon Knowledge release thread.

Lethalmon contributes the high-level sortie/return structure: a bounded expedition can produce value before an entire environment is exhausted. Pokémon Knowledge contributes variable-order lead pursuit and inspectable environments with relatively little mandatory Trainer combat.

New proposal: `The Leads Do Not Wait`, status PROPOSED / NON-CANON. One incident can produce several attributed leads while semantic time keeps moving. The player may pursue one and persistent named NPCs may pursue others only when they actually know the lead, receive the obligation, have time/access and can travel there. Unvisited leads do not retroactively produce observations.

The reduced version runs through existing world-agent, travel, knowledge, communication, provenance and site-revision systems. A richer tactical version remains capability-gated.

No source plot, character, dialogue, faction, map, puzzle, economy or distinctive implementation was copied.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked as a routing aid. Campaign/session, encounter, movement, hazard, terrain/weather, Item and Feature material still requires exact source validation before mechanics are admitted.

No Skill DC, Move behavior, Ability effect, Item effect, Trainer Feature, forced movement, hazard, reaction, weather rule or special objective completion rule is granted by this pass.

## Live engine evidence

AutoPTU-Java head is now `b0563ab0c0998648a93d3e4daf52fb7734c81fd0`, merge PR #435, `Synchronize replacement tactical position during switch`, dated 2026-09-10.

The audited change makes `CombatantSwitchExecutor` synchronize the replacement combatant's server-owned runtime position to the validated switch destination before post-entry effects/hooks. Its regression also verifies that failed field-presence validation leaves the runtime position unchanged.

This strengthens one concrete switching/base-position synchronization seam. It does not promote complete movement, action economy, initiative, lifecycle, damage/status pipelines, hazards/zones/reactions, Abilities or Trainer Features as complete families.

AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The latest change remains explicitly presentation-only viewport coordinate synchronization.

Both engine repositories remained read-only.

## Capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes. PR #435 strengthens switch destination materialization but does not expand this into complete movement.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: PARTIAL / individually gated.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for audited ordinary scopes. Tactical investigate/retrieve/escort/protect/extract interactions need explicit admission.

AI tactical policy: BLOCKING for evidence-first, escort-first, protect-observer, extraction and objective-aware withdrawal/disengagement unless separately verified.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for authoritative tactical objective state, non-KO completion, specialized interactables and in-flight battle recovery.

## Current recovery boundary

Ouros can now prove that a persistent NPC AutoPTU reference and its Ouros-side session identity came from the exact same V5 recovery generation before identity reconciliation occurs.

The remaining external seam is authoritative engine reconciliation. Given a durable `engine_session_ref`, Ouros still needs a verified AutoPTU-side authority capable of distinguishing an active session, a completed session with a verifiable result, an unknown/unrecoverable session, and an explicitly authorized abandonment transition. Until that exists, unresolved tactical ownership stays unresolved.
