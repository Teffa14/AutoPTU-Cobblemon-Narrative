# Wreck Sites, Salvage, Recovery & Preservation Extension

Status: proposed systems design. Not established Ouros canon.

Pass: 77

## Purpose

Ouros already knows how to track significant objects, travel routes, expeditions, archives, protected areas, facility condition, found property, emergencies and institutional custody. This extension adds the site-level continuity needed for wrecked vessels, abandoned transport, flooded facilities and comparable structural remains.

The objective is to preserve the identity and history of a site while allowing it to change through survey, ecological occupation, selective recovery, stabilization, partial dismantling, restoration, access changes or later reuse.

This extension does not define universal salvage law, ownership law, archaeology law, diving mechanics or underwater combat rules.

## 1. Authority boundaries

### Material Culture

`material-culture-economy-crafting-layer.md` owns persistent item identity and provenance.

When an object is recovered from a wreck, Pass 77 creates the contextual recovery event and links it to the existing `item_instance` or `material_batch`. It does not create a second identity for the same object.

### Travel / Transport

`travel-transport-expedition-layer.md` owns routes and active transport services.

A wreck may originate from a former service, but Pass 77 does not infer the operator's current status, replacement route or liability.

### Archives / Collections

`archives-museums-collections-preservation-layer.md` owns accession, conservation and collections.

A recovered historical object can be handed off to that layer after recovery. Pass 77 preserves where it came from.

### Conservation

`conservation-protected-areas-stewardship-layer.md` owns protected-area status and ecological stewardship.

A wreck becoming habitat does not automatically make it protected. Pass 77 records ecological occupation and produces a handoff candidate.

### Found Property / Case

Ordinary personal property follows Pass 66. Evidence or formal disputes follow Case/Authority. Pass 77 must not resolve ownership merely because an object came from a wreck.

### Facility Maintenance

If the structure is being returned to active use, Maintenance owns technical repair and reopening. Pass 77 owns historical/site continuity and intervention history.

### Crisis

Active rescue, evacuation or immediate danger belongs to Crisis. Pass 77 begins or resumes once the site can be treated as a persistent location rather than an active emergency.

## 2. Persistent wreck-site record

```yaml
wreck_site:
  wreck_site_id: null
  location_id: null
  former_asset_ref: null
  former_service_ref: null
  site_type: null
  known_since: null
  origin_event_ref: null
  current_site_state: UNKNOWN
  structural_condition_ref: null
  access_profile_ref: null
  ecological_occupation_refs: []
  survey_ids: []
  intervention_ids: []
  recovered_object_refs: []
  in_situ_object_refs: []
  restriction_refs: []
  public_memory_refs: []
  archive_refs: []
  current_steward_ref: null
  provenance_refs: []
```

Candidate `site_type` values:

- WRECKED_VESSEL
- SUNKEN_VESSEL
- ABANDONED_PLATFORM
- FLOODED_FACILITY
- COLLAPSED_TRANSPORT_STRUCTURE
- DERELICT_CARGO_SITE
- PARTIALLY_SUBMERGED_INFRASTRUCTURE
- OTHER_REVIEWED_REMAINS

Candidate `current_site_state` values:

- UNKNOWN
- UNSURVEYED
- SURVEYED_LIMITED
- SURVEYED
- ACCESS_RESTRICTED
- STABILIZATION_PENDING
- STABILIZED_IN_PLACE
- SELECTIVE_RECOVERY_ACTIVE
- RECOVERY_PAUSED
- PARTIALLY_DISMANTLED
- ECOLOGICAL_STEWARDSHIP
- RESTORATION_CANDIDATE
- RESTORATION_ACTIVE
- PUBLIC_ACCESS_LIMITED
- PUBLIC_ACCESS_OPEN
- CLOSED

These are narrative/site states only. They do not define legal authority.

## 3. Survey record

A survey separates what is observed from what is inferred.

```yaml
wreck_site_survey:
  survey_id: null
  wreck_site_id: null
  conducted_at: null
  actor_refs: []
  access_method_refs: []
  surveyed_zone_refs: []
  condition_observations: []
  object_observations: []
  ecological_observations: []
  hazard_observations: []
  mapped_connections: []
  inaccessible_zone_refs: []
  confidence_notes: []
  source_refs: []
```

