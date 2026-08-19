# Ouros Infiltration, Stealth & Cover Identity Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already has actor knowledge, cases, evidence custody, faction plans, communications, settlements, travel, public memory and encounter implementation contracts. This layer adds covert access and counter-infiltration without collapsing them into a single `hidden` flag or forcing every failed operation into combat.

The model supports physical concealment, social cover, insider access, authorized audits, covert observation, tailing, counter-infiltration and extraction. It does not define PTU skill DCs, Trainer Feature effects, Pokémon capability effects or Minecraft detection math.

## 1. Identity has several layers

An actor can have one canonical identity, several legitimate roles and one or more temporary presented identities.

```yaml
identity_state:
  actor_id: null
  canonical_identity_ref: null
  legitimate_role_refs: []
  public_identity_refs: []
  cover_identity_refs: []
  retired_identity_refs: []
  identity_privacy: private
```

A cover does not rewrite canonical identity.

```yaml
cover_identity:
  cover_id: null
  actor_id: null
  presentation_name: null
  claimed_affiliations: []
  claimed_role: null
  appearance_presentation_refs: []
  supporting_credential_refs: []
  supporting_contact_ids: []
  rehearsed_claim_refs: []
  intended_access_scope_ids: []
  created_for_operation_id: null
  activation_time: null
  expiry_condition: null
  status: prepared
  compromised_observer_ids: []
  compromised_institution_ids: []
  provenance_refs: []
```

Suggested states:
- PREPARED
- ACTIVE
- QUESTIONED
- PARTIALLY_COMPROMISED
- BURNED
- RETIRED

A cover can be burned in one institution while still unknown elsewhere.

## 2. Observer belief is local

Security actors and NPCs should react to what they know or believe.

```yaml
observer_identity_belief:
  observer_id: null
  subject_actor_id: null
  believed_identity_ref: null
  confidence: low
  supporting_observation_ids: []
  contradicting_observation_ids: []
  last_updated: null
  shared_with_ids: []
```

Hard rules:
- seeing an actor does not reveal canonical identity;
- recognizing a Pokémon does not automatically identify its Trainer;
- one witness discovering a cover does not notify an entire faction instantly;
- information spreads through the existing communications layer;
- a wrong belief remains a belief until evidence changes it.

## 3. Security zones

Restricted locations need explicit access state.

```yaml
security_zone:
  zone_id: null
  location_id: null
  owner_institution_id: null
  normal_access_policy_ref: null
  public_entry_points: []
  restricted_entry_points: []
  credential_categories: []
  escort_policies: []
  active_security_actor_ids: []
  patrol_plan_refs: []
  alarm_channel_refs: []
  known_hazard_refs: []
  known_camera_or_sensor_refs: []
  current_security_state: normal
```

The generator must not invent cameras, scanners, locks, radio networks or biometric systems unless the location canon says they exist.

A disguise is not an access token. A real credential is not proof that the holder is who an observer believes them to be. Both facts can matter independently.

## 4. Access claims and credentials

```yaml
access_claim:
  claim_id: null
  actor_id: null
  cover_id: null
  zone_id: null
  credential_ref: null
  escort_actor_id: null
  stated_purpose_ref: null
  submitted_at: null
  reviewed_by_id: null
  result: pending
  result_reason_ref: null
```

Suggested results:
- GRANTED
- GRANTED_LIMITED
- ESCORT_REQUIRED
- QUESTIONED
- DENIED
- REVOKED

This is world-state access logic. It does not define a Guile roll or a Stealth check.

## 5. Infiltration operation

```yaml
infiltration_operation:
  operation_id: null
  sponsor_actor_or_institution_id: null
  participant_ids: []
  objective_refs: []
  target_location_ids: []
  target_information_refs: []
  allowed_methods: []
  prohibited_methods: []
  cover_refs: []
  legitimate_access_refs: []
  entry_plan_refs: []
  exit_plan_refs: []
  fallback_plan_refs: []
  abort_conditions: []
  exposure_risks: []
  evidence_risks: []
  current_phase: planning
  status: active
```

Suggested phases:
- PLANNING
- APPROACH
- ENTRY
- ACCESS
- OBJECTIVE
- EXTRACTION
- DEBRIEF
- CLOSED

An operation can succeed at its objective while losing the cover, or preserve the cover while failing to obtain the objective.

## 6. Covert modes remain distinct

Useful modes include:
- physical concealment;
- social cover;
- legitimate insider access used discreetly;
- authorized inspection with undisclosed investigative purpose;
- observation from a public area;
- tailing;
- covert evidence preservation;
- counter-infiltration;
- extraction of a willing actor;
- reconnaissance before a battle.

The mode determines what information and permissions matter. It does not grant mechanics by itself.

## 7. Suspicion is local and evidential

