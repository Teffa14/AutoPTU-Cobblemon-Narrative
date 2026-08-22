# Ouros Retail Markets, Auctions & Merchant Networks Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already tracks physical items, material provenance, money/funding, supply chains, public spaces, transport, tourism, postal delivery and illicit diversion. This layer owns the player-facing exchange surface between those systems: market venues, vendor presence, offers, market sessions, auctions, merchant routes and completed transfers.

The goal is a living marketplace without turning Ouros into a continuous economic simulator.

Routine shopping should remain fast. Detailed state appears when provenance, scarcity, timing, competition, relationships, institutional capacity or player-directed merchant gameplay makes the exchange meaningful.

## Authority boundary

The market layer may expose and orchestrate state. It does not create upstream truth.

Authority split:

- Material Culture owns physical item/batch identity and provenance.
- Supply Chains owns stock availability, reservations, storage and freight.
- Finance owns authoritative money balances/transfers where those exist.
- Public Space owns the physical shared space used by stalls and crowds.
- Travel/Transport owns whether merchants can actually reach a venue.
- Postal owns addressed delivery after a purchase when used.
- Cases own evidence/allegations if a transaction is disputed.
- Illicit Networks owns evidence-backed clandestine commerce.
- Pokémon Agency owns Pokémon identity, custody, partnership and transfer constraints.
- AutoPTU owns mechanical Item behavior and battle legality.
- Minecraft/Cobblemon renders the current projection only.

A market never manufactures stock, ownership, authority or PTU effects by inference.

## 1. Market venue

```yaml
market_venue:
  market_venue_id: null
  location_id: null
  venue_type: null
  public_space_ids: []
  operator_institution_id: null
  permanent_vendor_space_ids: []
  temporary_vendor_space_ids: []
  service_node_ids: []
  transport_connection_ids: []
  storage_node_ids: []
  operating_calendar_id: null
  access_policy_ids: []
  current_operating_state: OPEN
  current_session_id: null
  linked_event_ids: []
  history_event_ids: []
```

Candidate venue types:

- MARKET_HALL
- STREET_MARKET
- HARBOR_MARKET
- AUCTION_HOUSE
- MARKET_SQUARE
- SWAP_MEET
- SPECIALIST_ARCADE
- MOBILE_MARKET
- INSTITUTIONAL_SALE
- SEASONAL_FAIR_MARKET

Operating states:

- OPEN
- LIMITED
- SETTING_UP
- CLOSING
- CLOSED_SCHEDULED
- CANCELLED
- RELOCATED
- DISRUPTED
- EMERGENCY_ONLY

The venue is persistent even when no session is active.

## 2. Market session

Recurring markets need edition-level history.

```yaml
market_session:
  market_session_id: null
  market_venue_id: null
  scheduled_window: null
  actual_open_time: null
  actual_close_time: null
  vendor_presence_ids: []
  active_listing_ids: []
  auction_event_ids: []
  temporary_service_ids: []
  visitor_pressure_revision_id: null
  route_dependency_ids: []
  disruption_ids: []
  public_information_ids: []
  chronicle_event_ids: []
  final_state: null
```

A Saturday market can recur for decades while every Saturday remains a separate session.

A cancelled session remains historical state.

## 3. Merchant profile

A merchant is an actor or institution with continuity beyond one stall.

```yaml
merchant_profile:
  merchant_id: null
  actor_or_institution_id: null
  public_trade_name: null
  specialty_tags: []
  permanent_venue_ids: []
  merchant_route_id: null
  supplier_relationship_ids: []
  commission_service_ids: []
  consignment_policy_id: null
  public_contact_id: null
  current_operating_state: ACTIVE
  observed_history_ids: []
```

Narrative specialty tags do not grant Skills, Features or price modifiers.

A merchant can retire, relocate, change specialty, train a successor or stop attending one venue without disappearing from Chronicle.

## 4. Vendor presence

A merchant profile does not prove the merchant is physically present today.

```yaml
vendor_presence:
  vendor_presence_id: null
  merchant_id: null
  market_session_id: null
  vendor_space_id: null
  actual_arrival_time: null
  actual_departure_time: null
  operator_actor_ids: []
  presence_state: EXPECTED
  limitation_ids: []
  source_route_ids: []
  active_listing_ids: []
```

