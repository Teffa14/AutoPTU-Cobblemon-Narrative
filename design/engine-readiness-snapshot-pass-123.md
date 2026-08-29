# Engine Readiness Snapshot — Pass 123

Status: EVIDENCE SNAPSHOT. This file records current evidence and does not promote capability families from isolated representative mechanics.
Date: 2026-08-29

## Read-only heads inspected

AutoPTU-Java current head: `91a61de675a08f8144849eb80b41f10648a81907` — `Derive intercept skills from server-owned content (#271)`.

Compared with the Pass 122 head `87fbcb2ab75b4642c762017a037a6c0dccb9d8ad`, AutoPTU-Java is two commits ahead. The current slice adds server-owned PTU Skill ranks to combatant rule content and derives the Intercept check's Acrobatics/Athletics inputs from that authoritative content. Regression coverage verifies the derived ranks, PTU zero default for absent skills, required content input and that the helper is not exposed as public adapter API.

This is a useful authority-boundary improvement for the existing Intercept path. It does not establish broad movement or reaction coverage.

AutoPTU current head: `b173542b1a28a886f50e8d581228e60c98a10cfa` — `Career: reject blank persisted Pokemon ids`.

Compared with Pass 122, AutoPTU adds Career/browser recovery hardening that removes empty or whitespace-only persisted Pokémon IDs and regression coverage. It adds no tactical battle capability.

## Permanent capability map

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

No family is promoted in Pass 123.

## Intercept evidence update

The earlier evidence already verified a concrete Intercept route inside the PRE-target registry and authoritative Move pipeline.

The new head strengthens authority over one input to that route:
- Acrobatics and Athletics ranks are read from server-owned `CombatantRuleContent`;
- missing Skills use the project's PTU zero default;
- the server-owned builder remains internal rather than becoming adapter-facing authority;
- separate modifiers remain explicit for other rule families.

This supports the principle that the Minecraft/Cobblemon adapter must not invent PTU Skill conclusions.

The evidence remains bounded. It does not verify:
- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- every Intercept timing/window;
- environmental displacement;
- generalized competing reactions;
- reaction ordering across all mechanics;
- every Move, Ability, Item or Trainer Feature registration;
- objective-aware AI;
- semantic adapter playback.

## Pass 123 core narrative readiness

The adjudication/review continuity model is world-state and provenance data. It requires no new tactical capability for:
- matters and proceeding scope;
- notices and delivery state;
- review record manifests;
- sessions;
- findings separated from world truth;
- decision versions;
- review requests;
- preserved/vacated/remanded finding lineage;
- remand work;
- implementation conditions;
- compliance events;
- public-summary corrections;
- archive callbacks.

Mysteries such as `Five Dates on One Decision`, `The Finding That Survived`, `The Record Was Complete Yesterday` and `Seven Records, Three Scopes` are READY with current narrative infrastructure.

The exploration `The Review Office Above the Old Station` is READY when all traversed geometry is static and already authorized as safe.

## Encounter readiness — Record Transfer Diversion

Targeting/footprints/range/LoS — VERIFIED.

Base movement legality — VERIFIED.

Complete movement including push/pull/knockback/interception/forced movement — PARTIAL if an escort, Intercept or forced displacement is part of the encounter.

Core calculations — VERIFIED.

Action economy/initiative — VERIFIED.

Full turn/round lifecycle — PARTIAL when departure or handoff has a timed tactical window.

Full stateful damage pipeline — PARTIAL for selected governed combat effects.

Status lifecycle — PARTIAL when selected legal effects apply status.

Terrain/weather/hazards/zones/reactions — BLOCKING if a protected corridor, moving boundary or generalized reaction is required.

Move-specific behavior — PARTIAL.

Abilities — PARTIAL.

Items — PARTIAL.

Trainer Features/perks — PARTIAL.

AI legal-action infrastructure — VERIFIED.

AI tactical policy — BLOCKING for PROTECT/WITHDRAW/CLEAR_ROUTE behavior.

Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING for authoritative semantic escort, record handoff or withdrawal playback.

Reduced form: READY. Complete record custody/transfer in Ouros world state before BattleSpec creation. Exclude the custodian and record package. Run a static conventional battle at the chokepoint. Victory can clear immediate access only.

