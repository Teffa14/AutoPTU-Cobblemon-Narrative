# Global NPC memory / belief / communication contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-05
Scope: all persistent/recurring Ouros NPC world agents
Parent: `design/global-npc-world-agent-ai-contract.md`
Consumes: agenda, social/faction and world-travel layers

## Purpose

Give every named NPC one region-neutral epistemic state so observation, memory, hearsay, institutional records and later contradiction can affect decisions without granting omniscience or turning faction membership into shared consciousness.

The core separation is:

`WORLD_TRUTH != NPC_CLAIM != NPC_BELIEF != DIALOGUE`

Ouros owns world truth. This layer owns what a specific NPC has been exposed to and how strongly that agent currently supports competing interpretations.

## Claim record

A persistent claim requires a stable claim ID, subject, asserted value, source kind, source actor where applicable, semantic time, bounded confidence and a provenance root. Reports also preserve the parent claim and message that transmitted them.

Initial source kinds are direct observation, report, institutional record, authored starting knowledge and inference. These labels describe origin. They do not guarantee truth.

A remembered statement can therefore be wrong while remaining a valid record of what the NPC remembers or was told.

## Provenance lineage

Communication preserves derivation. If Alpha observes an event, tells Beta, and Beta retells it to Gamma, Gamma's report remains derived from Alpha's original observation.

Several retellings of one root cannot manufacture independent corroboration.

`MULTIPLE_RETELLINGS_OF_ONE_SOURCE != MULTIPLE_INDEPENDENT_SOURCES`

The first executable policy therefore counts at most the strongest surviving claim for each value/provenance-root pair when evaluating support.

This is an Ouros evidence heuristic, not a PTU rule and not a statement of real-world probability.

## Communication

Information moves only through an explicit channel such as a message, conversation result, accessible record or authored observation event.

Shared faction membership, shared location or relationship state does not copy private claims between ledgers.

Trust can affect how much confidence survives a report. It cannot convert a report into direct observation, improve the claim above its source confidence or change world truth.

`TRUSTED_SPEAKER != INFALLIBLE_SPEAKER`

The current executable attenuation is deterministic and versioned in `tools/global_npc_memory.py`. Content must not treat its numeric score as a psychological measurement.

## Belief assessment

For a subject, the ledger groups active evidence by asserted value and independent provenance root.

Possible states are:

- `UNKNOWN`: the agent has no claim about the subject;
- `INCONCLUSIVE`: exposure exists but support does not clear the configured threshold;
- `CONTESTED`: competing values remain too close to select one safely;
- `SUPPORTED`: one value clears the threshold and required margin.

Contradiction is retained. A later observation does not delete an earlier memory merely because the newer claim is different.

Future forgetting or explicit supersession policy may reduce active influence while preserving history; Pass 282 does not erase provenance.

## Planner integration

Only supported beliefs may be projected into the existing planner as eligible fact keys. Unknown, inconclusive or contested subjects do not silently satisfy `required_knowledge` gates.

This allows travel, investigation, social and work plans to react to what the NPC believes while keeping hidden global state unavailable.

A belief changing from `SUPPORTED` to `CONTESTED` can therefore invalidate an assumption and trigger investigation or replanning without altering the underlying world fact.

## Travel integration

A direct observation that a route is closed can support a route-state belief. A trusted report can also become sufficient under the configured policy, but it remains hearsay with provenance.

The world-route subsystem still owns actual edge availability. NPC belief about a closure may cause precautionary replanning; it does not itself close the edge for every actor.

Likewise, hearing about a secret route does not automatically grant physical permission or prove the route exists. Knowledge and permission gates remain separate.

## Social and faction integration

Directional trust from the social layer can parameterize report attenuation.

No other relationship dimension grants facts. Affinity, respect, rivalry, fear or faction standing may affect willingness to communicate or investigate, but they do not populate the receiver ledger by themselves.

Institutional records must be explicit records that an agent can access. Membership alone does not imply access to every record.

## Dialogue boundary

Dialogue may later render the current ledger: direct certainty, reported information, uncertainty, contradiction, attribution and correction.

Language generation cannot create claims, observations, permissions or world outcomes by emitting text. Any conversational information transfer must be backed by a semantic communication event recorded by this layer.

## Deliberate exclusions in Pass 282

The first seam does not implement deceptive speech, deliberate lying, memory decay, source confusion, inference chains, secret discovery permissions, mass broadcast scaling or natural-language dialogue generation. These require explicit follow-up contracts.

This avoids silently equating an interesting narrative possibility with an implemented system.

## AutoPTU boundary

Memory and communication are world-agent capabilities. Ordinary remembering, telling, questioning, investigating or replanning requires no tactical engine capability.

If a belief motivates a structured confrontation, pursuit or battle, Ouros emits `REQUEST_AUTOPTU`. Memory confidence never selects battle squares, legal Moves, targets, initiative, damage, statuses, reactions or tactical policy.

Mechanically rich encounters retain the permanent dependency families: targeting/footprints/range/LoS; base movement legality; complete movement; core calculations; action economy/initiative; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; terrain/weather/hazards/zones/reactions; move-specific behavior; Abilities; Items; Trainer Features/perks; AI legal-action infrastructure; AI tactical policy; and Minecraft/Cobblemon/Craftics adapter/playback support.

Only the exact families used by a structured encounter are required. The reduced investigation/rumor version can remain entirely in Ouros world-agent state.

## Current executable seam

Pass 282:

- `tools/global_npc_memory.py`;
- `implementation/global-npc-memory-belief-communication-fixture-v1.json`;
- `tests/test_global_npc_memory.py`.

## Canon boundary

This is global implementation architecture. Synthetic agents, route states, confidence values and messages in fixtures are not Ouros canon. No NPC, faction, rumor, route closure or regional fact is promoted by this contract.
