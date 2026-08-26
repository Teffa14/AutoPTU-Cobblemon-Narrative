# Pass 174 Research — Molting, Shedding & Seasonal Coats

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon.

## Why this gap is worth filling

A full repository inventory and code search found no dedicated authority for molt, shedding, pelage/plumage replacement, shed skins, or other reversible body-covering cycles. Existing layers already own adjacent truths:

- `evolution-life-stage-transformation-layer.md` owns Evolution and authoritative form changes.
- `diel-activity-circadian-rhythms-layer.md` owns daily activity/rest.
- seasonality/phenology systems own recurring seasonal timing.
- `field-signs-tracking-spoor-layer.md` owns physical traces once observed.
- `visual-records-photography-imaging-provenance-layer.md` owns images.
- Care owns individual welfare assessment.
- Material Culture owns persistent objects only after an explicit handoff makes shed material an object of custody/provenance.

The missing layer is the biological episode itself: an individual or population replacing fur, feathers, skin, scales, plant-like ornament, or other authored body covering while remaining the same persistent Pokémon entity.

This should not be generalized into a universal biology engine. Species-specific or population-specific behavior must be authored or evidenced.

## Pokémon sources

### Deerling and Sawsbuck — seasonal appearance and scent

Official Pokédex pages maintain four seasonal forms for Deerling and Sawsbuck. Deerling entries also explicitly connect seasonal state with different scents. Sawsbuck entries tie seasonal appearance to flowers, branches, leaves, foliage and observed behavior/preferences.

Sources:
- https://www.pokemon.com/us/pokedex/deerling
- https://www.pokemon.com/us/pokedex/sawsbuck

Reusable structure for Ouros:

Seasonal appearance can be a persistent, observable history attached to one individual. Observers can record which appearance was seen at which place/time without assuming that every seasonal-looking change is a mechanical Form change. If the authoritative species data says a Form changed, Evolution/Form systems own that fact. Otherwise the narrative layer records only the observed covering or ornament state.

Do not import the Pokédex's aesthetic preferences or behavioral statements as universal regional truth for Ouros populations.

### Dratini — repeated skin shedding during growth

Official Dratini Pokédex text states that Dratini repeatedly sheds its skin as it grows, with one entry associating the process with a rapid waterfall.

Source:
- https://www.pokemon.com/us/pokedex/dratini

Reusable structure:

A shed skin can become longitudinal evidence that the same persistent individual was present, grew, or used a recurring site. The skin is evidence, not automatic proof of exact age, current location, health, Evolution readiness, or mechanical `Shed Skin` activation.

### Silicobra — repeated sheds with a body consequence

Official Silicobra material says its neck pouch becomes more elastic each time it sheds its skin.

Source:
- https://www.pokemon.com/uk/pokedex/silicobra

Reusable structure:

Repeated biological cycles can accumulate authored physical history without becoming stat progression. Ouros may preserve a series of shedding observations while PTU stats remain governed only by authoritative mechanics.

### Burmy — body covering versus external constructed cloak

Burmy's official Pokédex describes a cloak assembled from nearby materials and rapidly rebuilt when damaged. Burmy also has the mechanical Ability `Shed Skin` in official game data.

Source:
- https://www.pokemon.com/us/pokedex/burmy

Reusable structure:

Visual replacement can have different ontologies. A shed skin, regrown coat, seasonal foliage and a constructed cloak should never be collapsed into one `molt` boolean. Burmy's cloak remains governed by species/form mechanics and material observations where relevant.

## PTU / project rules cross-check

The project AutoPTU corpus contains PTU ability data and a broad Ability implementation log. `Shed Skin` and `Seasonal` exist as mechanical concepts in source material/searchable project data. AutoPTU's ability log demonstrates that many individual Ability contracts have Python test coverage, but ability-family coverage must still be treated as PARTIAL for the Java migration.

Project evidence:
- `Teffa14/AutoPTU/files/Copia de Fancy PTU 1.05 Sheet - Version Hisui - Abilities Data.csv`
- `Teffa14/AutoPTU/ABILITY_LOG.md`
- AutoPTU search results for `Seasonal` and species data.

Important boundary:

A biological shed or seasonal coat change in world state does not trigger the PTU Ability `Shed Skin`, cure a Status, change stats, grant an Ability, change Type, change Move access, or activate any season-dependent battle effect. If PTU/Caelo defines a real Form/Ability transition, authoritative mechanics must perform it separately.

