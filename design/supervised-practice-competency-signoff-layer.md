# Supervised Practice and Competency Sign-off Layer

Status: DESIGN / PROPOSED ARCHITECTURE
Canon authority: none by itself
Pass: 190

## Goal

Represent gradual professional growth for persistent NPCs without turning ordinary training into a hidden XP system, a relationship meter, a new legal regime, or a shortcut around PTU mechanics.

The layer answers four questions:
1. What narrow task is being practiced?
2. Under what supervision may it be performed?
3. What evidence exists from prior attempts?
4. Which already-authorized role may change the person's operational scope?

It does not decide who holds institutional authority. That comes from canon.

## Core records

### practice_pathway
- pathway_id
- institution_or_context
- role_family
- scope_definition
- current_procedure_version
- evidence_requirements
- recognized_supervisor_roles
- allowed_practice_modes
- review_trigger
- status

### competency_observation
- observation_id
- subject_id
- pathway_id
- task_scope
- procedure_version
- supervision_mode
- timestamp
- location
- observer_id
- observable_actions
- result
- exceptions_encountered
- escalation_behavior
- caveats
- evidence_refs
- provenance

### operational_scope_grant
- grant_id
- subject_id
- institution
- scope_definition
- supervision_level
- issuer_id
- authority_basis_ref
- effective_from
- review_after
- suspension_or_revocation_state
- notes

### procedure_handoff
- handoff_id
- from_actor
- to_actor
- procedure_id
- procedure_version
- demonstrated_steps
- unresolved_exceptions
- reference_materials
- witnessed_at

## Proposed supervision states

OBSERVE_ONLY
ASSIST_UNDER_DIRECT_SUPERVISION
PERFORM_UNDER_DIRECT_SUPERVISION
PERFORM_WITH_SUPERVISOR_AVAILABLE
INDEPENDENT_WITHIN_DEFINED_SCOPE
SUSPENDED_PENDING_REVIEW

These are architecture states, not Caelo credentials or canon titles.

## Evaluation rule

Competency evidence is contextual. A record should preserve task scope, procedure version, supervision mode and conditions. The evaluator can record successful work while still declining broader independence.

Recognizing a limit and escalating correctly is a positive observable outcome. The design must not reward a trainee for improvising beyond authorized scope merely because the improvisation succeeds.

A failed attempt may result in a narrower next task, another supervised attempt, a procedure correction, equipment review, or no change. It must not automatically create humiliation, hostility, relationship damage or permanent incompetence.

## Procedure revision

A material procedure revision does not erase old observations. It can reduce how strongly they support current readiness.

Example:
- observation A proves safe performance under procedure v2;
- procedure v3 changes one critical step;
- observation A remains historical evidence;
- independent scope for the changed step can remain pending until demonstrated under v3.

This preserves world history instead of rewriting it.

## Player participation

The player can:
- demonstrate a task when canon allows;
- observe and report factual behavior;
- assist within a defined role;
- create an opportunity for practice;
- choose not to take over a routine problem;
- provide evidence to an authorized reviewer.

The player cannot, merely by quest completion:
- grant institutional authority;
- promote an NPC;
- award a PTU Feature, Edge, Skill Rank, Move, Ability, level or Experience;
- certify a procedure;
- redefine another institution's scope;
- convert a relationship state into competence.

## PTU boundary

The PTU Mentor class is mechanical content. Its Effects operate only through PTU rules and authoritative engine state.

Narrative terms such as teacher, supervisor, apprentice, trainee, lesson or mentorship remain ordinary world concepts unless a character sheet explicitly establishes the relevant PTU Class/Feature.

If an encounter depends on a Trainer Feature interrupt, Move Tutor effect, Ability change, Skill Rank, Pokémon capability or other mechanical consequence, that dependency must be classified against the corresponding engine capability family and verified contract. Narrative never emulates the effect.

## Minecraft/Cobblemon boundary

Visible work may be projected through blocks, tools, animation, carried items, NPC pathing, signs, books, UI or Cobblemon entities.

