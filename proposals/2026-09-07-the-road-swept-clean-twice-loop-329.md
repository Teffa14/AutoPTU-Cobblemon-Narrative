# The Road Swept Clean Twice — Pass 329

Status: PROPOSED / NON-CANON
Date: 2026-09-07

## Premise

A regional road was covered during an older ashfall. Public works cleared the corridor, documented the work, and reopened it. Later, fresh gray deposits appear on one section of the route and a downstream culvert begins to obstruct again. The observatory has no evidence of a corresponding new primary ashfall during the relevant window.

The immediate question is operational rather than apocalyptic: where did the material come from, which features are affected now, and what evidence is sufficient for the next access decision?

The premise supports a persistent-world investigation because multiple actors can report accurate observations without sharing the same causal interpretation.

## Persistent features

Use stable feature IDs so evidence and consequences survive revisits:

- `ASH_CATCHMENT_UPPER_SLOPE` — an exposed or partially vegetated area where older deposits remain available for remobilization.
- `ROAD_SEGMENT_CUT` — a route section previously cleaned and reopened.
- `CULVERT_INLET` — a drainage feature that can accumulate transported material.
- `SERVICE_SHELTER` — a roofed observation or maintenance point that preserves a different exposure history.
- `ASH_DISPOSAL_FEATURE` — a cleanup storage/disposal location with documented material lineage.
- `WATER_OR_UTILITY_INTAKE` — optional dependent infrastructure that can create consequences beyond travel.
- `OBSERVATION_POINT` — a location used by an observatory or field team for direct observations.

Names, region, settlement, volcano, road class, infrastructure, and ownership remain unresolved until canon approval.

## Actors and bounded knowledge

An observatory or geological monitoring office knows the records and observations it actually produced or received. It can report whether its evidence supports a new primary fallout event. It does not automatically know road-cleanup disposition, culvert condition, or every field observation.

A public-works crew knows what segment it cleared, where it moved material, what equipment was used, and what its work order required. Its successful completion of that task does not grant knowledge of later remobilization outside its observation window.

A road authority knows closures, reopening decisions, inspections, and reports delivered into its process. A valid reopening decision can later require revision after new evidence.

A water or drainage operator knows intake flow, blockage, maintenance, and received upstream reports. It does not know volcanic cause by default.

Residents and road users can provide dated observations such as clear skies, dust plumes, traffic conditions, fresh deposits, or runoff. Their evidence remains local to place and time.

A freight or passenger operator has legitimate pressure for predictable access and can provide route-use evidence. It does not become an antagonist merely because closure is costly.

## Investigation loop

The first visit establishes the contradiction: the road carries a fresh-looking deposit after cleanup, while monitoring records do not establish a new primary ashfall in the same window.

The player can inspect feature-scoped evidence rather than search for a single dramatic clue. Useful evidence includes deposit position, dry or wet transport traces, cleanup boundaries, material stored at the disposal feature, culvert accumulation, traffic timing, rainfall history, wind exposure, public-works records, observatory reports, and witness observations.

The second stage compares provenance. A deposit on the road may share history with the original ashfall while having a much younger transfer event. A blocked culvert may integrate material from several upstream features. A clean service shelter can support a limited timing inference without proving conditions across the catchment.

The decision stage asks what can safely be concluded now. Possible decisions include reopening one segment, restricting another, moving or securing stored material, clearing drainage, monitoring a catchment, altering traffic during a vulnerable window, or withholding a larger intervention until evidence improves.

A later revisit should expose consequences. The chosen cleanup can reduce one problem while shifting work elsewhere. Monitoring can confirm or weaken the original hypothesis. A new weather event can test whether the material source was correctly identified. NPC trust and institutional procedures can change based on whether earlier claims were carefully scoped.

## Open causal hypotheses

Keep these proposed rather than preselecting canon truth:

- wind moved older unconsolidated ash from an exposed source feature;
- traffic resuspended residual material left within or beside the route corridor;
- rainfall/runoff transported stored material into the road or drainage network;
- a previous cleanup stockpile or disposal area was poorly protected from later redistribution;
- a maintenance action correctly cleared one feature while transferring material into another future source location;
- several small transfer mechanisms occurred in sequence;
- verified Pokémon activity changed local material movement without becoming the default explanation;
- a new primary ashfall occurred despite incomplete observations, if later canon evidence supports it.

The mystery does not require sabotage, deception, or a villain.

## Consequence model

Consequences are feature-scoped and preserve lineage. Examples:

- `ROAD_SEGMENT_CUT` moves from `RESTRICTED` to `OPEN` after clearance and inspection.
- `CULVERT_INLET` remains `MONITORING` because upstream material is unresolved.
- `ASH_DISPOSAL_FEATURE` gains a corrective work order and later inspection event.
- `WATER_OR_UTILITY_INTAKE` gains a maintenance obligation without implying the road is closed.
- a public notice is corrected to distinguish current access from wider catchment condition.
- an NPC receives a new report and updates belief; faction membership does not propagate that belief automatically.

Later evidence can revise a decision without rewriting the original observation or pretending the earlier decision never occurred.

## Reduced implementation — current-capability version

The narrative premise can run without dynamic ash simulation.

World state authors transfer events between scenes. Example semantic events can state that material moved from an upstream storage feature to a road segment after a wind or rainfall window. Those events preserve source feature, receiving feature, event time, observation time, and evidence confidence.

Route state can use authored values such as `OPEN`, `RESTRICTED`, `MAINTENANCE_ONLY`, `CLOSED`, and `MONITORING`. Evidence labels such as `FRESH_DEPOSIT_OBSERVED`, `CULVERT_BLOCKAGE_OBSERVED`, `OLD_ASH_SOURCE_OBSERVED`, `NO_PRIMARY_FALLOUT_EVIDENCE_RECEIVED`, and `DISPOSAL_RECORD_RECEIVED` are world-state facts, not PTU statuses.

If combat occurs, use static geometry, ordinary verified targeting/range/LoS, base movement, calculations, initiative/action economy, and legal-action infrastructure. Unsupported ash fields, collapse zones, or flows remain outside legal tactical space or are resolved as between-scene world events.

No reduced-version rule creates ash-cloud visibility penalties, wind displacement, difficult terrain, slipping, environmental damage, respiratory conditions, lahar movement, rescue interrupts, or Pokémon-specific ash interaction.

## Intended full version and exact engine dependencies

A mechanically richer version may eventually include dynamic particulate clouds, gust-driven visibility changes, changing deposit zones, debris or wet-ash movement, unstable slopes or roofs, timed cleanup machinery, civilians, rescue, and objectives other than defeating all combatants.

Dependency classification:

- targeting/footprints/range/LoS — ordinary capability is verified within audited contracts; dynamic ash or particulate obscurement requires explicit additional support and cannot inherit ordinary LoS verification.
- base movement legality — verified for ordinary audited movement; ash-specific footing or terrain modifiers require separate evidence.
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL; required for gust displacement, debris movement, slides, rescue, interception, or moving-flow effects.
- core calculations — verified for ordinary audited combat calculations.
- action economy/initiative — verified for ordinary audited combat flow.
- full turn/round lifecycle — PARTIAL; required for timed gusts, changing ash zones, delayed failures, machinery phases, or weather-driven transitions during combat.
- full stateful damage pipeline — PARTIAL; required if falling debris, collapse, abrasion, heat, impact, or environmental exposure causes battle damage.
- status lifecycle — PARTIAL; required for any persistent exposure or condition represented as a real tactical status.
- terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by subfamily; required for ash fields, wind, wet-debris zones, unstable ground, shelter zones, or reaction windows.
- move-specific behavior — PARTIAL and individually gated.
- abilities — PARTIAL and individually gated.
- items — PARTIAL and individually gated.
- Trainer Features/perks — PARTIAL and individually gated.
- AI legal-action infrastructure — verified for ordinary audited legal actions.
- AI tactical policy — BLOCKING for general autonomous evacuation, escort, shelter-seeking, rescue, dynamic-hazard reasoning, and non-defeat work objectives.
- Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING end-to-end for authoritative dynamic environmental playback.

A representative implemented mechanic never promotes the whole family.

## Minecraft / Cobblemon presentation boundary

Minecraft may render gray deposits, dust particles, blocked culverts, cleanup stockpiles, road barriers, crews, observation equipment, and changed scenery after a world event. Those visuals are projections of authoritative narrative/tactical state.

Particle density cannot decide PTU LoS. A flowing block cannot create a forced-movement rule. A gray surface cannot decide difficult terrain, damage, exposure, or whether a deposit came from a new eruption. NPCs learn through explicit observations, communications, archives, and receipts rather than by reading the rendered world globally.

## Canon questions intentionally unresolved

Region, volcano, eruption history, ash composition, road identity, settlement, disposal practice, observatory structure, public-works authority, water infrastructure, economy, affected Pokémon populations, cultural memory, true material path, final access decision, and whether any combat is necessary remain open.
