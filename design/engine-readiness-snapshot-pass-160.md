# Engine Readiness Snapshot — Pass 160

Status: READ-ONLY EVIDENCE SNAPSHOT for narrative dependency planning.
Date: 2026-08-25

## Narrative authority added

Pass 160 adds `design/remote-sensing-aerial-imagery-change-detection-layer.md`.

This layer owns repeated remote acquisition, spatial coverage/obscuration, derived products, processing revisions, comparability and change-detection claims.

It does not replace Visual Records, Metrology, Cartography, Science, Airspace, Timekeeping, Research Ethics, environmental domain layers or PTU/Caelo rules.

Remote sensing remains overworld evidence state. It is not a battle targeting or perception subsystem.

## Live heads inspected

- AutoPTU-Java main: `2c83099de0f558a6e387f39174c0223f8e1668e6`
- AutoPTU Python main: `5f795fb7d55b87a8fb95433fb0d6661b981fbd93`

Java's newest inspected slice adds a runtime-owned `END_ACTION` move-special bridge and freezes Python aggregation/order behavior for that phase. The immediately preceding slices run POST_DAMAGE move specials in the live attack pipeline and preserve mutable move-special result state across defender reactions.

This is meaningful evidence for move-specific hook ordering and runtime ownership. It does not prove the complete Move catalog, full damage pipeline, complete reaction family, environmental systems, remote observation or Minecraft playback.

Python's newest inspected change fixes the GitHub Pages production build for Career. It does not change tactical readiness.

## Java README boundary

The live README still marks these large families as incomplete:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Recent move-special bridges are substantial plumbing progress but cannot promote the full hook families.

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

Pass 160 does not promote any category.

## Remote-sensing mechanical boundary

Current engine evidence does not authorize:

- remote imagery as combat LoS;
- aerial images as legal target lists;
- map overlays as Accuracy or initiative bonuses;
- remote heat signatures as Fire-type detection;
- vegetation products as Grassy Terrain;
- water classifications as Water Terrain, safe water or potable water;
- snow products as Ice-type bonuses;
- remote counts as encounter population truth;
- remote products as spawn modifiers;
- change polygons as tactical zones;
- survey platform range as Pokémon movement range;
- Minecraft render distance as acquisition coverage;
- Minecraft map pixels as scientific evidence;
- automatic identification from silhouettes or low-resolution imagery;
- a Rotom/Rotom Phone reference as generic sensing or network authority.

Any encounter that invokes an exact Move, Ability, Item, Status, Feature or Capability needs its own PTU/Caelo and runtime evidence.

## Encounter dependency matrix

### Remote Tower Retrieval — FULL

VERIFIED baseline:

- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

BLOCKING:

- complete movement if technician/retrieval actors must reposition through contested space, withdraw, cross or be intercepted;
- AI tactical policy for `REACH_DEVICE`, `PROTECT_TECHNICIAN`, `WITHDRAW`, `CLEAR_ROUTE`;
- Minecraft/Cobblemon/Craftics adapter/playback for technicians, survey equipment, semantic objectives and world-state handoff.

CONDITIONAL BLOCKING:

- terrain/weather/hazards/zones/reactions if storm debris, unstable ground or active weather changes tactical state.

CONDITIONAL PARTIAL:

- full turn/round lifecycle if objective state needs deeper multi-round battle semantics;
- full stateful damage pipeline for complete ordinary damage behavior;
- status lifecycle for an exact Status;
- move-specific behavior for an exact Move;
- abilities for an exact Ability;
- items for battle-semantic survey/protective equipment;
- Trainer Features/perks for an exact Feature.

REDUCED:

World state closes unsafe sectors, moves the technician outside the tactical fight and resolves equipment access separately. AutoPTU receives static safe geometry and only actual combatants. The retrieval resumes after battle.

### Change-Polygon Field Validation — FULL

VERIFIED baseline:

- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

BLOCKING:

- complete movement for `CROSS`, `WITHDRAW`, route protection or investigator movement inside the tactical grid;
- AI tactical policy for non-elimination objectives;
- adapter/playback for investigators, observation points and domain handoff.

CONDITIONAL BLOCKING:

