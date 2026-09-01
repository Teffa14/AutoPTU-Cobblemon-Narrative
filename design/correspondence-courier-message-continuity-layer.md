# Correspondence, Courier and Message Continuity Layer

Status: DESIGN. NON-CANON UNTIL ADOPTED.
Pass: 189

## Purpose

This layer gives Ouros a persistent model for correspondence without creating a universal postal service or replacing existing authority, provenance, custody, archive, notice, rumor, routing or quest systems.

The design answers six separate questions:

1. What message exists?
2. Who claims to have issued it?
3. Where is each physical or projected copy?
4. Who currently has custody of the addressed copy?
5. What delivery, reading and acknowledgment events actually occurred?
6. Which message version is currently effective for the institution that owns the decision?

The layer must preserve uncertainty when evidence is incomplete.

## Boundary with neighboring systems

Rumor handles socially transmitted claims whose path and authority can differ from formal correspondence.

Archive and provenance systems preserve source history and documentary evidence.

Custody systems answer who physically or institutionally holds an object.

Public notice systems project selected information into the world.

Institutional authority decides who may approve, interpret, assign, close or supersede work.

Quest state tracks authored gameplay consequences.

Correspondence connects those systems but does not replace any of them.

## Core record: correspondence_message

Recommended fields:

- message_id: stable server identity;
- thread_id: optional logical chain shared by request, reply and later correction;
- message_kind: request, instruction, update, acknowledgment, reply, correction, notice-copy, invitation, report-cover, private-note or other authored type;
- claimed_sender_actor_id;
- issuing_institution_id when applicable;
- authentication_state: unreviewed, provisionally-attributed, authenticated, disputed, rejected;
- intended_recipient_actor_ids and/or intended_recipient_role_ids;
- privacy_scope: public, addressed, restricted, confidential-by-authored-policy when such policy exists;
- created_at_world_time;
- issued_at_world_time;
- effective_from and effective_until when explicitly authored;
- supersedes_message_id when applicable;
- superseded_by_message_id when known;
- content_ref or immutable content payload;
- content_revision_id;
- requested_action_ref when the message requests existing world work;
- related_case_or_quest_refs;
- archive_state;
- notes with provenance.

A message should not mutate its historical text after issuance. A correction creates another record linked to it.

## Physical and projected copies

A message may have zero, one or several representations.

Recommended correspondence_copy fields:

- copy_id;
- message_id;
- copy_kind: original, duplicate, posted-copy, sealed-packet, office-copy, transcription, projection;
- created_at;
- physical_location_ref when materialized;
- container_ref when inside a packet, crate, desk or archive box;
- current_custodian_ref;
- legibility_state;
- seal_or_mark_observations;
- currentness_projection;
- destroyed_or_missing_representation_state;
- provenance notes.

The authoritative message record survives a Minecraft entity despawn. Destroying a physical copy can matter narratively while leaving the historical record intact when another authoritative record legitimately exists.

## Delivery attempt

Recommended delivery_attempt fields:

- attempt_id;
- message_id;
- copy_id when physical;
- courier_or_holder_ref;
- intended_delivery_target;
- attempt_time;
- attempt_location;
- result;
- actual_receiver_ref if someone accepted custody;
- evidence_refs;
- reason_code when known;
- follow_up_required.

Useful result states:

- DELIVERED_TO_INTENDED_RECIPIENT;
- DELIVERED_TO_AUTHORIZED_ROLE;
- DELIVERED_TO_AUTHORIZED_CUSTODIAN;
- REFUSED;
- RECIPIENT_UNAVAILABLE;
- LOCATION_INACCESSIBLE;
- ROUTE_BLOCKED;
- RETURNED_TO_SENDER_OR_ORIGIN;
- ATTEMPT_INCOMPLETE;
- OUTCOME_UNKNOWN.

The vocabulary can be reduced during implementation. The semantic separation must remain.

## Read and acknowledgment events

Delivery does not automatically create knowledge.

Recommended read_event:

- message_id;
- actor_id;
- time;
- evidence of read/access;
- whether actor had authority to act;
- optional interpretation note.

Recommended acknowledgment_event:

