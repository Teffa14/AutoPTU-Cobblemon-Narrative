# Auctions, Consignment & Secondary-Market Continuity Extension

Status: proposed systems design. Not established Ouros canon.
Date: 2026-08-28

## Purpose

Ouros already tracks persistent objects, provenance, ownership/custody references, finance, storefronts, procurement, courier movement, public notices, temporary events, collections and found property.

This extension handles a narrower lifecycle: an already-existing object or group of objects is deliberately offered for secondary exchange through a listing, consignment or auction, inspected by possible counterparties, awarded or negotiated, and then handed back to the systems that own payment and transfer.

This layer is useful when the exchange itself creates persistent story state.

Routine purchases from ordinary stock remain Storefront behavior and should usually compress.

## 1. Authority boundaries

Material Culture owns:
- exact `item_instance` identity;
- provenance;
- maker/source history;
- current owner/custodian references;
- significance and repair history.

Finance owns:
- mechanical balance references;
- payment commitments/events;
- sponsorship or institutional funding;
- financial risk when explicitly authored.

Storefront owns:
- recurring commercial service availability;
- ordinary public stock surfaces;
- normal customer-facing service state.

Procurement owns:
- institutional sourcing needs;
- specifications;
- supplier selection;
- purchase-order/commission fulfillment.

Courier owns:
- intentional shipment after or before exchange when transport is needed.

Found Property owns:
- ordinary recovered objects separated from their holder without an intended transfer.

Archives/Collections own:
- accession/deaccession policy;
- collection custody;
- conservation/access rules.

Case/Authority owns:
- formal fraud, theft, evidence, prohibited access or other authored investigations.

This extension owns only:
- offer/consignment representation;
- lot/listing composition;
- published description/version;
- viewing/inspection access events;
- offer/bid records;
- selection/adjudication event;
- withdrawal/no-sale state;
- closeout handoff.

## 2. Secondary-market venue

```yaml
secondary_market_venue:
  venue_id: null
  location_id: null
  operator_actor_ids: []
  operator_institution_id: null
  service_node_ref: null
  event_instance_refs: []
  exchange_modes: []
  public_schedule_claim_ref: null
  access_policy_ref: null
  current_state: OPERATING
  catalogue_cycle_refs: []
  active_lot_ids: []
  history_event_ids: []
  canon_refs: []
```

Candidate modes:
- FIXED_LISTING
- NEGOTIATED_LISTING
- SEALED_OFFER
- LIVE_AUCTION
- SPECIALIST_MARKET_DAY
- INSTITUTIONAL_DISPOSAL

These labels describe authored world procedures. They do not create universal law or mechanical pricing rules.

## 3. Consignment case

```yaml
consignment_case:
  consignment_id: null
  represented_item_instance_ids: []
  represented_batch_ids: []
  consignor_id: null
  claimed_owner_ids: []
  current_custodian_id: null
  venue_id: null
  intake_event_id: null
  authority_basis_ref: null
  seller_claim_ids: []
  provenance_refs: []
  condition_observation_refs: []
  reserve_or_minimum_claim_ref: null
  listing_or_lot_ids: []
  withdrawal_event_id: null
  closeout_event_id: null
  state: INTAKE_PENDING
```

Suggested states:
- INTAKE_PENDING
- REPRESENTATION_REVIEW
- ACCEPTED
- CATALOGUED
- OPEN_FOR_VIEWING
- OPEN_FOR_OFFERS
- AWARDED_PENDING_CLOSE
- SOLD_PENDING_TRANSFER
- CLOSED_TRANSFERRED
- WITHDRAWN
- NO_SALE
- PAUSED_PROVENANCE_REVIEW
- REFERRED_TO_CASE
- RETURN_PENDING

The consignor is not automatically the owner.

A venue accepting an object into custody does not become its owner.

## 4. Market lot

