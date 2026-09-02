# Identity, Credential and Delegated Authority Research Scan — Pass 201

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-02
Canon effect: NONE. This file records sources and transformed design lessons. It does not establish Ouros law, identification documents, licensing, government, citizenship, employment doctrine or institutional powers.

## Repository gap checked before research

The repository tree, all current files in `canon/`, and adjacent continuity layers were inspected before this scan. Existing systems already cover stable NPC identity, temporary visitors, narrow temporary access, service requests, information claims, document provenance, custody, markets and relationship history. No dedicated layer currently owns the seam between:

- a person or organization claiming an identity;
- evidence used to distinguish that actor from another actor with a similar name or presentation;
- a credential or role marker;
- the scope and time window of authority attached to that credential;
- delegated authority for one task;
- expiry, revocation, replacement or later re-verification;
- a Minecraft/Cobblemon presentation actor and the authoritative Ouros actor it projects.

The visitor layer already contains `temporary_access_grant`. Pass 201 must reuse that record as one kind of scoped authority rather than create a competing visitor-access system.

The information-circulation layer already owns identity claims as claims when they travel socially. Pass 201 owns verification and authority state, not rumor propagation.

## Source 1 — Pokémon Original Trainer and Trainer ID

Source:
https://bulbapedia.bulbagarden.net/wiki/Original_trainer
https://bulbapedia.bulbagarden.net/wiki/Trainer_ID_Number

Accessed: 2026-09-02

Useful structure:
Pokémon games distinguish an Original Trainer using more than a displayed name. OT name, ID data and other stored attributes can participate in deciding whether a Pokémon came from the same Trainer. Two Trainers can share visible names without necessarily being the same originating actor.

Transformed Ouros lesson:
A display name is evidence about identity, not a globally unique person key. Persistent people, Pokémon and institutions should use stable internal IDs. Visible names, titles, nicknames and skins are presentation fields linked to those IDs.

Important exclusion:
Do not import game Trainer ID numbers as Caelo civil identification. OT/Trainer ID mechanics are useful evidence for Pokémon provenance and game identity only until PTU/Caelo material says otherwise.

## Source 2 — Galar League Cards

Source:
https://swordshield.pokemon.com/en-au/gameplay/league-card/
https://bulbapedia.bulbagarden.net/wiki/League_Card

Accessed: 2026-09-02

Useful structure:
League Cards are created and exchanged by Trainers, carry information about a Trainer, and are also deliberately customizable presentation objects.

Transformed Ouros lesson:
A portable profile or card can communicate attributed information without becoming universal proof of identity or authority. Presentation and credential verification should remain separable. A visually convincing card can be a real artifact whose scope still requires interpretation by the institution that relies on it.

Important exclusion:
No Ouros League Card, Trainer passport, universal ID card or League bureaucracy is established by this research.

## Source 3 — Pokémon Ranger missions and rank

Source:
https://bulbapedia.bulbagarden.net/wiki/Ranger_Missions

Accessed: 2026-09-02

Useful structure:
Pokémon Ranger distinguishes an official assignment from general capability. Missions can be assigned by leaders, sometimes to multiple Rangers, while higher-ranked Rangers have additional authority to assign missions under particular circumstances.

Transformed Ouros lesson:
Role, assignment and authority scope should be separate records. A person can belong to an institution but lack authority for a specific action. A task-specific delegation can be valid without transferring the delegator's whole office or every institutional permission.

Important exclusion:
Marea Field Office is canonically not the Pokémon Ranger organization and is not a police force. Ranger ranks, mission law and command structure are not imported.

## Source 4 — Mystery Dungeon job acceptance

Source:
https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Mystery_Dungeon:_Red_Rescue_Team_and_Blue_Rescue_Team/Intro
https://bulbapedia.bulbagarden.net/wiki/Job_(Mystery_Dungeon)

Accessed: 2026-09-02

Useful structure:
A published job and an accepted job are separate states. Teams can know about several jobs while only chosen jobs become active work.

Transformed Ouros lesson:
Awareness of a request, possession of a copy, and authority to act on it should remain distinct. This reinforces pass 198 service-request continuity and supplies a clean handoff into delegated authority.

Important exclusion:
Rescue ranks, mission points, rewards and Mystery Dungeon institutional rules are not imported.

## Source 5 — NIST SP 800-63-4 and SP 800-63A-4

