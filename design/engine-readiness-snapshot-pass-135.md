# Engine Readiness Snapshot — Pass 135

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-29

This snapshot records live implementation evidence checked while adding public-library circulation, access and service continuity.

AutoPTU-Java and AutoPTU were inspected read-only. This pass writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Narrative repository inspection

Narrative head before Pass 135:

`fb4391c9ed6d8fec05ed1588029412d772642a44`

The recursive tree and root directories were inspected before topic selection. Targeted searches checked for dedicated public-library circulation, lending, holds, branch service, Canalave, Malie and Nacrene material.

Adjacent design checked directly included:

- `design/archives-museums-collections-preservation-layer.md`
- recent engine-readiness snapshots
- repository inventory for courier/logistics, formal education, accessibility, communications, public space, construction and maintenance

The selected gap is ordinary public-library access-service continuity. Existing Archives/Museums remains owner of collection provenance, archival holdings, conservation, restricted access and institutional collection loans.

## AutoPTU-Java live evidence

Current head inspected:

`106dd1010eeec7ec2423688ed5eeec2274ae8d18`

Commit:

`Freeze terrain skill-check helper closure`

This is newer than the head recorded in Pass 134.

## Concrete new evidence

The commit extends `tools/python/export_intercept_check_contract.py`.

The exporter now builds a local function index and walks the closure of local helpers called from the pinned `_terrain_skill_check_bonus` root.

For each reachable local helper it records:

- helper name;
- normalized source;
- called-function names;
- string literals;
- integer literals.

This strengthens the oracle contract for the specific terrain skill-check path used by the current Intercept parity surface. It reduces the chance that semantic changes hidden in helper functions escape the exported contract.

## What the new evidence does not establish

This commit is contract-freezing/tooling evidence around one existing path.

It does not by itself prove:

- generalized terrain state;
- terrain creation or removal;
- weather lifecycle;
- hazards;
- changing zones;
- generalized reactions;
- competing reaction ordering;
- environmental forced movement;
- broad Push/Pull/Knockback coverage;
- every Intercept window;
- escort objective semantics;
- protected civilian semantics;
- library objective semantics;
- tactical AI understanding of terrain or objectives;
- Minecraft/Cobblemon/Craftics semantic playback.

No permanent capability category is promoted from this evidence.

## Intercept evidence retained

The localized Intercept route continues to provide evidence for:

- PRE-target integration in the implemented route;
- interceptor movement in that sequence;
- effective-defender replacement in that sequence;
- server-owned Acrobatics/Athletics inputs;
- server-owned Coaching state;
- server-owned exact `Justified [Errata]` presence;
- pinned exact Justified bonus;
- pinned `_terrain_skill_check_bonus` contract;
- now the local helper closure used by that terrain skill-check contract.

This remains representative-path evidence only.

## AutoPTU live evidence

Current head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer AutoPTU commit was present during this run.

The change remains presentation-only. It synchronizes cached Pixi screen dimensions after viewport resize so later sprite destinations use current renderer geometry.

It does not establish:

- library service-state playback;
- branch opening authority;
- hold or checkout authority;
- return/check-in semantics;
- catalog authority;
- patron identity authority;
- custody/ownership authority;
- combatant-selection authority;
- legality authority;
- HP/status authority;
- narrative consequence authority.

## Permanent capability map — Pass 135

No category receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

Baseline targeting and spatial legality remain sufficient for conventional reduced encounters on static geometry.

`base movement legality`

Basic movement remains verified for conventional static BattleSpecs.

`core calculations`

Previously established parity-backed calculation infrastructure remains verified at the existing baseline.

`action economy/initiative`

Baseline action economy and initiative remain verified.

`AI legal-action infrastructure`

Legal-action enumeration and validation remain verified at the established baseline. This does not provide tactical objective policy.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

