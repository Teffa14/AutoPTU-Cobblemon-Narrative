# Cross-fixture persistent-actor continuity scan — Pass 244

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-03
Canon effect: NONE. This note proposes reusable structures and validation targets. It does not approve new species, actors, mechanics, populations or outcomes.

## Question

How should Ouros preserve the identity and ecological meaning of one persistent wild Pokémon while that actor moves through population state, Cobblemon projection, observation, an ecology-driven event, optional AutoPTU adjudication, semantic return, later sightings and world/server lifecycle?

Passes 238–243 established each boundary separately. The remaining risk is cross-boundary drift: the same diegetic Pokémon can accidentally become multiple records, a renderer UUID can be mistaken for identity, a tactical result can be promoted into death/emigration, or an ecology event can be resolved merely because a battle ended.

## Repository constraints reviewed

- `design/ecology-development-program.md`: ecology remains active until a Marea ecosystem works end-to-end and the invariants survive projection, encounter handoff and lifecycle.
- `implementation/marea-sendero-population-demography-fixture-v1.json`: abundance changes require explicit demographic events.
- `implementation/marea-sendero-spawn-reconciliation-fixture-v1.json`: persistent identity belongs to Ouros; Minecraft UUID is temporary correlation; projection uses leases.
- `implementation/marea-sendero-observation-knowledge-fixture-v1.json`: sightings expose evidence, not hidden ledger truth.
- `implementation/marea-sendero-ecology-world-event-fixture-v1.json`: events arise from persistent pressure and resolve only after ecological reevaluation.
- `implementation/marea-sendero-autoptu-handoff-fixture-v1.json`: AutoPTU receives a frozen participant manifest and returns narrow semantic results.
- `tools/validate_ecology_fixtures.py`: current executable regression checks these contracts independently.

## New public sources

### 1. PTU campaign log #22 — ecological cause, cultural practice, investigation, remedy

Source: Reddit, r/PokemonTabletop, “campaign log #22” (2022-05-01)
https://www.reddit.com/r/PokemonTabletop/comments/ug8b7t

The session summary describes a chain in which local Pokémon behavior, a town festival/offering practice, a diseased tree and regional drought are connected. The players gather information from Pokémon, identify the environmental mechanism and cure the tree rather than treating every wild interaction as a battle.

Reusable structure for Ouros:

`observable Pokémon behavior -> human interpretation -> hidden environmental driver -> investigation -> intervention -> later ecological consequence`

Design lesson: the same actor or local population should remain traceable through the whole problem. A quest log or combat result should never replace the environmental causal chain.

No plot, named character, dialogue or distinctive setting element is imported.

### 2. Tales of Visiwa retrospective — terrain, non-combat resolution and campaign continuity

Source: official Pokémon Tabletop community site, “Tales of Visiwa: A Retrospective”
https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

The retrospective records a long-running PTU campaign and explicitly notes the amount of GM-side preparation/crunch. One memorable encounter used shallow water as hindering terrain with changing heat, while the confrontation was also altered through persuasion rather than only by defeating the opponent.

Reusable structures:

- tactical terrain can matter without becoming the entire narrative premise;
- a structured encounter can end or transform through a semantic outcome other than KO;
- campaign-scale continuity benefits from recording the consequence that matters to the world, not only the combat winner;
- executable automation should reduce bookkeeping at boundaries because PTU already imposes high GM-state overhead.

No campaign characters, factions, gods, dialogue or encounter plot are imported.

### 3. NPS human/wildlife interaction categories — pursuit is an ecological event even without injury

Source: U.S. National Park Service, “Who Is the Bad Guy Here? When Animals Misbehave”
https://www.nps.gov/articles/000/who-is-the-bad-guy-here-when-animals-misbehave.htm

The NPS separates tolerated contact from fear, pursuit, feeding and other interaction categories. In particular, pursuit includes a human following an animal that is avoiding or showing alarm. This is useful for Ouros because an overworld chase can create disturbance/avoidance history even when no AutoPTU battle opens and no demographic change occurs.

Reusable structure:

`interaction class -> actor response -> local disturbance memory -> future tolerance/avoidance pressure`

### 4. USGS/NPS bird disturbance evidence — displacement can be temporary and species/context dependent

Sources:

- USGS, “Birds at a Southern California beach: seasonality, habitat use and disturbance by human activity”
  https://www.usgs.gov/publications/birds-a-southern-california-beach-seasonality-habitat-use-and-disturbance-human
- NPS, “Vessels Disturb Kittlitz’s Murrelets in Glacier Bay National Park and Preserve”
  https://www.nps.gov/articles/aps-9-2-2.htm

These sources support two distinctions already important to Ouros. Disturbance can cause animals to move or flee without implying emigration, and local use can rebound after a short displacement. Response also depends on species, activity type and reproductive context.

Reusable rule: `TACTICAL_WITHDRAWAL`, `OVERWORLD_FLEE` and `TEMPORARY_LOCAL_DISPLACEMENT` must remain semantically distinct from `EMIGRATION`.

