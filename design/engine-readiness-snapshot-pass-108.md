# Engine Readiness Snapshot — Pass 108

Status: IMPLEMENTATION-READINESS EVIDENCE. Creates no PTU rules or Ouros canon.
Date: 2026-08-28

## Scope

Pass 108 adds proposed continuity for stormwater collection, drainage, local flood-control assets and staged post-flood restoration.

Narrative baseline before Pass 108 writes: `7a58c7123a0ad4d7427e77788bbf9ab4f7f3a0c6`.

The complete recursive Narrative repository inventory was inspected at baseline and returned `truncated=false`. Water Management, Drinking-Water Continuity, Waste/Sanitation, Roads/Bridges, the internal PTU/Caelo source scan and Pass 107 readiness were inspected directly. Repository search found no dedicated stormwater/drainage/culvert layer.

Pass 108 files:

- `research/2026-08-28-stormwater-drainage-flood-control-continuity-scan-108.md`
- `design/stormwater-drainage-flood-control-continuity-extension.md`
- `proposals/2026-08-28-stormwater-drainage-flood-control-seeds-108.md`
- this readiness snapshot

## Live engine evidence

### AutoPTU-Java

Head inspected during this pass: `9f63f0a81af45af2fbc87928b96c1cec4fcff4b0`, PR #262, `Rebind move preparation after pre-resolution target replacement`.

New evidence since Pass 107:

- pre-resolution target replacement now composes with authoritative move preparation;
- after a redirect, target-bound inputs are rebuilt from the effective target before accuracy RNG is consumed;
- the new runtime composition explicitly addresses defender-bound evasion, defense, type interaction and other target-scoped preparation;
- tests cover re-preparation against the redirected target;
- this continues the #256-#262 Intercept/target-replacement chain.

Recent reviewed chain:

- #256 authoritative Intercept d20 RNG;
- #257 Python-oracle mutation ordering;
- #258 candidate-attempt sequence composition;
- #259 spatial-success branch composition;
- #260 ordered pre-resolution target-hook registry;
- #261 runtime target-replacement application;
- #262 target-bound move re-preparation after replacement.

This is important server-owned orchestration evidence. It does not prove complete family coverage for:

- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- generalized competing reactions;
- every reaction trigger window and ordering rule;
- all Move/Ability/Item/Trainer Feature target-redirection registrations;
- all Move-specific behavior;
- environmental displacement;
- current, flood or debris movement;
- objective-aware tactical policy;
- Minecraft/Cobblemon semantic playback.

The current AutoPTU-Java README still lists as incomplete: core combatant/grid battle state, full damage resolution, status controller, terrain, hazards, forced movement, reactions, move/ability/item/perk/Trainer Feature registries, semantic battle-event/full transcript parity, AI scoring/policy and the Craftics/Cobblemon adapter.

No permanent capability category is promoted by #262.

### AutoPTU Python

Head inspected during this pass: `27064aa1a44128211fe65d1039c2d7dd6f09b6b0`, PR #216, `Career: tolerate legacy battle transcripts with null spec`.

The change makes Career battle presentation fail closed instead of crashing when a legacy transcript has a null presentation spec, with regression coverage.

This improves resilience/backward compatibility. It adds no tactical battle-family coverage relevant to stormwater or flood encounters.

## PTU / Caelo boundary for stormwater and flood-control systems

The project source scan identifies PTU Core, Caelo Player's Guide, Caelo Region Location & Encounter List, character creation, errata/extras and Pokédex material as governing internal references.

Caelo can establish exact environmental mechanics for a particular authored location. That does not authorize generic flood mechanics elsewhere.

No inspected evidence establishes universal PTU/Caelo rules for:

- rainfall-to-flood-depth conversion;
- storm-drain or culvert capacity;
- pump output;
- flood-current forced movement;
- drowning/suffocation from ordinary flooded geometry;
- slippery pavement;
- debris impact;
- structural washout/collapse;
- contaminated floodwater applying Poison or another status;
- Water-type immunity to flood/current hazards;
- Electric-type generic danger or immunity around wet equipment;
- species-level flood prediction;
- species-level drain clearing;
- Move-powered pumping/drainage/diversion;
- universal flood-control Skill checks or Trainer Feature bonuses.

Any tactical effect needs an exact governing Move, Ability, Item, Trainer Feature, Capability, terrain/weather rule or authored Caelo condition plus current AutoPTU implementation evidence.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Verified for reviewed static arenas. A drainage network or flood extent is not battle range/LoS by default.

`base movement legality`

Verified for ordinary reviewed movement. It does not create current, mud, slipping, wading, flood depth, culvert crawlspace or evacuation semantics.

`core calculations`

Verified primitives remain available. No hydrology, pump, flood-depth or debris arithmetic is inferred.

`action economy/initiative`

Verified typed action budget and ordering remain available.

`AI legal-action infrastructure`

Verified legal-action enumeration remains available. It does not choose safe withdrawal corridors, protect responders or understand flood-control objectives.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

PARTIAL. #256-#262 substantially deepen one reviewed Intercept/target-replacement route. Broad Push/Pull, broad Knockback, generalized reactions, all forced-movement sources and environmental displacement remain incomplete.

`full turn/round lifecycle`

PARTIAL. Drainage/pumping/flood stages are world state and do not become battle-round mechanics automatically.

`full stateful damage pipeline`

PARTIAL. No generic floodwater, debris, collision, electrical, drowning or structural damage is established.

`status lifecycle`

PARTIAL. Flood/closure/drainage states are world state, not PTU statuses. No environmental status is inferred from wetness or water appearance.

`move-specific behavior`

PARTIAL. #262 strengthens target-bound move re-preparation after a redirect, but this is not evidence that all Moves or environmental interactions exist.

