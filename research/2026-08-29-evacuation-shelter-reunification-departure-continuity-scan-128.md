# Ouros Research — Evacuation Shelter, Reunification & Departure Continuity — Pass 128

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon.
Date: 2026-08-29

## Research question

What reusable structures can help Ouros preserve the human and Pokémon continuity between emergency evacuation, temporary sheltering, separation, verified contact, reunification and eventual departure without inventing guardianship, custody law, emergency powers, Pokémon ownership or tactical mechanics?

The repository was inspected recursively before this pass. The tree was complete (`truncated=false`) at Pass 127 head `b4c1f0d3141b03f747385579b1e781a0155b42b6`.

The relevant existing boundaries are already strong:

- Crisis/Rescue owns hazard truth, evacuation, staging, shelter objects, missing-actor cases and the abstract operational verb `REUNITE`.
- Residential owns normal residence, displacement, temporary accommodation references and return-to-home review; emergency shelter occupancy must not overwrite normal residence.
- Family/Kinship owns only explicitly established relationship facts and forbids inferred family/guardianship.
- Pokémon Agency owns persistent Pokémon identity, current custody, association, transfer and release, while keeping ownership, custody, active Trainer and residence separate.
- Pokémon Shelter/Sanctuary owns its own Pokémon placement-program intake and reunification workflow, not human emergency shelter population tracking.
- Community Aid owns volunteer commitments/check-in/handoff, not evacuee identity or reunification.
- Care owns health and treatment truth.
- Travel owns journeys and route use.
- Public Notices/Communications own publication and communication delivery.

The missing layer is therefore narrow: persistent continuity for emergency shelter population and reunification records across multiple sites and changing timestamps.

## Public Pokémon research

### Destiny Deoxys / LaRousse evacuation

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Destiny_Deoxys
- https://bulbapedia.bulbagarden.net/wiki/M7

Reusable structure:

LaRousse City uses multiple evacuation channels, including monorail and ferry movement. Some people leave, some remain trapped, automation fails, alternative paths become important, and a laboratory later becomes a place of safety for a subset of characters.

Ouros transformation:

- evacuation instruction;
- intended route;
- actual departure;
- arrival at a safe site;
- known current location;
- inability to leave;
- alternate route;
- later contact/reunification;

must remain distinct facts.

A citywide evacuation order or successful transport operation does not prove that every actor reached the intended destination.

Do not copy LaRousse, Deoxys, Rayquaza, characters, dialogue, technology or plot.

### Gulpin it Down

Source:
- https://bulbapedia.bulbagarden.net/wiki/Gulpin_it_Down

Reusable structure:

An emergency announcement can empty ordinary streets and convert familiar civic locations into operational spaces. The underlying event may involve Pokémon, but the evacuation state of residents is independently important.

Ouros transformation:

A settlement can preserve:

- the announcement that applied to an area;
- observed departure;
- known shelter/staging destinations;
- still-unconfirmed residents;
- later ordinary return.

Do not infer that a Pokémon species is dangerous because one authored incident involved that species.

### Lost at the Stamp Rally!

Source:
- https://bulbapedia.bulbagarden.net/wiki/BW51

Reusable structure:

A Trainer and Pokémon become separated in a crowded transit setting. Searchers use a known meeting point, leave a message when the other party is absent, and use transport-system staff/infrastructure to reconnect them.

Ouros transformation:

`MEETING_POINT_EXPECTED`, `MESSAGE_LEFT`, `MESSAGE_RECEIVED`, `LOCATION_CONFIRMED`, `CONTACT_ESTABLISHED` and `PHYSICAL_REUNIFICATION` are separate milestones.

This is useful well beyond emergencies. During a crisis, stale meeting-point assumptions and delayed messages can create fair mysteries without making anyone incompetent or deceptive.

### The Lonely Deino!

Source:
- https://bulbapedia.bulbagarden.net/wiki/The_Lonely_Deino%21

Reusable structure:

A Pokémon can remain at a care location while the expected Trainer is overdue, and the later arrival supplies an explanation for the separation. Temporary care does not automatically erase or replace the prior relationship.

Ouros transformation:

- expected pickup time;
- overdue state;
- temporary care/custody;
- claimant/association evidence;
- arrival/contact;
- authorized handoff;

should remain independently recorded.

This does not establish universal Pokémon boarding, ownership or release law.

### Lost at the League!

Source:
- https://bulbapedia.bulbagarden.net/wiki/Lost_at_the_League

Reusable structure:

A missing Pokémon search in a crowded public event uses surveillance, split search teams, physical traces and witness information before actual reunion. Different clues narrow location without becoming proof of current position forever.

Ouros transformation:

`SIGHTING`, `TRACE`, `CAMERA_DETECTION`, `WITNESS_REPORT`, `SEARCH_SCOPE` and `CURRENT_LOCATION_CONFIRMED` remain separate evidence types.

### Lumiose recovery after Team Flare

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Lumiose_City
- https://bulbapedia.bulbagarden.net/wiki/Shauna_(anime)

Reusable structure:

The setting continues after evacuation/crisis. Residents recover, public activity resumes, damaged places remain part of continuity, and characters later observe wildlife that left during the incident.

Ouros transformation:

Shelter closure, household reunification, return-to-home, infrastructure recovery and ecological return should not collapse into one `CRISIS_OVER` event.

## Public operational research

These sources are used only to extract information architecture. No US policy, legal authority, eligibility rule, health rule, shelter restriction, microchip regime, family definition or animal-handling procedure becomes Ouros canon.

### American Red Cross — contact and locate loved ones

Source:
- https://www.redcross.org/get-help/disaster-relief-and-recovery-services/contact-and-locate-loved-ones.html

