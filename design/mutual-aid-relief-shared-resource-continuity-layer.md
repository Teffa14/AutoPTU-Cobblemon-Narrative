# Mutual Aid, Relief & Shared Resource Continuity Layer

Status: DESIGN / PROPOSED ARCHITECTURE. NOT CANON.
Date: 2026-09-02
Pass: 202
Research basis: `research/2026-09-02-mutual-aid-relief-shared-resource-scan-202.md`

## Purpose

Represent voluntary assistance, shared recovery resources, local relief projects and contribution history without inventing insurance law, taxation, entitlement, reputation points or mechanical rewards.

This layer exists so a settlement can respond collectively to shortages, damage and local needs through traceable contributions and constrained capacity.

## Existing-system boundaries

Reuse existing owners:
- crisis/rescue/recovery owns incident state and immediate response;
- service-request continuity owns requests, scheduling and work orders;
- market/transaction continuity owns governed offers, payment and transfer;
- case/custody owns disputed custody and evidence chains;
- care/welfare owns care cases while PTU owns mechanical health state;
- material culture owns physical item instances and provenance;
- civic works owns public infrastructure projects;
- cooperative/agriculture owns producer and storage state;
- identity/delegation owns authority and proxy scope;
- public memory owns later commemoration/public interpretation;
- PTU/Caelo/AutoPTU owns currency, Items, Skills, Features, healing and battle mechanics.

This layer owns only aid intent, contribution allocation and relief-project continuity.

## Core record: aid_need

```yaml
aid_need:
  need_id: null
  reported_by_ref: null
  beneficiary_refs: []
  location_refs: []
  need_kind: RESOURCE | SERVICE | TRANSPORT | REPAIR | CARE_SUPPORT | SHELTER | INFORMATION | OTHER
  description_ref: null
  reported_at: null
  verification_state: REPORTED | PARTIALLY_VERIFIED | VERIFIED | DISPUTED | CLOSED
  evidence_refs: []
  urgency_claim_refs: []
  current_remaining_need_ref: null
  owner_system_refs: []
```

A reported need may be sincere and still incomplete.

## Aid offer

```yaml
aid_offer:
  offer_id: null
  offered_by_ref: null
  need_id: null
  offered_at: null
  contribution_kind: ITEM | SERVICE | TIME | TRANSPORT_SLOT | STORAGE | INFORMATION | FUNDS_REF | OTHER
  governed_resource_ref: null
  quantity_or_scope_ref: null
  conditions_ref: null
  availability_window_ref: null
  status: OFFERED | ACCEPTED | DECLINED | REDIRECTED | EXPIRED | WITHDRAWN | FULFILLED
  provenance_refs: []
```

Narrative does not create the underlying governed resource. `FUNDS_REF` points to authoritative transaction/economy state.

## Allocation record

```yaml
aid_allocation:
  allocation_id: null
  need_id: null
  offer_ids: []
  allocated_by_ref: null
  allocation_basis_ref: null
  allocated_at: null
  beneficiary_refs: []
  status: PROPOSED | RESERVED | TRANSFERRED | DELIVERED | RELEASED | CANCELLED
  conflict_refs: []
  outcome_refs: []
```

Allocation records who made the decision and why. They do not establish universal priority law.

## Shared relief pool

A relief pool is an accounting view over separately governed resources.

```yaml
shared_relief_pool:
  pool_id: null
  purpose_ref: null
  steward_refs: []
  contribution_refs: []
  eligible_need_refs: []
  allocation_refs: []
  opened_at: null
  closed_at: null
  policy_ref: null
  state: OPEN | LIMITED | CLOSED | REVIEW_PENDING
```

Hard rule:

`POOL_RECORD != CURRENCY_LEDGER`

The pool never mints money or Items. Each contribution references an actual authoritative resource/event.

## Recovery project

```yaml
relief_project:
  project_id: null
  project_kind: REPAIR | RESTOCK | TEMPORARY_SERVICE | ACCESS_RESTORE | COMMUNITY_SUPPORT | OTHER
  location_refs: []
  sponsor_or_owner_refs: []
  need_refs: []
  contribution_refs: []
  dependency_refs: []
  work_order_refs: []
  status: PROPOSED | READY | ACTIVE | BLOCKED | PARTIAL | COMPLETE | CANCELLED
  started_at: null
  completed_at: null
  aftermath_refs: []
```

Project completion records the delivered result only. It does not grant contributors ownership or authority.

## Reciprocity without debt

The system may record that an actor previously received assistance and later chose to help another person or project.

```yaml
reciprocity_note:
  note_id: null
  actor_ref: null
  prior_support_refs: []
  later_contribution_refs: []
  stated_motivation_ref: null
```

Do not infer obligation.

`RECEIVED_HELP != OWES_HELP`

`LATER_HELP != DEBT_REPAID`

## Priority handling

Different needs can compete for one scarce resource. Preserve:
- who identified each need;
- evidence available at decision time;
- available alternatives;
- who had authority over the resource;
- whether allocation was temporary or final;
- unresolved disagreement.

Do not create a hidden global priority score.

## Mechanical-resource boundary

