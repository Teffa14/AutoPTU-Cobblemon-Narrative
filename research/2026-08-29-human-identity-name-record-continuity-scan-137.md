# Ouros Narrative Research — Human Identity, Name & Record Continuity Scan 137

Status: RESEARCH / PROVENANCE ONLY. Not established Ouros canon.
Date: 2026-08-29

## Research question

What reusable structures can help Ouros preserve a human actor's identity across changing names, institutional records, local aliases, credentials, transfers and historical documents without inventing a universal civil registry, citizenship model, biometric infrastructure or Trainer-license regime?

This pass treats identity as a continuity and provenance problem. It does not define who is legally recognized by any Ouros institution. Any authoritative naming, registration, identity-document or privacy regime remains region- and institution-specific until canon establishes it.

## Repository gap check

The recursive narrative repository tree was inspected before topic selection.

Existing layers already own adjacent concerns:

- `design/infiltration-stealth-cover-identity-layer.md` models canonical-identity references, legitimate roles, presented cover identities and observer beliefs. It deliberately does not define the underlying canonical human-identity record.
- `design/credentials-authorizations-recognition-extension.md` models credentials, authorizations, verification and scope. A credential can reference an actor without becoming the actor's complete identity.
- `design/personal-records-oral-history-correspondence-extension.md` owns letters, diaries, interviews and private historical records. Those records can contain names without themselves becoming an identity authority.
- `design/interregional-mobility-recognition-layer.md` models home/host-region association and portable-record recognition while explicitly refusing to invent nationality, citizenship, passports or immigration law.
- `design/interregional-arrival-inspection-hold-release-continuity-extension.md` can perform a scoped identity check using persistent IDs and provenance, but it does not create the identity being checked.
- `design/family-kinship-household-continuity-extension.md` owns family/household relationships, not identity proof.
- `design/residential-housing-relocation-continuity-extension.md` owns residence and relocation, not person identity.
- `design/case-authority-custody-layer.md` owns investigative authority and evidence custody when a case exists.
- `design/pokemon-agency-partnership-release-layer.md` owns persistent Pokémon identity and keeps Pokémon registration, custody, ownership claims and active Trainer separate.

The missing seam is therefore a neutral human-identity continuity object that can preserve name history, contextual names, record-linkage evidence, corrections, unresolved collisions and scoped verification without silently choosing a legal identity system.

## Pokémon source scan

### Trainer ID numbers and Original Trainer metadata

Sources:
- https://bulbapedia.bulbagarden.net/wiki/ID
- https://bulbapedia.bulbagarden.net/wiki/Original_Trainer

Reusable pattern:

Pokémon games sometimes identify an origin relationship by combining several fields rather than trusting a visible name alone. Bulbapedia documents that Original Trainer identity and outsider-Pokémon determination can involve Trainer name, visible ID, secret ID and other stored attributes. It also documents why a hidden identifier exists: two Trainers may share the same visible name and visible ID while still being distinct.

Ouros transformation:

`SAME_VISIBLE_NAME != SAME_ACTOR`.

`SAME_VISIBLE_IDENTIFIER != SAME_ACTOR` unless a governing system explicitly guarantees uniqueness in that scope.

`ORIGIN_METADATA_MATCH != CURRENT_RELATIONSHIP_STATE`.

This is a provenance lesson only. Ouros does not inherit game-save IDs, secret IDs, outsider-Pokémon mechanics or Original Trainer algorithms as human civil-identity rules.

The Pokémon Agency layer remains authoritative for Pokémon origin/association continuity. Human identity records may be referenced by Pokémon provenance when canon permits, but Pokémon metadata cannot become a universal human registry by implication.

### Trainer Cards, Trainer Passports and League Cards

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Trainer_Card_(game)
- https://bulbapedia.bulbagarden.net/wiki/League_Card
- https://bulbapedia.bulbagarden.net/wiki/User:TrainerSplash/Trainer_Passport

Reusable pattern:

Pokémon regions represent Trainer-facing identity and progression artifacts differently. Galar's League Card is explicitly a regional Trainer card form, while Alola's Trainer Passport is presented as a region-specific replacement for earlier Trainer Cards and includes a combination of identity-like fields and progression markers.

Ouros transformation:

A visible card or profile should be modeled as an institution-specific presentation record, not the actor's identity itself.

`CARD_PRESENTED != IDENTITY_FULLY_PROVEN`.

`REGIONAL_TRAINER_DOCUMENT != UNIVERSAL_OUROS_IDENTITY_DOCUMENT`.

`ACHIEVEMENT_MARKER != IDENTITY_ATTRIBUTE`.

