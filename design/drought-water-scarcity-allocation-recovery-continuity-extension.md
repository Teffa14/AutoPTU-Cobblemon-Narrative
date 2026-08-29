# Drought, Water Scarcity, Allocation & Recovery Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Date: 2026-08-29

## Purpose

This layer preserves long-running scarcity state without turning Ouros into a hydrology simulator. It connects Weather, Water Management, Drinking Water, Agriculture, Conservation, Fisheries, Civic Governance, Crisis, Infrastructure Outage and Public Notices while leaving each owner system authoritative for its own decisions.

The layer owns scarcity-episode identity, observation provenance, assessment revision history, cross-system handoffs, temporary arrangements and staged recovery history.

## Authority boundaries

Weather owns observed and forecast weather. Water Management owns managed assets, operating regimes and executed water-control operations. Drinking Water owns treatment and potable distribution. Agriculture owns crop and farm outcomes. Conservation and Fisheries own ecological decisions. Civic Governance owns collective allocation/restriction decisions where canon grants that authority. Crisis owns emergency coordination. Public Notices owns published messages. Care owns health consequences.

This layer does not calculate rainfall deficits, reservoir yield, groundwater recharge, crop loss, dehydration, ecological mortality or legal water rights.

## Core episode

```yaml
water_scarcity_episode:
  scarcity_episode_id: null
  geographic_scope_ids: []
  first_signal_ids: []
  observation_bundle_ids: []
  assessment_ids: []
  cause_claim_ids: []
  affected_source_refs: []
  affected_service_refs: []
  allocation_handoff_ids: []
  temporary_supply_ids: []
  downstream_handoff_ids: []
  recovery_checkpoint_ids: []
  low_water_feature_ids: []
  pokemon_observation_ids: []
  unresolved_questions: []
  provenance_refs: []
  canon_status: proposed
```

## Observation model

```yaml
scarcity_observation:
  observation_id: null
  observed_at: null
  location_or_system_ref: null
  observation_kind: null
  qualitative_state: null
  measured_value_ref: null
  source_ref: null
  coverage_scope: null
  confidence: UNKNOWN
```

Candidate observation kinds include precipitation, stream presence, reservoir level, well level, spring flow, intake availability, demand pressure, ecological observation, agricultural observation and household/service report. These labels do not define real-world measurement standards.

A missing interval is recorded as `UNKNOWN_FOR_INTERVAL`.

## Assessment revision

```yaml
scarcity_assessment:
  assessment_id: null
  episode_id: null
  valid_from: null
  geographic_scope_ids: []
  supported_claims: []
  uncertain_claims: []
  rejected_claim_refs: []
  evidence_refs: []
  supersedes_assessment_id: null
  status: ACTIVE
```

Hard separations:

`DRY_WEATHER_OBSERVED != WATER_SCARCITY_CONFIRMED`

`WATER_SCARCITY_CONFIRMED != METEOROLOGICAL_DROUGHT_SUPPORTED`

`LOW_RESERVOIR != DRINKING_WATER_UNAVAILABLE`

`RAIN_RETURNED != SCARCITY_EPISODE_CLOSED`

`SOURCE_RECOVERED != EVERY_DOWNSTREAM_SYSTEM_RECOVERED`

`LOW_WATER_FEATURE_EXPOSED != FEATURE_IDENTITY_CONFIRMED`

## Cause claims

```yaml
scarcity_cause_claim:
  claim_id: null
  episode_id: null
  claimed_factor: null
  evidence_refs: []
  competing_claim_ids: []
  confidence: UNKNOWN
  owner_system_ref: null
```

Possible factors remain descriptive: prolonged precipitation deficit, conveyance interruption, source depletion, high demand, contamination hold, maintenance outage, land-use change or mixed causes. The system never invents causation because a narrative needs a culprit.

## Allocation and restriction handoffs

This layer may preserve that another owner system made a decision.

```yaml
scarcity_allocation_handoff:
  handoff_id: null
  episode_id: null
  receiving_owner_system: null
  subject_scope_ids: []
  decision_ref: null
  effective_from: null
  effective_until: null
  evidence_refs: []
```

The scarcity layer does not create water law. Different institutions can receive the same evidence and make different canon-valid decisions.

## Temporary supply arrangements

```yaml
temporary_water_arrangement:
  arrangement_id: null
  episode_id: null
  service_area_ids: []
  arrangement_type: authored
  operator_refs: []
  source_refs: []
  start_at: null
  end_at: null
  current_state: PLANNED
  verification_refs: []
```

