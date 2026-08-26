# Research Scan — Pokémon Coloration, Camouflage, Mimicry & Visual Signaling — Pass 180

Status: RESEARCH / PROVENANCE. Not canon.
Date: 2026-08-26

## Why this gap is worth adding

The repository already has strong authorities for visual records, taxonomy, evolution/forms, seasonal coverings, courtship, spatial ecology, olfactory landscapes, soundscapes, field signs and social learning. A full-tree audit found no dedicated authority for the biological appearance strategies themselves: background matching, disruptive patterning, masquerade, object imitation, dynamic color change, conspicuous warning-like signals, false-target patterns or context-dependent visual display.

This pass therefore treats coloration and mimicry as observed biological/world-state phenomena. It does not turn them into Accuracy, Evasion, Stealth, Invisibility, Type changes, Abilities, capture modifiers or automatic species identification.

## Existing Ouros boundaries

Visual Records owns photographs, image derivatives and visual identification claims.

Taxonomy owns species/form determinations.

Evolution/Form authority owns actual mechanical Form transitions.

Seasonal Coverings owns molt and reversible covering changes.

Courtship owns reproductive-display interpretation.

Field Signs owns traces left behind.

Spatial Ecology owns home-range and territorial interpretations.

This pass owns only observed appearance state and evidence-backed functional interpretations of that appearance.

## Pokémon sources

### Kecleon: ecological color change is not the Ability Color Change

Official Pokédex material states that Kecleon changes hue to blend into its surroundings and also changes coloration with mood or health. On the same official page, its Ability Color Change is defined separately as changing the Pokémon's Type to the Type of the Move used on it.

Source: https://www.pokemon.com/us/pokedex/kecleon

Reusable structure:

observed appearance shift -> context comparison -> possible concealment/mood/health interpretation -> repeated evidence

Do not collapse this into:

appearance shift -> PTU Color Change trigger

The narrative value is that one persistent Kecleon can accumulate a history of appearance observations across substrates, lighting, stress contexts and seasons without changing identity or Type.

### Sudowoodo: masquerade can be behavioral rather than a mechanical Ability

Official Pokédex material describes Sudowoodo as mimicking a tree to avoid attack while being compositionally more like rock than vegetation. Its listed Abilities are Rock Head and Sturdy, not a generic camouflage Ability.

Source: https://www.pokemon.com/us/pokedex/sudowoodo

Reusable structure:

body shape + stillness + environmental resemblance -> observer misclassification -> later correction

This is useful because mimicry can generate mistaken observations without granting invisibility or a battle bonus.

### Foongus: resemblance can be culturally interpreted without a confirmed origin

Official Pokédex material preserves a theory connecting Foongus's appearance with the modern Poké Ball while explicitly leaving that theory unconfirmed. Official TCG flavor has also used the Poké Ball resemblance as a lure motif.

Sources:
- https://www.pokemon.com/us/pokedex/foongus
- https://assets.pokemon.com/assets/cms2-ru-ru/pdf/trading-card-game/tcg_sun_moon_11_card_translation.pdf

Reusable structure:

striking resemblance -> popular explanation -> repeated retelling -> scientific uncertainty remains

This is a strong model for Ouros public memory: a resemblance can be famous without its evolutionary or historical cause being known.

## Comparative ecology sources

### Camouflage is not one mechanism

NPS describes cryptic coloration as useful both for avoiding predators and for approaching prey, and gives ptarmigan as an example whose appearance changes between summer rock-like and winter snow-like conditions.

Source: https://home.nps.gov/romo/animal_camouflage.htm

Smithsonian library metadata for modern camouflage literature separates background matching, disruptive coloration, countershading and shape/color imitation rather than treating camouflage as a single property.

Source: https://www.si.edu/object/camouflaged-wildlife-how-creatures-hide-order-survive-text-joe-mcdonald-photos-joe-and-mary-ann%3Asiris_sil_1079526

Reusable categories for Ouros research records:

- BACKGROUND_MATCHING
- DISRUPTIVE_PATTERNING
- COUNTERSHADING
- MASQUERADE_OBJECT_RESEMBLANCE
- DYNAMIC_COLOR_CHANGE
- FALSE_TARGET_PATTERN
- CONSPICUOUS_SIGNAL
- UNKNOWN_OR_MULTIFUNCTIONAL

