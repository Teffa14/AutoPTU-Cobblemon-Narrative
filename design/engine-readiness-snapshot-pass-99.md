# Engine Readiness Snapshot — Pass 99

Status: IMPLEMENTATION-READINESS EVIDENCE. This snapshot does not create PTU rules or Ouros canon.
Date: 2026-08-28

## Scope

Pass 99 adds winter mountain-pass operational continuity: stable winter sectors, field observations, assessments, clearing history, observed snow-slide events, temporary winter access, refuge use and staged reopening.

Narrative baseline before Pass 99 writes: `aee7933fe23c789fb249e2de254188e6e8063895`.

Read-only evidence inspected:

- complete recursive Narrative repository inventory and design directory;
- Weather Forecast & Preparedness;
- Roads/Bridges/Detours;
- Crisis/Rescue/Recovery;
- Pass 98 readiness snapshot;
- permanent Cobblemon runtime authority boundary;
- current AutoPTU-Java commits;
- current AutoPTU commits;
- PTU 1.05 Movement and Positioning evidence for Slow Terrain;
- PTU 1.05 named Hail/Ice Move evidence.

## Live engine evidence

AutoPTU-Java head remains `39b81222af080dd5b2db9b3efdfe742b746d5f5d`, #255, “Freeze intercept orchestration control flow”. The commit freezes a specific `_attempt_intercept` path against the pinned Python oracle, including candidate/check/resource/position checkpoints and melee forced movement for that path.

This remains narrow evidence. It does not verify competing reactions, generalized reaction ordering, broad knockback, all forced-movement sources, environmental displacement, dynamic snow hazards, complete Move/Ability/Item/Trainer Feature hooks, objective-aware tactical policy or complete Minecraft playback.

AutoPTU head advanced from the Pass 98 baseline to `80d5735208bc1a7fe836b107736e98ea964d6259`, merging Career bootstrap protection for blocked browser storage. This is Career client stability and persistence hardening. It adds no tactical battle family.

No permanent capability category is promoted in Pass 99.

## PTU 1.05 winter-specific evidence

PTU 1.05 Movement and Positioning explicitly defines Slow Terrain and lists deep snow and even ice as examples that may qualify. In Slow Terrain, movement cost increases according to the governing PTU rule.

This is useful but narrow:

- authored reviewed deep-snow squares may be representable using an existing PTU terrain rule;
- not every snow-covered Minecraft block is automatically Slow Terrain;
- exact battlefield mapping still requires reviewed geometry and adapter support;
- this evidence does not create avalanche, cold, burial, visibility, falling or snowstorm mechanics.

PTU also contains Hail Weather and named Ice Moves including Blizzard and Avalanche. Those are specific battle rules. The Move named Avalanche is not an environmental avalanche engine. Ordinary overworld snowfall does not become Hail automatically.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Family-level geometry/range/LoS support remains sufficient for static reviewed battlefields. This does not provide blowing-snow visibility penalties or dynamic occlusion.

`base movement legality`

Base movement and established movement-mode legality remain verified. PTU Slow Terrain is governing rules evidence, but full winter-terrain authoring still requires deliberate mapping rather than native block behavior.

`core calculations`

Core stat, DB, accuracy, type and related primitives remain verified. They do not define environmental avalanche or cold damage.

`action economy/initiative`

Typed action budget and deterministic initiative/order remain verified.

`AI legal-action infrastructure`

Legal-action enumeration remains verified. It does not provide withdrawal, shelter, route-protection or hazard-avoidance policy.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

PARTIAL. Push/Pull and the frozen Intercept orchestration path have substantial evidence. Family-wide reactions, broad knockback and all environmental displacement sources remain incomplete. An avalanche cannot force-move actors merely because forced movement exists elsewhere.

`full turn/round lifecycle`

PARTIAL. Existing phases/action budgets do not establish all behavior needed for changing snow/weather zones, delayed collapse, burial clocks or multi-round environmental transitions.

`full stateful damage pipeline`

PARTIAL. Named damage behavior exists. No verified generic avalanche-impact, environmental cold, fall, burial or suffocation pipeline exists.

`status lifecycle`

PARTIAL. Representative statuses are implemented. No environmental winter condition may create Frozen, Slowed or another status without an exact governing effect and engine contract.

`move-specific behavior`

PARTIAL. Specific Ice/Weather Moves exist in the rules and representative engine coverage exists, but registry-complete behavior is not verified. Move names cannot be repurposed as environmental systems.

`abilities`

PARTIAL. Individual Abilities exist. Their presence does not establish generic cold resistance, snow traversal or avalanche sensing.

`items`

PARTIAL. Representative Item behavior does not establish winter equipment, rescue gear or environmental modifiers.

`Trainer Features/perks`

PARTIAL. Existing representatives do not establish full winter-rescue, environmental or reaction coverage.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

