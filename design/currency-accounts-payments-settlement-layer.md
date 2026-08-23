# Ouros Currency, Accounts, Payments & Settlement Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already models funding, budgets, grants, sponsorships, markets, auctions, insurance, procurement, digital systems and physical goods. What it did not yet own was the operational transfer of monetary value.

This layer defines the world-state contract for:

- currency and institutional point systems;
- physical cash/token holdings where they exist;
- accounts and balances;
- available versus reserved funds;
- payment instruments;
- merchant acceptance;
- payment instructions;
- authorization;
- holds/reservations;
- settlement;
- receipts/confirmations;
- returns/reversals;
- reconciliation;
- outages and fallback payment methods.

The goal is not a banking simulator. Routine payments should compress. Detailed state appears when timing, custody, institutional access, outages, restricted funds, disputes, multiple media of exchange or player-directed commercial play make the transfer narratively significant.

## Authority boundary

This layer may move or represent value only through authored mechanical/world contracts.

Authority split:

- PTU/Caelo/implementation owns mechanical money values, item prices and any rules-level rewards.
- Finance owns grants, sponsorships, scholarships, prizes, budgets, commitments, receivables/payables and funding restrictions.
- Markets owns listings, negotiation, auctions and agreed commercial terms.
- Supply Chains owns physical stock and freight.
- Material Culture owns physical item identity and provenance.
- Insurance owns coverage decisions and claim/recovery finance.
- Digital Systems owns software/accounts/authentication/logs as information infrastructure.
- Credentials owns authorization/eligibility unrelated to value itself.
- Cases owns allegations/evidence when transfers are disputed.
- Illicit Networks owns evidence-backed clandestine money flows when authored.
- Pokémon Agency owns Pokémon identity/custody/transfer constraints.
- Minecraft/Cobblemon renders terminals, tills, cash objects, receipts and UI but does not own monetary truth.

A payment record must never invent stock, delivery, ownership, legality, market terms, PTU effects or institutional authority.

## 1. Monetary system

A monetary system is a persistent definition of a unit/medium accepted by some set of actors or institutions.

```yaml
monetary_system:
  monetary_system_id: null
  display_name: null
  unit_symbol_ref: null
  system_type: null
  issuer_or_governing_institution_id: null
  mechanical_currency_ref: null
  valid_from: null
  valid_to: null
  denomination_rules_ref: null
  accepted_scope_claim_ids: []
  conversion_service_ids: []
  status: PROPOSED
  canon_reference_ids: []
```

Possible authored types:

- GENERAL_CURRENCY
- INSTITUTIONAL_POINTS
- EVENT_SCRIP
- TRANSIT_STORED_VALUE
- CLUB_CREDIT
- RELIEF_VOUCHER
- MARKET_TOKEN
- OTHER_AUTHORED_MEDIUM

No type is automatically canon.

A secondary point system does not become general money because some merchants accept it.

## 2. Value container

Value can be held in different places/forms.

```yaml
value_container:
  container_id: null
  monetary_system_id: null
  container_type: null
  holder_actor_or_institution_id: null
  custody_actor_or_institution_id: null
  account_id: null
  physical_asset_ref: null
  mechanical_balance_ref: null
  last_reconciled_balance_ref: null
  availability_state: null
  access_policy_ids: []
  history_event_ids: []
```

Candidate container types:

- ON_PERSON_CASH
- SECURE_DEPOSIT
- ACCOUNT_BALANCE
- INSTITUTIONAL_WALLET
- EVENT_TOKEN_HOLDING
- ESCROW_OR_HOLD
- CASHBOX
- CLUB_OR_BUSINESS_TREASURY

Holder, custody and authority remain separate.

A cashier may control a till without owning its funds.

A club treasurer may execute approved payments without owning the club balance.

## 3. Account

An account is a scoped ledger relationship with an operator.

```yaml
financial_account:
  account_id: null
  operator_institution_id: null
  account_type: null
  recognized_holder_ids: []
  authorized_operator_ids: []
  monetary_system_ids: []
  current_balance_refs: []
  reserved_balance_refs: []
  restricted_balance_refs: []
  access_policy_id: null
  service_scope_ids: []
  opened_at: null
  closed_at: null
  current_state: ACTIVE
  statement_record_ids: []
  mechanical_account_ref: null
```

