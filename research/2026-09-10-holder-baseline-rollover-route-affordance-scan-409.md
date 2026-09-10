# Holder Baseline Rollover and Route Affordance Scan — Pass 409

Status: RESEARCH / PROVENANCE ONLY
Canon authority: NONE
Date: 2026-09-10

## Repository inspection and duplicate control

The complete recursive repository tree at narrative head `90e96c6e06f7c37e81ba2f4f464bade132495b9e` was inventoried before writing. Current focus, canon governance, all tracked canon paths, source-authority policy, the current holder-history/recovery chain, Passes 399–408, recent proposals, tests, tools and the PTU/Caelo/Kairos routing material were checked before selecting this slice.

Repository-wide source searches were used to avoid repeating already processed material. The Reckless Rollers, Pokémon Adventures in the Millennium, Pokémon Tectonic, Monomyth, Nova, Crossroads, Stalactite, Burning Scales and other recurring sources were deliberately not treated as new research.

The exact `Pokémon: A Farfetch'd Story 2` Eevee Expo page and `A Short Hike` postmortem/interview material used below had no prior processed-source match in the research corpus.

## Internal technical finding

Pass 408 can recover an older holder-history baseline selected by Recovery Manifest V4, replay later holder transitions, validate the current WorldResource catalog and then issue a new same-cut baseline for future generations.

The missing operational seam is generation advancement. A certificate issued after safe recovery at T must be persistable into a later baseline-owner checkpoint at T+N without changing the certificate's own `at_tick`. Otherwise persistence could accidentally make an old holder fact look like a new holder fact.

Pass 409 therefore adds a rollover helper that carries only baselines emitted by a safe post-restore validation. The owner checkpoint may be written at a later semantic minute, but every certificate preserves the cut at which its holder was actually established. The next recovery must still replay all holder transitions after that original cut.

The new regression exercises two consecutive advancements. A baseline at T=10 proves holder A. A handoff at 15 leads to a safe recovery at 20 and a fresh baseline for holder B. That new certificate is carried into a checkpoint for 40, a later handoff at 30 is replayed, and recovery at 40 issues a new baseline for holder C. A discontinuous journal fails closed.

## New source 1 — Pokémon: A Farfetch'd Story 2

Public project page:
https://eeveeexpo.com/a-farfetchd-story-2/

Published: 2026-06-19.
Inspected: 2026-09-10.

The public description presents a story-driven Pokémon adventure with exploration and puzzles, no ordinary wild encounters, and an overworld-switching system where different party Pokémon have field abilities.

Reusable high-level structures for Ouros:

- exploration can give party composition meaning outside battle;
- a companion can reveal a different way to interact with a place rather than merely adding combat power;
- environmental problems can be full encounters without requiring a wild battle;
- multiple useful field roles make a group feel operationally different from a single avatar with a universal interaction button.

Transformation boundary:

Do not import Farrow, Farley, the Golden Leek, the story premise, puzzles, field abilities, maps, dialogue, party structure or specific encounter content. Ouros uses only the abstract lesson that different companions can change perceived or available environmental affordances.

No external field ability becomes an Ouros mechanic through this note. Any Pokémon Move, Ability, Item or Trainer Feature used for traversal must be verified against the active Ouros rules profile and admitted by the relevant engine capability family.

## New source 2 — A Short Hike exploration design

Public postmortem index:
https://gamedesign.gg/watch/a-short-hike-postmortem/

Creator interview:
https://canadiangamedevs.com/features/interview-with-a-short-hike-creator-adam-robinson-yu

Inspected: 2026-09-10.

The public design material describes a compact open world built around dense landmarks, flexible goals and exploration that is guided through curiosity rather than a single mandatory path. The creator also describes influences centered on hiking and relaxed discovery.

Reusable design lessons for Ouros:

- a physically small route network can feel open when several landmarks continuously suggest plausible next destinations;
- optional activities can sit directly on traversal paths instead of living in separate quest corridors;
- route guidance can come from readable world geometry, signs, local knowledge and visible landmarks rather than omniscient objective arrows;
- an alternate path is more valuable when it creates a different observation, contact or logistical consequence rather than only shortening travel time;
- not every discoverable detail has to be guaranteed to every player or NPC.

Transformation boundary:

Do not import Hawk Peak, characters, Golden Feathers, shovel/fishing activities, map geometry, dialogue, progression objects or specific secrets. Ouros uses the general design lesson of dense landmarks, flexible traversal goals and optional discoveries embedded in a compact route network.

## Ouros synthesis

The two sources support an original exploration pattern where route choice depends on the actual traveling party and its knowledge rather than on a universal player power.

A compact route knot can have several legitimate ways around the same obstacle. One route may be public and slow. Another may require permission or a work relationship. A third may only be considered by an actor who knows a local path, understands a landmark, possesses suitable ordinary equipment or is accompanied by someone with relevant demonstrated capability.

