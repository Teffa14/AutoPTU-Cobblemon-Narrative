# Global NPC AI readiness snapshot — Pass 339

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Scope

Pass 339 extends the Pass 338 world-resource gate with an executable temporal reservation lifecycle. AutoPTU-Java and AutoPTU were inspected read-only. Only the narrative repository was modified.

No family-wide combat capability is promoted from representative mechanics.

## Narrative inspection basis

Narrative `main` began this pass at `810ac652d23df663e02be68490c895ad9cc06047`.

Before writing, the recursive repository tree, current focus, recent history, Pass 338 resource owner, executable resource gate/tests and repository-wide inventory for reservation/loan/resource-related owners were inspected. Pass 338 explicitly left reservation mutation, expiry/release and borrowing-related work unresolved.

Pass 339 adds a bounded V1 reservation owner rather than duplicating specialized custody systems.

## New executable narrative evidence

Added:

- `tools/global_npc_resource_reservations.py`
- `tests/test_global_npc_resource_reservations.py`
- `implementation/global-npc-resource-reservation-fixture-v1.json`
- `design/global-npc-resource-reservation-lifecycle-contract-pass-339.md`
- `research/2026-09-07-temporal-resource-reservation-lifecycle-scan-339.md`
- `proposals/2026-09-07-the-slot-that-expired-case-339.md`

The V1 layer supports stable reservation IDs, non-overlapping semantic windows for indivisible resources, explicit release/cancel, derived scheduled/active/expired status, read-only projection into Pass 338, reservation-gated checkout and explicit return.

Planning does not create or mutate reservations.

## Live read-only engine heads

### AutoPTU-Java

Observed `main` head:

`342399375c2053907c0951e41950073c1b5836d3`

Merge: `Freeze Python round-start ability dispatch order` (PR #395).

Narrow evidence remains unchanged from Pass 338. `RoundStartAbilityDispatchPlan` freezes orchestration for selected round-start Ability families including Air Lock, Arena Trap, Intimidate and Impostor against the pinned Python oracle. The planner explicitly owns orchestration rather than complete Ability effects.

### AutoPTU Python

Observed `main` head:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

The head commit is still `Career: keep battle coordinates synced after viewport resize (#237)` and explicitly states that the change is presentation-only with no battle-rule or outcome change.

## PTU / Caelo boundary

Exact tactical mechanics remain sourced from the project's PTU/Core/Pokédex/Caelo source boundary. Pass 339 does not create PTU Item use rules, carrying limits, action costs, equipment damage, social checks or Trainer Feature effects.

Public shared-equipment policies and Pokémon/PTU campaign material were used only for reusable narrative/logistics structures.

## Permanent capability audit

### targeting / footprints / range / LoS

Rating: VERIFIED for ordinary audited contracts.

Reservation lifecycle has no targeting dependency. Any future targeted equipment effect remains separately gated.

### base movement legality

Rating: VERIFIED for ordinary audited contracts.

The reduced lifecycle does not move an actor or resource automatically. Acquisition/return travel must use existing world travel state; tactical movement remains AutoPTU-owned.

### complete movement including push / pull / knockback / interception / forced movement

Rating: PARTIAL.

Only a rich encounter involving carrying, rescue, interception or forced displacement depends on this family.

### core calculations

Rating: VERIFIED for ordinary audited deterministic battle arithmetic.

Semantic reservation-window comparison is world logistics, not PTU combat calculation.

### action economy / initiative

Rating: VERIFIED for ordinary audited primitives.

World reservation, checkout and return events consume no invented tactical action. Any equivalent in-combat action needs an exact contract.

### full turn / round lifecycle

Rating: PARTIAL.

PR #395 provides narrow round-start orchestration evidence only. Reservation windows run on world semantic time. Timed in-combat equipment behavior remains gated.

### full stateful damage pipeline

Rating: PARTIAL.

V1 does not damage equipment or actors. Rich equipment-damage behavior requires exact implementation evidence.

### status lifecycle

Rating: PARTIAL.

Reservation states are world-logistics states and are not PTU Status Afflictions.

### terrain / weather / hazards / zones / reactions

Rating: MIXED / PARTIAL / BLOCKING by subfamily.

No tactical zone or hazard is created by the reduced reservation layer.

### move-specific behavior

Rating: PARTIAL.

No Move behavior is inferred.

### abilities

Rating: PARTIAL.

PR #395 remains narrow ordering evidence for selected round-start families and does not justify family-wide completion.

### items

Rating: PARTIAL and individually gated.

A reserved `WorldResource` can be mundane. Even if later mapped to a PTU Item, reservation/checkout proves only world availability and current holder, not legal use or effect support.

### Trainer Features / perks

Rating: PARTIAL and individually gated.

A booking never grants or satisfies an unknown Trainer Feature by itself.

### AI legal-action infrastructure

Rating: VERIFIED for ordinary audited legal-action infrastructure.

No tactical reserve/checkout/pass action is added. Any such action needs explicit legal-action generation support.

### AI tactical policy

Rating: BLOCKING for rich resource-objective behavior.

Protecting equipment, transferring it under pressure, withdrawing with it or prioritizing a field objective over defeat remains outside current rich tactical policy evidence.

### Minecraft / Cobblemon / Craftics adapter/playback

Rating: PARTIAL / BLOCKING end-to-end.

Minecraft may display a locker, carried kit or handoff animation. It cannot authoritatively reserve a resource, expire a booking, establish ownership, perform an institutional checkout or prove PTU Item effects from inventory state.

## Reduced-version readiness

The Pass 339 reduced layer is world-agent executable and does not need AutoPTU.

Required world inputs are stable resource IDs, stable actor IDs, semantic time, reservation windows, explicit closure operations and Pass 338 resource state.

## Rich encounter dependencies

If a later story makes the checked-out resource part of a structured encounter, exact families remain visible: ordinary targeting/base movement/core calculations/action primitives are verified within their audited scope; complete movement, full lifecycle, damage and status are partial; hazards/zones are mixed; Moves, Abilities, Items and Trainer Features are partial and individually gated; tactical policy is blocking for non-defeat resource objectives; adapter/playback is partial/blocking end-to-end.

## Unresolved questions

Next resource-system work includes quantity/capacity booking, waitlists/fairness, delegated/institutional authority, borrowing across organizations, resource-acquisition intents, no-show policy consequences, checkout due state, transfer/travel integration, consumable decrement, inspection/repair/calibration, checkpoint persistence and player inventory binding.

Canon remains unresolved for any institution-specific booking policy, equipment identity, local penalty or rich encounter built on this global contract.
