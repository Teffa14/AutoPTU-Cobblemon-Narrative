# Counted source resolution contract

Status: PROPOSED ARCHITECTURE. This contract does not canonize a new individual.

## Purpose

Convert one already-counted anonymous ecology source into one persistent individual when durable individual-specific history requires stable internal identity. The conversion changes representation, not abundance.

## Authoritative transaction

`RESOLVE_COUNTED_SOURCE(source_ref, target_persistent_ref, lineage_proof, transaction_id)`

Preconditions:

- `source_ref` exists in the authoritative ecology ledger.
- its class is `UNRESOLVED_POOL_SLOT` or an explicitly compatible counted anonymous class;
- it contributes exactly one unit to the population represented by the transaction;
- it is not retired, already resolved, or concurrently leased in a way that would create two physical presentations;
- `target_persistent_ref` does not already represent another source;
- lineage proof identifies this source specifically enough for internal continuity;
- the operation holds a source-lineage lock;
- the transaction ID has not been committed for a different payload.

Atomic commit:

- anonymous counted sources: -1;
- persistent counted sources: +1;
- population total: +0;
- demographic events: +0;
- source lineage: preserved;
- observation provenance: preserved;
- old source: `RETIRED_RESOLVED`;
- target source: `PERSISTENT_MEMBER`.

If any precondition fails, no ledger field changes.

## Identity proof classes

`INTERNAL_SOURCE_CONTINUITY` may resolve when Ouros itself can prove continuity from an already-counted source, for example an authoritative source token/lease lineage that survives the relevant lifecycle. This is an internal fact and must not be surfaced as character knowledge.

`DIEGETIC_DISCRIMINATIVE_EVIDENCE` may contribute to a reviewed identity decision when evidence genuinely distinguishes an individual, subject to Passes 253–254.

`SAME_SITE_RECURRENCE`, `SPECIES_ONLY`, `ORDINARY_RUMOR_RELAY`, and `NONDISCRIMINATIVE_BEHAVIOR_ONLY` cannot resolve a counted source by themselves.

`AMBIGUOUS_MULTIPLE_CANDIDATES` fails closed.

## Knowledge separation

Persistent identity in the ecology ledger and player-facing recognition are separate state machines.

A successful internal resolution must not automatically promote public knowledge. A character-facing record may remain `UNRESOLVED`, `POSSIBLE_SAME_INDIVIDUAL`, or `PROBABLE_SAME_INDIVIDUAL` even after Ouros has individualized the source internally.

The public payload must not contain `persistent_actor_id`, `internal_source_ref`, lease ID, lineage token, transaction ID, Minecraft UUID, or hidden population slot.

## Idempotency and concurrency

The same transaction ID with the same payload replays as a no-op returning the original resolution result.

The same transaction ID with different payload is rejected.

Two transactions cannot consume the same source. The first committed resolution retires the source; later attempts fail as `SOURCE_ALREADY_RESOLVED`.

A retired source cannot acquire a new projection lease. It cannot materialize through Cobblemon. Any later presentation must use the persistent source created by the resolution.

## History migration

Resolution attaches eligible internal histories to the persistent source by reference. It does not rewrite original observations, timestamps, confidence, provenance roots, or former uncertainty states.

Durable ecological state such as an individual response history may migrate only if the history was already attached to the source being resolved. It cannot absorb records from similar-looking candidates.

## Restart contract

After restart the ledger must preserve:

- population total;
- source-to-persistent lineage mapping;
- retired state of the old source;
- committed transaction IDs;
- migrated internal history references;
- unchanged player-facing epistemic state unless independent evidence changed it.

## Battle boundary

`RESOLVE_COUNTED_SOURCE` never creates a combatant, opens a battle, modifies PTU stats, applies status, deals damage, changes ownership, performs capture, or selects a tactical action.

If a later scene turns into pursuit or battle, normal AutoPTU admission and combatant-manifest contracts apply separately.

## Capability dependencies

Reduced implementation: Minecraft/Cobblemon/Craftics adapter/playback support is PARTIAL/BLOCKING end-to-end because the production source-lineage signal still needs adapter verification. No tactical AutoPTU family is required for the ledger conversion itself.

Mechanically rich pursuit after resolution can require targeting/footprints/range/LoS; base movement legality; complete movement when interception/blocking/forced movement occurs; action economy/initiative; full turn/round lifecycle; AI legal-action infrastructure; AI tactical policy; and adapter/playback. Damage, status, terrain/weather/hazards/zones/reactions, move-specific behavior, abilities, items, and Trainer Features/perks become dependencies only when the authored scene invokes those mechanics.
