# Courier, Parcel & Last-Mile Research Scan — Pass 60

Status: provenance/research only. Nothing in this file is Ouros canon.
Date: 2026-08-26

## Why this scan exists

Ouros already has information delivery, transport services, supply routes, storefront continuity, staffing and residential relocation. The missing seam is physical delivery as persistent world state: an entrusted object can be accepted, sorted, routed, delayed, handed off, returned, redirected, damaged, lost, recovered or delivered to a recipient whose location has changed.

This pass focuses on delivery structures rather than inventing postal law, prices, cargo capacities, ownership rules or Pokémon labor mechanics.

## Internal overlap review

Relevant existing layers inspected before writing:

- `design/media-communications-information-layer.md` already owns information packets, message delivery, channels, coverage and courier as a logical communication channel.
- `design/travel-transport-expedition-layer.md` already owns routes, journeys, services and cargo carried during travel.
- `design/commercial-services-storefront-continuity-extension.md` already owns service availability and supplier/customer consequences.
- `design/material-culture-economy-crafting-layer.md` owns physical item provenance and supply-side economic state.
- `design/workplaces-professions-staffing-layer.md` owns roles, shifts and staffing continuity.
- `design/residential-life-household-relocation-layer.md` owns current residence and relocation history.

Pass 60 therefore treats delivery as an orchestration layer connecting those systems. It does not create a second travel graph or a second communications model.

## Source A — Pokémon Mystery Dungeon: Rescue Team DX official site

Source: Pokémon.com, Pokémon Mystery Dungeon: Rescue Team DX — World
https://mysterydungeon.pokemon.com/en-us/world/

Observed structure:

- requests arrive through both a public bulletin board and direct mailbox delivery;
- a persistent office acts as a routing institution rather than a one-off quest giver;
- requests enter an accepted job list before execution;
- completion changes organizational progression and can produce future work.

Reusable lesson:

A delivery institution is more interesting when it maintains queues, public intake, direct intake and persistent completion history. Ouros can use this pattern without importing rescue-rank math or Mystery Dungeon rules.

## Source B — Pelipper Post Office / Wonder Mail structure

Sources:

- Pokémon.com, Wonder Mail Passwords
  https://mysterydungeon.pokemon.com/en-us/news/Wonder_Mail_Passwords/
- Spike Chunsoft, Pokémon Mystery Dungeon rescue overview
  https://www.spike-chunsoft.co.jp/pages/games/pokedun_i/rescue01.html

Observed structure:

- requests can be generated outside the immediate location and enter a central job queue;
- the institution separates receipt of a request from active execution;
- mail can carry job state, acknowledgement and later response.

Reusable lesson:

Ouros can separate `shipment created`, `accepted by carrier`, `out for delivery`, `delivered`, and `acknowledged`. A world event should not jump directly from sender intent to recipient possession.

## Source C — Professor Oak / Barry parcels

Source: Bulbapedia, Parcel
https://bulbapedia.bulbagarden.net/wiki/Parcel

Observed structure:

- a physical parcel is explicitly entrusted to the player;
- the destination and intended recipient are known;
- delivery unlocks a later relationship or progression beat;
- the package remains a distinct object until handoff.

Reusable lesson:

An entrusted object can create responsibility without requiring combat. The important state is custody, destination and handoff. Ouros should preserve the package as an item instance or referenced object rather than treating delivery as a dialogue flag.

## Source D — Poké Jobs: Pelipper Couriers and cargo companies

Source: Bulbapedia, Poké Job
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9_Job

Observed structure:

- the setting explicitly contains courier and cargo organizations;
- delivery work includes both transport and sorting;
- different operational problems exist upstream of the final handoff;
- Pokémon can participate in work in official Pokémon fiction/game systems.

Reusable lesson:

Delivery gameplay should include sorting, dispatch, route allocation, backlog and exception handling, not only walking an item from A to B.

Guardrail:

The source's type-based Poké Job requests are not PTU/Caelo mechanics. Ouros must never infer that a Flying type can legally carry cargo, that a Steel type can sort electronics, or that any species has a workplace capability. Individual capability must come from approved world state and governing mechanics.

