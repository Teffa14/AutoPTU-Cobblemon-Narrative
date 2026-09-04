# Provisional counted-source state contract

Status: PROPOSED DESIGN CONTRACT. Does not change established species canon or PTU rules.

## Purpose

A counted anonymous population source may accumulate a small amount of individual-specific history before Ouros knows whether it deserves durable actor identity. This contract defines that bounded middle state and delegates final promotion to the Pass 258 counted-source resolution contract.

## Authority invariant

A provisional episode belongs to exactly one already-counted source. It never contributes another unit to population total. Opening, updating, expiring or promoting an episode is not birth, immigration, death, emigration, capture or release.

`population total before == population total after`

## State machine

`ANONYMOUS_COUNTED -> PROVISIONAL_ACTIVE`

From `PROVISIONAL_ACTIVE`, evaluation produces one of:

- `EPHEMERAL_ONLY`: keep bounded state until expiry or fresh evidence.
- `DURABLE_CANDIDATE`: meaningful state exists, but continuity evidence is not yet sufficient for promotion.
- `PROMOTION_REQUIRED`: durable individual consequences would be lost by aggregation and an admissible internal continuity basis exists.

Then:

- `EPHEMERAL_ONLY -> EXPIRED_TO_AGGREGATE`
- `DURABLE_CANDIDATE -> EPHEMERAL_ONLY`, `EXPIRED_TO_AGGREGATE`, or `PROMOTION_REQUIRED` as evidence changes.
- `PROMOTION_REQUIRED -> RETIRED_RESOLVED` only through Pass 258 `RESOLVE_COUNTED_SOURCE(...)`.

`EXPIRED_TO_AGGREGATE` closes the provisional episode. It does not erase public historical observations and does not destroy a population member.

## One active episode per source

Only one `PROVISIONAL_ACTIVE` episode may exist for a given `source_ref`. Opening and closing are transactional. Replaying the same transaction and payload is an idempotent no-op. Reusing a transaction ID with a different payload is rejected.

A source already in `RETIRED_RESOLVED` cannot open a new provisional episode.

## Allowed provisional state

The private episode may retain bounded references needed to evaluate continuity and durable consequences, including:

- recent observation provenance roots;
- recent site-use episodes without treating a site as identity;
- recent disturbance-response history from the ecology layer;
- short-lived projection/save-load correlation evidence;
- unresolved identity-confounder references;
- expiry and last-evaluated metadata;
- the classification `EPHEMERAL_ONLY`, `DURABLE_CANDIDATE`, or `PROMOTION_REQUIRED`.

The record stores references and compact consequences rather than cloning entire observation or actor histories.

## Forbidden state

A provisional source cannot author or infer exact PTU stats, level, HP, injuries, damage, statuses, Moves, Abilities, held items, Trainer Features/perks, tactical AI state, ownership, capture state or combatant membership. It cannot create a Minecraft entity without the existing projection/lease contracts.

Public payloads cannot expose `source_ref`, provisional episode ID, lineage proof, projection lease, persistent actor ID, transaction ID or Minecraft UUID as character knowledge.

## Durable identity pressure

Promotion pressure is qualitative and consequence-based. This contract intentionally defines no universal numeric score or sighting threshold.

Evidence that is never sufficient by itself:

- number of sightings;
- same species;
- same site;
- same time window;
- compatible appearance or ordinary behavior;
- Minecraft UUID continuity;
- one observer or relay chain repeating the same claim.

A source may become `DURABLE_CANDIDATE` when a consequence should probably remain bound to one biological individual, for example a continuing individual disturbance-response history. It becomes `PROMOTION_REQUIRED` only when both conditions hold:

1. aggregating the source would discard or misattribute a durable individual consequence; and
2. an admissible internal continuity basis identifies which already-counted source owns that consequence.

Examples of future durable consequences such as physical marker linkage, persistent injury, relationship state or quest responsibility remain PROPOSED/UNCERTAIN unless separately canonized and mechanically authorized.

## Expiry

Expiry removes private provisional linkage that no longer has a durable reason to persist. It must preserve:

- population total;
- public observation records and their original uncertainty;
- source count contribution;
- demographic history;
- provenance required to audit why the episode existed and closed.

Expiry must not rewrite earlier observations as false. A later provisional episode requires fresh continuity evidence; the old expired episode cannot be silently resurrected.

## Promotion handoff to Pass 258

When status is `PROMOTION_REQUIRED`, this layer supplies the source and admissible lineage proof to Pass 258. Pass 258 alone performs the atomic representation swap:

`anonymous sources -1`

`persistent sources +1`

`population total +0`

The provisional episode is then retired with the old source. Legitimate durable history transfers by reference to the new persistent actor. Player-facing identity state does not automatically increase.

## Restart

`PROVISIONAL_ACTIVE` episodes may survive restart only while their bounded retention policy remains valid. `PROMOTION_REQUIRED` must survive restart until resolved or explicitly invalidated by contradictory evidence. `EXPIRED_TO_AGGREGATE`, resolution transactions and retired-source guards must also survive restart sufficiently to prevent duplicate promotion.

## Engine boundary

Reduced ecology-only use does not call AutoPTU. A richer scene that generates evidence through following or interception must declare the exact permanent engine capability families it uses. This contract must never emulate missing PTU rules in the Minecraft adapter.