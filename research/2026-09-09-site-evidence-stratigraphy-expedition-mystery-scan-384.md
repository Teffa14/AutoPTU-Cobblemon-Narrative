# Site evidence, stratigraphy and expedition mystery research — Pass 384

Date: 2026-09-09
Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE

## Repository deduplication

Before external research, the recursive main-branch tree at `e30ca2e3ebf6c54e9bb1dc5062a22e5bd7ab3ec0` was inspected along with CURRENT_FOCUS, canon governance, Pass 383 archaeological design/research/proposal material, Kairos/PTU source routing and current global-NPC provenance modules/tests.

Repository search found no prior references by name to `Ghosts of Knowledge: Kensho`, `Pokémon Ranger: Shadows of Almia`, the CIfA stratigraphic-relationships toolkit or Historic England Historic Environment Records. Recent sources already used in adjacent passes, including Pokémon Gaia, Wastelands, Golurk Rising, PokéTaka, Dreamstone Mysteries, Infinity, Bushido, Valoryn, Prisme, Odyssey and Stalactite, were not processed again.

## Public sources

### CIfA — Checking Stratigraphic Relationships & Correlations

Source: https://www.archaeologists.net/work/toolkits/ag2gp/strat-overview

Reusable structure: primary records, identifiers and stratigraphic relationships are checked and cross-referenced after fieldwork; later analysis can revise interpretation while original records retain their integrity. Relationships such as above, below and equals provide a structured way to reason about sequence without rewriting observations.

Ouros transformation: preserve immutable observation records tied to site revisions, then let later interpretations reference or supersede other interpretations. Do not silently modify the original field observation when a new theory wins.

No archaeological procedure, legal standard or professional authority from the real source becomes Ouros canon.

### Historic England — Historic Environment Records

Source: https://historicengland.org.uk/advice/technical-advice/information-management/hers/

Reusable structure: monuments, fieldwork events, sources and archives can be maintained as linked record families rather than a single flattened description of a place.

Ouros transformation: a persistent ruin or research site should have stable place identity, explicit physical revisions, evidence observations and actor interpretations as linked records. A site database can know that several records concern the same location without asserting that every NPC knows them.

### Ghosts of Knowledge: Kensho

Source: https://pokemonworkshop.com/en/games/ghosts-of-knowledge-kensho/

Reusable structure: exploration begins after an expedition is physically disrupted and separated. Progress is open-ended, path creation and discovery matter, and the lost environment itself carries the mystery.

Ouros transformation: a research party can discover an earlier layer through access change, separation or equipment failure; player progress can come from reconnecting observations across a persistent site rather than from a gym/boss sequence. No characters, forms, locations, plot revelations, maps or exact mechanics are imported.

### Pokémon Ranger: Shadows of Almia

Source: https://en.wikipedia.org/wiki/Pok%C3%A9mon_Ranger%3A_Shadows_of_Almia

Reusable structure: a ruin can simultaneously be an archaeological place, an active extraction/work site and a source of documentary evidence. A later investigation can reveal that present industrial activity and older site history are causally linked.

Ouros transformation: the same persistent location may support research, maintenance, extraction, protection and investigation objectives at different semantic times. Documentary evidence and physical evidence should remain separate records that can corroborate or contradict one another. No named characters, organizations, crystals, locations or story beats are imported.

## Design lessons extracted

The strongest common pattern is layered truth. Physical state, field observation, archive record and interpretation can all be valid at the same time while saying different things.

A useful mystery does not need a false earlier clue. An earlier observation can remain accurate within the site revision that actor actually saw. The new puzzle begins when a later revision exposes a relationship the earlier observer could not access.

Institutional records should be evidence sources, not omniscient truth. An archive can preserve a claim about a site; an NPC needs an explicit access/receipt path before that claim affects their belief.

Revisitation gains value when the same persistent site changes. This supports longer-term arcs in which repair, erosion, excavation, flooding, Pokémon activity or deliberate disturbance changes what can be observed without spawning a disconnected new dungeon.

## PTU/Caelo cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a router rather than a replacement for source text. Relevant authority areas include Researcher, Paleontologist, Topographer and other utility classes, movement, terrain and encounter creation. No specific Feature, item, skill bonus, species or archaeological procedure is inferred from the index alone.

Pass 384 therefore adds no PTU mechanical rule. Any later authored challenge that requires a particular Trainer Feature, item or Move must verify that exact contract against the supplied PTU/Caelo material and engine tests.

## Read-only engine evidence

AutoPTU-Java head inspected: `de73c857d3ae3c20b47f34d1355b2b95dc590ffd`, merge #418. It adds a reusable deterministic nearest-active-opponent resolver and pins Impostor target selection against Python using active/alive/opposing-team filtering, Chebyshev distance and combatant-ID tie breaking. That is concrete evidence for this specific selection seam only.

AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its latest change remains presentation-only viewport synchronization.

Neither engine repository was modified.

## Resulting Ouros direction

Pass 384 turns the Pass 383 site-evidence proposal into an executable first slice: deterministic site revisions, observations and interpretations with snapshot/restore. The intended narrative proof case is `The Foundation That Made Both Maps Correct`, stored separately as PROPOSED / NON-CANON.
