# Ouros Covert Operation, Infiltration, Access & Extraction Research — Pass 151

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is canon by inclusion.

Date: 2026-08-30

## Research target

Pass 151 investigates a narrative gap left after the existing Mission & Dungeon Grammar, Antagonist Agency, Case/Authority, Organization Lineage, World Agency and Campaign Convergence layers.

The repository already knows that a mission can contain an INFILTRATE activity block, that adversarial actors can maintain plans and cells, that institutions can own records and authority, and that long arcs can converge. The missing reusable structure is the continuity of a covert operation itself: preparation, cover state, access state, objective state, exposure, extraction, evidence and fallout.

This is deliberately broader than a single stealth dungeon and narrower than criminal-law simulation.

## Internal repository cross-check

Existing owners remain authoritative:

- Mission & Dungeon Grammar owns mission assembly and activity-block composition.
- World Agency owns actor goals, knowledge, reach and autonomous action.
- Antagonist Agency owns opposing plans, attention, escalation, cells, defection and adversarial intent.
- Case/Authority/Custody owns allegations, evidence handling and institutional authority where established.
- Organization Lineage owns persistent organization identity and succession.
- Communications owns message delivery and actor knowledge propagation.
- Material Culture owns persistent item instances such as badges, keys, uniforms, tools and records.
- Travel owns physical journey state outside tactical battle.
- AutoPTU owns tactical battle facts.
- Minecraft/Cobblemon/Craftics owns representation and playback only.

Pass 151 therefore must not invent a universal stealth meter, criminal procedure, security law, disguise bonus or battle-state shortcut.

## Internal PTU / Caelo guardrails

The project's PTU/Caelo source scan already establishes that PTU supports central plots, character arcs and sandbox play, and that Caelo provides distinct containers such as Social, Job, Raid, Contest, Gym and Dojo. Those structures are sufficient to host infiltration or investigation fiction without inventing a new universal PTU subsystem.

No internal evidence reviewed in this pass establishes:

- a universal infiltration action;
- a universal disguise mechanic;
- a universal suspicion meter;
- a generic access-card rule;
- generic stealth takedowns;
- generic alarm mechanics;
- generic silent capture rules;
- generic hacking;
- generic lockpicking;
- generic escort/extraction rules;
- automatic authority to impersonate an institution;
- a universal consequence table for being discovered;
- automatic faction reputation changes from covert activity.

Any exact Skill Check, Feature, Move, Ability, item or environmental rule must be cited from the governing PTU/Caelo material and verified against current engine support.

## Public source 1 — Silph Co.

Source: https://bulbapedia.bulbagarden.net/wiki/Appendix:Red_and_Blue_walkthrough/Section_10

Reusable structure:

Silph Co. combines an occupied institution, multiple floors, internal warp routes, locked electronic doors, a reusable Card Key, optional rooms, staff, hostile personnel and a final leadership confrontation. The building's normal transportation infrastructure becomes navigation complexity during hostile occupation.

Design lesson for Ouros:

An infiltration location is more believable when its obstacles are ordinary institutional systems used under abnormal conditions. Elevators, staff-only doors, badge-controlled areas, records rooms, loading bays, maintenance corridors and communication relays can create route choice without requiring arbitrary dungeon puzzles.

Do not copy Silph Co., Team Rocket, named NPCs, exact layout, warp-panel arrangement or plot.

## Public source 2 — Team Rocket Hideout

Sources:

- https://bulbapedia.bulbagarden.net/wiki/Team_Rocket_Hideout
- https://bulbapedia.bulbagarden.net/wiki/Lift_Key

Reusable structure:

The hideout gates deeper access behind a physical access object and separates public-facing space from restricted infrastructure. Progress can involve obtaining a key, learning where it applies and choosing how much of the complex to explore before confronting leadership.

Design lesson for Ouros:

Access should be modeled as a scoped capability tied to a place or system. Possessing one credential should not silently become universal access. A key can open specific doors while leaving social legitimacy, knowledge of the site and extraction safety unresolved.

## Public source 3 — Team Galactic HQ

Sources:

- https://bulbapedia.bulbagarden.net/wiki/Galactic_Key
- https://bulbapedia.bulbagarden.net/wiki/Appendix:Platinum_walkthrough/Section_15

Reusable structure:

The player obtains access through one part of the complex, uses it to reopen or shortcut previously blocked paths, and later enters the main headquarters with a different tactical and narrative purpose. Observation of an internal speech also creates intelligence without requiring immediate confrontation.

Design lesson for Ouros:

Covert operations can have information objectives that matter even when no object is stolen and no target is defeated. Route knowledge and previously opened shortcuts should persist as world state when physically plausible.

## Public source 4 — Plasma Frigate

Source: https://bulbapedia.bulbagarden.net/wiki/Plasma_Frigate

Reusable structure:

The same hostile mobile facility appears in multiple places and contains version-dependent internal access puzzles such as password and warp-panel sections. Its mobility changes the relationship between site knowledge and future access.

Design lesson for Ouros:

A covert target does not need to be a static dungeon. A ship, convoy, train, field camp or temporary laboratory can preserve identity while its location changes. Knowledge of one configuration may later be stale.

Do not import Kyurem power systems, exact passwords, named factions or layout.

## Public source 5 — PTU campaign premise: Pokémon Undercover

Source: https://www.reddit.com/r/PokemonTabletop/comments/z24ni1

Community provenance only. Not a rules source.

The public campaign pitch describes player characters going undercover inside a criminal organization, performing heists to preserve cover and reveal leadership while trying to limit irreversible harm. It explicitly combines PTU battles with operation planning.

Reusable lesson:

The dramatic core of undercover play comes from conflicting objectives, not only stealth. The party may need to preserve cover, learn something, protect an uninvolved person, avoid irreversible consequences and still complete enough of the apparent assignment to remain credible.

