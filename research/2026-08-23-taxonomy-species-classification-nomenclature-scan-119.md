# Research Scan — Taxonomy, Species Classification & Nomenclature — Pass 119

Status: research/provenance only. Not Ouros canon. Not PTU/Caelo rules authority.

## Why this pass exists

The repository already has Science, Evolution, Island Biogeography, Biosecurity, Field Signs, Photography, Metrology, Archives and many ecology layers. Those systems can produce observations about Pokémon, but none currently owns the classification question: what species or form an observation belongs to, how confident that determination is, which name/version was used at the time, and how a later reclassification affects old records.

Internal inventory review found no dedicated taxonomy/classification/nomenclature layer. The closest authorities are:

- `design/science-research-discovery-layer.md`, which owns observations, datasets, hypotheses and publications;
- `design/evolution-life-stage-transformation-layer.md`, which owns persistent individual identity through species-changing evolution;
- `design/island-biogeography-endemism-dispersal-layer.md`, which owns population differentiation and endemism claims;
- `design/metrology-calibration-measurement-standards-layer.md`, which owns measurement provenance and comparability;
- `design/archives-museums-collections-preservation-layer.md`, which owns preserved records/specimens and changing catalog interpretations.

Pass 119 adds the missing cross-cutting classification authority without changing canonical Pokémon mechanics or inventing new species/forms.

## Source 1 — Wiglett: resemblance can be misleading

Source: official Pokémon Pokédex, Wiglett.
https://www.pokemon.com/es/pokedex/wiglett

The official entry states that Wiglett resembles Diglett but is a different species, and attributes the resemblance to adaptation to the environment.

Reusable Ouros structure:

- visible resemblance is evidence, not identity;
- a provisional field identification may later be corrected;
- ecological convergence can explain similarity without kinship;
- the original observation remains valid even when its label changes.

Ouros should therefore store the observed body/behavior separately from the taxonomic determination attached to the record.

## Source 2 — Wugtrio: an older classification can remain historical evidence

Source: official Pokémon Pokédex, Wugtrio.
https://www.pokemon.com/us/pokedex/wugtrio

The official entry notes that Wugtrio was once considered a regional form of Dugtrio before being recognized as a different kind of Pokémon.

Reusable Ouros structure:

A reclassification should create a new classification revision, not rewrite every historical document. An old field guide can remain historically accurate about what experts believed at the time while being taxonomically superseded today.

This creates useful mysteries:

- two museums can use different labels because one exhibit is old;
- an archive search under the current name can miss records filed under a superseded name;
- an old route report can describe the right Pokémon under the wrong classification;
- public memory can lag behind institutional taxonomy.

## Source 3 — Toedscool: similar body plan, different lineage and ecology

Source: official Pokémon Pokédex, Toedscool.
https://www.pokemon.com/uk/pokedex/toedscool

The entry explicitly says Toedscool resembles Tentacool but is a completely different species and places it in humid forests.

Reusable Ouros structure:

Morphology, habitat, Type, behavior and evolutionary line are separate evidence dimensions. A field team should be able to record “Tentacool-like morphology in forest habitat” before knowing what the classification means.

Do not convert resemblance into a hidden evolution relationship, shared Ability, common ancestry or mechanical compatibility.

## Source 4 — Regional forms are recognized variants of a species

Source: official Pokémon Sword/Shield site, Galarian forms.
https://swordshield.pokemon.com/en-us/pokemon-galar-region/galarian-forms/

The official site describes regional forms as Pokémon that adapted to a specific region and can differ in appearance and behavior from the same species elsewhere.

Source: official Pokémon Legends: Arceus site, Hisuian forms.
https://legends.arceus.pokemon.com/en-au/pokemon/

The site distinguishes newly discovered Pokémon from regional forms and lists Hisuian forms as forms found specifically in Hisui.

Reusable Ouros structure:

- species identity and form identity must be separate fields;
- region-associated form does not imply every individual in the region uses that form;
- form recognition is a canonical content dependency, not something procedural generation may invent;
- a newly observed phenotype can remain `UNRESOLVED_VARIANT` until authoritative content or authored canon defines it.

## Source 5 — Basculin: classification can remain genuinely contested

Source: official Pokémon Pokédex, Basculin.
https://www.pokemon.com/us/pokedex/basculin

