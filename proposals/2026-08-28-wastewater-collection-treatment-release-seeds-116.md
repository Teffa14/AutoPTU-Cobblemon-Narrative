# Ouros Wastewater Collection, Treatment & Release Seeds — Pass 116

Status: PROPOSED / NON-CANON. Nothing here is canon-approved.
Date: 2026-08-28
Research provenance: `research/2026-08-28-wastewater-collection-treatment-release-continuity-scan-116.md`
Design dependency: `design/wastewater-collection-treatment-release-continuity-extension.md`

## Design intent

These candidates turn wastewater continuity into ordinary world history, investigations, recovery work, recurring places and capability-aware encounters. They avoid automatic contamination, disease, Poison status, species-based blame and invented engineering.

## Situation seed — The Pump Is Running, the Sector Is Not

A recently repaired station visibly runs again. Residents in one downstream block still report service problems.

The contradiction is only apparent. Power restoration, pump operation, path verification, sector verification and endpoint recovery have separate records.

Useful actors: maintenance crew, wastewater operator, resident representative, shop owner, infrastructure archivist and a Pokémon repeatedly observed near a dry access gallery.

Possible outcomes include a second isolated fault, stale public information, an unverified downstream path or a building-local issue. The generator must choose only from established evidence.

## Situation seed — The Treatment Hall Finished First

Operators complete an authored treatment operation, but release remains pending because output verification or receiving-handoff state is unresolved.

The site can look calm while downstream restrictions remain active. This creates a useful story about different institutions finishing their own work at different times.

No amount of visual machinery activity authorizes a release.

## Situation seed — The Old Manhole Name Never Died

A redeveloped market uses a current street grid, while veteran workers still refer to an old sewer access by a demolished building name. New maps use a numbered access ID. Residents use a third nickname.

All three labels can point to one persistent access-point identity.

A later investigation becomes easier if Ouros preserves aliases and effective dates instead of treating disagreement as deception.

## Situation seed — The Temporary Bypass Became the Emergency Route

A temporary arrangement created during an older service incident was never physically removed because later reviews found it useful as a contingency asset.

Years later, workers know the route while most residents think it is abandoned infrastructure.

This can seed maintenance stories, training exercises, archive questions and a future outage without making the temporary path continuously active.

## Situation seed — The Pokémon Uses the Dry Gallery

A known Pokémon individual repeatedly shelters in a dry service gallery during quiet periods and leaves when crews arrive.

The observation can support an ecological relationship, a worker tradition or a later clue about access timing.

It does not prove the Pokémon caused a blockage, senses wastewater failures, resists contamination or has a sanitation role.

## Situation seed — The Overflow Report Was Correct, the Map Was Wrong

A witness reports an overflow beside a building that current network maps do not show as connected to the affected sector.

Later review reveals a retired alignment still physically exists, a map revision has an error, or the observation referred to another nearby asset. The resolution must follow actual evidence.

The story works without sabotage or hidden villains.

## Situation seed — The Outfall Is Available, the Shore Is Restricted

The wastewater system completes its own verified receiving handoff. A coastal or conservation owner still keeps a nearby access area restricted for an unrelated or downstream reason.

This seed reinforces owner-system separation. Wastewater recovery does not automatically reopen beaches, fishing areas, roads or public spaces.

## Situation seed — The Market Reopened Before the Basement

A commercial district returns to normal public operation while one building keeps a lower service area isolated after a wastewater incident.

The business can operate under a temporary arrangement while Facility Maintenance and Wastewater Continuity finish separate verification work.

A later callback can show that the temporary loading practice became permanent because staff preferred it.

## Situation seed — Two Operators, One Historical Network

A regional boundary or institutional reorganization splits responsibility for a network that was once operated as one system.

Old plans, staff vocabulary and maintenance records still describe the former topology. New operational records divide it differently.

This enables administrative mysteries and cross-boundary recovery without requiring corruption.

## Situation seed — Nothing Was Recorded Between 02:10 and 03:05

One monitoring point has a documented gap during an incident window. Other observations before and after the gap are valid.

Ouros preserves `UNKNOWN_FOR_INTERVAL` rather than deciding that the system was normal or failed during the missing period.

A future investigation can add evidence without rewriting the original record.

## Mystery — Five Times the Sewer “Came Back”

Five records contain different restoration times:

- power returned to the station;
- station operation resumed;
- one collection path passed verification;
- treatment output passed its authored check;
- the affected sector was declared restored.

The mystery is solved by matching each timestamp to its subject and scope. Nobody needs to be lying.

## Mystery — Four Access Maps, Two Actual Shafts

A current utility plan, a maintenance sketch, an archived redevelopment map and a resident hand-drawn map appear to show four different entrances.

Persistent IDs and renovation history reveal that two entrances changed names and surface geometry across several decades.

The investigation teaches the player how Ouros records physical continuity beneath changing settlements.

## Exploration — The Old Alignment Under the Market

