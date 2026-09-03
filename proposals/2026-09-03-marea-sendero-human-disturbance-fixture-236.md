# Marea / Sendero human disturbance fixture — Pass 236

Status: PROPOSED REGRESSION FIXTURE
Date: 2026-09-03

## Scope

Use the existing canon-approved Sendero lower-shelf Fletchling population as the first deterministic disturbance/habituation fixture. This does not redefine Fletchling globally and does not create new Marea species canon.

Population under test:
`ouros.marea.wild.sendero_lower_shelf.fletchling.v1`

Site:
`ouros.marea.sendero_vidrio`

## Narrative premise

A normally low-traffic shelf begins receiving repeated player and survey traffic. The same wild population remains present, but individual visibility and response changes over several in-world days.

The player can notice that approach distance changes before any battle begins. A superficially calmer population may still show reduced feeding time or delayed return to the shelf after peak traffic.

## Deterministic test sequence

### Window A — baseline

- low foot traffic;
- no pursuit;
- no battle pressure;
- no deliberate feeding;
- normal authored resources available.

Expected ecology result:
- population size unchanged;
- baseline tolerance retained;
- ordinary diurnal projection eligibility remains possible.

### Window B — repeated harmless traffic

Apply repeated human-presence observations without chase, capture request or battle.

Expected ecology result:
- `harmless_exposure_memory` rises;
- compatible individual/population response may reduce avoidance pressure;
- canonical HP/status/moves/Ability remain untouched;
- no encounter starts automatically.

### Window C — harmful pursuit event

Record a pursuit/harassment exposure without resolving it through vanilla Minecraft damage.

Expected ecology result:
- `harmful_exposure_memory` rises;
- avoidance and/or activity-shift pressure rises;
- visibility may decrease or move to a lower-traffic window;
- population size remains unchanged unless a separate canonical demographic event occurs.

### Window D — recovery

Remove abnormal traffic for an implementation-configured period.

Expected ecology result:
- short-term pressure decays;
- memories decay more slowly than immediate disturbance;
- chunk unload/reload does not reset exposure state;
- persistent individuals keep their own overrides if the runtime supports them.

## Observation quest wrapper

Working title: Quiet Shelf Survey.

A station log reports fewer daytime sightings despite no evidence of a population crash. The player is asked to compare observation windows, not to defeat or capture Pokémon.

Useful evidence:
- sighting time;
- return latency after a person passes;
- feeding interruptions;
- use of cover;
- distance before retreat;
- whether activity resumes after traffic falls.

Successful conclusion can distinguish at least three explanations:
1. true absence or demographic loss;
2. visibility reduction caused by avoidance/activity shift;
3. continued visibility with elevated welfare cost.

The quest should not expose hidden numerical state directly.

## Reduced encounter version

No tactical encounter is required. The full fixture can run as persistent world state plus Cobblemon projection and observation evidence.

If the player deliberately escalates to battle, only explicit combatants hand off to AutoPTU. Nearby population members remain outside the tactical grid unless Ouros explicitly selects them.

## Rich encounter version

Possible later scenario: a disturbed adult guards access to a retreat corridor while juveniles/noncombatants leave the shelf.

Additional capability dependencies:
- complete movement/interception/forced movement: PARTIAL;
- full turn/round lifecycle for timed retreat: PARTIAL;
- terrain/zones/reactions for corridor control: MIXED/PARTIAL/BLOCKING;
- move-specific behavior/abilities/items/Trainer Features: PARTIAL and content-specific verification required;
- AI tactical policy for defend-withdraw priorities: BLOCKING as complete family;
- Minecraft/Cobblemon/Craftics playback/writeback: PARTIAL/BLOCKING end-to-end.

The reduced version preserves the same ecological premise without those dependencies.

## Acceptance assertions

- population identity remains constant through all windows;
- no generic spawn row is allowed to duplicate a persistent individual;
- approach behavior can change without battle-state mutation;
- tolerance and welfare can diverge;
- harmful and harmless exposure are distinguishable;
- recovery is gradual;
- no Minecraft despawn is interpreted as emigration or death;
- any battle is an explicit handoff.

## Canon questions intentionally left open

- exact tolerance baseline for the Sendero population;
- numeric memory/decay constants;
- whether Fletchling individuals generalize experience from one human to all humans;
- whether a juvenile/nesting context exists at this exact shelf;
- which additional Marea species later occupy high-disturbance or subsidy niches.
