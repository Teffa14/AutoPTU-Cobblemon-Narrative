# Research Scan — Pass 139: Working Pokémon, Institutional Roles & Task Partnerships

Status: research/provenance only. Nothing in this file is Ouros canon.
Date: 2026-08-23

## Why this scan

The repository already models workplaces, staffing, occupations, Pokémon agency, custody, care, credentials, retirement, emergency services, transport and many domain-specific institutions. What remains under-specified is the durable state of a Pokémon that performs work inside one of those institutions.

The missing question is not “can Pokémon work?” Pokémon canon clearly says they can. The missing question is how Ouros records the difference between:

- a Pokémon physically present at a workplace;
- a Pokémon that voluntarily helps once;
- a Pokémon temporarily assigned to one task;
- a recurring worker with a stable role;
- a captured partner whose Trainer accepted an assignment;
- an institutionally housed Pokémon;
- a wild Pokémon cooperating during one local incident;
- a role that has requirements the individual Pokémon may or may not satisfy;
- a Pokémon that refuses, pauses, becomes unavailable or retires;
- a species that is commonly associated with work and the actual individual currently doing the work.

This scan looks for structures that let work become persistent world state without turning Pokémon into equipment, replacing PTU rules, or inventing consent/obedience mechanics.

## Existing repo boundary

`design/workplaces-professions-staffing-layer.md` already says institutions need people and Pokémon who keep them running, but its core assignment model is actor-generic and its strongest safeguards focus on occupations versus Trainer Classes.

`design/pokemon-agency-partnership-release-layer.md` is already the authority for persistent Pokémon identity, association, custody, observed cooperation/refusal and mechanical Loyalty boundaries.

Therefore a new layer should own institutional task-role state and delegate identity/agency to Pokémon Agency, staffing to Workplaces, welfare to Care, qualifications to Credentials, equipment to Material Culture/Items, and battle consequences to AutoPTU.

## Source 1 — Poké Jobs: work is institutional, scoped and time-bounded

Source: Pokémon Sword and Pokémon Shield official site, “Poké Jobs.”
https://swordshield.pokemon.com/en-us/gameplay/pokejobs/

The official page states that corporations and universities in Galar request Pokémon help through Poké Jobs. Pokémon are sent to a particular job for a selected duration and later return. The game also associates some job requests with Pokémon types and gives rewards/experience according to the game’s own mechanics.

Reusable structure:

- work can originate as an explicit institutional request;
- the request has scope and duration;
- the Pokémon leaves ordinary availability while assigned;
- completion and return are separate events;
- job suitability can be a stated requirement rather than a universal species truth;
- a Pokémon can have a work history without becoming an employee in the human/legal sense.

Guardrail for Ouros:

The Sword/Shield reward formula, type-suitability formula, experience awards, durations and box-to-job transfer are game-specific mechanics. Ouros should not import them. A narrative work assignment must not award XP, EVs/base points, items or Skills unless PTU/Caelo and AutoPTU explicitly authorize that result.

## Source 2 — Galar: Pokémon in the workforce are ordinary regional life

Source: Pokémon Sword and Pokémon Shield official site, “The Galar region.”
https://swordshield.pokemon.com/en-us/story/the-galar-region/

The official description says companies are eager to include Pokémon as part of their workforce and frames people and Pokémon working/living together as ordinary regional culture.

Reusable structure:

Work does not need to be a special quest. A persistent world becomes more believable when some Pokémon are routinely present in workshops, stations, farms, laboratories, transport services or civic facilities without requiring a story beat every shift.

Design implication:

Routine successful work should compress into world state. Narrative attention belongs on changes: a new assignment, failed handoff, altered equipment, refusal, retirement, changed workload, disrupted route, changed qualification, unusual observation or conflict between two legitimate service needs.

## Source 3 — Machoke: species lore can support a role without defining every individual

Source: Pokémon.com Pokédex, Machoke.
https://www.pokemon.com/us/pokedex/machoke

The official Pokédex says Machoke helps people with work such as moving heavy goods.

Reusable structure:

- species lore can establish that a task is plausible;
- a moving company, depot or public-works crew can have a long history of working alongside individual Machoke;
- tools, procedures and architecture can evolve around recurring Pokémon participation.

Guardrail:

The Pokédex sentence does not define carrying capacity, fatigue immunity, lifting DCs, work speed, shift length, equipment safety, payment, consent or the competence of every Machoke. Those remain individual/world-state or rules questions.

## Source 4 — Timburr and Conkeldurr: work can become cultural and technological history

Sources:

Pokémon.com Pokédex, Timburr.
https://www.pokemon.com/us/pokedex/timburr

Pokémon.com Pokédex, Conkeldurr.
https://www.pokemon.com/br/pokedex/conkeldurr

Timburr is described as helping with construction while carrying squared logs. Conkeldurr’s Pokédex lore says humans are thought to have learned concrete-making from the species long ago.

Reusable structures:

1. A Pokémon can participate directly in a trade without that trade becoming a Trainer Class.
2. Human institutions may inherit techniques, standards, tools or architecture from long histories of human-Pokémon collaboration.
3. The historical contribution can outlast active Pokémon participation.
4. A present-day institution can preserve contested or incomplete records about who introduced a technique.

High-value Ouros pattern:

A construction guild might still use a process whose origin is attributed to a Pokémon population centuries earlier. Modern workers may disagree about the exact history. The process can be materially real while the attribution remains a historical claim.

## Source 5 — Poké Jobs as anti-pattern for agency if copied literally

Source: Pokémon.com strategy guide, “Top Tips to Begin Your Pokémon Sword or Pokémon Shield Adventure.”
https://www.pokemon.com/us/strategy/top-tips-to-begin-your-pokemon-sword-or-pokemon-shield-adventure

The guide describes selecting Pokémon from Boxes, choosing how long they work and receiving rewards afterward.

For a video-game subsystem this is coherent. For Ouros’s persistent-character design, copying the interface literally would create problems:

- the Trainer appears to choose work without any represented Pokémon-side response;
- individual workload is abstracted into one duration choice;
- type can become a shortcut for suitability;
- successful completion is largely assumed.

Ouros should keep the institutional-job structure while adding first-class records for observed acceptance/refusal, actual attendance, role scope, workload, supervision, welfare checks and interruption.

## Source 6 — PTU community: Ranger-like cooperation is often imagined as temporary assistance

Source: public r/PokemonTabletop discussion, “Ranger Class for PTU?”
https://www.reddit.com/r/PokemonTabletop/comments/izr3b3

This thread includes a community/homebrew Ranger-style concept where a wild Pokémon helps for a bounded purpose and does not become the Trainer’s Pokémon. It is not authoritative PTU rules and must not be treated as such.

Reusable high-level lesson only:

Temporary task cooperation is narratively distinct from capture and permanent partnership. This matches the repository’s existing Pokémon Agency layer and supports service incidents where local wild Pokémon assist once without entering a roster.

No mechanics, rolls, titles or durations from the thread are adopted.

## Source 7 — Choice and control as a welfare design principle

Source: Rust, Clegg & Fernandez (2024), “The voice of choice: A scoping review of choice-based animal welfare studies,” Applied Animal Behaviour Science 275.
https://www.sciencedirect.com/science/article/pii/S0168159124001187

The review treats choice/control as an important welfare concept and reports that many included studies found positive welfare effects from providing animals meaningful choices, while emphasizing that evidence remains limited and species/context dependent.

Reusable design lesson:

Do not encode a working Pokémon as permanently available just because it once accepted the role. Preserve opportunities to decline, disengage, choose between task variants or end participation when the story/world state supports observable refusal.

This is a welfare design influence, not a claim that Pokémon cognition maps directly onto real animal studies.

## Source 8 — Working-animal systems need rest, health checks and role-specific safeguards

Source: McDowall et al. (2024), “Evaluation of current practices for dogs engaged in assistance and therapy support programs within Australia,” Journal of Veterinary Behavior 73.
https://www.sciencedirect.com/science/article/pii/S1558787824000170

The study reports variation in welfare practices across organizations, including rest and regular behavioral/health checks.

Reusable architecture:

A work system should be able to record:

- active duty windows;
- rest/unavailable periods;
- health/welfare review references;
- equipment or environmental restrictions;
- temporary relief from duty;
- organizational differences in practice.

Do not import real-world standards, required intervals or Australian policy into Ouros.

## Source 9 — Retirement is a role transition, not entity deletion

Source: Ng et al. (2019), “Paving the Path Toward Retirement for Assistance Animals: Transitioning Lives,” Frontiers in Veterinary Science.
https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2019.00039/full

The review treats retirement as withdrawal from a working role while the animal continues its life and notes that retirement decisions are individualized and under-standardized.

Reusable structure:

This aligns directly with Pass 134. A working Pokémon can stop one task, move to lighter work, transfer to another role, remain a companion, continue living at the same site or retire entirely from institutional duty without losing identity.

No real-world retirement ages or thresholds should be imported.

## Derived design principles

### 1. Work assignment is not ownership

An institution may schedule, house, supervise or equip a Pokémon without owning it. Custody, registration claims, active Trainer and work authority remain separate.

### 2. Role authority is narrower than battle command authority

A station master who can request that a Pokémon perform a routine station task does not automatically have authority to issue PTU battle commands.

### 3. Species plausibility is not individual qualification

Machoke being known for moving goods makes the role plausible. The individual’s participation, capabilities, mechanical state and workplace requirements still require validation.

### 4. Acceptance is event-scoped

Observed cooperation on Monday does not imply blanket acceptance of every future task.

### 5. Refusal is normal state

A Pokémon declining a task should be representable without automatically creating disobedience, hostility, low Loyalty, injury or misconduct.

### 6. Workload must be longitudinal

Ouros should be able to remember that the same Pokémon has worked twenty storm deployments, six festival nights or three years of ferry duty even if there is no mechanical fatigue system.

### 7. Equipment is separate

Harnesses, carts, uniforms, tools, radios and safety gear belong to Material Culture/Items. A role can require equipment without the narrative layer inventing item bonuses.

### 8. Human/Pokémon teams need handoffs

When one partner is unavailable, replacement is not identity substitution. The service may continue with a different team, reduced scope or temporary closure.

### 9. A role can survive the individual

A famous Pokémon can retire while the station, rescue unit or workshop continues. The institution should preserve the role’s history without turning the successor into a clone.

### 10. A Pokémon can survive the role

A retired work Pokémon can remain a partner, resident, research subject, public figure or ordinary community member.

## Useful original Ouros directions derived from the research

- institutional task requests with explicit scope and duration;
- recurring work histories attached to persistent Pokémon IDs;
- “relief Pokémon” or alternate teams without implying interchangeable personalities;
- equipment-fit and site-access checks as world-state requirements;
- public misunderstanding when a famous work Pokémon stops appearing;
- a service disruption caused by staffing/availability rather than villainy;
- historical trades whose techniques were learned from Pokémon but are now human-run;
- workplace culture around how Pokémon can indicate “not today” through observable behavior;
- voluntary wild assistance during a crisis that ends after the local objective;
- training programs that certify the institution/team for a task without inventing PTU Skill Ranks;
- retirement ceremonies that have no mechanical reward;
- successor teams inheriting responsibility but not the retired Pokémon’s reputation, memories or mechanics.

## PTU/Caelo mechanical boundary

No accessible source in this run established a project-local authoritative rule for:

- Pokémon work shifts;
- institutional task consent;
- lifting/carrying capacity for workplace logistics;
- occupational fatigue;
- task-specific qualification;
- workplace training;
- payment/reward for Pokémon labor;
- equipment-fit bonuses;
- retirement from work;
- service-Pokémon command authority.

The public PTU/community material is insufficient to invent those rules. Super PTU Online Helper was not available as an invocable capability in this runtime. The full project Caelo corpus was not reliably accessible in this run, so no Caelo-specific mechanics are asserted here.

## Sources not promoted to rules

External Pokémon canon, real-world animal-welfare research and community PTU discussion are inspiration/evidence for narrative architecture only. AutoPTU/PTU/Caelo remain authoritative for mechanics.