## Source E — PTU one-shot discussion using a weekly delivery rhythm

Source: Reddit /r/PokemonTabletop, “Help with one shot PTU”
https://www.reddit.com/r/PokemonTabletop/comments/hmh8ku

Observed structure:

- the scenario treats a weekly delivery as a normal settlement rhythm;
- an unusual vehicle arriving outside that rhythm immediately becomes a clue;
- the delivery worker and store supply cadence help players detect that something is wrong before combat.

Reusable lesson:

Routine logistics can be environmental storytelling. The interesting event is often a deviation from a known schedule, not the shipment itself.

This is community campaign-design material, not rules authority.

## Source F — fan-made delivery-focused game

Source: Ducumon summary of Pokémon Concord’s Delivery Service
https://www.ducumon.click/2023/06/pokemon-concords-delivery-service.html

Observed structure:

- a whole short adventure can be framed around one important parcel;
- route geography and delivery responsibility provide the central spine;
- the premise works without requiring the parcel itself to have magical properties.

Reusable lesson:

A delivery job can be an adventure container. The narrative value comes from people, geography, timing and responsibility encountered along the route.

The fan game’s characters, region, plot and prose are not reusable.

## High-level patterns extracted

### 1. Intake is distinct from execution

A shipment can exist before any courier accepts it. This supports backlog, urgency, staffing shortages and player choice.

### 2. Custody is explicit

At any moment the world should be able to answer who or what currently possesses the parcel, where it was last verified and what evidence supports that state.

### 3. Delivery is a chain, not a teleport

Useful stages include intake, sorting, dispatch, line-haul transport, local handoff and receipt. Not every shipment needs every stage, but the model can represent them.

### 4. Exceptions create stories

Interesting exceptions include:

- recipient moved;
- route closed;
- address incomplete;
- parcel damaged;
- wrong parcel loaded;
- recipient unavailable;
- sender recalls shipment;
- carrier loses contact with a route segment;
- package reaches the correct settlement but wrong service desk;
- weather or infrastructure delays line-haul transport;
- staffing backlog causes a known cadence to slip.

### 5. Normal cadence makes anomalies legible

A settlement that usually receives a delivery every few days can notice when the pattern changes. Logistics become a quiet world clock.

### 6. The package can matter without being special

Medicine, documents, replacement parts, personal belongings, research samples, event materials or ordinary orders can carry narrative importance because of context, not intrinsic power.

### 7. Handoff can produce future state

A successful delivery can change:

- service availability;
- a repair project;
- a research case;
- an event readiness gate;
- a household move;
- a commercial restock;
- an institutional response;
- a relationship or promise;
- a public record.

The delivery layer should emit those effects to the system that owns them.

## Original Ouros design direction derived from the scan

Pass 60 should add a persistent physical-delivery layer with:

- shipment records;
- parcel/item references;
- sender, intended recipient and current custodian;
- service desk or carrier intake;
- route/leg references rather than duplicated geography;
- custody-transfer history;
- delivery attempts;
- redirect/return state;
- condition observations;
- delivery evidence and acknowledgements;
- backlog and service exceptions;
- residential relocation integration;
- commercial/facility/project handoffs;
- Minecraft-visible desks, depots, parcel props and notices where feasible.

## Rules and canon boundaries

This research does not establish:

- a regional postal service;
- named courier companies;
- shipping prices;
- insurance;
- postal crimes;
- customs;
- ownership law;
- signatures as a legal requirement;
- guaranteed delivery times;
- cargo weight limits;
- mail privacy law;
- teleportation delivery;
- species-based courier capability;
- new PTU skills or checks;
- combat bonuses for carrying a package.

Those remain canon/mechanics decisions.

## Engine implications

Most delivery scenes are noncombat world-state content and can run before the Minecraft adapter is complete.

Mechanically rich delivery encounters become dependent on exact engine families when they require escort objectives, interception, moving cargo, forced displacement, terrain/weather effects, hazards, reactions or objective-aware AI.

Pass 60 therefore needs intended and reduced encounter versions, preserving the delivery premise while keeping unsupported PTU behavior outside tactical resolution.