Examples may include temporary pickup points, alternate source routing or delivery arrangements only where canon establishes them. Availability does not imply quality, accessibility or sufficient capacity.

## Recovery checkpoints

Recovery is subsystem-specific.

```yaml
scarcity_recovery_checkpoint:
  checkpoint_id: null
  episode_id: null
  owner_system_ref: null
  subject_ref: null
  checkpoint_type: null
  observed_at: null
  state: PENDING
  evidence_refs: []
```

A sequence can include rainfall improvement, stream recovery, reservoir recovery, groundwater recovery, drinking-water service normalization, agricultural recovery, ecological review and closure of temporary arrangements. These do not need to occur together.

## Low-water exploration continuity

```yaml
low_water_exposed_feature:
  feature_id: null
  episode_id: null
  first_observed_at: null
  location_ref: null
  feature_claims: []
  evidence_refs: []
  access_owner_ref: null
  preservation_or_case_refs: []
  current_visibility_state: UNKNOWN
```

Lower water can expose structures, markers, roads, foundations or objects. Exposure establishes visibility only. Archives, archaeology, found-property, case/custody or civic systems decide identity, ownership and disposition.

## Pokémon observations

```yaml
scarcity_pokemon_observation:
  observation_id: null
  actor_or_group_ref: null
  observed_at: null
  location_ref: null
  behavior_claim: null
  evidence_refs: []
  interpretation_refs: []
```

Observed relocation, congregation or return can support ecology and local knowledge. It never grants species-wide drought sensing, rainmaking, water generation or immunity.

## Encounter contracts

### Reservoir Margin Withdrawal

Full intent: noncombatants withdraw from a newly restricted shoreline while conflict unfolds. Dependencies: complete movement including interception/forced movement; full turn/round lifecycle if withdrawal windows matter; terrain/weather/hazards/zones/reactions if mud, changing shoreline or exclusion zones are tactical; AI tactical policy for PROTECT/WITHDRAW; adapter/playback for semantic movement.

Reduced form: complete withdrawal and access restriction before BattleSpec. Use static inspected terrain. Victory secures the immediate perimeter only.

### Exposed Causeway Perimeter

Full intent: a newly visible historic causeway remains partly unstable or changes tactical access. Dependencies: terrain/weather/hazards/zones/reactions; complete movement if forced displacement exists; damage/status only when an exact governing rule defines an effect; lifecycle for phased exposure; AI tactical policy and adapter/playback.

Reduced form: declare the stable surveyed portion before combat and exclude uncertain cells. Resolve a conventional static encounter. Battle success does not authenticate the structure or reopen it for public use.

### Temporary Water Point Diversion

Full intent: a conflict occurs while civilians are redirected between temporary pickup points. Dependencies: complete movement, generalized reactions, objective-aware AI, lifecycle and playback. Any queue or service-capacity logic remains world state, not battle logic.

Reduced form: finish rerouting civilians before BattleSpec. Keep service equipment and water custody outside tactical authority. Victory clears the immediate route only.

## Permanent capability classification

Current baseline carried forward from Pass 120:

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: complete movement including push/pull/knockback/interception/forced movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback support.

No family is promoted by this design.

## PTU/Caelo unknowns

Remain UNKNOWN unless exact governing evidence appears: dehydration, thirst, fatigue from scarcity, dry-ground penalties, dust effects, drought-driven weather persistence, groundwater movement, water-production volume from Moves, Rain Dance as civic drought resolution, Drought Ability as regional climate authority, Sunny Day as hydrology, species-based water finding, species-based rain prediction, crop-yield effects, ecological mortality, water-carrying combat rules and any drought-specific Trainer Feature interaction.

## Minecraft/Cobblemon boundary

Minecraft can present dry riverbeds, lower reservoirs, cracked terrain, exposed structures, temporary water points, queues, signs, NPC routines, Pokémon, particles and sound. Visual rain does not close an episode. Water blocks do not prove supply or quality. Buckets do not establish custody or capacity. Native hunger/status does not implement PTU dehydration. Cobblemon BattleState remains outside combatant selection, legality, HP/status, positions and outcomes.

## Canon questions left open

Which Ouros regions experience recurring dry periods? Which water systems exist? Who monitors them? Which institutions may allocate or restrict use? Which communities maintain historical water knowledge? Which habitats and industries are sensitive? Which temporary arrangements became permanent? Which individual Pokémon have documented roles?

All remain unresolved until canon establishes them.