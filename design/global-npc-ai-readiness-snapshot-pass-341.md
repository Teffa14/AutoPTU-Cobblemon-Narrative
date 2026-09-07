# Global NPC AI readiness snapshot — Pass 341

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Scope

Pass 341 adds an executable recovery-intent bridge after Pass 338 resource blocking. It derives safe world-level follow-up options such as requesting a known holder, traveling to a resource already reserved for the actor, or waiting behind another valid reservation.

AutoPTU-Java and AutoPTU were inspected read-only. Only the narrative repository was modified.

No family-wide combat capability is promoted from representative mechanics.

## Narrative inspection basis

Narrative `main` began this pass at `39e679817d98373d9795eab99d0fe6bfb4bcc41b`.

Before writing, the recursive repository tree was inspected and repository-wide searches were run for resource acquisition/request, borrowing, transfer and existing PTU actual-play sources. Existing owners were confirmed for Pass 338 resource availability, Pass 339 reservations, Pass 340 readiness, travel, communication, maintenance/shared equipment and the base agenda planner.

No existing executable owner was found for deriving next-step world intents from a resource-blocked task. Pass 338 and Pass 340 explicitly left that seam unresolved.

## New executable narrative evidence

Added:

- `tools/global_npc_resource_recovery.py`
- `tests/test_global_npc_resource_recovery.py`
- `implementation/global-npc-resource-recovery-fixture-v1.json`
- `design/global-npc-resource-recovery-intent-contract-pass-341.md`
- `research/2026-09-07-resource-request-acquisition-recovery-scan-341.md`
- `proposals/2026-09-07-the-request-before-the-kit-case-341.md`

The executable V1 derives only state-justified follow-up intents.

A known other holder may yield `REQUEST_RESOURCE`. A remote resource already reserved for the blocked actor may yield `TRAVEL_TO_RESERVED_RESOURCE` only when the existing semantic travel graph can build a route. Another actor's reservation may yield `WAIT_FOR_RESOURCE`. An unreserved remote resource fails closed because access authority is not established.

The module does not transfer, reserve, checkout, consume, repair, approve or deploy resources and never requests AutoPTU by itself.

## Live read-only engine heads

### AutoPTU-Java

Observed `main` head:

`83ec9610ef83a7d71186a404ef509faa317109d1`

Merge: `Add round-start ability effect execution for Air Lock` (PR #396).

The merged slice adds a server-owned round-start Ability effect path and freezes Air Lock behavior against the pinned Python oracle. It strengthens evidence for one Ability and one round-start/weather seam. It does not establish complete Ability execution, complete weather/hazard behavior or the full turn/round lifecycle.

### AutoPTU Python

Observed `main` head:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

The head remains `Career: keep battle coordinates synced after viewport resize (#237)` and explicitly describes the change as presentation-only with no battle-rule or outcome change.

## PTU / Caelo boundary

Exact tactical mechanics remain sourced from the project's PTU/Core/Pokédex/Caelo boundary.

Pass 341 introduces no Item rule, Trainer Feature, Skill check, borrowing DC, travel modifier, carrying rule, communication action, Move effect or Ability effect. Public resource-management and PTU actual-play material is used only as narrative/design evidence.

## Permanent capability audit

### targeting / footprints / range / LoS

Rating: VERIFIED for ordinary audited contracts.

The reduced recovery layer has no targeting dependency. A rich field tool or delivery objective that targets creatures, tiles or zones remains separately gated.

### base movement legality

Rating: VERIFIED for ordinary audited movement.

Pass 341 reuses the existing world travel graph to verify semantic travel viability. It does not execute PTU tactical movement.

### complete movement including push / pull / knockback / interception / forced movement

Rating: PARTIAL.

Carrying, dragging, interception, rescue and forced displacement involving a resource remain dependent on this family.

### core calculations

Rating: VERIFIED for ordinary audited deterministic battle arithmetic.

Resource matching, semantic route duration and planner scoring remain world-system calculations, not new PTU combat math.

### action economy / initiative

Rating: VERIFIED for ordinary audited primitives.

A world request or semantic travel intent consumes no invented tactical action. In-combat pickup, handoff, equip or use remains separately gated.

### full turn / round lifecycle

Rating: PARTIAL.

PR #396 proves a narrow round-start Air Lock execution seam only. Pass 341 uses world semantic time and adds no round lifecycle rule.

### full stateful damage pipeline

Rating: PARTIAL.

The reduced resource recovery path causes no combat damage.

### status lifecycle

Rating: PARTIAL.

Resource reservation/readiness states remain world logistics, not PTU Status Afflictions.

### terrain / weather / hazards / zones / reactions

Rating: MIXED / PARTIAL / BLOCKING by subfamily.

PR #396 adds narrow Air Lock weather-suppression evidence but does not prove complete weather, hazard, zone or reaction behavior.

### move-specific behavior

Rating: PARTIAL.

No Move behavior is inferred.

### abilities

Rating: PARTIAL.

Air Lock has materially stronger round-start effect evidence after PR #396. That evidence remains narrow and does not promote the Ability family.

### items

Rating: PARTIAL and individually gated.

A recovered `WorldResource` may be mundane equipment. If it later maps to a PTU Item, possession and world readiness do not prove tactical legality or effect implementation.

### Trainer Features / perks

Rating: PARTIAL and individually gated.

Resource request/travel logic does not grant or execute Trainer Features.

### AI legal-action infrastructure

Rating: VERIFIED for ordinary audited legal-action infrastructure.

Pass 341 adds world planning intents only. Any future structured pickup, transfer or protect-object action must be represented and validated separately.

### AI tactical policy

Rating: BLOCKING for rich resource-objective behavior.

Protecting, delivering, abandoning or sharing equipment under tactical pressure, or prioritizing observation/escort over defeat, remains outside current rich policy evidence.

### Minecraft / Cobblemon / Craftics adapter/playback

Rating: PARTIAL / BLOCKING end-to-end.

Minecraft may present a request, resource location, pickup animation or later result. It cannot infer provider consent, grant access, transfer authoritative ownership, complete semantic travel or activate a PTU Item effect.

## Reduced-version readiness

Pass 341 is executable as world-agent planning and needs no AutoPTU handoff.

It consumes existing agent/resource state and optionally the existing semantic route graph. Communication delivery, travel execution, reservation mutation and resource transfer remain with their current owners.

## Rich encounter dependencies

`The Request Before the Kit` has a reduced version with no combat requirement.

Any rich variant that turns pickup/delivery/fieldwork into structured play preserves exact gates: ordinary targeting/base movement/core arithmetic/action primitives remain VERIFIED within their audited scope; complete movement, lifecycle, damage and status remain PARTIAL; terrain/weather/hazards/zones/reactions remains MIXED/PARTIAL/BLOCKING; Moves, Abilities, Items and Trainer Features remain PARTIAL and individually gated; tactical policy remains BLOCKING for non-defeat resource objectives; adapter/playback remains PARTIAL/BLOCKING end-to-end.

## Unresolved questions

Resource-system work now centers on provider consent/request-state lifecycle, institutional pools and delegated authority, explicit transfer events, quantity/capacity booking, waitlists/fairness, consumable decrement/replenishment, checkpoint persistence, player inventory binding, Minecraft acknowledgement and capability-scoped LIMITED readiness.

The communication/travel integration seam also needs an explicit coordinator after a resource request is actually accepted; Pass 341 intentionally stops before that state transition.

Canon remains unresolved for institution-specific equipment pools, owners, borrowing policy, request authority, courier responsibility, field scenario and any exact PTU/Caelo Item mapping.
