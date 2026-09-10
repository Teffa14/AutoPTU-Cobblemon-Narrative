# Global NPC AI Readiness Snapshot — Pass 392

Status: READINESS EVIDENCE. Not canon.
Date: 2026-09-09

## Slice completed

Pass 392 adds `OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1` as an explicit recovery owner for the complete mutable `WorldResource` catalog.

Implementation:
- `tools/world_resource_catalog_checkpoint.py`;
- `tests/test_world_resource_catalog_checkpoint.py`;
- `design/world-resource-catalog-recovery-contract-pass-392.md`.

Research/content:
- `research/2026-09-09-resource-status-accountability-expedition-scan-392.md`;
- `proposals/2026-09-09-the-repeater-that-was-available-yesterday-pass-392.md`.

No canon file or engine repository was changed.

## Recovery boundary

The new owner snapshots current stable identity, capability refs, quantity, operational state, location, holder and reservation target for every declared resource at one semantic minute.

It does not copy request, reservation, custody, consumption or discovery history.

This is required because `WorldResource` already carries mutable current state while `ResourceHandoffLedger` separately carries authorized transfer history. Restoring one from the other would silently merge two authorities.

The snapshot is deterministic by resource ID and capability reference. It rejects duplicate resource identities and malformed resource records. Restore validates schema/digest and can reject a checkpoint generated after the selected recovery minute.

Per-resource mutation time remains unavailable because `WorldResource` does not currently carry it. V1 therefore proves one whole-catalog image at the checkpoint boundary, not the timestamp of each field mutation.

## Public research contribution

FEMA/NIMS resource-management guidance separates maintained inventory from changing operational status and emphasizes current tracking of availability, capability and location. Ouros reuses that structure only as a systems-design lesson.

A previously unused public PTU campaign premise about expedition teams leaving an isolated settlement when supplies run low supports resource acquisition as an exploration driver rather than a combat-only objective.

Pokémon Tabula Rasa was not previously found in repository research. Its public description of a sparsely settled tundra region supports the high-level pattern that remote geography can make a small number of depots and field resources narratively important. No protected characters, region details, creatures, maps or plot were imported.

PTU public rules references were used only to reinforce that travel supplies and specialized equipment exist while actual Item effects remain their own mechanical rules. A generic `WorldResource` does not gain PTU Item behavior by implication.

## New narrative candidate

`The Repeater That Was Available Yesterday` is PROPOSED / NON-CANON.

Two teams rely on the same field capability. One receives accurate information that the resource is available, but before arrival another authorized mission checks it out. The first team reaches the correct depot with stale but historically correct information.

The reduced version is a resource-state, travel, communication and replanning scenario with no AutoPTU requirement. The rich version can stage escort/extraction/protection of the returning resource while keeping safe recovery or transfer as the objective rather than a KO sweep.

## Read-only engine evidence

AutoPTU-Java inspected head remains `36e6d7e34791cc7e950bdff31f80bb8a1abec1dd`, merge #420.

That head wires the tested Impostor path through authoritative round-start execution with effective-Ability resolution, nearest eligible opponent selection, battle-owned Python-compatible RNG, transformation mutation, once-per-round guard and Ability event. It strengthens that exact seam only.

AutoPTU Python inspected head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change is presentation-only viewport-coordinate synchronization.

Neither engine was modified.

## Permanent capability classification

Targeting/footprints/range/LoS: VERIFIED within audited scopes only.

Base movement legality: VERIFIED within audited scopes only.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED within audited scopes only.

Action economy/initiative: VERIFIED for audited primitives only. New resource-objective interactions are not implied by those primitives.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: individually gated. Impostor #420 remains representative evidence for its tested seam only.

Items: individually gated. `WorldResource` is not equivalent to a PTU Item.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED within ordinary audited scopes only.

AI tactical policy: BLOCKING for protect-resource, retrieve-object, escort-carrier, transfer-object, objective-aware withdrawal and disengage-after-objective until exact policies are verified.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for stable resource projection, pickup/handoff acknowledgement, objective state and authoritative non-KO completion playback.

## Reduced playable version

The new proposal can run with semantic time, live `WorldResource` state, the new catalog checkpoint, existing request/reservation/handoff owners where their histories matter, private knowledge, communication, world travel and replanning.

No tactical battle resolution is required.

## Rich-version dependency gates

Ordinary tactical placement can use verified targeting/base-movement scopes. Forced carrier movement, drag, push/pull, knockback and interception require complete movement. Timed extraction or return windows require full turn/round lifecycle. Persistent damage-linked objective changes require the stateful damage pipeline. Lasting conditions require status lifecycle. Storms, unstable terrain, visibility effects and reaction hazards require exact terrain/weather/hazards/zones/reactions support.

Moves, Abilities, Items and Trainer Features remain individually gated. Objective-aware tactical AI and authoritative adapter playback remain blocking for the full non-KO scenario.

## PTU / Caelo / Kairos boundary

The project source index and existing PTU/Caelo references were rechecked only as authority routers. Pass 392 does not introduce a new Skill check, Trainer Feature, Item effect, communications rule, supply-consumption rule or tactical interrupt.

If the proposed repeater later receives a PTU mechanical effect, that exact effect must be cross-checked and capability-gated separately.

## Next implementation seams

Highest-value recovery work after this pass:

- independently validate the new resource catalog owner in CI;
- extend the outer persistent-world recovery manifest only after that owner is stable, binding its exact digest at the same semantic minute as V19 and evidence V2;
- define cross-owner reconciliation between current holder/reservation state and their historical ledgers without reconstructing missing history;
- define in-flight AutoPTU session reconciliation by battle/session identity and authoritative tactical result;
- keep Minecraft/Cobblemon acknowledgement downstream of world and battle authority.

## Canon unresolved

Still open:

- which institution owns or operates shared resource catalogs;
- whether the proposed field repeater exists;
- assignment/reassignment authority;
- ownership versus custody;
- remote locations where shared capability scarcity matters;
- applicable PTU/Caelo Skills, Edges, Features and Items;
- whether resource allocation becomes a regional faction arc.

No answer is promoted by Pass 392.
