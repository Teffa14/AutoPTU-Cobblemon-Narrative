# Ouros Identity, Names, Aliases & Record Linkage Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

Ouros needs one persistent identity model beneath credentials, records, public personas, employment, family history, archives, digital accounts, competitive history and Pokémon partnership state.

The system must support ordinary changes over time without turning them into mysteries by default:
- a person changes the name they use publicly;
- two institutions spell the same name differently;
- a battle circuit uses a stage name;
- a researcher publishes under an alternate form;
- an old archive uses a former name;
- two unrelated people share the same name;
- a Pokémon receives a nickname after years of prior records;
- a player corrects how their character should be displayed;
- a historical record cannot yet be confidently linked to a known NPC.

This layer owns stable actor identity, name/identifier history and record-linkage claims.

It does not create a universal civil registry, legal-name law, citizenship, passports, universal Trainer licenses or mandatory real-name disclosure.

## Core separation

Keep these independent:

persistent actor identity → who the entity is in Ouros;

name assertion → one label used for that actor in one context/time;

public presentation → what an audience sees;

institutional identifier → what one institution uses to link records;

digital identity → account/handle state;

credential → recognized qualification/permission;

membership/employment → relationship with an institution;

record-linkage claim → whether two records refer to the same entity;

public belief → what other actors think;

mechanical PTU state → Skills, Features, stats, Pokémon state and battle legality.

None of these automatically proves the others.

## 1. Persistent actor identity

```yaml
actor_identity:
  actor_id: null
  actor_kind: PERSON|POKEMON|INSTITUTIONAL_ENTITY|OTHER
  current_preferred_name_ref: null
  name_assertion_ids: []
  identifier_ids: []
  public_profile_refs: []
  digital_identity_refs: []
  credential_refs: []
  record_linkage_claim_ids: []
  identity_status: ACTIVE
  created_at: null
  provenance_refs: []
  canon_status: proposed
```

`actor_id` is the stable world anchor.

Renaming does not create a new actor.

Changing jobs does not create a new actor.

Joining or leaving a faction does not create a new actor.

For Pokémon, evolution, transfer, release and later reacquisition must preserve the same `pokemon_entity_id` when the world has evidence that it is the same individual.

## 2. Name assertion

```yaml
name_assertion:
  name_assertion_id: null
  actor_id: null
  name_text: null
  name_type: PREFERRED|FORMER|NICKNAME|PUBLIC_BATTLE_NAME|BYLINE|TITLE_STYLE|LOCAL_FORM|ALTERNATE_SCRIPT|TRANSLITERATION|TEMPORARY_ALIAS|POKEMON_NICKNAME|OTHER
  script_or_language_ref: null
  valid_from: null
  valid_until: null
  asserted_by_id: null
  source_record_refs: []
  visibility: PRIVATE|RESTRICTED|GROUP|PUBLIC
  confidence: CONFIRMED
  supersedes_name_ref: null
  notes: null
```

A name can be historically valid even when it is no longer preferred.

A typo or disputed transcription should be stored as a record-specific label or uncertain assertion rather than silently promoted to the actor's name history.

## 3. Preferred display name

Preferred display is presentation state.

```yaml
preferred_display:
  actor_id: null
  name_assertion_id: null
  context_scope: GENERAL
  set_at: null
  set_by_id: null
  visibility: PUBLIC
```

Possible scopes:
- GENERAL
- LEAGUE
- RESEARCH
- MEDIA
- PERFORMANCE
- WORKPLACE
- SCHOOL
- CLUB
- PRIVATE_PARTY

One actor may legitimately use different display forms in different contexts.

A public battle name should not overwrite a private preferred form.

## 4. Institutional identifier

```yaml
institutional_identifier:
  identifier_id: null
  actor_id: null
  issuer_id: null
  identifier_type: null
  identifier_value: null
  valid_from: null
  valid_until: null
  status: ACTIVE
  visibility: RESTRICTED
  cross_reference_ids: []
  provenance_refs: []
```

Examples may eventually include:
- battle-circuit participant ID;
- academy record number;
- clinic patient record number;
- research contributor ID;
- employee record number;
- archive authority ID;
- local membership number.

Do not invent a region-wide identifier merely because individual institutions need their own IDs.

