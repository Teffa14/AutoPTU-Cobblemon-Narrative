# Engine Readiness Snapshot — Pass 133

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-29

This snapshot records live implementation evidence checked while adding civic-office, mandate and transition continuity.

AutoPTU-Java and AutoPTU were inspected read-only. This pass writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Narrative repository inspection

Narrative head before Pass 133:

`b07ded69c2b719189c57c6fcad4dded808ecc0df`

The complete recursive tree was inspected before topic selection. The response reported `truncated: false`.

Potential duplicate topics were rejected after inventory inspection. In particular, found-property/restitution already has dedicated research, design and proposal material.

Adjacent files checked before writing included:

- `design/civic-governance-public-works-layer.md`
- `design/memorial-absence-succession-continuity-extension.md`
- engine readiness through Pass 132
- repository inventory entries for credentials/authorization, archives, public notices, adjudication and institutional continuity

The selected gap is operational continuity after an authored office transition fact exists.

## AutoPTU-Java live evidence

Current head inspected:

`80f08b5d66f3451f70743ac0d4717f3a3dd21a0b`

Commit:

`Derive intercept Justified bonus from server state (#275)`

No newer AutoPTU-Java commit was present during this run.

### Concrete evidence retained

The current Intercept path provides localized evidence for:

- PRE-target integration;
- interceptor movement in the implemented sequence;
- effective-defender replacement in the implemented sequence;
- Acrobatics/Athletics ranks derived from server-owned combatant rule content;
- Coaching automatic-success state derived from server-owned temporary effects;
- exact `Justified [Errata]` presence derived from server-owned Ability state;
- +4 Justified bonus pinned against the Python authority in regression coverage.

This remains one concrete Intercept route.

### Evidence not generalized

The current head does not verify the entire movement/reaction family.

Still unverified as complete families:

- broad Push;
- broad Pull;
- broad Knockback;
- every forced-movement source;
- environmental displacement;
- every Intercept timing window;
- generalized reaction ordering;
- multiple competing reaction windows;
- protected-civilian reaction contracts;
- escort objective contracts;
- protected-record/courier reactions;
- broad terrain authority;
- all Abilities;
- all Trainer Features/perks;
- objective-aware tactical policy;
- semantic Minecraft/Cobblemon/Craftics playback.

## AutoPTU live evidence

Current head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer AutoPTU commit was present during this run.

The change synchronizes cached Pixi dimensions after viewport resize so visual destinations use the current renderer geometry. Its documented scope is presentation; rules and battle outcomes do not change.

This does not establish:

- civic-state playback;
- office-holder authority;
- record custody semantics;
- credential semantics;
- meeting state;
- objective-aware escort playback;
- combatant authority;
- legality authority;
- HP/status authority;
- narrative consequence authority.

## Permanent capability map — Pass 133

No category receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

Baseline targeting and spatial legality remain sufficient for conventional reduced encounters. Bespoke cover or unusual targeting shapes still require exact implementation evidence.

`base movement legality`

Basic movement remains verified for conventional BattleSpecs.

`core calculations`

Previously established parity-backed calculation infrastructure remains at the verified baseline.

`action economy/initiative`

Baseline action economy and initiative remain verified.

`AI legal-action infrastructure`

Legal-action enumeration/validation remains verified at the established baseline. It does not provide strategic objective selection.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

The current Intercept route is meaningful evidence, but the complete family remains broader. Escort, protected-courier movement and generalized forced movement remain unsupported as a complete contract.

`full turn/round lifecycle`

Ordinary battle progression exists. Timed evacuation waves, handoff windows and staged withdrawal remain incomplete as a generalized family.

`full stateful damage pipeline`

Substantial implemented behavior exists, but the permanent category remains partial.

`status lifecycle`

Existing statuses do not authorize invented panic, civic, escort, protected-record or authority statuses.

`move-specific behavior`

Representative Move implementations do not prove complete coverage.

`abilities`

`Justified [Errata]` evidence remains local to the Intercept route. No Ability grants civic truth, mandate or office authority.

`items`

Items remain partial. No generic credential, archive container or civic-document tactical effect is inferred.

`Trainer Features/perks`

Coaching evidence remains local to Intercept. No Feature grants office eligibility, voting power, public mandate or transition authority.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

Rich transition encounters would need this family for protected entrances, evacuation corridors, changing access zones or generalized reactions.

No generalized contract is verified.

`AI tactical policy`

Rich versions require objective-aware behavior such as `PROTECT`, `WITHDRAW`, `CLEAR_ROUTE`, hold-position or avoid-protected-area decisions.

Legal-action infrastructure alone cannot provide this policy.

`Minecraft/Cobblemon/Craftics adapter/playback support`

Coordinate rendering hardening does not provide semantic projection of office state, handoff state, record custody, meeting state or transition consequences.

This family remains BLOCKING.

## Encounter review — Transition Archive Handoff Perimeter

### Full intended version

