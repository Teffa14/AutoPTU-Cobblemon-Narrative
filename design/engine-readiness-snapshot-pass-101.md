# Engine Readiness Snapshot — Pass 101

Status: implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Live evidence inspected

AutoPTU-Java head observed during this pass:

`add15a4f9fcd55eb174d7f8b3a2dc9a4f4aa4655`

Latest relevant commit:

`Match Python round cleanup ordering (#136)`

This commit reorders canonical ROUND_START temporary-effect cleanup so Java matches the Python ordering contract more closely. The specific change moves the temporary-effect cleanup hook earlier in the lifecycle sequence. It strengthens one narrow but important lifecycle-ordering guarantee.

It does not establish complete round lifecycle parity, complete temporary-effect coverage, broad reactions, objective AI or any festival/crowd subsystem.

AutoPTU main remains:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Recent visible Python work remains Career-oriented and does not justify any tactical capability promotion.

The current Java README still treats Python as authoritative while the port remains incomplete and continues to list large unfinished families including full battle state/damage/status behavior, terrain/hazards/forced movement/reactions, complete hook registries/transcript parity, tactical AI and Minecraft/Cobblemon integration.

## Permanent capability map

### VERIFIED

`targeting / footprints / range / LoS`

Static tactical geometry, target footprints, range and geometric LoS remain verified.

Pass 101 non-inference:

- a procession route does not become a targeting line;
- a crowd does not block LoS unless represented by validated tactical objects;
- a festival stall is not automatically cover;
- a bell tower or stage is not targetable without an object-target contract;
- decorative lighting does not alter vision mechanics.

`base movement legality`

Established base Shift/Jump and known movement-mode legality remain verified.

Pass 101 non-inference:

- participating in a procession grants no movement bonus;
- carrying a ceremonial object does not change movement unless an exact rule says so;
- being an organizer does not permit moving through occupied squares;
- a public route is not a tactical legal path by itself.

`core calculations`

Established calculation primitives remain verified.

Pass 101 adds no luck formula, ritual modifier, crowd morale calculation, festival fatigue, ceremony score or participation bonus.

`action economy / initiative`

Established action economy/initiative remain verified.

The live Java branch continues to improve authoritative ROUND_START state ordering, but festival state does not alter initiative by default.

Pass 101 non-inference:

- ceremonial role -> initiative bonus;
- parade position -> free action;
- public acclaim -> action budget;
- festival music -> Speed bonus.

`AI legal-action infrastructure`

Deterministic legal-choice generation remains verified.

This does not prove tactical policy goals such as:

- PROTECT_PROCESSION;
- WITHDRAW_FROM_CROWD;
- CLEAR_ROUTE;
- ESCORT_OFFICIAL;
- AVOID_CIVILIANS;
- REACH_CEREMONIAL_OBJECTIVE;
- HOLD_EXIT;
- DEESCALATE.

Those require objective-aware tactical policy.

### PARTIAL

`full turn / round lifecycle`

Representative phase/round-start ordering, temporary-effect cleanup, initiative, field-effect progression, delayed-hit behavior, Trainer AP/action reset, declared-action cleanup and Trainer Feature ordering slices exist.

The latest commit improves cleanup ordering relative to Python.

Still PARTIAL because the complete set of START/END effects, durations, interrupts, Statuses, Abilities, Features, delayed effects and transcript behavior is not proven.

An annual observance schedule is an overworld clock. It must never be encoded as battle-round lifecycle.

`full stateful damage pipeline`

Representative authoritative damage paths exist.

Still PARTIAL.

Pass 101 non-inference:

- crowd crush -> damage;
- falling decoration -> damage;
- ritual fire -> damage;
- thrown festival object -> damage;
- broken stall -> injury.

Those require exact environment/object rules.

`status lifecycle`

Representative statuses and lifecycle hooks exist.

Still PARTIAL.

Pass 101 non-inference:

- blessing -> status immunity;
- loud festival -> Confused;
- incense -> Sleep/Poison;
- emotional ceremony -> Focused/Enraged;
- mask -> Fear immunity;
- prayer -> cured Status.

`move-specific behavior`

Representative Move slices exist.

Still PARTIAL.

A festival challenge can depend on a Move only after that exact Move behavior is verified. The presence of a symbolic song, flame, bell, mask, offering or dance does not stand in for a Move.

`abilities`

Representative Ability hooks exist.

Still PARTIAL.

No Ability becomes a generic festival capability. Examples of prohibited inference:

- Soundproof = immune to all festival sound;
- Illuminate = public-lighting service;
- Plus/Minus = electrical event infrastructure;
- Pickup = festival prize discovery;
- Run Away = procession withdrawal AI.

`items`

Representative held-item behavior exists.

Still PARTIAL.

Masks, ribbons, lanterns, bells, costumes, offerings, commemorative tokens and ceremonial tools are overworld/material-culture objects unless an exact PTU Item definition says otherwise.

`Trainer Features / perks`

Representative Feature infrastructure and several concrete Features exist.

Still PARTIAL.

Organizer, steward, priest-like role, volunteer, performer, judge, marshal or ceremonial leader are narrative/institutional roles unless exact PTU/Caelo Features are validated.

### BLOCKING

`complete movement including push / pull / knockback / interception / forced movement`

Still BLOCKING as a complete family.

Pass 101 impact:

- no true in-grid moving procession;
- no dynamic escort lane;
- no crowd displacement;
- no interception corridor around a ceremonial object;
- no live rerouting through moving participants;
- no objective race to a landmark when complex movement is required.

`terrain / weather / hazards / zones / reactions`

