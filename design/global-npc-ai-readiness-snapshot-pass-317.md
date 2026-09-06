# Global NPC / encounter readiness snapshot — Pass 317

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-06
Scope: narrative dependency classification; AutoPTU-Java and AutoPTU inspected read-only

## Narrative slice

Pass 317 adds research and proposed design for olfactory ecology, scent-trace provenance and a non-canon investigation loop. The reduced scenario does not require a new tactical scent simulator. The full version makes every mechanically consequential dependency explicit.

## Live engine evidence

### AutoPTU-Java

Inspected head: `704722ffecbef9e003abe1870829843f29f029c7` (PR #385, `Add declarative round-window history state`).

This commit adds a server-core store for specific round-indexed histories, including Echoed Voice, Fusion Bolt and Fusion Flare, with tests and comparison against the pinned Python oracle. It is positive evidence for a reusable slice of round-history retention/pruning. It does not verify the complete turn/round lifecycle, dynamic environmental zones, delayed scent transport, statuses, reactions or general tactical policy.

### AutoPTU Python

Inspected head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

The current change remains presentation-only for this audit. No narrative dependency is promoted from it.

## Permanent capability categories

Targeting / footprints / range / LoS — VERIFIED within audited ordinary spatial contracts. Pass 317 explicitly excludes scent-based detection/targeting from this verification.

Base movement legality — VERIFIED within audited contracts. Sufficient for the reduced investigation's ordinary navigation.

Complete movement including push/pull/knockback/interception/forced movement — PARTIAL. Required only if a richer scene adds panic, rescue, machinery or forced displacement.

Core calculations — VERIFIED within audited deterministic contracts. No olfactory calculation is introduced.

Action economy / initiative — VERIFIED within audited contracts for structured tactical scenes.

Full turn/round lifecycle — PARTIAL. PR #385 strengthens a narrow round-history seam but does not establish phase-complete environmental timing.

Full stateful damage pipeline — PARTIAL. Not required by the reduced investigation; relevant only if a separate hazard causes real damage.

Status lifecycle — PARTIAL. Pass 317 introduces no new status.

Terrain / weather / hazards / zones / reactions — MIXED / PARTIAL / BLOCKING by subfamily. A dynamic odor plume, ventilation state, masking zone, weather-driven trace transport or reaction rescue would depend here.

Move-specific behavior — PARTIAL. PTU `Odor Sleuth` is directly relevant but must use exact verified semantics; one verified move cannot promote this family.

Abilities — PARTIAL. Species flavor or main-series descriptions do not prove engine Ability coverage.

Items — PARTIAL. Narrative sampling equipment can remain world props; PTU Item effects require direct verification.

Trainer Features / perks — PARTIAL. Any tracking/investigation Feature requires direct source validation.

AI legal-action infrastructure — VERIFIED within audited contracts.

AI tactical policy — BLOCKING for general autonomous tactical reasoning. No evidence supports autonomous scent-hypothesis selection, plume exploitation or general rescue policy.

Minecraft / Cobblemon / Craftics adapter and playback — PARTIAL / BLOCKING end-to-end. Visualizing a trace does not establish authoritative detection or tactical legality.

## PTU / Caelo state

Public PTU 1.05 material provides concrete evidence that `Tracker` is an olfactory Pokémon Capability with Perception-based tracking procedures and that `Odor Sleuth` can grant Tracker. Before executable implementation, those details must be checked against the project-authoritative PTU/Caelo source used by Ouros.

No adopted Caelo olfactory overlay was located during this pass. Caelo-specific modifications remain `UNVERIFIED`.

## Reduced-version readiness

The proposed `The Trail That Arrived Without Footprints` loop can proceed as authored world investigation without dynamic scent simulation. It needs persistent/provenance-backed observations, ordinary world navigation and explicit NPC knowledge propagation. If implemented as executable state later, restart persistence should be tested.

No battle dependency blocks writing or canon review of the premise.

## Full-version blocking dependencies

A mechanically rich version becomes dependent on additional families only when those features are authored:

- scent fields or environmental masking -> terrain/weather/hazards/zones plus lifecycle;
- within-round plume changes -> full turn/round lifecycle;
- panic/rescue/forced movement -> complete movement;
- damaging chemical hazard -> full stateful damage pipeline;
- persistent chemical condition -> status lifecycle;
- Odor Sleuth or other scent Move -> move-specific behavior;
- sensory Ability -> abilities;
- PTU tracking equipment -> items;
- investigator Feature -> Trainer Features/perks;
- autonomous pursuit or hypothesis choice -> AI tactical policy;
- authoritative in-world trace playback -> Minecraft/Cobblemon/Craftics adapter.

## No promotion rule

Pass 317 deliberately makes no capability promotion. A single implemented representative mechanic, Move, Feature, history store or adapter path is evidence for that seam only.