# Ouros Migration, Stopover & Corridor Seeds — Pass 124

Status: NON-CANON proposals. Every item requires continuity, originality, PTU/Caelo and implementation review before promotion.

## 30 original candidates

1. The Stopover That Moved — A flock still crosses the same valley, but its main resting site has shifted from a reedbed to a restored quarry pond over five years.

2. The Missing First Wave — Researchers record the second and third movement waves but no first wave. Equipment failure, route shift and genuinely smaller early movement remain competing explanations.

3. The Bridge Under the Flight Line — A new bridge does not block migration physically, but lighting and construction noise coincide with a change in the time of passage.

4. The Orchard at Dusk — A seasonal group repeatedly pauses in a working orchard for several evenings. The owner allows observation but not public access.

5. The Route Everyone Draws Too Narrow — An old guidebook shows one line through the mountains. New observations reveal a broad corridor with several interchangeable paths.

6. The Old Stopover Is Still Used — A newly restored wetland becomes famous, but field signs show that a smaller historic marsh remains part of the route.

7. The Former Partner in the Southbound Wave — A released Pokémon is photographed among a migrating group. Identity is plausible but unconfirmed, and no prior Trainer authority is restored.

8. The Village Counts Differ — Two settlements publish different totals for the same migration because one counts passage and the other counts overnight stopover use.

9. The Rain Year Detour — A river crossing is unusable during one unusually wet season. The herd uses a longer route, then returns to the old corridor the following year.

10. The Quiet Crossing — A road crossing has almost no visible collisions, yet monitoring shows groups accelerating through the area and skipping a nearby stopover.

11. The Empty Lookout — A famous migration viewpoint has almost no observations this year while another ridge receives more reports. Tourism information lags behind ecology.

12. The Last Ferry Before Passage — A small ferry reduces service for two nights each year because a marine movement corridor intersects its normal route.

13. The New Rail Embankment — A rail project includes a crossing structure before opening. The first season shows partial use, but no one can yet call the mitigation successful.

14. The Chinchou Road Without Chinchou — A community maintains a yearly protection practice even in a year when the expected migration is not confirmed.

15. The Migration That Became a Festival — A public observance grew around a reliable arrival window. Climate and phenology shifts now make the civic date and ecological event drift apart.

16. The Wrong Wind Theory — Local belief links migration to a particular wind. Ten years of records show correlation in some years and contradiction in others.

17. The Two Stopover Problem — One stopover has food but little shelter. Another has shelter but declining water. Different movement waves use them differently.

18. The Same Flock, Different Year — Photographic evidence suggests several persistent individuals return, but most membership remains unknown and variable.

19. The Quarry Lights — A quarry that operates legally during the day adds overnight lighting. No direct harm is proven, but passage height and timing change nearby.

20. The Storm-Separated Juvenile — A young Pokémon is found alone during a migration episode. The correct first assumption is temporary separation, not abandonment or ownership availability.

21. The Island Week — A small island is nearly empty most of the year but becomes a high-use stopover for one week. Development proposals underestimate its regional importance.

22. The Migration Through the Market — An old corridor now passes above and around a growing market district. Residents treat the event as normal; visitors create the actual pressure.

23. The Route That Became Safer but Longer — A restored crossing reduces one hazard but adds distance. Passage remains successful while stopover use changes.

24. The Noisy Success — A new underpass is used frequently, but only after surrounding fencing channels animals into a narrow approach. Monitoring must evaluate the full system, not the structure alone.

25. The Southbound Count Is Fine — Autumn counts look normal, while spring return counts fall. The difference triggers a multi-season investigation instead of an instant population-collapse claim.

26. The Migration Atlas Has Layers — A regional archive overlays corridor revisions from twenty years. None is “the wrong map”; each shows the best-supported route for its period.

27. The First Year After Wildfire — A migration still crosses the burned landscape but uses different stopovers as vegetation and water recover unevenly.

28. The Reservoir Shortcut — A low-water year exposes a temporary route across an old reservoir margin. The following year the path disappears again.

29. The Persistent Individual Skips a Year — A well-known marked Pokémon is not observed one season and reappears the next. Missing one year never becomes death or permanent departure automatically.

30. The Migration Without a Quest — A major seasonal movement passes normally. Players can observe, travel around it or ignore it. The world records the event without generating mandatory conflict.

## Long arc A — Five Springs Across Meridian Corridor