## Encounter readiness — Hearing Hall Evacuation

Full form pressure:
- complete movement — PARTIAL for Intercept/withdrawal interactions;
- lifecycle — PARTIAL for phased departure;
- terrain/weather/hazards/zones/reactions — BLOCKING if a protected corridor is represented as a tactical zone or crossing triggers generalized reactions;
- AI tactical policy — BLOCKING for WITHDRAW/PROTECT;
- adapter/playback — BLOCKING for semantic evacuation and proceeding-state presentation during battle.

Reduced form: READY. Adjourn the proceeding first, move participants and records to safe world state, and use a static exterior arena. Battle outcome does not reschedule or resume the proceeding.

## Encounter readiness — Compliance Site Perimeter

The full form becomes PARTIAL/BLOCKING when workers or controlled objects remain tactical objectives, when Intercept/escort movement matters, or when AI must understand a protection objective.

If machinery, environmental hazards, changing access zones or reaction areas are added, `terrain/weather/hazards/zones/reactions` remains BLOCKING unless exact contracts and tests demonstrate the required behavior.

Reduced form: READY. Pause work, remove workers and controlled objects from BattleSpec, resolve a conventional static fight, then let the owner system resume work and the authored verification route decide compliance.

## PTU/Caelo boundary

The internal PTU/Caelo source scan supports campaign structures, social play, cases, exploration, standard Skills and exact authored environmental mechanics. It does not establish a universal adjudication subsystem.

Remain UNKNOWN without exact governing evidence:
- generic restraint procedure;
- detention duration or release rules;
- hearing-specific Skill DCs;
- testimony mechanics;
- automatic lie detection;
- species-derived truth or guilt detection;
- universal review or appeal procedure;
- formal procedural authority from a Trainer Feature;
- Move/Ability/Item effects that prove a contested fact;
- battle victory as institutional proof;
- capture as institutional custody.

Any social Skill use must follow its actual PTU/Caelo rule and current character state. Narrative procedure cannot manufacture a mechanical check.

## Boundary with existing narrative systems

Case & Authority continues to own investigation, evidence and custody.

Agreements & Mediation continues to own voluntary negotiated commitments.

Civic Governance continues to own future public choices and consultations.

Media/Public Notices/Public Memory continue to own publication and audience knowledge.

Archives continues to own long-term record access.

Pass 123 stores a decision/review lineage only when an authored institution and mandate already exist. It does not create those authorities.

## Minecraft/Cobblemon boundary

Minecraft/Cobblemon may render meeting spaces, notices, archives, waiting areas, courier routes, NPC attendance, public summaries and later access changes.

A visible sign is not authoritative notice state. A locked door is not a decision. NPC placement does not establish a proceeding. A chest or book does not establish record authenticity. Battle outcome does not establish a finding. Cobblemon BattleState remains outside deciding authority, evidence provenance, review state and compliance verification.

## Readiness result

Narrative/world-state adjudication continuity: READY, subject to canon providing the institution, mandate, scope, outcomes and any review route.

Provenance mysteries and archive exploration: READY.

Reduced static Record Transfer Diversion: READY.

Reduced Hearing Hall Evacuation: READY.

Reduced Compliance Site Perimeter: READY.

Full versions: PARTIAL/BLOCKING where complete movement, phased lifecycle, generalized reactions/zones, tactical objectives or semantic playback are required.

## Unresolved mechanical and canon questions

- Which Ouros institutions, if any, receive deciding authority for contested matters?
- Does any region have a review/reconsideration route, and what exact scope can it address?
- Which decision outcomes can each institution authorize?
- Which records are public or protected?
- How can an individual Pokémon participate when communication is limited?
- Are any PTU/Caelo Skills, Features, Moves, Abilities or Items relevant to specific fact-finding tasks, and what do their exact rules permit?
- How should objective-aware AI represent WITHDRAW, PROTECT and CLEAR_ROUTE when those policies are eventually implemented?
- Which semantic playback events are needed for escorts, adjournment, safe withdrawal and record handoff without allowing the adapter to become authoritative?

Until those questions have exact contracts or canon, the reduced encounter forms and provenance-first procedural state are the implementation-safe path.