Suggested states:

- EXPECTED
- ARRIVED
- OPEN
- LIMITED
- TEMPORARILY_AWAY
- CLOSED_EARLY
- NO_SHOW
- DEPARTED

A no-show may come from transport, illness, staffing, crisis or a personal choice. Do not infer motive automatically.

## 5. Vendor space / stall / storefront

```yaml
vendor_space:
  vendor_space_id: null
  market_venue_id: null
  physical_location_ref: null
  space_type: null
  current_assignee_id: null
  signage_ref: null
  storage_link_ids: []
  utility_dependency_ids: []
  accessibility_state_id: null
  current_visual_projection_id: null
```

The stall is physical space. Its contents are not inventory truth.

Minecraft shelves, chests and displays are representative unless linked through a server-authoritative inventory contract.

## 6. Offer listing

An offer is a versioned proposal, not a transfer.

```yaml
offer_listing:
  offer_listing_id: null
  seller_id: null
  seller_authority_claim_id: null
  market_session_id: null
  vendor_presence_id: null
  offer_type: null
  subject_ref: null
  item_instance_ids: []
  batch_ref_ids: []
  quantity_band: null
  mechanical_item_ref: null
  advertised_terms_id: null
  currency_ref: null
  quoted_amount: null
  exchange_request_refs: []
  valid_from: null
  valid_until: null
  access_requirement_ids: []
  provenance_summary_ref: null
  current_state: DRAFT
```

Offer types:

- FIXED_OFFER
- NEGOTIABLE_OFFER
- EXCHANGE
- CONSIGNMENT
- AUCTION_LOT
- SERVICE_OFFER
- COMMISSION_INTAKE
- INSTITUTIONAL_RELEASE

States:

- DRAFT
- ANNOUNCED
- ACTIVE
- RESERVED_PENDING_TRANSFER
- SUSPENDED
- WITHDRAWN
- EXPIRED
- COMPLETED
- CANCELLED

`quoted_amount` exists only when the approved economy actually provides a valid value. This layer never invents price formulas.

## 7. Availability validation

Before an offer becomes ACTIVE, validate its underlying state.

```yaml
offer_availability_check:
  check_id: null
  offer_listing_id: null
  checked_at: null
  supply_state_ref: null
  ownership_or_transfer_authority_ref: null
  custody_ref: null
  reservation_ref: null
  restriction_ref_ids: []
  mechanical_item_validation_ref: null
  result: UNKNOWN
  blocker_ids: []
```

Results:

- AVAILABLE
- AVAILABLE_LIMITED
- RESERVED
- QUALITY_HOLD
- TRANSFER_AUTHORITY_UNRESOLVED
- NOT_PHYSICALLY_AVAILABLE
- MECHANICALLY_UNRESOLVED
- WITHDRAWN
- UNKNOWN

A stale display may disagree with this check. That disagreement can be content without becoming fraud automatically.

## 8. Advertised terms versus agreed terms

```yaml
trade_terms:
  terms_id: null
  offer_listing_id: null
  version: 1
  currency_ref: null
  amount: null
  exchange_object_refs: []
  service_commitment_ids: []
  pickup_or_delivery_method: null
  transfer_location_id: null
  deadline: null
  condition_claims: []
  accepted_by_ids: []
  accepted_at: null
```

Negotiation can create a new version.

The system stores observable agreed terms. It does not infer whether either participant is happy, desperate, exploited or generous without evidence.

## 9. Transaction record

```yaml
market_transaction:
  transaction_id: null
  offer_listing_id: null
  buyer_id: null
  seller_id: null
  agreed_terms_id: null
  payment_authorization_ref: null
  payment_transfer_ref: null
  transfer_authority_ref: null
  physical_handoff_ref: null
  provenance_event_refs: []
  postal_or_freight_handoff_ref: null
  transaction_state: AGREED
  dispute_case_id: null
  completed_at: null
```

States:

- NEGOTIATING
- AGREED
- PAYMENT_PENDING
- PAYMENT_CONFIRMED
- HANDOFF_PENDING
- IN_DELIVERY
- COMPLETED
- CANCELLED_MUTUAL
- CANCELLED_BLOCKED
- DISPUTED

Important:

`AGREED` does not mean `COMPLETED`.

`PAYMENT_CONFIRMED` does not mean custody changed.

`physical_handoff_ref` changes custody only through the authoritative Material/Custody systems.

## 10. Secondhand provenance

Resale must preserve identity.

```yaml
secondhand_sale_context:
  item_instance_id: null
  current_offer_listing_id: null
  known_provenance_event_ids: []
  provenance_gap_ids: []
  authenticity_assessment_ids: []
  condition_assessment_ids: []
  public_story_claim_ids: []
  restricted_information_ids: []
```

A seller can truthfully know little about an object.

A provenance gap is not proof of theft.

A famous story about an object is not mechanical metadata.

A replica openly sold as a replica is not counterfeit.

## 11. Consignment

```yaml
consignment_record:
  consignment_id: null
  consignor_id: null
  merchant_id: null
  subject_item_instance_ids: []
  custody_transfer_ref: null
  sale_authority_ref: null
  terms_id: null
  start_time: null
  end_time: null
  current_state: ACTIVE
  returned_event_id: null
  completed_transaction_id: null
```

Consignment is useful for museums, artisans, collectors and player vendors because custody and ownership can remain distinct.

## 12. Auction event

```yaml
auction_event:
  auction_event_id: null
  market_session_id: null
  auctioneer_id: null
  auction_lot_ids: []
  eligibility_rule_ref: null
  scheduled_start: null
  actual_start: null
  actual_end: null
  public_information_ids: []
  state: ANNOUNCED
```

States:

- ANNOUNCED
- CHECK_IN
- OPEN
- PAUSED
- CLOSED
- CANCELLED

The auction event contains lots. It does not create their value.

## 13. Auction lot

```yaml
auction_lot:
  auction_lot_id: null
  auction_event_id: null
  item_instance_ids: []
  batch_ref_ids: []
  consignor_id: null
  sale_authority_ref: null
  provenance_summary_ref: null
  opening_terms_ref: null
  bid_record_ids: []
  winning_bid_id: null
  state: ANNOUNCED
  resulting_transaction_id: null
```

States:

- ANNOUNCED
- OPEN
- SOLD_PENDING_TRANSFER
- NO_SALE
- WITHDRAWN
- CANCELLED
- DISPUTED
- TRANSFERRED

Unique items keep the same item instance IDs before and after the auction.

## 14. Bid record

```yaml
bid_record:
  bid_id: null
  auction_lot_id: null
  bidder_id: null
  timestamp: null
  currency_ref: null
  amount: null
  exchange_terms_ref: null
  eligibility_validation_ref: null
  accepted_by_auctioneer: null
  withdrawn_at: null
```

A bid is an observable action.

It does not prove wealth beyond the validated requirement, emotional attachment, rivalry or future willingness to pay.

Exact increments, budgets and bidder AI are authored economy/gameplay questions, not narrative defaults.

## 15. Auction cancellation and provenance hold

An auction should be able to stop without pretending the story failed.

Potential causes:

- provenance unresolved;
- consignor authority challenged;
- item condition changed;
- venue evacuation;
- payment system outage;
- bidder eligibility issue;
- institutional stewardship review;
- seller withdrawal;
- route disruption before the lot arrives.

The result may generate a case, archive record or later relisting.

## 16. Merchant routes

```yaml
merchant_route:
  merchant_route_id: null
  merchant_id: null
  route_leg_ids: []
  regular_market_venue_ids: []
  planned_calendar_id: null
  transport_service_dependency_ids: []
  overnight_location_ids: []
  current_revision_id: null
  history_revision_ids: []
```

Merchant routes should react to roads, ferries, rail and regional access.

A rail opening can change a route without deleting the old one from history.

A merchant may skip a town one week without abandoning it permanently.

## 17. Market information

Markets create public information, but information can go stale.

```yaml
market_information_packet:
  market_information_id: null
  subject_ids: []
  venue_id: null
  session_id: null
  claims: []
  published_at: null
  channel_ids: []
  valid_through: null
  correction_ids: []
```

