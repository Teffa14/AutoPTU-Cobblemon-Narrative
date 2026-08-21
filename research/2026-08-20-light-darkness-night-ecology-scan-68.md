# Pass 68 Research — Light, Darkness, Night Ecology and Illumination

Status: RESEARCH ONLY. Not canon. Not a mechanics source.
Date: 2026-08-20

## Why this pass exists

The repository already has dedicated systems for soundscapes, astronomy, seasonality, meteorology, technology, settlements, travel and ecology. It does not yet have one authoritative narrative layer for light itself.

This pass studies:

- natural darkness;
- artificial light at night;
- biological light;
- beacon and navigation light;
- lighting infrastructure;
- night visibility;
- nocturnal ecology;
- light-based communication;
- darkness as exploration pressure;
- light pollution;
- the boundary between visual presentation and PTU mechanics.

The key design problem is that Minecraft can render darkness and light very easily, but visual brightness must not silently become PTU accuracy, Blinded, stealth, perception or encounter rules.

## Internal repository overlap review

Existing layers already own adjacent concerns:

- `astronomy-celestial-observation-layer.md` owns sky events, celestial visibility and observatory state;
- `soundscapes-acoustic-ecology-layer.md` owns acoustic information and sound cues;
- `seasonality-calendar-phenology-layer.md` owns day length and seasonal timing;
- `technology-energy-infrastructure-layer.md` owns electrical networks and technical assets;
- `architecture-built-environment-adaptive-reuse-layer.md` owns physical structures;
- `conservation-protected-areas-stewardship-layer.md` owns habitat management;
- `wild-collective-agency-layer.md` and `interspecies-ecological-relations-layer.md` own wild behavior and ecological relations;
- `accessibility-participation-accommodations-layer.md` owns alternative information channels and accessibility.

This pass therefore focuses on light-state provenance and its ecological, cultural and operational consequences.

## Source scan

### 1. PTU official Gym design — darkness can be a real tactical condition

Source:
https://pokemontabletop.com/gym-design-signature-elements/

The PTU blog presents a Gym where Darkvision, Blindsense or an external light source such as the Glow Capability is needed along certain routes to avoid being Blinded. Torches can go out as combatants faint, making the arena progressively darker.

Reusable design lessons:

- darkness can be an authored battlefield state;
- the relevant counterplay can depend on exact capabilities;
- lighting can change during an encounter;
- visibility should be treated as a rules-bearing state only when the governing rules actually define it;
- a Pokémon seeing in darkness does not imply its Trainer automatically sees the same information.

Important boundary:

This public PTU example is evidence that exact darkness mechanics exist in PTU contexts. It does not authorize a generic Ouros rule that every visually dark Minecraft area applies Blinded or an Accuracy penalty.

### 2. Ampharos — biological light as infrastructure and navigation

Sources:
https://www.pokemon.com/us/pokedex/ampharos
https://www.pokemon.com/us/animation/seasons/4/episode-51-fight-for-the-light
https://www.pokemon.com/uk/pokemon-news/remember-the-region-johto-spotlight

Official material repeatedly links Ampharos with lighthouse service. Its tail can be seen at great distance and has historically been used as a beacon. Olivine Lighthouse depends on an Ampharos for its light in multiple official portrayals.

Reusable structures:

- a Pokémon can participate in infrastructure without becoming equipment;
- one persistent Pokémon can become part of a settlement landmark and public memory;
- infrastructure can have staffing/care dependencies;
- losing a light source can affect navigation, schedules, public expectations and institutional workload without automatically creating a battle.

### 3. Chinchou / Lanturn — light as communication and predation

Sources:
https://www.pokemon.com/us/pokedex/chinchou
https://www.pokemon.com/us/pokedex/lanturn

Chinchou uses flashing antennae to communicate in deep water beyond sunlight. Lanturn uses intense light to incapacitate or lure prey.

Reusable structures:

- biological light can have different functions in different species;
- communication signals and hunting signals must not be conflated;
- a glowing individual may create an observation opportunity without creating a universal `Illuminate` mechanic;
- underwater light can interact with the maritime and ecological layers.

### 4. Volbeat / Illumise — patterned light as social communication

Sources:
https://www.pokemon.com/us/pokedex/volbeat
https://www.pokemon.com/us/pokedex/illumise

Volbeat flashes to communicate with others. Illumise guides Volbeat into many patterned displays, and scholars study those patterns.

Reusable structures:

- repeated light patterns can become research material;
- visual signals can vary over time and location;
- observers can record a pattern without immediately understanding its meaning;
- a regional tradition may interpret the same natural display differently from a scientist.

### 5. Morelull / Shiinotic — light can attract without being safe

Sources:
https://www.pokemon.com/us/pokedex/morelull
https://www.pokemon.com/us/pokedex/shiinotic

These Pokémon live in dark environments and produce visible light, but their illumination is associated with spores and predatory or defensive behavior.

Reusable structure:

A visible light in wilderness is information, not a promise of safety. The world can use light as lure, warning, communication, orientation or habitat cue depending on the species and evidence.

### 6. PTU campaign retrospective — night can change strategic pressure

Source:
https://pokemontabletop.com/over-there-a-world-war-one-pokemon-campaign-a-retrospective/

In `Over There!`, nighttime attacks create a recurring pressure cycle, exploration after dark is more dangerous, and the players must decide how to spend limited daytime activity before night arrives.

Reusable design lessons:

- night can alter risk and available choices without changing every rule;
- preparation during daylight can matter later;
- recurring evening pressure can create pacing;
- time-of-day should change content only where authored state supports it.