- message_id;
- acknowledging actor or role;
- time;
- acknowledgment type: received, read, accepted-action, declined-action, needs-clarification;
- linked reply message when one exists.

A resident can acknowledge receipt while declining the requested work. Another can accept custody while lacking authority to decide the request.

## Message thread

A thread links records without erasing chronology.

Example:

request A -> update B -> reply C -> correction D -> acknowledgment E.

Each retains its own sender, timestamp, content and provenance. A later record can supersede a requested action while the older record remains visible as historical evidence.

## Effective current instruction

Correspondence itself should not calculate institutional authority from text.

When a message claims to issue an instruction, the owning institution evaluates:

- whether the sender or role had authority;
- whether the message was authentic;
- whether its effective window applies;
- whether another valid instruction superseded it;
- whether the recipient role has authority to execute it.

The layer may expose `effective_message_ref` after that decision. It must not decide authority from a signature texture or sender string.

## Key invariants

A sent message can remain undelivered.

A delivered packet can remain unread by the intended decision-maker.

A reader can understand a request without accepting it.

A courier can carry an instruction without gaining authority to interpret or alter it.

An addressed copy held by the wrong person does not make that person the intended recipient.

A posted notice can remain visible after a newer revision becomes effective.

A genuine old instruction can be stale today.

A reply creates a new record and does not rewrite the original.

An undeliverable letter does not prove that the recipient is missing or endangered.

A visible signature, stamp, handwriting style, wax mark or item name is evidence to evaluate, not automatic authentication.

Physical destruction of one copy does not automatically erase an archived record.

Minecraft pickup does not automatically transfer institutional custody.

Minecraft duplication does not create a second legitimate original.

A Pokémon carrying a physical message creates transport state. It does not prove the Pokémon understood the contents, intended delivery or chose the recipient unless authored evidence supports that conclusion.

Battle outcome never determines authenticity, currentness, delivery, reading, acknowledgment or institutional authority.

## Public posting

Public posting is a projection of a message or notice record.

A board or handbill should preserve:

- source message or notice reference;
- projection creation time;
- displayed revision;
- intended removal/replacement condition if known;
- actual physical presence;
- whether the projection is stale compared with current authoritative state.

This permits a board to be physically wrong while the underlying institution is correct, or vice versa if a staff record was never properly updated.

## Privacy and visibility

This layer does not invent Caelo privacy law.

Authored episodes can still distinguish practical visibility:

- public board;
- addressed packet;
- sealed packet;
- office-only record;
- archival copy with explicitly authored access.

NPC knowledge should derive from legitimate access, observation, conversation or other established systems. The player opening a sealed packet should be a world action with authored consequences when such access matters, not a UI shortcut that silently grants universal knowledge.

## Delay and autonomous world resolution

The message system should support cases where the world moves ahead while correspondence is in transit.

Examples:

- a request arrives after another resident solved the problem;
- an old route instruction arrives after a closure changed the safe path;
- a reply is written while the original courier is already returning;
- a public correction is posted before every addressed copy of the old notice is recovered;
- the player carries a packet for several world days while the receiving institution continues other work.

The message is evidence of what was known or intended at issuance time, not a time-free command over the current world.

## Quest integration

A quest may reference a message without storing all quest state inside it.

Recommended narrow transitions:

- MESSAGE_ISSUED;
- COPY_TAKEN_INTO_CUSTODY;
- DELIVERY_ATTEMPT_RECORDED;
- MESSAGE_DELIVERED;
- MESSAGE_READ_BY_ROLE;
- ACKNOWLEDGMENT_ISSUED;
- REPLY_ISSUED;
- MESSAGE_SUPERSEDED;
- COPY_RETURNED;
- THREAD_CLOSED_BY_OWNING_WORKFLOW.

The quest owns authored consequences. The correspondence layer owns documentary state.

## Minecraft / Cobblemon representation

A physical letter, parcel or board may be represented by an item, block, entity, book, UI view or custom object.

The adapter should bind that representation to stable server identifiers.

The adapter may present:

- who the visible addressee is;
- whether a packet is sealed when that is authored;
- visible marks;
- legible content once access is valid;
- whether a board copy is visibly old or damaged.

The adapter must not recompute:

