# Pass 110 Proposals — Sacred Sites, Pilgrimage, Belief, and Practice

Status: NON-CANON candidates. These concepts are reusable seeds only. They do not define regional religion, cosmology, supernatural truth, Legendary behavior, or PTU mechanics.

## 30 candidate concepts

1. The Shrine That Stayed After the Road Moved
An old route is abandoned after a landslide, but visitors still reach the hillside shrine by a longer path. The place remains significant while the journey changes.

2. The Bell That Rang During Clear Weather
A bell sounds once with no one near it. Wind, building movement, a Pokémon, prank, sensor fault, and genuine anomaly remain separate hypotheses.

3. Two Custodians, One Site
Two families maintain different parts of the same old sanctuary under practices that overlap but are not identical.

4. The Empty Pilgrimage Year
A traditional journey continues normally, but the wild Pokémon usually observed near the destination do not appear. The absence becomes an ecological investigation, not a spiritual verdict.

5. The Route With an Accessible Second Path
A newer accessible approach becomes common. Some residents initially call it “not the traditional way,” while others document earlier historical route changes that complicate that claim.

6. The Replica Everyone Knows
A modern replica of a lost ritual object becomes more publicly recognizable than archival photographs of the original.

7. The Offering That Was Evidence
An object assumed to be a recent offering is actually an archaeological item exposed by erosion. Custody and context become more important than possession.

8. The Pilgrim Who Is a Researcher
A visitor joins the journey for scientific reasons and is careful not to claim participation implies belief.

9. The Researcher Who Also Participates
A scientist is personally part of the tradition but keeps private practice separate from published claims.

10. The Visitor Who Saw Nothing
A long-awaited observation window produces no anomaly. The journey still changes relationships, route knowledge, and public memory.

11. The Visitor Who Saw Something Else
A supposed omen is documented clearly, but the event is a rare meteorological phenomenon. One other detail remains unexplained.

12. The Sacred Spring That Runs Dry
A culturally significant spring stops flowing. Groundwater investigation, custodianship, tourism, and tradition all respond differently.

13. The Pokémon That Keeps Returning
The same persistent wild Pokémon is observed near a sanctuary across several years. No motive, ownership, blessing, or guardian role is inferred automatically.

14. The Route Closed for Nesting
A customary pilgrimage route is seasonally rerouted because a nesting population begins using the original path.

15. Three Translations of One Inscription
A sacred inscription has one old local reading, one modern academic translation, and one newer interpretation based on comparative evidence.

16. The Temple Under the Temple
Restoration work reveals older foundations with a different orientation. The modern site remains culturally valid even if its physical history becomes more complex.

17. The Shared Sanctuary
Two historical communities contributed architecture and practices to the same complex. Later narratives incorrectly try to assign the whole site to one founder.

18. The Abandoned Practice That Returns
A ritual discontinued for practical reasons is revived by younger residents in a changed form. The revival is itself new history.

19. The Quiet Custodian
A site caretaker knows maintenance, route history, visitor habits, and old repairs extremely well but refuses to speculate about supernatural claims.

20. The Famous Skeptic
A public figure regularly visits a sacred place for family/history reasons while openly declining to endorse supernatural interpretations.

21. The Scholar Who Was Wrong
A respected academic interpretation becomes obsolete after new excavation evidence. Old publications remain in archives instead of disappearing.

22. The Miracle Headline
A media outlet labels an unusual natural event a miracle before local custodians themselves make any such claim.

23. The Missing Page
An archive preserves a ritual record with one missing section. Different communities remember the gap differently.

24. The Shrine Beside the Working Forest
A small sanctuary remains active inside a managed forest. Harvest planning, access, buffers, and visitation must coexist.

25. The Pilgrimage That Became Tourism
A once-small route grows famous through photography and social media. Residents, pilgrims, vendors, conservation staff, and tourists now use the same corridor differently.

26. The Place With No Building
A site is culturally significant because of a landscape feature and has never required a constructed shrine.

27. The Building With No Current Practice
An old sanctuary remains historically important after its original practice stops. It becomes a preservation and interpretation question rather than an active ritual center.

28. The Sacred Object With No Powers
A centuries-old object is deeply important and carefully transported between institutions. Mechanical tests repeatedly show no unusual battle effect.

