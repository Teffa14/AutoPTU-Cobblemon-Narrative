# Global NPC AI Readiness Snapshot — Pass 389

Status: READINESS EVIDENCE. Not canon.
Date: 2026-09-09

## Slice completed

Pass 389 implements the executable identity seam designed in Pass 388 between archaeological `PORTABLE_FIND` evidence and the existing `WorldResource` subsystem.

New executable owner:
- `tools/global_npc_portable_find_resource_binding.py`
- schema `OUROS_PORTABLE_FIND_RESOURCE_BINDING_V1`

Regression coverage:
- `tests/test_global_npc_portable_find_resource_binding.py`

Research/content:
- `research/2026-09-09-portable-find-numbering-identity-scan-389.md`
- `proposals/2026-09-09-the-find-with-two-numbers-pass-389.md`
- updated `design/portable-find-context-custody-bridge-pass-388.md`

No canon file was changed.

## Internal authority check

The Pass 389 owner preserves only the cross-system identity relation.

`SiteEvidenceLedger` remains authoritative for discovery context and the exact historical observation.

`WorldResource` remains the operational physical-resource model used by resource-aware world-agent logic.

`ResourceHandoffLedger` and its checkpoint chain remain authoritative for authorized custody history.

The new binding stores the stable `resource_id` plus a SHA-256 fingerprint of the exact historical `PORTABLE_FIND` observation. It does not copy or freeze current holder, location, reservation, quantity or operational state.

## Resource recovery limitation discovered

`OUROS_NPC_WORLD_CHECKPOINT_V10` persists the resource reservation/request/handoff/attempt/appointment/reschedule bundle supplied to it. It does not currently persist a canonical catalog of all `WorldResource` definitions.

Pass 389 therefore validates against an explicit `declared_resources: Mapping[str, WorldResource]` supplied by the caller. Restore fails if the bound resource ID is absent or if the mapping key disagrees with the resource's own stable ID.

This avoids inventing a resource-catalog owner that does not exist yet.

## Executable guarantees

The ledger now fails closed when:
- the referenced site observation is missing;
- the observation is not `PORTABLE_FIND`;
- the declared world resource is missing;
- the binding predates the observation;
- one observation is assigned to multiple resources;
- one resource is assigned to multiple discovery observations;
- the exact historical observation changes after binding;
- a restore minute is earlier than binding time;
- the declared-resource mapping key and resource identity disagree.

A legitimate later change to holder, location or operational state does not break the historical association.

## Public research contribution

Collections Trust numbering guidance distinguishes entry numbers, accession/object numbers and external numbers, and its archaeology guidance explicitly allows museum accession numbers to coexist with excavator site codes and small-find identifiers.

The Archaeology Data Service A14 public archive demonstrates separate context records and find-level identifiers in one accessible archaeological dataset.

The public PTU campaign pitch `Pokémon Heroes: Champions of Jugdral` contributes only a high-level structural lesson: custody uncertainty around important physical objects can create factional consequences before the full truth is known. No setting, characters, relic system or plot is imported.

## New narrative candidate

`The Find With Two Numbers` is PROPOSED / NON-CANON.

One physical find may have an early field identifier and a later catalog identifier. Different NPCs with access to only one record set can reasonably infer duplication, loss or substitution. The identity bridge can establish that a particular field observation and world resource were associated, while still leaving disputed later records open to investigation.

The reduced version uses no AutoPTU handoff.

## Live engine evidence

AutoPTU-Java inspected head: `01a7787048ba92068f8c1340d80c9e9cb89c371d`, merge #419.

That commit freezes parity for the Impostor random Ability choice and the next value consumed from the same battle RNG stream. It is narrow evidence for that behavior only. It does not verify the complete Abilities family or the broader tactical systems.

AutoPTU Python inspected head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its latest change remains presentation-only viewport-coordinate synchronization and adds no battle-mechanics evidence.

Neither engine was modified.

## Permanent capability classification

Targeting/footprints/range/LoS: VERIFIED within audited scopes only.

Base movement legality: VERIFIED within audited scopes only.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED within audited scopes only.

Action economy/initiative: VERIFIED for audited primitives only.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: individually gated. AutoPTU-Java #419 does not make the family complete.

Items: individually gated. A portable world resource is not a PTU battle Item unless authoritative rules/data separately establish that identity.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED within ordinary audited legal-action scopes.

AI tactical policy: BLOCKING for protect-object, retrieve-object, evidence-first, escort, rescue-first, objective-aware withdrawal and disengage-after-objective unless the exact policy is later verified.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for stable resource projection, pickup/handoff acknowledgement, site/evidence identity and authoritative non-KO objective playback.

## PTU/Caelo/Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` routes relevant questions toward Researcher, Chronicler, Paleontologist, Topographer, Skills/Edges/Features, Items/Gear and encounter construction. It explicitly does not grant Ouros mechanical permission by itself.

Pass 389 therefore adds no Skill check, Trainer Feature effect, Item effect, ownership rule or excavation procedure.

## Reduced playable version

The new proposal can operate with semantic time, site evidence, private knowledge, `PortableFindResourceBindingLedger`, a declared resource mapping, existing custody records and ordinary archive/communication access.

The player can reconcile identifiers without battle and without forcing Minecraft to own object identity.

## Rich version dependency gates

A tactical protect/recover/transport variant may use targeting geometry and verified base movement. Forced movement, interception and carrier repositioning require complete movement. Timed phases and delayed environmental events require the full turn/round lifecycle. Damage-linked persistent objective state requires the stateful damage pipeline. Lasting statuses require the status lifecycle. Flooding, debris, visibility, unstable terrain and reactions require exact terrain/weather/hazards/zones/reactions support. Moves, Abilities, Items and Trainer Features remain individually gated.

The rich version remains blocked on AI tactical policy for objective-aware protect/retrieve/escort/withdraw behavior and on adapter support for authoritative non-KO objective playback.

## Next implementation seam

The smallest next recovery slice is a versioned integration of `PortableFindResourceBindingLedger` into the persistent-world-evidence checkpoint, while continuing to pass the declared-resource state externally.

A later outer recovery manifest should bind global-NPC state, persistent-world evidence, resource/custody state and the future declared-resource catalog owner by digest. That work should not merge their responsibilities.

## Canon unresolved

Open questions remain:
- which institution owns accession/catalog practice;
- whether Tideglass handles physical collections in the relevant district;
- who has authority to create a field-to-resource binding;
- removal/extraction authority;
- legal ownership versus custody;
- identifier-alias evidence and correction policy;
- exact PTU/Caelo Skills, Edges, Features or Items relevant to documentation and conservation.

No answer is promoted in Pass 389.
