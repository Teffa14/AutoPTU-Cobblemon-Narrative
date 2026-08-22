# Pass 100 Research — Field Signs, Tracking & Spoor Evidence

Status: research/provenance only. Not Ouros canon. No mechanics are established by this file.

Date: 2026-08-22

## Why this pass exists

The repository already has layers for Cartography, Photography, Wild Collectives, Interspecies Ecology, Conservation, Cases, Biosecurity, Diel Activity, Soundscapes, Pokémon Agency and Science.

Those layers can store direct observations, maps, images, population hypotheses and evidence. A distinct state problem remains: indirect physical signs left by an actor after the actor is gone.

Examples include footprints, drag marks, scratches, shed fur/feathers, scent traces, scat-like biological remains, gnawed plants, disturbed soil, sleeping sites, burrow entrances, rub marks, feeding remains and repeated path wear.

This pass studies how those signs can support exploration, ecological research, rescue, cases and hunting/tracking stories without becoming an omniscient Pokémon radar.

## Sources inspected

### PTU 1.05 — Tracker Capability

Publicly accessible copy of PTU 1.05 Core:
https://anyflip.com/qloz/xgfq/basic/301-350

The publicly accessible text describes `Tracker` as a specialized scent-following Capability that uses Perception and distinguishes a known scent from picking up scents without an existing sample. It also links Odor Sleuth to Tracker.

Reusable structure:

- scent tracking is a specific capability, not a universal action;
- a known sample changes what can reasonably be followed;
- tracking can fail and can require renewed attempts;
- scent is one evidence channel among several;
- mechanics should live in PTU authority, not in narrative prose.

Ouros guardrail:

Do not copy public-web DC values into canon or implementation until the exact project PTU/Caelo source is verified. The public copy is discovery evidence only. AutoPTU/AutoPTU-Java remain read-only, and no generic overworld Tracker implementation was found in the current repository search.

### PTU — Perception examples

Public PTU reference:
https://pturpg.wikidot.com/skills

The Perception description explicitly uses examples such as noticing buried Pokémon and discovering fur/feathers at a crime scene, then notes that noticing a detail and interpreting it correctly can require different specialized knowledge.

Reusable structure:

- detection and interpretation should be separate records;
- finding a sign does not prove species, individual, timing or cause;
- a field sign can become case evidence or ecological evidence depending on context;
- an expert may disagree with another expert without changing the physical trace.

Ouros adaptation:

A player can observe a footprint or fur sample while its interpretation remains uncertain. Science, Cases, Conservation or Biosecurity can later consume that observation.

### Stoutland treasure hunt

Official Pokémon episode synopsis:
https://www.pokemon.com/us/animation/seasons/20/episode-32-treasure-hunt-akala-style

Stoutland uses scent to locate hidden objects while different riders obtain different outcomes.

Reusable structure:

- tracking can be an exploration loop rather than pursuit of a living target;
- the helper Pokémon can reveal a direction or find without explaining what the object is;
- persistence and handler/partner coordination can matter narratively;
- discovery can lead to archaeology, geology or material provenance instead of combat.

Copyright boundary:

Do not reuse the episode's competition, characters, exact finds or scene sequence.

### Swinub tracking Cresselia's scent

Official Pokémon episode synopsis:
https://www.pokemon.com/us/animation/seasons/11/episode-52-sleepless-in-pre-battle

The synopsis includes Swinub following Cresselia's scent to a shrine.

Reusable structure:

- scent can connect a known or suspected subject to a route;
- the endpoint can be a place rather than a battle encounter;
- successful tracking does not prove why the subject traveled there;
- a trail can lead into mythology, archives or a health investigation without making the tracker omniscient.

### Mightyena scent pursuit

Official Pokédex:
https://www.pokemon.com/us/pokedex/mightyena

The Pokédex describes Mightyena catching the scent of distant prey and then coordinating pursuit as a group.

Reusable structure:

- species lore can justify authored observations about pursuit behavior;
- scent use and group coordination are separate facts;
- a pack can react to a trail without every individual needing an identical role;
- pursuit behavior does not imply a universal Pack Mon mechanic or tactical AI implementation.

Ouros guardrail:

Do not infer `Tracker`, Pack Mon, shared initiative, guaranteed pursuit, capture pressure or target-locking merely from Pokédex prose.

### Wildlife tracks and other field signs

U.S. National Park Service:
https://www.nps.gov/places/wildlife-tracks.htm
https://home.nps.gov/teachers/classrooms/tracks-on-the-trail.htm
https://www.nps.gov/places/000/wildlife-signatures.htm

NPS materials treat tracks as one of many signs. Other useful signs include scat, beds, gnawed bark, hair, feathers, nests, burrows and other physical traces. Track identification can become difficult as substrate, snow, age and weather alter the sign.

Reusable structure:

- signs degrade over time;
- substrate affects detectability and preservation;
- different signs answer different questions;
- repeated signs can suggest patterns of use;
- a sign can support a behavioral interpretation without identifying an individual.

Ouros adaptation:

Every field-sign observation should store substrate/environment context and an uncertainty state. A perfect footprint icon should never be treated as permanent truth after rain, snowmelt, traffic or construction.

### Sign identification can be wrong

U.S. Forest Service — lynx track study:
https://research.fs.usda.gov/treesearch/25473

The study notes that snow-track species identification can be ambiguous or misleading and uses DNA from hair/scat collected along tracks to improve identification.

Reusable structure:

- sign identification can be provisional;
- physical samples can corroborate or reject a track hypothesis;
- a route inferred from prints can be valid even when the species attribution is wrong;
- sample provenance must remain attached to the trace location/time.

