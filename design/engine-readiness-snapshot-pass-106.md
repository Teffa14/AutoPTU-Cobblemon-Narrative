# Engine Readiness Snapshot — Pass 106

Status: implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Live evidence inspected

AutoPTU-Java head observed during Pass 106:

`1ac0eab794f2179297c5d32575e9c82746556a9f`

Latest relevant commit:

`Port generic Trainer Feature usage bookkeeping (#141)`

This slice adds a Python-parity primitive for Trainer Feature usage/cooldown mutation after a Feature effect has actually applied.

The Java contract now records/mutates, for the Feature usage map:

- total uses;
- last round used;
- uses in the current round;
- actor-specific uses in the current round where applicable;
- cooldown-until state from declared cooldown values.

The implementation comment explicitly states that the resolver runs only after an effect has applied and deliberately excludes:

- target/effect semantics;
- resource consumption;
- AP.

This follows the recent generic Trainer Feature sequence:

- #137 — prerequisite gates;
- #138 — context gates;
- #139 — frequency/cooldown gates;
- #140 — resource availability/consumption primitive;
- #141 — usage/cooldown bookkeeping mutation.

This is substantial generic infrastructure progress, but it still does not prove complete Feature dispatch, target scopes, AP integration, effect application or the concrete Trainer Feature catalog.

The #141 parity workflow pins Python AutoPTU commit:

`16d228efa63aabecb67fa788959a359aac7f8f03`

for the Trainer Feature usage contract.

Current AutoPTU repository head observed separately during Pass 106:

`7030e158f8a4e1c30814a3b682a585e0320d2475`

Its newest visible change hardens Career persistence around corrupt decision-bond data. That is relevant to product persistence but does not justify a tactical capability promotion.

The AutoPTU-Java README still states that Python remains authoritative while the port is incomplete and continues to list major unfinished work including:

- core combatant/grid battle state expansion;
- full damage resolution;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full semantic transcript parity;
- tactical AI scoring/policy;
- Minecraft/Cobblemon adapter.

## Permanent capability map

### VERIFIED

#### targeting / footprints / range / LoS

Remains VERIFIED for static battle geometry, footprints, anchors, range and geometric LoS.

Pass 106 non-inference:

- a market stall is not a combatant;
- a displayed item is not a legal target;
- an auction lot is not an objective entity unless BattleSpec explicitly models it;
- a counter does not create cover automatically;
- a merchant standing behind a counter does not change LoS rules;
- a crowd is not targetable geometry by default;
- market signage has no tactical effect.

#### base movement legality

Remains VERIFIED for established Shift/Jump and known movement-mode legality.

Pass 106 non-inference:

- pushing a market cart is not base Shift;
- carrying an auction lot is not a movement mode;
- moving through a crowded aisle has no new cost automatically;
- stalls do not create Rough Terrain;
- merchant convoys are not combatants with base movement rules;
- civilians do not gain autonomous pathfinding from this category.

#### core calculations

Remains VERIFIED for established PTU calculation primitives.

Pass 106 adds no:

- bargaining calculation;
- appraisal formula;
- market value formula;
- dynamic price formula;
- auction budget formula;
- merchant reputation modifier;
- rarity score;
- provenance bonus;
- resale multiplier;
- Pokémon valuation formula.

#### action economy / initiative

Remains VERIFIED.

Pass 106 non-inference:

- auction bid order is not battle initiative;
- negotiation turns are not battle rounds;
- buying or selling does not consume a Standard/Shift/Swift battle action unless an exact implemented battle rule says so;
- market priority does not grant initiative priority;
- seller/buyer order has no combat meaning;
- transaction completion cannot be driven by initiative progression.

#### AI legal-action infrastructure

Legal `BattleChoice` generation remains VERIFIED.

It still does not prove tactical policy for:

