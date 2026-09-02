# Ouros Market Offer, Quote & Transaction Continuity Layer

Status: PROPOSED SYSTEMS DESIGN. Not established canon.
Pass: 199
Date: 2026-09-02

## Purpose

This layer gives Ouros a durable record for concrete market exchanges without turning the setting into a full economic simulator.

It extends the existing material-culture/economy layer and service-request/capacity layer. Those systems already model goods, provenance, workshops, supply routes, scarcity, commissions and service queues. This layer covers the transactional seam between a specific available thing and a completed exchange.

Core chain:

`stock/lot evidence -> offer -> quote revision -> reservation -> agreement -> governed consideration -> transfer -> pickup/delivery -> provenance`

The chain is intentionally decomposed. A market board, conversation, UI click, Minecraft item pickup and mechanical inventory mutation should not all collapse into one event.

## Authority model

Three authorities must remain separate.

### Narrative/world authority

Narrative owns:
- who made an offer;
- where and when it was made;
- what stock/lot the offer claimed to concern;
- quote history and supersession;
- reservation history;
- pickup/delivery history;
- transaction provenance;
- attributed claims about shortage, value or scarcity;
- NPC knowledge and later callbacks.

### PTU/Caelo/AutoPTU mechanical authority

The governing mechanical layer owns any executable rule for:
- Trainer currency;
- item stacks/inventory;
- authoritative PTU item prices when adopted;
- resale values;
- item effects;
- item use legality;
- mechanical acquisition/removal;
- any Feature, Edge or service effect attached to a transaction.

### Minecraft/Cobblemon presentation authority

The adapter may display:
- vendor NPCs;
- stalls;
- boards;
- crates;
- stock models;
- pickup points;
- receipts/messages;
- transaction UI.

These surfaces project authoritative state. They do not independently create stock, money, ownership, purchase completion or item effects.

## 1. Market actor

```yaml
market_actor:
  market_actor_id: null
  actor_or_institution_id: null
  location_id: null
  role_tags: []
  current_presence_state: null
  current_service_refs: []
  supply_relationship_refs: []
  public_contact_refs: []
  canon_status: null
```

Role tags may include VENDOR, BUYER, PURCHASING_LEAD, COOPERATIVE_REPRESENTATIVE, TEMPORARY_TRADER or INSTITUTIONAL_REQUESTER.

Tags organize orchestration only. They create no legal powers.

## 2. Stock record versus stock claim

A stock record should distinguish authoritative inventory known to a governed system from what an actor or board says is available.

```yaml
stock_record:
  stock_record_id: null
  holder_or_market_id: null
  mechanical_item_ref: null
  material_batch_refs: []
  item_instance_refs: []
  quantity_or_band: null
  location_id: null
  provenance_refs: []
  authoritative_source_ref: null
  observed_at: null
```

```yaml
stock_claim:
  stock_claim_id: null
  claimant_id: null
  market_or_location_id: null
  item_or_scope_ref: null
  claimed_quantity_or_band: null
  source_ref: null
  issued_at: null
  valid_until: null
  superseded_by: null
  confidence: null
```

A sign saying `available today` is evidence of a claim. It does not create the physical stock.

## 3. Lot

A lot binds a specific quantity or batch to one potential exchange context.

```yaml
market_lot:
  lot_id: null
  seller_or_holder_id: null
  item_or_batch_refs: []
  quantity_scope: null
  provenance_refs: []
  location_id: null
  available_from: null
  available_until: null
  disposition_state: AVAILABLE
  governing_mechanics_refs: []
```

Suggested narrative states:
- AVAILABLE
- RESERVED
- AGREED
- TRANSFER_PENDING
- TRANSFERRED
- WITHDRAWN
- EXPIRED
- UNAVAILABLE

The state names are implementation proposals, not legal terminology.

## 4. Market offer

