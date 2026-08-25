# Engine Readiness Snapshot — Pass 167

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-25
Narrative topic: passive acoustic monitoring, bioacoustic survey and automated detection review

## Read-only engine evidence inspected

### AutoPTU-Java

Inspected `main` head: `0566685bf0d84b2d41bbf0bb75185c6723dd0c44`.

Latest visible slice: `Port generic move-special effect-roll modifiers (#197)`. Java now has a parity-backed deterministic resolver for a set of Move Special secondary-effect roll modifiers including representative interactions such as Serene Grace, Stench, Firebrand, Effect Range modifiers, Mindbreak, Polished Shine, Brutal Training, Stat Stratagem and Hardened-related inputs. The fixture pipeline pins Python oracle behavior and keeps final roll authority inside the core runtime rather than the Minecraft adapter.

This is useful evidence for `move-specific behavior` and some interactions that touch Abilities/Trainer Features. It does not demonstrate complete Move Special coverage, complete Abilities, complete Trainer Features, the full damage pipeline, complete Status behavior, generic movement/reactions, environmental systems, tactical AI or adapter integration.

The live README continues to state that Python AutoPTU is authoritative while the Java port remains incomplete. It marks targeting, shift/jump legality, core PTU tables/calculations, typed action flow, initiative and legal action-space generation as implemented. It still lists full combatant/grid state, full damage, status controller, terrain, hazards, forced movement, reactions, remaining hook registries, full transcript parity, AI scoring/policy and Craftics/Cobblemon integration as unfinished.

### AutoPTU Python oracle

Inspected `main` head: `0bff7521ecb8b1163cbd5f366dea4651de83c353`.

Latest visible change is Career-facing draw presentation and explicitly preserves combat rules, AI, RNG, transcript and season resolution. It does not justify a tactical capability promotion.

The Python repository contains a broad Ability implementation/audit surface, but its own `ABILITY_HOOKS.md` states that code references are broader than test coverage. That remains a reason to treat `abilities` as PARTIAL rather than infer family completeness from individual implemented examples.

### PTU source evidence relevant to Pass 167

`audit_sources/Indices and Reference.txt` exposes `Blindsense` as a Special Capability. Its descriptive text allows heightened senses such as echolocation or increased hearing as possible manifestations, while the actual mechanical contract concerns functioning in darkness and immunity to Blindness. Pass 167 must therefore avoid turning descriptive echolocation into an invented distance, localization or recorder-equivalent rule.

The project also contains concrete Sonic/Soundproof-related data and keyword demos. These confirm that sound-linked PTU mechanics are specific rules objects. They do not authorize a generic acoustic-physics subsystem or make passive monitoring a combat mechanic.

No primary Caelo contract for passive acoustic recorders, automated call classifiers, hydrophone arrays, acoustic survey ranges or recorder equipment was recovered during this pass.

No result is attributed to Super PTU Online Helper because it was not available as an invocable capability.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Battle range, anchor geometry, areas, footprints and line of sight remain parity-backed. This cannot be reused as recorder coverage, hearing radius or acoustic propagation.

`base movement legality`

Current shift/jump legality remains verified at its existing boundary. It does not include the complete movement family.

`core calculations`

Core PTU tables and calculation primitives remain covered at the established verified boundary.

`action economy/initiative`

Typed action flow, action budgets and deterministic initiative/declared-action ordering remain covered.

`AI legal-action infrastructure`

The engine can enumerate and filter legal battle choices. It does not supply ecological or research objectives.

### PARTIAL

`full turn/round lifecycle`

Many lifecycle seams exist, including delayed effects and Move Special phase work, but the whole lifecycle remains unproven.

`full stateful damage pipeline`

Damage primitives and ordering slices exist. The Java README still explicitly lists full damage resolution as unfinished.

`status lifecycle`

Representative application, prevention and Status Move contracts exist. The complete status controller remains unfinished.

`move-specific behavior`

This family has substantial recent progress: PRE_DAMAGE, POST_DAMAGE and END_ACTION bridges; multi-target execution; Status Move plumbing; mutable result transport/aggregation; follow-up Move seams; and now generic secondary-effect roll modifiers. Full catalogue parity is not demonstrated.

`abilities`

Representative Ability behavior exists in Python and multiple parity-backed slices exist in Java. Full catalogue parity remains unproven.

`items`

Representative Item behavior exists. Complete item coverage remains unproven.

`Trainer Features/perks`

Generic gating, resource, target, effect and bookkeeping infrastructure plus representative effects exist. Full catalogue execution remains unproven.

### BLOCKING

`complete movement including push/pull/knockback/interception/forced movement`

Narrow reaction movement and push/redirect contracts exist, while the README still explicitly lists forced movement as unfinished.

`terrain/weather/hazards/zones/reactions`

The complete family remains BLOCKING. Individual reaction and field slices do not demonstrate terrain, Weather, hazards, zones and reactions as a complete coherent system.

`AI tactical policy`

Legal actions exist; goal-aware policies for `WITHDRAW`, `REACH_DEVICE`, `PROTECT_TECHNICIAN`, `CLEAR_ROUTE`, `SEARCH`, `REACH_EXIT` and other non-standard objectives remain unfinished.

`Minecraft/Cobblemon/Craftics adapter/playback`

The README still places integration after a parity-safe vertical slice. Minecraft cannot own PTU rules or passive-acoustic science state.

## Pass 167 overworld readiness

Passive acoustic monitoring itself is an overworld/science protocol and can advance without AutoPTU.

Required world-state contracts include:

