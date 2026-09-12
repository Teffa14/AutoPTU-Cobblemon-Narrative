# Active Replacement Start Research — Pass 453

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Date: 2026-09-12
Narrative baseline inspected before writing: `a1a43a960e73fa13adbec4a7de20a0a1607d5c11`.

The repository tree was inventoried recursively before writing. Current focus, canon, assistance lineage/renegotiation owners, viability, start/disposition owners, checkpoints, recent research/proposals and tests were checked first. Existing anchors repeatedly used in recent passes were not selected again.

## New public source: Pokémon Ranger: Shadows of Almia mission structure

Public walkthrough material for Mission 3 describes a forest emergency that changes local traversal and requires several distinct interventions: move through a hazardous environment, calm or collect affected Pokémon, use locally available Pokémon capabilities to clear obstacles, then address the larger fire. The broader Ranger mission list also includes investigation, delivery, rescue and recovery missions without requiring a boss in every case.

Reusable structure for Ouros:

A scheduled obligation can reach its start while the location itself has changed. The first meaningful fact is therefore not automatically “combat begins.” It can be “the agreed work window opened while access is still unsafe.” World evidence can then lead to observation, help-seeking, alternative access, postponement or a later structured scene.

Transformation boundary: no Ranger characters, regions, dialogue, mission text, device mechanics or exact set pieces are imported.

Sources:
- Bulbapedia, `Walkthrough: Pokémon Ranger: Shadows of Almia/Part 3`, accessed 2026-09-12.
- Bulbapedia, `Ranger Mission`, accessed 2026-09-12.

## New public source: Pentiment

Obsidian's public description emphasizes investigation inside a community where decisions have lasting consequences. The useful abstraction is persistence of prior choices while later circumstances continue changing.

Reusable structure for Ouros:

A replacement appointment should inherit historical context without causing the original agreement to remain executable. When the new window begins, the current condition of the world must be evaluated separately from the historical reason the appointment exists.

Transformation boundary: no characters, murder plots, historical setting, dialogue or distinctive story events are imported.

Source:
- Obsidian Entertainment, `Pentiment`, accessed 2026-09-12.

## New PTU community evidence: campaign log #25

A public PTU campaign log describes a group skipping a repeated gym battle after a prior long attempt because repeating the same structured encounter was judged unhelpful. The point is not the retcon itself; the useful design lesson is that structured combat has a real pacing cost and should not be the automatic resolution for every persistent objective.

Reusable structure for Ouros:

If an obligation has already been delayed or renegotiated, the eventual start should first inspect present viability and narrative purpose. A later battle should exist only when current world state and admitted capabilities justify one.

Transformation boundary: no campaign characters, gym content, teams, rewards or plot events are imported.

Source:
- r/PokemonTabletop, `campaign log #25`, 2022-10-02, accessed 2026-09-12.

## PTU/Caelo and engine boundary

This research does not establish PTU rules. PTU/Caelo references remain comparative inputs subject to project contracts.

Live read-only engine evidence checked 2026-09-12:
- AutoPTU-Java `23e747c504a2253d8ce05eebef76ad0dc99b33ce` adds explicit Quick Switch interrupt response and replacement-choice semantics. This verifies that narrow Quick Switch path only. It does not promote generic reactions, action economy or Trainer Features/perks as complete families.
- AutoPTU Python `729bae2d424963ff9bb3f4159c9a7ac9152128a7` remains presentation-only and explicitly changes no battle rules or outcomes.

Capability posture remains conservative: targeting/footprints/range/LoS, base movement legality and core calculations are VERIFIED only in audited scopes; complete movement is PARTIAL; action economy/initiative, full turn/round lifecycle, full stateful damage pipeline and status lifecycle remain PARTIAL; terrain/weather/hazards/zones/reactions remains MIXED/PARTIAL/BLOCKING by behavior; move-specific behavior, abilities, items and Trainer Features/perks remain individually gated; specialized objective verbs require explicit AI legal-action admission; AI tactical policy remains blocking for unadmitted specialized objectives; Minecraft/Cobblemon/Craftics adapter/playback remains partial/blocking for specialized objective state, non-KO completion and interrupted structured-scene recovery.
