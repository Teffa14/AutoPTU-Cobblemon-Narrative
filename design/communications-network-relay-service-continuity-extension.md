# Ouros Communications Network / Relay Service Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established canon.
Date: 2026-08-28

## Purpose and ownership boundary

Ouros already has three adjacent authorities:

- Media/Communications owns information packets, channels, publication, delivery and audience receipt;
- Technology/Energy owns physical communications assets, faults, maintenance and technical controls;
- Infrastructure Outage owns multi-service outage propagation, backups and restoration handoffs.

This extension owns the missing operational bridge for communications networks themselves: persistent relay topology, service sectors, service paths, endpoint readiness, temporary relays, reroutes, verification tests and communications-specific restoration history.

It does not duplicate message delivery. It does not duplicate physical repair. It does not create a universal telecommunications technology for Ouros.

## 1. Communications network identity

```yaml
communications_network:
  communications_network_id: null
  operator_id: null
  network_role: null
  node_ids: []
  authored_link_ids: []
  service_ids: []
  sector_ids: []
  fallback_plan_ids: []
  current_operational_summary: unknown
  canon_reference_ids: []
```

Possible high-level roles include regional broadcast distribution, institutional dispatch, local relay, long-distance link, research communication or emergency fallback. These labels describe story function only.

## 2. Relay/network node

Physical condition remains owned by Technology. This record stores the node's role inside a communications topology.

```yaml
communications_node:
  communications_node_id: null
  technical_asset_id: null
  location_id: null
  network_id: null
  role_tags: []
  upstream_node_ids: []
  downstream_node_ids: []
  supported_service_ids: []
  current_network_state: unknown
  dependency_refs: []
  last_network_verification_id: null
```

Suggested network states:

- UNKNOWN
- AVAILABLE
- DEGRADED
- ISOLATED
- BYPASSED
- OFFLINE
- UNDER_REPAIR
- TESTING
- TEMPORARY_SERVICE
- DECOMMISSIONED

`technical_asset repaired` does not automatically mean `communications_node AVAILABLE`.

## 3. Authored network link

```yaml
communications_link:
  link_id: null
  network_id: null
  endpoint_a_id: null
  endpoint_b_id: null
  link_role: null
  supported_service_ids: []
  dependency_ids: []
  current_state: unknown
  temporary: false
  valid_from: null
  valid_until: null
  verification_ids: []
```

The project must author links deliberately. Physical proximity, Minecraft line-of-sight, redstone adjacency or loaded chunks never create network connectivity automatically.

Suggested states:

- UNKNOWN
- EXPECTED_AVAILABLE
- VERIFIED_AVAILABLE
- DEGRADED
- INTERMITTENT
- UNAVAILABLE
- REROUTED
- TESTING

No numeric bandwidth, signal strength, frequency, latency or packet-loss model is implied.

## 4. Communications service

```yaml
communications_service:
  service_id: null
  network_id: null
  media_channel_id: null
  operator_id: null
  required_node_ids: []
  required_link_ids: []
  eligible_sector_ids: []
  endpoint_requirement_refs: []
  priority_or_fallback_policy_ref: null
  current_service_state: unknown
  last_verified_at: null
```

Suggested states:

- UNKNOWN
- AVAILABLE
- DEGRADED
- INTERMITTENT
- LIMITED
- FALLBACK_ONLY
- SUSPENDED
- RESTORING
- TESTING

Media still owns whether a specific message was sent, delivered or acknowledged.

## 5. Service sector

A sector is the smallest authored geographic/service scope whose availability matters to Narrative.

```yaml
communications_service_sector:
  sector_id: null
  service_id: null
  geographic_scope_ids: []
  expected_path_ids: []
  fallback_path_ids: []
  current_availability: unknown
  last_observation_ids: []
  last_verified_at: null
  active_exception_ids: []
```

Suggested availability states:

- UNKNOWN
- EXPECTED_AVAILABLE
- VERIFIED_AVAILABLE
- DEGRADED
- INTERMITTENT
- LOCAL_ONLY
- UNAVAILABLE
- RESTORING

This is intentionally coarse. The extension does not simulate radio propagation per block.

## 6. Endpoint readiness and entitlement

A healthy service can remain unusable to a particular endpoint.

```yaml
communications_endpoint_state:
  endpoint_id: null
  actor_or_institution_id: null
  service_id: null
  physical_device_asset_id: null
  current_readiness: unknown
  entitlement_or_access_ref: null
  configuration_state: unknown
  last_successful_test_id: null
  failure_claim_ids: []
```

