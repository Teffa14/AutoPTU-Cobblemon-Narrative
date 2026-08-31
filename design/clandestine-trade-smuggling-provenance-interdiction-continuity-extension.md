# Ouros Clandestine Trade, Smuggling, Provenance & Interdiction Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This extension gives Ouros persistent continuity for clandestine supply chains without inventing a universal criminal-law, customs, policing or black-market subsystem.

The layer tracks how a disputed, restricted, concealed or illicitly sourced object, material batch, Pokémon, specimen or shipment moves through source, intermediary, transit, storage, brokerage and destination stages when the world has enough evidence to justify those records. It preserves partial knowledge and provenance gaps instead of collapsing an investigation into a single `contraband=true` flag.

It does not decide whether something is legally prohibited. That conclusion requires an already authored rule, mandate, case finding or other governing authority.

## Existing authority boundaries

Material Culture owns physical item identity, material batches, ownership, custody and ordinary provenance events.

Courier, Port, Storage, Travel, Rail, Road, Aviation and Transit Hub systems own ordinary physical movement, shipment legs, facilities, calls and journey state.

Interregional Arrival Inspection owns a scoped inspection episode only when an authored inspection requirement exists.

Credentials owns authorization records, representations and scope.

Covert Operations owns infiltration, cover, access, exposure and extraction state for a covert mission.

Case Authority owns allegations, investigative evidence and case custody.

Investigation/Inference owns hypotheses about routes, actors, motive and causal relationships until evidence supports narrower conclusions.

Organization Lineage owns organization identity and membership evidence. Participation in one clandestine handoff never creates organization membership by itself.

Conservation, Wildlife, Science, Care, Pokémon Agency and Shelter systems own ecological interpretation, individual Pokémon identity, welfare, agency and later placement.

Finance owns actual payment or financial obligations when they become relevant.

This extension owns only the continuity of a clandestine chain episode, including intermediary roles, route fragments, concealment or relabeling events, market offers, interdictions and reconfiguration after disruption.

## 1. Clandestine chain episode

```yaml
clandestine_chain_episode:
  chain_episode_id: null
  subject_refs: []
  source_claim_refs: []
  chain_node_ids: []
  handoff_ids: []
  concealment_event_ids: []
  market_offer_ids: []
  participant_knowledge_slice_ids: []
  interdiction_event_ids: []
  route_hypothesis_refs: []
  related_case_ids: []
  related_operation_ids: []
  current_state: OBSERVED_FRAGMENT
  canon_status: proposed
  provenance_refs: []
  chronicle_event_ids: []
```

Candidate continuity states:

- OBSERVED_FRAGMENT
- SUSPECTED_CHAIN
- PARTIALLY_MAPPED
- ACTIVE
- DISRUPTED
- RECONFIGURING
- DORMANT
- CLOSED_BY_EVIDENCE
- UNKNOWN

These states describe how much of one chain episode is understood or operationally active. They do not declare guilt, criminal liability or organization status.

`DISRUPTED` means at least one material route or handoff stopped. It does not mean every participant was found or the demand disappeared.

## 2. Chain node

```yaml
clandestine_chain_node:
  node_id: null
  chain_episode_id: null
  node_type: null
  location_ref: null
  actor_or_org_refs: []
  subject_refs: []
  observed_event_refs: []
  claimed_function_refs: []
  knowledge_state: PARTIAL
  active_from: null
  active_until: null
  provenance_refs: []
```

Candidate node types:

- SOURCE
- ASSEMBLY
- PROCESSING
- STORAGE
- TRANSIT
- BROKERAGE
- MARKET
- DESTINATION
- UNKNOWN_ROLE

A node type is an investigative/world-state description for one chain. A legitimate warehouse can be a STORAGE node in one episode and remain a normal warehouse generally.

`CHAIN_NODE_RECORDED != LOCATION_IS_CRIMINAL`

## 3. Handoff record

```yaml
clandestine_chain_handoff:
  handoff_id: null
  chain_episode_id: null
  subject_refs: []
  from_actor_or_custodian_refs: []
  to_actor_or_custodian_refs: []
  from_node_ref: null
  to_node_ref: null
  planned_window_ref: null
  observed_time: null
  custody_transfer_ref: null
  transport_event_refs: []
  documentary_claim_refs: []
  evidence_refs: []
  confidence_state: OBSERVED_OR_AUTHORED
```

A handoff can be observed even when payment, intent, legality or final destination remains unknown.

Hard separations:

- `HANDOFF_OBSERVED != SALE_COMPLETED`
- `HANDOFF_OBSERVED != FULL_ROUTE_KNOWN`
- `CARRIER_PRESENT != NETWORK_MEMBER`
- `BROKER_CONTACT != ORGANIZATION_MEMBERSHIP`

Ordinary custody remains owned by Material Culture/Courier/Storage. This record links that custody event into the clandestine-chain context.

## 4. Origin claim and provenance disagreement

