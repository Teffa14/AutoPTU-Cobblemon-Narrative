# Pass 264 research — quarantined aftermath reconciliation

Status: RESEARCH / PROVENANCE. No canon promotion.
Date: 2026-09-04

## Question

When AutoPTU-shaped aftermath reaches Ouros but fails a current subject/capability admission gate, how should Ouros retain, review and eventually resolve that information without mutating PTU truth, losing provenance, or treating elapsed time/retry as evidence?

This follows Pass 262 semantic-result ingress and Pass 263 battle-subject binding/capability admission. It does not reopen identity resolution, observation grading, population accounting, or semantic-horizon design already covered by earlier passes.

## New public sources

### iNaturalist — Data Quality Assessment

Source: iNaturalist Help, “What is the Data Quality Assessment (DQA) and how do observations qualify to become Research Grade?”
https://help.inaturalist.org/en/support/solutions/articles/151000169936

Reusable structure: an observation can remain useful while its current confidence/quality classification changes as identifications or quality assessments change. A prior Research Grade observation can move back to Needs ID when the community identification changes. The durable observation and the current assessment are separate concepts.

Ouros adaptation: quarantine should preserve the immutable result envelope/receipt while review state can change. Re-evaluation does not rewrite the original producer claim. Player/NPC observations can gain or lose confidence independently from whether a PTU consequence is admitted.

Not imported: community voting thresholds, Research Grade terminology, taxonomic workflow, or any claim that collective agreement can adjudicate PTU mechanics.

### Amazon EventBridge — dead-letter queues

Source: Amazon EventBridge User Guide, “Using dead-letter queues to process undelivered events in EventBridge.”
https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-dlq.html

Reusable structure: failed events can be retained together with failure metadata, then processed later after the underlying problem is resolved. The record of failure and retry attempts helps reconciliation instead of requiring the producer to fabricate a new event.

Ouros adaptation: quarantined semantic results keep the original envelope, immutable reason snapshot, receipt identity and review history. A later capability admission or subject-lineage repair triggers an explicit reconciliation attempt against that same result identity.

Not imported: SQS, AWS retry timings, cloud infrastructure, or generic TTL behavior. Pass 261 already prohibits treating arbitrary elapsed time as semantic expiry.

### Azure Event Grid — delivery, retry and dead-letter reconciliation

Source: Microsoft Learn, “Azure Event Grid Delivery and Retry Explained.”
https://learn.microsoft.com/azure/event-grid/delivery-and-retry

Reusable structure: retryable delivery failure and non-retryable/configuration failure are different classes; undelivered events may be dead-lettered for later reconciliation; duplicate delivery can occur.

Ouros adaptation: distinguish transient transport retry from semantic quarantine. Replaying the same semantic result cannot change admission. Review happens only when relevant authority/evidence state changes. This complements the idempotency rule introduced in Pass 262.

Not imported: Azure HTTP status mapping, retry schedule, cloud delivery guarantees, or TTL values.

### Pokémon Legends: Arceus — repeated survey loop

Source: official Pokémon Legends: Arceus gameplay site.
https://legends.arceus.pokemon.com/en-us/gameplay/

Reusable structure: repeated visits to the same area, including at different times, produce additional discoveries; research progression comes from continued study rather than a single contact. Base camps support a fieldwork loop.

Ouros adaptation: a post-battle ecological aftermath can become an investigation loop. The player can return, observe gait, feeding, roost use, avoidance or recovery cues, and add knowledge records. Those observations can explain the world and guide later review, but cannot manufacture PTU Injury/status state.

Not imported: Pokédex task counts, Hisui institutions, catching requirements, named characters or plot.

### Pokémon Tabletop United campaign log — environmental consequence and repair

Source: r/PokemonTabletop, “campaign log #24” (2022).
https://www.reddit.com/r/PokemonTabletop/comments/wudfhz

Reusable structure: a player damages part of the environment, discovers a guarding Pokémon/eggs context, then takes a restorative action rather than resolving the situation only through combat. The encounter consequence remains meaningful after the immediate interaction.

Ouros adaptation: aftermath scenes can present observable ecological consequences and corrective player actions while withholding mechanical claims that the engine did not adjudicate.

Not imported: the campaign’s characters, exact Pokémon encounter, dialogue, location, sequence, or plot.

## PTU / project cross-check

PTU 1.05 treats Injury as a mechanical condition with downstream combat and recovery effects. The current Ouros authority policy therefore remains correct: observation of limping, animation damage, entity velocity or a Minecraft health event cannot create a PTU Injury. A semantic result must come through the adopted AutoPTU rules path.

The current narrative source policy keeps PTU as the mechanical baseline and treats Caelo/Kairos as references unless a rule is explicitly adopted. No local Caelo source pack was found in the current narrative tree during this pass, so no Caelo-specific claim is inferred. Kairos remains reference material only under the existing authority policy.

AutoPTU-Java live head inspected for this pass: `136c8d9a7d124849954748c780b12a0e1faf28e0`. Recent work routes AoE move-special registry construction through runtime composition. This is useful path evidence but does not expose a public durable-aftereffects API and does not verify the full damage/status families.

AutoPTU Python oracle live head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change is presentation-only and explicitly does not alter battle rules/outcomes.

## Design conclusions

Quarantine is durable audit state, not a delayed mutation queue.

A quarantined result must retain its original identity and immutable producer payload. Review adds metadata; it does not edit the envelope into something that would have passed.

Retry alone cannot change semantic disposition. Reconciliation requires a relevant evidence transition such as a newly admitted exact producer path, restored subject lineage, an adopted rules-profile compatibility mapping, or an explicit operator decision to permanently reject/archive an irreparable record.

Player/NPC observations can accumulate while a mechanical result is quarantined. They remain knowledge evidence. They cannot vote a PTU Injury/status into existence.

A battle binding may retire after quarantine receipts are safely persisted. Reconciliation must use the preserved binding/lineage proof and original session record rather than reopening a live combat session.

## Proposed lifecycle vocabulary

`QUARANTINED_OPEN`

`REVIEW_BLOCKED_NO_CHANGE`

`RECONCILIATION_ELIGIBLE`

`RECONCILING`

`ADMITTED_COMMITTED`

`PERMANENTLY_REJECTED`

`ARCHIVED_UNRESOLVED`

These names are proposal-level. They do not alter canon or engine state.

## Unresolved questions

The production store and index for quarantine receipts remain undefined.

The exact event that announces a new `SEMANTIC_RESULT_ADMISSION_V1` record from AutoPTU-Java remains undefined.

There is no verified public semantic-result export API in Java yet, so production Injury/status reconciliation remains blocked.

The retention policy for irreparable quarantine records needs an audit/archive rule distinct from ecological semantic horizons.

The UI must decide how much uncertainty is player-visible without exposing private result IDs, subject bindings, capability states or engine internals.
