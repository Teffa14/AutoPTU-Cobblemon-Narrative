# Engine Readiness Snapshot — Pass 158

Status: READ-ONLY EVIDENCE SNAPSHOT for narrative dependency planning.
Date: 2026-08-24

## Repository authority correction

The final full-tree compare surfaced `design/decomposition-fungi-deadwood-nutrient-cycling-layer.md` from Pass 72. Pass 72 already owns fungal occurrence, root/fungal associations, decomposer activity and the foundational separation between fruiting observations and PTU mechanics.

The temporary duplicate Pass 158 fungal authority was deleted. Pass 158 now adds only `design/fungal-fruiting-survey-harvest-monitoring-protocol.md`, extending Pass 72 with monitoring series, survey effort/detectability, fruiting episodes, occurrence linkage, sample provenance, spore observations and harvest records.

## Live heads inspected

- AutoPTU-Java main: `3caac611a987322a70dbdc34c56d613b96dadb92`
- AutoPTU Python main: `5ab2c175be6542b867f1676cf6848b9b15fd346f`

The Java head adds a runtime-owned POST-damage Move-special bridge carrying Python `damage_dealt`. Recent preceding slices cover PRE-damage bridges, live PRE-damage execution, mutable move-special state, a generic move-special registry and zero-damage Status Move execution.

This is concrete progress for move-specific ordering. It does not prove all Spore/powder Moves, Status applications, Ability hooks, environmental spores, terrain, hazards or reactions.

Python's latest change is Career resilience and does not change tactical readiness.

## PTU fungal evidence inspected

Read-only AutoPTU search exposes PTU/audit Mushroom Item data and an `Effect Spore` Python hook under `auto_ptu/rules/hooks/abilities/contact_effects.py`. The project corpus also contains Spore/powder Move and status infrastructure.

Those are exact downstream mechanics. Pass 72/158 world state never synthesizes them from scenery.

## Permanent capability classification

VERIFIED:
- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

PARTIAL:
- full turn / round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features / perks.

BLOCKING as complete families:
- complete movement including push / pull / knockback / interception / forced movement;
- terrain / weather / hazards / zones / reactions;
- AI tactical policy;
- Minecraft / Cobblemon / Craftics adapter and playback.

The POST-damage Move-special bridge does not promote a complete family.

## Pass 158 encounter dependencies

### Fruiting Chamber Survey — FULL

VERIFIED baseline: targeting, base movement legality, core calculations, action economy/initiative and AI legal-action infrastructure.

BLOCKING:
- complete movement if researchers or Pokémon must cross, withdraw or protect a moving route;
- terrain/weather/hazards/zones/reactions if darkness, slick substrate, cave conditions or environmental spores alter tactical state;
- AI tactical policy for `WITHDRAW`, `PROTECT_SAMPLE_ROUTE`, `CLEAR_ROUTE`, `REACH_EXIT`;
- adapter/playback for researchers, sample sites and world-state handoff.

PARTIAL if invoked:
- status lifecycle for actual Sleep/Poison/Paralysis;
- move-specific behavior for an exact Spore/powder Move;
- abilities for Effect Spore, Illuminate or another exact Ability;
- items for tactical protective/sampling gear;
- Trainer Features/perks when explicitly used.

REDUCED: sampling/exposure happens in world state; researchers leave; any battle uses static safe geometry and no ambient fungal Status mechanic.

### Deadwood Plot Disturbance — FULL

Main blockers are complete movement, AI tactical policy and adapter/playback for non-hostile withdrawal/crowd clearing. The environmental family is needed only if an exact verified tactical terrain/hazard is authored.

REDUCED: visitor/wildlife movement resolves outside battle; a static conventional confrontation opens only if a separate threat remains.

### Orchard Root Association Survey

No battle dependency is required. Pass 72 fungal records, Flora, Soil, Irrigation, IPM, Science and Metrology compare evidence. Combat cannot establish causation.

### Harvest Closure Dispute

No battle dependency is required. Monitoring, fruiting history, harvest records, Markets, Land Tenure, Public Memory and institutional authority can produce a decision or preserve uncertainty.

## Fungal-specific non-inferences

Current evidence does not authorize ambient spores as `Spore`; mushroom contact as Effect Spore; visible fungi as Sleep/Poisoned/Paralysis; fruiting patches as Rough Terrain/cover; particle clouds as powder Move geometry; mycorrhizae as healing/stat bonuses; deadwood fungi as structural failure; Parasect presence as proof of root disease; market mushrooms as local abundance; wild harvest as PTU Mushroom Item acquisition; loaded mushroom blocks as population truth; block removal as eradication; or chunk reload as ecological reset.

## Why current Move-special work does not solve the FULL encounters

Runtime-owned PRE/POST-damage seams do not provide survey history, fruiting state, substrate ecology, non-hostile movement policy, tactical environmental rules, objective-aware AI or Minecraft persistence. The adapter must not imitate those missing systems with custom Status or damage rules.

## PTU / Caelo boundary

Concrete PTU Mushroom/Spore/Effect Spore evidence exists in project sources, but each exact mechanic still requires its authoritative rule/runtime contract when invoked.

The complete primary Caelo corpus was not reliably exposed during this pass. Super PTU Online Helper was not available as an invocable capability. No missing Caelo foraging DC, mushroom rule, spore range or fungal hazard is invented.

## Narrative consequence

Pass 72 remains the fungal/decomposition authority. Pass 158 can immediately deepen it through multi-year monitoring, detectability records, fruiting episodes, occurrence-linkage assessments, sample provenance and harvest monitoring. Mechanically rich fungal encounters stay gated behind exact capability families and retain reduced static versions.
