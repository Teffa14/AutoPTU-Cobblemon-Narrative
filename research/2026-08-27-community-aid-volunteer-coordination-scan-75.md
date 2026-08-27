# Community Aid, Volunteer Coordination & Mutual Support Research — Pass 75

Status: research/provenance only. Nothing in this file is Ouros canon.

## Why this pass

The repository already has strong ownership boundaries for workplaces, clubs, civic bodies, crises, service access, finance, equipment, credentials and public memory. After inspecting the full repository tree and the adjacent systems, one operational gap remained: help that is offered and coordinated without automatically becoming employment, club membership, formal authority, professional qualification or a crisis command role.

This pass researches reusable structures for community aid, volunteer participation, temporary support teams, informal assistance and persistent local contribution. It does not define labor law, compensation, mandatory service, charity institutions, legal liability, emergency powers or universal cultural expectations for Ouros.

## Repository overlap review

### Workplaces

`design/workplaces-professions-staffing-layer.md` owns occupational roles, work assignments, shifts, staffing capacity, backlogs and professional handoffs. A volunteer commitment must not silently become a job, occupational role or proof of professional competency.

### Social bonds and clubs

`design/social-bonds-mentorship-clubs-layer.md` owns clubs, membership, mentorship and relationship history. Helping at one cleanup, food table or search does not create club membership, friendship, debt or loyalty.

### Crisis / rescue / recovery

`design/crisis-rescue-recovery-layer.md` owns emergency truth, response state, shelters, staging, hazards, evacuation and recovery. A volunteer layer may coordinate helpers only within roles and areas that the crisis owner actually makes available.

### Civic governance

`design/civic-governance-public-works-layer.md` owns collective decisions and institutional mandates. Community participation cannot manufacture government authority.

### Finance / procurement / material culture

Money, goods, purchase, custody and exact items remain owned by their specialist systems. An aid record may reference an in-kind contribution or a funded need, but does not invent prices, ownership transfer or item effects.

## Source 1 — Pokémon Mystery Dungeon rescue-team base renovation

Public source:
https://mysterydungeonwiki.com/wiki/Rescue_Team%3AStatues

Additional corroborating source:
https://bulbapedia.bulbagarden.net/wiki/Uproar_Forest

Observed high-level structure:

- a persistent place receives help from several actors;
- contribution changes the visible world rather than disappearing after a quest-complete flag;
- different helpers participate for different reasons;
- participation can pause when a helper's condition for continuing is not met;
- completion creates a new baseline for later scenes.

Reusable lesson for Ouros:

A community project can persist as a sequence of contribution episodes. Each participant may have a separate commitment, limit and end condition. A project should survive a helper leaving, pausing or renegotiating involvement if other world-state dependencies allow it.

Transformation boundary:

Do not copy the rescue-team characters, chestnut bargain, base design, dialogue or plot. Ouros should use original locations, motives and project types. Do not infer that Pokémon species have construction capability merely because a Pokémon performed work in another continuity.

## Source 2 — Pokémon Mystery Dungeon secondary response team

Public source:
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Mystery_Dungeon:_Red_Rescue_Team_and_Blue_Rescue_Team

Observed high-level structure:

When a capable standing team fails to return, other capable actors organize a separate response rather than waiting indefinitely for the original group.

Reusable lesson for Ouros:

Response capacity can be layered. A standing institution may remain the authority while temporary outside helpers form a supplementary team, especially when workload exceeds normal capacity. The supplementary group still needs role boundaries, eligibility and a handoff to the system that owns the incident.

Transformation boundary:

Ouros must not infer rescue qualifications, leadership, combat capability or emergency authority from willingness alone. Exact eligibility must come from credentials, authored qualifications, demonstrated capability and the owner system.

## Source 3 — Pokémon Legends: Arceus, Setting Up the Bogbound Camp

Public source:
https://pokejungle.net/pokemon-legends-arceus/requests-guide/

Cross-check:
https://pokemondb.net/legends-arceus/missions-requests

Observed high-level structure:

- an institution is already responsible for establishing a persistent field facility;
- an outsider is asked to remove one blocker;
- after the blocker is resolved, the responsible institution completes the site;
- the resulting camp remains available afterward.

Reusable lesson for Ouros:

Player help can be narrow and still matter permanently. A helper does not need to perform every step of a project. The cleanest handoff is often: specialist system identifies need -> outside actor removes one blocker -> specialist staff completes or verifies the work -> world state changes persistently.

Transformation boundary:

Do not make every player contribution equivalent to employment, construction competency or permanent staff status. The owning institution retains responsibility for the work it actually performs.

## Source 4 — PTU community discussion: nonviolent travel encounters

Public source:
https://www.reddit.com/r/PokemonTabletop/comments/1fta66r/

