# Global NPC AI readiness snapshot — Pass 342

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Scope

Pass 342 adds an executable provider-consent and resource-request lifecycle after Pass 341 recovery-option derivation.

AutoPTU-Java and AutoPTU were inspected read-only. Only the narrative repository was modified.

No family-wide combat capability is promoted from one representative Move, Ability, status, Feature or lifecycle seam.

## Narrative inspection basis

Narrative `main` began this pass at:

`0daf2fb1f1cd15333fd14444b08c052cfe40d94f`

Before writing, the recursive repository tree, `CURRENT_FOCUS.md`, `README.md`, Pass 338–341 resource owners, reservation/readiness code, recovery tests, workflow configuration, existing research-source usage and canon boundaries were inspected.

Repository-wide search found no existing executable owner for provider acceptance/rejection/cancellation/expiry/withdrawal of resource requests while preserving the distinction between consent and physical transfer.

Pass 341 explicitly deferred this lifecycle.

## New executable narrative evidence

Added:

- `tools/global_npc_resource_requests.py`
- `tests/test_global_npc_resource_requests.py`
- `implementation/global-npc-resource-request-lifecycle-fixture-v1.json`
- `design/global-npc-resource-request-consent-contract-pass-342.md`
- `research/2026-09-07-resource-request-consent-lifecycle-scan-342.md`
- `proposals/2026-09-07-the-yes-before-the-handoff-case-342.md`

The executable V1 stores immutable requests and append-only response events.

It distinguishes:

- request authored/submitted;
- pending response;
- provider acceptance;
- provider rejection;
- requester cancellation;
- derived expiry;
- provider withdrawal after acceptance;
- alternate resource offer without rewriting the original request.

No state transition reserves, transfers, checks out, transports or activates a resource.

## CI evidence correction

During inspection, the existing `Global NPC AI Regressions` workflow was found to run:

`python -m unittest discover -s tests -p 'test_global_npc_*.py' -v`

Many recent global-NPC tests use module-level pytest-style test functions. `unittest discover` does not provide reliable evidence that those functions ran.

Pass 342 updates `.github/workflows/global-npc-ai.yml` to:

- install pytest explicitly;
- run `python -m pytest tests/test_global_npc_*.py -v`;
- include the Pass 338–342 resource modules and fixtures in path triggers.

The corrected workflow run #182 for head:

`4f62cae61831065962cdf66f3fc9b4912d3aede8`

completed successfully.

Therefore Pass 342 treats that corrected pytest run as the first direct CI evidence for the whole current `test_global_npc_*.py` suite under the intended test style. Older green `unittest discover` runs are not retroactively treated as proof that every module-level function test executed.

## Live read-only engine heads

### AutoPTU-Java

Observed `main` head:

`b85fe17319d16e54402a5a45fb6acccd6b388553`

Merge PR #397:

`Freeze Python Arena Trap target eligibility`

The merged slice adds `ArenaTrapTargetingContract`, frozen against the pinned Python oracle. The contract currently proves narrow target eligibility semantics for regular Arena Trap and its errata activation input, including:

- active and non-fainted targets;
- opposing-team filtering;
- 5-meter range;
- exclusions based on Flying type, Levitate Ability/capability, Sky speed threshold and Burrow speed threshold represented by the oracle fixture.

The Java class explicitly isolates target eligibility from eventual status mutation handling.

The merge therefore strengthens evidence for one Ability's target-selection/range contract. It does not prove:

- Arena Trap's complete stateful Slowed application;
- full Slowed lifecycle;
- all Ability triggers/effects;
- all range/LoS semantics;
- complete movement interactions;
- the full turn/round lifecycle.

The retrieved main-branch workflow set for this head showed completed successful runs and no failure/in-progress result in the inspected set.

### AutoPTU Python

Observed `main` head:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

The head remains:

`Career: keep battle coordinates synced after viewport resize (#237)`

Its commit message explicitly states the change is presentation-only and does not change battle rules or outcomes.

## PTU / Caelo boundary

The repository README continues to identify PTU Core, Pokédex material and the Caelo source set as the mechanical authority boundary when exact rules are invoked.

Pass 342 introduces no:

- PTU Item effect;
- borrowing or persuasion Skill check;
- social DC;
- Feature;
- movement rule;
- carrying capacity;
- battle action;
- payment rule;
- ownership law;
- transfer mechanic.

Public resource-management material and official Pokémon material are used only for high-level workflow/story structure.

## Permanent capability audit

### targeting / footprints / range / LoS

Rating: VERIFIED for ordinary audited contracts.

PR #397 adds narrow Arena Trap target/range eligibility evidence. It does not promote the complete category or prove special object targeting, every Ability range, footprints or all LoS behavior.

Pass 342 reduced execution has no tactical targeting dependency.

### base movement legality

Rating: VERIFIED for ordinary audited movement.

The reduced request lifecycle performs no tactical movement. A later pickup/delivery story may use existing world travel without implying tactical movement execution.

### complete movement including push / pull / knockback / interception / forced movement

Rating: PARTIAL.

Carrying restrictions, dragging, interception, rescue and forced displacement involving a resource remain dependent on this family.

