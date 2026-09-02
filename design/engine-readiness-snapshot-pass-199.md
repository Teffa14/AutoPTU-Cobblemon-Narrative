# Engine Readiness Snapshot — Pass 199

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-02
Narrative head before pass: `85be9ea8cdb4457036ac13c185a348a1577411a8`

Read-only engines inspected:
- AutoPTU-Java head: `dd8097910da62f98d07047cd0603fa8d858f4c67`
- AutoPTU head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

## Live engine delta

No engine head changed since pass 198.

AutoPTU-Java remains on `dd8097910da62f98d07047cd0603fa8d858f4c67` (`Add forced movement prevention semantic event adapter (#322)`). The evidence remains narrowly scoped to semantic projection for an already-resolved Insectoid Utility / Wallclimber forced-movement prevention path.

AutoPTU remains on `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, a presentation-only viewport-resize synchronization change that explicitly does not alter battle rules or outcomes.

No permanent battle capability category is promoted in pass 199.

## Permanent capability classification

### VERIFIED within currently audited contracts

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

`VERIFIED` remains scoped to audited contracts. It does not claim exhaustive combinatorial coverage.

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING when the complete family is required

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Why complete movement remains PARTIAL

Current Java evidence does not close the complete matrix across:
- Push;
- Pull;
- Knockback;
- Interception;
- collisions;
- partial stops;
- chained displacement;
- footprint interactions during displacement;
- reaction ordering;
- terrain-mediated displacement;
- all combinations with Moves;
- all combinations with Abilities;
- all combinations with Items;
- all combinations with Trainer Features;
- statuses and temporary effects;
- semantic-event parity for every path.

A representative prevention path cannot stand in for the whole category.

## AutoPTU campaign-shop evidence

Pass 199 additionally inspected the read-only AutoPTU Python campaign layer.

`auto_ptu/rules/campaign_commands.py` currently exposes:
- `shop.create`;
- `shop.buy`;
- `shop.sell`.

Observed `shop.buy` behavior includes:
- shop lookup;
- current-location requirement;
- stock quantity validation;
- Trainer currency validation;
- currency subtraction;
- Trainer inventory increment;
- shop stock decrement;
- deterministic event payload including cost and remaining Trainer currency.

Observed `shop.sell` behavior includes:
- Trainer inventory validation;
- removal from Trainer inventory;
- currency addition;
- increase of shop stock;
- a resale calculation based on half the shop stock price in this current implementation.

This is useful live evidence for one AutoPTU Python campaign transaction path.

It does not establish:
- Caelo compatibility of those prices;
- Java parity;
- transaction provenance;
- unique item-instance transfer;
- auctions;
- reservations;
- deposits;
- delivery;
- taxes;
- credit;
- bargaining;
- ownership law;
- refunds;
- regional economic simulation.

Therefore pass 199 treats the Python shop command as an authoritative mechanical reference candidate only where the project explicitly adopts that campaign path. Narrative records must link to its output rather than independently recalculate currency or inventory.

Search of AutoPTU-Java for shop/buy/sell/currency/inventory/price returned no indexed implementation evidence during this pass. No Java commerce capability is declared.

## Pass 199 narrative-mechanics boundary

Pass 199 adds proposed Narrative records for:
- market actors;
- stock claims;
- lots;
- offers;
- quotes and revisions;
- price observations;
- reservations;
- agreements;
- governed consideration/payment references;
- transfer events;
- pickup/delivery fulfillment;
- substitutions;
- reversals/corrections when separately authorized.

Narrative does not become the price or currency engine.

Required separation:

```text
NARRATIVE_AGREEMENT_RECORDED
  !=
MECHANICAL_PURCHASE_EXECUTED
```

and:

```text
MECHANICAL_INVENTORY_CHANGED
  !=
