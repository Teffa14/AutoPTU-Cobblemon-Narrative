# Radio, Wireless Propagation & Communications Scan — Pass 123

Status: RESEARCH / PROVENANCE. NON-CANON. This document records reusable patterns and source interpretation. It does not establish Ouros technology, radio law, PTU mechanics, frequencies, signal ranges or canon institutions.

## Why this scan exists

The repository already has a broad Media/Communications layer and a Technology/Energy/Infrastructure layer. The former owns information packets, channels and delivery state. The latter owns physical assets, service networks, faults and maintenance. What remains under-specified is the physical/operational layer between a functioning wireless asset and a message channel being usable: propagation, coverage, relay topology, dead zones, interference, channel congestion and interoperability.

This pass therefore studies wireless communication as an unreliable spatial service rather than as universal connectivity.

## Internal repository boundary checked first

`design/media-communications-information-layer.md` already establishes that a message can be sent without being delivered and that communication channels can have coverage states. It keeps actual technology level as a canon decision.

`design/technology-energy-infrastructure-layer.md` already owns generators, relays, communications backhaul, operational state, faults, maintenance and service dependencies.

`design/geomagnetism-magnetic-navigation-interference-layer.md` owns physical magnetic-field state and geomagnetic interference causes. It explicitly leaves message delivery and radio services to Communications.

The new material must therefore specialize wireless reach without replacing any of those authorities.

## Pokémon sources

### Pokémon Ranger: Guardian Signs — communication as operational dependency

Source: Pokémon.com, “Pokémon Ranger: Guardian Signs.”
https://www.pokemon.com/us/pokemon-video-games/pokemon-ranger-guardian-signs/

The official page treats communication as part of Ranger operations rather than background flavor. Murph is described as helping keep communication lines open between the player and Professor Hastings. The same page distinguishes local wireless multiplayer, which requires players to be in close proximity, from broader Ranger communication. That separation is valuable for Ouros: two communication services can coexist while having different ranges, infrastructure and failure modes.

Reusable pattern:
- field teams depend on communications;
- local wireless service and regional service can be separate;
- communication availability can shape mission logistics without changing battle statistics;
- a communications role can matter even when that character never enters battle.

Do not import the Ranger Union, Capture Styler, Oblivia institutions or Nintendo DS technology.

### Wireless Tower — damaged communications as persistent regional state

Source: Bulbapedia, “Wireless Tower,” summarizing Pokémon Ranger: Guardian Signs.
https://bulbapedia.bulbagarden.net/wiki/Wireless_Tower

The Wireless Tower functions as a long-range communication hub. When the tower is disabled and later physically damaged, communication with the Ranger Union is interrupted and repairs remain relevant for an extended period. The useful structure is not the original plot. It is the persistence of degraded communications after the immediate confrontation ends.

Reusable pattern:
- taking control of a site and restoring its service are separate problems;
- a damaged antenna can create regional consequences after combat;
- repair takes time and may depend on staff, parts, access and power;
- the same landmark can be social identity, infrastructure and adventure location.

Do not copy the tower layout, villains, Raikou incident or specific hazards.

### Goldenrod Radio Tower — broadcast infrastructure as civic identity

Source: Pokémon.com, “Remember the Region: Johto Spotlight,” published April 24, 2026.
https://www.pokemon.com/us/pokemon-news/remember-the-region-johto-spotlight

The official retrospective identifies Goldenrod City partly through its radio tower. This supports a broader worldbuilding principle: communications infrastructure can become a landmark and cultural institution rather than remaining invisible backend machinery.

Reusable pattern:
- broadcast sites can define a city visually;
- public information infrastructure can host work, tourism, archives and civic memory;
- losing service and losing the landmark are different consequences.

### Rotom — device inhabitation does not equal network authority

Source: Pokémon.com Pokédex, “Rotom.”
https://www.pokemon.com/us/pokedex/rotom

The Pokédex describes Rotom as having an electricity-like body that can enter certain machines and take control of them. Research continues on machine applications. This is useful primarily as a guardrail. Rotom has authored machine interaction. That does not grant generic control of networks, authentication, signal amplification, radio interception, data access or administrator privileges.

Reusable pattern:
- a Pokémon can have a specific technical relationship with devices;
- the relationship should be tied to evidence about that individual/device;
- machine control, communications access and network authorization remain separate states.

Do not infer that Rotom Phone means unlimited connectivity or that a Rotom can repair a repeater by species alone.

## PTU community/actual-play scan

Publicly indexed PTU material was searched for radio, relay, signal and communication-centered encounters. This pass did not find a sufficiently clear PTU campaign source where wireless infrastructure itself was the main documented subsystem. General PTU actual plays remain useful for pacing and character structure, but no weak communication reference is promoted here merely to fill a source category.