Do not use one universal stealth meter for the whole region.

```yaml
suspicion_state:
  observer_or_institution_id: null
  subject_actor_or_cover_id: null
  stage: unaware
  trigger_observation_ids: []
  unresolved_questions: []
  confidence: low
  current_response_refs: []
  expires_or_decays_under: []
```

Suggested narrative stages:
- UNAWARE
- NOTICED
- CURIOUS
- QUESTIONING
- CONCERNED
- COVER_COMPROMISED
- ACTIVE_ALARM

These are narrative states only. Exact opposed checks and PTU modifiers remain external.

A minor inconsistency can create `QUESTIONING` without starting combat. A confirmed hostile act may create an alarm immediately if the institution has the means to communicate it.

## 8. Patrols have jobs

```yaml
security_patrol:
  patrol_id: null
  institution_id: null
  actor_ids: []
  responsibility_refs: []
  route_ref: null
  shift_window_ref: null
  checkpoints: []
  expected_contacts: []
  current_task: patrol
  current_knowledge_ref: null
  response_policy_ref: null
```

Patrols should protect something or perform a task. They should not wander solely to create arbitrary detection rolls.

World-state changes can alter patrols:
- staff shortage;
- public event;
- crisis response;
- known intrusion;
- route closure;
- shift change;
- maintenance work;
- false alarm;
- internal faction conflict.

## 9. Detection event

Detection must have a source.

```yaml
detection_event:
  event_id: null
  observer_ids: []
  subject_ids: []
  cover_id: null
  location_id: null
  observation_type: null
  observed_fact_refs: []
  inferred_claim_refs: []
  confidence: null
  immediate_response_refs: []
  communication_packet_refs: []
  evidence_created_refs: []
```

Possible observations:
- unexpected presence;
- inconsistent statement;
- invalid credential;
- recognized face;
- recognized Pokémon;
- unauthorized item;
- door or object state changed;
- visible trespass;
- sound or movement where none was expected;
- witness report;
- recovered physical trace.

The observation and the observer’s inference remain separate.

## 10. Distractions are world events

```yaml
distraction_event:
  event_id: null
  source_actor_id: null
  location_id: null
  observable_effect_refs: []
  intended_observer_ids: []
  actual_observer_ids: []
  response_events: []
  unintended_consequences: []
```

A distraction can draw a patrol only when the patrol can perceive it and considers it relevant to its responsibility.

The narrative system must not invent a universal “guard distracted for 30 seconds” rule.

## 11. Alarm propagation

Alarms use the communications layer.

```yaml
security_alert:
  alert_id: null
  originating_event_id: null
  sender_id: null
  channel_ref: null
  recipient_scope_refs: []
  claim_refs: []
  confidence: null
  delivery_records: []
  correction_refs: []
```

Consequences:
- some guards may receive the alert;
- some may receive it late;
- some areas may be isolated;
- the alert may contain a wrong description;
- later corrections do not erase the first alert from history.

This prevents instant faction omniscience.

## 12. Traces and evidence

Covert operations can create ordinary evidence.

Possible traces:
- witness memory;
- altered access record;
- moved object;
- copied document record;
- damaged lock or door if canonically present;
- lost equipment;
- unusual Pokémon sighting;
- communication intercept if supported;
- false credential record;
- inconsistent shift log.

All traces feed the existing evidence/custody system. The infiltration layer does not create a separate truth system.

## 13. Cover compromise

```yaml
cover_compromise_event:
  event_id: null
  cover_id: null
  discovering_actor_ids: []
  discovering_institution_ids: []
  evidence_refs: []
  confidence: null
  communicated_to_ids: []
  access_revocations: []
  public_visibility: low
  affected_future_operations: []
```

Compromise can be partial.

Examples:
- one guard recognizes the actor but has not reported it;
- a credential is revoked but the alias remains unknown;
- a faction learns the alias but not the real name;
- public media reports an alias incorrectly;
- an ally knows the true identity but continues to protect it.

## 14. Recognition and persistent memory

Recognition can come from repeated contact.

```yaml
recognition_record:
  observer_id: null
  subject_ref: null
  recognition_basis_refs: []
  confidence: null
  last_seen_location_id: null
  last_seen_time: null
```

The system should never generate “everyone forgets” merely because an operation ended.

A distinctive Pokémon can become part of recognition history. That still does not prove who currently controls it or who a disguised actor is without supporting evidence.

## 15. Team infiltration

```yaml
team_cover_plan:
  operation_id: null
  participant_cover_ids: []
  shared_story_refs: []
  individual_story_refs: []
  known_relationship_claims: []
  meeting_points: []
  emergency_signals: []
  separation_plan_refs: []
```

One participant being questioned should not automatically burn every other cover. Contradictions can create localized suspicion and force the group to adapt.

