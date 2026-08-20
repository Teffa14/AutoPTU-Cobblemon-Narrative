# Ouros Illicit Networks, Smuggling & Diversion Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already models cases, custody, evidence, antagonists, factions, transport, finance, conservation, digital records and persistent Pokémon identity. This layer models the missing operational chain connecting illicit acquisition, storage, movement, brokerage, demand and recovery.

The system must not assume a universal criminal code. It stores facts, claims, authorization, provenance and institutional assessments. Whether a specific act is illegal must come from authored Ouros canon or an explicit institutional rule.

## 1. Core separation

Keep these states separate:

- physical possession;
- custody;
- ownership claim;
- authorization;
- provenance;
- transaction history;
- allegation;
- evidence;
- institutional assessment;
- public belief;
- mechanical PTU state.

A Pokémon being captured successfully does not prove the capture was lawful.

A Pokémon being stolen does not transfer ownership.

A rare Pokémon being sold does not prove a black-market transaction.

A hidden shipment does not prove criminality.

## 2. Illicit operation object

```yaml
illicit_operation:
  operation_id: null
  status: suspected
  known_actor_ids: []
  suspected_actor_ids: []
  cell_ids: []
  target_asset_classes: []
  source_locations: []
  destination_locations: []
  known_methods: []
  suspected_methods: []
  transport_dependencies: []
  storage_dependencies: []
  finance_links: []
  front_business_ids: []
  linked_case_ids: []
  evidence_ids: []
  public_visibility: low
  legal_basis_refs: []
  unresolved_questions: []
```

Suggested states:

- rumor;
- suspected;
- corroborated;
- active;
- disrupted;
- fragmented;
- dormant;
- dissolved;
- unresolved.

These are investigation/operation states, not guilt verdicts for every associated actor.

## 3. Asset flow graph

Track movement leg by leg.

```yaml
asset_flow_leg:
  flow_leg_id: null
  asset_ids: []
  origin_location_id: null
  destination_location_id: null
  departure_window: null
  arrival_window: null
  carrier_actor_ids: []
  transport_service_id: null
  custody_from_id: null
  custody_to_id: null
  declared_purpose: null
  authorization_ref: null
  concealment_state: none
  evidence_refs: []
  verified_state: unknown
```

Possible flow shapes:

- source → buyer;
- source → holding site → broker → buyer;
- institutional storage → diverted shipment → legitimate carrier → hidden buyer;
- wild capture → temporary enclosure → maritime transfer → regional broker;
- museum theft → private storage → attempted resale;
- stolen Pokémon → multiple transfers → recovery.

Do not assume every intermediate actor understands the full network.

## 4. Acquisition events

```yaml
acquisition_event:
  event_id: null
  asset_ids: []
  actor_ids: []
  acquisition_type: unknown
  source_location_id: null
  prior_custodian_id: null
  prior_owner_claim_ids: []
  authorization_refs: []
  evidence_refs: []
  observed_by_ids: []
  canonical_status: unresolved
```

Candidate high-level acquisition types:

- voluntary transfer;
- institutional issue;
- wild capture;
- recovery/salvage;
- theft allegation;
- diversion allegation;
- fraudulent transfer allegation;
- unknown provenance.

Never convert an allegation field into a canonical fact automatically.

## 5. Diversion

Diversion means an asset leaves an expected or authorized flow.

```yaml
diversion_event:
  diversion_id: null
  asset_ids: []
  expected_flow_leg_id: null
  observed_actual_destination_id: null
  discovered_at: null
  discovered_by_ids: []
  stated_explanation: null
  supporting_evidence_ids: []
  alternate_explanations: []
  case_id: null
```

A diversion may result from:

- theft;
- clerical error;
- emergency reroute;
- legitimate transfer not recorded correctly;
- fraud;
- coercion;
- accidental loss;
- unknown cause.

The generator should preserve these alternatives until evidence narrows them.

## 6. Front businesses and mixed institutions

```yaml
front_business_state:
  institution_id: null
  legitimate_services: []
  legitimate_client_ids: []
  suspected_illicit_functions: []
  verified_illicit_functions: []
  informed_staff_ids: []
  uninformed_staff_ids: []
  compartmentalized_access: []
  linked_asset_flow_ids: []
  linked_case_ids: []
```

Do not mark an entire workplace as criminal because one employee misuses it.

A front can also provide genuine services. That mixed truth is often more useful than a fake storefront with no other function.

## 7. Brokers, buyers and clients

