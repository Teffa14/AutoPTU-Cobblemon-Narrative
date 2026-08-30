# Boss Encounter Dramaturgy, Phase Logic & Objective Persistence Extension

Status: DESIGN PROPOSAL. New boss scenes, NPCs, locations and events in this document are NON-CANON unless separately approved. Existing engine-authority and provenance boundaries remain CANON-APPROVED project architecture.

Date: 2026-08-30

## Scope

This layer owns the narrative grammar of major confrontations: how a threat is introduced, how pressure becomes readable, when the player's decision changes, what counts as an opening, how objectives can change, how a confrontation ends and what persists afterward.

It does not own PTU legality, damage, statuses, movement, AI policy, dungeon routing, faction simulation, ecology, institutional rules or Minecraft battle authority.

`encounter-implementation-contracts.md` remains the implementation-readiness owner. `mission-dungeon-grammar.md` remains the adventure-route owner. AutoPTU remains the tactical authority for combat facts. Ouros remains the authority for world facts and narrative consequence.

## Core distinction: narrative beat vs runtime phase

A narrative boss beat is a meaningful change in what the confrontation asks the player to understand or do.

A runtime phase is an engine state transition inside one BattleSpec.

These are deliberately separate.

A boss may have five narrative beats and zero runtime phase transitions if those beats are represented through pre-battle discovery, one ordinary battle and post-battle consequence.

A future engine may support a genuine multi-phase BattleSpec. That support must be verified before the narrative layer compiles a beat into an in-battle transition.

## Boss-scene grammar

A boss scene may use the following ordered beats. Authors may omit beats that add no value, but must preserve causality.

### READ

The player receives enough information to understand what is threatened and what the major actor appears to want, fear, guard, pursue or prevent.

Valid signals include environmental damage, tracks, prior victims, a recurring sound, NPC testimony, previous encounters, visible equipment, territorial behavior or a known institutional objective.

READ must not silently reveal canonical truth. It may contain mistaken interpretation, rumor or incomplete evidence when provenance requires it.

### TELEGRAPH

The scene exposes the characteristic pressure before the hardest expression of that pressure.

Examples include a safe-space demonstration of a charge lane, visible preparation before reinforcement, a warning siren before a closure, or a recurring Pokémon behavior already seen during exploration.

Telegraphing belongs to presentation and narrative logic unless an actual combat reaction window is invoked. A visual warning does not itself prove that generalized reactions exist.

### COMMITMENT

The player chooses or enters an approach with consequences. Examples include defending an access route, drawing a territorial Pokémon away from a settlement, confronting an antagonist before they depart, or entering a sealed chamber after evacuation.

The commitment point should freeze the encounter's explicit combatants and the BattleSpec facts that AutoPTU will own.

### PRESSURE

The encounter expresses its tactical problem through currently supported mechanics.

Pressure must be described in capability terms, not in vague prose such as “the boss uses the arena.” If the intended pressure requires moving hazards, Push/Pull, reactions, status triggers, ability terrain or tactical coordination, those exact families must be declared.

### OPENING

An opening changes what action is desirable or what objective can now be pursued.

Openings may be tactical, spatial, social or world-state transitions. Only tactical openings that are explicitly implemented belong inside BattleSpec.

A safe reduced form can establish the opening between two BattleSpecs after Ouros receives the first encounter's authoritative result.

### ESCALATION OR OBJECTIVE SHIFT

A new beat is justified only if the player's decision changes.

Valid changes include protecting a new route, preventing an escape, switching from defeat to containment, prioritizing an ally, choosing whether to pursue, or surviving until evacuation finishes.

Pure numerical inflation does not require a new narrative beat.

### RESOLUTION

The encounter ends with an explicit narrow result. The result must identify which owner may convert the combat fact into world state.

### AFTERMATH

The world records what changed. A boss defeat does not reset scars, witnesses, damaged infrastructure, faction response, ecological displacement, public memory or the boss's own later behavior when those owners preserve such state.

