# Global NPC AI readiness snapshot — Pass 338

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Scope

Pass 338 adds resource-aware world-intent gating. AutoPTU-Java and AutoPTU were inspected read-only. Only `Teffa14/AutoPTU-Cobblemon-Narrative` was modified.

No family-wide combat capability is promoted from representative mechanics.

## Narrative inspection basis

The pass began from narrative `main` head `138ee2fb905bdc478b1b45500be9f42f4080aefe`.

Before writing, the recursive repository tree was inventoried and the current focus, canon governance, recent Pass 337 contract/snapshot, base global NPC planner, agenda tests and repository-wide matches for custody, inventory, equipment, resource availability and double-booking were inspected.

Existing owners already cover evidence custody, found property, cold-chain continuity and other specialized domains. No global ordinary-resource readiness owner was found. `CURRENT_FOCUS.md` explicitly lists resource/inventory-aware intents as an immediate next slice.

Pass 338 therefore adds a narrow executable readiness gate rather than another custody system.

## New executable narrative evidence

Added:

- `tools/global_npc_resources.py`
- `tests/test_global_npc_resources.py`
- `implementation/global-npc-resource-availability-fixture-v1.json`
- `design/global-npc-resource-availability-intent-contract-pass-338.md`

The new layer:

- represents stable world resources by capability, quantity, state, location, holder and reservation holder;
- binds resource requirements to existing `NpcIntent` objects without changing the base planner schema;
- deterministically assesses same-location or actor-held availability;
- excludes resources reserved for another actor;
- blocks insufficient quantities;
- filters unavailable intents before reusing the existing deterministic `choose_intent` scorer;
- allows a lower-priority ready task to proceed when a higher-priority task lacks its required resource;
- requests AutoPTU only after world-resource readiness passes;
- never reserves, consumes, transfers or mutates a resource merely by planning.

This is world-system execution, not PTU Item execution.

## Live read-only heads

### AutoPTU-Java

Current `main` head observed during Pass 338:

`342399375c2053907c0951e41950073c1b5836d3`

Merge commit:

`Merge pull request #395 from Teffa14/parity/round-start-ability-dispatch-plan — Freeze Python round-start ability dispatch order`

This is unchanged from Pass 337.

Narrow evidence retained:

- `RoundStartAbilityDispatchPlan` freezes orchestration order for selected Python `start_round()` Ability work after Trainer Features;
- selected dispatch families include Air Lock, Arena Trap, Intimidate and Impostor;
- effect ownership remains outside the planner in registries/executors;
- the change does not prove complete Ability behavior or complete lifecycle behavior.

### AutoPTU Python

Current `main` head observed during Pass 338:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

The commit explicitly describes a presentation-only change with no battle-rule or outcome change.

## PTU / Caelo boundary

The repository README identifies PTU Core, Pokédex material and Caelo documents as the mechanical source set when exact rules are required. Current GitHub-accessible comparative material does not authorize inventing mechanics.

Public PTU community material was used only to confirm the high-level fact that some crafting activities can depend on specific equipment. Pass 338 does not import costs, checks, crafting outputs, item-use action costs, inventory limits or battle effects.

## Permanent capability audit

### targeting / footprints / range / LoS

Rating: VERIFIED for ordinary audited contracts.

The reduced resource gate does not depend on tactical targeting. A future device that targets a combatant or work point must use exact verified targeting behavior.

### base movement legality

Rating: VERIFIED for ordinary audited contracts.

Pass 338 currently requires a resource to be held by the actor or at the actor's world location. It does not teleport resources. Future acquisition from another location must use the existing world travel planner; tactical movement remains separately audited.

### complete movement including push / pull / knockback / interception / forced movement

Rating: PARTIAL.

The reduced resource gate avoids this family. Carrying, dragging, rescue, interception or forced relocation during a rich encounter requires exact support.

### core calculations

Rating: VERIFIED for ordinary audited deterministic battle calculations.

Resource quantity addition and deterministic selection are world logistics, not PTU combat arithmetic. Exact battle calculations remain AutoPTU-owned.

### action economy / initiative

Rating: VERIFIED for ordinary audited primitives.

Planning or checking world-resource readiness consumes no tactical action. Equipping, transferring, using or protecting a resource during combat requires an exact sourced action contract.

### full turn / round lifecycle

Rating: PARTIAL.

PR #395 retains additional narrow round-start evidence but does not prove full lifecycle behavior. Timed equipment activation, delayed effects or phase-dependent resource use remain gated.

### full stateful damage pipeline

Rating: PARTIAL.