Ouros should therefore support multiple operation objectives with different owners and different disclosure levels.

## Public source 6 — Blades in the Dark planning and engagement

Source: https://bladesinthedark.com/planning-engagement

Used as general scenario-design research, not imported mechanics.

The system intentionally avoids exhaustive pre-planning. Players choose a broad plan and a key detail, then the operation begins at the first meaningful obstacle. Flashbacks can establish prior preparation without forcing players to predict every contingency in advance.

Reusable lesson:

Ouros should record concrete preparations that actually occurred, but authored covert adventures should not require players to solve the whole operation before entering it. Preparation can create assets, route knowledge, contacts, planted resources or documented cover state. It should not guarantee success.

Do not import stress, engagement dice, position/effect or flashback mechanics unless separately designed and approved.

## Public source 7 — Node-based scenario design

Sources:

- https://www.thealexandrian.net/creations/misc/node-design/node-design.html
- https://www.thealexandrian.net/creations/misc/node-design/node-design2.html

Reusable lesson:

Scenario progress becomes fragile when every step requires one exact clue or route. Multiple clues and multiple connected nodes let players choose their approach and recover from missed information.

Ouros use:

A covert site should expose multiple plausible access nodes when world state supports them: public entrance, service access, staff contact, records route, scheduled delivery, maintenance route, prior credential, adjacent structure, known shortcut or later discovered alternate route.

No route should exist merely because the generator needs a fallback.

## Cross-source synthesis

The most reusable structure is a stateful operation with six separable dimensions:

1. Objective state — what the actors are trying to accomplish.
2. Cover state — what identity or explanation is currently being presented and to whom.
3. Access state — what places, systems or information channels are currently reachable.
4. Exposure state — what other actors have observed, suspected, confirmed or communicated.
5. Extraction state — what route or condition allows participants, evidence or assets to leave.
6. Fallout state — what durable consequences remain afterward.

These dimensions should never collapse into one `stealth_success` boolean.

## Reusable boundary rules

- ACCESS_GRANTED does not imply TRUSTED.
- CREDENTIAL_VALID does not imply HOLDER_AUTHORIZED.
- COVER_ACCEPTED_BY_ACTOR_A does not imply COVER_ACCEPTED_BY_ACTOR_B.
- OBSERVED does not imply IDENTIFIED.
- IDENTIFIED does not imply MOTIVE_KNOWN.
- SUSPICION does not imply CANONICAL_GUILT.
- ALARM_RAISED does not imply EVERY_ACTOR_KNOWS.
- OBJECTIVE_ACQUIRED does not imply EXTRACTED.
- EXTRACTED does not imply UNDETECTED.
- UNDETECTED does not imply NO_EVIDENCE_LEFT.
- BATTLE_WON does not imply COVER_PRESERVED.
- LEADER_DEFEATED does not imply ORGANIZATION_EXPOSED.
- OPENED_SHORTCUT does not imply SHORTCUT_REMAINS_OPEN FOREVER.
- STOLEN_IDENTITY does not imply LEGAL OR SOCIAL AUTHORITY.
- DISGUISED does not imply MECHANICALLY INVISIBLE.

## Useful operation objectives

Candidate objective types for future Ouros proposals:

- observe a meeting;
- confirm whether an actor is present;
- copy or photograph a record without removing it;
- recover a specific item instance;
- place a harmless monitoring marker where canon supports it;
- escort information to a receiver after leaving;
- verify a route;
- identify a supplier or recipient;
- protect a witness without revealing why;
- recover a companion or captive only where case/authority state supports that premise;
- sabotage an authored machine only where its owner system defines legal effects;
- create an extraction window;
- discover which branch of an organization actually controls a site;
- leave without escalating a conflict.

## Failure-forward patterns

A covert operation can remain playable after partial failure.

Examples:

- the party is recognized but the target does not know their real objective;
- an alarm closes one route but opens a public evacuation route;
- the record is seen but cannot be removed;
- a credential is burned but another contact remains usable;
- a battle exposes presence but protects an uninvolved actor;
- the target moves operations afterward, creating a new lead;
- an extraction succeeds but evidence of intrusion remains;
- the operation fails locally but reveals that the site belongs to a different organizational branch than expected.

## Long-term narrative value

Persistent covert operations can enrich later play through:

- burned identities;
- trusted aliases known only to specific actors;
- retired credentials;
- changed access policies;
- relocated operations;
- internal investigations;
- faction paranoia;
- innocent employees remembering suspicious behavior;
- an old shortcut later sealed or repurposed;
- a former adversary recognizing the player years later;
- evidence that an infiltration happened without proof of who performed it;
- competing historical accounts of the same operation.

## Safety and originality boundary

This research is for fictional game design. It intentionally stays at narrative abstraction and does not document real-world bypass procedures, credential forgery methods, surveillance evasion techniques, weapon use or actionable intrusion instructions.

External stories and games are used only for high-level structures. No protected dialogue, character, distinctive plot sequence or map is copied into Ouros.

## Recommended architecture output

Pass 151 should add a covert-operation continuity object that references existing owners instead of replacing them.

It should include:

- operation identity;
- participants and declared roles;
- objectives with visibility scope;
- cover claims and which actors know them;
- access grants and their provenance;
- observed/suspected/confirmed exposure events;
- route knowledge;
- extraction condition;
- evidence outputs;
- Chronicle/faction/case follow-up references;
- exact capability dependencies for any tactical encounter.

## Canon status

No organizations, criminal networks, covert agencies, universal laws, security technologies, disguise systems or infiltration procedures are established as Ouros canon by this research.

All concrete Ouros concepts generated from this pass remain NON-CANON until reviewed.