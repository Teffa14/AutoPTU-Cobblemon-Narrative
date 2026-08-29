# Engine Readiness Snapshot — Pass 128

Status: EVIDENCE SNAPSHOT. This file records current evidence and does not promote capability families from isolated representative mechanics.
Date: 2026-08-29

## Read-only heads inspected

AutoPTU-Java current head: `80f08b5d66f3451f70743ac0d4717f3a3dd21a0b` — `Derive intercept Justified bonus from server state (#275)`.

This remains unchanged from Pass 127.

The bounded Intercept path still demonstrates PRE-target integration, interceptor movement to the resolved position, effective-defender replacement, server-owned Acrobatics/Athletics, server-owned Coaching temporary-effect state and exact `Justified [Errata]` detection with the pinned +4 modifier. Terrain remains an explicit internal input whose authoritative environment contract is not frozen.

This evidence is important but localized. It does not establish broad Push, Pull, Knockback, every forced-movement source, every Intercept timing window, generalized reactions, broad terrain authority, all Ability/Trainer Feature behavior or objective-aware tactical policy.

AutoPTU current head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`.

This is newer than Pass 127 head `2991a5492306678d49629d2001f076852032c4b0`.

The change synchronizes cached Pixi screen dimensions after viewport resize so later tactical sprite destinations use current renderer geometry. Regression coverage reproduces the stale-coordinate problem. The commit explicitly states that it is presentation-only and changes no battle rules or outcomes.

This is useful playback/UI hardening, but it does not verify the permanent `Minecraft/Cobblemon/Craftics adapter/playback support` family. That family includes authoritative semantic projection, combatant binding, world-state handoff and Minecraft/Cobblemon integration far beyond a Career Pixi resize fix.

## Permanent capability map

VERIFIED:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:

- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:

- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

No capability family is promoted in Pass 128.

## Pass 128 narrative readiness

The evacuation shelter/reunification/departure extension is predominantly world-state, provenance, privacy and owner-system handoff infrastructure.

READY without new tactical capability:

- time-scoped shelter population episodes;
- registration events that do not imply indefinite presence;
- separation records;
- reunification inquiries;
- location/contact evidence with timestamps and visibility scope;
- contact events separated from physical reunion;
- physical reunion separated from custody/residence changes;
- household displacement distribution by reference to existing household state;
- Pokémon identity/reunification by reference to Pokémon Agency;
- departure records with destination allowed to remain unknown;
- versioned roster snapshots;
- stale-record mysteries;
- former-shelter environmental callbacks;
- shelter closure separated from residential return;
- communication attempts separated from delivery/receipt/reply.

READY proposal patterns include:

- The Empty Cot Still Has a Name Card;
- Three Shelters, One Household;
- The Pokémon Arrived First;
- The Bus Left, the Registry Did Not;
- The Message Was Delivered to the Old Site;
- Two Similar Pokémon at Two Different Sites;
- The Reunion Happened Before the Roster Update;
- The Gymnasium That Still Has Tape on the Floor;
- The Actor Who Never Checked Out;
- Four Rosters, Three Times;
- Five Times They Were “Found”;
- The Shelter Closed, the Household Did Not Return;
- A Town Learns Where Everyone Went.

Any implementation that creates child/dependent release rules, guardianship, compulsory disclosure, emergency Pokémon custody or a formal reunification authority remains canon-dependent.

## Encounter readiness — Shelter Loading Bay Withdrawal

Full intended form can require active evacuee movement, protection objectives, Intercept, forced movement, staged departure timing, protected corridors, generalized reactions, tactical AI and semantic playback.

Capability classification:

- targeting/footprints/range/LoS — VERIFIED baseline;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL for exact governed effects;
- status lifecycle — PARTIAL for exact governed statuses;
- terrain/weather/hazards/zones/reactions — BLOCKING for protected corridors, changing safe areas or crossing reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for PROTECT/WITHDRAW/CLEAR_ROUTE behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced form: READY.

Crisis completes or pauses evacuee movement before BattleSpec creation. Evacuees, records, controlled belongings, vehicles and noncombatant Pokémon remain outside the tactical grid. AutoPTU receives static reviewed geometry and explicit combatants.

Victory may secure immediate access. It cannot register or discharge anyone, complete reunification, transfer Pokémon custody, reveal protected location information or prove destination arrival.

## Encounter readiness — Reunification Route Chokepoint

Full intended form can require escort-like movement, Intercept, forced displacement, timed route availability, protected crossing zones, objective-aware AI and semantic movement playback.

Capability classification remains the same as the Loading Bay encounter where those features are used: movement PARTIAL, lifecycle PARTIAL, terrain/zones/reactions BLOCKING, tactical policy BLOCKING and adapter/playback BLOCKING.

Reduced form: READY.

Identity, location and contact are resolved first in authoritative world state. Reunion subjects stay outside BattleSpec. AutoPTU resolves a conventional battle at a static chokepoint. Travel/Crisis decides whether the route becomes usable afterward. This layer records physical reunion only when it actually occurs.

Battle victory is never a reunification event.

## Encounter readiness — Temporary Registration Site Diversion

Full intended form can require staff withdrawal, protected equipment/records, changing service zones, reaction handling and objective-aware AI.

Reduced form: READY.

The owner pauses intake and removes staff/records before battle. AutoPTU receives a static perimeter. Battle result cannot authenticate identity, modify registration, expose private records or reopen the site.

## PTU / Caelo boundary

The standing source scan supports central plots, character-centric arcs, sandbox activity, social play, jobs, wild encounters and exact environmental mechanics where governing sources define them.

It does not establish universal mechanics for:

- evacuation;
- human shelter intake;
- shelter population/capacity;
- missing-person or reunification procedure;
- guardian/dependent release;
- crowd movement;
- panic or morale;
- carrying/dragging evacuees;
- protected-civilian escort reactions;
- generic rescue Skill DCs;
- communication through arbitrary Pokémon;
- emergency Pokémon custody;
- Pokémon identity from visual similarity alone;
- Loyalty changes from separation/reunion;
- species-derived rescue competence;
- automatic route clearing via Move/Ability/Item/Trainer Feature;
- emergency institutional authority granted by a Trainer Feature.

These remain narrative, UNKNOWN or exact-rule dependent.

## Existing narrative-system boundary

Crisis/Rescue owns hazard truth, evacuation, search/rescue priorities and shelter activation.

Residential owns normal residence, displacement, relocation and return review.

Family/Kinship owns explicit human relationship facts and player-consent boundaries.

Pokémon Agency owns persistent Pokémon identity, association, custody, residence, transfer and release.

Pokémon Shelter/Sanctuary owns formal Pokémon placement-program workflow where such a program exists.

Community Aid owns helper/volunteer participation.

Care owns health/treatment.

Travel owns journey and route use.

Communications/Public Notices own delivery/publication.

Pass 128 owns none of those decisions. It preserves time-scoped population, separation, contact, reunion and departure continuity among them.

## Minecraft / Cobblemon boundary

Minecraft/Cobblemon may present shelters, temporary partitions, registration desks, route signs, representative evacuees, authorized Pokémon entities, queue visuals, changed building use and former-shelter traces.

It cannot decide presence from chunk loading, household/family relation, guardianship, Pokémon ownership/custody, reunification from entity proximity, shelter departure, destination arrival or return-home authorization.

The new AutoPTU Career resize fix improves presentation coordinate synchronization only. It does not change this authority boundary.

Cobblemon BattleState remains outside combatant selection, tactical legality, HP/status, positions, shelter population truth, reunion state and narrative outcomes.

## Current implementation-safe pattern

For mechanically rich shelter/reunification scenes:

1. resolve crisis scope, shelter operations, privacy, identity evidence and noncombatant movement in Ouros world state;
2. preserve registration/roster history rather than rewriting old snapshots;
3. exclude guardianship, custody and unsupported rescue mechanics from BattleSpec;
4. keep evacuees, private records, controlled belongings and noncombatant Pokémon off-grid;
5. use static reviewed geometry;
6. explicitly select combatants in Ouros;
7. let AutoPTU resolve only supported battle mechanics;
8. return the battle result as one fact;
9. let Crisis, Travel, Residential, Pokémon Agency and this continuity layer determine downstream state.

## Unresolved canon questions

- Which Ouros institutions can open/operate emergency shelters?
- Do all regions use registration, or only some?
- What actor-level information is collected?
- Who can access or disclose current shelter location?
- What rules exist for children, dependents or guardians, if any?
- How are partner Pokémon accommodated during human evacuation?
- Are human and Pokémon shelter sites colocated, linked or region-dependent?
- Which Pokémon identity/custody records are available during crisis operations?
- Who can authorize temporary Pokémon custody or handoff?
- How are self-departures and unresolved roster entries recorded?
- Which former shelter sites and past evacuation episodes are established canon?
- What review or correction route exists for a disputed reunification record?

No answer is assumed in Pass 128.