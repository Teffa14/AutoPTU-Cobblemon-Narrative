# Global NPC AI Readiness Snapshot — Pass 388

Status: READINESS EVIDENCE. Not canon.
Date: 2026-09-09

## Slice completed

Pass 388 closes the design seam between archaeological `PORTABLE_FIND` observations and the existing world-resource/custody subsystem.

New material:
- `research/2026-09-09-portable-find-custody-context-scan-388.md`
- `design/portable-find-context-custody-bridge-pass-388.md`
- `proposals/2026-09-09-the-object-that-arrived-without-its-context-pass-388.md`

No runtime code was changed in this pass. The bridge remains a proposed contract pending implementation.

## Internal authority check

`SiteEvidenceLedger` already owns portable-find discovery context.

`WorldResource` already owns stable resource state, holder and location.

`ResourceHandoffLedger` already owns authorization and transfer history.

Pass 388 therefore rejects a second archaeological inventory and defines the intended binding boundary instead.

## Live engine evidence

AutoPTU-Java inspected head: `01a7787048ba92068f8c1340d80c9e9cb89c371d` (merge #419, Impostor ability RNG choice parity).

This strengthens only the fixed Impostor RNG-choice seam and deterministic RNG consumption demonstrated by its tests. It does not verify the entire Abilities family, tactical policy, movement family, status lifecycle, terrain/reaction systems or adapter playback.

AutoPTU Python inspected head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its latest change is presentation-only viewport-coordinate synchronization and does not expand battle capability evidence.

Neither engine was modified.

## Permanent capability classification

Targeting/footprints/range/LoS: VERIFIED within audited scopes only.

Base movement legality: VERIFIED within audited scopes only.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED within audited scopes only.

Action economy/initiative: VERIFIED for audited primitives; do not generalize beyond tested lifecycle seams.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: individually gated. Pass 419 evidence does not make the family complete.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED within ordinary audited legal-action scopes.

AI tactical policy: BLOCKING for protect-find, recover-object, escort, rescue-first, documentation-first, objective-aware withdrawal and disengage-after-objective unless a specific policy is later verified.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for stable evidence/resource identity, pickup/handoff acknowledgement, site-revision projection and authoritative non-KO objective playback.

## Reduced playable version

The Pass 388 narrative premise can run without AutoPTU if the implementation uses:
- semantic time;
- site revision and observation;
- private knowledge materialization;
- world resource state;
- existing resource custody transfer;
- ordinary information delivery for provenance/context.

The physical object and its context report can travel independently while remaining causally traceable.

## Blocking implementation seam

The next executable slice should implement a small `PortableFindResourceBindingLedger` with deterministic snapshot/restore and strict cross-validation:
- observation must exist and be `PORTABLE_FIND`;
- resource ID must exist in the selected resource recovery state;
- one-to-one binding in V1;
- binding time cannot predate observation;
- binding cannot mutate holder/location/state;
- restore fails closed if evidence and resource recovery states disagree.

The outer recovery-manifest seam from Pass 387 remains relevant. It should eventually bind persistent-world evidence and resource/custody recovery by digest rather than merge their ownership.

## Canon unresolved

No site, institution, artifact, ownership law, species, historical interpretation or PTU Feature was promoted.

Open questions remain legal ownership vs custody, removal authority, repository rules, allowed field actions and the exact PTU/Caelo support for documentation/conservation tasks.