Sources:
https://www.nist.gov/publications/nist-sp-800-63-4-digital-identity-guidelines
https://www.nist.gov/publications/nist-sp-800-63a-4digital-identity-guidelines-identity-proofing-and-enrollment

Published: 2025-08-01
Accessed: 2026-09-02

Useful structure:
NIST treats identity proofing, enrollment, authentication and assertions as separate processes. It also recognizes that a system may need different assurance depending on the harm associated with accepting a claim.

Transformed Ouros lesson:
Verification should be proportional to the consequence. An ordinary conversation may accept a self-asserted name. Collecting a reserved object, entering a bounded work area or speaking for an institution may require stronger evidence. The system should preserve what was checked rather than expose a magical `verified_person` boolean that means everything everywhere.

Important exclusion:
No NIST assurance level, digital-identity standard, biometric requirement or government procedure is canonized in Ouros. Only the separation of concerns is reused.

## PTU 1.05 cross-check — Guile, disguise and social adjudication

Public PTU 1.05 material:
https://anyflip.com/qloz/xgfq/basic
https://anyflip.com/gqibw/ifqm/basic

PTU describes Guile as relevant to deception, hiding in plain sight, posing as an innocuous person and disguises. Perception may oppose Guile when attempting to see through a disguise.

Design consequence:
Narrative must not resolve impersonation, forged presentation, deception detection or seeing through a disguise with an invented identity score. When the situation is mechanically contested, the authoritative PTU/Caelo/AutoPTU Skill path must resolve the check.

A verified world record can still answer non-contested questions such as whether an access grant exists, when it expires, who issued it and what scope it names.

## PTU/Caelo project cross-check

Current Narrative canon requires stable NPC IDs, persistent identity and revalidation of current mechanical permissions. It also states that Minecraft entities cannot author canonical identity/history changes through unload, death, duplication or pathing behavior.

A fresh literal search for `Caelo` in the currently indexed Narrative/AutoPTU material did not expose a Caelo identity, credential, licensing or delegation rule during this pass. Therefore the following remain unresolved:

- civil identity documents;
- legal names and name changes;
- citizenship/residency documents;
- Trainer licenses;
- institutional credential standards;
- signatures/seals and their legal effect;
- employment or contractor authority;
- proxy pickup rules;
- guardianship;
- age-based authority;
- revocation/appeal doctrine;
- recognition of outside-region credentials.

## Reusable design patterns

### Stable actor, mutable presentation

A persistent actor can change clothes, displayed name, title, location or Minecraft entity instance while retaining one authoritative actor ID.

### Scoped verification

Record what evidence was checked, by whom, for what purpose and when. Do not elevate one successful verification into universal identity assurance.

### Authority as a bounded grant

Store issuer, subject, institution, scope, effective window, conditions and status. Membership or employment can be separate from authority for a particular action.

### Delegation as a link

A delegator can authorize another actor to perform one task while retaining the underlying office. Delegation should never copy every permission automatically.

### Presentation artifact versus authority state

Cards, badges, notes, seals, uniforms, Minecraft items and signs can project a claim. The authoritative record decides whether the claim is current and sufficient for the requested action.

### Verification can age

A once-valid credential may expire, be revoked, be superseded or simply require fresh confirmation for a new visit or purpose. Preserve old validity history instead of rewriting it away.

### Similar names require disambiguation

Ouros canon already deliberately refuses to infer family relationships from shared surnames. The same discipline should apply to identity: same name or surname cannot merge actors.

## Candidate narrative consequences

- a repeat visitor returns after a previous access window expired;
- a person arrives to collect a repaired object on someone else's behalf;
- an old copied authorization note remains visible after its validity ends;
- two archival records refer to people with the same display name but insufficient evidence to merge them;
- Lia delegates one dock coordination action while retaining overall responsibility;
- a visiting specialist presents a genuine external credential whose local meaning remains uncertain;
- a Minecraft duplicate actor appears and must collapse onto one persistent NPC ID or be rejected as presentation corruption;
- a disguise or impersonation attempt becomes a PTU Guile/Perception problem only when mechanically contested.

## Copyright/transformation note

No protected dialogue, plots, named Ranger missions, Mystery Dungeon jobs or distinctive character arcs are imported into Ouros. Sources are used only for high-level state separation and design lessons.