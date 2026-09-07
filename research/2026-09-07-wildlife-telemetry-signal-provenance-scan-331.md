# Wildlife Telemetry, Signal Provenance & Tracking Uncertainty Scan — Pass 331

Status: RESEARCH / PROVENANCE. Not Ouros canon.
Date: 2026-09-07

## Repository inspection before research

The current recursive repository tree at `c042c9d6262f13382c238d417f65bdf7941cb397` was inventoried before authoring. `CURRENT_FOCUS.md`, canon governance, the latest readiness snapshot, recent environmental/investigation passes and repository-wide searches for telemetry, radio collars, tracking tags, directional receivers, wildlife tags and triangulation were reviewed.

No dedicated wildlife-telemetry or tracking-device provenance workstream was found. Existing communication systems remain about information delivery between actors and institutions; they do not make a wildlife transmitter an authoritative statement about the current location, health or intent of the tagged Pokémon.

Canon remains untouched. This file is research only.

## Public research sources

### U.S. Geological Survey — releasable GPS radio collars

Source: https://www.usgs.gov/publications/testing-releasable-gps-radiocollars-wolves-and-white-tailed-deer

Reusable lessons:

- telemetry devices can produce many useful locations while still missing a substantial fraction of attempted fixes;
- collar release mechanisms can fail;
- antennas can fail or be attached incorrectly;
- battery life and sampling frequency create tradeoffs;
- device state and animal state must remain separate facts.

Ouros abstraction:

`DEVICE_REPORT != ANIMAL_TRUTH`

A valid transmitter identity does not guarantee a fresh location. A missing fix does not prove absence. A stationary transmitter does not by itself prove that the tagged Pokémon is stationary.

### U.S. Geological Survey — GPS fix success and accuracy under forest cover

Source: https://www.usgs.gov/publications/fix-success-and-accuracy-gps-radio-collars-old-growth-temperate-coniferous-forests

Reusable lessons:

- canopy, terrain and satellite view can influence whether a fix is obtained;
- error and data loss can vary by habitat, season and time of day;
- missing data can bias interpretations of habitat use;
- some location errors can be large enough to change which feature appears to contain the animal.

Ouros abstraction:

A dataset can be internally authentic and still provide an incomplete or spatially biased model of movement. NPCs should distinguish raw observations, device-quality metadata, derived tracks and interpretation.

### U.S. Geological Survey — screening GPS telemetry errors

Source: https://www.usgs.gov/publications/gps-telemetry-location-error-screening-beneficial

Reusable lessons:

- aggressive filtering can remove bad points while also discarding substantial real information;
- environmental context may explain error better than a single quality metric;
- cleaning a dataset can create its own bias.

Ouros abstraction:

`FILTERED_TRACK != COMPLETE_TRACK`

A researcher can improve confidence in a dataset while simultaneously reducing coverage. A public map generated from filtered data therefore needs provenance back to the underlying observations and filter policy.

### U.S. National Park Service — radio telemetry bearings

Source: https://www.nps.gov/samo/learn/nature/bobcattelemetry.htm

Reusable lessons:

- radio telemetry uses a transmitter, directional receiver and signal strength;
- one bearing gives a direction, not a unique location;
- multiple bearings from different positions can be combined to estimate a location;
- receiver position and observation time matter.

Ouros abstraction:

A field observation should record observer position, time, bearing or signal-strength result and device identity. A triangulated estimate is derived evidence rather than direct sighting.

### U.S. National Park Service — telemetry for long-term wildlife movement

Source: https://www.nps.gov/articles/white-tailed-deer-movement-study.htm

Reusable lessons:

- collars can combine stored GPS observations with radio transmitters used for field monitoring;
- devices can be designed to release after a study interval;
- movement data becomes useful when compared across longer-term ecological monitoring rather than treated as isolated points.

Ouros abstraction:

A transmitter can outlive the decision that originally placed it, and a study can create obligations for retrieval, archiving, follow-up and public explanation.

### Pokémon official material — Pokémon Ranger

Source: https://www.pokemon.com/it/videogiochi/pokemon-ranger-tracce-di-luce

Reusable high-level structure:

Pokémon Ranger supports a world where people perform explicit field missions to protect Pokémon and environments, use specialized equipment, maintain contact with other staff and revisit environmental problems as assigned work.

Ouros use:

