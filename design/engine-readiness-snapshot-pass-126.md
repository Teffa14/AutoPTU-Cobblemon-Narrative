# Engine Readiness Snapshot — Pass 126

Status: EVIDENCE SNAPSHOT. This file records current evidence and does not promote capability families from isolated representative mechanics.
Date: 2026-08-29

## Read-only heads inspected

AutoPTU-Java current head: `80f08b5d66f3451f70743ac0d4717f3a3dd21a0b` — `Derive intercept Justified bonus from server state (#275)`.

This is unchanged from Pass 125. The concrete Intercept route still has server-owned Acrobatics/Athletics skill inputs, Coaching temporary-effect state and exact `Justified [Errata]` ability bonus. Successful interception movement and target replacement have evidence through the PRE-target registry into the authoritative Move pipeline. Terrain remains an internal input whose authoritative environment contract has not been frozen.

No newer AutoPTU-Java evidence was found in this pass.

AutoPTU current head: `91b15a2efc0d762fc87937b2514095bb4937d5f8` — `Career: cap recovered active lineup at six Pokémon (#235)`.

Compared with Pass 125 head `d97c45e76647642105fee3ff1b9b80a38e092778`, the new Career slice repairs persisted browser saves whose active roster contains more than six valid unique Pokémon IDs. It preserves the first six in order and keeps additional Pokémon as reserves. This is persistence/recovery hardening and provides no tactical battle coverage.

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

No capability family is promoted in Pass 126.

## Bounded Intercept evidence

Currently supported evidence remains limited to a concrete route in which:
- interception can execute through a PRE-target runtime bridge;
- successful Intercept movement uses the resolved interceptor position;
- the effective defender can be replaced before authoritative Move resolution;
- Acrobatics and Athletics derive from server-owned combatant rule content;
- Coaching derives from server-owned temporary effects;
- exact `Justified [Errata]` state and its pinned modifier derive from server-owned ability state;
- similarly named `Justified` does not satisfy that exact contract;
- the check-input factory remains internal to core authority.

Still outside verified scope:
- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- every Intercept timing/window;
- environmental displacement;
- generalized competing reactions;
- generalized reaction ordering;
- broad terrain authority;
- every Move, Ability, Item or Trainer Feature registration/behavior;
- objective-aware AI tactical policy;
- semantic adapter playback.

## Pass 126 narrative readiness

The land-parcel/boundary continuity model is primarily world-state, provenance and institutional-handoff infrastructure.

READY without new tactical capability:
- persistent neutral land-unit IDs;
- versioned geometry claims;
- links to existing Cartography surveys and map editions;
- physical fence/wall/post/ditch observations without authority inference;
- boundary discrepancy records;
- neutral land-interest claims when canon provides the interest type and source;
- residence/occupancy links without ownership inference;
- ranch/conservation/public-work stewardship links;
- path/crossing observations separated from authored access permissions;
- public-work intersections with independent construction and record-update state;
- address history;
- natural-feature movement separated from any rule about legal boundary movement;
- Pokémon behavior observations without parcel-right inference;
- record revision lineage;
- archival mysteries based on chronology, scope and map purpose.

`The Fence Was Built for Mareep`, `The Address Survived the Land Change`, `The Marker Is Genuine and Still Misleading`, `Two Maps, Two Jobs`, `Five Lines Around One Field`, `Four Stones, Three Surveys`, `The Path That Is Missing From Every Official Map`, `One Farm, Three Names`, `The Boundary Walk Above the Old Canal` and `The Orchard Behind Two Addresses` are READY as narrative/world-state content.

## Encounter readiness — Survey Marker Recovery Perimeter

Targeting/footprints/range/LoS — VERIFIED.

Base movement legality — VERIFIED.

Complete movement including push/pull/knockback/interception/forced movement — PARTIAL for active withdrawal, Intercept or forced displacement.

Core calculations — VERIFIED.

Action economy/initiative — VERIFIED.

Full turn/round lifecycle — PARTIAL if survey-team withdrawal or perimeter closure occurs over staged turns.

Full stateful damage pipeline — PARTIAL for selected governed combat effects.

Status lifecycle — PARTIAL for selected governed statuses.