Examples inspected during the broader scan include current public PTU actual-play feeds such as Pokémon Rollout! and The Reckless Rollers. Their existence confirms continued long-form PTU campaign play, but this pass does not claim a specific radio design lesson without a directly relevant episode record.

This absence is recorded rather than invented around.

## External systems research used only as abstraction

### Interoperability

Source: NIST, “Public Safety Communication Standards.”
https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir6575.pdf

The document defines interoperability around multiple organizations being able to communicate and share information, and describes the problems caused by fragmented systems. Ouros should borrow the structural lesson, not real public-safety standards.

Reusable pattern:
- two organizations can each possess functional radios and still fail to communicate directly;
- a gateway, shared procedure or common service can bridge them;
- interoperability can be partial by message type, location or incident;
- joint exercises can reveal compatibility problems before a crisis.

No US agency structure, radio bands, standards or law is imported.

### Coverage is modeled, observed and revised

Sources:
- FCC material on terrain, line-of-sight/non-line-of-sight and clutter effects.
- NTIA/ITS reports on terrain, vegetation, man-made clutter and propagation-model uncertainty.

Representative sources:
https://docs.fcc.gov/public/attachments/FCC-18-147A1.pdf
https://www.ntia.gov/files/ntia/publications/wg1_report_07232013.pdf

The reusable lesson is that coverage depends on more than distance. Terrain, buildings, vegetation, antenna placement and conditions can matter, and different modeling assumptions can disagree. Ouros should not implement physical RF equations. It should preserve a coarse difference between predicted coverage and observed service.

Reusable pattern:
- a published coverage map is a versioned model;
- a field survey can contradict it without either side being fraudulent;
- construction or vegetation changes can alter local reach;
- one successful contact does not prove reliable service;
- coverage can change seasonally or after infrastructure changes.

### Quiet/interference-sensitive sites

NTIA research on radio interference and protected measurement environments shows that some technical sites deliberately control nearby emissions so weak signals can be studied. Ouros can use the abstract pattern for observatories, research stations or historical listening sites if canon later authorizes it.

Do not import US radio-quiet-zone boundaries, spectrum rules, frequencies or enforcement powers.

## Reusable design lessons

Wireless communication should have at least six distinct layers:

1. physical assets exist and have an operational state;
2. those assets are configured into a service topology;
3. propagation conditions create potential reach;
4. observations and models estimate actual coverage;
5. networks may or may not interoperate;
6. the Media/Communications layer attempts actual message delivery.

The generator should never jump directly from `tower_online=true` to `message_delivered=true`.

A dead zone can be caused by terrain, a building, vegetation, configuration, missing power, failed backhaul, congestion, interference or unknown causes. “No signal” is a symptom.

A repeater can be powered and healthy but useless because it is misconfigured or incompatible with the intended network.

A device can display signal while the service needed by the actor remains unavailable.

Broadcast reach and two-way communication can differ.

Local communications can keep functioning while regional backhaul fails.

Restoring hardware can leave routing/configuration/interoperability problems unresolved.

## Pokémon-specific non-inferences

Electric-type Pokémon do not automatically act as generators, antennas, repeaters, chargers or jammers.

Rotom does not gain network-admin authority from inhabiting a device.

Magnemite, Magneton, Probopass or other magnetically associated Pokémon do not prove the cause of radio interference merely by being nearby.

Electric Terrain is a tactical PTU field effect when mechanically established. Its existence does not create communications interference in the overworld.

Thunder, Discharge, Eerie Impulse or other moves do not damage radio equipment unless an authoritative PTU/world interaction specifically establishes that consequence.

## PTU/Caelo validation result

The accessible project/File Library search did not recover the complete primary Caelo Player’s Guide/rulebook/errata corpus required to establish exact Technology Education, radio-device, electronic-interference or equipment rules. Super PTU Online Helper was not exposed as an invocable capability.

The available Python AutoPTU evidence contains concrete tactical Electric Terrain behavior, including a sleep-prevention interaction for grounded combatants. That narrow rule does not imply any wireless-network effect.

No communication Skill DC, device range, jamming rule, equipment damage rule or Electric-type infrastructure bonus is created by this research.

## Candidate Ouros direction

A specialized Radio/Wireless layer can safely own:
- wireless service identity;
- radio-site topology;
- repeaters and relay links;
- versioned coverage models;
- field coverage observations;
- dead-zone history;
- interference incidents and competing hypotheses;
- channel congestion episodes;
- interoperability profiles;
- temporary field relays;
- fallback communication plans;
- restoration verification.

Media/Communications must remain authoritative for messages and delivery receipts. Technology remains authoritative for the physical asset and fault state. Geomagnetism remains authoritative for magnetic causes. The new layer should connect these systems rather than duplicate them.