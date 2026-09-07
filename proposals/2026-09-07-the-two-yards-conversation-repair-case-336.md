# The Two Yards — conversation-repair case, Pass 336

Status: PROPOSED / NON-CANON
Date: 2026-09-07
Depends on: `design/global-npc-conversational-grounding-repair-contract-pass-336.md`
Uses canon regression site: Puerto Bruma

## Premise

A small but time-sensitive equipment delivery in Puerto Bruma goes to the wrong place because two work groups use the same shorthand for different destinations.

The written instruction says to leave a serviced field lamp at `the yard` before a scheduled pickup.

Sela Orrin naturally interprets `the yard` as the canonical Bruma Battle Yard. Teo Lark and one repair-row work context have been using the same shorthand for a proposed local work apron/storage area associated with repair row. Pia Min carries the instruction from a source that understood one meaning but never made the referent explicit.

No one needs to be lying, careless or incompetent. The failure is conversational coordination that was never completed.

The repair-row shorthand itself remains proposed. This file does not add a new canonical site or rename repair row.

## Why this case exists

Pass 335 lets an NPC answer from their own evidence and belief. Pass 336 needs a regression case where the factual content can be simple while the referent remains ambiguous between people.

The player should be able to solve the operational problem by asking better questions rather than discovering a hidden culprit.

## Existing canon used

The case reuses:

- Puerto Bruma;
- Bruma Battle Yard;
- repair row;
- Tideglass Archive branch;
- ferry landing if the eventual pickup uses Mina or Lia;
- Sela Orrin;
- Teo Lark;
- Pia Min;
- Lia Morn or Mina Cors as optional downstream receiver/operator.

Their canonical roles remain unchanged.

## Initial state

A field lamp or similarly ordinary serviced instrument has a persistent item instance and custody history. Its exact PTU item identity remains unresolved unless the supplied rules source establishes one; the recommended implementation treats it as narrative equipment with no combat effect.

A source instruction exists with:

- explicit item identity;
- intended delivery window;
- phrase `the yard` as the destination expression;
- source/sender identity;
- recipient identity;
- no resolved canonical feature ID attached to the phrase.

Pia receives or carries the instruction. The message can be successfully delivered while the destination referent remains under-specified.

## Conversation states

### Sela's interpretation

Sela has strong local reason to map `the yard` to Bruma Battle Yard because that is her ordinary workplace and canonical institution.

If asked only `where is the yard?`, she may responsibly answer with the Battle Yard based on her own conversational context.

If asked `which yard did Teo mean in this instruction?`, she may have insufficient evidence.

### Teo's interpretation

Teo may use `the yard` informally inside his work context for a proposed work apron/storage area at repair row.

He cannot assume Pia shares that shorthand unless their prior common-ground state says so.

### Pia's state

Pia knows the wording and source path of the instruction. She does not automatically know which physical feature the sender meant.

Her role as document courier does not grant perfect interpretation of every local shorthand.

## Player-facing repair loop

The useful questions are semantic rather than skill-gated:

- `When you say the yard, which place do you mean?`
- `Do you mean the Battle Yard or the repair-row work area?`
- `Was that the same place you meant in the original instruction?`
- `Did Pia ever confirm the destination with you?`
- `Who needs the lamp after delivery?`
- `Which pickup point is connected to the next step?`

A successful clarification produces a pair-scoped grounded referent and, where appropriate, a corrected instruction event.

The world fact changes only if an owning action changes it: someone moves the equipment, revises the instruction, reschedules pickup or records a clearer destination.

## Branches

### Early repair

The player notices the ambiguity before delivery.

Consequence: the instruction is clarified and the lamp reaches the intended destination without disruption. Historical state still records that clarification was needed.

### Wrong-place delivery, quick recovery

Pia leaves the lamp at Bruma Battle Yard under a reasonable interpretation. The intended receiver notices the missing item before pickup.

Consequence: a short retrieval/re-delivery task and a corrected note. No relationship penalty is automatic.

### Compounded misunderstanding

A later actor sees the lamp at Battle Yard and assumes the change was intentional. They relay that assumption without checking the original instruction.

