# Adjudication, Hearing, Decision & Review Continuity Scan — Pass 147

Status: RESEARCH ONLY. Provenance and design evidence. Nothing in this file is automatically Ouros canon.

Date: 2026-08-30

## Research question

Ouros already has persistent cases, allegations, evidence, authority, mediation, civic institutions, credentials, public notices, battle institutions and organization lineage. The remaining gap is the lifecycle of a formal or semi-formal decision after a matter is submitted to an institution: intake, scheduling, notice, hearing or record review, decision, effective state, reconsideration, review, remand, supersession, implementation and closure.

This pass does not establish courts, criminal law, civil law, administrative law, universal due process, deadlines, appeal rights or evidentiary standards for Ouros. It provides a continuity grammar that a canon-approved institution may use if that institution is later established.

## Internal repository fit

The full repository tree was inventoried before writing. Relevant existing owners were checked directly.

`design/case-authority-custody-layer.md` owns case identity, allegation/evidence separation, authority scope, custody and investigation provenance.

`design/agreements-mediation-repair-layer.md` owns consensual agreements, mediation and negotiated repair.

`design/civic-governance-public-works-layer.md` and `design/civic-office-mandate-transition-continuity-extension.md` own civic institutions, mandates and office continuity.

`design/battle-institutions-challenge-circuits-layer.md` owns formal challenge structures and authoritative battle-result ingestion.

`design/credentials-authorizations-recognition-extension.md` owns credentials and authorizations.

Pass 147 therefore needs a narrow owner: the history of a decision process. It must reference the case, institution, parties, record and resulting implementation state rather than duplicating their underlying systems.

## PTU / Caelo cross-check

The project's original source scan records that PTU supports central plots, character arcs and sandbox activity, while Caelo provides activity containers such as Social, Job, Raid, Contest, Gym and Dojo. It also records the permanent guardrail that allegations, hypotheses, evidence, public belief and canonical truth stay separate, and that legal powers or criminal status must not be invented without governing setting material.

No supplied source evidence reviewed for this pass establishes a universal PTU/Caelo court system, generic appeal mechanics, generic hearing DCs, legal rights, sentencing tables, tribunal hierarchy, evidence admissibility rules or a Trainer Skill that automatically resolves institutional disputes.

These remain UNKNOWN unless a future source-specific rule proves them.

## Pokémon structural sources

### Battle judges

Source: https://bulbapedia.bulbagarden.net/wiki/Referee

Bulbapedia's battle-judge summary describes official judges who state match parameters, begin sanctioned matches, enforce rules, determine whether a Pokémon may continue and make official calls that determine the match outcome.

Reusable lesson: an institution can separate the underlying contest from the recognized result. The judge's role, scope and event record matter independently of the combatants.

Ouros transformation: a canon-approved decision body should have explicit scope, decision event, subject matter and source record. The existence of an official decision does not mean the decision engine knows every underlying fact.

### League Conferences

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Lumiose_Conference
- https://bulbapedia.bulbagarden.net/wiki/Manalo_Conference

The conference structures separate eligibility/participation, match assignment, officiation, individual match results and progression to later rounds.

Reusable lesson: decision state can be consequential without replacing the event that produced it. A battle result can advance a bracket while remaining one bounded institutional fact.

Ouros transformation: if a local body recognizes a result, that recognition may unlock a later stage, credential or access path, but the narrative layer must consume authoritative world or AutoPTU facts rather than fabricate the result.

### Contest judges

Source: https://bulbapedia.bulbagarden.net/wiki/Contest_Judge

Contest judges oversee proceedings, enforce event rules, assign scores and determine winners. Different contest formats use different judge arrangements.

Reusable lesson: adjudication structure is institution-specific. One format may use one judge; another may use a panel. There is no need for Ouros to force one universal hearing model.

## PTU community sources

### Organized judged event

Source: https://www.tapatalk.com/groups/pokemon_tabletop/july-tcc-complete-t6119.html

A public Pokémon Tabletop community event specifies entry restrictions, time limits, scoring, weather, map setup and a final judged submission. The useful pattern is the explicit separation between participation rules, activity during the event and the later scoring/recognition step.

Ouros use: institution-authored procedure should be represented as world state rather than improvised after the event. A later review can then inspect what rule set was actually in force at that time.

### Premade modules

