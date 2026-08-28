# Engine Readiness Snapshot — Pass 109

Status: IMPLEMENTATION-READINESS EVIDENCE. Creates no PTU rules or Ouros canon.
Date: 2026-08-28

## Scope

Pass 109 adds proposed continuity for authored fuel supply, operating storage, allocation/release, distribution, local service points, shortage episodes, temporary supply and staged recovery.

Narrative baseline before Pass 109 writes: `aebe36f39eafb9d9554d3e302368b28b6de9d426`.

The complete recursive Narrative repository inventory was inspected at baseline and returned `truncated=false`. Technology/Energy, Infrastructure Outage, Procurement, Storage/Warehousing, Fire Response, the internal PTU/Caelo source scan and Pass 108 readiness were checked directly before writing. Repository inventory contained no dedicated fuel supply/storage/distribution continuity layer.

Pass 109 files:

- `research/2026-08-28-fuel-supply-storage-distribution-continuity-scan-109.md`
- `design/fuel-supply-storage-distribution-continuity-extension.md`
- `proposals/2026-08-28-fuel-supply-storage-distribution-seeds-109.md`
- this readiness snapshot

## Live engine evidence

### AutoPTU-Java

Head inspected during this pass: `9f63f0a81af45af2fbc87928b96c1cec4fcff4b0`, PR #262, `Rebind move preparation after pre-resolution target replacement`.

No newer Java commit was present during this inspection than the one reviewed in Pass 108.

Current relevant evidence:

- pre-resolution target replacement runs in the server-owned runtime path;
- target replacement composes with authoritative move preparation;
- the effective redirected target is used to rebuild defender-bound values before accuracy RNG;
- tests cover defense/evasion rebinding and preserve the server-owned boundary;
- this continues the reviewed #256-#262 Intercept/target-replacement chain.

This remains narrow evidence. It does not verify:

- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- generalized competing reactions;
- every reaction trigger window/order;
- all Move/Ability/Item/Trainer Feature hook registrations;
- environmental displacement;
- technical-object interaction;
- active vehicle movement;
- fuel/fire/spill hazard behavior;
- objective-aware protection/withdrawal tactical policy;
- Minecraft/Cobblemon semantic adapter/playback.

No permanent capability category is promoted by the current Java evidence.

### AutoPTU Python

Head inspected during this pass: `396e94f92cdc2da0af4bcdf3e795175525439e57`, PR #217, `Career: normalize null battle spec at API boundary`.

New evidence since Pass 108:

- the Career API boundary now normalizes a missing/null legacy battle transcript `spec` to a safe object;
- this composes with the existing events normalization before caching/presentation;
- regression coverage verifies the boundary behavior.

This is stability/backward-compatibility work for Career presentation. It adds no tactical battle-family capability relevant to Pass 109.

## PTU / Caelo boundary for fuel systems

The project source scan identifies PTU Core, Caelo Player's Guide, Caelo Region Location & Encounter List, character creation, errata/extras and Pokédex material as governing internal references.

The public PTU resource page continues to identify PTU 1.05 as the rules corpus. A separate Pokémon Tabletop community thread found during Pass 109 proposes petroleum/coal mechanics, prices and bonuses; it is community homebrew and is explicitly excluded from governing mechanics.

No inspected project evidence establishes universal PTU/Caelo rules for:

- fuel extraction;
- refining;
- fuel quality/grade arithmetic;
- tank capacity;
- transfer or pipeline flow;
- vehicle fuel consumption;
- generator/heating-fuel consumption;
- generic ignition probability;
- generic fuel explosions/blast damage;
- fuel fumes or exposure statuses;
- spill spread;
- generic contamination effects;
- Fire-type automatic ignition;
- Water-type automatic suppression;
- Poison-type exposure immunity;
- Pokémon species-level fuel handling competence;
- universal fuel-terminal Skill checks;
- fuel-specific Trainer Feature bonuses.