Possible states:

- PENDING_OPEN
- ACTIVE
- LIMITED
- FROZEN
- SERVICE_UNAVAILABLE
- CLOSING
- CLOSED
- ARCHIVED

An account does not imply credit, overdraft, interest, deposit insurance, investment or lending.

Those require separate authored institutions/rules.

## 4. Balance dimensions

One number is insufficient when reservations/restrictions matter.

```yaml
balance_state:
  balance_state_id: null
  account_or_container_id: null
  monetary_system_id: null
  ledger_balance_ref: null
  reserved_amount_ref: null
  restricted_amount_refs: []
  pending_incoming_ref: null
  pending_outgoing_ref: null
  available_amount_ref: null
  as_of_event_id: null
  mechanical_balance_ref: null
```

Do not invent arithmetic independently from the authoritative mechanical balance implementation.

Narrative values can remain symbolic/qualitative when exact balances are unnecessary.

Useful qualitative bands for institutions when mechanics do not need exact numbers:

- EMPTY
- LOW
- ADEQUATE
- COMFORTABLE
- HIGH
- RESTRICTED
- UNRECONCILED

## 5. Payment rail

A payment rail defines how a transfer can be initiated and when it is considered complete.

```yaml
payment_rail:
  payment_rail_id: null
  operator_institution_ids: []
  supported_monetary_system_ids: []
  instrument_type_ids: []
  payer_requirements: []
  payee_requirements: []
  connectivity_dependency_ids: []
  settlement_model_ref: null
  accepted_scope_ids: []
  offline_mode_ref: null
  fallback_rail_ids: []
  service_state: AVAILABLE
  history_event_ids: []
```

Possible rails:

- PHYSICAL_CASH_HANDOFF
- ACCOUNT_TRANSFER
- STORED_VALUE_TERMINAL
- INSTITUTIONAL_LEDGER_TRANSFER
- SIGNED_VOUCHER_REDEMPTION
- EVENT_SCRIP_REDEMPTION
- OTHER_AUTHORED_RAIL

No rail implies a particular modern banking technology.

## 6. Payment instrument

```yaml
payment_instrument:
  instrument_id: null
  instrument_type: null
  issuing_institution_id: null
  owner_or_authorized_user_ids: []
  linked_account_or_container_ids: []
  supported_monetary_system_ids: []
  expiry_time: null
  credential_ref_ids: []
  current_state: ACTIVE
```

Possible types:

- CASH
- TOKEN
- VOUCHER
- STORED_VALUE_CARD
- ACCOUNT_CREDENTIAL
- TERMINAL_AUTHORIZATION
- INSTITUTIONAL_PURCHASE_AUTHORITY

Possessing an instrument is not always equivalent to authority to spend.

A lost credential and the underlying account/permission remain different objects.

## 7. Acceptance profile

A merchant or institution can accept some media/rails and not others.

```yaml
payment_acceptance_profile:
  acceptance_profile_id: null
  actor_or_institution_id: null
  venue_ids: []
  accepted_monetary_system_ids: []
  accepted_rail_ids: []
  minimum_or_maximum_scope_refs: []
  exception_ids: []
  valid_from: null
  valid_to: null
  public_notice_id: null
  current_state: ACTIVE
```

Acceptance is versioned.

Examples:

- a harbor market accepts cash but not institutional points;
- a League venue accepts League credits and ordinary currency;
- an emergency depot accepts relief vouchers during a declared response period;
- a rural merchant accepts only physical cash during a network outage.

Do not infer universal acceptance from one transaction.

## 8. Payment intent and obligation linkage

A payment may originate from a purchase, invoice, prize, grant, refund or other obligation.

```yaml
payment_intent:
  payment_intent_id: null
  payer_id: null
  intended_payee_id: null
  obligation_ref_ids: []
  market_transaction_ref: null
  finance_commitment_ref: null
  insurance_claim_payment_ref: null
  monetary_system_id: null
  amount_ref: null
  selected_rail_id: null
  selected_instrument_id: null
  purpose_ref: null
  created_at: null
  status: CREATED
```

The intent does not move value.

## 9. Payment instruction

