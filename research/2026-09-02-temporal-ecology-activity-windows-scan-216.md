# Temporal ecology, activity windows and human-pressure scan — pass 216

Status: RESEARCH / PROVENANCE — NOT CANON
Date: 2026-09-02
Implementation correction: 2026-09-03 — native Cobblemon spawn authority verified

## Why this pass exists

The repository already contains strong layers for persistent wild identity, species/individual tolerance, Trainer approach, alarm propagation, shared sites, field observation, access windows and seasonal incidents. The remaining gap is temporal ecology: the same physical site should not present the same wildlife opportunities, tolerance context or observable behavior at every hour simply because the Minecraft chunk is loaded.

This pass originally described temporal opportunity too close to a parallel Ouros spawn scheduler. That boundary is now corrected after checking current Cobblemon documentation.

Cobblemon already provides native spawn files under `spawn_pool_world` that control natural spawning, including time ranges and combinations with biome, block, light, moon phase and other conditions. Cobblemon Spawn Rules can additionally filter or reweight eligible spawns using world context. Ouros must reuse those systems for ordinary species-level natural spawning instead of recreating `day/night` availability in a second runtime.

The first Sendero wild canon already authorizes future time/weather/ecology windows while explicitly warning that one visible actor does not equal local abundance and that normal ecology should not remain deterministic. This research stays inside that boundary.

## Public research reviewed

### Cobblemon — native temporal spawn authority

Current Cobblemon documentation states that `spawn_pool_world` JSON files control how Pokémon spawn naturally and can express conditions as specific as a narrow clock interval combined with terrain, moon phase and biome. Spawn Rules provide global filter/weight components over spawn details and context. Cobblemon configuration also includes `savePokemonToWorld`, which allows Pokémon to persist across chunk/world reloads when enabled.

Reusable Ouros lesson: ordinary temporal availability belongs in Cobblemon spawn data and server world context. Ouros should not run a duplicate species spawn clock. Ouros adds authority only where narrative semantics exceed generic natural spawning: authored population state, provenance, a known persistent individual, memory/history, institutional observations, or a canon restriction that must gate projection.

Sources:
- Cobblemon Wiki — Spawn Pool World: https://wiki.cobblemon.com/index.php/Spawn_Pool_World
- Cobblemon Wiki — Spawn Rules: https://wiki.cobblemon.com/index.php/Spawn_Rules
- Cobblemon Wiki — Config (`savePokemonToWorld`): https://wiki.cobblemon.com/index.php/Config
- Cobblemon Wiki — Pokémon/Behaviour (time ranges also used for resting behaviour): https://wiki.cobblemon.com/index.php/Pok%C3%A9mon/Behaviour

### New Pokémon Snap — same place, different research window

Official New Pokémon Snap material repeatedly presents the same research areas in Day and Night forms. Nintendo's Australian description frames midday and starry-night traversal as opportunities to observe distinct Pokémon behaviours. The official free-update material similarly lists Secret Side Path, Mightywide River and Barren Badlands as Day/Night research areas and describes Pokémon hiding, gathering or showing different behavior within the same physical area.

Reusable Ouros lesson: a location identity can remain stable while the set of observable behaviors changes with the research window. Time should alter opportunities and evidence rather than replace the site with a separate map.

Sources:
- New Pokémon Snap — Nintendo Australia: https://www.nintendo.com/au/games/nintendo-switch/new-pokemon-snap/
- New Pokémon Snap free update — official Pokémon site: https://newpokemonsnap.pokemon.com/en-ca/free-update/
- New Pokémon Snap exploration — official Pokémon site: https://newpokemonsnap.pokemon.com/en-au/explore/

### Human disturbance and nocturnality

Gaynor et al. (2018) synthesized 62 mammal species across six continents and found a broad increase in nocturnality under human disturbance. UC Berkeley's summary reports an average 1.36-fold increase in nocturnality and stresses that animals responded to multiple forms of human presence, including disturbance that did not necessarily pose a direct lethal threat.

Reusable Ouros lesson: human activity can move wildlife use of a site into a different time window. This supports context-sensitive behavior in populated regions, but it does not authorize a universal `urban = nocturnal` rule. Species, population and individual evidence remain necessary.

Source:
- UC Berkeley, “Mammals going nocturnal to avoid humans” (summary of Gaynor et al., Science 2018): https://vcresearch.berkeley.edu/news/mammals-going-nocturnal-avoid-humans

### Human pressure can change relationships between species, not only individual schedules

A 2026 Nature Communications meta-analysis examined 480 mammalian predator–prey / intraguild-predator dyads from 57 studies. It found strong changes in diel activity under human disturbance but no single universal direction for temporal overlap. Effects differed with ecological relationship and relative body size.

Reusable Ouros lesson: a shift in human traffic can alter when two populations overlap without implying that every species moves in the same direction. Cobblemon can express authored spawn availability/weight conditions, while Ouros research records preserve why a regional datapack rule exists and whether it is canon-approved.

