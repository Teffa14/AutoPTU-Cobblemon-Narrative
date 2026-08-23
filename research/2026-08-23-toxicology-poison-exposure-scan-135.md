# Toxicology, Poison Exposure & Exposure-Route Research — Pass 135

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. External fiction and community material are inspiration sources, not rules authority.
Date: 2026-08-23

## Why this pass

The repository already has separate systems for Care, Outbreak/Health Surveillance, Air Quality, Waste/Sanitation, Food, Drinking Water, Research Ethics, Cases and environmental hazards. None of those layers owns the narrower question of toxic exposure: what substance or biological agent may have contacted a subject, by what route, at what time, with what evidence, and how that exposure should remain separate from diagnosis and PTU Status state.

This pass therefore researches toxicology as an evidence-and-world-state problem, not as a new damage system.

## Internal boundary found before research

`design/outbreak-health-surveillance-layer.md` already allows a health investigation to consider a `toxic` hypothesis, but it deliberately does not define a toxicology subsystem.

`design/care-recovery-welfare-layer.md` owns diagnosis/treatment records and explicitly prevents narrative observations from fabricating mechanical health state.

Air Quality, Waste, Drinking Water and Food may establish environmental or material source state. They should not themselves decide dose, diagnosis or PTU Poisoned.

The gap is therefore:

source/agent -> exposure opportunity -> route -> evidence -> exposure assessment -> clinical interpretation -> response -> later review.

## Pokémon sources

### Seviper — venomous delivery is specific behavior

Official Pokédex material describes Seviper as hiding in grass and striking prey with venomous fangs.

Reusable structure:

- a biologically hazardous substance may be associated with a specific delivery route;
- observed proximity to a venomous Pokémon is not the same as confirmed envenomation;
- fang marks, witnessed attack, residue, symptoms and clinical assessment are separate evidence layers.

Do not infer a universal venom dose, toxicity rating or automatic PTU Poisoned state from this Pokédex description.

Source:
https://www.pokemon.com/us/pokedex/seviper

### Salandit — inhaled gas, behavior and toxicity must remain separate

Official Pokédex material describes Salandit using toxic gas against prey. It also describes pheromone-laden gas in a different behavioral context.

Reusable structure:

- one species can produce more than one chemically relevant emission;
- behavioral influence, dizziness, toxicity and PTU Status effects must not be merged merely because the same species produces the agent;
- a gas plume can create an exposure investigation without automatically creating Poisoned, Confused, Flinched or another battle state.

Source:
https://www.pokemon.com/br/pokedex/salandit

### Croagunk — a toxin-producing organ does not imply ambient hazard

Official Pokédex material describes Croagunk inflating poison sacs and using a poison jab after producing an audible cue.

Reusable structure:

- possession of a toxin-producing organ is species behavior, not proof that every location occupied by the Pokémon is contaminated;
- a field observer can document warning behavior before any contact occurs;
- a known toxic species can still be innocent in a separate poisoning incident.

Source:
https://www.pokemon.com/uk/pokedex/croagunk

### Shiinotic — apparent sleep-inducing exposure needs a mechanics boundary

Official Pokédex material describes Shiinotic using spores that can put prey to sleep.

Reusable structure:

- a biological aerosol can be observed in world fiction;
- environmental exposure and PTU Sleep must remain separate unless the exact Move/Ability/rule is invoked by the authoritative engine;
- narrative field conditions must not silently recreate Spore or another Move.

Source:
https://www.pokemon.com/uk/pokedex/shiinotic

## PTU public rules references

### Poison Moves are exact mechanics, not a generic toxicology model

Public PTU rules references list specific Move behavior such as Poison Gas, Poison Fang, Toxic and Toxic Spikes. These are mechanically defined effects with exact targeting, frequency and Status consequences.

Reusable design lesson:

- if a battle effect is meant to Poison or Badly Poison, invoke the actual authoritative PTU mechanic;
- an environmental odor, venom trace, contaminated barrel, polluted stream or toxic plant does not inherit a Move's effect merely because both involve poison.

Source:
https://pturpg.wikidot.com/poison

Public PTU Core mirror for Move text:
https://anyflip.com/qloz/xgfq/basic/401-450

### Gas Mask demonstrates that some environmental toxin protection is explicitly authored

The public PTU Core mirror describes Gas Mask equipment as protecting breathing in toxic environments/heavy smoke and also interacting with a defined list of Moves.

Reusable design lesson:

- environmental protection can exist when an exact source rule defines it;
- the narrative layer should record whether the authoritative equipment state is present, but must not invent concentrations, durations or protection beyond the rule;
- one protection item is not proof of a complete environmental toxicology engine.

Source:
https://anyflip.com/deia/psdg/basic/251-300

## Live AutoPTU evidence

The current Python repository includes a phase coverage matrix with a regression test for `Badly Poisoned` damage escalating over time. It cites PTU Core status timing and confirms that poison is real battle state in the Python oracle.

Relevant source:
`PHASE_COVERAGE.md`

Current public repository:
https://github.com/Teffa14/AutoPTU

A recent AutoPTU public development post also notes tests for Toxic respecting Poison/Steel immunities and suppression. This is useful implementation evidence, not a replacement rules source.

