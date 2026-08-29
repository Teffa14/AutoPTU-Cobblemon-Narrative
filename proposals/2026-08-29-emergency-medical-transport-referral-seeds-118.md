# Ouros Narrative Seeds — Emergency Medical Transport & Referral — Pass 118

Status: NON-CANON PROPOSALS. These are authoring candidates only. Promotion requires explicit canon review.
Research basis: `research/2026-08-29-emergency-medical-transport-referral-continuity-scan-118.md`
Design basis: `design/emergency-medical-transport-referral-continuity-extension.md`

## Proposal boundary

These seeds assume only that a future Ouros region may canonize some form of organized medical transport. They do not establish ambulances, aircraft, sirens, emergency numbers, treatment protocols, response times, medical qualifications or legal rights of way as universal Ouros facts.

Every patient condition remains owned by Care/PTU/AutoPTU as appropriate. Every route remains owned by its transport/infrastructure layer. Battle concepts use reduced forms until the required engine families are proven.

## Seed — The Vehicle Arrived, the Patient Did Not Leave

A transport unit reaches the recorded scene address on time, but the subject has already been moved by neighbors to a safer nearby building after access conditions changed.

Playable structure:

- compare request location with latest verified subject location;
- establish who moved the subject and when;
- reconnect the responding crew with the correct access route;
- preserve both timestamps as valid records.

Useful lesson: `UNIT_AT_SCENE` and `SUBJECT_CONTACT` are different events.

No negligence, deception or medical deterioration is implied.

## Seed — Accepted There, Diverted Here

A regional care facility accepted a transfer, but the route becomes unavailable before departure. Another receiving site later accepts the subject.

The story can focus on:

- the original acceptance remaining historically valid;
- the later diversion decision;
- family/Trainer information lagging behind operational state;
- different institutions holding correct but differently timed information.

The cause of the route closure belongs to its owner system.

## Seed — The Old Pickup Point Still Gets Visitors

A temporary medical pickup point established during an old crisis disappeared from formal maps years ago. Residents still use its name when giving directions, and a local Pokémon regularly waits near the former shelter.

Possible outcomes:

- recover the location's service history;
- distinguish current service from local memory;
- discover why the old route remained socially important;
- preserve the Pokémon's behavior as observation rather than inferred loyalty or profession.

## Seed — The Center Is Open, the Transfer Is Pending

A local care site is operating normally, but a subject requires a service available only elsewhere. The referral is accepted; the transport assignment is delayed by a separate service constraint.

This creates meaningful world state without declaring the clinic incapable or the patient unstable.

Potential linked systems:

- Care;
- Travel;
- Infrastructure Outage;
- Accessibility;
- Weather;
- Crisis;
- Communications.

## Seed — The Crew Returned, the Unit Did Not

A transport crew is back at base while the unit remains unavailable pending authored turnaround work or maintenance.

The settlement hears "the crew is back" and assumes service is restored.

The mystery comes from scope:

- personnel availability;
- vehicle availability;
- base status;
- replacement asset availability;
- dispatch coverage.

No mechanical failure is invented until Maintenance provides evidence.

## Seed — Two Facilities, One Referral Name

A long-standing specialist service moved from one building to another without changing its common local name. Old records therefore appear to send patients to the wrong address.

Resolution uses:

- institution ID;
- effective dates;
- building/location aliases;
- maps;
- referral records;
- public notices.

This seed can connect to urban redevelopment and public memory without requiring a villain.

## Seed — The Ferry Was the Medical Link

NON-CANON geography candidate.

An island settlement relies on an ordinary ferry connection for planned transfers and a separately authored contingency for urgent movement. A ferry disruption therefore changes referral feasibility even though the island clinic itself remains operational.

The narrative value comes from dependency visibility. Maritime decides service state; Care decides referral need; this layer preserves transport coordination.

No helicopter, flying Pokémon or emergency boat is generated automatically as a fallback.

## Seed — The Wrong Uniform Was Enough Once

A historical custody dispute involved people who appeared to be medical transport staff but were not linked to a valid assignment record.

The present-day hook begins when an archive review finds:

- vehicle appearance evidence;
- witness statements;
- missing or mismatched dispatch assignment;
- a receiving record that begins later in the chain.

The quest is about reconstructing authority and custody from provenance. It should never make routine workers seem suspicious by default.

## Seed — The Pokémon Knows the Route Better Than the Map

A specific long-serving Pokémon partner repeatedly reacts at the same old turnoff during transfers. Investigation shows that the service route once used a road removed from modern maps.

The Pokémon's behavior is evidence of familiarity with an individual route history. It does not establish supernatural navigation, species-level medical skill or authority to select destinations.

## Seed — The Handoff Happened After Midnight

A transfer appears to be recorded on two different dates because the vehicle arrived shortly before midnight and the care handoff completed afterward.

This small chronology puzzle can matter later when players reconstruct:

- where a witness was;
- which staff shift received the subject;
- which public notice was current;
- which route closure had already taken effect.

Both records can be correct.

## Seed — The Field Team Became Permanent

A crisis creates a temporary mobile care/transport team. Long after the immediate event, residents continue requesting the service because it solved a geographic access problem that predated the disaster.

