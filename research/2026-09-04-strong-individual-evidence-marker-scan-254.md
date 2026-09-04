# Strong individual evidence and marker uncertainty scan — Pass 254

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Date: 2026-09-04

## Research question

What evidence can legitimately raise a recurring-wild-Pokemon identity hypothesis beyond ordinary behavioural similarity, and how should PTU skills/features affect the observation without leaking Ouros persistent identity?

## New source patterns

### Deliberate individual marks are useful but fallible

Smithsonian National Zoo material on bird banding explains that unique colour-band combinations let observers distinguish individuals visually without recapturing them. Re-sightings then support movement and survival histories. The useful Ouros pattern is a deliberately assigned, externally observable research marker linked to a field registry rather than to the hidden world-state key.

Source: https://nationalzoo.si.edu/migratory-birds/what-bird-banding

The Australian Bird and Bat Banding Scheme describes colour bands, flags and temporary plumage dyes. Colour combinations can identify an individual at distance; some marks are deliberately regional rather than individual, and dye is temporary. Reusable lesson: marker type has a declared semantic scope and lifetime. A visible mark must not automatically mean unique persistent identity.

Source: https://www.dcceew.gov.au/science-research/bird-bat-banding/about-banding/different-marks

USGS reported a coloured-leg-band technique for individually identifying Amazona parrots over repeated observations. This is useful as a biological analogue for a small flying Pokemon research programme, but it does not authorize a Fletchling band in Ouros canon.

Source: https://www.usgs.gov/publications/a-colored-leg-banding-technique-amazona-parrots

Rakhimberdiev et al. (2022) show that misidentification of marked individuals still occurs and can bias ecological inference. McMahon et al. show that tag loss itself must be modelled rather than assumed independent or impossible. Reusable lesson: `marker_observed` and `identity_confirmed` must remain separate facts, and a marker registry needs status such as active, uncertain, lost or retired.

Sources:
- https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.13825
- https://researchers.mq.edu.au/en/publications/tag-loss-probabilities-are-not-independent-assessing-and-quantify

### Natural-mark photo identification can be strong without handling

Australian sea-lion whisker-pattern work demonstrates that natural patterns can support individual photo-identification, but matching accuracy changes with angle, distance and elapsed time. Work on free-ranging skinks similarly found experienced observers outperform inexperienced observers while still making errors. Reusable lesson: a stable-looking natural marker can produce high-quality evidence only when observation conditions and observer competence are recorded.

Sources:
- https://pubmed.ncbi.nlm.nih.gov/26937048/
- https://onlinelibrary.wiley.com/doi/full/10.1002/ece3.1883

### Pokemon already supports ecology through repeated photographic observation

The official New Pokemon Snap site frames repeated expeditions, photography and expert evaluation as an ecological survey. Photo quality depends on framing, subject size, facing and other observable conditions, while behaviour rarity is recorded separately. Ouros can reuse the high-level pattern: evidence quality and behavioural significance are separate dimensions, and repeated field records can build a research history without capture or combat.

Sources:
- https://newpokemonsnap.pokemon.com/en-us/create-photodex/
- https://newpokemonsnap.pokemon.com/en-au/explore/

No Photodex scoring formula or Lental story content is imported.

### PTU supports better observation, not omniscient identity

PTU Survival explicitly covers scouting an area and tracking through wilderness. Perception covers attention to environmental detail and investigation, while specialised knowledge remains necessary to interpret what was noticed.

PTU's generic Skill Stunt Feature can improve a narrowly approved use of a Skill by adding +3 or using 2d10 instead of 1d20. Journey of Skill can re-roll a Skill Check and also grants Skill Stunt instances. These are legitimate candidate mechanisms for improving an observation attempt if the active Ouros rules profile adopts them and AutoPTU-Java implements the relevant Trainer Feature/perk path.

Sources:
- https://pturpg.wikidot.com/skills
- https://pturpg.wikidot.com/general-features
- https://pturpg.wikidot.com/journey-features

Channeler can expose a Pokemon's intentions, emotions, motivations, Moves, Abilities, Capabilities and vague recent memories while the channel is active. That is strong behavioural information, but the rule does not state that it reveals an Ouros persistent actor key or a complete lifetime identity history. Treating Channeler as automatic identity confirmation would therefore be an Ouros invention requiring explicit adoption and Trainer Feature implementation.

Source: https://pturpg.wikidot.com/channeler

## Transformed design lessons for Ouros

1. Separate the visible marker from the hidden persistent actor identifier.
2. Every deliberate marker needs a public registry record with marker type, observable code, application provenance, validity state and last verification.
3. Marker loss, damage, obscuration and transcription error remain possible states.
4. Natural-mark photo identification can be strong evidence, but quality must depend on actual observation conditions and cannot silently become a permanent unique key.
5. Trainer competence modifies evidence acquisition or interpretation. It does not rewrite hidden truth.
6. A successful PTU Survival/Perception/Skill-Stunt-style check may raise the quality of a newly captured evidence record after rules-profile and engine verification; it must not directly set `confirmed_identity=true`.
7. Strong evidence may justify `CONFIRMED_BY_DIEGETIC_MARKER` only when an active registry entry is observed with sufficient quality and no unresolved contradiction.
8. A confirmation can later be downgraded if the marker is reported lost, invalidated or ambiguous. Historical observations remain preserved.
9. Research gameplay can advance through repeated non-combat observation, photography and field-note accumulation.

## Project cross-check

Pass 253 caps ordinary unmarked field evidence at `PROBABLE_SAME_INDIVIDUAL` and explicitly leaves stronger diegetic markers unresolved. This pass addresses that gap without changing the existing Marea population or canonizing a physical band.

The canon-approved lower-Sendero population remains 12 Fletchling and `ouros.marea.encounter.sendero_lower_shelf.fletchling.0` remains the first persistent actor used by fixtures. A Pass 254 marker is fixture-only.

The source-authority policy remains controlling: PTU skills/features are rules evidence; Caelo/Kairos may inform living-world structure; no source automatically activates a mechanical overlay. Minecraft/Cobblemon presents observable marker state but cannot author the hidden identity link.

## Status boundaries

CANON-ALIGNED: persistent identity remains Ouros-authoritative; observer knowledge can be wrong; observation and demography remain separate; stronger claims need provenance.

PROPOSED: public marker registry, marker validity lifecycle, `CONFIRMED_BY_DIEGETIC_MARKER`, evidence-quality modifiers and later downgrade when marker validity becomes uncertain.

FIXTURE-ONLY: a blue/white research band code, exact observation conditions, exact confidence/quality values and the marker application event used in Pass 254 tests.

UNCERTAIN: whether Ouros will canonize physical research marking at Sendero; which institution can authorize it; welfare/procedure requirements; exact PTU skill DCs; which Trainer Features/perks are implemented in Java; whether natural Fletchling variation is visually distinctive enough for non-invasive confirmation.