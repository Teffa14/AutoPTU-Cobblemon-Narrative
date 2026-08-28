# Coastal Navigation Aids, Lighthouses & Beacon Continuity Research — Pass 92

Status: research/provenance only. Nothing in this file is Ouros canon.
Date: 2026-08-28

## Research question

What reusable structures can make coastal navigation in Ouros feel like a persistent public system rather than a collection of decorative lighthouses, while preserving the project's existing Maritime, Cartography, Weather, Technology, Maintenance, Public Notice, Soundscape and AutoPTU authority boundaries?

## Internal repository inspection

Before writing, the current recursive Narrative repository tree was inspected at head `51eae1907e1861d0a90b1cbc99c48e894d44a606`. The root, `design/`, `research/` and `proposals/` trees were reviewed; the design tree reported `truncated=false`.

Direct overlap review included:
- `design/maritime-coasts-depths-layer.md`;
- `design/cartography-survey-wayfinding-layer.md`;
- `design/technology-energy-infrastructure-layer.md`;
- `design/facility-maintenance-repair-inspection-extension.md`;
- `design/infrastructure-outage-restoration-extension.md`;
- `design/weather-forecast-preparedness-operational-extension.md`;
- `design/public-notices-signage-world-information-extension.md`;
- `design/soundscapes-acoustic-ecology-layer.md`;
- `design/travel-transport-expedition-layer.md`;
- `design/fisheries-aquatic-harvest-landing-stewardship-extension.md`;
- `design/cobblemon-runtime-authority-boundary.md`;
- `design/encounter-implementation-contracts.md`;
- `design/engine-readiness-snapshot-pass-91.md`.

The existing Maritime layer already permits navigation assets, buoys, lighthouses and navigation knowledge. Cartography already owns charts and editions. Technology owns machine/network operation. Public Notices owns published information. No existing layer tracks the operational identity of individual aids, their intended signal characteristics, observed state, temporary changes, promulgated corrections and route consequences across time. Pass 92 fills only that gap.

## Source set

### 1. Olivine Lighthouse — Pokémon Gold/Silver/Crystal, HeartGold/SoulSilver and animation

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Olivine_Lighthouse
- https://www.pokemon.com/us/animation/seasons/4/episode-51-fight-for-the-light

Classification: official-franchise narrative/location reference; Bulbapedia is secondary documentation, Pokémon.com is primary episode summary.

Reusable structures:
- a lighthouse can be an operational service, a workplace, a landmark and a social location at the same time;
- the beacon depends on a concrete operating resource/actor, so failure creates downstream consequences without requiring physical destruction of the tower;
- restoring the source of the light and resuming a separate institutional activity can occur on different timelines;
- a lighthouse can remain publicly meaningful even after another technology begins performing much of its practical work.

Transformation for Ouros:
- do not copy Jasmine, Amphy, Cianwood medicine or the Gym gate;
- use the broader dependency pattern: navigation asset -> operating dependency -> observed degradation -> service consequence -> intervention -> verification -> resumption;
- any Pokémon participating in operation must be an individual actor with an approved work assignment and authoritative capability evidence, never a species/type shortcut.

### 2. Ampharos signal lore

Source:
- https://bulbapedia.bulbagarden.net/wiki/Ampharos

Classification: franchise species-lore reference, secondary documentation.

Reusable structures:
- Pokémon-world communities can plausibly have older signalling traditions that use visible Pokémon-generated light;
- a signalling practice can predate modern technical systems and survive as heritage, backup, ceremony or local practice.

Transformation boundary:
- an Ampharos Pokédex association with beacons does not establish that any Ouros Ampharos can serve as a lighthouse;
- no light range, electrical output, fatigue rule, navigation bonus or work suitability is imported;
- if Ouros later establishes a Pokémon-assisted beacon, Pokémon Work and PTU/Caelo capability review must validate the individual case.

### 3. Olivine lighthouse in fog — animation continuity

Source:
- Olivine Lighthouse documentation above, including the animation account in which the lighthouse light helps an aircraft correct course in fog.

Reusable structures:
- the visible value of an aid becomes clearest under degraded visibility;
- a navigation asset can affect actors who never enter the building;
- an operating aid produces route confidence and decision information rather than directly moving a vessel.

Ouros lesson:
- the beacon should publish/express information; Travel/Maritime still owns whether a journey proceeds, reroutes or suspends;
- visible light must not become an automatic tactical visibility modifier.

### 4. Vista Lighthouse — Sunyshore

Source:
- https://bulbapedia.bulbagarden.net/wiki/Vista_Lighthouse

Classification: official-franchise location reference, secondary documentation.

Reusable structures:
- a lighthouse can combine maritime safety function with public observation/tourism;
- public access may cover only part of a technical facility;
- a high landmark can become a normal social destination between major plot events.

Ouros lesson:
- separate `operational_area`, `public_area` and `restricted_service_area`;
- closure of a lantern room does not necessarily close the public promenade, and a public viewpoint can close while the aid remains operational.