Reusable architecture:

The service distinguishes different inquiry contexts and treats locating/reconnecting as a process rather than assuming a shelter roster proves reunion.

Ouros use:

- inquiry creation;
- relationship/household claim kept as a claim until already supported by Ouros canon;
- search scope;
- candidate information;
- verified contact;
- case closure reason.

A request to locate someone does not prove their relationship, current location or consent to disclose it.

### CDC — Stay Connected

Source:
- https://www.cdc.gov/prepare-your-health/plan-ahead/stay-connected.html

Reusable architecture:

Emergency communication may use multiple methods and planned meeting points. Separation therefore produces multiple possible evidence channels rather than a single global location field.

Ouros use:

Store message attempts and meeting-point expectations separately from verified receipt and physical presence.

### CDC — Emergency Shelter / Evacuation

Sources:
- https://www.cdc.gov/radiation-emergencies/response/emergency-shelter.html
- https://www.cdc.gov/radiation-emergencies/response/evacuation.html

Reusable architecture:

Evacuation route, reception point, shelter destination and later return are distinct stages. Communication failures can persist even when shelter services operate.

Ouros use:

Do not treat `EVACUATED`, `SHELTERED`, `CONTACTABLE`, `REUNITED` and `RETURNED_HOME` as synonyms.

### CDC — pets in emergencies

Sources:
- https://www.cdc.gov/healthy-pets/emergency-preparedness/index.html
- https://www.cdc.gov/healthy-pets/emergency-preparedness/pets-in-evacuation-centers.html

Reusable architecture only:

Human and animal accommodation may be physically or operationally separated during displacement, and reunification depends on persistent identity and records.

Ouros transformation:

Pokémon must use Pokémon Agency identity/custody/association state rather than importing real-world pet status. A Trainer and Pokémon can be at different sites. A Pokémon at a temporary care site does not automatically change owner, custodian, residence or active Trainer unless the authoritative Ouros state says so.

## Public tabletop/community cross-check

The standing project source scan already records public Pokémon Tabletop guidance favoring modular situation seeds, sandbox activity, self-contained local resolution and campaign callbacks. That supports using shelter/reunification records as persistent world state rather than a scripted disaster plot.

This pass did not find a sufficiently detailed new public PTU evacuation log that justified importing encounter procedure. No tabletop anecdote is used as mechanical evidence.

## Reusable narrative structures

### Distributed truth

One emergency can legitimately create multiple partial rosters:

- origin-area evacuation list;
- transport manifest;
- shelter intake record;
- care transfer record;
- temporary Pokémon accommodation record;
- household inquiry;
- self-reported relocation;
- departure record.

They answer different questions and may disagree without any record being fraudulent.

### Stale roster mystery

A person can be correctly registered at Site A at 14:10, depart at 15:00, make contact from Site B at 16:20 and still appear on a printed Site A roster at 17:00.

The mystery is resolved by timestamps and record purpose, not by making the roster “wrong.”

### Reunion as a sequence

A robust sequence can be:

`SEPARATION_REPORTED -> SEARCH/INQUIRY OPEN -> CANDIDATE LEAD -> LOCATION VERIFIED -> CONTACT VERIFIED -> MOVEMENT/HANDOFF IF NEEDED -> PHYSICAL REUNION -> FOLLOW-UP/DEPARTURE`.

Any stage may be skipped when direct evidence exists. None should be silently inferred from the preceding stage.

### Shelter history persists

A gymnasium, school hall, community building, arena concourse or other canon-approved site can temporarily function as a shelter and later return to ordinary use while preserving:

- floor markings;
- archived notices;
- photographs;
- altered storage;
- a new ramp or doorway;
- remembered routes;
- community relationships;
- future preparedness practices.

The site does not need to remain an emergency facility forever to remain narratively meaningful.

## Copyright transformation notes

No protected dialogue, distinctive characters, episode scripts, exact plot sequences or setting-specific technology is copied into proposed Ouros content.

Public Pokémon sources are used for abstract structures: distributed evacuation, search evidence, delayed pickup, multiple routes and post-crisis continuity.

Operational sources are used for information architecture only. Real-world law, eligibility, emergency powers, family definitions, animal rules and medical practices are excluded.

## PTU / Caelo cross-check

The internal source scan supports central plots, character-centric arcs, sandbox activity, Social/Wild Encounter/Job/Raid/Contest/Gym/Dojo containers and exact location mechanics when a governing source defines them.

It does not establish a universal PTU/Caelo subsystem for:

- emergency shelter intake;
- human reunification;
- guardian/child release;
- missing-person search procedure;
- carrying evacuees;
- crowd movement;
- panic;
- morale;
- protected civilian escort;
- shelter capacity;
- communication-network failure;
- Pokémon identification through visual recognition alone;
- emergency Pokémon custody;
- species-derived rescue competence;
- automatic communication between humans and Pokémon;
- evacuation created by a Move, Ability, Item or Trainer Feature.

These remain narrative/world-state or UNKNOWN unless a specific governing source and engine contract establishes them.

## Candidate design conclusion

Pass 128 should add a continuity layer that references Crisis shelter identity rather than replacing it. Its primary objects should be time-scoped presence, separation/inquiry, evidence-backed location/contact, reunification, departure and roster revision.

It should preserve human household/family facts by reference only, use Pokémon Agency for individual Pokémon identity and custody, and treat privacy as an explicit visibility problem.

Mechanically rich evacuation encounters need full and reduced versions. The reduced form should move all evacuees, records and noncombatant Pokémon in authoritative world state before BattleSpec creation, then use a static conventional battle.