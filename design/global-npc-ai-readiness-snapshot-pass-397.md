# Global NPC AI readiness snapshot — Pass 397

Status: IMPLEMENTED PROVISIONAL
Date: 2026-09-10

## Slice completed

Pass 397 makes the Pass 396 resource holder-transition journal recoverable through `OUROS_RESOURCE_HOLDER_TRANSITION_CHECKPOINT_V1`.

Implementation:

- `tools/resource_holder_transition_checkpoint.py`;
- `tests/test_resource_holder_transition_checkpoint.py`;
- `design/resource-holder-transition-recovery-contract-pass-397.md`.

Research/content:

- `research/2026-09-10-holder-journal-recovery-expedition-scan-397.md`;
- `proposals/2026-09-10-the-expedition-log-that-survived-the-storm-pass-397.md`.

No `canon/` file changed.

## What is now executable

The holder-transition journal can be serialized at one semantic recovery cut with deterministic ordering and a SHA-256 identity.

Restore validates schema, digest, transition shape, transition kind, duplicate identity, per-resource causal order, holder continuity and canonical serialization order.

The recovered owner preserves checkout, return and authorized handoff history that was actually journaled before the checkpoint.

It does not reconstruct missing transitions from current holder, reservation history, custody history, Minecraft presentation or NPC belief.

## Authority boundary

Current mutable resource state still belongs to `OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1`.

Reservation claims still belong to `ReservationLedger`.

Authorized custody transfer history still belongs to `ResourceHandoffLedger`.

The new checkpoint owns only recovery of the explicit holder-transition journal.

The journal is not yet declared universally complete. Pass 396 covered the production mutation paths found by repository inspection, but a final authority claim requires proving that all production holder mutations route through those wrappers.

## Recovery status

The current outer recovery manifest remains `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V2`, which selects global NPC state, persistent evidence and current resource catalog at one semantic cut.

Pass 397 deliberately does not mutate that existing manifest in place.

The next recovery step is a new manifest generation that includes the holder-transition checkpoint digest at the same semantic minute. After that, the Pass 394/395 reconciliation layer can consume the recovered holder journal without mixing generations.

## Narrative consequence

Restart no longer needs to destroy holder-history events that were already written into the Pass 396 journal and captured by a Pass 397 checkpoint.

A recovered event remains historical evidence. Events after the selected semantic cut remain unknown until another authoritative source establishes them.

This distinction supports investigations without turning incomplete recovery into fabricated theft, deception or teleportation.

## Live AutoPTU evidence

AutoPTU-Java main inspected at `ca235409e6d317055ae4afd9008bd82156b739f7`, merge #423, “Freeze authoritative switch transition plan”.

The head adds parity evidence for one successful combatant replacement plan: outgoing active/off-field result, replacement active result, replacement destination and switch validity guards. It strengthens only that switching seam.

AutoPTU Python remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its latest change remains presentation-only.

No engine repository was modified.

## Permanent capability classification

Targeting/footprints/range/LoS: VERIFIED only inside previously audited scopes.

Base movement legality: VERIFIED only inside previously audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only inside previously audited scopes.

Action economy/initiative: VERIFIED only for the audited primitives, not the whole family.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING depending on the exact mechanic.

Move-specific behavior: individually gated.

Abilities: individually gated; Impostor and related entry/round-start seams do not prove the family.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for ordinary audited scopes.

AI tactical policy: BLOCKING for objective-specific field behavior such as rescue-first, survey-first, escort, protect-resource, objective-aware withdrawal and disengage-after-objective.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for persistent resource interaction, pickup/handoff acknowledgement, non-KO objective state and authoritative end-to-end playback.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked. It remains a routing aid to supplied source material, not an acceptance mechanism.

Pass 397 grants no Skill, Edge, Trainer Feature, Item effect, environmental modifier, switch rule, hazard rule or encounter exception.

## Next highest-value seams

First, add the holder-transition checkpoint to a new coherent outer recovery manifest generation instead of rewriting V2 in place.

Second, extend post-restore reconciliation so recovered holder history can prove a current holder when coverage is complete, while retaining `INDETERMINATE` where the journal does not cover the required interval.

Third, audit every production and adapter-side holder mutation before declaring the journal universally authoritative.

The larger unresolved integration remains AutoPTU session recovery. A battle that was in flight during a crash still needs stable battle/session identity plus authoritative tactical state or terminal result. Persistent-world recovery and Minecraft presentation must not guess that outcome.