Source:
- Nature Communications, “Predator-prey temporal niche partitioning under human disturbance: a meta-analysis” (2026): https://www.nature.com/articles/s41467-026-69113-9

### Corridors can have hourly use patterns under different human landscapes

Research on African elephant corridor use in Botswana found different diel use patterns across human-modified landscapes. The study reports urban corridors being used both diurnally and nocturnally while agricultural corridors were used only nocturnally, with seasonality and landscape affecting presence.

Reusable Ouros lesson: route use can be temporal and local. A Sendero crossing may be physically open all day while different populations prefer different windows. A schedule observed at one corridor should not silently propagate to every route in the region.

Source:
- Frontiers in Conservation Science, “Who is adjusting to whom?: Differences in elephant diel activity in wildlife corridors across different human-modified landscapes” (2022): https://www.frontiersin.org/journals/conservation-science/articles/10.3389/fcosc.2022.872472/full

### Infrastructure habituation can coexist with timing changes

A long-term review of Tibetan antelope migration around the Qinghai–Tibet Highway and Railway describes animals using wildlife corridors and crossing roads during periods of lower traffic, while some individuals forage or rest near infrastructure. The work emphasizes adaptation over time rather than a simple permanent avoidance response.

Reusable Ouros lesson: habituation and temporal avoidance can coexist. A population can tolerate the physical presence of infrastructure while still selecting lower-traffic windows for particular activities.

Source:
- Ecosystem Health and Sustainability, “Adaptation of migratory Tibetan antelope to infrastructure development” (2021): https://spj.science.org/doi/10.1080/20964129.2021.1910077

### PTU living-world community signal

Public PTU living-world recruitment material continues to emphasize persistent worlds that change from player actions and asynchronous participation. This is weaker evidence than rules text or a campaign log, but it reinforces a useful implementation requirement: temporal ecology should persist as shared server/world state rather than depend on one player's client clock.

Source:
- r/PokemonTabletop, “Super Pokémon Online - PTU Living World RPG” (2025): https://www.reddit.com/r/PokemonTabletop/comments/1mkct0y/super_pok%C3%A9mon_online_ptu_living_world_rpg/

## Corrected authority split

```text
Minecraft server world state
(time / weather / light / biome / moon / location)
        |
        v
Cobblemon spawn_pool_world + Spawn Rules
(generic species eligibility and weight)
        |
        v
Cobblemon natural spawn candidate / existing world Pokémon
        |
        +--> ordinary generic population projection
        |
        v
Ouros narrative/world constraints
(authored population state, canon gates, persistent identity, history,
 observation provenance, disturbance/social context)
        |
        v
Ouros wild behavior/tolerance policy
(species -> population/context -> individual -> Trainer behavior)
        |
        v
AutoPTU when structured mechanics begin
        |
        v
Minecraft/Cobblemon/Craftics playback
```

Important boundary: Cobblemon owns ordinary natural spawn eligibility and weighting. Ouros may constrain, annotate or replace projection only when a canon/world-state fact requires stronger identity or population semantics. Minecraft/Cobblemon still do not become battle-state authority.

## Derived structures for Ouros

### `WILD_ACTIVITY_PROFILE`

Proposed, not canon-approved.

This is now explicitly a provenance/design record, not a second runtime spawn scheduler. When an approved profile can be represented by native Cobblemon conditions, the implementation target should be a datapack spawn condition/rule with a trace back to this record.

```yaml
wild_activity_profile:
  subject_ref: population_or_persistent_individual
  site_ref: null
  provenance_refs: []
  confidence: OBSERVED | SOURCE_BACKED | PROVISIONAL
  preferred_windows: []
  tolerated_windows: []
  activity_modes_by_window: {}
  human_traffic_sensitivity: null
  seasonal_conditions: []
  recent_disturbance_refs: []
  cobblemon_spawn_mapping_ref: null
  notes: []
```

For a generic population, preferred temporal availability should normally map to Cobblemon spawn conditions/weights. For a persistent named/identified individual, the profile may instead inform availability/location transitions without cloning that individual through generic spawning.

### `SITE_ACTIVITY_WINDOW`

Proposed, not canon-approved.

```yaml
site_activity_window:
  site_ref: null
  window_id: null
  world_time_bounds: null
  routine_human_activity: LOW | MODERATE | HIGH | UNKNOWN
  infrastructure_activity_refs: []
  population_activity_refs: []
  observation_quality_notes: []
  authored_access_constraints: []
```

This remains separate from the administrative `ACCESS_WINDOW`. It also does not replace Cobblemon spawn conditions. Its role is narrative/research context: why an observation differs, why a datapack condition was authored, or why a human activity pulse matters.

### `TEMPORAL_SITE_OBSERVATION`

Proposed, not canon-approved.

```yaml
temporal_site_observation:
  observation_id: null
  site_ref: null
  timestamp: null
  observer_ref: null
  subject_ref: null
  evidence_kind: DIRECT | TRACE | SOUND | ABSENCE_WITH_EFFORT
  effort_record: null
  human_traffic_context: null
  disturbance_refs: []
  observation_payload: null
  interpretation_refs: []
```

