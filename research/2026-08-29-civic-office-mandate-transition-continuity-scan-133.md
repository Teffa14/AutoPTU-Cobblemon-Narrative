# Public Research Scan — Civic Office, Mandate & Transition Continuity — Pass 133

Status: RESEARCH / PROVENANCE ONLY. Not canon.
Date: 2026-08-29

## Purpose

This scan supports a narrow missing continuity layer in Ouros: what happens when an authored civic or institutional role changes occupant, becomes temporarily vacant, receives acting coverage, or transfers records and pending responsibilities.

It does not define Ouros as an electoral democracy, monarchy, League administration, guild republic, hereditary polity, appointed bureaucracy, or any other universal political model.

The existing Civic Governance layer already requires decision procedures, mandate, quorum, tie rules and review routes to be authored locally. The existing Memorial/Absence/Succession extension already routes vacant-role questions to the owning institution and forbids automatic election, appointment, heredity or promotion.

The missing question is operational continuity after a role-change fact exists.

## Repository overlap check

The complete recursive repository tree was inspected before this topic was selected. The tree response was not truncated.

Adjacent material checked:

- `design/civic-governance-public-works-layer.md`
- `design/memorial-absence-succession-continuity-extension.md`
- existing credentials/authorization material in the repository inventory
- public adjudication/review continuity
- archives/records continuity
- workplace and institution continuity material
- public notice/public meeting layers
- engine readiness snapshots through Pass 132

This pass does not create a new universal election system. It adds provenance and design support for role-holder continuity once a local canon source has already established how a role exists and how a transition can occur.

## Source A — Marion Town / elected mayor as world-history consequence

Source:
https://bulbapedia.bulbagarden.net/wiki/Marion_Town

Publicly documented Pokémon pattern:

- Marion Town has a present-day mayor.
- The identity of that mayor is tied to a changed historical sequence.
- The changed office-holder coincides with a settlement that preserves more older buildings, vegetation and historical continuity than the earlier version shown in the story.

Reusable high-level lesson:

An office-holder can be a durable world-state variable whose effects are visible in later settlement history. The useful structure is not “the mayor personally controls every change.” It is:

`office holder -> authored decisions/influence -> projects or preservation choices -> persistent settlement state`

Ouros transformation:

- preserve office-holder history;
- preserve decision/project references separately;
- never infer that every world difference was directly caused by the office-holder;
- allow later players to reconstruct which changes were actually linked to an administration and which merely occurred during the same period.

Not imported:

- Marion Town characters;
- its time-travel plot;
- Celebi causality;
- electoral rules;
- mayoral powers;
- any protected dialogue or scene sequence.

## Source B — Trovitopolis / election pressure and abuse of current authority

Sources:
https://bulbapedia.bulbagarden.net/wiki/Mayor_of_Trovitopolis
https://bulbapedia.bulbagarden.net/wiki/EP102

Publicly documented Pokémon pattern:

- a current mayor is facing an election;
- actions taken while still in office affect public perception before that election;
- the episode distinguishes current office authority, campaigning/public image, an operational crisis and the later electoral consequence.

Reusable high-level lesson:

`CURRENT_OFFICE_HOLDER`, `CANDIDATE`, `PUBLIC_SUPPORT`, `AUTHORIZED_ACTION` and `NEXT_OFFICE_HOLDER` should be separate state.

Ouros transformation:

A person can still possess a valid authored mandate while their continuation in office is uncertain. Conversely, campaign popularity or anticipated succession cannot grant current authority early.

Useful invariants:

- `CANDIDATE != CURRENT_AUTHORITY`
- `CURRENT_AUTHORITY != GUARANTEED_NEXT_HOLDER`
- `PUBLIC_DISAPPROVAL != AUTOMATIC_REMOVAL`
- `ELECTION_EXPECTED != RESULT_KNOWN`
- `OFFICE_ACTION != PERSONAL_ACTION` unless provenance links the act to that office mandate

Not imported:

- the mayor character;
- coercive-response plot details;
- election calendar;
- police powers;
- civic structure;
- voting rules.

## Source C — Castelia mayor / bounded delegation during an emergency

Source:
https://bulbapedia.bulbagarden.net/wiki/Mayor_of_Castelia_City

Publicly documented Pokémon pattern:

The Castelia mayor authorizes an initial response to the Venipede crisis, listens to an alternative operational proposal, and allows another actor to handle a specific part of the response while retaining a broader responsibility if that effort fails.

Reusable high-level lesson:

Delegation can be scoped and reversible without transferring the entire office.

Ouros transformation:

Represent:

