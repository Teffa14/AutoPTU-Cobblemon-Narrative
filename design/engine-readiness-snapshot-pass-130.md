# Engine Readiness Snapshot — Pass 130

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-23
Narrative topic: Libraries, Lending, and Public Knowledge

This snapshot records live read-only evidence used when classifying encounter dependencies introduced in Pass 130. It does not modify AutoPTU-Java or AutoPTU.

## Inspected revisions

### AutoPTU-Java

Repository: `Teffa14/AutoPTU-Java`
Inspected `main`: `7de79dcd30b241d439724050fb24ee893a7c5c63`
Commit date: 2026-08-23
Latest inspected commit: `Freeze forced movement instruction contract (#160)`

Observed evidence:

- Java defines a language-neutral `ForcedMovementInstruction` with PUSH/PULL and distance.
- The contract extracts forced-movement intent from PTU move metadata with oracle fixtures/parity coverage.
- The Java source explicitly states that the contract does not move a combatant.
- Later spatial resolution is still required to execute displacement authoritatively.

Interpretation:

This is real evidence for parsing/identifying a forced-movement instruction inside move-specific behavior. It is not evidence that complete movement exists.

Do not promote:

- Push execution;
- Pull execution;
- collision handling;
- obstacle resolution;
- edge/fall handling;
- occupied-tile handling;
- interception;
- knockback chains;
- forced-movement reactions;
- movement-triggered hazards;
- objective-aware movement.

### AutoPTU Python

Repository: `Teffa14/AutoPTU`
Inspected `main`: `99ba07ea47b8896d96bd37f6c06cffb8695f69bb`
Commit date: 2026-08-23
Latest inspected commit: `test(career): lock capture overflow to PC (#68)`

Observed evidence:

- Career regression coverage proves a seventh owned Pokémon can overflow to PC without replacing the active six.
- The test verifies Poké Ball consumption and authoritative capture event recording.

Interpretation:

This is meaningful Career/persistence evidence. It does not change the battle-engine tactical capability classifications used by the narrative project.

## Permanent capability map

### VERIFIED

#### targeting / footprints / range / LoS

Evidence remains sufficient for the project's existing VERIFIED classification for static battle targeting geometry.

Non-inference:

A verified geometric LoS system does not prove library visibility, shelf-search rules, crowd navigation, radio propagation, darkness perception, or knowledge access.

#### base movement legality

Evidence remains sufficient for ordinary static legal movement.

Non-inference:

Static legal Shift validation does not prove escort, evacuation, civilian routing, dynamic chokepoints, or forced displacement.

#### core calculations

Existing verified calculation slices remain intact.

No Pass 130 library concept creates a new calculation rule.

#### action economy / initiative

Existing initiative/action-economy evidence remains VERIFIED.

Library patrons, staff, carts, books, or vehicles do not gain initiative merely because they appear in a battle scene.

#### AI legal-action infrastructure

Existing infrastructure can constrain an AI to legal actions.

It does not prove the AI understands why it should evacuate, protect a route, withdraw, or avoid civilians.

### PARTIAL

#### full turn / round lifecycle

Java has substantial lifecycle slices, but the complete family is not proven.

Pass 130 rule:

A library encounter using only conventional turns can operate within a frozen static battle. Any scenario requiring sophisticated phase events, delayed environmental progression, interrupts, or complete transcript parity stays behind this category or the environment/reactions category as appropriate.

#### full stateful damage pipeline

Substantial stateful-damage behavior exists, but the family remains PARTIAL.

No bookcase, water leak, glass panel, vehicle, or collection object receives improvised damage rules from narrative description.

#### status lifecycle

Status prevention/application/removal has multiple parity-backed slices, but the complete controller remains incomplete.

Pass 130 does not introduce:

- wet-book status;
- panic status;
- smoke status;
- knowledge status;
- confusion from reading;
- fatigue from study;
- environmental Poisoned/Burned from library incidents.

#### move-specific behavior

Many move-specific contracts exist and forced-movement instruction parsing adds evidence, but the complete Move catalog is not verified.

The presence of a Push/Pull parser does not mean every Push/Pull Move can execute displacement.

#### abilities

Many Ability families have parity evidence, but catalog completeness remains unproven.

No Pokémon gets a generic librarian, translator, catalog, shelving, research, or retrieval Ability because of species flavor.

#### items

Item support remains partial.

A library copy is not a PTU Item merely because Minecraft renders it as a book object.

#### Trainer Features / perks

Generic prerequisite/context/frequency/resource/bookkeeping/effect infrastructure has progressed in prior passes, but the catalog remains partial.

Library employment, research experience, reading habits, or ownership of manuals do not grant Features.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

Status: BLOCKING.

New evidence at Java head freezes an instruction only. It does not apply spatial displacement.

Pass 130 implications:

- moving civilians through a flooded annex;
- protecting a mobile-library route;
- interception around an escort;
- pushing/pulling actors out of danger;
- dynamic withdrawal lanes;
- crowd separation;
- movement of semantic objectives

remain blocked in their full versions.

#### terrain / weather / hazards / zones / reactions

Status: BLOCKING.

Pass 130 implications:

A flooded annex cannot gain tactical rising-water rules merely because Freshwater/Stormwater world state says water is present. Wet flooring cannot become Rough Terrain. Shelves cannot create cover rules unless the battle snapshot and PTU rules explicitly support them. Glass, fire, smoke, collapsing stacks, or water zones cannot be improvised by the adapter.

