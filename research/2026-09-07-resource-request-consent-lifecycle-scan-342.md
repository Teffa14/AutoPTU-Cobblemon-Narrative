# Resource request consent and response lifecycle scan — Pass 342

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-07

## Research question

Pass 341 can derive a `REQUEST_RESOURCE` recovery option when another known actor holds a needed resource. The missing world-state seam is what happens after that option exists.

This pass asks how real resource-sharing systems separate request, provider consent, discrepancy, pickup, temporary control, expiry and later withdrawal so Ouros can model ordinary logistics without turning a message into possession.

Nothing in this note establishes Ouros institutional law, ownership, PTU Item behavior or canon.

## Repository duplication check

The recursive repository tree, current focus, canon layer and relevant resource owners were inspected before writing.

Existing owners already cover:

- Pass 338 resource availability gating;
- Pass 339 temporal reservation and checkout/return;
- Pass 340 operational readiness projection;
- Pass 341 recovery-option derivation;
- communication delivery, audience resolution and selective replanning;
- travel, custody, maintenance/inspection and shared-equipment domains elsewhere in the repository.

No existing executable owner was found for a provider response lifecycle with explicit acceptance, rejection, cancellation, expiry and withdrawal while preserving `REQUEST_ACCEPTED != RESOURCE_TRANSFERRED`.

## Source 1 — FEMA / NIMS order and acquire

Source:
https://emilms.fema.gov/_is0700b/groups/293.html

Supporting source:
https://training.fema.gov/emiweb/is/is703b/studentmanual/is0703%20sm.pdf

High-level evidence:

NIMS separates identifying a resource requirement from ordering/acquiring it. When another jurisdiction or organization is asked to provide a resource, the providing organization must consent. The provider can also communicate discrepancies between what was requested and what is actually available for delivery.

Reusable structure for Ouros:

1. need exists;
2. request is authored;
3. provider receives/evaluates it;
4. provider accepts, rejects or offers a different available resource;
5. mobilization/transfer remains later work.

Transformation rule:

No FEMA emergency-management authority, incident-command procedure or legal regime is imported into Ouros. The reusable lesson is state separation and provider agency.

Derived boundary:

`REQUEST_CREATED != PROVIDER_CONSENT`

`PROVIDER_CONSENT != RESOURCE_MOBILIZED`

`REQUESTED_RESOURCE != OFFERED_RESOURCE`

## Source 2 — FEMA / USFA current resource-management guidance

Source:
https://www.usfa.fema.gov/a-z/nims/managing-resources.html

Page reviewed May 1, 2026.

High-level evidence:

Current NIMS guidance emphasizes schedules for requested/delivered resources, operational priorities and provider-side planning through deployment and demobilization. The supplier remains an active actor in the process rather than becoming a passive inventory endpoint when a request is made.

Reusable Ouros structure:

A request can be valid while remaining unresolved. Provider obligations, timing and competing uses can justify refusal, delay or later withdrawal without requiring sabotage or deception.

Derived boundary:

`VALID_REQUEST != GUARANTEED_FULFILLMENT`

## Source 3 — FEMA National Resource Hub

Source:
https://preptoolkit.fema.gov/web/national-resource-hub

High-level evidence:

The National Resource Hub explicitly states that its inventory systems do not themselves perform resource requests, deployments or tracking. Resource description and discovery therefore remain distinct from operational deployment authority.

Reusable Ouros structure:

Pass 338 can know that a resource exists. Pass 341 can know whom to ask. Neither fact grants deployment, transfer or ownership.

Derived boundary:

`RESOURCE_DISCOVERABLE != RESOURCE_DEPLOYABLE`

## Source 4 — University of Illinois loanable technology policy

Source:
https://www.library.illinois.edu/sc/loanable-technology/technology-policies/

High-level evidence:

The policy distinguishes bookings from pickup, permits pickup by the borrower or an authorized proxy, notes that reservations depend on prior users returning equipment, and keeps responsibility attached to the borrower until return issues are resolved.

Reusable Ouros structure:

An accepted booking or loan request can still require a separate pickup/handoff step. Another actor may be authorized to collect only when proxy authority exists. A prior holder can prevent later availability simply by still possessing the object.

Derived boundaries:

`BOOKING_ACCEPTED != PICKUP_COMPLETE`

`PICKUP_BY_OTHER_ACTOR != PROXY_AUTHORIZED`

`DUE_TO_RETURN != RETURNED`

No Illinois policy, penalties, loan duration or institutional rule is copied into Ouros.