A survey may establish:

- a corridor is blocked;
- a compartment is flooded;
- an object is visible;
- a wall has shifted;
- corrosion has increased since the prior visit;
- a known Pokémon group is using one section;
- a hatch exists but has not been opened.

It may not establish without evidence:

- ownership;
- historical cause;
- structural safety for all future visits;
- mechanical hazard damage;
- species-wide ecological conclusions;
- intentional sabotage;
- criminal responsibility.

## 4. Site zones and layered access

```yaml
wreck_site_zone:
  zone_id: null
  wreck_site_id: null
  parent_zone_id: null
  name_or_descriptor: null
  access_state: UNKNOWN
  physical_connection_refs: []
  observed_blocker_refs: []
  environment_refs: []
  structural_condition_ref: null
  ecological_occupation_refs: []
  known_object_refs: []
  survey_required: true
```

Suggested access states:

- UNKNOWN
- VISIBLE_NOT_REACHED
- REACHABLE
- REACHABLE_WITH_REVIEWED_CAPABILITY
- TEMPORARILY_BLOCKED
- STRUCTURALLY_RESTRICTED
- ENVIRONMENTALLY_RESTRICTED
- INSTITUTIONALLY_RESTRICTED
- SEALED

Minecraft can make every zone physically present before every zone is narratively/mechanically available.

A visible doorway or water passage does not waive the requirements owned by Travel, Credentials, Conservation, Maintenance or PTU/Caelo movement rules.

## 5. Structural condition history

```yaml
site_condition_revision:
  condition_revision_id: null
  wreck_site_id: null
  zone_id: null
  observed_at: null
  observed_state: null
  evidence_refs: []
  prior_revision_ref: null
  change_claim: null
  assessor_refs: []
```

Possible descriptive states:

- INTACT_RELATIVE
- WEATHERED
- CORRODED
- PARTIALLY_COLLAPSED
- FLOODED
- SHIFTED
- EXPOSED
- BURIED_PARTIAL
- STABILIZED
- UNKNOWN

These are descriptive. They do not create combat penalties.

## 6. Ecological occupation

A wreck can become habitat without losing historical identity.

```yaml
wreck_ecology_observation:
  observation_id: null
  wreck_site_id: null
  zone_id: null
  observed_at: null
  observer_ref: null
  pokemon_refs: []
  collective_refs: []
  habitat_use_claim: null
  behavior_observations: []
  environmental_refs: []
  confidence: null
  source_refs: []
```

The system must keep these statements separate:

- Pokémon were observed here;
- the site is repeatedly used;
- the site provides habitat;
- the site is essential habitat;
- the species owns or controls the site;
- the site is protected.

Each stronger claim needs its own evidence or governing system.

## 7. Intervention proposal

A player or institution may propose action without automatically gaining permission to perform it.

```yaml
wreck_intervention_proposal:
  proposal_id: null
  wreck_site_id: null
  proposed_by_ref: null
  intervention_type: null
  target_zone_refs: []
  target_object_refs: []
  stated_goal: null
  evidence_refs: []
  dependency_refs: []
  authority_review_ref: null
  conservation_review_ref: null
  technical_review_ref: null
  status: PROPOSED
```

Candidate intervention types:

- DOCUMENT_ONLY
- RESTRICT_ACCESS
- STABILIZE_IN_PLACE
- SELECTIVE_OBJECT_RECOVERY
- CARGO_RECOVERY
- HAZARD_REMOVAL
- ECOLOGICAL_PROTECTION
- PARTIAL_DISMANTLING
- RESTORATION_ASSESSMENT
- RESTORATION
- PUBLIC_ACCESS_PREPARATION

No option is automatically superior.

## 8. Recovery event

```yaml
wreck_recovery_event:
  recovery_event_id: null
  wreck_site_id: null
  zone_id: null
  object_or_batch_refs: []
  recovered_at: null
  recovered_by_refs: []
  authorized_by_ref: null
  intervention_ref: null
  original_context_record: null
  condition_at_recovery: null
  custody_handoff_ref: null
  destination_system_ref: null
  notes: null
```

