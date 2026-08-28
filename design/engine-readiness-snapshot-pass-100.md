# Engine Readiness Snapshot — Pass 100

Status: IMPLEMENTATION-READINESS EVIDENCE. This snapshot does not create PTU rules or Ouros canon.
Date: 2026-08-28

## Scope

Pass 100 adds proposed Hospitality/Lodging continuity: establishment identity, accommodation units, reservations, guest parties, stay records, service availability, staffing/capacity, interruptions, recurring guests and explicit PTU rest boundaries.

Narrative baseline before Pass 100 writes: `74bb82828015eaafb4a93ec683189685ed66822a`.

Read-only evidence inspected:
- complete recursive Narrative repository inventory and design directory;
- repository search for hotel/inn/lodging/hospitality/guest accommodation concepts;
- Pass 99 readiness snapshot;
- current AutoPTU-Java commit history and README;
- current AutoPTU commit history;
- PTU 1.05 Resting/Pokémon Center evidence.

## Live engine evidence

AutoPTU-Java head remains `39b81222af080dd5b2db9b3efdfe742b746d5f5d`, #255, “Freeze intercept orchestration control flow”.

That commit remains narrow evidence for one Intercept orchestration route. Current README still lists major unfinished families including core battle state, full damage, status controller, terrain, hazards, forced movement/reactions, move/ability/item/perk/Trainer Feature registries, full transcript parity, AI scoring/policy and the Craftics/Cobblemon adapter.

AutoPTU head advanced to `d81381779e9c587cfa2e0a594f6db6f16971a2dd`, merging Career protection for remaining browser-storage access on UI surfaces. This is client stability work, not tactical battle-family evidence.

No permanent capability category is promoted in Pass 100.

## PTU 1.05 hospitality-specific evidence

PTU 1.05 defines ordinary Rest, Extended Rest and Pokémon Center healing separately.

Relevant narrow evidence:
- rest depends on inactivity rather than merely occupying a room;
- Extended Rest requires at least four continuous hours;
- Extended Rest refreshes specific resources/effects defined by PTU;
- Pokémon Centers perform separate advanced healing with timing modified by Injuries;
- extended travel generally does not count as rest.

This supports a strict separation between Hospitality world state and PTU recovery.

Unsupported in current live evidence:
- a verified nonbattle AutoPTU API for starting, interrupting and completing Extended Rest from Ouros world time;
- adapter rules converting Minecraft bed use into PTU rest;
- automatic Pokémon Center service execution from a Cobblemon/Minecraft facility;
- exact interruption semantics if combat or travel occurs during an in-progress rest interval.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Verified for static reviewed battlefields. Hospitality does not add dynamic visibility mechanics.

`base movement legality`

Verified for ordinary static arena movement. It does not establish evacuation objectives.

`core calculations`

Verified primitives remain available. They do not create lodging or recovery semantics.

`action economy/initiative`

Verified typed action budget/order remains available.

`AI legal-action infrastructure`

Verified legal-action enumeration remains available. It does not understand guest evacuation, private-room avoidance or perimeter protection.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

PARTIAL. Push/Pull and the frozen Intercept route have substantial evidence, but broad reactions/forced movement are incomplete.

`full turn/round lifecycle`

PARTIAL. Hospitality encounters need no new turn model in reduced form, but full evacuation/reaction scenes still depend on broader lifecycle integration.

`full stateful damage pipeline`

PARTIAL. No new hospitality-specific damage behavior is required, but family-wide completion remains unverified.

`status lifecycle`

PARTIAL. Rest must not be confused with the battle Sleep status; no new status behavior is introduced.

`move-specific behavior`

PARTIAL. Specific implemented Moves cannot be treated as evidence for generic evacuation/service interactions.

`abilities`

PARTIAL. No Ability may imply hospitality competence, guest status or rest acceleration without exact rules.

`items`

PARTIAL. No generic lodging, bed or camping item rule is verified by this pass.

`Trainer Features/perks`

PARTIAL. No broad hospitality/rest-management Feature coverage is established.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

BLOCKING for mechanically rich occupied-building evacuation or dynamic service-area hazards. Reduced versions avoid those mechanics.

`AI tactical policy`

