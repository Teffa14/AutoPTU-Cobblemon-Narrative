# Pass 99 Research — Postal, Courier & Parcel Logistics

Status: research/provenance only. Not Ouros canon. No mechanics are established by this file.

Date: 2026-08-22

## Why this pass exists

The repository already has strong layers for Communications, Travel, Workplaces, Rail, Aerial Transport, Maritime Transport, Credentials, Custody, Finance, Illicit Networks and Material Provenance.

`media-communications-information-layer.md` already allows a `COURIER` communication channel, a postal hub as infrastructure, and message delivery states. That layer answers whether information was sent, delivered or acknowledged.

A different state problem remains unresolved: the physical journey of a letter, parcel, specimen, medicine shipment, repaired object, contest entry, archive loan or other tangible item.

This pass studies the reusable structure of physical delivery without creating a second communication system or a generic supply-chain simulator.

## Sources inspected

### Pokémon Mystery Dungeon: Rescue Team DX — Pelipper Post Office

Official source: Pokémon Company, Rescue Team DX world overview.
https://mysterydungeon.pokemon.com/en-us/world/

The official overview states that job requests can arrive by letters in the rescue-team mailbox or appear on the bulletin board outside Pelipper Post Office. Pelipper Post Office is a persistent institution rather than a transient quest prompt.

Reusable structure:

- a delivery institution can act as quest intake;
- mailbox delivery and public bulletin-board publication are different channels;
- a request can have a destination and remain pending until accepted;
- the same hub can connect routine correspondence with expedition-scale work;
- successful delivery of information does not mean the requested field task is complete.

Ouros adaptation:

A physical post/courier network can produce letters, parcels and service notices while Communications remains responsible for the claims inside a message. A posted request and a sealed private letter should not become the same visibility state.

### Pokémon Mystery Dungeon — Pelipper delivery to a team base

Public official Chunsoft archive:
https://www.spike-chunsoft.co.jp/pages/games/pokedun_i/rescue01.html

The archived game page describes rescue jobs being delivered to the team's mailbox by Pelipper and other requests being posted at the post office.

Reusable structure:

- scheduled/local delivery can continue while the player is away;
- delivery destination can be an institution or base rather than a person standing in one place;
- incoming work can accumulate without requiring the sender and recipient to share a scene.

Ouros adaptation:

A mailbox, reception desk, club headquarters or workshop can be a valid delivery endpoint if its access policy allows it. Physical receipt by an institution does not automatically prove the intended individual read the contents.

### Pokémon: Dragonite and the Special Delivery

Official Pokémon news article, English release dated 2026-05-19:
https://www.pokemon.com/us/pokemon-news/watch-pokemon-dragonite-and-the-special-delivery-on-youtube

The official synopsis centers on a young postal worker who finds a letter without an address, identifies its sender, and then must solve the last-mile/interregional delivery problem because the intended recipient is working far away.

Reusable structure:

- sorting is a distinct job from carriage;
- malformed or incomplete addressing can become a real problem before transport begins;
- finding the sender can be part of resolution rather than guessing the destination;
- urgent delivery can cross regional boundaries;
- a postal worker can have a career arc independent of battling;
- the package/letter remains the same object while custody and route change.

Ouros adaptation:

Treat address resolution, sorting, transport, local handoff and final delivery as separate events. An unresolved address should create an exception state, not an omniscient quest marker pointing to the intended recipient.

Copyright boundary:

Do not copy Hana, Rio, the postmaster, their personal story, dialogue, scene sequence or the short's exact route. Only the operational structure is reused.

### Delibird Pokédex

Official Pokémon Pokédex:
https://www.pokemon.com/uk/pokedex/delibird

The Pokédex identifies Delibird with carrying food and stories of lost people surviving because of that food.

Reusable structure:

- some species can have authored cultural associations with carrying supplies;
- delivery-related behavior can generate rescue/support stories rather than only commerce;
- a Pokémon may carry its own resources without being an institutional courier.

Ouros guardrail:

Delibird's lore does not establish generic payload mass, mail capacity, flight endurance, passenger carrying, delivery accuracy, inventory slots or a PTU courier bonus. Any mechanical Capability must come from PTU/Caelo/AutoPTU evidence for the exact individual.

### Public PTU actual-play thread — secure delivery as a route-aligned job

Public PTU play thread on Eagle Time:
https://eagle-time.org/showthread.php?mode=linear&pid=87702&tid=792

A campaign scene includes a character volunteering to make a secure delivery because the group is already travelling in the relevant direction and appears trustworthy enough to be considered for the task.

Reusable structure:

- delivery work can emerge from an existing journey rather than spawning a dedicated trip;
- trust and institutional affiliation can affect who is offered custody;
- route alignment can make a small commission worthwhile;
- the parcel can add stakes to travel without becoming a combat objective every time.

Ouros adaptation:

The generator should prefer piggybacking delivery work onto real planned movement where reasonable. This avoids filler travel and helps small jobs connect to the living route network.

Copyright boundary:

Do not reuse the campaign's characters, dialogue, parcel, destination or plot context.

### Universal Postal Union — item identity and supply-chain handoffs

UPU postal supply-chain overview:
https://www.upu.int/en/postal-solutions/programmes-services/postal-supply-chain

UPU S10 item-identifier standard:
https://www.upu.int/UPU/media/upu/files/postalSolutions/programmesAndServices/standards/S10-12.pdf

The UPU describes postal transport as a multi-stakeholder physical supply chain and uses a stable item identifier across processing. The S10 standard also makes an important conceptual distinction: one item has one authoritative identifier even if the physical representation of that identifier appears more than once.

Reusable structure for game state:

- physical item identity survives handoffs;
- a route can include multiple operators and modes;
- tracking events are observations of handling, not teleportation;
- labels and routing data can be wrong while item identity remains stable;
- custody transfer should append events rather than replace history;
- duplicated labels must not duplicate the physical object.

Ouros adaptation:

Ouros does not need to reproduce real-world UPU numbering, customs law, tariffs or postal regulation. The useful principle is stable shipment identity plus append-only handling events.

## Synthesis for Ouros

### 1. Separate information delivery from physical delivery

A letter contains an information packet governed by Communications.

The envelope is a physical item governed by Postal Logistics.

If the envelope reaches a reception desk, the physical delivery may be complete to that endpoint while the intended actor still has not read or acknowledged the message.

For parcels, samples, fossils, medicine, contest entries or repaired equipment, there may be no separate message at all.

### 2. Stable item identity is more important than perfect tracking

A physical shipment should retain one `postal_item_id` or reference to an existing item/asset ID across:

acceptance -> sorting -> dispatch -> transport -> handoff -> local delivery -> receipt/exception/return.

Tracking can have gaps. A missing scan is not proof that the object disappeared during that leg.

### 3. Planned route and actual route must diverge safely

A parcel may be planned for rail, rerouted to ferry, held overnight at a hub, then delivered by a local courier.

Travel owns whether those connections and services are usable.

Postal Logistics records which leg was actually attempted and completed.

### 4. Address resolution is a gameplay problem without omniscience

Useful exception states:

- incomplete destination;
- outdated address;
- destination institution moved;
- recipient travelling;
- recipient unknown at destination;
- access denied at final endpoint;
- no safe route currently exists;
- physical location valid but recipient identity uncertain.

The system should never reveal the answer merely because delivery is a quest objective.

### 5. Handoff state creates small stories naturally

A shipment may pass through:

- sender;
- intake clerk;
- sorter;
- hub custodian;
- vehicle/operator;
- regional transfer;
- local depot;
- final courier;
- reception desk;
- recipient.

Each transition can produce provenance without every step becoming a scene.

Expand only when a decision or exception matters.

### 6. Failed delivery is useful state

Useful terminal or temporary outcomes include:

- delivered;
- delivered to authorized endpoint;
- recipient unavailable;
- address exception;
- route delayed;
- held for pickup;
- refused;
- returned to sender;
- damaged;
- missing;
- recovered after missing;
- custody disputed;
- delivery attempt cancelled before transfer.

`MISSING` should describe logistics knowledge, not metaphysical truth. The item may still exist somewhere in world state.

### 7. Physical post can make world change legible

Postal friction can expose state elsewhere:

- a washed-out road creates mail delay;
- a rail closure changes sorting volume at a ferry hub;
- a festival overwhelms a small depot;
- a moved household keeps receiving old mail;
- a hospital referral arrives before a physical sample;
- a museum loan reaches the destination but its paperwork does not;
- a correction reaches one settlement days after another;
- a former resident's forwarding record becomes historically relevant.

These outcomes connect existing systems without manufacturing unrelated quests.

## Original Ouros directions suggested by the research

Candidate design objects:

- `POSTAL_SERVICE`
- `POSTAL_HUB`
- `POSTAL_ITEM`
- `ADDRESS_RECORD`
- `ROUTING_PLAN`
- `DELIVERY_LEG`
- `HANDOFF_EVENT`
- `DELIVERY_ATTEMPT`
- `POSTAL_EXCEPTION`
- `FORWARDING_RECORD`
- `RETURN_EVENT`
- `PHYSICAL_RECEIPT`

Candidate narrative loops:

1. ordinary delivery -> route disruption -> reroute -> delayed arrival -> downstream consequence;
2. incomplete address -> sender research -> destination hypothesis -> safe attempt -> correction;
3. institutional parcel -> custody handoffs -> missing event -> case opens -> object recovered -> provenance preserved;
4. seasonal route -> accumulated mail -> reopening -> community event without combat;
5. long-term postal career -> sorting -> local route -> difficult route -> regional coordination -> mentor role.

## Mechanical boundary

This research does not define:

- carrying capacity;
- flight endurance;
- mounted transport;
- item weight rules;
- theft checks;
- chase rules;
- interception;
- package HP;
- damage from dropped parcels;
- courier initiative;
- Trainer Skill modifiers;
- route Weather effects;
- Pokémon delivery bonuses;
- mail-related Features;
- automatic teleportation between hubs.

Those require exact PTU/Caelo rules and implementation evidence.

## Engine implications

Most postal state belongs outside the battle core.

A delivery encounter may use the VERIFIED foundations for static targeting, base movement, calculations, action economy and legal-action generation.

Mechanically rich versions commonly depend on currently broader families:

- complete movement / push / pull / knockback / interception / forced movement;
- terrain / weather / hazards / zones / reactions;
- full lifecycle when timing or delayed effects matter;
- exact Move/Ability/Item/Trainer Feature behavior when referenced;
- AI tactical policy for ESCORT, BREAK_THROUGH, WITHDRAW, PROTECT_ITEM or REACH_EXIT goals;
- Minecraft/Cobblemon/Craftics adapter/playback for route/cargo representation.

Reduced versions should remove the parcel from the tactical grid, resolve physical handoff before or after battle, and preserve the same narrative premise.

## Canon questions intentionally left open

- Does Ouros have one regional postal institution or many operators?
- Which regions have formal street addresses versus landmark-based delivery?
- What technology is used for sorting and tracking?
- Can players operate courier businesses or only accept commissions?
- Which Pokémon species are institutionally used as couriers, if any?
- How are privacy and sealed correspondence treated?
- Which institutions can accept delivery on another actor's behalf?
- How does interregional forwarding work?
- What happens to mail for retired, missing or deceased actors?
- Which item categories need special custody rather than ordinary parcel handling?

None of these are promoted to canon by this research pass.