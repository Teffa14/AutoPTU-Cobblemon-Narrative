# Organization / Faction Identity & Lineage Continuity Extension

Status: PROPOSED / NON-CANON until explicitly approved.

Pass: 146

Purpose: preserve the historical identity of organizations across renames, leadership changes, branches, affiliations, coalitions, schisms, mergers, dissolution, attempted revival, and disputed succession without replacing the existing owners for faction behavior, employment, clubs, civic authority, human identity, facilities, records, or battle mechanics.

## Scope boundary

This layer owns organizational continuity facts only.

It does not own:

- faction strategy, projects, resources, influence, or autonomous action selection;
- employee roles, shifts, assignments, or workplace capacity;
- friendship, mentorship, club participation, or social-bond consequences;
- public-office mandates, incumbency, delegation, or succession authority;
- personal identity or cover identity;
- property ownership, facility operations, access control, finance, contracts, credentials, archives, or public notices;
- battle legality, combatant selection, tactical consequences, or PTU rules.

Those systems may reference an `organization_ref_id` and this layer's relationship history.

## Core principle

An organization needs a persistent internal reference that survives changes in visible presentation while allowing genuine discontinuity to be represented explicitly.

The internal reference is implementation metadata. NPCs do not know it unless a separate local identifier has been canonized.

## Core entities

### `organization_record`

Suggested fields:

```yaml
organization_ref_id: org_ref_...
continuity_status: ACTIVE | INACTIVE | DISSOLVED | TRANSITIONING | DISPUTED | UNKNOWN
organization_kind_tags: []
formed_at: optional timestamp_or_interval
ended_at: optional timestamp_or_interval
formation_event_ref: optional
ending_event_ref: optional
current_primary_name_ref: optional
provenance_refs: []
canon_status: CANON | PROPOSED | UNKNOWN
notes: []
```

`organization_kind_tags` remain descriptive. They must not imply a universal legal taxonomy. Examples could include volunteer group, club, association, company, research body, civic body, criminal group, federation, coalition, guild-like body, committee, or informal network, but only where local canon supports the label.

### `organization_name_record`

```yaml
name_ref_id: org_name_...
organization_ref_id: org_ref_...
name_text: "..."
name_kind: CURRENT | FORMER | COMMON | ABBREVIATION | TRANSLATED | HISTORICAL | OUTSIDER | DISPUTED | OTHER
language_or_script: optional
valid_from: optional
valid_to: optional
source_ref: ...
confidence: CONFIRMED | SUPPORTED | CLAIMED | DISPUTED | UNKNOWN
visibility: PUBLIC | LIMITED | PRIVATE | UNKNOWN
```

Several names may be valid simultaneously for different contexts.

### `organization_identifier_record`

Optional local identifiers can exist when canon supports them.

```yaml
identifier_ref_id: ...
organization_ref_id: ...
issuer_ref: ...
identifier_value: ...
scope: ...
valid_from: ...
valid_to: ...
status: ACTIVE | RETIRED | UNKNOWN
provenance_ref: ...
```

Uniqueness is scoped to the issuer/context unless explicitly established otherwise.

### `organization_relationship`

```yaml
relationship_ref_id: ...
from_organization_ref_id: ...
to_organization_ref_id: ...
relationship_kind: PARENT_OF | BRANCH_OF | AFFILIATED_WITH | FEDERATED_WITH | COALITION_WITH | PREDECESSOR_OF | SUCCESSOR_OF | SPUN_OFF_FROM | ABSORBED_BY | MERGED_WITH | SHARES_HISTORY_WITH | CLAIMS_SUCCESSION_FROM | OTHER
valid_from: optional
valid_to: optional
status: CONFIRMED | CLAIMED | DISPUTED | UNKNOWN
source_refs: []
notes: []
```

Relationship direction and effective intervals matter. A historical branch relation must not automatically apply to present-day world state.

### `organization_lineage_event`

```yaml
lineage_event_id: ...
event_kind: ...
effective_at: timestamp_or_interval
announced_at: optional timestamp_or_interval
actor_refs: []
organization_refs: []
predecessor_refs: []
successor_refs: []
place_refs: []
source_refs: []
status: CONFIRMED | CLAIMED | DISPUTED | UNKNOWN
summary: ...
```