Claims might include:

- market open today;
- merchant expected;
- auction announced;
- specialist item advertised;
- vendor relocated;
- session cancelled;
- delivery delayed.

Publication does not guarantee the underlying state stayed unchanged afterward.

## 18. Market reputation without a universal score

Do not create one omniscient `merchant_reputation = 82` value.

Actors can instead know records and claims:

```yaml
merchant_public_record:
  merchant_id: null
  observer_or_community_id: null
  observed_transaction_ids: []
  public_claim_ids: []
  correction_ids: []
  institutional_review_ids: []
  current_summary_claim_ids: []
```

One community may trust a merchant while another barely knows them.

A successful transaction does not automatically create Friendship.

## 19. Routine-shopping compression

Routine shops should usually resolve through a validated service menu.

Expand the scene when:

- the player asks to interact socially;
- availability changed;
- provenance matters;
- the object is unique;
- an auction or negotiation is the point;
- a market session is culturally important;
- a vendor is a recurring NPC with relevant state;
- the transaction affects another project;
- there is a legitimate access/custody question;
- a route disruption creates a meaningful choice.

Do not turn every refill into roleplay tax.

## 20. Market day as world state

A recurring market session can alter:

- public-space occupancy;
- temporary jobs;
- transport demand;
- lodging occupancy;
- food service;
- tourism;
- waste generation;
- policing/stewardship presence only if authored;
- wild Pokémon observations;
- communications/public notices;
- local soundscape;
- postal pickup volume.

These changes require actual linked state. A market day should not randomly increase every system.

## 21. Pokémon at markets

Pokémon can participate in market life as:

- partners accompanying Trainers;
- institutional workers where legal and consented;
- wild visitors/scavengers;
- performers during an event;
- delivery partners;
- recurring local individuals;
- subjects of care or observation.

Hard guardrail:

A Pokémon is never generic market stock by default.

Any permanent Pokémon transfer must pass through the authoritative Pokémon Agency/Custody/Ownership/Consent contracts and project rules. No marketplace UI may bypass those systems.

The narrative generator must not assign monetary value to a Pokémon based on species, level, rarity, stats, Ability, Nature or battle record.

## 22. Player-to-player exchange

Multiplayer item exchange needs explicit consent and identity-safe transfer.

```yaml
player_exchange:
  exchange_id: null
  participant_ids: []
  offered_item_instance_ids: []
  offered_batch_refs: []
  offered_currency_refs: []
  proposed_terms_id: null
  participant_confirmation_refs: []
  authority_validation_refs: []
  final_handoff_refs: []
  current_state: PROPOSED
```

Irreversible transfers require confirmation from the players who control the affected property/state.

Do not infer consent from co-location, party membership, friendship state or chat silence.

## 23. Market disputes

Common disputes can include:

- item identity disagreement;
- condition disagreement;
- provenance question;
- payment mismatch;
- delivery mismatch;
- seller-authority challenge;
- listing expired before acceptance;
- duplicate/stale listing caused by system state;
- wrong batch/specification delivered.

The market layer records the transaction state. Cases/Institutional Review resolve evidence and mandate where applicable.

A dispute is not fraud automatically.

## 24. Minecraft projection

Minecraft/Cobblemon may render:

- stalls;
- merchant NPC representatives;
- signs;
- banners;
- sample display items;
- crowds in coarse numbers;
- auction podiums;
- closed shutters;
- delivery crates;
- noticeboards.

It must not infer:

- authoritative stock counts from containers;
- ownership from who stands behind a counter;
- price from sign text unless server state authored it;
- custody transfer from item pickup alone;
- successful payment from animation;
- availability from a visible model;
- Pokémon ownership from leashes, position or stall association.

Server state projects to Minecraft, not the reverse.

## 25. Battle handoff

A market conflict must freeze a legal battle snapshot.

Before starting AutoPTU:

1. identify actual combatants;
2. move or abstract civilians where the reduced encounter requires it;
3. preserve item/cargo identities outside BattleSpec unless mechanically implemented;
4. freeze geometry;
5. validate implemented mechanical Items in battle inventory;
6. preserve custody/transaction state;
7. open the battle;
8. consume authoritative battle transcript afterward;
9. update world state without fabricating damage to stalls/stock.

