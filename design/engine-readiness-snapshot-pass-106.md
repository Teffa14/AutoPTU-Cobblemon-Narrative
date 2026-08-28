# Engine Readiness Snapshot — Pass 106

Status: IMPLEMENTATION-READINESS EVIDENCE. Creates no PTU rules or Ouros canon.
Date: 2026-08-28

## Scope

Pass 106 improves the existing Technology/Energy POWER-network model with a narrower operational continuity extension for generation sources, authored nodes/links, service sectors, isolation/switching records, alternate supply, staged restoration and scoped verification.

Narrative baseline before Pass 106 writes: `0b939cb06858aa9668ff4b34b9124e06c76942d5`.

The complete recursive Narrative repository inventory was inspected at baseline and returned `truncated=false`. Technology/Energy, Civic/Public Works, Waste/Sanitation, Commercial Services, Food/Agriculture/Hospitality, the prior technology research scan, the original PTU/Caelo source scan and Pass 105 readiness were inspected directly. The initial food-service candidate was rejected because that authority already exists.

## Live engine evidence

### AutoPTU-Java

Head inspected during this pass: `52b84f8e280252793791e318f204c45da8069e8b`, PR #260, `Add ordered pre-resolution target hook registry`.

New evidence since Pass 105:

- server-owned `PreResolutionTargetContext` exists for target replacement before accuracy/damage;
- an ordered `PreResolutionTargetHookRegistry` composes registered hooks deterministically;
- tests demonstrate ordered target replacement and semantic events;
- replacement targets are required to exist in authoritative battle state;
- duplicate source/id registrations are rejected;
- the Python Intercept target-replacement call site is frozen by a parity gate;
- the registry recognizes hook source classes including reactions and abilities as orchestration infrastructure.

This is meaningful architecture for future pre-resolution effects and target redirection. It does not prove that every reaction, Ability, redirection rule or Intercept variant is implemented. A generic hook registry is infrastructure, not family-wide mechanic coverage.

The recent Intercept chain therefore now includes #256 through #260:

- #256 authoritative battle RNG for the Intercept d20;
- #257 Python-oracle mutation ordering including failed attempts;
- #258 authoritative candidate-attempt sequence composition;
- #259 spatial-success branch composition;
- #260 ordered pre-resolution target hook infrastructure and target-replacement parity gating.

Still outside family-wide verified coverage:

- broad Push/Pull from all supported sources;
- broad Knockback from all supported sources;
- generalized competing-reaction behavior;
- all reaction trigger windows and ordering semantics;
- every forced-movement source;
- environmental/equipment displacement;
- complete concrete Move/Ability/Item/Trainer Feature registrations against the hook infrastructure;
- objective-aware tactical policy;
- semantic Minecraft/Cobblemon playback.

No permanent category is promoted.

### AutoPTU Python

Head inspected during this pass: `1e060895a39b4694d92039b7f56f9a3fe9d3a692`, PR #214, `Career: tolerate malformed opponent knowledge transcripts`.

The change fails closed when legacy Career transcript combatant/event collections are malformed and prevents opponent-knowledge reconstruction from crashing. This is Career stability/privacy-boundary hardening. It adds no tactical battle-family coverage for Pass 106.

## PTU / Caelo electrical boundary

Existing project source evidence identifies PTU Core, Caelo Player's Guide, Caelo Region Location & Encounter material, character creation, errata/extras and Pokédex material as governing references available to the project.

No inspected source establishes a universal PTU/Caelo electric-grid ruleset for generator output, voltage/current/frequency, line capacity, substations, switching checks, outage probability, black start, electrical-worker bonuses, technical shock damage, Electric-type safety, Move-powered generation or species-level grid roles.

A Caelo/PTU location may have an authored mechanical environmental effect when the rules explicitly define one. That does not authorize Minecraft electricity or generic power infrastructure to synthesize damage, Burn, Paralysis, forced movement, terrain, Weather or reactions.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Verified for reviewed static arenas. Electrical-network topology and power-flow paths are unrelated to battle targeting range.

`base movement legality`

Verified for ordinary static tactical movement. It does not create energized-floor, equipment-climb, evacuation or escort semantics.

`core calculations`

Verified core calculation primitives remain available. No electrical engineering arithmetic is inferred.

`action economy/initiative`

Verified typed action budget/order remains available.

`AI legal-action infrastructure`

Verified legal-action enumeration remains available. It does not choose technician protection, withdrawal corridors, alternate access routes or infrastructure objectives.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

PARTIAL. #256-#260 substantially deepen a particular Intercept/target-replacement orchestration path. They do not verify broad Push/Pull, Knockback, competing reactions or every forced-movement source.

`full turn/round lifecycle`

PARTIAL. No timed repair, switching, energization, verification or restoration phase is embedded in battle.

`full stateful damage pipeline`

PARTIAL. Pass 106 introduces no generic electricity, arc, transformer, cable, collision or equipment damage.

`status lifecycle`

PARTIAL. Power loss, shock, equipment fault and sector outage are world/technical states, not PTU statuses. Any concrete status needs exact rules.

`move-specific behavior`