A closed section beneath a redeveloped market preserves wall markings, old access labels, patched junctions and records from several network eras.

Current version:

The route is inspected, dry and static before exploration. Players compare plans, photographs, work records and testimony. Pokémon observations can identify repeated use of a section but never establish technical function.

Future mechanically rich version:

Designers could add changing access, active liquids, machinery, pressure, gas, slippery surfaces or emergency withdrawal only after exact PTU/Caelo rules and engine contracts exist.

Narrative premise remains the same in both versions.

## Long arc — A District Learns What Runs Under It

Phase one establishes ordinary life. Wastewater infrastructure is mostly invisible. Workers, businesses, housing blocks and service access points have recurring routines.

A localized incident then exposes part of the network to public attention. Different actors learn different pieces of the system. Temporary routing changes deliveries and pedestrian habits. A service yard becomes a neighborhood reference point.

Recovery happens through separate checkpoints. Some buildings resume first. A treatment facility finishes its work before another owner system lifts a downstream restriction. Public notices lag behind one operational transition and lead to apparently conflicting memories.

Months later the temporary arrangement is reviewed. Part is removed; another piece remains as an emergency asset. An old alignment becomes habitat or an industrial-history location. Workers retain names that no longer appear on maps.

A later incident reuses those facts. The arc does not reset the district or rely on a single `wastewater_recovery_level`.

## NPC archetype — The Route Keeper

A long-serving operator remembers retired access names and which records correspond to which renovation era.

Useful narrative function: translate institutional memory into evidence without making the NPC omniscient. Their memory can be precise about work routines and uncertain about causes outside their role.

## NPC archetype — The Verification Specialist

This actor repeatedly arrives after visible repair work and refuses to equate “machine runs” with “service restored.”

Useful narrative function: teach the player that operational verification is a distinct step. The character should not become a universal safety authority outside their authored scope.

## NPC archetype — The Downstream Steward

A conservation, fisheries, coastal or water-system actor receives release or incident handoffs but controls a different domain.

Useful narrative function: show why one system can finish while another remains restricted. Their decisions require their own evidence.

## Faction dynamic — Operations vs Redevelopment Archive

Current operators optimize around the live network. A civic redevelopment office maintains historical plans. A heritage group preserves retired industrial sites. None owns the whole truth.

Quests can emerge when a current fault intersects an old alignment or when a new construction project exposes a retired asset.

## Encounter — Lift Station Access Withdrawal

Narrative premise:

A territorial or hostile situation develops near an already isolated station access. Staff need to leave the immediate corridor before inspection can resume.

Full intended version:

The encounter can include moving withdrawal actors, Intercept, forced movement, reactions around protection, changing restricted technical cells, objective-aware AI and semantic playback.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL if exact environmental damage is introduced
- status lifecycle — PARTIAL if exact conditions are introduced
- terrain/weather/hazards/zones/reactions — BLOCKING for technical/wet/confined zones or generalized reactions
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced version:

Complete worker withdrawal and station isolation before BattleSpec. Exclude wastewater, pump machinery, pits and controls. Use a static dry service approach with explicit combatants. Winning records only immediate perimeter security.

## Encounter — Treatment Gallery Perimeter

Narrative premise:

A treatment site's process is already isolated. One dry service gallery must be secured so operators can later inspect equipment.

Full intended version:

If future design puts active machinery, liquids, changing barriers, environmental exposure or technical zones inside combat, it directly depends on terrain/weather/hazards/zones/reactions plus whichever lifecycle, damage, status and movement categories each effect uses.

Reduced version:

Freeze process state before battle. Remove workers and controlled material. Technical equipment is inert scenery or outside the grid. Resolve a conventional encounter in a reviewed static corridor. Victory never advances treatment or verification state.

## Encounter — Outfall Inspection Diversion

Narrative premise:

An inspection team encounters a territorial conflict near an already restricted receiving-handoff approach.

Full intended version:

Protection/escort behavior, Intercept, forced movement, active water-edge/current zones, generalized reactions and semantic playback may be desirable.

Reduced version:

Withdraw the inspection team first. Keep discharge and receiving water outside BattleSpec. Use stable dry ground. Winning allows the owner system to consider a later inspection; it does not verify a release, determine pollution or reopen downstream access.

## Implementation rule shared by all three encounters

The reduced variants are first-class designs, not placeholders. They preserve the same narrative premise while leaving wastewater hydraulics, environmental exposure and technical operation in world state.

Minecraft/Cobblemon/Craftics must never fill the missing PTU rule gap with native water physics, poison, suffocation, redstone machinery, collision damage or ad hoc status application.

## Canon review questions

Before promotion, determine which Ouros settlements have authored wastewater systems, whether any combine stormwater and sanitary flows, technology level, operators, treatment/release topology, public access practices, historical/decommissioned sites, temporary arrangements, receiving-system relationships and documented Pokémon roles.

Do not canonize universal contamination mechanics, treatment methods, environmental immunities or species jobs through this proposal.