Suggested event vocabulary:

- `FORMATION_RECORDED`
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

The vocabulary is intentionally event-oriented so history is append-only.

## Organization identity resolution

When new evidence arrives, resolution should consider several independent dimensions:

- explicit self-identification;
- continuity of governing structure where known;
- membership overlap;
- leadership overlap;
- assets and records transferred;
- mandate or charter continuity where such concepts actually exist;
- public naming continuity;
- branch or parent relations;
- explicit predecessor/successor statements;
- external recognition;
- temporal continuity;
- contrary claims and source reliability.

No single dimension is universally decisive.

### Resolution outcomes

Suggested output states:

- `SAME_ORGANIZATION_CONFIRMED`
- `DISTINCT_ORGANIZATIONS_CONFIRMED`
- `LINEAGE_RELATED_DISTINCT`
- `SUCCESSOR_CLAIM_SUPPORTED`
- `SUCCESSOR_CLAIM_DISPUTED`
- `RELATIONSHIP_UNCERTAIN`
- `ACCEPTED_AMBIGUITY`

`ACCEPTED_AMBIGUITY` is a valid terminal state for historical records when available evidence cannot distinguish between continuity and reuse.

## Name continuity

A rename should close or supersede a name interval without replacing the underlying organization record.

Example:

```yaml
organization_ref_id: org_ref_harbor_circle
names:
  - text: "Old Harbor Circle"
    valid_from: 1984
    valid_to: 2007
  - text: "Harbor Circle"
    valid_from: 2007
    valid_to: null
```

This says nothing about legal continuity, authority, or membership unless other evidence supports it.

## Same-name collisions

Two organizations may share the same visible name.

Resolution must use context such as place, date, people, records, assets, and relationships instead of merging records by string equality.

A journal entry that says "Harbor Association" may remain unresolved if two organizations used that name at the relevant time.

## Leadership changes

Leadership records belong to the relevant authority/staffing/social systems. This layer only receives the consequence that organizational identity persisted or changed when evidence establishes it.

A leadership change should normally append a relationship/event record rather than create a new organization.

However, if a leadership dispute produces two independently operating groups, a later `SPLIT_OCCURRED` event may create two organization records with lineage edges to the predecessor.

## Branches and chapters

A branch can be modeled as its own organization record when it has persistent identity worth tracking.

Branch state may include:

- parent relationship;
- local name;
- operating area;
- effective interval;
- degree of autonomy as descriptive metadata;
- local sites;
- branch-specific records.

A branch may later:

- close;
- become inactive;
- merge with another branch;
- transfer parent affiliation;
- become independent;
- split;
- survive after the parent dissolves.

None of these outcomes should be inferred from name changes alone.

## Internal factions

An internal tendency, caucus, camp, committee, or informal bloc does not automatically become a separate organization record.

Promote it to a persistent organization only when world evidence supports independent continuity, such as separate decision-making, records, assets, membership boundaries, public action, or an explicit split.

This prevents every disagreement from multiplying entities.

## Splits

A split event can produce multiple descendants.

```yaml
lineage_event_id: split_001
event_kind: SPLIT_OCCURRED
predecessor_refs: [org_ref_a]
successor_refs: [org_ref_b, org_ref_c]
status: CONFIRMED
```

The model must not automatically mark either B or C as "the same" organization as A.

Possible later evidence can establish:

- both as lineage-related distinct successors;
- one as operational successor while the other is a new group;
- competing successor claims;
- unresolved continuity.

The generator should narrate the disagreement through actor knowledge rather than reveal a database verdict unavailable to characters.

## Mergers and absorptions

Announcement and effect are separate events.

A proposed merger can be delayed, rejected, partially implemented, or reversed.

When effective, possible structures include:

- both predecessors end and a new organization begins;
- one absorbs another and continues;
- a federation forms while members retain identity;
- a coalition forms without identity transfer.

The exact interpretation must be recorded, not inferred from shared branding.

## Dissolution, inactivity, remnants, and revival

Suggested distinction:

- `INACTIVE`: organization still has continuity but currently performs little or no activity;
- `DISSOLVED`: continuity has formally or socially ended according to the best available evidence;
- `REMNANT_ACTIVITY`: former members coordinate, but this alone does not reactivate the predecessor;
- `REACTIVATION_CLAIMED`: a group claims to revive the predecessor;
- `REACTIVATION_CONFIRMED`: project canon/evidence accepts continuity;
- `NAME_REUSE`: a new organization adopts a historical name without proven identity continuity.

The last three should be modeled through events/relationships rather than a destructive status rewrite.

## Symbols, colors, uniforms, seals, and slogans

Presentation records may link to an organization over time.

They can support recognition but never prove identity by themselves.

A splinter may retain old colors. A successor may adopt a predecessor's seal. A historical uniform may be worn by a collector. A counterfeit or theatrical reproduction may exist. A branch may use a local emblem while remaining part of the parent.

Minecraft/Cobblemon should only display these facts after Ouros has decided them.

## Sites and facilities

Organizations may be associated with offices, halls, depots, laboratories, shops, camps, arenas, archives, or meeting places.

The relation needs an interval and role:

```yaml
site_association:
  organization_ref_id: ...
  place_ref_id: ...
  role: HEADQUARTERS | BRANCH_SITE | MEETING_SITE | STORAGE | PUBLIC_COUNTER | HISTORICAL | OTHER
  valid_from: ...
  valid_to: ...
  provenance_ref: ...
```

A shared site does not merge organizational identity. Moving headquarters does not create a new organization.

## Membership handoff

Membership state remains owned by the relevant social/credentials/infiltration system.

This layer only offers a stable organization target and lineage context.

Important cases:

- membership in predecessor does not automatically transfer to successor;
- membership in parent does not automatically imply branch membership;
- branch membership does not automatically imply central authority;
- former membership remains historical after departure;
- cover affiliation remains separate from true affiliation;
- wearing organization symbols is evidence at most, not membership truth.

## Authority handoff

Civic Office, Credentials, Contracts, Staffing, or another domain decides authority.

Organizational continuity alone does not carry every authority forward.

A successor may inherit:

- some records but no mandate;
- a facility but no license;
- staff but no contract;
- public goodwill but no formal authority;
- a name but none of the predecessor's obligations.

Each transfer is a separate world event.

## Records and archive continuity

Organization lineage should make archive provenance more precise.

Records may be:

- retained by the predecessor until dissolution;
- transferred to a successor;
- divided after a split;
- deposited in a public/private archive;
- duplicated;
- lost;
- retained by former officers;
- contested;
- left physically in a shared building.

Possessing records does not prove succession. Succession does not automatically prove custody.

## World Agency integration

World Agency should reference organization IDs in actor state.

When a lineage event changes continuity, the orchestrator can decide which projects:

- remain with the predecessor until closure;
- transfer to a successor;
- split into multiple projects;
- become disputed;
- terminate;
- persist as independent civic/world problems.

No automatic global transfer should occur.

### Example

```yaml
project_ref: project_ferry_repair
sponsor_organization_ref: org_ref_old_association
lineage_event: split_001
handoff:
  status: DISPUTED
  claimant_organization_refs:
    - org_ref_harbor_branch
    - org_ref_civic_cooperative
```

Players may encounter the dispute without the generator inventing a legal answer.

## Journal and rumor integration

Player-facing language should use what the relevant source knows.

Examples:

- archival fact: "The register identifies the East Chapter as a branch from 1998 to 2004."
- NPC claim: "We're the same association that ran the old clinic."
- rumor: "People say the new committee just stole the old name."
- unresolved journal note: "Two groups claim the predecessor's archive. The available records do not settle succession."

The global data model may know more than the player journal. Do not leak hidden certainty.

## Mystery affordances

This layer supports mysteries about:

- same-name organizations;
- reused emblems;
- disputed successor claims;
- records filed under historical names;
- branches that became independent without synchronized notices;
- merger announcements that never took effect;
- former members acting under obsolete symbols;
- duplicate archives after a split;
- historical sites that outlived the organization;
- organization names revived generations later.

A mystery can close in `ACCEPTED_AMBIGUITY` when the evidence genuinely cannot decide identity.

## Quest affordances

Potential quest shapes include:

- determine which organization requested a service when two names overlap;
- reconcile branch records before a shared festival;
- retrieve duplicated archives without deciding succession;
- notify counterparties of a real lineage change;
- trace former members who know which projects transferred after a split;
- document a historical organization for a museum or local archive;
- update public signs after a coalition forms while preserving member identities;
- deliver equipment to the correct successor after a warehouse handoff;
- mediate shared use of a hall by two descendants of the same predecessor.

None requires battle.

## Battle contract

Organizational semantics remain outside BattleSpec.

A battle can only return narrow physical outcomes that Ouros can consume.

### Encounter A — Branch Archive Withdrawal Corridor

Full premise: a contested archive handoff occurs while hostile actors attempt to block a withdrawal route. The narrative objective is to preserve people and records, not determine the legitimate successor.

Full capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL if timed withdrawal/reinforcement phases matter
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL if conditions affect escort timing
- terrain/weather/hazards/zones/reactions — BLOCKING for reactive doorway control or dynamic zones
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL if battle items matter; archive records remain world objects outside item semantics
- Trainer Features/perks — PARTIAL for interrupts/reactions
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced version: READY using verified/basic capability families. Remove archivists, records, custody objects, and neutral participants before BattleSpec. Freeze the archive as inaccessible scenery. Run a static combat over the corridor. On success return only `IMMEDIATE_ARCHIVE_WITHDRAWAL_ROUTE_CLEAR`. Ouros then resolves the record handoff separately.

### Encounter B — Assembly Hall Split Perimeter

Full premise: two organizational descendants hold separate meetings while a hostile third party threatens the shared perimeter. Neither descendant's legitimacy is a battle objective.

Full capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for timed arrival/departure phases
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if exits or crowd edges become reactive zones
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced version: evacuate meeting participants before combat. Use a static exterior perimeter and explicit combatants. Victory returns `IMMEDIATE_ASSEMBLY_HALL_PERIMETER_CLEAR`. It changes no leadership, lineage, membership, affiliation, or meeting decision.

### Encounter C — Shared Depot Handoff Chokepoint

Full premise: a depot contains material allocated during an organizational transition. Hostile actors threaten the approach while staff prepare a documented handoff.

Full capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL if handoff timing exists inside initiative
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic access zones/reactions
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL; controlled depot assets stay outside generic battle-item semantics
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced version: move staff and controlled assets outside BattleSpec, freeze shutters/vehicles/equipment as static scenery, and fight only over the approach. Victory returns `IMMEDIATE_DEPOT_HANDOFF_APPROACH_CLEAR`. Ouros then decides custody and organizational handoff from the world-state records.

## Capability rule

A representative implemented Intercept path does not make complete movement or reactions verified. An encounter that needs knockback, reaction ordering, dynamic terrain, weather phases, delayed effects, complex status interactions, ability-triggered terrain, or Trainer Feature interrupts must remain dependent on those exact families until tests/contracts prove them.

## Adapter rule

Minecraft/Cobblemon/Craftics may present:

- current and old signs;
- branch banners;
- retired emblems;
- shared meeting halls;
- former headquarters;
- archive boxes;
- public notices about renames or mergers;
- separate areas used by descendants.

Presentation cannot establish:

- organizational identity;
- membership;
- leadership;
- succession;
- authority;
- archive ownership;
- merger effectiveness;
- dissolution;
- coalition membership;
- battle outcomes.

Those facts originate in Ouros/world systems or AutoPTU where battle rules specifically apply.

## Generator guardrails

Never infer organizational identity solely from:

- exact name match;
- abbreviation;
- crest or uniform;
- shared color;
- shared building;
- shared leader;
- overlapping membership;
- predecessor archives;
- a claimed founding date;
- an NPC's confidence;
- a battle result.

Never silently collapse disputed successors into one record.

Never silently transfer authority, membership, contracts, assets, debts, archives, or public standing during a split/merger. The relevant owner must record each transfer.

Never convert a local historical description into universal organizational law.

## Canon posture

This extension creates no canonical Ouros organization and no universal organization registry. All concrete organizational forms, governance practices, titles, charters, symbols, affiliation rules, succession practices, and legal consequences remain local canon decisions.
