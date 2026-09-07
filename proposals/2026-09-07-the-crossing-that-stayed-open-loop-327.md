# The Crossing That Stayed Open — Pass 327

Status: PROPOSED / NON-CANON
Date: 2026-09-07
Canon effect: NONE unless separately reviewed and promoted.

## Premise

A transport corridor remains operational through a seasonal migration window. Years earlier, a dedicated underpass and approach fencing were built so a recurring wild Pokémon population could cross without using the road surface.

This season, the underpass is physically open and the maintenance crew reports no structural failure. Yet field observers record fewer successful crossings, more hesitation near the approaches and several sightings on the wrong side of the barrier.

The immediate public argument becomes simple: either the crossing works or it does not.

The actual investigation is narrower and more useful: which parts of the migration system still function, which evidence applies to which population and time window, and what changed around a structure that never technically closed?

## Persistent features

The site should contain stable world features that survive revisits:

- an active human transport route;
- a dedicated crossing structure;
- two approach zones on opposite sides of the barrier;
- an upstream or upland seasonal habitat;
- a downstream or lowland seasonal habitat;
- one temporary stopover patch;
- maintenance access;
- observation points with imperfect sightlines;
- fencing, landscaping or other guidance infrastructure that may have its own state history.

Exact region, settlement, road type, crossing design and resident Pokémon remain unresolved.

## Initial evidence

Several claims can all be true at once:

- maintenance confirms the passage itself is unobstructed;
- a researcher has fewer verified crossings than the previous season;
- a driver reports several Pokémon near the road surface;
- a resident says the herd arrived later than usual;
- an older monitoring record shows the same crossing once carried more traffic;
- a road crew completed work near one approach shortly before the migration window;
- a stopover site has changed since the last survey.

None of these observations alone establishes cause.

## Investigation loop

The player can inspect the structure, compare both approaches, identify whether stopover evidence persists, review maintenance records, speak with observers who worked different shifts, compare recent and historical crossing reports, and return during a later movement window.

The useful deductions are feature-scoped:

- passage physically available during a stated window;
- approach use reduced on one side;
- animals observed diverting before reaching the structure;
- stopover occupancy lower than historical baseline;
- fencing or maintenance changed after an earlier report;
- report stale after a later world event;
- migration timing shifted relative to staff coverage.

The investigation should never require the player to infer hidden ecological truth from one spawn group.

## Candidate explanations

The final cause remains open until canon review. Plausible combinations include:

- the structure is intact but one approach became less attractive or harder to reach;
- routine vegetation or drainage work changed the guidance path;
- a stopover resource declined and the population now reaches the crossing at a different time;
- human activity near one entrance increased during the movement window;
- a weather or disturbance event altered the preferred corridor before the crossing;
- public monitoring covers the wrong hours this season;
- the apparent decline is a timing artifact while later movement remains possible;
- different subgroups are using different segments;
- several small changes accumulated without any single failure.

Sabotage is not required.

## NPC and faction pressure

The route operator wants to keep transport reliable and can honestly point to a structurally sound crossing.

A field researcher wants more observation before declaring success or failure.

A maintenance supervisor knows what work was performed but may not know its ecological effect.

Local drivers care about collision risk and schedule disruption.

Residents may hold long-term observations that are useful but unevenly recorded.

A habitat steward may care more about the stopover and approaches than the concrete structure itself.

The global NPC system should preserve exactly which report each actor received. Shared employment or faction membership does not create automatic knowledge.

## Consequence space

The outcome should support selective intervention rather than a global binary.

Possible responses include changing work hours, reopening a stopover patch, adjusting one approach, adding temporary observation coverage, restricting a short road segment during a narrow window, changing signage, scheduling a follow-up survey or leaving the structure untouched while gathering better evidence.

A later revisit can reveal:

- crossing counts recovering;
- movement shifting to a neighboring segment;
- human delays reduced or increased;
- a temporary measure becoming unnecessary;
- new evidence contradicting the first explanation;
- public confidence changing because an earlier notice was corrected;
- a different species using the same infrastructure in another season.

The world should retain the decision lineage instead of resetting the site.

## Reduced implementation

This version can run without dynamic migration simulation.

Population movement is authored through semantic world events and observations. Suggested world-state values include:

- `MIGRATION_WINDOW_EXPECTED`
- `MIGRATION_WINDOW_ACTIVE`
- `CROSSING_PHYSICALLY_OPEN`
- `APPROACH_USE_REDUCED_OBSERVED`
- `SUCCESSFUL_CROSSING_OBSERVED`
- `FAILED_APPROACH_OBSERVED`
- `STOPOVER_USE_OBSERVED`
- `SOURCE_UNRESOLVED`
- `OBSERVATION_STALE_AFTER_EVENT`
- `FOLLOWUP_REQUIRED`

These are narrative/world states, not PTU statuses.

A battle, if one occurs, uses static ordinary geometry and only currently verified tactical capabilities. The crossing investigation does not depend on combat.

## Rich implementation

A richer version may eventually support moving traffic, timed passage windows, escort/rescue objectives, dynamic barriers, weather-driven route changes, forced movement near hazards, reactions, species-specific movement behavior and autonomous tactical choices around civilians or fleeing wild Pokémon.

Those features are optional and must remain gated by exact engine capability families.

## Canon questions left open

Region; transport mode; institution; crossing type; migration species; population identity; seasonal habitats; stopover site; historical construction reason; current maintenance authority; monitoring baseline; actual cause; legal authority for temporary restrictions; economic consequences; whether any battle occurs; and final resolution remain unresolved.