A tactical effect requires an exact governing Move, Ability, Item, Trainer Feature, Capability, terrain/weather rule or authored Caelo condition plus current implementation evidence.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Verified for reviewed static arenas. A tank, pipe, terminal or service sector does not become a target/range object automatically.

`base movement legality`

Verified for ordinary reviewed movement. It does not create vehicle traffic, spill movement, restricted industrial access, evacuation or technical-object traversal semantics.

`core calculations`

Verified primitives remain available. No fuel quantity, combustion, pressure, blast, consumption or transfer arithmetic is inferred.

`action economy/initiative`

Verified typed action budget and ordering remain available.

`AI legal-action infrastructure`

Verified legal-action enumeration remains available. It does not understand route protection, worker withdrawal, terminal isolation or service restoration objectives.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

PARTIAL. The #256-#262 chain materially strengthens one Intercept/target-replacement route. Broad Push/Pull, broad Knockback, generalized reactions, every forced-movement source and environmental displacement remain incomplete.

`full turn/round lifecycle`

PARTIAL. Fuel transfer, shortage and service recovery are world-state workflows and do not become battle-round clocks automatically.

`full stateful damage pipeline`

PARTIAL. Generic fire, explosion, collision, fumes, spill or technical-object damage is not established by fuel presence.

`status lifecycle`

PARTIAL. Fuel-service state is world state. No Burn, Poison, exposure or other status may be inferred from facility presentation.

`move-specific behavior`

PARTIAL. Current target-replacement composition improves one pre-resolution route but does not verify every Move or industrial interaction.

`abilities`

PARTIAL. No generic Ability-to-fuel-system interaction is established.

`items`

PARTIAL. Tanks, hoses, pumps, valves, containers and service equipment do not become PTU Items/tactical objects through presentation.

`Trainer Features/perks`

PARTIAL. No universal fuel handling, terminal operation, engineering, allocation or emergency-response Feature family is established.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

BLOCKING for active fire/fumes/spill/explosion/technical zones, generalized reaction windows, dynamic machinery/vehicle zones or authored environmental effects that require this family.

`AI tactical policy`

BLOCKING for WITHDRAW, PROTECT, SECURE_ROUTE, HOLD_PERIMETER, ESCORT, TERRITORIAL_WITHDRAWAL and similar objectives.

`Minecraft/Cobblemon/Craftics adapter/playback support`

BLOCKING for stable fuel-system/facility/sector/service-point bindings, authoritative state projection, reviewed world-to-arena conversion and semantic battle playback.

## Encounter readiness

### Fuel Depot Access Withdrawal

Full intended form wants multiple withdrawal/protection routes, Intercept/forced movement, generalized reactions, objective-aware AI and semantic playback. Any active fuel/fire/spill/equipment mechanic also requires exact governing rules and the environmental/hazard family.

Current profile: REDUCED.

Safe implementation:

Stop/isolate operations before BattleSpec creation. Evacuate workers, vehicles, handling equipment, travelers and nonparticipant Pokémon. Fuel assets remain excluded or inert. Ouros chooses combatants explicitly. AutoPTU receives a static reviewed access arena. Battle outcome changes immediate access/security only.

### Delivery Yard Perimeter

Full intended form wants route protection, withdrawal/escort behavior, complete movement/reactions, tactical policy and semantic playback. Active vehicles or transfer equipment require additional exact rules.

Current profile: REDUCED.

Safe implementation:

Freeze custody and distribution at the last verified handoff. Cargo, drivers, workers, vehicles and transfer equipment remain outside BattleSpec. Fight in a static adjacent perimeter. Victory does not load/unload, transfer custody, change allocation or establish delivery.

### Isolated Service Point Diversion

Full intended form wants multiple routes, protect/withdraw behavior, generalized reactions, possibly reviewed technical zones, tactical AI and playback.

Current profile: REDUCED.

Safe implementation:

