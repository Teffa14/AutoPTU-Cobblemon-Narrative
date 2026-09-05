# Global NPC memory cue retrieval contract — Pass 294

Status: PROPOSED EXECUTABLE FOUNDATION
Date: 2026-09-05

## Purpose

Extend Pass 293 memory retrieval with explicit contextual cues while preserving the historical KnowledgeLedger as the causal record.

## Invariants

- A retrieval cue may change present accessibility. It cannot edit, replace or delete the underlying Claim.
- A cue must explicitly reference the claim or claims it can help retrieve. Similarity is not inferred globally.
- Cues are deterministic inputs. Identical claim, semantic time, policy and cue set produce identical recall.
- Cue bonuses are bounded. Repeated equivalent prompts cannot create unbounded accessibility.
- Restored source attribution may only reveal the source already stored on the Claim. A cue cannot invent a different source.
- Loss of present recall never means the historical event did not occur.
- Documentary lookup and unaided/cued personal recall are different evidence paths.
- Looking up a record does not automatically add that record to an NPC KnowledgeLedger. A later explicit reading/learning event must do that if the NPC actually acquires the information.

## Supported cue families

The executable seam currently supports PLACE, OBJECT, PERSON, RECORD_REFERENCE and REHEARSAL. These are simulation categories, not claims about human psychology and not PTU rules.

Each RetrievalCue carries explicit claim IDs plus bounded content and source-access bonuses. The implementation sorts applied cue IDs before reporting them so replay remains stable.

## Archive boundary

ArchiveRecord is a documentary pointer into a ledger owned by an archive or record system. `lookup_archive()` returns the referenced claims without mutating an investigator's personal ledger.

Future adapters may model reading, copying, interviewing, photographing or hearing a record as separate world events that transmit a claim into a personal ledger with appropriate provenance.

## Narrative uses

A witness can fail to retrieve a detail during an interview and remember it when returning to the original location. An old object can restore content without restoring attribution. A signed dispatch can help identify who delivered a report. A municipal log can independently establish what was recorded even when no witness remembers it.

## Canon boundary

No cue type, threshold or bonus is canon-approved world lore. Pass 294 provides a global simulation primitive only. Local authored content must define which places, objects, people or documents are valid cues.

No PTU, Caelo or Kairos rule is adopted by this contract.

## Mechanical dependency boundary

The reduced memory/investigation loop requires no AutoPTU battle capability.

If recalled information leads to a structured encounter, that encounter inherits only the capability families it actually uses. Do not infer category completion from a representative Java hook.
