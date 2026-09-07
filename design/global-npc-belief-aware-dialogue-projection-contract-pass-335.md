# Global NPC Belief-Aware Dialogue Projection Contract — Pass 335

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-07
Scope: all persistent/recurring Ouros NPC world agents
Parent: `design/global-npc-world-agent-ai-contract.md`
Research basis: `research/2026-09-07-belief-aware-dialogue-epistemic-stance-scan-335.md`

## Purpose

Project existing NPC knowledge, current recall, subjective source attribution, uncertainty and belief into dialogue without allowing generated wording to create or rewrite world state.

This is a region-neutral global seam. Marea, Sendero, Puerto Bruma or any future place may consume it as content bindings only.

## Authority chain

Dialogue is downstream of durable state:

`world truth / event`
`-> observation or received information`
`-> durable claim ledger`
`-> current memory accessibility`
`-> subjective source attribution where present`
`-> belief assessment`
`-> dialogue projection`
`-> rendered text / voice / animation`

The projection step is read-only with respect to evidence and world truth.

`DIALOGUE_TEXT != EVIDENCE`

`DIALOGUE_FLUENCY != EVIDENCE_STRENGTH`

`NPC_SAYS_X != WORLD_TRUTH_X`

`NPC_SAYS_SOURCE_Y != ACTUAL_PROVENANCE_Y`

## Required input packet

A dialogue projection concerning a factual claim should consume an inspectable packet containing at least:

- `speaker_agent_id`;
- `topic_id`;
- `claim_id` or explicit no-claim state;
- claim content available to the speaker;
- current retrieval state;
- actual immediate source reference retained internally;
- current subjective source attribution, if one exists;
- provenance root retained internally;
- current belief assessment;
- accessible supporting and contradicting evidence references;
- semantic time of the underlying evidence;
- semantic time of the dialogue;
- conversational purpose such as answer, volunteer information, correction, warning or refusal;
- privacy/permission filters from the owning systems.

The text renderer does not receive hidden facts that the speaker cannot access merely to make dialogue more informative.

## Epistemic stance classes

Dialogue projection may expose a bounded stance derived from existing state.

Recommended semantic classes:

- `DIRECT_OBSERVATION_RECALLED` — accessible firsthand evidence;
- `REPORTED_INFORMATION_RECALLED` — accessible information received from another source;
- `CONTENT_RECALLED_SOURCE_UNCERTAIN` — content accessible while source attribution is unavailable or confused;
- `WORKING_BELIEF` — current belief supported enough to act on, while uncertainty remains;
- `CONFLICTED_EVIDENCE` — accessible evidence materially disagrees;
- `INSUFFICIENT_EVIDENCE` — the NPC lacks enough accessible evidence for a responsible factual answer;
- `PREDICTION_OR_EXPECTATION` — statement concerns a future or unresolved outcome;
- `DECLINED_OR_RESTRICTED` — information exists but cannot be disclosed under current permission/privacy state.

These are world-dialogue semantics. They are not PTU social conditions or character Skills.

## Uncertainty dimensions

The projection must distinguish uncertainty types where the underlying state supports them.

### Speaker-knowledge uncertainty

The NPC lacks access to enough evidence.

Example semantic form:

`I did not see enough to know.`

### Evidence-resolution uncertainty

The NPC has evidence but it does not distinguish competing explanations.

Example semantic form:

`The record confirms the arrival, not which route they used.`

### Source-attribution uncertainty

The NPC recalls content but cannot responsibly identify the source.

Example semantic form:

`I remember hearing that, but I cannot place who told me.`

### World-outcome uncertainty

The relevant event has not resolved yet.

Example semantic form:

`They are expected tonight; they have not arrived yet.`

These example forms demonstrate semantics only. Final dialogue style belongs to characterization/localization.

## Direct observation versus report

A dialogue answer to `what happened?` may summarize a current belief.

A dialogue answer to `what did you personally see?` must filter to accessible firsthand observations.

A dialogue answer to `who told you?` must use subjective source attribution if available and must preserve uncertainty if source access is incomplete.

A dialogue answer to `how do you know?` may project a bounded evidence summary, never hidden ledger metadata the speaker cannot know.

`ASKED_FOR_BELIEF != ASKED_FOR_OBSERVATION`

`ASKED_FOR_SOURCE != ASKED_FOR_WORLD_TRUTH`

This distinction allows investigation dialogue to become gameplay without inventing a separate interrogation minigame.

## Sincere relay boundary

An NPC may sincerely repeat a false or later-disproved claim through the ordinary information path.

The dialogue layer must preserve:

- current speaker = relaying NPC;
- claimed source = whatever subjective attribution state says;
- historical provenance = unchanged internal lineage;
- deceptive intent = absent unless the deception subsystem explicitly created it.

`SINCERE_RELAY_OF_FALSE_CLAIM != DECEPTION`

A later discovery that the upstream source lied must not retroactively mark every relay as a liar.

## Deception boundary

When a `DeceptiveStatement` exists, dialogue may project the authored assertion available to the speaker/receiver state. It must not expose the hidden basis claim or deception flag to characters who do not know it.

A language model or template system cannot decide that an NPC is lying from tone, contradiction or plot convenience.

`CONTRADICTION != DECEPTION_PROVEN`