```yaml
market_lot:
  lot_id: null
  venue_id: null
  consignment_ids: []
  item_instance_ids: []
  batch_ids: []
  lot_title_claim: null
  catalogue_description_id: null
  quantity_or_composition_ref: null
  viewing_access_ref: null
  opening_or_asking_value_ref: null
  offer_window_ref: null
  adjudication_method_ref: null
  current_state: ANNOUNCED
  selected_offer_id: null
  closeout_ref: null
```

Suggested states:
- ANNOUNCED
- VIEWING
- OPEN
- PAUSED
- AWARDED
- NO_SALE
- WITHDRAWN
- CLOSED

A lot is a transaction grouping. It does not replace the identities of its component objects.

## 5. Catalogue description with provenance

```yaml
catalogue_description:
  catalogue_description_id: null
  lot_id: null
  revision: 1
  authored_by_ref: null
  published_at: null
  public_descriptor_claims: []
  attribution_claim_ids: []
  provenance_claim_ids: []
  condition_claim_ids: []
  mechanical_item_refs: []
  uncertainty_notes: []
  supersedes_id: null
  source_refs: []
```

Hard rule:
A catalogue description is an information packet. It can be wrong, incomplete or superseded.

The description must not silently overwrite Material Culture provenance or canonical truth.

## 6. Viewing and inspection

```yaml
market_viewing_event:
  viewing_event_id: null
  lot_id: null
  viewer_ids: []
  access_scope_ref: null
  observed_descriptor_ids: []
  observed_condition_refs: []
  documentation_seen_refs: []
  questions_asked_claim_ids: []
  answers_received_claim_ids: []
  world_time: null
```

Viewing can reveal information already perceptible or disclosed.

It does not automatically reveal:
- private provenance;
- hidden defects;
- exact mechanical item internals;
- owner identity when protected;
- authenticity;
- future value;
- secret contents.

If a PTU Skill/Feature is used for an inspection, exact mechanical support requires source review.

## 7. Offer/bid record

```yaml
market_offer:
  offer_id: null
  lot_id: null
  offeror_id: null
  represented_principal_id: null
  offer_type: BID
  amount_ref: null
  submitted_at: null
  authorization_ref: null
  condition_claim_ids: []
  funding_ref: null
  current_state: ACTIVE
  supersedes_offer_id: null
```

Suggested types:
- BID
- FIXED_PRICE_ACCEPTANCE
- NEGOTIATED_OFFER
- INSTITUTIONAL_OFFER
- PROXY_BID

Suggested states:
- ACTIVE
- OUTBID
- WITHDRAWN
- REJECTED
- SELECTED
- EXPIRED
- INVALIDATED

Narrative records never mutate mechanical balances directly.

## 8. Proxy or principal representation

```yaml
market_purchase_mandate:
  mandate_id: null
  principal_id: null
  representative_id: null
  venue_or_lot_scope_refs: []
  amount_limit_ref: null
  condition_refs: []
  effective_from: null
  expires_at: null
  revocation_event_id: null
  source_document_refs: []
```

This allows a character to bid for an institution, family, expedition or another actor without inferring personal ownership.

## 9. Award is separate from completion

```yaml
market_award_event:
  award_event_id: null
  lot_id: null
  selected_offer_id: null
  selected_offeror_id: null
  selected_principal_id: null
  awarded_at: null
  adjudication_basis_ref: null
  pending_payment_ref: null
  pending_transfer_refs: []
  state: AWARDED_PENDING_CLOSE
```

Winning/selection establishes only that the offer was chosen under the authored market procedure.

It does not prove:
- payment completed;
- object was delivered;
- ownership legally changed;
- the object was authentic;
- no later dispute exists.

## 10. Closeout handoff

```yaml
market_closeout:
  closeout_id: null
  lot_id: null
  award_event_id: null
  payment_event_refs: []
  custody_transfer_refs: []
  ownership_transfer_ref: null
  shipment_ref: null
  provenance_event_refs: []
  unsold_return_ref: null
  public_result_claim_ref: null
  completed_at: null
  state: PENDING
```

Possible states:
- PENDING
- PAYMENT_PENDING
- TRANSFER_PENDING
- SHIPMENT_PENDING
- COMPLETED
- FAILED_TO_CLOSE
- DISPUTED
- RETURNING

