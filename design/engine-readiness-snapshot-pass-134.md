# Engine Readiness Snapshot — Pass 134

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-29

This snapshot records live implementation evidence checked while adding formal-education, enrollment, course, assessment and transfer continuity.

AutoPTU-Java and AutoPTU were inspected read-only. This pass writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Narrative repository inspection

Narrative head before Pass 134:

`2f1b43fff5bc223c783389326bd7c35dbb92dc25`

The recursive repository inventory was inspected before topic selection. Directory inventory and targeted code searches were also used to check likely overlaps.

Searches for school, academy, student, enrollment, attendance, curriculum and graduation found no dedicated formal-education continuity layer.

Adjacent material checked before writing included:

- `design/social-bonds-mentorship-clubs-layer.md`
- repository inventory entries for credentials/authorization, accessibility, research/fieldwork, crisis/recovery, evacuation/temporary placement, archives/privacy and institutional continuity
- engine readiness through Pass 133

The selected gap is formal institutional learning continuity without treating academic state as PTU character advancement.

## AutoPTU-Java live evidence

Current head inspected:

`0c2cdcca6634784cf0cd261f810c818897f65ac1`

Commit:

`Freeze pinned intercept terrain skill-check contract (#277)`

This is newer than the head recorded in Pass 133.

### Concrete new evidence

The commit modifies the Intercept parity workflow and the Python contract exporter.

It now exports a dedicated artifact for the Python oracle function `_terrain_skill_check_bonus` containing:

- normalized function source;
- called function names;
- string literals;
- integer literals.

CI emits the resulting `intercept-terrain-contract.tsv` alongside the existing Intercept check contract.

This is meaningful evidence that the exact Intercept terrain skill-check helper is now pinned and visible as an oracle contract.

### What this does not establish

The commit does not implement or verify the full permanent `terrain/weather/hazards/zones/reactions` capability family.

It does not by itself prove:

- generalized tactical terrain state;
- terrain creation/removal during battle;
- weather lifecycle;
- environmental hazards;
- changing zones;
- generalized reactions;
- competing reaction ordering;
- environmental forced movement;
- protected-civilian or escort reactions;
- semantic terrain playback in Minecraft/Cobblemon/Craftics;
- tactical AI understanding of terrain objectives.

The new evidence therefore does not justify a category promotion.

### Intercept evidence retained

The previously established concrete Intercept route still provides localized evidence for:

- PRE-target integration;
- interceptor movement in the implemented sequence;
- effective-defender replacement in the implemented sequence;
- server-owned Acrobatics/Athletics inputs;
- server-owned Coaching automatic-success state;
- server-owned exact `Justified [Errata]` presence;
- pinned exact Justified bonus;
- now a pinned Python terrain skill-check helper contract.

This remains a representative route, not proof of the whole movement/reaction family.

## AutoPTU live evidence

Current head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer AutoPTU commit was present during this run.

The change remains presentation-only: cached Pixi dimensions are synchronized after viewport resize so visual destinations use current renderer geometry. It does not change battle rules or outcomes.

It does not establish:

- education-state playback;
- enrollment authority;
- attendance authority;
- assessment authority;
- record-transfer semantics;
- student or instructor custody semantics;
- academic progression authority;
- combatant selection authority;
- legality authority;
- HP/status authority;
- narrative consequence authority.

## Permanent capability map — Pass 134

No category receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

Baseline targeting and spatial legality remain sufficient for conventional reduced encounters. Bespoke cover or unusual targeting geometry still needs exact evidence.

`base movement legality`

Basic movement remains verified for conventional static BattleSpecs.

`core calculations`

Previously established parity-backed calculation infrastructure remains at the verified baseline.

`action economy/initiative`

Baseline action economy and initiative remain verified.

`AI legal-action infrastructure`

Legal-action enumeration and validation remain verified at the established baseline. This does not provide objective-aware strategy.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

The current Intercept route is meaningful localized evidence, including a newly pinned terrain skill-check helper contract, but broad Push, Pull, Knockback, every forced-movement source, environmental displacement, escort semantics and generalized movement reactions remain incomplete as a family.

`full turn/round lifecycle`

Ordinary battle progression exists. Timed class withdrawal waves, staged evacuation, escort windows and protected-arrival phases are not established as a generalized contract.

`full stateful damage pipeline`

Substantial implemented behavior exists, but the permanent family remains partial.

`status lifecycle`

Existing legal statuses do not authorize invented panic, academic, attendance, stress, discipline or evacuation statuses.

`move-specific behavior`

Representative Move implementations do not prove complete coverage.

`abilities`

Representative Ability behavior and Intercept-specific Justified evidence do not prove the entire family. No Ability creates enrollment, academic standing or institutional authority.

`items`

Items remain partial. No generic diploma, school record, assignment, teaching prop or student ID tactical effect is inferred.

`Trainer Features/perks`

Exact PTU education-related Features such as Mentor remain rule-governed. Their existence does not make attendance or course completion equivalent to gaining a Feature.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

The pinned Intercept terrain skill-check oracle contract improves evidence for one helper path. Rich educational encounters still require generalized protected areas, environmental hazard state, changing zones or reactions that are not verified as a full family.

This category remains BLOCKING.

`AI tactical policy`

Rich versions require objective-aware behavior such as `PROTECT`, `WITHDRAW`, `CLEAR_ROUTE`, hold-position or avoid-protected-area decisions.

Legal-action infrastructure does not provide that policy.

