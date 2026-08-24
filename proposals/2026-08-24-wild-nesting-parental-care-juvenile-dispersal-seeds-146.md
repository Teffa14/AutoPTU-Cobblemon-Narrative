# Wild nesting, parental care & juvenile dispersal seeds — Pass 146

Status: NON-CANON PROPOSALS. Original Ouros candidates derived from the research scan and existing repository architecture. None are approved lore.

## Candidate seeds

1. The Empty Nest Is Not Abandoned — surveyors find young with no adult visible during three short visits. The interesting question is monitoring effort and timing, not immediate rescue.
2. The Adult Returns After Dusk — a suspected abandonment case changes when remote observations show provisioning only after visitor traffic stops.
3. The Nest Moved Across the Trail — the same persistent breeding group shifts its site a short distance after vegetation changes, forcing maps and access boundaries to update.
4. Three Nests, One Colony — three nearby nest structures have different activity histories; loaded entity count repeatedly misleads casual observers.
5. The Camera Visit Changed the Behavior — researchers discover that servicing a camera coincides with temporary avoidance of the site.
6. The Chick Left the Nest but Not the Territory — a juvenile begins using nearby cover while still receiving care and following familiar adults.
7. The First Solo Night — observers record a juvenile alone overnight; the event is notable but does not by itself establish independence.
8. The Provisioning Route Changed — a recurring Mandibuzz-like provisioning route shifts after a road opening; the nest remains active.
9. The Nursery Chamber — a Nidoqueen-like caregiver repeatedly shelters young in a rock chamber. The behavior is documented without adding mechanical protection.
10. The Brood Nobody Should Count Twice — two observation teams publish different totals because mobile young move between visible sub-sites.
11. The Road Closure That Worked — a seasonal closure reduces disturbance so effectively that future seasons become routine and no longer generate quests.
12. The Closure That Outlived the Nest — an old protected boundary remains posted years after breeding activity moved, creating a governance update rather than a wildlife emergency.
13. Nest on Old Infrastructure — a retired signal tower becomes a breeding site, complicating a proposed heritage restoration.
14. Storm Exposed a Former Nest — erosion reveals old nesting material and archived tags from a long-finished monitoring program.
15. The Decoy Study — an institution tests non-invasive social cues at a restoration site; the arrival pattern changes, but attribution remains cautious.
16. The Former Nest Became Shelter — a structure used for breeding in one decade later becomes a regular refuge during migration.
17. The Viral Nest Photo — a beautiful public image creates visitor pressure; the original photographer had already redacted the exact location.
18. Every Other Year — a site appears inactive in alternating seasons, challenging assumptions that absence means abandonment of the broader landscape.
19. Dispersal Came Late — juveniles remain near the natal site much longer in a low-food year without any authored fixed-age failure state.
20. The Missing Parent Was Never Assigned — a database imported `parent_id` from an old assumption that the original observer never actually made.
21. Two Adults Feed the Same Young — field staff record cooperative provisioning while leaving parentage unresolved.
22. Bone-Lined Ledge — a nest accumulates durable material over many years; Material Culture may eventually treat individual pieces as provenance-bearing objects only after they leave ecological use.
23. Emergency Egg Custody — a flood physically isolates an Egg from a destroyed nest. Crisis, Research Ethics and Care must establish intervention before the Egg/Nursery system takes custody.
24. Post-Fledging Reservoir — juveniles leave their nesting shoreline but concentrate at a nearby reservoir for several weeks before dispersal.
25. The Monitoring Blackout — no observations exist during the most important week because the camera network lost power; Chronicle records uncertainty rather than filling the gap.
26. The Old Nest Under New Canopy — a tree used repeatedly for nesting remains the same landmark while canopy succession changes access and visibility.
27. Rooftop Nest Season — an urban population uses roofs that are active workplaces during the day, creating scheduling and coexistence pressure rather than automatic conflict.
28. The Nesting Atlas — decades of site revisions, camera records and closures reveal that the breeding range moved gradually rather than suddenly.
29. The Young That Returned — an individually marked juvenile is observed years later near its natal area; philopatry is a hypothesis until enough evidence exists.
30. Nothing Happened at the Colony — the breeding season proceeds normally. The monitoring record still matters because future anomalies need a baseline.

## Long arcs

### Five Springs at Redbank Colony