Close the service point and redirect customers before battle. Staff and fuel-specific equipment remain outside the tactical scene. Combat occurs on ordinary reviewed ground. Winning can permit later inspection but cannot reopen service or verify supply.

## Immediate noncombat readiness

Usable now as proposed narrative state without adding tactical mechanics:

- stable fuel-system identity;
- terminal/depot/service-point identity;
- accepted-supply handoffs;
- broad operating-storage presence/availability observations;
- allocation/release provenance;
- internal-transfer readiness state without flow simulation;
- authored distribution paths;
- service-sector availability;
- shortage observations separated from cause claims;
- temporary supply arrangements;
- staged service recovery;
- downstream availability handoffs;
- decommissioning/repurposing history;
- environmental/fire/safety handoffs to existing owner systems;
- individual Pokémon assignments with unresolved mechanical validation;
- mysteries resolved through scope/timestamps/IDs rather than hidden truth scores.

## Minecraft/Cobblemon/Craftics boundary

Safe presentation reuse can include:

- terminals, depots and roadside service-point geometry;
- tanks, pipes, hoses, pumps, containers and vehicles as visual/non-authoritative props;
- barriers, signs, status lights and notices;
- NPC workers/travelers;
- Pokémon models/forms/poses/animations/cries;
- sound/particles where they do not imply mechanical effects;
- UI/networking/entity tracking/persistence hooks;
- decommissioned/repurposed industrial assets.

The adapter must not infer world or tactical truth from Minecraft state.

Explicitly unsafe shortcuts:

- tank block exists → stock exists;
- connected pipe model → distribution path verified;
- redstone active → transfer complete;
- item entity entered chest → custody/delivery complete;
- native Minecraft fire → PTU damage/Burn;
- native explosion → PTU blast damage;
- smoke particle → status/visibility penalty;
- liquid flow → forced movement;
- Pokémon proximity/species/Type → work competence or technical effect;
- Cobblemon BattleState/controller → combatant selection, legality, HP/status, position or outcome authority.

Authority remains Ouros world state → explicit AutoPTU BattleSpec → AutoPTU tactical resolution → adapter/playback.

## Current source/evidence summary

Narrative gap evidence:

- recursive repository inventory at Pass 108 head returned complete/not truncated;
- generic Technology/Energy already recognizes energy/fallback dependencies but not this operational supply chain;
- Infrastructure Outage deliberately avoids inventing fuel amounts/durations;
- Procurement, Storage, transport owners, Fire Response and Pollution already own adjacent states.

Public transformed-source evidence:

- Outskirt Stand: small fuel service point as recurring travel/social node;
- Virbank Complex: distinct industrial processing functions;
- Almia Oil Field Hideout/Sea of Wailord: decommissioning, reuse and legacy environmental consequences;
- Pokémon Tabletop fossil thread: useful homebrew provenance boundary, not PTU authority;
- DOE emergency-energy/SPR materials: high-level source-storage-distribution topology only.

## Unresolved canon questions

- Which Ouros regions use stored fuels?
- Which fuel kinds and use cases exist?
- Which systems are local versus imported/interregional?
- Which settlements have terminals, depots or service points?
- Which institutions operate them?
- Does heating-fuel delivery exist anywhere?
- Which transport or backup systems depend on fuel?
- What allocation authority exists during shortages?
- Which legacy sites remain and how are they reused?
- Which environmental histories are canon-approved?
- Which individual Pokémon have verified roles?

## Unresolved mechanical questions

- exact PTU/Caelo handling effects, if any;
- fuel as tactical Item/object;
- generic ignition/combustion/explosion/fumes/spill behavior;
- vehicle or generator consumption;
- thermal exposure;
- active vehicles/equipment inside combat;
- environmental displacement around liquids or machinery;
- complete Move/Ability/Item/Trainer Feature registrations;
- generalized competing reactions after the current Intercept chain;
- objective-aware withdrawal/protection AI;
- semantic adapter/playback.

Pass 109 intentionally leaves all of these UNKNOWN rather than inventing rules.