This source was processed in earlier passes for crisis/time structure, so this pass extracts only the underused lighting/night-pressure dimension.

### 7. Eevee Expo — dynamic lighting can support exploration without sacrificing readability

Sources:
https://eeveeexpo.com/flux/
https://www.eeveeexpo.com/resources/528/
https://eeveeexpo.com/resources/408/

Public fangame resources use dynamic light sources, caves, forests and day/night tones. Several authors explicitly prioritize maintaining visibility even when scenes become darker.

Reusable design lesson:

Visual darkness and gameplay legibility are separate design goals. Ouros can present night strongly without hiding required information from the player.

Do not copy shaders, code, art, exact palettes or game-specific mechanics from these projects.

### 8. NPS — artificial light at night is an ecological variable

Sources:
https://www.nps.gov/articles/effectsoflight.htm
https://www.nps.gov/articles/night-skies.htm
https://www.nps.gov/articles/night-sky-lightscape-monitoring-goga.htm

The U.S. National Park Service maintains a large synthesis of peer-reviewed work on artificial light at night. It reports effects across wildlife and ecosystems. NPS monitoring material specifically notes effects on foraging, reproduction, communication, orientation and navigation.

Reusable structures:

- lightscape can be measured and versioned;
- an illuminated road, port, stadium or industrial site can change nearby nighttime ecology;
- different taxa can respond differently;
- management can reduce glare or change fixture design rather than simply turning all lights off;
- a successful infrastructure project may create a new ecological externality.

This is an ecological design reference, not a source for Pokémon-specific behavior.

### 9. USGS — artificial light can change predator/prey interactions in water

Sources:
https://www.usgs.gov/staff-profiles/tessa-code
https://www.usgs.gov/staff-profiles/david-a-beauchamp

USGS work on Lake Washington notes that even small increases in artificial light can improve some predators' ability to hunt juvenile fish.

Reusable structure:

A lighting project near water can have downstream ecological effects even when the infrastructure itself is functioning correctly.

This connects Pass 68 to Freshwater, Maritime, Interspecies Ecology and Public Works.

## PTU / Caelo mechanics cross-check

### Verified narrow PTU evidence

The official PTU Gym-design source explicitly references:

- Darkvision;
- Blindsense;
- Glow Capability;
- Blinded in a darkness context.

This is sufficient to establish that light/darkness can matter mechanically in authored PTU encounters.

### Caelo boundary

The project already treats Caelo source text as higher-priority when Caelo modifies PTU. The complete primary Caelo corpus was not reliably retrievable in this run for a dedicated darkness/visibility extraction.

Therefore this pass does not define:

- Caelo-specific darkness penalties;
- Caelo-specific vision ranges;
- Caelo-specific Glow behavior;
- Caelo-specific Flash behavior;
- nocturnal encounter bonuses;
- stealth bonuses in darkness;
- accuracy modifiers from light level.

Those remain unresolved until the relevant primary text is extracted directly.

## Engine implications

The current Java head inspected for this pass is:

`b705561395b0ae776740e9207b44c1c53856f326`

Latest commit:

`Project authoritative runtime state into Pokemon initiative candidates (#101)`

The new slice projects canonical runtime combatant state into initiative-candidate construction. It can consume semantic weather/terrain inputs for specific initiative calculations, but it does not establish a lighting, darkness or visibility subsystem.

Battle LoS being VERIFIED does not mean low-light visibility is implemented.

`LoS` answers whether geometry blocks a line.

`light visibility` would answer whether an actor can perceive a target under the current illumination and capabilities.

Those must remain separate.

## Reusable Ouros principles from this scan

1. Light has provenance.

A scene should be able to distinguish sunlight, moonlight, firelight, electric fixtures, lighthouse beams, reflected light, bioluminescence and temporary event lighting.

2. Darkness is not one boolean.

A location can have bright areas, shadowed corridors, glare, intermittent light, backlighting and dark refuges at the same time.

3. Perception is actor-specific.

One Pokémon may have a legal PTU capability that another actor lacks. Minecraft rendering cannot decide what every actor mechanically perceives.

4. Artificial light can change ecology.

The effect must be discovered or authored. Do not assume every species avoids light or every predator benefits.

5. Light can be infrastructure.

Beacons, signals, streets, harbors, hospitals, stadiums, workshops and emergency routes may depend on reliable lighting.

6. Light can be communication.

Patterned signals can become research, culture or navigation content without automatically becoming language.

7. Presentation must remain accessible.

Required information must not disappear because the renderer makes a scene dark. Critical cues need visual/textual alternatives where appropriate.

8. Night can alter pacing without becoming a universal difficulty multiplier.

Different schedules, actors, services, species and risks may appear at night. The game should not simply give all enemies a night bonus.

## Copyright and transformation boundary

No copied dialogue, plot, character arc, map or distinctive prose is used here.

Pokemon species entries are used as factual/lore references at a high level.

PTU campaign and Gym examples are used only to extract encounter-design patterns and rule-boundary lessons.

Fangame sources are used for implementation/design patterns only.

## Research gaps for future passes

- exact PTU Core Rulebook text for Glow, Darkvision, Blindsense, Blinded and Flash;
- exact Caelo modifications, if any;
- current Cobblemon hooks for per-player or per-area lighting and night behavior;
- Minecraft server-side light-level access versus client-only rendering;
- whether AutoPTU-Java has any hidden light/darkness keyword or visibility state not surfaced in README-level inspection;
- how nocturnal encounter tables should read lightscape state without becoming directly manipulable rare-spawn exploits;
- whether individual artificial-light projects should expose spectrum/color or only coarse intensity and direction.