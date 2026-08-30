# Ouros Narrative Research — Road Vehicle, Fleet Assignment, Inspection & Serviceability Continuity — Pass 142

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon.
Date: 2026-08-30

## Research question

What persistent world-state is missing between an authored road-passenger service, a physical vehicle, its current operator/custodian, an inspection or defect report, maintenance work, a temporary restriction, substitution and eventual return to service or retirement?

The goal is not to create a vehicle simulator. The goal is to let Ouros remember which physical vehicle existed, where it belonged, what role it was assigned to, what was known about its condition at each point in time, and why a service used a different asset later.

## Repository inspection before research

The complete recursive tree of `Teffa14/AutoPTU-Cobblemon-Narrative` was inspected before topic selection and returned `truncated: false` at head `faedfc5b9d3e49e8707e2c2df7904bcf4c9b9fbb`.

The candidate was checked against the existing owners most likely to overlap:

- `design/travel-transport-expedition-layer.md` owns journeys, route viability, transport-service references and generic mobile-base composition.
- `design/road-passenger-transport-services-continuity-extension.md` owns service patterns, stops, runs, dispatch, boarding/alighting and road-passenger operating history. It already references `vehicle_asset_ids` but does not define the lifecycle of those physical vehicles.
- `design/shared-equipment-lending-issued-assets-extension.md` owns temporary-use entitlement, checkout, custody and return for general reusable equipment. It explicitly delegates repair/readiness work to Maintenance and does not specialize road vehicles.
- `design/facility-maintenance-repair-inspection-extension.md` owns facility faults, assessments, work orders, restrictions, repair and reopening. It is facility-focused rather than a neutral vehicle/fleet identity layer.
- `design/fuel-supply-storage-distribution-continuity-extension.md` owns fuel availability and distribution where canon supports it.
- `design/request-dispatch-response-resource-continuity-extension.md` owns dispatch and field-resource assignment, but not the long-lived identity and technical readiness of a road vehicle.
- Finance owns purchases, charges, insurance and monetary settlement where authored.
- Human Identity / Credentials / Workplaces own people, qualification and authority.
- Material Culture owns persistent physical-object provenance when a vehicle is represented as a story-significant object instance.
- Pokémon Agency / Work Role owns individual Pokémon participation. A Pokémon is never converted into a vehicle asset by this research.

Repository search found no dedicated owner for road-vehicle identity, fleet numbering, vehicle-to-operator relationship, defect chronology, roadworthiness/serviceability state, inspection lineage, vehicle substitution or retirement/repurposing.

## Pokémon sources

### Rotom Bike — one persistent travel asset can gain a new mode

Source: Bulbapedia, `Rotom Bike`.
https://bulbapedia.bulbagarden.net/wiki/Rotom_Bike

The Sword/Shield Rotom Bike begins with land travel and later receives Water Mode. It can also receive recharge upgrades and cosmetic variants.

Reusable high-level lesson:

- asset identity can persist while capabilities/configuration change;
- an upgrade event should be historical state rather than a replacement by default;
- appearance/configuration changes should not silently create a new physical object;
- capability history should be versioned when it affects traversal.

Ouros transformation:

A canon-approved vehicle may have `configuration_episode` or `upgrade_event` records. A later configuration does not rewrite what the vehicle could do earlier. No Rotom technology, Water Mode, Watt pricing or exact game mechanic is imported.

### Flying Taxi — service identity can persist while transport assets differ by region

Sources: Bulbapedia, `Flying Taxi`; `Corviknight (Pokémon)`.
https://bulbapedia.bulbagarden.net/wiki/Flying_Taxi
https://bulbapedia.bulbagarden.net/wiki/Corviknight_(Pok%C3%A9mon)

The Flying Taxi concept exists across multiple regions while the Pokémon used to provide the service differs. Paldea uses Squawkabilly instead of Corviknight, with local ecological danger given as the reason Corviknight is unsuitable there.

Reusable high-level lesson:

- service identity and assigned transport asset are separate;
- local ecology can constrain which assets are safe/appropriate without abolishing the service concept;
- substitution can preserve the public function while changing the operating asset;
- visible species or vehicle type should not be treated as the identity of the service itself.

