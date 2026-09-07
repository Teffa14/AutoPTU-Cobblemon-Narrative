# Global NPC multiparty audience and overhearing contract — Pass 337

Status: PROPOSED CONTRACT / NON-CANON
Date: 2026-09-07

## Purpose

Pass 335 made dialogue a projection of memory, source attribution and belief. Pass 336 added conversational grounding and repair between interlocutors. Pass 337 extends that chain to conversations with more than two nearby actors without granting shared knowledge by proximity.

The target chain is:

world evidence -> actor knowledge/belief -> semantic conversational act -> audience assignment -> per-listener reception -> grounding/repair -> disclosure/relay state -> durable memory and belief consequences

Text, subtitles, voice playback and Minecraft animation remain downstream presentation.

## Core invariants

`PRESENT != PARTICIPANT`

`PARTICIPANT != ADDRESSEE`

`HEARD != ADDRESSED`

`HEARD != UNDERSTOOD`

`HEARD != BELIEVED`

`HEARD != AUTHORIZED_TO_RELAY`

`RATIFIED_SIDE_PARTICIPANT != ADDRESSEE`

`OVERHEARD != GROUNDED_WITH_OVERHEARER`

`PRIVATE_DISCLOSURE != UNOBSERVABLE_BY_DEFINITION`

`PUBLIC_LOCATION != PUBLIC_INFORMATION`

`SAME_WORDS_RECEIVED != SAME_CONTEXT_RECEIVED`

`RELAYED_CONTENT != ORIGINAL_SPEAKER_ENDORSEMENT_OF_RELAY`

## Conversation audience object

Proposed semantic object:

```yaml
ConversationAudienceFrame:
  conversation_id: null
  utterance_id: null
  speaker_id: null
  addressed_actor_ids: []
  ratified_side_participant_ids: []
  known_unratified_listener_ids: []
  unknown_listener_refs: []
  audience_assignment_basis: EXPLICIT | CONTEXTUAL | PRIOR_GROUNDING | UNCERTAIN
  information_scope_ref: null
  transmission_constraint_ref: null
  created_at: null
```

`unknown_listener_refs` is for world-system observations such as an actor who could perceive the utterance but whom the speaker did not know was present. It must never reveal hidden listener identity to the speaker's planner.

## Per-listener reception object

Audience assignment is not delivery. Each listener receives an independent record.

```yaml
ConversationReception:
  reception_id: null
  conversation_id: null
  utterance_id: null
  listener_id: null
  role_at_reception: ADDRESSEE | RATIFIED_SIDE_PARTICIPANT | KNOWN_OVERHEARER | UNKNOWN_OVERHEARER
  reception_kind: FULL | PARTIAL | PARAPHRASED | NONVERBAL_ONLY | NONE
  received_content_refs: []
  omitted_content_refs: []
  uncertainty_refs: []
  perceived_source_actor_id: null
  historical_source_ref: null
  received_at: null
```

The world system may know historical provenance while the listener knows only a perceived source. Existing source-attribution rules remain authoritative for the listener's subjective memory.

## Participant-role transitions

Roles can change during one conversation.

Examples:

A side participant asks a question and becomes an active addressee in a new turn.

A speaker explicitly invites a nearby listener into the discussion.

An addressed actor leaves; a later statement is directed only to the remaining participant.

A person walks into earshot after the topic has already started and receives only later utterances.

Each transition creates a new audience frame or updates the active participation state prospectively. It does not rewrite earlier turns.

## Multiparty grounding

Pass 336 pair-scoped common ground remains the safest primitive.

For three or more actors, do not infer one universal `COMMON_GROUND(conversation)` bit. Represent grounded propositions by the exact participant set that completed or ratified the exchange.

Suggested extension:

```yaml
GroundedParticipantSet:
  grounding_id: null
  proposition_ref: null
  participant_ids: []
  evidence_utterance_refs: []
  confirmation_refs: []
  established_at: null
  superseded_by: null
```

A three-person set is valid only when the interaction gives evidence that all three ratified the same proposition/referent. Two overlapping pairwise grounds are not automatically equivalent to one three-person ground.

`GROUND(A,B) + GROUND(B,C) != GROUND(A,B,C)`

## Partial overhearing

Partial reception must be representable without fabricated sentence reconstruction.

Useful semantic forms:

- heard proposition fragment;
- heard named entity without predicate;
- heard answer without question;
- heard correction without original statement;
- heard original statement without later correction;
- heard tone/nonverbal event with no recoverable proposition;
- heard summary relayed by another actor.

The renderer can phrase uncertainty naturally, but the persistent record must retain which semantic components were actually available.

## Privacy and disclosure

This contract does not define Ouros law. It defines information-flow state needed by domain systems.

Proposed disclosure constraint values:

```text
PUBLIC
PARTICIPANTS_ONLY
NAMED_RECIPIENTS_ONLY
ROLE_SCOPED
INSTITUTION_SCOPED
SUBJECT_CONSENT_REQUIRED
RELAY_ALLOWED_WITH_REDACTION
NO_FURTHER_RELAY
UNSPECIFIED
```

These values are descriptive implementation candidates. Domain owners may later refine them.

A listener can violate a constraint and relay information anyway if actor policy, motive and capability support that action. The system records the violation as a new event; it does not make forbidden knowledge impossible to acquire.

