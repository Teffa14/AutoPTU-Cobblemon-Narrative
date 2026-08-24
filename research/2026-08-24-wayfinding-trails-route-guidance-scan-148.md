# Pass 148 — Wayfinding, Trails, Route Guidance, Landmarks

Status: RESEARCH / NON-CANON
Date: 2026-08-24

## Why this gap exists

The repository already has authoritative layers for travel-route existence and service state, cartographic representations, language/translation, accessibility, land access, field signs/tracking, emergency response, roads, rail, waterways, mountains and seasonal change. What was still missing was a dedicated authority for guidance itself: signs, blazes, cairns, mileposts, named junctions, landmarks, route descriptions, temporary detours and the scoped knowledge an actor has about how to follow a route.

This layer must not decide whether a route physically exists, whether access is permitted, what a map depicts, or whether a traveller mechanically succeeds at a PTU Skill check. It records the guidance system and its history.

## Fresh public-source scan

### National Park Service — Zuni-Acoma Trail / cairned routes

Source: https://www.nps.gov/elma/planyourvisit/zuni-acoma-trail.htm
Inspected: 2026-08-24.

Reusable pattern: some routes have little or no continuous tread and are followed through a sequence of cairns. A traveller is advised to locate the next cairn before committing to the next segment. NPS specifically warns visitors not to move existing cairns or construct new ones because false markers can disorient later travellers.

Ouros use: a guidance network can be a sequence of persistent assets rather than a painted path. A well-intentioned player or NPC can create a real guidance error without changing the underlying route. Each marker therefore needs identity, position history, status and provenance.

Do not import: Pueblo cultural history, the real trail, real rules, real names or its archaeological context.

### U.S. Forest Service — Trail Maintenance and Construction Notebook

Source: https://www.fs.usda.gov/sites/default/files/fs_media/fs_document/trail-maintenance-notebook.pdf
Inspected: 2026-08-24.

Reusable pattern: route guidance can use reassurance markers, blazes, arrows and junction information. Marker placement should account for poor visibility and bidirectional travel; the material and mounting method also affect maintenance and longevity.

Ouros use: `GUIDANCE_ASSET` should have type, orientation, intended viewing direction, visibility context, maintenance state and route revision. A marker can physically survive after the route it described changes.

Do not import: Forest Service standards, dimensions, color codes or maintenance policy as Ouros law.

### U.S. Forest Service — outdoor planning guidance

Source: https://www.fs.usda.gov/r04/safety-ethics/recreating-outdoors-planning-hiking-hunting-fishing-equestrian
Inspected: 2026-08-24.

Reusable pattern: signs and markers are aids, not a guarantee. Route users can combine maps, terrain knowledge, alternate-route planning and communication; markers can also be missing or damaged.

Ouros use: actor knowledge and physical guidance stay separate. A traveller may know the route despite a missing sign, or follow a sign confidently even though it is stale.

### National Park Service — Guadalupe Mountains trail descriptions

Source: https://www.nps.gov/gumo/planyourvisit/trails.htm
Inspected: 2026-08-24.

Reusable pattern: a trail may remain formally defined while vegetation makes it difficult to follow. Different navigation aids become important under different conditions.

Ouros use: `ROUTE_TRUTH`, `GUIDANCE_STATE` and `VISIBILITY_CONTEXT` remain separate. Canopy growth, snow, flood debris or redevelopment can reduce marker visibility without deleting the route.

### Pokémon Legends: Arceus — official story/gameplay pages

Sources:
- https://legends.arceus.pokemon.com/en-au/story/
- https://legends.arceus.pokemon.com/en-gb/gameplay/
Inspected: 2026-08-24.

Reusable pattern: expeditions depart from a persistent settlement, use base camps as field outposts, return after survey work, and gradually gain access to new areas. Exploration is framed as repeated fieldwork rather than a one-use corridor.

Ouros use: trailheads, camps, survey stations and route knowledge can persist as infrastructure and Chronicle history. Repeated use should improve records and local knowledge without granting an automatic PTU bonus.

Do not import: Galaxy Team institutions, rank progression, Hisui maps or research-task mechanics.

### Public PTU campaign discussion — open-world exploration

Source: https://www.reddit.com/r/PokemonTabletop/comments/1oz4e7w/first_time_dm_thinking_of_making_a_ptu_campaign/
Published: 2025-11-17.

Reusable pattern: community advice for open-ended campaigns recommends scattering lightly specified hooks across a region and expanding only the locations players engage with.

Ouros use: wayfinding can reveal optional branches, landmarks and old route references without turning every junction into a mandatory quest. The world may contain meaningful route history that players simply pass through.

### Public PTU road-trip discussion

Source: https://www.reddit.com/r/PokemonTabletop/comments/tglxnl/asking_out_of_curiousity/
Published: 2022-03-17.

Reusable pattern: long travel can become empty if every stretch of road is treated identically. The route itself needs recurring places, interruptions, services and consequences.

Ouros use: guidance assets become Chronicle anchors: a marker, shelter, ferry landing, junction, old blaze or view landmark can recur for years and show change without requiring a battle.

## PTU/Caelo mechanical guardrails

The project file-library search did not recover a reliable primary Caelo rules passage for generic navigation or route-finding. A previous project research package does confirm the project policy that route traversal must check actual required PTU capabilities/equipment rather than infer capability from a convenient Cobblemon model. That package is research, not a rules authority, so no DC or Skill rule is imported here.

The public PTU ecosystem contains Survival and Perception concepts, but this pass does not assume a universal navigation check, automatic familiarity bonus, route-memory mechanic, compass bonus, or marker-based mechanical effect. Exact PTU/Caelo text must be pinned before any such rule is authored.

Super PTU Online Helper was not exposed as an invocable capability in this runtime. No output is attributed to it.

## Synthesis for Ouros

The key authority chain should be:

`physical route state -> guidance assets -> guidance revision -> observation -> actor knowledge -> navigation attempt -> result -> Chronicle`

Other authorities remain external:

- Travel decides whether a route or service is physically/operationally available.
- Cartography owns map artifacts and map revisions.
- Languages owns wording, translation and script.
- Accessibility owns accommodation/accessibility semantics.
- Land Tenure owns permission and passage rights.
- Tracking owns traces left by actors or wildlife.
- Meteorology/Cryosphere/Fire/Freshwater/etc. own environmental change.
- AutoPTU owns any actual PTU battle mechanic.

## High-value design lessons

1. Guidance can be wrong while the route is physically intact.
2. The route can change while old guidance remains historically correct for its revision.
3. A landmark can disappear without invalidating the old document that referenced it.
4. User-generated markers require provenance; helpful additions can create false confidence.
5. `NOT OBSERVED` guidance does not prove `MISSING`; visibility and search effort matter.
6. A temporary detour may become socially familiar without becoming an authorized permanent route.
7. Route familiarity belongs to actor knowledge, not global world truth.
8. An accessible route may be longer and still be the correct route for a particular traveller.
9. Minecraft geometry and signs are projections, not navigation authority.
10. Getting lost is a world-state/navigation outcome, not an automatic PTU Status or stat penalty.

## Canon questions deliberately left open

- Which regions use signs, blazes, cairns, painted markers, posts, maps, guides or oral route descriptions?
- Which institutions maintain official guidance?
- Can player organizations publish unofficial route guides?
- How much route knowledge persists for an actor after years away?
- Which temporary closures or detours become part of public memory?
- What exact PTU/Caelo mechanics, if any, govern Survival/Perception navigation, map use, getting lost and route finding?