Different regions may eventually have different trainer-facing records, but Pass 137 does not canonize any of them.

### Name Rater / renaming mechanics

Source:
- https://bulbapedia.bulbagarden.net/wiki/Renamer

Reusable pattern:

Across game generations, the fields used to decide whether a player is treated as a Pokémon's Original Trainer have changed. This is useful as a continuity warning: identity matching rules can be versioned and context-specific.

Ouros transformation:

A historical record should preserve which matching rule or institutional interpretation was in effect at the time. Later rule changes do not retroactively rewrite earlier events.

This source applies to Pokémon game mechanics and does not establish human naming law, Pokémon ownership law or renaming authority in Ouros.

## Pokémon tabletop community scan

Public PTU discussions commonly treat Trainer licenses, IDs and onboarding tests as campaign-specific setting decisions rather than universally enforced PTU mechanics. Community examples use trainer-license tests as tutorials or story gates, while other campaigns omit such structures entirely.

Reusable lesson:

A license ceremony can be useful worldbuilding only when a campaign has authored that institution. It must not be inferred from the existence of Trainer classes, badges or battle participation.

Ouros transformation:

`TRAINER_CLASS != TRAINER_LICENSE`.

`BADGE != CIVIL_IDENTITY`.

`BATTLE_PARTICIPATION != REGISTRATION`.

`PLAYER_CHARACTER != AUTOMATICALLY_REGISTERED_TRAINER` unless project canon says so.

Community material is design inspiration, never PTU rules authority.

## Identity architecture scan

### NIST identity-proofing separation

Sources:
- https://pages.nist.gov/800-63-3/
- https://pages.nist.gov/800-63-3/sp800-63a.html
- https://pages.nist.gov/800-63-3-Implementation-Resources/63A/validation/
- https://pages.nist.gov/800-63-3-Implementation-Resources/63A/verification/

The currently published NIST digital-identity suite separates several questions that are often collapsed in fiction:

- identity resolution: which identity within a relevant population/context is being claimed;
- evidence validation: whether presented evidence is authentic/current enough for its purpose;
- identity verification: whether that evidence belongs to the person presenting it;
- authentication: whether a returning claimant controls an authenticator associated with an account;
- authorization: whether that authenticated identity may perform a particular action.

Reusable Ouros architecture:

`CLAIMED_IDENTITY != RESOLVED_IDENTITY`.

`EVIDENCE_AUTHENTIC != EVIDENCE_BELONGS_TO_PRESENTER`.

`IDENTITY_VERIFIED_FOR_SCOPE != AUTHORIZED_FOR_ACTION`.

`AUTHENTICATED_ACCOUNT != PERSON'S COMPLETE IDENTITY`.

`ONE_CONTEXT_UNIQUE_ID != UNIVERSAL_PERSON_IDENTIFIER`.

This pass imports only the separation of questions. It does not import U.S. federal assurance levels, acceptable document lists, biometrics, retention rules, address-confirmation requirements or technology requirements.

### Privacy and minimization lesson

NIST identity-proofing guidance also emphasizes collecting only attributes needed for a stated proofing purpose. This is useful for Ouros because identity continuity can otherwise become an omniscient dossier system.

Ouros transformation:

A service should request or reveal only the identity attributes required by its authored scope. A library pickup, clinic appointment, academy transfer or ferry booking need not expose every former name, residence, family link or case record.

`IDENTITY_RECORD_EXISTS != EVERY_INSTITUTION_CAN_READ_IT`.

`LINKAGE_EXISTS != LINKAGE_IS_PUBLIC`.

`FORMER_NAME_KNOWN_TO_AUTHORITY != FORMER_NAME_PUBLIC`.

No real-world privacy law is imported.

## High-level design lessons

### 1. Actor identity needs a stable internal key

Narrative continuity should use an immutable `actor_id` even when display names, titles, spellings, transliterations, institutional identifiers or public aliases change.

The internal key is a simulation identity, not automatically an in-world number printed on documents.

### 2. Names are time-bounded claims

A name record needs at minimum the actor, name form, context, time interval or known effective range, source/provenance and visibility.

A former name remains historically relevant without remaining the current public name.

### 3. Homonyms need first-class support

Two actors can legitimately share a name. The generator must never merge them because a roster, letter or newspaper contains the same string.

### 4. Different names do not imply different people

Spelling variants, shortened forms, transliteration, titles, married names, stage names, pen names, nicknames, regional naming conventions or corrected records can all point to one actor when supported by provenance.

This is a candidate capability, not a canon list of naming practices in Ouros.

### 5. Corrections should append history

When a record is corrected, preserve the prior record version, correction event, reason/evidence scope and effective interpretation. Do not rewrite old Chronicle events to show the new value as if it had always been present.

