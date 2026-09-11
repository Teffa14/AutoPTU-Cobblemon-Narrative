# Assistance response replanning research — Pass 427

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Retrieval date: 2026-09-11

Repository basis

The recursive narrative repository tree at `95dfae83fcd6c6846b10f8392701d65af9674818` was inventoried before writing. Current focus, canon governance, Marea resident network, Pass 422–426 assistance-request chain, private knowledge, information delivery, world-event replanning and recent source-name matches were checked first. AutoPTU-Java and AutoPTU remain read-only.

Duplicate avoidance

Recent or repeated anchors including Pokémon Burning Scales, Pokémon Pokopia, Pokémon Odyssey, Pokémon Ashen Frost, Pokémon Coda, Pokémon Nimbus, Pokémon Rejuvenation, A Farfetch'd Story 2, Roadwarden, Pentiment, Wildermyth and 80 Days were not selected as primary sources. Repository search found no prior use of `Signs of the Sojourner` as a named source. `Pokemon Reclamation` had no prior source-level match; unrelated geological reclamation material exists and is not the same source.

## Source 1 — Pokemon Reclamation

Public source: https://eeveeexpo.com/threads/9497/

The public project description records an unusual relay-development structure: four creators produced five chapters in sequence, with each chapter being handed to another person. The useful abstraction is not the comedy plot or its characters. It is the continuity property of a handoff: the next participant inherits an existing situation, but authors the next contribution rather than retroactively becoming the previous participant.

Ouros transformation: an assistance response should remain a distinct actor-owned event. When the requester receives it, the requester may form a new decision from that received state. The response must not mutate the requester's earlier decision or pretend that requester and responder shared one continuous mind.

No characters, dialogue, regime plot, chapter content or distinctive jokes are imported.

## Source 2 — Signs of the Sojourner

Public source: https://store.steampowered.com/app/1058690/Signs_of_the_Sojourner/

The public description treats communication, travel, changing relationships and consequences as persistent parts of one narrative loop. Conversations can succeed or fail, the story continues either way, travel is difficult, and later interactions reflect what happened before.

A secondary public review describes time-sensitive objectives, characters whose availability changes, and failure states that alter later conversations instead of ending the game: https://www.xboxtavern.com/signs-of-the-sojourner-review/

Ouros transformation: a delivered ACCEPT, DEFER, REJECT or COUNTERPROPOSE should change the requester's information state and open a new planning opportunity. It should not directly force the same downstream action. The requester may already have solved the problem, moved, accepted another obligation or lost the relevant window.

No card mechanics, named characters, shop premise, dialogue or route content are imported.

## Design lesson

A response is useful narrative state even when it does not cause the originally expected action. The durable sequence should remain queryable as request decision, outbound communication, recipient decision, return communication, requester receipt and requester replan. Each actor owns only their own decisions.

This supports late answers, contradictory obligations, failed coordination, graceful fallback, relationship interpretation and later accountability without requiring omniscient quest-state rewrites.

## PTU/Caelo and engine boundary

This pass adds no PTU rule. The reduced narrative version requires only semantic time, private knowledge, explicit communications, schedules, obligations, travel constraints and selective replanning.

A rich field-assistance version can later involve protection, escort, retrieval, rescue, extraction or environmental pressure. Such scenes retain the current capability posture: targeting/footprints/range/LoS VERIFIED only in audited scopes; base movement legality VERIFIED only in audited scopes; complete movement including push/pull/knockback/interception/forced movement PARTIAL; core calculations VERIFIED only in audited scopes; action economy/initiative PARTIAL; full turn/round lifecycle PARTIAL; full stateful damage pipeline PARTIAL; status lifecycle PARTIAL; terrain/weather/hazards/zones/reactions MIXED/PARTIAL/BLOCKING by behavior; move-specific behavior individually gated; abilities PARTIAL and individually gated; items individually gated; Trainer Features/perks individually gated; AI legal-action infrastructure VERIFIED only for audited ordinary actions; AI tactical policy BLOCKING for specialized objective policies; Minecraft/Cobblemon/Craftics adapter/playback PARTIAL/BLOCKING for authoritative specialized objective state, non-KO completion and in-flight recovery.

AutoPTU-Java live head checked read-only: `0415392b3391aed7329a062da159c882e0e2d43e`. Its replacement-initiative caller-policy work strengthens one initiative seam only and does not promote the action-economy family.

No canon change is proposed by this research note.