Conversely, an actor who knows private information does not automatically reveal it merely because the player asks.

## Relay lineage

Every relay appends provenance.

```text
SOURCE_EVENT
 -> ORIGINAL_UTTERANCE
 -> LISTENER_RECEPTION
 -> LISTENER_MEMORY/BELIEF
 -> RELAY_DECISION
 -> RELAY_UTTERANCE
 -> NEW_RECIPIENT_RECEPTION
```

A relay may preserve content, omit details, paraphrase, introduce uncertainty, or intentionally distort under the existing deception policy. The original record remains unchanged.

If actor B truthfully reports to C what B heard from A, B's relay sincerity is separate from whether A's original content was true.

## Conversation privacy and player access

Player proximity does not grant UI access to every semantic utterance.

The presentation layer needs a bounded observation decision from world state. If the player character is not an eligible listener, the UI must not display the private line merely because server simulation executed it.

Likewise server logs/debug traces are not player knowledge.

`SERVER_KNOWS != PLAYER_CHARACTER_KNOWS`

## Minecraft / Cobblemon / Craftics boundary

Minecraft may provide spatial facts used by an authoritative observation service: actor positions, loaded entities, room/feature IDs and explicit interaction state.

Minecraft presentation must not decide:

- who was semantically addressed;
- whether a side participant was ratified;
- whether a listener understood;
- whether a statement was private;
- whether further relay was permitted;
- whether a correction grounded successfully;
- whether two listeners formed the same belief.

No subtitle visibility, head rotation, proximity, chat bubble or voice playback writes those semantic states by itself.

## Reduced implementation

A reduced implementation can work before acoustic simulation exists.

Use authored conversational scenes or world-agent conversation intents with explicit participant sets. Reception is deterministic from scene participation plus explicit channel/access state. Partial overhearing occurs only when an authored or simulated world event says it occurred.

This version needs no PTU battle mechanic and no generic hearing radius.

Recommended first executable fixture:

Three persistent NPCs A, B and C occupy one canonical feature. A addresses B with proposition P. C is a ratified side participant for the first turn. A then gives B a recipient-only detail Q. C receives P but not Q. B asks a clarification that establishes P' with A. C leaves before the correction and later relays P. Assertions must prove that C does not gain Q or P', while A/B retain the correction history.

## Rich implementation

A richer version may later derive candidate listeners from spatial/audio/visibility systems, doors, environmental noise, language capability, deliberate eavesdropping and communication devices.

That version must preserve this semantic boundary: perception can create a reception candidate, but cannot create addressee status, understanding, belief or permission.

If deliberate tactical eavesdropping occurs during combat, exact dependencies must be audited rather than represented with an invented generic `hearing check`.

## Integration points

This contract should consume or extend existing owners for:

- `KnowledgeMemoryLedger`;
- `ClaimRecord`;
- `BeliefState` / `BeliefRevision`;
- `SourceAttributionRecord`;
- `SimulatedConversationState`;
- Pass 335 `DialogueProjection` semantics;
- Pass 336 common-ground and repair semantics;
- communication delivery and correction history;
- care/mourning/dreams/photography/dispatch privacy scopes;
- deception motive and relay policy;
- player observation/knowledge separation.

It must not replace those systems.

## Failure cases this contract prevents

A nearby NPC learns a whole private conversation because entities share one room.

A renderer guesses the addressee from wording and writes that guess to memory.

An overhearer hears the first version, misses a correction, yet later behaves as if they received the corrected form.

Three actors receive one sentence and the engine marks universal common ground despite one actor misunderstanding the referent.

A private medical/care fact is exposed in dialogue because it exists in global world state.

A player sees an off-screen simulated conversation in debug output and the game treats the player character as informed.

A relay strips provenance and makes the newest speaker appear to be the historical source.

## Mechanical dependency classification

The reduced contract is world-agent infrastructure and has no required AutoPTU combat dependency.

A rich tactical version may depend on:

- targeting / footprints / range / LoS if line-of-sight or explicit tactical visibility matters;
- base movement legality if actor position changes determine observation eligibility;
- complete movement for interception, forced relocation or pursuit while attempting to observe/communicate;
- action economy / initiative if listening, warning, communication or interruption becomes a tactical action;
- full turn / round lifecycle for corrections or information arriving at exact round phases;
- terrain / weather / hazards / zones / reactions for noise, occlusion or reactive communication zones when such rules are actually supported;
- move-specific behavior, abilities, items and Trainer Features/perks if any exact content changes communication/perception;
- AI tactical policy if actors must choose between attacking, warning, protecting a speaker, withdrawing or preserving secrecy;
- Minecraft/Cobblemon/Craftics adapter/playback for spatial/audio presentation and exact recipient-scoped UI.

No mechanic is assumed merely because this contract can describe the narrative state.

## Unresolved implementation questions

The next implementation review should decide:

- exact executable schema for audience frames and receptions;
- whether group common ground is stored directly or derived from explicit confirmation events;
- how conversation compression preserves recipient-specific history;
- how player characters and multiple human players enter the participant model;
- how door/room/audio systems expose perception candidates without granting semantic authority;
- how privacy constraints intersect with institutional roles and subject consent;
- how localization preserves references without changing addressee identity;
- what debug/admin tooling can display without contaminating character knowledge.