Terrain/weather/hazards/zones/reactions — BLOCKING for protected survey zones, crossing reactions, environmental displacement or changing safe areas.

Move-specific behavior — PARTIAL.

Abilities — PARTIAL. Current `Justified [Errata]` evidence remains bounded to one exact Intercept modifier and does not prove broad Ability coverage.

Items — PARTIAL.

Trainer Features/perks — PARTIAL. Coaching evidence remains bounded to the concrete Intercept route.

AI legal-action infrastructure — VERIFIED.

AI tactical policy — BLOCKING for PROTECT/WITHDRAW.

Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic withdrawal, evidence-secure and perimeter-state playback.

Reduced form: READY. Finish or pause surveying first. Secure field notes and measurements in world state. Remove staff, controlled evidence and survey objects from BattleSpec. Use static reviewed geometry. Battle victory may secure immediate access but cannot validate a boundary, accept a survey or update a registry.

## Encounter readiness — Access Corridor Diversion

Targeting/footprints/range/LoS — VERIFIED.

Base movement legality — VERIFIED.

Complete movement — PARTIAL for active escort, withdrawal, Intercept or forced displacement.

Core calculations — VERIFIED.

Action economy/initiative — VERIFIED.

Full turn/round lifecycle — PARTIAL for timed closure/rerouting windows.

Full stateful damage pipeline — PARTIAL for selected governed combat effects.

Status lifecycle — PARTIAL for selected governed statuses.

Terrain/weather/hazards/zones/reactions — BLOCKING if corridor boundaries change tactically or generalized crossing reactions are required.

Move-specific behavior — PARTIAL.

Abilities — PARTIAL.

Items — PARTIAL.

Trainer Features/perks — PARTIAL.

AI legal-action infrastructure — VERIFIED.

AI tactical policy — BLOCKING for CLEAR_ROUTE/PROTECT/WITHDRAW.

Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING for semantic closure, reroute and objective playback.

Reduced form: READY. Close the crossing and reroute civilians/workers before BattleSpec creation. Keep noncombatants and controlled objects off-grid. Resolve a conventional static chokepoint battle. Winning can permit later inspection; it cannot create a right of way or decide a land-interest claim.

## Encounter readiness — Flood-Shifted Fence Reinspection

Targeting/footprints/range/LoS — VERIFIED baseline. Dynamic water/visibility modifications would require additional governed environmental evidence and are not implied by the baseline.

Base movement legality — VERIFIED baseline for static reviewed geometry.

Complete movement — PARTIAL for forced movement, Intercept or displacement near environmental edges.

Core calculations — VERIFIED.

Action economy/initiative — VERIFIED.

Full turn/round lifecycle — PARTIAL for staged environmental or withdrawal events.

Full stateful damage pipeline — PARTIAL only for exact governed effects. Generic mud/current/falling-bank damage remains UNKNOWN.

Status lifecycle — PARTIAL only for exact governed effects. No generic flood or mud status is inferred.

Terrain/weather/hazards/zones/reactions — BLOCKING for moving water, mud, unstable cells, bank collapse, environmental displacement or generalized reactions.

Move-specific behavior — PARTIAL.

Abilities — PARTIAL.

Items — PARTIAL.

Trainer Features/perks — PARTIAL.

AI legal-action infrastructure — VERIFIED.

AI tactical policy — BLOCKING for PROTECT/WITHDRAW around field objectives.

Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING for authoritative changing-water/terrain and semantic reinspection playback.

Reduced form: READY. The flood has ended. Keep unstable scopes inaccessible. Use dry static reviewed approach geometry. The land discrepancy remains outside BattleSpec and continues through Cartography and any canon-authored land-record process after combat.

## PTU / Caelo boundary

The internal source scan supports campaign/world-state play and exact authored environmental mechanics when a governing source defines the effect. Toxic Ravine remains the known project example of a location-specific environmental mechanic.

That precedent does not create property, survey or boundary mechanics.