The actual owner/custodian state must be updated by the appropriate authoritative object/transaction layer.

## 11. Withdrawal and no-sale

```yaml
market_withdrawal_event:
  withdrawal_id: null
  lot_id: null
  initiated_by_ref: null
  authority_basis_ref: null
  reason_claim_ids: []
  affected_offer_ids: []
  return_custody_ref: null
  world_time: null
```

A lot can leave the market without changing ownership.

The system must preserve the fact that it was publicly offered if that was already observed.

## 12. Provenance discrepancy review

```yaml
market_provenance_review:
  review_id: null
  lot_id: null
  trigger_observation_refs: []
  catalogue_claim_refs: []
  material_culture_refs: []
  archive_refs: []
  found_property_refs: []
  case_refs: []
  current_assessment: UNRESOLVED
  action: PAUSE
  revision_event_refs: []
```

Candidate assessments:
- UNRESOLVED
- DESCRIPTION_OUTDATED
- ATTRIBUTION_UNCERTAIN
- PROVENANCE_INCOMPLETE
- CATALOGUE_ERROR_CONFIRMED
- REFERRED_FOR_FORMAL_INVESTIGATION
- CLEARED_FOR_CONTINUED_OFFER

No hidden authenticity score is introduced.

## 13. Market memory

```yaml
market_history_event:
  event_id: null
  venue_id: null
  lot_id: null
  event_type: null
  public_claim_refs: []
  participant_refs: []
  world_time: null
  public_memory_ref: null
```

Candidate event types:
- CATALOGUE_PUBLISHED
- VIEWING_OPENED
- LOT_WITHDRAWN
- LOT_AWARDED
- NO_SALE
- CLOSE_COMPLETED
- CATALOGUE_CORRECTED
- PROVENANCE_REVIEW_OPENED
- OBJECT_REAPPEARED

Past results may influence expectations and dialogue. They never create a universal market-price oracle.

## 14. Character and faction use

This layer can support recurring roles without making them automatically trustworthy or corrupt:
- auctioneer;
- catalogue writer;
- conservator/condition specialist;
- collector;
- institutional buyer;
- seller/consignor;
- proxy bidder;
- courier/handler;
- researcher following provenance;
- regular spectator;
- specialist dealer;
- community representative deciding whether an object should remain local.

Competing institutions can disagree over whether an acquisition is worth scarce resources. The disagreement can be financial, historical, scientific, cultural or operational without becoming villainy.

## 15. Relationship to public events

An auction may be:
- an ordinary recurring service;
- a specialist market day;
- one activity inside a festival;
- a charity/fundraising event when Finance establishes the funding agreement;
- an institutional disposal event;
- a temporary sale attached to relocation or closure.

Temporary Event Operations owns crowd/service readiness. This extension owns lots and exchange state.

## 16. Pokémon boundary

Pokémon are actors, not generic `item_instance` lots.

This extension must never create a market lot whose semantic object is a Pokémon merely because a game, server or Cobblemon addon supports buying/selling Pokémon.

Any transfer of Pokémon association, custody or ownership must go through the Pokémon Agency system and governing PTU/Caelo/Ouros decisions.

## 17. Cobblemon/Minecraft integration

Strong SAFE_REUSE candidates:
- blocks, stalls, containers and decorative displays;
- item models/icons where legally available;
- signs/books/lecterns;
- NPC/Pokémon models and animations used as presentation;
- particles, sounds and ambience;
- UI screens and client widgets through reviewed adapter code;
- networking and synchronization primitives;
- persistent identifiers/storage hooks where they do not establish narrative authority.

ADAPTER_REQUIRED:
- mapping persistent Ouros `item_instance`/lot identity to displayed Minecraft objects;
- opening catalogue/offer UI from a world interaction;
- synchronizing published lot state;
- applying reviewed closeout changes after authoritative transaction state changes.