```yaml
clandestine_origin_claim:
  origin_claim_id: null
  subject_ref: null
  claimed_origin_ref: null
  claimant_actor_or_record_ref: null
  claim_time: null
  supporting_record_refs: []
  conflicting_claim_refs: []
  verified_provenance_refs: []
  current_assessment: UNRESOLVED
```

Candidate assessments:

- UNRESOLVED
- CONSISTENT_WITH_CURRENT_EVIDENCE
- CONFLICTS_WITH_CURRENT_EVIDENCE
- PARTIALLY_SUPPORTED
- SUPERSEDED_BY_BETTER_EVIDENCE

Never overwrite the underlying original provenance when a later label changes.

`DECLARED_ORIGIN != VERIFIED_ORIGIN`

`BROKEN_PROVENANCE != ILLEGAL_ORIGIN`

`FALSE_RECORD != INTENT_PROVEN`

A bad record can result from fraud, copying, transcription, stale data, mistaken identity or another cause. Investigation owns causal inference.

## 5. Concealment, relabeling and provenance-obscuring events

```yaml
provenance_obscuring_event:
  event_id: null
  chain_episode_id: null
  subject_refs: []
  event_type: null
  actor_refs: []
  location_ref: null
  prior_label_or_record_refs: []
  resulting_label_or_record_refs: []
  observed_physical_change_refs: []
  evidence_refs: []
  intent_claim_refs: []
  timestamp: null
```

Candidate event types:

- REPACKAGED
- RELABELED
- IDENTIFIER_REMOVED
- IDENTIFIER_REPLACED
- MIXED_WITH_OTHER_BATCH
- TRANSFERRED_TO_NEW_CONTAINER
- ROUTE_RECORD_GAP
- DOCUMENT_SUBSTITUTED
- OTHER_AUTHORED_EVENT

The event can preserve what physically or documentarily changed without deciding intent.

`RELABELED != FRAUD_CONFIRMED`

`HIDDEN_COMPARTMENT_FOUND != STOLEN`

When a container or compartment is relevant, another system owns the physical object and access state.

## 6. Participant knowledge slice

Do not expose a universal omniscient network graph to participants or AI.

```yaml
chain_participant_knowledge_slice:
  knowledge_slice_id: null
  chain_episode_id: null
  actor_id: null
  known_subject_refs: []
  known_handoff_refs: []
  known_actor_refs: []
  known_location_refs: []
  believed_origin_claim_refs: []
  believed_destination_claim_refs: []
  known_risk_or_restriction_refs: []
  unknown_or_compartmentalized_refs: []
  learned_event_refs: []
  last_updated_event_ref: null
```

A carrier may know only a pickup and dropoff. A broker may know several contacts but never touch the cargo. A buyer may know the seller but not the source. A processor may know the material is unusual without knowing it was taken from a protected site.

`POSSESSION != KNOWLEDGE_OF_ORIGIN`

`PARTICIPATION != KNOWLEDGE_OF_FULL_CHAIN`

Communications owns later information propagation.

## 7. Market offer

```yaml
clandestine_market_offer:
  offer_id: null
  chain_episode_id: null
  offered_subject_refs: []
  offering_actor_or_org_ref: null
  intended_audience_refs: []
  access_context_ref: null
  asking_terms_ref: null
  claimed_origin_refs: []
  claimed_authorization_refs: []
  offered_at: null
  offer_state: OPEN
  transaction_ref: null
  evidence_refs: []
```

Candidate states:

- OPEN
- WITHDRAWN
- EXPIRED
- ACCEPTED_PENDING_TRANSFER
- TRANSFERRED
- DISPUTED
- UNKNOWN

An offer does not establish market value. No universal `black market markup` exists.

`MARKET_OFFER != SALE_COMPLETED`

If a real transaction occurs, Finance and Material Culture own payment and transfer.

## 8. Restriction and legality references

This layer may reference an authored restriction but cannot create one.

```yaml
restriction_context_ref:
  restriction_context_id: null
  subject_scope_refs: []
  activity_scope_refs: []
  location_scope_refs: []
  governing_authority_ref: null
  governing_rule_ref: null
  effective_window_ref: null
  authorization_exception_refs: []
  current_validation_state: VERIFIED_REFERENCE
```

Hard rules:

`RESTRICTED_BY_ONE_POLICY != UNIVERSALLY_ILLEGAL`

`NO_DOCUMENT_PRESENT != PROHIBITED`

`AUTHENTIC_DOCUMENT != ACCURATE_SHIPMENT_CLAIM`

`AUTHENTIC_CREDENTIAL != AUTHORIZED_FOR_THIS_SHIPMENT`

If Ouros canon has not defined the relevant restriction, the narrative generator may propose a story premise but must keep it NON-CANON and cannot enforce it as world law.

## 9. Interdiction event

An interdiction is a factual interruption, hold, recovery or route break. It does not establish guilt by itself.