BLOCKING. Legal-action generation does not establish policy for guest withdrawal, protecting exits, separating participants from occupants or avoiding private spaces.

`Minecraft/Cobblemon/Craftics adapter/playback support`

BLOCKING. Minecraft/Cobblemon can represent rooms, beds, buildings, guests and animations, but no adapter currently makes those visuals authoritative PTU state.

## Encounter readiness — Guest Wing Withdrawal

Full intended form wants several withdrawal routes, protection objectives, Intercept/forced movement, reactions, objective-aware AI and authoritative playback.

Current profile: REDUCED.

Safe reduced form:
- evacuate every uninvolved guest before battle;
- exclude private/occupied rooms, luggage and service equipment;
- select combatants explicitly in Ouros;
- use a static lobby/courtyard/corridor;
- no dynamic evacuation objective;
- battle secures only the immediate area;
- Hospitality/Crisis retain re-entry and stay-continuation authority.

## Encounter readiness — Overflow Camp Perimeter

Full intended form wants route-control/protection behavior, reactions, reviewed terrain and tactical policy aware of the nonparticipant zone.

Current profile: REDUCED.

Safe reduced form:
- keep occupants, tents, luggage and resting Pokémon outside BattleSpec;
- use a static perimeter;
- do not infer rest completion or guest relocation from battle outcome;
- Hospitality retains accommodation allocation.

## Encounter readiness — Service Courtyard Interruption

Full intended form may want worker withdrawal, protection objectives, reactions and tactical AI.

Current profile: REDUCED.

Safe reduced form:
- Maintenance suspends work before combat;
- workers and equipment leave;
- fight on a static service lane/courtyard;
- battle cannot repair an asset or restore an amenity.

## Noncombat readiness

Hospitality continuity is usable immediately without tactical expansion:
- reservations and changes;
- check-in/check-out history;
- room allocation and reassignment;
- guest recurrence across towns;
- capacity/overflow state;
- service outage history;
- privacy-aware investigations;
- maintenance/travel/crisis handoffs;
- disputed booking reconciliation;
- lodging interruption and later restoration.

## Cobblemon/Minecraft consequence

Binding architecture remains:

`Ouros encounter/world state -> AutoPTU BattleSpec -> AutoPTU authoritative state/result -> adapter -> Minecraft/Cobblemon presentation`

Safe presentation candidates:
- hotel/inn/lodge geometry;
- rooms, furniture and decorative beds;
- signs, doors, lamps and service desks;
- camps/tents if assets exist;
- Pokémon models/forms/poses/animations/cries;
- day/night and weather visuals;
- UI, networking, world coordinates, entity tracking and persistence hooks.

Adapter-required:
- stable establishment/unit/stay identity bindings;
- authoritative access projection;
- reviewed tactical arena conversion;
- stable guest/Pokémon identity through load/unload;
- semantic playback;
- any future explicit nonbattle PTU rest service bridge.

Minecraft/Cobblemon must never decide:
- reservation from a sign or chest;
- occupancy from presence near a bed;
- guest party from proximity;
- Trainer/Pokémon ownership from room sharing;
- PTU Rest/Extended Rest from sleeping animation;
- Pokémon Center healing from building type;
- combatants from everyone inside the property;
- eviction, re-entry or checkout from KO result;
- battle result.

## Readiness conclusion

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: complete movement including push/pull/knockback/interception/forced movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback support.

## Unresolved canon questions

- Which Ouros regions use hotels, inns, lodges, hostels, camps or resorts?
- Do any Pokémon Centers offer accommodation?
- Can Pokémon be independent lodging guests under Ouros law/custom?
- How do reservations, identification, privacy, payment and deposits work?
- How are emergency shelters related to normal lodging?
- Which accessibility standards or practices exist?
- Which individual Pokémon have established hospitality roles?

## Unresolved mechanical questions

- exact nonbattle PTU Rest/Extended Rest event contract;
- exact interruption semantics for in-progress rest;
- world-time accounting without double counting;
- dedicated Pokémon Center healing service bridge;
- Item/Ability/Trainer Feature interactions with nonbattle rest;
- whether any bed/tent/shelter grants mechanical modifiers;
- how saved/loaded world state preserves an in-progress rest interval.

No answer is invented by this snapshot.