The Intercept path has stronger frozen contract evidence, but broad Push, Pull, Knockback, every forced-movement source, escort semantics, environmental displacement and generalized movement reactions remain incomplete as a family.

`full turn/round lifecycle`

Ordinary progression exists. Staged branch withdrawal, timed evacuation, escort windows and objective phases are not established as a generalized contract.

`full stateful damage pipeline`

Substantial implemented behavior exists, but the permanent family remains partial.

`status lifecycle`

Existing implemented statuses do not authorize invented panic, confusion-from-information, smoke, dust, stress, crowd, research or service-disruption statuses.

`move-specific behavior`

Representative Move implementations do not prove complete coverage.

`abilities`

Representative Ability behavior and Intercept-specific Justified evidence do not prove the entire family.

No Ability creates a hold, checkout, access right, catalog truth, ownership or library authority.

`items`

Items remain partial.

A book, library card, routing crate, catalog terminal or returned item does not receive tactical effects unless governed by exact rules.

`Trainer Features/perks`

Exact PTU Features remain source-governed. A research scene or successful library search does not automatically grant a Feature, Edge, Skill Rank, Move or Trainer Level.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

The frozen helper closure strengthens one specific Intercept terrain skill-check contract. It does not verify generalized terrain, hazards, zones or reactions.

Rich library encounters involving protected exits, collapsing shelving, smoke, water intrusion, dynamic obstruction or reaction windows therefore remain blocked on this family.

`AI tactical policy`

Rich variants need objective-aware behavior such as:

- PROTECT;
- WITHDRAW;
- CLEAR_ROUTE;
- HOLD_POSITION;
- avoid protected areas;
- prioritize an exit or objective rather than raw attack value.

Legal-action infrastructure does not provide this policy.

`Minecraft/Cobblemon/Craftics adapter/playback support`

Current rendering evidence does not provide semantic projection of:

- branch service scopes;
- hold state;
- checkout/return state;
- transfer state;
- reading-room state;
- patron access;
- catalog freshness;
- library recovery checkpoints;
- tactical-to-world consequence handoff.

This category remains BLOCKING.

## Encounter review — Branch Closing-Time Withdrawal

Full intended objective:

A routine library closing is interrupted by a separate tactical incident while visitors and staff are still withdrawing from public areas.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL if attacks occur
- status lifecycle — PARTIAL for ordinary legal statuses only
- terrain/weather/hazards/zones/reactions — BLOCKING for protected exits, dynamic obstacles or generalized reactions
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full version status:

BLOCKED FOR RICH SEMANTICS.

Reduced version status:

READY.

Reduced world-state contract:

1. Library Service closes or pauses the affected public scope before BattleSpec creation.
2. Visitors, staff, records, carts, circulating material and noncombatant Pokémon leave the tactical grid.
3. Ouros selects explicit legal combatants.
4. AutoPTU receives static reviewed geometry.
5. Tactical resolution determines immediate physical access only.
6. Library Service separately records whether closing, check-in, security or later reopening completes.

Forbidden automatic transitions:

- victory => branch secured
- victory => all visitors accounted for
- victory => all material safe
- victory => return processed
- victory => hold ready
- victory => branch reopened

## Encounter review — Transfer Crate Chokepoint

Full intended objective:

A branch-transfer shipment is paused near a loading route while a tactical incident blocks movement.

Rich dependencies:

- complete movement — PARTIAL for escort/Intercept/forced movement
- full lifecycle — PARTIAL for timed withdrawal or transfer windows
- terrain/hazards/zones/reactions — BLOCKING for protected cargo zones or changing route state
- AI tactical policy — BLOCKING for protect/withdraw/clear-route behavior
- adapter/playback — BLOCKING

Reduced version status:

READY.

Reduced contract:

1. Transfer shipment stops before combat.
2. Crates, courier, receiving staff and transfer records stay outside BattleSpec.
3. AutoPTU resolves a conventional static encounter.
4. Courier/Logistics and Library Service evaluate dispatch, delivery and receipt afterward.

