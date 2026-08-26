# Pass 175 — Civic volunteering, donations & community support research

Status: research/provenance only. Nothing in this file is Ouros canon.

## Why this pass exists

Repository audit before writing found no dedicated authority for general civic volunteering, spontaneous helpers, community-service projects, donation drives, donor intent, volunteer assignment, shift completion, or the handoff from donated goods into an existing Supply Chain/Inventory system.

This is intentionally separate from:

- `social-bonds-mentorship-clubs-layer.md`, which owns clubs and relationship state;
- `worker-associations-collective-representation-layer.md`, which owns worker-created associations, workplace mutual aid and representation;
- `crisis-rescue-recovery-layer.md` and `emergency-services-dispatch-incident-coordination-layer.md`, which own incidents, operational objectives and responder coordination;
- `currency-accounts-payments-settlement-layer.md`, which owns money transfer and settlement;
- `supply-chains-procurement-inventory-layer.md`, which owns physical stock after acceptance into an inventory system;
- `credentials-permissions-eligibility-layer.md`, which owns any real qualification or access requirement;
- `working-pokemon-institutional-roles-layer.md`, which owns Pokémon participation in institutional work.

The missing layer is the civic participation process itself: an institution or community has a bounded need; people offer time, goods or other support; those offers are screened, assigned, accepted, declined, redirected, completed or closed; the receiving system then owns the resulting work or goods.

## New source scan

### Pokémon Rescue Squad — recurring local service teams

Official Pokémon episode page: “Team Eevee and the Pokémon Rescue Squad!”
https://www.pokemon.com/us/animation/seasons/16/episode-5-team-eevee-and-the-pokemon-rescue-squad

The episode presents a family-operated Pokémon Rescue Squad dedicated to helping people in need. The squad has multiple teams, receives distress calls, investigates a dam incident, evacuates workers and attempts a rescue.

Reusable structure:

1. a persistent community service organization exists before the protagonists arrive;
2. requests arrive through an established route;
3. several teams can divide work;
4. the incident still has separate infrastructure and hazard truth;
5. helping during one emergency does not imply ownership of the affected facility or authority over all future incidents.

Ouros transformation: civic groups can maintain readiness, local knowledge and public trust across years. Their volunteer/service identity should remain distinct from the formal Emergency Services layer. A community rescue association may assist an authorized incident commander without becoming the command authority.

### Pokémon Ranger — helping people and Pokémon as an institutional mission

Official Pokémon Ranger pages:
https://www.pokemon.com/us/pokemon-video-games/pokemon-ranger/
https://www.pokemon.com/us/pokemon-video-games/pokemon-ranger-guardian-signs/

Pokémon describes Rangers as protecting nature and helping people and Pokémon in need. The games also distinguish recruitment/training, missions and repeated public-service work.

Reusable structure:

- civic or institutional service can be a long-term identity rather than a sequence of unrelated quests;
- service work can cross ecology, rescue, transport, investigation and public safety;
- a participant can be trained for some roles and not others;
- Pokémon assistance remains contextual rather than a universal resource.

Ouros transformation: recurring service institutions should emit bounded opportunities such as trail stewardship, festival support, shelter logistics, wildlife monitoring or public-information assistance. Actual PTU mechanical qualifications remain with Credentials/PTU rules.

### Pokémon Mystery Dungeon: Rescue Team DX — request-driven helping loop

Official game page:
https://mysterydungeon.pokemon.com/en-us/

The game centers on rescue/help requests and repeated journeys undertaken because others need assistance. The useful structure is not its dungeon mechanics; it is the social loop where helping creates an identity, recurring request channel and history of completed missions.

Ouros transformation: community-support organizations can accumulate a service ledger and public memory. Routine low-risk requests should compress; unusual requests become playable when they intersect with real world state or player choice.

### PTU community campaigns — service organizations as campaign framing

Public PTU examples:
https://www.reddit.com/r/PokemonTabletop/comments/sj1mk8/
https://www.reddit.com/r/PokemonTabletop/comments/9nrfy4/

One campaign frames players as Rangers serving cities across Fiore. A later community reply describes academy Ranger coursework built around simulated disasters and rescue tasks.

Reusable lessons:

- service can provide a durable campaign frame without requiring every episode to be villain-driven;
- simulated drills can prepare characters before real incidents;
- noncombat objectives can remain meaningful even when battle is possible;
- the same institution can support episodic stories while retaining persistent facilities, staff and records.

These are community/homebrew references, not PTU rules sources.

### FEMA — spontaneous volunteers need assignment and coordination

