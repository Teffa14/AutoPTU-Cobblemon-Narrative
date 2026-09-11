# The Terms Have to Arrive — Pass 433

Status: PROPOSED / NON-CANON
Canon approval: NOT GRANTED
Runtime dependency: Pass 433 counterproposal terms delivery

## Premise

A request for help produces a counterproposal rather than a yes/no answer. The responder offers concrete limits: another time, another location, a narrower task, or an alternate form of help.

The offer matters only when its terms actually reach the requester.

This creates a small but important persistent-world story unit. Two actors may agree that a response exists while holding different practical knowledge because the detailed terms are still in transit, delayed behind channel load, waiting for local acknowledgement or already stale when received.

## Candidate Ouros use

Marea can be used only as a regression binding because its resident network already contains work, coordination and observation roles. No new Marea canon is asserted here.

Example shape:

Mara requests assistance with an equipment problem. Teo cannot take the implied full task. He authors a counterproposal: inspect during a later window at the field office, diagnose only, or provide a remote parts list instead.

The durable proposal exists immediately for Teo. Mara knows none of those terms until the explicit message arrives.

If the message arrives after expiry, Mara may learn what Teo had offered, but the offer is no longer silently actionable. If it arrives in time, Mara still has to choose what to do with it.

## Reduced playable version

This version requires no AutoPTU mechanics.

Narrative sequence:

request → responder replanning → counterproposal action → structured terms → explicit terms delivery → requester replanning → later accept/reject/defer/new counterproposal decision.

Possible scenes include:
- equipment diagnosis;
- archive consultation;
- route advice;
- short inspection;
- meeting at a different work site;
- referral to another qualified person.

The drama comes from time, knowledge, obligations and changing circumstances. No combat is necessary.

## Full mechanically rich version

The same accepted proposal can later lead into a hazardous retrieval, escort, rescue, containment or disputed-site operation. The negotiated constraints remain part of the premise: the helper may have agreed only to diagnosis, one location, one time window or one role.

If the scene crosses into structured mechanics, AutoPTU owns resolution through the existing explicit handoff.

Dependencies must be attached to the actual encounter behavior:

- ordinary target/placement/range/LoS: targeting/footprints/range/LoS, VERIFIED only in audited scopes;
- ordinary legal movement: base movement legality, VERIFIED only in audited scopes;
- push/pull/knockback/interception/forced rescue repositioning: complete movement, PARTIAL;
- standard numeric resolution: core calculations, VERIFIED only in audited scopes;
- initiative-sensitive participation or replacement timing: action economy/initiative, PARTIAL;
- timed multi-round phases, delayed collapse or evacuation clocks: full turn/round lifecycle, PARTIAL;
- injury/damage-linked objective state: full stateful damage pipeline, PARTIAL;
- persistent affliction consequences: status lifecycle, PARTIAL;
- changing dangerous ground, weather phases, zones or reactions: terrain/weather/hazards/zones/reactions, MIXED / PARTIAL / BLOCKING by mechanism;
- named Move interactions: move-specific behavior, individually gated;
- Ability-triggered effects: abilities, PARTIAL and individually gated;
- rules-level equipment effects: items, individually gated;
- Trainer interrupts or specialist Features: Trainer Features/perks, individually gated;
- ordinary audited actions: AI legal-action infrastructure, VERIFIED only in audited scopes;
- objective-aware escort/rescue/protect/retrieve/extract choices: AI tactical policy, BLOCKING;
- authoritative objective display/playback and non-KO completion: Minecraft/Cobblemon/Craftics adapter/playback support, PARTIAL / BLOCKING.

A reduced implementation may replace unsupported tactical detail with ordinary world-state inspection, travel and explicit narrative completion while preserving the same negotiated premise. It must not fake knockback, reactions, statuses, weather phases or Trainer interrupts in the adapter.

## Narrative consequences

This pattern produces consequences without forcing hostility:

A late offer can expose a missed opportunity. A narrow offer can make the requester seek a second helper. A different location can introduce travel and access constraints. An alternate method can redirect the incident toward investigation rather than battle. A rejected term can remain part of relationship history without automatically changing trust.

Future relationship changes require their own provenance-backed event.

## Canon questions

Still unresolved and therefore not asserted:

- which Ouros institutions may formally negotiate assistance scope;
- whether any role carries mandatory emergency duties that constrain the freedom to counterpropose;
- which location references should be standardized for negotiated work;
- whether `scope_ref` and `alternative_ref` become registries or remain validated opaque references;
- which proposal expiries should close silently versus produce an explicit requester-facing closure event.

## Implementation follow-through

Pass 433 makes terms explicitly deliverable. The next safe step is a requester-owned durable decision that names the exact `proposal_id` and proves the terms-delivery trigger in its causal history. Acceptance can then feed a separate commitment creation step. Route reservation, resource allocation and tactical execution remain later owners.