- terrain/weather/hazards/zones/reactions when wetland water, mud, vegetation, shoreline instability or another environmental feature changes tactical rules.

CONDITIONAL PARTIAL:

- exact Status/Move/Ability/Item/Feature families only when explicitly invoked.

REDUCED:

Field observations and wildlife movement resolve outside battle. Any independent confrontation uses static geometry away from survey points and remote-sensing evidence stays outside the grid.

### Sensitive Roost Publication Incident — FULL

VERIFIED baseline:

- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

BLOCKING:

- complete movement for civilians/wildlife rerouting and withdrawal;
- AI tactical policy for `EVACUATE`, `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT_SITE`;
- adapter/playback for crowd state, protected-site semantics and handoff.

CONDITIONAL BLOCKING:

- terrain/weather/hazards/zones/reactions only if the protected site or current environment has validated tactical effects.

REDUCED:

Media/Conservation generalize the product, Travel closes or redirects access and civilians move outside battle. AutoPTU opens only after the sensitive site is clear.

### Processing Review Meeting

No battle-engine dependency.

Metrology, Science, Remote Sensing and the owning environmental layer can resolve to `SUFFICIENT_WITH_LIMITATIONS`, `REQUIRES_REPROCESSING`, `ARTIFACT_OR_PROCESSING_DIFFERENCE`, `INSUFFICIENT_COMPARABILITY` or `UNRESOLVED` without combat.

## Why targeting VERIFIED does not help remote sensing

The verified targeting family concerns legal battle geometry: range, areas, footprints, target anchors and line of sight inside authoritative battle state.

Remote acquisition coverage is a world-observation concept with different inputs:

- platform footprint;
- sensor/method capability;
- viewing geometry;
- timing;
- cloud/smoke/canopy/terrain obscuration;
- processing revision;
- spatial resolution;
- access policy;
- validation history.

Battle LoS must never be repurposed as aerial-image visibility or remote-sensor coverage.

## Latest move-special evidence

Java's recent sequence now includes:

- generic move-special registry work;
- mutable result preservation;
- PRE_DAMAGE runtime bridges and live execution;
- POST_DAMAGE runtime bridges and live execution;
- result preservation across supported defender reactions;
- `END_ACTION` runtime aggregation/order behavior.

This is strong architectural evidence that move-specific behavior is becoming more composable and runtime-owned.

It still leaves the permanent category `move-specific behavior` PARTIAL because coverage of representative seams and handlers is not coverage of every Move.

Likewise, reactions remain BLOCKING as a complete family even though several concrete reaction contracts exist.

## PTU/Caelo source boundary

No generic PTU remote-sensing mechanic was verified for Pass 160.

The public Pokémon material supports survey/exploration structures and elevated reconnaissance in Pokémon Legends: Arceus. That is narrative precedent, not a PTU rule.

Project evidence did not expose a complete primary Caelo rules corpus defining aerial imagery, sensor platforms, remote classification, automated identification or remote-sensing equipment.

Super PTU Online Helper was not exposed as an invocable capability in this runtime. No helper result is claimed.

Future use of Technology Education, Perception, Pokémon Education, Chronicler/Researcher-like Features, flight capabilities, equipment or Pokémon-assisted platforms requires exact validation against the project's rules source and live implementation.

## New overworld blockers / contracts

Pass 160 requires future world-state support for:

- remote observation program identity;
- acquisition-platform state;
- acquisition events and footprints;
- coverage/obscuration quality;
- source spatial products;
- processing revisions;
- derived spatial products;
- repeat-acquisition series;
- comparability assessments;
- change-detection claims;
- field-validation links;
- sensitive product access/generalization;
- owning-domain handoff;
- safe projection into Minecraft/map UI without inferring truth from render state.

These are world-system requirements. They do not belong in AutoPTU-Java battle rules.

## Why the reduced encounters are safe

The reduced versions keep survey platforms, technicians, imagery, classification, coverage, environmental interpretation, civilians, wildlife routing and sensitive-site management in world state.

AutoPTU receives only a conventional static confrontation after those elements are made safe.

That preserves the narrative premise while preventing the Minecraft adapter from inventing remote sensing, dynamic objectives, crowd AI, wildlife withdrawal, environmental hazards or unsupported PTU rules.