# V4 Baseline Reconciliation and Curiosity Puzzle Network Scan — Pass 408

Status: RESEARCH / PROVENANCE ONLY
Canon authority: NONE
Date: 2026-09-10

## Repository inspection and duplicate control

The complete recursive repository tree at narrative head `018ebe5e9e097c12040c6ab11bf7fe5191b8a263` was inventoried before writing. Current focus, all files under `canon/`, recovery manifests/checkpoints, holder-history coverage, holder-transition reconciliation, recent research/proposals and the PTU/Caelo/Kairos routing material were reviewed before selecting this slice.

The current research corpus is already extensive. Repeated sources were deliberately excluded. Pokémon Tectonic, Pokémon Monomyth, Pokémon Nova, Pokémon Crossroads, Pokémon Pokopia, Pokémon Stalactite, Pokémon Adventures in the Millennium, Pokémon Rollout! and other frequently resurfacing projects were not reprocessed as new evidence.

A repository search found no prior processed reference for the Pokémon Sky Blue project page used below. The GDC Relic Ruins session was also selected as a new design anchor rather than reusing already-cited dungeon references.

## Internal technical finding

`OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V4` already selects a fifth owner: `OUROS_HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_V1`. Before this pass, post-restore validation did not consume that selected owner.

The integration has an important temporal constraint. A baseline issued from the WorldResource catalog at semantic minute T cannot be used to prove that same catalog at T. Only a baseline strictly earlier than a later recovery cut can provide bounded historical proof, after replaying all holder transitions following its own cut.

Pass 408 therefore restores the exact V4-selected baseline checkpoint, verifies its manifest-selected digest, and admits only baseline records whose `at_tick` is strictly earlier than the current recovery minute. Same-cut certificates remain future-facing evidence.

## New source 1 — Pokémon Sky Blue

Public project index:
https://pokehackzone.com/hacks/pokemon-sky-blue

Inspected: 2026-09-10.

The public project page describes a GBA ROM hack that combines material from canceled fangame regions into an open-world adventure with many distinct explorable sub-worlds and dynamic level scaling.

Reusable high-level structures for Ouros:

- a broader exploration network can consist of locally self-contained spaces rather than one linear dungeon chain;
- access order can vary while each site still preserves its own observations and consequences;
- older or abandoned places can gain new relevance when later evidence gives players a reason to reinterpret them;
- exploration rewards can be information and changed understanding instead of only combat progression or loot.

Transformation boundary:

Do not import the project's characters, relationships, star-fragment premise, Distortion World story, Forgotten Worlds identity, Fakemon, maps, dialogue, events or plot. Ouros uses only the abstract structure of independently explorable spaces whose meaning can change when information from another site becomes available.

## New source 2 — GDC 2024, Relic Ruins environmental-puzzle design

GDC Vault session:
https://www.gdcvault.com/play/1034875/Relic-Ruins-Creating-Environmental-Puzzles

Speaker: Daniel Wewerinke, Guerrilla.
Inspected: 2026-09-10.

The session overview describes environmental puzzle spaces developed through concept work, block-outs, interdisciplinary iteration and playtesting inside a large open world. The stated design goal is to create interesting, distinct and surprising puzzle spaces.

Reusable design lessons for Ouros:

- an exploration room should communicate a concrete environmental question rather than exist only as scenery around combat;
- puzzle spaces benefit from readable physical evidence and iterative validation;
- multiple sites can teach related spatial conventions without requiring one scripted order;
- a room can have a complete exploration purpose even when no battle occurs;
- environmental interaction should remain separate from tactical rules unless the engine explicitly owns those mechanics.

Transformation boundary:

Do not import Horizon locations, machines, traversal tools, puzzle solutions, ruin layouts, story context or proprietary level content. Ouros uses only the general process lesson: build compact environmental questions, make evidence readable and playtest the inference path.

## Ouros synthesis

The two sources support an original pattern suitable for the existing Ouros graph: several small survey-era spaces can be discovered independently, while observations from one change how another is interpreted. This can create curiosity-driven exploration without a magical key chain or mandatory combat progression.

