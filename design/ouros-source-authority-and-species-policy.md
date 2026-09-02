# Ouros source authority, rules-profile and species policy

Status: OUROS PROJECT INVARIANT
Date: 2026-09-02

## Product target

Ouros is a Minecraft-native Pokémon MMORPG whose deep mechanical authority is PTU-derived. Minecraft is the playable world and interaction surface; the PTU engine owns mechanical adjudication. Caelo and Kairos are living-world references that can improve the product, but neither is automatically the rules constitution or setting of Ouros.

The project must be able to learn from multiple PTU communities without hard-coding any one campaign into the engine.

## Authority layers

Use these layers when evidence conflicts:

1. **Explicit Ouros project invariants and canon decisions.**
2. **PTU baseline and project-selected errata/supplements.**
3. **Rules-profile overlays explicitly adopted by Ouros.** Caelo, Kairos and future source packs can propose overlays; their rules do not activate automatically.
4. **Ouros MMO adaptations.** Persistent/multiplayer/Minecraft constraints may require declared adaptations. These must be documented and tested instead of hidden inside implementation details.
5. **World-specific Ouros content.** Regions, institutions, NPCs, encounter tables, progression gates and events consume the active rules profile.
6. **Minecraft/Cobblemon/Craftics presentation.** Presentation may express world and mechanical state but may not silently author canonical PTU outcomes.

A source's own claim of authority applies only inside that source's campaign/server. It does not outrank Ouros merely because the source compiled PTU rules successfully.

## Rules-profile requirement

Mechanical differences must be represented as explicit rules-profile data/contracts rather than campaign-name conditionals spread through battle code.

Target shape:

```text
PTU_BASE
+ SELECTED_ERRATA
+ OUROS_CORE_RULES
+ optional source-derived overlay(s)
+ world/server configuration
= ACTIVE_OUROS_RULES_PROFILE
```

Examples of rules-profile seams include capture, rest, experience, encounter generation, progression, item/service availability, class content and living-world downtime. A rule imported from Kairos or Caelo must record its provenance and why Ouros adopted it.

`SOURCE_HAS_RULE != OUROS_USES_RULE`

`SOURCE_IS_MATURE != OUROS_APPROVED`

`CAELO_VARIANT != KAIROS_VARIANT != OUROS_DEFAULT`

## Minecraft authority boundary

Minecraft is not merely a static renderer. It owns physical presentation and realtime interaction: navigation requests, visible actors, schedules, world construction, doors, vehicles, ambient behavior, animation, gathering surfaces, UI and social presence.

Minecraft does **not** get to decide PTU mechanical truth when that truth belongs to the authoritative rules engine.

```text
Minecraft intent / world interaction
    -> Ouros authoritative world service
    -> active PTU rules profile / AutoPTU-Java adjudication when mechanical
    -> semantic result
    -> Ouros persistent world state
    -> Minecraft projection
```

Examples:

- Minecraft pathfinding may propose a path; PTU/Ouros validates capability-dependent traversal when required.
- A visible wild Pokémon may wander, warn, flee or approach through Minecraft behavior, but combat legality and authoritative battle outcomes come from AutoPTU.
- Entity despawn, chunk unload, duplicate presentation actors, vanilla death events or animation state do not create canon by themselves.

## Species and form gate

Ouros uses official Pokémon as the default species universe. Availability in a particular region is still an Ouros content decision.

### Default allowed input

- Official Pokémon species.
- Official regional forms and other official forms when explicitly enabled for the relevant Ouros region/content.
- Official Mega Evolutions or other official gimmick forms only when the active Ouros rules profile supports them.

### Exceptional approval required

The following must never pass an automatic importer or ordinary proposal pipeline:

- Fakemon.
- Unofficial regional forms.
- Type Sync/TOSIKI or equivalent unofficial species/type conversions.
- Custom Mega forms or custom evolution lines.
- Unofficial species stat/type/Ability/evolution/learnset mutations.
- Any campaign-specific form treated as though it were an official Pokédex entry.

These require explicit `OUROS-APPROVED` authorization from the project itself. Source provenance, community popularity or presence in Caelo/Kairos is not authorization.

### Fusion prohibition

Pokémon fusions are prohibited by default.

No content-generation system, source importer, quest generator, Pokédex importer, encounter generator or NPC-team generator may create or import a fusion.

Before any individual fusion could be considered, the Ouros project would first need an explicit project-level decision reversing this prohibition. Ordinary canon approval is not sufficient.

## Import validation

Every species/form record imported from external material must include at minimum:

```text
species_id
form_id
official_status
source
source_version
ouros_authorization
mechanical_profile_source
visual_asset_source
```

Required gate:

```text
if official_status == OFFICIAL:
    require Ouros regional/content enablement
else:
    require exceptional OUROS-APPROVED authorization

if content_type == FUSION:
    reject unless project-level fusion prohibition has been explicitly reversed
```

Never allow a regional Pokédex import to bypass this gate.

## Source-specific interpretation

### Caelo

Use as evidence for a functioning PTU living world, campaign operations, encounter structures, missions, services, travel, progression and other systems. Caelo-specific rules remain Caelo rules unless Ouros explicitly adopts them.

### Kairos

Use as evidence for large-scale living-world operations and alternative PTU mechanics. High-value reference areas include downtime, open-ended player progression, real estate, hunting, prestige, classes, crafting, boss/encounter design, contests and post-cap play.

Kairos explicitly contains homebrew. Its custom species/forms, Type Sync/TOSIKI-style content and other custom gimmicks must not enter Ouros through ordinary source ingestion.

### Future sources

Treat future campaign rulesets identically: extract useful structures, diff mechanics, preserve provenance, and route every actual rule/content change through Ouros approval.
