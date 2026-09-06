# Olfactory ecology and trace provenance scan — Pass 317

Status: RESEARCH / PROVENANCE
Date: 2026-09-06
Scope: narrative/world ecology research only; no canon mutation

## Why this pass exists

Passes 315 and 316 separated acoustic and visual/light evidence from ecological truth. Repository-wide inventory and targeted searches before writing found no existing Ouros research note or implementation contract centered on olfaction, scent trails, odor transport or chemical-trace provenance. Pass 317 therefore adds a third sensory axis without changing established canon.

The working evidence chain is:

`physical source or actor -> trace production/deposition -> environmental persistence/transport -> observer detection -> identity attribution -> interpretation`

Each link must remain separable. A detectable trace can outlive the actor that produced it, move away from its original location, become contaminated, or be detected by one species and missed by another. Conversely, failure to detect a trace does not establish absence.

## Existing project material checked

This pass follows inspection of the recursive repository tree, `CURRENT_FOCUS.md`, current canon/ecology material, Passes 307–316, existing evidence/provenance contracts and the live read-only AutoPTU-Java / AutoPTU heads.

The relevant existing invariants are preserved:

- NPC knowledge comes from observations, communication or other explicit provenance rather than hidden world state;
- environmental evidence can persist after the event that created it;
- Minecraft/Cobblemon presentation cannot manufacture ecology truth or PTU legality;
- PTU source mechanics and adopted Ouros contracts outrank community practice or narrative convenience;
- Caelo/Kairos material is reference-only unless an explicit project overlay adopts it.

## Public source findings

### Odor is a spatial and temporal information layer

A BioScience review proposes the concept of an `olfactory landscape`: odor can come directly from organisms or indirectly from deposited marks, feces, urine, vegetation, water, smoke and other sources, while wind and turbulence continually change its spatial distribution. The useful lesson for Ouros is that a scent observation has both source history and transport history.

Source:

- Webster et al., `Olfactory Landscape Concept: A Key Source of Past, Present, and Future Information Driving Animal Movement and Decision-making`, BioScience 72(8), 2022: https://academic.oup.com/bioscience/article/72/8/745/6618787

Reusable Ouros lessons:

- a trail may indicate previous presence rather than current position;
- a detected odor can be displaced from its source;
- repeated observations across space and time are stronger than a single detection;
- the simulator should preserve source, deposition time and transport context separately when those facts matter.

No real-world plume model, decay constant, wind equation or species threshold is imported as a game rule.

### Chemical signals can carry identity while remaining species/context dependent

USGS work on black-legged kittiwakes found experimentally detectable odors and later evidence of individual/sex signatures in preen chemistry. The important design lesson is not the bird biology itself; it is that chemical evidence can carry different classes of information and that those classes require validation rather than automatic interpretation.

Sources:

- USGS, `Can kittiwakes smell? Experimental evidence in a larid species`, 2009: https://www.usgs.gov/publications/can-kittiwakes-smell-experimental-evidence-a-larid-species
- USGS, `An individual and a sex odor signature in kittiwakes?`, 2011: https://www.usgs.gov/publications/individual-and-a-sex-odor-signature-kittiwakes-study-semiochemical-composition-preen

Reusable Ouros lessons:

- `trace detected` and `individual identified` are distinct claims;
- a species that can detect an odor does not automatically understand all information encoded in it;
- cross-species interpretation must be source-backed or remain uncertain.

### Human-centered smell assumptions are unsafe for non-human ecology

A Frontiers review on chemosensation warns against projecting human olfactory categories onto animals, especially in environments such as soil where chemical movement and sensing do not fit ordinary human experience cleanly.

Source:

- Frontiers in Ecology and Evolution, `Going belowground: burying anthropomorphic biases on gustation and olfaction`, 2023: https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2023.1231042/full

Reusable Ouros lessons:

- do not treat Minecraft/player-visible particles as a universal representation of what a Pokémon senses;
- do not assume all Pokémon perceive airborne and surface-bound traces the same way;
- aquatic, subterranean and terrestrial chemical sensing may require different authored evidence contracts.

### Pollution and contamination can alter chemical information

Recent ecology literature documents that contaminants can interfere with sensory cues or cause animals to respond to misleading chemical signals. Separate experimental work has shown particulate contamination can impair insect olfactory perception. Ouros should use the high-level pattern only: environmental change can affect trace production, transmission or detection.

Sources:

- `Advancing the Spatiotemporal Dimension of Wildlife–Pollution Interactions`, Environmental Science & Technology Letters, 2025: https://pubs.acs.org/doi/10.1021/acs.estlett.5c00042
- Wang et al., `Short-term particulate matter contamination severely compromises insect antennal olfactory perception`, Nature Communications, 2023: https://www.nature.com/articles/s41467-023-39469-3

Reusable Ouros lessons:

- apparent trail loss can be a detection problem rather than population loss;
- an anthropogenic odor may attract, repel, mask or confuse depending on species and context;
- contamination should be an authored causal possibility, never a generic global debuff.

No pollution dose, toxicity or physiological effect is imported.

### Official Pokémon material supports species-specific odor production and detection

The official Pokédex describes Slurpuff as able to distinguish extremely faint scents and using that sense in work with pastry chefs. Aromatisse can produce different scents, including scents that affect companions or opponents. These entries establish Pokémon-world precedent for strong olfactory specialization and biologically meaningful scent production without implying that every species has those abilities.

Sources:

- The Pokémon Company, official Pokédex, `Slurpuff`: https://www.pokemon.com/uk/pokedex/slurpuff
- The Pokémon Company, official Pokédex, `Aromatisse`: https://www.pokemon.com/uk/pokedex/aromatisse

Reusable Ouros lessons:

- sensory competence can be species-specific and narratively useful;
- producing a strong odor and interpreting another actor's trace are separate capabilities;
- species placement in Ouros remains a canon decision.

This pass does not place Slurpuff, Aromatisse or any other species in a region.

### PTU 1.05 has a specific Tracker capability

Publicly accessible PTU 1.05 text defines `Tracker` as a Pokémon Capability based on a strong sense of smell and gives explicit Perception-based procedures for following a known or newly detected scent. The same rules text states that `Odor Sleuth` grants Tracker if the user lacks it.

Sources:

- Pokémon Tabletop United 1.05 Core, capability section, public mirror: https://anyflip.com/qloz/xgfq/basic/301-350
- PTU community rules reference for `Odor Sleuth`: https://pturpg.wikidot.com/normal

Project implication:

- a full implementation must use the exact authoritative PTU/Caelo project source selected by the repository before numeric checks are coded;
- narrative scenes can safely say that a source-validated Tracker-capable Pokémon may attempt olfactory tracking;
- ordinary Perception alone must not be silently upgraded into universal scent tracking;
- `Odor Sleuth` cannot be given additional ecological or combat effects beyond verified semantics.

The external mirror is provenance for this research note, not a replacement for the project's authoritative PTU/Caelo source policy.

### Long-running PTU actual play supports recurring evidence and return loops

`Pokémon Rollout!` is a public PTU actual-play series with more than two hundred published episodes and continued releases in 2026. Its value to this pass is structural rather than textual: a campaign can maintain long-running relationships, locations and unresolved problems while still alternating between investigation, travel and battles.

Source:

- `Pokémon Rollout!`, public podcast listing: https://www.podchaser.com/podcasts/pokemon-rollout-238076

No character, dialogue, location, plot or encounter is imported.

### Contemporary fan puzzle design emphasizes evidence comparison instead of guessing

The 2026 fan browser project `PokéMystery` describes a loop in which players investigate locations, collect clues and compare evidence against Pokémon attributes before accusing a suspect. The useful abstraction is to make the player compare independent observations rather than simply activate a tracking interaction and receive a culprit.

Source:

- public developer post, 2026-08-25: https://www.reddit.com/r/pokemonbrowsergames/comments/1vxtpy6/

Ouros does not import its cases, suspects, UI, scoring or daily format.

## Reusable evidence model

A future olfactory observation record should be able to distinguish:

- candidate physical source;
- source identity confidence;
- trace type and source-backed sensory channel;
- deposition or first-observed time;
- sample/observation location;
- environmental context such as rain, airflow, substrate or machinery state when authored;
- contamination possibility;
- detector identity and verified sensory capability;
- raw detection result;
- tracking attempt result when PTU-authorized;
- cross-channel corroboration such as footprints, feeding traces, visual observation or camera evidence;
- interpretation claim and confidence;
- provenance for every derived conclusion.

A world simulator may know that a source deposited a trace. An ordinary NPC does not know that hidden fact unless they observed it or received evidence supporting it.

## Proposed narrative structures

### A trail with no matching footprints

A repeatedly detected odor trail crosses a managed corridor, but fresh footprints and feeding evidence do not match the expected crossings. The party must determine whether the scent represents current movement, an older deposited trace, transferred material, contamination or a real animal route that leaves little visible evidence.

### Carried trace

A maintenance cart, worker garment, shipping crate or reusable tool carries odor from one zone to another. A Tracker-capable Pokémon correctly follows the trace, but the initial human interpretation of what the trail means is wrong. The sensor succeeds while the investigator's causal model fails.

### Weather-separated revisit

The same route is checked before and after rain, a maintenance cycle or a wind-direction change. A trail that weakens, moves or vanishes provides evidence about persistence/transport without automatically identifying its source.

### Multi-sensor contradiction

Olfactory evidence suggests recent presence while visual/acoustic evidence suggests absence. The conflict becomes the quest. The resolution may be stale trace, changed activity timing, masking, a different individual/species, detector error or concurrent causes.

## PTU / Caelo / Kairos boundary

PTU Tracker/Odor Sleuth are relevant and must be validated against the project's authoritative source before implementation. No new Perception DC, duration, range, weather modifier, contamination rule, scent-field shape or odor status is introduced here.

Repository inspection did not establish an adopted Caelo olfactory overlay for this pass. Any Caelo-specific Tracker, Perception, Survival, scent, pollution or environmental modification remains `UNVERIFIED` until located and explicitly adopted.

Kairos remains reference material unless a project overlay says otherwise.

## Engine boundary

Existing verified targeting/range/LoS does not imply scent-based targeting or detection through walls. Existing base movement does not imply trail-following AI. A dynamic scent plume would be a zone/environment system with lifecycle and adapter requirements of its own.

AutoPTU-Java head inspected for this pass is `704722ffecbef9e003abe1870829843f29f029c7` (PR #385), which adds declarative round-window history state with Python-oracle parity for specific histories. This is narrow lifecycle evidence only. AutoPTU head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, whose current change is presentation-only.

## Canon boundary

This file is research only. It does not canonize a region, facility, orchard, species population, chemical ecology, detector species, pollution source, culprit, faction, NPC, numeric tracking rule or new condition.

Any adopted scenario must specify geography, stakeholders, species evidence and the exact PTU/Caelo authority used for mechanically meaningful scent tracking.