# Global NPC AI Readiness Snapshot — Pass 414

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE
Date: 2026-09-10

## Slice completed

Pass 414 adds `tools/autoptu_engine_authority_report.py`, a consumer-side evidence boundary for future post-crash AutoPTU session reconciliation.

Pass 413 already proves that one persistent NPC binding and one Ouros-side tactical-session record came from the exact V5 recovery generation. Pass 414 now validates external engine-authority claims against that restored session identity without pretending that AutoPTU currently exposes the required query API.

Supported evidence classifications are `ACTIVE`, `COMPLETED`, `UNKNOWN` and `EXPLICITLY_ABANDONED`.

A report must match the durable Ouros `session_id` and exact `engine_session_ref`, carry explicit authority/report provenance and fit inside the recovery time boundary. Completed claims require an authoritative result reference. Abandonment requires an explicit authorization reference.

The reconciler returns classification only. It does not mutate the session ledger, release agents, record a battle result, quarantine unknown sessions automatically or reconstruct tactical state.

## Research and narrative progress

New source anchors are Pokémon Diadem 2.0 and a January 2026 PokémonRMXP side-quest design discussion.

Diadem contributes the high-level structure of recurring characters pursuing goals that intersect with the protagonist without existing solely as followers. The community side-quest discussion contributes the useful timing principle that a visible world problem can exist before a quest offer, and that an optional request should support refusal rather than disguise mandatory participation.

New proposal: `The Request Did Not Create the Problem`, status PROPOSED / NON-CANON.

The proposal separates world condition, observation, information transfer, request, player commitment and later resolution. The reduced version can run on existing semantic-time, world-agent, knowledge, communication, travel, permissions and replanning systems without new AutoPTU mechanics.

No source plot, character, dialogue, location, faction, puzzle, battle system or distinctive setting element was copied.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked. Campaign/session, encounter, movement, status, hazards, weather, Items and Trainer Features remain routing references that require exact source validation before mechanics are admitted.

No Skill DC, Move behavior, Ability effect, Item effect, Trainer Feature, forced movement, hazard, reaction, weather rule or special completion rule is granted by this pass.

## Live engine evidence

AutoPTU-Java head inspected during this pass: `5ff41b03ffb960a66ecfe0b79080638ac4ac12d4`, merge PR #436, `Add generic switch post-entry dispatcher`, dated 2026-09-10.

The new Java work strengthens a concrete switch post-entry dispatch seam under pinned oracle coverage. It does not provide the durable session query/recovery authority that Pass 414's consumer contract anticipates and does not promote complete movement, lifecycle, Abilities or Trainer Features as complete families.

AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit remains explicitly presentation-only and states that battle rules/outcomes do not change.

Both engine repositories remained read-only.

## Capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

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

AI legal-action infrastructure: VERIFIED only for audited ordinary scopes. Specialized rescue, escort, retrieve, inspect, carry and interact actions need explicit admission.

AI tactical policy: BLOCKING for rescue-first, escort-first, preserve-evidence, objective-aware withdrawal and disengage-after-objective unless separately verified.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for authoritative non-KO objective state, specialized interactables, durable tactical recovery and presentation that would otherwise assert PTU truth.

## Current recovery boundary

Ouros can now represent and validate a future external statement about an unresolved engine session without conflating that statement with a Minecraft observation or immediately mutating world state.

The missing external dependency remains real AutoPTU authority output for a durable `engine_session_ref`. Until the project has a verified adapter or engine contract that produces such output, reports are a consumer-side schema and test seam only.

## Next seam

The next safe pass is to integrate a verified fixture or real adapter response into the V5 recovery path, then define audited state transitions for completed, unknown and explicitly abandoned sessions. Result payload validation must happen before a `COMPLETED` report can release world-agent tactical ownership.
