# Engine Readiness Snapshot — Pass 201

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-02
Narrative head before pass: `f79553533bf705c127dec03426caa3d3b5ecea89`

Read-only engines inspected:
- AutoPTU-Java head: `fbd38166b664eafe148950bfaaf915aa956e9195`
- AutoPTU head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

## Live engine delta

No engine head changed after pass 200.

AutoPTU-Java remains on `fbd38166b664eafe148950bfaaf915aa956e9195` — `Compose forced movement prevention semantics at post-hit boundary (#323)`.

That commit carries already-resolved forced-movement prevention semantic events through the post-hit boundary using the same combatant rule-content snapshot. It is meaningful evidence for one integration path and prevention-provenance projection. It does not close the full movement family.

AutoPTU remains on `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head explicitly describes presentation-only coordinate synchronization after viewport resize and states that battle rules/outcomes do not change.

No permanent capability category is promoted in pass 201.

## Permanent capability classification

### VERIFIED within currently audited contracts

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

`VERIFIED` remains contract-scoped and does not imply exhaustive combinatorial coverage.

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

## Complete movement caution

Current evidence still does not close the combined matrix across:

- Push;
- Pull;
- Knockback;
- Interception;
- collisions;
- partial stops;
- chained displacement;
- footprint interactions during displacement;
- reaction ordering;
- terrain-mediated displacement;
- every Move path;
- every Ability path;
- every Item path;
- every Trainer Feature/perk path;
- status and temporary-effect interactions;
- semantic-event parity for all outcomes.

A representative forced-movement prevention path cannot promote `complete movement`.

## Pass 201 PTU boundary

Public PTU 1.05 material explicitly treats Guile as relevant to deception, disguise and posing, with Perception potentially opposing Guile when an observer attempts to see through a disguise.

Pass 201 therefore does not create an identity/deception Skill system.

Narrative may preserve:
- stable actor IDs;
- presented identity claims;
- evidence/provenance;
- purpose-scoped verification events;
- credentials as world records;
- authority grants;
- delegation history;
- observer beliefs after an authoritative adjudication.

Mechanically contested impersonation, disguise, deception detection, concealment and relevant Features/Edges remain delegated to PTU/Caelo/AutoPTU.

Pokémon-game OT/Trainer-ID concepts are treated as design evidence that visible names need not uniquely determine originating identity. They are not promoted into Caelo civil-identity rules.

A fresh literal `Caelo` search in currently indexed project material did not expose identity/credential/delegation rules in this pass.

Unresolved Caelo surfaces include:
- civil/legal identity;
- names/aliases;
- Trainer licensing;
- age/guardianship authority;
- institutional credentials;
- signatures/seals;
- employment/agency authority;
- proxy collection;
- outside-region credential recognition;
- revocation/appeal rules.

## Pass 201 narrative-mechanics boundary

Pass 201 adds proposed Narrative records for:
- stable actor identity references;
- identity assertions;
- purpose-scoped verification;
- credentials and their lifecycle;
- authority grants;
- delegations;
- action-specific authority checks.

Critical boundaries:

`SAME_DISPLAY_NAME != SAME_ACTOR`

`CREDENTIAL_VALID != AUTHORIZED_FOR_EVERY_ACTION`

`PRIOR_ACCESS != CURRENT_ACCESS`

`DELEGATION != TRANSFER_OF_OFFICE_OR_OWNERSHIP`

`MINECRAFT_ENTITY_UUID != CANONICAL_SOCIAL_IDENTITY`

`BATTLE_VICTORY != LICENSE_OR_AUTHORITY`

The existing visitor-layer `temporary_access_grant` remains the owner of visit-specific access. Pass 201 provides identity/verification links instead of replacing that record.

## Pass 201 rich encounter

Encounter: `Authorized Recovery at Mirador Perimeter`.

Narrative premise:
Nerea authorizes a bounded recovery of a specific Mirador package from a route-side observation point. One actor may retrieve it and another may carry it. Wild activity complicates immediate withdrawal. The task tests delegated scope without granting general Mirador authority.

### Full intended dependency matrix

- targeting/footprints/range/LoS: VERIFIED within audited contracts
- base movement legality: VERIFIED within audited contracts
- complete movement: PARTIAL; required if protected withdrawal, Interception, Push, Pull, Knockback, collisions or other displacement matters
- core calculations: VERIFIED within audited contracts
- action economy/initiative: VERIFIED within audited contracts
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL where selected content uses statuses
- terrain/weather/hazards/zones/reactions: BLOCKING if route terrain, weather, tactical safe zones or reactions affect the encounter
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL where battle Items participate
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED within audited contracts
- AI tactical policy: BLOCKING if wild actors must prioritize territory, withdrawal, corridor control, package indifference or other non-KO objectives
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for faithful world -> battle -> world projection

Disposition: FULL RICH VERSION BLOCKED.

## Reduced encounter contract

Narrative retains:
- actor identity and verification;
- authority/delegation records;
- package custody and task scope;
- noncombatants;
- route purpose;
- later handoff and institutional consequences.

Before combat:
- resolve current authority independently of battle;
- move noncombatants/package semantics to a safe Narrative state where appropriate;
- identify one immediate wild actor still preventing withdrawal;
- select audited combatants/content;
- use stable geometry;
- omit unverified tactical weather/hazards/zones;
- avoid forced-movement objectives unless each selected interaction is contract-verified.

Allowed narrow handoffs:
- `IMMEDIATE_RECOVERY_ROUTE_CLEAR`
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_TEAM_CAN_WITHDRAW`

