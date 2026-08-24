# Institutional Succession, Vacancies & Handoffs — Research Scan — Pass 153

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. External examples are inspiration, not rules authority.
Date: 2026-08-24

## Why this pass exists

The repository already models civic bodies, workplaces, credentials, retirement, institutional review, battle institutions, archives and public memory. The remaining gap is narrower: what happens to a persistent institution when a specific officeholder leaves, cannot act, is replaced, returns, or transfers responsibility to someone else.

This pass studies succession as institutional continuity rather than as a political system. It does not define elections, hereditary offices, regional law, appointment powers, term limits, voting rules or a League hierarchy for Ouros.

## Existing Ouros boundaries reviewed before research

The full `design/`, `research/` and `proposals/` inventories were reviewed before selecting this subject.

Relevant existing authorities:

- `design/civic-governance-public-works-layer.md` owns authored mandates and local decision procedures, and explicitly refuses to invent voting/election rules.
- `design/workplaces-professions-staffing-layer.md` owns ordinary roles, assignments, shifts, staffing and task handoffs. It already states that a role may exist while vacant.
- `design/aging-senescence-retirement-role-transition-layer.md` owns retirement and explicitly leaves institutional succession to another system.
- `design/credentials-permissions-eligibility-layer.md` owns access and eligibility, not appointment.
- `design/institutional-review-adjudication-sanctions-layer.md` owns scoped review, findings and remedies, not routine succession.
- `design/battle-institutions-challenge-circuits-layer.md` owns formal challenge institutions and current leadership, not the transition transaction between leaders.
- Archives/Public Memory/Identity preserve historical records, public narrative and names after a transition.

That makes institutional succession a missing connective layer rather than a duplicate.

## Pokémon precedent: an office can outlive its holder

Official Pokémon Sword/Shield material describes Kabu as the current Gym Leader of a prestigious Gym that has existed since the early Galar League, while also noting that he once lost the Gym Leader seat and later reclaimed it. This separates person, office and tenure. A former officeholder can return without the institution becoming a new entity.

Source: Pokémon Sword and Pokémon Shield official site, Kabu.
https://swordshield.pokemon.com/en-us/people-galar-region/fire-gym-leader-kabu/

Reusable structure:

`persistent institution -> officeholder term -> interruption/loss of seat -> later term -> same institution`

Ouros lesson: do not store `gym_leader` only as a permanent property of an NPC. Store an office and versioned terms.

## Pokémon precedent: succession can include scouting, training and continued advice

Ballonlea provides a stronger transition example. Community-maintained references to Sword/Shield record Opal selecting Bede as her successor, bringing him into the Gym, training him for the role, and later passing the Gym Leader title to him. Opal can still appear around the institution afterward. The useful structure is that selection, preparation, assumption of office and former-holder involvement are separate moments.

Sources:

- Bulbapedia, Opal: https://bulbapedia.bulbagarden.net/wiki/Opal_%28Gym_Leader%29
- Bulbapedia, Ballonlea Stadium: https://bulbapedia.bulbagarden.net/wiki/Ballonlea_Stadium
- Official Sword/Shield Gym Leaders page: https://swordshield.pokemon.com/en-us/people-galar-region/gym-leaders/

Reusable structure:

`incumbent plans transition -> potential successor observed -> preparation/shadowing -> title/authority transfer -> former holder remains historically and socially present`

Guardrail: a mentor naming someone as promising does not prove that the mentor has appointment authority. Ouros must consult the institution's authored succession procedure.

## PTU community precedent: player-founded institutions can survive their founders

A public r/PokemonTabletop discussion about establishing Gyms proposes that PCs could create local trial/Gym institutions and later hire NPCs to take their place, including using the transition as a way to retire a PC into a long-term leadership role.

Source: r/PokemonTabletop, “Establishing Gyms”, 2024.
https://www.reddit.com/r/PokemonTabletop/comments/1b01w4t

Reusable structure:

`player-founded institution -> founder term -> replacement/continuity plan -> persistent institution after PC role changes`

Ouros lesson: a successful player project should not require the founder to remain permanently active. Succession can be evidence that the world has become self-sustaining.

## PTU community precedent: institutions may use different selection procedures

A public PTU Hoenn rework explicitly gives different Gyms different leader-selection processes; one example uses nomination by a school chairman and approval by a board. This is homebrew, not canon or PTU rules, but it demonstrates a useful campaign architecture: local institutions can have different succession rules rather than one universal League algorithm.

Source: r/PokemonTabletop, “Hoen Revamp (PTU)”, 2023.
https://www.reddit.com/r/PokemonTabletop/comments/11ehoto

Reusable structure:

`same office family -> different local selection procedure -> different political/social hooks`