PARTIAL. The new target-hook registry is extensible infrastructure, but it does not prove all concrete Move behaviors or any Move-to-grid interaction.

`abilities`

PARTIAL. #260 tests hook-source ordering that can include an Ability source, but this does not implement every Ability or establish any electrical-infrastructure Ability effect.

`items`

PARTIAL. Technical world objects do not become PTU Items by presentation or proximity.

`Trainer Features/perks`

PARTIAL. No universal grid-operation, engineering, switching or electrical-safety Feature family is established.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

BLOCKING for energized technical zones, electrical exposure, moving machinery, downed-line areas, dynamic worksite hazards, generalized reaction windows or weather-coupled grid effects.

`AI tactical policy`

BLOCKING for WITHDRAW/PROTECT/SECURE_ROUTE/DEFEND_OPERATOR and other objective-aware behaviors.

`Minecraft/Cobblemon/Craftics adapter/playback support`

BLOCKING for stable power-system/source/node/link/sector bindings, authoritative technical-state projection, reviewed world-to-arena conversion and semantic battle playback.

## Encounter readiness

### Substation Access Withdrawal

Full intended form requires multiple protection/withdrawal routes, Intercept/forced movement, generalized reactions, objective-aware AI and playback. Any live electrical/worksite zone additionally requires exact PTU/Caelo mechanics and the blocking environmental family.

Current profile: REDUCED.

Safe form: Ouros records the site as isolated before combat. Workers, controls and equipment remain outside BattleSpec. AutoPTU receives explicit combatants in a reviewed static yard/access corridor. Victory secures access only; Technology/Maintenance/Power Grid perform inspection and verification later.

### Alternate Supply Perimeter

Full intended form may require protection, route control, reactions, forced movement, weather/technical zones, tactical policy and playback.

Current profile: REDUCED.

Safe form: the temporary source and operators remain outside the grid and technical state is frozen during battle. Combat occurs in a static neighboring space. Battle result cannot change source capacity, fuel, priority, switching, service-sector state or verification.

### Legacy Corridor Inspection

Full intended form may require multiple approaches, wildlife withdrawal/territorial policy, reviewed terrain, reactions/forced movement and playback.

Current profile: REDUCED.

Safe form: electrical state remains UNKNOWN until post-encounter inspection. Any battle is static with explicit participants. Old cables/pylons are scenery. Victory proves neither continuity nor usability of the legacy link.

## Immediate noncombat readiness

Usable immediately as proposed narrative state:

- stable power-system/source/node/link/sector identity;
- source-running versus network-available separation;
- link availability/isolation history;
- scoped sector state;
- repair-complete versus verification separation;
- energized versus verified separation;
- path-verified versus sector-verified separation;
- sector-verified versus downstream-service-ready separation;
- alternate and temporary supply records;
- staged restoration sequences;
- field observations with scope/timestamp/provenance;
- legacy/decommissioned topology;
- restoration reports that can disagree without any witness lying;
- downstream handoff to Care, Communications, Transit, Manufacturing, Water/Waste, Hospitality and other existing owners.

## Minecraft/Cobblemon consequence

Binding architecture remains:

`Ouros power/world state -> explicit encounter composition -> AutoPTU authoritative BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`.

Safe presentation reuse includes generation/substation structures, fences, line/cable scenery, panels, lamps/screens, temporary equipment, barriers, technician NPCs, sounds, particles, Pokémon models/forms/poses/animations/cries, UI, networking, tracking and persistence hooks.

Adapter work is required for stable system/source/node/link/sector IDs, authoritative state projection, world-object association, reviewed arena conversion and semantic playback.

Minecraft/Cobblemon must never decide that:

- redstone connectivity proves an electrical link;
- a lit lamp proves sector verification;
- a spinning/animated generator is available to the network;
- a repaired block authorizes energization;
- a cable entity applies PTU damage;
- native lightning/electricity applies PTU damage or status;
- an Electric-type Pokémon is electrically safe or supplies power;
- a nearby Rotom/Porygon controls infrastructure;
- every entity at a technical site is a combatant;
- Cobblemon BattleState/controller logic owns combatants, legality, HP/status, positions or result.

## Readiness conclusion

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: complete movement including push/pull/knockback/interception/forced movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback support.

## Unresolved canon questions

- Which generation/distribution arrangements exist by Ouros region?
- Which settlements share systems, and which are independent?
- Which institutions operate them?
- Which services have authored restoration priority, if any?
- Which legacy/decommissioned sites remain physically present?
- What technical-record access/privacy norms exist?
- Which individual Pokémon perform technical work?
- Which temporary supply arrangements are culturally remembered or retained?

## Unresolved mechanical questions

- exact PTU/Caelo support for any electrical technical task;
- any valid environmental electricity damage/status;
- technical equipment as tactical objects;
- worksite/electrical zones;
- complete competing-reaction semantics after #260 infrastructure;
- concrete Ability/Move/Item/Feature registrations into pre-resolution hook systems;
- objective-aware withdrawal/protection policy;
- adapter semantics for technical state without granting Minecraft grid or battle authority.

No answer is invented by this snapshot.
