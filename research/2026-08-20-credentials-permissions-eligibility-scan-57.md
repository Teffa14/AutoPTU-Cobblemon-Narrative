# Pass 57 Research — Credentials, Permissions, Eligibility & Scoped Access

Status: RESEARCH ONLY. Not Ouros canon. No rule text in this note supersedes the project PTU/Caelo corpus or the pinned AutoPTU oracle.

Date: 2026-08-20

## Research question

Ouros already models institutional invitations, regional recognition, conservation access policies, case participation, education, battle institutions, science programs, archives, workplaces and infiltration. Those layers repeatedly need to answer a narrower operational question: what evidence shows that an actor is qualified for a specific activity, who recognized that evidence, what access was actually granted, what scope does the grant cover, and when does that grant stop being valid?

The repository did not yet have one shared lifecycle for qualification evidence, credentials, admission tokens and permission grants. Without one, different systems risk inventing incompatible meanings for rank, badges, tickets, staff roles, research access or temporary authorizations.

This pass studies high-level structures only. It does not create a universal Trainer license, passport, visa, professional licensing regime, criminal-law framework or modern bureaucracy for Ouros.

## Internal repository overlap check

The existing `interregional-mobility-recognition-layer.md` already separates temporary access permissions from regional identity and treats recognition as an institutional decision rather than universal truth. It explicitly avoids assuming passports, visas, citizenship or nation-state borders.

The existing `conservation-protected-areas-stewardship-layer.md` already separates ecological state, management designation, visitor policy and enforcement capacity. Protected-area labels do not automatically create powers or PTU mechanics.

The existing `case-authority-custody-layer.md` already separates authored institutional mandate from general authority and stores per-case access levels and evidence access.

Pass 57 therefore should not replace those systems. It should provide shared records that those systems can reference.

## Public-source findings

### Pokémon Legends: Arceus — rank as scoped progression

Official Pokémon material for Pokémon Legends: Arceus describes Survey Corps research as increasing the player's rank, with higher ranks opening more areas for survey.

Source:
https://www.pokemon.com/uk/pokemon-video-games/pokemon-legends-arceus/

Reusable structure:

- rank can summarize demonstrated progression inside one institution;
- progression may unlock specific activity scopes or areas;
- higher rank does not imply universal authority outside the institution;
- access can be tied to a known progression state rather than public fame.

Ouros adaptation:

A research institution may recognize a field qualification and grant access to a named survey sector. The stored fact should be the grant and its scope, not a global statement that the Trainer is "authorized everywhere."

### Pokémon Ranger: Shadows of Almia — training, rank and responsibility

Official material describes the protagonist starting as a Ranger recruit, attending Ranger School and progressing toward higher Ranger standing.

Source:
https://www.pokemon.com/us/pokemon-video-games/pokemon-ranger-shadows-of-almia/

Reusable structure:

- formal training can precede operational responsibility;
- rank can describe progression within an institution;
- responsibilities can expand over time;
- education and active assignment remain separate concepts.

Ouros adaptation:

A completed course, a qualification record and an active mission permission should be three separate records. Graduating from a course should not automatically place an actor on duty or give access to every restricted location.

### Pokémon Legends: Z-A — earned eligibility token for one promotion challenge

The official gameplay description for the Z-A Royale states that advancement involves earning enough Ticket Points to obtain a Challenger's Ticket, which is then used for the relevant promotion match.

Source:
https://legends.pokemon.com/en-au/gameplay

Reusable structure:

- eligibility can be earned before an event;
- a token can prove eligibility for one bounded activity;
- holding the token does not equal winning the challenge;
- completing the challenge is a separate authoritative result.

Ouros adaptation:

Admission tokens can be single-use, limited-use or event-scoped records. They should never imply permanent rank unless an institution explicitly grants that rank after a separate resolution.

### Great Marsh — venue-specific admission and explicit limits

Official Brilliant Diamond/Shining Pearl guidance describes Great Marsh admission as a bounded activity with an entry fee, a defined step limit and a fixed number of Safari Balls.

Source:
https://diamondpearl.pokemon.com/en-au/trainersguide/fundamentals/

Reusable structure:

- admission can be specific to one venue and one visit;
- entry can grant bounded resources or opportunities;
- leaving or exhausting the visit can end the grant;
- admission does not create ownership of the venue or institutional status.

Ouros adaptation:

A protected-area observation ticket, event pass or guided-site entry can exist as a temporary permission record. Any PTU capture or item mechanics still require their own rules validation.

### Play! Pokémon organizer eligibility — operational precedent only

Current official Play! Pokémon support material uses time-bounded eligibility criteria for organizers, including reporting requirements for League Cups and Challenges.