`Minecraft/Cobblemon/Craftics adapter/playback support`

Coordinate-rendering hardening does not provide semantic projection of enrollment, attendance, course state, assessment state, exchange placement, student custody or educational consequences.

This category remains BLOCKING.

## Encounter review — Field Class Withdrawal

### Full intended version

Narrative objective:

Safely interrupt a supervised practical class and withdraw learners from a field site while a separate tactical incident is resolved.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL if attacks occur
- status lifecycle — PARTIAL for ordinary legal statuses
- terrain/weather/hazards/zones/reactions — BLOCKING for protected withdrawal lanes, live environmental effects or generalized reactions
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

1. Education pauses the activity.
2. Learners, instructors, teaching/rental Pokémon, records, samples and protected equipment are removed from BattleSpec or secured through world state.
3. Ouros selects explicit legal combatants.
4. AutoPTU receives static geometry.
5. Conventional combat determines immediate physical access only.
6. Education separately decides whether the class resumes, relocates or cancels.

Forbidden automatic transitions:

- victory => attendance completed
- victory => fieldwork completed
- victory => assessment satisfied
- victory => course credit granted
- victory => Skill Rank increased
- victory => Edge/Feature granted
- victory => teaching Pokémon ownership changed

## Encounter review — Practical Site Access Diversion

### Full intended version

Narrative objective:

Clear or protect an approach so a supervised class can later reach a field site, laboratory annex or training ground.

Rich requirements may include escort/Intercept movement, protected-route reactions and objective-aware AI.

Permanent dependencies remain the same as above.

Full version status:

BLOCKED FOR RICH SEMANTICS.

### Reduced version

Status: READY.

Learners and instructors remain outside BattleSpec. Explicit combatants resolve a conventional static encounter at the obstruction. Education later decides whether enough time and institutional authorization remain for the practical to proceed.

Forbidden automatic transitions:

- victory => practical started
- victory => practical completed
- victory => assignment submitted
- victory => assessment passed

## Encounter review — Exchange Arrival Perimeter

### Full intended version

Narrative objective:

Protect or restore immediate access while an exchange cohort arrives at a host institution.

Rich requirements can include staged movement, escort, protected areas and semantic playback.

Full version status:

BLOCKED FOR RICH SEMANTICS.

### Reduced version

Status: READY.

Travel/education resolves or safely pauses arrival, luggage custody and record transfer before BattleSpec creation. Students, staff, luggage, private records and teaching Pokémon remain outside tactical state. A conventional battle determines immediate perimeter access only.

Forbidden automatic transitions:

- victory => exchange enrollment accepted
- victory => records recognized
- victory => course equivalence decided
- victory => dorm assignment valid
- victory => academic completion granted

## PTU/Caelo cross-check for formal education

Project-accessible PTU rule material provides exact mechanical education and tutoring concepts, including:

- Education Skills;
- Researcher prerequisites;
- Breadth of Knowledge;
- Instruction for Assisted Skill Checks using Education Skills;
- Scholar bonuses to Education Skill checks;
- Mentor prerequisites;
- Lessons;
- Move Tutor and related Tutor Point transactions.

These mechanics are authoritative only under their exact prerequisites, targets, costs and effects.

They do not establish a universal school system.

Keep UNKNOWN unless an exact governing PTU/Caelo source plus current implementation contract establishes otherwise:

- school admission check;
- universal attendance threshold;
- grade calculation;
- course-credit system;
- graduation threshold;
- universal diploma;
- academic year based on Trainer Level;
- class attendance raising General Education or Pokémon Education;
- course completion granting Edges or Features;
- exams granting Trainer Levels;
- battle victories granting academic credit;
- Trainer Class serving as a degree;
- Education Skill Rank serving as school-year placement;
- generic teaching rules beyond exact Mentor/Tutor contracts.

Formal educational world state must never approximate exact PTU advancement or tutoring mechanics.

## Minecraft/Cobblemon implementation boundary

Safe presentation after Ouros decides state:

- class schedules and notice boards;
- cohort NPC routines;
- temporary classrooms;
- dormitory use;
- archived photographs;
- old course equipment;
- exchange students present for bounded periods;
- alumni visits;
- repurposed classrooms and field sites;
- project displays updated after authoritative educational decisions.

Minecraft/Cobblemon must not derive:

- enrollment from classroom presence;
- attendance from chunk loading;
- course completion from proximity to a teacher;
- academic success from a battle result;
- ownership from a teaching Pokémon following a learner;
- transfer recognition from inventory contents;
- a Skill Rank, Edge, Feature or Trainer Level from educational props;
- institutional authority from an NPC standing at a lectern or desk.

Ouros remains authoritative for educational world facts. AutoPTU remains authoritative for tactical battle and exact PTU mechanics.

## Canon questions remaining open

- Which Ouros regions have formal schools, academies or vocational institutions?
- What age/life-stage assumptions exist in each region?
- Are any institutions mixed-age?
- Which programs are residential?
- Which specialize in battle, research, ecology, care, craft, performance or general study?
- Which institutions exchange learners?
- What records are retained?
- What privacy scopes apply?
- What counts as course/program completion locally?
- Do any educational completions connect to separate professional credentials?
- How are practical field activities supervised?
- How are teaching/rental Pokémon owned and custodied?
- Which historical institutions have closed, merged or changed curriculum?
- Which current NPCs are students, staff or alumni?
- Which educational sites should exist physically in Minecraft?

Pass 134 intentionally answers none of these without canon authority.