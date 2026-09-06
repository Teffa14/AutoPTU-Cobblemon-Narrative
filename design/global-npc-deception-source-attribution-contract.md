# Global NPC deception and source-attribution contract — Pass 295

Status: PROPOSED EXECUTABLE FOUNDATION
Date: 2026-09-05

## Purpose

Persistent NPCs need to be able to mislead other actors, repeat false claims, misattribute a source, and later remember a source incorrectly without corrupting Ouros' causal record.

This contract extends the Pass 282 knowledge ledger and the Pass 293–294 retrieval layers. It does not replace them.

## Authority boundaries

Historical provenance remains server truth about information flow.

An NPC's assertion, belief or remembered attribution is subjective state. It may disagree with historical provenance.

`ACTUAL_INFORMATION_PROVENANCE != NPC_PERCEIVED_SOURCE`

`NPC_ASSERTION != WORLD_TRUTH`

`DECEPTIVE_STATEMENT != RETROACTIVE_LEDGER_EDIT`

## Deceptive statement

A `DeceptiveStatement` is authored from a claim already present in the speaker's private ledger. The executable seam currently supports:

- false content: the speaker asserts a different value from the basis claim;
- false source: the speaker attributes the information to a different source from the basis claim;
- both at once.

The API deliberately rejects a fully truthful restatement. Ordinary truthful relays continue to use the existing information-transfer path.

The current implementation defines deception relative to the speaker's selected basis claim. It does not claim to determine objective metaphysical truth. An NPC can be honestly wrong elsewhere in the information system without using this API.

## Materialization into receiver knowledge

When a deceptive statement reaches a receiver, the receiver gets an ordinary `REPORT` claim.

The report preserves the real immediate speaker in `source_agent_id`.

Its provenance root is the deceptive communicative act, not the speaker's original evidence root. This prevents the altered statement from masquerading as an unchanged relay of the original evidence.

The speaker's basis claim remains linked for audit, but the receiver is not granted access to that private basis merely because the lie references it.

## Subjective source attribution

`SourceAttributionStore` records what an NPC currently attributes a received claim to.

Supported attribution events are:

- `SPEAKER_DECLARATION`: the speaker explicitly names a purported source;
- `MEMORY_CONFUSION`: a later world event assigns a different remembered source.

These records never mutate the underlying `Claim`.

The latest attribution is selected deterministically by semantic minute and stable attribution ID.

Without an attribution overlay, perceived source falls back to the claim's actual immediate source.

## Source confusion boundary

Pass 295 does not randomly generate memory errors. It only provides a safe representation when authored content or a future deterministic memory policy says source confusion occurred.

A source-confusion event must occur at or after the original claim. It must differ from the actual immediate source.

Future systems may use cues, social pressure, repeated retellings or other explicit causes to create source confusion. Those causes must remain inspectable and must not rewrite provenance.

## Persistence

The subjective attribution layer uses `OUROS_NPC_SOURCE_ATTRIBUTION_V1`.

Snapshot/restore preserves attribution history and deterministic effective attribution.

The underlying knowledge ledger continues to use its own existing snapshot contract.

## Narrative consequences

This contract enables investigations where actors disagree for different reasons:

- one NPC deliberately lied;
- another repeated the lie honestly;
- another remembers the content but assigns it to the wrong witness;
- an archive preserves the original chain;
- later corroboration can expose the mismatch without erasing the earlier decisions that followed from it.

## Reduced implementation form

The reduced form is entirely world-state driven:

knowledge -> deceptive statement -> receiver report -> subjective attribution -> later interview/corroboration -> replanning

No AutoPTU battle capability is required.

## Rich encounter dependency rule

If a deception-driven investigation causes a structured encounter, declare only the exact capability families that encounter uses.

A chase requiring interception or forced movement depends on complete movement.

A scene using mechanical weather, hazards, zones or reactions depends on that family.

Temporary statuses or delayed battle effects depend on their lifecycle and owner-specific behavior.

Autonomous tactical choices remain dependent on AI tactical policy.

Minecraft display or playback remains dependent on the adapter boundary.

No representative engine seam promotes an entire family to complete.

## Canon status

The architecture in this file is proposed executable foundation.

No named liar, faction, incident, settlement, institution or plot outcome becomes canon through this contract.

No PTU, Caelo or Kairos rule is adopted here.