### 5. Pokémon Rejuvenation — “Lurking Lighthouse!”

Source:
- https://rejuvenation.wiki.gg/wiki/Lurking_Lighthouse%21

Classification: fan-game inspiration, not rules or canon authority.

Reusable structures:
- several navigation assets can form one maintenance/recovery program;
- restoring a coastal aid can require visiting multiple facilities rather than treating every lighthouse as an isolated dungeon;
- each site may fail for a different reason while contributing to the same network-level service objective.

Discarded:
- specific villains, puzzle sequence, reward, Pokémon requirement and story beats;
- any rule that a particular type is mandatory to power or repair an aid.

### 6. Pokémon World Online — Lighthouse Quest

Source:
- https://pwo-wiki.info/index.php/Lighthouse_Quest

Classification: fan MMO quest inspiration.

Reusable structure:
- a familiar landmark can become a restoration target with exact missing components;
- repair can change the persistent state of the location and later activity.

Ouros correction:
- procurement, installation, inspection and service resumption remain separate states;
- acquiring a component does not itself restore service.

### 7. Kairos Isles PTU living world — lighthouse as persistent crisis location

Sources:
- https://kairosptu.wiki.gg/
- https://kairosptu.wiki.gg/wiki/Range_Rondo

Classification: public Pokémon Tabletop United living-world campaign material; narrative inspiration only.

Observed pattern:
- a lighthouse remains part of persistent regional geography and can later become relevant during an unrelated severe-weather/community incident;
- living-world character logs make the same infrastructure accumulate history across dates rather than respawning as a fresh quest site.

Transformation:
- retain only the persistence pattern;
- do not copy the blizzard, Legendary/Pokémon identity, character, faction or supernatural explanation;
- Ouros lighthouse incidents should originate from current infrastructure, weather, ecology, actor and route state.

### 8. Official PTU blog — Mareep family plot hooks

Source:
- https://pokemontabletop.com/pokemon-spotlight-mareep-family/

Classification: official Pokémon Tabletop RPG/PTU developer blog; inspiration and species discussion, not an Ouros rules source by itself.

Useful boundary:
- the blog explicitly recognizes that the obvious Ampharos-lighthouse plot has already been used and encourages transforming species traits into different campaign hooks;
- this supports avoiding a direct replay of Olivine in Ouros.

### 9. Maritime Safety Queensland — navigation marks

Source:
- https://www.msq.qld.gov.au/Safety/Navigation-buoys-marks-and-beacons

Classification: real-world operational reference only. No Queensland law, authority or standard becomes Ouros canon.

Reusable information architecture:
- navigation aids communicate through combinations of location, colour/shape and light characteristics;
- different marks communicate different route information;
- the visible object and the meaning assigned to it are distinct but linked.

Ouros transformation:
- create an `aid_characteristic` object with version/provenance;
- do not import Region A colours, shapes or meanings unless a future Ouros canon decision deliberately chooses them.

### 10. U.S. Coast Guard Navigation Center — Local Notices and Light Lists

Sources:
- https://www.navcen.uscg.gov/lnm-frequently-asked-questions
- https://www.navcen.uscg.gov/light-list-annual-publication

Classification: real-world operational documentation only.

Reusable structures:
- each aid can have a stable reference identity;
- published lists describe expected characteristics;
- temporary changes and hazards are distributed through notices;
- keeping charts/publications current is an ongoing process;
- a corrected publication does not erase the older version from history.

Ouros transformation:
- model an `aid_registry_entry` and revisioned `navigation_notice`;
- Cartography and Public Notices remain owners of the actual chart/publication surfaces;
- no USCG terminology, jurisdiction, cadence or legal requirement is imported.

### 11. International Association of Marine Aids to Navigation and Lighthouse Authorities — buoy/light definitions

Sources:
- https://www.iala.int/wiki/dictionary/index.php/Buoy
- https://www.iala.int/wiki/dictionary/index.php/Light_%284%29

Classification: real-world technical vocabulary reference only.

Reusable distinction:
- a buoy is an exact physical mark with recognizable characteristics;
- a light is an identifiable signal attached to a known geographical location.

Ouros transformation:
- preserve `asset identity`, `physical position`, `intended characteristic` and `observed characteristic` as separate fields;
- never infer that an aid works merely because its Minecraft block/entity exists.

### 12. Northern Lighthouse Board — automated and monitored aids

Source:
- https://www.nlb.org.uk/navigation/physical-and-electronic-aids-to-navigation/

Classification: real-world operational inspiration only.

Reusable structures:
- aids may be automated yet still need monitoring, inspection and modernization;
- an unstaffed site can remain an important persistent workplace because maintenance visits and remote monitoring create episodic activity.

Ouros transformation:
- staffing is optional and canon-specific;
- automation never creates omniscient condition knowledge: remote monitoring produces observations that can be stale, missing or wrong.

## Cross-source synthesis

The strongest reusable loop is:

