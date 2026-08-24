# Wayfinding, Trails, Route Guidance and Landmark Layer

Status: PROPOSED / NON-CANON
Pass: 148

## Purpose

This layer owns persistent guidance for movement through Ouros. It records how a traveller is told to follow a route, how that guidance changes, what was actually observed, and what a specific actor knows. It does not own the physical existence of the route, access permission, maps, language rules, environmental hazards, or PTU navigation mechanics.

## Authority boundary

Travel owns route/service existence and operational availability.
Cartography owns map artifacts and revisions.
Languages owns wording, script and translation.
Accessibility owns accessibility requirements and route suitability for an actor.
Land Tenure owns access and passage permission.
Tracking owns spoor and traces left by actors.
Environmental layers own terrain/weather/fire/water/snow/vegetation changes.
This layer owns guidance assets, route descriptions, landmark references, temporary detour notices and actor route knowledge.

## Persistent entities

### WAYFINDING_NETWORK

A named or scoped system of guidance associated with one or more Travel routes.

Fields should include stable ID, geographic scope, maintaining institution if any, linked route IDs, current guidance revision, known historical revisions and status.

### JUNCTION_IDENTITY

A persistent decision point. Its identity survives renamed roads, rebuilt signs or a changed route geometry when the Chronicle still treats it as the same junction.

### GUIDANCE_ASSET

Examples: sign, post, blaze, cairn, mile marker, trail shield, painted mark, board, temporary flag, beacon used only as a visual landmark, or a documented natural landmark.

Suggested fields: asset ID, type, physical location, orientation, intended direction(s) of travel, linked junction/route, owner/maintainer if any, first known date, current condition, visibility notes and provenance.

### GUIDANCE_ASSET_REVISION

Records relocation, rotation, replacement, text update, destruction, concealment, restoration or retirement. Old revisions remain queryable.

### LANDMARK_IDENTITY

A persistent referenced feature used in route descriptions: tree, rock formation, tower, bridge, ruin, ridge, fountain, station entrance or other authored feature.

A landmark may disappear physically while historical descriptions remain valid for their date.

### ROUTE_GUIDANCE_REVISION

Versioned guidance for following a route. It links ordered junctions, marker sets, descriptions, known ambiguities, temporary conditions and the Travel route revision it was authored against.

### WAYPOINT_SEQUENCE

An ordered sequence of coarse navigation anchors. It is descriptive and must not become a hidden Minecraft pathfinding rail.

### DETOUR_NOTICE

Temporary guidance with start, reason/source, scope, authority, intended expiry/review date and linked Travel closure/disruption. A detour may remain physically usable after the notice expires without becoming permanent guidance automatically.

### NAVIGATION_OBSERVATION

An observation of a sign, marker, junction, landmark or mismatch. Preserve observer, time, position, method, conditions, confidence and source media if any.

### NAVIGATION_ATTEMPT

Records a specific actor/group trying to reach a destination using specified guidance. Possible outcomes include reached destination, route corrected, turned back, requested assistance, off-route, unresolved, or aborted.

This record never fabricates a PTU Skill result unless an authoritative mechanic actually produced one.

### NAVIGATION_KNOWLEDGE_RECORD

Scoped evidence of what an actor has previously learned: route revision seen, landmarks personally observed, guide/map consulted, date, confidence and known stale portions.

Do not model this as a universal numeric familiarity score.

### GUIDANCE_CONFLICT_CASE

Used when map, signs, route truth, institutional guidance and local knowledge disagree. It preserves competing claims until evidence resolves them.

## State rules

1. Route truth and guidance truth are separate.
2. A marker can be physically present and semantically stale.
3. A missing marker can be unobserved, obscured, destroyed, moved or never installed; do not select a cause automatically.
4. Multiple guidance revisions can be correct for different dates.
5. Unofficial guidance must preserve authorship/provenance and cannot silently become official.
6. Actor knowledge is private/scoped and cannot be inferred from residence, profession or previous presence alone.
7. A successful trip does not grant perfect knowledge of every branch or reverse direction.
8. A failed trip does not imply incompetence; guidance/environment/access may have changed.

## Environmental coupling

Weather, wildfire, flood, snow, vegetation growth, shoreline/rivers, landslides and construction may change visibility or physical relevance of guidance assets. Those source layers issue the change. Wayfinding stores the resulting guidance impact and revision.

Examples:
- a blaze survives but canopy growth hides it from one approach;
- flood moves a ford while the sign still points to the old crossing;
- wildfire reveals an older marker set;
- snow buries low markers while elevated winter poles remain visible;
- a river cutoff leaves a bridge landmark beside the old channel.

None of these observations automatically creates PTU Rough Terrain, Weather, Accuracy penalties or Status.

## Minecraft projection

Minecraft renders only the current authorized projection of guidance state. Blocks/entities are not the source of truth.

Placing a sign or stack of rocks does not create an official guidance asset until the server accepts a world-state action. Breaking a marker block does not erase its identity/history. Chunk reload cannot restore an obsolete revision. Map pins supplied by a client cannot directly rewrite route knowledge.

Useful presentation can include signs, marker models, map overlays, landmark labels, temporary closure boards and optional route hints. Accessibility settings may present equivalent information differently without changing the underlying route.

## Actor knowledge and privacy

Knowledge may come from direct travel, a guide, map, briefing, local resident, archive, emergency notice or repeated institutional work. Preserve provenance and date. Do not infer that all members of a faction or family share route knowledge.

Route descriptions may contain sensitive site information. Conservation, Research Ethics or Sacred Sites can require redaction or restricted disclosure.

## Battle handoff

Wayfinding itself should normally resolve before battle. When a confrontation occurs, the server freezes a legal arena from authoritative world state. Guidance assets may remain visual unless a verified PTU mechanic explicitly makes them interactive.

A sign does not grant cover. A cliff marker does not create falling rules. Being off-route does not create a Status. A cairn does not become an Item. A route boundary does not become a tactical zone unless the battle engine has an exact supported contract.

## Encounter dependency pattern

A FULL search/escort encounter with moving civilians or wildlife usually needs complete movement including interception/forced movement, AI tactical policy, and Minecraft/Cobblemon/Craftics adapter/playback. Dynamic water, snow, wildfire or protected corridors additionally require terrain/weather/hazards/zones/reactions when those effects matter tactically.

A REDUCED version resolves search, route choice and escort movement in world state, then freezes a static arena and uses AutoPTU only for a discrete confrontation. It still inherits whatever normal move/status/item/ability parity gaps the battle engine has.

## PTU/Caelo guardrails

No generic Survival check, Perception check, compass modifier, map bonus, navigation DC, lost Status or route-memory rule is authored here. Exact PTU/Caelo source text must be pinned first.

Geometric LoS is not navigation. Base movement legality is not pathfinding knowledge. A verified reaction movement path is not escort AI. A Cobblemon model with a movement capability is not proof that the associated PTU capability or route requirement is satisfied.

## Canon decisions still required

Ouros must eventually define regional marker traditions, official maintainers, emergency detour authority, public versus restricted guidance, player-published guide policy, route knowledge persistence and any actual PTU/Caelo navigation mechanics.
