# Pass 126 Research — Olfactory Landscapes, Scent & Chemical Signals

Status: research/provenance notes only. Not Ouros canon. No mechanics are promoted by this file.

## Why this is a distinct gap

The repository already has Soundscapes, Lightscapes, Air Quality, Field Signs/Tracking, Urban Wildlife, Flora, Waste, Decomposition, Pokémon Agency and Social Learning. Field Signs already allows a `scent_trace`, but only as specialized evidence left by an actor. No current layer owns ambient odor fields, overlapping scent sources, chemical communication, odor baselines, olfactory masking, smell-based place identity or long-lived changes in the sensory landscape.

That makes olfaction a clean missing sensory layer rather than a duplicate of Tracking.

## Pokémon sources

### Spritzee — diet-dependent fragrance

Official Pokédex: https://www.pokemon.com/us/pokedex/spritzee

Reusable structure:

- one persistent Pokémon can produce different scent profiles over time;
- diet can change the observed fragrance without changing species or identity;
- smell observations can therefore become longitudinal evidence rather than a fixed species label.

Guardrail:

Do not convert diet into an automatic combat modifier, Healer activation, mood control or perfume economy rule.

### Aromatisse — strong and varied scents

Official Pokédex: https://www.pokemon.com/us/pokedex/aromatisse

Reusable structure:

- scent can be intense enough to affect how nearby actors perceive the environment;
- one individual can produce multiple odor classes;
- prolonged exposure can affect olfactory perception in the fiction.

Guardrail:

The Pokédex flavor does not authorize generic morale penalties, confusion, suppression, healing, status application or a radius in AutoPTU. Any such mechanic must come from verified PTU rules and Java parity.

### Slurpuff — specialized scent discrimination

Official Pokédex: https://www.pokemon.com/us/pokedex/slurpuff

Reusable structure:

- Pokémon can have authored olfactory specialization useful in work or investigation;
- professional roles can emerge from a sensory capability without requiring combat;
- a scent-sensitive Pokémon can help discriminate subtle differences without becoming an omniscient tracker.

Guardrail:

Do not infer exact detection range, identity certainty, hidden-object automation, Tracker capability, or bonus dice from Pokédex flavor.

### Stunky / Skuntank — odor as deterrence and disturbance

Official Pokédex:

- https://www.pokemon.com/us/pokedex/stunky
- https://www.pokemon.com/uk/pokedex/skuntank

Reusable structure:

- an odor source can change where other Pokémon choose to remain;
- an odor event can outlast the actor that created it;
- a settlement can experience a real nuisance or ecological displacement without the source being malicious.

Guardrail:

The official Ability `Stench` has a defined battle effect in Pokémon media, but overworld odor does not automatically become Flinch, Poisoned, Accuracy penalties, forced movement or a hazard zone in PTU.

### Skiploom — scent as geographic clue

Official Pokédex: https://www.pokemon.com/us/pokedex/skiploom

Reusable structure:

- experienced observers can sometimes associate scent with geographic origin;
- scent can connect Taxonomy, Migration and Biogeography;
- this remains an inference with uncertainty, not a universal geolocation mechanic.

## PTU / project-source evidence

AutoPTU project data exposes `Tracker` as a recognized capability in `PTUDatabase-main/PTUDatabase/Enums/OtherCapability.cs`. That confirms Tracker exists in the source corpus, but the inspected Java/Python repositories do not expose a general authoritative overworld olfaction system.

Relevant project path:

`PTUDatabase-main/PTUDatabase/Enums/OtherCapability.cs`

The prior Field Signs layer already enforces the correct boundary: no actor may use scent mechanically without verified PTU/Caelo authority for that actor; scent is not a coordinate feed; overlapping traces can be uncertain; and environmental degradation should not be improvised into unsupported DC math.

Pass 126 extends that principle from a single trace to an entire odor landscape.

## External ecological sources

### The olfactory landscape concept

Finnerty et al., 2022, BioScience. Public full text via PMC:
https://pmc.ncbi.nlm.nih.gov/articles/PMC9343233/

Useful high-level lessons:

- landscapes contain overlapping odor contours from food, predators, conspecifics, vegetation, water, smoke and decay;
- odor information is dynamic in both space and time;
- animals can use these cues when deciding where and when to move;
- the same location can present a different olfactory landscape after weather, disturbance, seasonal change or movement of odor sources.

Ouros adaptation:

Represent odor as a coarse, dynamic information layer. Do not simulate chemistry cell-by-cell.

### Scent marks persist after the sender leaves

Review of chemical/sensory characterization of scent markings:
https://pmc.ncbi.nlm.nih.gov/articles/PMC4003951/

Useful high-level lessons:

- scent marks can communicate when the sender is absent;
- marks can degrade due to rain and other environmental conditions;
- repeated marking can refresh a location without implying permanent ownership;
- chemical signals can carry different types of information, but interpretation requires evidence.

Ouros adaptation:

A scent mark can have its own identity, observation history and degradation state. It does not prove territory, dominance, mating state or individual identity unless the project has authored evidence for that species/population.

### Conservation relevance of chemical communication

Review summary:
https://www.sciencedirect.com/science/article/abs/pii/S0006320711001686

Reusable lesson:

Ignoring olfaction can distort how a species’ movement and habitat use are interpreted. For Ouros this supports sensory-diverse ecology: route choice, avoidance and site use do not need to be explained only by vision, sound or direct encounters.

## New design deductions for Ouros

1. Smell should be a first-class observation channel, not an automatic mechanical effect.
2. Odor source, odor event, propagation/extent, observer detection and observer interpretation must be separate records.
3. A smellscape needs baselines before anomalies can be claimed.
4. Scent marks persist after the maker leaves and may degrade independently of the maker’s current location.
5. Multiple odor sources can overlap and mask one another.
6. Odor can link ecological systems: flowering, decomposition, waste, wildfire smoke, markets, kitchens, waterways, urban wildlife and Pokémon behavior.
7. A scent-sensitive Pokémon can support an investigation without revealing world truth automatically.
8. Odor-management interventions can change wildlife use without being modeled as battle hazards.
9. A strong smell can be culturally meaningful, commercially useful, ecologically relevant or simply unpleasant; those are different states.
10. Minecraft presentation must never become the authority for smell because vanilla blocks/particles cannot represent the semantic source or certainty of an odor observation.

## Sources deliberately not converted into canon

No source here establishes:

- a regional Ouros perfume tradition;
- a universal scent language;
- territory rules;
- breeding pheromone mechanics;
- scent-based Friendship/Loyalty;
- automatic tracking bonuses;
- wild encounter attraction/repulsion formulas;
- Stench as an overworld radius;
- Sweet Scent behavior;
- Aroma Veil as ambient fragrance protection;
- Poisoned/Confused/Flinch from ordinary smell exposure.

All such material remains blocked until project canon and PTU/Caelo mechanics support it.

## Open mechanical questions

- Exact PTU/Caelo text for Tracker and any olfactory Perception rules.
- Whether Sweet Scent, Odor Sleuth, Stench, Aroma Veil, Sweet Veil or similar effects have implemented PTU behavior relevant outside battle.
- Which Pokémon receive olfactory capabilities from PTU data rather than Pokédex flavor.
- Whether Java needs a future semantic sensory context separate from LoS.
- How weather, water, doors, ventilation and indoor/outdoor boundaries affect smell in canon without creating unsupported simulation math.

## Super PTU Online Helper

No invocable Super PTU Online Helper capability was exposed in this runtime. No output was invented or attributed to it.