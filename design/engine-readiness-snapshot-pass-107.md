# Engine Readiness Snapshot — Pass 107

Status: IMPLEMENTATION-READINESS EVIDENCE. Creates no PTU rules or Ouros canon.
Date: 2026-08-28

## Scope

Pass 107 adds proposed continuity for drinking-water treatment and distribution between the existing raw-water/source authority and downstream service points.

Narrative baseline before Pass 107 writes: `bb24cb2820dfbc80814150a987ceac268ff86dca`.

The complete recursive Narrative repository inventory was inspected at baseline and returned `truncated=false`. The water-management, waste/sanitation, infrastructure-outage and Pass 106 readiness documents were inspected directly. This confirmed that wastewater, contamination, dams/reservoirs/canals and generic outage restoration already had owners; the new work is limited to treatment/distribution service continuity.

Pass 107 files:

- `research/2026-08-28-drinking-water-treatment-distribution-scan-107.md`
- `design/drinking-water-treatment-distribution-continuity-extension.md`
- `proposals/2026-08-28-drinking-water-treatment-distribution-seeds-107.md`
- this readiness snapshot

## Live engine evidence

### AutoPTU-Java

Head inspected during this pass: `b828913726b68ebb039cfdfead129530f2da34a6`, PR #261, `Apply pre-resolution target replacement in runtime`.

New evidence since Pass 106:

- the server-owned pre-resolution target hook infrastructure from #260 is now applied in the runtime path;
- replacement is performed before later target resolution stages;
- runtime tests and gating cover that application;
- the work continues the specific Intercept/target-replacement parity chain rather than implementing a generic environmental or utility mechanic.

Recent chain:

- #256 authoritative Intercept d20 RNG;
- #257 Python-oracle mutation ordering;
- #258 candidate-attempt sequence composition;
- #259 spatial-success branch composition;
- #260 ordered pre-resolution target-hook registry;
- #261 runtime application of target replacement.

This is strong evidence for server-owned orchestration around target replacement and the reviewed Intercept path. It does not prove family-wide coverage for:

- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- generalized competing reactions;
- every reaction trigger window/order;
- all Ability/Move/Item/Trainer Feature target-redirection registrations;
- environmental displacement;
- objective-aware tactical policy;
- Minecraft/Cobblemon semantic playback.

No permanent category is promoted.

### AutoPTU Python

Head inspected during this pass: `4a7d8019a11442be12aa16ba47ebe260ea4d9535`, PR #215, `Career: normalize malformed battle events at API boundary`.

The change normalizes malformed legacy battle-event collections at the Career API/cache boundary and aligns tests with the normalized transcript. It improves stability and backward compatibility. It adds no tactical battle-family coverage relevant to Pass 107.

## PTU / Caelo boundary for drinking-water systems

The project source scan identifies PTU Core, Caelo Player's Guide, Caelo Region Location & Encounter List, character creation, errata/extras and Pokédex material as governing internal references.

Caelo can author explicit environmental mechanical effects when a source defines them. That does not create a generic drinking-water system.

No inspected evidence establishes universal PTU/Caelo mechanics for:

- potability or water-quality clearance;
- treatment chemistry or filtration efficiency;
- distribution pressure/flow;
- pipe/tank HP;
- burst-pipe forced movement;
- slip/current zones;
- waterborne illness;
- drinking water as healing;
- dirty water applying Poison;
- Water-type purification;
- Poison-type contamination immunity;
- Move-powered treatment/pumping;
- generic utility-operation Skills/Features;
- species-level treatment/distribution jobs.

Any concrete tactical effect must point to an exact governing Move, Ability, Item, Feature, Capability, terrain/weather rule or authored Caelo condition.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Verified for reviewed static arenas. Distribution topology is not battle range/LoS.

`base movement legality`

Verified for ordinary static tactical movement. It does not create wet-floor, pipe-crossing, ladder, current or evacuation semantics.

`core calculations`

Verified primitives remain available. No hydraulic, pressure, treatment or quality arithmetic is inferred.

`action economy/initiative`

Verified typed action budget/order remains available.

`AI legal-action infrastructure`

Verified legal-action enumeration remains available. It does not choose withdrawal corridors, protect operators or understand water-service restoration objectives.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

PARTIAL. #256-#261 significantly deepen a specific Intercept/target-replacement route. Broad Push/Pull, broad Knockback, generalized reactions and environmental displacement remain unverified as complete families.

`full turn/round lifecycle`

PARTIAL. No treatment stage, pump cycle, verification window or restoration checkpoint is embedded as a universal battle lifecycle mechanic.

`full stateful damage pipeline`

PARTIAL. Pass 107 adds no generic water, contamination, equipment, pressure or collision damage.

`status lifecycle`

PARTIAL. Water-service restrictions and quality clearances are world/service state, not PTU statuses. Exact statuses require exact rules.

`move-specific behavior`

PARTIAL. Pre-resolution target replacement infrastructure is stronger, but not every Move is implemented and no Move-to-treatment conversion is established.

`abilities`

PARTIAL. Hook infrastructure can orchestrate sources, but it does not establish broad Ability coverage or utility effects.

