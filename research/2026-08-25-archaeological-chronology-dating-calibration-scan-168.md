# Archaeological Chronology, Dating, and Calibration — Research Scan 168

Status: research/provenance only. Not established Ouros canon.

Date: 2026-08-25

## Scope and repository fit

The repository already has a deep-history authority in `design/myth-archaeology-sacred-sites-layer.md`. That layer owns archaeological sites, stratigraphic contexts, observations, interventions and historical interpretations. It already stores an `estimated_period`, but it does not define a shared workflow for how chronological claims are produced, calibrated, revised or compared.

Pass 168 fills that narrower gap. It does not create another Archaeology system.

Related authorities remain separate:

- Myth/Archaeology/Sacred Sites owns the site, contexts, interventions and historical claims.
- Material Culture owns persistent artifact identity and provenance.
- Paleontology owns fossil localities and deep-time biological interpretation.
- Museums owns accession, conservation, exhibition and collection custody.
- Metrology owns instrument/reference traceability and uncertainty where a dating method uses measured quantities.
- Timekeeping owns modern timestamp conventions, not ancient chronology.
- Science owns datasets, analyses and publications.
- Languages owns inscriptions, translations and terminology.
- Research Ethics and site stewardship own sampling authorization.
- Minecraft/Cobblemon cannot infer age from blocks, depth or visual style.

## New-source findings

### Relative and numeric chronology answer different questions

The U.S. National Park Service distinguishes relative dating, which orders events, from methods that produce numeric or calendar age estimates. Very few archaeological objects can be assigned a single exact date. Stratigraphy, cross-dating, seriation, dendrochronology, radiocarbon, thermoluminescence and terminus post/ante quem constraints provide different kinds of evidence.

Reusable Ouros lesson: never collapse all chronology into `year = X`. A context may only be `earlier_than_context_B`; another may have a broad interval; a timber may have a narrow felling estimate while the building event remains later or uncertain.

Sources:
https://www.nps.gov/articles/000/how-do-archeologists-date-sites-and-artifacts.htm
https://www.nps.gov/articles/000/how-do-archeologists-know-how-old-a-site-is.htm

### Stratigraphy is powerful only when context is understood

NPS material on superposition explains that undisturbed lower layers are generally older than layers above them. Archaeological teaching material also emphasizes that later digging, animal burrows, construction and other disturbance can move objects between strata.

Reusable Ouros lesson: `deeper = older` is a hypothesis conditioned on context integrity. A modern intrusion can contain an old object. A redeposited ancient object can occur inside a younger fill. The original observation must survive even when the chronological interpretation changes.

Sources:
https://www.nps.gov/articles/geologic-principles-superposition-and-original-horizontality.htm
https://home.nps.gov/orgs/1539/learn-about-archeology.htm

### A dated material is not automatically the event being investigated

NPS dendrochronology guidance notes that tree-ring analysis can date growth and sometimes felling very precisely, but a timber may have been reused or stored before construction. A tree death date therefore does not automatically equal a building date.

Reusable Ouros lesson: every chronological result needs an explicit `dated_subject` and `inference_target`. `WOOD_FELLING`, `CHARCOAL_FORMATION`, `CERAMIC_PRODUCTION`, `DEPOSIT_FORMATION`, `STRUCTURE_CONSTRUCTION` and `SITE_OCCUPATION` must not be interchangeable.

Sources:
https://www.nps.gov/articles/archeology-dendrochronology.htm
https://home.nps.gov/tont/learn/nature/dendrochronology.htm

### Radiocarbon results require calibration and can be revised without changing the sample

The IntCal working group publishes calibration curves used to convert radiocarbon measurements into calendar-age estimates. IntCal20 replaced earlier curve versions and extends the Northern Hemisphere calibration framework to 55,000 calibrated years before present. The underlying principle is important for Ouros: a laboratory measurement may remain unchanged while a later calibration model changes the interpreted calendar interval.

Reusable Ouros lesson: store raw measurement/result provenance separately from calibration revision and published interval. Recalibration creates a new chronological interpretation, not a new historical event.

Sources:
https://www.intcal.org/publications.html
https://eprints.gla.ac.uk/210753/

### Chronological precision depends on method, material and regional reference sequences

Dendrochronology can be extremely precise when suitable wood, preserved outer rings and a strong regional reference chronology exist. NPS also documents sites where hundreds of samples produced only a few usable dates because the material was unsuitable.

Reusable Ouros lesson: a sophisticated institution can legitimately fail to date a sample. `NO_USABLE_DATE` is a valid result. Method availability must depend on authored technology, sample condition and reference datasets rather than narrative convenience.

