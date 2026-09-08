# Pass 352 research — terminal message envelope provenance

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-08
Canon effect: NONE

## Repository gap confirmed before research

The recursive repository inventory at head `f29478826c2a8decc0bc694bf356e077e505d163` was inspected before writing. Relevant owners were then read directly: `CURRENT_FOCUS.md`, `tools/global_npc_information_network.py`, `tools/global_npc_resource_allocation_notices.py`, `tests/test_global_npc_resource_allocation_notice_binding.py`, `tools/global_npc_deception_runtime.py`, canon governance, and the Global NPC CI workflow.

Pass 351 correctly bound an allocation notice to the actual sender and affected recipient while an `InformationEnvelope` was still pending or awaiting local acknowledgement. It deliberately failed closed after final delivery because the queue retained `DELIVERED` plus the event ID but discarded the addressable envelope metadata.

That creates a later-audit gap. A completed delivery could no longer safely prove which sender, receiver, message, source claim, channel, and authored/delivery times belonged to the transport event.

No prior research note was found using RFC 3464 or NIST audit-trail guidance for this seam.

## Public source 1 — RFC 3464 delivery status notifications

Source: RFC Editor, RFC 3464, “An Extensible Message Format for Delivery Status Notifications”
https://www.rfc-editor.org/info/rfc3464/

Reusable structures:

- a delivery report needs a stable way to correlate back to the original transaction;
- per-recipient delivery status retains the recipient identity rather than collapsing all outcomes into one broadcast result;
- delivery can be delayed, failed, relayed, expanded, or delivered;
- preserving the original envelope identifier and recipient information supports later correlation and troubleshooting;
- “delivered” is a transport result and should not be stretched into unrelated conclusions.

Ouros adaptation:

Keep terminal transport provenance addressable by stable event ID after the queue removes the event from pending work. Preserve sender, receiver, message ID, source/new claim IDs, channel and transport times. Do not use the archive to manufacture comprehension, agreement, memory accessibility, truth, or relationship effects.

## Public source 2 — NIST audit trail / log guidance

Sources:

- NIST CSRC audit trail glossary: https://csrc.nist.gov/glossary/term/audit_trail
- NIST CSRC audit log glossary: https://csrc.nist.gov/glossary/term/audit_log
- NIST SP 800-92 log-management overview: https://csrc.nist.gov/pubs/sp/800/92/final

Reusable structures:

- an audit trail is useful when it can reconstruct the sequence surrounding an operation from inception through result;
- logs preserve documentary evidence of specific events and support later operational investigation;
- event records need stable chronology and enough identity to correlate related records.

Ouros adaptation:

A terminal communication event should remain queryable as documentary transport evidence after delivery or terminal channel failure. The archive is evidence of what the communication runtime processed. It is not evidence that the world fact inside the message was correct.

## Public source 3 — NARA electronic-message recordkeeping

Sources:

- National Archives electronic-message management: https://www.archives.gov/records-mgmt/email-mgmt
- NARA AC 23.2025 on third-party messaging records: https://www.archives.gov/records-mgmt/memos/ac-23-2025

Reusable structures:

Electronic messages can remain records after their immediate operational use ends. A system may need later access to the message record for accountability and reconstruction rather than deleting all metadata when live delivery work is complete.

Ouros adaptation:

World simulation can retain compact transport provenance for completed events without forcing every message to remain a live pending object.

## Public source 4 — Pokémon Unbound mission-log structure

Sources:

- Pokémon Unbound missions index: https://unboundwiki.com/missions/
- Missions guide: https://pokemonunboundpokedex.com/wiki/missions/

Reusable structure only:

A persistent mission log lets side obligations remain inspectable across a long-running adventure. Some missions activate, remain unresolved through unrelated play, and become actionable again when prerequisites or locations line up.

Ouros adaptation:

A communication dispute or allocation audit can remain a compact persistent side case while the player continues other work. The case can later resume from stored evidence instead of recreating the scene or forcing it into the main story.

No characters, dialogue, protected plot, map content, rewards, or mission text from Pokémon Unbound are imported.

## PTU / Caelo / project boundary

This pass adds world-simulation communication provenance only.

The inspected project source-authority material keeps PTU/Caelo/AutoPTU as authority for battle legality and mechanical consequences. The current repository inventory still does not expose a newly adopted Caelo rules source that would authorize a new combat mechanic for this pass.

A late audit of a communication can be resolved without battle mechanics. If an investigation later requires physical searching, interception, pursuit, battle, a status effect, weather, a Trainer Feature, an Item, an Ability or a Move, that mechanic remains gated by the appropriate PTU/AutoPTU owner.

## Design lessons extracted

1. Live queue membership and historical transport evidence should be separate concepts.
2. A terminal event should remain correlatable by its stable event ID.
3. Recipient identity belongs to provenance and must survive final delivery.
4. A successful transport record does not imply that a claim was true.
5. A delivery archive should survive the same restart boundary as the communication queue.
6. Deceptive statements need the same transport archive; preserving transport provenance must not sanitize deception into an ordinary statement.
7. Resource-notice audits can safely attach after delivery only when the archived sender/receiver metadata matches the obligation.
8. Wrong-recipient deliveries remain wrong after archival; persistence must not make a bad linkage valid.

## New original Ouros hooks derived from the pattern

### Late reconstruction

A team disputes whether a changed resource allocation was ever communicated. The original booking, allocation application, notice obligation and terminal envelope remain available. The player reconstructs what actually happened without requiring every participant to remember the event identically.

### Correct delivery, inaccessible recall

The archive proves the message reached the correct managed NPC. The NPC’s current retrieval state can still make the memory inaccessible under the existing memory-access owner. That creates a legitimate disagreement without classifying the NPC as deceptive.

### Wrong recipient discovered after the fact

The terminal archive shows a real message went to another actor. The allocation obligation therefore remains unsatisfied even though a communication event ended successfully for somebody else.

### Channel troubleshooting

A terminal channel failure can retain the original envelope metadata for later inspection. Retaining that envelope does not retroactively count the notice as delivered.

## Canon classification

All hooks above are PROPOSED / NON-CANON.

No canon file is changed by Pass 352.