### 5. USGS site fidelity evidence — identity continuity should not imply fixed coordinates

Source: USGS, “Regional fidelity and movement patterns of wintering killdeer in an agricultural landscape”
https://www.usgs.gov/publications/regional-fidelity-and-movement-patterns-wintering-killdeer-agricultural-landscape

Radio-tagged individuals showed different residency modes, local movements and occasional longer exploratory movements. The important design implication is that persistent identity and persistent position are separate concepts. A known Ouros Pokémon may move among microhabitats and later return without becoming a new member.

## Proposed Ouros continuity model

One actor should be represented by a stable `persistent_actor_ref` owned by Ouros. All other identifiers are scoped references:

- population membership: persistent ecological relation;
- projection lease: temporary right to materialize the member;
- Minecraft entity UUID: temporary renderer/world correlation;
- observation subject token: evidence-layer reference that may be unresolved/probable/supported;
- BattleSpec participant reference: frozen tactical enrollment;
- AutoPTU semantic result actor reference: narrow authoritative result mapping;
- post-event observation: later evidence about the same world actor.

The cross-system invariant is:

`persistent_actor_ref survives every boundary unless an explicit authoritative world event retires or transfers that actor.`

A changing Minecraft UUID, a KO, a forced withdrawal, chunk unload, no sighting, event resolution or server restart cannot by itself retire the actor.

## Pass 244 implementation target

Create one executable cross-fixture trace using the existing first persistent Sendero Fletchling. The scenario remains non-canon test data.

The trace should prove:

1. the actor exists inside the population before rendering;
2. projection reserves the actor before entity materialization;
3. observation refers to the visible subject without exposing the internal persistent ID;
4. ecology pressure can open a world event without altering abundance;
5. a warning/flee interaction may remain overworld;
6. explicit structured engagement freezes the same actor into the AutoPTU manifest;
7. AutoPTU returns a semantic result for that actor;
8. KO/withdrawal can update encounter/disturbance history but cannot imply death or emigration;
9. the source ecology event is reevaluated instead of auto-resolved;
10. later materialization may receive a different Minecraft UUID while keeping identity;
11. a later observation may identify a probable/supported repeat sighting;
12. server/world lifecycle preserves actor, population relationship and consequence history.

## Battle capability dependencies

The baseline trace intentionally uses a simple direct structured engagement so it can advance without pretending missing PTU families are complete.

- targeting/footprints/range/LoS: required for direct structured engagement; VERIFIED in current audited contracts.
- base movement legality: required for ordinary tactical positioning; VERIFIED.
- complete movement including push/pull/knockback/interception/forced movement: not required by the reduced trace; PARTIAL overall.
- core calculations: required for ordinary resolved attacks; VERIFIED.
- action economy/initiative: required; VERIFIED.
- full turn/round lifecycle: potentially required by a real battle sequence; PARTIAL overall.
- full stateful damage pipeline: required for authoritative HP/KO semantics; PARTIAL overall.
- status lifecycle: not required by this reduced scenario; PARTIAL overall.
- terrain/weather/hazards/zones/reactions: not required by the reduced scenario; MIXED/PARTIAL/BLOCKING overall. The rich version could use route hazards only after exact contracts exist.
- move-specific behavior: depends on selected moves; PARTIAL overall.
- abilities: depends on selected actors; PARTIAL overall.
- items: optional; PARTIAL overall.
- Trainer Features/perks: optional; PARTIAL overall.
- AI legal-action infrastructure: required for legal structured choices; VERIFIED.
- AI tactical policy: rich autonomous pursuit/escape version depends on it; BLOCKING overall.
- Minecraft/Cobblemon/Craftics adapter/playback: required for real materialization, suspension and rematerialization; PARTIAL/BLOCKING end-to-end.

## Full vs reduced encounter

Reduced executable version: direct engagement between explicitly selected participants, followed by a narrow `TACTICAL_KO_CONFIRMED` or `TACTICAL_WITHDRAWAL_FORCED` semantic result. Ouros records encounter history and reevaluates ecology. It does not simulate pursuit, reaction chains or dynamic hazards.

Full intended version: the same Fletchling can warn, retreat along a known route, be pursued, use cover/terrain, and potentially disengage without KO. That version additionally depends on complete movement, turn/round lifecycle, terrain/zones/reactions, AI tactical policy and end-to-end adapter playback. It remains blocked/reduced until those exact families are verified.

## Canon status

Canon-approved inputs referenced only:

- Marea / Sendero del Vidrio existing location framework;
- existing Sendero Fletchling population;
- existing first persistent Fletchling actor.

Proposed/test-only:

- all Pass 244 event pressures, interaction sequence, battle result, later sighting and numerical consequence deltas.

Uncertain / unresolved:

- exact ecological delta produced by a KO, chase or withdrawal;
- whether verified battle HP/status writes back immediately or through a later care/condition normalization layer;
- exact threshold for a probable repeat sighting to become a supported identity claim;
- which semantic result vocabulary will be frozen across Ouros, AutoPTU-Java and the Minecraft adapter.