## 5. Public identity card/profile

```yaml
public_identity_profile:
  profile_id: null
  actor_id: null
  profile_type: LEAGUE_CARD|PUBLIC_DIRECTORY|STAFF_PAGE|PERFORMER_CARD|RESEARCH_BYLINE|OTHER
  revision: null
  display_name_ref: null
  public_identifier_refs: []
  public_role_refs: []
  image_record_refs: []
  public_fact_refs: []
  issued_at: null
  retired_at: null
  issuer_id: null
  provenance_refs: []
```

Historical copies remain valid evidence of how the actor presented themselves at that time.

A profile is not a complete biography.

A profile can contain outdated information without becoming fraudulent.

## 6. Record identity reference

Every record that refers to an actor should preserve what the source itself said.

```yaml
record_identity_reference:
  reference_id: null
  source_record_id: null
  literal_name_or_identifier: null
  linked_actor_id: null
  linkage_claim_id: null
  linkage_state: CONFIRMED|PROBABLE|POSSIBLE|UNRESOLVED|REJECTED
  source_context: null
  source_date: null
  provenance_refs: []
```

This allows an archive to display the original wording while still linking the record to the current actor.

## 7. Record-linkage claim

Do not merge records by string matching.

```yaml
record_linkage_claim:
  linkage_claim_id: null
  subject_record_refs: []
  candidate_actor_ids: []
  claim_type: SAME_ACTOR|DIFFERENT_ACTORS|PARENT_CHILD_RECORD|POKEMON_SAME_INDIVIDUAL|OTHER
  proposed_actor_id: null
  evidence_refs: []
  contradiction_refs: []
  confidence: POSSIBLE
  assessed_by_ids: []
  assessed_at: null
  status: OPEN
  supersedes_claim_id: null
  privacy: RESTRICTED
```

Suggested confidence values:
- POSSIBLE
- PROBABLE
- HIGH_CONFIDENCE
- CONFIRMED
- DISPROVEN
- UNRESOLVED

For player characters, irreversible identity merges require player-authored confirmation unless an already-established authoritative world record makes the mapping explicit.

## 8. Duplicate-name collision

Two actors can share the same display name.

Never solve this by modifying one automatically.

Disambiguation can use contextually safe fields such as:
- public institution;
- public role;
- region or settlement when already public;
- public participant ID;
- public photograph;
- explicit user selection.

Do not reveal private address, clinic data, family records or other restricted attributes merely to disambiguate a UI.

## 9. Name change

A name change is an append-only identity event.

```yaml
name_change_event:
  event_id: null
  actor_id: null
  prior_preferred_ref: null
  new_preferred_ref: null
  effective_at: null
  actor_confirmed: true
  affected_public_profile_ids: []
  update_request_ids: []
  historical_rewrite_forbidden: true
```

Expected behavior:
- future interfaces use the new preferred display where permitted;
- old battle transcripts preserve the old display label plus stable actor ID;
- search indexes can find both forms;
- public memory can say what name was used at the time;
- downstream institutions may update at different times;
- stale records can create ordinary follow-up work without implying wrongdoing.

## 10. Alternate scripts and transliterations

A name rendered in another script is usually another representation, not another actor.

```yaml
name_rendering_link:
  source_name_ref: null
  rendered_name_ref: null
  relation: TRANSLITERATION|TRANSLATION|LOCALIZED_FORM|ALTERNATE_SCRIPT
  method_ref: null
  reviewed_by_id: null
  confidence: confirmed
```

Two different transliterations can both be acceptable.

The system should not force every region to share one universal spelling convention.

## 11. Titles and offices

Titles are role-linked labels.

Examples:
- Professor;
- Gym Leader;
- curator;
- captain;
- doctor;
- champion;
- coordinator;
- ranger role if canon establishes it.

A title:
- does not change `actor_id`;
- may expire when the role ends;
- does not prove current authority outside its scope;
- does not grant PTU Features or Skill ranks;
- may remain historically correct in old records.

## 12. Public persona and stage identity

Use the Fandom/Media/Performance layers for audience state.

This layer only links the persona label to the persistent actor when that link is known.