Ouros adaptation:

A `TRACKWAY` can exist before the system knows which Pokémon created it. Later analysis may revise the maker hypothesis without deleting the trackway record.

### Detection methods have different probabilities

USGS — nutria detection methods:
https://www.usgs.gov/publications/evaluation-nutria-myocastor-coypus-detection-methods-maryland-usa

This study compares hair snares, scat and trail cameras and finds different detection probabilities. The important design lesson is not the specific numbers; it is that method choice changes what can be observed.

Reusable structure:

- failure to find a sign does not prove absence;
- monitoring method affects detection probability;
- placement can alter detections;
- combining methods can improve confidence;
- sampling effort must be preserved.

### Non-invasive samples can support individual identity

USGS / Forest Service references:
https://www.usgs.gov/publications/hair-dog-obtaining-samples-coyotes-and-wolves-noninvasively
https://www.usgs.gov/centers/forest-and-rangeland-ecosystem-science-center/science/conservation-ecology-and-monitoring

Hair, scat and feathers can sometimes support genetic identification of individuals without capture.

Reusable structure:

- a physical trace may support individual re-identification;
- identity should require a validated method rather than visual guesswork;
- non-invasive monitoring can preserve Pokémon agency and avoid forced capture;
- the sample and the identity claim remain separate records.

Ouros adaptation:

A sample can support `candidate_pokemon_id` only after a project-defined identification process. The generator must never create a persistent identity solely because two tracks look similar.

## Synthesis for Ouros

### 1. The sign is physical state; the story about it is interpretation

Recommended separation:

physical trace -> observation -> classification -> maker hypothesis -> behavior hypothesis -> route hypothesis -> corroboration -> downstream decision.

A large footprint is real if observed. `An Ursaring made it last night while chasing someone` is several additional claims.

### 2. Trackways should be persistent but degradable

A trackway can have a stable identity while its visible segments degrade.

Useful causes of degradation:

- rain;
- snowmelt;
- wind;
- new snowfall;
- tides;
- traffic;
- crowds;
- construction;
- fire;
- flooding;
- deliberate disturbance;
- ordinary time.

Degradation should affect observation confidence, not rewrite what originally happened.

### 3. One trace can feed many systems

A trackway might support:

- a Conservation occupancy assessment;
- a Biosecurity arrival hypothesis;
- a Case involving a missing Pokémon;
- a Wildlife Collective route model;
- a Science dataset;
- a Cartography informal path;
- a Photography comparison;
- a Health Surveillance sample;
- a Pokémon Agency re-identification question.

The trace should remain one object with multiple consumers.

### 4. Absence of sign needs effort context

`No footprints found` is weak information without:

- substrate suitability;
- survey length;
- weather since last possible passage;
- observer capability;
- time window;
- alternate paths;
- sign type sought.

This prevents empty Minecraft terrain from becoming proof that no Pokémon used the area.

### 5. Scent is specialized

Narrative generation may describe scent only when a source supports it for the species/individual or when the PTU/Caelo mechanical capability is verified.

Do not give every canine Pokémon `Tracker`. Do not treat scent as exact coordinates. Do not let a scent trail bypass doors, dimensional boundaries, teleportation, weather, water, crowds or time without an explicit rule.

### 6. Tracking should often end before combat

Valid outcomes include:

- locate a resting site;
- confirm route use;
- discover an old shed feather;
- find a damaged fence;
- locate an injured or missing Pokémon;
- reach a feeding site after the subject has left;
- discover that two apparent trails are different individuals;
- lose the trail at a transport hub;
- identify an environmental change that redirected movement;
- prove that a rumor was based on old sign.

A successful tracking scene should not manufacture a battle just to reward the player.

## Original Ouros directions suggested by the research

Candidate objects:

- `FIELD_SIGN`
- `TRACKWAY`
- `SCENT_TRACE`
- `SIGN_OBSERVATION`
- `SIGN_CLASSIFICATION`
- `MAKER_HYPOTHESIS`
- `ROUTE_HYPOTHESIS`
- `BIOLOGICAL_TRACE_SAMPLE`
- `SIGN_DEGRADATION_REVISION`
- `TRACKING_SURVEY`
- `SIGN_CORROBORATION_LINK`
- `KNOWN_TRAIL_USE`

Candidate loops:

1. sign found -> provisional classification -> follow route -> corroborating sign -> route model updated;
2. repeated tracks -> occupancy hypothesis -> camera placement -> identity revision -> conservation decision;
3. missing Pokémon -> last confirmed sign -> scent/track split -> environmental disruption -> recovery without forced combat;
4. old sign archive -> new observation -> apparent contradiction -> substrate/date correction -> historical route reconstructed.

## Mechanical boundary

Public PTU discovery material shows `Tracker` and Perception-based sign discovery, but the exact project PTU/Caelo text must be re-verified before mechanical implementation.

Current repository search of AutoPTU found PTU reference material mentioning Tracker but no visible generic overworld tracking/scent subsystem. AutoPTU-Java's README continues to scope the Java project as a battle core and does not claim overworld tracking.

Therefore Pass 100 proposes no new DCs, scent ranges, track aging formulas, opposed checks, pursuit bonuses, surprise rules, capture modifiers or tactical target revelation.

## Copyright and provenance policy

No protected dialogue, characters, distinctive plot sequences or campaign scenes are copied into Ouros. Pokémon, PTU, scientific and community sources are used only to derive reusable design structures. All Pass 100 concepts remain proposals until explicitly promoted through the project's canon process.