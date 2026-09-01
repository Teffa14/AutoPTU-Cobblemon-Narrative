# Marea provisioning, stock, and replenishment seeds

Status: PROPOSED / NON-CANON
Date: 2026-09-01
Pass: 185

These candidates use only already canonized Marea residents, workplaces, route anchors, and ordinary responsibilities. They do not canonize quantities, shortages, policies, suppliers, recipes, PTU Item effects, or new institutions.

## One Coil Short

Teo prepares a routine repair and discovers that the shelf count overstates usable stock. One piece is already reserved, one may be damaged, and the physical count does not match the usable count.

Player loop: inspect labels and condition, compare issue notes, identify which quantity is genuinely allocatable, and help Teo decide whether the work proceeds, waits, or uses an approved substitute.

Useful consequence: the repair may be delayed without theft, sabotage, or villainy. Later the same missing capacity can affect another mundane task.

Battle dependency: none.

## Mirador Field Kit Checkout

Ema prepares a field kit for a scheduled transect. The manifest says the kit is complete, but one reusable component was returned to the wrong rack after an earlier job.

Player loop: reconcile the manifest with physical objects, locate custody history, update the return record, and perform a final condition check.

Nerea can review the observation protocol without becoming the automatic custodian of every item.

Battle dependency: none.

## Restock Arrived, Inspection Pending

A delivery reaches the ferry landing and is recorded by Lia, but the destination cannot treat the entire shipment as usable yet. Packaging damage or an unresolved count means intake remains open.

Player loop: distinguish ARRIVED from ACCEPTED, preserve the delivery record, route the questionable portion for review, and let unaffected stock enter normal use.

This is a good first physical crate implementation because it exercises server authority without requiring a new economy.

Battle dependency: none.

## Ferry Priority Crate

Two legitimate requests compete for a limited unloading window or a limited shipment. Lia can verify what arrived and when; Brin or another authorized role can speak to allocation within established scope. The story centers on conflicting obligations rather than hidden villains.

Possible outcomes include partial issue to both requests, one request waiting for the next delivery, or a compatible substitute being approved for one purpose.

Battle dependency: none.

## Brin's Reserve Shelf

The cooperative storehouse has stock visible on a shelf, but part of it is reserved for an already approved dispatch. A player request cannot consume the reserve merely because the object exists in front of them.

The seed tests `PHYSICAL_STOCK != AVAILABLE_STOCK` and `KNOWN_LOCATION != AUTHORIZED_ACCESS` with an ordinary conversation and ledger check.

Battle dependency: none.

## The Substitute That Almost Fits

Teo or Ivo proposes a substitute for a requested material. It is suitable for one use but its suitability for the actual request is uncertain.

For Teo, this can be a mundane fixture or component. For Ivo, it can be an ingredient or packaging substitution. Exact recipes and mechanical crafting remain outside the proposal until sourced.

The player gathers compatibility evidence rather than rolling a generic crafting check.

Battle dependency: none unless a future PTU mechanical Item becomes involved, in which case Items and any relevant Features require exact parity review.

## Borrowed From Tomorrow

After an earlier incident or drill, a reserve was legitimately used. The immediate problem ended, but the restock never completed. A later ordinary job exposes the depleted reserve.

This connects preparedness aftermath to provisioning continuity. The earlier drawdown remains valid; the current shortage is a consequence rather than evidence of wrongdoing.

Battle dependency: none in the seed itself.

## Upper Bend Cache

A physical cache or old storage point near a route segment is discovered during ordinary work. Its existence, age, contents, current ownership, inspection status, and authorization are all uncertain.

The player can document and secure it without opening every container or taking objects. If it belongs to a superseded plan, preparedness history can explain why it exists while provisioning decides whether any content is still usable.

Battle dependency: none.

## Field School Packing Block

Jo teaches a practical session about checking a manifest, separating required from optional supplies, recording borrowed equipment, and returning it in usable condition.

This creates a player-facing tutorial for the provisioning UI without inventing a `Preparedness` statistic or granting PTU Mentor/Trainer Features.

Battle dependency: none.

## The Crate With Two Destinations

A crate label, dispatch note, and later correction do not agree. Lia can establish where it arrived. Brin can compare cooperative dispatch records. Pia/Taro may preserve the document versions if the discrepancy becomes historically relevant.

The solution may be a stale label rather than a dramatic diversion.

Battle dependency: none.

## What Marea Keeps in Reserve

Longer-term arc candidate. Over several ordinary jobs, the player learns that reserve capacity is distributed across institutions and purposes. A ferry delay, field kit issue, repair shortage, kitchen substitution, and preparedness drawdown can all leave small traces in later stories.

The arc should never collapse into a single global `Marea Supplies` meter. Each shortage, allocation and recovery retains location, purpose, evidence, responsible role, and time.

No crisis is required. The payoff is continuity: decisions made during an earlier week visibly constrain or enable work later.

## Mechanically rich candidate: Last Crate at Upper Bend

Narrative premise: a limited resupply is needed for later work on an upper route segment. During movement toward the site, wild activity interrupts the route. The logistical problem matters before and after combat.

Full intended version can include a carrier, workers, a narrow corridor, contested movement, protective positioning, route hazards, and a wild actor whose behavior may shift during the encounter.

Required capability families for that full version:

- targeting/footprints/range/LoS: required
- base movement legality: required
- complete movement including push/pull/knockback/interception/forced movement: required if interception, displacement, collision, partial stops, or forced retreat are represented
- core calculations: required
- action economy/initiative: required
- full turn/round lifecycle: required
- full stateful damage pipeline: required
- status lifecycle: required according to audited roster/content
- terrain/weather/hazards/zones/reactions: required if the route itself affects tactics
- move-specific behavior: required and roster-audited
- abilities: required and roster-audited
- items: required only for actual tactical Items; logistical cargo stays outside BattleSpec
- Trainer Features/perks: required if selected Trainers use them
- AI legal-action infrastructure: required
- AI tactical policy: required for escort/protection/withdrawal intent
- Minecraft/Cobblemon/Craftics adapter/playback support: required for faithful live presentation

Full-version readiness: BLOCKED under the live evidence snapshot for pass 185.

Reduced version: the carrier, workers, crate, route allocation and custody remain authoritative world state outside combat. Everyone moves to a safe holding location before BattleSpec. If a wild threat blocks further travel, a separate audited battle occurs on stable terrain. No dynamic cargo objective, civilian escort, weather phase, route hazard, or unsupported forced-movement interaction enters the tactical state.

Allowed battle outcomes are narrow: `IMMEDIATE_PATH_CLEAR` or `IMMEDIATE_WILD_THREAT_WITHDREW`. Narrative retains authority over shipment condition, delivery acceptance, allocation, repair readiness, and future replenishment.

## Promotion questions

Before any seed becomes canon, confirm which resident or role may allocate each stock class; whether quantities should be simulated exactly or in operational units; how ownership and custody records connect; what ordinary supply routes exist beyond the already canonized ferry/storehouse relationships; whether any standardized field kits exist; what PTU Items can legitimately appear in those kits; and whether Caelo source material defines relevant commerce, crafting, supply, expedition, or item-access rules.