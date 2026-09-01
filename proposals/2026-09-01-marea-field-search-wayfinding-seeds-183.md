# Marea field-search and wayfinding seeds 183

Status: PROPOSALS / NOT CANON
Date: 2026-09-01

These candidates use only already-canonized Marea places and residents where possible. Any new procedure, historical incident, object, route practice or authority remains proposed until promoted explicitly.

## 1. The Walker Who Returned Another Way

Premise: a routine arrival expectation at Loma Clara is missed. Mara receives the concern at the Field Office. Lia can eliminate a ferry explanation, while a route witness remembers seeing the traveler earlier than first reported.

The search never needs a villain. Before the player reaches the upper route, the traveler returns safely to Puerto Bruma after abandoning the planned journey and failing to communicate the change.

Useful consequences:

- the case teaches that overdue does not equal endangered;
- the player must update people already searching rather than simply complete a quest objective;
- Taro can preserve the corrected timeline without erasing the initial report;
- Mara may propose a future check-in procedure, but that procedure is not canon until separately approved.

Engine dependency: none beyond ordinary RPG world interaction.

Recommended first implementation because it validates the whole epistemic loop without battle.

## 2. Found Equipment, Unknown Owner Status

Premise: a field instrument or ordinary travel item is found near the lower shelf. Its appearance makes several residents think they know who left it.

The player traces custody and recent use through Teo, Ema and/or Nerea. The item may belong to the expected traveler, have been borrowed earlier, or be unrelated to the active concern.

Rule exercised:

`OBJECT_FOUND != SUBJECT_LOCATION_PROVED`

The item remains a provenance object even after the search case resolves.

Engine dependency: none if handled as server-owned quest object and dialogue/evidence state.

## 3. Two Search Teams, One Old Map

Premise: Tideglass holds an older map edition whose route annotation differs from the current fixed route anchors. One searcher interprets the annotation as a still-usable branch; another treats it as historical only.

Taro and Pia can establish the map's edition and provenance. Mara/Teo can establish current physical accessibility. The quest resolves the operational disagreement without requiring the archive to declare why the old route changed unless evidence exists.

Rule exercised:

`HISTORICAL_MAP_ACCURATE_FOR_ITS_EDITION != CURRENT_ROUTE_VALID`

Engine dependency: none.

Canon risk: do not create a new physical alternate trail until the canonical map is intentionally extended.

## 4. Three Flags from the Same Morning

Premise: three temporary field markers appear along a Mirador transect during the same morning. The markers are real, but their placement times and purpose are initially unclear.

Ema's preparation notes, Nerea's observation window and Teo's equipment servicing record can bound when each marker could have been placed. The player reconstructs a time interval rather than receiving a hidden coordinate.

Possible outcome: the markers narrow a search sector but never establish who placed them.

Rule exercised:

`TIME_BOUND != IDENTITY_PROOF`

Engine dependency: none.

## 5. Margin's Repeated Turn

Premise: while Taro and Pia review an overdue courier concern near Tideglass, Margin the Noctowl repeatedly turns attention toward the same direction during separate moments.

This produces an observation. It may justify checking a nearby route surface. It does not establish a universal Noctowl tracking ability, telepathy, intent or a missing person's location.

If later PTU/Caelo evidence supports a relevant Capability, the mechanical layer may upgrade what this behavior can author. Until then it stays soft evidence.

Engine dependency: none for the observational version.

## 6. Mirador Timing Window

Premise: Nerea and Ema's ordinary observation records show when a route-side area was under active observation and when nobody was looking there.

A witness says an overdue person passed during the morning. The Mirador record cannot prove passage, but it can challenge an impossible timestamp or reduce the credible window.

This composes the phenology/observation architecture with search work and gives routine science an operational role without turning Mirador into surveillance.

Rule exercised:

`NOT_OBSERVED_DURING_WINDOW != ABSENT`

Engine dependency: none.

## 7. The Check-In That Never Arrived

Premise: the expected traveler completed the route safely, but the message confirming arrival never propagated to Mara. The concern becomes visible because Field Office, destination and courier/ferry communication states disagree.

The player can discover the mismatch through normal communications provenance. The useful consequence is procedural: future cases can distinguish COMMUNICATION_UNCONFIRMED from PERSON_UNACCOUNTED_FOR when evidence allows.

This proposal should reuse the existing communication/delivery layer rather than introduce a new message system.

Engine dependency: none.

## 8. Search Paused at the Crossing

Premise: a search reaches the seasonal crossing while an existing closure or unsafe route state prevents further movement. Some residents want to continue immediately because the case feels urgent.