- delegating role-holder;
- delegated actor;
- delegated scope;
- start condition;
- expiry/review condition;
- retained responsibilities;
- evidence that the delegation was actually communicated.

Useful invariants:

- `DELEGATED_TASK != OFFICE_TRANSFER`
- `DELEGATION_GRANTED != EVERY_POWER_GRANTED`
- `DELEGATE_ACTS != ORIGINAL_HOLDER_ABSENT`
- `DELEGATION_EXPIRED != WORK_RESULT_INVALIDATED`

Not imported:

- the exact emergency;
- the mayor's powers;
- firefighting/containment rules;
- Pokémon behavioral assumptions.

## Source D — Fula City / mayoral office embedded in recurring civic traditions

Sources:
https://bulbapedia.bulbagarden.net/wiki/Fula_City
https://bulbapedia.bulbagarden.net/wiki/Mayor_Oliver

Publicly documented Pokémon pattern:

Fula City has a current mayor and a recurring Wind Festival tied to civic history and infrastructure. The useful lesson is that recurring public practices can outlast one office-holder.

Ouros transformation:

Keep institutional calendar, festival ownership, infrastructure responsibilities and office-holder identity separate. A transition should not silently cancel every recurring practice, and a new holder should not automatically inherit personal relationships or private knowledge from the predecessor.

Useful invariants:

- `OFFICE_CONTINUES != EVERY_PERSONAL_RELATIONSHIP_CONTINUES`
- `ANNUAL_EVENT_CONTINUES != SAME_SPONSOR_EVERY_YEAR`
- `ROLE_RECORDS_TRANSFERRED != PRIVATE_MEMORY_TRANSFERRED`

## Source E — Pokémon tabletop community: region design should contain civic texture beyond the League spine

Source:
https://www.reddit.com/r/PokemonTabletop/comments/iqxtg0

Community discussion around a custom PTU region recommends adding non-essential towns, intermediate areas and locations beyond Gyms and the League path.

Reusable lesson:

Civic continuity works best when offices serve ordinary places and services the players revisit. It should not exist only to issue plot orders.

Ouros transformation:

Role transitions can alter:

- maintenance priorities;
- meeting schedules;
- public notices;
- project sequencing;
- archive access procedures;
- festival coordination;
- conservation or market coordination where a local mandate already supports it.

The campaign should see those effects through ordinary world state, not only exposition.

This Reddit source is community experience, not PTU rules authority.

## Source F — Pokémon Mystery Dungeon community worldbuilding: office structures can vary by settlement

Source:
https://www.reddit.com/r/MysteryDungeon/comments/12ffr1e

A fan worldbuilding post proposes guildmasters, mayors, temporary appointments and sector representation with locally authored rules.

Reusable lesson:

The valuable design pattern is institutional heterogeneity. Different settlements can answer “who covers this role?” differently.

Ouros transformation:

Do not import the posted constitution. Instead, preserve a schema capable of representing:

- elected transitions where canon establishes elections;
- appointments where canon establishes appointments;
- temporary acting coverage;
- guild or League-linked roles where canon establishes them;
- elder or steward roles;
- deliberately unresolved vacancies.

The method must be referenced by an authored governing rule, never selected by the generator because it seems plausible.

## Source G — National Archives transition material / records and office continuity

Sources:
https://www.archives.gov/presidential-libraries/presidential-transitions
https://www.archives.gov/presidential-libraries/presidential-transitions-faqs
https://www.archives.gov/news/topics/presidential-records-act

These sources are used only as information-architecture references.

Public operational pattern:

- outgoing-office records can have a defined custody transition;
- institutional accounts can continue while prior content is preserved separately;
- official records and personal material require distinct treatment;
- archival preservation can occur independently from the incoming office-holder's current operations.

Ouros transformation:

Represent separate objects for:

- office record set;
- outgoing holder's private material;
- institutional communication channel;
- archived prior content;
- custody handoff;
- access state;
- unresolved records still needed for current work.

Useful invariants:

- `OFFICE_CHANGED != RECORDS_DELETED`
- `RECORDS_ARCHIVED != RECORDS_PUBLIC`
- `INSTITUTIONAL_CHANNEL_CONTINUES != PRIOR_CONTENT_REWRITTEN`
- `CUSTODY_TRANSFERRED != ALL_ACCESS_GRANTED`
- `PERSONAL_RECORD != OFFICE_RECORD`

Not imported:

- U.S. constitutional structure;
- Presidential Records Act rules;
- FOIA rules;
- transition dates;
- legal ownership doctrine;
- records-retention periods.

## Cross-source design synthesis

