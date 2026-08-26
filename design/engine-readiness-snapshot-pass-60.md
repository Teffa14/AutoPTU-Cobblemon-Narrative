# Engine Readiness Snapshot — Pass 60

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.
Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live evidence

Newest inspected AutoPTU-Java commit:

`55bdeb0cb9146054d4d80a0999bcd793275fe140` — Freeze canonical Chronicler profile metadata (#223).

This freezes metadata shape and parity for one Chronicler profile slice. It strengthens one exact Trainer Feature data-contract edge. It does not establish the complete Trainer Features/perks family or new tactical execution families.

The current Java README still explicitly lists as unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- move/ability/item/perk/Trainer Feature hook registries;
- semantic transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Newest inspected Python AutoPTU commit:

`3953a701e8b756fa0f5da7b568cb2fc278d866f7` — Career: keep battle positions authoritative (#157).

This hardens persisted battle-coordinate presentation by rejecting malformed values before the renderer. Its commit description states that it does not change combat rules. It therefore provides no new tactical family evidence for narrative encounter design.

## Permanent capability map

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No Pass-60 evidence justifies a category promotion.

## Courier and parcel non-inference gates

A shipment accepted by a carrier is not delivered.

Arrival in the same settlement as the intended recipient is not delivery.

Custody is not ownership.

A package label or declared description is not verified proof of hidden contents.

Packaging damage is not automatically mechanical item damage, Medicine spoilage, sample loss or another PTU effect.

A recipient moving does not expose their new private address to the sender, courier or player. The residential/privacy and communication layers determine whether a valid forwarding or contact path exists.

A courier who repeatedly works a route may know its normal schedule and transfer points. That does not give them knowledge of private contents, motives or household relationships.

A transfer prop visible in Minecraft does not prove server-side custody unless the authoritative shipment record records the handoff.

A physical delivery cannot create, destroy or mutate item instances silently.

A Pokémon cannot gain a courier, sorting or cargo role from species or type inference. Mechanically relevant participation requires approved individual state and governing PTU/Caelo evidence.

Narrative urgency cannot create shipping speed, cargo capacity, delivery DCs, initiative bonuses, escort mechanics or item-protection bonuses.

## Encounter review — Moving Convoy Interruption

Intended version may require:

- convoy/cargo position changing during battle;
- protect, escape or breakthrough objectives;
- interception;
- forced displacement;
- route terrain/weather entering tactical resolution;
- hazards or zones tied to route state;
- objective-aware enemy/allied AI;
- explicit cargo-condition effects;
- Minecraft playback synchronized with convoy progress.

Dependency state:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Stop the convoy before combat. Keep the shipment outside tactical targeting, movement, damage and ownership changes. Run one ordinary static legal encounter using only individually verified mechanical slices. After the authoritative battle result, world-state logic may resume, reroute or retreat the shipment. Do not simulate escort scoring, cargo HP, forced displacement, moving-objective rules or route weather inside combat.

## Encounter review — Depot Recovery

Intended version may require:

- worker evacuation overlapping tactical play;
- changing blocked aisles;
- protected storage objectives;
- destructible or hazardous zones;
- forced movement or knockback near cargo;
- containment/escape goals;
- AI that values exits, protected storage or withdrawal;
- Minecraft playback preserving depot state.

Dependency state:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Evacuate all workers and freeze the depot layout before tactical resolution. Keep stored shipments outside combat interaction. Run a static ordinary battle with legal combatants only. After combat, perform a separate world-state parcel-identification and custody-transfer interaction. No crate damage, hazardous shelf mechanics or objective scoring is invented.

## Noncombat review — The Address That Changed

This concept can run now as narrative/world-state content using:

- shipment history;
- residential relocation state;
- contact/privacy state;
- authored delivery attempts;
- institutional forwarding only where already established;
- sender/recipient communication paths already valid in world state.

The scene must keep old destination, current residence, courier knowledge, sender knowledge and canonical location separate.

The generator cannot invent forwarding law, expose a private address, assume a household relationship or declare delivery complete because the package reached the former residence.

## Noncombat review — Three Parcels, One Wrong Cart

This concept can run now using:

- intake timestamps;
- custody-transfer records;
- dispatch batches;
- route/service state;
- physical observations;
- staff claims;
- receiving records.

It requires no tactical engine feature if the resolution is investigative.

The scene must keep declared destination, observed label, current physical location, staff belief and authoritative shipment state separate.

## Pass-60 outcome

Physical-delivery continuity can advance now through shipment lifecycle state, explicit custody, route/service references, delivery attempts, redirect/return handling, condition observations, service-node backlogs and downstream handoffs to existing residential, commercial, facility, care, science, event, travel and communication systems.

Mechanically rich convoy, escort, moving-cargo and depot-defense encounters should retain reduced static versions until complete movement, environmental interaction, tactical AI, broader lifecycle/content registries and Minecraft/Cobblemon/Craftics playback become verified.

Capability classifications remain unchanged from Pass 59.