Ouros transformation:

Road passenger services may substitute vehicles or Pokémon-assisted assets while preserving `service_id` and run history. The exact reason must come from current world state. No region, species assignment or taxi rule becomes Ouros canon.

### Bicycle / ride systems — access mode and ownership are separate concepts

Source: Bulbapedia, `Bicycle`.
https://bulbapedia.bulbagarden.net/wiki/Bicycle

Across Pokémon games, bicycles, Ride Pokémon and partner travel systems occupy similar traversal roles but use different ownership/access structures.

Reusable lesson:

A world should not collapse `can use this travel mode`, `owns the transport asset`, `has custody of the asset`, `is assigned the asset`, and `the asset is mechanically capable right now` into one fact.

Ouros transformation:

Vehicle use must reference the correct owner: personal property/provenance, institutional allocation, public transport assignment, temporary lending, or another canon-approved relationship.

## PTU community evidence

Source: public r/PokemonTabletop discussion, `Do Riders Trigger Attacks of Opportunity When Their Mount Shifts? And Other Mount Related Questions`.
https://www.reddit.com/r/PokemonTabletop/comments/f5glt8/

The discussion highlights ambiguity around mounted movement, shared spaces, attacks of opportunity and which participant is considered to be shifting. It is community interpretation, not governing rules authority.

Reusable lesson:

Mounted/vehicle-adjacent tactical behavior is exactly the kind of subsystem that must not be invented from narrative convenience. A vehicle encounter that needs rider/mount co-location, moving platforms, boarding during initiative, collision, edge displacement or special reaction semantics must expose those dependencies and remain blocked until exact PTU/engine contracts are verified.

## Operational provenance sources

These sources are used only to learn state separation and recordkeeping patterns. Their laws, identifiers, inspection intervals, agencies and thresholds are not imported into Ouros.

### NHTSA recall lookup — persistent vehicle identity versus repair state

Source: U.S. National Highway Traffic Safety Administration, `Check for Recalls`.
https://www.nhtsa.gov/recalls

The public lookup uses a VIN as a unique vehicle identifier and distinguishes a specific vehicle from an unresolved recall affecting it. It also notes that a plate can be associated with a previously owned vehicle until records update.

Reusable lessons:

- a stable physical-asset identifier can be distinct from a locally reused visible identifier;
- `AFFECTED_BY_NOTICE` and `REMEDY_COMPLETED` are different events;
- a changed or reused registration/plate-like identifier must not automatically create or merge vehicle identity;
- record updates can lag behind physical ownership/custody changes.

Ouros transformation:

Use an internal `vehicle_ref_id` for continuity. Any in-world fleet number, registration mark, nickname, livery or institution-issued identifier remains a versioned record whose existence and format are canon-dependent.

### FMCSA inspection/maintenance material — control, ownership, defect, repair and release are distinct

Sources: Federal Motor Carrier Safety Administration, `Inspection, Repair, and Maintenance for Motor Carriers of Passengers - Part 396`; related guidance on inspection/maintenance records and out-of-service restrictions.
https://www.fmcsa.dot.gov/safety/passenger-safety/inspection-repair-and-maintenance-motor-carriers-passengers-part-396
https://www.fmcsa.dot.gov/safety/question-5-where-must-vehicle-inspection-and-maintenance-records-be-retained-if-vehicle-not

The guidance separates vehicle identification, ownership or leasing/control, scheduled maintenance, defect reporting, repair, inspection and the operational consequence of an out-of-service condition.

Reusable lessons:

- owner and controlling operator can be different;
- a defect report is evidence, not automatically a confirmed diagnosis;
- repair activity and permission/decision to return an asset to service can be separate events;
- inspection records can live separately from the vehicle while still referring to the same physical object;
- a vehicle can remain physically present while operationally unavailable.

Ouros transformation:

Create append-only observation, defect, assessment, maintenance and release records. Do not import U.S. inspection periods, certification requirements or legal authority.

### FTA transit asset management — a fleet is a portfolio of long-lived assets