Year 1 establishes several breeding sites near a popular river crossing. Year 2 brings a storm that removes one site and creates another. Year 3 introduces remote monitoring after direct surveys show disturbance concerns. Year 4 a road detour pushes visitors closer to the colony, requiring a temporary access change. Year 5 the colony uses fewer original nests but fledged/juvenile observations remain stable in a different post-natal area.

The arc is about accumulated evidence, changing habitat and institutional learning. It does not require a villain, a boss or declining population every year.

### The Nest That Moved Three Times

A persistent wild group uses three nearby sites across several seasons. Each move has a different plausible driver: vegetation succession, water level and later human disturbance. Old maps remain historically correct. The Chronicle gradually distinguishes site identity from group identity and avoids creating three separate populations.

### From Nest to First Territory

One juvenile becomes individually identifiable through non-invasive marks or a canon-approved persistent identity method. The story can follow nest departure, continued dependency, first solo foraging, natal dispersal, temporary use areas and eventual later settlement. Gaps remain gaps; the system never fabricates unseen survival events or motivations.

## Encounter contracts

### Nesting Shore Evacuation

Premise: visitor pressure and a separate threat create a situation near an active breeding area. The objective is to clear people from the site without making Eggs/young tactical prizes.

FULL version:
- civilians and wild adults can `WITHDRAW` through changing lanes;
- defenders can choose routes that avoid the active site;
- AI recognizes `EVACUATE`, `WITHDRAW`, `PROTECT_NEST` and `CLEAR_ROUTE` goals;
- if tide, storm or fragile ground changes tactical legality, the environment is represented by validated zones/hazards;
- Minecraft playback preserves the exclusion boundary and noncombatants.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement incl. interception/forced movement: BLOCKING;
- action economy/initiative: VERIFIED;
- terrain/weather/hazards/zones/reactions: BLOCKING as a complete family;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version:
- evacuate visitors in world state before combat;
- mark the nest/young as outside the tactical grid;
- freeze a safe shoreline arena;
- run a conventional battle only with actual combatants if confrontation remains;
- resume nesting/access state after the battle.

### Juvenile at the Road Crossing

Premise: a juvenile and associated adults need to cross a road corridor during a temporary traffic closure. A separate hostile or panicked actor may complicate the crossing.

FULL version:
- moving crossing objective;
- protected lanes and road traffic state;
- non-hostile AI goals `CROSS`, `REACH_GROUP`, `WITHDRAW`;
- possible interception only where PTU rules authorize it;
- playback of traffic closure and participants.

Dependencies:
- complete movement: BLOCKING;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING;
- terrain/hazards only if the road itself has an authored tactical effect.

REDUCED version:
- traffic closure and juvenile crossing happen in world state;
- if a separate opponent blocks the route, AutoPTU resolves a static battle at a nearby safe perimeter;
- crossing resumes after the conflict;
- the juvenile never becomes automatically capturable because it appeared in the scene.

### Colony Monitoring After Storm

Premise: a storm changed access to a breeding colony and monitoring equipment must be recovered or replaced without repeatedly disturbing active sites.

FULL version:
- technicians move between safe survey points;
- fragile/excluded site zones can change movement choices;
- wildlife can withdraw rather than fight;
- AI understands `RETRIEVE_DEVICE`, `WITHDRAW`, `PROTECT_TECHNICIAN` and `AVOID_SITE`;
- if storm debris has mechanical effects they must come from validated environment rules.

Dependencies:
- complete movement: BLOCKING;
- terrain/weather/hazards/zones/reactions: BLOCKING when required;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING.

REDUCED version:
- survey/retrieval is resolved from fixed safe points in world state;
- equipment state and site observations remain outside the grid;
- a static battle can occur at the perimeter if a real combatant confrontation exists.

### Dependency Assessment

Non-combat concept. Observers compare direct sightings, remote images and feeding/foraging behavior to decide whether a juvenile is still dependent. The correct outcome may remain `UNKNOWN`. No battle victory, Skill shortcut or species stereotype resolves the assessment automatically.

## Canon guardrails

These proposals do not establish regional species, breeding seasons, parentage, Egg availability, adoption rules, reproduction rates or institutional powers. They also do not create juvenile stats, nest-defense mechanics, capture rules or Loyalty effects.

Any later canon promotion must cross-check PTU/Caelo breeding/hatching rules and the final Cobblemon projection model.
