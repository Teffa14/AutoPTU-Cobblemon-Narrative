# Engine readiness snapshot — Pass 250

Status: LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-04
Narrative repo pass: 250

## Read-only engine evidence

### AutoPTU-Java

Observed main head during this pass:

`4e5ff6bbd6637d46598bce99e1dccf77f81ee9e8` — `Run Java landing contract in forced movement parity gate (#340)`

This advances CI/parity coverage for the already-existing forced-movement landing contract. It does not establish complete support for all forced movement, interception, reactions, hazards or movement interactions.

### AutoPTU Python oracle

Observed main head:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — presentation-only viewport/coordinate synchronization change.

No new Python rules evidence was observed in this pass.

## Permanent capability categories

The classifications remain conservative and scoped to audited evidence.

| Capability family | Status | Pass 250 interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Existing audited core contracts; not required by reduced spawn admission path. |
| base movement legality | VERIFIED | Existing audited core contracts; not required by reduced path. |
| complete movement incl. push/pull/knockback/interception/forced movement | PARTIAL | Java has representative forced-movement landing contracts and parity gating; family remains incomplete. |
| core calculations | VERIFIED | Existing audited deterministic core. |
| action economy / initiative | VERIFIED | Existing audited primitives. |
| full turn / round lifecycle | PARTIAL | Do not assume complete phase/timing coverage. |
| full stateful damage pipeline | PARTIAL | Not required for spawn admission. |
| status lifecycle | PARTIAL | Not required for spawn admission. |
| terrain / weather / hazards / zones / reactions | MIXED / PARTIAL / BLOCKING | Landing-trap seams are evidence for specific cases only. |
| move-specific behavior | PARTIAL | Exact Move coverage must be checked encounter-by-encounter. |
| abilities | PARTIAL | Naturewalk representative behavior does not complete the family. |
| items | PARTIAL | Exact Item coverage must be checked. |
| Trainer Features / perks | PARTIAL | Exact Feature coverage must be checked. |
| AI legal-action infrastructure | VERIFIED | Existing audited infrastructure. |
| AI tactical policy | BLOCKING | Rich autonomous tactical pursuit/evasion remains blocked as a family. |
| Minecraft / Cobblemon / Craftics adapter & playback | PARTIAL / BLOCKING | Pass 250 identifies concrete Cobblemon spawn-control primitives but no Ouros runtime adapter implementation is yet verified end-to-end. |

## Cobblemon adapter evidence added this pass

Current public Cobblemon source verifies a cancellable entity-spawn event surface and a PokemonEntity-filtered stream. Current Spawn Rules documentation verifies a filter mechanism that can block natural spawns.

This improves adapter readiness from an abstract quarantine requirement to a specific proposed double gate:

1. data-driven natural spawn denial in ecology-managed scope;
2. cancellable entity admission backstop requiring an Ouros lease/token for managed direct projections.

Still blocking:

- pinned Cobblemon version in the eventual adapter module;
- verified classification of natural versus owned/system/restored Pokemon entity paths;
- real admission-token propagation into the materialization callback;
- loader-specific cancellation tests;
- end-to-end proof that a cancelled native entity cannot interact/capture/battle before removal;
- upgrade regressions for Cobblemon API changes.

## Encounter dependency note

Pass 250 reduced ecology path requires no AutoPTU tactical capability. It depends on the Minecraft/Cobblemon/Craftics adapter family only.

If the admitted actor later enters pursuit/interception, the authored full version additionally depends on base movement, complete movement, lifecycle, AI tactical policy and adapter/playback. Add targeting, calculations, damage, statuses, terrain/reactions, exact Moves, Abilities, Items and Trainer Features only when the specific encounter uses them.

No representative mechanic in this snapshot promotes an entire family.