Victory never establishes:

- copy identity;
- original-object identity;
- ownership;
- authenticity;
- shipment delivery;
- library receipt;
- hold fulfillment.

## Encounter review — Temporary Reading-Room Access Perimeter

Full intended objective:

A temporary service point must suspend public access while a nearby tactical threat is cleared.

Rich dependencies:

- complete movement — PARTIAL for escort/Intercept
- lifecycle — PARTIAL for staged withdrawal
- terrain/hazards/zones/reactions — BLOCKING for protected public-service zones
- tactical AI — BLOCKING
- semantic adapter/playback — BLOCKING

Reduced version status:

READY.

Reduced contract:

1. Reading-room access pauses in world state.
2. Readers, staff, requested materials and noncombatant Pokémon leave BattleSpec.
3. Ouros provides static geometry and explicit combatants.
4. AutoPTU resolves conventional combat.
5. The responsible library owner later decides whether the temporary service point reopens.

Victory never establishes:

- access permission;
- research success;
- source authenticity;
- knowledge gain;
- service restoration;
- membership or account standing.

## PTU/Caelo unresolved mechanics

The following remain UNKNOWN unless a governing source and exact implementation contract are located:

- universal library-search checks;
- General Education DCs for finding or understanding sources;
- automatic Researcher or Scholar bonuses in library scenes;
- reading-time rules;
- memory checks;
- translation checks for arbitrary texts;
- misinformation detection;
- automatic Skill Rank increases through study;
- automatic Edges/Features from research;
- Move learning from books outside exact tutor/manual rules;
- battle bonuses from reading rooms, shelves or books;
- shelf-cover rules;
- falling-shelf damage;
- smoke or water hazards in library spaces;
- protected-civilian reactions;
- escort actions;
- book/crate HP;
- universal lifting/carrying of collection material;
- librarian profession mechanics;
- species-derived research competence;
- Psychic/Telepathy-based automatic source reading or authentication;
- Trainer Features that create institutional authority.

## Minecraft/Cobblemon authority boundary

Minecraft/Cobblemon may present world facts already decided by Ouros:

- branch signage;
- open or closed service desks;
- stacks;
- pickup areas;
- return carts;
- routing crates;
- temporary counters;
- mobile library stops;
- NPC schedules;
- old labels;
- renovation barriers;
- Pokémon routines.

Minecraft block/entity state does not decide:

- library membership;
- access permission;
- copy availability;
- hold assignment;
- checkout;
- return completion;
- authenticity;
- authorship;
- source truth;
- reading comprehension;
- ownership;
- custody beyond authored world state.

Cobblemon BattleState remains outside authority for combatant selection, legality, HP/status, tactical positions and narrative outcome.

## Canon questions left open

- Which regions have public-library systems?
- Which institutions operate them?
- Which services circulate material?
- What membership/access rules exist, if any?
- What data is retained about readers or borrowing?
- How are privacy and record access handled?
- Which catalogs are digital, paper, hybrid or otherwise?
- Which regions use mobile services?
- How do remote communities request material?
- What resource-sharing networks exist?
- How do libraries coordinate with Archives, schools, League institutions or research bodies?
- Which buildings were reused from earlier civic, transport, school or battle functions?
- Which historical service disruptions remain visible in present-day routines?
- Which named Pokémon have canon-authored roles around library service?

No answer is silently canonized by Pass 135.

## Pass 135 readiness conclusion

The public-library layer is implementation-safe at the world-state level now.

Its three reduced encounter variants are READY because they deliberately remove service-state transitions, civilians, records, circulating material and noncombatant Pokémon from BattleSpec before conventional combat begins.

Rich tactical variants remain blocked by the same permanent families as before. The new AutoPTU-Java helper-closure contract strengthens evidence for one Intercept-related terrain skill-check path, but it does not change the family-level classification.