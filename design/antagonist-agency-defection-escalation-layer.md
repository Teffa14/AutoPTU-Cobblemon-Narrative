# Ouros Antagonist Agency, Defection & Escalation Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already has factions, actor knowledge, faction fronts, cases, public memory, crisis state and recurring rivals. This layer adds a dedicated model for persistent opposition.

The goal is to make adversaries behave like actors with goals, limits, uncertainty and social ties rather than like quest triggers that exist only when a player enters their room.

## 1. Opposition is relational

Do not store `villain = true` as the primary narrative model.

Store conflicts between goals.

```yaml
opposition_relation:
  relation_id: null
  actor_a: null
  actor_b: null
  conflicting_goals: []
  contested_resources: []
  contested_locations: []
  active_methods: []
  intensity: low
  public_visibility: low
  last_direct_conflict: null
  deescalation_conditions: []
  coexistence_possible: unknown
```

An actor may oppose the player on one issue and cooperate on another.

## 2. Adversarial actor state

```yaml
adversarial_actor:
  actor_id: null
  active_goals: []
  red_lines: []
  preferred_methods: []
  forbidden_methods: []
  resource_access: {}
  known_allies: []
  hidden_allies: []
  dependencies: []
  obligations: []
  current_plan_id: null
  fallback_plan_ids: []
  actor_knowledge_ref: null
  attention_state: {}
  risk_tolerance: medium
  exposure_tolerance: medium
  surrender_conditions: []
  withdrawal_conditions: []
  defection_pressure: 0
  status: active
```

The generator must not add a hidden goal merely to justify a twist. Hidden intent must come from authored state, prior evidence or an approved generation path.

## 3. Doctrine, leadership and membership remain separate

```yaml
organization_belief_structure:
  faction_id: null
  public_doctrine: []
  operational_doctrine: []
  leadership_goals: []
  internal_groups: []
  member_belief_distributions: []
  tolerated_dissent: unknown
```

This permits:

- leaders who exploit a sincere movement;
- members who accept the cause but reject the method;
- cells that radicalize independently;
- reformers who stay inside;
- defectors who preserve part of the ideology;
- organizations whose leadership changes without erasing institutional history.

## 4. Plan objects

```yaml
actor_plan:
  plan_id: null
  owner_actor_id: null
  goal_id: null
  current_step: 0
  steps: []
  required_assets: []
  required_information: []
  blockers: []
  exposure_risk: low
  cost_profile: {}
  fallback_on_failure: []
  abort_conditions: []
  evidence_outputs: []
  world_state_outputs: []
```

A plan must be executable from the actor's known state and resources.

The generator may not select an action because it would create a dramatic scene if the actor lacks the knowledge, access or means to attempt it.

## 5. Attention budget

Persistent enemies should not counter the player everywhere.

```yaml
attention_state:
  actor_id: null
  target_id: null
  awareness: none
  concern: low
  priority: low
  last_verified_event: null
  intelligence_confidence: low
  assigned_resources: []
```

Escalation should usually require a change in awareness, concern or priority.

Possible causes:

- player interrupts a front;
- public exposure;
- loss of an important asset;
- rescue of a target;
- theft or recovery of evidence;
- repeated interference;
- faction ally request;
- credible intelligence about future player action.

Rumors alone may raise concern without creating certainty.

## 6. Escalation ladder

Escalation is a state transition with cost and cause.

```yaml
escalation_state:
  conflict_id: null
  stage: observation
  prior_stage: null
  trigger_event_ids: []
  resources_committed: []
  methods_unlocked: []
  methods_still_prohibited: []
  visibility_change: none
  deescalation_routes: []
```

Suggested abstract stages:

- unaware
- observation
- obstruction
- targeted pressure
- active operation
- major confrontation
- collapse / settlement / transformation

These are narrative stages only. They do not grant battle bonuses.

An actor may deescalate when cost rises, goals change, evidence changes, leadership changes or a negotiated condition is met.

## 7. Internal cells and fault lines

```yaml
internal_group:
  group_id: null
  parent_faction_id: null
  members: []
  shared_beliefs: []
  preferred_methods: []
  leader_ids: []
  grievances: []
  external_contacts: []
  cohesion: medium
  break_conditions: []
```

Internal conflict can produce:

- leadership challenge;
- policy dispute;
- resource split;
- reform attempt;
- coup;
- splinter group;
- quiet defection;
- whistleblowing;
- negotiated exit;
- reconciliation.

Do not create an internal schism merely to rescue the players from consequences.

## 8. Defection state

```yaml
defection_event:
  event_id: null
  actor_id: null
  from_faction_id: null
  to_faction_id: null
  new_status: independent
  trigger_facts: []
  retained_beliefs: []
  rejected_beliefs: []
  retained_contacts: []
  severed_contacts: []
  knowledge_carried: []
  access_revoked: []
  access_retained: []
  public_status: unknown
  retaliation_risk: unknown
```

Hard rules:

- defection does not erase prior wrongdoing;
- defection does not imply friendship with the player;
- leaving an organization does not automatically reveal every secret;
- a former member may retain incorrect beliefs;
- knowledge carried out must be knowledge the actor actually had;
- access should be explicitly revoked or retained.

## 9. Surrender, withdrawal and temporary alliance

Narrative state may recognize these outcomes before AutoPTU can execute them mechanically.

