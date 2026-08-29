# Engine Readiness Snapshot — Pass 137

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-29

This snapshot records live implementation evidence checked while adding human identity, name and record continuity.

AutoPTU-Java and AutoPTU were inspected read-only. This pass writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Narrative repository inspection

Narrative head before Pass 137:

`9868727c14b4d18a84c160634069bbccdf452835`

The full recursive repository tree was inspected before topic selection and was not truncated. Existing identity-adjacent files were then read directly, including:

- `design/infiltration-stealth-cover-identity-layer.md`;
- `design/credentials-authorizations-recognition-extension.md`;
- `design/personal-records-oral-history-correspondence-extension.md`;
- `design/interregional-mobility-recognition-layer.md`;
- `design/interregional-arrival-inspection-hold-release-continuity-extension.md`;
- `design/land-parcels-boundaries-use-rights-records-continuity-extension.md`;
- `design/cartography-survey-wayfinding-layer.md`;
- `design/pokemon-agency-partnership-release-layer.md`;
- `design/care-recovery-welfare-layer.md`;
- `design/memorial-absence-succession-continuity-extension.md`;
- `design/wildfire-fire-response-incident-continuity-extension.md`;
- `research/2026-08-18-source-scan.md`;
- Pass 136 readiness.

Potential topics such as address continuity, generic map/wayfinding continuity and structural fire response were rejected because existing layers already own them.

The selected gap is narrow: existing systems consume human identity references but do not yet preserve a neutral versioned graph for human names, issuer-local identifiers, record linkages, corrections, homonym collisions, scoped verification and disclosure.

## AutoPTU-Java live evidence

Current head inspected:

`106dd1010eeec7ec2423688ed5eeec2274ae8d18`

Commit:

`Freeze terrain skill-check helper closure`

No newer AutoPTU-Java commit was present during Pass 137.

The current commit strengthens a localized Intercept parity contract by walking reachable local helper functions used by `_terrain_skill_check_bonus` and freezing normalized helper source, calls and literals.

This remains valuable evidence for one Intercept-related terrain-skill-check path.

It does not establish generalized terrain state, protected service zones, escort semantics, broad Push/Pull/Knockback, all forced movement, generalized reactions or identity-specific mechanics.

No permanent capability category is promoted.

## AutoPTU live evidence

Current head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer AutoPTU commit was present during Pass 137.

The change synchronizes cached Pixi viewport dimensions after resize so tactical sprite destinations use current renderer geometry. Its commit message explicitly states presentation only and no battle rules or outcomes change.

It does not establish semantic projection for identity records, appointments, corrections, record custody, verification, disclosure or tactical-to-world identity consequences.

## Permanent capability map — Pass 137

No category receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

Baseline targeting and static spatial legality remain sufficient for reduced perimeter encounters.

`base movement legality`

Basic movement remains verified for conventional static BattleSpecs.

`core calculations`

Previously established parity-backed calculation infrastructure remains verified at its current baseline.

`action economy/initiative`

Baseline action economy and initiative remain verified.

`AI legal-action infrastructure`

Legal-action enumeration and validation remain verified. This does not provide objective-aware protection, escort or withdrawal policy.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

The localized Intercept path has strong contract evidence. Broad Push, Pull, Knockback, every forced-movement source, escort semantics and generalized movement reactions remain incomplete as a family.

`full turn/round lifecycle`

Ordinary progression exists. Staged staff withdrawal, protected appointment windows and multi-step escort timing are not verified as generalized lifecycle contracts.

`full stateful damage pipeline`

Substantial implemented behavior exists, but the permanent family remains partial.

`status lifecycle`

Implemented legal statuses can be used only where their exact contracts apply. No confusion, panic, disguise, identification or document-related status may be invented by this narrative layer.

`move-specific behavior`

Representative Moves do not establish full coverage. No Move may automatically authenticate, reveal identity, copy records, unlock a registry, compel disclosure or validate evidence without exact governing mechanics.

`abilities`

Representative Ability behavior does not prove the full family. No Ability creates identity truth, institutional authorization or disclosure authority.

`items`

Items remain partial. Cards, IDs, documents, stamps, seals, files or tokens receive no tactical effect unless exact rules support it.

`Trainer Features/perks`

Exact Features remain source-governed. No Feature automatically creates a license, civil identity, registry authority, forgery detector or universal identity-verification power.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

Rich office/perimeter encounters could require protected exits, protected record zones, dynamic access lanes or generalized reactions. The localized Intercept terrain helper does not provide this family.

`AI tactical policy`

Rich variants may require PROTECT, WITHDRAW, CLEAR_ROUTE, HOLD_POSITION, escort-aware behavior or avoidance of sensitive zones. Legal-action infrastructure alone does not provide those policies.

`Minecraft/Cobblemon/Craftics adapter/playback support`

Current rendering evidence does not provide semantic projection for identity verification, record-linkage state, correction propagation, privacy/disclosure, record custody or service resumption. This family remains blocking.

## Encounter review — Registry Counter Withdrawal

Full intended objective:

A tactical incident intersects an institution while staff and visitors are handling identity-related appointments. The process pauses while civilians withdraw and the tactical threat is addressed.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL for escort, Intercept and forced displacement
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for staged withdrawal
- full stateful damage pipeline — PARTIAL if attacks occur
- status lifecycle — PARTIAL for exact implemented statuses only
- terrain/weather/hazards/zones/reactions — BLOCKING for protected exits, dynamic access lanes or generalized reactions
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full version status:

BLOCKED FOR RICH SEMANTICS.

Reduced version status:

READY.

Reduced contract:

