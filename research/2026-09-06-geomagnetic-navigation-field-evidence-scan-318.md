# Pass 318 research — geomagnetic navigation and field evidence

Status: RESEARCH / PROVENANCE ONLY / NOT CANON

Date: 2026-09-06

## Why this scan

Passes 315–317 already established separate observation contracts for acoustic masking, artificial light, and olfactory traces. Repository search found no equivalent research or design contract centered on magnetic orientation, compass disagreement, geomagnetic field evidence, or navigation errors caused by field interpretation. This scan therefore explores a distinct worldbuilding axis rather than extending the same sensory premise again.

The useful Ouros question is not "does magnetism exist?" It is: what can an observer legitimately conclude when mapped geometry, landmarks, instruments, infrastructure, and a Pokémon's species-specific orientation cues disagree?

## External source scan

### Animal magnetoreception and interpretation uncertainty

Source: "Sense of doubt: inaccurate and alternate locations of virtual magnetic displacements may give a distorted view of animal magnetoreception ability" (2023), open-access review in PMC.
https://pmc.ncbi.nlm.nih.gov/articles/PMC9941108/

Reusable structure:
- Animals in multiple taxa can use geomagnetic information, but experiments can be overinterpreted when the sensory parameters actually available to the animal are uncertain.
- A magnetic signature need not correspond uniquely to one geographic position.
- Experimental evidence can therefore support an observed response without uniquely proving the researcher's location hypothesis.

Ouros transformation:
- Separate field state, sensor response, actor knowledge, and geographic interpretation.
- A deflected compass or orientation response can be a valid observation while the conclusion "the route moved" remains wrong.
- Do not grant universal magnetoreception to Pokémon species.
- Do not translate real-world magnetic sensitivity, field strength, or biological thresholds into PTU numbers.

Additional review: "On the evolutionary trail of MagRs" (2024), open access in PMC.
https://pmc.ncbi.nlm.nih.gov/articles/PMC11298677/

Reusable structure:
- Magnetic orientation has been studied across marine, terrestrial, and aerial animals.
- Navigation can combine geomagnetic cues with other information rather than requiring a single infallible compass sense.

Ouros transformation:
- Cross-check magnetic evidence with landmarks, prior surveys, route geometry, time, and independent observations.
- Conflicting channels are a mystery generator rather than automatic proof that one channel is false.

### Official Pokémon species evidence

Source: official Pokémon Pokédex — Nosepass.
https://www.pokemon.com/br/pokedex/nosepass

Directly useful canon-level franchise evidence:
- Nosepass is categorized as the Compass Pokémon.
- Its nose functions as an accurate compass in the cited Pokédex entry.
- The entry also associates increased magnetism with attraction of nearby iron objects when endangered.

Source: official Pokémon Pokédex — Probopass.
https://www.pokemon.com/uk/pokedex/probopass

Directly useful canon-level franchise evidence:
- Probopass is categorized as the Compass Pokémon.
- The cited entry describes a strong magnetic field capable of disrupting nearby electrical appliances.
- It controls its Mini-Noses through magnetic force.
- Its listed Magnet Pull ability is explicitly magnetic.

Ouros transformation:
- Nosepass can become a candidate species for a field-survey story because official material supports a compass relationship.
- Probopass can become a candidate source of localized interference if the story later needs a biological source.
- These facts do not establish PTU implementation, ranges, magnitudes, automatic navigation checks, device-disruption mechanics, forced movement, or combat effects.
- Species inclusion remains proposed until regional ecology and PTU/Caelo authority are checked.

### PTU long-form campaign structure

Source: Pokémon Adventures in the Millennium, public podcast listing.
https://podcasts.apple.com/au/podcast/pokemon-adventures-in-the-millennium/id1412810716

The listing identifies an 87-episode Pokémon Tabletop United actual play organized into multiple named acts, running from 2018 through 2025.

Reusable structure:
- A campaign can divide long continuity into thematic acts while preserving the same party and world.
- Investigation, travel, science-themed material, and escalating arcs can coexist across a durable campaign rather than being compressed into one dungeon.