Battle output cannot determine:
- identity truth;
- credential validity;
- delegation validity;
- ownership;
- general Mirador access;
- employment/membership;
- whether an actor exceeded authority;
- recognition of an outside credential;
- future permissions;
- disciplinary or relationship consequences.

Disposition: REDUCIBLE USING AUDITED BASIC BATTLE CONTENT.

## AI tactical-policy caution

Legal-action infrastructure does not demonstrate understanding of a recovery objective.

A rich version could require AI to:
- maintain territorial distance;
- retreat instead of pursuing a KO;
- stop pursuit once the team withdraws;
- ignore a noncombat package;
- respond to protected withdrawal geometry;
- choose corridor pressure over damage.

Those are tactical-policy requirements and remain BLOCKING until live tests/contracts verify them.

## Adapter/playback caution

Identity/authority requires strong separation from Minecraft presentation.

Required boundaries include:
- username/display name != canonical actor ID;
- entity UUID != social/legal identity;
- skin/uniform != current credential;
- badge-like item present != authority active;
- duplicate entity != duplicate person;
- stale sign/card != current permission;
- entity unload != authority expiry;
- entity death != revocation or identity deletion;
- client localization != name/role mutation;
- battle animation != institutional authorization.

The complete adapter/playback family remains BLOCKING.

## Narrative repository state for this pass

Pass 201 writes only to Narrative.

New files:
- `research/2026-09-02-identity-credential-delegated-authority-scan-201.md`
- `design/identity-credential-delegated-authority-continuity-layer.md`
- `proposals/2026-09-02-marea-identity-credential-delegated-authority-seeds-201.md`
- `design/engine-readiness-snapshot-pass-201.md`

No AutoPTU-Java or AutoPTU write is authorized or performed.

## Implementation recommendation

Prototype `The Access Note Outlives the Visit` first.

It requires:
- no battle;
- no new canonical NPC;
- no new Pokémon species;
- no new institution;
- no civil-ID system;
- no external geography;
- no contested PTU Skill check.

It verifies the new seam immediately: a repeat visitor can be genuinely recognized while a previous access grant remains expired, and a stale physical note can remain evidence of past authority without becoming current authority.