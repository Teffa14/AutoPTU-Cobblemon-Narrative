# Engine Readiness Snapshot — Pass 122

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU were inspected read-only.

## Live heads inspected

AutoPTU-Java `main`: `5eef0c0e8364a4f4a4f8bdb811107895e4cdbe7d`

Newest Java slice wires the previously frozen Safeguard status-prevention contract into the authoritative status-application hook registry. The implementation preserves target Ability-prevention priority, Infiltrator bypass and the Python behavior where Safeguard blocks applicable status application without consuming/removing the Safeguard entry. Runtime regression tests cover the boundary.

This is concrete progress for status lifecycle, move/status interaction and Ability interaction. It does not complete the full status controller, every status-prevention rule, Safeguard duration/progression in all contexts, all Move interactions, all Abilities or all field-state semantics.

AutoPTU `main`: `91270f54b237e177fef46a875f5599e114db97e3`

Newest Python commit adds a Career browser-entrypoint smoke test. The preceding battle change fixes Color Change same-type event emission. These changes do not promote a permanent tactical family.

## Java README evidence

The live README still lists these major areas as incomplete:
- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Permanent capability categories

VERIFIED:
- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

PARTIAL:
- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

BLOCKING:
- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No permanent category is promoted in Pass 122.

## Why identity belongs outside the battle core

Nothing inspected establishes authoritative overworld systems for:
- stable cross-institution actor identity;
- historical name changes;
- aliases and stage names;
- contextual display names;
- alternate scripts/transliterations;
- institutional identifiers outside battle state;
- public identity-card revisions;
- duplicate-name disambiguation;
- archival record linkage;
- account-to-actor identity claims;
- persona-to-actor knowledge state;
- identity privacy;
- Pokémon nickname history outside battle;
- persistent post-release Pokémon identity reconciliation.

These belong to world/server persistence. AutoPTU should receive stable combatant/controller IDs and mechanically relevant state after identity resolution has occurred.

## Pass 122 encounter dependency map

### Duplicate Challenger Record — FULL

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if evacuation/protection lanes are tactical
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only if a validated venue hazard or protected zone has tactical behavior
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for PROTECT/WITHDRAW/CLEAR_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: both challengers and identity records remain outside the grid. Any combat uses a conventional static arena. The identity decision resumes afterward and cannot be determined by battle outcome.

### Archive Alias Retrieval — FULL

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING if archive staff or protected holdings must be escorted tactically
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if a validated archive hazard/protected zone enters battle
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for PROTECT/CLEAR_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: archival search, alias linkage and provenance resolve entirely in world state. If confrontation occurs, use a safe static room and keep records/holdings outside tactical authority.

### Former Partner, Same Nickname — FULL

- targeting/footprints/range/LoS: VERIFIED if a battle actually occurs
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING for dynamic approach/withdrawal routes
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only when a verified environmental rule is active
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for autonomous WITHDRAW/AVOID/PROTECT
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for persistent individual projection and semantic withdrawal

Reduced version: identity investigation uses photography, prior partnership records and current observations in overworld state. No battle is required. Same species/name/history never grants old command authority.

## New overworld blockers introduced by Pass 122

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

## Hard non-inferences for Pass 122

Do not infer:
- same name -> same actor;
- different name -> different actor;
- shared surname -> family relationship;
- alias -> crime;
- stage name -> deception;
- display name -> authoritative identifier;
- account handle -> physical actor;
- account action -> conclusive attribution;
- old name -> invalid historical record;
- title -> Command/authority outside authored scope;
- uniform/card -> identity proof beyond its verified purpose;
- nickname -> Pokémon ownership;
- nickname -> Pokémon Loyalty;
- same species + nickname -> same Pokémon;
- evolution -> new individual identity;
- transfer/release -> erased individual history;
- identity mismatch -> fraud;
- hidden persona -> automatic Guile/disguise mechanics;
- battle victory -> identity claim resolved.

## PTU/Caelo validation state

The accessible File Library search recovered a previous PTU-oriented project research package and AutoPTU code evidence but did not recover the complete primary Caelo rulebook/Player's Guide/errata corpus required to establish exact identity-related mechanics. Super PTU Online Helper was not exposed as an invocable capability.

Pass 122 therefore does not validate or invent:
- disguise checks;
- Guile/Charm/Command modifiers;
- forgery rules;
- impersonation rules;
- memory/telepathy identity rules;
- universal Trainer registration;
- legal-name requirements;
- Pokémon nickname restrictions;
- ownership inferred from names;
- identification Skill DCs.

## Current engine conclusion

Java's status path is materially stronger than at Pass 121 because Safeguard is now wired into the canonical status-application registry with tested Ability priority and Infiltrator bypass. Status lifecycle, Abilities and move/status interaction remain PARTIAL because this is one validated slice, not family-complete coverage.

Identity-heavy Ouros stories are therefore low-risk when resolved primarily in world state. Tactical escalation should remain a separate battle snapshot whose mechanics use only the permanent capability families proven above.