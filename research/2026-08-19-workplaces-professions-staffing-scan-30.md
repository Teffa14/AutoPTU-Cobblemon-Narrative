# Workplaces, Professions & Staffing Research — Pass 30

Status: research and provenance only. Nothing in this file is automatically Ouros canon.

## Research goal

Ouros already has persistent institutions, services, clubs, workshops, clinics, farms, media, transport, infrastructure and public works. The missing layer is the ordinary work that makes those places function: roles, staffing, schedules, training, handoffs, workload, vacancies, temporary assignments and careers that change over time.

This pass studies how Pokémon settings and broader simulation research represent work without importing external plots, characters or mechanical reward systems.

## Existing-repository gap check

The repository already covers:

- mentorship and apprenticeships as social relationships;
- workshops and production;
- food/hospitality venues;
- care facilities;
- scientific institutions;
- transport services;
- media and communications;
- technology and maintenance;
- civic bodies and public works;
- faction agency;
- battle and performance careers.

What is not yet modeled as its own system:

- a workplace roster;
- operational roles distinct from PTU Trainer Classes;
- who is actually on duty;
- staffing shortages;
- workload and service backlogs;
- shift handoffs;
- temporary assignments;
- job postings;
- workplace training;
- qualification claims;
- career changes;
- succession inside ordinary organizations;
- Pokémon participating in work without being reduced to generic resource units.

## Source 1 — Pokémon Sword and Shield: Poké Jobs

Official source:
https://swordshield.pokemon.com/en-us/gameplay/pokejobs/

The official Galar material establishes that companies and universities request Pokémon help through Poké Jobs. Jobs are presented as requests from actual organizations rather than abstract grinding tasks. Different assignments prefer different kinds of Pokémon, and assignments have a duration.

Reusable structural lessons:

- work can originate from institutions with concrete needs;
- the same regional economy can contain many kinds of employers;
- assignments can remove an actor from immediate availability for a period;
- work demand can be discoverable through a shared posting system;
- Pokémon can participate in ordinary regional life outside battles.

Do not import Galar's EXP, EV, item rewards, type-matching formulas, durations or success ratings into Ouros.

## Source 2 — Galar regional culture

Official source:
https://swordshield.pokemon.com/en-au/story/the-galar-region/

The official region overview explicitly describes people and Pokémon living and working together and companies incorporating Pokémon into their workforce.

Reusable lesson:

Work should be visible in the physical world. If a settlement has shipping, farms, utilities, media, healthcare, construction or transport, there should be people and Pokémon whose routines make those services plausible.

This does not mean every worker needs a full simulation.

## Source 3 — Breadth of Galar employers

Secondary reference used for indexing/discovery:
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9_Job

The indexed Poké Job companies span shipping, monorail, restaurants, farms, pharmacies, laboratories, construction, courier services, media, energy, postal service, mining, banking, police and telecommunications.

Reusable structural lesson:

A believable Pokémon region should not treat Trainer, Professor, Gym Leader and shopkeeper as the only careers. Ordinary institutions create connective tissue between existing Ouros systems.

This source is not used as a mechanical authority.

## Source 4 — Characters can hold multiple professional identities

Official Pokémon sources:
https://www.pokemon.com/us/pokemon-news/a-look-at-pokemon-tcg-scarlet-violet-paldea-evolved-illustration-rare-cards
https://www.pokemon.com/us/features/reminisce-on-pokemon-scarlet-and-pokemon-violet-with-the-pokemon-tcg

Official material presents Iono as both a Gym Leader and streamer, while Cortondo is tied to Katy's bakery and other Paldean leaders are strongly embedded in local cultural work.

Reusable structural lesson:

A battle title should not consume the entire identity of an NPC. A Gym Leader can also have a profession, business, craft, public role or ordinary workplace obligation. A character can change one role without disappearing from every other social system.

## Source 5 — Work continues while adventures happen

Official Pokémon Horizons source:
https://www.pokemon.com/us/features/pokemon-horizons-season-2-the-search-for-laqua-part-1-quiz