- EVACUATE_MARKET;
- PROTECT_EXIT;
- AVOID_CIVILIANS;
- WITHDRAW_FROM_STALLS;
- CLEAR_ROUTE;
- PROTECT_MERCHANTS;
- DISENGAGE_AFTER_ACCESS;
- AVOID_SENSITIVE_LOTS;
- SEPARATE_WILDLIFE_FROM_CROWD;
- PRESERVE_PROVENANCE_OBJECTS.

Those require AI tactical policy.

### PARTIAL

#### full turn / round lifecycle

Still PARTIAL.

Existing evidence covers meaningful slices of phase ordering, round cleanup, initiative rollover, delayed hits, temporary effects, declared actions, Trainer AP/action resets and Trainer Feature gate/order infrastructure.

Pass 106 adds stronger Trainer Feature usage bookkeeping evidence, not complete lifecycle coverage.

Market sessions, offer validity, auction windows and merchant routes are world clocks, not battle rounds.

#### full stateful damage pipeline

Still PARTIAL.

Representative authoritative damage and hook slices exist, but complete damage remains unfinished per Java README.

Pass 106 non-inference:

- broken stall -> HP damage;
- dropped auction lot -> damage roll;
- damaged packaging -> mechanical Item damage;
- frightened crowd -> damage modifier;
- expensive object -> increased damage;
- market fire visual -> Burn damage;
- shattered display -> area damage.

Property/material condition remains world state unless a specific battle mechanic exists.

#### status lifecycle

Still PARTIAL.

Market state does not create PTU Status conditions.

No automatic mapping exists for:

- crowding -> Slowed;
- panic -> Fear;
- negotiation pressure -> Confused;
- bad food claim -> Poisoned;
- smoke visual -> Poisoned;
- carrying stock -> Slowed;
- losing an auction -> Enraged;
- market noise -> Distracted/Accuracy penalty.

#### move-specific behavior

Still PARTIAL.

Pass 106 adds no evidence for commerce-specific Move behavior.

A Move name/flavor cannot be repurposed as:

- appraisal;
- theft detection;
- bargaining;
- cargo manipulation;
- instant delivery;
- auction interruption;
- ownership transfer.

Any object manipulation must be validated against the exact Move implementation and then handed back to world-state authority.

#### abilities

Still PARTIAL.

Pass 106 explicitly prohibits flavor inference such as:

- Pickup -> free market stock or legal ownership;
- Frisk -> appraisal/authenticity authority;
- Super Luck -> auction advantage;
- Pickup -> theft detection;
- Honey Gather -> automatic sellable Honey production;
- Harvest -> retail restocking;
- Pickup/Thief/Magician -> ownership transfer outside exact battle rules.

Representative Ability hooks do not prove these world interactions.

#### items

Still PARTIAL.

A mechanical Item type and a market item instance are different layers.

Pass 106 rules:

- visible stock is not battle inventory;
- a completed market transaction is not sufficient by itself to project an Item into BattleSpec;
- secondhand provenance does not modify mechanical stats;
- an auction lot is not mechanically usable until it maps to an implemented Item and is legally held by the actor;
- a unique narrative object may have no mechanical Item representation at all.

#### Trainer Features / perks

Still PARTIAL, with stronger generic infrastructure evidence at Java head `1ac0eab...`.

Recent parity primitives now cover:

- prerequisites;
- context gates;
- frequency/cooldown eligibility;
- declared resource availability/consumption;
- usage/cooldown bookkeeping after an effect applies.

This is meaningful progress toward a generic dispatcher boundary.

The family remains PARTIAL because the latest code itself preserves separate responsibilities for effect semantics, targeting, AP and resource coupling, and because concrete Feature behavior remains incomplete across the catalog.

Pass 106 non-inference:

- merchant profession -> Trainer Feature;
- shopkeeper -> Skill rank;
- auctioneer -> Command/Guile bonus;
- market reputation -> Feature prerequisite;
- currency -> Feature resource automatically;
- purchasing an item -> Feature usage;
- store restock -> Feature cooldown;
- vendor schedule -> frequency gate;
- bargaining -> Feature effect;
- listing an item -> Feature target scope.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

