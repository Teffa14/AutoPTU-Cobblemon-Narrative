# Marea Cartography, Survey and Route-Marker Seeds — Pass 203

Status: PROPOSED / NON-CANON
Date: 2026-09-02

These candidates reuse canonical Marea locations, residents and institutions. They do not alter canonical coordinates or establish new regional geography.

## 1. Two Maps, One Bend

Recommended first implementation slice.

Tideglass holds an older Sendero del Vidrio route survey while Estación Mirador maintains a newer working copy. Both are legitimate records. They disagree about one bounded feature near an existing route segment: the older edition places a maintained route marker on one side of the bend, while the newer copy shows it on the other.

The initial question is intentionally small: did the marker move, was one map copied imprecisely, or are the two editions using different reference descriptions?

Existing actors:
- Ema can perform a bounded field observation.
- Nerea can review the current Mirador record.
- Pia can retrieve/carry the Tideglass copy.
- Taro preserves edition provenance.
- Mara consumes the operational result if route guidance needs updating.

Possible outcomes:
- current field observation confirms one marker position;
- the old edition remains historically valid for its date;
- evidence shows the marker was replaced or moved at an unknown time;
- the discrepancy remains partially unresolved.

No battle required.

No new coordinate is required. The represented feature should reference an existing canonical Sendero segment and use a relative narrative position until a canon review explicitly adds a marker anchor.

What this slice tests:
- edition lineage;
- field observation versus representation;
- route-marker history;
- archive custody;
- correction without retcon;
- actor knowledge update;
- UI/map projection boundaries.

## 2. The Board Still Shows Last Week

A public route board in Puerto Bruma still displays an older map copy after Mirador has issued a newer internal annotation about one route condition.

The old board was accurate when posted. Lia, Mara or Pia may notice that it is now stale.

The story is about update propagation, not deception.

Information-circulation integration:
- some residents may still know only the older edition;
- replacing the board does not rewrite their memories;
- the retired copy can remain archived.

## 3. The Marker Nobody Moved on Paper

Ema finds that a physical route marker appears displaced relative to the currently circulated map.

Possible explanations stay open:
- maintenance moved it;
- weather displaced it;
- an old replacement event was never entered into the map edition;
- field interpretation is wrong.

Do not infer vandalism, negligence or weather causation without evidence.

This can create a small service task for Teo or Mara only after responsibility and physical condition are established.

## 4. Same Place, Three Names

Tideglass, Mirador and ordinary residents use three labels for the same already-canonical route feature or bend.

The task is to reconcile identifiers, not force one cultural name to disappear.

Potential records:
- archive survey code;
- field-team shorthand;
- local spoken name.

Language/translation continuity owns any disputed meaning. Cartography only links name usage to the same world feature when evidence supports it.

## 5. The Personal Copy

A repeat visitor returns with an annotated copy of a public Marea route map from their earlier stay.

Their notes include:
- one useful landmark reminder;
- one outdated route preference;
- one personal warning based on an old experience.

The annotation is evidence of what the visitor believed or experienced, not a current institutional route report.

This seed links visitor continuity, identity, information circulation and cartographic provenance.

## 6. The Missing Annotation

Pia discovers that two physical copies nominally derived from the same edition differ because one omitted a marginal access note during copying.

The omission can matter operationally without implying deliberate falsification.

Tideglass preserves:
- source edition;
- copy lineage;
- omitted note;
- correction event.

This provides a spatial counterpart to language/pass-195 copy errors without duplicating translation semantics.

## 7. Mirador's Narrower Map

A Mirador working diagram covers only the transect and observation points relevant to one project. A visitor assumes blank space means no route or feature exists there.

Ema or Nerea clarifies the artifact's scope.

Design lesson inside the fiction:
`NOT_SHOWN != DOES_NOT_EXIST`.

No hidden dungeon or secret reward needs to occupy the blank space.

## 8. The Route Exists, the Crossing Does Not

A public map correctly shows Sendero del Vidrio, but current physical state makes the seasonal crossing temporarily unusable or degraded if a canon-supported route event establishes that state.

The map does not need to be declared wrong. The operational annotation changes while the underlying connection remains.

This seed should only activate from explicit route-state evidence. It must not invent a closure merely to create content.

## 9. Thin Delivery: The Shortcut Everyone Draws

During Thin Delivery Season, several people mark what they call a shortcut or alternate path on personal copies.

The line's popularity does not establish:
- that carriers actually used it;
- that it is a legal/maintained route;
- that it caused delays;
- that it is safe;
- that it exists as a canonical connection.

Mara can treat it as a lead requiring field verification. Brin and Lia can provide shipment/arrival evidence separately.

The arc remains unresolved unless independent evidence converges.

## 10. Old Survey, New Watercourse

An old Tideglass survey and a current Mirador observation disagree about the visible shape or crossing behavior of a seasonal watercourse along Sendero del Vidrio.

The old document can remain correct for its observed season while the current field state differs.

Do not invent hydrology or permanent erosion as cause without evidence.

This seed supports longitudinal environmental storytelling.