PR #397's target exclusions based on movement capabilities do not prove complete movement behavior.

### core calculations

Rating: VERIFIED for ordinary audited deterministic battle arithmetic.

Request-state projection and semantic expiry are world-state calculations, not PTU battle arithmetic.

### action economy / initiative

Rating: VERIFIED for ordinary audited primitives.

Submitting, accepting or cancelling a world request creates no invented tactical action. In-combat pickup, handoff, equip, activation, guarding or dropping remain separately gated.

### full turn / round lifecycle

Rating: PARTIAL.

Previous round-start slices plus PR #397 strengthen specific seams, but no evidence establishes the complete lifecycle.

Pass 342 uses semantic world time only.

### full stateful damage pipeline

Rating: PARTIAL.

The reduced request lifecycle causes no combat damage. Equipment damage in a rich transfer encounter remains separately dependent on this family.

### status lifecycle

Rating: PARTIAL.

PR #397 freezes Arena Trap target eligibility but explicitly leaves eventual state mutation outside the new contract. It therefore does not prove complete Slowed application, duration, cleanup or broader status lifecycle behavior.

### terrain / weather / hazards / zones / reactions

Rating: MIXED / PARTIAL / BLOCKING by subfamily.

Prior Air Lock evidence remains narrow. Pass 342 adds no new terrain, weather, hazard, zone or reaction evidence.

### move-specific behavior

Rating: PARTIAL.

No Move behavior is inferred from the request system or from Arena Trap Ability work.

### abilities

Rating: PARTIAL.

Air Lock has prior round-start stateful-effect evidence. Arena Trap now has stronger target-eligibility parity evidence after PR #397.

Neither representative slice establishes the Ability family.

### items

Rating: PARTIAL and individually gated.

A requested `WorldResource` may be mundane equipment. If it maps to a PTU Item, request acceptance, possession, readiness and later handoff still do not prove tactical Item legality or effect execution.

### Trainer Features / perks

Rating: PARTIAL and individually gated.

Pass 342 creates no Trainer Feature behavior.

### AI legal-action infrastructure

Rating: VERIFIED for ordinary audited legal-action infrastructure.

Pass 342 adds world-agent request transitions only. Structured pickup, transfer, guard-object, equip or resource-use actions still need explicit tactical legal-action contracts if introduced.

### AI tactical policy

Rating: BLOCKING for rich resource-objective behavior.

Protecting a carrier, deciding to abandon equipment, completing a handoff under pressure, retreating with a resource or prioritizing delivery/observation over defeating all opponents remain outside current rich tactical-policy evidence.

### Minecraft / Cobblemon / Craftics adapter/playback

Rating: PARTIAL / BLOCKING end-to-end.

Minecraft may eventually present request messages, provider responses, carried objects and handoff animations. It cannot decide consent, ownership, reservation, technical readiness, transfer authority, request expiry or PTU Item effects.

## Reduced-version readiness

Pass 342 is executable as world-agent state with no AutoPTU dependency.

A blocked NPC may now have a durable request whose provider explicitly accepts or rejects, whose requester cancels, whose deadline expires, or whose prior acceptance is later withdrawn.

The lifecycle can produce schedule, belief, communication and relationship consequences without starting combat.

## Rich encounter dependency map

`The Yes Before the Handoff` has a reduced version with no combat requirement.

If a later handoff, delivery route or field deployment enters structured play:

- targeting / footprints / range / LoS: ordinary audited scope VERIFIED; exact special targeting still gated;
- base movement legality: ordinary audited scope VERIFIED;
- complete movement: PARTIAL for carrying/interception/rescue/forced movement;
- core calculations: ordinary audited scope VERIFIED;
- action economy / initiative: primitive scope VERIFIED; exact handoff/equip/drop actions separately gated;
- full turn / round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING;
- move-specific behavior: PARTIAL and individually gated;
- abilities: PARTIAL and individually gated;
- items: PARTIAL and individually gated;
- Trainer Features/perks: PARTIAL and individually gated;
- AI legal-action infrastructure: VERIFIED for ordinary current scope, with object-transfer actions still unimplemented as a family claim;
- AI tactical policy: BLOCKING for rich non-defeat logistics objectives;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING end-to-end.

## Unresolved questions

The next resource-system seams are:

- request delivery/response communication coordinator;
- provider authority versus current physical holder;
- institutional resource pools;
- delegated approval and proxy authority;
- accepted-request to reservation transition;
- explicit transfer/handoff/courier world events;
- pickup versus delivery responsibility;
- quantity/capacity requests and partial fulfillment;
- waitlists and fairness;
- checkpoint persistence;
- expiry wake-ups and selective replanning;
- player-facing inventory/request binding;
- Minecraft acknowledgement;
- capability-scoped `LIMITED` readiness;
- exact PTU/Caelo mapping when a requested world resource has mechanical Item behavior.

Canon remains unresolved for institution-specific equipment pools, owners, borrowing policy, provider authority, courier responsibility, pickup expectations, proxy rules, exact work scenario and any PTU/Caelo Item mapping.