The player helps preserve operational discipline: evidence can be gathered, another contact route can be checked and the case can remain active without authorizing unsafe traversal.

Rule exercised:

`SEARCH_URGENCY != ACCESS_OVERRIDE`

Engine dependency: none for the reduced form. Any attempt to model dynamic crossing hazards tactically invokes the terrain/weather/hazards/zones/reactions family and remains blocked until verified.

## 9. Found, But Not Ready to Walk

Premise: the subject is contacted near an existing route anchor and can communicate, but ordinary return travel is not immediately appropriate.

The narrative question changes from WHERE to WHAT ASSISTANCE IS AUTHORIZED. Mara owns field coordination; Oren owns actual care within verified scope; Mina/Lia may contribute transport only where ferry operations plausibly apply.

The player does not receive a generic healing mini-game from this proposal.

Rule exercised:

`SUBJECT_FOUND != SUBJECT_SAFE_TO_TRAVEL`

Engine dependency: no battle required. Care mechanics require separate PTU validation before mechanical effects are authored.

## 10. The Upper Bend Search

Premise: an overdue field traveler was last reliably seen beyond the lower shelf. Search evidence narrows the concern toward the upper section. Wild activity and route conditions can complicate access.

### Intended full version

The scene can support searchers, a located-but-vulnerable subject, objective-aware wild actors, unstable terrain and a protection/withdrawal problem.

Dependencies:

- targeting/footprints/range/LoS: required;
- base movement legality: required;
- complete movement including push/pull/knockback/interception/forced movement: required for tactical protection/displacement;
- core calculations: required;
- action economy/initiative: required;
- full turn/round lifecycle: required;
- full stateful damage pipeline: required;
- status lifecycle: roster dependent, required if selected content applies statuses;
- terrain/weather/hazards/zones/reactions: required for tactical route instability or weather pressure;
- move-specific behavior: exact audit required;
- abilities: exact audit required;
- items: exact audit required;
- Trainer Features/perks: exact audit required;
- AI legal-action infrastructure: required;
- AI tactical policy: required for escort/protection/withdrawal intent;
- Minecraft/Cobblemon/Craftics adapter/playback support: required for faithful full projection.

Current disposition: BLOCKED as a full encounter.

### Reduced version

The search sectors, clues and subject contact remain outside BattleSpec. The subject and searchers are moved to or kept in a safe world-state location before combat authority begins.

If wild hostility blocks the immediate exit, run one ordinary audited battle on stable terrain with a roster selected to avoid unsupported forced movement, weather phases, hazard zones, complex statuses and unverified interrupts.

Allowed handoff:

`IMMEDIATE_WILD_THREAT_WITHDREW`

or

`IMMEDIATE_CLEARING_SECURED`

World state still decides whether assistance is needed, whether the route remains closed and when the case can close.

## 11. The Search That Ends Without the Player

Premise: while the player follows one lead, another resident receives credible contact that the overdue subject is already safe.

The active objective updates or cancels. The player can still return found equipment, close a sector log or report a clue, but the world does not wait for the protagonist to discover the person personally.

This is a useful demonstration of autonomous institutional continuity.

Engine dependency: none.

## 12. Marea Search Ledger

Longer-term arc candidate.

Mara keeps operational case references while Tideglass preserves appropriate historical records. Over time the district accumulates patterns:

- recurring communication gaps;
- route sections that generate ambiguous reports;
- false leads that teach evidence discipline;
- safe self-returns;
- searches suspended by conditions;
- equipment/custody lessons;
- changes to route signage or check-in practice after documented incidents.

The ledger should never become a public database of sensitive personal information by default. Privacy and retention policy remain unresolved canon questions.

Narrative payoff: later incidents emerge from actual history. Residents can say that a route has caused several communication ambiguities because prior cases exist, not because exposition declares it dangerous.

## Recommended implementation order

Start with The Walker Who Returned Another Way. Follow with Found Equipment, Unknown Owner Status and The Check-In That Never Arrived. Together they test expected presence, verification, uncertain evidence, communications correction, autonomous resolution and closure without touching incomplete battle families.

The Upper Bend Search should remain a design target with its reduced version available only after the exact ordinary battle roster is parity-audited.

## Canon gates left open

No proposal above canonizes:

- a formal Marea search-and-rescue service;
- any new route branch;
- a legal definition of missing person;
- exact emergency response times;
- field-radio or phone infrastructure;
- special tracking powers for named Pokémon;
- Mirador surveillance;
- a historical disappearance;
- injury to a current resident;
- rescue certification;
- Caelo emergency law.

Those require explicit promotion and, where relevant, Caelo/PTU provenance.