```yaml
market_offer:
  offer_id: null
  issuer_id: null
  audience_scope: null
  lot_or_service_ref: null
  offered_terms_ref: null
  issued_at: null
  valid_until: null
  publication_or_message_ref: null
  status: OPEN
  superseded_by: null
```

An offer can be:
- public on a board;
- directed to one buyer;
- tied to a temporary visitor;
- attached to a specific incoming shipment;
- institution-only;
- provisional pending stock confirmation.

Narrative should record the actual scope rather than assuming every visible offer is open to everyone.

## 5. Quote and revision chain

```yaml
price_quote:
  quote_id: null
  offer_id: null
  issuer_id: null
  recipient_id: null
  lot_or_service_ref: null
  price_or_consideration_ref: null
  quantity_scope: null
  substitution_terms: []
  issued_at: null
  valid_until: null
  source_message_ref: null
  revision_of: null
  superseded_by: null
  mechanics_validation_state: PENDING
```

Narrative may store an amount emitted by an approved mechanical/shop system or authored canon source. It must not calculate a new PTU price merely because supply changed.

A new quote preserves the old quote.

## 6. Price observation

A quote or completed sale may be useful as evidence without becoming a global price table.

```yaml
price_observation:
  observation_id: null
  observed_amount_ref: null
  item_or_scope_ref: null
  quantity_scope: null
  actor_or_market_id: null
  location_id: null
  observed_at: null
  transaction_or_quote_ref: null
  conditions: []
  provenance_ref: null
```

Examples of legitimate later questions:
- Was the same supplier quoting a different amount two weeks earlier?
- Did one vendor preserve an old posted figure after receiving a revised notice?
- Was the quote for the same quantity and grade?
- Did a visitor report a different rate somewhere else?

The system should answer from records rather than manufacture an economic explanation.

## 7. Reservation

```yaml
market_reservation:
  reservation_id: null
  lot_or_scope_ref: null
  requester_id: null
  accepted_by_id: null
  created_at: null
  expires_at: null
  quantity_scope: null
  deposit_or_consideration_ref: null
  status: HELD
  release_reason_ref: null
```

Suggested states:
- REQUESTED
- HELD
- PARTIALLY_HELD
- RELEASED
- EXPIRED
- CONVERTED_TO_AGREEMENT
- CANCELLED

Reservation state does not itself grant custody or inventory.

## 8. Agreement record

```yaml
transaction_agreement:
  agreement_id: null
  seller_or_provider_id: null
  buyer_or_recipient_id: null
  lot_or_service_ref: null
  accepted_quote_ref: null
  accepted_quantity_scope: null
  accepted_substitution_refs: []
  agreement_time: null
  mechanics_validation_ref: null
  consideration_state: null
  transfer_state: PENDING
  source_refs: []
```

This is the narrative record that both sides accepted a particular version of the terms.

It does not override the mechanical engine if the purchase is illegal or cannot be executed.

## 9. Consideration/payment record

```yaml
consideration_record:
  consideration_id: null
  agreement_id: null
  payer_or_provider_id: null
  recipient_id: null
  governed_currency_or_asset_ref: null
  governed_amount_ref: null
  mechanical_event_ref: null
  recorded_at: null
  state: PENDING
```

Possible states:
- PENDING
- AUTHORIZED
- COMPLETED
- FAILED
- REVERSED
- DISPUTED_CLAIM

For ordinary PTU purchases, the actual currency mutation should come from the authoritative mechanical command. Narrative stores the link and context.

Narrative cannot mint money or assume a currency denomination.

## 10. Transfer event

```yaml
transaction_transfer:
  transfer_id: null
  agreement_id: null
  lot_or_item_refs: []
  from_actor_or_holder_id: null
  to_actor_or_holder_id: null
  physical_custody_changed: false
  ownership_claim_changed: false
  authoritative_inventory_event_ref: null
  location_id: null
  occurred_at: null
  delivery_or_pickup_ref: null
  provenance_event_ref: null
```