Still BLOCKING as a complete family.

Pass 106 full-version impact:

- no moving merchant convoy inside battle;
- no civilian evacuation paths inside battle;
- no cart/lot interception;
- no escorting a seller through a live grid;
- no crowd displacement;
- no moving stall boundaries;
- no forced movement around market obstacles;
- no in-grid wildlife withdrawal through crowds.

Reduced encounters must move/abstract noncombatants and commercial objects before BattleSpec freezes.

#### terrain / weather / hazards / zones / reactions

Still BLOCKING as a complete family.

Pass 106 non-inference:

- stall aisle -> terrain;
- wet market floor -> slippery hazard;
- market awning -> Weather protection mechanic;
- restricted lot area -> protected tactical zone;
- smoke from cooking -> smoke hazard;
- dropped produce -> Rough Terrain;
- live electrical vendor equipment -> hazard;
- crowd barrier -> reaction zone;
- market closure -> field effect.

Existing field-state lifecycle primitives do not prove full environment behavior.

#### AI tactical policy

Still BLOCKING.

Market encounters frequently need non-KO policies:

- evacuate;
- withdraw;
- protect an exit;
- clear a route;
- avoid civilians;
- disengage once access is restored;
- prevent wildlife/crowd contact;
- preserve sensitive objects;
- avoid fighting around fragile lots.

Legal-choice generation alone cannot select these goals reliably.

#### Minecraft / Cobblemon / Craftics adapter and playback

Still BLOCKING.

No verified end-to-end authority contract yet exists for:

- market session -> NPC/stall projection;
- vendor presence -> loaded representative actors;
- offer listing -> signs/UI without stale authority;
- authoritative stock -> display-only Minecraft items;
- transaction -> custody-safe item transfer;
- player trade -> consent-safe handoff;
- Pokémon transfer -> persistent entity ownership/consent handoff;
- auction lot -> persistent instance without duplication;
- server correction -> loaded/unloaded market chunks;
- battle perimeter -> crowd/stall abstraction;
- battle transcript -> post-market consequence playback;
- visible container -> non-authoritative inventory projection.

## Pass 106 specific overworld blockers

### MARKET_VENUE_SESSION_STATE

Persistent venue identity plus recurring session history and actual operating windows.

Status: BLOCKING outside battle core.

### VENDOR_PRESENCE_AND_SCHEDULE

Expected versus actual merchant attendance linked to real routes/services.

Status: BLOCKING outside battle core.

### OFFER_LISTING_AUTHORITY

A listing must reference real stock, custody and transfer authority without duplicating the subject.

Status: BLOCKING outside battle core.

### OFFER_AVAILABILITY_VALIDATION

Server-side validation against reservations, quality holds, restrictions and mechanical Item support.

Status: BLOCKING outside battle core.

### TRANSACTION_HANDOFF_STATE

Agreement, payment, custody, physical handoff, delivery and provenance updates remain distinct.

Status: BLOCKING outside battle core.

### AUCTION_SESSION_STATE

Auctions, lots, eligibility, bid records, cancellation and resulting transactions without an invented economy model.

Status: BLOCKING outside battle core.

### SECONDHAND_PROVENANCE_HANDOFF

Stable item-instance identity through resale and consignment.

Status: BLOCKING outside battle core.

### PLAYER_EXCHANGE_CONSENT

Explicit multiplayer acceptance for irreversible item/currency transfers.

Status: BLOCKING outside battle core.

### POKEMON_TRANSFER_AUTHORITY

Persistent Pokémon identity, custody/ownership/registration and participant consent before any market-related transfer.

Status: BLOCKING outside battle core.

### MARKET_TO_SUPPLY_CHAIN_HANDOFF

Market offers consume stock truth rather than creating it.

Status: BLOCKING outside battle core.

### MARKET_TO_FINANCE_HANDOFF

Quoted/agreed price state cannot spend or create funds itself.