BLOCKING for rich winter encounters. Dynamic snowfall, blowing-snow visibility, ice changes, avalanche paths, moving debris, burial areas, collapsing snow, cold exposure, changing exclusion zones, environmental Hail handoff and competing reactions need exact rules and verified engine contracts.

The presence of PTU Slow Terrain is not enough to promote this family. It is one supported terrain behavior, not complete terrain/weather/hazard/zone/reaction coverage.

`AI tactical policy`

BLOCKING. Legal action generation does not establish policy for withdrawal, preserving an escape route, defending a refuge approach, avoiding avalanche terrain, separating from civilians or holding a perimeter.

`Minecraft/Cobblemon/Craftics adapter/playback support`

BLOCKING. Minecraft can represent snow/ice/weather/geometry, while the authoritative adapter remains unfinished. Native powder-snow behavior, ice slipperiness, weather, block updates and entity proximity may not decide PTU state.

## Encounter readiness — Pass Closure Withdrawal

Full intended form wants reviewed Slow Terrain where applicable, several withdrawal routes, Intercept/forced movement, possible visibility or exclusion effects, objective-aware AI and authoritative playback.

Current profile: REDUCED.

Safe reduced form:

- complete route closure and ordinary withdrawal in Ouros state before battle;
- remove travelers, workers, equipment and nonparticipants;
- select combatants explicitly;
- use a static reviewed approach/clearing/refuge edge;
- use authored PTU Slow Terrain only if exact cells are deliberately mapped and tested;
- otherwise keep snow visual;
- do not simulate avalanche, burial, cold, live visibility changes or changing snow;
- battle may secure the immediate perimeter only;
- Winter Operations/Roads/Travel retain reopening authority.

## Encounter readiness — Slide Debris Search Perimeter

Full intended form wants protected lanes, route-control objectives, complete reactions/forced movement, reviewed terrain, tactical AI and any future exact burial/extraction rules.

Current profile: REDUCED.

Safe reduced form:

- suspend active search/rescue movement before battle;
- keep debris, unknown search subjects and responders outside the BattleSpec;
- fight on a verified stable perimeter;
- do not derive injury, burial or location from tactical outcome;
- battle cannot clear the route;
- Crisis/search and clearing operations resume afterward.

## Encounter readiness — Winter Refuge Approach

Full intended form wants reviewed winter terrain, protection/withdrawal objectives, exact Weather/visibility effects if ever verified, complete reactions, tactical AI and adapter playback.

Current profile: REDUCED.

Safe reduced form:

- keep refuge occupants inside;
- close the approach operationally;
- use a static safe battle area;
- no environmental cold, storm or avalanche effects;
- refuge availability remains owner-system state after combat.

## Cobblemon/Minecraft consequence

The binding architecture remains:

`Ouros encounter/world state -> AutoPTU BattleSpec -> AutoPTU authoritative state/result -> adapter -> Minecraft/Cobblemon presentation`

Safe presentation candidates include mountain/snow geometry, controlled snow and weather visuals, shelters, barriers, signs, particles, sounds, Pokémon models/forms/poses/animations/cries, UI, world coordinates, networking and persistence hooks.

Adapter-required work includes stable winter-sector geometry bindings, projection of closures/temporary access, exact reviewed conversion of snow/ice surfaces into AutoPTU terrain cells, stable actor identity and semantic battle playback.

Minecraft/Cobblemon must never decide:

- combatants from proximity;
- PTU Slow Terrain directly from block type without reviewed mapping;
- Hail or other PTU Weather from native weather;
- damage/status from powder snow, freezing or block contact;
- avalanche displacement from falling/changing blocks;
- access reopening from visual clearing;
- Pokémon responder competence from Type/species presentation;
- battle result.

## Pass 99 readiness conclusion

The new winter layer can ship as world-state continuity now: observation provenance, sector identity, assessment revision, clearing history, partial closure/reopening, temporary access, refuges, ecological handoffs, noncombat investigations and reduced encounter forms.

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: complete movement including push/pull/knockback/interception/forced movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback support.

## Unresolved canon questions

Pass 99 leaves open every setting choice about regional winter climate, specific passes, operating institutions, seasonal closure practice, warning terminology, clearing technology, shelters, communications, sacred/protected zones and Pokémon winter-work roles.

## Unresolved mechanical questions

Still unsupported or insufficiently verified:

- automatic overworld-snow to Slow Terrain mapping;
- snow/blizzard visibility effects;
- overworld storm to Hail mapping;
- environmental cold/exposure;
- generic avalanche impact/forced movement;
- burial/suffocation/extraction;
- cornice/fall/collapse behavior;
- changing snow zones during rounds;
- rescue/carry actions;
- snow-clearing Move/Capability conversions;
- generic environmental cold immunity;
- winter-equipment bonuses.

No answer is invented by this snapshot.