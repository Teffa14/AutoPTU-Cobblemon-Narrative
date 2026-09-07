# Global NPC / AutoPTU readiness snapshot — Pass 320

Status: LIVE EVIDENCE SNAPSHOT

Date: 2026-09-06

## Read-only engine heads inspected

AutoPTU-Java:
- repository: `Teffa14/AutoPTU-Java`
- head inspected: `ce39aea49b957da388e076e59e9d329e24dc0799`
- current merged work: `Add generic round-start effects lifecycle seam (#387)`
- evidence: a generic round-start effect resolution seam exists and is ordered before the first initiative actor; tests cover that ordering contract.
- parent work from PR #386 materializes declarative round-window histories and prunes them through a lifecycle hook with Python oracle/parity coverage.

AutoPTU Python:
- repository: `Teffa14/AutoPTU`
- head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
- current merged work: `Career: keep battle coordinates synced after viewport resize (#237)`
- commit description explicitly limits the change to presentation and states that battle rules/outcomes do not change.

These repositories were inspected read-only. Pass 320 writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Permanent capability categories

### Targeting / footprints / range / LoS — VERIFIED within audited contracts

Ordinary tactical geometry remains usable. This does not verify smoke-obscured LoS, visibility attenuation, heat shimmer, wildfire sensing, or illumination changes caused by fire.

### Base movement legality — VERIFIED within audited contracts

Sufficient for the reduced Pass 320 concept when routes are represented as ordinary open/closed/restricted edges. Debris, unstable slopes, temporary fire barriers, special traversal, and changing terrain still require exact rule coverage when mechanically relevant.

### Complete movement including push/pull/knockback/interception/forced movement — PARTIAL

Required for any authored forced evacuation, push/pull, knockback near hazards, rescue/interception, or displacement caused by environmental effects. None is required by the reduced version.

### Core calculations — VERIFIED within audited deterministic arithmetic

Does not authorize fire-spread equations, smoke concentration, heat/fuel modeling, ecological succession formulas, severity scores, or suppression math.

### Action economy / initiative — VERIFIED within audited primitives

Can sequence valid tactical actions once those actions exist. It does not define firefighting, evacuation, rescue, stabilization, observation, or suppression actions by itself.

### Full turn / round lifecycle — PARTIAL

PR #387 adds and tests a generic round-start-effects seam resolved before the first initiative actor. PR #386 adds declarative round-window history lifecycle/pruning. These are meaningful verified seams, but they do not establish complete lifecycle coverage.

Timed flare-ups, spreading/changing fire zones, smoke expiration, weather transitions, delayed collapse, and generalized environmental phase effects therefore remain dependent on exact unverified lifecycle coverage.

### Full stateful damage pipeline — PARTIAL

Required for fire, smoke, collapse, impact, or other environmental battle damage. The reduced concept uses no tactical environmental damage.

### Status lifecycle — PARTIAL

Required for Burn or any other persistent mechanical condition. Pass 320 observation labels and recovery states are not statuses.

### Terrain / weather / hazards / zones / reactions — MIXED / PARTIAL / BLOCKING by subfamily

Dynamic fire sectors, smoke zones, weather interactions, changing hazard boundaries, reactive rescue, and mechanically active terrain require exact subfamily verification. Static authored route/feature states in the reduced version do not.

### Move-specific behavior — PARTIAL

Every Move used for ignition, suppression, weather, clearing, terrain alteration, rescue, or combat must be individually verified. No Water-type or Fire-type Move gains environmental behavior merely from type identity.

### Abilities — PARTIAL

No Ability receives wildfire immunity, smoke immunity, ignition behavior, heat sensing, suppression, hazard traversal, or weather authority from Pokédex flavor alone.

### Items — PARTIAL

Rules-level protective equipment, detectors, suppression tools, held items, ropes, masks, pumps, or rescue gear require exact item-family evidence. Narrative props may remain authored evidence without mechanical effects.