The Pokédex includes an entry where a Basculin ecology is described as sufficiently different that theories of separate species status gained traction.

Reusable Ouros structure:

The world can contain legitimate unresolved classification debates. The system should support:

- competing hypotheses;
- evidence for and against a split;
- institution-specific positions;
- a final state of `UNRESOLVED` for years if evidence remains insufficient.

The generator should not force every dispute to resolve during a quest.

## Source 6 — PTU Pokédex data is a rules/content source, not a narrative inference engine

Source: Pokémon Tabletop forum, Gen 8 Pokédex.
https://www.tapatalk.com/groups/pokemon_tabletop/gen-8-pokedex-t7257.html

The public PTU community release describes a Gen 8 Pokédex compatible with PTU 1.05 plus referenced errata/updates. This reinforces that PTU species records are curated rule content with specific Moves/Abilities/statlines rather than something narrative generation should derive from resemblance.

Source: Pokémon Tabletop forum, PTU 1.05 Gen 7 Pokédex compilation/update.
https://www.tapatalk.com/groups/pokemon_tabletop/ptu-1-05-gen-7-pokedex-and-reference-compilation-a-t3524.html

The update history demonstrates that a rules Pokédex itself can have versions and revisions.

Ouros implication:

`mechanical_species_key` must point to an authoritative PTU/AutoPTU species/form record. Narrative taxonomy may have historical or provisional names around it, but it may never fabricate Types, stats, Moves, Abilities, capabilities or evolution links.

## Source 7 — PTU campaigns use researchers and Pokédexes as ongoing world institutions

Source: public PTU campaign log #3.
https://www.reddit.com/r/PokemonTabletop/comments/mfgwzd

The log includes PCs leaving another character behind to work with a professor while travel and encounters continue. The reusable pattern is institutional research occurring in parallel with player travel rather than every classification task becoming a battle.

Source: Thrilling Intent PTU session synopsis.
https://thrilling-intent.fandom.com/wiki/Pokemon_Tabletop_United

The campaign begins with a professor distributing Pokédexes and Pokémon to PCs before sending them onward. The useful high-level pattern is that a Pokédex can be an instrument of a research network and travel campaign, not an omniscient encyclopedia.

No protected dialogue, characters or plots are imported.

## Source 8 — eDNA: detection is not the same as confirmed live presence

Source: USGS Resource Manager's eDNA Toolbox.
https://www.usgs.gov/centers/upper-midwest-environmental-sciences-center/science/resource-managers-edna-toolbox

USGS notes that environmental DNA can detect rare/cryptic species but that DNA can be transported, persist after the organism leaves, or produce false positives/negatives.

Source: USGS, “What do you mean by false positive?”
https://www.usgs.gov/publications/what-do-you-mean-false-positive

The source distinguishes detection at sample level from inference of taxon presence at site level.

Ouros adaptation:

A molecular or residue detection should be represented as evidence such as `TAXON_SIGNAL`, not as “Pokémon currently present.” This integrates cleanly with Field Signs and Science.

## Source 9 — reproducible taxonomy and reference libraries

Source: USGS eDNA Taxonomy Pipeline, released 2 May 2026.
https://www.usgs.gov/software/edna-taxonomy-pipeline

The project emphasizes reproducible taxonomic assignment against reference libraries rather than opaque classification.

Ouros adaptation:

When technological level permits, a classification can record:

- method;
- reference-library version;
- candidate matches;
- confidence/quality state;
- reviewer;
- unresolved ambiguity.

The layer must remain technology-agnostic. A region without molecular methods can classify from morphology, behavior, calls, tracks, photographs, specimens or expert comparison.

## Source 10 — names and accepted classifications can change while occurrence records persist

Source: GBIF Backbone Taxonomy.
https://www.gbif.org/dataset/d7dddbf4-2cf0-4f39-9b2a-bb099caae36c

GBIF uses a common taxonomy to reconcile names from multiple datasets.

Source: GBIF training, handling taxonomic uncertainty.
https://training.gbif.org/en/data-use/taxonomic-uncertainty

The material distinguishes accepted names from synonyms and recommends retaining evidence that can support later validation.

Reusable Ouros structure:

- stable `taxon_concept_id` separate from display name;
- name history and synonyms;
- determination history per observation/specimen;
- reclassification without deleting occurrence history;
- uncertain records allowed at higher level or unresolved concept.

No real-world nomenclatural code is imported into Ouros.

## Reusable narrative structures

### The correct observation with the wrong label

A field team accurately records morphology, location and behavior but assigns the wrong species name. Years later another team corrects the classification. The first record remains scientifically useful.

### The field guide is outdated

A route guide, museum panel and ranger handbook use different names because they were published under different taxonomic revisions. The quest is reconciliation, not exposing fraud.

### The “new species” that is not new

A spectacular observation goes public before comparison with archived specimens. The same population was documented decades earlier under another name.

### The “regional form” that is only behavioral variation

A local population looks or acts differently, but current evidence does not support a canonical form. Ouros records population differentiation without inventing a new PTU form.

### The suspected duplicate

Two Pokédex records may represent the same taxon, or one record may have combined two species. Reanalysis of photos, calls, tracks, specimens and geography can resolve or preserve the ambiguity.

### The reference library is incomplete

A sample produces an uncertain match because the comparison library lacks relevant populations. The right response can be new sampling rather than forcing the nearest known label.

### The local name remains valid culturally

A community can retain a historical or local name after scientific nomenclature changes. Public-facing systems should cross-reference rather than erase it.

## Character and institution archetypes

- field naturalist who recognizes habitat and behavior better than formal taxonomy;
- museum curator maintaining synonym history across old specimens;
- young taxonomist whose proposed split is plausible but not yet accepted;
- ranger using a practical local field name while the university uses a formal concept ID;
- archivist who finds the oldest specimen under a superseded label;
- molecular analyst who refuses to overstate a weak match;
- professor famous for a classification later revised without making the professor fraudulent;
- community expert whose local distinctions predate institutional recognition;
- Pokédex editor maintaining crosswalks between old and new classifications.

## Quest, dungeon and mystery hooks

- compare three records of a Tentacool-like forest Pokémon before deciding whether they describe one taxon;
- recover an old museum specimen whose original label no longer matches the current catalog;
- revisit a route after reports of a “new regional form” and determine what is actually observed;
- trace an eDNA-like signal upstream without claiming live presence at the sampling point;
- compare calls, footprints and photographs that disagree about the maker;
- reconstruct which species name an old conservation agreement intended;
- decide whether two island populations warrant separate management before taxonomy is resolved;
- find that a suspected rare species is a familiar species in an unusual life stage;
- discover that two rival researchers are using different species concepts rather than different raw evidence.

## Mechanical boundaries

This pass creates no PTU/Caelo rule.

Do not infer:

- visual resemblance -> shared species/form;
- ecological similarity -> evolution relation;
- local variation -> regional form;
- unusual color -> Shiny or new form;
- taxonomic split -> new PTU species entry;
- provisional species -> new Types/Abilities/Moves/stats;
- Pokédex scan -> perfect identification;
- researcher opinion -> world truth;
- eDNA/scent/track detection -> currently loaded Pokémon;
- museum specimen -> mechanically usable held item;
- scientific name -> ownership/authority;
- taxonomic uncertainty -> Accuracy/evasion/status modifier;
- newly recognized species -> rare-spawn bonus.

## PTU/Caelo validation state

The project's primary Caelo Core/Player/encounter/character-creation source corpus was not recovered from the accessible file library during this run. File-library search returned the prior narrative arc research package, which itself treats public PTU resources as context and the pinned AutoPTU dataset as mechanical authority. Super PTU Online Helper was not available as an invocable capability.

Public PTU sources were therefore used only for content/version context. No Pokédex Skill check, Pokémon Education DC, Researcher Feature, identification bonus, specimen rule, taxonomy mechanic or Fakemon rule was imported.

Generation 9 examples such as Wiglett and Toedscool are narrative/reference examples only. They do not imply that current PTU 1.05/Gen 8 mechanical data already contains those species.

## Design conclusion

The durable Ouros chain should be:

physical Pokémon/population -> observation/sample/media -> taxonomic determination -> taxon concept/version -> accepted/institutional position -> public name/field guide -> actor knowledge.

The classification can change while the observed world event stays fixed. That gives Ouros a way to support genuine discovery, scientific disagreement and historical continuity without retconning evidence or inventing Pokémon mechanics.