ALL_OWNERSHIP_OR_DELIVERY_QUESTIONS_RESOLVED
```

The first protects PTU/AutoPTU authority. The second preserves custody/provenance and unresolved Ouros law.

## PTU cross-check

Public PTU 1.05 references verify that:
- Trainers use money and items;
- item purchase availability is a GM/setting decision;
- the rules corpus provides example prices and NPC service availability.

Pass 199 therefore cannot derive PTU prices from narrative scarcity, relationship state or world importance.

Community PTU discussions show substantial variation in campaign reward economies. This supports configurability but has no rules authority.

## Caelo uncertainty

The Narrative README identifies Caelo Player's Guide, Caelo rulebook/errata, character-creation material and regional source material as authoritative project inputs.

A fresh literal `Caelo` search across Narrative, AutoPTU-Java and AutoPTU returned no indexed source file during this pass.

Pass 07 previously recorded Caelo shop/market/buy/crafting surfaces, but pass 199 does not treat that older summary as enough live evidence to establish exact rules.

Currently unresolved:
- retained Caelo currency conventions;
- exact local item prices;
- buy/sell ratios;
- shop commands intended for Ouros;
- bargaining rules;
- taxes;
- credit/debt;
- deposits;
- refunds/cancellations;
- auction rules;
- institutional purchasing powers;
- ownership-transfer doctrine.

## Pass 199 rich encounter

Encounter: `Shortfall Delivery at Glass Bend`.

Narrative premise:
A shipment linked to an already-recorded Bruma Market transaction is moving through Sendero del Vidrio. A localized wild confrontation threatens immediate passage.

The shipment's commercial facts exist outside BattleSpec.

### Full intended dependency matrix

- targeting/footprints/range/LoS: VERIFIED within audited contracts
- base movement legality: VERIFIED within audited contracts
- complete movement: PARTIAL; required when escort geometry, Interception, Push, Pull, Knockback, forced movement, collision or displacement protection matters
- core calculations: VERIFIED within audited contracts
- action economy/initiative: VERIFIED within audited contracts
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL when selected content uses statuses
- terrain/weather/hazards/zones/reactions: BLOCKING when route surface, weather, protected zones, reactions or hazards have tactical consequences
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL when battle Items participate
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED within audited contracts
- AI tactical policy: BLOCKING when wild actors must prioritize retreat, territory, cargo avoidance, corridor pressure or another non-KO objective
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for faithful world -> battle -> world projection

Disposition: FULL RICH VERSION BLOCKED.

## Reduced encounter contract

The narrative premise can run without the blocking tactical families.

Narrative retains:
- transaction agreement;
- lot identity;
- buyer/seller/provider refs;
- shipment provenance;
- cargo custody;
- fulfillment destination;
- noncombatants;
- delay state;
- Thin Delivery Season evidence state.

Before combat:
- move cargo to a safe semantic state outside BattleSpec;
- withdraw noncombatants;
- identify one immediate threat still preventing passage;
- select only audited combatants/content;
- use stable battle geometry;
- omit unverified tactical weather, hazards, zones and objective reactions;
- avoid forced-movement objectives unless every selected interaction has a live contract.

Allowed narrow handoffs:
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_PASSAGE_CLEAR`
- `IMMEDIATE_DELIVERY_TEAM_CAN_WITHDRAW`

Battle output cannot determine:
- price;
- payment completion;
- ownership;
- whether the delivered goods satisfy the agreement;
- shortage cause;
- future stock;
- vendor trust;
- liability;
- regional economic conditions;
- Thin Delivery Season truth.

Disposition: REDUCIBLE USING AUDITED BASIC BATTLE CONTENT.

## AI tactical-policy caution

Legal-action infrastructure does not prove objective-aware market-route behavior.

A rich delivery encounter could require an AI actor to:
- retreat when a corridor opens;
- avoid damaging cargo;
- defend territory rather than chase a KO;
- stop pressure after withdrawal;
- prioritize blocking movement;
- preserve distance from noncombatants.

These are tactical-policy requirements and remain blocking until verified by live tests/contracts.

## Adapter/playback caution

Transaction continuity adds another reason the adapter must not treat presentation as authority.

Required boundaries include:
- visible stall stock != authoritative stock unless explicitly linked;
- Minecraft item pickup != purchase completion;
- duplicated client entity != duplicated lot;
- sign destruction != offer cancellation;
- render-distance disappearance != vendor closure;
- chunk unload != reservation expiry;
- chest contents != regional supply level;
- battle playback result != payment event;
- cargo model destroyed client-side != provenance destroyed;
- UI confirmation != mechanical currency mutation unless linked to the authoritative command result.

The complete Minecraft/Cobblemon/Craftics family remains BLOCKING.

## Narrative repository state for this pass

Pass 199 writes only to Narrative.

New files:
- `research/2026-09-02-market-offer-quote-transaction-continuity-scan-199.md`
- `design/market-offer-quote-transaction-continuity-layer.md`
- `proposals/2026-09-02-marea-market-offer-transaction-seeds-199.md`
- `design/engine-readiness-snapshot-pass-199.md`

No AutoPTU-Java or AutoPTU write is authorized or performed.

## Implementation recommendation

Prototype `Ivo's Quote, Tomorrow's Delivery` first.

It needs:
- no battle;
- no new NPC;
- no new institution;
- no invented currency;
- no dynamic pricing;
- no ownership law;
- no new item mechanics.

It validates quote versioning, substitution, actual-lot provenance and off-screen purchasing continuity while strengthening the canonical Thin Delivery Season evidence model without resolving its cause.