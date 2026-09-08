# Resource handoff, proxy pickup and custody scan — Pass 343

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-07

## Question

What reusable structures should Ouros use after a resource request has been accepted, when the actual object still needs to pass from one actor to another?

This scan follows Pass 342. It does not establish PTU mechanics, Ouros canon, ownership law or institution-specific policy.

## Repository overlap check

Before external research, the current recursive tree and targeted searches were inspected.

Existing owners already cover:
- resource identity and local availability: Pass 338;
- reservation windows and checkout/return separation: Pass 339;
- technical readiness projection: Pass 340;
- blocked-work recovery intents: Pass 341;
- request/provider-consent lifecycle: Pass 342;
- specialized evidence custody and other domain custody systems elsewhere in the repository.

The missing global seam was physical handoff after provider acceptance.

Pass 342 explicitly deferred handoff, courier movement, physical delivery, pickup, proxy pickup, custody transfer and checkout.

## Source: University of Hawaiʻi CIS equipment-loan policy

Public source:
https://www.cis.hawaii.edu/equipment/

Useful source facts:
- equipment may be reserved, picked up and returned through a defined office;
- faculty/staff may authorize another named person to pick up and return equipment;
- the pickup person's identity is checked against the authorized name;
- the original borrower remains responsible for care/security even when an authorized representative performs pickup;
- reservation, pickup, return and extension are distinct operations;
- a no-show at pickup remains distinct from cancellation.

Reusable abstraction:
- beneficiary/accountable borrower and physical receiving actor can be different people;
- proxy authority should be explicit and scoped;
- proxy pickup does not imply that the beneficiary already possesses the object;
- a handoff should record identity, place and time.

Transformation boundary:
No University of Hawaiʻi names, sanctions, operating hours, campus limits or exact loan periods become Ouros canon.

## Source: Metropolitan State University of Denver material-lending policy

Public source:
https://www.msudenver.edu/wp-content/uploads/2021/09/University_Material_Lending_Policy_20210601.pdf

Useful source facts:
- a loan workflow identifies the borrower and the specific material;
- checkout includes confirming the item's condition;
- pickup and return time/place are arranged explicitly;
- condition is confirmed at pickup;
- signed checkout documentation records disposition and return expectations.

Reusable abstraction:
A transfer record can preserve the condition/context observed at the handoff without claiming that this observation proves future readiness.

Transformation boundary:
No legal obligations, signatures, student policy or institutional procedure is imported as Ouros law.

## Source: National Archives direct-offer transfer guidance

Public source:
https://www.archives.gov/records-mgmt/accessioning/direct-offer.html

Useful source facts:
- physical delivery and pick-up can be separate transfer modes;
- the receiving organization can impose scheduling/receiving procedures;
- physical receipt and final acceptance of custody can be represented as distinct states.

Reusable abstraction:
Arrival at a place does not necessarily equal accepted custody. For the first executable Ouros handoff seam, a custody transfer occurs only after an explicit authorized handoff event.

Transformation boundary:
No archival accession rules, classified-record rules or NARA procedures become Ouros policy.

## Source: USGS HGB equipment-use policy

Public source:
https://water.usgs.gov/usgs/espd/hgb/equipment/equipment_use.html

Useful source facts:
- equipment is scheduled individually;
- the current user can be responsible for sending equipment to its next scheduled destination;
- extensions depend on later scheduled use.

Reusable abstraction:
A resource can move through a chain of temporary custodians. The next destination is a future obligation; it is not proof that the next user already holds the object.

Transformation boundary:
No USGS scheduling duration, priority policy, technical procedure or equipment catalog is imported.

## Pokémon / PTU scan

Fresh public searches were run for PTU actual plays, campaign listings and Pokémon quest structures. Several prominent actual plays surfaced again, including Pokémon World Tour: United, The Reckless Rollers and Adventures in the Millennium. These have already been used elsewhere in the repository, so they were not reprocessed as new provenance for this pass.

A 2025 public PTU campaign recruitment post described an original-setting campaign prioritizing roleplay and exploration over combat. This is weak evidence and is retained only as corroboration that ordinary noncombat obligations can be legitimate PTU play. It is not used as a mechanical source.

Public source:
https://www.reddit.com/r/lfg/comments/1l43cev

No distinctive plot, character, region or house rule is imported.

## High-level Ouros lessons

1. Provider consent can authorize a later handoff without moving the object.
2. Borrower/accountable actor and physical recipient may differ.
3. Proxy pickup must identify the proxy explicitly.
4. The provider must still possess the actual unit at handoff time.
5. The object must physically be at the authored handoff location.
6. Handoff windows can expire without deleting the earlier consent.
7. A transfer should create append-only custody history.
8. Condition observed at handoff is provenance, not automatic technical-readiness authority.
9. Pickup and delivery are different coordination modes even if both culminate in a custody transfer.
10. A later courier system should be built from successive custody/travel events rather than teleporting resources.

## Proposed invariants

`REQUEST_ACCEPTED != HANDOFF_AUTHORIZED`

`HANDOFF_AUTHORIZED != RESOURCE_TRANSFERRED`

`ACCOUNTABLE_BORROWER != PHYSICAL_RECIPIENT`

`PROXY_AUTHORIZED != REQUESTER_POSSESSES_RESOURCE`

`RESOURCE_AT_DESTINATION != CUSTODY_ACCEPTED`

`TRANSFER_RECORDED != RESOURCE_TECHNICALLY_READY`

`TRANSFER_RECORDED != PTU_ITEM_EFFECT_LEGAL`

## Mechanical boundary

This research adds no PTU/Caelo rule.

Any later structured encounter involving carrying, interception, dropping, forced movement, tactical item use, damage to equipment or timed delivery must declare the exact engine capability families it depends on. A world-level custody transfer does not prove any of those mechanics exist.
