# Engine Readiness Snapshot — Pass 206

Status: READ-ONLY ENGINE AUDIT
Date: 2026-09-02

## Evidence inspected

Narrative repository head before this pass: `fe4ae2c5077127f773a295a7578d58011afbf776`.

AutoPTU-Java current head inspected: `716687c6f8431807b91f33567cc8c9c7fd010756`.

Latest Java change wires forced-movement semantic events into authoritative move results and tests ordering/content for a concrete prevention path. The runtime now appends a `TrainerFeatureEvent` after the `MoveResolvedEvent` when Insectoid Utility prevents canonical push in the covered test.

This is stronger evidence for semantic event propagation and one forced-movement prevention path. It is not evidence that every forced-movement rule or every Trainer Feature exists.

AutoPTU Python remains the parity oracle while the Java port is incomplete and is read-only for this task.

## Permanent capability audit

### Targeting / footprints / range / LoS

State: VERIFIED within currently audited contracts.

Usable for the reduced first visible-wild battle when selected combatants remain inside those contracts.

### Base movement legality

State: VERIFIED within currently audited contracts.

Usable for ordinary reduced battle movement. Do not infer every terrain/capability interaction from this label.

### Complete movement: push / pull / knockback / interception / forced movement and interactions

State: PARTIAL.

New evidence: semantic forced-movement prevention now reaches authoritative `BattleRuntime` results for a tested path and event ordering is asserted.

Still not sufficient to claim full Push/Pull/Knockback/Interception coverage, collision behavior, partial displacement, chained displacement, footprint interactions, terrain-mediated displacement, or every Move/Ability/Item/Feature/status interaction.

### Core calculations

State: VERIFIED within audited contracts.

### Action economy / initiative

State: VERIFIED within audited contracts.

### Full turn / round lifecycle

State: PARTIAL.

Reduced first encounter must use audited ordinary paths and avoid lifecycle-dependent special objectives.

### Full stateful damage pipeline

State: PARTIAL.

### Status lifecycle

State: PARTIAL.

Do not make the first Sendero visible-wild slice depend on delayed/complex status behavior.

### Terrain / weather / hazards / zones / reactions

State: BLOCKING as a complete family.

Minecraft may render terrain/weather aesthetically, but a battle concept requiring tactical weather, hazardous cells, zones or reactions must remain dependency-marked until engine contracts verify them.

### Move-specific behavior

State: PARTIAL.

### Abilities

State: PARTIAL.

### Items

State: PARTIAL.

### Trainer Features / perks

State: PARTIAL.

The new Insectoid Utility event path is representative evidence only.

### AI legal-action infrastructure

State: VERIFIED within audited contracts.

### AI tactical policy

State: BLOCKING for the complete intended family.

Minecraft presentation behaviors such as wander/flee/warning must not be counted as tactical AI progress.

### Minecraft / Cobblemon / Craftics adapter and playback support

State: BLOCKING for complete target support.

The separate RPG repository already has a fixed Marea world build, NPC binding, quest runtime and location observation surfaces, so visible wild projection can be developed there without waiting for the entire adapter family. However, end-to-end battle projection/reconciliation must still be verified before the slice is called playable.

## Pass-206 encounter impact

The proposed first visible Sendero battle can be reduced to avoid complete movement, tactical terrain/weather, reaction systems and objective-aware AI.

Required minimal families:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- AI legal-action infrastructure — VERIFIED;
- selected ordinary lifecycle/damage/status/move/ability/item/feature paths — must be individually audited because their parent categories remain PARTIAL;
- Minecraft projection/handoff/reconciliation — implementation blocker outside AutoPTU-Java parity itself.

## Mechanical questions still unresolved

- Which exact PTU/Caelo/Kairos/Ouros rules profile governs deliberate tracking in production.
- Whether Ouros keeps Caelo's once-per-day specific search and Bait follow-up structure.
- Which first Sendero species/forms and level band are canonically approved.
- Which selected early encounter Moves/Abilities are fully parity-safe in Java.
- Exact capture handoff readiness from Minecraft-visible actor through AutoPTU-Java and back.
- Whether ambient avoidance/territorial presentation ever escalates through PTU Skill checks automatically or always waits for explicit player interaction.
- How server time/weather selects a population context before full tactical weather support exists.

No unresolved point was silently promoted to canon in pass 206.