`abilities`

PARTIAL. Hook infrastructure can host sources, but broad Ability coverage and stormwater utility interactions are not established.

`items`

PARTIAL. Pumps, barriers, ropes, drains and maintenance equipment do not become legal PTU Items or tactical objects by presentation alone.

`Trainer Features/perks`

PARTIAL. No universal flood-control, drainage, engineering, rescue or inspection Feature family is established.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

BLOCKING for active floodwater, currents, changing water levels, mud/slip zones, debris fields, energized wet equipment, collapse zones, weather phases and generalized reaction windows.

`AI tactical policy`

BLOCKING for WITHDRAW, PROTECT, SECURE_ROUTE, HOLD_PERIMETER, ESCORT, TERRITORIAL_WITHDRAWAL and other objective-aware policies.

`Minecraft/Cobblemon/Craftics adapter/playback support`

BLOCKING for stable stormwater-system/sector/asset bindings, authoritative flooding/closure projection, reviewed world-to-arena conversion and semantic battle playback.

## Encounter readiness

### Flooded Underpass Withdrawal

Full intended form wants multiple safe routes, withdrawal/protection behavior, Intercept/forced movement, generalized reactions, reviewed flood/wet zones only when mechanically supported, objective-aware AI and semantic playback.

Current profile: REDUCED.

Safe implementation:

Ouros closes the underpass before battle. Floodwater, ordinary traffic, responders, pumping equipment and civilians remain outside BattleSpec. AutoPTU receives explicit participants on a reviewed dry static approach. Victory changes only immediate perimeter/security state. Drainage and Road Operations retain all restoration/reopening authority.

### Culvert Access Perimeter

Full intended form wants route control, territorial/withdrawal policy, complete reactions/forced movement and possibly edge/water/debris zones if exact mechanics exist.

Current profile: REDUCED.

Safe implementation:

Inspectors remain outside the scene. Culvert interior, flowing water and debris are noninteractive. Battle occurs on stable adjacent ground. Winning can permit a later inspection attempt; it cannot clear, repair or verify the culvert.

### Temporary Pump Site Perimeter

Full intended form wants protected technical space, withdrawal behavior, generalized reactions and possibly active hoses/cables/water/equipment zones.

Current profile: REDUCED.

Safe implementation:

Freeze the temporary mitigation state before battle. Workers, pumps, hoses, vehicles and water stay outside the grid. Use an adjacent static arena. Battle outcome cannot start, stop, repair, operate or verify the drainage process.

## Immediate noncombat readiness

Usable now as proposed narrative state without adding tactical mechanics:

- stable drainage-system identity;
- catchment sectors;
- inlet/catch-point observations;
- authored conveyance links;
- culvert identity and post-event inspection state;
- broad stormwater-storage state;
- drainage-pump operational records;
- outfall/receiving handoffs;
- authored drainage paths;
- scoped flood/ponding observations;
- obstruction observations separated from causal claims;
- temporary pumping/bypass/mitigation records;
- staged restoration checkpoints;
- contradictory recovery times resolved through scope/timestamps/provenance;
- legacy/decommissioned drainage assets;
- explicit ecology links without species blame;
- handoffs to Roads, Residential, Commercial, Care, Conservation and other downstream owners.

## Minecraft/Cobblemon consequence

Binding remains:

`Ouros stormwater/world state -> explicit encounter composition -> AutoPTU authoritative BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`.

Safe presentation reuse can include roads, gutters, drains, manholes, culverts, channels, basins, pump buildings, barriers, signs, temporary equipment, authored water visuals, weather presentation, workers, individually authored Pokémon, models/forms/poses/animations/cries, sounds, particles, UI, networking, tracking and persistence hooks.

Adapter work is required for stable system/sector/asset IDs, authoritative state projection, reviewed arena conversion and semantic playback.

Minecraft/Cobblemon must never decide that:

- touching pipes/channels create drainage topology;
- native water spread is the authoritative flood simulation;
- an empty-looking street proves drainage verification;
- disappearing water blocks reopen a road;
- redstone or a pump animation proves successful drainage;
- visible debris proves a blockage's cause;
- a Pokémon near a drain caused or predicted flooding;
- Water typing grants flood immunity or drain-clearing ability;
- water blocks apply current/forced movement/drowning;
- native fire/electric/collision/water applies PTU damage/status without an exact contract;
- nearby entities become operators or combatants;
- Cobblemon BattleState/controller logic owns combatants, legality, HP/status, positions or outcome.

## Readiness conclusion

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: complete movement including push/pull/knockback/interception/forced movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback support.

## Unresolved canon questions

- Which settlements use dedicated storm drains, open channels, combined systems, natural drainage or hybrid arrangements?
- Which catchment sectors and flood-prone places actually exist?
- Which institutions operate and maintain drainage systems?
- Which culverts, basins, pumps, barriers and temporary mitigation technologies exist by region?
- How are underground access, inspection and public notices handled?
- Which drainage assets overlap important habitat or public spaces?
- Which legacy systems remain visible or reusable?
- Which individual Pokémon perform explicitly authored drainage-related work roles?

## Unresolved mechanical questions

- exact PTU/Caelo treatment of flood current or environmental forced movement;
- drowning/suffocation;
- wet/slip/mud terrain;
- contaminated floodwater damage/status;
- debris impact and structural collapse;
- water-depth changes during combat;
- pumps, gates, culverts or barriers as tactical objects;
- concrete Move/Ability/Item/Trainer Feature interactions with drainage or rescue work;
- rescue/carry interactions;
- complete competing-reaction semantics after #262;
- objective-aware withdrawal/protection/territorial policy;
- semantic adapter playback of flooding without giving Minecraft battle or infrastructure authority.

No answer is invented by this snapshot.