Status: BLOCKING outside battle core.

### MARKET_TO_MINECRAFT_PROJECTION

Representative stalls, signs, displayed goods and NPCs without client-owned inventory truth or duplication.

Status: BLOCKING.

### MARKET_BATTLE_PERIMETER_HANDOFF

Move civilians/commercial objects out of tactical authority, freeze legal geometry/combatants and resume market state from transcript aftermath.

Status: BLOCKING.

## Encounter readiness

### Auction Hall Evacuation

FULL:

Requires complete movement for moving civilians/lots where modeled, AI tactical policy for evacuation/protection, adapter/playback and environment family only when a validated tactical hazard exists.

Current state: BLOCKED at full fidelity.

REDUCED:

Evacuate before battle, keep lots off-grid under custody, freeze a static hall/perimeter and pause the auction.

Current state: narratively viable using verified static geometry and whatever implemented PARTIAL combat rules the chosen combatants require.

### Traveling Market Chokepoint

FULL:

Requires moving-objective/interception support, objective-aware AI, adapter/playback and optional validated route environment.

Current state: BLOCKED at full fidelity.

REDUCED:

Merchants/stock remain outside BattleSpec. AutoPTU resolves a static chokepoint battle. Travel and Market systems then decide whether arrival still occurs.

Current state: viable as reduced orchestration.

### Night Market Wildlife Spillover

FULL:

Requires complete movement for crowd/wildlife withdrawal, tactical AI for non-KO separation goals and adapter/playback. Environment family only when actual authored mechanics apply.

Current state: BLOCKED.

REDUCED:

Redirect crowds and most wildlife first. Only actual remaining combatants enter a static battle. Market session and ecology update afterward.

Current state: viable without inventing crowd or withdrawal mechanics.

## Market-specific no-inference ledger

Pass 106 explicitly prohibits:

- `stock exists` -> `listing exists`;
- `listing exists` -> `still available`;
- `displayed` -> `owned by seller`;
- `possessed` -> `authorized to sell`;
- `low price` -> `stolen`;
- `high price` -> `rare mechanically`;
- `auction bid` -> `wealth identity`;
- `auction loss` -> `rivalry`;
- `repeat customer` -> `friendship`;
- `vendor` -> `Trainer Feature`;
- `market reputation` -> `mechanical bonus`;
- `visible stock` -> `battle inventory`;
- `transaction completed` -> `mechanical item supported`;
- `market crowd` -> `combat penalty`;
- `stall` -> `cover`;
- `aisle` -> `terrain`;
- `Pickup` -> `free stock`;
- `Frisk` -> `appraisal`;
- `Super Luck` -> `auction advantage`;
- `Pokémon at stall` -> `Pokémon for sale`;
- `Pokémon transfer discussed` -> `ownership transferred`;
- `species/level/stats` -> `Pokémon price`;
- `Minecraft item entity` -> `custody truth`;
- `Minecraft chest count` -> `inventory truth`.

## Canon/mechanical questions still unresolved

- What currency model does Ouros use?
- Are exact prices globally authored, vendor-specific or abstracted?
- Which settlements have permanent versus recurring markets?
- Which institutions can operate auctions?
- What constitutes valid sale/consignment authority?
- Which goods require provenance checks?
- Can players operate stalls or shops?
- How are player-to-player exchanges confirmed?
- What is the exact Pokémon transfer/ownership/registration contract?
- Which PTU/Caelo Skills or Trainer Features affect commerce, appraisal or negotiation?
- What are the exact buying/selling rules for mechanical Items?
- How does an acquired world Item become available in battle inventory?
- Which goods can be resold?
- How are stale listings corrected in multiplayer?
- How much market/merchant-route state advances offline?
- How does Minecraft represent displayed stock without duplication?

The full primary Caelo corpus was not reliably retrievable during this runtime, so no new Caelo commerce rule is asserted in Pass 106.

Super PTU Online Helper was not exposed as an invocable capability. No output is attributed to it.