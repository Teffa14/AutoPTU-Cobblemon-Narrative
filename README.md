# AutoPTU-Cobblemon-Narrative

Narrative and world-state design repository for the Ouros AutoPTU + Cobblemon project.

The long-term goal is a persistent Pokémon world where player decisions, battles, discoveries, relationships, faction activity, ecological knowledge, settlement changes and environmental changes can become durable world state. Minecraft/Cobblemon provides the explorable overworld; AutoPTU provides the tactical grid-battle rules engine.

## Repository layers

- `research/`: external-source research and provenance. Nothing here is automatically canon.
- `design/`: narrative architecture, schemas and implementation-facing design.
- `proposals/`: original Ouros worldbuilding, quest, faction, NPC, dungeon, encounter and story-arc candidates. Explicitly non-canon until reviewed.
- future `canon/`: only reviewed material promoted after originality, continuity, PTU/Caelo rules and implementation review.

## Current foundation

### Research
- [Narrative research scan — pass 01](research/2026-08-18-source-scan.md)
- [Mission, dungeon & RP research — pass 02](research/2026-08-18-missions-dungeons-rp-scan-02.md)
- [Factions, fields, bonds & investigation research — pass 03](research/2026-08-18-factions-fields-bonds-scan-03.md)
- [Observation, settlement & time research — pass 04](research/2026-08-18-observation-settlement-time-scan-04.md)

### Systems design
- [Ouros narrative architecture](design/ouros-narrative-architecture.md)
- [Mission & dungeon grammar](design/mission-dungeon-grammar.md)
- [World agency layer](design/world-agency-layer.md)
- [Observation, settlement & time layer](design/observation-settlement-time-layer.md)

### Non-canon Ouros candidates
- [First worldbuilding seeds](proposals/2026-08-18-worldbuilding-seeds.md)
- [Adventure seeds — pass 02](proposals/2026-08-18-adventure-seeds-02.md)
- [World agency seeds — pass 03](proposals/2026-08-18-world-agency-seeds-03.md)
- [Observation & settlement seeds — pass 04](proposals/2026-08-18-observation-settlement-seeds-04.md)

## Mechanical source priority

Narrative proposals must not invent combat legality. When mechanics are required, validate against the project's supplied PTU/Caelo source set, including the PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List, plus the actual AutoPTU implementation state.

External stories are inspiration sources, not rules sources.

## Generation rule

Research may propose structures and original candidates, but generated objectives should be traceable to current world facts, actor motives, ecological state, player history or executable game mechanics. Material should not enter future `canon/` until reviewed.