### Trainer Features / perks — PARTIAL

Fire response, Survival, weather control, rescue, hazard mitigation, interruption, investigation, or environmental manipulation Features/perks require individual sourcing and verification.

### AI legal-action infrastructure — VERIFIED within audited contracts

Can enumerate legality after actions, movement, terrain, and environmental contracts exist. It does not invent fire-response actions or infer hazard semantics from Minecraft presentation.

### AI tactical policy — BLOCKING for generalized autonomous tactics

General autonomous evacuation, dynamic fire avoidance, rescue prioritization, suppression strategy, changing-zone navigation, and coordinated environmental response remain blocking.

### Minecraft / Cobblemon / Craftics adapter and playback — PARTIAL / BLOCKING end-to-end

Minecraft may present charred blocks, regrowth, smoke, flames, barriers, route signage, NPC activity, and Pokémon animation. Presentation cannot decide PTU damage, Burn, LoS penalties, forced movement, legality, hazard timing, species ecology, event cause, route authority, or NPC belief.

## Pass 320 encounter compatibility

Reduced version:
- historical disturbance footprint as provenance-backed world data;
- persistent patch/feature IDs;
- ordinary route graph;
- feature-scoped `OPEN` / `RESTRICTED` / `CLOSED` / `MONITORING` state;
- scene-authored observation labels such as `REFUGE_OBSERVED`, `REGENERATION_OBSERVED`, and `RECOVERY_UNRESOLVED`;
- semantic-time revisits;
- explicit NPC receipt/belief updates;
- feature-level decisions and selective consequences;
- no spreading fire;
- no tactical smoke LoS modification;
- no Burn;
- no environmental damage;
- no forced movement;
- no rescue reactions;
- no inferred Move/Ability/Item/Feature behavior;
- no generalized tactical AI requirement.

Full version can additionally require:
- targeting/LoS subfamily support for mechanically active smoke/obscurement;
- complete movement for forced evacuation, knockback, displacement, and rescue/interception;
- full turn/round lifecycle for timed flare-ups, spreading/changing zones, weather transitions, and delayed effects;
- full stateful damage pipeline for fire/smoke/environmental damage;
- status lifecycle for Burn or other persistent conditions;
- terrain/weather/hazards/zones/reactions for active fire sectors, smoke, weather, and reactive rescue;
- move-specific behavior for verified suppression, ignition, weather, terrain, or rescue Moves;
- Abilities for any real Ability interaction;
- Items for rules-level response/protection equipment;
- Trainer Features/perks for specialized intervention;
- AI tactical policy for autonomous evacuation/rescue/suppression tactics;
- Minecraft/Cobblemon/Craftics adapter/playback for faithful presentation without duplicate rules authority.

## PTU / Caelo source boundary

Current Narrative source inventory exposes `sources/kairos` with a PTU/Kairos routing index. No adopted `sources/caelo` directory or fire-specific Ouros overlay was located.

The Kairos index routes relevant comparison toward movement/terrain, status, hazards, terrain/weather, and encounter-creation sections. The index itself explicitly states that these references are routing aids and that Kairos/homebrew content is not automatically accepted by Ouros.

Official Fletchinder material supports one species-specific narrative hypothesis about scattering embers in vegetation. It does not establish PTU ignition probability, Fire Hazard squares, Burn, spread rate, damage, culpability, immunity, or regional presence.

Pass 320 therefore adds no PTU/Caelo DC, damage value, fire-spread rule, smoke penalty, terrain cost, Burn rule, hazard duration, weather interaction, rescue interrupt, species immunity, Move behavior, Ability behavior, Item effect, or Trainer Feature behavior.

## Promotion decision

No permanent capability category is promoted by Pass 320.

AutoPTU-Java PR #387 strengthens evidence for one generic round-start lifecycle seam. It does not complete the lifecycle category or prove dynamic environmental effects. AutoPTU Python's current head remains presentation-only.
