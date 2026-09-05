# Global NPC AI readiness snapshot — Pass 291

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

This snapshot records live engine evidence relevant to the Pass 291 persistence pattern. A representative hook never promotes an entire capability family.

## Read-only engine heads checked

AutoPTU-Java: `3913afb17430967f925179694693e6d6041b67c2`

Latest inspected change: `Add selective temporary-effect cleanup contract (#369)`. It adds a declarative lifecycle hook that removes selected temporary-effect entries by effect family and metadata while preserving unrelated entries, with actor/all-combatant scopes and dedicated tests. This is useful lifecycle infrastructure. It does not establish full lifecycle, status, terrain, Trainer Feature or other owner-family parity.

AutoPTU Python: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Latest commit remains presentation-only and explicitly states that battle rules/outcomes do not change.

## Permanent capability categories

| Capability family | Pass 291 status | Live-evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Existing audited core contracts remain sufficient for the base family. |
| base movement legality | VERIFIED | Existing audited base movement contract remains verified. |
| complete movement: push / pull / knockback / interception / forced movement | PARTIAL | Representative interactions exist; complete family parity is not proven. |
| core calculations | VERIFIED | Existing deterministic calculation contracts remain verified. |
| action economy / initiative | VERIFIED | Existing audited primitives remain verified. |
| full turn / round lifecycle | PARTIAL | Java continues gaining declarative lifecycle hooks, but full behavior across phases and owners is not proven. |
| full stateful damage pipeline | PARTIAL | Server-owned seams exist; complete stateful parity remains unverified. |
| status lifecycle | PARTIAL | Selected temporary-effect cleanup/refresh behavior exists; complete status lifecycle remains unverified. |
| terrain / weather / hazards / zones / reactions | MIXED / PARTIAL / BLOCKING | Coverage remains uneven and family-wide parity is not established. |
| move-specific behavior | PARTIAL | Representative Moves exist; corpus breadth and interactions remain incomplete. |
| abilities | PARTIAL | Selected Ability/lifecycle seams exist; full Ability corpus is not verified. |
| items | PARTIAL | Selected Item rules exist; full corpus and lifecycle interactions remain incomplete. |
| Trainer Features / perks | PARTIAL | Selected Trainer mechanics exist; complete feature/interrupt coverage is not verified. |
| AI legal-action infrastructure | VERIFIED | Existing audited legality infrastructure remains verified. |
| AI tactical policy | BLOCKING | Autonomous tactical policy is still not complete. |
| Minecraft / Cobblemon / Craftics adapter / playback | PARTIAL / BLOCKING end-to-end | Full authoritative request/result/ack playback remains incomplete. |

## Pass 291 dependency interpretation

Knowledge-ledger snapshot/restore requires no tactical capability family.

The reduced investigation pattern can run entirely in semantic world state.

A full encounter inherits exact dependencies from its chosen mechanics. Persistence does not relax any engine gate and does not allow Minecraft to reproduce missing PTU rules.

## Unresolved mechanical / integration questions

- Can world-event causal references persist through AutoPTU request, tactical resolution and return?
- Will Minecraft acknowledgement state survive restart without replaying a completed local projection?
- Which selective lifecycle cleanup registrations will be parity-frozen next, and which owner family proves each registration?
- How will tactical policy eventually expose why one legal action was chosen?
- What production transaction boundary will atomically persist world ledgers, queues, scheduler state and adapter acknowledgements?

None of these blocks the reduced investigation or the new ledger persistence seam.
