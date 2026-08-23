# Research Scan — Identity, Names, Aliases & Record Linkage — Pass 122

Status: research/provenance only. Not Ouros canon. External stories, products and administrative systems are inspiration sources, not rules sources.

## Why this pass

The repository already distinguishes credentials, digital identities, public personas, archival records, Pokémon persistent identity, taxonomy, family relationships, employment, memberships and access permissions. What was still missing was the common identity layer beneath those systems: the fact that one actor can appear under several names, handles, titles, nicknames, historical spellings or institutional identifiers while remaining the same persistent person or Pokémon.

Pass 122 therefore focuses on identity resolution rather than identity as a personality trait. The core problem is simple: records can disagree about the label while still referring to the same entity, and identical labels can refer to different entities.

This layer must not create a universal civil registry, citizenship system, legal-name regime, passport system or compulsory Trainer registration unless Ouros canon later establishes those institutions.

## Existing repository boundary

Credentials already states that Ouros must not invent a universal Trainer license, passports, citizenship or visas. It also notes that a damaged registry or a name change can create record mismatches without changing the underlying permission.

Digital Systems already treats a handle or account as a digital identity that may or may not be verified to an actor. An account action supports attribution; it does not automatically prove who physically used the account.

Archives already separates physical holdings, catalog records and later corrections. Public Memory preserves what was published at the time. Pokémon Agency preserves individual Pokémon identity across custody, partnership and release.

Pass 122 does not replace any of those authorities. It supplies stable actor identity, name/identifier history and record-linkage claims that those systems can reference.

## Sources and reusable structures

### Pokémon Sword/Shield — League Cards
Source: https://swordshield.pokemon.com/en-au/gameplay/league-card/

Galar Trainers create League Cards containing detailed information about themselves, customize how they are presented and exchange the cards with other people. Copies are retained in an album.

Reusable structure:
- a public-facing identity card can be presentation, not the complete authoritative identity record;
- the same Trainer can issue multiple visual revisions over time;
- recipients can retain historical copies after the Trainer changes their current presentation;
- public persona and institutional identity can overlap without becoming the same object.

Do not import Galar's specific Card Maker, graphics, league rules or card fields as mandatory Ouros infrastructure.

### Pokémon Trainer Central — name, username and screen name
Source: https://support.pokemon.com/hc/en-us/articles/6235404548628-What-s-the-difference-between-a-name-username-and-screen-name-in-Pok%C3%A9mon-Trainer-Central

Updated June 10, 2026, Pokémon Support explicitly distinguishes account username, publicly displayed screen name and the person's name. The username can be private while the screen name is public.

Reusable structure:
- private login identifier, public handle and personal name can coexist;
- changing which label is displayed should not change the actor identity;
- different visibility policies can apply to different identity attributes.

Ouros adaptation should remain fictional and server-owned. Do not copy real account requirements, privacy rules or platform policies.

### Play! Pokémon — Player ID linkage
Source: https://support.play.pokemon.com/hc/en-us/articles/25695447659540-How-do-I-add-a-Player-ID-to-my-Pok%C3%A9mon-Trainer-Central-account

A Player ID can be linked to an account and later event participation appears after an organizer records it.

Reusable structure:
- institutional identifiers can be issued separately from an actor's ordinary name;
- an identifier may be linked to multiple event records without becoming the actor's public display name;
- event participation can arrive later than identity enrollment.

Do not import real-world tournament account policy, minors policy or ID-number format into Ouros.

### Pokémon Trainer Central — current registration fields
Source: https://support.pokemon.com/hc/en-us/articles/360043974292-How-do-I-opt-in-for-Play-Pok%C3%A9mon-on-my-Pok%C3%A9mon-Trainer-Central-account

The current Pokémon service distinguishes personal name, screen name, leaderboard display name and optional Player ID within the same profile workflow.

Reusable structure:
- one actor can have several context-specific labels simultaneously;
- leaderboards, public profiles and internal systems need not expose the same identifier;
- mapping among identifiers should be explicit rather than inferred from matching strings.

### Play! Pokémon — Trainer username/team name policy
Source: https://www.pokemon.com/static-assets/content-assets/cms2/pdf/play-pokemon/rules/play-pokemon-trainer-username-and-team-name-policy-en.pdf

The policy separately discusses Trainer usernames, team names, Pokémon nicknames and other custom labels used in organized play.

Reusable structure:
- identity labels are typed and context-dependent;
- a nickname or team name cannot safely stand in for actor identity;
- moderation or renaming of a display label should not erase the historical events recorded under it.

No conduct policy or sanction framework is imported into Ouros.

### PTU — Character Creation
Sources:
- https://pturpg.wikidot.com/character-creation
- https://pokemontabletop.fandom.com/wiki/Character_Creation

PTU treats the Trainer character as a persistent player character with a character sheet and narrative description. Campaigns may range from first-journey Trainers to detective-agency rookies or villain-team grunts.

Reusable structure:
- character identity persists across changes of role, institution and public presentation;
- institutional membership is not the same thing as identity;
- one character can participate in several campaign contexts without becoming a new entity.

These mirrors are supporting references only. The project PTU/Caelo source set remains authoritative for rules.

### Kairos Isles — persistent living-world character records
Source: https://kairosptu.wiki.gg/

Kairos Isles is a public PTU living world with character pages, NPC lists and persistent player participation across quests and downtime.

