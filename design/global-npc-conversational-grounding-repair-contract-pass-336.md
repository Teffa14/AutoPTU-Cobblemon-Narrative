# Global NPC conversational grounding and repair contract — Pass 336

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-07
Scope: all persistent/recurring Ouros NPC world agents
Parent: `design/global-npc-belief-aware-dialogue-projection-contract-pass-335.md`
Research basis: `research/2026-09-07-conversational-grounding-repair-common-ground-scan-336.md`

## Purpose

Add an explicit conversation-state seam between belief-aware dialogue projection and rendered conversation so two interlocutors can establish, fail to establish, repair and later reuse shared references without creating omniscience or rewriting evidence.

The design is region-neutral. Marea and Puerto Bruma are regression/content bindings only.

## Authority chain

Existing world-agent state remains authoritative for what each actor can access:

`world truth / events`
`-> observations and received information`
`-> private claim ledgers`
`-> current retrieval`
`-> subjective source attribution`
`-> belief assessment`
`-> dialogue projection`

Pass 336 adds:

`dialogue projection`
`-> semantic conversational act`
`-> addressee response / repair signal`
`-> grounding assessment`
`-> pair-scoped conversational state`
`-> rendered continuation`

Rendered wording remains downstream.

A language model may phrase a semantic act. It may not decide that grounding succeeded, invent a referent, add participants or mutate hidden world facts.

## Core invariants

`SPEAKER_KNOWS_X != PAIR_GROUNDED_X`

`UTTERANCE_PRODUCED != UTTERANCE_UNDERSTOOD`

`HEARD != ACCEPTED_AS_UNDERSTOOD`

`ACKNOWLEDGED != BELIEVED`

`BELIEVED != WORLD_TRUTH`

`REFERENT_GROUNDED != REFERENT_GLOBALLY_NAMED`

`COMMON_GROUND(A,B) != COMMON_GROUND(A,C)`

`OVERHEARD != GROUNDED_WITH_OVERHEARER`

`REPAIR_COMPLETED != ORIGINAL_UTTERANCE_ERASED`

`PARAPHRASE_ACCEPTED != EVIDENCE_STRENGTH_CHANGED`

## Pair-scoped common-ground record

A minimal persistent record may use:

```text
CommonGroundEntry {
  grounding_id
  participant_ids[]
  topic_id
  proposition_or_referent_id
  grounding_kind
  source_utterance_id
  grounding_evidence_act_id
  semantic_time
  scope
  status
  supersedes_grounding_id?
}
```

Recommended `grounding_kind` values:

- `REFERENT`
- `PROPOSITION_UNDERSTANDING`
- `TASK_INSTRUCTION`
- `TIME_REFERENCE`
- `SOURCE_REFERENCE`
- `SCOPE_REFERENCE`

Recommended `status` values:

- `PROPOSED`
- `GROUNDED`
- `DISPUTED`
- `REPAIRED`
- `SUPERSEDED`

This record captures conversational coordination. It does not copy the private evidence ledger and does not state that the grounded proposition is true.

## Semantic conversational acts

A conversation runtime should use inspectable acts rather than infer world consequences directly from generated prose.

Core acts:

- `ASSERT_OR_REPORT`
- `ASK`
- `ACKNOWLEDGE_HEARING`
- `ACKNOWLEDGE_UNDERSTANDING`
- `ACCEPT_TASK_INSTRUCTION`
- `REQUEST_REPEAT`
- `REQUEST_REFERENT_CLARIFICATION`
- `REQUEST_TIME_CLARIFICATION`
- `REQUEST_SOURCE_CLARIFICATION`
- `REQUEST_SCOPE_CLARIFICATION`
- `PARAPHRASE_FOR_CONFIRMATION`
- `CONFIRM_PARAPHRASE`
- `REJECT_PARAPHRASE`
- `SELF_CORRECT`
- `CORRECT_PRIOR_UTTERANCE`
- `DECLINE_DISCLOSURE`

The renderer may realize the same act with different character voice. The semantic act is the persistent/auditable object.

## Acknowledgment boundary

A short response such as an equivalent of `okay` is ambiguous unless the semantic runtime has already resolved its function.

Possible meanings include:

- heard the message;
- understood the words;
- accepted a task;
- believed the factual content;
- merely kept the conversation moving.

These meanings cannot collapse into one flag.

For world-changing instructions, use an explicit `ACCEPT_TASK_INSTRUCTION` or another owning-system commitment event. A generic acknowledgment must not create a schedule obligation.

## Referential grounding

Two actors may use a shorthand such as `the yard`, `the lower path` or a nickname for a tool after they establish what it refers to.

A `REFERENT` common-ground entry is scoped to the participants and relevant context.

It does not rename the canonical feature globally.

If the same phrase maps to different referents for different groups, both mappings may coexist until a conversation exposes the ambiguity.

A new listener must not inherit a pair's shorthand merely by faction membership, workplace membership or physical proximity.

## Repair sequence

A repair sequence preserves all steps:

```text
repairable utterance
-> repair initiation
-> repair target
-> speaker repair / clarification
-> addressee grounding evidence
-> outcome
```

Recommended repair targets:

- `REFERENT`
- `TIME`
- `SOURCE`
- `SCOPE`
- `QUANTITY`
- `INTENDED_ACTION`
- `PROPOSITION_CONTENT`

Recommended outcomes:

- `RESOLVED`
- `PARTIALLY_RESOLVED`
- `UNRESOLVED`
- `ABANDONED`

A repair can make a task instruction actionable while leaving the underlying factual claim uncertain.

## Self-correction and other-correction

An NPC may realize they misspoke or used a locally ambiguous reference.

`SELF_CORRECT` appends a new semantic act linked to the original. It does not delete the earlier act.

Another participant may present a correction through ordinary evidence/dialogue systems. The speaker can accept, dispute or remain uncertain. Common-ground repair and private belief reassessment remain separate operations.

## Overhearing boundary

An NPC who is present may receive an authored overhearing observation if the communication system says the utterance was perceptible and privacy rules permit it.

That NPC is not a participant in the pair's grounding sequence unless they enter the conversation through an explicit act.

Overhearing can create private evidence about what was said. It cannot automatically create shared shorthand or task acceptance.

## Medium boundary

Face-to-face dialogue, a written note, radio traffic and delayed messages can provide different grounding affordances.

Pass 336 does not invent ranges, audibility values, signal quality or communication-device bonuses.

The communication owner supplies delivery and channel state. The conversation owner records only semantic acts that the medium actually supports.

A one-way notice can communicate content without proving interactive grounding. A reply-enabled channel may support explicit clarification sequences if both sides actually exchange them.

## Memory and restart

Important conversational state survives restart when future action depends on it.

Persist at minimum:

- semantically important utterance acts;
- accepted task instructions;
- unresolved repair sequences;
- pair-scoped referent mappings needed by future scenes;
- corrections that affected later action.

Do not persist every casual line as permanent world history. Compression may summarize completed low-stakes exchanges once no future system needs exact sequence identity.

Memory retrieval still governs whether an NPC can currently recall an old grounded reference. Historical common ground can exist while current recall is inaccessible.

## Dialogue projection integration

Pass 335's `DialogueProjection` supplies what the speaker may responsibly express.

Pass 336 adds a conversation packet such as:

```text
ConversationTurnContext {
  conversation_id
  speaker_agent_id
  addressee_ids[]
  dialogue_projection
  active_common_ground_ids[]
  unresolved_repair_ids[]
  candidate_referent_ids[]
  semantic_time
  channel_context
}
```

`candidate_referent_ids` must come from the speaker/listener's accessible context and authored world index. A renderer cannot invent a hidden candidate to make a phrase convenient.

## Planner integration

Grounding can unlock world-agent planning only through explicit semantics.

Examples:

- a task instruction becomes an obligation only after an owning commitment/assignment event;
- a route reference becomes usable only after the planner can resolve the grounded feature to an actual known route node;
- a correction may wake an NPC only if it materially changes knowledge, commitment or eligibility through existing replanning contracts;
- a failed repair does not create a destination or task by guessing.

## AutoPTU boundary

Conversational grounding requires no battle mechanics.

If a conversation occurs before, after or during a structured encounter, AutoPTU remains the only owner of battle legality and tactical state.

A tactical communication act would need an explicit engine contract before it can consume initiative, alter legal actions, interrupt a turn, change targets or produce a reaction. Pass 336 creates none of those mechanics.

## Minecraft / Cobblemon / Craftics boundary

Minecraft may render conversation UI, facing, gestures, subtitles and local speech indicators.

Presentation cannot infer:

- that a phrase was understood from proximity;
- that a nod meant task acceptance;
- that two NPCs share a referent because they used the same display string;
- that an overhearer joined the common ground;
- that a correction changed belief;
- that a dialogue bubble created a planner obligation.

All consequential semantics return through the world-agent conversation runtime.

## Reduced implementation

A useful first implementation can be deterministic and menu-driven.

Player-facing intents can include:

- `Which place do you mean?`
- `Which time do you mean?`
- `Who told you that?`
- `Do you mean <candidate>?`
- `Can you say that another way?`
- `I understand the instruction.`
- `I heard you, but I do not agree.`

The exact surface wording may vary. The semantic options remain explicit.

This version needs no battle handoff and no generative dialogue.

## Rich implementation

A future natural-language renderer may recognize or generate repair phrasing but must resolve it into bounded semantic acts before any durable effect.

A rich multiplayer or multi-NPC conversation may also track subgroup grounding. That extension must avoid assuming that every participant heard or accepted every contribution.

## Acceptance tests for an executable slice

1. A speaker utterance alone does not create common ground.
2. An explicit understanding acknowledgment can ground a referent without changing world truth.
3. A generic hearing acknowledgment does not create belief or task acceptance.
4. A referent clarification can repair `the yard` to one feature for one dyad while another dyad retains a different mapping.
5. A third-party overhearer does not inherit the pair's common-ground entry.
6. A self-correction preserves the original act and links the replacement.
7. An unresolved repair cannot create a planner destination by guessing.
8. A correction can remain conversationally grounded while private belief stays disputed.
9. Snapshot/restore preserves semantically important unresolved repairs and grounded referents.
10. A renderer cannot mutate common-ground state without a validated semantic act.
11. No Marea-specific condition exists in the global core.
12. No PTU/Caelo social mechanic is invented.

## Canon and rules status

This is global proposed architecture. It creates no canonical phrase, nickname, NPC belief, location label, social rule or communication mechanic.

It consumes existing canonical IDs when bound to content and preserves the authority of PTU/Caelo/AutoPTU for any mechanical action.