Reuse the mission structure only: field assignment, specialized observation equipment, institutional contact, evidence return and follow-up. Do not copy Oblivia, characters, villains, Styler mechanics, Guardian Signs, mission layouts or dialogue.

### PTU community source — Kehalo Isles Expeditions

Source: https://www.reddit.com/r/westmarches/comments/1gf7nvx

The public recruitment post describes a Pokémon Tabletop United living-world server focused on storytelling, discovery, exploration and community-driven play across multiple seasons.

Reusable high-level structure:

- discoveries can enter a shared persistent world rather than vanish with one party;
- one expedition can create information that affects later groups;
- exploration can be a primary activity instead of merely travel between battles.

Ouros use:

Use only the persistent-expedition pattern. Do not copy region identity, custom Pokémon, server lore, homebrew rules or story material.

## Design synthesis for Ouros

Telemetry is useful because it creates evidence that is neither omniscient nor useless.

A durable observation chain can be:

`tagged subject identity -> device identity -> device state -> raw transmission/fix -> field receiver observation -> derived location estimate -> analyst interpretation -> explicit recipient -> institutional decision -> follow-up observation`

Every arrow can fail independently.

Important separations:

- `TAGGED_POKEMON_IDENTITY != DEVICE_IDENTITY`
- `DEVICE_TRANSMITTING != DEVICE_ATTACHED`
- `DEVICE_LOCATION != SUBJECT_LOCATION`
- `NO_FIX != SUBJECT_ABSENT`
- `STRONG_SIGNAL != EXACT_LOCATION`
- `DERIVED_TRACK != RAW_OBSERVATION_SET`
- `TRACK_GAP != TELEPORTATION`
- `LAST_KNOWN_POSITION != CURRENT_POSITION`
- `COLLAR_RECOVERED != SUBJECT_RECOVERED`
- `STATIONARY_SIGNAL != MORTALITY_CONFIRMED`

## Narrative opportunities

### Misleading stationary signal

A transmitter remains in one feature while the tagged Pokémon has moved elsewhere. Plausible causes include a scheduled release, snagged equipment, damaged fastening, deliberate researcher removal or a device retained after treatment. The mystery concerns provenance before causality.

### Missing-fix corridor

Repeated GPS gaps occur in one terrain band. Researchers initially infer avoidance. Field observation later shows the population using the area while canopy or terrain reduces fix success. The correction changes a habitat map and possibly an infrastructure decision.

### Two valid datasets

Radio bearings collected by field crews and delayed GPS uploads disagree because they refer to different times or have different uncertainty. Both teams can be competent.

### Retrieval obligation

A detached device becomes a persistent world object. Recovering it may reveal stored data, close a permit obligation, update a study archive or correct a public movement map.

### Data-filtering dispute

One analyst removes low-confidence fixes and publishes a clean movement corridor. Another preserves them with uncertainty flags. The disagreement is methodological rather than villainous.

## Battle implementation boundary

Telemetry itself is world-state evidence and does not require a battle mechanic.

A mechanically rich field encounter could later include a fleeing Pokémon, moving observers, unstable terrain, line-of-sight loss, rescue, interception, weather effects, delayed environmental changes or a protect-the-equipment objective. Those concepts must remain gated by the permanent engine capability families.

Reduced implementation:

- use static authored terrain;
- resolve telemetry observations before or after combat as semantic world events;
- use ordinary verified targeting/range/LoS only where no special visibility rule is needed;
- use ordinary base movement only;
- keep the tagged subject's persistent world identity outside the Minecraft entity lifecycle;
- never let adapter pathfinding or rendering decide the subject's canonical movement history.

## PTU / Caelo source boundary

The inspected narrative repository continues to expose comparative material under `sources/kairos`. No adopted `sources/caelo` rules source was found in the current source inventory.

This pass therefore defines no numerical rules for tracking, Perception, Survival, Technology Education, signal range, device accuracy, concealment, pursuit, capture, movement, weather interference, Moves, Abilities, Items or Trainer Features.

Public wildlife science and Pokémon/PTU community material support narrative structure only. Mechanical authority remains with the project's adopted PTU/Caelo/AutoPTU evidence.

## Copyright boundary

No protected dialogue, named plotline, encounter map, distinctive character or campaign storyline is copied. Research sources are preserved for provenance while Ouros material uses transformed structural lessons only.