Source:
https://support.play.pokemon.com/hc/en-us/articles/34818694136084-Eligibility-for-League-Cups-and-Challenges

This is real-world organized-play administration, not in-world Pokémon lore. It is useful only as an operational design precedent:

- eligibility can depend on recent verified records;
- qualification can expire or require re-verification;
- the system can keep the criteria version used for an assessment;
- failure to meet one criterion should not erase historical achievements.

Do not import current Play! Pokémon policy, reporting windows or organizer rules into Ouros.

### Public Ranger roleplay — prerequisite and mission-rank patterns

Public Pokémon Ranger roleplay communities have used mission prerequisites, recommended levels, party-size requirements and rank-limited assignments.

Examples:
https://bulbagarden.net/threads/pokemon-ranger-on-thin-ice.119603/post-3548729
https://forums.serebii.net/threads/pok%C3%A9mon-ranger-legends-in-the-making.338071/

Reusable structures:

- mission availability can be filtered before acceptance;
- prerequisites can be displayed clearly rather than discovered after failure;
- rank and specialization can be separate gates;
- player-created assignments can require institutional review before becoming official content.

These are community examples. Do not copy their missions, ranks, characters or setting material.

## PTU/Caelo boundary

The project-supplied Caelo material reviewed in earlier passes already establishes that some locations have explicit access requirements tied to items, levels or other authored conditions. Pass 57 should treat those as location-specific gates, not evidence that Caelo defines a universal credential system.

The complete Caelo primary files were not reliably recoverable in this runtime. No new Caelo-specific permit, certification or license rule is asserted here. Before canon promotion, any access requirement that claims to come from Caelo must be re-opened against the governing source document.

The implementation-oriented PTU narrative library available to this project also describes server-owned Trainer class, skill, capability and revision state and a gate service that evaluates canonical predicates rather than client claims. That is a useful authority pattern for future access checks, but it is project implementation evidence rather than a substitute for PTU rule text.

## High-value design lessons

### Qualification evidence should remain separate from permission

An actor may demonstrate a skill, pass a course or complete prior assignments without automatically receiving access to a new location. The institution must still decide what that evidence qualifies them for.

### Rank should never become a universal power score

A Survey rank, Ranger rank, tournament rank, academic standing and local guide qualification can coexist. They should not collapse into one global tier.

### Credentials need issuer and scope

A credential without an issuer and recognized scope is too ambiguous for a persistent world. The same record can be accepted fully, provisionally or not at all by another institution.

### Admission can be temporary

Many useful story structures require access for one event, one shift, one expedition, one supervised visit or one seasonal window. Temporary permission should be a first-class state rather than an exception.

### Physical token and authoritative permission are different

A badge, card, key, ticket, uniform or wristband can represent a grant. The world authority should still own the actual access record. Losing a card need not erase the underlying permission if the issuer can re-verify it. Possessing a stolen or counterfeit token should not create the grant.

### Suspension, expiry and revocation must preserve history

A credential can expire or be suspended while its issuance remains part of the Chronicle. Historical validity and current validity are different facts.

### Emergency access needs provenance

A crisis may justify temporary access by a responder, technician or specialist. That should create an explicit emergency grant with a source, scope and end condition rather than silently bypassing every future gate.

### Knowledge, reputation and permission are different

Being famous does not grant access. Being qualified does not guarantee public trust. Having access does not make an actor knowledgeable about everything inside the site.

## Copyright and transformation policy

This pass stores source attribution and high-level system patterns only. It does not copy protected dialogue, narrative scenes, unique missions, character arcs or distinctive plots. Official game mechanics referenced here are used as examples of structure and remain subject to project rules review before implementation.

## Proposed design direction

A shared Ouros layer should provide at minimum:

- qualification records;
- credentials with issuer and scope;
- versioned eligibility rules;
- eligibility assessments;
- temporary and permanent permission grants;
- admission tokens;
- supervision requirements;
- expiry, suspension and revocation events;
- access checkpoints;
- reciprocal recognition links;
- emergency overrides;
- audit/provenance history.

Other systems should reference these records instead of inventing their own `has_access=true` booleans.

## Research gaps

Before canon promotion, Ouros still needs authored answers for:

- which institutions actually issue credentials;
- whether any universal Trainer registration exists;
- what Badges prove outside League progression;
- what qualifications Rangers, researchers, guides, medics, technicians or excavators require;
- whether credentials expire;
- which interregional records are mutually recognized;
- how emergency access is granted;
- what access information is public versus private;
- whether a Pokémon can hold an institutional role or permission in its own right;
- the exact PTU/Caelo rules, if any, governing relevant classes, Skills, Features, badges, ranks or location requirements.