### 6. Linkage needs evidence and confidence

A record-linkage claim should state why two records are believed to refer to the same actor and whether the conclusion is verified, probable, disputed or unresolved.

### 7. Institutions can disagree

One institution may have updated a name while another still carries an older record. This can create realistic administrative friction without implying fraud or incompetence.

### 8. Deceptive cover remains separate

The Infiltration layer already owns cover identity. Pass 137 must not label every alias, nickname, artistic name or former name as deception.

`ALIAS != COVER_IDENTITY`.

`NAME_DISCREPANCY != FRAUD`.

### 9. Recognition can be local

An academy may accept that two records belong to one student while a remote institution still has an unresolved linkage. Interregional Mobility can own recognition of the linked record without changing the underlying actor.

### 10. Identity and relationship remain separate

Matching a person does not establish residence, employment, family relationship, Pokémon ownership, credential validity, guilt, entitlement or authority. Those remain with their governing layers.

## Candidate story structures

### Record mismatch without villainy

A recurring character returns to a familiar service under a current name while an older roster uses a former or differently rendered name. The player's task is to follow provenance, not expose a criminal.

### Homonym mystery

Two people with the same common name appear in different archives. Chronology, location and institutional references resolve which record belongs to whom.

### Delayed correction

An institution corrected a record weeks ago but a downstream copied roster predates the correction. Both documents can be authentic while disagreeing.

### Public/private identity split

A performer, author, researcher or community figure is widely known by one public form while a private service uses another verified identity record. The quest must preserve the privacy boundary.

### Cross-region transliteration or formatting mismatch

Two regions record the same actor differently. The puzzle is not to choose which spelling is 'real' but to establish that the records refer to one actor and preserve each record's local form.

### Historical succession of names

A long-running shop, school, club or household archive contains records under several names for one recurring NPC. The visible change becomes environmental storytelling across years.

## Encounter-design lessons

Identity should almost never be resolved by combat. Tactical incidents can interrupt an appointment, office, transfer or archive process, but the battle result must stay physically narrow.

Useful full-version situations may include:

- staff withdrawal from a record office;
- clearing access while a protected packet remains under separate custody;
- securing an appointment perimeter while verification is paused.

Reduced versions can be combat-ready by removing applicants, records, couriers and sensitive identity processes from BattleSpec before combat begins.

Battle victory must never:

- authenticate a person;
- validate a document;
- link two records;
- approve a name correction;
- reveal a former name;
- grant a credential;
- establish citizenship or residence;
- establish family relationship;
- establish Pokémon ownership;
- prove deception;
- create institutional authority.

## PTU/Caelo cross-check

The internal `research/2026-08-18-source-scan.md` confirms PTU/Caelo support for campaign structure, actor-centered arcs, skill backgrounds, Features, social play, persistent activities and mechanically authored environmental effects.

No inspected governing source establishes a universal Ouros/PTU human civil registry, Trainer ID database, passport requirement, legal-name change procedure, biometric identity system or universal identity-check Skill DC.

Therefore the following remain UNKNOWN unless exact project sources later establish them:

- universal Trainer registration;
- universal Trainer ID numbers as in-world civil identifiers;
- passports or visas;
- citizenship or nationality mechanics;
- birth-registration mechanics;
- mandatory surnames;
- universal legal-name rules;
- universal age-of-majority identity rules;
- universal signature checks;
- document forgery detection DCs;
- identity proof via General Education, Perception, Intuition, Guile or Command;
- biometric systems;
- Aura, Telepathy, Psychic sensing or Pokémon species as universal identity verification;
- Trainer Features that establish civil identity or institutional authority.

## Research exclusions

No protected prose, dialogue, distinctive character or plot is copied.

Bulbapedia material is used for high-level mechanics/worldbuilding patterns only.

Community posts are treated as anecdotal design evidence, not rules authority.

NIST material is used only to separate proofing, validation, verification, authentication, authorization, minimization and scope. No federal policy is imported.

## Pass 137 design target

Create a proposed `Human Identity, Name & Record Continuity Extension` that provides:

- persistent simulation identity;
- versioned name records;
- public/contextual/former name forms;
- institutional identifiers kept local to their issuer;
- record-linkage claims;
- correction history;
- scoped verification episodes;
- privacy and disclosure boundaries;
- explicit handoffs to Credentials, Infiltration, Personal Records, Family, Residential, Mobility, Case Authority and Pokémon Agency;
- mysteries and quests based on chronology/provenance rather than automatic fraud;
- full and reduced encounter variants with permanent engine dependency categories visible.

Nothing in this research file is canon-approved merely by inclusion.