Sources: Federal Transit Administration, `Asset Management Guide`; `Performance Management` / transit asset management material.
https://www.transit.dot.gov/sites/fta.dot.gov/files/docs/FTA_Report_No._0027.pdf
https://www.transit.dot.gov/PerformanceManagement

The material treats revenue vehicles and service/support vehicles as persistent assets with lifecycle, maintenance, condition, rehabilitation/replacement and fleet-level planning.

Reusable lessons:

- service fleet and support fleet can overlap operationally but retain different roles;
- asset age, condition, current assignment and replacement planning are separate dimensions;
- spare assets matter because service continuity can depend on substitution;
- retirement from primary service does not imply physical destruction.

Ouros transformation:

Fleet membership and role assignment are versioned. A retired bus might later become a training prop, community shelter, food stall, museum piece or private vehicle only if authored. Repurposing preserves prior service history.

## New design conclusions

The missing continuity chain is:

physical vehicle identity
→ identifier/name/livery history
→ ownership/custody/operator relationship
→ fleet membership
→ current role/service assignment
→ inspection/condition observation
→ defect claim and assessment
→ restriction/serviceability decision
→ maintenance episode
→ verification/release
→ substitution or return to assignment
→ retirement, disposal or repurposing.

These stages should remain independently timestamped.

Useful invariant candidates:

- `SAME_FLEET_NUMBER != SAME_VEHICLE`
- `DIFFERENT_LIVERY != DIFFERENT_VEHICLE`
- `VEHICLE_PRESENT != VEHICLE_AVAILABLE`
- `VEHICLE_ASSIGNED != VEHICLE_OPERATING_NOW`
- `OWNER != OPERATOR`
- `OPERATOR != DRIVER`
- `DEFECT_REPORTED != DEFECT_CONFIRMED`
- `INSPECTION_PASSED_AT_T1 != SAFE_AT_T2`
- `REPAIR_RECORDED != RETURN_TO_SERVICE_APPROVED`
- `OUT_OF_SERVICE != RETIRED`
- `RETIRED_FROM_PUBLIC_SERVICE != DESTROYED`
- `VEHICLE_SUBSTITUTED != SERVICE_CANCELLED`
- `ROUTE_OPEN != VEHICLE_AVAILABLE`
- `FUEL_AVAILABLE != VEHICLE_SERVICEABLE`
- `VEHICLE_SERVICEABLE != CREW_AVAILABLE`
- `VISIBLE_VEHICLE != AUTHORIZED_TRANSPORT_SERVICE`

## PTU/Caelo cross-check boundary

The existing project source scan confirms PTU/Caelo support for travel, Jobs, location-specific mechanics and individual Pokémon capabilities, but does not establish a universal road-vehicle simulator.

Remain UNKNOWN unless exact governing source/tests are located:

- generic vehicle HP, Armor, DR or damage model;
- acceleration, braking and turning rules;
- road-vehicle speed by round;
- collision damage;
- moving-platform tactical coordinates;
- boarding/disembarking timing during combat;
- passengers sharing vehicle spaces;
- vehicle cover;
- vehicle knockback, pushing or forced movement;
- crash/fall/ejection transitions;
- road chase mechanics;
- generic repair/inspection Skill Checks or DCs;
- Technology Education as universal vehicle-operation authority;
- Trainer Classes/Features as generic licenses;
- Pokémon Type/species as automatic driving, towing or propulsion competence;
- Rotom, Revavroom or any other species as a universal vehicle subsystem;
- Move/Ability interaction with vehicles unless an exact implemented mechanic says so.

## Copyright / transformation note

No protected prose, dialogue, maps, characters or plot sequences are copied into Ouros. Pokémon sources contribute only abstract patterns around asset continuity, capability changes and service substitution. Public operational sources contribute only state-separation and provenance concepts.

## Candidate Ouros output

Proceed with a PROPOSED road-vehicle/fleet continuity extension, NON-CANON story seeds and an engine-readiness snapshot. Do not establish whether Ouros has registration systems, VIN-like identifiers, mandatory inspections, private automobiles, specific fuel technologies, licensing regimes or any particular road-vehicle class.