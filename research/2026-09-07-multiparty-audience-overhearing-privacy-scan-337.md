# Multiparty audience, overhearing and privacy scan — Pass 337

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-07

## Purpose

Pass 336 established pair-scoped conversational grounding and repair. It deliberately left multi-party conversation, overhearing and privacy unresolved.

This scan asks a narrower question: when several persistent actors are physically or socially near one conversation, which utterances can each actor legitimately receive, what conversational role did each actor occupy, and what may later be repeated?

This is not a social-skill rules pass. It does not create hearing ranges, stealth checks, eavesdropping DCs, telepathy, privacy law, deception bonuses or PTU combat mechanics.

## Repository duplication check

The complete recursive repository tree was inventoried before research. Focused repository-wide searches were then run for `overhear`, privacy, dialogue, conversation, common ground, receipt, access and communication.

Relevant prior owners already exist:

- Pass 19 contains `The Overheard Broadcast`, where a player receives only part of a public report;
- Pass 151 contains a covert-operation seed where another actor may overhear an alias;
- privacy scopes already appear in care, mourning, dreams/aura, photography, dispatch and other domain layers;
- Pass 335 owns belief-aware dialogue projection;
- Pass 336 owns pair-scoped grounding and explicitly states `OVERHEARD != GROUNDED_WITH_OVERHEARER`.

What is still missing is a reusable conversation-level audience contract that records addressee, ratified side participant, bystander/overhearer, partial reception and disclosure constraints without turning physical proximity into shared knowledge.

## Source 1 — Multi-party conversation structure and participant roles

Source:
https://aclanthology.org/2026.eacl-long.349/

Chang et al., `Multimodal Conversation Structure Understanding`, EACL 2026, models conversation structure using explicit roles and threading. Its participant-role scheme distinguishes an addressee from side participants and bystanders; the paper also reports that side participants alter conversational structure and register.

Reusable structure for Ouros:

A conversation event should identify participant role independently from entity proximity. `speaker`, `addressee`, `ratified_side_participant` and `unratified_listener` are different semantic states.

Do not import dialogue, dataset scenes, character identities or model behavior.

## Source 2 — Addressee recognition is not safe to infer from fluent text

Source:
https://aclanthology.org/2025.iwsds-1.36/

Inoue et al., `An LLM Benchmark for Addressee Recognition in Multi-modal Multi-party Dialogue`, studies triadic conversations. Explicit addressees appeared in only about one fifth of the annotated turns, and the tested LLM performed only marginally above chance on addressee recognition.

Reusable structure for Ouros:

The renderer must not decide the addressee after generating natural-language text. Addressee identity belongs in the semantic conversational act before wording is rendered. If the semantic layer does not know who was addressed, state remains uncertain rather than being guessed from a name, pronoun, gaze animation or next speaker.

## Source 3 — Side participants can listen without being the addressed party

Source:
https://aclanthology.org/2021.sigdial-1.28/

Inoue et al., `A multi-party attentive listening robot which stimulates involvement from side participants`, explicitly treats a listening side participant as distinct from the current speaker/addressee pair and explores how that listener may later be invited into the interaction.

Reusable structure for Ouros:

A ratified side participant can have legitimate access to the conversation without being the current addressee. Their receipt state must therefore be tracked separately from grounding between speaker and addressee. Later participation can promote them into an active grounding exchange, but that transition is an event rather than an automatic consequence of being present.

## Source 4 — Privacy depends on information flow, not a universal private/public bit

Sources:
https://plato.stanford.edu/archives/spr2024/entries/privacy/
https://nissenbaum.tech.cornell.edu/papers/Going%20Against%20the%20%28Appropriate%29%20Flow.pdf

The contextual-integrity literature characterizes information flow through sender, recipient, information type/attribute, subject and a transmission principle or constraint. Whether a flow is appropriate depends on context and roles rather than on every datum possessing one universal privacy property.

Reusable structure for Ouros:

A conversation record should be able to say that an actor legitimately received a claim while further forwarding is restricted, that another actor received only a redacted form, or that a piece of information was suitable for an institutional recipient but not a public bulletin.

This pass uses the structure only. It does not author real-world privacy law into Ouros.

## Source 5 — Pokémon Mystery Dungeon: request channels have different audiences

Source:
https://mysterydungeon.pokemon.com/pt-pt/world/

The official Pokémon Mystery Dungeon: Rescue Team DX site describes requests arriving through both a public Bulletin Board outside the Pelipper Post Office and letters received in the rescue team's mailbox.

Reusable structure for Ouros:

The same broad gameplay function can use channels with different intended audiences. A public posting and an addressed message should not produce identical knowledge propagation merely because both can generate a job.

Do not copy Pokémon Mystery Dungeon locations, characters, request text, plot or reward structures into Ouros.

## PTU campaign/community search result

Current searches also re-surfaced Pokémon Rollout!, Pokémon World Tour: United, The Reckless Rollers, Pokémon Adventures in the Millennium, Kairos, Zenkari, Midgarden and Pokémon Aftershocks. All have already been processed by earlier repository passes or exist as supplied comparative material.

They were not re-used as a new attribution source here. This avoids repeatedly laundering the same actual-play evidence into every communication pass.

## Ouros design lessons

### Conversational role precedes receipt

For each semantic utterance, store the intended audience role first. Delivery then determines who actually perceived some representation of it.

`PHYSICALLY_PRESENT != ADDRESSED`

`HEARD_WORDS != INTENDED_RECIPIENT`

`RATIFIED_SIDE_PARTICIPANT != CURRENT_ADDRESSEE`

### Receipt can be partial

An actor can hear only the end of a sentence, a paraphrased relay, or the answer without the question. The resulting knowledge object should reference the fragment actually received rather than silently expanding to the full source utterance.

`PARTIAL_RECEPTION != FULL_UTTERANCE_KNOWLEDGE`

### Grounding stays participant-scoped

If A asks B to confirm a referent while C merely hears the exchange, successful repair establishes common ground for the participants who actually completed the grounding sequence. C can form a belief from what C heard, but does not inherit the same grounding status automatically.

### Privacy/disclosure attaches to flows

A useful world-state record needs at minimum:

- sender;
- subject of information when relevant;
- intended recipient set;
- actual recipient/listener set;
- content/claim references;
- participant roles;
- transmission/disclosure constraint reference;
- what fragment or representation each actor received;
- semantic time and receipt time;
- subsequent relay events.

### Overhearing is an observation, not a permission grant

An unratified listener may genuinely acquire information. That changes their private knowledge state. It does not retroactively make the original disclosure intended, authorized or public.

### Natural-language generation remains downstream

A future LLM can render a semantic act differently depending on addressee and known side participants, but it cannot infer hidden audience membership, invent a privacy scope or decide that an unaddressed actor understood a message.

## Originality boundary

Pass 337 imports no protected prose, characters, plots or dialogue. External work supplies only high-level distinctions about audience roles, grounding, information flow and request channels.

All Ouros schemas, cases, NPC behavior and consequences authored from these distinctions must remain original and non-canon until reviewed.

## Mechanical boundary

No new PTU/Caelo rule is introduced here. `OVERHEARD`, `ADDRESSED`, `PARTIAL_RECEPTION`, `RATIFIED_SIDE_PARTICIPANT` and disclosure state are world-agent/information states, not PTU statuses.

If a later scene requires tactical eavesdropping, stealth, sound occlusion, telepathy, interception, sound-based Moves, Trainer Features or combat communication, each exact rule must be validated against the supplied PTU/Caelo source set and live AutoPTU capability evidence.
