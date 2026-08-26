# Pokémon Vigilance, Alarm Signals and Anti-Predator Behavior Layer

Status: PROPOSED SYSTEMS DESIGN / NON-CANON
Date: 2026-08-26
Pass: 181

## Purpose

This layer records how Pokémon detect possible risk, monitor surroundings, emit or receive warning signals, change vigilance and choose non-combat anti-predator responses over time.

It does not own predator/prey truth, collective identity, acoustic truth, learned traditions, tactical fear or battle bonuses.

Existing authorities remain:

- Wild Collective Agency: persistent groups and group-scale lifecycle;
- Interspecies Ecological Relations: predator/prey and other ecological relations;
- Soundscapes and acoustic monitoring: recorded sounds and signal evidence;
- Social Learning: transmission of learned alarm behavior;
- Spatial Ecology: ranges, core areas and site use;
- Care: welfare and clinical interpretation;
- PTU/Caelo/AutoPTU: exact battle mechanics.

## Core separation

Ouros keeps these states separate:

`possible risk source -> detector observation -> vigilance state -> signal emission -> signal reception -> receiver interpretation -> behavioral response -> later ecological consequence`

No step proves the next automatically.

## Behavioral objects

### Vigilance episode

A bounded observation of monitoring behavior.

Fields should include:

- episode id;
- individual or collective scope;
- location and time;
- observed posture/activity;
- baseline activity interrupted or maintained;
- possible trigger refs;
- observer/source refs;
- confidence;
- end condition;
- unresolved interpretations.

Suggested states:

- routine watch;
- elevated vigilance;
- repeated scanning;
- shelter-oriented vigilance;
- group clustering;
- reduced foraging;
- unknown attentive behavior.

These are descriptions, not modifiers.

### Alarm-signal event

A signal suspected or confirmed to carry warning information.

Track:

- signal id;
- emitter if known;
- modality: acoustic, visual, tactile, mixed, other;
- recording/observation refs;
- apparent trigger;
- receiver candidates;
- observed receiver responses;
- signal-function assessment;
- competing explanations.

An alarm function can remain `PROPOSED` or `UNRESOLVED` indefinitely.

### Reception event

Signal emission does not prove reception.

Track which individuals or groups had a plausible opportunity to detect it and what changed afterward.

### Sentinel-role assessment

Do not assign a permanent role because one Pokémon stood watch once.

Possible states:

- no role established;
- candidate recurring lookout;
- rotating watch behavior observed;
- stable sentinel-like role supported;
- former role;
- unresolved.

Evidence may include repeated observations, location consistency, behavior of other group members and response after the candidate leaves.

### Risk-perception assessment

This stores the observer's best interpretation of what risk the group appears to be responding to.

It must distinguish:

- confirmed external threat;
- plausible threat;
- disturbance with unknown significance;
- false alarm candidate;
- signal-only response where the original threat was not observed;
- unresolved.

A false alarm is not deception unless intentional misleading behavior is separately established.

## Anti-predator response repertoire

Candidate descriptive responses:

- WATCH;
- WARN;
- FREEZE;
- WITHDRAW;
- SEEK_COVER;
- CLUSTER;
- SCATTER;
- MOVE_VULNERABLE_MEMBERS;
- ALTER_FORAGING;
- ALTER_ROUTE;
- INCREASE_DISTANCE;
- APPROACH_AND_MONITOR;
- MOB_OR_HARASS_CANDIDATE;
- RECRUIT_OTHERS;
- RESUME_BASELINE;
- UNKNOWN_RESPONSE.

These labels never imply battle actions unless AutoPTU explicitly receives a tactical encounter with legal choices.

## Tradeoffs

Vigilance can affect world-state opportunity without becoming a stat bonus.

Examples:

- less time spent feeding;
- delayed departure;
- shorter use of an exposed site;
- increased use of cover;
- missed social or feeding opportunities;
- altered survey detectability;
- temporary aggregation.

Persist these only when they matter to Chronicle, ecology or a later decision.

## Signal reliability and false alarms

A warning system can be noisy.

Track:

- signal frequency;
- confirmed-threat correlation where known;
- false-alarm candidates;
- missed-alarm candidates;
- environmental masking;
- receiver-specific response;
- method/coverage limits.

Do not create a universal numerical reliability score unless canon later requires one.

## Environmental masking

Sound, light, vegetation, weather, infrastructure and crowd activity may change whether a signal is detectable.

The relevant environmental authority owns the physical condition. This layer records the behavioral consequence only when observed or reasonably assessed.

Example:

`rail noise increased -> alarm call audibility hypothesis -> fewer receivers visibly react -> follow-up study`

Do not jump directly from noise to population decline.

## Multi-species warning networks

A signal from one species may affect another species.

This requires evidence.