Observed high-level structures reported by PTU GMs/players include:

- lost travelers asking for directions;
- injured wild Pokémon that can be helped instead of fought;
- rescue of a person or Pokémon stuck in a difficult location;
- foraging assistance for a craftsperson;
- recovering a lost personal object;
- bargaining or problem-solving with wild Pokémon rather than defaulting to combat.

Reusable lesson for Ouros:

Small acts of assistance can be complete scenes without becoming combat, formal quests or permanent relationships. A persistent world benefits from remembering the specific action and later consequence rather than rewarding every act with a generic reputation meter.

Source-quality note:

This is community practice, not PTU rules authority. It is used only for scenario structure and pacing. Mechanical checks, Pokémon agency, capture, healing, Skills, Features and rewards remain governed by PTU/Caelo plus project implementation.

## Source 5 — PTU living-server practice

Public source:
https://www.reddit.com/r/PokemonTabletop/comments/1dm8936/

Recent related source:
https://www.reddit.com/r/PokemonTabletop/comments/1jxrz43/

Observed high-level structure:

Public descriptions of Kehalo present a PTU living world where characters persist outside a single fixed party and can participate when their schedule permits. The world is described as changing through player activity.

Reusable lesson for Ouros:

Participation should be compatible with asynchronous availability. A persistent community system should not require the same actors at every stage of a project. Stable project IDs, role slots, handoff records and contribution history allow multiple actors to participate across different windows.

Source-quality note:

Kehalo uses homebrew PTU and is not a mechanics authority. Only the persistence/participation structure is reusable.

## Cross-source design lessons

### Help must have an owner

A community need should point to the specialist system that owns the underlying problem. Examples:

- crisis evacuation -> Crisis;
- public event cleanup -> Event Operations / Public Space / Waste;
- trail stewardship -> Conservation / Travel;
- clinic support -> Care / Staffing;
- library inventory day -> Libraries / Archives;
- neighborhood repair request -> Maintenance / Civic Public Works;
- camp setup -> Travel / institutional field operations.

The aid layer coordinates people. It does not take ownership of the underlying state.

### Willingness, availability and eligibility are separate

A person can want to help but be unavailable. A person can be available but not eligible for a specialist task. A credentialed actor can be eligible but decline. These states should never be collapsed into one volunteer flag.

### Help can end without moral judgment

A helper may withdraw because of time, changed conditions, fatigue, another commitment or a personal boundary. The world records the withdrawal and resulting coverage problem. It must not infer selfishness, betrayal, resentment or damaged relationships unless authored evidence supports that interpretation.

### Community capacity can be aggregate

A cleanup with 40 helpers does not require 40 persistent Minecraft NPCs. The world can retain a cohort/count and instantiate only actors who matter to current decisions, relationships or handoffs.

### Repeated participation creates history, not a hidden virtue score

Ouros can remember that an actor repeatedly helped at a shelter, cleanup, archive day or trail survey. Future NPCs may know those events if information plausibly spread. The system should not convert them into a universal morality, friendship or reputation statistic.

### Pokémon participation requires individual evidence

A Pokémon may assist only when the individual actor's relationship, behavior, capabilities and governing PTU/Caelo rules support the action. Species/type alone cannot prove carrying, sensing, construction, medical, rescue or logistics competence. Participation never implies ownership.

## Original design opportunity

A useful Pass 75 object family is:

`community_aid_need -> aid_call -> helper_offer -> suitability/role review -> aid_commitment -> check_in -> contribution_episode -> handoff -> release/withdrawal -> owner-system completion -> public/personal memory`

This sequence adds persistence without turning Ouros into a volunteer-management simulator. Routine contributions can compress; only conflicts, shortages, unusual handoffs, consequences or recurring relationships need scenes.

## Mechanical caution

Community-aid scenes should default to world-state/social/logistical resolution. If a scene puts helpers or civilians inside tactical danger, the full version may depend on:

- complete movement including interception and forced movement;
- tactical terrain/weather/hazards/zones/reactions;
- full lifecycle and stateful damage;
- objective-aware AI for WITHDRAW/PROTECT/CLEAR_ROUTE;
- Minecraft/Cobblemon/Craftics adapter/playback that can preserve civilian positions and objective state.

Current live Java evidence does not verify those families completely. Reduced implementations should remove noncombatants from the grid before battle and keep aid commitments in world state.

## Canon boundary

Nothing in this research establishes:

- a named Ouros volunteer organization;
- mandatory civic service;
- labor or compensation law;
- insurance or liability rules;
- universal emergency powers;
- tax benefits or donation rules;
- formal background checks;
- a standard volunteer credential;
- specific cultural expectations around helping;
- Pokémon labor norms;
- mechanical bonuses for volunteering;
- relationship or reputation rewards.

Those remain canon questions.