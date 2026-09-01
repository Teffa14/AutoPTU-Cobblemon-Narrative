# Marea Temporary Visitor / Hosting Seeds — Pass 193

Status: PROPOSED / NOT CANON
Date: 2026-09-01
Depends on: `design/temporary-visitor-hosting-continuity-layer.md`

These candidates reuse current Marea places and residents. No named external settlement, hotel, lodging proprietor, room count, price, immigration authority, or visitor law is established here.

## 1. Room Held, Ferry Delayed

A temporary visitor is expected in Puerto Bruma and a boarding room has been held. Lia records that the relevant ferry movement is delayed.

Playable work:

- distinguish expected arrival from observed arrival;
- decide whether the room hold remains active under the local arrangement;
- update Ivo only with the guest-count information he actually needs for meal planning;
- avoid marking the person missing because they never arrived.

No battle.

Best first implementation candidate because it exercises transport, capacity, information scope, and autonomous schedule change with minimal new canon.

## 2. A Familiar Traveler Returns

A repeat traveler appears again after a prior stay.

The visitor remembers an earlier local contact, but their purpose this time is different. Old relationship history persists while access and current plans are revalidated.

Core test:

`REPEAT_VISITOR != SAME_VISIT_STATE`.

## 3. The Visitor Who Never Checked In

A traveler was listed as expected but chooses another arrangement before reaching the assigned room. The room record must become cancelled/no-show only after evidence supports that state.

Do not create a search merely from an unused bed.

## 4. Visiting Researcher, Narrow Access

An outside researcher asks to consult Tideglass material and later visit Mirador.

Taro can authorize a specific archive surface. Nerea separately decides whether any station activity is open to the visitor. Approval at one institution does not propagate to the other.

The visitor may contribute an attributed claim about another region, but the claim does not create new regional canon.

## 5. A Trainer in the Gallery

A visiting Trainer spends an afternoon at Bruma Battle Yard.

Jace wants to test them. Sela has scheduled work and may decline or defer a match. The guest can observe a session without receiving ranking, rivalry, membership, or guaranteed challenge rights.

Optional later battle only through an audited challenge contract.

## 6. Guest Pokémon Needs a Different Plan

A visiting Trainer expects a particular activity with their companion Pokémon. The Pokémon shows authored/observed discomfort with the proposed arrangement.

The local response is to adjust the plan or ask better questions. No species stereotype and no universal 'happiness' score is used.

This seed can connect Ivo, Oren, Mara, or another relevant resident depending on the actual need without creating a new hospitality NPC.

## 7. Departure Extended by Route Conditions

A visitor plans to leave by a specific connection, but current transport or route conditions change the viable window.

The extension affects room use and local scheduling. It does not imply residency, emergency, or wrongdoing.

If a later incident makes safe travel uncertain, preparedness/search/access layers own those decisions.

## 8. Something Left in the Room

After confirmed departure, an object remains in the previously assigned space.

Hosting supplies the occupancy history. Salvage/found-property continuity owns custody and provenance. The next guest does not inherit the object.

No assumption is made about whether it was forgotten, abandoned, planted, or intentionally left for someone.

## 9. Two Visitors, One Remaining Slot

Two proposed arrivals overlap with one locally available assignment slot in the currently modeled slice.

The narrative tension is mundane prioritization and communication. The implementation must not invent a universal lodging entitlement or pricing auction.

A cancellation, alternate local arrangement, changed timing, or transport delay may resolve it without player intervention.

## 10. Visitor as Source, Not Truth

A traveler tells Mara that another coastal area has seen unusual Pokémon behavior.

Mara can record the report and perhaps compare it with local observations. The claim stays attributed. It cannot spawn a new ecology state, species migration, emergency, or named outside location without later evidence/canon.

## 11. The Visit Happens Without the Player

A guest arrives, stays, completes an ordinary purpose, and leaves while the player is elsewhere.

On return, the player may find legitimate aftermath:

- Lia's arrival/departure record;
- an archive request completed through normal authority;
- a message left with Pia;
- a changed room assignment state;
- a resident mentioning the contact if they actually participated.

This proves that visitors belong to world continuity rather than player-triggered spawn logic.

## 12. Companion and Trainer Leave at Different Times

A legitimate situation causes a Trainer and companion Pokémon to have temporarily different confirmed locations near departure.

The system first checks expected arrangements and last confirmed contact. It does not classify theft, abandonment, transfer, or missing status automatically.

If verification fails and concern becomes justified, field-search continuity can open a case.

## Longer arc — People Who Pass Through Bruma

Over multiple visits, Puerto Bruma slowly accumulates outward-facing social history without requiring immediate expansion of the regional map.

Possible persistent effects:

- known repeat visitors;
- older room-assignment records;
- corrected travel claims;
- archived correspondence;
- relationships that continue across absences;
- visitors who return and notice local changes;
- residents who adjust routines based on actual prior hosting experience.

The arc should not converge on a single visitor reputation meter. Each person keeps their own history and each institution retains separate authority.

## Rich encounter — Guest Route Check at Glass Bend

### Narrative premise

A temporary visitor has a legitimate reason to travel a known segment of Sendero del Vidrio with local guidance. Wild activity creates an immediate safety problem during the movement.

The visitor's identity, purpose, stay state, belongings, route plan, and local host remain Narrative-owned.

### Intended full version

If implemented as a spatial protective/withdrawal encounter, it may require:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including interception, push/pull/knockback and other forced movement if those effects are present;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle for selected content;
- terrain/weather/hazards/zones/reactions if trail conditions are tactical;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy for objective-aware withdrawal/protection;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Disposition under pass-193 evidence: FULL VERSION BLOCKED.

### Reduced runnable form

1. Narrative owns the visitor's route position and resolves withdrawal to a safe non-BattleSpec state.
2. Luggage, lodging, guest access, companion custody, and route purpose never become battle objectives.
3. If an immediate wild threat still prevents passage, assemble a separate ordinary audited battle on stable geometry.
4. Use only roster content covered by current verified/accepted contracts.
5. Permit a narrow handoff such as `IMMEDIATE_ROUTE_THREAT_WITHDREW` or `IMMEDIATE_PASSAGE_CLEAR`.
6. Narrative decides whether the visitor continues, returns, delays departure, or changes plans.

Battle victory cannot grant residency, lodging rights, relationship improvement, institutional access, outside-world truth, ownership of the guest's property, or authority over the guest Pokémon.

## Recommended implementation order

First candidate: `Room Held, Ferry Delayed`.

Second: `A Familiar Traveler Returns` after a stable visitor identity record exists.

Third: `Visiting Researcher, Narrow Access` to test cross-institution permission boundaries.

The rich Glass Bend encounter should remain reduced until its exact tactical dependency families are verified end to end.