Remain UNKNOWN without exact governing evidence:
- universal property ownership or transfer rules;
- land title/deed/registry mechanics;
- survey-specific Skill DCs;
- exact-boundary discovery checks;
- automatic access-right determination by Skill Check;
- universal trespass mechanics;
- survey-marker or fence object HP;
- physical marker movement changing a legal boundary;
- river/shoreline movement automatically changing recorded land geometry;
- Pokémon species sensing human parcel lines;
- Ground, Rock or Steel Type conferring survey/legal competence;
- Dig, Earthquake, Bulldoze, Strength or another Move creating or validating a land boundary;
- Abilities or Items that authenticate land records;
- Trainer Features granting universal land authority.

If a future canon source establishes a regional rule, implement that exact rule and classify its engine dependencies separately.

## Existing narrative-system boundary

Homes/Housing owns residence and household state and already states that residence does not prove ownership.

Cartography owns surveys, map editions, map geometry claims and corrections.

Ranching and Conservation own operational stewardship within their domains.

Travel/Roads own route existence, condition and journey execution.

Civic Governance owns public proposals and decisions only through authored mandates.

Adjudication owns deciding-process lineage only when canon establishes jurisdiction, scope and available outcomes.

Archives/Public Notices own record custody/publication.

Pass 126 links these records through stable land identity and provenance. It does not replace any owner system.

## Minecraft/Cobblemon boundary

Minecraft/Cobblemon may render:
- fences, walls, hedges, ditches and gates;
- survey posts and markers;
- field equipment;
- old/new map displays;
- ranch or reserve visual divisions;
- roads, paths and crossings;
- construction changes;
- individual Pokémon routines around those features.

All of those are presentation or overworld observations.

Block coordinates do not automatically become cadastral truth. A fence block does not establish a boundary. Breaking or replacing it does not transfer ownership. Chunk claims do not create Ouros canon. Standing inside a polygon does not create occupancy permission. A sign does not create an access right. A Pokémon crossing a line does not alter human land records. Cobblemon BattleState remains outside land identity, claims, survey conclusions, record revisions, access rights and adjudication.

## Current implementation-safe pattern

For any land/boundary scene with unsupported tactical complexity:
1. resolve map, survey, claim and institutional facts in Ouros world state;
2. preserve each source and version explicitly;
3. complete staff/civilian withdrawal and secure records/equipment before BattleSpec creation;
4. select explicit combatants in Ouros;
5. use static reviewed geometry with no inferred property or environmental mechanics;
6. let AutoPTU resolve only supported battle facts;
7. use the adapter only to present authoritative state/events;
8. return to Cartography or the canon-authored authority for survey acceptance, record update, access decisions or claim review.

## Unresolved mechanical questions

- Are any exact PTU/Caelo Skills intended to resolve field surveying, and what are their bounded consequences?
- Are there governed rules for protecting/carrying survey equipment during combat?
- Which exact forced-movement/reaction contracts are required for withdrawal or corridor encounters?
- How should objective-aware AI represent PROTECT, WITHDRAW and CLEAR_ROUTE?
- What semantic adapter events are required for survey-team withdrawal, route closure and later reinspection?
- If a future location defines mud/current/unstable-bank effects, which exact terrain/hazard lifecycle owns them?

## Unresolved canon questions

- Do Ouros regions maintain formal land-unit records, and what are their local names?
- Which institutions can record ownership, stewardship, access, maintenance or operational interests?
- Which records are public, private or protected?
- How are older approximate maps treated?
- What process, if any, changes a record after a new survey?
- Do river, shoreline, road or disaster changes affect recorded boundaries, and under which regional rule?
- What arrangements govern ranches, reserves, sacred sites, League facilities and public corridors?
- Which disputes have an authored review/adjudication route?
- Which individual Pokémon have documented trained surveying or field-support roles without species-wide inference?

## Readiness result

Land-unit identity/provenance continuity: READY.

Map/survey/physical-marker discrepancy tracking: READY.

Neutral claim/interests linking: READY only when canon supplies the interest type/source.

Cross-system handoffs: READY.

Provenance mysteries and static historical exploration: READY.

Reduced Survey Marker Recovery Perimeter: READY.

Reduced Access Corridor Diversion: READY.

Reduced Flood-Shifted Fence Reinspection: READY.

Full forms remain PARTIAL/BLOCKING wherever complete movement, staged lifecycle, environmental zones/reactions, objective-aware tactical policy, object interaction or semantic adapter playback are required.