Candidate readiness states:

- UNKNOWN
- READY
- EQUIPMENT_UNAVAILABLE
- CONFIGURATION_PENDING
- ACCESS_PENDING
- DEGRADED
- FAILED_TEST

A service becoming available never grants credentials, subscriptions, access rights, receiver upgrades or private-channel visibility.

## 7. Path selection and reroute

```yaml
communications_service_path:
  path_id: null
  service_id: null
  ordered_node_ids: []
  ordered_link_ids: []
  path_role: primary
  activation_state: standby
  valid_sector_ids: []
  activation_event_ids: []
  verification_ids: []
```

Candidate path roles:

- PRIMARY
- ALTERNATE
- CONTINGENCY
- EMERGENCY
- TEMPORARY

Candidate activation states:

- STANDBY
- REQUESTED
- ACTIVATING
- ACTIVE
- ACTIVE_LIMITED
- FAILED
- RETURNING_TO_STANDBY

Fallback order is authored. The extension does not automatically choose the morally or politically preferred service when capacity is constrained.

## 8. Temporary relay episode

```yaml
temporary_relay_episode:
  temporary_relay_id: null
  network_id: null
  technical_asset_refs: []
  supported_service_ids: []
  supported_sector_ids: []
  established_reason_ids: []
  established_at: null
  verified_at: null
  current_state: planned
  retirement_trigger_ids: []
  historical_effect_ids: []
```

Possible states:

- PLANNED
- DEPLOYING
- TESTING
- ACTIVE
- ACTIVE_LIMITED
- FAILED
- RETIRING
- RETIRED

A temporary relay may become socially important even if it is later removed. Public Memory, Travel or Commercial layers can preserve downstream consequences.

## 9. Communications verification test

```yaml
communications_verification_test:
  verification_id: null
  test_scope_type: null
  tested_subject_ids: []
  service_id: null
  sector_id: null
  endpoint_id: null
  performed_by_ids: []
  performed_at: null
  expected_result: null
  observed_result: null
  evidence_refs: []
  conclusion_state: unresolved
```

Suggested conclusion states:

- PASS_FOR_SCOPE
- FAIL_FOR_SCOPE
- PARTIAL
- INCONCLUSIVE
- SUPERSEDED

A successful test at one endpoint does not verify the whole region. A failed endpoint test does not prove the relay itself is down.

## 10. Restoration sequence

A communications-specific restoration can use:

```text
incident observed
-> affected service/sector bounded
-> physical dependency isolated or repaired by owner system
-> node/link returned to TESTING
-> path verification
-> selected sectors VERIFIED_AVAILABLE
-> endpoint tests where required
-> Media delivery resumes according to channel state
-> temporary path retired only after its exit conditions pass
```

Important separations:

- repair complete != network path verified;
- path verified != every sector verified;
- sector verified != every endpoint ready;
- service available != every queued message delivered;
- public notice updated != service state changed.

## 11. Coverage/version discrepancy

```yaml
communications_coverage_claim:
  coverage_claim_id: null
  service_id: null
  sector_id: null
  claimed_state: null
  effective_at: null
  published_or_recorded_by_id: null
  provenance_refs: []
  superseded_by_id: null
```

A map, notice or operator board can become stale. Field observations can contradict it. Reconciliation preserves both records and their timestamps.

This enables mysteries where nobody lied.

## 12. Interference and unexplained degradation

```yaml
communications_degradation_observation:
  observation_id: null
  service_id: null
  sector_id: null
  endpoint_id: null
  observed_at: null
  symptom_tags: []
  observer_id: null
  suspected_cause_claim_ids: []
  confirmed_cause_ids: []
  evidence_refs: []
```

The extension can store symptoms such as intermittent reception, delayed contact or service unavailable. It cannot invent jamming rules, radio physics, electromagnetic hazards or Pokémon causation.

## 13. Ecology and relay sites

Relay sites may change light, noise, access patterns or human traffic. Wildlife observations belong to Conservation/Ecology. Co-location does not prove interference.

A recurring Pokémon near a tower may become a memorable local actor without becoming a technician, battery, signal booster or combatant by species inference.

## 14. Noncombat scenario patterns

### The Relay Passed, the Village Did Not

A repaired node passes its local test. The downstream sector remains unavailable. Investigation can reveal a separate link, endpoint or authorization problem.

