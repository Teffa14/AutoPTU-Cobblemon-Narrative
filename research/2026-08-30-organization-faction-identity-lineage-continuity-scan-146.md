# Ouros Narrative Research — Organization/Faction Identity & Lineage Continuity — Pass 146

Status: RESEARCH / NON-CANON. Provenance and reusable design evidence only. No organization, institution, faction, charter, authority model, legal regime, or named Ouros group becomes canon through this file.

Date: 2026-08-30

## Why this pass exists

The repository already contains strong faction behavior, staffing, clubs, public-office succession, identity, provenance, records, and antagonist-agency layers. The earlier faction scan explicitly supports autonomous projects, local influence, splinter groups, temporary alliances, and location-specific action history. What remains under-specified is the durable identity of the organization itself when its visible presentation changes.

This pass therefore asks narrower questions:

- When a group changes name, is it still the same organization?
- When leadership changes, what historical identity persists?
- When a chapter or branch closes, does the parent still exist?
- When a group splits, which successor, if any, may claim continuity?
- When two groups merge, when does the merger become effective rather than merely announced?
- When an old name returns years later, is this a revival, a successor, or an unrelated new group?
- How can records preserve disputed lineage without forcing the generator to choose an answer that the evidence does not support?

The intended result is a neutral continuity layer that World Agency, Civic Governance, Workplaces, Social Bonds, antagonist systems, archives, notices, credentials, procurement, finance, and future faction content can reference without surrendering their own authority.

## Repository cross-check before research

The full recursive `main` tree was inspected before selecting this topic. The tree was not truncated. Relevant existing owners were then read directly.

### Existing faction research

`research/2026-08-18-factions-fields-bonds-scan-03.md` already establishes:

- factions as autonomous world actors;
- local projects and graded influence;
- concrete action history rather than only a global reputation number;
- reform, splinter groups, temporary alliances, and uneasy coexistence as desirable consequences;
- actor-specific knowledge boundaries and partial observability.

Pass 146 does not recreate those ideas. It supplies the identity/lineage substrate underneath them.

### World Agency

`design/world-agency-layer.md` owns autonomous actors, action selection, resources, influence, projects, goals, and downstream world effects. It needs a stable organization reference when an actor is organizational, but should not become the authority for historical naming, predecessor/successor claims, or branch genealogy.

### Workplaces and staffing

`design/workplaces-professions-staffing-layer.md` owns workplaces, roles, shifts, staffing, capacity, assignments, and employment continuity. A workplace may belong to, be operated by, host, or contract with an organization. That relation does not make workplace identity and organization identity interchangeable.

### Social bonds, mentorship, and clubs

`design/social-bonds-mentorship-clubs-layer.md` owns voluntary social ties, clubs, mentorship, participation, and relationship consequences. Some clubs may also need durable organizational identity, but membership episodes and social bonds remain separate records.

### Civic office / mandate transition

`design/civic-office-mandate-transition-continuity-extension.md` owns public offices, mandates, incumbency, delegation, transition, and authority continuity. A civic organization can persist across officeholders, while an office can persist across reorganizations. Neither layer should infer the other's continuity automatically.

### Human identity and place identity

Human identity continuity and place-reference continuity already establish a useful pattern: stable internal references should be separated from mutable visible names, aliases, labels, and locations. Pass 146 applies that pattern to organizations without importing any universal registry.

## Public research

### 1. Pokémon — Team Plasma split as a clean schism pattern

Sources:

https://bulbapedia.bulbagarden.net/wiki/Villainous_team
https://en.wikipedia.org/wiki/Pok%C3%A9mon_Black_2_and_White_2

In Black 2 and White 2, the earlier Team Plasma history is followed by two distinct factions: members still aligned with N's earlier ideals and Neo Team Plasma pursuing a different program under different leadership. The useful structural lesson is that shared history, personnel, symbols, vocabulary, and a prior organizational name do not force two post-schism groups to be represented as one actor.

Ouros translation:

- a split event can produce multiple descendants;
- lineage can be shared without identity being shared;
- each successor can make different continuity claims;
- public language may continue using an old umbrella name even after operational divergence;
- a branch, remnant, reform group, and successor should be representable without requiring a universal legal ruling about which one is the 'real' organization.

Do not copy Team Plasma characters, plot, ideology, uniforms, locations, or campaign beats. Only the schism/continuity structure is reused.

### 2. Pokémon — Team Rocket remnants and attempted reconstitution

Sources:

https://en.wikibooks.org/wiki/Pok%C3%A9mon/Groups/Team_Rocket
https://bulbapedia.bulbagarden.net/wiki/Villainous_team

The game continuity provides a useful second pattern. Team Rocket is disbanded under Giovanni, yet later remnants continue activity and attempt to restore the organization and its absent leader. The structural lesson is that dissolution, remnant activity, reconstitution attempts, and leadership return are separate events.