Sources:
https://www.nps.gov/articles/tonto-dendrochronology.htm
https://www.nps.gov/meve/learn/education/tree-rings.htm

## Pokémon and spin-off inspiration

### Relic Castle — physical burial can preserve several histories at once

Relic Castle is an ancient Unovan city/castle complex that became progressively buried in desert sand. Different games expose different portions of the ruins, and excavation/access changes what later visitors can reach.

Reusable structure: one site can contain construction history, burial history, later excavation history and modern access history. A layer of sand above architecture establishes a relative sequence but does not by itself give the construction a calendar date.

Source:
https://bulbapedia.bulbagarden.net/wiki/Relic_Castle

### Solaceon Ruins — inscriptions and spatial sequence can guide exploration without proving age

Solaceon Ruins combine repeated chambers, inscriptions and Unown-associated writing. Their structure is useful for separating `what the inscription says`, `where it occurs`, `when the wall was built`, `when the inscription was made` and `when modern researchers interpreted it`.

Reusable structure: a deciphered text can be genuine while its date remains uncertain. A later inscription on an older wall does not inherit the wall's age.

Source:
https://bulbapedia.bulbagarden.net/wiki/Solaceon_Ruins

### PTU community ruin puzzles — puzzle solution must not become chronology proof

A public Pokémon Tabletop campaign puzzle used carved Pokémon, Unown symbols and environmental motifs inside old ruins. The useful lesson is encounter grammar: architecture and inscriptions can gate exploration and invite interpretation. Ouros adds a stricter evidence boundary: solving the intended puzzle can open a door without proving who built it, when it was built or whether the modern reading matches the original cultural meaning.

Source:
https://www.reddit.com/r/PokemonTabletop/comments/1e3huvj/

Another PTU discussion proposes a multi-part ruin puzzle leading toward ancient/fossil Pokémon environments. The reusable lesson is to distribute evidence across several locations rather than place one omniscient tablet at the end.

Source:
https://www.reddit.com/r/PokemonTabletop/comments/110yfpe/

## PTU / project-source cross-check

Public PTU 1.05 material describes Occult Education as potentially relevant to magical ancient ruins such as the Ruins of Alph, while also stating that campaigns may treat ancient ruins as largely mundane. This is an important boundary: the presence of ruins does not automatically make chronology an Occult Education problem.

Source:
https://pturpg.wikidot.com/skills

No evidence inspected in AutoPTU-Java demonstrates an archaeological dating subsystem, laboratory simulation, automatic historical identification or a generic rule that converts Skills into calendar dates. This pass therefore does not invent chronology DCs, Skill bonuses, sample-processing times or supernatural dating.

Caelo-specific chronology rules were not recovered reliably in the accessible project material during this pass. Super PTU Online Helper was not exposed as an invocable capability.

## High-value Ouros design lessons

1. Preserve relative chronology even when numeric dates are unavailable.
2. Store the object being directly dated separately from the historical event being inferred.
3. Context integrity must be explicit; redeposition and intrusion are normal hypotheses, not automatic misconduct.
4. Raw measurements and samples survive later calibration revisions.
5. A date interval should preserve method, laboratory/institution, calibration/reference revision and uncertainty.
6. Exact-looking numbers must not imply exact historical knowledge.
7. Different methods can disagree without either institution being fraudulent.
8. Reused materials can be older than the structures containing them.
9. A later inscription can occur on an older wall.
10. A famous traditional date can remain culturally important after scientific revision.
11. `NO_USABLE_DATE` and `UNRESOLVED` are valid outcomes.
12. Excavation can improve chronology while destroying unrecoverable context if poorly documented.
13. New reference datasets can change historical estimates without retconning Chronicle events.
14. Dungeon puzzles can reveal access or cultural practice without acting as dating instruments.
15. Minecraft depth, block palette and weathering visuals can never become authoritative chronological evidence by themselves.

## Copyright / transformation note

External material above is used only for abstract structures, scientific constraints and encounter grammar. No protected dialogue, puzzle solution, distinctive character arc or plot is copied into Ouros.

## Open questions

Which Ouros institutions can perform which dating methods? Which methods exist technologically at campaign start? Are any long regional tree-ring or other reference sequences already established? How are deep-history calendars expressed across Languages and Timekeeping? Which sampling actions require explicit stewardship approval? Which chronology claims are public versus restricted for sensitive sites? Which Caelo rules, if any, modify archaeological fieldwork or laboratory analysis?
