# Ouros Narrative Research — Electoral Selection, Candidacy & Results — Pass 162

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon.
Date: 2026-08-31

## Why this pass exists

The full repository inventory was inspected before writing. The recursive `main` tree was not truncated.

Existing layers already cover adjacent responsibilities:

- Civic Governance owns civic bodies, proposals, consultations and authored decision procedures. It explicitly refuses to invent elections or voting rules.
- Civic Office owns holder episodes, acting coverage, mandate continuity and handover after a selection route produces a result. It explicitly refuses to invent the selection method.
- Public Notices owns notices and signage.
- Media owns publication and attributed claims.
- Public Memory owns later community remembrance.
- Supporter/Fandom owns organized support communities without converting support into formal authority.
- Archives and Personal Records own preserved source material and provenance.

The missing seam is narrower: when canon already says that an office or bounded public choice uses an electoral procedure, Ouros needs to preserve candidacy, eligibility, ballot options, voting windows, aggregate result states, recount/review lineage and the handoff from a confirmed result into Civic Office.

This pass does not establish that any Ouros polity is democratic, nor does it establish mayors, councils, parties, universal suffrage, secret ballots, terms, campaign finance, recall, veto or any other political institution.

## Pokémon source — Trovitopolis mayor

Source: https://bulbapedia.bulbagarden.net/wiki/Mayor_of_Trovitopolis

The anime includes a local mayor whose concern about a future election affects how he responds to a current problem.

Reusable structure:

- holding office, seeking another mandate and responding to an incident can be separate state objects;
- campaign incentive can influence an NPC without making every civic problem an election plot;
- public exposure can affect later political expectations without the narrative engine silently calculating a vote total.

Ouros use:

A candidate or incumbent may have authored motives connected to a selection process, but incident facts remain owned by the incident/evidence systems. The election layer records campaign context and official result state only.

Exclusion: no character, sewer incident, dialogue, creature reveal or plot resolution is imported.

## Pokémon GO — explicit candidate, voting window and later winner

Source: https://pokemongo.com/en/post/communityday-junjuly2020

Pokémon GO publicly used a community choice process with a defined candidate set, a bounded voting window, a stated counting rule and a later announced outcome. The two highest-ranked options had different downstream event consequences.

Reusable structure:

- option set exists before voting;
- eligibility to appear as an option is separate from support received;
- voting window has explicit opening and closing times;
- the count method is authored rather than assumed;
- rank can determine different downstream outcomes;
- campaigning/public advocacy can exist without being the authoritative count.

Ouros use:

Represent the procedure as data. Never infer `one person = one vote`, secrecy, geographic eligibility or tally rules from the word election. A local rule owns those details.

Exclusion: this is a real-world player-facing Pokémon GO event, not evidence that in-universe Ouros politics work this way.

## Election administration — preliminary result, canvass and certification are distinct

Source: https://www.eac.gov/election-officials/election-results-canvass-and-certification
Source: https://www.eac.gov/why-do-election-results-change-after-election-night

The U.S. Election Assistance Commission distinguishes unofficial reporting, canvass/reconciliation, audit where applicable and final certification. Procedures vary by jurisdiction.

Reusable structure only:

- first reported totals can be valid reports without being final;
- counting, reconciliation and certification are different episodes;
- chain of custody and discrepancy resolution can matter without implying fraud;
- a recount is not the same event as an audit;
- finality has an authored procedural source.

Ouros use:

`RESULT_REPORTED`, `COUNT_RECONCILED`, `RESULT_CONFIRMED` and `OFFICE_AUTHORITY_EFFECTIVE` remain separate clocks. Local Ouros canon must define which of these steps actually exist.

Exclusion: no United States election law, deadlines, offices, voting technology or certification procedure becomes Ouros canon.

## Public opinion research — poll, turnout and electorate are different populations

Source: https://www.pewresearch.org/course/public-opinion-polling-basics/

Pew's polling guidance emphasizes that election participation and broader public opinion answer different questions; participants in politics or public communication are not automatically representative of everyone.

Reusable structure:

- crowd size is not an electorate snapshot;
- a poll sample is not a vote count;
- nonparticipants remain part of the wider population even when they do not appear in the result;
- a winning result does not imply support for every proposal associated with the winner.

Ouros use:

Polls, rally attendance, supporter membership, endorsements, media attention, turnout and final result must remain separate observations.

## Pokémon fangame community discussion — political content needs world-specific issues

Source: https://www.reddit.com/r/PokemonRMXP/comments/1ls5vjw

A public Pokémon fangame discussion asks how politics can be included without merely reproducing current real-world disputes and proposes grounding conflict in the setting's own urban institutions and Pokémon-related questions.

Reusable lesson:

Political worldbuilding works better when disputes grow from established local resources, institutions, Pokémon relationships and consequences rather than importing contemporary partisan templates.

Ouros use:

Any future electoral arc should be generated from existing Ouros facts: route access, habitat stewardship, public works, Gym administration, service capacity, market rules, research access or other canon-owned issues.

This Reddit discussion is community design evidence only. It is not PTU or Pokémon canon.

## PTU/Caelo cross-check

Internal project source scan reviewed: `research/2026-08-18-source-scan.md`.

Relevant source priority remains:

- PTU Core Rulebook;
- Caelo Player's Guide 1.5;
- Caelo Region Location & Encounter List;
- character-creation material;
- errata/extra material;
- Pokédex material.

The source scan supports sandbox, character-centric and central-plot campaign structures, meaningful player choice, persistent activity containers and mechanically meaningful locations. It does not establish a universal election subsystem.

UNKNOWN until exact source review proves otherwise:

- universal election or voting Skill Checks;
- Charm, Command, Guile or Intimidate directly converting into votes;
- Trainer level, Badge count, League rank or class determining civic eligibility;
- a battle deciding a civic office by default;
- Cheerleader/Coordinator/public-attention mechanics becoming electoral support;
- Pokémon Loyalty representing constituency support;
- Features granting governmental mandate;
- Psychic/Aura abilities verifying ballots or candidate truth;
- Items or Moves authenticating political records;
- campaign rewards, office perks or election XP.

## Design conclusions

The selection layer must be procedurally explicit and politically agnostic. It should instantiate only after canon supplies a governing rule.

Candidate identity, qualification, option confirmation, endorsement, polling, voting, count, result reporting, review and office transition require distinct records.

Individual secret choices should not be persisted by default. Aggregate outcomes and authorized procedural events are enough for most stories. If a local canon rule allows named or public votes, that fact must be explicit.

A result should create a transition link, not mutate office authority immediately. Civic Office remains responsible for effective dates, acting coverage, credentials, records and pending matters.

## Copyright / transformation note

This pass extracts only high-level structures and design lessons. No protected dialogue, prose, distinctive plot sequence or character design is copied into Ouros proposals.