- authenticity;
- institutional authority;
- effective revision;
- whether a named actor actually read it;
- whether a message counts as accepted;
- quest completion;
- sender intent.

## Pokémon transport

A future episode can use a Pokémon to carry correspondence if the world simulation can represent the behavior safely.

Default conservative contract:

- the message remains world state;
- the carrier has a current custody/transport association;
- dropping or losing the visible object can create a delivery incident;
- no generic PTU Move, Ability, Capability or Feature is invented;
- any mechanic-dependent transport action must audit that exact mechanic first.

## Failure modes that create useful stories

Wrong location, right recipient.

Right location, recipient absent.

Authorized custodian receives it, reviewer unavailable.

Old message arrives after a newer decision.

Two copies differ because one was transcribed incorrectly.

Packet arrives intact but its seal provenance is disputed.

Public board retains an obsolete revision.

Reply references the wrong earlier version.

Message is delivered but the requested action cannot be accepted.

Courier returns while the underlying issue has already resolved.

These failures should normally produce correction and follow-up rather than automatic villainy.

## Mechanically rich encounter contract

### Courier at the Glass Bend

Narrative premise:

A legitimate packet is moving between existing Marea institutions when a wild encounter makes a section of the route temporarily unsafe. The packet matters because of custody and timing. The courier is a resident, not a tactical objective token whose survival must be improvised by the battle engine.

### Intended full version

The richest version could include:

- courier and message position represented in the world;
- safe and unsafe route geometry;
- wild actors with tactical movement;
- interception or protective positioning;
- push, pull, knockback or other forced movement when selected content uses it;
- weather, hazards or zones only when the exact encounter calls for them;
- Trainer participation when explicitly authored;
- message custody and physical aftermath after combat;
- later delivery attempt and acknowledgment.

Permanent engine capability requirements when present:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle for selected content;
- terrain/weather/hazards/zones/reactions when those environmental or timing elements become tactical;
- move-specific behavior for every selected Move;
- abilities for every selected Ability;
- items for any mechanically active Item;
- Trainer Features/perks when Trainers participate mechanically;
- AI legal-action infrastructure;
- AI tactical policy when actors must reason about corridor protection, retreat, priorities or noncombatant safety;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Current classification: BLOCKED for the intended full version.

### Reduced version

The same narrative premise can run before those families are complete.

1. Courier identity, packet custody, intended route and delivery deadline remain authoritative world state.
2. When danger appears, RPG orchestration moves the courier to a safe authored position outside BattleSpec.
3. The packet remains bound to its persistent correspondence/custody records rather than becoming battle loot.
4. If an immediate wild threat still blocks passage, compile a separate ordinary battle on stable audited terrain with an exact reviewed roster.
5. AutoPTU returns only battle facts and a narrow handoff such as `IMMEDIATE_ROUTE_THREAT_WITHDREW` or `IMMEDIATE_PASSAGE_CLEAR`.
6. Narrative then evaluates whether the courier continues, turns back, transfers custody, records delay or attempts delivery later.
7. The receiving institution separately records delivery, reading and acknowledgment.

The battle cannot decide:

- whether the packet was authentic;
- whether its instruction remains current;
- whether the courier had authority to interpret it;
- whether the addressee read it;
- whether the requested work is accepted;
- whether the message counts as public knowledge;
- whether a missed delivery proves anyone is missing;
- whether a reply is required;
- whether the correspondence thread is closed.

Current classification: REDUCIBLE when the separate battle is selected entirely inside audited engine contracts.

## Implementation priority

First slice: a packet arrives at Tideglass while the normal reviewer is unavailable. A known resident can accept custody, log receipt and store it. Review remains pending until the authorized role reads it. No combat, new law or new institution is needed.

Second slice: an old public copy remains physically posted after a newer revision exists. The player can observe the mismatch; the underlying authoritative record stays stable.

Third slice: delayed addressed correspondence reaches a recipient after the requested practical problem has already resolved through autonomous world activity.

These three slices test the architecture before adding courier-route pressure.

## Canon guardrail

This layer does not canonize a postal service, mailboxes, postage, seals, literacy rates, messenger Pokémon, communication technology, privacy law, courier guild, delivery schedule, regional Caelo policy or any specific Marea message route.

It supplies a continuity contract for future authored content.