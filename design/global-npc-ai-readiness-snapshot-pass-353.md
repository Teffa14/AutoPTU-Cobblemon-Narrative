# Global NPC AI readiness snapshot — Pass 353

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-08

## Read-only engine heads inspected

AutoPTU-Java: `4da4c077840513ce666d1675bd6a6e9edd6ddd3e`, merge of PR #403, `Execute Arena Trap through round-start ability registry`.

AutoPTU Python: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, presentation-only viewport-coordinate synchronization; the commit message states that battle rules and outcomes do not change.

## New Java evidence in PR #403

`RoundStartAbilityEffectRegistry` now registers Arena Trap in the server-owned Python-parity built-ins when a `RoundStartAbilityExecutionContext` is supplied. The handler resolves active Arena Trap holders from authoritative battle state, projects candidates from battle state plus canonical rule content, applies the existing targeting contract, converts targets into the already-frozen status instructions and applies them through `StatusEffectMutationExecutor`.

`RoundStartArenaTrapHandlerOracleParityTest` is added and the relevant parity workflow gates it.

This is stronger evidence than Pass 352 because the previously separate Arena Trap seams now execute through the round-start ability registry. It still proves one audited Ability path, not the entire Ability family or the entire lifecycle engine.

## Permanent capability categories

Targeting / footprints / range / LoS: VERIFIED within the previously audited ordinary scope. Arena Trap now has an integrated authoritative targeting path, but that representative Ability does not broaden the category beyond tested contracts.

Base movement legality: VERIFIED within the audited ordinary scope.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. No new evidence in PR #403 completes carrying, interception or forced-movement interactions.

Core calculations: VERIFIED within the audited deterministic arithmetic scope.

Action economy / initiative: VERIFIED for audited primitives. Tactical cargo pickup/drop/handoff remains individually gated.

Full turn/round lifecycle: PARTIAL, strengthened narrowly. PR #403 proves Arena Trap dispatch through a round-start registry path, but does not establish every phase, trigger ordering family, cleanup or round transition.

Full stateful damage pipeline: PARTIAL. No promotion from this slice.

Status lifecycle: PARTIAL. Arena Trap applies its planned Slowed status through authoritative state, but full expiration/cleanup and all consumers of that state still require evidence.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact family. Arena Trap does not promote these systems.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL and individually gated. Arena Trap now has target projection, effect planning, authoritative status mutation and round-start registry execution under parity tests. One completed path does not establish the family.

Items: PARTIAL and individually gated.

Trainer Features/perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED within its audited ordinary scope.

AI tactical policy: BLOCKING for delivery-first, protect-carrier, escort, intercept-to-inform, preserve-resource and disengage-after-objective priorities.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING end-to-end. PR #403 keeps Arena Trap resolution server-owned; it does not prove complete client playback/acknowledgement.

## Pass 353 narrative dependency

The reduced `The Obligation After the Handover` case requires no AutoPTU combat capability. Its persistent reservation/request premise belongs to world-agent state.

The richer transport encounter must use the exact gates above. In particular, carrying/interception cannot be inferred from base movement; a round deadline cannot be inferred from the Arena Trap round-start handler; and Slowed application cannot be treated as evidence of complete status lifecycle.

## Mechanical questions still open

- complete Slowed expiration/cleanup evidence for Arena Trap;
- whether every movement path consumes restored Slowed state consistently;
- objective-aware tactical policy for escort/cargo/interception;
- explicit legal actions for tactical pickup/drop/handoff;
- complete Minecraft/Cobblemon/Craftics playback acknowledgement for these events;
- broader Ability, Move, Item and Trainer Feature family coverage beyond representative slices.

## World-simulation questions exposed by Pass 353

- when to advance the global atomic checkpoint from V5 to include the resource checkpoint bundle;
- which Pass 343–352 ledgers enter the next resource schema and what cross-reference validation each requires;
- how to preserve backward compatibility for older checkpoints without fabricating resource history;
- whether long resource histories need compaction while retaining authoritative provenance.