Because regional ownership doctrine remains unresolved, `ownership_claim_changed` records the system's transaction claim. It should not silently decide disputed legal ownership.

## 11. Pickup and delivery

```yaml
transaction_fulfillment:
  fulfillment_id: null
  agreement_id: null
  mode: PICKUP
  source_location_id: null
  destination_location_id: null
  responsible_actor_ids: []
  custody_chain_refs: []
  expected_at: null
  actual_at: null
  status: PENDING
  exception_refs: []
```

Suggested modes:
- PICKUP
- LOCAL_DELIVERY
- ROUTE_DELIVERY
- INSTITUTIONAL_HANDOFF

This connects to correspondence, transport, custody and service-capacity layers.

## 12. Substitution

```yaml
transaction_substitution:
  substitution_id: null
  original_scope_ref: null
  proposed_scope_ref: null
  proposer_id: null
  reason_claim_refs: []
  proposed_at: null
  decision_actor_id: null
  decision_state: PENDING
  decided_at: null
  governing_mechanics_refs: []
```

Suggested states:
- PENDING
- ACCEPTED
- DECLINED
- EXPIRED
- SUPERSEDED

A shortage can motivate a substitution proposal. The substitution remains a decision with provenance.

For Ivo, this supports the canonical principle that preserving local dishes and accepting substitutes are different judgments. It does not invent recipe mechanics.

## 13. Reversal, refund or correction candidate

Ouros does not yet have canonical consumer law. The architecture can still preserve that an exchange was reversed or corrected when an authoritative system or authored scenario says so.

```yaml
transaction_reversal:
  reversal_id: null
  original_agreement_id: null
  authoritative_basis_ref: null
  initiated_by_id: null
  mechanical_reversal_event_ref: null
  custody_return_refs: []
  occurred_at: null
  notes_claim_refs: []
```

No automatic refund rule is defined here.

## 14. Thin Delivery Season integration

Market data can become evidence for the canonical open question.

Useful evidence:
- quote revisions;
- smaller delivered lots;
- changed delivery dates;
- substitutions;
- unavailable lots;
- differences between posted and received quantities;
- supplier statements;
- repeated observations across time.

Forbidden inference:
A higher observed quote, lower stock, substitution or delayed delivery does not establish a cause by itself.

Narrative should preserve competing explanations and source attribution.

## 15. Off-screen ordinary commerce

The world may conduct routine exchanges without the player present when all required authoritative state exists.

Compression requirements:
- named actors or institutions have a plausible role;
- required stock/lot state exists;
- governing mechanical transfer can legally occur or the transaction remains narrative-only where no mechanical item is involved;
- important provenance is written;
- exceptional substitutions or disputed claims remain inspectable;
- no hidden transaction is used to manufacture a desired plot outcome.

Player absence does not freeze Ivo's ordinary purchasing work.

## 16. Minecraft/Cobblemon mapping

Safe projections include:
- price/availability boards generated from current offer records;
- crates linked to shipment/lot ids;
- stall displays reflecting current availability bands;
- vendor dialogue showing a current quote version;
- receipt or note items linked to transaction records;
- pickup markers for already authorized fulfillment;
- visual empty spaces after actual stock exhaustion.

Hard boundaries:
- breaking a display does not cancel an offer;
- copying a display item does not duplicate stock;
- picking up a decorative Minecraft entity does not complete a purchase;
- despawn does not reverse a transfer;
- chunk unload does not expire a reservation unless authoritative world time actually crosses its expiry;
- a container count is not population-scale market truth unless that container is the designated authoritative inventory projection;
- UI success cannot bypass PTU/AutoPTU currency/inventory validation.

## 17. Integration with pass 07

Pass 07 remains owner of:
- item instance provenance;
- material batches;
- workshops;
- production actions;
- commissions;
- supply routes;
- broad market state;
- scarcity events.

Pass 199 adds event-level transaction continuity.

