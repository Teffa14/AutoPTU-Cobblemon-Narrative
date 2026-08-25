# Engine Readiness Snapshot — Pass 158

Status: READ-ONLY EVIDENCE SNAPSHOT for narrative dependency planning.
Date: 2026-08-24

## New narrative authority

Pass 158 adds `design/fungal-ecology-mycology-spore-networks-layer.md` after a repository-wide keyword audit found no existing fungal/mycology authority. It is intentionally bounded by existing Flora, Soil, Decomposition, Forest Management, Interspecies Ecology, Toxicology, Food Safety, Taxonomy and battle authorities.

## Live heads inspected

- AutoPTU-Java main: `3caac611a987322a70dbdc34c56d613b96dadb92`
- AutoPTU Python main: `5ab2c175be6542b867f1676cf6848b9b15fd346f`

The Java head adds a runtime-owned POST-damage Move-special bridge carrying Python `damage_dealt` through move-special context. Recent preceding slices also add PRE-damage bridges, live PRE-damage execution, mutable move-special result state, a generic move-special registry and zero-damage Status Move execution.

This is meaningful progress for move-specific ordering and runtime ownership. It is not proof that all Status Moves, Spore/powder effects, Ability hooks, environmental spores, terrain, hazards or reactions exist.

The Python head is a Career resilience fix guarding repeated clicks during stalled battle retries. It does not change tactical readiness.

## PTU fungal/mechanical evidence inspected

Read-only AutoPTU search exposes:

- PTU/audit/item records containing `Tiny Mushroom` and related mushroom items;
- an `Effect Spore` Python hook path under `auto_ptu/rules/hooks/abilities/contact_effects.py`;
- Spore/powder Move data and status infrastructure in the project corpus.

This proves that mushrooms, Spore-family mechanics and Effect Spore are concrete PTU/runtime concepts. It does not authorize an overworld generic spore mechanic.

Therefore the fungal ecology layer may reference those exact mechanics as downstream dependencies but never synthesize them from ambient scenery.

## Permanent capability classification

### VERIFIED

- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

### PARTIAL

- full turn / round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features / perks.

### BLOCKING as complete families

- complete movement including push / pull / knockback / interception / forced movement;
- terrain / weather / hazards / zones / reactions;
- AI tactical policy;
- Minecraft / Cobblemon / Craftics adapter and playback.

The new Java POST-damage Move-special bridge does not promote any complete family.

## Pass 158 encounter dependency matrix

### Fruiting Chamber Survey — FULL

VERIFIED baseline:

- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

BLOCKING:

- complete movement if researchers or Pokémon must cross, withdraw, intercept or protect a moving route inside the grid;
- terrain/weather/hazards/zones/reactions if darkness, slick substrate, cave geometry changes or an environmental spore field must alter tactical state;
- AI tactical policy for `WITHDRAW`, `PROTECT_SAMPLE_ROUTE`, `CLEAR_ROUTE`, `REACH_EXIT`;
- Minecraft/Cobblemon/Craftics adapter/playback for researchers, sample points, world-state revisions and semantic objectives.

PARTIAL when invoked:

- status lifecycle if an actual Sleep/Poison/Paralysis mechanic is required;
- move-specific behavior if Spore, Sleep Powder, Poison Powder, Stun Spore or another exact Move is required;
- abilities if Effect Spore, Illuminate or another exact Ability is required;
- items if protective/sampling gear is represented as PTU battle Items;
- Trainer Features/perks if an exact Feature is invoked.

REDUCED version completes sampling/exposure handling in world state, removes researchers from battle and uses a static arena with no ambient spore, darkness or substrate mechanics.

### Deadwood Plot Disturbance — FULL

VERIFIED baseline remains available.

BLOCKING:

- complete movement for non-hostile withdrawal, crowd clearing or moving objectives;
- AI tactical policy for `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT_RESEARCH_SITE`;
- adapter/playback for visitors, plot boundaries and wildlife/world-state handoff.

Environmental family is needed only when exact terrain/hazard behavior is authored and mechanically verified.

REDUCED version resolves visitor and wildlife movement outside battle and opens a normal static confrontation only if a separate threat remains.

### Orchard Root Association Survey

No battle-engine dependency is required for the primary version.

Fungal Ecology, Flora, Soil, Irrigation, IPM, Science and Metrology can preserve competing hypotheses and evidence. The result may remain unresolved. Combat cannot establish fungal causation.

### Harvest Closure Dispute

No battle-engine dependency is required.

Fungal Ecology, Land Tenure, Markets, Public Memory, Science and institutional authority can resolve or defer the decision. Weak fruiting is not population collapse; closure is not proof of collapse.

## Fungal-specific engine non-inferences

Current evidence does not authorize:

- ambient spores as `Spore` Move;
- touching a mushroom block as Effect Spore contact;
- visible mushroom density as a Status zone;
- particle clouds as powder Move geometry;
- glowing fungi as Illuminate Ability;
- fungal growth as Poisoned, Sleep or Paralysis;
- fruiting patches as Rough Terrain or cover;
- mycorrhizae as healing/stat bonuses;
- decomposition as damage;
- deadwood fungi as automatic structural failure;
- Parasect presence as proof of plant/root disease;
- Amoonguss-like growth as confirmed Amoonguss causality;
- wild mushroom harvest as authoritative PTU Mushroom Item acquisition;
- loaded Minecraft mushroom blocks as fungal abundance;
- block removal as eradication;
- chunk reload as ecological reset.

## Why current Move-special work does not solve fungal encounters

The live Java runtime now has bounded PRE/POST-damage Move-special seams. Pass 158 FULL encounters are primarily gated by non-hostile movement objectives, environmental-state authority, tactical AI and Minecraft playback.

A Move-special seam cannot provide:

- mycelial or substrate state;
- fruiting history;
- spore ecology;
- scientific identification;
- harvest/access governance;
- non-hostile wildlife withdrawal policy;
- cave/forest environmental simulation;
- Minecraft ecological persistence.

The adapter must not imitate those missing systems with custom Status or damage logic.

## PTU / Caelo source boundary

Project evidence confirms concrete PTU mushroom, Spore/powder and Effect Spore concepts, but each exact rule still requires the project rules source/runtime contract when invoked.

The complete primary Caelo corpus was not reliably exposed during this pass. Super PTU Online Helper was not available as an invocable capability.

No missing Caelo foraging DC, mushroom rule, toxic-environment rule, spore range, forest modifier or fungal hazard was invented.

## Narrative implementation consequence

Fungal worldbuilding can advance immediately through persistent fungal-system IDs, observations, fruiting episodes, samples, ecological-role assessments, harvest records and non-combat investigations.

Mechanically rich fungal battles remain bounded behind exact capability families. Reduced versions preserve the same narrative premise without requiring Minecraft to duplicate PTU rules.