```yaml
clandestine_chain_interdiction:
  interdiction_id: null
  chain_episode_id: null
  interdiction_type: null
  location_ref: null
  actor_refs: []
  subject_refs: []
  authority_or_mandate_ref: null
  triggering_observation_refs: []
  battle_result_refs: []
  custody_change_refs: []
  resulting_case_refs: []
  resulting_chain_state: DISRUPTED
  timestamp: null
  provenance_refs: []
```

Candidate types:

- VOLUNTARY_STOP
- AUTHORIZED_HOLD
- RECOVERY
- ROUTE_BLOCKED
- HANDOFF_PREVENTED
- SITE_ABANDONED
- SHIPMENT_DIVERTED
- OTHER_AUTHORED_EVENT

`SEIZURE_RECORDED != GUILT_ESTABLISHED`

`INTERDICTION_SUCCESS != NETWORK_DESTROYED`

`RECOVERED != RETURNED_TO_OWNER`

Authority for search, seizure, arrest or detention must come from other canon systems if such powers exist at all.

## 10. Reconfiguration after disruption

Clandestine chains should be capable of adapting through ordinary world agency.

```yaml
chain_reconfiguration_event:
  reconfiguration_id: null
  chain_episode_id: null
  triggering_event_refs: []
  actor_or_org_refs: []
  retired_node_refs: []
  new_or_changed_node_refs: []
  retired_route_refs: []
  new_route_claim_refs: []
  knowledge_constraints: []
  effective_time: null
```

World Agency determines whether actors actually have the knowledge, motive, resources and access to reconfigure.

Do not automatically generate a replacement route merely because players disrupted one. Reconfiguration requires plausible actors and state.

## 11. Recovered Pokémon and living subjects

If a Pokémon or other living subject is recovered from a clandestine chain, this extension ends its authority at the recovery/custody fact.

Use Pokémon Agency, Care, Shelter, Case Authority and existing ownership/custody systems afterward.

Hard rules:

- `POKEMON_RECOVERED != PLAYER_OWNERSHIP`
- `POKEMON_RECOVERED != ORIGINAL_OWNER_IDENTIFIED`
- `ORIGINAL_OWNER_CLAIMED != CLAIM_VERIFIED`
- `RECOVERED_FROM_CHAIN != WILLING_TO_JOIN_PLAYER`
- `SPECIES_RARITY != ILLEGAL_ORIGIN`

Battle capture mechanics, if used, cannot silently replace narrative custody/ownership decisions.

## 12. Investigation and caseboard projection

Investigation may build route hypotheses from observed handoffs, documents, testimonies, timings and provenance conflicts.

The player-facing projection may show:

- confirmed handoffs;
- observed route segments;
- unresolved origin claims;
- known custody gaps;
- conflicting declarations;
- possible intermediaries explicitly marked as hypotheses;
- known interdictions;
- unresolved destinations.

It must not display hidden guilt flags, omniscient membership, secret buyer identity or undiscovered route nodes.

`ROUTE_HYPOTHESIS != ROUTE_FACT`

## 13. Battle authority boundary

AutoPTU can resolve only tactical facts delegated in an explicit BattleSpec.

A tactical win may establish narrow physical consequences such as:

- immediate access to a handoff area is clear;
- a fixed exit route is no longer contested by current combatants;
- named combatants were defeated or withdrew if the verified battle contract says so.

A battle cannot establish:

- illicit origin;
- ownership;
- intent;
- guilt;
- organization membership;
- buyer identity;
- provenance authenticity;
- search legality;
- seizure validity;
- future custody disposition;
- that the entire network ended.

`BATTLE_WON != CHAIN_PROVEN`

## 14. Minecraft / Cobblemon / Craftics boundary

The adapter may render crates, containers, warehouses, vehicles, doors, tags, NPCs, Pokémon, documents, route changes, animations and aftermath after Ouros/AutoPTU has established the authoritative facts.

It may not decide:

- whether cargo is illicit;
- whether a hidden compartment exists unless world state already authored it;
- whether a search succeeds;
- whether a document is fraudulent;
- who knows what;
- who becomes a combatant;
- whether a carrier escapes;
- ownership or custody transfer;
- guilt or organization membership;
- PTU HP/status;
- network closure.

Cobblemon BattleState remains non-authoritative for Ouros combatant selection and tactical truth.

## 15. Required capability categories for tactical variants

Any encounter built from this layer must declare all permanent engine categories:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

If cargo carrying, escorting, moving vehicles, dynamic doors, reaction windows, environmental displacement, timed reinforcements or tactical withdrawal matter, the encounter must name those dependencies explicitly rather than treating them as implied by a generic smuggling theme.

## 16. Canon status model

Every concrete chain, route, restriction, market, organization, policy, enforcement body or protected subject introduced from this extension must carry one of:

- CANON_APPROVED
- PROPOSED
- UNCERTAIN
- RESEARCH_ONLY

The default for Pass 155 worldbuilding is PROPOSED.

This layer supplies a continuity grammar. It does not silently establish who the criminals of Ouros are.