## 11. A Map After the Repair

A route fixture or ordinary infrastructure point is repaired under an existing service/recovery workflow. The physical repair finishes before the public map/diagram is revised.

For a short period:
- world state is current;
- one map edition is stale;
- actors with direct knowledge may navigate correctly;
- actors relying only on the older copy may possess outdated information.

This shows that world changes and publications have different clocks.

## 12. The Minecraft Drift Audit

Implementation-facing seed, not an in-world mystery by default.

A build audit detects that a rendered sign, path segment or structure has drifted from the frozen canonical anchors/graph.

Correct response:
- flag implementation drift;
- compare build to canon;
- repair the projection or open an explicit canon migration if a deliberate redesign is desired.

Incorrect response:
- invent a landslide, moved settlement or new road in narrative merely to explain a placement bug.

This seed should primarily generate developer/admin work, not player-facing lore.

## 13. The Map That Wins No Argument

Two residents disagree about whether a route condition has been persistent or recent. One produces an old map as evidence.

The map can establish that a feature was represented at a historical date. It cannot by itself establish:
- why it existed;
- whether the compiler personally observed it;
- whether conditions were continuous between then and now;
- who is socially 'right' about the broader argument.

Taro can help trace sources rather than act as an omniscient judge.

## Longer arc — Lines Marea Keeps Redrawing

This arc accumulates small spatial revisions over seasons without changing the canonical backbone arbitrarily.

Phase 1: ordinary discrepancies
- map copies differ;
- a marker is missing or replaced;
- a working diagram has limited scope;
- local names diverge from archive labels.

Phase 2: longitudinal comparison
- Mirador field observations add dated spatial evidence;
- Tideglass preserves old editions;
- Mara consumes operationally relevant updates;
- public copies update on their own circulation schedule.

Phase 3: meaningful change
- an explicit world event may degrade, restore or reroute an existing connection;
- maps document that change after it occurs;
- old editions remain usable for historical inquiry.

Phase 4: outward growth
- later Ouros districts can use the same architecture for expedition maps, ruins, caves, coastlines and dungeon plans;
- new geography still requires canon approval before a representation can create it.

The arc's reward is a world with spatial memory, not a percentage-complete minimap.

## Mechanically rich encounter — Survey Line at Glass Bend

Narrative premise:
Ema and a small field party are checking a bounded map/marker discrepancy on Sendero del Vidrio. Their work is interrupted by a localized wild confrontation while the team needs to withdraw from the immediate area.

The survey question remains outside combat authority.

### Full intended version

Potential tactical features:
- uneven route geometry;
- protected withdrawal;
- a field observer who must not become an arbitrary combatant;
- a specific marker or instrument as semantic world object;
- wild actor behavior oriented around territory/withdrawal rather than simple KO priority;
- possible Interception or forced movement near constrained terrain;
- environmental route conditions if separately established.

Permanent dependency categories:
- targeting/footprints/range/LoS: required
- base movement legality: required
- complete movement including push/pull/knockback/interception/forced movement: required if displacement/protected withdrawal is active
- core calculations: required
- action economy/initiative: required
- full turn/round lifecycle: required for sustained objective form
- full stateful damage pipeline: required
- status lifecycle: required if selected content uses statuses
- terrain/weather/hazards/zones/reactions: required if uneven/unstable route conditions become mechanical
- move-specific behavior: required
- abilities: required
- items: required if battle Items participate
- Trainer Features/perks: required if field Trainers use them
- AI legal-action infrastructure: required
- AI tactical policy: required for withdrawal/territory/objective-aware behavior
- Minecraft/Cobblemon/Craftics adapter/playback: required for faithful overworld-to-battle-to-overworld projection

Current disposition: FULL RICH VERSION BLOCKED pending complete capability families described in the pass-203 readiness snapshot.

### Reduced version

Before BattleSpec creation, Narrative resolves:
- which survey artifact is being checked;
- which marker/feature assertion is in dispute;
- field-party purpose;
- noncombatant safety state;
- instrument and document custody;
- current observations already made;
- current route-state facts supplied by Travel/Observation.

If one immediate wild actor still prevents safe withdrawal, assemble an ordinary audited battle on stable geometry using content verified for that slice.

Omit:
- tactical weather/hazards/zones;
- semantic map objects from battle state;
- forced-movement objectives unless the exact selected interactions are contract-verified;
- AI objectives beyond currently proven policy.

Allowed narrow world handoffs:
- `IMMEDIATE_SURVEY_TEAM_CAN_WITHDRAW`
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_SURVEY_SEGMENT_CLEAR_AT_TIMESTAMP`

Combat output cannot determine:
- which map edition is correct;
- whether a marker moved historically;
- why it moved;
- whether the route is permanently safe;
- whether a map should be published or withdrawn;
- canonical coordinates;
- route-closure authority;
- Thin Delivery Season cause;
- whether a personal annotation becomes public truth.

The narrative premise remains intact: the party was performing survey verification and experienced a localized interruption. Rich tactical behavior can be added later without rewriting the spatial mystery.