When aid contains mechanical content:
- currency transfer must use authoritative economy commands/state;
- PTU Items remain real item instances;
- healing remains governed by PTU/Caelo/AutoPTU;
- crafting/repair bonuses are not invented;
- Pokémon work requires verified individual capability where mechanics matter;
- Trainer Features/Edges/Skills are not granted by volunteering;
- no narrative resource becomes a battle Item automatically.

## NPC agency

Aid can progress without the player.

Examples:
- Lia finds another unloading slot;
- Teo completes a repair after a component arrives;
- Brin redirects reusable crates;
- Ivo accepts a substitute ingredient lot;
- residents complete ordinary sorting work;
- Mara closes a small assistance request once evidence supports completion.

Player absence cannot freeze valid dependencies.

## Minecraft/Cobblemon boundary

Minecraft may project:
- crates;
- carts;
- work tables;
- temporary supply stacks;
- volunteers;
- posted requests;
- repaired structures;
- Pokémon present as individual actors.

Projection cannot author allocation or ownership.

`VISIBLE_CRATE != AVAILABLE_FOR_AID`

`ITEM_ENTITY_PICKUP != CONTRIBUTION_ACCEPTED`

`NPC_AT_PROJECT != VOLUNTEER_COMMITMENT`

`POKEMON_NEAR_WORKSITE != WORK_CAPABILITY`

`BLOCK_REPAIRED != PROJECT_GOVERNANCE_COMPLETE`

## Quest grammar

Low-mechanics episodes can include:
- connect a need with an existing available resource;
- discover that a pledged resource was already committed elsewhere;
- redirect an offer when the original need is resolved;
- decide between two timing windows without inventing a morality score;
- document partial fulfillment;
- return unused contributed property;
- verify that a repair is actually complete before closing the request;
- preserve disagreement about allocation without forcing a villain;
- show a later voluntary contribution by someone previously helped;
- complete a recovery project while leaving incident causation unresolved.

## First implementation slice — The Shared Cart Repair

Premise:
A cooperative cart used for ordinary movement between Loma Clara and Puerto Bruma needs repair. Teo can do the work. One replacement component is available through an existing supply path, while a short work window must align with current service capacity.

State exercised:
- one `aid_need`;
- two `aid_offer` records;
- one allocation decision;
- one existing work order;
- one persistent cart/project record;
- partial then complete fulfillment.

Actors:
- Teo owns repair work within his canon role;
- Brin can expose cooperative custody/availability;
- Lia may expose a transport window if the component is arriving through the dock;
- no new NPC or institution is required.

Persistent consequence:
The cart returns to ordinary service. The contribution history remains queryable.

No automatic outputs:
- reputation;
- friendship;
- ownership share;
- money reward;
- crafting XP;
- Thin Delivery Season cause.

Current disposition: IMPLEMENTABLE AS NARRATIVE/WORLD STATE.

## Mechanically rich encounter — Relief Shipment Withdrawal at Glass Bend

Premise:
A small shipment already allocated to a legitimate Marea need is moving through Sendero del Vidrio. Wild activity creates an immediate withdrawal problem. The shipment's social purpose is not a combat objective owned by AutoPTU.

### Intended full version

Potential tactical content:
- combatants and protected withdrawal geometry;
- one or more noncombat relief actors outside or adjacent to tactical scope;
- Interception;
- Push/Pull/Knockback/forced movement if selected content uses them;
- route terrain/weather/hazards where mechanically verified;
- exact Moves, Abilities, Items and Trainer Features;
- AI that can prioritize withdrawal/territory rather than KO;
- faithful Minecraft/Cobblemon/Craftics playback.

Permanent capability dependencies:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle when selected content uses statuses;
- terrain/weather/hazards/zones/reactions when authored tactically;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Current disposition: FULL VERSION BLOCKED.

### Reduced version

1. Aid need, allocation, shipment custody and beneficiary remain Narrative-owned.
2. Move noncombatants and semantic cargo to a safe world-state position before BattleSpec where appropriate.
3. Identify only the immediate wild actor preventing withdrawal.
4. Use stable geometry and audited combatants/content.
5. Omit tactical weather/hazards/reactions and forced-movement objectives unless separately verified.
6. Run an ordinary audited battle.
7. Consume only narrow results such as `IMMEDIATE_ROUTE_THREAT_WITHDREW`, `IMMEDIATE_PASSAGE_CLEAR` or `IMMEDIATE_RELIEF_TEAM_CAN_WITHDRAW`.

Battle cannot determine:
- who deserves aid;
- ownership of contributed resources;
- project priority;
- adequacy of relief;
- repayment/debt;
- relationship changes;
- Thin Delivery Season cause;
- future contribution obligations.

Current disposition: REDUCIBLE WITH AUDITED BASIC CONTENT.

## Strong invariants

`NEED_REPORTED != NEED_VERIFIED`

`AID_OFFERED != AID_DELIVERED`

`RESOURCE_PLEDGED != RESOURCE_TRANSFERRED`

`CONTRIBUTION != OWNERSHIP`

`CONTRIBUTION != REPUTATION_GAIN`

`RECEIVING_HELP != PERSONAL_DEBT`

`POOL_RECORD != CURRENCY_LEDGER`

`PROJECT_COMPLETE != INCIDENT_CAUSE_RESOLVED`

`BATTLE_RESULT != AID_PRIORITY`

`MINECRAFT_PROJECTION != RESOURCE_AUTHORITY`