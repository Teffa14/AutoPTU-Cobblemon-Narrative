# Multigeneration Commitment Lineage Scan — Pass 451

Status: RESEARCH / PROVENANCE ONLY. Not canon.
Date: 2026-09-12

## Repository inspection

The repository was inventoried recursively at `e89cf3992ee15d6734fd9cbe013c0c670121d30b` before writing. Relevant current contracts, tools, tests, proposals and research through Pass 450 were checked. Canon was read for constraints and left unchanged.

The existing assistance chain preserves an original accepted commitment, later renegotiation, a replacement commitment and checkpoint V6. The remaining structural risk is multigeneration lineage: future replacement-of-replacement records need one query model that cannot branch, cycle, orphan a child or reactivate an ancestor schedule.

## New public research anchors

### Tales of Visiwa retrospective — Pokémon Tabletop United

Source: Pokémon Tabletop RPG, “Tales of Visiwa: A Retrospective”
https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

Reusable observations:

- a long-running PTU campaign can let character history, personal obligations and earlier choices remain relevant far beyond the scene where they began;
- non-combat decisions can materially reshape later confrontations;
- environmental terrain can carry tactical meaning while dialogue or persuasion can still redirect a confrontation;
- the retrospective explicitly notes substantial GM-side preparation/crunch, supporting late binding of encounter detail instead of over-authoring every future tactical state.

Ouros transformation:

Keep historical commitments as queryable causal evidence while only one current generation controls execution. Build the actual encounter from current world state. Do not copy Visiwa factions, characters, gods, regional history, dialogue, special Pokémon, set pieces or plot.

### Battle Brothers contract structure

Source: public Battle Brothers contract documentation
https://battlebrothers.fandom.com/wiki/Contracts
https://battlebrothers.fandom.com/wiki/Factions_and_Relations

Reusable observations:

- contracts separate offer/acceptance from later completion, poor completion, failure and cancellation;
- world conditions and settlement state can change as a consequence of contract outcomes;
- negotiation itself can affect later social state independently from the eventual mission result;
- the same broad objective type can resolve differently because intervening events alter the route, opposition or local situation.

Ouros transformation:

Preserve negotiation history and later execution outcome as separate facts. Do not import Battle Brothers factions, economy, reputation numbers, enemies, contract text or event plots.

### Wildermyth Legacy and opportunity structure

Sources:
https://wildermyth.com/wiki/Legacy
https://wildermyth.com/wiki/Opportunity

Reusable observations:

- long-lived history can remain queryable while later campaigns or opportunities consume only selected durable aspects;
- optional opportunities are gated by current relationships and timing rather than appearing as timeless obligations;
- persistent history does not require every old state to remain currently active.

Ouros transformation:

Treat the assistance lineage as durable history with a single active leaf. Historical generations remain evidence but must not return to the active agenda merely because a checkpoint or later system queries them. Do not import Wildermyth characters, campaigns, transformations, hooks or prose.

### PTU campaign-log ecological encounter

Source: public Pokémon Tabletop campaign log #24
https://www.reddit.com/r/PokemonTabletop/comments/wudfhz/

Reusable observation:

A travel segment changed because the group disturbed a local ecological situation; communication/observation allowed a non-combat resolution. The useful pattern is route-state reactivity: a scheduled destination does not imply a frozen journey or mandatory battle.

Ouros transformation:

A repeatedly rescheduled field visit can encounter changed Pokémon behavior, access conditions or environmental evidence on the latest date. The premise can remain intact even when tactical content is reduced or omitted. No characters, dialogue, species arrangement or plot sequence is copied.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing/reference surface, not automatic Ouros authority. PTU/Kairos references to travel, terrain, statuses, hazards, weather, encounters, rivals, bosses or Trainer Features do not prove engine support. No adopted Caelo-specific mechanic was found that changes the assistance-lineage ownership boundary.

The narrative history layer therefore remains mechanic-neutral. Any later structured encounter must use current AutoPTU admission evidence and the permanent capability taxonomy.

## Live engine evidence

Read-only AutoPTU-Java head inspected: `1ff22f2bb1495527ca6aea08d40ce87f38f4a9d5`, merge PR #452. It provides server-authoritative guarded dispatch for specific switch-trigger behavior. That is narrow evidence and does not establish complete action economy, generic reactions/interrupts or Trainer Features/perks as full families.

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The latest commit is presentation-only and explicitly does not change battle rules or outcomes.

Current conservative posture:

- targeting/footprints/range/LoS: VERIFIED only within audited scopes;
- base movement legality: VERIFIED only within audited scopes;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED only within audited scopes;
- action economy/initiative: PARTIAL at family level despite narrow verified paths;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact behavior;
- move-specific behavior: individually gated;
- abilities: PARTIAL and individually gated;
- items: individually gated;
- Trainer Features/perks: individually gated;
- AI legal-action infrastructure: specialized objective verbs require explicit admission;
- AI tactical policy: BLOCKING for unsupported specialized objective policies;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

## Design conclusion

The safe next foundation is a generation-neutral assistance lineage view. It should preserve all accepted historical generations, expose one latest leaf, reject cycles/branches/orphans and optionally verify that only that leaf remains executable. It must remain outside tactical execution and outside social/accountability judgment.