## Objective vocabulary

Proposed objective outcomes for boss-scene authoring include:

`TACTICAL_DEFEAT_CONFIRMED`
`TACTICAL_WITHDRAWAL_FORCED`
`ESCAPE_ROUTE_CLEARED`
`PURSUIT_ROUTE_DENIED`
`PROTECTED_ACTOR_REACHED_SAFETY`
`IMMEDIATE_THREAT_CONTAINED`
`CALMING_WINDOW_CREATED`
`INTERRUPTION_WINDOW_CREATED`
`OBJECTIVE_AREA_HELD`
`OBJECTIVE_AREA_LOST`
`BOSS_ESCAPED`
`PLAYER_FORCE_WITHDREW`

These are contracts, not automatic deductions. Each encounter must state which results AutoPTU can author directly and which require a post-battle Ouros decision.

`CALMED`, `CAPTURED`, `RITUAL_INTERRUPTED`, `SETTLEMENT_SAVED`, `FACTION_DEFEATED`, `CRISIS_ENDED`, `GUARDIAN_TRUST_GAINED` and similar world conclusions must remain outside combat unless a governing owner explicitly derives them from a narrower result.

## Non-KO boss contract

A boss premise may center on calming, protecting, rescuing, containing, delaying, escaping or interrupting.

The author must define:

- the world objective;
- the tactical fact AutoPTU is allowed to establish;
- the conversion rule from tactical result to world-state evaluation;
- the state preserved on failure;
- the fallback if the rich mechanic is unavailable.

Example:

World objective: calm a distressed territorial Pokémon.

Safe tactical fact: `CALMING_WINDOW_CREATED` after an explicit opposing force is defeated or driven from the immediate perimeter.

Ouros then evaluates the separately defined calming interaction. Battle victory alone does not assert `CALMED`.

## Recurring boss identity

A recurring major actor should persist through state rather than through artificial stat escalation alone.

Useful persistent facts include:

- what the actor learned or witnessed;
- injuries or damage only when the correct owner supports persistence;
- allies still available;
- routes or resources lost;
- reputation and public interpretation;
- equipment or location changes;
- promises, debts, fears and relationships;
- whether the previous confrontation ended through defeat, escape, withdrawal, containment or negotiation.

A future encounter should acknowledge the previous result. Exact tactical adaptation by an AI opponent depends on `AI tactical policy`; authored narrative preparation between battles does not.

## Failure persistence

Major encounters should fail forward whenever the premise permits it.

Failure may establish a lost route, delayed rescue, escaped antagonist, damaged asset, changed public belief, displaced Pokémon, missed opportunity or stronger future position for another actor.

Failure must not invent irreversible harm where the owning system has no evidence. It also must not silently restart the world from a pre-fight checkpoint.

A rematch can exist, but it should be a new event with provenance.

## Multi-stage encounters as linked BattleSpecs

Until full lifecycle and adapter playback are production-ready, this is the preferred reduced architecture for rich bosses.

Stage A ends with an authoritative AutoPTU result.

Ouros commits the allowed world facts.

A deterministic transition function evaluates whether Stage B exists and what static initial facts it receives.

Stage B begins as a new BattleSpec with explicit combatants, static geometry and no inherited tactical state unless that carryover is separately verified and serialized.

This prevents the narrative layer from fabricating persistent HP, statuses, initiative, weather, temporary terrain, reaction resources or per-scene feature state.

## Carryover rule

Never assume tactical carryover because two scenes belong to the same boss encounter.

Potential carryover families requiring explicit support include:

- HP and injuries;
- status conditions;
- temporary stat stages;
- action points or per-scene resources;
- move frequency/usage state;
- initiative order;
- weather and terrain;
- summoned units;
- destructible-object state;
- Trainer Feature/perk usage;
- item consumption;
- positions and footprints.

If exact serialization is not verified, Ouros may preserve only narrative/world facts and construct the next BattleSpec from a reviewed fresh tactical state.

