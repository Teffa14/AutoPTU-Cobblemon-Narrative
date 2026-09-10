# Persistent World Recovery Manifest — Pass 391

Status: IMPLEMENTED DESIGN CONTRACT. Not canon.
Date: 2026-09-09

## Purpose

Ouros now has two independent recovery owners that can each be internally valid:

- `OUROS_NPC_WORLD_CHECKPOINT_V19` for global-NPC causal/action state;
- `OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V2` for persistent site evidence and its explicit evidence bridges.

Pass 391 adds a small outer selection contract so recovery cannot accidentally pair valid checkpoints from different semantic moments.

Schema: `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V1`.

Owner: `tools/persistent_world_recovery_manifest.py`.

## Authority boundary

The manifest owns checkpoint-pair identity only.

It does not own or duplicate:

- global-NPC state;
- site-evidence state;
- private NPC knowledge;
- mutable world-resource state;
- custody history;
- AutoPTU tactical state;
- Minecraft/Cobblemon presentation state.

`PAIR_SELECTION != OWNER_STATE`

Each referenced checkpoint must remain independently valid under its own restore contract.

## V1 payload

The manifest records:

- schema;
- one non-negative `semantic_minute`;
- SHA-256 of the selected V19 global-NPC checkpoint;
- SHA-256 of the selected V2 persistent-world-evidence checkpoint;
- SHA-256 of the manifest itself.

It stores no embedded copy of either checkpoint.

## Build rule

A manifest can be built only when both supplied owner checkpoints:

- use the current schemas named above;
- have valid owner-level SHA-256 values;
- carry the same semantic minute.

A valid V19 from minute 100 and a valid V2 from minute 101 are not a coherent recovery pair.

`VALID_A + VALID_B != COHERENT_PAIR`

## Reconciliation rule

At recovery selection time, candidate checkpoints are accepted only when:

- the manifest digest is valid;
- both candidate checkpoints still have valid owner digests;
- both candidates use the expected current schemas;
- both candidates carry the manifest semantic minute;
- each candidate SHA-256 exactly matches the digest selected by the manifest.

This prevents a recovery bootstrap from silently substituting another individually valid generation of either owner.

## Owner validation remains mandatory

The manifest does not attempt to duplicate the domain validation already implemented by the two owners.

After manifest reconciliation, bootstrap must still invoke the ordinary restore APIs with their existing dependencies:

- V19 requires its global-NPC channels/agendas and nested causal owners;
- V2 requires the matching private `KnowledgeLedgerStore` and declared resource identities.

A maliciously changed owner checkpoint that has been recomputed and then deliberately selected into a newly recomputed manifest can only be rejected by the owner whose semantic invariants were violated. Pass 391 does not claim otherwise.

## Current exclusion: resource-state checkpoint

Pass 390 established that V2 knows only the stable resource-identity catalog digest. The repository still has no authoritative recovery owner for the complete mutable `WorldResource` catalog.

Pass 391 therefore does not fabricate one and does not bind mutable resource/custody state into this manifest.

That can be added only after an explicit owner exists.

## Current exclusion: AutoPTU

The manifest does not contain an AutoPTU session ID, tactical battle snapshot or tactical result.

Recovery of an in-flight `REQUEST_AUTOPTU` remains a separate reconciliation problem. World-agent recovery must not manufacture battle completion or tactical state merely because the narrative owners restored successfully.

## Reduced implementation value

This seam is useful before any richer adapter work. A restart can select one coherent pair of world-agent causality and persistent-world evidence without requiring AutoPTU or Minecraft to duplicate either state family.

## Next seams

The next recovery work should be evidence-led:

1. define an authoritative mutable world-resource catalog recovery owner if the existing resource subsystem can support one without duplicating custody authority;
2. extend the manifest only after that owner exists;
3. add explicit in-flight AutoPTU reconciliation by battle/session identity and authoritative tactical result, not by inference from world state;
4. keep Minecraft/Cobblemon as projection and acknowledgement only.
