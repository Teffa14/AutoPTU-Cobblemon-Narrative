# Visual Records, Photography & Imaging Provenance — Research Scan 141

Status: RESEARCH / PROVENANCE ONLY. Not canon.
Date: 2026-08-23

## Why this pass exists

The repository already models observations, archives, media publication, public memory, identity, metrology, wildlife disturbance and institutional records. It did not yet have one authority for visual-record capture itself: original image versus edited derivative, capture context, camera placement, camera-trap sessions, image metadata, identification claims, privacy, image reuse and whether the act of obtaining a photograph changed the observed behavior.

This pass therefore treats photography as evidence and cultural material, not as an automatic truth machine.

## Existing Ouros boundaries inspected

Relevant existing layers were inspected before writing:

- `design/observation-settlement-time-layer.md` owns observation events and disturbance-aware wildlife context;
- `design/media-communications-information-layer.md` owns publication, channels and delivery;
- `design/archives-museums-collections-preservation-layer.md` can preserve photographs/recordings as collection objects;
- `design/metrology-calibration-measurement-standards-layer.md` owns measurement/instrument calibration concepts;
- `design/identity-names-aliases-record-linkage-layer.md` owns actor identity and linkage;
- wildlife, tracking, diel, migration, public-memory and research-ethics layers own their respective domain interpretations.

The missing layer is the capture-to-visual-record chain and the provenance of transformations after capture.

## Source 1 — New Pokémon Snap official site

Source:
https://newpokemonsnap.pokemon.com/en-us/

Official Pokémon material frames photography as ecological survey. The player photographs Pokémon living in natural habitats and builds a Photodex from repeated field expeditions.

Reusable structures:

- visual records can be a legitimate research output;
- repeated visits to the same site can reveal different behavior;
- a photograph captures one moment, not a complete species profile;
- research institutions can request specific visual observations;
- a visual archive can accumulate across biomes and years.

Do not copy:

- Lental, L.E.N.S., NEO-ONE, Illumina plot or Photodex scoring as Ouros canon.

## Source 2 — New Pokémon Snap: official game page

Source:
https://www.pokemon.com/us/pokemon-video-games/new-pokemon-snap

The official description separates ecological observation from photographic quality. Pokémon may patrol, play, live in groups or move alone, while photo scores also depend on framing and presentation.

Important design lesson:

A scientifically valuable photograph and an aesthetically excellent photograph are not the same thing.

Ouros should therefore keep at least three independent concepts:

- what the image physically captured;
- how useful it is as evidence;
- how it is received as a photograph or publication.

## Source 3 — New Pokémon Snap Photodex / edited photos

Sources:
https://newpokemonsnap.pokemon.com/en-au/create-photodex/
https://newpokemonsnap.pokemon.com/en-us/edit-and-share/

The official material distinguishes photos submitted for research from copies saved to a personal album and later altered through crop/zoom/brightness/focus, stickers, frames or filters.

Reusable structure:

`original capture -> research use -> derivative edit -> publication/share`

A derivative can remain legitimate while no longer being the best source for exact visual evidence. Editing does not automatically mean fraud; provenance determines what claims remain supportable.

## Source 4 — Official New Pokémon Snap tips

Source:
https://www.pokemon.com/us/features/top-tips-to-begin-your-new-pokemon-snap-journey

The official guide explicitly notes that Pokémon are living normally rather than posing, that day/night changes behavior, and that tools such as scanning, food and music can alter what Pokémon do.

This is an important guardrail for Ouros:

A photograph of a behavior after baiting, calling, scanning, approaching or otherwise intervening is still an observation, but its disturbance/intervention context must travel with the image.

The image cannot later be represented as proof of undisturbed natural behavior unless that claim is independently supported.

## Source 5 — Original Pokémon Snap official page

Source:
https://www.pokemon.com/us/pokemon-video-games/pokemon-snap

The original game also uses photography as research and explicitly uses tools to attract, wake or otherwise alter Pokémon behavior.

Reusable design lesson:

Visual research can include intervention experiments, but intervention must be recorded. The research question, method and ethics matter as much as the resulting image.

## Source 6 — Pokémon Tabletop community discussion: Photographer / Chronicler

Source:
https://www.reddit.com/r/PokemonTabletop/comments/12zi5db

A public PTU discussion describes the Photographer concept as attractive in theme but difficult to manage mechanically, and discusses Chronicler archive play in campaigns with recurring people and locations.

Useful high-level lesson:

Photography becomes more valuable in a persistent campaign when images refer back to the same actors, locations, techniques and events over time. A visual archive should support continuity rather than only one-off rewards.

Rules caution:

Community discussion is not authority. The project AutoPTU evidence contains implemented Chronicler archive actions, but this pass does not infer Photographer/Chronicler Features, AP costs, technique learning, bonuses or archives beyond exact validated contracts.

## Source 7 — Ethical wildlife photography, National Park Service

