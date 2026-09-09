# Global NPC AI readiness snapshot — Pass 379

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative repository baseline inspected before writing: `a143ea570bc1c9840de7e9a79efe2301ae1119ed`.

Read-only AutoPTU-Java head inspected: `6cc66d91d286fab06365cf37d88dd04038589195` (merge #415, oracle-backed authoritative round-start rollover parity for round number, initiative order/cursor and first actor after rollover).

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives. Java merge #415 strengthens the authoritative round-rollover initiative seam specifically.
6. full turn/round lifecycle — PARTIAL. Merge #415 verifies rollover round/initiative state against the pinned Python oracle; it does not establish all round-start/end effects, nested reactions or lifecycle families.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism.
10. move-specific behavior — INDIVIDUALLY GATED.
11. abilities — INDIVIDUALLY GATED.
12. items — INDIVIDUALLY GATED.
13. Trainer Features/perks — INDIVIDUALLY GATED.
14. AI legal-action infrastructure — VERIFIED for ordinary audited actions.
15. AI tactical policy — BLOCKING for narrative-objective policies including rescue-first, protect-cargo/equipment, escort, search, route-clearing, calming/redirecting, objective-aware withdrawal and disengage-after-objective.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for persistent route/objective/cargo identity, rescue/non-KO objective acknowledgement and authoritative end-to-end result playback.

No category is promoted globally from one representative mechanic.

## Pass 379 boundary

V17 from Pass 378 remains the coherent world checkpoint. Pass 379 adds standalone `OUROS_NPC_ACTION_TERMINAL_PROVENANCE_V1`.

The first supported terminal family is deliberately narrow:

`TRAVEL_DESTINATION_ARRIVED`

It must reference `TRAVEL_EDGE_STARTED`, replay semantic travel to `ARRIVED`, preserve destination state and remain cross-consistent with the source action-start evidence.

The durable causal chain demonstrated by the standalone owners now reaches:

`DELIVERED -> MATERIALIZED_AS_EVIDENCE -> REPLAN_TRIGGER_CREATED -> REPLAN_TRIGGER_CONSUMED -> PLAN_SELECTED -> ACTION_STARTED -> TRAVEL_DESTINATION_ARRIVED`

The final arrow is not yet inside one coherent world digest. A future checkpoint pass must integrate the terminal ledger after V17.

## Non-claims

Travel arrival does not establish:

- mission success;
- objective completion;
- successful handoff to another actor;
- sample/equipment preservation;
- AutoPTU resolution;
- AutoPTU result ingress;
- Minecraft playback completion.

For AutoPTU, the boundary remains:

`AUTOPTU_BINDING_ACCEPTED != AUTOPTU_RESOLVED != AUTOPTU_RESULT_INGRESSED`

The existing semantic-result ingress contract and fixtures do not currently provide a replayable global-NPC `AUTOPTU_RESOLVED` owner tied to Pass 377 action starts. Pass 379 does not synthesize one.

## Encounter dependency note

The Pass 379 proposal `The Team That Arrived After the Window Closed` has a world-agent-only reduced version and does not require AutoPTU.

Any tactical version must gate the exact mechanics it adds. Forced movement, interception, hazards/weather phases, complex statuses, reactive terrain, move-specific control, Ability-authored effects, Items and Trainer Feature interrupts require evidence for those exact families. Objective-aware rescue, escort, search, protect-equipment and withdrawal remain AI tactical-policy blockers. Minecraft/Cobblemon/Craftics remains partial/blocking for persistent non-KO objective identity and authoritative result playback.

## Next boundary

Integrate `OUROS_NPC_ACTION_TERMINAL_PROVENANCE_V1` into a coherent world checkpoint after V17.

After that, define terminal failure/cancellation separately and add `AUTOPTU_RESOLVED` only when a live replayable owner exists. Semantic-result ingress should then be linked to the exact resolved session rather than inferred from later world state.
