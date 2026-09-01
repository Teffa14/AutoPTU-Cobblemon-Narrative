# Community Education and Field-School Learning Continuity Layer

Status: DESIGN / PROPOSED ARCHITECTURE
Pass: 192
Canon authority: none by itself

## Goal

Represent ordinary teaching, field-school sessions, public instruction, revision, and learner history in Marea without converting education into a hidden XP system, certification framework, or substitute for PTU mechanics.

This layer answers:
1. What was taught?
2. Which source or procedure version supported it?
3. Who attended or contributed?
4. What understanding was actually observed?
5. What was corrected later?

It does not grant work authority. Pass 190 remains responsible for supervised practice and operational scope changes.

## Core records

### learning_program
- program_id
- institution_or_context
- subject_family
- stated_purpose
- coordinator_role
- active_from
- active_to
- source_refs
- status

### lesson_instance
- lesson_id
- program_id
- topic
- facilitator_id
- guest_contributors
- location
- scheduled_at
- held_at
- source_or_procedure_version
- materials_refs
- attendance_mode
- interruption_state
- completion_state
- notes

### learning_evidence
- evidence_id
- learner_id
- lesson_id
- topic_scope
- evidence_type
- observable_response
- confidence
- assessor_id
- caveats
- source_refs
- recorded_at

Suggested non-mechanical evidence types:
- RECALL
- COMPARISON
- SOURCE_IDENTIFICATION
- CORRECT_UNCERTAINTY
- SAFE_REFUSAL_OR_ESCALATION
- PROCEDURE_EXPLANATION
- CORRECTION_OF_PRIOR_NOTE
- FIELD_OBSERVATION

### teaching_correction
- correction_id
- lesson_or_material_ref
- issue_found
- previous_claim_or_instruction
- corrected_claim_or_instruction
- authority_or_source_ref
- issued_by
- issued_at
- distribution_state

### learner_question
- question_id
- learner_id
- lesson_id
- question_text_or_summary
- answered_by
- answer_source_refs
- unresolved_state
- privacy

## Permanent boundaries

ATTENDED_LESSON != LEARNED_MECHANICAL_SKILL
CORRECT_ANSWER != SKILL_RANK_GAINED
FIELD_SCHOOL_RECORD != CAELO_CREDENTIAL
TEACHER_ROLE != PTU_MENTOR_EFFECT
GUEST_EXPERT != AUTHORITY_TRANSFERRED
LESSON_COMPLETED != COMPETENCY_GRANTED
COMPETENCY_EVIDENCE != CLASSROOM_MASTERY
BATTLE_WIN != EDUCATIONAL_SUCCESS
WRONG_ANSWER != PERMANENT_INCOMPETENCE
UPDATED_MATERIAL != OLD_RECORD_ERASED
MINECRAFT_BOOK_READ != KNOWLEDGE_STATE_AUTOMATICALLY_GRANTED

## Relationship to pass 190

Education and competency may touch the same person, but they track different facts.

Example:
- Jo explains a safe observation protocol during a field-school lesson;
- a learner later repeats the steps correctly: learning evidence;
- the learner later performs the task under authorized supervision: competency evidence under pass 190;
- an authorized role may later change operational scope: pass 190 grant.

The classroom record never skips those later steps.

## Learning without omniscience

Narrative should not infer that an NPC knows every fact because they attended a lesson. Knowledge should remain scoped to evidence that was actually taught, observed, or later corroborated.

A learner may:
- remember one part and forget another;
- retain an outdated version;
- understand the procedure but misunderstand the reason;
- correctly state that evidence is insufficient;
- ask another resident for clarification;
- revise an old note later.

This creates useful persistence without a single abstract 'education level'.

## Source-aware curriculum

Every lesson that teaches a factual procedure or claim should point to its source or procedure version when feasible.

Examples:
- Mirador public observation summary v3;
- Tideglass edition record;
- field-school safety sheet v2;
- Oren prevention handout;
- cooperative cultivation record template;
- Sela's published Battle Yard challenge rules.

If a source changes, create a correction or revised lesson. Preserve the old record.

## Guest instruction

Canon residents may contribute only inside their established expertise and authority.

Examples compatible with current Marea canon:
- Jo: observation, cultivation records, safe field practice;
- Oren: prevention education within verified care scope;
- Nerea: ecological/weather observation method and uncertainty;
- Taro: source comparison, editions, interviews, provenance;
- Alba: one producer's practical cultivation evidence;
- Brin: storehouse intake records and custody workflow;
- Lia: arrival/departure records and dock procedure within her role;
- Teo: ordinary equipment maintenance demonstrations;
- Sela: audited battle procedure and published yard rules;
- Ivo: purchasing and recipe substitution as ordinary practice.

