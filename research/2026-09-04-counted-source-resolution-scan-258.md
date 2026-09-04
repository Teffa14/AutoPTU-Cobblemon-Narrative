# Pass 258 research — counted-source identity resolution

Status: RESEARCH / PROVENANCE ONLY. Nothing in this note promotes a new Fletchling individual, marker, site, NPC, institution, or encounter fact to canon.

## Gap after Pass 257

Pass 257 correctly separates site-use history from individual identity. The remaining architecture gap is different: an `UNRESOLVED_POOL_SLOT` can already be part of a population total and later accumulate enough durable individual-specific state that keeping it anonymous becomes unsafe. Ouros needs a transaction that changes the representation of one already-counted source from unresolved to persistent without changing abundance.

This is an internal ecology/identity operation. It is deliberately separate from player-facing recognition under Passes 253–254.

## New public sources

### Wildbook — encounter first, identity assignment later

Wildbook documentation separates an animal Encounter from later individual-ID assignment. Matching produces candidate results for review; an encounter can have its individual ID set later. The useful structure is `observation record -> candidate matching -> reviewed identity assignment -> individual history`, rather than `every sighting creates an individual`.

Source: Wildbook documentation, “Matching Process,” accessed 2026-09-04: https://wildbook.docs.wildme.org/data/matching-process.html

Reusable Ouros lesson: observation persistence and persistent-individual resolution can be separate lifecycle stages. Candidate similarity must not create an identity automatically.

### USGS — partial identity must not be treated as several known individuals

Augustine et al. describe spatial capture–recapture where observations may contain only partial identity. Their model uses location and other evidence to probabilistically resolve identity instead of discarding partial histories or assuming deterministic identities. The paper is useful here because identity uncertainty and abundance inference are coupled: bad identity treatment can bias population inference.

Source: U.S. Geological Survey, “Spatial capture–recapture with partial identity: An application to camera traps,” 2018: https://www.usgs.gov/publications/spatial-capture-recapture-partial-identity-application-camera-traps

Reusable Ouros lesson: uncertainty belongs in the identity layer. It must not be converted into extra animals in the population ledger.

### USGS — categorical evidence can narrow identity without proving it

Augustine et al. later show that partially identifying covariates can reduce identity uncertainty while still requiring a latent/partial-identity model. Spatial proximity becomes more or less informative depending on density and home-range structure.

Source: U.S. Geological Survey, “Spatial capture–recapture for categorically marked populations with an application to genetic capture–recapture,” 2019: https://www.usgs.gov/publications/spatial-capture-recapture-categorically-marked-populations-application-genetic-capture

Reusable Ouros lesson: site, morphology, behavior, time and other covariates may narrow candidates. None should silently become an internal primary key. This directly reinforces Pass 257.

### Wildbook — individual records collect later encounters

Wildbook’s analysis workflow produces ranked potential matches and individual pages that accumulate where/when an identified animal was seen. This suggests a clean transition: prior encounter history can be attached to the resolved individual once the assignment is made, while preserving provenance of the original observations.

Source: Wildbook documentation, “Image Analysis Pipeline,” accessed 2026-09-04: https://wildbook.docs.wildme.org/introduction/image-analysis-pipeline.html

Reusable Ouros lesson: identity resolution should preserve encounter provenance rather than rewrite earlier observations as if certainty had existed from the start.

## PTU / Caelo cross-check boundary

No PTU rule located in the current project evidence grants a trainer omniscient persistent identity merely because a wild Pokémon has been observed repeatedly. Existing Ouros contracts already keep Survival/Perception-style evidence and Trainer Features separate from hidden ledger identity. Pass 258 therefore adds no PTU Skill, Feature, stat, capture, ownership, battle or species rule.

Caelo/Ouros setting authority remains unchanged. The canon population total and the already-approved first persistent Fletchling are inputs; this pass does not establish a second canon individual.

## Derived design rules

1. Resolution is a source-category conversion, never a demographic event.
2. Exactly one already-counted unresolved source is consumed by exactly one persistent source.
3. `population.total` is invariant across the transaction.
4. Source lineage and observation provenance survive the conversion.
5. The retired unresolved source can never lease or materialize again.
6. Replaying the same resolution transaction is idempotent.
7. Ambiguous source lineage fails closed.
8. Same-site recurrence is insufficient, consistent with Pass 257.
9. Internal certainty and character-facing certainty are independent. Ouros may have a deterministic lineage reason to individualize a source while the character still sees only `POSSIBLE` or `PROBABLE` identity evidence.
10. Resolving a source must not open AutoPTU or mutate PTU state.

## Status classification

CANON-ALIGNED: population conservation; source-before-projection; internal IDs are hidden from public knowledge; Pass 253/254 recognition remains separate; Pass 257 site use cannot alias identity.

PROPOSED: the generic `RESOLVE_COUNTED_SOURCE` transaction and its invariants.

FIXTURE-ONLY: any second resolved Fletchling ID used by Pass 258 tests, its observation history, and the trigger that makes durable individual state necessary.

UNCERTAIN: the production threshold for when an unresolved counted member should be individualized; which source-lineage signal is strong enough in the real adapter; whether long-lived individual ecological state alone should force resolution or merely make it desirable.