FEMA “Managing Spontaneous Volunteers in Times of Disaster”:
https://www.fema.gov/pdf/emergency/disasterhousing/ManagingSpontaneousVolunteers.pdf

FEMA IS-244.B, Developing and Managing Volunteers:
https://training.fema.gov/programs/independent-study/courseoverview.aspx?code=IS-244.b&lang=

The material separates offers to help from actual assignments. It recommends reception/coordination, identifying needs, matching skills/interests to roles, orientation, supervision, referral to receiving organizations, and deactivation when work is complete.

High-value abstraction for Ouros:

`NEED -> OFFER -> INTAKE -> SCOPE CHECK -> ASSIGNMENT -> RECEIVING ORGANIZATION -> WORK EVENT -> COMPLETION/HANDOFF -> REVIEW`

Important design lesson: good intent is not the same as authorization or suitability. A spontaneous helper can be valuable without being permitted to enter a restricted area, administer medicine, handle hazardous material, operate machinery or command Pokémon.

### FEMA — donations can become a second logistics problem

Volunteer and Donations Management Support Annex:
https://www.fema.gov/sites/default/files/2020-07/fema_nrf_support-annex_volunteer.pdf

FEMA training material also warns that unsolicited donated goods can overwhelm distribution systems when they are not matched to actual needs.

Ouros abstraction:

`DONATION_OFFER -> ACCEPT/REDIRECT/DECLINE -> RECEIPT -> CONDITION/USE CHECK -> INVENTORY HANDOFF -> ALLOCATION`

Donor intent and recipient need remain separate. A donation can be generous, authentic and unusable for the stated purpose at the same time.

This source is used only as operations architecture. Ouros does not inherit US emergency law, NGO structures, tax treatment, liability rules or federal terminology.

## Design conclusions

### Volunteer does not mean employee

A person can contribute time without acquiring an employment relationship, workplace authority, permanent membership or professional credential.

### Arrival does not mean assignment

Showing up at a site never creates permission to work there. This is especially important for multiplayer, crises and sensitive ecological sites.

### Service completion does not create permanent reputation mechanics

Public Memory may record participation. Social layers may remember shared events. No Charm, Command, Skill Rank, XP or mechanical reputation bonus is created by this layer.

### Donation does not mean acceptance

A physical item remains under its prior ownership/custody rules until the recipient actually accepts the handoff. After acceptance, Material Culture and Supply Chains become authoritative.

### Donation does not mean useful

The item may be wrong, redundant, damaged, incompatible, unsafe, excessively costly to store, or simply no longer needed.

### Donor intent is not recipient authority

A donor can request that a gift support a specific purpose. The receiving institution still decides whether it can lawfully/operationally accept and use it within its authored rules.

### Volunteer history should be bounded and factual

Record what happened: assignment, hours/session, site, supervisor/host, outcome, handoff and incident references. Do not infer altruism, loyalty, ideology, friendship, sainthood or future willingness.

### A volunteer can decline

Declining an assignment, leaving after a shift, refusing a hazardous task or choosing not to return must not create a hostility state.

### Pokémon participation stays separate

A Pokémon accompanying a volunteer does not automatically become a working Pokémon. Any institutional assignment goes through Pokémon Agency / Working Pokémon and the applicable PTU capability evidence.

## PTU/Caelo mechanical cross-check

Public PTU material contains Skills such as Command, Charm, General Education, Medicine Education, Pokémon Education, Survival and Technology Education, plus Features that can reference them. None of that creates a generic “Volunteer” rule or allows narrative service history to grant mechanical qualification.

No reliable Caelo primary text was recovered in this run that defines volunteer organizations, charitable donations, civic service ranks or service-based progression. Super PTU Online Helper was not exposed as an invocable capability in this runtime.

Therefore Pass 175 adds no volunteer DCs, service XP, morale bonuses, donation prices, fundraising rolls, emergency credentials, Pokémon work bonuses or automatic social progression.

## Narrative lessons for Ouros

- Mature institutions should sometimes solve ordinary needs without the player.
- A surge of goodwill can create its own coordination problem without making volunteers foolish or malicious.
- Community groups can persist across crises and quiet years.
- The interesting choice is often where limited people/time/goods should go, not whether anyone is willing to help.
- A declined or redirected donation can still produce a good story about mismatched needs, storage, provenance or public expectations.
- Volunteers can become future staff, club members, specialists or recurring NPCs only through later authored transitions.
- Successful preparedness should reduce emergency quest volume over time.
- Service history can become Public Memory, Archives, oral history or memorial material without becoming a universal prestige score.
