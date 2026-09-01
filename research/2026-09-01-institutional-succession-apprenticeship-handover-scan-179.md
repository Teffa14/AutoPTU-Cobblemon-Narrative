# Institutional Succession, Apprenticeship, and Handover Scan — Pass 179

Status: RESEARCH / PROVENANCE — NOT CANON
Date: 2026-09-01

## Purpose

This pass examines how Pokémon stories and tabletop play represent institutions that outlast one individual: leaders change posts, students gain bounded responsibility, apprentices graduate, former holders return, and organizations keep operating while a person is absent.

The goal is not to import Pokémon League structures into Ouros. The useful pattern is continuity of responsibility. Ouros already has persistent workplaces, resident relationships, service dispatch, schedules, communication provenance, public memory and fixed institutions. What is missing is an explicit distinction between relationship, skill, assigned duty, temporary authority and permanent office-holding.

This research therefore supports a proposed institutional-role continuity layer without altering established Marea canon.

## Repository duplication check

Before research, the Narrative repository tree and current design directory were inspected for succession, delegation, apprenticeship, acting roles, vacancies and handovers. Existing layers already cover relationships, questlines, service dispatch, local knowledge, communications, festivals, aftermath/recovery, language interpretation and ecological continuity. No dedicated authority/delegation/succession layer was found.

Relevant fixed Marea relationships remain authoritative and unchanged:

- Taro Min mentors Pia Min professionally. Their surname does not establish kinship.
- Sela Orrin mentors Jace Orrin. Their exact family relationship remains unresolved.
- Ema Rey works under Nerea Sol's project protocols.
- Lia Morn coordinates docks while Mina Cors operates ferry services.
- Brin Havel holds cooperative storehouse responsibilities.
- Mara Veyra coordinates Field Office reports and assistance.

None of these facts implies succession, promotion, legal authority outside the stated work, or inheritance.

## Public sources reviewed

### Janine and Koga — office continuity after promotion

Source: Bulbapedia, Janine
https://bulbapedia.bulbagarden.net/wiki/Janine

Source: Bulbapedia, Koga
https://bulbapedia.bulbagarden.net/wiki/Koga

Reusable structure:

Koga moves from one League office to another and Janine becomes the holder of the Fuchsia Gym role. The Gym remains a recognizable institution while the office-holder changes.

Design lesson:

An institution can have identity, responsibilities and public expectations independent of the current holder. A character's advancement may create a vacancy somewhere else. Succession therefore creates downstream continuity work rather than simply adding a new title to one NPC.

Do not import:

- Fuchsia Gym identity or visual design;
- Koga, Janine, their family structure or dialogue;
- Pokémon League promotion rules as universal Ouros law.

### Juan and Wallace — mentorship is not identical to office ownership

Source: Bulbapedia, Juan
https://bulbapedia.bulbagarden.net/wiki/Juan

Source: Bulbapedia, Wallace
https://bulbapedia.bulbagarden.net/wiki/Wallace

Reusable structure:

Juan is Wallace's mentor and previously held the Sootopolis Gym role. He entrusts that role to Wallace, then later returns when Wallace assumes another post. The relationship and the office persist on different timelines.

Design lesson:

Mentorship, competence, delegation, succession and return should be separate facts. A student may temporarily or permanently hold a role. A former holder may return. None of those facts requires the mentoring relationship to end.

Do not import:

- Sootopolis institutions;
- Water-specialist succession customs;
- Wallace/Juan story beats, personality or dialogue.

### Wigglytuff's Guild — graded responsibility and graduation

Source: Bulbapedia, Wigglytuff's Guild
https://bulbapedia.bulbagarden.net/wiki/Wigglytuff%27s_Guild

Reusable structure:

Apprentices perform ordinary chores and board jobs. Performance changes the difficulty of later assignments. Graduation is a distinct milestone, and successful graduates can remain associated with the institution afterward.

Design lesson:

Training can be represented through increasingly independent duties rather than only XP or dialogue. Small operational tasks establish trust and competence. Graduation or certification should not erase prior relationships, institutional memory or ongoing affiliation.

Do not import:

- the Guild's economics;
- its characters, graduation test or location;
- board percentages or exact advancement rules.

### Pokémon Ranger — rank expands assignment authority

Source: Bulbapedia, Ranger Mission
https://bulbapedia.bulbagarden.net/wiki/Ranger_Mission

Source: Bulbapedia, Pokémon Ranger
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Ranger_(video_game)

Reusable structure:

Ranger Missions are formally assigned jobs. Advancement follows completed work. Higher-status Rangers gain wider discretion, including the ability to initiate mission work in urgent circumstances.

Design lesson:

A role can expose capabilities through mandate rather than raw personal power. Authority should be scoped: who can request work, approve it, sign a record, redirect resources or act without prior permission can each be represented independently.

Do not import:

- Ranger ranks as Ouros civic grades;
- capture-styler mechanics;
- Ranger Union hierarchy wholesale.

### Public PTU campaign logs — institutions can be changing places, not static checkpoints

Source: r/PokemonTabletop campaign log #23
https://www.reddit.com/r/PokemonTabletop/comments/vgdvzc

The log describes a Gym during a grand opening or redesign and a team-oriented challenge. It is anecdotal tabletop evidence, not PTU rules authority.

Reusable structure:

A familiar institution can be introduced while it is changing. New participants can meet because a venue is reopening, reorganizing or testing a revised public function. The institution itself becomes a social scene rather than only a battle endpoint.

Do not import:

- campaign characters;
- its Gym challenge or homebrew rules;
- any GM ruling as PTU canon.

### PTU community discussion — mechanical Mentor must not be confused with social mentorship

Source: r/PokemonTabletop discussion, “What's your Favorite Class?”
https://www.reddit.com/r/PokemonTabletop/comments/f8hlxj

The discussion treats Mentor as a PTU class and discusses its table function. Community opinions are not rules authority, but they reinforce a terminology collision that Ouros must avoid.

The project's own read-only PTU catalogue is the rules cross-check: `TRAINER_CLASS_CATALOG.md` lists Mentor with explicit prerequisites and unlockables including Guidance, Lessons, Lifelong Learning and Move Tutor.

Design consequence:

`social_relationship = mentor/student` and `trainer_class = Mentor` must be stored independently. Neither proves the other.

## High-level patterns extracted

### 1. Role continuity can outlive the holder

A workplace should have a stable identity and mandate even when its regular holder is absent, promoted, transferred, incapacitated, retired or replaced.

### 2. Responsibility can increase before title changes

Training becomes visible when a character receives bounded independent work. This is more useful than an invisible “apprenticeship meter.”

### 3. Delegation has scope

Someone may be allowed to collect records but not certify them, run a warm-up but not authorize an official match, prepare an observation packet but not approve its interpretation, or receive cargo but not change berth priority.

### 4. Handover is evidence

Continuity creates documents and observable acts: keys change hands, a duty roster changes, records receive different preparer/reviewer names, a public notice identifies an acting contact, or a ledger contains a handover timestamp.

### 5. Absence should not freeze the institution

If Mara is on a route check, the Field Office should not become inert. The system should know which work can proceed, which waits for her, and which person is temporarily responsible for a narrow lane.

### 6. Succession can fail or reverse

An acting holder may return to the prior role. A trainee may need more supervised work. A role may stay vacant. A former holder can return. The model should not assume a one-way promotion ladder.

### 7. Public belief and actual authority can diverge

Residents may assume that a visible assistant is now “in charge.” Canonical authority remains a server-owned fact. Rumor/public-memory systems can represent the mistaken belief without granting powers.

### 8. Institutional advancement need not be combat advancement

A battle can demonstrate one kind of competence, but it cannot automatically prove document custody, research judgment, medical authority, scheduling discretion or leadership mandate.

## PTU / engine cross-check

The read-only AutoPTU source confirms that Mentor is a mechanical Trainer Class with explicit prerequisites and Features. Therefore ordinary language such as “Taro mentors Pia” must remain relationship canon only unless a separate PTU class assignment is canon-approved and parity-audited.

No PTU source inspected here establishes a universal game rule for civic succession, workplace promotion, delegated signatures or institutional hierarchy. Those should remain Ouros world-state concepts, not hidden mechanical bonuses.

No indexed Caelo material was found in Narrative, AutoPTU-Java or AutoPTU during this pass. This does not prove Caelo lacks such material. It means no Caelo-specific office law, inheritance custom, certification system, guild hierarchy or promotion ceremony is proposed as fact here.

## Original Ouros opportunities

The strongest immediate use is Marea because existing canon already contains real mentor/supervisor relationships and workplaces.

Potential arcs include:

- assistants receiving their first independently auditable duty;
- regular holders going off-site while services continue;
- a temporary acting assignment that residents misread as permanent promotion;
- a handover error that creates provenance ambiguity rather than a villain plot;
- a former responsibility being returned after a short assignment;
- two people being competent in different portions of one institutional workflow;
- a trainee deciding that they do not want the senior role despite being capable;
- an institution changing procedure after discovering that too much knowledge depended on one person.

## Provenance boundary

Everything above is research extraction or design inference.

Canon-approved material remains only what existing canon files already state. No Marea NPC receives a new title, rank, family relationship, PTU class, promotion, retirement plan, office, legal power or successor in this pass.