## 16. Pokémon participation

Pokémon can contribute only through authoritative state.

Possible relevant PTU concepts include Stealth, Telepathy, Phasing, Invisibility, Dead Silent, Blender, unusual senses and movement capabilities. Exact legality and effects must be read from PTU/Caelo and the individual Pokémon record.

Hard rules:
- species flavor never grants a capability;
- a narrative tag never grants mechanical concealment;
- a Pokémon partner can itself be recognizable;
- a capability useful in battle is not automatically an overworld stealth system;
- if a capability has frequency, action, duration or restriction rules, those rules remain authoritative.

## 17. Counter-infiltration

NPC factions use the same model.

An institution or hostile group may infiltrate another organization only when its actors possess:
- a plausible plan;
- access;
- knowledge;
- resources;
- a cover or legitimate role;
- time;
- an objective.

The operation can generate traces and mistakes. It does not happen because the generator needs a twist.

Counterintelligence content can emerge from:
- inconsistent records;
- a staff member with unexplained access;
- two identities linked by evidence;
- a contact who knows more than their role suggests;
- repeated information leaks;
- a patrol responding before an alert should have reached them;
- an internal group changing plans after supposedly private meetings.

These are investigation hooks, not automatic proof of an infiltrator.

## 18. Success, failure and partial outcomes

Possible successful outcomes:
- observation completed;
- information copied or remembered;
- actor contacted;
- target identified;
- route mapped;
- evidence preserved;
- object tagged;
- access established for later;
- willing person extracted;
- battle avoided;
- future battle begins with better information.

Possible costs:
- cover weakened;
- credential burned;
- witness created;
- target becomes suspicious;
- faction attention rises;
- exit route lost;
- evidence left behind;
- ally exposed;
- objective only partially completed.

Failed covert access does not automatically equal failed quest.

## 19. Extraction and debrief

```yaml
operation_debrief:
  operation_id: null
  objective_results: []
  confirmed_observations: []
  unverified_claims: []
  evidence_refs: []
  cover_status_changes: []
  institution_attention_changes: []
  witness_ids: []
  unresolved_risks: []
  future_hook_refs: []
```

A debrief should preserve what was learned, what was only inferred and which access routes remain viable.

## 20. Player authorship and privacy

The system must not invent a PC’s secret identity, criminal history, institutional affiliation, reason for using a disguise, private loyalties or willingness to impersonate someone.

Cover identities for PCs require player-authored or explicitly chosen state.

In multiplayer:
- a cover’s true owner can remain private from other players;
- private operation data must not leak through UI or NPC dialogue;
- another player seeing the cover does not reveal the canonical identity;
- PvP counter-infiltration needs explicit server rules and consent boundaries before use.

## 21. Minecraft/Cobblemon representation

Possible presentation:
- restricted doors and checkpoints;
- staff-only corridors;
- visitor badges or in-world credentials;
- patrol NPCs;
- shift changes;
- public and private entrances;
- disguises as cosmetic presentation when supported;
- location-specific dialogue based on observer belief;
- alarms delivered through actual communication infrastructure;
- suspicious NPC behavior without a global visible stealth meter;
- evidence objects and logs;
- alternate routes unlocked by world state.

The adapter must not calculate PTU skill success, perception, capability effects or combat interruption rules.

## 22. PTU/Caelo boundary

Before implementation, extract authoritative rules for:
- Stealth;
- Guile;
- Perception and opposed checks relevant to detection;
- Rogue, Ninja, Mastermind and other applicable Trainer Features;
- Invisibility;
- Dead Silent;
- Blender;
- Phasing;
- Telepathy and communication;
- any Caelo modifications to Skills, capabilities or scene resolution.

Do not create custom concealment bonuses, detection DCs, disguise bonuses, alert penalties or surprise rules from this narrative layer.

## 23. Engine dependency map

The permanent capability categories remain the only implementation-readiness vocabulary.

| Capability family | Current evidence | Infiltration relevance |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | useful geometric foundation for sightlines, but does not by itself implement observer perception |
| base movement legality | VERIFIED | supports legal static traversal on battle grids |
| complete movement including push/pull/knockback/interception/forced movement | BLOCKING | required for tactical interception, pursuit and some escape scenarios |
| core calculations | VERIFIED | battle calculation foundation; does not define stealth checks |
| action economy/initiative | VERIFIED | supports ordinary battle turns after confrontation |
| full turn/round lifecycle | PARTIAL | strengthened by authoritative active actor/phase state, still incomplete overall |
| full stateful damage pipeline | PARTIAL | relevant only once confrontation becomes combat |
| status lifecycle | PARTIAL | required if concealment/detection depends on a real PTU status effect |
| terrain/weather/hazards/zones/reactions | BLOCKING | required for darkness/smoke/visibility zones, reaction-based detection or security hazards when governed by PTU |
| move-specific behavior | PARTIAL | required for Moves that actually create concealment, detection or bypass effects |
| abilities | PARTIAL | required for Ability-specific perception/concealment effects |
| items | PARTIAL | required for mechanically active tools or held items |
| Trainer Features/perks | BLOCKING | required for authoritative Rogue/Ninja/Mastermind/etc. effects |
| AI legal-action infrastructure | VERIFIED | enumerates legal battle choices; does not choose patrol/search tactics |
| AI tactical policy | BLOCKING | required for tactical guard search, pursuit, interception and objective-aware responses |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | required for overworld visibility, NPC patrols, disguise presentation, access checks and event playback |

