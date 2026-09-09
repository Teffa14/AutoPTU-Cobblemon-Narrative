# Persistent world-evidence checkpoint research — Pass 387

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-09
Canon effect: NONE

## Repository-first inspection and deduplication

Baseline inspected before writing: `6da348ecbdb77b4980ed6495f0e09dde2bea7bc7` (Pass 386).

The recursive repository tree, current focus, canon governance, Pass 383–386 archaeology chain, `OUROS_SITE_EVIDENCE_LEDGER_V1`, observer-only knowledge bridge, private interpretation bridge, their tests, global-NPC checkpoint family, CI paths and Kairos/PTU source router were inspected before selecting a new seam.

Recent research already used or explicitly excluded Gaia, Reborn, Wastelands, Infinity, Tectonic, Clockwork was not present, Harris Matrix was not present, CIDOC CRM, CIfA inference guidance, archaeological context recording, Giant in the Playground PTU logs, Frozen Spirit, Dreamstone Mysteries, Golurk Rising, PokéTaka, Valoryn, Prisme, Bushido and Odyssey. These were not recycled as primary inspiration except CIfA is referenced below only for a new stratigraphic relationship point not previously used as the central structure.

## Source 1 — Harris Matrix: physical relationships need a durable sequence

Sources:
- https://harrismatrix.com/about-the-matrix/
- https://harrismatrix.com/about-the-book/

The Harris Matrix represents archaeological stratification as explicit relationships among uniquely identified units through relative time. Its value is not a single photograph of the current surface. It preserves the sequence needed to reconstruct how the visible site came to exist.

Reusable Ouros structure:
- persistent world evidence needs an owner whose snapshot preserves the sequence of physical revisions;
- a later visible condition must not replace the earlier recorded state;
- the recovery unit must keep enough identity to distinguish two different historical snapshots of the same site.

No archaeological terminology is promoted to Ouros canon as an in-world institution or procedure.

## Source 2 — CIfA: cross-check relationships rather than flatten discrepancies

Source:
- https://www.archaeologists.net/work/toolkits/ag2gp/strat-overview

CIfA guidance calls for recording stratigraphic relationships such as above/below/equivalent and using the resulting matrix to cross-check primary records. Different pieces of documentation can expose disparities that need investigation instead of silent normalization.

Reusable Ouros structure:
- checkpoint restore should validate the relationships among site evidence, direct-observation materialization and private inference;
- a valid hash alone is insufficient if the restored records no longer agree semantically;
- a bridge record must fail closed when its evidence owner or private claim history has diverged.

## Source 3 — Pokémon Clockwork: one place can support distinct temporal readings

Sources:
- official project page: https://pokemonclockwork.wixsite.com/clockworkgame
- public project summary: https://pokemon-fan-game.fandom.com/wiki/Pok%C3%A9mon_Clockwork

The public feature list includes travel between past and present, a quest system and timed encounters. Ouros does not import time travel, Rosari, Celebi, Team Epsilon, characters, quests, maps, mechanics or story.

Reusable structural lesson:
- the same geographic identity can be encountered under materially different temporal states;
- what an actor can observe depends on which state they actually reached;
- revisiting a place can change interpretation without invalidating a prior observation made under an earlier state.

Ouros adapts this without supernatural time travel: restoration, collapse, excavation, flooding, construction, seasonal exposure or emergency access changes can create distinct site revisions.

## PTU/Caelo cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing aid. It points to Researcher, Paleontologist, Topographer, Skills/Edges/Features, movement/terrain, campaign structure and encounter construction in the supplied PTU/Kairos material. Pass 387 does not infer a new Skill check, Trainer Feature, excavation action, Item behavior, species placement or battle permission.

The PTU running-the-game material already supports ancient ruins as adventure locations and emphasizes that reaching them may itself be part of the challenge. This pass uses that only as setting/mechanical compatibility evidence, not as new Ouros canon.

## Read-only engine evidence

AutoPTU-Java inspected head: `01a7787048ba92068f8c1340d80c9e9cb89c371d` (merge #419). The demonstrated change remains seeded Impostor Ability selection plus the subsequent RNG-stream parity for that exact scenario.

AutoPTU Python inspected head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change remains presentation-only viewport synchronization.

No engine repository is modified by this pass.

## Design conclusion

Pass 386 left three related owners without a coherent recovery boundary. Appending archaeology-specific state directly to `OUROS_NPC_WORLD_CHECKPOINT_V19` would mix persistent-world evidence ownership with world-agent action provenance.

The safer boundary is a separate `OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V1` that owns site-evidence and bridge snapshots while binding them cryptographically to the exact external `KnowledgeLedgerStore` recovery state. Private NPC memory remains owned by the global-NPC recovery system.

This produces a deliberate two-owner recovery relation:

`GLOBAL_NPC_PRIVATE_KNOWLEDGE <-> PERSISTENT_WORLD_EVIDENCE`

Neither side is allowed to restore against an unrelated version of the other.