Use Interspecies Ecology for the ecological relation and this layer for the warning/reception events.

Possible outcomes:

- another species increases vigilance;
- another species withdraws;
- another species ignores the signal;
- response differs by season or site;
- an apparent shared alarm network later proves to be independent response to the same threat.

## Learning boundary

If juveniles or newcomers begin responding after exposure to experienced individuals, create a Social Learning handoff.

This layer stores the behavior before and after exposure. Social Learning decides whether transmission is supported.

Never infer teaching from co-presence.

## Individual identity

Persistent individuals can accumulate histories such as:

- repeated lookout behavior;
- signal repertoire revisions;
- changed response after injury, age or relocation;
- former partner reappearing in a wild group;
- loss or gain of a recurring lookout role.

The role does not become personality, loyalty, leadership or Trainer-like authority.

## Chronicle compression

Routine watches and ordinary alarm responses should compress.

Expose them when:

- behavior changes;
- a signal is newly interpreted;
- a false alarm creates consequences;
- an infrastructure project masks communication;
- a known lookout disappears or retires from the role;
- a new species begins responding;
- public belief diverges from evidence;
- player action modifies the risk environment.

## Minecraft boundary

Minecraft/Cobblemon may render already-authorized states such as:

- a lookout posture;
- a warning animation or cry;
- a group moving toward shelter;
- an observation site;
- an authored disturbance.

Minecraft must not derive:

- sentinel roles from entity position;
- alarm truth from sound playback;
- threat location from aggro targets;
- group knowledge from loaded entities;
- vigilance from head rotation;
- ecological fear from pathfinding;
- collective response from combat AI.

## PTU mechanics boundary

Hard prohibitions:

- lookout behavior -> Keen Eye or Illuminate;
- warning signal -> Intimidate;
- alarm -> Frightened, Flinch, Confused or Status;
- sentinel role -> Perception bonus;
- mobbing -> Pack Mon;
- received warning -> free Shift or reaction;
- collective alarm -> shared Initiative;
- vigilance -> Accuracy/Evasion Combat Stage;
- SOS-battle precedent -> reinforcement rule;
- false alarm -> Guile check;
- predator detection -> Forewarn or Anticipation.

Any exact mechanic requires PTU/Caelo validation and live engine support.

## Encounter contract — Alarm Network at Cedar Meadow

Narrative premise: repeated warning calls now cause an entire mixed-species feeding area to leave early. Researchers suspect a new disturbance near the meadow edge.

FULL version:

Wild actors can warn, receive information, withdraw, cluster, seek cover and choose between several exit routes while a separate hostile pressure may enter the area.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED for battle actors;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: BLOCKING for dynamic withdrawal/crossing;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL if exact Status mechanics are invoked;
- terrain/weather/hazards/zones/reactions: BLOCKING if shelter zones, noise zones or environmental pressure have tactical effects;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for WITHDRAW/SEEK_COVER/REJOIN_GROUP/AVOID_THREAT;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version:

Resolve alarm reception and wildlife withdrawal in world state. Remove non-combatants. If an independent hostile confrontation remains, instantiate a static AutoPTU battle afterward. The battle does not decide whether the alarm was accurate.

## Encounter contract — The False Alarm Corridor

Narrative premise: a repeated alarm response is closing a route even though no predator has been confirmed. Traffic noise, construction vibration, a new species and an actual predator are competing explanations.

FULL version requires dynamic civilians/wildlife movement, tactical withdrawal objectives and any environmental masking mechanic to be implemented authoritatively.

REDUCED version keeps route closure, signal observations and wildlife response outside combat. A static battle can occur only if a separate actor becomes hostile.

## Encounter contract — Mobbing at the Research Tower

Narrative premise: several wild Pokémon repeatedly approach and harass something near a monitoring tower. The apparent target may be a predator, competitor, machine or harmless object.

FULL version requires AI tactical policy capable of approach, harassment, disengagement and withdrawal without treating all actors as KO-seeking enemies. Complete movement and adapter/playback remain blocking.

REDUCED version resolves the mobbing episode as world state, clears the area and preserves observations. Any later combat is independent.

## Non-combat scenario — Which Signal Means Danger?

Researchers compare recordings, observation notes and receiver responses across several seasons. Multiple interpretations may remain viable.

No battle capability is required. `UNRESOLVED` is a legitimate final state.

## Canon questions

- which Ouros species or populations have authored alarm behavior;
- whether any mixed-species warning networks exist at campaign start;
- which individuals already have recurring lookout histories;
- which routes or settlements have human-noise masking problems;
- whether any community traditions interpret particular warning calls;
- which sites should remain protected because repeated observation disrupts vigilance;
- how much behavioral change can advance offline.

Nothing in this document establishes those answers as canon.
