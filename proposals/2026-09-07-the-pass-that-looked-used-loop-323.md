# The Pass That Looked Used — Pass 323

Status: PROPOSED / NON-CANON
Date: 2026-09-07

## Premise

A mountain crossing has reopened after a storm cycle. The lower road has been cleared, route markers are visible again, and fresh tracks show that somebody crossed recently. A second field report recommends keeping one upper traverse restricted because the snow history there does not match the cleared road below.

Both reports may be accurate.

The player is asked to establish which route features are currently usable, which claims are stale, and what evidence should drive the next access decision before a scheduled movement of people, supplies, or Pokémon uses the pass.

No region, settlement, institution, species population, economic dependency, final cause, or PTU mechanic in this proposal is canon-approved.

## Why this belongs in Ouros

The loop turns a route into persistent world state rather than a corridor between battles. It uses existing Ouros principles: explicit feature identity, non-omniscient NPC knowledge, provenance-backed observations, semantic time, institutional decisions, selective consequences, and revisits.

The mystery is not “is the mountain dangerous?” The question is narrower: which persistent features support which conclusions at this time?

## Persistent site features

Use region-neutral identifiers until canon placement is approved.

### Lower approach

A maintained road segment where snow has been physically cleared. It can legitimately be open while other connected features remain unresolved.

Possible evidence:
- dated maintenance completion;
- exposed route markers;
- wheel, hoof, boot, or Pokémon tracks with uncertain age and provenance;
- a public reopening notice that may refer only to the lower approach.

### Cross-loaded gully

A short traverse or road cut whose local accumulation can differ from the lower road. The feature exists to make local state matter; it must not receive an automatic real-world avalanche model.

Possible evidence:
- drift distribution;
- an older debris boundary partly covered by later snow;
- an observation whose timestamp predates the latest weather event;
- a field note recommending continued restriction.

### Sheltered bench

A staging pocket with a different exposure history from the gully. It can serve as an observation point, rest location, communication relay, or later rich-encounter refuge if mechanics support that role.

### Upper traverse

A higher route segment whose appearance may be deceptively ordinary. Previous tracks can exist here without becoming a stability certificate.

### Pass shelter / maintenance cache

A persistent human-use feature containing logs, marker replacements, old closure notices, equipment custody records, or communication evidence. The shelter provides provenance, not omniscience.

## Investigation loop

The player begins with at least two claims that use different evidence bases.

A maintenance actor can truthfully report that the lower road was cleared and inspected within their mandate. A field observer can truthfully report that an upper feature remained unresolved when they visited. A trader or traveler can truthfully say that someone crossed. None of those statements alone establishes the state of the entire pass.

The player can inspect persistent features, compare timestamps, determine which report applies to which segment, identify observations made before or after relevant weather/world events, receive or recover records, and return to an observation point after semantic time advances.

The desired deduction is feature-scoped:

`this evidence supports this claim about this feature during this time window`

The loop should never require the player to solve a real-world avalanche forecast.

## Open explanations

Keep several explanations valid until canon review selects one or leaves the uncertainty durable.

- The lower road was correctly reopened while the upper traverse remained legitimately restricted.
- A later wind event changed one local accumulation after the maintenance inspection.
- A report is accurate but applies to a different feature than administrators assumed.
- Tracks belong to a maintenance team that used a limited-access route rather than ordinary public traffic.
- Old debris was mistaken for evidence of a new event.
- A public notice lagged behind a feature-scoped decision revision.
- A route observer generalized from a sheltered bench to a nearby exposed section.
- A Pokémon or wildlife movement created persuasive but incomplete evidence of passage.
- Several of these are simultaneously true.

Sabotage, criminal intent, and supernatural causation are not required.

## Actors and faction pressure

### Route maintenance crew

Goal: keep the crossing functional and avoid redoing work unnecessarily.

Knowledge boundary: knows its own work, observations and instructions; does not automatically know hidden slope state or every later report.

### Route authority or local administrator

Goal: make an access decision from incomplete evidence while balancing continuity of travel and credible risk reports.

Knowledge boundary: receives only explicit reports/publications/messages available through the global NPC information system.

### Shelter keeper / relay operator

Goal: maintain a reliable local record and support travelers.

Narrative use: can preserve logs, message timing, missed deliveries and who actually reached the pass.

### Convoy, trader, courier or community traveler

Goal: cross before a scheduling or supply consequence becomes costly.

Narrative use: creates pressure without becoming an antagonist.

### Ecological or field observer

Goal: preserve an accurate local record and avoid turning one observation into a mountain-wide claim.

### Resident Pokémon

Species remain unresolved. If later approved, their movement or habitat use can become another bounded observation. They cannot function as automatic hazard detectors or route-authority substitutes.

## Decisions and persistent consequences

Possible feature-scoped decisions include:
- reopen lower approach;
- keep upper traverse restricted;
- allow maintenance-only access to one segment;
- require monitoring before public reopening;
- reroute a scheduled convoy;
- keep the shelter operational while closing the exposed approach;
- publish a revision that narrows an earlier broad closure.