The official recap describes Murdock working at Patisserie Soapberry while Orla repairs the Brave Olivine. This is a small but useful structural example: supporting characters can temporarily occupy different operational roles while the wider adventure continues.

Reusable lesson:

NPC availability should come from current commitments. A familiar NPC being absent from their normal location can have an ordinary cause such as a work assignment, repair job, training session or temporary coverage.

Absence does not need to imply kidnapping, betrayal or a quest.

## Source 6 — Believable daily planning in simulated communities

Research paper:
https://arxiv.org/abs/2304.03442

Generative Agents models agents that remember experiences, create plans, perform ordinary daily activities and revise behavior through observation, planning and reflection.

Reusable systems lesson:

Ouros does not need minute-by-minute NPC simulation. It can instead keep coarse schedules and commitments, then materialize detailed behavior only when the player is nearby or when a world-state event changes the plan.

Useful distinction:

- baseline schedule;
- current commitment;
- interruption;
- revised plan;
- historical record.

## Source 7 — Daily activity diversity warning

Research paper:
https://arxiv.org/abs/2603.23933

ORACLE studies generation of daily NPC activity plans and specifically targets repetitive activity sequences.

Reusable systems lesson:

Schedules should express role and context without becoming deterministic loops. Variation should arise from work state, season, workload, incidents, training, social commitments and player-caused changes rather than random noise.

## PTU/Caelo cross-check

The supplied PTU/Caelo material remains authoritative for mechanics.

Important boundary from the supplied character-creation material:

- a character concept, Skill Background, Edges, Features and combat statistics are separate authored/mechanical choices;
- therefore an Ouros occupational title such as mechanic, courier, archivist, nurse, baker, ranger aide, clerk or line worker cannot silently grant a PTU Trainer Class, Skill Rank, Edge, Feature or mechanical bonus.

Caelo already distinguishes Jobs as a mission/activity category. This pass uses `work assignment` for ongoing institutional labor and reserves `JOB` quest/activity semantics for playable missions. The two can intersect but should not be conflated.

Example:

- NPC occupation: ferry engineer;
- current work assignment: inspect western drive assembly;
- playable Job: retrieve a replacement component after the route is disrupted.

## Design lessons for Ouros

1. Work roles should be world-state facts, not mechanical classes.
2. Institutions need staffing capacity, not infinite omnipresent NPCs.
3. Routine work should compress unless it creates a decision or consequence.
4. Staff absence should have traceable causes.
5. Workplaces should produce backlogs when demand exceeds capacity.
6. Training and handoff can create story without granting free PTU progression.
7. Characters may hold multiple roles simultaneously.
8. A workplace can survive leadership change if its staff, knowledge and resources remain.
9. A title does not prove competence; qualifications need provenance.
10. Pokémon participation must be individual and capability-aware when mechanics matter.
11. Sending a Pokémon to work cannot imply unrestricted consent, ownership transfer or universal suitability.
12. Work should generate ordinary connections between systems: transport affects shops, clinics depend on staffing, maintenance affects utilities, festivals change hospitality demand.
13. Not every shortage is sabotage.
14. Not every resignation or transfer is a dramatic betrayal.
15. Career changes can emerge from accumulated experience without rewriting the character's past identity.

## Copyright/provenance boundary

No external dialogue, characters, plots, company branding, job text or game reward tables should be copied into Ouros.

Use only high-level structures:

- institutional demand;
- postings;
- staffing;
- temporary availability;
- ordinary occupations;
- multi-role identities;
- coarse daily schedules;
- plan revision.

## Research gaps

Future work still needs:

- exact PTU/Caelo rules for Skill use during professional tasks;
- which Caelo Trainer Features or homebrew rules affect downtime employment;
- whether AutoPTU should ever resolve non-combat work checks or leave them to a separate world-system service;
- what labor institutions, employment norms and compensation systems are actually canon in Ouros;
- how Pokémon agency/consent should be represented in institutional work;
- how much staffing simulation Minecraft can support without unnecessary entity load.