```yaml
payment_instruction:
  payment_instruction_id: null
  payment_intent_id: null
  payer_container_id: null
  payee_container_id: null
  amount_ref: null
  monetary_system_id: null
  rail_id: null
  submitted_at: null
  authorization_ref_ids: []
  current_state: SUBMITTED
  failure_reason_claim_id: null
  settlement_event_id: null
```

Suggested states:

- CREATED
- SUBMITTED
- VALIDATING
- AUTHORIZATION_REQUIRED
- AUTHORIZED
- RESERVED
- ACCEPTED
- REJECTED
- SETTLING
- SETTLED
- RETURN_PENDING
- RETURNED
- REVERSED
- CANCELLED
- EXPIRED
- FAILED
- UNRECONCILED

The allowed transition graph belongs to the rail definition.

## 10. Authorization

Authorization answers whether the payer side permits the instruction.

```yaml
payment_authorization:
  authorization_id: null
  payment_instruction_id: null
  authorizing_subject_id: null
  authority_ref_ids: []
  authorization_method_ref: null
  authorized_amount_ref: null
  authorized_at: null
  valid_until: null
  result: APPROVED
  denial_reason_claim_id: null
```

Authorization does not prove settlement.

Authorization does not prove the underlying purchase/contract was legitimate.

## 11. Reservation / hold

Some rails may reserve funds before final settlement.

```yaml
funds_reservation:
  reservation_id: null
  account_or_container_id: null
  payment_instruction_id: null
  amount_ref: null
  created_at: null
  expires_at: null
  current_state: ACTIVE
```

States:

- ACTIVE
- CAPTURED_IN_SETTLEMENT
- RELEASED
- EXPIRED
- CANCELLED

A reservation can reduce available balance without yet creating a settled outgoing transfer.

## 12. Settlement event

```yaml
settlement_event:
  settlement_event_id: null
  payment_instruction_id: null
  rail_id: null
  payer_container_id: null
  payee_container_id: null
  monetary_system_id: null
  amount_ref: null
  settled_at: null
  finality_state: null
  ledger_event_refs: []
  mechanical_transaction_ref: null
  confirmation_record_ids: []
```

Finality states can remain implementation-specific:

- PROVISIONAL
- FINAL_BY_RAIL_RULE
- RETURNABLE_BY_SEPARATE_PROCESS
- UNKNOWN

Do not import real-world legal definitions into Ouros by default.

## 13. Receipt and confirmation

```yaml
payment_receipt:
  receipt_id: null
  payment_instruction_id: null
  issued_by_id: null
  issued_at: null
  receipt_type: null
  represented_state: null
  amount_ref: null
  monetary_system_id: null
  merchant_transaction_ref: null
  verification_ref: null
```

A receipt represents what a system/institution asserted at that moment.

It may represent authorization, acceptance or settlement depending on the rail.

The receipt itself is evidence, not universal world truth.

## 14. Returns, refunds and reversals

Keep these distinct.

```yaml
value_return_event:
  return_event_id: null
  original_payment_instruction_id: null
  return_type: null
  initiated_by_id: null
  amount_ref: null
  reason_claim_id: null
  new_payment_instruction_id: null
  current_state: PENDING
```

Possible types:

- MERCHANT_REFUND
- FAILED_SETTLEMENT_RETURN
- DUPLICATE_PAYMENT_CORRECTION
- OVERPAYMENT_RETURN
- CANCELLED_AUTHORIZATION_RELEASE
- DISPUTE_ADJUSTMENT
- OTHER_AUTHORED_RETURN

A refund is normally a new value movement tied to the original transaction.

Do not rewrite the original settled event to pretend it never occurred.

## 15. Reconciliation

Different systems can temporarily disagree.

```yaml
payment_reconciliation_case:
  reconciliation_case_id: null
  related_payment_instruction_ids: []
  related_account_ids: []
  conflicting_record_ids: []
  opened_at: null
  discrepancy_type: null
  hypotheses: []
  evidence_ids: []
  resolution_event_id: null
  current_state: OPEN
```

Candidate discrepancy types:

- MISSING_CONFIRMATION
- DUPLICATE_DISPLAY
- PENDING_TOO_LONG
- WRONG_ACCOUNT_REFERENCE
- PARTIAL_SETTLEMENT
- CASH_TILL_DIFFERENCE
- OFFLINE_BATCH_NOT_SYNCED
- RETURN_NOT_POSTED
- CURRENCY_OR_MEDIUM_MISMATCH

A discrepancy is not fraud by default.

## 16. Currency/point conversion

Conversions are authored services, not global exchange rates.

```yaml
conversion_service:
  conversion_service_id: null
  operator_institution_id: null
  source_monetary_system_id: null
  destination_monetary_system_id: null
  direction: ONE_WAY
  conversion_rule_revision_ids: []
  access_requirement_ids: []
  valid_from: null
  valid_to: null
  current_state: ACTIVE
```

```yaml
conversion_rule_revision:
  revision_id: null
  conversion_service_id: null
  effective_from: null
  effective_to: null
  rate_or_rule_ref: null
  cap_ref: null
  minimum_ref: null
  provenance_ids: []
```

The rate/rule must come from canon/implementation. The narrative generator may not invent one.

## 17. Physical cash/token path

Physical value uses custody/provenance.

```yaml
physical_value_batch:
  value_batch_id: null
  monetary_system_id: null
  form_type: null
  denomination_refs: []
  quantity_ref: null
  current_custody_id: null
  storage_location_id: null
  authenticity_claim_ids: []
  issue_or_origin_ref: null
  retired_or_invalidated_at: null
```

Most routine cash should not be tracked as individual coins.

Track batches or exact physical instances only when:

- custody matters;
- counterfeit/authenticity is a plot point;
- transport/security matters;
- a historic token is collectible;
- a disaster interrupts access to account systems;
- a unique payment object has provenance value.

## 18. Cashbox / till state

```yaml
cashbox_state:
  cashbox_id: null
  venue_or_service_id: null
  custodian_id: null
  monetary_system_ids: []
  opening_balance_ref: null
  inflow_event_ids: []
  outflow_event_ids: []
  closing_balance_ref: null
  reconciliation_case_id: null
  current_state: OPEN
```

A till difference does not prove employee theft.

Possible explanations include entry error, unposted refund, wrong medium, counting error, delayed batch or actual loss.

## 19. Offline and degraded payment operations

Technology/Communications own outages. This layer owns payment consequences.

```yaml
payment_service_incident:
  incident_id: null
  payment_rail_id: null
  dependency_event_ids: []
  start_time: null
  end_time: null
  affected_scope_ids: []
  unavailable_operation_types: []
  fallback_rail_ids: []
  queued_instruction_ids: []
  reconciliation_required: false
```

A payment outage should create gameplay only when it changes access, timing or obligations.

Routine outages can simply make one method unavailable.

## 20. Emergency/relief payments

Crisis/Finance may authorize temporary value mechanisms.

```yaml
emergency_value_program:
  program_id: null
  authorizing_institution_id: null
  crisis_event_id: null
  monetary_system_or_voucher_id: null
  eligible_actor_or_service_ids: []
  issuance_event_ids: []
  accepted_venue_ids: []
  redemption_deadline: null
  settlement_or_reimbursement_ref: null
  current_state: ACTIVE
```

This supports relief vouchers or temporary offline systems without making them general currency.

## 21. Clubs, parties and shared funds

Shared balances require explicit authority.

```yaml
shared_treasury:
  treasury_id: null
  owner_institution_or_group_id: null
  account_or_container_ids: []
  authorized_spender_ids: []
  approval_rule_ref: null
  purpose_restriction_ids: []
  statement_visibility_policy_id: null
  current_state: ACTIVE
```

A party member cannot spend shared funds merely because they can physically access a chest or terminal.

Irreversible shared-fund operations require server-side authorization and, when authored, multiplayer consent/approval.

## 22. Player privacy

Exact balances are private by default unless mechanics/UI explicitly expose them.

Narrative generation may know only what it is authorized to know.

Do not infer:

- poverty/wealth from clothing;
- account balance from purchases;
- source of funds from possession;
- private debt from a failed payment;
- sponsorship amount from public signage;
- financial dependence from repeated transactions.

## 23. Pokémon guardrails

Pokémon do not become monetary assets through this layer.

Do not model:

- a Pokémon as an account balance;
- ownership transfer as payment settlement;
- a Pokémon as collateral;
- a Pokémon as a stored-value token;
- capture as creation of monetary value;
- Loyalty/Friendship as creditworthiness;
- species rarity as automatic financial value.

If canon later permits fees or compensation around Pokémon care/transport/services, the monetary transfer and Pokémon agency/custody state remain separate.

## 24. Integration with markets

Recommended purchase flow:

```text
listing visible
  -> seller authority validated
  -> buyer accepts terms
  -> stock reservation / item availability validation
  -> payment intent
  -> payment authorization
  -> settlement or approved fallback
  -> item handoff / ownership-custody update
  -> receipt / provenance update
```

A payment can settle and the item handoff can still fail.

The market transaction then remains incomplete/disputed according to Market/Case rules.

## 25. Integration with Finance

Finance may create an obligation such as a prize, grant installment or invoice.

This layer executes value transfer when/if authorized.

Recommended flow:

```text
finance commitment
  -> payment intent
  -> authorization
  -> settlement
  -> finance commitment marked paid/partially paid
```

Finance must not mark a commitment paid solely because an instruction was submitted.

## 26. Integration with Digital Systems

Digital Systems owns:

- account software;
- access logs;
- backups;
- service incidents;
- identity/authentication records.

This layer owns:

- monetary ledger meaning;
- balance changes;
- payment state;
- settlement state;
- reconciliation state.

A restored database backup must not silently duplicate money. Restoration requires reconciliation against authoritative monetary events.

## 27. Chronicle behavior

Record narratively significant events:

- first opening/closure of a payment institution;
- new medium/point system introduced;
- acceptance policy changes;
- major outage;
- failed settlement affecting a project;
- emergency voucher program;
- conversion rule revision;
- lost/returned historic value batch;
- major reconciliation incident;
- public controversy over a payment claim;
- club treasury governance change.

Do not log every routine purchase as a major world event.

## 28. Long-horizon consequences

This layer supports consequences such as:

- a rural settlement remaining cash-heavy because connectivity is unreliable;
- a rail corridor gradually increasing acceptance of one institutional payment rail;
- an old event-scrip token becoming an archive/museum object;
- a club building governance after a disputed shared purchase;
- a storm demonstrating the value of offline fallback payments;
- a market losing customers temporarily because a common payment method is unavailable;
- a regional conversion service being introduced after years of incompatible institutional points.

These changes must come from prior state, not procedural economic noise.

## 29. Encounter contracts

### Settlement Hall Outage — FULL

Premise:

A payment hub loses connectivity during a crowded market session. Some transactions are authorized, some reserved and some unsubmitted. An unrelated Pokémon disturbance blocks access to the backup terminal and staff need the route cleared without treating every pending transaction as lost money.

Full tactical dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including interception/forced movement if staff/crowd routes occur inside battle;
- core calculations;
- action economy/initiative;
- full lifecycle;
- full stateful damage;
- status lifecycle;
- terrain/weather/hazards/zones/reactions only if a real environmental hazard is active;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy for `CLEAR_ROUTE`, `WITHDRAW`, `PROTECT`;
- Minecraft/Cobblemon/Craftics playback.

Reduced version:

Public Space evacuates customers. Technology/Communications marks the primary rail unavailable. Payments already in flight are frozen in their current authoritative states. AutoPTU receives a static safe room/corridor and only the actual combatants. After battle, staff access the backup terminal and reconciliation resumes. Battle victory does not settle any payment by itself.

### Relief Voucher Depot — FULL

Premise:

A crisis has temporarily authorized relief vouchers at a depot. A route disruption creates a crowding problem while wild Pokémon attempt to withdraw through the same area.

Full tactical dependencies:

- complete movement/interception for moving civilians/wild Pokémon;
- AI tactical policy for `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT`;
- environment families only when separately validated;
- adapter/playback for crowds, depot objects and objectives.

Reduced version:

Crisis resolves queue/crowd movement in world state first. Voucher issuance/redemption remains outside battle. If an actual confrontation remains, use a static encounter nearby. Winning does not create voucher eligibility or balances.

### Historic Token Reconciliation — FULL

Premise:

A cache of old market tokens is discovered during building work. Some may still be redeemable under an old institutional promise; others may be collectible but financially invalid. During examination, a Pokémon incident threatens the temporary archive/assessment area.

Full tactical dependencies:

- standard battle families for any confrontation;
- complete movement only if staff/objects move tactically;
- AI tactical policy for protection/withdrawal;
- adapter/playback.

Reduced version:

Archive/Finance secure the tokens and document custody before battle. AutoPTU resolves a separate static threat. Redemption status is determined afterward from historical agreements and payment-system records, not from the battle.

## 30. Hard non-inferences

Do not infer:

- account -> loan availability;
- account -> interest;
- balance -> available balance;
- authorization -> settlement;
- settlement -> item delivery;
- receipt -> final settlement unless the rail defines it;
- pending -> failed;
- failed -> insufficient funds;
- failed -> fraud;
- reversal -> wrongdoing;
- refund -> original transaction erased;
- points -> currency;
- one venue accepts points -> all venues accept them;
- exchange service -> floating market rate;
- displayed terminal value -> authoritative balance;
- chest contents -> financial ledger;
- physical token -> currently valid currency;
- digital outage -> balances lost;
- restored backup -> duplicated funds;
- payment institution -> credit/insurance/investment powers;
- wealth -> reputation/authority/Trainer Level;
- financial hardship -> morale penalty;
- monetary reward -> XP unless PTU/Caelo says so;
- Pokémon possession -> monetary asset;
- Pay Day/Amulet Coin-like mechanics -> general economy rules without validation.

## 31. Implementation blockers outside AutoPTU-Java

- `MONETARY_SYSTEM_REGISTRY`
- `VALUE_CONTAINER_STATE`
- `ACCOUNT_LEDGER_STATE`
- `AVAILABLE_VS_RESERVED_BALANCE_CONTRACT`
- `PAYMENT_RAIL_REGISTRY`
- `PAYMENT_INSTRUMENT_STATE`
- `PAYMENT_ACCEPTANCE_POLICY`
- `PAYMENT_INSTRUCTION_STATE_MACHINE`
- `PAYMENT_AUTHORIZATION_CONTRACT`
- `FUNDS_RESERVATION_STATE`
- `SETTLEMENT_EVENT_LEDGER`
- `PAYMENT_RECEIPT_SEMANTICS`
- `RETURN_REFUND_REVERSAL_STATE`
- `PAYMENT_RECONCILIATION_CASES`
- `CONVERSION_SERVICE_REGISTRY`
- `PHYSICAL_VALUE_CUSTODY`
- `CASHBOX_RECONCILIATION`
- `PAYMENT_OUTAGE_FALLBACK_STATE`
- `EMERGENCY_VALUE_PROGRAM_STATE`
- `SHARED_TREASURY_AUTHORITY`
- `FINANCE_TO_PAYMENT_HANDOFF`
- `MARKET_TO_PAYMENT_HANDOFF`
- `PAYMENT_TO_ITEM_HANDOFF`
- `PAYMENT_TO_DIGITAL_SYSTEM_HANDOFF`
- `PAYMENT_TO_MINECRAFT_PROJECTION`

These belong in world/economy/server architecture, not in the battle core.

## 32. PTU/Caelo mechanical guardrail

Pass 120 does not define:

- currency amounts;
- item prices;
- Pay Day;
- Amulet Coin;
- prize-money formulas;
- capture-related income;
- Trainer Feature income;
- gambling;
- interest/credit/debt mechanics;
- theft or fraud checks;
- bargaining Skill checks;
- conversion rates;
- transaction fees.

Those require project-authoritative PTU/Caelo/implementation evidence or explicit canon/product decisions.

## Design consequence

Ouros can now treat money as persistent world state without requiring economic simulation:

```text
obligation/listing
  -> payment intent
  -> accepted medium/rail
  -> authorization
  -> reservation if required
  -> settlement
  -> confirmation/receipt
  -> physical/service handoff
  -> reconciliation if records disagree
```

The major narrative gain is causal precision. A project can fail because money was never authorized, because settlement stalled, because the wrong medium was offered, because the rail was down, because funds were restricted, or because delivery failed after successful payment. Those are different stories and can now remain different in Chronicle.