#### AI tactical policy

Status: BLOCKING.

Legal-action infrastructure does not prove goals such as:

- `EVACUATE`
- `WITHDRAW`
- `REACH_EXIT`
- `PROTECT_ROUTE`
- `CLEAR_ROUTE`
- `AVOID_CIVILIANS`
- `PROTECT_VEHICLE`

Therefore full library evacuation/escort encounters remain blocked.

#### Minecraft / Cobblemon / Craftics adapter and playback

Status: BLOCKING.

The adapter must eventually render semantic objectives and events without deciding rules.

Pass 130 adds another explicit authority boundary:

Minecraft shelves, lecterns, chests, books, signs, doors, catalog terminals, and mobile-library builds are presentation/state projections. They must not become the authoritative library catalog or lending ledger.

## Pass 130 overworld blockers

These are outside the battle core and belong to future world-state implementation:

- `LIBRARY_SYSTEM_STATE`
- `BIBLIOGRAPHIC_WORK_IDENTITY`
- `CONTENT_EXPRESSION_HISTORY`
- `PUBLICATION_EDITION_HISTORY`
- `LIBRARY_COPY_IDENTITY`
- `HOLDINGS_RECONCILIATION`
- `CIRCULATION_LEDGER`
- `PATRON_PRIVACY_SCOPE`
- `HOLD_REQUEST_STATE`
- `RESOURCE_SHARING_REQUEST_STATE`
- `REFERENCE_REQUEST_HISTORY`
- `MOBILE_LIBRARY_ROUTE_STATE`
- `SENSITIVE_ACCESS_SCOPE`
- `LIBRARY_TO_POSTAL_HANDOFF`
- `LIBRARY_TO_DIGITAL_ACCESS_HANDOFF`
- `LIBRARY_TO_ARCHIVE_OR_MUSEUM_HANDOFF`
- `LIBRARY_TO_MINECRAFT_PROJECTION`

None belongs inside AutoPTU-Java.

## Encounter dependency matrix

### `LIB-130-A — Flooded Reading Annex Evacuation`

Narrative objective:

Protect people/Pokémon first, preserve access to significant collection material where feasible, and restore service after the incident.

FULL dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL if phase progression matters
- full stateful damage — PARTIAL if ordinary attacks occur; no environmental object-damage inference
- status lifecycle — PARTIAL only for real PTU statuses
- terrain/weather/hazards/zones/reactions — BLOCKING if rising water is tactical
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

REDUCED readiness:

Narrative premise is implementable using world-state flood/evacuation plus a static legal battle snapshot. No dynamic environmental mechanics required.

### `LIB-130-B — Mobile Library Chokepoint`

FULL dependencies:

- complete movement — BLOCKING for escort/route-clearing actors
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING
- terrain/environment family — only if a real tactical hazard is included
- ordinary static combat foundations — usable under existing VERIFIED/PARTIAL boundaries

REDUCED readiness:

Vehicle/staff remain out of grid. Resolve a static confrontation at the chokepoint. Reopen route in overworld state afterward.

### `LIB-130-C — Reading Courtyard Wildlife Intrusion`

FULL dependencies:

- complete movement — BLOCKING
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

REDUCED readiness:

Patrons evacuate in world state. Wildlife receives an overworld withdrawal path. Only an unavoidable residual confrontation enters AutoPTU.

### `LIB-130-D — Reference Desk Misinformation`

Battle dependency: NONE.

This concept should remain non-combat and can be implemented entirely through reference/catalog/world-state interactions.

## Specific non-inferences added by Pass 130

Do not infer:

- `book present` → content true;
- `book borrowed` → content read;
- `book read` → content believed;
- `field guide owned` → Pokémon Education rank;
- `battle manual owned` → Move/Feature/Ability access;
- `library worker` → Researcher or other Trainer Class;
- `library card` → credential outside library scope;
- `open door in Minecraft` → authorized special-collection access;
- `book block destroyed` → work destroyed;
- `catalog outage` → holdings disappeared;
- `missing scan` → theft;
- `annotation` → authored text;
- `old edition` → false in every respect;
- `new edition` → retroactive overwrite of earlier knowledge;
- `digital scan` → duplicate unique physical copy;
- `specific copy` → PTU Item unless an explicit mapping exists;
- `shelf geometry` → battle cover or terrain;
- `flooded room` → Water Terrain, damage, Slowed, Tripped, forced movement, or drowning.

## PTU/Caelo validation status

Public PTU resources confirm PTU 1.05 remains the downloadable rules baseline and explicitly recommend learning the rules instead of blindly trusting automated sheets.

The named primary Caelo corpus was not recovered reliably during this run from the accessible File Library search. Therefore no new Caelo rule is asserted for:

- books;
- reading;
- libraries;
- literacy;
- research material;
- General Education;
- Pokémon Education;
- library tools;
- study time;
- reference work.

Super PTU Online Helper was not exposed as an invocable tool. No result is fabricated.

## Capability conclusion

Pass 130 does not justify any permanent-category promotion.

The correct live classification remains:

VERIFIED:

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

PARTIAL:

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

BLOCKING:

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter / playback

The new forced-movement instruction contract is evidence of progress inside move parsing. It is not movement execution.