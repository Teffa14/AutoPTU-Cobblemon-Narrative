# Resource request, acquisition and recovery scan — Pass 341

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-07

## Research question

Passes 338–340 established resource availability, reservation lifecycle and operational readiness. The remaining world-agent gap is what a blocked NPC can do next without fabricating possession, permission, transfer or tactical effects.

This scan asks how real resource-management systems separate requirement identification, requesting, provider consent, mobilization, tracking and restocking, and what reusable structures can support original Ouros quests and NPC planning.

## Source 1 — FEMA NIMS resource management: order and acquire

Public source:
https://training.fema.gov/emiweb/is/is703b/studentmanual/is0703%20sm.pdf

The NIMS Resource Management student material separates a resource-management cycle into identifying requirements, ordering/acquiring, mobilizing, tracking/reporting, demobilizing and reimbursement/restocking. It also states that a providing organization consents to a request and communicates discrepancies between what was requested and what is available for delivery.

Reusable Ouros structure:

- identifying a need does not acquire the resource;
- sending a request does not imply provider consent;
- provider consent does not imply physical arrival;
- mobilization and transport remain separate events;
- return/restock remains part of the lifecycle after use;
- the world can contain several legitimate requests competing for limited capability.

Transformation boundary:

Ouros uses these as state-separation principles. It does not copy FEMA organizational roles, forms, terminology requirements or emergency doctrine into canon.

## Source 2 — FEMA / USFA NIMS resource management overview

Public source:
https://www.usfa.fema.gov/a-z/nims/managing-resources.html

The current page emphasizes planning responsibility, resource typing, inventory, mutual-aid agreements, requested/delivered schedules, operational priorities, tracking and restocking. It distinguishes the requester from the supplier/provider and treats both sides as participants in the resource lifecycle.

Reusable Ouros structure:

- a request can cross institutional boundaries;
- the provider can have its own obligations and competing priorities;
- schedule and location remain first-class resource facts;
- a requested resource can be delayed without disappearing;
- institutional borrowing should eventually use explicit agreements/authority rather than assuming faction membership creates access.

## Source 3 — FEMA National Resource Hub / resource typing

Public sources:
https://preptoolkit.fema.gov/web/national-resource-hub/resource-typing
https://preptoolkit.fema.gov/web/national-resource-hub

FEMA describes resource typing as categorizing resources by capability and minimum criteria. The National Resource Hub separately notes that inventory information does not itself operate as a deployment/request system.

Reusable Ouros structure:

- capability description can help find a candidate resource;
- inventory discovery does not grant deployment authority;
- `KNOWN_RESOURCE_CAPABILITY != REQUEST_ACCEPTED`;
- `RESOURCE_LISTED != RESOURCE_MOBILIZED`.

This directly supports keeping Pass 338 capability matching separate from Pass 341 recovery intent generation.

## Source 4 — USGS Geophysical Equipment Program

Public source:
https://water.usgs.gov/usgs/espd/hgb/equipment/

USGS describes a shared equipment program in which offices may request to borrow specialized equipment, recommends requesting ahead because equipment is in high demand, and makes loans subject to availability and usage policies.

Reusable Ouros structure:

- another institution can possess a capable substitute;
- borrowing is a request with policy and availability constraints;
- high-demand equipment can create scheduling conflict without villainy;
- the provider remains authoritative over whether a loan occurs.

No USGS equipment list, policy text or institutional identity is imported into Ouros canon.

## Source 5 — USGS ANSS depot request workflow

Public source:
https://www.usgs.gov/programs/earthquake-hazards/science/anss-depot-requests

The public workflow asks requesters to identify the person, delivery location, equipment, serial/property identifiers and the problem being addressed. This is useful as a provenance pattern: a resource request can carry enough identity and purpose to be audited later.

Reusable Ouros structure:

- requests should have stable identities;
- the requested capability/resource can be named separately from destination and requester;
- the purpose/problem should remain attached to the request;
- a fulfilled request can later be traced back to the obligation that generated it.

## Source 6 — P.U.C.L. PTU actual play

