# Counterproposal Explicit Consent Scan — Pass 434

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Date: 2026-09-11

## Repository inspection and duplicate control

The recursive repository tree at `364c34635e36d7532b6adb0a30588a34cd123942` was inventoried before writing. `CURRENT_FOCUS.md`, current canon surfaces, Passes 422–433, the world-action owner, counterproposal owner, counterproposal delivery seam, information queue, private knowledge boundary, current PTU/Kairos routing material and recent source notes were checked.

Recent anchors including Roadwarden, Pentiment, Citizen Sleeper, Citizen Sleeper 2, Six Ages, Heaven's Vault, Pyre, Unsighted, Pokémon Desolation, Pokémon Gaia, Pokémon Rejuvenation, Valoryn and recent PTU pacing material were not reused as primary sources.

Repository search found no prior named use of `Archmage Rises`. The PTU campaign-log scene below was also checked by its distinctive haunted-mansion/Sinistea/Honedge terms and returned no repository match.

## Source 1 — Archmage Rises: time-bound commitments

Public source:
https://www.gamedeveloper.com/design/rethinking-the-passage-of-time-in-rpgs

The design article describes quests as commitments with meaningful due dates. It distinguishes accepting a responsibility from later completing it, and allows the world to continue when the player does not resolve the task.

Reusable Ouros transformation:

- agreement should become a durable fact before execution;
- accepting terms does not mean the promised work already occurred;
- deadlines belong to world state rather than UI flavor;
- later failure, withdrawal or replacement by another actor should be downstream consequences instead of retroactive deletion of the original agreement.

Excluded material:

No Archmage Rises characters, dialogue, locations, quest text, economy values or distinctive plots are imported.

## Source 2 — Game Developer quest-offer / acceptance distinction

Public source:
https://www.gamedeveloper.com/design/quest-design-in-linear-media

The article separates the way an opportunity is offered from the way it is accepted or refused. The high-level lesson is useful even though Ouros does not need conventional quest UI: receiving an offer and choosing to act on it are different events.

Reusable Ouros transformation:

- a counterproposal can exist globally before the requester learns it;
- delivery can make the terms available without forcing agreement;
- acceptance should be an explicit actor-owned decision with its own provenance;
- later commitment creation can consume that decision rather than inferring consent from message receipt.

Excluded material:

No example plot, dialogue, movie material, game-specific quest, UI convention or protected prose is copied.

## Source 3 — Pokémon Tabletop United campaign log, haunted-mansion one-shot

Public source:
https://www.reddit.com/r/PokemonTabletop/comments/nwtoj5

The public campaign log records a one-session haunted-house scenario that mixed room exploration, combat, a riddle, capture opportunities, conversation and environmental interaction. The useful lesson is structural rather than fictional: a bounded PTU incident can permit several verbs and partial outcomes instead of requiring every discovered situation to collapse immediately into combat.

Reusable Ouros transformation:

- a negotiated assistance scope may authorize only one part of a broader incident;
- accepting “inspect the site” need not imply “fight everything there”;
- room/object/puzzle/social discoveries can remain world-level state until a tactical seam is actually required;
- a reduced implementation can preserve the narrative premise even when richer tactical behaviors are unavailable.

Excluded material:

No mansion layout, riddle, captured Pokémon sequence, hooded antagonist, dialogue, encounter composition or campaign character is imported.

## Combined design lesson

A counterproposal is a new offer. Delivery makes it knowable. Acceptance or rejection belongs to the receiver of that offer. Acceptance then becomes evidence for a later commitment owner; it does not itself perform the work.

This supports negotiated field work where a specialist says, in abstract terms, “later,” “elsewhere,” “diagnosis only,” or “I can provide this alternative.” The requester can explicitly accept those changed terms, reject them, or let them expire.

## Canon boundary

Nothing in this research establishes a Marea incident, a standing contract between residents, a new duty, a new site, a relationship change or a quest outcome. Existing named residents may be used as regression fixtures only where their already-canonical roles make the interaction plausible.

## PTU / Caelo mechanics boundary

The research does not promote any engine family. Negotiated agreement is world-level state. If later execution becomes tactical, every used rule family must be checked independently against live AutoPTU evidence.

Current conservative posture:

- targeting/footprints/range/LoS: VERIFIED only in audited scopes;
- base movement legality: VERIFIED only in audited scopes;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED only in audited scopes;
- action economy/initiative: PARTIAL;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact behavior;
- move-specific behavior: individually gated;
- abilities: PARTIAL and individually gated;
- items: individually gated;
- Trainer Features/perks: individually gated;
- AI legal-action infrastructure: ordinary audited actions only; specialized field verbs need explicit admission;
- AI tactical policy: BLOCKING for specialized objective policies;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for specialized objective state and non-KO resolution.

## Live read-only engine evidence

AutoPTU-Java main was inspected read-only at `536e495e91e28d65637e4f2af2ebd06bcf262940`, merge of PR #446, `Freeze Quick Switch entry contract`. This is material evidence for a specific switch-entry path. It does not verify action economy/initiative as a complete family, nor turn lifecycle, reactions or interrupts generally.

AutoPTU Python main was inspected read-only at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head remains explicitly presentation-only and states that battle rules and outcomes do not change.
