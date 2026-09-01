# Engine Readiness Snapshot — Pass 193

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-01
Narrative head before this pass: `37d9acf861aec1a1f525aca5eafccef0f8c174aa`

Read-only engine repositories:
- AutoPTU-Java head inspected: `c34e10a57a7c3f93dd184c09a03d87fb9a014a34`
- AutoPTU head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

## Live Java change since pass 192

Commit `c34e10a57a7c3f93dd184c09a03d87fb9a014a34` preserves Python forced-movement defender-prevention precedence and first-blocker provenance.

The change separates status-only prevention from temporary-effect-only prevention, lets authoritative runtime orchestration apply the frozen Python ordering, and returns a resolution carrying either movement or prevention provenance without allowing both simultaneously.

This is meaningful evidence for parity and auditability inside forced-movement prevention.

It does not prove complete movement as a family.

Still not demonstrated as one verified complete matrix by this commit:

- all Push behavior;
- all Pull behavior;
- all Knockback behavior;
- all Interception behavior;
- collision handling;
- partial stops;
- chained displacement;
- footprint interactions throughout displacement;
- every reaction-ordering interaction;
- terrain-mediated displacement;
- every combination with move-specific behavior, Abilities, Items, Trainer Features, statuses, and temporary effects.

The category therefore remains PARTIAL.

## Permanent capability classification

### VERIFIED within currently audited contracts

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

`VERIFIED` remains contract-scoped. It does not assert complete universal coverage.

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING when a concept requires the complete family

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No category is promoted merely because one representative behavior exists.

## Pass 193 rich encounter disposition

Encounter: `Guest Route Check at Glass Bend`

Full version dependencies:

- targeting/footprints/range/LoS: VERIFIED for audited contracts;
- base movement legality: VERIFIED for audited contracts;
- complete movement: PARTIAL and blocking for interception/displacement-rich escort behavior;
- core calculations: VERIFIED for audited contracts;
- action economy/initiative: VERIFIED for audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL when roster/content uses statuses;
- terrain/weather/hazards/zones/reactions: BLOCKING if route surface, weather, hazards, zones, or reactions become tactical rules;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED for audited contracts;
- AI tactical policy: BLOCKING for competent objective-aware protection/withdrawal;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for faithful end-to-end world execution.

Disposition: FULL VERSION BLOCKED.

Reduced version remains viable by keeping the visitor, purpose, luggage, stay state, access, and route movement in Narrative world state. Narrative first resolves the visitor to a safe position. Any remaining immediate threat becomes a separate ordinary BattleSpec on stable geometry using audited content only.

Allowed handoffs remain narrow, for example:

- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_PASSAGE_CLEAR`

The battle cannot decide lodging, residency, access, relationships, visitor claims, ownership, or guest-Pokémon custody.

## Temporary-visitor mechanical boundary

No inspected PTU/Caelo evidence establishes a generic mechanical hospitality subsystem.

Narrative visitor state must not create:

- healing or recovery bonuses from a room;
- Skill bonuses from being hosted;
- Trainer Features or Edges;
- relationship bonuses;
- travel bonuses;
- guest Pokémon loyalty or ownership changes;
- mechanical access to protected institutional data;
- battle permissions beyond separately validated challenge contracts.

If later PTU/Caelo material defines a relevant mechanic, implementation must bind to that authoritative rule rather than emulate it in Narrative.

## AutoPTU Python evidence

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its current head is presentation-only coordinate synchronization after viewport resize and explicitly does not change battle rules or outcomes. No permanent capability category is promoted from that repository in this pass.

## Caelo unresolved

Repository-wide indexed search again returned no `Caelo` material in Narrative, AutoPTU-Java, or AutoPTU.

No live evidence inspected establishes:

- regional lodging law;
- visitor registration;
- residence categories;
- identity-document requirements;
- border/immigration authority;
- lodging pricing or taxes;
- institutional guest-access doctrine;
- companion-Pokémon accommodation rules;
- external ferry destinations.

Narrative must keep those uncertain.

## Implementation recommendation

Implement `Room Held, Ferry Delayed` before any tactical visitor encounter. It requires no new battle capability and tests the important distinctions between expected arrival, transport evidence, actual presence, temporary capacity, and downstream local planning.