```yaml
persona_identity_link:
  persona_id: null
  actor_id: null
  public_name_ref: null
  public_link_state: OPENLY_KNOWN|LIMITED|SECRET|DISPUTED
  evidence_refs: []
  privacy: null
```

A secret persona should not be deanonymized by backend convenience.

The server may know a linkage for authority purposes while keeping it unavailable to players who have not learned it.

## 13. Temporary cover identities

Cover identities belong to authored infiltration/espionage stories, not routine renaming.

```yaml
cover_identity:
  cover_identity_id: null
  actor_id: null
  presented_name_ref: null
  supporting_record_refs: []
  active_scope: []
  starts_at: null
  ends_at: null
  authorized_by_ref: null
  public_link_state: hidden
  mechanics_review_required: true
```

This layer stores the presented identity and knowledge graph. It does not decide Guile, disguise, impersonation or detection mechanics.

## 14. Pokémon names and nicknames

A Pokémon's name presentation must remain separate from individual identity.

```yaml
pokemon_name_history:
  pokemon_entity_id: null
  nickname_assertion_ids: []
  species_name_display_ref: null
  current_preferred_nickname_ref: null
  trainer_or_custodian_display_context: null
  historical_record_refs: []
```

Hard rules:
- nickname change does not create a new Pokémon;
- evolution does not erase nickname history;
- transfer does not erase prior nickname history;
- release does not erase identity;
- same nickname does not prove same Pokémon;
- same species + same nickname does not prove same Pokémon;
- public records should not expose private ownership/custody information automatically.

Any actual nickname-change restrictions from Pokémon or PTU require source validation before becoming mechanics.

## 15. Identity conflicts and corrections

Identity problems should be represented as cases, not instant backend rewrites.

Possible states:
- DUPLICATE_RECORD
- MISLINKED_RECORD
- UNLINKED_HISTORICAL_RECORD
- STALE_NAME
- TYPO_OR_TRANSCRIPTION_ERROR
- DUPLICATE_NAME_COLLISION
- IDENTIFIER_REUSE_CLAIM
- ACCOUNT_ACTOR_MISMATCH_CLAIM
- POKEMON_IDENTITY_MERGE_CLAIM
- PUBLIC_PERSONA_LINK_CLAIM

A correction event should preserve:
- what the record said;
- what was believed at the time;
- what evidence changed the assessment;
- who authorized the correction;
- which downstream systems still need reconciliation.

## 16. Privacy and player agency

Identity is high-sensitivity state.

For PCs:
- the player controls preferred display name and private aliases unless a game mechanic explicitly constrains a particular authored scenario;
- the system must not infer a former name, family name, gendered naming convention, legal status or private identity history;
- public performance or battle participation does not make all identity fields public;
- one player's private identity information cannot be exposed to another player because they are in the same party.

For NPCs:
- private aliases require authored provenance;
- hidden identities should have explicit knowledge-state controls;
- generated content should not create secret family relationships merely to explain a name mismatch.

## 17. Knowledge model

Different actors can know different identity links.

```yaml
identity_knowledge_claim:
  knower_id: null
  subject_actor_or_record_id: null
  claimed_actor_id: null
  claim_type: SAME_PERSON|ALIAS_OF|FORMER_NAME_OF|POKEMON_SAME_INDIVIDUAL|OTHER
  confidence: null
  learned_from_refs: []
  learned_at: null
  superseded: false
```

The authoritative server may know the real linkage while a player does not.

Do not leak hidden identity by autocomplete, quest labels, scoreboard names, chat formatting or Minecraft entity nameplates.

## 18. Search and archive behavior

Search should support:
- exact current name;
- historical name;
- nickname;
- public alias;
- alternate script;
- transliteration;
- institutional public ID;
- archive cross-reference.

Search results should return identity candidates, not silently merge records.

A historical document should display its literal source wording even when the catalog adds a modern linked identity.

## 19. Integration with existing layers

Credentials references the stable actor and can preserve historical holder names without changing grant validity.

Digital Systems owns accounts and logs; this layer owns the actor-account linkage claim.

Archives stores the source record; this layer stores variant-name authority and cross-record linkage.

Public Memory preserves historical public labels.

Media preserves bylines, screen names and reported identity claims.

Fandom preserves audience knowledge and public personas.

Workplaces/Associations preserve role memberships without becoming identity authorities.

