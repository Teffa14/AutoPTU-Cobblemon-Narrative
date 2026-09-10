# Persistent World Recovery Manifest V4 Contract — Pass 407

Status: ACTIVE IMPLEMENTATION CONTRACT
Canon effect: NONE

## Purpose

`OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V4` selects one exact generation of five independent persistent-world owners at one semantic minute.

The selected owners are the global NPC checkpoint, persistent-world evidence checkpoint, current `WorldResource` catalog checkpoint, resource-holder transition checkpoint, and holder-history coverage baseline checkpoint.

The manifest stores each owner digest and protects its own payload with SHA-256. Build rejects mixed semantic cuts. Reconciliation verifies every supplied owner independently and rejects a valid checkpoint from the wrong generation even when its semantic minute matches.

## Compatibility

V1 remains readable as a two-owner generation. V2 remains readable as a three-owner generation. V3 remains readable as a four-owner generation that includes holder transitions but no baseline checkpoint. Legacy recovery does not fabricate the newer owner and rejects an injected baseline candidate that its manifest never selected.

## Authority boundary

Selection does not change ownership semantics.

The resource catalog owns current resource state at its cut. The holder-transition journal owns recorded holder changes. A holder-history coverage baseline owns only its certified starting holder at its recorded baseline cut. V4 does not make history before that baseline complete and does not permit the baseline to prove the catalog generation that originally caused it to be issued.

The baseline checkpoint and transition checkpoint being selected at one outer semantic minute means only that both persisted owners belong to the same recovery generation. Individual baseline records may have earlier `at_tick` values and remain bounded by their own provenance.

## Restore rule

A V4 caller must supply all five selected checkpoint candidates. Missing baseline evidence fails closed. A digest mismatch fails closed. A schema mismatch fails closed. A semantic-minute mismatch fails closed.

Downstream restore code must still run each owner's semantic validation and the cross-owner resource reconciliation stages. The manifest does not replace those checks.

## Regression coverage

`tests/test_persistent_world_recovery_manifest.py` covers exact five-owner round trip, mixed-cut rejection, wrong-but-valid baseline generation rejection, tampering, required V4 baseline evidence, V3 compatibility, rejection of baseline injection into V3, V1/V2 compatibility and current baseline schema enforcement.

## Next seam

The next safe integration step is to restore the manifest-selected baseline checkpoint and feed those certificates into bounded holder-history reconciliation only for intervals after each certificate cut. Cross-owner chronology must reject any transition sequence that cannot continue from the restored certified holder.
