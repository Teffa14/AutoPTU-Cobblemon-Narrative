# Engine Readiness Snapshot — Pass 120

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU were inspected read-only.

## Live heads inspected

AutoPTU-Java `main`: `5d9e5069fa0c68432825a48be25fff6ba245d305`

Newest relevant Java evidence remains the Pass 119 status/Ability slice:

- status application uses declarative Ability prevention;
- `RuntimeCombatantState` owns Ability-suppression state;
- suppression is respected by the status-application boundary;
- tests cover Inner Focus -> Flinch, Immunity -> Poison/Badly Poisoned, Insomnia -> Sleep and Vital Spirit -> Sleep;
- suppression cases prove that disabling the Ability disables that prevention path;
- this is representative coverage only and does not complete the status controller or Ability catalog.

AutoPTU `main`: `743b0ff76c63d8ab2131fbf8de4e2e2430b9eea4`

Newest visible Python changes are Career/service recovery work. The recent sequence adds and narrows recovery for an impossible exhausted decision phase, including the stale `2-of-1` style state, and preserves a pre-battle rollback checkpoint. This is valuable Career resilience but does not promote any permanent tactical capability category.

## Java README evidence

The live Java README still lists major work as incomplete:

- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature registries;
- semantic full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Java remains intended to own authoritative PTU battle behavior. Minecraft/Cobblemon/Craftics should adapt world state and render events rather than duplicate PTU rules.

## Permanent capability categories

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No permanent category is promoted in Pass 120.

## Why currency/payments are outside the battle core

Nothing inspected in Java or Python establishes authoritative overworld systems for:

- currency registries;
- bank/deposit institutions;
- account balances;
- available versus reserved funds;
- payment instruments;
- merchant acceptance;
- payment authorization;
- payment settlement/finality;
- returns/refunds/reversals;
- payment reconciliation;
- conversion services;
- physical-cash custody;
- club/shared treasuries;
- payment-network outages;
- relief-voucher programs.

These belong to persistent world/economy/server state.

AutoPTU should receive only already-authoritative battle inventories/resources when a battle begins. A market payment, account transfer or payment outage must never change battle legality unless a separately validated mechanical item/resource state was actually transferred into the combatant's authoritative loadout before battle.

## Pass 120 encounter dependency map

### Settlement Hall Outage — FULL

Narrative objective:

Clear a route to a backup payment terminal during a market-session outage while keeping evacuated staff/civilians safe and preserving the exact pre-existing state of pending payments.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for moving staff/crowd lanes
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only if a validated tactical hazard exists
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `CLEAR_ROUTE`, `WITHDRAW`, `PROTECT`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Public Space evacuates customers. Technology/Communications marks the primary rail unavailable. The payment layer freezes each instruction in its actual state (`AUTHORIZED`, `RESERVED`, `SETTLING`, etc.). AutoPTU receives a static safe room/corridor and only actual combatants. After battle, reconciliation resumes. Battle victory never changes payment state directly.

### Relief Voucher Depot — FULL

Narrative objective:

Maintain a crisis distribution point where eligible actors receive/redeem temporary relief vouchers while evacuees and wild Pokémon need safe passage through the same area.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED if combat occurs
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING for true crossing/evacuation objectives
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only when the crisis environment creates a validated tactical effect
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Crisis resolves queue movement, eligibility and wildlife displacement in world state before battle. Voucher balances and redemption remain outside AutoPTU. If a confrontation remains, use a conventional static encounter nearby. Winning cannot create voucher eligibility or payment value.

### Historic Token Reconciliation — FULL

Narrative objective:

Protect a cache of historic market tokens and assessors while an unrelated Pokémon incident occurs, then determine afterward which tokens are artifacts, invalid old value or still redeemable under an authored promise.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING only if staff/token containers become moving tactical objectives
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only if a real environmental hazard exists
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `PROTECT`, `WITHDRAW`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Archive/Finance secures the token cache and custody record before battle. AutoPTU resolves a static threat. Redemption/authenticity/value questions are handled afterward by Archives, Finance, Material Culture and the payment layer. Combat cannot decide historical validity.

## New overworld blockers introduced by Pass 120

These belong outside AutoPTU-Java:

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

## Hard non-inferences for Pass 120

Do not infer:

- account balance -> spendable balance;
- account -> credit/loan service;
- authorization -> settlement;
- settlement -> item/service delivery;
- receipt -> final settlement unless defined by the rail;
- pending -> failed;
- failed -> insufficient funds;
- failed/reversed payment -> fraud;
- digital outage -> lost balances;
- backup restore -> duplicated money;
- institutional points -> ordinary currency;
- acceptance at one venue -> universal acceptance;
- conversion service -> floating exchange market;
- chest/terminal display -> monetary truth;
- market price -> PTU mechanical price unless validated;
- wealth -> Trainer Level, Skill, Feature, reputation or social authority;
- payment state -> combat modifier;
- historic token -> valid current currency;
- Pokémon -> collateral/value container;
- Pay Day/Amulet Coin flavor -> general economy rules.

## PTU/Caelo validation state

Public PTU 1.05 Core material confirms that mechanical starting money and purchase availability are campaign/GM/rules concerns. It does not, from the material validated in Pass 120, establish a complete bank/account/payment system.

The project’s full primary Caelo Core/Player/encounter/character-creation corpus was not recoverable from the narrative repository/GitHub sources available in this run.

Super PTU Online Helper was not exposed as an invocable capability.

Pass 120 therefore does not validate or invent:

- banking Features;
- interest;
- credit/debt;
- account fees;
- exchange rates;
- taxes;
- prize-money formulas;
- Pay Day;
- Amulet Coin;
- bargaining/payment Skill checks;
- monetary theft/fraud procedures;
- transaction fees;
- payment-based XP/reputation.

## Design consequence

The narrative/economy server can now preserve a value-transfer chain independently from battle rules:

```text
obligation or market agreement
    -> payment intent
    -> accepted medium / rail
    -> authorization
    -> reservation if required
    -> settlement
    -> confirmation / receipt
    -> physical/service handoff
    -> reconciliation when records disagree
```

This lets Ouros distinguish financial and logistical failures without forcing Minecraft to simulate banking and without making AutoPTU responsible for anything beyond already-authoritative battle resources.