- persistent passive-acoustic program identity;
- versioned method and site-selection history;
- recorder deployment identity;
- scheduled and realized recording effort;
- device uptime and data gaps;
- raw recording integrity linkage back to Soundscapes;
- detector/model revision provenance;
- candidate-detection state;
- review history and source-attribution uncertainty;
- duplicate-event linkage;
- target-specific coverage revisions;
- scoped non-detection assessment;
- detection-series comparability;
- sensitive-location publication transforms;
- Soundscapes -> Passive Monitoring handoff;
- Metrology -> device/calibration handoff;
- Timekeeping -> timestamp quality handoff;
- Research Ethics -> deployment/site authorization handoff;
- Science -> interpretation/publication handoff;
- Minecraft presentation boundary.

None of these contracts should be inferred from loaded entities, audible client sounds or battle geometry.

## Encounter dependency matrix

### Recorder Array Retrieval After Storm — FULL

- targeting/footprints/range/LoS: VERIFIED for ordinary battle targeting only.
- base movement legality: VERIFIED.
- complete movement: BLOCKING for technician/wildlife traversal, withdrawal, interception or dynamic repositioning.
- core calculations: VERIFIED.
- action economy/initiative: VERIFIED.
- full turn/round lifecycle: PARTIAL.
- full stateful damage: PARTIAL.
- status lifecycle: PARTIAL when exact combat statuses are invoked.
- terrain/weather/hazards/zones/reactions: BLOCKING if storm debris, unstable ground or weather changes tactical state.
- move-specific behavior: PARTIAL.
- abilities: PARTIAL.
- items: PARTIAL.
- Trainer Features/perks: PARTIAL.
- AI legal-action infrastructure: VERIFIED.
- AI tactical policy: BLOCKING for `WITHDRAW`, `PROTECT_TECHNICIAN`, `REACH_DEVICE`, `CLEAR_ROUTE`.
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED: world state resolves storm access, technicians, wildlife and device positions. Any independent confrontation occurs on a stable static arena. Recorder validity and recovery resolve afterward.

### Rare Call Alert at Chorus Marsh

Core investigation is non-combat and needs no battle capability. It may resolve as a validated acoustic pattern with unresolved source attribution.

If an independent battle occurs, use only the permanent capability families actually required by that battle. The recording itself grants no combat effect.

### Ultrasonic Cave Survey — FULL

- targeting/footprints/range/LoS: VERIFIED for battle, not acoustic localization.
- base movement legality: VERIFIED.
- complete movement: BLOCKING if survey actors/wildlife must cross or withdraw tactically.
- core calculations: VERIFIED.
- action economy/initiative: VERIFIED.
- lifecycle: PARTIAL.
- damage: PARTIAL.
- status lifecycle: PARTIAL if a specific legal sound-based effect applies a Status.
- terrain/weather/hazards/zones/reactions: BLOCKING if cave acoustics, unstable terrain or darkness becomes a tactical system.
- move-specific behavior: PARTIAL for any exact Sonic Move.
- abilities: PARTIAL for any exact sound-related Ability.
- items: PARTIAL.
- Trainer Features/perks: PARTIAL.
- AI legal-action infrastructure: VERIFIED.
- AI tactical policy: BLOCKING for `SEARCH`, `WITHDRAW`, `REACH_EXIT` and non-hostile movement goals.
- adapter/playback: BLOCKING.

REDUCED: instrument readings, source hypotheses and wildlife movement resolve outside battle. Any confrontation uses a static validated arena and only explicit legal combat effects.

### Hydrophone Mooring Recovery — FULL

- complete movement: BLOCKING for underwater traversal and dynamic withdrawal.
- terrain/weather/hazards/zones/reactions: BLOCKING if current, depth or debris affects combat.
- AI tactical policy: BLOCKING for `RETRIEVE_DEVICE`, `WITHDRAW`, `PROTECT_DIVER`.
- adapter/playback: BLOCKING.
- all normal battle families retain the permanent VERIFIED/PARTIAL map above.

REDUCED: Freshwater/Maritime world state resolves access and recovery. Any battle occurs separately on a static arena. A missing signal remains an evidence gap.

## What the new Java slice does not prove

The effect-roll modifier contract does not prove:

- acoustic classifier confidence;
- hearing or recorder ranges;
- sound propagation;
- ambient Sonic effects;
- full Serene Grace/Stench/Trainer Feature catalogue parity;
- complete secondary-effect handling;
- full reaction coverage;
- environmental sound zones;
- passive acoustic survey automation;
- Pokémon identification from audio;
- individual counting from calls;
- Minecraft audio authority.

The effect-roll resolver is a battle-rule contract. It must not be reused to score scientific detector confidence.

## Prohibited shortcuts

- battle LoS -> recorder coverage;
- battle range -> hearing radius;
- Sonic keyword -> acoustic detectability;
- Soundproof -> mundane deafness;
- Blindsense -> exact echolocation map;
- automated candidate -> validated observation;
- validated call -> confirmed source species;
- repeated detections -> individual count;
- many recorders -> many individuals;
- no detections -> absence;
- loud recording -> near source;
- client audio volume -> world acoustic measurement;
- loaded Pokémon count -> acoustic abundance;
- rare call -> spawn or capture eligibility;
- recorder block destroyed -> scientific history erased.

## Promotion decision

No permanent capability category is promoted in Pass 167.

Java head `0566685bf0d84b2d41bbf0bb75185c6723dd0c44` adds meaningful parity-backed evidence for Move Special effect-roll modifiers, but the live README still identifies the large unfinished systems directly. The conservative permanent capability map remains appropriate.