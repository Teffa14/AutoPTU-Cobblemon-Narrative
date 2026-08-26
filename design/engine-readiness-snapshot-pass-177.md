# Engine Readiness Snapshot — Pass 177

Status: IMPLEMENTATION EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-26

## Pass scope and authority correction

Pass 177 adds multimodal biological orientation and homing assessments. It does not create magnetic-field or magnetic-navigation state. Full-tree comparison during the run surfaced the existing Pass 81 `geomagnetism-magnetic-navigation-interference-layer.md`; all magnetic field revisions, anomaly state, interference incidents, magnetic navigation profiles and magnetic Pokémon observations remain owned there.

Pass 177 consumes Pass 81 references alongside Olfactory Landscapes, Light/Astronomy, Soundscapes, Wayfinding, Telemetry, Wildlife Migration, Pokémon Spatial Ecology and Pokémon Agency.

## Live read-only engine evidence

AutoPTU-Java head inspected for this snapshot:

`a9fb0d81238e69a5263f074b4a8ad8ef1905325d` — `Route seven Combat Stages through authoritative hooks (#215)`.

Recent Java evidence includes canonical storage and authoritative mutation/hook routing for all seven Combat Stages, including Accuracy and Evasion, plus secondary Combat Stage application and Mirror Armor coverage. This is meaningful evidence for a defined Combat Stage slice. It does not complete the full Ability catalog, Move-specific catalog, Status controller, damage pipeline, reaction family or world-navigation logic.

The current Java README still explicitly leaves the following major areas incomplete: core combatant/grid battle state, full damage resolution, status controller, terrain, hazards, forced movement, reactions, remaining hook registries, full transcript parity, AI scoring/policy and Craftics/Cobblemon integration.

AutoPTU Python head inspected for this snapshot:

`44305a1b3f06a45fbd06392a64573f287ac31555` — `Career: preserve sponsor renewal memory across name drift (#139)`.

That Python change is Career presentation/persistence work and explicitly preserves battle behavior, so it does not alter the battle-readiness classification below.

Search of AutoPTU source material confirms Nosepass/Probopass and `Magnet Pull` material exist in the imported corpus. AutoPTU-Java search did not expose a generic homing, multimodal animal-navigation, route-memory or magnetoreception subsystem.

## Permanent capability map

| Capability family | Pass 177 status | Evidence boundary |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | Java README lists range, areas, footprints, target anchors and LoS as ported. Tactical LoS is not biological navigation visibility. |
| base movement legality | VERIFIED | Shift/jump legality and movement-medium boundaries are ported. This does not imply route knowledge or homing. |
| complete movement including push/pull/knockback/interception/forced movement | BLOCKING | README still lists forced movement/reaction family incomplete; no generic crossing/escort/interception objective system is proven. |
| core calculations | VERIFIED | Core PTU tables, stages, accuracy primitives and other calculation primitives are ported. |
| action economy/initiative | VERIFIED | Typed turn flow, action budget and deterministic initiative/declaration ordering are ported. |
| full turn/round lifecycle | PARTIAL | Multiple lifecycle slices exist, but the repository does not claim complete parity across all battle state and hooks. |
| full stateful damage pipeline | PARTIAL | README still lists full damage resolution as incomplete. |
| status lifecycle | PARTIAL | Secondary Status and prevention paths have concrete coverage, but the status controller remains explicitly incomplete. |
| terrain/weather/hazards/zones/reactions | BLOCKING | Several representative reaction paths exist, but README still lists terrain, hazards and reactions as incomplete. No orientation cue may be mapped to a tactical zone without an exact contract. |
| move-specific behavior | PARTIAL | Move-special bridges, secondary Status/Combat Stage work and effect-roll plumbing cover concrete slices, not the catalog. |
| abilities | PARTIAL | Mirror Armor and other representative Ability hooks have evidence; no full Ability registry parity claim exists. |
| items | PARTIAL | Item behavior is not complete as a family. |
| Trainer Features/perks | PARTIAL | Generic Feature infrastructure has prior slice evidence, but catalog/effect parity remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Java README lists deterministic legal `BattleChoice` action-space generation. |
| AI tactical policy | BLOCKING | README still lists scoring/policy over legal choices as future work. Non-KO homing/search/withdrawal goals therefore cannot be assumed. |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | Java is intentionally not yet a Minecraft mod; adapter work remains future work. |

No category is promoted in Pass 177.

## Orientation-specific implementation boundary

The new narrative layer introduces world-state concepts that do not exist as proven battle/runtime subsystems:

- `ORIENTATION_PROFILE`
- `NAVIGATION_GOAL_CONTEXT`
- `ORIENTATION_OBSERVATION`
- multimodal cue snapshots and assessments
- natural-return events
- Research-Ethics-gated homing trials
- cue-conflict cases
- orientation baseline revisions
- handoffs to/from Pass 81 geomagnetism, Migration, Spatial Ecology, Olfactory Landscapes, Telemetry, Light/Astronomy, Passive Acoustics and Minecraft presentation

These are overworld/Chronicle data contracts. AutoPTU should receive only an already-defined tactical snapshot when combat occurs.

## Encounter dependency matrix

### Disoriented Night Crossing — FULL

Narrative goal: protect a nocturnal wildlife crossing while preserving evidence about possible cue conflict.

Required current categories:

- targeting/footprints/range/LoS: VERIFIED for combat targeting only
- base movement legality: VERIFIED
- complete movement: BLOCKING for dynamic crossing, withdrawal and interception
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL only if an exact Status is genuinely invoked; the orientation problem itself creates none
- terrain/weather/hazards/zones/reactions: BLOCKING if light, traffic barriers or environmental state changes tactical legality
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `CROSS`, `WITHDRAW`, `REJOIN_GROUP`, `SEARCH` and avoidance behavior
- adapter/playback: BLOCKING

REDUCED: close the transport corridor through world state, resolve ecological movement outside the grid, then use a static AutoPTU battle only for an independent confrontation.

### Homing Trial Site Emergency — FULL

Narrative goal: abort an already-authorized observational trial safely when an unrelated incident occurs.

Complete movement, tactical policy and adapter/playback are BLOCKING because researchers and a non-hostile subject must withdraw/reach safe positions without being treated as ordinary hostile AI. Environmental family is also BLOCKING if unstable terrain or equipment creates tactical effects. Normal lifecycle/damage/status/Move/Ability/Item/Feature families remain PARTIAL when invoked.

REDUCED: formally abort the trial first, move subject/researchers in world state, preserve the last valid observation, and resolve only the independent threat on a static arena.

### Landmark Loss at the Roost — FULL

Narrative goal: observe changed final-approach behavior after a landmark disappears while a construction incident creates a separate danger.

Complete movement, AI tactical policy and adapter/playback remain BLOCKING. Dynamic construction hazards or changing access also require the environmental family, which is BLOCKING. Basic targeting/movement legality/calculations/action economy remain VERIFIED; all exact Move/Status/Ability/Item/Feature dependencies remain PARTIAL by family.

REDUCED: halt construction and remove workers before combat; observe orientation outside the battle engine and run a static confrontation separately.

### The Wrong Home

Primarily non-combat. It can be resolved through Chronicle state, Migration, Spatial Ecology, Rehabilitation, Telemetry and Pass 177 records. No battle capability is required to decide that the original assumed goal was wrong.

## PTU/Caelo guardrails

Pass 177 must never infer:

- `Magnet Pull` -> magnetic navigation
- Probopass/Nosepass flavor -> universal compass accuracy
- Steel/Rock/Electric Type -> magnetoreception
- Pass 81 magnetic anomaly -> battle modifier
- battle LoS -> landmark-navigation visibility
- base movement legality -> route knowledge
- Tracker -> homing mechanism
- Perception -> perfect orientation
- Telepathy -> shared maps
- familiar home range -> Accuracy/Evasion/Initiative/Speed/capture bonus
- cue conflict -> Confused/Slowed/Tripped/Fatigue
- Minecraft shortest-path or mob-home AI -> ecological evidence

The searchable project sources did not expose a reliable primary Caelo rule for multimodal homing/orientation during this run. Super PTU Online Helper was not available as an invocable capability. No missing rule is filled by invention.

## Minecraft boundary

Minecraft/Cobblemon/Craftics may eventually present positions, movements, lights, weather, landmarks, signs and environmental assets. It must not decide cue use, homing success, research interpretation or magnetic state.

Required direction of authority:

`Chronicle/ecology + owning source layers -> reviewed orientation intent/state -> adapter presentation`

Never:

`Minecraft pathfinding/animation -> navigation truth`.

## Unresolved implementation questions

The narrative repo can proceed without answering these immediately, but FULL encounters remain gated until the engine/runtime can support the needed contracts:

- non-hostile tactical objectives such as homing/search/rejoin/withdraw
- safe escort/crossing behavior with interception
- authoritative overworld-to-battle actor identity handoff
- dynamic cue/environment changes during battle
- any exact PTU/Caelo Skill/Capability interaction with navigation
- any verified relationship between Pass 81 geomagnetic state and a Pokémon’s mechanical behavior

Until those exist, the REDUCED contracts are the implementation-safe default.