FORBIDDEN AUTHORITY:
- Minecraft inventory proximity deciding ownership;
- Cobblemon trade state silently deciding Ouros provenance;
- Cobblemon nearby entities becoming market participants automatically;
- any Cobblemon `BattleState`/participant/controller logic deciding market or combat truth.

When a market scene creates a battle:
`Ouros market/world state -> explicit encounter composition -> AutoPTU -> adapter -> Minecraft/Cobblemon presentation`.

## 18. Encounter profile — Auction Hall Evacuation

Narrative premise:
A disruption occurs while a viewing/auction is underway. Visitors, staff and persistent lots must be removed or secured before the venue can be assessed.

Intended full version:
- civilians withdraw through several routes;
- some routes may become blocked;
- protected market lots remain world objects, not HP targets unless a future reviewed object-interaction system exists;
- combatants may use Intercept/forced movement where legal;
- AI understands withdrawal/route-control priorities;
- adapter presents authoritative positions and state.

Capability dependencies:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions when dynamic access/hazards matter;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version:
- venue staff evacuate visitors before BattleSpec creation;
- lots are secured outside tactical targeting;
- unstable/blocked areas become fixed world-state exclusions before battle;
- Ouros selects exact combatants;
- AutoPTU runs a reviewed static arena;
- after resolution, Event Operations/Facility/Market state determines reopening and custody.

Winning does not complete an auction or transfer a lot.

## 19. Encounter profile — Consignment Transfer Interruption

Narrative premise:
A significant sold or consigned object is being moved between venue, custodian and recipient when a hostile encounter interrupts the route.

Intended full version:
- transfer party has a movement objective;
- protected noncombatant/cargo state persists;
- Intercept and forced movement may matter;
- terrain/weather may matter when the route genuinely has those mechanical effects;
- AI can pursue withdrawal, route denial or escape rather than only KO.

Full capability dependencies match Auction Hall Evacuation, especially complete movement, terrain/zones/reactions, tactical AI and adapter/playback.

Reduced version:
- transfer stops before battle;
- staff/cargo move to a world-state safe location outside the grid;
- combat occurs on a static legal arena;
- afterward Courier/Market/Material Culture decide whether transfer resumes, reroutes or remains paused.

A battle result never authenticates the object or completes ownership transfer.

## 20. Noncombat encounter profile — Catalogue Provenance Review

Premise:
A familiar object appears in a catalogue with a history that conflicts with an archive, repair record, old photograph or prior owner claim.

Current executable form:
- inspect catalogue revisions;
- compare source lineage;
- query actor knowledge;
- locate prior custody/provenance events;
- preserve contradictions;
- pause or continue the listing according to authored authority.

This can run without battle mechanics.

Potential mechanical dependencies only arise if PTU Skills/Features are explicitly invoked, and those must be reviewed before use.

## 21. Revisit loop

A persistent venue can support:
1. baseline market day and regular actors;
2. first memorable lot;
3. later provenance correction or failed close;
4. return of an old participant in a different role;
5. institutional acquisition changing a museum/workshop/public site;
6. a formerly unsold object resurfacing elsewhere;
7. public expectations changing after a controversial but legitimate sale;
8. updated procedures that become visible in the venue.

The venue accumulates history without needing a hidden market-level stat.

## 22. Anti-false-completion rules

- A bid does not transfer money.
- Winning does not prove payment.
- Payment does not prove delivery.
- Delivery/custody does not prove ownership.
- A catalogue statement does not prove authenticity.
- A high offer does not establish objective value.
- A low offer does not establish worthlessness.
- A prior sale price does not bind a later transaction.
- A consignor is not automatically the owner.
- A venue is not automatically a legal authority.
- Public interest does not create ownership.
- Winning a battle does not award the lot.
- Minecraft pickup state does not decide any of the above.

## 23. Canon status

Everything introduced here is PROPOSED systems design.

No Ouros settlement is established as having an auction house. No fee, price method, ownership rule, currency policy, appraisal profession, collector institution, deaccession practice, proxy-bidding rule or market custom becomes canon through this extension.