The canonical Tideglass Archive already preserves route surveys, old market records and ecological observations. Sendero del Vidrio is already a canonical old survey road. These facts provide existing graph edges for a proposal, but no hidden chamber, survey recess, abandoned facility or puzzle site is canonized by this research note.

A useful implementation pattern is:

`ARCHIVE OR FIELD CLUE -> CANDIDATE SITE -> LOCAL OBSERVATION -> PRIVATE KNOWLEDGE -> OPTIONAL CROSS-SITE REINTERPRETATION -> NEW INVESTIGATION QUESTION`

The player may discover sites in different orders. Persistent NPCs may also inspect them off-screen if their schedules, knowledge and obligations support doing so. A site nobody visits produces no retrospective observation.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing aid rather than rules authority. Relevant source families include Skills/Edges/Features, Researcher, Chronicler, Librarian, Paleontologist, Survivalist, Topographer, movement/terrain, hazards, terrain/weather, encounter creation, bosses and Items/Gear.

This scan does not create a Topographer bonus, Researcher check, climbing rule, puzzle Skill DC, hazard, weather effect, Item function, Ability interaction, Trainer Feature interrupt or movement permission. Any such mechanic requires source-level verification and engine admission.

## Engine capability posture for the derived exploration concept

Targeting/footprints/range/LoS: VERIFIED only inside audited scopes. A spatial combat variant may use only those demonstrated contracts.

Base movement legality: VERIFIED only inside audited scopes. Ordinary legal Shift evidence exists; that does not establish all traversal behavior.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Any collapsing floor displacement, rescue reposition, forced slide, interception or knockback remains dependent on this family.

Core calculations: VERIFIED only inside audited scopes.

Action economy/initiative: PARTIAL as a complete family.

Full turn/round lifecycle: PARTIAL. Timed puzzle windows, phased collapse, delayed opening/closing or round-based extraction need this family.

Full stateful damage pipeline: PARTIAL. Persistent damage or injury consequences cannot be assumed from a scene description.

Status lifecycle: PARTIAL. Complex ongoing conditions remain gated.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact behavior. Reactive debris, unstable floors, active flooding, visibility changes, weather phases and triggered zones require direct verification.

Move-specific behavior: individually gated.

Abilities: individually gated and PARTIAL as a family. AutoPTU-Java now has a narrow oracle-backed generic ability approach-Shift executor demonstrated with Ball Fetch. That verifies only that specific ability-triggered approach seam and does not establish general Ability coverage or complete movement.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for previously audited ordinary legal-action scopes. Puzzle-object interaction and specialized rescue/traversal actions need explicit admission if they become tactical actions.

AI tactical policy: BLOCKING for investigate-first, preserve-evidence, solve-before-engage, protect-observer, rescue-first, objective-aware withdrawal and disengage-after-objective policy.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for persistent environmental puzzle state, authoritative clue interaction, site revision projection and non-KO objective completion.

## Read-only engine evidence

AutoPTU-Java live head inspected during this pass: `52439df965145702ddbd5f4a3a65857ea1080918`, merge PR #431, `Add generic ability approach Shift execution`.

The change adds a server-owned `AbilityApproachShiftExecutor`. Effective Ability holders are resolved in active battle state. Movement destination selection remains delegated to the canonical legal Shift resolver. An oracle parity test demonstrates sequential Ball Fetch holder movement against the pinned Python behavior.

This strengthens one narrow combination of Ability selection and legal approach Shift. It does not complete Abilities, complete movement, forced movement, action economy, initiative, lifecycle, hazards, Trainer Features or tactical policy.

AutoPTU Python live head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit is presentation-only viewport coordinate synchronization and explicitly does not alter battle rules or outcomes.

## Resulting proposal direction

The companion proposal for this scan is `proposals/2026-09-10-survey-recess-network-seed-408.md`.

It remains PROPOSED / NON-CANON. The reduced version uses persistent-world evidence, archive lookup, semantic travel and private knowledge only. The rich version declares every battle/environment dependency explicitly rather than making the Minecraft adapter reproduce missing PTU behavior.