## Retrieval boundary

Durable history can exist while current recall is inaccessible.

If retrieval returns `INACCESSIBLE`, ordinary dialogue cannot reconstruct exact content from hidden ledger state.

If retrieval returns `CONTENT_ONLY`, exact source attribution must not be fabricated.

If an archive lookup supplies external evidence, dialogue can discuss that evidence through the normal new-evidence path; the archive result does not silently become autobiographical memory.

## Publication and correction boundary

An NPC may have received:

- original publication only;
- correction only;
- both;
- neither.

Dialogue must consume that individual receipt history. It cannot answer from the latest global publication revision unless that version reached the speaker through an authorized path.

A correction does not erase the historical fact that the NPC earlier repeated or acted on the original.

## Character voice boundary

Characterization may alter:

- vocabulary;
- sentence length;
- formality;
- politeness;
- directness;
- habitual metaphors;
- whether the NPC volunteers caveats immediately or only when asked.

Characterization may not alter:

- claim provenance;
- actual evidence strength;
- belief state;
- permissions;
- remembered source;
- whether an observation was firsthand;
- canonical truth.

A confident personality can state an uncertain belief forcefully, but the underlying projection packet retains the uncertainty. A cautious personality can hedge around strong evidence without downgrading the evidence ledger.

## Proposed projection output

A renderer-facing object may use this shape:

```text
DialogueProjection {
  speaker_agent_id
  topic_id
  stance_class
  proposition
  firsthand: bool
  perceived_source_id?
  source_known: bool
  contradiction_present: bool
  uncertainty_kind[]
  semantic_evidence_time?
  semantic_dialogue_time
  disclosure_scope
  evidence_reference_ids[]
  projection_reason
}
```

`evidence_reference_ids` are audit references for the server/runtime. They are not automatically spoken to the player.

## Dialogue interaction pattern

A factual conversation can expose separate player intents without requiring free-form parsing:

- ask for current belief;
- ask what the NPC directly observed;
- ask what they were told;
- ask who supplied the information;
- ask why they currently believe it;
- present a contradiction;
- present a source/document cue;
- ask for a correction or re-evaluation.

A generative dialogue surface can phrase these naturally after the intent is resolved.

## Replanning integration

Dialogue itself does not rewrite belief.

New player-provided evidence, an identified contradiction, an archive record or a verified source correction can create ordinary evidence/communication events. Those events may update belief through existing systems and trigger selective replanning.

`CONVERSATION_OCCURRED != BELIEF_CHANGED`

`NEW_EVIDENCE_RECEIVED -> MAY_REASSESS_BELIEF`

## Persistence and replay

The projection is reproducible from persistent state at a semantic moment.

Generated surface wording does not need to be stored as world truth. If exact dialogue history matters for a quest, legal case, promise, deception or player choice, the conversation subsystem should record an explicit utterance event with its source projection and semantic time.

Restart must not cause an NPC to gain a source, lose a contradiction or access a correction they had not received.

## AutoPTU boundary

Belief-aware dialogue itself requires no battle resolution.

A conversation may produce a world intent such as investigate, confront, escort, flee or request structured resolution. Only then can the world planner emit `REQUEST_AUTOPTU`.

The dialogue layer cannot choose legal Moves, targets, positions, reactions, damage, statuses or tactical policy.

## Minecraft/Cobblemon boundary

Minecraft/Cobblemon may render speaker presence, gesture, facing, conversation UI, subtitles and local animation.

Entity proximity does not grant knowledge. Chunk load does not refresh belief. A speech bubble does not become evidence unless the conversation runtime records the corresponding communicative event.

## Reduced implementation

A reduced implementation can work now using deterministic templates keyed by:

- stance class;
- firsthand/report distinction;
- source-known/source-uncertain distinction;
- contradiction flag;
- disclosure state.

This already improves investigations because `what did you see?`, `what did you hear?` and `what do you think happened?` can return different source-backed answers.

No free-form LLM dialogue is required to validate the contract.

## Rich implementation

A future generative renderer may produce natural, character-specific dialogue from the same packet. It must be constrained so generation cannot:

- add evidence;
- invent source identity;
- collapse uncertainty;
- expose hidden truth;
- reveal deception metadata;
- grant permissions;
- change relationship state by wording alone;
- create PTU mechanics.

## Acceptance tests for a future executable slice

A region-neutral implementation should prove at minimum:

1. firsthand and relayed evidence project differently;
2. content-only recall cannot fabricate source identity;
3. inaccessible memory cannot leak into dialogue;
4. conflicting evidence produces a bounded uncertain stance instead of invented reconciliation;
5. sincere retransmission of a false claim remains non-deceptive;
6. a deceptive assertion does not expose its hidden basis to the receiver;
7. original-only and correction-aware NPCs answer differently from their actual receipt histories;
8. dialogue generation cannot mutate the knowledge ledger;
9. identical state and dialogue intent produce deterministic semantic projections;
10. no region-specific logic exists in the global core.

## Canon and rules status

This is proposed global architecture. It creates no canon NPC, location, testimony, crime, faction or event.

It adopts no PTU, Caelo, Kairos or fan-game social mechanic. No social Skill check, lie-detection rule, interrogation DC, Trainer Feature, Move, Ability or Item effect is created here.