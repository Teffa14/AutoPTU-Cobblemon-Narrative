# Engine readiness snapshot — Pass 170

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-31

## Read-only heads inspected

AutoPTU-Java main: `54feddaa3d95ab75d1efb90ea062ef20234627a8`.
Head message: `Freeze shadow tag forced movement geometry (#310)`.

AutoPTU main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.
Head remains presentation-only: renderer coordinates stay synchronized after viewport resize; the commit explicitly states that battle rules and outcomes do not change.

Neither engine repository was modified by this pass.

## Java evidence

PR #310 adds a pinned Python-oracle contract for `shadow_tag_anchor` inside `apply_forced_movement`. The test freezes the anchor setup and the per-candidate distance guard using `_combatant_distance_to_coord`, and CI now exports and checks that geometry contract alongside the existing forced-movement oracle suite.

This improves evidence for one temporary-state forced-movement geometry rule. It does not by itself prove equivalent production Java behavior for Shadow Tag movement restriction, nor does it establish complete movement as a whole.

Live evidence across recent heads already demonstrates a production post-hit forced-movement seam, selected Push behavior, ability modifiers, selected defender ability prevention, status/temporary-state prevention and now additional oracle coverage for Shadow Tag anchor geometry.

Still unverified as complete families include all Push and Pull cases, general Knockback, every Intercept ordering, arbitrary forced movement, all terrain/weather displacement, every Item/Ability/Feature source, escort/rescue, protected-object carrying, crowd routing, vehicles/platforms, generalized reaction windows and objective-aware tactical policy.

No permanent category is promoted.

## Permanent capability map

VERIFIED
- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL
- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING
- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Pass 170 encounter dependency review

Field Practicum Route Incident full version: BLOCKED. It can require escort/protection behavior, Intercept and forced movement under complete movement, full lifecycle, terrain/weather/hazards/zones/reactions, audited move/ability/item/Feature behavior, AI tactical policy and semantic adapter/playback. Reduced version is READY at narrative-contract level after individual combat-content audit because learners and supervisors leave BattleSpec before initiative.

Laboratory Evacuation Exercise Interrupted full version: BLOCKED. A rich implementation requires escort/protection, potentially protected-object movement, full lifecycle, hazard and reaction behavior, tactical objectives and semantic playback. Reduced version keeps students, staff and equipment outside BattleSpec and permits only immediate perimeter clearance.

Assessment Site Access Incident full version: BLOCKED if timed access, evaluator protection or dynamic route control are tactical objectives. Reduced version pauses the assessment until after an ordinary audited battle and allows only `IMMEDIATE_ASSESSMENT_SITE_APPROACH_CLEAR` as a tactical-world output.

Field Project Artifact Recovery Perimeter full version: BLOCKED by protected-object carrying, complete movement, lifecycle, possible hazards/reactions, tactical-objective policy and semantic adapter/playback. Reduced version keeps the artifact outside BattleSpec and permits only immediate area clearance.

## Education mechanics boundary

Project-source search confirms explicit PTU mechanics around Education Skills and Features including Scholar, Mentor, Lessons, Move Tutor, PokéManiac and Ace Trainer. Those mechanics have prerequisites, frequencies and effects and therefore cannot be granted by narrative schooling.

The education continuity layer must never infer:

- Skill Rank gain from attendance;
- Edge gain from course completion;
- Feature gain from graduation;
- Trainer Class from a diploma or job title;
- Mentor Feature from employment as an instructor;
- Tutor Points or Move learning from generic classroom participation;
- battle modifiers from student status;
- progression from a school battle unless governing PTU/Caelo rules explicitly authorize it.

UNKNOWN pending exact Caelo source verification:

- named Caelo schools, academies, universities or training institutions;
- Caelo-specific enrollment, graduation or certification rules;
- education-related downtime systems;
- credential requirements for occupations or institutions;
- formal recognition of apprenticeship or non-formal learning;
- school-specific battle, fieldwork or examination mechanics;
- Feature, Edge or Skill progression explicitly tied to instruction or curriculum;
- institutional permissions for specialist equipment;
- any Caelo rule that converts academic performance into mechanical progression.

## Adapter boundary

Minecraft/Cobblemon may render campuses, classrooms, laboratories, dormitories, teachers, students, schedules, blackboards, books, uniforms, examinations and ceremonies.

Presentation does not establish enrollment, attendance, curriculum completion, grades, credentials or recognition.

Loaded NPC count is not class enrollment.

A Minecraft book is not a transcript without an Ouros academic-record link.

A scoreboard number is not an assessment result unless Ouros authors it under the governing educational rule.

Cobblemon/Minecraft battle-state authority remains excluded. AutoPTU decides tactical facts. Narrative decides what educational consequence, if any, follows under authored institutional rules.

## Promotion rule

A permanent capability category changes only when live tests/contracts demonstrate the family broadly enough to justify promotion. A single Shadow Tag geometry contract, selected Push integration, one educational encounter or one school-related Feature remains representative evidence only.