Public sources:
https://podcasts.apple.com/us/podcast/p-u-c-l-ptu/id1448567421
https://podnews.net/podcast/i5kev/episodes

The public listing identifies P.U.C.L. PTU as a Pokémon Tabletop United actual-play series. Public episode descriptions show repeated use of a regional job board, ordinary jobs for local institutions, travel between locations, downtime, training and later consequences.

Reusable narrative lesson:

A PTU campaign can sustain play through ordinary institutional work and local requests between larger encounters. A request can originate from a board or institution and send characters into the world without requiring every assignment to be a conspiracy or boss fight.

Ouros transformation:

- NPC obligations may originate from ordinary institutional work;
- missing equipment can become a practical obstacle inside an otherwise normal job;
- solving the obstacle can involve communication, travel, lending or rescheduling;
- the job itself remains independent from the resource-acquisition process.

No P.U.C.L. characters, Belleza locations, Monument structure, episode plots, dialogue, job-board text or encounter design is copied.

## Cross-check against existing Ouros material

Repository-wide search before writing found explicit owners for:

- Pass 338 resource availability and intent gating;
- Pass 339 temporal reservation lifecycle;
- Pass 340 operational readiness projection;
- world travel;
- communication delivery;
- audience resolution;
- agenda selection;
- shared-equipment and maintenance domain layers.

No existing executable owner was found for deriving safe next-step world intents from a resource-blocked task.

Pass 338 explicitly deferred `ACQUIRE_RESOURCE`, `REQUEST_RESOURCE`, `WAIT_FOR_RESOURCE` and resource travel. Pass 340 still lists resource-acquisition/request intents among deferred work.

Therefore Pass 341 should bridge existing owners instead of introducing a new inventory, ownership, maintenance or communication system.

## Proposed invariants

`RESOURCE_NEEDED != RESOURCE_REQUESTED`

`RESOURCE_REQUESTED != REQUEST_ACCEPTED`

`REQUEST_ACCEPTED != RESOURCE_TRANSFERRED`

`RESOURCE_TRANSFERRED != RESOURCE_ARRIVED`

`RESOURCE_FOUND_REMOTE != ACCESS_AUTHORIZED`

`RESOURCE_RESERVED_FOR_ACTOR != ACTOR_AT_RESOURCE_LOCATION`

`TRAVEL_PLAN_DERIVED != TRAVEL_COMPLETED`

`REQUEST_INTENT_DERIVED != MESSAGE_DELIVERED`

`REQUEST_DELIVERED != PROVIDER_CONSENT`

`PROVIDER_CONSENT != CHECKOUT`

`WORLD_RESOURCE_ACQUIRED != PTU_ITEM_EFFECT_LEGAL`

## Implementation direction

The bounded executable slice should derive recovery options only from facts that existing state can justify:

- if a usable matching resource is held by another known actor, derive `REQUEST_RESOURCE` addressed to that holder;
- if a matching resource is reserved for the blocked actor at another location, derive travel using the existing semantic travel graph;
- if another actor currently owns the reservation claim, derive `WAIT_FOR_RESOURCE` rather than stealing or overriding it;
- if an unheld remote resource is merely known to exist, fail closed because access authority is not established;
- if no usable candidate exists, expose that narrow reason rather than creating a resource.

The slice must not transfer, reserve, checkout, consume, repair, approve or deploy resources. Those transitions remain with their authoritative owners.

## Mechanical dependency note

The reduced recovery layer is world-agent planning and needs no AutoPTU combat capability.

A later rich encounter may require exact families independently: targeting/range/LoS for tool targeting; base movement for ordinary tactical approach; complete movement for carrying, dragging, interception or rescue; action economy for handing over or using equipment; full lifecycle for timed effects; damage/status/hazard families if the encounter invokes them; exact Move, Ability, Item or Trainer Feature support when used; AI tactical policy for protect/deliver/withdraw objectives; and Minecraft/Cobblemon/Craftics only for presentation/playback.

No mechanical family is promoted by this research note.