Year 1 establishes baseline movement, stopovers and community observation points.

Year 2 a road upgrade changes crossing behavior but not the overall route.

Year 3 drought shifts the timing of plant growth and the main stopover becomes less useful.

Year 4 a restoration project creates a new optional resting site and monitoring shows partial adoption.

Year 5 the route remains recognizable but no longer matches the oldest public maps. The story is about accumulated adaptation, not a single villain or disaster.

Possible connections: Seasonality, Flora, Road Ecology, Freshwater, Public Memory, Tourism, Science, Cartography.

## Long arc B — The Flock With Three Histories

Three settlements describe what they believe is the same recurring flock.

One remembers a traditional lowland route.
One has records of a coastal detour after a historic storm.
One tracks a modern urban-edge route.

Over years, photography, field signs and repeated observations show that the histories partially overlap but do not describe one perfectly fixed group. The arc teaches the region to preserve uncertainty without erasing local memory.

Possible connections: Wild Collectives, Identity, Photography, Archives, Public Memory, Urban Wildlife.

## Long arc C — The Stopover Network

A series of small ponds, rooftops, meadows and islands appear insignificant individually. Multi-year monitoring reveals that the migration depends on the network rather than one flagship site.

One site is lost to construction.
Another is restored.
A third only functions in wet years.
A fourth becomes too popular with visitors.

The network survives by changing composition. Conservation choices become distributed and cumulative.

Possible connections: Land Tenure, Tourism, Island Biogeography, Urban Public Space, Conservation, Demography.

## Encounter contract 1 — Corridor Crossing at Redbank

Narrative premise: a migrating group reaches a road/rail interface during a temporary operational disruption. The objective is to keep the passage from escalating into unnecessary conflict while restoring safe separation between infrastructure and wildlife.

FULL version dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING for moving wildlife, crossing lanes and interception
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if traffic, barriers or environmental state becomes tactical
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for CROSS/WITHDRAW/PROTECT/CLEAR_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

REDUCED version:

The migration group is held outside the battle grid. World state resolves the crossing window and moves civilians/workers first. If a confrontation remains, AutoPTU receives a static cleared verge with only actual combatants. After battle, Migration + Road/Rail state determines whether passage resumes. Battle victory does not equal corridor success.

## Encounter contract 2 — Stopover Disturbance at Reedglass Marsh

Narrative premise: a high-use stopover becomes crowded by visitors during a short migration window. Wild Pokémon are attempting to rest and depart, not conquer the area.

FULL version dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING for retreating groups and moving crowd boundaries
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full lifecycle — PARTIAL
- full stateful damage — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING only if marsh terrain/weather is mechanically active and verified
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for WITHDRAW/PROTECT/AVOID_CONFLICT
- Minecraft/Cobblemon/Craftics playback — BLOCKING

REDUCED version:

Visitor routing and migrating subgroups are resolved in world state. A small static perimeter is cleared. AutoPTU handles only any real confrontation that remains. The migration episode can continue even if no battle occurs.

## Encounter contract 3 — Separated Individual at North Pass

Narrative premise: a known or potentially identifiable Pokémon becomes separated from a movement wave during poor conditions. The question is reunion and route state, not capture availability.

FULL version dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING for pursuit/reunion during active movement
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full lifecycle — PARTIAL
- full stateful damage — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if mountain/weather effects enter tactical resolution
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for REACH_GROUP/WITHDRAW/ESCORT
- Minecraft/Cobblemon/Craftics playback — BLOCKING

REDUCED version:

Tracking, route search and reunion happen in overworld world state. If an unrelated threat produces combat, the Pokémon and migration group remain outside tactical authority unless they are actual combatants. Successful reunion updates participation state only; it does not change ownership, Loyalty or capture status.

## Canon questions raised by Pass 124

- Which migrations exist before players arrive?
- Are migrations authored at species, population or collective level?
- Which routes are common knowledge and which require discovery?
- Which stopovers have cultural practices or seasonal access rules?
- How much route/timing change can occur procedurally versus authored review?
- How should migration state advance while chunks are unloaded?
- How should Cobblemon project large migration waves without entity-count inflation or spawn exploits?
- Can players create infrastructure that permanently changes a corridor, and what evidence threshold promotes that change?
- Which persistent Pokémon are known to participate in migrations at campaign start?
- What exact PTU/Caelo rules govern pursuit, withdrawal, tracking, capture during movement and any group-movement interactions?