Source:
https://www.nps.gov/sajh/planyourvisit/ethical-wildlife-photography.htm

NPS guidance emphasizes distance, quiet observation and photography that does not disrupt natural behavior. It also shows how the same subject can change behavior after human disturbance.

Reusable structures:

- photographer disturbance should be recorded;
- approaching for a better image can invalidate the behavior the observer wanted to document;
- long lenses/remote observation can reduce disturbance;
- image quality should never justify overriding a site or wildlife protection rule.

Ouros does not import US law or exact distance rules.

## Source 8 — Wildlife viewing and photography as a driver of human-wildlife interaction

Source:
https://www.nps.gov/articles/000/who-is-the-bad-guy-here-when-animals-misbehave.htm

NPS research describes how visitors interested in seeing or photographing wildlife can themselves change interactions through approach or feeding.

Reusable structure:

`popular photograph -> increased attention -> changed visitor behavior -> changed wildlife behavior -> new observations`

This can produce a feedback loop in Ouros without declaring photographers or wildlife to be villains.

## Source 9 — Visual archive indexing and retrieval

Source:
https://www.archives.gov/preservation/technical/imaging-storage-report.html

National Archives material emphasizes the separation between image files and descriptive/index information. Incorrect indexing can make a real image effectively unretrievable.

Reusable structure:

The visual record and its catalogue metadata are independent persistent objects. A wrong date, location or subject tag should be correctable without rewriting the original image.

## Derived Ouros principles

### A. Original and derivative must be separate

A crop, brightness adjustment, annotation, frame or publication layout is a new derivative record linked to the source image.

The source remains immutable except for preservation migrations that preserve its identity and checksum/provenance.

### B. Image content and interpretation must be separate

A photograph can show:

- one Pokémon;
- several similar Pokémon;
- an object;
- tracks;
- damage;
- a building;
- a weather condition;
- a person near a site.

It does not by itself prove identity, motive, ownership, cause, sequence, friendship, crime, species-wide behavior or institutional responsibility.

### C. Capture context matters

Store whether the image was made through:

- passive observation;
- remote camera trap;
- public event coverage;
- staged portrait;
- scientific intervention;
- bait/food;
- call/music;
- light/flash;
- pursuit/approach;
- battle aftermath;
- controlled institutional setting.

These are provenance facts, not moral verdicts.

### D. Camera traps are observations, not omniscience

A camera trap session needs time window, placement, field of view, trigger method, downtime, maintenance and retrieval state. No image can support claims about periods when the camera was unavailable or pointed elsewhere.

`NOT PHOTOGRAPHED` is never automatically `ABSENT`.

### E. Publication creates a new information event

Media owns publication. Public Memory owns what persists socially. This layer owns the image/derivative being published.

A viral image may change visitor behavior, tourism, conservation pressure or rumor without becoming more factually correct.

### F. Privacy and sensitive locations need scope

Photography can include people, private interiors, clinical environments, research subjects, nesting locations, restricted collections or culturally sensitive sites. Existing Research Ethics, Identity, Sacred Sites and institutional access layers remain authoritative.

A valid photograph is not automatically a valid public release.

## PTU / AutoPTU constraints found

Project evidence shows Chronicler archive mechanics exist in AutoPTU Python, including named records and archive categories. That is narrow evidence for the class implementation, not a generic photography rules engine.

No generic camera, image-evidence, camera-trap, visual-identification or photographic-scoring subsystem was located in the inspected AutoPTU-Java state.

Therefore this pass does not invent:

- Photography checks or DCs;
- Perception bonuses for owning a camera;
- Chronicler/Photographer Features;
- photo-derived combat bonuses;
- scan ranges;
- flash-induced Accuracy or Status effects;
- camera-trap spawn modifiers;
- automatic species identification;
- proof-of-identity from one image;
- image-based ownership or custody.

## Engine relevance

Most visual-record state belongs outside battle. Mechanically rich photo encounters may still depend on:

- complete movement when subjects, photographers or crowds move through threatened space;
- terrain/weather/hazards/zones/reactions if exact validated field conditions affect the encounter;
- AI tactical policy when the objective is observation, withdrawal, route protection or camera recovery rather than KO;
- Minecraft/Cobblemon/Craftics adapter/playback for camera positions, noncombat actors, semantic objectives and visual record capture.

The permanent capability map must remain conservative; a representative implemented Move or reaction does not promote an entire category.

## Canon questions left open

- What camera technology exists in each Ouros region?
- Are instant cameras, film, digital cameras, fixed camera traps and video all common?
- Which institutions maintain visual archives?
- Who may publish sensitive wildlife locations?
- What privacy expectations apply to public spaces, workplaces, clinics and homes?
- Does any Trainer Class in the project ruleset grant explicit photography mechanics beyond Chronicler-style archive behavior?
- How does Caelo modify Chronicler, Perception, research or imaging rules, if at all?
- Which visual records already exist before players arrive?

No answer above is promoted to canon by this research file.