The reusable structure across the sources is a continuity chain:

`authored office -> current mandate state -> transition trigger -> governing transition route -> effective change -> scoped delegation/acting coverage -> record and credential handoff -> pending-matter continuity -> public notice -> later audit/history`

Each arrow can have its own timestamp and evidence.

A transition can therefore produce a mystery without fraud:

- a notice was signed by the outgoing holder before the effective transition but posted later;
- a delegate retained a narrow authority for one project after a broader office changed hands;
- an archive copied the old office account before the public directory was updated;
- a project decision was validly made under the old mandate and implemented under the new holder;
- a temporary acting holder handled routine service but lacked authority for a particular decision;
- two public sources can name different people because they answer different effective-time questions.

## Narrative structures extracted

### Transition without regime change

Routine office change changes some NPC relationships and priorities while the institution persists.

### Vacancy with bounded continuity

A role is empty while predefined routine functions continue through staff, delegated actors or another office. Any exceptional authority remains unresolved until the governing rule says otherwise.

### Project spanning holders

A public work, conservation decision, festival or service reform begins under one holder and completes under another. Players can investigate the project lineage without assuming sabotage or reversal.

### Competing clocks

Useful clocks include:

- result announced;
- result certified/approved if the local system has such a step;
- term ends;
- successor authority becomes effective;
- records physically move;
- public directory updates;
- old credentials deactivate;
- new credentials activate;
- pending delegation expires;
- first meeting occurs.

Only clocks explicitly supported by local canon should exist.

### Acting does not equal permanent

Temporary coverage can preserve service without deciding the final succession route.

### Institutional memory has seams

Some knowledge is in records. Some belongs to people. Some is tacit operational practice. A handover can be complete in one channel and incomplete in another without anyone acting maliciously.

## Faction dynamics extracted

Useful faction tension can arise from different interests rather than morality labels:

- continuity faction wants projects and services to keep moving;
- review faction wants inherited decisions checked before implementation;
- local operators care about practical deadlines;
- archive staff care about record integrity;
- public-interest groups care about notice and participation;
- outgoing allies may lose informal access without losing formal rights;
- incoming allies may expect access they do not yet possess.

No faction automatically becomes corrupt because it supports or opposes a transition.

## NPC archetypes extracted

### Acting Holder Who Knows the Limits

Can keep routine service moving and repeatedly refuses requests outside the temporary mandate.

### Outgoing Clerk With the Last Complete Timeline

Possesses practical knowledge of where decisions and records sit but cannot decide current policy.

### Incoming Holder With Inherited Decisions

Must distinguish active commitments, revisable proposals and completed facts.

### Continuity Officer / Records Steward

Tracks handoff packets, missing references and effective dates. This role exists only in regions/institutions where canon approves it.

### Long-Serving Operator

Knows how the service actually runs but may not know the formal reason behind every old procedure.

### Former Candidate or Alternate

Can remain a meaningful civic actor after losing or withdrawing without becoming an antagonist.

## PTU/Caelo mechanical guardrails

This topic is primarily world-state and social/institutional continuity.

Do not infer any of the following without an exact governing PTU/Caelo source plus implementation evidence:

- a universal Politics Skill;
- a universal election Skill Check;
- one Charm/Command/Guile roll deciding an electorate;
- Trainer Features granting civic authority;
- Pokémon species granting voting or office eligibility;
- Aura, Telepathy or Psychic Moves verifying political truth;
- Loyalty determining electoral support;
- battle victory granting office;
- battle defeat removing office;
- badges granting public mandate;
- League rank granting municipal authority;
- capture/ownership relationships determining representation.

Where a canon-authored social check exists, it may affect a narrow interaction. It must not silently replace the governing institutional procedure.

## Battle implementation implications

Most transition content should remain noncombat.

Mechanically rich scenes may involve protecting a handoff site, clearing access after an unrelated incident, or evacuating a public meeting. Those encounters must never make the battle winner the office-holder.

Full versions can require:

- Intercept or escort movement;
- phased withdrawals;
- protected zones/reactions;
- objective-aware AI;
- semantic Minecraft/Cobblemon/Craftics playback.

Reduced versions should resolve the transition/records operation before combat, remove protected actors and records from BattleSpec, and use a static conventional battle whose result only affects immediate physical access.

## Research-to-canon boundary

Everything in this file is research synthesis.

No election, office title, term length, succession route, delegation power, record-retention rule, mayor, council, guild government, League government, hereditary rule, appointment method or civic constitution becomes Ouros canon through this scan.

Promotion requires explicit regional and institutional canon approval.