```yaml
conflict_resolution_intent:
  type: SURRENDER | WITHDRAW | TEMPORARY_ALLIANCE | NEGOTIATED_PAUSE | DEFEAT | ESCAPE
  initiating_actor_id: null
  conditions: []
  accepted_by: []
  rejected_by: []
  mechanical_resolution_ref: null
  followup_state_changes: []
```

No narrative script may end a battle mechanically until the authoritative battle layer supports or validates the relevant outcome.

A reduced encounter can move negotiation before or after an ordinary legal battle while preserving the same story premise.

## 10. Successor problem

Defeating a leader should trigger a successor evaluation, not automatic faction deletion.

```yaml
succession_review:
  faction_id: null
  triggering_event_id: null
  leader_status: removed
  viable_successors: []
  internal_groups: []
  asset_control: {}
  doctrine_pressure: []
  likely_outcomes:
    - dissolve
    - reform
    - fragment
    - radicalize
    - continue
    - merge
    - retreat
```

The resulting outcome should depend on actual organization state.

## 11. Antagonist memory

Important adversaries may remember:

- confirmed player tactics they personally observed;
- public battle footage or records they plausibly accessed;
- prior negotiations;
- injuries or losses that affected them;
- broken promises;
- spared or captured allies;
- locations compromised;
- evidence exposed;
- successful deception later discovered.

They may not read private movesets, hidden inventories, future player plans or world truth.

## 12. Opposition without combat

Valid adversarial actions include:

- withholding service where they control it;
- recruiting;
- lobbying or influencing a civic process if their role allows it;
- moving assets;
- evacuating a site;
- destroying their own compromised records;
- spreading a claim through existing media channels;
- hiring protection;
- relocating a target;
- abandoning a front;
- negotiating;
- infiltrating;
- observing;
- cutting a supply relationship;
- offering cooperation against a third threat.

Every action must pass the same world-state, knowledge and resource checks as any other actor action.

## 13. Encounter implementation contracts

Mechanically rich antagonist scenes must use the permanent capability categories from `design/encounter-implementation-contracts.md`.

### Ambush at the Switch House

Narrative premise: an adversarial cell attempts to seize a control point before the players can secure evidence stored there.

Full version:

- two approach routes;
- interception and body-blocking;
- a DISABLE_OBJECT / PROTECT objective around the control console;
- delayed attack behavior from a prepared attacker;
- opponents change priorities if the evidence leaves the room.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced version:

The console and evidence transfer resolve in the overworld before combat. AutoPTU runs a static legal battle against the cell after the players secure or fail to secure the evidence. No interception, forced movement or objective-aware AI is simulated.

### Defector Extraction

Narrative premise: a former member has agreed to leave an organization but both sides have incomplete information about whether pursuit is underway.

Full version:

- ESCAPE / PROTECT objective;
- pursuers may choose the defector over player combatants;
- route blockers and interception;
- surrender/withdrawal possible if leadership conditions change mid-fight;
- actor knowledge determines which exits pursuers cover.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- status lifecycle — PARTIAL if status-heavy pursuit is used
- terrain/weather/hazards/zones/reactions — BLOCKING if reactive zone control is used
- move-specific behavior — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced version:

The defector remains outside the grid. Players fight a normal legal chokepoint battle whose authoritative result changes whether the overworld extraction route remains open. Pursuers never target an off-grid actor through scripted damage.

### Negotiated Last Stand

Narrative premise: a hostile leader is cornered but still has a concrete objective and may choose to withdraw, surrender or continue depending on verified state.

Full version:

- battle state exposes SURRENDER and WITHDRAW intents;
- leader AI evaluates objective success, ally state and escape viability;
- environmental hazards may change the acceptable risk calculation;
- delayed-hit mechanics may remain active if legal moves create them.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced version:

The battle remains a standard DEFEAT encounter. If the authoritative battle reaches an authored checkpoint where negotiation is legally possible, the battle can end only through an approved external handoff rather than hidden Minecraft scripting. Until such a handoff exists, negotiation occurs before battle or after defeat.

## 14. Delayed-hit evidence update

Current AutoPTU-Java evidence inspected for this pass includes commit `62e6bef9e45b2e30febb48b4b6b73927c36328c0`, which binds delayed-hit entries to canonical move execution inputs and targets with Python-oracle parity.

This is meaningful evidence for a delayed-hit slice of move-specific behavior and lifecycle infrastructure.

It does not establish:

- all delayed move execution;
- all move-specific behavior;
- all lifecycle hooks;
- all target-change semantics;
- hazards;
- reactions;
- tactical AI.

The category remains PARTIAL.

## 15. Promotion rules

A proposed antagonist encounter may enter future canon as narrative content while its tactical form remains reduced.

Promotion to a full battle implementation requires:

- exact PTU/Caelo legality review;
- Python-oracle evidence for required behavior;
- Java evidence for each exact dependency;
- adapter support for all required playback/state transitions;
- no Minecraft-side substitute rule;
- AI policy evidence when outcome depends on objective-aware enemy decisions.

## 16. Anti-railroading rules

The antagonist system must not preserve a planned confrontation at all costs.

If players:

- expose the plan early;
- remove the required resource;
- persuade a key member;
- relocate the target;
- create a stronger alliance;
- make the plan irrational;

then the actor should replan, retreat, escalate differently or abandon the objective.

The story may preserve consequences. It must not preserve an invalid plan merely because a boss room was authored.
