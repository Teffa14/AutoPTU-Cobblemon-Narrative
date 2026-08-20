# Photography, Visual Evidence & Documentary Practice — Research Pass 46

Status: research and provenance only. Nothing in this file is Ouros canon.

Date: 2026-08-20

## Why this pass exists

The repository already models observation, research, media, archives, public memory, cases, cartography and soundscapes. It does not yet have a dedicated model for photographs, video, camera traps, documentary records, image editing, visual provenance or the difference between an image and the claim someone makes from it.

This pass studies those structures without adding new PTU rules.

## Existing repository overlap checked

This pass is intentionally downstream of:

- observation / settlement / time;
- science / research / discovery;
- media / communications / information;
- archives / museums / preservation;
- case / authority / custody;
- cartography / survey / wayfinding;
- public memory / event / legacy;
- fashion / visual culture;
- soundscape / acoustic ecology;
- Pokémon agency / partnership / release.

The proposed layer should connect these systems rather than duplicate them.

## Pokémon source patterns

### New Pokémon Snap — ecological survey through photography

Official New Pokémon Snap material frames photography as field research. The player travels through varied habitats, observes wild Pokémon, records behavior and builds a Photodex. Research level can reveal different behaviors in the same course, so repeated observation can produce new evidence rather than merely higher numerical rewards.

Sources:
- https://newpokemonsnap.pokemon.com/en-us/
- https://newpokemonsnap.pokemon.com/en-au/explore/
- https://www.pokemon.com/us/strategy/top-tips-to-begin-your-new-pokemon-snap-journey

Reusable structures:

- photography as ecological observation rather than capture;
- repeated surveys of the same place producing different records;
- habitat and behavior attached to each image;
- unusual behavior becoming a research lead;
- a vehicle or safe observation platform enabling noncombat research;
- visual discovery feeding a larger scientific mystery.

Do not import Photodex scoring or Illumina mechanics into Ouros.

### Research record versus personal edited image

New Pokémon Snap explicitly separates the Photodex research record from a personal album. Personal copies can be adjusted and decorated after the expedition.

Source:
- https://newpokemonsnap.pokemon.com/en-us/edit-and-share/

Reusable principle:

A visual record used as evidence should have an immutable or versioned primary record. A publication, crop, annotation, filtered copy or commemorative image is a derivative object with its own provenance.

Editing a display copy should not silently rewrite the primary observation.

### Behavior rarity is not factual certainty

Professor Mirror evaluates photos using framing and observable behavior categories. For Ouros, the useful part is not the scoring formula. The useful part is that one image can document a behavior while remaining a partial observation of a larger ecological situation.

Source:
- https://newpokemonsnap.pokemon.com/en-gb/create-photodex/

A dramatic image should not automatically prove:

- population abundance;
- cause of behavior;
- kinship;
- aggression motive;
- ownership;
- long-term habitat use;
- faction responsibility;
- guilt in a case.

## Camera-trap and citizen-science patterns

### Distributed classification can be useful when uncertainty remains explicit

Snapshot Serengeti research circulated wildlife images to many volunteers and aggregated classifications. Expert validation showed high overall agreement, but rare species were harder and confidence metrics mattered.

Source:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4999033/

Reusable Ouros structures:

- many players can independently classify the same image;
- agreement can raise confidence without becoming automatic canon;
- low-confidence or rare observations can be routed to experts;
- `no Pokémon visible` is itself an observation, not proof of absence;
- classification history should remain attached to the image.

### Camera traps create scale and bias problems

Long-term camera monitoring can create enormous image volumes. Research also warns that placement, sampling design and geographic/taxonomic bias shape what is observed.

Sources:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11885691/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7663993/

Reusable Ouros structures:

- a camera network needs placement metadata;
- coverage gaps remain visible;
- detection probability is not the same as presence/absence truth;
- a camera pointing at a trail overrepresents animals using that trail;
- damaged or offline cameras create missing data, not zero activity;
- automated classifiers can suggest labels but should retain confidence and review state.