Source:
https://www.reddit.com/r/PokemonTabletop/comments/1r0kqww/autoptu_update_data_overhaul_offline_ptu_engine/

Important boundary:

Python poison support does not establish an overworld exposure model. Java parity for the entire status lifecycle also remains incomplete.

## Toxicology references

### Exposure route matters

CDC's 2026 Toxicological Outbreak Investigation training distinguishes major exposure routes including ingestion, inhalation, injection and dermal contact. It also notes that route affects dose and the pattern of illness.

Reusable architecture:

- `agent present` and `subject exposed` are different states;
- the same source can generate different exposure records depending on route;
- dose/exposure uncertainty must be preservable rather than collapsed to a binary flag.

Source:
https://www.cdc.gov/environmental-health-studies/media/pdfs/2026/06/Module-2-Toxicological-Principles-2026-508.pdf

### Hazard and risk are different

WHO toxicology guidance distinguishes hazard from risk and treats risk as dependent on exposure conditions. It also distinguishes dose-response from dose-effect relationships.

Reusable architecture:

- a dangerous substance can exist without a subject receiving a harmful exposure;
- an exposure can be suspected without a known dose;
- two subjects can have different outcomes from apparently similar events;
- a visible source should not generate a universal severity score.

Source:
https://iris.who.int/bitstream/10665/66398/1/WHO_PCS_99.2_eng.pdf

## Community material and anti-patterns

A public PTU campaign-log thread includes extensive custom/homebrew status rewrites and severe poison concepts. It is useful as a warning that community campaigns often modify Status behavior aggressively.

Ouros rule:

Never treat community poison damage, severe-status tables or rewritten Features as PTU/Caelo authority. Preserve the idea that poison can create escalating tension, but mechanically cross-check every effect against the project's source material and live engine.

Source:
https://forums.giantitp.com/showsinglepost.php?p=22090680&postcount=2

## Reusable narrative structures

### 1. Source present, exposure absent

A toxic biological or industrial source exists, but evidence later shows nobody received a meaningful exposure.

Useful for false alarms, preparedness and institution-building without mandatory injury.

### 2. Shared symptom, different source

Several actors show similar observations but have different exposure histories. The apparent cluster fragments into separate causes.

Useful for avoiding one-cause mysteries.

### 3. Same source, different route

One event creates inhalation exposure for some actors, dermal contact for others and no contact for another group.

Useful for evacuation, triage and witness reconstruction.

### 4. Exposure confirmed, diagnosis unresolved

A subject definitely contacted an agent, but investigators do not yet know whether observed symptoms came from that exposure.

Useful for medical uncertainty without false certainty.

### 5. Agent identity revised later

A sample is initially classified broadly and later identified more specifically. The original observation remains valid.

Useful for Science, Metrology and Taxonomy integration.

### 6. Old exposure, delayed investigation

Years later, archive records, retained samples or a changed water/soil pattern reveal that an old incident deserves review.

Useful for Chronicle-heavy stories.

### 7. Pokémon scapegoat

A Poison-type or venomous Pokémon is blamed because it is visible near an incident. Timing or exposure-route evidence later weakens that hypothesis.

Useful for Cases, Urban Wildlife, Conservation and Public Memory.

### 8. Correct containment, wrong public interpretation

An institution closes a zone or uses protective equipment before a diagnosis is confirmed. The measure is precautionary, not proof that the worst rumor was true.

Useful for institutional credibility stories.

## Candidate system objects suggested by the research

- `TOXIC_AGENT_PROFILE`
- `TOXIC_SOURCE_EVENT`
- `EXPOSURE_OPPORTUNITY`
- `EXPOSURE_RECORD`
- `EXPOSURE_ROUTE`
- `EXPOSURE_ESTIMATE`
- `TOXICOLOGY_SAMPLE`
- `TOXICOLOGY_ASSESSMENT`
- `DECONTAMINATION_EVENT`
- `EXPOSURE_ADVISORY`
- `SOURCE_ATTRIBUTION_HYPOTHESIS`
- `EXPOSURE_RECONSTRUCTION`

These should remain world-state/evidence objects. They must not duplicate mechanical PTU Status state.

## Explicit non-inferences

Do not infer any of the following:

- Poison-type nearby -> source of poisoning;
- toxic agent present -> exposure occurred;
- exposure occurred -> harm occurred;
- symptoms observed -> cause known;
- venomous bite observed -> exact dose known;
- gas visible -> all actors inhaled it;
- contaminated water -> every consumer was exposed;
- environmental toxin -> PTU Poisoned;
- PTU Poisoned -> environmental contamination;
- Poison immunity in battle -> immunity to every environmental toxin;
- Gas Mask equipped -> universal immunity to all gases;
- Antidote exists -> every toxin has a simple antidote;
- cleanup completed -> clinical consequences are resolved;
- battle won -> decontamination or diagnosis completed.

## Source-status notes

Super PTU Online Helper was not exposed as an invocable capability during this run. No output is attributed to it.

The project's complete primary Caelo corpus was not available through the runtime in a form reliable enough to assert new Caelo-specific toxicology rules. Exact PTU/Caelo treatment, environmental toxin, antidote, Medicine and Status interactions remain unresolved until the primary project sources can be extracted directly.
