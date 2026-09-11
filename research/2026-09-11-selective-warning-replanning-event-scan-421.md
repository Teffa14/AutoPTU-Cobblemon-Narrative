# Selective warning replanning and relevant-actor event scan — Pass 421

Status: RESEARCH / PROVENANCE ONLY. Nothing in this note is canon.

## Repository-first deduplication

The recursive main-branch tree at `88c4c699f229fead12fad3c9fd9ba28ffcbada09` was inventoried before writing. Canon governance, the current Marea foundation, Pass 418–420 consequence/observation/delivery contracts, private information queues, world-event replanning, recent research/proposals and the Kairos/PTU source router were reviewed.

Previously processed anchors from recent passes were excluded, including Pokémon Space Pog Jam, Pokémon Memories, The Case of the Golden Idol, Pokémon Starwish, Pokémon Unchosen, Outer Wilds, Pokémon Shadowside, Pokémon Hollow Woods, Pokémon Lithic Veil, Lethalmon, Pokémon Knowledge, Pokémon Crystal Inheritance, Pokémon Rollout!, Pokémon Diadem and The Roaring Trainers.

Repository search found no prior use of `Aipom's Great Pirate Adventure` and no prior use of the paper `Event-Driven Storytelling with Multiple Lifelike Humans in a 3D Scene` under those titles.

## New source: Aipom's Great Pirate Adventure

Public source: Eevee Expo project thread by PikachuMazzinga, published August 11, 2026.

https://eeveeexpo.com/threads/9673/

Observed high-level structure:

The public project description frames the game around building a crew by finding and recruiting a large cast and combining those recruits with a large relic pool before facing major opponents. The useful design lesson is not the pirate fiction or combat system. It is that the composition available for an objective can be a meaningful state variable rather than a fixed party assumed by the quest text.

Ouros-safe abstraction:

A delivered field warning can change who is considered appropriate or available for the next assignment. The report does not need to cancel the assignment globally. One recipient may delay, seek another specialist, request equipment, choose another route or continue because a harder obligation outranks the warning.

Do not import the game's characters, pirate setting, treasure, relics, encounter roster, foes, plot, dialogue, UI or auto-chess mechanics.

## New source: Event-Driven Storytelling with Multiple Lifelike Humans in a 3D Scene

Public source: Donggeun Lim, Jinseok Bae, Inwoo Hwang, Seungmin Lee, Hwanhee Lee and Young Min Kim, arXiv:2507.19232, first submitted July 25, 2025.

https://arxiv.org/abs/2507.19232

Observed high-level structure:

The paper decomposes a changing multi-character scene into a temporal sequence of smaller events. Each event concerns the relevant characters and objects rather than forcing the whole scene population to react as one synchronized unit.

Ouros-safe abstraction:

A world event should wake the actors whose state actually changed or whose information was delivered. The event can then produce a local decision that becomes new world state. Other agents keep their prior schedules until they receive their own trigger, observe the consequence, or are contacted through an explicit channel.

The paper is used only as a structural reference for event scope and temporal decomposition. No generated motions, benchmark scenes, prompts, characters or implementation details are copied.

## Combined design lesson

The two sources support a selective-response pattern:

1. A field fact becomes a durable observation.
2. A concrete report reaches one actor.
3. That actor reassesses the next assignment using their own goals, obligations, permissions, location and knowledge.
4. The resulting change may alter departure time, route, requested support or team composition.
5. Other actors remain unchanged until another world event legitimately reaches them.

This preserves causal legibility. The player can later reconstruct why two people from the same institution made different decisions without requiring hidden global quest flags or omniscient faction knowledge.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` routes questions involving Trainer capabilities, combat, movement/terrain, status, hazards/weather, encounter creation, bosses and Items to the supplied source material. It also documents living-world play, one-shot quests, downtime and persistent player-created teams/factions.

Those references are routing evidence only. This pass introduces no new PTU/Caelo mechanic and does not infer that a world-agent replan can execute a tactical action.

If a replanned objective requires structured combat, the normal AutoPTU handoff remains mandatory.

## Capability impact

No permanent battle capability family is promoted by this research.

Targeting/footprints/range/LoS remains VERIFIED only in audited scopes. Base movement legality remains VERIFIED only in audited scopes. Complete movement including push/pull/knockback/interception/forced movement remains PARTIAL. Core calculations remain VERIFIED only in audited paths. Action economy/initiative remains PARTIAL. Full turn/round lifecycle, full stateful damage pipeline and status lifecycle remain PARTIAL. Terrain/weather/hazards/zones/reactions remains MIXED/PARTIAL/BLOCKING by exact behavior. Move-specific behavior, Items and Trainer Features/perks remain individually gated. Abilities remain PARTIAL and individually gated. AI legal-action infrastructure remains VERIFIED only for audited ordinary actions. AI tactical policy remains BLOCKING for specialized warning-aware rescue, escort, extraction and objective-aware withdrawal unless implemented. Minecraft/Cobblemon/Craftics adapter/playback remains PARTIAL/BLOCKING for authoritative tactical objective state and in-flight battle recovery.

## Candidate unlocked by the scan

See `proposals/2026-09-11-the-warning-changes-one-assignment-421.md`.