Still BLOCKING as a complete family.

Pass 101 impact:

- temporary stalls/decorations do not create cover or terrain automatically;
- lanterns/torches do not create fire zones;
- rain on a festival does not automatically initialize PTU Weather;
- ceremonial boundaries do not create zones;
- spectators do not create reaction triggers;
- food spills do not create slippery terrain;
- loud sound does not create a Sonic field effect.

`AI tactical policy`

Still BLOCKING.

This is a principal blocker for mechanically rich festival encounters. Legal actions alone do not make actors protect civilians, withdraw from a crowd, preserve a procession route, race toward a landmark, avoid ceremonial objects or pursue a non-KO objective.

`Minecraft / Cobblemon / Craftics adapter and playback`

Still BLOCKING.

There is no verified end-to-end contract for projecting temporary event geometry, crowds, processions, ceremonial objects, nested activity state or semantic objectives into Minecraft while preserving world-state authority and AutoPTU-Java battle authority.

## Pass 101 specific overworld blockers

`CULTURAL_OBSERVANCE_STATE`
Persistent identity across editions, independent of one `PUBLIC_EVENT` execution.

`OBSERVANCE_RECURRENCE_POLICY`
Date/season/phenology/celestial/institutional/historical trigger authority.

`OBSERVANCE_EDITION_HISTORY`
Append-only edition records with preparation, schedule, incidents, archive and aftermath.

`RITUAL_PRACTICE_STATE`
Meaning and sequence without invented mechanical effects.

`OBSERVANCE_PARTICIPATION_PERMISSIONS`
Guest/local/steward/official/media/performer roles and access scope.

`OBSERVANCE_PREPARATION_PROJECTS`
Staffing, volunteer work, temporary infrastructure, logistics and cleanup.

`CEREMONIAL_OBJECT_CUSTODY`
Stable object identity/provenance through annual use and handoffs.

`OBSERVANCE_NESTED_ACTIVITY_HANDOFF`
Contest/sport/battle/market/performance/science activities remain under their own mechanics.

`OBSERVANCE_TO_PUBLIC_MEMORY`
Edition outcomes enter public memory without rewriting world truth.

`OBSERVANCE_TO_TOURISM_PRESSURE`
Visitor surge and branding remain distinct from local meaning.

`OBSERVANCE_TO_MINECRAFT_PROJECTION`
Decorations/crowds/stalls are projections of current edition state; chunk reload cannot restart preparation or restore previous editions.

`OBSERVANCE_TO_BATTLE_SNAPSHOT`
A public event can freeze a safe battle arena without importing crowd/event logic into the battle core.

## Encounter dependency summary

### Procession Route Interruption — FULL

VERIFIED foundations:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL when exact combat content invokes them:

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING for FULL:

- complete movement/interception/forced movement;
- terrain/weather/hazards/zones/reactions if temporary route features matter tactically;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics playback.

REDUCED viability:

HIGH. Pause the procession, evacuate noncombatants, freeze a static street/square map, resolve a legal battle, then continue the event through world state.

### Festival Grounds Evacuation — FULL

VERIFIED foundations:

- static targeting/geometry;
- base movement legality for combatants;
- core calculations;
- action economy/initiative;
- legal-action generation.

BLOCKING for FULL:

- crowd/civilian movement objectives;
- complete movement/interception;
- AI tactical policy;
- dynamic temporary-object interaction;
- hazards/weather if invoked;
- adapter/playback.

REDUCED viability:

HIGH. Resolve crowd evacuation before opening AutoPTU and use a static perimeter.

### Bell Tower Challenge — FULL

VERIFIED foundations:

- static battle geometry if a battle checkpoint exists;
- base movement legality inside that checkpoint;
- core calculations;
- action economy/initiative;
- legal-action generation.

Potential PARTIAL dependencies:

- exact Moves/Abilities/Features used by competitors.

BLOCKING for a true tactical race/climb:

- complete movement when climbing/interception/forced movement matters;
- AI tactical policy for REACH_OBJECTIVE behavior;
- adapter/playback;
- exact PTU/Caelo Skills/Features if traversal is mechanically resolved outside battle.

REDUCED viability:

HIGH. Resolve traversal as overworld route/validated Skill challenge, use static battle checkpoints if needed, and treat the final bell interaction as cultural world state only.

## Mechanical non-inference summary

Pass 101 does not establish:

- festival buffs;
- ritual buffs;
- blessings;
- lucky items;
- luck stats;
- healing ceremonies;
- friendship/Loyalty gains;
- capture bonuses;
- evolution triggers;
- automatic Weather;
- crowd morale;
- spectator reactions;
- ceremonial equipment effects;
- holiday-only Move effects;
- rites that grant Trainer Features;
- procession movement rules;
- civilian battle rules.

## Unresolved rules/canon questions

- Which recurring observances are present in Ouros before players arrive?
- Which are civic, seasonal, ecological, institutional, sacred, memorial or purely recreational?
- Which communities may have internal participation restrictions?
- Which observances are tied to phenology rather than fixed dates?
- How much can editions advance while a player is offline?
- Which personal ceremonies require explicit player presence/consent?
- How are crowds represented without thousands of NPC entities?
- What exact PTU/Caelo rules govern any nested Skill challenge, Contest, battle, ceremonial Item, supernatural effect or Pokémon participation?
- Which ritual claims, if any, correspond to real supernatural phenomena in Ouros canon?

The full primary Caelo corpus was not reliably retrievable during this pass. No Caelo-specific festival, ceremony, ritual or rite mechanic is asserted.
