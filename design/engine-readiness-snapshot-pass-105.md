# Engine Readiness Snapshot — Pass 105

Status: IMPLEMENTATION-READINESS EVIDENCE. Creates no PTU rules or Ouros canon.
Date: 2026-08-28

## Scope

Pass 105 adds proposed communications-network continuity between existing Technology/Infrastructure and Media ownership: persistent communications nodes/links, service paths, sectors, endpoint readiness, temporary relays, reroutes and scoped verification.

Narrative baseline before Pass 105 writes: `91b1774f26ae5841e4a04e4d67d9c40bfd8acbfb`.

The complete recursive Narrative repository inventory was inspected at baseline and returned `truncated=false`. Media/Communications, Technology/Energy, Infrastructure Outage and Digital Systems were inspected directly so this pass does not create a duplicate delivery, maintenance, outage or data subsystem.

## Live engine evidence

AutoPTU-Java head inspected during this pass: `136cf6d090b6387481fc7bb908abb098abddd8be`.

This is unchanged from Pass 104. Current recent Intercept evidence remains:

- #256 moves the Intercept d20 to authoritative battle RNG;
- #257 preserves Python-oracle mutation ordering, including failed attempts;
- #258 composes the candidate-attempt sequence authoritatively;
- #259 composes the sequence through the spatial-success branch and gates parity for that path.

This is meaningful, increasingly deep evidence for a specific Intercept orchestration path. It does not verify the permanent family `complete movement including push/pull/knockback/interception/forced movement` as a whole.

Still outside family-wide verified coverage:

- broad Push/Pull from all supported sources;
- broad Knockback from all supported sources;
- generalized/competing reactions;
- reaction ordering outside the frozen Intercept path;
- every forced-movement source;
- environmental displacement;
- equipment-driven displacement;
- complete Move/Ability/Item/Trainer Feature integration;
- objective-aware tactical policy;
- semantic Minecraft/Cobblemon playback.

AutoPTU Python head inspected during this pass: `8c8b99959ce43901105ed7dc325d5bd5063f2fcf`.

New evidence since Pass 104:

- PR #213 `Career: tolerate malformed legacy battle state arrays`;
- the change normalizes malformed legacy Career battle-state arrays to avoid client/replay crashes.

This is Career stability/backward-compatibility work. It does not add tactical battle-family coverage for Pass 105 encounters.

No permanent capability category is promoted.

## PTU / Caelo communications boundary

Existing project source evidence identifies PTU Core, Caelo Player's Guide, Caelo Region Location & Encounter material, character creation, errata/extras and Pokédex material as governing references available to the project.

Nothing inspected establishes a universal PTU/Caelo telecommunications ruleset for:

- radio/signal range;
- coverage geometry;
- frequency allocation;
- interference or jamming actions;
- antenna/tower repair DCs;
- endpoint configuration bonuses;
- electrical hazards from communications equipment;
- Move/Ability-based radio transmission;
- species-level repeater/operator roles;
- communication-derived initiative, Accuracy, damage or status effects.

Any concrete telepathy, Aura, Electric Move, Porygon/Rotom, Item, Capability, Skill or Trainer Feature use must cite its exact governing rule and implementation evidence.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Verified for reviewed static arenas. Tower geometry, relay huts, fences and access paths only gain tactical meaning after explicit arena review. Radio/network range is unrelated to battle targeting range.

`base movement legality`

Verified for ordinary static tactical movement. It does not create climbing-tower, cable traversal, active machinery, evacuation or escort semantics.

`core calculations`

Verified calculation primitives remain available. No signal-strength, frequency, power, bandwidth, latency, collision or electrical arithmetic is inferred.

`action economy/initiative`

Verified typed action budget/order remains available.

`AI legal-action infrastructure`

Verified legal-action enumeration remains available. It does not choose withdrawal routes, defend relays, protect operators or prioritize communications objectives.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

PARTIAL. Java #256-#259 provide increasingly strong evidence for one Intercept path. Broad Push/Pull, Knockback, competing reactions and all forced-movement sources remain unverified as a family.

`full turn/round lifecycle`

PARTIAL. No timed repair, timed signal restoration or technician progress phase is assumed.

`full stateful damage pipeline`

PARTIAL. Pass 105 introduces no electricity, falling antenna, wind, cable, collision or equipment damage.

`status lifecycle`

PARTIAL. Interference, service loss, panic, shock or endpoint failure are not PTU statuses unless exact rules establish them.

`move-specific behavior`

PARTIAL. A Move cannot be generalized into transmitting, jamming, powering, repairing, calibrating or authenticating communications.

`abilities`

PARTIAL. An Ability does not automatically make a Pokémon a repeater, receiver, jammer, technician or electrically safe operator.

`items`

PARTIAL. Antennas, radios, cables, relays, batteries and terminals remain world/technical objects unless governing Item rules apply.