1. establish the aid's normal identity and characteristic;
2. allow actors to learn that normal pattern;
3. record an observation that differs from expectation;
4. separate the observed symptom from the cause;
5. determine whether the aid itself, its supply, its monitoring, the publication, the observer or environmental visibility explains the mismatch;
6. publish a temporary notice when appropriate;
7. let Maritime/Travel make route/service decisions from that information;
8. perform repair/inspection through Technology/Maintenance;
9. verify the actual characteristic again;
10. issue a correction or restoration notice;
11. preserve the outage and old notice as history.

## High-value narrative structures

### The aid is correct; the chart is stale

A buoy appears “wrong” because a channel was revised after the observer's chart edition.

### The chart is correct; the aid is off station

The registered position is still valid, but the floating mark has physically moved.

### The light exists; the characteristic is wrong

A lantern still shines, but its pattern no longer identifies it correctly. This creates a more subtle problem than total darkness.

### The tower works; visibility does not

Fog, smoke, precipitation or line-of-sight obstruction prevents an otherwise healthy signal from being useful. Weather/observation state matters without turning the asset into a fault.

### The asset is down; the route remains usable with mitigation

A service can continue LIMITED with a temporary mark, pilot/local guide, daylight-only window or other canon-approved mitigation. Travel/Maritime owns the service decision.

### The public landmark and the technical aid diverge

A historic lighthouse can remain a cultural/tourism landmark after navigation shifts to a different technical aid. Conversely, a remote modern beacon can matter operationally while having almost no public presence.

### Pokémon-assisted signalling as history, not default infrastructure

A region may preserve stories or practices involving Pokémon-generated light. The existence, current use and mechanical feasibility of each case require explicit canon and rules review.

## Mystery patterns

- Three sightings, two actual lights: observers confuse a harbor light with a navigation aid.
- A “missing” buoy: the chart edition predates a planned relocation.
- The light that flashes correctly from shore but wrong from sea: obstruction or viewing geometry changes perception.
- The notice that arrived late: different communities possess different current versions of route information.
- The beacon that failed only on certain nights: intermittent supply, monitoring gap or environmental occlusion rather than sabotage.
- Two correct reports that seem contradictory because they were made at different tide/weather windows.

## Dungeon / exploration patterns

A lighthouse should not default to six floors of Trainer battles. Better reusable structures include:
- public lower area + restricted service spaces;
- external maintenance path exposed to weather;
- machinery/energy room with inspection records;
- lantern/beacon room with exact asset state;
- old keeper quarters reused as archive, workshop or habitat;
- cliff path or breakwater connecting the aid to the wider coast;
- remote buoy/marker maintenance trip connected to the tower's records.

Any tactical hazard on stairs, cliffs, surf, wind, machinery or electrified equipment remains unavailable until PTU/Caelo and AutoPTU support it.

## PTU/Caelo mechanical boundary

Pass 92 does not establish:
- Navigation Skill bonuses from a lighthouse;
- fog/visibility Accuracy penalties;
- signal range formulas;
- fall, surf, wave, cliff or collision damage;
- electrical/heat hazards from lantern machinery;
- a Pokémon's eligibility to power a beacon;
- Trainer Feature effects for navigation work;
- vehicle reroute checks;
- rescue or piloting DCs;
- automatic bonuses for having an Ampharos or Electric-type Pokémon.

If a mechanically rich encounter requires darkness, weather, cliffs, reactions, forced movement, electricity or equipment interactions, those exact families must remain visible in its contract.

## Cobblemon reuse boundary

Strong reuse candidates:
- lighthouse/building geometry;
- lamps, glass, blocks and decorative mechanisms;
- buoy/beacon models built from Minecraft blocks/entities;
- particles, sounds and visible beams where supported;
- Pokémon models/forms/poses/cries;
- UI, networking and synchronization;
- world coordinates and entity/block tracking;
- signs/books/maps as presentation surfaces;
- day/night and weather presentation.

Adapter-required:
- translating an Ouros aid state into the correct visual light/sound/notice;
- converting a player interaction into an intent to inspect, repair or acknowledge;
- recording an overworld observation with provenance;
- projecting approved route consequences.

Forbidden authority:
- redstone/lamp state deciding canonical aid operation;
- a visible Cobblemon Pokémon becoming the power source by proximity;
- nearby entities becoming combatants;
- Cobblemon BattleState deciding any battle fact;
- Minecraft fog/weather directly imposing PTU modifiers.

## Canon questions deliberately left open

- Which Ouros regions have maritime navigation aids?
- Which use staffed lighthouses, automated lights, buoys, acoustic signals or other technologies?
- Is there a common regional standard or several incompatible traditions?
- Who maintains registries and publishes changes?
- Which aids are public landmarks versus restricted technical sites?
- Do any cultures use Pokémon-assisted signalling today, historically, ceremonially or never?
- How are temporary navigation changes communicated to isolated settlements?
- What information is public and what operational data is restricted?

No answer in this research note is canon.