Out-of-combat stealth itself is not proven by Java’s battle LoS. Treat it as an overworld authority problem until a dedicated contract exists.

## 24. Encounter implementation contracts

### Contract A — Archive Night Shift

Narrative premise: players need to verify information inside a restricted archive during a period of reduced staffing. The objective is evidence access, not defeating security personnel.

FULL version:
- actual patrol routes;
- observer-specific sight and suspicion;
- restricted access zones;
- distractions that can redirect security actors;
- dynamic alarm propagation;
- alternate entry/exit paths;
- combat only if the situation legitimately escalates.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED foundation;
- base movement legality: VERIFIED foundation;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING;
- Trainer Features/perks: BLOCKING if a Feature changes infiltration resolution;
- terrain/weather/hazards/zones/reactions: BLOCKING if darkness, reaction zones or similar mechanics are used.

REDUCED version:
The archive is handled in overworld narrative state with explicit access claims and PTU/Caelo-validated checks. If confrontation occurs, launch a normal static AutoPTU battle on a legal map. No grid stealth simulation is attempted.

### Contract B — Depot Cover Story

Narrative premise: a team needs temporary access to a freight depot to identify which shipment is connected to an existing case. The strongest approach may be legitimate visitor access, social cover or discreet observation from public areas.

FULL version:
- cover identity tracking;
- multiple checkpoints;
- shift-based patrols;
- observer memory;
- zone-specific access;
- alarm packets;
- optional tailing after the target leaves.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED foundation if tactical sightlines are used;
- base movement legality: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING;
- Trainer Features/perks: BLOCKING where Feature effects apply;
- complete movement: BLOCKING for tactical pursuit/interception.

REDUCED version:
Resolve cover/access and observation in the overworld with authoritative world and PTU state. A discovered hostile party can trigger an ordinary static battle. Tailing becomes route-state content rather than tactical pursuit.

### Contract C — Willing Insider Extraction

Narrative premise: an insider chooses to leave an organization and asks the players for help reaching a safe meeting point. The target’s agency is explicit; this is not a kidnapping objective.

FULL version:
- moving protected actor;
- hostile patrol search;
- escort and interception;
- alternate exits;
- surrender/withdrawal possibilities;
- objective-aware AI;
- communication delays between search teams.

Dependencies:
- complete movement including interception/forced movement: BLOCKING;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING;
- terrain/weather/hazards/zones/reactions: BLOCKING if reaction-based chokepoints are used;
- full turn/round lifecycle: PARTIAL if complex timed effects are introduced.

REDUCED version:
Keep the insider outside the battle grid. Players clear or survive one static chokepoint encounter, then the overworld operation resolves extraction according to world state. The battle engine never simulates escort movement.

### Contract D — Authorized Security Exercise

Narrative premise: an institution hires players to test whether an important facility can detect an unauthorized approach. This allows stealth-oriented content without requiring criminal framing.

FULL version:
- patrol and observer AI;
- access zones;
- detection logs;
- nonlethal exercise stop conditions;
- performance debrief based on actual detection events.

Dependencies:
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING;
- Trainer Features/perks: BLOCKING if specialist Features are mechanically used;
- targeting/LoS and base movement: VERIFIED foundations only.

REDUCED version:
Run the approach as world-state checks and observations. If the exercise includes a battle drill, resolve it separately under ordinary legal combat rules. Do not invent a stealth score.

## 25. Promotion gate

Before any covert concept moves toward canon or implementation:
1. Confirm the institution, access policy and technology exist in Ouros canon.
2. Validate any Skill, Capability, Move, Ability, Item or Trainer Feature against PTU/Caelo.
3. Confirm player-authored cover identity and privacy state when a PC is involved.
4. Identify every required permanent engine capability family.
5. Use a REDUCED version where blocked families would otherwise be duplicated in Minecraft scripts.
6. Preserve all discovery, suspicion and alarm information as actor-local knowledge until communicated.
7. Record traces in the existing evidence system.
8. Keep combat resolution authoritative in AutoPTU.