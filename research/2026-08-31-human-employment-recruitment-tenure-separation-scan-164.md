# Human Employment, Recruitment, Tenure & Separation Scan — Pass 164

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file establishes Ouros canon.
Date: 2026-08-31

## Why this pass exists

The repository already has strong coverage for workplaces, staffing, assignments, careers, training, credentials, finance, organization identity, Pokémon work participation and service continuity. The full recursive repository tree was inspected before selecting this topic, followed by direct review of the closest design layers.

`design/workplaces-professions-staffing-layer.md` already owns workplace structure, occupational roles, staffing capacity, assignments, shifts, backlogs, career history and basic player employment. It also deliberately leaves labor law, wage standards, contracts, unions, retirement systems and workweek norms unresolved.

`design/pokemon-work-role-participation-extension.md` owns bounded participation by an exact Pokémon in an exact work task and explicitly excludes wages, labor law, compensation and human employment rights.

`design/finance-sponsorship-risk-layer.md` already separates financial promises, transfers and receipts. Therefore an employment extension should reference compensation commitments and payment events rather than create a second money system.

The missing continuity is the human employment relationship itself. Existing career history can record that a person held a role, but it does not yet preserve enough provenance for vacancy, application, selection, offer, acceptance, actual start, onboarding, changes during tenure, leave or temporary absence, return, separation, rehire and succession.

The aim of this scan is to identify reusable narrative structures for that lifecycle without importing a real-world legal regime or inventing PTU progression.

## Public source scan

### Pokémon Sword and Pokémon Shield — Poké Jobs

Source: The Pokémon Company, official Pokémon Sword and Shield website, “Poké Jobs.”
https://swordshield.pokemon.com/en-us/gameplay/pokejobs/

Observed high-level structures:

- institutions can publish bounded requests for help;
- different organizations can request different categories of work;
- assignment participation has an explicit beginning and return point;
- the posting exists separately from the individual selected for it;
- work can be a recurring part of ordinary regional life instead of a crisis or villain plot.

Useful Ouros transformation:

A job opportunity, a person accepting it and the later active employment relationship should be separate persistent records. The world should be able to remember that an opening was advertised even after it is filled, or that someone was selected but never actually started.

Explicit exclusions:

The videogame’s Pokémon Type suitability, duration/reward formulas, Experience Points, base-point rewards and item rewards are mechanics of Pokémon Sword and Shield. They are not imported into Ouros. This source also does not establish human labor rules for Ouros.

### Pokémon Concierge — newcomer, experienced staff and later mentoring

Sources:

Netflix Media Center, “Pokémon Concierge.”
https://media.netflix.com/en/only-on-netflix/81186864

About Netflix, “Sunny Skies and Bright Smiles: Stop-Motion Series ‘Pokémon Concierge’ Premieres on December 28.”
https://about.netflix.com/en/news/pokemon-concierge-main-trailer

Netflix official title page, episode descriptions.
https://www.netflix.com/title/81186864

About Netflix, “Stop-Motion Series ‘Pokémon Concierge’ Unveils Heartwarming Trailer for New Episodes Returning September 4.”
https://about.netflix.com/en/news/pokemon-concierge-new-episodes-premieres-september-4

Observed high-level structures:

- a newcomer joins an already functioning workplace rather than creating the institution by arriving;
- experienced coworkers remain distinct from the newcomer’s role and learning curve;
- first-day orientation and later responsibility can be separate episodes;
- a worker can progress from being shown how the workplace operates to helping orient someone else;
- daily work supports long-term character continuity without requiring promotion after every successful task.

Useful Ouros transformation:

Employment history should preserve tenure episodes and responsibility changes without equating them with PTU progression. A later mentoring or onboarding responsibility can be recorded as a workplace fact while Training/Coaching still owns any formal learning state.

Explicit exclusions:

No character, plot, dialogue, resort design, episode sequence or distinctive scenario is copied. The source supplies only the structural lesson that workplaces can support newcomer integration and changing responsibility over time.

### Pokémon Tabletop United — Trainer Classes remain mechanical surfaces

Source: public PTU reference index, “Classes - Pokemon Tabletop United.”
https://pturpg.wikidot.com/classes

The public reference distinguishes Trainer Classes and includes Professional classes such as Chef, Chronicler, Fashionista, Researcher and Survivalist alongside many other mechanical classes.

Reusable design lesson:

A world occupation and a PTU Trainer Class require separate authority. Someone employed as a cook, reporter, researcher, guide or musician does not acquire the corresponding PTU class by job title. Likewise, losing a job does not remove a Trainer Class.

Project rule:

Exact PTU/Caelo mechanics must still be checked against the project’s supplied Core Rulebook, Pokédex material, Caelo Player’s Guide, Caelo rulebook/errata, character-creation material and Location & Encounter List. The public index is corroborating evidence, not a replacement for project sources.

### Job offer and pre-start state as separate stages

Sources:

NSW Government, “Accepting your first job offer.”
https://www.nsw.gov.au/employment/your-first-job/accepting-a-job-offer

Fair Work Ombudsman, “Before starting employment.”
https://www.fairwork.gov.au/starting-employment/before-starting-employment

These sources distinguish receiving/reviewing an offer, accepting a position and actually starting employment. They also show that work-related records can be created between acceptance and the first day.

Reusable Ouros transformation:

`OFFER_ISSUED`, `OFFER_ACCEPTED` and `TENURE_STARTED` should remain separate events. A character may accept a future role while still finishing another commitment. A delayed start should not be rewritten as a rejected offer. An offer that expires without acceptance should remain historical.

Explicit exclusions:

Australian employment law, National Employment Standards, awards, minimum wages, probation rules, tax, superannuation, leave entitlements, notice requirements, age rules and record-retention requirements are jurisdiction-specific. None becomes Ouros canon through this research.

## Reusable narrative structures

A robust employment continuity chain can use the following authored stages when they actually apply:

```text
workplace need or vacancy
        ↓
opportunity/posting/referral
        ↓
application or candidacy
        ↓
selection/review episode
        ↓
offer
        ↓
acceptance or decline
        ↓
pre-start / onboarding preparation
        ↓
actual tenure start
        ↓
active work and responsibility changes
        ↓
leave / temporary coverage / return when applicable
        ↓
separation from the role
        ↓
handoff / vacancy / successor / rehire
```

No arrow is automatic.

A vacancy can be filled without a public posting. An applicant can be qualified and not selected. A selected candidate can decline. An accepted offer can have a future start date. Someone can leave a role without leaving the organization. A role can remain vacant after a departure. A previous worker can return later under a new tenure episode.

## High-value continuity separations

The following distinctions are useful for Ouros world state:

- vacancy exists separately from a posting;
- application exists separately from eligibility or selection;
- selection exists separately from an issued offer;
- issued offer exists separately from acceptance;
- acceptance exists separately from actual start;
- employment exists separately from mastery, PTU class or mechanical qualification;
- one shift absence exists separately from formal leave;
- leave exists separately from separation;
- separation exists separately from firing, resignation, retirement or misconduct;
- role end exists separately from workplace closure;
- promotion or transfer does not erase the prior role episode;
- compensation promised exists separately from compensation paid;
- payment evidence exists separately from any mechanical account update;
- holding workplace equipment or credentials exists separately from continuing employment;
- employment can coexist with organization membership, civic office, club membership or another job without collapsing those relationships into one state.

## Character and NPC structures

### The newcomer who becomes the person doing the handoff

A recurring NPC can first appear during onboarding, later become a reliable worker and eventually orient a successor or newcomer. This provides visible time progression without requiring a combat escalation.

### The qualified applicant who was never hired

An application can remain historically important even when the person was not selected. Years later the actor may work elsewhere, collaborate with the original institution or become a competitor. The old application is provenance, not a grievance generator by default.

### The worker with two simultaneous roles

A person may have a primary job and a recurring seasonal, civic, competitive or family-linked responsibility. Scheduling conflicts and availability emerge from explicit commitments rather than from arbitrary NPC disappearance.

### The former worker who still matters

A separation can end authority and routine responsibilities while preserving knowledge, relationships and public memory. The character may later answer a historical question, return as a guest, or help during an emergency without silently becoming an employee again.

## Quest and mystery patterns

Employment continuity supports low-violence investigations where several statements can all be correct:

- “she was hired” may mean selected, offered, accepted or actually started;
- “he stopped working there” may mean a shift ended, leave began, a transfer occurred or the tenure ended;
- “the replacement started Monday” may refer to orientation while the prior holder retained responsibility until Friday;
- “the old supervisor still has access” may reflect an unreturned credential rather than active authority;
- “the position was never filled” can coexist with temporary coverage by existing staff.

The mystery should reconstruct the correct state transitions instead of relying on automatic deception.

## Employment and compensation boundary

Narrative employment may store a reference to agreed or expected compensation only when canon establishes it.

Finance continues to own:

- payment commitments;
- payment events;
- balances or mechanical money references;
- reimbursements;
- grants or sponsorship funding;
- financial disputes.

Employment should be able to say that a compensation obligation was associated with a tenure. It should not generate a wage formula, calculate taxes, infer debt or change a mechanical balance.

## Pokémon participation boundary

Human employment and Pokémon work participation must remain distinct.

A human employee may work alongside a Pokémon. That does not mean the Pokémon is an employee. A Pokémon may have a bounded work assignment without implying salary, human employment status or ownership change. Any future canon concerning Pokémon labor rights or compensation requires an explicit separate decision.

## Battle implementation lessons

Most hiring, onboarding, leave, handoff and separation stories require no battle at all.

When a workplace incident intersects combat, the employment state should explain why an actor is present or absent but must never choose BattleSpec participants by itself.

Mechanically rich versions of workplace encounters may require:

- complete movement for escort, withdrawal or forced displacement;
- full turn/round lifecycle for multi-stage tactical timing;
- terrain/weather/hazards/zones/reactions for active workplace conditions;
- move-specific behavior, Abilities, Items or Trainer Features when explicitly used;
- AI tactical policy for protect, withdraw, route-control or objective behavior;
- Minecraft/Cobblemon/Craftics adapter/playback to present staff and noncombatants without granting them tactical authority.

Reduced versions can move workers and equipment outside BattleSpec before initiative, freeze geometry and allow AutoPTU to resolve only a conventional static confrontation.

## Canon questions left open

This scan does not establish:

- any Ouros labor law;
- wage standards or salary bands;
- employment contracts or enforceability;
- unions or collective bargaining;
- dismissal procedures;
- notice periods;
- mandated leave;
- probation rules;
- retirement benefits;
- workweek norms;
- child employment rules;
- anti-discrimination law;
- workers compensation;
- tax or payroll systems;
- Pokémon employment status or compensation;
- universal hiring exams;
- Trainer-level, Badge or Skill thresholds for ordinary jobs;
- automatic mechanical rewards for employment.

All of those remain uncertain until explicitly established by Ouros canon and, where mechanics matter, checked against PTU/Caelo and implementation evidence.

## Research conclusion

The useful addition is a provenance-rich human employment lifecycle that sits between Workplaces, Finance, Credentials, Training, Identity and institutional continuity. It should remember how a person entered, changed and left a role while keeping selection, authority, compensation, competence and PTU mechanics separate.