The repository also contains PTR2e/Foundry reference material, including a different `Seasonal` implementation. That material is not PTU/Caelo authority and must not be imported into Ouros rules.

## Ecological sources

### Molt creates temporary changes in visibility and site use

National Park Service harbor-seal monitoring documents breeding and molt seasons separately. During molt, seals spend extended periods hauled out while replacing fur, which changes how observable they are and can make certain sites disproportionately important during that period.

Sources:
- https://www.nps.gov/articles/elephant-seal-monitoring-faq.htm
- https://www.nps.gov/articles/harbor-seal-monitoring.htm
- https://www.nps.gov/articles/000/sfan-updates_2025-breeding-harbor-seal-monitoring.htm

Reusable structure:

Higher counts during a molt aggregation do not automatically mean a population increase. Detectability, behavior and site occupancy can change during the cycle. Ouros should preserve survey method and molt stage before interpreting counts.

### Molt timing is not identical across species or individuals

USGS work on Hawaiian forest birds found extended molt periods, species differences, age-related plumage states and only limited overlap between energetically expensive breeding and molt for most studied species.

Sources:
- https://pubs.usgs.gov/publication/70239740
- https://www.usgs.gov/data/hawaii-island-forest-bird-phenology-and-morphometrics-1994-2019

Reusable structure:

A region should not use a universal `molt season`. A population can have a typical window while individual episodes vary. Juvenile, formative and mature appearances may also be distinguishable observationally without granting the observer perfect age knowledge.

### A messy coat can be healthy seasonal change

NPS educational material on white-tailed deer notes that seasonal coat replacement can make an animal look rough while still representing normal change.

Source:
- https://www.nps.gov/media/photo/gallery-item.htm?gid=036EE5EF-B1C8-4A4B-8FF6-9B46B8CA3873&id=a59074d2-8e49-4de2-b0ad-fe2730ee9421

Reusable structure:

Visual roughness is an observation, not a diagnosis. Care decides welfare interpretation when there is evidence for concern.

## Community / tabletop material

A public r/PokemonTabletop discussion about the `Seasonal` Ability shows a recurring tabletop problem: Pokédex/species concepts and PTU mechanical text can be hard to locate or can differ between rule documents/playtest material.

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/h9g7vz/

Design lesson:

Ouros research notes must state exactly whether a seasonal claim comes from Pokémon lore, PTU mechanics, Caelo material, engine code, or a proposed world model. Similar names are not enough to merge them.

A public PokeMedia thread invents its own explanation for why wild versus captured Sawsbuck might change season differently. It is useful only as a warning about plausible-sounding fan extrapolation.

Source:
- https://www.reddit.com/r/PokeMedia/comments/1j6qvxu/

Design lesson:

Fan explanations can inspire questions but must remain non-canon unless supported independently. Ouros should preserve uncertainty rather than silently canonize an attractive biological explanation.

## Reusable narrative structures

A recurrent molt site can become locally important without being a nest, territory or sacred place.

An old shed skin can support identity or movement hypotheses while remaining weaker evidence than direct observation or telemetry.

A population can shift molt timing across years, creating a phenology question without requiring a mechanical Form change.

A visible patchy coat can trigger a welfare report that later resolves as normal molt, producing a small investigation rather than a villain.

A museum or research archive can hold shed material from the same persistent Pokémon across decades, providing a non-invasive longitudinal record if collection was authorized.

A public seasonal festival may have been timed to a highly visible molt/coat transition; climate or local phenology can later desynchronize the cultural date from the biological event.

A road, rail line, trail or development can become important only during a short seasonal window because animals concentrate at a molt/rest site.

## Hard guardrails

- Molt/shedding does not equal PTU `Shed Skin` activation.
- Seasonal coat does not equal a Form change unless authoritative mechanics say so.
- A shed skin/feather/fur sample does not prove the individual is currently nearby.
- Patchy or rough appearance does not diagnose Injury, disease, neglect or low Loyalty.
- Loaded Minecraft appearance does not become authoritative biology.
- Despawn does not mean molt completed.
- Dropped visual particles/items do not automatically become samples or loot.
- Shed material never grants species ownership, DNA rights, capture rights or consent for research.
- Species lore does not define all Ouros populations.

## Canon status

No Ouros species, population, molt site, institutional program, material use, seasonal timing or PTU effect is established by this scan. All worldbuilding derived from it must remain PROPOSED until canon approval.