`items`

PARTIAL. Utility equipment and water containers do not become PTU Items or gain effects from presentation.

`Trainer Features/perks`

PARTIAL. No universal water-treatment, plumbing, sampling, repair or public-utility Feature family is established.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

BLOCKING for contaminated-water zones, currents, wet/slip zones, active machinery, pressure releases, generalized reaction windows or environmental water effects.

`AI tactical policy`

BLOCKING for WITHDRAW/PROTECT/SECURE_ROUTE/DEFEND_OPERATOR/ESCORT and other objective-aware behavior.

`Minecraft/Cobblemon/Craftics adapter/playback support`

BLOCKING for stable drinking-water system/facility/stage/node/link/sector/service-point bindings, authoritative state projection, reviewed world-to-arena conversion and semantic battle playback.

## Encounter readiness

### Treatment Plant Access Withdrawal

Full intended form requires multiple protection/withdrawal routes, Intercept/forced movement, generalized reactions, possible technical zones, objective-aware AI and playback.

Current profile: REDUCED.

Safe implementation:

Ouros isolates the relevant process before battle. Workers, process water, controls and equipment remain outside BattleSpec. AutoPTU receives explicit participants in a reviewed dry static access area. Victory changes only immediate access/security state. Maintenance, Water Continuity, Science/Sanitation and other owners perform their post-battle steps independently.

### Service Reservoir Perimeter

Full intended form may require route control, reviewed elevation/edge terrain, reactions, forced movement, tactical policy and playback.

Current profile: REDUCED.

Safe implementation:

The storage asset and water are noninteractive protected scenery. Combat uses adjacent stable ground. Victory permits later inspection; it does not establish storage integrity, potability, path availability or service restoration.

### Temporary Water Point Perimeter

Full intended form may require civilian withdrawal, protected access, Intercept/forced movement, generalized reactions, objective-aware AI and playback. Any spill/equipment/vehicle hazard additionally requires exact environmental mechanics.

Current profile: REDUCED.

Safe implementation:

Suspend distribution and evacuate civilians/workers before combat. Freeze fallback state. AutoPTU resolves a static nearby encounter. The battle result cannot allocate water, change quality clearance or resume public distribution.

## Immediate noncombat readiness

Usable now as proposed narrative state without new tactical mechanics:

- stable drinking-water-system identity;
- authored source-water handoffs;
- treatment facility and stage identities;
- treatment running versus output verified separation;
- quality-clearance references with scope and validity windows;
- treated-water handoffs;
- treated storage with broad narrative reserve bands;
- authored distribution nodes/links/paths;
- service-sector state;
- service-point state;
- scoped field observations;
- isolation records;
- temporary/alternate supply;
- staged restoration checkpoints;
- legacy/decommissioned topology;
- contradictory reports resolved through scope/timestamp/provenance rather than hidden truth scores;
- explicit handoffs to Care, Residential, Hospitality, Fire Response, Manufacturing and other downstream owners.

## Minecraft/Cobblemon consequence

Binding remains:

`Ouros drinking-water/world state -> explicit encounter composition -> AutoPTU authoritative BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`.

Safe presentation reuse can include treatment buildings, basins, tanks, authored pipe/valve scenery, pump buildings, public taps, barriers, temporary distribution points, workers, individually authored Pokémon, sounds, particles, UI, networking, tracking and persistence hooks.

Adapter work is required for stable IDs, state projection, reviewed arena conversion and semantic playback.

Minecraft/Cobblemon must never decide that:

- touching pipes are connected in the authored distribution graph;
- flowing water proves service;
- clear/blue water is potable;
- a pump/control animation proves treatment or delivery;
- redstone is water-system authority;
- drinking grants HP/status recovery;
- dirty water applies Poison;
- water blocks apply current/forced movement;
- a Water-type Pokémon purifies water;
- a Poison-type Pokémon is contamination-safe;
- nearby entities become operators or combatants;
- Cobblemon BattleState/controller logic owns combatants, legality, HP/status, positions or outcome.

## Readiness conclusion

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: complete movement including push/pull/knockback/interception/forced movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback support.

## Unresolved canon questions

- Which regions/settlements use centralized treatment, wells, springs, rain collection or other systems?
- Which raw-water systems feed drinking-water systems?
- Which institutions operate treatment/distribution?
- Which treatment technologies actually exist in each region?
- Which quality-clearance categories and public-information practices exist?
- Which distribution/fallback arrangements exist?
- Which public water points are culturally important?
- Which legacy facilities remain in the world?
- Which individual Pokémon perform authored utility roles?

## Unresolved mechanical questions

- exact PTU/Caelo rules for any water-treatment or distribution technical task;
- environmental water/contamination damage or status;
- current, slipping, drowning or pressure effects;
- technical equipment as tactical objects;
- complete competing-reaction semantics after #261;
- concrete Move/Ability/Item/Trainer Feature utility registrations;
- rescue/carry interactions;
- objective-aware withdrawal/protection policy;
- semantic adapter representation without giving Minecraft utility or battle authority.

No answer is invented by this snapshot.