### Individual re-identification can support persistent Pokémon

Camera-trap research treats re-identifying the same individual across later images as an important ecological problem.

Source:
- https://arxiv.org/abs/1811.07749

Useful Ouros application:

A photo may become evidence that a persistent Pokémon entity appeared in two locations at different times. Identity matching should remain a hypothesis until corroborated unless the individual has a reliable canonical identifier.

## Image provenance and editorial context

Modern digital images can be cropped, brightened, filtered, annotated or otherwise transformed. For Ouros, technical standards are not required as canon, but the general provenance principle is valuable: retain source, capture context and transformation history rather than treating every visual copy as equivalent.

The game should support:

- original capture record;
- derivative crop;
- annotated research copy;
- publication copy;
- exhibit copy;
- disputed copy;
- missing-original state;
- redacted copy for sensitive locations.

A modified image can still be useful. Modification simply needs to remain visible in provenance.

## PTU / AutoPTU cross-check

Python AutoPTU currently exposes Chronicler-related runtime actions, including archive records and Cinematic Analysis. This is evidence that record-oriented Trainer Feature mechanics exist in the oracle. It is not evidence for a generic camera mechanic, photography Skill, photographic damage bonus or automatic evidence system.

Current Python Trainer runtime reporting also shows that many Trainer Features and Edges remain without runtime mappings. Therefore any visual-record mechanic tied to Chronicler, Researcher, Perception, Technology Education or another Feature must be checked individually before becoming executable.

Mechanical rule boundary:

- no invented photography DC;
- no invented camera accuracy bonus;
- no automatic Chronicler benefit from taking screenshots;
- no automatic Perception success because an image exists;
- no evidence authenticity check without an authoritative rule or authored investigation procedure;
- no battle scouting bonus from archived footage unless a supported Feature explicitly grants it;
- no automatic Pokémon identification beyond information the authoritative Pokédex/research state allows.

## Design lessons for Ouros

### A. The image is a record, not world truth

A photograph stores what the device captured from one position at one time under specific conditions.

It may be incomplete, misleading, ambiguous or correctly interpreted.

### B. Primary record and presentation copy must separate

Research, case and archival systems need stable source records. Media, museum and social systems may create derivatives.

### C. Visual absence needs coverage context

Ten empty frames can mean no Pokémon passed the camera, the camera was poorly positioned, the sensor failed, the time window was wrong or the species used another route.

### D. Camera networks can become world infrastructure

Camera traps, harbor cameras, laboratory imaging stations, battlefield recording systems, museum digitization rigs and public event cameras can all become persistent technical assets with ownership, maintenance, coverage and access state.

### E. Photos can create future content without forcing a conclusion

Examples:

- the same marked Pokémon appears months later in another valley;
- an old photo reveals a building that no longer exists;
- a crowd photo shows an unknown witness;
- a camera trap records a route used only during one season;
- a published crop accidentally removes context that matters later;
- an image believed to show one species is reclassified after better evidence;
- a historic battle photo becomes a disputed public-memory object.

## Copyright and transformation policy

External photographs, screenshots, manga panels, fanart and fan-game assets are research references only. Do not copy them into Ouros assets without permission or an appropriate license. Extract structural lessons and source attribution. Original Ouros visual assets should be created separately.

## Research gaps for later passes

- exact PTU/Caelo Chronicler wording and which archive/cinematic effects Ouros will retain;
- any Caelo-specific rules for recording, Pokédex evidence or field research;
- Minecraft/Cobblemon hooks for screenshots, map cameras, entities, frames and per-player visibility;
- privacy rules for player portraits and private-location photography;
- whether battle transcripts can generate deterministic replay metadata suitable for documentary footage;
- how an eventual classifier distinguishes persistent individual Pokémon without false identity merges;
- whether sensitive conservation images should automatically redact coordinates in public copies.