The world service must not select the "best" route from hidden global knowledge. An actor can consider only routes they know or can infer from evidence available to them. A route learned by one NPC remains private until communicated, observed or recorded through an existing information channel.

Different paths should create different side effects in world state: arrival time, who was encountered, what was observed, which institution noticed the group, what resource was used, or which later shortcut became known. These consequences make traversal narrative content instead of a loading screen.

The resulting companion proposal is `proposals/2026-09-10-path-depends-on-company-seed-409.md`.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing aid, not Ouros rules authority. Potentially relevant source families include Skills/Edges/Features, Survivalist, Topographer, Backpacker, movement/terrain, mounts, hazards, terrain/weather, encounter construction and Items/Gear.

This research does not create a Survivalist shortcut, Topographer bonus, climbing permission, Pokémon field action, Move effect, Ability traversal effect, Item function, Trainer Feature or special movement rule. Those require exact source-level review and engine admission.

Caelo and Kairos remain comparative living-world references under `design/ouros-source-authority-and-species-policy.md`; source presence does not activate a rule.

## Engine capability posture for the derived route concept

Targeting/footprints/range/LoS: VERIFIED only inside audited scopes. Relevant only if a route becomes a tactical encounter with spatial targeting.

Base movement legality: VERIFIED only inside audited scopes. The reduced route version can stay on ordinary world navigation and already admitted travel abstractions; tactical grid traversal must remain within demonstrated Shift legality.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Any shove across a ledge, rescue reposition, forced slide, interception or knockback requires this family.

Core calculations: VERIFIED only inside audited scopes.

Action economy/initiative: PARTIAL as a complete family. A field interaction performed inside structured combat cannot assume free timing.

Full turn/round lifecycle: PARTIAL. Timed gates, collapsing passages, delayed environmental changes or extraction clocks require this family.

Full stateful damage pipeline: PARTIAL. Persistent injuries or damage caused by route hazards cannot be authored by the narrative layer.

Status lifecycle: PARTIAL. Ongoing traversal conditions remain gated.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism. Slippery ground, active weather, triggered debris, visibility zones, reaction hazards and similar mechanics require direct verification.

Move-specific behavior: individually gated. A route unlocked through a specific Move requires that Move's authoritative implementation.

Abilities: PARTIAL / individually gated. AutoPTU-Java now has narrow oracle-backed approach-Shift Ability behavior and temporary-effect materialization; this does not establish generic field traversal abilities.

Items: individually gated. Equipment may exist narratively only within established world-resource semantics unless a PTU Item effect is verified.

Trainer Features/perks: individually gated. No class or Feature receives route authority from this research.

AI legal-action infrastructure: VERIFIED only for audited ordinary legal-action scopes. Specialized climb, manipulate-obstacle, carry, rescue or field-ability actions need explicit legal-action admission if made tactical.

AI tactical policy: BLOCKING for route-objective reasoning such as bypass-first, escort-first, rescue-first, preserve-equipment, objective-aware withdrawal and disengage-after-objective.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative route-affordance projection, persistent interactable state, companion-specific environmental actions and non-KO objective completion.

## Reduced implementation version

The reduced version needs no new PTU battle rule. Route availability is driven by already persistent facts such as actor knowledge, permissions, schedules, ordinary world resources, current location and communicated information. Travel can resolve through the existing world-agent travel abstraction. Environmental changes happen between persistent world revisions.

This preserves the narrative premise: who travels with you and what the group actually knows changes which path is considered.

## Full implementation version

A later mechanically rich version may let verified Pokémon Moves, Abilities, Items or Trainer Features create route affordances, and may place traversal under tactical pressure. Every such affordance must declare the exact capability family that owns it. Minecraft may present the interaction but must not implement a parallel substitute for missing PTU rules.

## Read-only engine evidence

AutoPTU-Java live head inspected during this pass: `70b20f502e34c4d3a3130a6a661476858330543e`, merge PR #433, `Materialize generic approach Shift ability effects`, dated 2026-09-10.

The change adds `AbilityApproachShiftEffectExecutor`. It delegates movement to the existing Ability approach-Shift executor, writes a named temporary effect to each holder that successfully shifts, and returns a semantic effect descriptor. The oracle parity test for Ball Fetch now checks target/Ability identity, movement results and the temporary marker.

This strengthens one narrow combination of Ability-triggered legal approach movement plus a stateful temporary marker. It does not complete Abilities, complete movement, push/pull, knockback, interception, forced movement, action economy, initiative, full lifecycle, status lifecycle, hazards/zones/reactions, Trainer Features or AI tactical policy.

AutoPTU Python live head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit remains presentation-only viewport coordinate synchronization and explicitly does not alter battle rules or outcomes.