Family preserves confirmed kinship without inferring family relationships from shared names.

Interregional Mobility can preserve different regional naming conventions without requiring universal standardization.

Cases can investigate impersonation, duplicate records or attribution claims.

Infiltration owns covert presentation mechanics and observation state.

Pokémon Agency remains authoritative for persistent Pokémon identity, custody and partnership.

Taxonomy remains authoritative for species/form classification; identity is individual, taxonomy is classification.

## 20. Minecraft/Cobblemon boundary

Minecraft can present:
- current public display name;
- role title where public;
- institution-specific ID where intentionally visible;
- historical card/profile item;
- NPC introduction text;
- private UI labels known to that player;
- Pokémon nickname.

Minecraft must not:
- use entity display name as the primary database key;
- merge actors because names match;
- expose hidden aliases in nameplates;
- determine permissions from name text;
- determine ownership from nickname;
- rewrite historical signs/books automatically after a rename unless the underlying world object is actually edited.

Preferred adapter flow:

world object references stable actor ID → server resolves audience-specific display label → client renders allowed label → interactions return stable actor ID → downstream services use authoritative state.

## 21. PTU/Caelo boundary

Identity state does not grant mechanics.

Do not infer:
- Guile rank from an alias;
- Charm from fame or a stage name;
- Command from a title;
- Perception DC from a spelling mismatch;
- disguise success from a credential;
- impersonation success from a copied card;
- Trainer Feature access from an institutional identifier;
- battle eligibility from display name alone;
- Pokémon Loyalty from nickname history;
- capture ownership from an owner-name field;
- social bonuses for using someone's preferred name.

Any dedicated Guile, disguise, illusion, memory, telepathy, forgery or identity-related mechanics require exact PTU/Caelo validation and Java parity before tactical use.

## 22. Encounter contract A — Duplicate Challenger Record

Narrative premise:

Two League records with nearly identical names appear to refer to one challenger, but their battle histories and public cards conflict. Before a scheduled exhibition, staff must determine whether this is a duplicate record, two different people or a stale cross-reference.

Full version:

An unrelated disturbance can escalate during the verification window, requiring staff evacuation and protection of a records terminal while the two challengers remain noncombatants. The identity decision continues after battle from evidence state.

Capability dependencies:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: BLOCKING if protection/evacuation lanes are tactical;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING only if validated dynamic site effects enter battle;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for PROTECT/WITHDRAW/CLEAR_ROUTE;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

Reduced version:

Keep both challengers and records staff outside the grid. If a battle occurs, use a static legal arena with unrelated combatants. Resume record reconciliation afterward. Battle outcome cannot decide identity.

## 23. Encounter contract B — Archive Alias Retrieval

Narrative premise:

A missing research notebook may have been catalogued under a former byline. The party traces several variant-name references through an archive while another incident threatens the collection area.

Full version:

A tactical escalation could require clearing a safe route through a collection wing while preserving restricted archive zones and moving staff to safety.

Dependencies:
- complete movement/interception/forced movement: BLOCKING if escorts are tactical;
- terrain/hazards/zones/reactions: BLOCKING only if archive hazards or protected zones have mechanical effects;
- AI tactical policy: BLOCKING for PROTECT/CLEAR_ROUTE;
- adapter/playback: BLOCKING;
- all other permanent families follow the same VERIFIED/PARTIAL states above.

Reduced version:

Resolve archival search and identity linkage entirely outside combat. If a confrontation occurs, freeze a safe room as a static arena. The notebook's identity/provenance remains an Archives/Identity question.

## 24. Encounter contract C — Former Partner, Same Nickname

Narrative premise:

A wild Pokémon observed near an orchard has the same species and nickname once used by a released former partner. The player may investigate whether it is the same individual, a coincidence or a nickname copied into a public record.

Full version:

The Pokémon may choose to approach, withdraw or ignore the player while other wild actors move through the site. A future full version would require autonomous withdrawal/route behavior and objective-aware AI without granting the old Trainer command authority.

Dependencies:
- complete movement including interception/forced movement: BLOCKING for dynamic withdrawal/route behavior;
- AI tactical policy: BLOCKING for autonomous WITHDRAW/AVOID/PROTECT behavior;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for persistent individual projection;
- terrain/weather/hazards/zones/reactions: only if an actual validated environmental effect is used;
- Pokémon identity/custody remains an overworld blocker outside the permanent battle families.