## Source 5 — Pokémon Sword/Shield Battle Stadium Rental Teams

Source:
https://swordshield.pokemon.com/en-au/gameplay/pokemon-battle-stadium/

High-level evidence:

The official Battle Stadium material describes Rental Teams as a way to use battle teams created through the game's rental system. The structural value for Ouros is temporary authorized use without transferring the underlying ownership identity.

Reusable abstraction:

`AUTHORIZED_TEMPORARY_USE != OWNERSHIP_TRANSFER`

No Rental Team mechanics, ranking rules, online-service requirements, characters or battle progression are imported.

## PTU / community search

A fresh search again surfaced long-running PTU actual plays such as Pokémon World Tour: United, The Reckless Rollers, Pokémon Rollout!, Adventures in the Millennium and previously processed one-shots. The repository search confirmed these families have already been used repeatedly, so Pass 342 does not reprocess them merely to satisfy a source count.

This pass instead treats the PTU/Caelo source set as mechanical authority only when the proposed lifecycle invokes actual Item, Skill, Feature, movement or battle rules.

No request/loan mechanical rule was established from a fan campaign.

## Design lessons extracted

### Provider agency should be explicit

The holder or supplying institution can accept, reject, fail to answer or later withdraw consent before physical handoff. A requester cannot infer consent from silence.

### Response and fulfillment should have separate clocks

A provider can answer immediately while the resource remains elsewhere. A delayed answer can arrive after the request's operational window has expired.

### Alternate offers need provenance

A provider may respond that the exact requested resource is unavailable while a different resource is available. The response should record the alternate identity; it must not silently rewrite the original request.

### Expiry should be derived, not destructive

An unanswered request may become operationally expired at a semantic tick. The original request remains historical evidence.

### Acceptance may later be withdrawn

Before transfer, new obligations, faults, reservations or readiness information can make a previously accepted offer unavailable. Withdrawal should be a new event, not deletion of the acceptance.

### Request state must remain independent of communication transport

A request object can exist before delivery. The existing communication runtime remains responsible for whether the provider actually receives the message. Pass 342 deliberately models the request/response ledger, not message transport.

## Original Ouros invariants proposed from the research

`REQUEST_OPTION != REQUEST_SUBMITTED`

`REQUEST_SUBMITTED != REQUEST_DELIVERED`

`REQUEST_DELIVERED != REQUEST_ACCEPTED`

`REQUEST_ACCEPTED != RESOURCE_RESERVED`

`REQUEST_ACCEPTED != RESOURCE_TRANSFERRED`

`REQUEST_ACCEPTED != RESOURCE_CHECKED_OUT`

`REQUEST_REJECTED != REQUEST_WAS_INVALID`

`REQUEST_EXPIRED != REQUEST_DELETED`

`ACCEPTANCE_WITHDRAWN != ACCEPTANCE_NEVER_HAPPENED`

`ALTERNATE_OFFERED != ORIGINAL_REQUEST_REWRITTEN`

`TEMPORARY_USE != OWNERSHIP_TRANSFER`

## Mechanical-source boundary

The repository README identifies PTU Core, Pokédex material and the Caelo source set as mechanical authorities to validate when exact rules are invoked.

Pass 342 adds no PTU/Caelo Item effect, borrowing Skill check, social DC, Feature, payment, carrying capacity, movement permission or combat action.

The request lifecycle is world-state infrastructure and can run without AutoPTU.

## New narrative affordances

The seam supports stories where:

- a technician agrees to lend a field meter but the requester assumes delivery while the provider expects pickup;
- an accepted resource becomes unavailable before handoff because a fault is discovered;
- a request expires while the provider is unreachable;
- the provider offers a different capable unit and the requester must decide whether the work can use it;
- a worker sincerely says “they said yes” while still lacking possession;
- two schedules diverge because consent and physical transfer happened at different times;
- a later dispute can reconstruct the exact request and response history without an omniscient summary.

These structures create consequences through ordinary work rather than forced villains.

## Deferred questions

- communication coordinator that materializes a request only after actual message delivery;
- provider authority versus mere physical holding;
- institutional resource pools;
- delegated approval/proxy rules;
- accepted-request to reservation transition;
- transfer/handoff world events;
- delivery versus pickup responsibility;
- quantity/capacity requests;
- queue fairness and waitlists;
- checkpoint persistence;
- expiry notification and replanning;
- exact PTU/Caelo validation if a resource becomes a mechanical Item.