```yaml
network_transaction_intent:
  intent_id: null
  requester_actor_id: null
  requested_asset_class: null
  requested_asset_ids: []
  quantity_or_scope: null
  offered_compensation_ref: null
  delivery_region_id: null
  deadline: null
  broker_ids: []
  status: rumored
  source_evidence_ids: []
```

Demand should be persistent state when known.

The system can support:

- anonymous buyer claims;
- recurring buyer patterns;
- commissioned captures;
- opportunistic resale;
- brokered transfers;
- buyers who do not know the asset was stolen;
- buyers who knowingly request illicit acquisition.

Knowledge must be actor-specific.

## 8. Network cells

```yaml
network_cell:
  cell_id: null
  operation_id: null
  actor_ids: []
  local_goals: []
  known_upstream_contacts: []
  known_downstream_contacts: []
  controlled_assets: []
  known_routes: []
  compartmentalization_state: null
  exposure_state: low
  fallback_routes: []
  current_activity_state: null
```

A cell does not automatically know the full organization.

Disrupting one cell can:

- remove a route;
- raise prices or delays if economy later supports that state;
- force rerouting;
- expose another contact;
- fragment the operation;
- create temporary dormancy;
- have no effect on distant cells if the organization is compartmentalized.

Do not generate a replacement cell only because the players were successful. A replacement needs actors, resources and motive.

## 9. Concealment records

```yaml
concealment_record:
  concealment_id: null
  asset_ids: []
  method_category: null
  container_or_location_ref: null
  installed_by_actor_id: null
  discovered_by_ids: []
  discovery_event_id: null
  evidence_ids: []
  mechanical_effect_ref: null
```

Narrative concealment cannot create a stealth modifier by itself.

If concealment requires Guile, Stealth, Perception, Technology Education, Survival or a Feature, use the governing PTU/Caelo rule only after validation.

## 10. Transport integration

The transport layer remains authoritative for route/service existence.

An illicit network may:

- use a legitimate ferry without the operator knowing;
- bribe or coerce an employee if canon/evidence supports it;
- operate its own vehicle;
- exploit abandoned routes;
- hide transfers inside regular freight;
- switch routes after exposure.

Do not mark a transport service as complicit simply because contraband moved through it.

## 11. Finance integration

The finance layer remains authoritative for actual transfers.

Pass 58 may attach transaction claims to an operation, but it must not invent:

- prices;
- laundering formulas;
- exchange rates;
- profit margins;
- bribe amounts;
- black-market multipliers.

Money can matter narratively through explicit transfers, promised payments, restricted funds or unexplained discrepancies.

## 12. Pokémon-specific protections

Persistent Pokémon identity is critical.

For a stolen, poached or diverted Pokémon, preserve:

```yaml
pokemon_asset_context:
  pokemon_id: null
  current_custody_id: null
  current_owner_claim_ids: []
  capture_record_ref: null
  partnership_history_ref: null
  transfer_history_refs: []
  recovery_case_ids: []
  current_location_id: null
```

Recovery must return the same Pokémon entity.

Do not generate a replacement specimen with the same species/level.

Do not infer that a recovered Pokémon wishes to return to a previous Trainer. Custody, ownership, partnership and agency remain distinct.

## 13. Conservation integration

Poaching and wildlife exploitation can modify conservation state only through traceable evidence and world-state changes.

A single capture does not automatically alter population abundance.

A suspected poaching network may create:

- increased survey effort;
- protected-location redaction;
- temporary visitor restrictions;
- patrol requests;
- camera-trap deployment;
- route monitoring;
- recovery/relocation work.

Exact ecological effects require the population/collective systems to support them.

## 14. Case and evidence integration

Every operation can link to one or more cases.

Useful evidence types already supported by adjacent systems:

- custody records;
- photographs/video;
- shipment identifiers;
- communication records;
- access logs;
- transaction records;
- witness reports;
- map/route records;
- specimen provenance;
- institutional inventory mismatches.

An evidence object can support a flow leg without proving the entire network.

## 15. Recovery and disposition

```yaml
recovery_event:
  recovery_id: null
  asset_ids: []
  recovered_from_location_id: null
  recovered_by_actor_ids: []
  immediate_custodian_id: null
  condition_observations: []
  linked_case_ids: []
  disposition_state: pending
  evidence_refs: []
```

Possible disposition states should remain canon-dependent:

- returned to prior custodian;
- transferred to care facility;
- held as evidence;
- placed under temporary stewardship;
- ownership disputed;
- released/relocated if separately authorized;
- unresolved.

Narrative generation must not decide legal ownership from possession alone.

## 16. Public information

The media/communications layer controls what becomes public.

Public reporting may contain:

- verified facts;
- institutional statements;
- allegations;
- corrections;
- incomplete suspect descriptions;
- warnings to travelers;
- requests for witnesses.