Ouros transformation:
- A navigation anomaly can first appear as a small survey problem, then reappear later when a new route, industrial project, migration, or field study depends on the same terrain.
- The anomaly should create reusable world state rather than a one-shot puzzle reset.

No characters, dialogue, episode plots, locations, or distinctive story content are imported.

### Wayfinding and environmental legibility

Source: Game Developer, "No More Wrong Turns."
https://www.gamedeveloper.com/design/no-more-wrong-turns

Reusable structure:
- Distinctive landmarks help players identify where they are in non-linear spaces.
- Navigation becomes easier when areas have recognizable identity independent of a map marker.

Source: Game Developer, "Navigation and Wayfinding in a Dark Game — Part 1."
https://www.gamedeveloper.com/design/navigation-and-wayfinding-in-a-quot-dark-game-quot-part-1

Reusable structure:
- Large, memorable environmental forms can anchor navigation even when visibility and route complexity are constrained.
- Layered environmental dressing can communicate progression and function.

Ouros transformation:
- A magnetic-navigation mystery must preserve non-magnetic ways to establish position: skyline, watercourse, rock formation, surveyed marker, built structure, or known junction.
- The player should be able to reason about disagreement between channels. The puzzle must not reduce to following a deliberately broken compass until a hidden trigger fires.

## Reusable Ouros design lessons

### 1. Position and orientation are separate facts

A character can know where a landmark is while holding an instrument that points somewhere unexpected. The route graph does not move merely because a compass disagrees with it.

### 2. A sensor reading needs provenance

Useful observation data should retain:
- observer,
- location,
- semantic time,
- instrument or species source,
- calibration/reference state where relevant,
- observed direction or anomaly class,
- environmental context,
- confidence/uncertainty,
- interpretation as a separate claim.

### 3. A magnetic signature need not identify one cause

Plausible authored causes can include:
- local ferromagnetic geology,
- buried or active infrastructure,
- a machine or electromagnet,
- a faulty or magnetized instrument,
- a species-specific Pokémon source,
- a bad survey assumption,
- concurrent causes.

Do not select one as canon merely because it supports the quest structure.

### 4. Calibration is gameplay

A known landmark or surveyed marker can serve as a control observation. If a compass behaves normally there and deflects only near one sector, the player has learned something stronger than "the compass is weird." If two devices disagree, instrument error becomes plausible. If a Nosepass and a mechanical compass agree while visual landmarks disagree, the hypothesis space changes again.

### 5. Controlled state changes create stronger evidence

If an authored machine can be safely powered down between scenes, repeating the same observation can establish correlation. Correlation still does not by itself prove intent, liability, ecological harm, or every downstream consequence.

### 6. Pokémon evidence remains species-specific

Official Pokédex evidence supports Nosepass/Probopass as candidates. It does not authorize a universal magnetic sense for Rock, Steel, Electric, Flying, migratory, or otherwise convenient Pokémon.

## PTU / Caelo cross-check status

The narrative repository's `sources/` directory currently exposes `sources/kairos` only. Repository search found no adopted Caelo source directory and no indexed project rule text establishing magnetic-navigation checks, compass equipment rules, Magnet Pull world effects, or Nosepass/Probopass travel mechanics.

Therefore:
- franchise biological/theme evidence: SOURCE-BACKED for Nosepass/Probopass;
- PTU numeric/navigation procedure: UNVERIFIED in this pass;
- Caelo override/overlay: UNVERIFIED;
- Magnet Pull combat/world implementation: must remain dependent on the Abilities capability family unless verified by current engine contracts/tests;
- any item or Trainer Feature that modifies navigation: must remain dependent on its own capability family.

No PTU number, DC, range, duration, accuracy modifier, movement rule, device-disruption radius, or magnetic-force formula is authored here.

## Canon boundary

This file changes no canon. It proposes no region placement, responsible institution, geological fact, species population, culprit, infrastructure owner, or final explanation.

The companion proposal may use a generic survey corridor so the idea can be evaluated without silently attaching it to an established settlement or faction.