Narrative objective:

Protect or clear physical access while an authorized records handoff is scheduled, without making the records tactical loot or battle-authenticated evidence.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL if attacks occur
- status lifecycle — PARTIAL where ordinary legal statuses occur
- terrain/weather/hazards/zones/reactions — BLOCKING if protected entrance/reaction semantics are active
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full version status:

BLOCKED FOR RICH SEMANTICS.

### Reduced version

Status: READY.

World-state contract:

1. Ouros pauses the handoff.
2. Records, manifests, credentials, clerks, couriers and noncombatants are removed from BattleSpec or secured behind world-state boundaries.
3. Ouros selects explicit legal combatants.
4. The battlefield uses static geometry.
5. Conventional engine combat determines immediate physical access only.
6. The record owner separately decides whether the handoff resumes.

Forbidden automatic transitions:

- victory => record authenticated
- victory => record custody transferred
- victory => credential activated
- victory => office authority effective
- victory => transition complete

## Encounter review — Public Meeting Evacuation

### Full intended version

Narrative objective:

Safely interrupt and evacuate a public meeting because of an unrelated tactical incident.

Rich requirements:

- moving noncombatants;
- phased withdrawal;
- protected exits;
- Intercept/escort interactions;
- objective-aware tactical AI;
- semantic playback.

Permanent dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL if attacks occur
- status lifecycle — PARTIAL for ordinary legal statuses
- terrain/weather/hazards/zones/reactions — BLOCKING when exit protection/reactions matter
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full version status:

BLOCKED FOR RICH SEMANTICS.

### Reduced version

Status: READY.

Ouros adjourns the meeting and clears attendees, officials, public records and protected participants before BattleSpec creation.

The static battle may determine whether the adjacent area is immediately accessible afterward.

Forbidden automatic transitions:

- victory => vote/result decided
- victory => quorum satisfied
- victory => consultation complete
- victory => office-holder selected
- victory => public support proven
- victory => transition route changed

## Encounter review — Pending Project Access Diversion

### Full intended version

Narrative objective:

Clear or protect a route so authorized inspectors can later reach a project that spans office-holder episodes.

Rich dependencies include escort/Intercept, possible forced movement, protected route semantics, tactical policy and semantic playback.

Full version status:

BLOCKED FOR RICH SEMANTICS under the same partial/blocking categories above.

### Reduced version

Status: READY.

Inspectors remain outside BattleSpec. Players resolve a conventional static encounter at the chokepoint. The relevant project owner decides after combat whether inspection can proceed.

Forbidden automatic transitions:

- victory => project approved
- victory => project cancelled
- victory => inherited decision reviewed
- victory => inspection complete
- victory => handover complete

## PTU/Caelo cross-check for this topic

The source material does not justify inventing universal political mechanics.

Keep UNKNOWN unless an exact governing source plus current engine contract establishes otherwise:

- generic election checks;
- universal public-support scores;
- one-roll persuasion of an electorate;
- Trainer class as office eligibility;
- Badge count as civic authority;
- League rank as settlement government authority;
- battle result as succession procedure;
- Command/Charm/Guile as automatic institutional outcome;
- Aura/Telepathy/Psychic effects as generic political truth verification;
- Pokémon Type/species as office eligibility or representation;
- Loyalty as electoral support;
- Trainer Features/perks as authority to appoint, dismiss, delegate or certify civic decisions;
- Moves, Abilities or Items as automatic document authentication.

World governance remains authored Ouros state, not inferred PTU flavor.

## Minecraft/Cobblemon implementation boundary

Safe presentation after Ouros decides state:

- office occupant NPC changes;
- nameplate replacement;
- archive boxes or shelves;
- updated public boards;
- former holder routine elsewhere;
- meeting calendar changes;
- project boards showing multiple holder episodes;
- old office spaces reused later.

Minecraft/Cobblemon must not derive:

- holder identity from which NPC occupies a chair;
- authority from proximity to a desk;
- credential validity from inventory contents;
- custody from holding a book/item;
- transition completion from opening a door;
- public notice receipt from rendering a sign;
- office selection from battle state.

Ouros remains authoritative for world facts. AutoPTU remains authoritative for tactical battle. Cobblemon/Minecraft BattleState remains outside combatant and rule authority.

## Canon questions remaining open

- Which Ouros institutions have offices whose holder can change?
- What are their mandates?
- Which transition routes actually exist?
- Do any settlements use elections?
- Which use appointment, rotation, guild rules, elder selection, League-linked processes or something else?
- What vacancy and acting rules exist?
- What can acting holders do?
- What may be delegated?
- When does authority become effective?
- What records are institutional rather than personal?
- Which records are public or restricted?
- How do credentials change?
- Which prior decisions survive a transition?
- Which have valid review routes?
- Which historical transitions already shaped settlements?
- What Minecraft-visible conventions represent office continuity?

Pass 133 intentionally answers none of these without canon authority.