Recovery must append provenance.

The object keeps:

- wreck/site reference;
- exact zone/context;
- survey/observation links;
- recovery timestamp;
- who physically recovered it;
- who received custody afterward;
- whether conservation/inspection is still pending.

`recovered_by` does not mean `current_owner`.

## 9. In-place preservation

```yaml
in_situ_preservation_record:
  preservation_id: null
  wreck_site_id: null
  zone_id: null
  target_refs: []
  reason_claim_refs: []
  stabilization_refs: []
  monitoring_plan_ref: null
  access_restriction_ref: null
  review_due_ref: null
  current_state: ACTIVE
```

Leaving an object in place can be a successful outcome.

This matters because removing an item from its context can destroy information, create conservation needs or disrupt habitat.

## 10. Repeated condition surveys

Wrecks should support callbacks.

A later survey can detect:

- new collapse;
- sediment changes;
- new ecological occupation;
- missing/relocated objects;
- new access created by weather or repair;
- deterioration after public access;
- stabilization success;
- old intervention marks.

The new observation appends history. It never silently overwrites the previous state.

## 11. Object categories at a wreck

A site may contain several classes of object with different handoffs:

- former cargo;
- personal property;
- equipment belonging to the former operator;
- structural components;
- later deposits unrelated to the original wreck;
- biological/ecological material;
- historical records;
- evidence tied to an authored case;
- ordinary debris.

The system must not classify all of them as salvageable inventory.

## 12. Site identity after intervention

The same `wreck_site_id` persists through:

- selective recovery;
- stabilization;
- partial dismantling;
- habitat protection;
- public interpretation;
- restoration assessment;
- restoration.

If a wreck is eventually rebuilt into an active structure, the restored asset may receive a new operational record while retaining the historical site link.

## 13. Historical claims and provenance

A plaque, archive, former worker, logbook or recovered object may make claims about the wreck.

Those claims remain separate from canonical truth.

Examples:

- claimed date of loss;
- claimed cargo manifest;
- claimed cause;
- claimed operator;
- claimed final route;
- claimed number of occupants;
- claimed ownership of recovered material.

Conflicting claims create investigation hooks without forcing a conspiracy.

## 14. Public access and interpretation

If the site becomes visitable, Public Memory/Travel/Accessibility own the visitor-facing state.

Pass 77 can provide:

- known safe zones;
- preserved zones;
- recovered-object context;
- condition history;
- ecological occupation history;
- intervention history.

It does not invent tourism policy, ticketing or public-liability rules.

## 15. Minecraft/Cobblemon projection

Follow `design/cobblemon-runtime-authority-boundary.md`.

### SAFE_REUSE

Use Minecraft/Cobblemon for:

- water volumes and visual depth;
- structure geometry;
- weathering/corrosion visual palettes;
- doors, hatches, ladders and routes;
- ambient particles;
- aquatic Pokémon embodiment;
- swimming/flying animations;
- cries and environmental audio;
- entity tracking;
- persistent props;
- signs/markers;
- UI/networking;
- chunk persistence and visual revisitation.

### ADAPTER_REQUIRED

Use Ouros adapters for:

- mapping persistent `wreck_site_id` and zone state into blocks/props;
- mapping known persistent Pokémon into Cobblemon entities;
- hiding or revealing interactables from authoritative access state;
- projecting a completed recovery event by removing/moving a prop;
- reconciling the site after server restart;
- presenting battle participants chosen by Ouros/AutoPTU;
- playing AutoPTU battle events without Cobblemon BattleState ownership.

### FORBIDDEN AUTHORITY

Cobblemon/Minecraft may not decide:

- which Pokémon at the wreck enter battle;
- underwater tactical movement legality;
- pressure/current/flooding combat effects;
- participant HP/status/initiative;
- battle outcomes;
- who owns recovered cargo;
- whether pickup equals recovery authorization;
- whether a visible object is mechanically usable;
- whether a destroyed block means a historical object was canonically destroyed.

## 16. Encounter contract — Flooded Compartment Withdrawal

Status: PROPOSED.

Narrative premise:

A survey team reaches a newly accessible flooded compartment. Defensive wild Pokémon occupy the space and the team needs to withdraw without losing the survey route.

### Intended full version

The full encounter could use:

- actual underwater/water movement;
- narrow LoS and footprint pressure;
- changing safe routes;
- WITHDRAW/CLEAR_ROUTE objective logic;
- interception or forced movement if rules support it;
- environmental water/visibility effects only when PTU/Caelo mapping exists;
- territorial AI that can retreat instead of optimizing only KO;
- exact adapter playback inside the wreck geometry.

Permanent capability dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement if used;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle where relevant;
- terrain/weather/hazards/zones/reactions if water/environment becomes tactical;
- move-specific behavior;
- abilities;
- items where relevant;
- Trainer Features/perks where relevant;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

### Reduced version

The survey team exits the flooded compartment in world state before combat begins. The confrontation occurs in a reviewed static chamber or dry staging area using only legal ordinary battle mechanics. The compartment remains inaccessible until after the result. No current, drowning, pressure, visibility or underwater penalty is scripted in Minecraft.

The battle can make access safe. It cannot prove ownership or complete recovery.

## 17. Encounter contract — Selective Recovery Perimeter

Status: PROPOSED.

Narrative premise:

A planned recovery team is removing one identified object from a structurally sensitive wreck zone while wild Pokémon repeatedly use the surrounding remains.

### Intended full version

Potential mechanics:

- protected recovery zone;
- technicians withdrawing if threatened;
- PROTECT/CLEAR_ROUTE objective;
- fragile/blocked areas;
- interception/forced movement;
- territorial/withdrawal AI;
- terrain/hazard behavior only when verified;
- adapter synchronization so recovery state changes only after the authoritative noncombat handoff.

### Reduced version

Remove technicians and the target object from the tactical grid. Pause recovery in world state. Run a static battle in an adjacent reviewed area. After the authoritative result, perform the actual recovery as a separate world interaction and append provenance/custody.

Winning does not place the object in player inventory automatically.

## 18. Noncombat encounter — Context Before Collection

A newly found object appears valuable, but the team can choose to:

- photograph/document it in place;
- map nearby objects;
- inspect maker marks without moving it;
- compare archive records;
- request a specialist review;
- recover it selectively;
- leave it and establish monitoring.

The important choice is information versus intervention, not combat success.

This can run before any additional tactical engine work.

## 19. Long-form arc pattern — A Wreck Changes Meaning

Visit 1: the site is known only as an obstruction/landmark.

Visit 2: a survey establishes layered access and ecological occupation.

Visit 3: a historical claim creates interest in one compartment or object.

Visit 4: an intervention debate produces competing preservation, recovery and access proposals.

Visit 5: one bounded intervention changes the site physically.

Visit 6: later ecology/public access reveals a consequence nobody could see from the first visit.

The same place supports multiple arcs without respawning loot or replacing the wreck with a new dungeon.

## 20. Anti-false-completion rules

- Seeing cargo does not establish ownership.
- Minecraft pickup does not authorize recovery.
- Recovery does not imply salvage rights.
- A wreck being abandoned does not mean every object is ownerless.
- A wild Pokémon occupying the site does not automatically make the site protected.
- A protection proposal does not establish legal authority.
- A structural collapse visual does not create tactical hazard damage.
- Water visible in the arena does not establish PTU underwater penalties.
- A Pokémon species associated with water does not automatically have the required individual movement/carrying capability.
- Winning a battle does not restore, dismantle or preserve a site.
- Removing a prop from Minecraft does not erase its provenance.
- Cobblemon Battle/BattleState code never decides participants, state or outcome.

## 21. Canon questions deliberately left open

- Which wrecks or abandoned marine/transport structures actually exist in Ouros?
- Which institutions survey them?
- Who can restrict access?
- What ownership/custody rules apply to former cargo and personal effects?
- Does Ouros have formal salvage customs or institutions?
- Which sites have historical/archaeological significance?
- Which have become habitat?
- How does public access work?
- What diving/recovery technologies exist regionally?
- Which professions/credentials are required?
- Can a former wreck be restored to active service, and under what institutions?

None of these answers are established by Pass 77.