29. The Former Partner on the Old Road
A released former partner is observed once along a historic route years later. The Chronicle records location and identity without assigning motive.

30. The Site That Changed Names Three Times
The same physical location accumulates three names from different eras and communities. Maps, archives, locals, and tourists use different names without one automatically erasing the others.

## Long arc A — Five Journeys to Cloud Bell Ridge

Year 1: a small local route is documented with a single annual observance.
Year 2: storm damage closes the upper approach and creates an alternate path.
Year 3: photographs make the ridge regionally famous, increasing visitor pressure.
Year 4: nesting wildlife causes a seasonal reroute and introduces conservation coordination.
Year 5: an unusual atmospheric event occurs during the observance. Multiple observers record it. Meteorology explains most of the event, while one separate signal remains uncertain.

The arc is about continuity under changing access, interpretation, ecology, and public attention. It does not require a Legendary appearance.

## Long arc B — The Temple Beneath Three Histories

An active sanctuary undergoes structural repair. Workers discover older foundations. Archaeologists identify two construction phases. Language specialists find inscriptions from different periods. Local tradition preserves a third chronology. Over several years, the community decides how to preserve all layers without forcing one clean origin story.

Possible outcomes:
- expanded archive;
- protected excavation area;
- revised visitor interpretation;
- shared custodianship;
- continued ritual practice in a newer section;
- unresolved disagreement that remains stable rather than becoming a faction war.

## Long arc C — The Pilgrim Road Becomes a Region

A path linking several small sacred or memorial sites gradually accumulates hostels, wayfinding, repair depots, research stations, accessible route variants, vendors, ecological protections, and public transport connections.

The story tracks how an old journey changes when infrastructure improves. The world should preserve the earlier harder route as history rather than treating modernization as erasure.

## Encounter contracts

### Shrine Approach Evacuation

Narrative premise:
A noncombat incident blocks a traditional approach while visitors and wild Pokémon occupy the area.

FULL dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if the incident changes tactical ground or environmental state
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT`, `REACH_EXIT`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

REDUCED version:
Evacuate visitors and resolve wildlife movement in world state. Freeze one safe static arena and open AutoPTU only if an actual combat conflict remains.

### Relic Custody Interruption

Narrative premise:
A culturally important object is being transferred between custodians when a separate hostile incident interrupts the route.

FULL dependencies:
- complete movement/interception/forced movement: BLOCKING for moving-object protection or interception
- lifecycle/damage/status/moves/abilities/items/Features: current PARTIAL categories where used
- AI tactical policy: BLOCKING for `PROTECT_CUSTODIAN`, `INTERCEPT`, `ESCAPE_WITH_OBJECT`
- adapter/playback: BLOCKING

REDUCED version:
Secure the object outside the grid before battle. Resolve custody and transport afterward using world state. Battle victory does not decide ownership or legitimacy.

### Bell Ridge Night Watch

Narrative premise:
Visitors gather for a traditional observation window while a wildlife disturbance develops nearby.

FULL dependencies:
- complete movement: BLOCKING for autonomous wildlife withdrawal and crowd routing
- terrain/weather/hazards/zones/reactions: BLOCKING if darkness, wind, weather, or field conditions gain mechanics
- AI tactical policy: BLOCKING for `WITHDRAW`, `AVOID`, `CLEAR_ROUTE`
- adapter/playback: BLOCKING
- ordinary targeting/calculation/action economy remain usable at current verified scope

REDUCED version:
Pause the observance and clear visitors. Keep weather, light, sounds, bells, and any supposed omen in presentation/world state unless exact mechanics are validated. Use a static battle only if a separate confrontation remains.

## Mechanical guardrails

No candidate above grants:
- healing;
- blessings;
- curses;
- divine intervention;
- guaranteed Legendary encounters;
- Weather or Terrain;
- Sonic effects from bells/chants;
- Aura from sanctity;
- reputation or XP for participation;
- supernatural detection;
- ownership of wild Pokémon;
- special capture rights;
- combat bonuses for relics;
- mandatory PC beliefs.

Any later canon promotion must cite the exact authored source and, for mechanics, the exact PTU/Caelo rule plus live Java capability evidence.