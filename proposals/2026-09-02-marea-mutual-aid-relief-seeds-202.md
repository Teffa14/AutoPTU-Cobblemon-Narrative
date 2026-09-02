# Marea Mutual Aid & Relief Seeds — Pass 202

Status: PROPOSALS / NOT CANON.
Date: 2026-09-02

These candidates reuse current Marea people, places and institutions. They do not establish welfare law, insurance, taxes, compulsory charity, reputation points or new mechanical rewards.

## 1. The Shared Cart Repair

A cooperative cart used for ordinary movement needs a repair. Teo can do the work, but one component and one usable work window come from different existing dependencies.

Useful consequence: the cart returns to service and later deliveries can reference its repair history.

Recommended first implementation slice.

## 2. Two Kitchens, One Preserved Lot

Ivo learns that one preserved ingredient lot is available while another expected delivery is delayed. A temporary redistribution can cover one meal plan without proving a district-wide shortage.

The receiving kitchen does not incur an automatic debt or relationship change.

## 3. Crates Back Before the Next Dispatch

Brin needs reusable containers returned before a later cooperative dispatch. A resident who previously borrowed them can return all, some or none by the relevant window.

This is a custody/logistics problem rather than a morality meter.

## 4. The Offered Room Is No Longer Needed

A temporary boarding-room offer is made during a ferry disruption. Before arrival, the original visitor finds another valid arrangement. The offer can be redirected or released without treating either party as unreliable.

## 5. Oren's Non-Medical Support List

A care case creates ordinary support needs around governed treatment: meal delivery, transport coordination or a quiet pickup window. Oren can identify the logistical need while all healing effects remain PTU-owned.

## 6. A Later Berth for the Same Cargo

Lia cannot create dock capacity, but she can identify a later unloading window. The aid consists of coordination, not a magical priority override.

## 7. The Component Someone Already Promised Elsewhere

Teo believes a repair part may be available. Provenance shows it is already reserved for another legitimate job. The aid offer must be corrected before allocation.

This tests `PLEDGED != AVAILABLE`.

## 8. Help Without a Receipt

A resident contributes ordinary labor to sorting or cleanup after a small disruption and declines reimbursement. The work is recorded as participation, not as a hidden favor currency.

## 9. The Returned Contribution

A need closes before an offered physical resource is consumed. The object returns to its contributor or original custodian instead of silently becoming institutional property.

## 10. The Same Need, Smaller Scope

A route problem initially generates a large assistance request. Later evidence shows only one segment requires work. Contributions are resized or released rather than consumed because they were once requested.

## 11. The Person Helped Last Season

A resident who previously received practical assistance later volunteers for an unrelated support task. Their stated motivation may reference prior help, but no debt ledger is created.

## 12. Relief Board Out of Date

A posted request remains visible after part of the need has been fulfilled. Pia or Mara corrects the public surface while preserving the old version as historical evidence.

## 13. Thin Delivery Buffer

During Thin Delivery Season, several small voluntary substitutions and shared-use decisions keep ordinary services functioning. The response produces a record of shortages and adaptations without resolving the cause of the season.

## Longer arc: What Bruma Can Share

Across several months, small assistance episodes accumulate around transport, food, repairs, care logistics and route recovery. The district develops recognizable patterns of who can help with which kinds of problems, but no universal relief authority is created.

Possible long-term consequences:
- some resources become commonly shared because repeated history supports it;
- some offers prove unreliable and are treated more cautiously;
- temporary arrangements become unnecessary when infrastructure improves;
- one recovery project can leave a repaired asset or revised procedure;
- public records can reveal that aid demand changed over time;
- residents can remember being helped without reducing relationships to a score.

## Mechanically rich encounter: Relief Shipment Withdrawal at Glass Bend

Premise:
A small legitimate shipment allocated to an existing Marea need is passing through Sendero del Vidrio. Wild activity creates immediate danger during withdrawal.

Narrative-owned state:
- aid need;
- allocation history;
- shipment/custody;
- beneficiaries;
- transport purpose;
- noncombatants;
- aftermath and later redistribution.

Full intended dependencies:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle where selected content requires it;
- terrain/weather/hazards/zones/reactions where tactical route conditions matter;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Full version status: BLOCKED.

Reduced version:
- secure noncombatants and semantic cargo in Narrative first;
- use one ordinary audited battle on stable geometry only if an immediate actor still prevents withdrawal;
- omit unverified weather, hazards, reactions and objective-sensitive displacement;
- consume only narrow handoffs such as `IMMEDIATE_ROUTE_THREAT_WITHDREW`, `IMMEDIATE_PASSAGE_CLEAR`, `IMMEDIATE_RELIEF_TEAM_CAN_WITHDRAW`.

Battle output cannot decide aid priority, ownership, debt, adequacy of relief, relationship state, liability or the cause of Thin Delivery Season.