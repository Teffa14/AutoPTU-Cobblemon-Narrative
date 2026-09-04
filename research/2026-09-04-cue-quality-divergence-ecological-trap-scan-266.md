# Cue-quality divergence and ecological-trap scan — Pass 266

Status: RESEARCH / PROVENANCE ONLY. Nothing in this note promotes a Marea/Sendero ecological trap, anthropogenic cue, site-quality conclusion or new actor to canon.

## Question

Pass 265 established that a temporary resource pulse can concentrate already-counted Pokémon without changing abundance. This pass asks a different question: can repeated attraction or use of a site be treated as evidence that the site is beneficial?

## Public-source findings

Schlaepfer, Runge and Sherman (2002), indexed by USGS as “Ecological and evolutionary traps,” describe rapid environmental change breaking the historical association between environmental cues and adaptive outcomes. The reusable structure is cue/outcome separation: an organism can respond to a formerly useful cue even when the changed environment produces worse survival or reproduction.

Hale and Swearer (2015), “Identifying, preventing and mitigating ecological traps,” summarize a stricter evidentiary standard. Demonstrating an ecological trap requires habitat preference/selection evidence, a difference in fitness or an appropriate outcome proxy between habitats, and evidence that the selected/equally selected habitat is the lower-quality option. Repeated occupancy alone is insufficient.

Courtois et al. (2021) show why multiple cues must remain separate from quality. Tree swallows selected sites using several environmental and social cues, while some cue-preference relationships did not align with reproductive performance. Ouros should therefore store candidate cues and outcome evidence independently rather than collapsing them into a single “habitat score.”

Oro et al. (2013) and Newsome et al. (2015) review anthropogenic food subsidies. Human-provided resources can change activity, diet, movement, abundance and interactions, with benefits or costs depending on species and context. A human-associated resource cannot be globally labeled beneficial or harmful by default.

Pokémon campaign/game-design reuse is deliberately high-level here: investigation works when first impressions can be revised by longitudinal evidence. The Ouros adaptation is an environmental mystery where visible concentration creates a hypothesis, later comparison tests it, and the world can preserve uncertainty rather than revealing an answer immediately. No protected characters, dialogue, plots or locations are imported.

## Reusable Ouros structures

Separate `CUE_STATE`, `SELECTION_EVIDENCE` and `SITE_QUALITY_EVIDENCE`.

Treat repeated presence, visible aggregation and site fidelity as observations. They can strengthen evidence that a site is used. They cannot by themselves prove preference, benefit, harm, demographic growth or an ecological trap.

Reserve `ECOLOGICAL_TRAP_SUPPORTED` for a deliberately high bar: admissible selection/preference evidence plus comparative evidence that outcomes are worse at the selected site than at available alternatives. Where either side is missing, preserve `TRAP_HYPOTHESIS_UNRESOLVED`.

Do not infer PTU Injury, status or HP change from an apparent ecological cost. Mechanical aftermath still requires the AutoPTU semantic-result ingress and exact admitted capability path from Passes 262–264.

## Canon boundary

CANON-ALIGNED: population/source authority remains separate from visibility and site-use observations; Minecraft/Cobblemon is presentation rather than ecology/PTU authority; uncertain evidence remains uncertain.

PROPOSED: `ECOLOGICAL_CUE_QUALITY_DIVERGENCE_V1`, explicit cue/quality separation, comparative trap-evidence gate, and an investigation loop based on repeated observations.

UNCERTAIN: which real cues, resources and outcome measures exist in Marea/Sendero; which species respond; whether any actual site is beneficial, neutral, harmful or a trap.

FIXTURE-ONLY: every cue, altered site, cost signal and comparison introduced by Pass 266 tests.

## Sources

- Schlaepfer MA, Runge MC, Sherman PW. 2002. Ecological and evolutionary traps. Trends in Ecology & Evolution. USGS Publications Warehouse: https://www.usgs.gov/publications/ecological-and-evolutionary-traps
- Hale R, Swearer SE. 2015. Identifying, preventing and mitigating ecological traps to improve management of urban aquatic ecosystems. Journal of Applied Ecology. https://doi.org/10.1111/1365-2664.12458
- Courtois et al. 2021. Nonideal nest box selection by tree swallows breeding in farmlands: Evidence for an ecological trap? Ecology and Evolution. https://doi.org/10.1002/ece3.8323
- Oro D et al. 2013. Ecological and evolutionary implications of food subsidies from humans. Ecology Letters. https://doi.org/10.1111/ele.12187
- Newsome TM et al. 2015. The ecological effects of providing resource subsidies to predators. Global Ecology and Biogeography. https://doi.org/10.1111/geb.12236
