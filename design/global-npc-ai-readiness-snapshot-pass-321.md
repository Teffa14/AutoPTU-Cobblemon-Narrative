# Global NPC / AutoPTU readiness snapshot — Pass 321

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-06

## Read-only engine heads inspected

AutoPTU-Java:
- repository: `Teffa14/AutoPTU-Java`;
- head inspected: `ce39aea49b957da388e076e59e9d329e24dc0799`;
- merged work: `Add generic round-start effects lifecycle seam (#387)`;
- live evidence: `ROUND_START_EFFECTS` is a distinct lifecycle hook, and the battle round controller resolves it after initiative/history setup and before selecting the first initiative actor; tests in the merged change cover the ordering contract;
- interpretation: this strengthens one exact lifecycle seam. It does not prove complete turn/round lifecycle, delayed environmental effects, changing hazard zones, rescue reactions, or fluid simulation.

AutoPTU Python:
- repository: `Teffa14/AutoPTU`;
- head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`;
- merged work: `Career: keep battle coordinates synced after viewport resize (#237)`;
- commit description explicitly states presentation only and no battle-rule/outcome changes.

Both engine repositories were inspected read-only. Pass 321 writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Permanent capability categories

### Targeting / footprints / range / LoS — VERIFIED within audited contracts

Ordinary tactical geometry remains usable. This status does not verify underwater visibility, turbidity, water-surface occlusion, depth-sensitive targeting, or flood-specific concealment.

### Base movement legality — VERIFIED within audited contracts

Ordinary route/node movement is sufficient for the reduced Pass 321 version. Swim, wading, water depth, special traversal, and water-terrain costs remain dependent on exact PTU/Caelo evidence.

### Complete movement including push/pull/knockback/interception/forced movement — PARTIAL

Required for currents that displace actors, debris-driven displacement, rescue/interception, pull from water, knockback near channel edges, or any forced movement. The reduced version avoids these mechanics.

### Core calculations — VERIFIED within audited deterministic arithmetic

No flood depth threshold, current-strength equation, hydrodynamic model, erosion score, or gauge-to-damage conversion is authorized by this status.

### Action economy / initiative — VERIFIED within audited primitives

Can order legal actions once those actions exist. Does not itself define swimming, rescue, stabilization, pumping, clearing, evacuation, or environmental observation actions.

### Full turn / round lifecycle — PARTIAL

AutoPTU-Java PR #387 verifies a generic round-start-effects seam before the first initiative actor. Earlier work also covers specific round-window history lifecycle/pruning. These are meaningful seams, not complete lifecycle coverage.

Pass 321 full-version features such as rising/falling water during combat, scheduled flood pulses, delayed debris, changing current zones, and water-state changes at phase boundaries remain gated on exact lifecycle support.

### Full stateful damage pipeline — PARTIAL

Required if a later version authors drowning, debris impact, crushing, falling, collision, or other environmental battle damage. The reduced version has no tactical flood damage.

### Status lifecycle — PARTIAL

Required only for actual persistent mechanical conditions. `DRY_OPEN`, `INUNDATED_CLOSED`, `HIGH_WATER_MARK_OBSERVED`, and similar Pass 321 labels are world/observation data, not PTU statuses.

### Terrain / weather / hazards / zones / reactions — MIXED / PARTIAL / BLOCKING by subfamily

Active current zones, rain-driven changes, dynamic inundation boundaries, unstable footing, flood hazards, weather coupling, and rescue reactions require exact subfamily verification. Static route restrictions in the reduced version do not.

### Move-specific behavior — PARTIAL

Every Move used for water manipulation, weather, terrain change, clearing, rescue, travel, or combat requires individual parity evidence. Water typing or animation alone grants no environmental effect.

### Abilities — PARTIAL

Every Ability interaction requires exact support. Pokédex ecology does not create current resistance, flood navigation, drowning immunity, hazard detection, or rescue authority.

### Items — PARTIAL

Rules-level ropes, flotation gear, pumps, gauges, protective equipment, held items, navigation tools, or rescue equipment require exact item-family evidence. Narrative props may remain non-mechanical evidence.

### Trainer Features / perks — PARTIAL

Any Feature used for Survival, swimming, navigation, weather, rescue, terrain intervention, hazard mitigation, or interrupts must be verified individually.

### AI legal-action infrastructure — VERIFIED within audited contracts

Can enumerate legal choices after actions and environmental legality are defined. It cannot infer current, passability, drowning risk, or rescue actions from Minecraft blocks.

### AI tactical policy — BLOCKING for generalized autonomous tactics

Autonomous current navigation, flood evacuation, rescue prioritization, changing-hazard avoidance, dynamic crossing strategy, and coordinated environmental response remain blocking for generalized tactical policy.

### Minecraft / Cobblemon / Craftics adapter/playback — PARTIAL / BLOCKING end-to-end

Minecraft can present water, silt, debris, causeways, culverts, signs, barriers, Pokémon, NPCs, route closures, and world-state changes. Presentation cannot decide PTU current, forced movement, damage, drowning, visibility penalties, route authority, ecological truth, historical provenance, or NPC belief.

## Pass 321 reduced-version compatibility

The reduced concept uses:
- persistent feature IDs;
- ordinary route graph edges;
- authored scene-to-scene hydrologic/operational states such as `DRY_OPEN`, `SHALLOW_RESTRICTED`, `INUNDATED_CLOSED`, `BYPASS_OPEN`, and `MONITORING`;
- provenance-backed observation records;
- semantic time;
- explicit actor receipt/knowledge boundaries;
- assessment/review lineage;
- feature-scoped institutional decisions and consequences;
- selective repair when later evidence changes only one consequence.

The reduced version requires no:
- current vectors;
- water-level changes inside tactical rounds;
- drowning;
- environmental battle damage;
- underwater/turbidity LoS rules;
- forced movement;
- rescue reactions;
- persistent water-related status;
- inferred Move/Ability/Item/Feature behavior;
- generalized tactical AI policy.

## Pass 321 full-version gates

A richer encounter may later activate:
- targeting/LoS support for underwater or turbid-water visibility;
- complete movement for currents, push/pull, forced displacement, and rescue/interception;
- full turn/round lifecycle for timed rises/falls, pulses, delayed debris, and changing hazard sectors;
- full stateful damage pipeline for drowning, debris, falls, or other environmental damage;
- status lifecycle if a real persistent condition is used;
- terrain/weather/hazards/zones/reactions for currents, rain, changing water boundaries, unstable footing, and reactive rescue;
- individually verified Moves for water/weather/terrain/rescue effects;
- individually verified Abilities;
- individually verified Items;
- individually verified Trainer Features/perks;
- AI tactical policy for autonomous hazard-aware behavior;
- Minecraft/Cobblemon/Craftics adapter/playback that faithfully displays authoritative state without duplicating PTU rules.

## PTU / Kairos / Caelo source boundary

Pass 321 repository inspection found `sources/kairos` and its source-routing index. No adopted `sources/caelo` directory and no project-local flood/current rules contract were located.

The repository search also did not surface a local authoritative contract for `Swim`, current, drowning, water terrain, or flood mechanics.

Official Pokémon material for Quagsire, Barboach, and Azumarill can support species-specific ecological hypotheses only. It does not authorize PTU movement values, sensor ranges, hazard immunity, rescue behavior, Ability behavior, or regional presence.

Therefore Pass 321 adds no numeric Swim/current rule, drowning rule, water terrain cost, visibility modifier, weather interaction, flood damage, rescue interrupt, Move behavior, Ability behavior, Item effect, or Trainer Feature behavior.

Those details remain UNVERIFIED until authoritative PTU/Caelo project material is located and inspected directly.

## Promotion decision

No permanent capability category is promoted by Pass 321.

AutoPTU-Java PR #387 remains concrete evidence for one round-start lifecycle seam only. AutoPTU Python's current head remains presentation-only. The floodplain proposal is deliberately built so narrative progress does not depend on unverified fluid mechanics.