The reduced resource layer creates no combat damage. Equipment that causes, prevents, redirects or receives damage requires exact implementation evidence.

### status lifecycle

Rating: PARTIAL.

`AVAILABLE`, `RESERVED`, `IN_USE`, `UNAVAILABLE`, `DEPLETED` and `RETIRED` are world-resource states, not PTU Status Afflictions.

### terrain / weather / hazards / zones / reactions

Rating: MIXED / PARTIAL / BLOCKING by subfamily.

The reduced layer does not create tactical terrain or equipment zones. Any resource that changes weather, terrain, hazards or reactions must be individually verified.

### move-specific behavior

Rating: PARTIAL.

No Move is inferred from resource capability or flavor.

### abilities

Rating: PARTIAL, with the same narrow round-start orchestration evidence as Pass 337.

PR #395 does not justify a family-wide promotion.

### items

Rating: PARTIAL.

This pass intentionally sharpens the boundary. A `WorldResource` may represent mundane equipment or a logistical representation of something later mapped to a PTU Item, but world availability never proves PTU Item legality or effect support.

Every exact Item remains individually gated.

### Trainer Features / perks

Rating: PARTIAL.

Existing round-start Trainer Feature work remains meaningful but incomplete. A world resource requirement cannot grant a Trainer Feature or satisfy an unknown mechanical prerequisite by itself.

### AI legal-action infrastructure

Rating: VERIFIED for ordinary audited legal-action infrastructure.

Pass 338 does not add tactical resource actions. If `USE_ITEM`, `TRANSFER_ITEM`, `PROTECT_EQUIPMENT` or similar tactical actions are later added, legal-action generation requires explicit support.

### AI tactical policy

Rating: BLOCKING for rich resource-objective behavior.

Potential rich policies include:

- protect a scarce tool rather than maximize damage;
- transfer equipment to an ally;
- withdraw with a recovered object;
- abandon equipment to rescue an actor;
- avoid consuming a scarce resource unnecessarily;
- complete a setup/repair objective instead of defeating every opponent.

The reduced Pass 338 planner has no tactical-policy dependency.

### Minecraft / Cobblemon / Craftics adapter and playback

Rating: PARTIAL / BLOCKING end-to-end.

Minecraft can display carried equipment, storage props, containers or setup animations. It cannot authoritatively create a `WorldResource`, reserve it, transfer institutional control, consume it or prove PTU Item effects merely because an item entity or inventory stack exists.

Production acknowledgement between world state and presentation remains unresolved.

## Pass 338 reduced-version readiness

The new resource gate is executable at world-agent level now.

It depends on:

- persistent NPC identity;
- stable world location refs;
- existing `NpcIntent` knowledge/permission gating;
- stable resource IDs and capability tags;
- deterministic resource-state input;
- existing `choose_intent` scoring and AutoPTU handoff boundary.

It avoids battle mechanics entirely unless the selected ready intent already declares `requires_structured_mechanics`.

## Rich encounter dependency matrix

For a future resource-dependent structured encounter:

- targeting/footprints/range/LoS — VERIFIED for ordinary audited contracts; exact device targeting still gated;
- base movement legality — VERIFIED for ordinary audited contracts;
- complete movement — PARTIAL for carrying/rescue/interception/forced movement complexity;
- core calculations — VERIFIED for ordinary audited math;
- action economy/initiative — VERIFIED for ordinary primitives, not for new equipment actions;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL and individually gated;
- Trainer Features/perks — PARTIAL and individually gated;
- AI legal-action infrastructure — VERIFIED for ordinary audited infrastructure, not for newly invented resource actions;
- AI tactical policy — BLOCKING for rich non-defeat/resource-protection objectives;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL/BLOCKING end-to-end.

## Unresolved implementation questions

World-agent resource system:

- reservation mutation, expiry and release;
- acquisition/request/wait/reschedule derived intents;
- institutional resource pools and borrowing permissions;
- resource transfer through communication/travel systems;
- checkpoint persistence;
- consumable decrement and durable return/repair;
- substitute capability grades;
- player inventory binding;
- multi-resource atomic reservation;
- contention fairness and backlog aging.

Mechanical:

- exact PTU/Caelo Item/crafting mappings when a world resource has mechanical effects;
- tactical resource-transfer actions;
- resource damage/destruction semantics;
- non-defeat tactical policy;
- production adapter acknowledgement.

Canon/content for `The Kit Booked Twice`:

- owning institution;
- actual field-kit identity;
- reservation authority;
- affected obligations and NPCs;
- substitute resources;
- persistent procedural consequence after the incident;
- whether the case remains operational or later intersects a structured encounter.