Ouros translation:

- `DISSOLVED` need not mean every former member disappears;
- former members can act together without automatically reactivating the old organization;
- a reconstitution attempt can fail;
- an absent founder or leader does not by itself determine whether an organization exists;
- later groups may claim continuity with a predecessor while records preserve the claim as disputed or unverified.

No Team Rocket story material is imported into Ouros.

### 3. Public PTU campaign practice — organizational identity can matter outside combat

Source:

https://www.reddit.com/r/PokemonTabletop/comments/z24ni1

A public PTU campaign recruitment post describes a campaign built around going undercover within a criminal organization, with heists and Pokémon battles as linked but distinct play. It is community material, not PTU rules authority. The reusable design lesson is that membership, cover affiliation, internal access, trust, and organizational role can drive sessions even when no battle is occurring.

Ouros translation:

- organization membership must remain a world-state fact outside BattleSpec;
- wearing symbols, knowing procedures, or being present at a site cannot prove membership by themselves;
- infiltration cover identity and true affiliation can coexist;
- internal factions can produce different NPC reactions without creating a new organization unless a real split event occurs.

### 4. ICA ISAAR(CPF) — corporate-body identity is richer than one visible name

Sources:

https://www.ica.org/app/uploads/2023/12/CBPS_Guidelines_ISAAR_Second-edition_EN.pdf
https://www.ica.org/ica-network/expert-groups/egad/records-in-contexts-foundations-of-archival-description/
https://www.ica.org/es/red-ica/grupos-de-expertos/egad/records-in-contexts-modelo-conceptual/

The International Council on Archives authority-record guidance distinguishes authorized, parallel, standardized, and other forms of name for corporate bodies. It also represents dates of existence, history, places, functions, mandates/sources of authority, internal structures/genealogy, related corporate bodies, relationship categories, descriptions, dates, and sources.

This is highly reusable provenance architecture because it demonstrates that organizational identity and organizational naming should be separate dimensions.

Ouros translation:

- retain a stable internal `organization_ref_id`;
- store multiple name records with time intervals and provenance;
- represent relationships to parent, child, predecessor, successor, federation, coalition, or peer organizations explicitly;
- preserve relationship dates and confidence instead of flattening lineage into one current label;
- keep source records so later discoveries can revise claims without rewriting history.

Do not import archival standards as in-world law or bureaucracy. Ouros may have no formal registry at all in a given region.

### 5. ICA Records in Contexts — predecessor/successor and hierarchy are contextual relations

Sources:

https://www.ica.org/es/red-ica/grupos-de-expertos/egad/records-in-contexts-modelo-conceptual/
https://www.ica.org/app/uploads/2023/12/session-7.8-ica-egad-ric-congress2016.pdf

Records in Contexts treats agents and their contextual relationships as first-class descriptive material. Published ICA material explicitly discusses temporal predecessor/successor and hierarchical superior/subordinate relations.

Ouros translation:

A lineage relation should be an event-supported edge between persistent organizations rather than an inference from names. Parent/branch hierarchy also needs effective intervals because a chapter can become independent, transfer affiliation, merge, close, or exist under uncertain parentage.

### 6. GLEIF — lifecycle events should carry dates and successor information

Source:

https://www.gleif.org/en/newsroom/blog/transforming-data-into-opportunities-metric-of-the-month-legal-entity-events

GLEIF's public material on legal-entity events emphasizes recording events such as previous name changes, plausible event dates, and successor information for relevant retired records. Ouros does not inherit LEIs, corporate law, reporting obligations, or any real-world entity-event taxonomy. The useful lesson is narrower: event-sourced identity history is easier to reason about than repeatedly overwriting a current organization record.

Ouros translation:

- name change is an event;
- merger announcement and effective merger are separate timestamps;
- predecessor/successor references should be explicit;
- retirement/dissolution should preserve the old organization record;
- a new record that reuses the old name should not silently inherit the old identity.

## Derived architecture lessons

### Durable identity

Use an internal, non-diegetic `organization_ref_id` to connect records over time. It must never be exposed as a universal in-world registration number unless a local canon system explicitly provides one.

### Names are presentation/history records

Each organization may have multiple name records:

- formal or locally recognized name;
- common name;
- abbreviation;
- former name;
- translated name;
- branch-specific form;
- hostile nickname or outsider label;
- historical spelling;
- disputed claimed name.

Each record should include validity interval, source, language/script when relevant, and confidence/status.

### Organizational state

Suggested neutral states are `ACTIVE`, `INACTIVE`, `DISSOLVED`, `TRANSITIONING`, `DISPUTED`, and `UNKNOWN`. Regions may use different public terminology. These states describe continuity records and do not grant authority.

### Lineage event families

Potential event types:

- `NAME_ADOPTED`
- `NAME_RETIRED`
- `BRANCH_ESTABLISHED`
- `BRANCH_CLOSED`
- `BRANCH_INDEPENDENT`
- `AFFILIATION_STARTED`
- `AFFILIATION_ENDED`
- `COALITION_FORMED`
- `COALITION_ENDED`
- `SPLIT_OCCURRED`
- `MERGER_PROPOSED`
- `MERGER_EFFECTIVE`
- `ABSORPTION_EFFECTIVE`
- `SPINOFF_EFFECTIVE`
- `DISSOLUTION_RECORDED`
- `REACTIVATION_CLAIMED`
- `SUCCESSOR_CLAIMED`
- `SUCCESSOR_CONFIRMED`
- `SUCCESSOR_DISPUTED`
- `SYMBOL_ADOPTED`
- `SYMBOL_RETIRED`
- `SITE_ASSOCIATION_STARTED`
- `SITE_ASSOCIATION_ENDED`

These are data vocabulary proposals only.

## Important invariants

The new layer should preserve these distinctions:

- `SAME_NAME != SAME_ORGANIZATION`
- `DIFFERENT_NAME != DIFFERENT_ORGANIZATION`
- `NAME_CHANGED != ORGANIZATION_REPLACED`
- `LEADER_CHANGED != ORGANIZATION_DISSOLVED`
- `MEMBER_LEFT != ORGANIZATION_SPLIT`
- `BRANCH_CREATED != NEW_PARENT_ORGANIZATION`
- `BRANCH_CLOSED != PARENT_DISSOLVED`
- `SHARED_SYMBOL != SAME_ORGANIZATION`
- `SHARED_SITE != SAME_ORGANIZATION`
- `SHARED_MEMBERS != SAME_ORGANIZATION`
- `AFFILIATED_WITH != CONTROLLED_BY`
- `COALITION_MEMBER != SUBORDINATE_BRANCH`
- `FORMER_MEMBER != CURRENT_AGENT`
- `SPLIT_OCCURRED != ONE_SUCCESSOR_AUTOMATICALLY_IS_THE_OLD_ORGANIZATION`
- `MERGER_ANNOUNCED != MERGER_EFFECTIVE`
- `DISSOLVED != FORGOTTEN`
- `REVIVED_NAME != SAME_ORGANIZATION`
- `INTERNAL_FACTION != SEPARATE_ORGANIZATION` unless a real split/independence event is established
- `SUCCESSOR_CLAIMED != SUCCESSOR_CONFIRMED`
- `ORGANIZATION_RECORD_LINKED != ALL_FIELDS_CORRECT`
- `PUBLIC_SPOKESPERSON != UNIVERSAL_AUTHORITY`

## PTU / Caelo cross-check

The project source material remains the governing authority for mechanics. Existing internal research records PTU support for character-focused and sandbox campaign play, Jobs/activities, meaningful choices, and concrete mechanics when the relevant rule actually defines them. Nothing inspected establishes a universal organizational-lineage subsystem.

Remain UNKNOWN unless a governing project source is later located and cited:

- universal organization registry;
- universal legal-personhood rules;
- mandatory charters, constitutions, bylaws, seals, or registration numbers;
- generic membership or resignation procedure;
- universal leadership succession rules;
- generic branch/split/merger/dissolution mechanics;
- faction reputation thresholds that apply to all organizations;
- generic infiltration/disguise DCs for organizational legitimacy;
- Command, Guile, Intuition, General Education, or Technology Education as automatic authority to decide organizational identity;
- Trainer Class or Feature as automatic office or organizational rank;
- species, Type, Move, Ability, held item, badge, uniform, crest, or location as automatic proof of membership;
- battle victory as a mechanism that determines lawful leadership, lineage, membership, branch ownership, merger effectiveness, or institutional authority.

## Battle implementation implications

Organizational identity should normally remain outside battle. A battle may change an immediate physical fact, such as whether an entrance, corridor, meeting room, archive approach, or withdrawal path is physically clear. It must not decide who the organization is.

Mechanically rich encounters involving escorting records, fighting around moving crowds, reactions at doors, forced movement, dynamic control zones, carried evidence, or Trainer Feature interrupts must declare those capability dependencies explicitly. Reduced versions should remove noncombatants and semantically controlled records before BattleSpec and preserve the same narrative premise through a static combat space.

## Copyright / provenance guardrail

No protected dialogue, prose, maps, character arcs, uniforms, distinctive scene sequencing, or complete plots from Pokémon, PTU campaigns, or external games are imported. Named external groups remain only in research provenance. Ouros proposals use original situations and generic organization roles.

## Research conclusion

The repository already knows how factions act. Pass 146 adds the missing research basis for remembering which organization those actions belong to across renames, branches, schisms, coalitions, mergers, dissolution, claimed revival, and disputed succession. This gives later quests and NPCs a stable history without requiring a universal registry or forcing disputed lineage into false certainty.