`ABSENCE_WITH_EFFORT` is deliberately not equivalent to `ABSENT_FROM_SITE`. A spawn not occurring during one visit is not ecological proof of absence.

## Temporal ecology decision order

For ordinary wild populations:

```text
authored/canon-approved species-population profile
-> Cobblemon spawn conditions / Spawn Rules
-> current server world context
-> eligible natural spawn opportunity
-> Ouros population/canon gates if applicable
-> world Pokémon projection
-> behavior/tolerance evaluates actual Trainer actions
-> AutoPTU owns structured legality and resolution
```

For a persistent individual:

```text
persistent identity/state/history
+ server world context
+ approved activity/location policy
-> authoritative availability/location
-> existing/saved Cobblemon entity may project that identity
-> never create a generic duplicate because a spawn window matched
```

Time of day does not grant a Move, Ability, Skill bonus, capture modifier or Status effect unless PTU/Caelo/Kairos or an approved Ouros rules profile explicitly supplies that mechanic.

## Canon cross-check

CANON-APPROVED constraints preserved:

- `ouros.marea.wild.sendero_lower_shelf.fletchling.v1` remains the first bounded population record.
- `ouros.marea.encounter.sendero_lower_shelf.fletchling.0` remains the first persistent encounter slot and keeps its frozen PTU 1.05 blueprint.
- The current Fletchling has Overland 3, Sky 5, Big Pecks, Tackle and Growl at level 5; this pass changes none of those facts.
- Minecraft entity visibility cannot author canonical species, level, HP, moves, Ability, status, injuries or battle result.
- The canon explicitly permits later time/weather/ecology windows and multiple species while rejecting deterministic single-species ecology as the final model.

PROPOSED:

- provenance-backed activity profiles and observations;
- time-sensitive human-traffic context;
- repeated observation as the way to establish a local activity pattern;
- mapping approved generic population windows into native Cobblemon spawn data instead of an Ouros duplicate scheduler.

UNCERTAIN / deliberately unresolved:

- the exact active hours of the canonical Sendero Fletchling population;
- whether this specific persistent Fletchling follows a stable diel schedule;
- the second Sendero species/population;
- how weather and season interact with the clock;
- any PTU mechanical modifier attached to visibility, Stealth, perception, capture or nocturnal conditions.

The supplied Caelo provenance already notes territorial/diurnal Fletchling behavior as comparative living-world inspiration. That can inform a future authored profile but should be re-audited before exact hours or deterministic behavior are approved.

## Anti-patterns

Do not implement `if night -> spawn species X` inside Ouros when native Cobblemon spawn conditions can express the requirement.

Do not use an Ouros scheduler to compete with `spawn_pool_world` or Spawn Rules.

Do not force-spawn or duplicate a persistent individual merely because a generic species spawn condition matches.

Do not equate Cobblemon despawn or failure to spawn with canonical ecological absence.

Do not equate a quiet route with safe capture. Lower human traffic can reduce habituated background disturbance while making an unusual Trainer more salient.

Do not treat one observation as a species law.

Do not encode darkness as a PTU accuracy/LoS penalty in Minecraft unless the rules authority supplies such an effect.

## Design consequences

Temporal ecology creates useful player choices without requiring another quest marker. A Trainer can revisit the same site at another hour, deliberately observe a transition, choose a low-traffic route window, compare direct sightings with traces, or discover that a familiar individual uses the site differently after disturbance.

Cobblemon should do the ordinary heavy lifting for species-level day/night/weather/light availability. Ouros records why those conditions exist, handles exceptional canon/population constraints, preserves persistent individual identity/history and interprets consequences.

It also creates consequences for institutions. Nerea and Ema can disagree about sampling because they observed different windows. Mara can schedule route checks for safety while accidentally biasing ecological observations toward daylight. Pia's deliveries can generate regular human-pressure pulses that wildlife learns to tolerate or avoid. These differences can produce evidence and planning problems without inventing antagonists.

## Mechanical boundary

Temporal spawning is primarily a Cobblemon/Minecraft adapter concern for ordinary populations, while population truth and persistent identity remain Ouros world-state concerns. Structured encounter mechanics remain AutoPTU concerns.

The reduced form needs the server world clock/context already consumed by Cobblemon, native spawn conditions for generic populations where applicable, persistent state for authored individuals, base movement where the player approaches or withdraws, and adapter playback. If a battle begins, use the normal verified BattleSpec path.

A richer version may require range/LoS, complete movement, status effects, Items, Features, AI legal actions and tactical policy if the Trainer actively stalks, contains or interferes with a wild Pokémon. Weather/hazards/reactions become dependencies only when the authored encounter actually uses those mechanics; dusk itself does not justify pretending those families exist.

## Research outcome

The corrected architecture uses Cobblemon rather than duplicating it. Generic temporal spawning belongs in Cobblemon datapacks and Spawn Rules. Ouros supplies provenance, population/canon constraints, persistent identity, memory, observations and behavior. AutoPTU remains authoritative once PTU mechanics are invoked.