# Pass 259 research — provisional counted-source state and durable identity pressure

Status: RESEARCH / PROVENANCE ONLY. This document does not change canon.

## Question

Pass 258 allows one already-counted `UNRESOLVED_POOL_SLOT` to become a persistent actor without changing abundance. The remaining problem is when that promotion is justified. Ouros needs a bounded middle state so a counted anonymous source can accumulate short-lived individual history without forcing every repeated sighting to become a heavyweight actor.

## Existing Ouros constraints checked before this scan

The full repository tree was inventoried before writing. The active ecology program, source-authority policy, Passes 239–258, recent implementation fixtures, tests and CI validator were checked for overlapping work. Pass 257 already forbids same-site recurrence as identity. Pass 258 already owns the atomic counted-source resolution transaction. Pass 259 therefore only defines the provisional state before that transaction.

The existing Marea/Sendero Fletchling population remains 12. No second Fletchling is canonized here.

## New public-source lessons

### Encounter records and individual records are different objects

Wildbook stores an Encounter first and associates it with a Marked Individual only after identity is assigned. Its matching workflow proposes candidates but requires an identity decision; encounters can also be unassigned or reassigned. Reusable lesson: observation history may exist before durable individual identity, and identity assignment should be reversible/auditable rather than inferred from record count alone.

Sources:
- Wildbook, “Encounter”: https://wildbook.docs.wildme.org/introduction/encounter.html
- Wildbook, “Matching Process”: https://wildbook.docs.wildme.org/data/matching-process.html
- Wildbook, “Marked Individual”: https://wildbook.docs.wildme.org/introduction/marked-individual.html

### Occurrence and organism identity are separate concepts

Darwin Core distinguishes an occurrence at a place/time from an organism whose identity/life history can persist across occurrences. Reusable lesson: an observation can be durable evidence without requiring Ouros to instantiate a persistent actor at the moment of observation.

Source:
- TDWG Darwin Core terms, Occurrence/Organism: https://dwc.tdwg.org/terms/

### Partial identity should remain explicit

USGS work on spatial capture–recapture with partial identity shows that throwing away unresolved observations loses information, while treating uncertain identities as certain can bias abundance inference. Spatial context can help resolve identity probabilistically but is not itself an identity key. Reusable lesson: retain provisional evidence and uncertainty; do not convert uncertainty into extra population members or automatic merges.

Source:
- Augustine et al. (2018), USGS, “Spatial capture–recapture with partial identity: An application to camera traps”: https://www.usgs.gov/publications/spatial-capture-recapture-partial-identity-application-camera-traps

### Aggregation has scaling value but hides individual variation

Ecological modelling literature uses super-individual or representative-individual approaches to reduce computational cost for large populations. Comparative work also warns that aggregation can hide individual-level deviations. Reusable lesson: keep anonymous population representation cheap, but split out a durable actor when individual state becomes consequential enough that aggregation would erase meaningful history.

Sources:
- Scheffer et al. (1995), “Super-individuals: a simple solution for modelling large populations on an individual basis”, Ecological Modelling, DOI 10.1016/0304-3800(94)00055-M.
- Parry & Evans (2008), comparative super-individual modelling study: https://eprints.whiterose.ac.uk/id/eprint/4129/

## PTU / Caelo cross-check

The current AutoPTU oracle was searched read-only for Survival, Perception, trainer-class and audit material. PTU skills/features can affect what a trainer notices or accomplishes, but Pass 259 is persistence bookkeeping rather than a PTU battle mechanic. The provisional record therefore cannot author exact PTU stats, Moves, Abilities, status, damage, Trainer Feature effects, ownership or capture truth.

No project file matching `Caelo` was found in the three current repositories searched (`AutoPTU-Cobblemon-Narrative`, `AutoPTU-Java`, `AutoPTU`). Therefore no Caelo-specific mechanical assertion is added by this pass. This absence is recorded as UNCERTAIN rather than interpreted as permission to invent rules.

## Ouros transformation

CANON-ALIGNED: population totals remain authoritative independently of presentation; observation identity remains epistemically separate from internal source identity; same-site recurrence alone is insufficient; Pass 258 remains the only resolution operation.

PROPOSED: an already-counted anonymous source may own one bounded provisional episode. The episode may retain recent private continuity evidence and short-lived individual ecological history while identity pressure is evaluated.

PROPOSED: promotion pressure is consequence-based, not sighting-count based. State that must remain bound to the same individual across restart or future consequences can demand resolution, provided independent internal continuity evidence exists.

PROPOSED: ephemeral private linkage may expire. Public observation records remain historical evidence. Expiry changes neither abundance nor demographic history.

FIXTURE-ONLY: all Pass 259 source IDs, episode IDs, exact expiry windows and example promotion causes.

UNCERTAIN: exact species-specific retention periods; which future PTU Features can improve evidence; whether physical injury/marker/relationship states will become promotion triggers; the production adapter signal that proves continuity for unresolved slots.

## Copyright boundary

Only high-level data-model and encounter-design lessons are used. No protected campaign prose, dialogue, characters, plots or distinctive quest content is copied.