A guest does not create new canon responsibilities by appearing in a lesson.

## Player participation

The player may attend, ask questions, compare sources, help set up materials, demonstrate already-authorized knowledge, retrieve a referenced document, or report an observed discrepancy.

The player cannot by lesson completion:
- grant PTU XP, levels, Skill Ranks, Features, Edges, Moves, Abilities, Tutor Points, or classes;
- certify another person;
- create Caelo credentials;
- override a supervisor or institution;
- make an uncertain interpretation canonical.

## Minecraft/Cobblemon projection boundary

Possible presentation surfaces include books, lecterns, boards, maps, item frames, sample plots, NPC gestures, field markers, projected Cobblemon companions, UI prompts, and revised handouts.

Presentation remains subordinate to Narrative state.

Examples:
- opening a Minecraft book does not prove comprehension;
- completing a quiz UI does not alter a PTU sheet unless an authoritative PTU mechanic explicitly owns that effect;
- a destroyed sign does not erase the lesson record;
- duplicated handouts do not create distinct authoritative versions;
- a Cobblemon animation can illustrate behavior but cannot prove a hidden Ability, Move, motive, or intent.

## Rich encounter template — Open Field-School Session at Glass Bend

Premise:
Jo runs a scheduled public field lesson on observation and safe route behavior near a familiar segment of Sendero del Vidrio. A wild Pokémon incident develops while learners are still present.

Full intended version:
The lesson begins with source-aware observation. When the incident occurs, participants must withdraw through constrained geometry while an authorized adult maintains safety. If tactical pressure reaches the corridor, interception, displacement, reactions, terrain, and autonomous action may matter.

Permanent capability dependencies:
- targeting/footprints/range/LoS: required;
- base movement legality: required;
- complete movement including push/pull/knockback/interception/forced movement: required if corridor protection, displacement, collision, partial stops, or interception enter BattleSpec;
- core calculations: required;
- action economy/initiative: required;
- full turn/round lifecycle: required;
- full stateful damage pipeline: required;
- status lifecycle: required if selected combat content uses statuses;
- terrain/weather/hazards/zones/reactions: required if route conditions become tactical rather than narrative framing;
- move-specific behavior: required for selected Moves;
- abilities: required for selected Abilities;
- items: required for selected battle Items;
- Trainer Features/perks: required if Trainer mechanics enter the battle contract;
- AI legal-action infrastructure: required;
- AI tactical policy: required for competent autonomous tactical choices;
- Minecraft/Cobblemon/Craftics adapter/playback support: required for faithful in-world execution and presentation.

Current disposition: FULL VERSION BLOCKED.

Reduced runnable version:
The lesson, participants, observations, withdrawal decision, and educational records remain Narrative world state. All learners and noncombatants reach a safe state before battle compilation. If a wild actor still prevents departure, AutoPTU receives a separate audited battle on stable terrain using supported content.

Allowed tactical handoffs may include:
- IMMEDIATE_ROUTE_THREAT_WITHDREW
- IMMEDIATE_CLEARING_SECURED
- SUPPORTED_MECHANICAL_AFTERMATH

Afterward, Jo may record that a learner identified a correct observation, asked for help, or followed the withdrawal instruction. Narrative may also record that the lesson was interrupted and must be rescheduled. The battle result cannot grant a Skill Rank, class, qualification, relationship improvement, or operational scope.

## Integration with existing layers

Supervised practice remains authoritative for competency observations and operational scope.
Preparedness remains authoritative for drills and corrective actions.
Public exhibition remains authoritative for public demonstrations and formal event procedure.
Mirador/Tideglass provenance systems remain authoritative for scientific and archival claims.
Care systems remain authoritative for actual treatment and recovery.
Battle institutions remain authoritative for Bruma Battle Yard challenge contracts.

This layer only tracks teaching, attendance, learning evidence, questions, and correction history.

## Promotion gate

Before any education concept becomes canon, verify:
- the teaching location and responsible role already exist or are explicitly promoted;
- the topic fits that role's current authority;
- no PTU advancement is being simulated narratively;
- any Caelo schooling, credential, age, licensing, or examination claim has a source;
- source/procedure versions are preserved;
- Minecraft presentation does not become rules authority.
