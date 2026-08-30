# Ouros Narrative Research — Service Reservation, Ticket, Pass & Admission Continuity — Pass 140

Status: RESEARCH / PROVENANCE ONLY. Not established Ouros canon.
Date: 2026-08-29

## Research question

What durable narrative structures can Ouros use to represent reservations, tickets, passes and admission rights without collapsing them into payment, credentials, queues, transport operations, event operations or inventory objects?

This pass follows a complete recursive inspection of the narrative repository. The tree returned `truncated: false`. Relevant neighboring layers were then checked directly, especially Service Access / Queues / Appointments, Credentials / Authorizations, Finance / Sponsorship / Risk, transport continuity layers, event operations, Material Culture and the PTU/Caelo source scan.

The missing connective state is an entitlement lifecycle. Existing systems can say that a service exists, that a slot or queue exists, that money moved, that an actor holds a professional authorization, or that a train/ferry/event is operating. They do not own a neutral cross-domain record for a bounded right such as "this holder may use this service under this scope," together with issuance, representation, validation, consumption, reissue, supersession and disruption handling.

This pass does not establish a universal Ouros ticketing network, fare system, identity document, digital wallet, refund law, transferability rule or mandatory admission control.

## Existing Ouros boundaries checked

### Service Access, Queues & Appointments

Pass 70 already owns access requests, appointment windows, walk-ins, queue entries, check-in and service-start coordination. It explicitly states that it does not create a universal ticketing system.

Therefore a reservation for a service slot may reference an entitlement, but queue position, appointment status and the ticket/pass remain separate facts.

### Credentials & Authorizations

The credentials layer owns institutionally issued or recognized scoped authority such as qualifications, roles and permissions. A ticket or travel pass normally represents bounded service entitlement rather than professional authority.

A venue may require both a credential and an admission entitlement. Passing one check does not satisfy the other.

### Finance

Finance already distinguishes promises, transfers, receipts, refunds and reversals. Payment can create or support an entitlement only when an owning policy says so.

`PAYMENT_RECEIVED != ENTITLEMENT_ISSUED` remains important. A refund record likewise belongs to Finance even when triggered by cancellation of an entitlement.

### Transport and Event owners

Transport layers own whether the service, departure, vehicle, berth, platform or route is operating. Event Operations owns whether an event or activity is actually running.

An entitlement can be valid while the underlying service is disrupted. It cannot force the service to exist.

### Material Culture

A paper ticket, card, wristband, stamped token or device can have physical representation, custody and provenance. The physical object does not become the service right by default.

Destroying a representation must not silently cancel the underlying record unless the authored system is explicitly bearer-only.

## Pokémon source scan

### Magnet Train Pass

Source: https://bulbapedia.bulbagarden.net/wiki/Pass
Source: https://bulbapedia.bulbagarden.net/wiki/Magnet_Train

Public reference material describes a Pass required to board the Magnet Train between Goldenrod and Saffron. The train itself also has an independent operational prerequisite: restoring the Power Plant permits the service to run.

Reusable structure:

- service operation and passenger entitlement are separate;
- holding a valid pass does not repair or activate the underlying service;
- one pass can cover repeated use over a defined network relationship rather than one single departure;
- validation occurs at the service boundary rather than by direct item activation.

Ouros transformation:

Represent persistent or multi-use passes as scoped entitlements whose validity can coexist with service outages. Never interpret the presence of a token as proof that the route is operating.

### Tri-Pass and Rainbow Pass

Source: https://bulbapedia.bulbagarden.net/wiki/Tri-Pass
Source: https://bulbapedia.bulbagarden.net/wiki/Rainbow_Pass
Source: https://bulbapedia.bulbagarden.net/wiki/Seagallop

FireRed/LeafGreen separates a limited network pass for the first three islands from a later successor pass that broadens the accessible network. The Rainbow Pass succeeds the Tri-Pass while retaining access to the earlier scope.

Reusable structure:

- entitlement scope can expand without creating a new physical transport network;
- a successor entitlement can supersede an earlier one while preserving historical provenance;
- the network owner still decides which services actually operate;
- destination scope is a first-class field rather than an implicit boolean "has ticket".

Ouros transformation:

Use versioned scope and explicit supersession. Do not erase the old entitlement event when a broader pass is issued.

### MysticTicket and AuroraTicket

Source: https://bulbapedia.bulbagarden.net/wiki/MysticTicket
Source: https://bulbapedia.bulbagarden.net/wiki/AuroraTicket
Source: https://bulbapedia.bulbagarden.net/wiki/Sevii_Island_passes

These tickets demonstrate layered prerequisites. In FireRed/LeafGreen, the special-destination ticket is accepted only after the broader Rainbow Pass has been obtained. In Emerald, the S.S. Ticket is the corresponding prerequisite.

Reusable structure:

- possession of a special entitlement can remain insufficient without a separate prerequisite;
- entitlement composition can be conjunctive rather than one token replacing every other access rule;
- a special destination can use the same transport operator while requiring a more specific access record.

Ouros transformation:

Allow an access decision to evaluate several independent requirements by reference. Do not merge all requirements into a single opaque "access level".

### S.S. Ticket

Source: https://bulbapedia.bulbagarden.net/wiki/S.S._Ticket

The same generic ticket concept appears in different games for different vessels and travel contexts. In one case it grants boarding while a ship is present; in another it supports continuing travel between regions.

Reusable structure:

- visible labels can repeat while the underlying issuer, scope and service relationship differ;
- a ticket should be identified by its provenance and entitlement record, not only by displayed name;
- access can depend on a temporal service state such as the vessel still being present.

Ouros transformation:

A displayed object labelled "Ferry Ticket" or "Festival Pass" is insufficient to resolve validity without issuer, scope and state.

## Operational source scan

### Amtrak eTicketing

Source: https://www.amtrak.com/eticket

Amtrak distinguishes booking/reservation, the eTicket representation, itinerary changes, ticket updates, reserved and unreserved service, cancellation and later monetary credit/refund handling.

Reusable structure:

- reservation and ticket representation are related but distinct records;
- modifying the itinerary can update the ticket while retaining the continuity of the journey record;
- a missed reserved departure can invalidate future use under a specific policy;
- monetary settlement after cancellation is a later financial event, not the same event as cancellation itself;
- one representation can cover several travelers or travel segments.

Ouros transformation:

Keep entitlement identity, representation identity, covered actors, covered segments and financial settlement separate. Do not import Amtrak fare rules, deadlines, penalties or legal conditions.

### National Rail ticket validity

Source: https://www.nationalrail.co.uk/ticket-types/tickets/las/

Public National Rail material exposes explicit validity windows and treats seat reservation as a related but separate concept.

Reusable structure:

- ticket validity can be time-bounded;
- travel entitlement and seat assignment need not be the same object;
- refund eligibility can depend on a different state machine from travel validity.

Ouros transformation:

A ticket can be valid for a service class or time window while no particular seat is assigned. Seat/cabin/berth allocation remains with the service owner or a specialized reservation record.

### Transport for London Oyster use

Source: https://visitorshop.tfl.gov.uk/fr/help

TfL describes a reusable card that is presented at journey boundaries, with journey charging determined from recorded entry/exit behavior.

Reusable structure:

- physical or digital carrier can persist across many journeys;
- one carrier can mediate multiple entitlement/payment events without being identical to any one journey;
- validation at the start and end can be distinct events.

Ouros transformation:

Permit reusable media and boundary validation if a local institution is authored to work that way. Do not assume tap systems, stored-value cards or distance fares exist in Ouros.

## PTU / Caelo cross-check

Internal source: `research/2026-08-18-source-scan.md`

The internal scan supports persistent locations, Jobs, social activity, exploration and authored location mechanics. It does not establish a universal ticket, reservation, fare, admission, identity-validation or refund subsystem.

PTU/Caelo mechanics therefore remain authoritative only when an exact rule exists. Narrative entitlement records must not create combat bonuses, Trainer Features, item effects or travel abilities by themselves.

Remain UNKNOWN unless exact source evidence is found:

- universal ticket prices or fare tables;
- generic reservation checks;
- universal transferability rules;
- Trainer Skill checks for ticket validation;
- generic forgery detection DCs;
- universal no-show penalties;
- seat-assignment mechanics;
- automatic discounts from Trainer Classes, Features or League rank;
- generic free travel from Pokémon Type, species, Move or Ability;
- ticket objects with PTU Item combat effects;
- battle victory granting admission or validating a pass;
- universal refund mechanics;
- universal digital ticketing technology.

## Narrative design lessons

### Entitlement, representation and use should have separate identities

A paper ticket can be lost while the issuer still retains a valid reservation. A bearer-only token can instead be the only authoritative representation. Ouros must know which model a specific institution uses rather than choose globally.

### Scope must be inspectable

Useful scope dimensions include:

- owning service or network;
- origin/destination or geographic zone;
- event/activity;
- actor or group binding;
- service class;
- date/time window;
- allowed number of uses;
- specific departure/session;
- seat/cabin/berth/area allocation reference;
- prerequisite entitlement refs;
- transfer policy ref.

### Validation is an event

A validator can observe a representation and produce a decision at a specific time. The decision should preserve what was checked and under which rule version.

A later rule change does not retroactively make an earlier valid validation wrong.

### Consumption is not universal

Some entitlements are single-use, some multi-use, some recurring, some duration-based and some are merely proof of an already-authorized reservation. Never apply a global "scan = consumed" rule.

### Disruption should preserve provenance

If a service is canceled, diverted or relocated, the entitlement can enter a disrupted, protected, rebooking-required or unresolved state according to authored policy. The original entitlement history remains intact.

### Ambiguity can remain legitimate

An old paper ticket can survive after the issuer's records were lost. The world may know that the object is historically genuine without being able to prove whether it remains usable. `HISTORICALLY_AUTHENTIC != CURRENTLY_VALID`.

## Candidate Ouros worldbuilding opportunities

- recurring commuters whose pass remains valid through a temporary service suspension;
- an island community that preserves old ferry passes as family artifacts after a network redesign;
- a festival that uses locally issued day marks while outsiders expect reservations;
- a tournament where registration, qualification, admission and spectator seating are four separate systems;
- a rail operator that reissues representations after a station relocation while preserving the same underlying entitlement;
- a closed attraction whose old tickets are collectible but no longer provide entry;
- a public service where access is free but still reservation-controlled because capacity is finite;
- a temporary evacuation transport service where no fare exists but each seat allocation is still tracked;
- a historical mystery where the date printed on a ticket proves planned access but not actual attendance.

## Research exclusions

This pass does not copy protected dialogue, characters, complete plots, proprietary fare formulas, real-world legal requirements or exact commercial procedures.

Pokémon references are used only to identify high-level access structures. Real transport systems are used only for event/state separation and provenance architecture.

No external source is treated as Ouros canon or PTU rules authority.

## Conclusion

A dedicated service-entitlement continuity layer can connect transport, events, appointments, commercial services and institutions while preserving their authority boundaries. Its principal value is preventing the generator from collapsing reservation, payment, token possession, validation, admission and actual service use into one boolean fact.