`Trainer Features/perks`

PARTIAL. No universal communications engineering or signal-control Feature family is established.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

BLOCKING for active electrical zones, strong-wind displacement, moving machinery, falling structures, dynamic technical hazards, weather-driven battle effects or generalized protective reactions.

`AI tactical policy`

BLOCKING for withdrawal, route protection, operator protection, relay defense and objective-aware access denial.

`Minecraft/Cobblemon/Craftics adapter/playback support`

BLOCKING for stable node/link/service/sector bindings, authoritative state projection, reviewed world-to-arena conversion and semantic battle playback.

## Encounter readiness

### Relay Access Withdrawal

Full intended form requires multiple withdrawal paths, Intercept/forced movement, generalized reactions, objective-aware AI and playback. Active tower/work hazards additionally require exact PTU/Caelo effects plus the blocking environmental family.

Current profile: REDUCED.

Safe form:

Ouros isolates the relay and evacuates technicians before combat. Tools, controls and nonparticipants remain outside BattleSpec. AutoPTU receives explicit combatants in a reviewed static access area. Victory secures immediate access only; Technology/Maintenance and Communications perform repair/verification afterward.

### Temporary Relay Perimeter

Full intended form can require route defense, reactions, forced movement, tactical policy and playback. Wind, energized equipment or other active zones directly require `terrain/weather/hazards/zones/reactions`.

Current profile: REDUCED.

Safe form:

Temporary equipment and operators remain outside BattleSpec. Combat uses a static adjacent perimeter. Victory does not prove service continuity. A post-battle communications verification determines whether the relay and supported sectors remain available.

### Repeater Ridge Diversion

Full intended form may require escort/withdrawal, several approach routes, Intercept/forced movement, reviewed weather/terrain effects, tactical policy and playback.

Current profile: REDUCED.

Safe form:

Travel selects a static encounter area before the technical site. Crew and equipment wait outside battle. Inspection occurs afterward as noncombat world state. No radio, electricity, wind or signal effect is synthesized tactically.

## Immediate noncombat readiness

Usable immediately as proposed narrative state:

- persistent communications-network identity;
- stable node and authored-link identity;
- separate logical service identity;
- service-sector availability with timestamped provenance;
- endpoint readiness/access state separate from network availability;
- primary/alternate/contingency/emergency/temporary paths;
- temporary-relay lifecycle;
- scoped verification tests;
- repair-complete versus network-verified separation;
- path-verified versus sector-verified separation;
- sector-verified versus endpoint-ready separation;
- stale coverage/service claims preserved as versioned evidence;
- unexplained degradation observations without automatic cause;
- restoration history and delayed retirement of workarounds.

## Minecraft/Cobblemon consequence

Binding architecture remains:

`Ouros communications/world state -> explicit encounter composition -> AutoPTU authoritative BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`.

Safe presentation reuse includes tower/relay geometry, antenna assets, cables as scenery, status lights/screens, barriers, technician NPCs, sounds, particles, Pokémon models/forms/poses/animations/cries, UI, networking, tracking and persistence hooks.

Adapter work is required for stable node/link/service/sector bindings, authoritative state projection, endpoint/world-object association, reviewed arena conversion and semantic battle playback.

Minecraft/Cobblemon must never decide that:

- towers form a link because of block geometry or line of sight;
- redstone continuity proves service availability;
- a powered block proves a sector is verified;
- an antenna animation proves transmission;
- a device in inventory proves endpoint entitlement;
- a nearby Pokémon supplies or disrupts communications;
- native lightning/electricity applies PTU damage/status;
- every entity at a relay is a combatant;
- Cobblemon BattleState/controller logic owns combatants, legality, HP/status, positions or battle result.

## Readiness conclusion

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: complete movement including push/pull/knockback/interception/forced movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback support.

## Unresolved canon questions

- Which communications technologies exist in each Ouros region?
- Which settlements use towers, repeaters, wired links, portable systems or other infrastructure?
- Which institutions operate those networks?
- Which services, if any, have authored fallback priority?
- Which endpoint access/entitlement models exist?
- What privacy and service-access norms apply?
- What cross-region communication dependencies exist?
- Which former relay sites were repurposed or became landmarks?
- Which individual Pokémon perform communications work, and what explicit evidence authorizes each task?

## Unresolved mechanical questions

- exact PTU/Caelo support for any communications-related Skill, Capability, Move, Ability, Item or Trainer Feature;
- telepathy/Aura/device interaction boundaries;
- Porygon/Rotom technical interaction where relevant;
- any legal electrical/technical tactical hazard;
- communications equipment as tactical objects;
- objective-aware withdrawal/protection policy;
- adapter semantics for technical animations without giving Minecraft network or battle authority.

No answer is invented by this snapshot.