## 26. Encounter contract — Auction Hall Evacuation

Narrative premise:

A public auction session is interrupted by a genuine threat. The priority is to clear people and preserve custody of the lots. The interruption may be unrelated to the auction itself.

FULL version:

Requires:

- complete movement including interception/forced movement if civilians or lots move tactically;
- terrain/weather/hazards/zones/reactions if the threat changes the hall environment;
- AI tactical policy for EVACUATE, WITHDRAW, PROTECT_EXIT and AVOID_SENSITIVE_LOTS;
- Minecraft/Cobblemon/Craftics adapter/playback for semantic civilians, temporary barriers and lots.

REDUCED version:

- evacuation occurs in world state before battle;
- auction lots remain off-grid under custody;
- a static hall/perimeter is frozen;
- AutoPTU resolves only actual combatants;
- the auction remains PAUSED until aftermath review.

Narrative premise preserved.

## 27. Encounter contract — Traveling Market Chokepoint

Narrative premise:

A traveling group of merchants cannot reach the next market session because a route is obstructed or contested.

FULL version:

Requires:

- complete movement/interception for moving wagons/pack carriers/escorts;
- AI tactical policy for CLEAR_ROUTE, WITHDRAW, PROTECT and DISENGAGE_AFTER_ACCESS;
- environment family when route conditions are tactical;
- adapter/playback for transport/cargo.

REDUCED version:

- merchants and stock stay off-grid;
- AutoPTU uses a static chokepoint encounter if confrontation occurs;
- afterward Travel decides whether the route is open;
- Market Session decides whether arrival was still possible.

## 28. Encounter contract — Night Market Wildlife Spillover

Narrative premise:

A temporary night market overlaps with wildlife activity that existed before the event. The goal is safe separation, not automatic defeat/capture.

FULL version:

Requires:

- complete movement for moving groups and withdrawal;
- AI tactical policy for WITHDRAW, CLEAR_ZONE, AVOID_CIVILIANS;
- terrain/zones/reactions only if actual authored battlefield effects exist;
- adapter/playback for stalls, crowd movement and wildlife routes.

REDUCED version:

- the crowd is redirected first;
- market stalls are frozen outside a safe battle perimeter;
- only Pokémon that genuinely remain in conflict enter AutoPTU;
- ecology and market scheduling update afterward.

## 29. Permanent capability dependency map

Market systems can exist largely outside battle, but the rich encounter versions depend on specific engine families.

Targeting/footprints/range/LoS:

- VERIFIED for static battle geometry;
- does not make stalls, auction lots or crates targetable objects.

Base movement legality:

- VERIFIED for known Shift/Jump/movement-mode legality;
- does not implement carts, civilians, moving lots or merchant convoys.

Complete movement including push/pull/knockback/interception/forced movement:

- required by full escort/evacuation/chokepoint versions;
- currently BLOCKING as a complete family.

Core calculations:

- VERIFIED;
- does not include appraisal, bargaining, market value or price formulas.

Action economy/initiative:

- VERIFIED;
- auction turn order and bargaining order are world/event state, not battle initiative.

Full turn/round lifecycle:

- PARTIAL;
- market clocks do not run on battle rounds.

Full stateful damage pipeline:

- PARTIAL;
- item/stall/property damage is not inferred from combat damage.

Status lifecycle:

- PARTIAL;
- crowding, financial stress, bad food claims or smoke visuals do not create Status.

Terrain/weather/hazards/zones/reactions:

- BLOCKING as a complete family;
- aisles, counters, spills and restricted areas are not automatic field effects.

Move-specific behavior:

- PARTIAL;
- no generic Move-to-commerce interaction is inferred.

Abilities:

- PARTIAL;
- Pickup, Frisk, Super Luck or similar names do not create merchant powers.

Items:

- PARTIAL;
- visible market stock is not battle inventory.

Trainer Features/perks:

- PARTIAL;
- narrative merchant roles do not grant Features.

AI legal-action infrastructure:

- VERIFIED;
- legal choices do not imply market-objective policy.

AI tactical policy:

- BLOCKING;
- needed for evacuation, protected-route and non-KO market goals.

Minecraft/Cobblemon/Craftics adapter/playback:

- BLOCKING;
- needed for reliable market projection and battle handoff.

## 30. No-inference ledger

Pass 106 explicitly prohibits:

- stock exists -> listing exists;
- listing exists -> stock still available;
- display item -> authoritative inventory;
- seller possesses item -> seller owns item;
- ownership -> unrestricted authority to sell;
- low price -> stolen;
- high price -> rare/valuable mechanically;
- repeated buyer -> relationship label;
- failed auction -> rivalry;
- famous vendor -> Skill/Feature bonus;
- merchant role -> Trainer class;
- auction win -> item mechanically usable;
- purchase -> battle inventory;
- market crowd -> initiative/Accuracy penalty;
- stall -> cover;
- aisle -> Rough Terrain;
- item pickup -> custody transfer;
- Pokémon beside vendor -> Pokémon for sale;
- Pokémon transfer discussion -> valid ownership transfer;
- Pokémon species/level/stats -> price;
- Pickup Ability -> free shop stock;
- Frisk -> appraisal authority;
- Super Luck -> auction advantage;
- Pay Day -> general economy generation beyond its exact validated rule;
- a visible chest -> stock count;
- a market session -> random price inflation;
- market closure -> settlement economic collapse.

## 31. Overworld implementation blockers

`MARKET_VENUE_SESSION_STATE`

Persistent venues and recurring session history.

Status: BLOCKING outside battle core.

`VENDOR_PRESENCE_AND_SCHEDULE`

Expected versus actual merchant presence and route-dependent arrival.

Status: BLOCKING outside battle core.

`OFFER_LISTING_AUTHORITY`

Listings linked to real stock/custody/transfer authority.

Status: BLOCKING outside battle core.

`TRANSACTION_HANDOFF_STATE`

Agreement, payment, custody, delivery and provenance as distinct transitions.

Status: BLOCKING outside battle core.

`AUCTION_SESSION_STATE`

Lots, bids, winning state, cancellation and transfer without invented price mechanics.

Status: BLOCKING outside battle core.

`SECONDHAND_PROVENANCE_HANDOFF`

Persistent item identity through resale/consignment.

Status: BLOCKING outside battle core.

`PLAYER_EXCHANGE_CONSENT`

Explicit multiplayer confirmation for irreversible transfers.

Status: BLOCKING outside battle core.

`POKEMON_TRANSFER_AUTHORITY`

Project-authoritative Pokémon custody/ownership/registration/consent contract.

Status: BLOCKING outside battle core.

`MARKET_TO_SUPPLY_CHAIN_HANDOFF`

Offer availability must consume upstream stock state.

Status: BLOCKING outside battle core.

`MARKET_TO_FINANCE_HANDOFF`

Quoted/agreed amounts must not mutate funds outside the finance authority.

Status: BLOCKING outside battle core.

`MARKET_TO_MINECRAFT_PROJECTION`

Visual stalls/listings without duplication or client-owned authority.

Status: BLOCKING.

`MARKET_BATTLE_PERIMETER_HANDOFF`

Freeze combatants/geometry while preserving civilians, stock and transaction state outside BattleSpec.

Status: BLOCKING.

## 32. Canon questions

- Which settlements have permanent markets?
- Which have weekly, seasonal, harbor or traveling markets?
- What currency model does Ouros use?
- Are prices centrally authored, vendor-specific or abstracted?
- Which institutions can run auctions?
- Which goods require provenance or transfer authority checks?
- Are player shops possible?
- Can clubs run stalls or markets?
- How are vendor spaces assigned?
- What records are public?
- How does bargaining work, if at all?
- Which Trainer Features/Skills interact with commerce under PTU/Caelo?
- How are exact Pokémon transfers authorized?
- Are any categories of Pokémon exchange prohibited or institutionally restricted?
- How does the server prevent duplication during a market handoff?
- How much merchant route/session state advances offline?
- Which merchant networks already exist before player arrival?

No answer is promoted to canon by this design file.