Those projections cannot themselves create qualification. Examples:
- completing a Minecraft interaction does not issue an operational grant;
- wearing a uniform or carrying a tool does not prove authority;
- an NPC path successfully reaching a station does not prove competence;
- a Cobblemon performing an animation does not prove a Trainer Feature occurred;
- client-side UI cannot promote a scope without server-authoritative Narrative state.

## Battle handoff contract

When supervised practice overlaps with combat, compile only facts the battle engine owns.

Permitted inputs include audited combatants, positions, battle contract, legal battlefield geometry and content known to be supported.

Permitted outputs include immediate tactical facts and supported mechanical aftermath.

Forbidden direct outputs include:
COMPETENCY_GRANTED
PROMOTION_APPROVED
RELATIONSHIP_IMPROVED
INSTITUTIONAL_AUTHORITY_GRANTED
PROCEDURE_CERTIFIED
PTU_FEATURE_LEARNED
MENTOR_CLASS_GAINED

A supervisor may later consider battle logs as one evidence source, but the battle result never performs the sign-off.

## Rich encounter template — Supervised Field Lead at Glass Bend

Premise:
A resident who already assists with routine field work is given a narrow opportunity to lead a familiar segment while an authorized senior remains available. A wild threat interrupts the task.

Full intended version:
The trainee must maintain a retreat corridor, keep noncombatant field participants out of tactical danger, communicate an escalation, and avoid exceeding the assigned field scope. If the threat reaches the tactical space, movement geometry and reactions matter.

Permanent capability dependencies:
- targeting/footprints/range/LoS: required;
- base movement legality: required;
- complete movement including push/pull/knockback/interception/forced movement: required if corridor protection, interception, displacement, collision or partial stops enter BattleSpec;
- core calculations: required;
- action economy/initiative: required;
- full turn/round lifecycle: required;
- full stateful damage pipeline: required;
- status lifecycle: required if selected combat content uses statuses;
- terrain/weather/hazards/zones/reactions: required if field conditions are tactical rules rather than world-state framing;
- move-specific behavior: required for selected Moves;
- abilities: required for selected Abilities;
- items: required for selected battle Items;
- Trainer Features/perks: required if Trainer mechanics enter the battle contract;
- AI legal-action infrastructure: required;
- AI tactical policy: required for competent autonomous tactical choices;
- Minecraft/Cobblemon/Craftics adapter/playback support: required for faithful in-world execution and presentation.

Current disposition: FULL VERSION BLOCKED.

Reduced runnable version:
The supervised field task, observers, retreat decision and competency evidence remain Narrative world state. All noncombatants are moved to a safe state before battle compilation. If a wild actor still prevents departure, AutoPTU receives a separate audited battle on stable terrain with a supported roster.

Allowed handoffs may include:
- IMMEDIATE_ROUTE_THREAT_WITHDREW
- IMMEDIATE_CLEARING_SECURED
- SUPPORTED_MECHANICAL_AFTERMATH

After the battle, the supervisor records what was actually observed before, during and after the interruption. Narrative decides whether scope remains unchanged, narrows, or becomes eligible for later review. Winning the battle cannot grant independence.

## Integration with existing Narrative layers

Institutional delegation remains authoritative for who may authorize work.
Field search remains authoritative for search cases and sectors.
Preparedness remains authoritative for drill plans and corrective actions.
Provisioning remains authoritative for institutional stock.
Correspondence remains authoritative for messages and acknowledgments.
Rival continuity remains authoritative for rivalry state.
Public exhibition remains authoritative for event procedure and audience records.

This layer only records supervised practice, contextual evidence and scoped responsibility changes issued by authority that already exists elsewhere.

## Promotion gate

Before any proposed practice pathway becomes canon, verify:
- the institution and role already exist in canon;
- the proposed supervisor actually has authority for that scope;
- the task does not silently require an unverified PTU mechanic;
- any Caelo-specific profession or credential is sourced;
- the procedure has a version/provenance trail;
- Minecraft representation does not become rules authority.