## Arena identity

A boss arena should teach or reinforce the narrative premise even when tactical environment mechanics are unavailable.

Static geometry, visible damage, lighting, props, blocked routes, NPC evacuation, sound cues, weather presentation and environmental storytelling may establish identity without creating tactical modifiers.

Dynamic terrain, damaging zones, weather rules, moving platforms, collision traps or reaction windows require the corresponding engine families.

Minecraft/Cobblemon may render these cues only after Ouros decides their state. Minecraft block changes, entity motion, particles or Cobblemon BattleState cannot create PTU rules or outcomes.

## Phase-authority contract

Each intended in-battle phase transition must declare:

`trigger_source`
`trigger_owner`
`observable_telegraph`
`state_mutations`
`capability_dependencies`
`failure_behavior`
`replay_behavior`
`reduced_translation`

Allowed trigger owners are limited to a verified AutoPTU subsystem or an Ouros inter-scene controller. Minecraft/Cobblemon/Craftics cannot own a rule-critical phase trigger.

## Reinforcement contract

Reinforcements are not a decorative spawn.

A full encounter using them must prove:

- when new combatants may enter;
- who determines legality;
- where they may enter;
- how initiative is assigned;
- whether their arrival consumes or changes action resources;
- whether target legality is recalculated;
- how AI legal choices and tactical policy handle them;
- how playback represents the authoritative arrival.

Until those contracts are verified, a reduced version should begin the next BattleSpec with the intended roster already explicit.

## Boss retreat contract

Retreat is a valuable resolution because it preserves recurring actors without falsely converting every loss into death or capture.

A tactical engine may establish `BOSS_ESCAPED` only if escape/movement and encounter-end semantics are fully contracted. Otherwise, a reduced battle can end at a narrow threshold such as `TACTICAL_WITHDRAWAL_FORCED`; Ouros then applies a separately authored post-battle departure if the route and world state permit it.

## Player withdrawal

The same rigor applies to players. A loss need not mean total defeat or death. A safe extraction, forced withdrawal, rescue by established allies or surrender must be authored through the correct owner and cannot be improvised from a renderer event.

## Telegraph checklist

Before a rich boss encounter is approved for canon implementation, the design should answer:

- what pressure can the player perceive before committing;
- what changed when a new beat begins;
- why the player can understand that change;
- what decision the new beat creates;
- which engine family owns that decision;
- what survives if the player loses;
- what reduced form preserves the premise.

## Anti-patterns

Do not use hidden arbitrary immunities because an actor is called a boss.

Do not add extra turns unless lifecycle/status timing contracts prove them.

Do not use an HP threshold as a universal story trigger unless that exact state is exposed authoritatively and the transition is owned server-side.

Do not infer “enraged,” “stunned,” “calmed” or “retreating” from animation alone.

Do not let a destructible prop become a battle objective unless object targeting, HP/damage and consequence contracts exist.

Do not let Minecraft physics resolve falling, collision, knockback or moving-platform effects.

Do not let Cobblemon select combatants or decide PTU battle state.

## Relationship to canon

CANON-APPROVED architecture retained:

- AutoPTU owns tactical battle facts within its verified contracts.
- Ouros owns world facts and consequence routing.
- Cobblemon/Minecraft/Craftics are presentation/projection layers, not battle-state authority.
- research provenance remains separate from canon.
- missing capability families must remain visible.

PROPOSED:

- this boss-scene dramaturgy grammar;
- the objective vocabulary above;
- linked-BattleSpec reduction as the default rich-boss fallback;
- recurring-boss persistence fields;
- phase/reinforcement/retreat authoring contracts.

UNCERTAIN / requires later product decision:

- whether every major boss must use this grammar;
- which objective result names become stable schemas;
- whether an Ouros boss controller becomes a dedicated service or remains part of mission/world-state orchestration;
- how much tactical carryover future AutoPTU serialization will support.
