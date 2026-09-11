# Overlapping Stewardship and Hidden-Route Scan — Pass 415

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-10
Canon effect: NONE

## Repository inspection and duplicate filter

The recursive repository tree at narrative head `ffa677899c1d93dda8851d733b910da81632df6e` was inventoried before writing. `CURRENT_FOCUS.md`, canon governance, the fixed Marea resident/location network, Pass 411–414 AutoPTU session/recovery contracts, current global-NPC implementation seams and recent research/proposal entries were checked before selecting this slice.

Searches rejected resurfaced material already present in the corpus, including Pokémon Rainbow Wing. The two primary public fangame references below returned no prior repository matches under their titles when selected.

## Source 1 — Pokémon Hollow Woods

Public source: A Start Gaming project page for Pokémon Hollow Woods, updated March 14, 2026.
URL: https://www.astartgaming.com/2024/05/pokemon-hollow-woods-rpgxp.html

Publicly described structure:

The region is divided between two factions. The protagonist is initially tasked with researching local Pokémon, while the larger story accumulates historical claims, organizational motives and mysteries centered on a major forest.

Reusable Ouros lesson:

A single place can be important to several institutions for different reasons. Research, access, stewardship, history and public safety can overlap without requiring one institution to own the whole truth. Different actors may possess different records and motives while still referring to the same physical place.

Not imported:

Oblar, the Lavender Faction, the second faction, the protagonist's mother, the ancient Pokémon, the Great Forest, characters, plot, dialogue, species placement or organization identity.

## Source 2 — Pokémon Lithic Veil

Public source: official itch.io page by Khydra.
URL: https://khydra98.itch.io/pokemon-lithic-veil

Publicly described structure:

The project uses point-and-click exploration, team management, automatic battles, hidden secrets and mysterious events across multiple regions.

Reusable Ouros lesson:

Exploration information can be surfaced through deliberate inspection rather than combat victory. A site may contain discoverable state that matters even when tactical resolution is absent or delegated. Narrative discovery therefore benefits from preserving the distinction between what exists at a location, what an actor has inspected, and what that actor can infer.

Not imported:

Point-and-click controls, automatic battle rules, Gym progression, regions, secrets, events, characters, teams or game-specific systems.

## Synthesis for Ouros

The combined pattern supports a shared-site investigation where several legitimate institutions have overlapping interests and incomplete information. The physical site exists independently of any quest giver. Each group can know a different subset of its history, maintenance state, access rules and ecological observations.

A player or persistent NPC can inspect one layer and report it. Another actor can later inspect a different layer. Their reports can disagree because of time, access, expertise or incomplete evidence rather than because one report is automatically false.

This pattern fits Ouros because current world-agent architecture already preserves private knowledge, provenance, communication, obligations, travel and site-level continuity without granting omniscient faction knowledge.

## PTU / Caelo / engine boundary

No PTU Skill DC, Move, Ability, Item, Trainer Feature, hazard, terrain rule or encounter outcome is inferred from these sources.

A reduced implementation can use semantic world state, authored inspectable evidence, permissions, travel, schedules, obligations, private knowledge and explicit communication only.

A mechanically rich implementation must expose dependencies explicitly:

- targeting/footprints/range/LoS: VERIFIED only in previously audited scopes;
- base movement legality: VERIFIED only in previously audited scopes;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED only in audited paths;
- action economy/initiative: PARTIAL;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact behavior;
- move-specific behavior: individually gated;
- abilities: PARTIAL and individually gated;
- items: individually gated;
- Trainer Features/perks: individually gated;
- AI legal-action infrastructure: VERIFIED only for ordinary audited scopes;
- AI tactical policy: BLOCKING for specialized inspect/protect/withdraw objective policy unless separately implemented;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative tactical objectives, non-KO completion and in-flight battle recovery.

Live AutoPTU-Java head inspected for this pass: `befea9488953a07e510b5ad9152abaa314ae1332`, PR #438. The change registers the parity-safe Ball Fetch post-entry handler in the production switch path. Other post-entry families remain pending. This narrow evidence does not promote complete movement, Abilities, action economy or lifecycle.

AutoPTU Python remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, whose latest commit is presentation-only.
