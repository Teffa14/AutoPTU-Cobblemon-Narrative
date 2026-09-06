# Global NPC false-source attribution exposure contract — Pass 299

Status: IMPLEMENTATION-FACING DESIGN; NOT CANON
Date: 2026-09-06

## Purpose

Pass 295 can represent a deliberately false source declaration without corrupting the actual immediate speaker recorded in `Claim`. Pass 298 can discover false content and gate trust consequences on evidence of intent. This contract closes the separate source-verification seam: an NPC may investigate whether the authority named in a message actually supplied that information.

Factual correctness and source legitimacy are independent questions. A statement can be factually true while falsely attributed, factually false while correctly attributed, or false on both dimensions.

## Invariants

- Historical `Claim.source_agent_id`, `provenance_root`, parent and message lineage are immutable evidence of actual delivery history.
- `SourceAttributionStore` remains subjective/presented attribution state; exposure never rewrites it retroactively.
- A denial by the named source creates a dispute. It does not by itself prove that the speaker fabricated the attribution, because the denial can itself be wrong or deceptive.
- A provenance-independent authorship/dispatch record that identifies a different source can corroborate false attribution without establishing deceptive intent.
- A sufficiently strong explicit speaker admission may establish both the false attribution and intent.
- Missing records are not proof of non-authorship.
- Repeated relays from one provenance root do not become independent corroboration.
- Trust consequences target the actual communicator whose intent was established, never the authority whose name was borrowed.
- Only evidence already present in the discoverer's private `KnowledgeLedger` may be used. Future evidence is rejected.
- Findings are deterministic, snapshot-safe and idempotent at the relationship consequence boundary.

## Executable phases

`SOURCE_DISPUTED`: the named source directly denies the attribution. Investigation remains open.

`FALSE_ATTRIBUTION_CORROBORATED`: independent authorship/dispatch evidence establishes a different source. Intent remains unresolved.

`INTENT_ATTRIBUTED`: explicit evidence establishes that the actual speaker knowingly used the false attribution. Only this phase can authorize the default directional trust penalty.

## Evidence kinds

`NAMED_SOURCE_DENIAL` requires the verification claim's immediate source to equal the authority named by the deceptive statement.

`AUTHORSHIP_RECORD` requires a provenance-independent claim plus an explicit different `actual_source_agent_id`.

`SPEAKER_ADMISSION` requires the evidence claim to come from the actual speaker and to identify that speaker as the actual source.

The evidence-kind wrapper is an Ouros verification descriptor over an existing private claim. It does not add facts to the ledger.

## Narrative use

This supports forged authority, borrowed institutional legitimacy, false referrals, fabricated orders, misrepresented eyewitness chains, disputed dispatches and retrospective investigation. It also supports a useful non-combat distinction: proving that an order did not come from the person named on it can matter even when the order's factual content happened to be correct.

## Engine boundary

The reduced loop is world-semantic only and has no AutoPTU dependency: statement -> perceived attribution -> verification evidence -> exposure phase -> relationship/replanning consequence.

If an authored version adds a structured pursuit, forced movement requires complete movement; mechanical weather/hazards/zones/reactions require that capability family; delayed/status effects require lifecycle/status plus the owning Move/Ability/Item/Trainer Feature family; autonomous combat choices require AI tactical policy; authoritative visible playback requires the Minecraft/Cobblemon/Craftics adapter.

No PTU, Caelo or Kairos mechanic is adopted by this contract.
