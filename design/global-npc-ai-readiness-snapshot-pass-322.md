# Global NPC AI readiness snapshot — Pass 322

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-06

## Narrative destination

Pass 322 adds pollinator-phenology research, the proposed `The Orchard That Bloomed Out of Sequence` loop, and a reusable phenology observation contract. These additions are NON-CANON unless separately approved through the repository's canon process.

## Read-only engine evidence

### AutoPTU-Java

Observed head: `2bb5ceaf21ab08d09a4048fec0f8498d24189142`
Commit: `Add Python-compatible round-start semantic event (#388)`

Live evidence from this commit includes a typed Python-compatible `round_start` semantic event, authoritative initiative-entry snapshots, event registration/emission before round-start effects, language-neutral fixture export, differential testing against the Python oracle, parity gating, and ordered/stacked status coverage in that event payload.

This is useful evidence for a specific turn/round lifecycle seam and semantic-event contract. It does not prove the full turn/round lifecycle, arbitrary delayed effects, all status transitions, every reaction window, environmental scheduling, or end-to-end Minecraft/Cobblemon/Craftics playback.

### AutoPTU Python oracle

Observed head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
Commit: `Career: keep battle coordinates synced after viewport resize (#237)`

The commit explicitly describes itself as presentation-only and says no battle rules or outcomes change. It provides no new rule-coverage evidence for the capability families below.

Both engine repositories remain read-only for this workstream.

## Permanent capability categories

### Targeting / footprints / range / LoS — VERIFIED within audited contracts

Existing evidence supports the ordinary audited targeting/footprint/range/LoS contract. This does not automatically cover vegetation concealment, pollen obscurement, weather-dependent visibility, scent, sound, or ecological detection.

Pass 322 reduced version needs no new targeting rule. A rich orchard encounter that changes visibility through vegetation or airborne material needs additional verified behavior.

### Base movement legality — VERIFIED within audited contracts

Ordinary movement legality remains available within the verified scope. No pollinator- or plant-specific movement privilege is inferred.

### Complete movement including push/pull/knockback/interception/forced movement — PARTIAL

A rich version involving wind displacement, forced movement, interception, rescue, or Move-driven pushes/pulls depends on this family. The reduced version does not.

### Core calculations — VERIFIED within audited deterministic contracts

No ecological conversion rate, pollination percentage, bloom probability, or invented environmental arithmetic is added by Pass 322.

### Action economy / initiative — VERIFIED within audited contracts

Ordinary ordering remains supported. This does not imply that every environmental transition can be scheduled legally.

### Full turn / round lifecycle — PARTIAL

PR #388 materially strengthens one seam by exposing a Python-compatible semantic `round_start` event with parity coverage. Earlier work also provides specific round-start/history seams. The family remains PARTIAL because those seams do not prove all phases, delayed effects, end-of-round processing, reactions, environment schedules, or every state transition.

A reduced phenology loop performs state changes between scenes. Dynamic weather, bloom/pollen pulses, or other within-battle transitions remain dependent on missing/partial lifecycle coverage.

### Full stateful damage pipeline — PARTIAL

Pass 322 does not author environmental damage. Any later hazard that damages actors must use the verified stateful damage pipeline rather than an adapter-side shortcut.

### Status lifecycle — PARTIAL

Pass 322 introduces no new PTU status. Evidence labels such as `BLOOM_OPEN` and `VISITATION_OBSERVED` are world/observation descriptors, not combat conditions.

Any later persistent pollen, irritation, sleep, poison, or similar effect must be independently rule-backed and lifecycle-backed.

### Terrain / weather / hazards / zones / reactions — MIXED / PARTIAL / BLOCKING by subfamily

The reduced orchard loop does not require dynamic terrain or hazards. Rich versions involving wind/rain, vegetation zones, airborne pollen fields, environmental reactions, or rescue windows depend on the exact subfamilies and remain blocked where contracts are absent.

### Move-specific behavior — PARTIAL

No representative Move proves this family complete. Pollen Puff, Sweet Scent, Powder-family Moves, weather Moves, terrain Moves, or any ecological use of a Move must be verified independently before authoring battle consequences.

### Abilities — PARTIAL

Official franchise material identifies Honey Gather for Combee, but franchise flavor is not an AutoPTU contract. Honey Gather and every other Ability remain subject to individual implementation evidence.

### Items — PARTIAL

No item behavior is inferred for pollination, monitoring, farming, habitat management, or environmental control.

### Trainer Features / perks — PARTIAL

No general surveying, farming, ecology, breeder, ranger, or specialist privilege is assumed. Each Feature/perk must be verified against the project-authoritative rules and engine implementation.

### AI legal-action infrastructure — VERIFIED within audited contracts

Verified infrastructure can enumerate supported legal actions. This does not make unsupported ecological actions legal and does not provide tactical policy.

### AI tactical policy — BLOCKING for general autonomous environmental reasoning

General autonomous reasoning about temporal bloom windows, changing weather, field management, environmental rescue, or unsupported ecological actions is not established by current evidence.

### Minecraft / Cobblemon / Craftics adapter and playback — PARTIAL / BLOCKING end-to-end

PR #388 improves semantic-event evidence on the Java authoritative side, but it does not prove complete adapter/playback coverage. Minecraft visuals may present orchard state after receiving authoritative data; they must not decide bloom truth, pollination success, legal PTU actions, damage, statuses, or hidden NPC knowledge.

## Pass 322 implementation decision

The proposed orchard loop is safe to advance now in reduced form because its core gameplay is evidence collection, repeated observation, temporal comparison, NPC information flow, institutional decisions, and persistent feature-scoped consequences.

The rich version remains optional and dependency-gated. Missing combat capability must not be recreated in the world adapter.

## PTU / Caelo questions

The narrative repository inventory exposed Kairos material but no adopted `sources/caelo` directory during this pass. Before mechanical authoring, verify project-authoritative definitions for relevant Skills, environmental observation, weather, Moves, Abilities, Items, Trainer Features, and any rule touching pollen/nectar/plant interaction.

Until then, franchise ecology and public biological research remain inspiration/provenance, not rule authority.

## Open canon questions

Region, crop, agricultural scale, land ownership, local climate, orchard age, wild margin history, pollinator species, resident Pokémon, management institutions, market dependency, historical bloom baseline, and the true cause of the reported mismatch all remain unresolved.