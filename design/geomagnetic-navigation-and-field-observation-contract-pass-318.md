# Geomagnetic navigation and field-observation contract — Pass 318

Status: DESIGN CONTRACT / NON-CANON MECHANICS BOUNDARY

## Purpose

This contract lets Ouros use compass disagreement, magnetic-field observations, and species-specific orientation evidence without turning an observation channel into omniscient world truth or silently inventing PTU battle mechanics.

It extends the provenance discipline already used for acoustic, light, and olfactory observations while keeping geomagnetic navigation as a distinct domain.

## Required state separation

The implementation must preserve five different layers.

### Physical route and location state

This is the authoritative world fact describing route nodes, edges, landmarks, surveyed markers, infrastructure, and actor positions. A compass reading never rewrites this layer by itself.

### Field state

This represents an authored magnetic condition at a location and semantic time. The source can remain unknown. The field state must not contain an omniscient cause label visible to ordinary NPC reasoning unless that cause has been established through evidence.

### Observation state

An observation records what a specific instrument, Pokémon, or observer actually produced or detected. It needs provenance: observer, place, time, channel, relevant device/species identity, reference/calibration state when applicable, result, and uncertainty.

### Knowledge state

An NPC can know an observation only after personally making it or receiving it through existing information infrastructure. World simulation data cannot leak directly into a KnowledgeLedger.

### Interpretation state

Claims such as "the route shifted," "the machine caused the anomaly," "a Probopass is nearby," or "the compass is faulty" are interpretations. They must remain separate from the underlying reading and retain their own provenance.

## Core invariants

1. `FIELD_DEFLECTED` does not mean `ROUTE_CHANGED`.
2. `INSTRUMENT_DISAGREEMENT` does not identify which instrument is wrong.
3. A valid reading can support an invalid geographic interpretation.
4. A known physical position does not imply that every actor knows that position.
5. A species-specific response does not authorize universal Pokémon magnetoreception.
6. Pokédex flavor does not implement PTU Move, Ability, Item, Feature, damage, movement, targeting, or status rules.
7. Minecraft client compass behavior, particles, sound, redstone state, or rendering cannot decide server-authoritative world truth.
8. Repeating an observation after a controlled state change can strengthen causal evidence but cannot silently establish intent, liability, ecological harm, or every downstream consequence.
9. Historical observations remain historical after a better explanation appears.
10. If multiple causes are authored, the evidence model must allow them to coexist rather than forcing one global culprit field.

## Minimal observation record

A future runtime can represent an observation with fields equivalent to:

- observation_id
- observer_id
- semantic_time
- world_location_ref
- observation_channel
- source_ref when known
- instrument_or_species_ref
- calibration_or_control_ref when applicable
- observed_value_or_class
- uncertainty_class
- provenance_root

The exact schema is not canonized by this document. The invariant is the separation of observation from interpretation.

## Suggested reduced-mode descriptors

The narrative layer may author descriptors such as:

- FIELD_BASELINE
- FIELD_DEFLECTED
- INSTRUMENT_AGREEMENT
- INSTRUMENT_DISAGREEMENT
- LANDMARK_ROUTE_CONFIRMED
- SOURCE_UNRESOLVED
- CONTROLLED_TEST_CHANGED
- CONTROLLED_TEST_NO_CHANGE

These are scenario/world evidence descriptors. They are not PTU statuses and must not enter the battle-status lifecycle.

## Species evidence boundary

Official Pokémon Pokédex material supports Nosepass as a compass-related Pokémon and Probopass as a Pokémon that emits a strong magnetic field. This justifies considering them during narrative authorship.

Before either species receives numeric navigation, sensing, disruption, movement, or combat behavior, the implementation must verify:

- the project's authoritative PTU source;
- any adopted Caelo overlay;
- the current engine contract for the relevant Move/Ability/Capability;
- regional/ecological canon establishing why the species is present.

No inferred rule may be added from flavor text alone.

## Full-version dependency boundary

Dynamic field zones depend on terrain/weather/hazards/zones/reactions and full turn/round lifecycle if they change during battle.

Any magnetic pull that changes positions depends on complete movement, including forced movement and any relevant interception/reaction semantics.

Any damage caused by electrical or impact hazards depends on the full stateful damage pipeline.

Any persistent battle condition depends on status lifecycle.

A magnetic Move depends on move-specific behavior.

Magnet Pull or another Ability depends on the Abilities family.

A compass or sensor with rules-level effects depends on Items.

A Trainer engineering/navigation specialization depends on Trainer Features/perks.

Autonomous tactical exploitation depends on both AI legal-action infrastructure and AI tactical policy; verified action enumeration alone does not establish the latter.

Minecraft/Cobblemon/Craftics presentation depends on adapter/playback support and must not duplicate rule authority.

## Reduced-version compatibility

The reduced version requires no dynamic field solver and no new AutoPTU rule family.

The world can keep a normal route graph and ordinary movement legality. Observation nodes can expose authored evidence between scenes. Landmarks and survey markers provide independent spatial anchors. A controlled infrastructure state change can be applied through authored world state. NPC knowledge advances only through personal observation or existing communication paths.

This preserves the mystery premise while the battle engine remains conservative.

## PTU / Caelo verification status

At Pass 318, repository inspection shows `sources/kairos` under the narrative repository's `sources/` directory. No adopted `sources/caelo` directory or indexed Caelo magnetic-navigation overlay was found. Repository search also did not establish a project-authoritative magnetic-navigation procedure.

Therefore all PTU/Caelo numeric magnetic-navigation behavior remains UNVERIFIED in this contract.

## Canon boundary

This design contract approves no location, faction, geology, infrastructure, species population, culprit, or final quest resolution. Companion research is provenance only. Companion proposal is explicitly PROPOSED / NON-CANON.