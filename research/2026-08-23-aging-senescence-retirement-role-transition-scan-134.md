# Research Scan — Aging, Senescence, Retirement & Role Transition — Pass 134

Status: RESEARCH / PROVENANCE. Not canon.
Date: 2026-08-23

## Scope and duplication check

This pass follows a full inventory of the narrative repository through Pass 133.

The closest existing systems are:

- `design/evolution-life-stage-transformation-layer.md`, which owns permanent Evolution/form transitions but does not model chronological aging or retirement;
- `design/family-kinship-generational-continuity-layer.md`, which owns kinship and continuity across generations but does not decide how one actor changes with age;
- `design/care-recovery-welfare-layer.md`, which owns care/recovery needs;
- `design/workplaces-professions-staffing-layer.md`, which owns current roles and staffing;
- `design/social-bonds-mentorship-clubs-layer.md`, which owns mentorship relationships;
- `design/pokemon-agency-partnership-release-layer.md`, which owns Pokémon identity, custody, partnership and agency;
- `design/memorials-remembrance-legacy-continuity-layer.md` and `design/loss-mourning-memorials-layer.md`, which own remembrance/loss rather than aging itself.

No existing layer owns chronological age, observed age-related change, competitive retirement, return from retirement, transition to mentoring/care/stewardship roles, or uncertainty around lifespan.

No material in this scan is promoted to canon.

## Project-source check — AutoPTU Career already has competitive longevity

Current read-only AutoPTU evidence contains a Career-only Pokémon longevity model.

Relevant project files:

- `tests/test_career_pokemon_longevity.py`
- `auto_ptu/career/roster.py`

Current inspected AutoPTU commit:

`8f003f5fa60b8d596c7f76daebb4c6a20235d53a`

The implementation tracks `career_health`, seasonal workload wear, intensive Training Kit wear, retirement reason/season, and removes a retired Pokémon from the active competitive roster. Tests explicitly distinguish sustainable normal training from intensive training wear and expect competitive retirement after accumulated seasonal workload.

Important boundary:

This is a Career simulation policy, not evidence for a universal PTU biological aging rule. The code itself describes the mechanic as competitive career health and workload. Ouros may reference this model when integrating Career-mode retirement, but must not reinterpret it as species lifespan, disease, death, permanent stat loss, or a canonical biological senescence formula.

A retired Career Pokémon remains the same persistent Pokémon. The current Career implementation makes it unavailable to the active competitive roster; it does not prove that the Pokémon cannot travel, socialize, mentor, work, live in a sanctuary, participate in non-competitive activities, or ever return under another ruleset.

No reliable Caelo age/lifespan rule text was recovered in an invocable form during this run. Super PTU Online Helper was not exposed as a callable capability. No result is invented for either source.

## Source 1 — Official Pokémon: elderly Stoutland and end-of-life care

Official episode page:
https://www.pokemon.com/us/animation/seasons/20/episode-21-one-journey-ends-another-begins

The official summary states that Stoutland is old, develops serious breathing trouble, and reaches a point where Nurse Joy can do little. The earlier episode also establishes Litten gathering food for the elderly Stoutland.

Related season page:
https://www.pokemon.com/us/animation/seasons/20

Reusable structure:

- old age can exist as a real state in the Pokémon world;
- an older Pokémon may receive care from another Pokémon without Trainer ownership;
- decline can be gradual and observable before death;
- care can become the story even when cure is not available;
- death is a separate event from being old, injured, fainted, missing, released or retired.

Ouros transformation:

Age-related observations should be longitudinal and individual. A Pokémon can have an `age_status` or estimated age range and separate functional observations. A decline in endurance, appetite, mobility or social routine becomes a care/science observation, not an automatic mechanical penalty.

Mechanical guardrail:

This source does not provide lifespan numbers, aging rates, PTU stat penalties, retirement thresholds, death checks, healing modifiers or species-wide senescence rules.

## Source 2 — Official Pokémon: Mustard, retirement without loss of competence

Official retrospective:
https://www.pokemon.com/uk/news/celebrate-25-years-of-pokemon-with-memorable-moments-from-the-galar-region

Official character page:
https://swordshield.pokemon.com/en-ca/expansionpass/characters/

Mustard is a former Galar Champion who retired from that role and became a teacher at the Master Dojo. The official material also emphasizes that his age and retired status do not make him an incapable battler. He held the Champion seat for 18 years and later trained Leon.

Reusable structure:

- retirement can mean a role transition rather than a loss of capability;
- former elite performers can become mentors, teachers, selectors, historians or institutional anchors;
- a retired person may still compete or demonstrate skill in selected contexts;
- public expectation based on age can be wrong.

Ouros transformation:

Store `role_status` separately from functional capability and current battle eligibility. A Trainer can retire from League competition while remaining a strong battler, teacher, Gym adviser or occasional exhibition participant.

Do not infer that every veteran wants to mentor others.

## Source 3 — Official Pokémon: Opal and very long tenure

Official character page:
https://swordshield.pokemon.com/en-au/people-galar-region/fairy-type-gym-leader-opal/

Opal is identified as the oldest Gym Leader in the Galar League and as having held her position for 70 years.

Reusable structure:

- institutions can contain extremely long tenures;
- advanced age does not automatically force retirement;
- succession planning can exist while the current holder remains active;
- institutional memory can become concentrated in one person without making that person omniscient.

Ouros transformation:

A long-serving Gym Leader, curator, ranger, engineer or researcher can accumulate historical observations and relationships. Their records and experience remain evidence, not infallible truth. Succession can be planned, delayed, contested or revised independently of age.

## Source 4 — PTU official blog: Torkoal and long-lived Pokémon as campaign continuity

Pokémon Spotlight: Torkoal:
https://pokemontabletop.com/pokemon-spotlight-torkoal/

The PTU developer blog explicitly treats Torkoal's assumed tortoise-inspired longevity as a source of plot hooks. One proposed structure is an old Torkoal that has lived through several Trainers and retains a long personal history.

Reusable structure:

- a long-lived Pokémon can connect different eras of Chronicle;
- old accessories, records and former partnerships can become provenance;
- an individual may outlive a Trainer or institution;
- age can increase narrative history without requiring mechanical bonuses or penalties.

Critical qualification:

The blog itself calls the lifespan assumption an assumption inspired by tortoises. Treat it as campaign inspiration, not a universal PTU/Caelo lifespan table. Do not promote Torkoal longevity to Ouros canon until the project authors it.

The article also contains optional variant/homebrew mechanics. None of those mechanics are imported by this pass.

## Source 5 — Wildlife aging: within-individual behavior can change with age

Nature Ecology & Evolution, 2022:
https://www.nature.com/articles/s41559-022-01817-9

A 46-year longitudinal study of individually monitored red deer found within-individual changes in social connectedness and spatial behavior as animals aged, including smaller home ranges and changes in where individuals spent time.

Reusable structure:

- aging can change routine and spatial use before creating obvious physical incapacity;
- longitudinal data on the same individual is more informative than comparing one young and one old animal;
- social withdrawal or route contraction may be an observation, not a personality judgment.

Ouros transformation:

If a persistent Pokémon gradually uses a smaller range, stops joining a seasonal aggregation or changes resting sites, Chronicle can preserve the pattern. The cause remains open: age, health, resources, social structure, disturbance, preference or another factor.

Do not create a universal `old Pokémon become solitary` rule.

## Source 6 — Older individuals can retain or contribute important knowledge

Scientific Reports, 2020:
https://www.nature.com/articles/s41598-020-70682-y

Research on African savannah elephants describes older males as disproportionately important leaders in collective movement and discusses the value of ecological knowledge in long-lived social species.

Nature Communications, 2016:
https://www.nature.com/articles/ncomms12793

Research on whooping cranes found age/experience important in innovation of migration patterns in changing environments and discusses how older individuals can contribute knowledge in long-lived social species.

Reusable structure:

- age-related decline in one domain can coexist with increased value in another;
- route knowledge, seasonal memory and institutional/ecological experience can persist after peak physical performance;
- removing an old individual from a system can have consequences beyond population count.

Ouros transformation:

A veteran Pokémon may become less active in competition while remaining important to Migration, Social Learning, field work or younger individuals. That importance must be demonstrated through observations and history, not inferred from age alone.

## Source 7 — Learning changes across life stages without a single global age effect

Nature Communications, 2021:
https://www.nature.com/articles/s41467-021-27626-5

A long-running study of whooping cranes found a shift from stronger reliance on social information in subadults toward greater reliance on individual experience in mature birds when adjusting migration timing.

Reusable structure:

- age, experience and learning mode are related but not interchangeable;
- the same individual may solve the same ecological problem differently at different stages;
- experience can matter without becoming a numeric intelligence or wisdom stat.

Ouros transformation:

Keep chronological age, accumulated experience, learned routines and demonstrated knowledge as distinct records. A newly evolved Pokémon can be old; a high-level Pokémon can be young; a long-lived individual may have little experience with a newly altered habitat.

## High-level Ouros design lessons

1. Chronological age, biological condition, competitive wear, injury and role status must remain separate.
2. Retirement is a transition, not death.
3. Old age does not mean weak, inactive, ill, wise, social, antisocial or ready to mentor.
4. A young actor can retire; an old actor can remain active.
5. Career's `career_health` is a competitive policy layer, not species biology.
6. Species lifespan claims need authored or rules-supported provenance.
7. Persistent individuals should retain identity across active career, retirement, care, return, release and later observation.
8. Longitudinal observations are safer than age stereotypes.
9. Experience and historical knowledge can increase while some physical capacities decline.
10. Succession should be triggered by role/institution state, not a hard age cutoff unless canon explicitly establishes one.
11. A retirement can be temporary, partial, role-specific or final for a specific activity.
12. Death requires its own confirmed event and rules boundary.
13. Minecraft appearance must never infer age mechanically.
14. No universal age-based stat modifier should be invented.
15. Some aging stories should contain no crisis: a character simply changes schedule, hands off a role or stops competing.

## Mechanics boundary

No source in this scan establishes a generic PTU/Caelo rule for:

- lifespan by species;
- age-based Combat Stage changes;
- age-based stat loss;
- age-based movement reduction;
- forced retirement;
- death from old age;
- veteran bonuses;
- mentor bonuses from age;
- healing penalties for older Pokémon;
- automatic memory or wisdom;
- reproduction limits by age;
- recovery from Career retirement;
- competitive re-entry after retirement.

Those remain blocked until the project has authoritative rule/canon support.

## Source reuse / copyright boundary

Only high-level structures and factual summaries are retained. No protected dialogue, distinctive plot sequence, character writing or fan-campaign prose is copied. The proposed Ouros material in Pass 134 must remain original and NON-CANON until explicitly promoted.