Now the case exercises both Pass 335 source-aware dialogue and Pass 336 conversational repair. The relay remains sincere unless separate deception state says otherwise.

### Procedure improvement

After the incident, an institution may choose to require stable feature IDs, explicit named destinations or confirmation for time-sensitive handoffs. That procedural change is a proposed consequence and requires canon review before becoming permanent Puerto Bruma policy.

## Relationship consequences

The case must not force distrust from a simple ambiguity.

Possible authored social consequences can depend on behavior:

- asking for clarification before acting can support competence/coordination history;
- blaming someone despite clear evidence of ambiguity may create conflict through existing relationship systems;
- acknowledging one's own ambiguous instruction can create a positive repair history;
- repeated refusal to clarify can become relevant later only if authored events support it.

No automatic friendship, trust score, rivalry or reputation reward is created here.

## Reduced implementation — recommended first version

No battle is required.

Required world systems:

- persistent NPC IDs;
- semantic messages and receipt;
- Pass 335 dialogue projections;
- Pass 336 conversation acts/common-ground records;
- persistent item/custody identity;
- schedules/commitments for pickup timing;
- explicit route/location IDs;
- selective replanning when corrected instructions materially affect a task.

The lamp remains a narrative object. Moving it can be an authored world interaction rather than an AutoPTU Item action.

This version can be implemented with deterministic dialogue options and existing Puerto Bruma coordinates.

## Mechanically rich optional version

The narrative premise can coexist with a scheduled Battle Yard session. If the lamp was mistakenly delivered there, the player may arrive while an ordinary audited battle is already scheduled or about to begin.

The dialogue/equipment objective remains outside battle authority. If a separate battle occurs, its result cannot determine which destination the instruction meant.

Possible full-version battle additions and dependencies:

- ordinary trainer/Pokémon battle on static Battle Yard geometry: targeting/footprints/range/LoS, base movement legality, core calculations, action economy/initiative and AI legal-action infrastructure;
- displacement, interception or ring-out behavior: complete movement, currently partial;
- round-timed interruption or an instruction arriving during battle: full turn/round lifecycle, currently partial;
- ordinary HP/status consequences: full stateful damage pipeline and status lifecycle, currently partial as complete families;
- special arena zones, hazards, weather or reactions: terrain/weather/hazards/zones/reactions, mixed/partial/blocking by subfamily;
- exact Moves, Abilities, Items and Trainer Features: individually audited; their families remain partial;
- an AI policy that prioritizes pausing, protecting equipment or safely de-escalating instead of winning: AI tactical policy, currently blocking for this richer objective;
- faithful visible handoff in Minecraft/Cobblemon/Craftics: adapter/playback support, partial/blocking end-to-end.

The recommended version avoids every one of those richer requirements.

## Success and failure

Success is narrower than `mystery solved`.

Possible successful outcomes include:

- intended referent established;
- item delivered correctly;
- pickup rescheduled with explicit destination;
- ambiguity documented but intended referent remains historically uncertain;
- future instruction revised to use a stable feature name.

Failure can be temporary:

- missed pickup;
- item remains at the wrong location;
- repair sequence stays unresolved;
- downstream actor acts on the wrong referent;
- new clarification is needed later.

None of these author a crime or permanent relationship consequence by themselves.

## Long-term reuse

The same contract can support later stories involving:

- two historical names for one route feature;
- one nickname reused for different Pokémon or equipment;
- time phrases such as `after the ferry` that different workers anchor to different events;
- radio instructions where repetition is possible but visual pointing is not;
- multilingual/localized naming where semantic referent IDs remain stable behind different surface forms;
- old colleagues whose shorthand survives even though new staff never learned it.

The reusable asset is the conversational state, not this specific lamp.

## Canon questions

Before promotion, decide only what the implementation actually needs:

- whether repair row has an informal work apron/storage subfeature;
- whether any group really calls that place `the yard`;
- which ordinary equipment instance is involved;
- who authored the first instruction;
- who needs the item after delivery;
- whether Puerto Bruma adopts a stable-destination procedure afterward.

No answer is required for the global Pass 336 contract to exist.