# Engine Readiness Snapshot — Pass 207

Status: READ-ONLY ENGINE AUDIT
Date: 2026-09-02

## Evidence inspected

Narrative base for this pass: `2b550193b609f0635a75cbbdc828ecc7bde118df`.

AutoPTU-Java current head: `496f7e15dbc4bb547449727cd60cd397d8d9005a`.

The only Java change after the pass-206 gameplay audit is the project/rulebook sanity workflow. The preceding gameplay head `716687c6f8431807b91f33567cc8c9c7fd010756` remains the latest evidence used for forced-movement semantic-event support. Therefore no gameplay capability family is promoted solely because CI coverage improved.

AutoPTU evidence head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its latest changes are Career presentation/save fixes and do not change the PTU engine capability assessment.

AutoPTU-Cobblemon-RPG evidence inspected from current main includes:

- server-owned WILD blueprint source/registry/table/provisioning contracts;
- visible wild Pokemon interaction binding that treats `PokemonEntity` as presentation only;
- immutable world encounter party handoff service;
- authoritative PTU HP nameplate projection on current RPG main.

These strengthen the presentation boundary but do not prove a completed normal world ecology -> battle -> outcome reconciliation loop.

## Permanent capability audit

| Capability family | State | Pass-207 use |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED within audited contracts | usable for reduced ordinary battle |
| base movement legality | VERIFIED within audited contracts | usable for reduced ordinary battle |
| complete movement: push/pull/knockback/interception/forced movement | PARTIAL | avoid in reduced clue encounter; full crossing encounter remains dependency-marked |
| core calculations | VERIFIED within audited contracts | usable for reduced ordinary battle |
| action economy / initiative | VERIFIED within audited contracts | usable for reduced ordinary battle |
| full turn / round lifecycle | PARTIAL | avoid multi-stage tactical scripting in first implementation |
| full stateful damage pipeline | PARTIAL | use only individually audited paths |
| status lifecycle | PARTIAL | no delayed/complex status objective in reduced version |
| terrain / weather / hazards / zones / reactions | BLOCKING as complete family | Minecraft may show environment; no tactical crossing hazard yet |
| move-specific behavior | PARTIAL | select only parity-audited moves |
| abilities | PARTIAL | select only parity-audited abilities |
| items | PARTIAL | observation props must not become unverified battle items |
| Trainer Features / perks | PARTIAL | field checks/features remain profile-governed |
| AI legal-action infrastructure | VERIFIED within audited contracts | usable when battle action space is supported |
| AI tactical policy | BLOCKING for complete family | protective/group tactics remain full-version dependency |
| Minecraft/Cobblemon/Craftics adapter/playback | PARTIAL/BLOCKING for complete target support | clue presentation can proceed before full battle reconciliation |

## Important distinction for pass 207

The observation layer is mostly pre-battle world state. A static clue, sighting ledger entry, warning marker or visible noncombat behavior does not require AutoPTU to simulate tactical mechanics.

The moment an observation interaction claims a PTU mechanical result — for example a Survival/Perception success, a Feature effect, a capture permission, a movement capability, an item effect or an encounter escalation outcome — it must call the active authoritative rules profile instead of implementing the rule in Minecraft.

## First safe implementation target implied by this research

A reduced `Fresh Marks` slice can be built without waiting for the blocking tactical families:

1. server-authored clue object/region in Sendero del Vidrio;
2. authenticated inspection action;
3. persistent provenance-aware observation record;
4. optional authoritative field-check request when a governing contract exists;
5. follow clue to one pre-provisioned visible WILD actor;
6. explicit observe/disengage/engage intent;
7. ordinary battle handoff only through existing authoritative encounter boundaries.

Do not add tactical weather, hazard damage, forced movement, group coordination, delayed status objectives or Minecraft-owned combat AI to make the scene feel richer.

## Unresolved mechanical questions

- Which production rules profile owns deliberate tracking and clue interpretation.
- Whether the observation record should store only direct facts until a generic Skill-check service exists.
- Which exact first Sendero species, level band, move loadout and ability set are parity-safe.
- Whether battle/capture completion exposes enough authoritative result state to reconcile the visible actor normally.
- Whether route disturbance can be persisted through the existing RPG world-object system without conflating Minecraft block mutation with ecological canon.
- Whether nesting evidence requires Egg/breeding provenance services before it can be used in a live route.

No partial capability is treated as complete by this snapshot.
