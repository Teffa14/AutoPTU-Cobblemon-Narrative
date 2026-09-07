# Global NPC / AutoPTU readiness snapshot — Pass 319

Status: LIVE EVIDENCE SNAPSHOT

Date: 2026-09-06

## Read-only engine heads inspected

AutoPTU-Java:
- repository: `Teffa14/AutoPTU-Java`
- head inspected: `ce39aea49b957da388e076e59e9d329e24dc0799`
- current merged work: `Add generic round-start effects lifecycle seam (#387)`
- evidence: a generic round-start effect resolution seam exists and is ordered before the first initiative actor; tests cover that ordering contract.
- parent work from PR #386 already materializes declarative round-window histories and prunes them through a lifecycle hook with Python oracle/parity coverage.

AutoPTU Python:
- repository: `Teffa14/AutoPTU`
- head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
- current merged work: `Career: keep battle coordinates synced after viewport resize (#237)`
- commit description explicitly limits the change to presentation and states that battle rules/outcomes do not change.

These repositories were inspected read-only. Pass 319 writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Permanent capability categories

### Targeting / footprints / range / LoS — VERIFIED within audited contracts

Useful for ordinary tactical geometry and future elevation/occlusion representation. This does not verify dust visibility, darkness, geological sensing, unstable-ground detection, hearing, or environmental perception.

### Base movement legality — VERIFIED within audited contracts

Sufficient for the reduced quarry concept using ordinary open/closed route edges. Exact climbing, jumping, water traversal, rough terrain, ledge handling, and species-specific exceptions still require their own verified rules.

### Complete movement including push/pull/knockback/interception/forced movement — PARTIAL

Required for slides, falling displacement, rock/debris push, knockback near drops, current-driven movement, or rescue/interception. None is required by the reduced version.

### Core calculations — VERIFIED within audited deterministic arithmetic

Does not authorize slope-stability formulas, geology, fall equations, water-flow simulation, contaminant thresholds, or quarry-specific math.

### Action economy / initiative — VERIFIED within audited primitives

Can sequence valid tactical actions once defined. Does not itself establish inspection, climbing, stabilization, rescue, machinery operation, or engineering actions.

### Full turn / round lifecycle — PARTIAL

PR #387 adds and tests a generic round-start-effects seam resolved before the first initiative actor. PR #386 adds declarative round-window history lifecycle/pruning. These are meaningful seams, not proof of complete lifecycle coverage.

Timed slope failure, delayed rockfall, multi-step structural degradation, round-phased drainage, rainfall transitions, and generalized start/end-of-turn environmental effects therefore remain dependent on exact unverified lifecycle coverage.

### Full stateful damage pipeline — PARTIAL

Required for fall, impact, rockfall, crushing, water, chemical, or other environmental battle damage. The reduced concept uses no tactical environmental damage.

### Status lifecycle — PARTIAL

Required only for persistent mechanical conditions. Pass 319 defines no quarry-specific status and does not convert evidence labels into conditions.

### Terrain / weather / hazards / zones / reactions — MIXED / PARTIAL / BLOCKING by subfamily

Dynamic scree, unstable ledges, falling debris, changing water, weather-triggered hazard sectors, rescue reactions, and changing hazard boundaries depend on exact subfamilies. Static blocked route edges and scene-authored feature states in the reduced version do not.

### Move-specific behavior — PARTIAL

Any Move used to dig, blast, stabilize, clear debris, alter terrain, traverse, rescue, or fight must be individually verified.

### Abilities — PARTIAL

No Ability receives quarry traversal, hazard immunity, mining behavior, rough-terrain privilege, or environmental manipulation from Pokédex flavor alone.

### Items — PARTIAL

Rules-level ropes, survey equipment, detectors, pumps, helmets, climbing gear, held items, or tools require item-family evidence. Narrative props can remain authored evidence without mechanical effects.

### Trainer Features / perks — PARTIAL

Engineering, Survival, climbing, geological interpretation, rescue, interruption, hazard mitigation, or surveying Features/perks must be individually sourced and verified.

### AI legal-action infrastructure — VERIFIED within audited contracts

Can enumerate legality once underlying actions and terrain contracts exist. It does not create quarry-specific actions or understand hazards automatically.

### AI tactical policy — BLOCKING for generalized autonomous tactics

General autonomous navigation through unstable sectors, rescue prioritization, hazard anticipation, route selection, terrain exploitation, or machinery operation remains blocking.

### Minecraft / Cobblemon / Craftics adapter and playback — PARTIAL / BLOCKING end-to-end

Block collapse, Minecraft water, falling entities, particles, barriers, pathfinding, sounds, or animations must follow authoritative world/battle state. They cannot decide PTU damage, forced movement, status, legality, timing, or causal world outcomes independently.

## Pass 319 encounter compatibility

Reduced version:
- ordinary authoritative route graph;
- feature-scoped OPEN/CLOSED/RESTRICTED state;
- static or between-scene evidence changes;
- deterministic world events outside tactical timing;
- observation provenance and separate interpretation;
- feature-level decisions/consequences;
- no forced movement;
- no dynamic rockfall zone;
- no fall/environmental damage;
- no persistent quarry status;
- no inferred Move/Ability/Item/Feature behavior;
- no generalized tactical AI requirement.

Full version can additionally require:
- complete movement for slides, knockback, falling displacement, currents, and rescue/interception;
- full turn/round lifecycle for timed collapse, delayed debris, phase-based drainage, and weather/machinery transitions;
- full stateful damage pipeline for environmental damage;
- status lifecycle for persistent authored conditions;
- terrain/weather/hazards/zones/reactions for unstable ground, debris, dynamic water, hazard sectors, and reactive rescue;
- move-specific behavior for terrain-altering or rescue Moves;
- Abilities for any actual Ability interaction;
- Items for rules-level survey/safety equipment;
- Trainer Features/perks for specialized intervention;
- AI tactical policy for autonomous exploitation/avoidance/rescue;
- Minecraft/Cobblemon/Craftics adapter/playback for faithful world representation without duplicate rules authority.

## PTU / Caelo source boundary

Current Narrative tree inspection still exposes `sources/kairos`. No adopted `sources/caelo` directory or project-authoritative quarry/reclamation overlay was located.

Official Rolycoly material supports mine/cave association, illumination flavor, and rough-terrain flavor as franchise evidence. It does not establish PTU Overland, terrain costs, immunity, darkness handling, mining labor, or automatic traversal.

Pass 319 therefore adds no PTU/Caelo DC, damage value, fall rule, terrain cost, collapse timer, water rule, contamination threshold, rescue interrupt, species immunity, Move behavior, Ability behavior, Item effect, or Trainer Feature behavior.

## Promotion decision

No permanent capability category is promoted by Pass 319.

AutoPTU-Java PR #387 is treated as evidence for one generic round-start ordering seam. It strengthens lifecycle evidence without completing the category. AutoPTU Python's current head remains presentation-only.