A completed transfer should write a pass-07 provenance event rather than create a competing item-history system.

## 18. Integration with pass 198

Service request and market transaction can coexist.

Example:
- Teo receives a repair request under pass 198;
- a replacement part is needed;
- Ivo or Teo obtains a quote under pass 199;
- the part is purchased through authoritative mechanics;
- its lot/provenance is linked to the work order;
- completion remains a service-work event, not a market event.

## 19. Integration with correspondence and visitor layers

A quote can arrive by courier or message. Delivery of the quote does not mean acceptance.

A temporary visitor can issue an offer. Departure can expire practical access while preserving the historical quote.

A repeat visitor can return with different stock without resetting relationship history.

## 20. Mechanical boundaries

Narrative must never infer:
- PTU item value from scarcity tags;
- purchase legality from visible stock alone;
- resale percentage from main-series Pokémon games;
- a haggling bonus from Charm or social state without an authoritative rule;
- item mechanical quality from price;
- ownership from physical possession alone;
- shop access from player proximity alone;
- a transaction reward from a battle result unless explicitly authored and mechanically valid.

## 21. Battle-aware transaction encounter pattern

### Full concept: Shortfall Delivery at Glass Bend

Premise:
A documented shipment tied to a legitimate Bruma Market transaction is returning through Sendero del Vidrio. A localized wild confrontation threatens immediate passage. Cargo provenance and commercial terms already exist before the battle.

If the full encounter uses escort geometry, cargo positions, interception, forced movement, terrain, reactions or objective-aware wild behavior, dependencies are:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle where selected content requires it;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

The full form remains unavailable while required families are partial/blocking.

### Reduced concept

Keep shipment, cargo custody, commercial terms, buyer/seller obligations and noncombatants under Narrative world state.

Move noncombatants and cargo to a safe semantic state before BattleSpec creation. If one immediate wild threat still blocks passage, compile one ordinary audited battle on stable geometry using content already supported by the engine.

Allowed narrow handoffs:
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_PASSAGE_CLEAR`
- `IMMEDIATE_DELIVERY_TEAM_CAN_WITHDRAW`

Battle output cannot decide:
- price;
- ownership;
- whether payment occurred;
- whether goods match the agreement;
- shortage cause;
- future supply;
- vendor trust;
- legal liability;
- Thin Delivery Season truth.

## 22. Generation rules

1. Use concrete actors, stock evidence and source records.
2. Keep offers versioned.
3. Preserve expired/superseded quotes as history.
4. Link mechanical currency/inventory mutations instead of duplicating them.
5. Keep possession, custody and ownership claims distinct where disputes matter.
6. Never turn one observed amount into a regional market index.
7. Let substitutions preserve the original request.
8. Keep scarcity causal but uncertain until evidence supports an explanation.
9. Avoid price micromanagement for routine purchases.
10. Compress ordinary transactions unless a decision, relationship, shortage, provenance issue or logistics dependency makes the exchange narratively meaningful.
11. Never create economic crime from mere anomaly.
12. Do not let market scenes become mandatory fetch quests.
13. Do not create new currencies or transaction law before Caelo/Ouros review.

## 23. Canon status

CANON-APPROVED inputs used by this layer:
- Puerto Bruma and Bruma Market Hall exist;
- Loma Clara Producers Cooperative exists;
- Thin Delivery Season facts and uncertainty;
- Ivo Serrat's purchasing role;
- existing Marea locations/institutions/NPC identities.

PROPOSED:
- all schemas in this file;
- transaction state names;
- quote/reservation workflow;
- fulfillment model;
- price-observation model;
- reduced encounter handoff names.

UNRESOLVED:
- Caelo currency and prices retained by Ouros;
- ownership doctrine;
- taxes;
- credit;
- deposits;
- cancellation/refund rules;
- auctions;
- bargaining;
- shop licensing;
- institutional purchasing authority;
- Java transaction support;
- adapter mapping for transaction UI and physical stock.