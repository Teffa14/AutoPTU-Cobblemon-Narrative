# Global NPC / AutoPTU readiness snapshot — Pass 318

Status: LIVE EVIDENCE SNAPSHOT

Date: 2026-09-06

## Read-only engine heads inspected

AutoPTU-Java:
- repository: `Teffa14/AutoPTU-Java`
- head inspected: `d6cd74d835085dcb0b20724c49effe774c23f73a`
- current merged work: `Wire declarative round-window histories into lifecycle (#386)`
- evidence: declarative round-window histories are materialized in battle state, a lifecycle hook exists, pruning is wired after initiative rebuild, and oracle/parity coverage compares the seam with pinned Python behavior.

AutoPTU Python:
- repository: `Teffa14/AutoPTU`
- head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
- current merged work: `Career: keep battle coordinates synced after viewport resize (#237)`
- commit description explicitly limits the change to presentation and states that battle rules/outcomes do not change.

These repositories were inspected read-only. Pass 318 writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Permanent capability categories

### Targeting / footprints / range / LoS — VERIFIED within audited contracts

Existing evidence supports the audited geometric/targeting contracts. Pass 318 does not reinterpret LoS as magnetic sensing, compass accuracy, electromagnetic interference, darkness, or any other perception system.

### Base movement legality — VERIFIED within audited contracts

Sufficient for the reduced geomagnetic-navigation scenario, which traverses an ordinary route graph.

### Complete movement including push/pull/knockback/interception/forced movement — PARTIAL

A full magnetic encounter that attracts or displaces actors/objects would depend on this family. No such displacement exists in the reduced version.

### Core calculations — VERIFIED within audited deterministic arithmetic

This does not authorize a magnetic-field equation, sensor model, compass error formula, or real-world physics simulation.

### Action economy / initiative — VERIFIED within audited primitives

Can support authored tactical actions once those actions have verified contracts. It does not by itself implement equipment operation or field observation.

### Full turn / round lifecycle — PARTIAL

PR #386 strengthens one concrete seam: declarative round-window history state and pruning are wired into a lifecycle hook with oracle parity. Representative history handling does not establish complete phase sequencing, delayed effects, field pulses, reactions, or every start/end-of-turn behavior.

A dynamically pulsing magnetic-field encounter therefore remains dependent on this category.

### Full stateful damage pipeline — PARTIAL

Required only if the full scenario introduces impact/electrical/environmental damage. The reduced concept does not.

### Status lifecycle — PARTIAL

Required only if an authored magnetic/electrical condition persists as a battle status. Pass 318 defines no new PTU status.

### Terrain / weather / hazards / zones / reactions — MIXED / PARTIAL / BLOCKING by subfamily

Dynamic magnetic zones, moving interference boundaries, reactive rescue, or changing equipment-danger sectors depend on exact subfamilies here. Static authored observation nodes in the reduced version do not.

### Move-specific behavior — PARTIAL

Any magnetic Move must be individually verified. Narrative references to magnetism do not establish Move implementation.

### Abilities — PARTIAL

Magnet Pull or any other Ability-based rule requires explicit Ability-family evidence. Official Pokédex descriptions are narrative/species evidence only.

### Items — PARTIAL

A compass, field meter, held item, or other sensor becomes dependent on this category only when it has rules-level effects. A narrative observation prop can remain authored world evidence.

### Trainer Features / perks — PARTIAL

Any navigation, engineering, surveying, interruption, mitigation, or specialized sensing Feature must be individually sourced and verified.

### AI legal-action infrastructure — VERIFIED within audited contracts

This supports legality enumeration when the underlying action exists. It does not establish a policy for choosing among competing navigation hypotheses or reacting intelligently to dynamic field hazards.

### AI tactical policy — BLOCKING for generalized autonomous tactics

General autonomous reasoning about field sectors, equipment shutdowns, rescues, magnetic movement, or safe-route selection is not promoted by Pass 318.

### Minecraft / Cobblemon / Craftics adapter and playback — PARTIAL / BLOCKING end-to-end

Minecraft compass animation, particles, redstone-like machinery, block state, or client rendering must not become rules authority. A full implementation needs authoritative world/battle state to drive playback and persistence without duplicating PTU mechanics in the adapter.

## Pass 318 encounter compatibility

Reduced version:
- ordinary route graph;
- static/scene-authored field-observation descriptors;
- visual landmarks and survey markers;
- explicit NPC observation provenance;
- controlled infrastructure state changes between scenes;
- no forced movement;
- no dynamic hazard zone;
- no battle status;
- no damage;
- no Ability/Move/Item rule assumed;
- no generalized tactical AI requirement.

Full version can additionally require:
- complete movement for magnetic attraction/displacement and rescue;
- full turn/round lifecycle for timed/pulsed field changes;
- full stateful damage pipeline for authored damaging hazards;
- status lifecycle for any persistent condition;
- terrain/weather/hazards/zones/reactions for dynamic field sectors;
- move-specific behavior for magnetic Moves;
- Abilities for Magnet Pull or similar effects;
- Items for rules-level navigation/sensor equipment;
- Trainer Features/perks for specialized interventions;
- AI tactical policy for autonomous exploitation/avoidance;
- Minecraft/Cobblemon/Craftics adapter/playback for faithful end-to-end presentation.

## PTU / Caelo source boundary

Narrative repository `sources/` inspection exposes `sources/kairos`. No adopted `sources/caelo` directory was found in the inspected tree, and repository search did not establish a project-authoritative magnetic-navigation overlay.

Pass 318 therefore leaves numeric PTU/Caelo magnetic-navigation mechanics UNVERIFIED. It adds no DCs, ranges, durations, modifiers, movement formulas, disruption radii, or inferred Feature/Ability behavior.

## Promotion decision

No permanent capability category is promoted by Pass 318.

AutoPTU-Java PR #386 is treated as evidence for a concrete round-window lifecycle seam only. AutoPTU Python's current head remains presentation-only. The geomagnetic proposal is designed around those limitations rather than treating representative engine work as category completeness.