Possible long arc:

1. emergency deployment;
2. temporary pickup network;
3. repeated ordinary use;
4. funding/mandate debate if such institutions exist in canon;
5. permanent station or revised service boundary;
6. old temporary sites becoming landmarks or social nodes.

No policy outcome is predetermined.

## Mystery — Five Times the Patient "Arrived"

Five records appear to give different arrival times:

- unit reached the scene;
- crew made subject contact;
- subject boarded;
- vehicle reached receiving facility;
- receiving team accepted care handoff.

The investigation resolves the contradiction by attaching each timestamp to the correct event type.

Design goal: teach players to ask "arrival of what, where?" rather than searching immediately for false records.

## Mystery — Three Destinations, One Journey

A transport log names three destinations.

Proposed explanation structure:

- destination A was initially requested;
- destination B accepted;
- a route or service change caused diversion;
- destination C ultimately received the subject.

Each entry is preserved with effective time and supersession rather than overwritten.

Potential later use: a witness remembers hearing destination B and is truthful even though the subject arrived at C.

## Exploration — The Station That Moved Twice

An old station building, a newer roadside base and the present medical-transport office all share variants of one local name.

Exploration beats:

- compare historical town maps;
- find the first base's repurposed building;
- match dated photographs to road alignments;
- talk to former staff or residents;
- identify why the second location was temporary;
- recover the persistent service identity across relocations.

Current implementation profile: world exploration. No missing battle capability is required.

## Longer arc — A Region Learns Its Referral Routes

Phase 1 establishes normal life before disruption:

- local clinic;
- regional specialist facility;
- ordinary road/water/air links where canon supports them;
- recurring transport staff and Pokémon individuals;
- routine planned transfers that usually compress.

Phase 2 introduces a bounded disruption:

- one route or receiving service changes state;
- the first diversion exposes weak information links;
- a temporary pickup point becomes socially important.

Phase 3 creates repeated but varied consequences:

- one transfer succeeds through an alternate route;
- another waits because destination acceptance is pending;
- public information catches up at a different pace;
- a local institution adapts its referral practice.

Phase 4 resolves the acute problem without resetting history:

- normal route may return;
- temporary location may close or persist;
- relationships and institutional memory remain;
- old records become future evidence.

Phase 5 reuses the history later:

- a missing-person timeline references an old handoff;
- a new crisis tests the alternate route created years earlier;
- a recurring Pokémon or worker recognizes a former pickup site;
- a renamed service causes a document mystery.

No single `medical_transport_level` represents this arc.

## Encounter — Roadside Pickup Withdrawal

Full narrative intention:

A protected medical subject and crew must leave a roadside pickup while a distinct hostile Pokémon subgroup threatens access.

Full dependencies:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL if exact validated status use exists;
- terrain/weather/hazards/zones/reactions: BLOCKING for generalized protection/reaction areas or active hazards;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for WITHDRAW/PROTECT/CLEAR_ROUTE;
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING.

Reduced implementation:

Boarding and departure finish before BattleSpec. Patient, crew and medical unit remain outside combat. Resolve a conventional static encounter at the emptied pickup area. Victory secures the immediate location after departure and cannot imply treatment, handoff or unit readiness.

## Encounter — Transfer Bay Perimeter

Full narrative intention:

A receiving handoff is threatened by a separate exterior disturbance, requiring a protected corridor.

Full version depends especially on:

- complete movement: PARTIAL for interception/forced displacement;
- terrain/weather/hazards/zones/reactions: BLOCKING for generalized reaction/protection zones;
- AI tactical policy: BLOCKING for protected-corridor reasoning;
- adapter/playback: BLOCKING;
- all remaining categories retain the permanent Pass 118 map.

Reduced implementation:

Finish the patient/care handoff behind a secure boundary first. Run battle in an exterior static perimeter with explicit combatants only. The result can secure access after the transfer but cannot perform or invalidate the medical handoff.

## Encounter — Diversion Junction

Full narrative intention:

Players help preserve a medical route while a transport unit diverts around an obstruction.

Full version may require:

- complete movement for escort/interception/forced movement — PARTIAL;
- lifecycle for timed route windows — PARTIAL;
- terrain/weather/hazards/zones/reactions for changing route cells or generalized reactions — BLOCKING;
- AI tactical policy for ESCAPE/PROTECT/CLEAR_ROUTE — BLOCKING;
- adapter/playback for moving transport assets — BLOCKING.

Reduced implementation:

The unit completes diversion in world state before combat. Players confront the explicit threat later at a static junction. No patient, crew member or medical vehicle is on-grid. Victory cannot rewrite the already recorded diversion chronology.

## Canon questions left open

Pass 118 deliberately does not choose:

- whether every settlement has organized medical transport;
- whether services are public, private, charitable, institutional or mixed;
- whether humans and Pokémon share transport/facilities;
- regional differences in emergency and planned transport;
- vehicle types;
- emergency communication systems;
- dispatch institutions;
- clinical referral rules;
- payment models;
- road-priority rules;
- air/water retrieval availability;
- medical privacy rules specific to transport;
- Pokémon worker roles;
- response-time expectations;
- historical service failures or successes.

Those require canon approval rather than procedural generation.
