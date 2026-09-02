# Engine Readiness Snapshot — Pass 196

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-01
Narrative head before this pass: `7187978b17553da62bfc39b5aae99cad7da11049`

Read-only engine repositories:

- AutoPTU-Java head inspected: `09fc8bcf22c18d3106718a9d98005aae501a41d4`
- AutoPTU head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

## Live-engine delta

AutoPTU-Java advanced one commit beyond the head inspected in pass 195.

New head:

`09fc8bcf22c18d3106718a9d98005aae501a41d4` — `Freeze forced movement Trainer Feature event contract (#320)`.

The commit freezes the pinned Python observable obligation for Insectoid Utility + Wallclimber forced-movement prevention. Its own parity guard documents an important remaining gap: Java can preserve prevention provenance internally without yet exposing the Python semantic event.

This is stronger evidence for one exact Trainer Feature + movement interaction. It does not establish:

- all Trainer Features;
- all Wallclimber interactions;
- all push prevention;
- all forced movement;
- the full movement matrix;
- complete semantic-event parity.

AutoPTU remains pinned at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head synchronizes cached presentation dimensions after viewport resize and explicitly changes no battle rules or outcomes.

## Permanent capability classification

### VERIFIED within currently audited contracts

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

`VERIFIED` remains scoped to audited contracts. It does not mean every content combination inside a family is complete.

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING when the complete family is required

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No permanent category is promoted in pass 196.

## Complete-movement caution after Java #320

The new parity fixture is valuable because it freezes a semantic obligation around an exact prevention case.

It also explicitly demonstrates why the category must remain PARTIAL: preserving one blocker and one event contract cannot stand in for a closed matrix covering:

- Push;
- Pull;
- Knockback;
- Interception;
- collision handling;
- partial stops;
- chained displacement;
- footprint interactions during displacement;
- reaction ordering;
- terrain-mediated displacement;
- combinations with Moves;
- combinations with Abilities;
- combinations with Items;
- combinations with Trainer Features;
- combinations with statuses and temporary effects;
- semantic-event parity for all of the above.

## Rest/Extended Rest source evidence

PTU 1.05 Core contains explicit rules for ordinary Rest and Extended Rest.

The rules affect several pieces of mechanical state, including:

- HP restoration under timing and Injury constraints;
- Persistent Status Conditions after a qualifying Extended Rest;
- Drained AP;
- Daily-Frequency Move restoration under its rule condition;
- natural Injury recovery on its own longer clock;
- Pokémon Center recovery as a separate path.

The pinned AutoPTU source set also contains content that can modify resting behavior. Source presence is not runtime implementation evidence.

A current AutoPTU-Java code search for `Extended Rest`, `Resting` and a rest resolver returned no implementation hit during this pass.

Disposition:

`PTU REST RULES KNOWN FROM SOURCE; END-TO-END JAVA REST RESOLUTION NOT VERIFIED`.

This is not a seventeenth permanent battle capability family. It is a world/recovery procedure that, once implemented, must compose correctly with the relevant existing families and persistent character/Pokémon state.

## Rest-specific authority boundary

Narrative may store:

- where an actor rested;
- start/end timestamps;
- interruptions;
- observed activity;
- planned wake/departure;
- duty assignments;
- handoffs;
- wait/time-advance requests;
- actor availability.

Narrative may not independently apply:

- HP recovery;
- Injury removal;
- Persistent Status removal;
- Drained AP restoration;
- Daily Move refresh;
- PTU Sleep status;
- a fatigue/exhaustion penalty;
- a Feature-derived rest modifier.

Those require authoritative mechanical handling when mechanically relevant.

## Relationship to permanent categories

A future end-to-end PTU Rest resolver will need evidence across multiple existing categories rather than a blanket `rest supported` claim.

Relevant examples:

- core calculations: exact recovery arithmetic and clamping where applicable;
- full stateful damage pipeline: HP/healing state transitions and persistent health integration;
- status lifecycle: removal of qualifying Persistent Status Conditions;
- move-specific behavior or move-frequency state: restoration of Daily-Frequency availability according to the ruleset;
- Trainer Features/perks: any Feature or content that modifies Rest behavior must be exact and audited;
- items: only if a real governed item affects the procedure;
- adapter/playback: Minecraft bed/camp interaction must request the authoritative transition rather than author it.

The presence of PTU prose or Python data alone does not verify Java parity.

## Pass 196 rich encounter disposition

Encounter: `Pre-Dawn Camp Withdrawal at Sendero`.

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED for audited contracts;
- base movement legality: VERIFIED for audited contracts;
- complete movement: PARTIAL; blocking if protection/withdrawal depends on Interception, Push, Pull, Knockback, collision or forced movement;
- core calculations: VERIFIED for audited contracts;
- action economy/initiative: VERIFIED for audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL when selected content uses statuses; ordinary narrative sleep must never be represented as PTU Sleep by default;
- terrain/weather/hazards/zones/reactions: BLOCKING if darkness, weather, camp terrain, zones or reactions affect tactical legality;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL; Java #320 strengthens one exact Feature-prevention contract only;
- AI legal-action infrastructure: VERIFIED for audited contracts;
- AI tactical policy: BLOCKING for objective-aware withdrawal, corridor control or deliberate avoidance of noncombatant camp space;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for the complete persistent camp-to-battle-to-world loop.

Disposition: FULL VERSION BLOCKED.

## Reduced encounter viability

The reduced version is viable without implementing missing rule families.

Narrative retains:

- staging/camp purpose;
- rest interval records;
- sleep/off-duty presentation;
- noncombatants;
- equipment and custody;
- observation schedule;
- interruption timestamp;
- later duty/schedule consequences.

Before BattleSpec:

- noncombatants move to a safe authored world-state position;
- no ordinary sleeper receives PTU Sleep status;
- stable arena geometry is selected;
- tactical darkness/weather/hazards are omitted unless separately verified;
- roster and content are audited.

Allowed narrow battle outputs:

- `IMMEDIATE_CAMP_APPROACH_CLEAR`
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_FIELD_TEAM_CAN_WITHDRAW`

Battle output cannot establish:

- Rest or Extended Rest eligibility;
- HP/AP/Daily Move recovery outside authoritative mechanics;
- fatigue or exhaustion;
- sleep quality;
- research success;
- ecological cause;
- permanent route safety;
- NPC responsibility or competence.

## Time-advance and adapter boundary

The complete Minecraft/Cobblemon/Craftics family remains BLOCKING for an end-to-end rest interface because projection must preserve several authority distinctions:

- clicking a bed is a request, not mechanical recovery;
- sleeping animation is presentation;
- client logout is not character sleep;
- server restart is not automatic world-time advance;
- chunk unload does not end a rest interval;
- actor reconstruction after time advance comes from Ouros schedule state;
- spawned Pokémon at night do not independently author ecology truth;
- a battle animation cannot decide whether an interrupted interval later qualifies for PTU mechanics.

## Caelo uncertainty

Literal `Caelo` search across Narrative, AutoPTU-Java and AutoPTU returned no indexed result during this run.

The project README identifies Caelo source books/material as authoritative, but no currently inspected indexed file establishes:

- Caelo-specific Rest/Extended Rest changes;
- mandatory watches;
- camp procedure;
- curfews;
- labor/rest law;
- night travel restrictions;
- lodging obligations;
- sleep customs relevant to mechanics.

All remain unresolved.

## Implementation recommendation

Implement `Mirador First-Light Handoff` first.

It exercises persistent clock state, actor availability, scheduled observation, actor-specific knowledge and a bounded duty handoff without depending on battle, Rest mechanics or a new species.

After that, a separate engine-parity slice should audit PTU Rest/Extended Rest end-to-end before any bed, camp or wait interaction applies mechanical recovery.