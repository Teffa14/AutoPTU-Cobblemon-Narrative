# Global NPC / encounter readiness snapshot — Pass 316

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-06

## Scope

This snapshot records capability evidence used by Pass 316. A representative implemented mechanic does not promote its entire family.

Read-only engine evidence inspected:

- `Teffa14/AutoPTU-Java` head `704722ffecbef9e003abe1870829843f29f029c7`, PR #385, `Add declarative round-window history state`;
- `Teffa14/AutoPTU` head `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, whose commit explicitly states that the change is presentation-only and changes no battle rules or outcomes.

## Live Java delta since Pass 315

PR #385 adds a declarative server-core store for round-indexed histories, including built-in definitions for Echoed Voice, Fusion Bolt and Fusion Flare history windows, runtime-owned record/restore boundaries, lifecycle pruning and Python-oracle parity tests/gating.

This strengthens evidence for one round-history state family. It does not prove:

- complete turn/round phase sequencing;
- all delayed effects;
- arbitrary phase hooks;
- reaction windows;
- complete stateful damage processing;
- status expiry/refresh;
- dynamic visibility/illumination;
- terrain/hazard zones;
- general Move behavior;
- Minecraft adapter/playback.

Full lifecycle therefore remains PARTIAL.

## Permanent capability categories

### Targeting / footprints / range / LoS

Status: VERIFIED within audited contracts.

Pass 316 boundary: ordinary spatial target/range/LoS support is verified only within existing contracts. No inspected evidence establishes dynamic darkness, glare, light radius, night vision or illumination-dependent legal targeting. Those must not be inferred.

### Base movement legality

Status: VERIFIED within audited contracts.

Pass 316 relevance: sufficient for reduced-version travel between static observation nodes and ordinary legal movement where otherwise supported.

### Complete movement including push/pull/knockback/interception/forced movement

Status: PARTIAL.

Pass 316 relevance: required only for forced displacement, moving machinery, panic movement or reaction rescue in the full encounter.

### Core calculations

Status: VERIFIED within audited contracts.

Pass 316 relevance: ordinary deterministic arithmetic can use verified contracts. No illumination attenuation, glare or visibility formula is introduced.

### Action economy / initiative

Status: VERIFIED within audited contracts.

Pass 316 relevance: supports structured actions where the underlying action is already legal.

### Full turn / round lifecycle

Status: PARTIAL.

Live evidence: PR #385 adds declarative round-window history state and oracle-backed pruning. PR #384 added reusable pruning; PR #383 strengthened history ordering around initiative rebuild. These are meaningful seams, not proof of the complete lifecycle.

Pass 316 relevance: exact mid-round lighting changes, delayed fixture failures or timed zone transitions remain dependent on missing/full lifecycle guarantees.

### Full stateful damage pipeline

Status: PARTIAL.

Pass 316 relevance: required if an electrical fixture, fall, environmental hazard or combat action causes real damage with ordinary downstream consequences. The narrative layer may not approximate it.

### Status lifecycle

Status: PARTIAL.

Pass 316 relevance: no `blinded`, `dazzled`, `night-adapted` or similar persistent condition is invented. Any real condition requires exact source and implementation evidence.

### Terrain / weather / hazards / zones / reactions

Status: MIXED / PARTIAL / BLOCKING by subfamily.

Pass 316 relevance: dynamic light/shadow zones, electrical hazards, moving safe areas, triggered fixture changes and reaction rescues depend on this family. Existing LoS does not substitute for a verified illumination-zone contract.

### Move-specific behavior

Status: PARTIAL.

Pass 316 relevance: Flash or any light-producing Move cannot gain exploration, visibility or ecology effects beyond verified PTU/engine behavior.

### Abilities

Status: PARTIAL.

Pass 316 relevance: Illuminate or other potentially relevant Abilities require exact implemented semantics. Ability names/flavor do not create field ecology.

### Items

Status: PARTIAL.

Pass 316 relevance: the reduced version can treat lamps, shields or observation tools as authored world equipment. Any PTU Item mechanic requires validation.

### Trainer Features / perks

Status: PARTIAL.

Pass 316 relevance: observation bonuses, darkness interaction, interrupts or specialist night-operation effects require direct source and implementation evidence.

### AI legal-action infrastructure

Status: VERIFIED within audited contracts.

Pass 316 relevance: can constrain autonomous actors to already-defined legal actions.

### AI tactical policy

Status: BLOCKING for general autonomous tactical choice.

Pass 316 relevance: general reasoning about light/shadow routes, fixture controls, rescue priorities or exploiting visibility remains blocked.

### Minecraft / Cobblemon / Craftics adapter and playback support

Status: PARTIAL / BLOCKING end-to-end.

Pass 316 relevance: Minecraft can render illumination changes, but inspected evidence does not establish client/block light as authoritative PTU visibility or ecology state. Full synchronized authoritative light-state playback remains unavailable end-to-end.

## Reduced-version readiness

`The Ridge That Never Got Dark` can run as world/narrative state without new AutoPTU mechanics:

- authored lighting states changed between scenes;
- fixed observation nodes;
- provenance-backed direct observations;
- separate interpretation claims;
- static open/blocked navigation;
- repeated authored time windows;
- explicit stakeholder information flow;
- no numerical darkness or glare modifier;
- no invented status or light-sensitive battle rule.

This preserves the investigation premise while avoiding unsupported mechanics.

## Intended full-version blockers

The rich version requires additional verification wherever it uses:

- illumination-sensitive legal targeting: explicit visibility/zone contract beyond ordinary LoS;
- in-round light changes: full turn/round lifecycle;
- forced movement/rescue interception: complete movement;
- electrical/environmental injury: full stateful damage pipeline;
- persistent visual conditions: status lifecycle;
- light/shadow fields or reactive infrastructure: terrain/hazards/zones/reactions;
- Flash or another special Move: move-specific behavior;
- Illuminate or another Ability: Abilities;
- specialized equipment: Items;
- observation/interrupt Features: Trainer Features/perks;
- autonomous exploitation of light state: AI tactical policy;
- authoritative fixture/light playback: Minecraft/Cobblemon/Craftics adapter support.

## PTU / Caelo uncertainty retained

Pass 316 makes no new PTU numeric rule. Direct validation remains required before mapping the scenario to Perception, Survival, concealment, darkness modifiers, Moves, Abilities, Items, Trainer Features or species sensory capability.

Repository inspection found no Caelo text/file match defining artificial-light or nocturnal-visibility mechanics. That overlay remains `UNVERIFIED` rather than reconstructed from memory.

## Canon uncertainty retained

No location, affected species, facility, observation tradition, stakeholder, incident or mitigation is canonized by this pass.