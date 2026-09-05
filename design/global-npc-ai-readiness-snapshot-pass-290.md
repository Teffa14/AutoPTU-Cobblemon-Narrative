# Global NPC AI readiness snapshot — Pass 290

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

This file records dependency evidence for narrative concepts added in Pass 290. It does not promote an engine capability family because one representative mechanic or generic hook exists.

## Read-only engine heads checked

AutoPTU-Java: `c24a287bbb41aa5fa712f4f465de7390d88c6f78`

Latest inspected change: `Add generic TURN_END effect registry (#367)`. It adds an ordered server-authoritative TURN_END registry, actor/global scopes, a lifecycle adapter, stable roster traversal for global registrations, duplicate-ID rejection and tests for hook ordering. The built-in registry is an infrastructure boundary; it does not itself prove coverage for every Move, Ability, Item, status, terrain rule or Trainer Feature that may execute there.

AutoPTU Python: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Latest commit remains presentation-only and explicitly states that battle rules/outcomes do not change.

## Permanent capability categories

| Capability family | Pass 290 status | Live-evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Existing audited core contracts cover the base family used by current narrative dependency mapping. No Pass 290 change. |
| base movement legality | VERIFIED | Existing audited base movement contract remains sufficient for basic structured movement. No Pass 290 change. |
| complete movement: push / pull / knockback / interception / forced movement | PARTIAL | Representative movement interactions exist, but full family parity is not established. |
| core calculations | VERIFIED | Existing audited deterministic calculation contracts remain verified. |
| action economy / initiative | VERIFIED | Existing audited primitives remain verified. |
| full turn / round lifecycle | PARTIAL | Java now has more declarative lifecycle seams, including generic TURN_END registration, but complete phase/round behavior across all owners is not proven. |
| full stateful damage pipeline | PARTIAL | Server-owned damage seams exist; complete stateful parity across all damage families remains unverified. |
| status lifecycle | PARTIAL | Temporary-effect/status hooks cover selected cases; complete status lifecycle remains unverified. |
| terrain / weather / hazards / zones / reactions | MIXED / PARTIAL / BLOCKING | Individual mechanics and seams exist unevenly; no complete family contract exists. |
| move-specific behavior | PARTIAL | Representative Moves exist; breadth and lifecycle interactions remain incomplete. |
| abilities | PARTIAL | Ability-phase traversal and selected effects exist; full Ability corpus and all triggers are not verified. |
| items | PARTIAL | Selected item rules exist; full corpus and lifecycle interactions are incomplete. |
| Trainer Features / perks | PARTIAL | Selected Trainer mechanics exist; complete feature/interrupt coverage is not verified. |
| AI legal-action infrastructure | VERIFIED | Existing audited legality infrastructure remains verified. |
| AI tactical policy | BLOCKING | No evidence promotes autonomous tactical policy to complete. Narrative AI must continue explicit AutoPTU handoff. |
| Minecraft / Cobblemon / Craftics adapter / playback | PARTIAL / BLOCKING end-to-end | Presentation and adapter seams exist, but full authoritative request/result/ack playback remains incomplete. |

## Pass 290 dependency interpretation

The publication-revision delivery runtime itself requires none of the tactical capability families. It operates in semantic world state through publication lineage, bounded audience expansion, information delivery, memory and selective replanning.

A reduced Correction Race adventure therefore remains runnable while tactical gaps exist.

A full encounter inherits exact dependencies from the selected scene mechanics. Knockback or interception requires complete movement. Weather/hazard pressure requires terrain/weather/hazards/zones/reactions. Delayed or phase-sensitive effects require the relevant lifecycle/status owner family. Move, Ability, Item and Trainer Feature behavior each require their own family. Autonomous combat choice remains blocked by AI tactical policy. Full visible execution remains dependent on Minecraft/Cobblemon/Craftics adapter/playback.

## Unresolved engine questions relevant to this narrative slice

- Can a future structured encounter preserve a world-event causal reference through AutoPTU request, resolution and return?
- Is local adapter acknowledgement durable across restart, or only in-process?
- Which lifecycle families will register through the generic TURN_END boundary first, and what parity tests prove each owner?
- How will AI tactical policy expose explanation/provenance so a world consequence can distinguish a legal option from the policy that selected it?

None of these questions blocks the reduced information-history loop.