### The Temporary Tower Became the Meeting Place

A temporary relay creates new foot traffic around a safe staging location. After permanent service returns, residents still use the spot for notices, trade or gatherings.

### Three Tests, Two Services

Three apparently contradictory reports refer to different services, sectors or endpoints. Provenance and scope resolve the discrepancy.

### Emergency Dispatch Returned First

A constrained fallback restores one authored priority service while ordinary public channels remain limited. The priority decision must come from an established authority/procedure, never from this extension.

## 15. Encounter contract — Relay Access Withdrawal

Narrative premise:

A relay site must remain isolated while technicians withdraw through a constrained access route after an unrelated Pokémon confrontation begins nearby.

Full intended version may include:

- multiple withdrawal paths;
- route protection;
- Intercept and other forced movement;
- generalized reactions;
- authored tower/work-zone hazards only if governing PTU rules exist;
- objective-aware AI;
- semantic adapter playback.

Permanent capability dependencies:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING if active technical/weather zones matter;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING.

Reduced version:

The relay is isolated before battle. Technicians, tools and all nonparticipants leave the tactical grid. AutoPTU receives explicit combatants in a reviewed static access area. Victory secures immediate access only. Technology/Maintenance performs repair and Communications runs verification afterward.

## 16. Encounter contract — Temporary Relay Perimeter

Narrative premise:

A temporary relay is supporting a limited communications sector while a territorial encounter threatens the staging perimeter.

Full intended version may require route defense, reactions, forced movement, objective-aware AI and playback. If wind, energized equipment, moving machinery or other zones matter mechanically, `terrain/weather/hazards/zones/reactions` is directly required.

Reduced version:

The temporary equipment and operators remain outside the BattleSpec. The battle uses a static adjacent perimeter. Winning does not prove the relay survived, restore a sector or deliver messages. A post-battle world-state verification determines whether service remains active.

## 17. Encounter contract — Repeater Ridge Diversion

Narrative premise:

A service crew must approach a remote node while a Pokémon encounter blocks the ordinary route.

Full intended version can include escort/withdrawal logic, several approach routes, Intercept/forced movement, weather/terrain effects, tactical policy and playback.

Reduced version:

Travel selects a safe static encounter area before the technical site. Crew and equipment wait outside battle. Once the route is secured, technical inspection happens as noncombat world state. No environmental radio or electricity effect is invented.

## 18. Minecraft/Cobblemon boundary

Safe presentation reuse includes:

- towers, antenna structures, relay huts and cables as world geometry;
- lights, screens and status indicators;
- signs and temporary barriers;
- technician NPCs;
- sounds and particles;
- Pokémon models, forms, poses, animations and cries;
- UI for sector/service status;
- networking, tracking and persistence hooks.

The authoritative flow remains:

`Ouros communications/world state -> explicit encounter composition -> AutoPTU battle state/result -> adapter -> Minecraft/Cobblemon presentation`.

Minecraft/Cobblemon never decides that:

- two towers are linked because they can see one another;
- a powered block means a communications service is verified;
- redstone continuity means a sector has coverage;
- an entity holding a device is authorized for a service;
- a visual antenna rotation proves transmission;
- a nearby Pokémon provides or disrupts signal;
- native lightning/electricity applies PTU damage or status;
- every entity at a relay becomes a combatant;
- Cobblemon BattleState/controller logic owns combatants, legality, HP/status, positions or battle outcome.

## 19. Canon questions left open

Ouros canon still must decide:

- which communication technologies exist by region;
- which settlements have towers, repeaters, wired links, portable relays or other infrastructure;
- who operates them;
- what services receive priority under constrained fallback, if any;
- what endpoint access/entitlement systems exist;
- privacy and access norms;
- whether long-distance communication crosses regional/institutional boundaries freely;
- how old relay sites are reused or remembered;
- whether individual Pokémon perform communications work and what exact evidence authorizes each task.

## 20. Mechanical questions left open

No governing answer is assumed for:

- signal/range calculations;
- interference or jamming actions;
- electronic/electrical tactical hazards;
- communications equipment as targetable tactical objects;
- repair or calibration checks;
- Move/Ability/Item/Trainer Feature effects on communications;
- telepathy/Aura/device bridge rules;
- Porygon/Rotom network/device interaction beyond exact validated rules;
- objective-aware withdrawal/protection;
- semantic adapter support for active technical sites.