Source: https://www.tapatalk.com/groups/pokemon_tabletop/ptu-fanaticrat-39-s-premade-module-repository-t3195.html

The public module repository shows that formal trials, rites and challenge structures can provide a narrative frame around exploration and battles rather than reducing the entire procedure to combat.

Ouros use: an adjudication arc can contain investigation, social access, document retrieval, travel and combat while the institutional decision remains a separate event.

## Public process/provenance sources

### Reconsideration before later appeal

Source: https://www.gov.uk/mandatory-reconsideration

The public guidance distinguishes an original decision, a request to reconsider it and the later outcome of that reconsideration. Some decisions use different routes.

Reusable lesson: review stages should be explicit events with their own status and provenance. A request for review does not itself modify the original decision.

### Appeal lifecycle and permission

Source: https://www.gov.uk/administrative-appeals-tribunal/how-to-appeal

The guidance distinguishes permission to appeal, refusal of permission, later application to another body and the appeal itself.

Reusable lesson: `REVIEW_REQUESTED`, `REVIEW_ACCEPTED` and `REVIEW_DECIDED` are separate states. Ouros should not collapse them into a single `APPEALED` boolean.

### Decision on documents or after hearing

Source: https://www.gov.uk/administrative-appeals-tribunal/how-your-case-will-be-decided

The public process can decide from supplied records or may hold a hearing, with notification and preparation steps before the hearing.

Reusable lesson: `HEARING_HELD` is not a universal prerequisite for `DECISION_ISSUED`. The governing procedure decides whether the matter is record-only, oral, hybrid or something else.

### Previous decisions and institutional memory

Source: https://www.gov.uk/administrative-appeals-tribunal/legislation-and-previous-decisions

The service exposes previous decisions separately from current cases.

Reusable lesson: a decision archive is historical state. Earlier decisions may influence public expectation, research and institutional memory without becoming automatic universal law in Ouros.

## Structural abstractions worth preserving

A decision process benefits from event-sourced state rather than one mutable status field.

Useful distinctions:

- `MATTER_REFERRED != MATTER_ACCEPTED_FOR_DECISION`
- `ACCEPTED_FOR_DECISION != HEARING_SCHEDULED`
- `NOTICE_SENT != NOTICE_RECEIVED`
- `HEARING_SCHEDULED != HEARING_HELD`
- `HEARING_HELD != DECISION_ISSUED`
- `RECORD_CLOSED != ALL_FACTS_KNOWN`
- `DECISION_ISSUED != DECISION_EFFECTIVE`
- `DECISION_EFFECTIVE != DECISION_IMPLEMENTED`
- `REVIEW_REQUESTED != REVIEW_ACCEPTED`
- `REVIEW_ACCEPTED != ORIGINAL_DECISION_STAYED`
- `STAYED != REVERSED`
- `REMANDED != FINAL_OUTCOME_KNOWN`
- `DECISION_AMENDED != NEW_UNRELATED_MATTER`
- `SUPERSEDING_DECISION != ORIGINAL_RECORD_DELETED`
- `IMPLEMENTATION_COMPLETE != PUBLIC_AGREEMENT`
- `MATTER_CLOSED != CONSEQUENCES_COMPLETE`

## Narrative opportunities

The strongest stories come from divergent timelines. A permit-like authorization can remain effective while a review is pending. A local competition decision can be final for the event but still produce a later conduct review. An institution can issue a decision before a physical remedy is implemented. A review can return a matter for more fact-finding without answering the underlying dispute. A closed historical file can preserve disagreement forever.

This architecture also allows non-adversarial uses: scholarship selection review, conservation-access eligibility, market-stall allocation, guild certification disputes, route-service decisions, archive-access requests, tournament protests, club membership decisions or public-resource allocation. None of these examples become canon merely because they are useful templates.

## Copyright and transformation guardrail

No protected dialogue, character, distinctive plot or complete source procedure is imported. Pokémon material contributes high-level institutional patterns. Government material contributes provenance structure only. Real deadlines, legal tests, jurisdictions, rights, remedies and court hierarchies are excluded.

## Research conclusion

Ouros benefits from a generic decision-continuity layer only if it stays subordinate to canon-approved institutions. The layer should remember what was submitted, what process occurred, what decision was issued, whether it became effective, what later review did to it and whether the physical or administrative consequence was implemented. It should never decide canonical truth merely because an institution made a ruling.