Reusable structure:
- a long-running shared world benefits from stable character references that survive individual sessions;
- display pages and public character summaries are useful indexes but should not become the sole world authority;
- identity resolution matters more as many players and NPCs accumulate years of records.

No Kairos rules, characters, IDs or setting details are imported.

### Library of Congress — authority records and variant names
Sources:
- https://www.loc.gov/marc/authority/adintro.html
- https://www.loc.gov/marc/authority/adx00.html
- https://www.loc.gov/marc/uma/pt1-7.html

Library authority records preserve an established form of a name while retaining variant and related forms so records can still be found when users search another spelling, former name or pen name.

Ouros adaptation:
- use a persistent actor ID as the entity anchor;
- store multiple name assertions with provenance and time scope;
- support search aliases without rewriting historical records;
- treat name forms as access paths to identity, not identity itself.

Do not import MARC fields or library catalog rules directly.

### ORCID — published name, ordinary name and “also known as”
Source: https://support.orcid.org/hc/en-us/articles/360006973853-Add-and-edit-your-name-on-your-ORCID-record

ORCID permits a published name, ordinary name and multiple “also known as” forms, including former names, alternate forms and different scripts.

Reusable structure:
- one persistent identifier can remain stable while names change;
- preferred public presentation can differ from older records;
- aliases can have their own visibility settings;
- alternate scripts and transliterations are first-class variants rather than separate people.

Do not import ORCID policy, identifier format or real personal-data requirements.

### National Archives of Australia — searching historical people under multiple names
Sources:
- https://www.naa.gov.au/help-your-research/getting-started
- https://www.naa.gov.au/help-your-research/getting-started/recordsearch-overview/namesearch

Historical research often requires searching full names, former names, aliases and different spellings. Exact-string searches can miss relevant records.

Reusable structure:
- duplicate or fragmented historical records can be ordinary data problems rather than conspiracies;
- an archive may need a linkage hypothesis before merging records;
- a single shared surname or exact name match is insufficient to prove identity.

Do not import Australian civil-record systems into Ouros.

## Design lessons for Ouros

1. Persistent actor identity should not be a mutable display name.
2. Names, handles, titles, nicknames, IDs and account labels should be typed records.
3. Historical names must remain searchable after a preferred display name changes.
4. Two people can share the same name without being the same actor.
5. Two differently named records can refer to the same actor without either record being fraudulent.
6. Record linkage should have evidence and confidence rather than an automatic string-match merge.
7. Public-facing cards and profiles should be snapshots or presentation records, not total identity truth.
8. Digital identity, physical credential, membership and actor identity remain separate.
9. A rename should not rewrite battle history, publications, claims, photographs, contracts or public memory.
10. A corrected identity link can supersede a prior interpretation without erasing that the prior interpretation once existed.
11. Identity privacy is scoped; a player may expose a battle handle while keeping other personal labels private.
12. Pokémon nicknames are labels attached to a persistent Pokémon entity, not a replacement for `pokemon_entity_id`.
13. Evolution, transfer, release or ownership change must not create a new Pokémon merely because displayed species/name fields change.
14. A trainer's public persona can be intentionally stylized without automatically becoming deception.
15. Impersonation should remain a claim/evidence problem unless a dedicated mechanic or authored event establishes it.

## Suggested identity classes

Useful typed labels can include:
- preferred personal name;
- former name;
- nickname;
- public stage/battle name;
- institutional display name;
- account handle;
- leaderboard name;
- pen name/byline;
- title or office style;
- local-language form;
- alternate-script form;
- transliteration;
- temporary cover identity when an authored infiltration scenario requires one;
- Pokémon nickname;
- registry identifier;
- event participant number;
- internal record identifier.

No class implies legal status unless canon explicitly says so.

## Record-linkage rules

A linkage claim should be able to use:
- explicit actor confirmation;
- persistent internal ID;
- issuing-institution cross-reference;
- trusted credential link;
- chronology;
- known residence/work/institution history;
- stable Pokémon partnership history;
- photographs or other records with provenance;
- direct archival cross-reference;
- player-authored confirmation for PCs.

Weak evidence includes:
- same name alone;
- same outfit;
- similar appearance;
- same species partner;
- rumor;
- matching public handle without account verification;
- proximity to an event.

## PTU/Caelo boundary

No new PTU mechanic is validated here.

Do not infer:
- Guile bonus from using an alias;
- disguise success from a changed display name;
- Charm/Command changes from a title;
- League eligibility from a public card;
- Trainer Feature access from an ID;
- Pokémon Loyalty/obedience from a nickname;
- capture ownership from the name shown on a record;
- identification DCs;
- impersonation DCs;
- forgery mechanics;
- mechanical effects for pseudonyms, titles or uniforms.

The accessible File Library returned a previous project research package and AutoPTU code evidence but did not recover a complete primary Caelo rules corpus for this pass. The project PTU/Caelo materials therefore remain the required authority before any mechanical identity, Guile, disguise or registration rule is implemented.

## Engine relevance

Identity resolution is primarily overworld/server state. Most identity stories can run without battle-specific rules.

When identity-linked stories escalate to tactical encounters, identity itself should be resolved before the battle snapshot. AutoPTU should receive combatant IDs, controllers and legal battle state; it should not determine whether two archival names refer to the same person.

The current Java evidence strengthens status prevention but does not change this boundary.

## Provenance status

Everything in this file is research-only. It establishes reusable structures and guardrails. Proposed schemas and original Ouros content belong in `design/` and `proposals/`. Nothing here is canon.