Publishing a suspect name does not make the allegation true.

## 17. Multiplayer secrecy

Store network knowledge per actor/player.

A player may know:

- one drop location;
- a broker alias;
- a shipment ID;
- a suspect vehicle;
- an unverified buyer rumor.

Other players should not receive this automatically unless the information is shared through an authorized communication, case record or party mechanic.

## 18. World generation rules

Generate an illicit-network hook only when at least one source fact exists:

- missing asset;
- suspicious custody break;
- verified diversion;
- poaching evidence;
- buyer request;
- unusual repeated route pattern;
- front-business inconsistency;
- witness report;
- financial discrepancy;
- recovered asset with unexplained provenance.

Do not generate a network solely because the world has been quiet.

## 19. Long-form network progression

A network arc can evolve through:

1. isolated incident;
2. evidence preservation;
3. repeated pattern;
4. route/broker identification;
5. partial disruption;
6. adaptation or fragmentation;
7. buyer/client discovery;
8. recovery and restitution;
9. institutional response;
10. long-term aftermath.

The arc may end at any stage.

Total eradication is not required for satisfying local closure.

## 20. PTU/Caelo boundary

This layer never invents:

- theft Skill checks;
- concealment bonuses;
- chase movement;
- restraint mechanics;
- surrender rules;
- capture modifiers;
- confiscation rules;
- ownership law;
- search powers;
- detention rules;
- surveillance bonuses;
- illegal-item lists;
- poaching penalties.

Use explicit PTU/Caelo rules only after source validation.

## 21. Encounter contract — Freight Yard Transfer

Narrative premise:

A shipment linked to an active case is about to move between two carriers at a freight yard. Players need to stop the transfer while preserving the identity and custody chain of the cargo.

### Full version

Possible objectives:

- prevent carrier A from reaching carrier B;
- protect recovered cargo;
- allow surrender/withdrawal;
- maintain evidence integrity;
- avoid damaging sensitive cargo zones.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED foundation;
- base movement legality — VERIFIED foundation;
- complete movement including interception/forced movement — BLOCKING;
- core calculations — VERIFIED foundation;
- action economy/initiative — VERIFIED foundation;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if active loading zones or route control are tactical;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

### Reduced version

Freeze the cargo transfer in overworld state before battle. Keep cargo, forklifts, civilians and evidence containers outside tactical authority. Run a normal static AutoPTU battle if confrontation occurs. On conclusion, update custody/flow state from the authoritative result and player choices.

## 22. Encounter contract — Hidden Nursery Recovery

Narrative premise:

A legitimate care facility contains a compartmentalized holding area used to divert Pokémon before onward transfer. Some staff are uninvolved.

### Full version

Potential mechanics:

- protect noncombatants;
- escort/recover specific Pokémon entities;
- secure exits;
- distinguish hostile, neutral and surrendering actors;
- preserve clinic infrastructure.

Blocking dependencies:

- complete movement/interception/forced movement;
- broad zones/reactions if exits are actively controlled;
- tactical AI;
- Minecraft playback;
- any escort/protect objective contract not yet verified.

### Reduced version

Resolve discovery, identity checks and evacuation outside battle. Freeze only hostile combatants into a static arena. Recovered Pokémon remain world-state entities and never become battle rewards automatically.

## 23. Encounter contract — Harbor Transfer Disruption

Narrative premise:

A case links a recurring handoff to a harbor service window. The players know the shipment ID but not every participant.

### Full version

Potential mechanics:

- timed transfer window;
- BREAK_THROUGH / INTERCEPT / WITHDRAW objectives;
- multiple exits;
- moving carriers;
- optional noncombat surrender;
- active dock hazards only if PTU/AutoPTU support them.

Blocking dependencies:

- complete movement/interception/forced movement;
- terrain/weather/hazards/zones/reactions if dock state is tactical;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics playback.

### Reduced version

Use world-state timing to determine whether the handoff occurred before battle. Once a confrontation freezes into AutoPTU, use a standard static encounter. Transfer/custody consequences are applied afterward by the overworld authority layer.

## 24. Implementation responsibility

This layer belongs primarily in the persistent world authority, not the battle core.

The future server layer should own:

- asset identity;
- custody;
- provenance;
- transaction/flow records;
- operation/cell state;
- actor knowledge;
- case linkage;
- permissions;
- recovery/disposition.

AutoPTU-Java owns tactical legality and results when combat starts.

Minecraft/Cobblemon presents world state and semantic outcomes. It must not decide theft, ownership, guilt, capture legality or transfer validity client-side.