Consequences should persist separately. A delayed delivery, missed training appointment, stranded field team, shelter supply drawdown, ecological observation gap, public frustration, revised schedule, or later repair order can continue after the immediate route decision changes.

A later correction must not erase the history of the earlier decision or consequences already produced.

## Revisit structure

The same pass should remain useful after the first investigation.

Possible returns:
- after additional snowfall;
- after a calm interval;
- during thaw and runoff;
- when an old restriction is challenged by new evidence;
- when a prior delay affects another NPC obligation;
- when a route publication must be corrected;
- when a seasonal Pokémon observation becomes relevant;
- when maintenance work changes one feature but not its neighbors.

This allows a single place to accumulate history without forcing a new dungeon instance for each world event.

## Reduced implementation version

The reduced version requires no dynamic avalanche simulation.

World state uses ordinary persistent route features and authored states such as:
- `OPEN`;
- `RESTRICTED`;
- `MAINTENANCE_ONLY`;
- `CLOSED`;
- `MONITORING`.

Evidence records can include:
- `LOWER_ROUTE_CLEARED_OBSERVED`;
- `OLD_DEBRIS_BOUNDARY_OBSERVED`;
- `TRACKS_OBSERVED_SOURCE_UNRESOLVED`;
- `FIELD_REPORT_RECEIVED`;
- `OBSERVATION_STALE_AFTER_EVENT`;
- `LOCAL_STATE_UNRESOLVED`.

These are narrative/world-state descriptors, not PTU statuses.

Weather and snow-state changes occur between scenes through explicit authored world events. Unsafe tactical spaces become blocked route edges or authored scene boundaries. The player still investigates provenance, resolves conflicting claims, influences institutional decisions, and sees durable consequences.

## Intended mechanically rich version

Only after exact capability families are verified, a richer encounter may include moving through deep or uneven snow, visibility loss during active snowfall, changing terrain zones, a timed environmental transition, moving debris, rescue/interception, forced displacement, a shelter/refuge objective, Pokémon-assisted traversal, or a battle whose safe geometry changes during the encounter.

The rich version must preserve the same narrative premise. Missing PTU rules must never be recreated in Minecraft/Cobblemon/Craftics merely to make the scene look dynamic.

## Dependency classification

Targeting / footprints / range / LoS: ordinary verified contracts are sufficient for the reduced version. Snowfall, whiteout, concealment, elevation-specific visibility, or obscured targeting need dedicated evidence beyond ordinary LoS.

Base movement legality: ordinary verified movement can support the reduced version on open routes. Snow, ice, climbing, special footing, or species-specific traversal require source-backed contracts.

Complete movement including push/pull/knockback/interception/forced movement: required for moving snow/debris, forced slides, rescue pulls, interception, or displacement near exposed terrain. Current evidence remains partial.

Core calculations: ordinary deterministic calculations are usable. No custom snow-load, stability, temperature, or risk formula is proposed.

Action economy / initiative: ordinary ordering is usable. Environmental actions or interrupts need their exact legal contracts.

Full turn/round lifecycle: required for within-battle weather changes, delayed collapse/debris events, timed refuge windows, or scheduled environmental transitions beyond the currently verified lifecycle seams. Current evidence remains partial.

Full stateful damage pipeline: required for any fall, impact, cold, crushing, debris, or environmental damage. Current evidence remains partial.

Status lifecycle: required for any persistent PTU-backed condition. The reduced version authors none.

Terrain / weather / hazards / zones / reactions: required for dynamic snow/ice terrain, active snowfall, hazardous sectors, changing refuge geometry, or rescue reactions. Current evidence remains mixed/partial/blocking by subfamily.

Move-specific behavior: every Move used to change snow, ice, wind, visibility, movement or rescue must be verified individually.

Abilities: every Ability used for snow, Ice Body, traversal, weather, detection or protection must be verified individually.

Items: winter/rescue/survey equipment may be narrative objects until exact mechanical behavior is source-backed; no item bonus is invented here.

Trainer Features / perks: Survivalist, Topographer, Climatologist or any comparable specialization must be checked against project-authoritative sources and implementation before granting privileges or modifiers.

AI legal-action infrastructure: may enumerate only already supported legal actions.

AI tactical policy: general autonomous reasoning about dynamic winter hazards, evacuation, shelter selection, or rescue remains blocking.

Minecraft / Cobblemon / Craftics adapter/playback: may present route state, snowfall, barriers, tracks, debris and authoritative semantic events. It must not decide snow stability, legal movement, damage, status, NPC knowledge, or encounter outcomes.

## Canon questions deliberately left unresolved

Region and mountain range; pass name; nearby communities; climate; road/trail type; responsible institution; economic importance; shelter history; prior incidents; resident species; whether Avalugg/Bergmite belong here; true source of each report; final operational decision; seasonal water consequences; exact PTU/Caelo mechanics; and whether a rich tactical version should ever be enabled all remain open.