1. Identity/service verification pauses before BattleSpec creation.
2. Applicants, ordinary visitors, staff, private records, identity evidence and noncombatant Pokémon leave the tactical grid.
3. Ouros selects explicit combatants.
4. AutoPTU receives reviewed static geometry.
5. Tactical resolution may produce only `IMMEDIATE_PUBLIC_APPROACH_CLEAR` or equivalent narrow physical state.
6. The institution decides separately whether appointments resume.

Victory never verifies a person, validates evidence, links records, approves a correction, discloses a former name or grants authorization.

## Encounter review — Record Transfer Chokepoint

Full intended objective:

An already authorized physical transfer of records encounters a separate tactical threat.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement — PARTIAL for escort/Intercept/forced movement
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full lifecycle — PARTIAL for staged transfer/withdrawal
- stateful damage/status/move/ability/item/Feature families — PARTIAL as applicable to selected combatants
- terrain/hazards/zones/reactions — BLOCKING for protected-object zones/generalized reactions
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- semantic adapter/playback — BLOCKING

Full version status:

BLOCKED FOR RICH SEMANTICS.

Reduced version status:

READY.

Reduced contract:

1. Courier/Archives/record owner pauses custody movement before battle.
2. Records and storage media remain outside BattleSpec.
3. Couriers and other noncombatants withdraw.
4. AutoPTU resolves a conventional static encounter.
5. The custody owner separately resumes, reroutes or delays transfer afterward.

Victory never transfers custody, authenticates a packet, validates its contents, links identities or updates records.

## Encounter review — Verification Appointment Perimeter

Full intended objective:

A scheduled identity-related appointment is physically inaccessible because a separate tactical incident blocks the approach.

Rich dependencies:

- complete movement — PARTIAL if escort/Intercept is active
- lifecycle — PARTIAL for staged access/reopening
- terrain/hazards/zones/reactions — BLOCKING for protected approach lanes/generalized reactions
- AI tactical policy — BLOCKING
- semantic adapter/playback — BLOCKING

Reduced version status:

READY.

Reduced contract:

1. Appointment state becomes `PAUSED_ACCESS_BLOCKED` outside AutoPTU.
2. Applicant, verifier, evidence and private records remain outside BattleSpec.
3. AutoPTU resolves only the physical perimeter incident.
4. Ouros records a narrow access result.
5. The institution separately decides if and when verification resumes.

`TACTICAL_VICTORY != VERIFIED_IDENTITY`.

## PTU/Caelo unresolved mechanics

The following remain UNKNOWN unless exact governing sources and implementation contracts are identified:

- universal Trainer registration;
- universal Trainer ID numbers as diegetic identity numbers;
- Trainer licenses as a universal PTU requirement;
- passports, visas, citizenship or nationality rules;
- legal-name change procedures;
- mandatory naming structure or surname rules;
- birth-registration or civil-registry mechanics;
- universal signature mechanics;
- document-authenticity checks;
- forgery-detection DCs;
- universal identity checks using General Education, Perception, Intuition, Guile or Command;
- universal disguise-versus-identification mechanics beyond exact authored rules;
- biometric identity systems;
- fingerprints or other biological identity rules;
- Aura, Telepathy or Psychic effects as universal identity proof;
- Pokémon species as universal lie detectors or identity verifiers;
- battle victory as identity proof;
- Trainer Features that create civil registration or institutional verification authority.

Pokémon game Trainer IDs, Original Trainer metadata, Trainer Cards, Trainer Passports and League Cards are useful worldbuilding references but do not become PTU/Ouros mechanics automatically.

## Minecraft/Cobblemon authority boundary

Minecraft/Cobblemon may present world facts already decided by Ouros:

- directory boards;
- old signs;
- current public names;
- historical posters;
- desks and waiting areas;
- document props;
- appointment queues;
- archive shelves;
- corrected notices;
- context-specific NPC labels where privacy rules permit.

Minecraft/Cobblemon state does not decide:

- actor identity;
- record linkage;
- name history;
- whether an alias is deceptive;
- document authenticity;
- identity verification;
- correction approval;
- former-name disclosure;
- credential validity;
- family relationship;
- residence;
- Pokémon ownership/custody;
- institutional authorization;
- combatant selection;
- tactical legality;
- narrative consequence.

Minecraft player/entity UUIDs, nametags, skins and scoreboard values are implementation state, not automatically diegetic identity evidence.

## Canon questions left open

Which Ouros institutions maintain persistent human identity records?

Do any regions use Trainer Cards, League-style cards, Trainer Passports, licenses or another local artifact?

Which identifiers are institution-local, regional, portable or public?

What naming conventions exist in each language and culture?

How are former names, contextual names, professional/stage names and transliterations handled where those concepts exist?

What records can be corrected, by whom, using which authored authority?

How does a correction propagate downstream?

Which attributes are public, protected, private or available only for a specific service?

How do regions recognize one returning actor across differently formatted records?

Which historical NPCs already have identity/name continuity facts established by canon?

What information, if any, links a Trainer-facing record to Pokémon Agency records?

No answer is silently canonized by Pass 137.

## Pass 137 readiness conclusion

The human identity/name/record continuity layer is safe to use as world-state infrastructure because it stores provenance, uncertainty, scope and privacy rather than inventing an authority regime.

The reduced encounter variants are READY because identity verification, private records, applicants, service decisions and custody all remain outside BattleSpec before conventional combat begins.

Rich variants remain blocked by the same permanent capability families as Pass 136 when they require complete escort/forced movement, staged withdrawal, protected zones/reactions, objective-aware tactical AI or semantic Minecraft playback.

The live AutoPTU-Java evidence remains unchanged at `106dd1010eeec7ec2423688ed5eeec2274ae8d18`; AutoPTU remains unchanged at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. No family-level promotion is justified.