Ouros lesson: store `succession_procedure_ref` on the office. Do not hardcode election, inheritance, nomination, duel, examination or appointment as a regional default.

## Continuity research: vacancy, acting authority and permanent succession are different

FEMA continuity-planning material distinguishes a vacancy/absence from a delegation of authority and from the later arrival of a permanent successor. Its template frames acting authority as temporary and bounded until the condition ends or a successor assumes the role.

Source: FEMA Continuity Plan Template.
https://www.fema.gov/sites/default/files/2020-07/COOP-Planning-Template_091813.pdf

Ouros adaptation:

- `VACANT`: nobody currently holds the office.
- `ACTING`: someone temporarily exercises an authored subset of authority.
- `SELECTED`: an authored procedure has produced a prospective permanent holder.
- `ASSUMED`: the new holder's term has actually begun.

Do not import US law, emergency authorities or agency structures. Only reuse the state separation.

## Continuity research: authority and knowledge transfer are separate

FEMA continuity guidance emphasizes predefined order, limits of authority, notification and training. GAO material identifies institutional knowledge, expertise and leadership continuity as risks when transitions are unplanned.

Sources:

- FEMA Continuity Plan Template: https://www.fema.gov/sites/default/files/2020-07/COOP-Planning-Template_091813.pdf
- GAO-26-108218: https://www.gao.gov/assets/gao-26-108218.pdf
- GAO succession-planning discussion: https://www.gao.gov/pdf/product/670598

Ouros adaptation: a transition should preserve separate records for formal authority, physical keys/tokens/equipment, digital access, active cases/projects, unresolved risks, restricted archives, public contacts, scheduled commitments and knowledge that was never written down. A signed appointment does not teleport any of those into the successor's mind.

## Narrative structures extracted

### The office survives the character arc

A Leader, curator, ranger chief, station director or transport supervisor can retire, resign, disappear, lose eligibility, be suspended, die, return, or simply move to another role while the institution persists.

### Acting authority creates tension without requiring conspiracy

An acting holder may keep a clinic, Gym, ferry office or research station operational while lacking authority for major appointments, irreversible projects or policy changes. The story hook comes from scope, not corruption.

### The best successor may still require a process

A community can broadly agree that one actor is qualified while the institution still needs nomination, review, training, a formal challenge, credential verification or a scheduled handoff.

### A failed handoff can create uncertainty rather than incompetence

Missing notebooks, obsolete credentials, an untransferred key, undocumented local knowledge or conflicting calendars can create play after an otherwise legitimate transition. Do not infer sabotage without evidence.

### Former officeholders remain world actors

Retirement should not delete the NPC. They may become advisor, critic, private citizen, occasional substitute, archivist, mentor, rival institution member or simply someone who no longer wants involvement.

### Institutional memory can improve

After one difficult transition, an institution may create better handoff procedures, deputy coverage, archives or training. Later vacancies can become routine instead of spawning the same quest again.

## Original Ouros design implications

Recommended state chain:

`office exists -> current term -> departure/absence trigger -> vacancy assessment -> temporary continuity if authorized -> selection procedure -> successor selected -> authority/access handoff -> assumption of office -> public/institutional reconciliation -> historical term preserved`

Each edge must be explicit. A public announcement may lag behind the actual assumption date. A Minecraft nameplate may lag behind both. Historical records preserve what was displayed at the time.

## Pokémon and battle-mechanics boundary

Nothing in this research creates a PTU Trainer Feature, command bonus, leadership aura, morale effect, initiative change or battle authority.

A Gym successor who participates in battle needs the same verified PTU/Caelo and AutoPTU mechanics as any other battle actor. Their office does not grant Skills, Features, extra actions, stronger AI or special Orders.

A succession ceremony does not create buffs. A formal duel does not decide office unless the authored institutional procedure explicitly says that its authoritative battle result is one input to the transition.

## Caelo/PTU validation status

The project README requires PTU/Caelo mechanics to remain authoritative and prohibits narrative generation from inventing rules. No reliable primary Caelo source defining institutional appointment, succession, officeholding, acting authority or Gym succession was recovered in this run.

The PTU community examples above are campaign-design inspiration only.

Super PTU Online Helper was not exposed as an invocable capability. No output is invented or attributed to it.

## Open research questions

- Which Ouros institutions actually have offices whose holder must be continuous?
- Which roles permit acting authority, and which must remain vacant?
- Which institutions use nomination, examination, appointment, election, challenge, apprenticeship or another authored procedure?
- Which transitions require credential or institutional review?
- How much of a handoff is public versus restricted?
- Can player-founded institutions define their own procedure, and what governance constraints apply?
- Which battle institutions require the officeholder personally to perform formal challenges?
- What happens to scheduled challenges, permits, payments and contracts during a vacancy?