Reduced version:

Keep identity investigation in overworld state using photographs, prior records and observed behavior. No battle is required. If an unrelated battle occurs, the possible former partner remains outside the grid unless it independently becomes a legal combatant. Same nickname never grants command authority.

## 25. Overworld implementation blockers

- `ACTOR_IDENTITY_REGISTRY`
- `NAME_ASSERTION_HISTORY`
- `CONTEXTUAL_DISPLAY_NAME_STATE`
- `INSTITUTIONAL_IDENTIFIER_REGISTRY`
- `PUBLIC_IDENTITY_PROFILE_REVISIONS`
- `RECORD_IDENTITY_REFERENCE`
- `RECORD_LINKAGE_CLAIM_GRAPH`
- `DUPLICATE_NAME_DISAMBIGUATION`
- `NAME_CHANGE_EVENT`
- `ALTERNATE_SCRIPT_TRANSLITERATION_LINKS`
- `PERSONA_IDENTITY_LINK`
- `COVER_IDENTITY_STATE`
- `IDENTITY_KNOWLEDGE_GRAPH`
- `IDENTITY_PRIVACY_POLICY`
- `SEARCH_ALIAS_INDEX`
- `DOWNSTREAM_IDENTITY_RECONCILIATION`
- `POKEMON_NICKNAME_HISTORY`
- `POKEMON_IDENTITY_LINKAGE_CLAIMS`
- `IDENTITY_TO_CREDENTIAL_HANDOFF`
- `IDENTITY_TO_DIGITAL_ACCOUNT_HANDOFF`
- `IDENTITY_TO_ARCHIVE_HANDOFF`
- `IDENTITY_TO_MEDIA_HANDOFF`
- `IDENTITY_TO_MINECRAFT_PRESENTATION`
- `IDENTITY_TO_BATTLE_COMBATANT_ID`

## 26. Hard non-inferences

Do not infer:
- same name → same actor;
- different name → different actor;
- shared surname → kinship;
- former name → secrecy;
- alias → criminality;
- stage name → deception;
- changed name → changed personality;
- public card → full identity record;
- account handle → physical actor;
- account action → conclusive attribution;
- title → authority outside scope;
- uniform → membership;
- nickname → Pokémon ownership;
- nickname → Pokémon Loyalty;
- same species + nickname → same Pokémon;
- evolution → new Pokémon identity;
- transfer → new Pokémon identity;
- old record name → record is invalid;
- name mismatch → fraud;
- duplicate record → malicious duplication;
- archival correction → historical record should be rewritten;
- hidden identity → automatic Guile mechanic;
- battle victory → identity claim resolved.

## 27. Canon promotion checklist

Before promoting an identity system or record to canon:

1. Confirm the relevant institution exists.
2. Confirm whether it actually issues an identifier or profile.
3. Confirm the identifier's scope and visibility.
4. Confirm whether the actor linkage is known, disputed or private.
5. Preserve source-record wording and provenance.
6. Preserve historical names rather than rewriting them away.
7. Confirm PC identity changes are player-authored.
8. Confirm no family, citizenship or legal-status system has been inferred from names.
9. Confirm Pokémon identity remains under Pokémon Agency.
10. Confirm Minecraft uses stable IDs rather than visible names as authority.
11. Confirm any disguise/Guile mechanics against PTU/Caelo and AutoPTU-Java before use.

## Open questions

- Does Ouros have any region-wide Trainer registration, or only institution-specific IDs?
- Which institutions publish public identity cards or profiles?
- Can different regions maintain independent spellings/transliterations for the same person?
- How should name changes propagate into public leaderboards without rewriting old events?
- Which identity attributes are private by default in multiplayer?
- Can a player choose different public names for performance and battle contexts?
- How should old NPC aliases be generated without overproducing secret-identity plots?
- What evidence is sufficient to merge two historical NPC records?
- How should persistent Pokémon be identified after release when nickname/species alone are insufficient?
- What exact PTU/Caelo rules, if any, govern disguise, Guile, impersonation, forgery, telepathy or memory-based identification?