These are scientific interpretations, not mechanical tags.

### Detection and identification are different questions

Experimental research on disruptive coloration distinguishes locating a camouflaged target from correctly identifying it. A pattern may interfere with recognition of body shape even after something has been noticed.

Source: https://www.nature.com/articles/s41598-018-25014-6

This supports a useful Ouros evidence chain:

something visible -> subject localized -> organism recognized -> individual/species identified -> function interpreted

Each step can fail independently.

### Mimicry can involve environmental modification

Smithsonian reporting on flea beetles describes a camouflage strategy where feeding damage creates beetle-shaped holes that act as visual decoys. The useful abstraction is that concealment can depend on a modified background rather than the body alone.

Source: https://www.si.edu/stories/tiny-beetles-chew-their-way-out-sight

Ouros can therefore support authored cases where a Pokémon's repeated interaction with bark, leaves, stones, sand, litter or structures changes the visual context in which it becomes difficult to distinguish.

## PTU campaign-design sources

The official PTU GM guidance recommends simple early encounters built around territorial wild Pokémon, injured Pokémon or retrieval problems, while warning that PTU combat can overwhelm early parties if encounter complexity is too high.

Source: https://pokemontabletop.com/gm-advice-your-first-ptu-session/

For Pass 180 the reusable lesson is to let camouflage affect how an encounter is framed or investigated without silently modifying combat math. A concealed subject can be discovered through world-state investigation before a normal battle begins.

A current public PTU campaign listing framed around social ecology emphasizes mysteries arising from relationships between society and nature. This is useful only as a high-level validation that ecological mystery can sustain a long PTU campaign; no characters or political plot are imported.

Source: https://startplaying.games/adventure/clnt20u4d000208ma3ty01n49

## Design lessons for Ouros

1. Appearance state must be evidence-bearing, not a hidden Accuracy/Evasion modifier.
2. Observation, detection, identification and functional interpretation must remain separate.
3. Resemblance does not prove evolutionary relationship, Form identity or intent.
4. A visual signal can have multiple proposed functions across contexts.
5. Dynamic coloration needs a time series if researchers want to distinguish substrate matching, physiological state, social display or another cause.
6. A famous folk explanation can stay culturally important after science weakens it.
7. Minecraft texture/skin state cannot become scientific truth by itself.
8. Camouflage should often create investigation content before battle rather than custom combat rules.

## PTU / AutoPTU cross-check

AutoPTU's current PTU ability tracker records Color Change as an implemented Python ability that changes Type to the triggering Move's Type when hit. This is a concrete mechanical contract and must not be reused for Kecleon's ecological color matching.

AutoPTU also contains many Ability and Move hooks whose names can sound visually relevant. Their existence proves only their exact rules behavior.

AutoPTU-Java head inspected for this pass: `b66fcb4dac909c2f44bf6caf54a15f8da82e3e0a`.

The latest Java slice adds an effective Accuracy-stage projection primitive. It improves a calculation boundary. It does not create camouflage, concealment, visual detection, Stealth AI, invisibility, mimicry or Minecraft appearance authority.

AutoPTU Python head inspected: `ad9c202ec9e3982c6797bd38b14df8f647852fc9`.

Its latest inspected change is Career validation and does not alter the battle capability map.

## Caelo / helper status

No reliable complete Caelo primary corpus defining camouflage, concealment, visual identification or mimicry was recovered during this run.

Super PTU Online Helper was not exposed as an invocable capability.

No output is attributed to either source.

## Candidate Ouros direction

A useful long-term layer should let one persistent Pokémon accumulate appearance observations such as:

forest bark -> almost perfect background match

wet stone -> poor match but strong shape masquerade

urban wall -> color shift observed, function uncertain

courtship season -> bright pattern appears only during social display

injury/recovery period -> color variation correlates with condition but causation remains uncertain

The same data can later support Visual Records, Taxonomy, Care, Courtship, Social Learning or Public Memory without any one system overwriting the others.