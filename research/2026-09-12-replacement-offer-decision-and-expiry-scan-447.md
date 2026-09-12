# Replacement Offer Decision and Expiry Scan — Pass 447

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Date: 2026-09-12

## Repository review before external research

The complete recursive `main` tree at `c395ae52788b1f27428af0a74c997337c4e35bd9` was inventoried before writing. The active global-NPC focus, canon inventory, canonical questline taxonomy, assistance/renegotiation chain through Pass 446, private-knowledge and information-delivery surfaces, current tests, prior research/proposals and the Kairos source index were checked before selecting this slice.

The immediate gap is downstream of Pass 446. A responder-authored replacement offer can exist and can reach the requester through the ordinary information network, but the repository did not yet have a durable owner for accepting, rejecting or allowing those exact received terms to expire.

No canon file is changed by this pass.

## Duplicate avoidance

Repository searches were used before source selection. Frequently recurring PTU sources and campaign references such as The Reckless Rollers, Pokémon World Tour: United, Pokémon Adventures in the Millennium and the Not Presently Deceased Reflection Cave scenario already have prior Ouros research coverage, so they were not reused as primary inspiration here.

A repository search for `Stoneshard` returned no existing research hit before this pass. It is therefore used as a new structural reference.

## Source 1 — Stoneshard contracts and settlement situations

Public sources:

- https://stoneshard.com/wiki/Contract
- https://stoneshard.com/wiki/Situations

Retrieved: 2026-09-12.

The public contract documentation separates an offered contract, acceptance, a time-limited active obligation, completion/failure and turn-in. It also documents several objective families rather than reducing every contract to the same kill condition. The settlement-situation documentation adds a stronger living-world pattern: contract success or failure can affect later settlement situations, including when another mercenary resolves the contract through background simulation.

Reusable Ouros structures:

- an offer can have a real window without freezing the surrounding world;
- acceptance is a separate event from receipt or availability;
- letting a window lapse is distinguishable from an explicit refusal;
- local world consequences can consume a documented outcome later rather than being embedded inside offer transport;
- another actor can change the practical value of an opportunity while the original recipient is deciding.

Excluded material:

No Stoneshard settlements, characters, factions, dungeons, enemies, rewards, reputation values, economy, dialogue or contract plots are imported.

## Source 2 — Unofficial Voyage quest lifecycle documentation

Public source:

- https://wiki.unofficial.voyage/world/quests

Retrieved: 2026-09-12.

This public authoring documentation exposes a useful explicit state model. An available quest can be accepted, rejected or expire; an accepted quest can later be abandoned. The useful lesson for Ouros is structural: offer state, decision state and later execution state are distinct records and should not be collapsed into one mutable quest flag.

Reusable Ouros structures:

- `AVAILABLE`, `ACCEPTED`, `REJECTED` and `EXPIRED` are semantically different facts;
- expiration conditions can be driven by time or world-state change;
- accepting an offer is the boundary after which execution/progress logic becomes relevant.

Excluded material:

No schema, code, AI prompt text, quest content or implementation dependency is copied. The source is used only as a state-separation comparison.

## Source 3 — UO Enigma Adventurer's Guild contracts

Public source:

- https://wiki.uo-enigma.com/adventurersguild

Retrieved: 2026-09-12.

The public guild documentation separates rotating board opportunities, explicit acceptance, active-contract progress, turn-in, abandonment and expiration. Board refresh replaces available opportunities, while an expired active contract is removed through its own rule.

Reusable Ouros structures:

- opportunity rotation and active obligations need different owners;
- expiration should not be represented as an implicit rejection;
- later systems can react differently to abandonment, refusal and timeout;
- a time-limited opportunity can coexist with longer-lived progression.

Excluded material:

No UO setting, guild ranks, monster lists, reward values, board cadence or combat objectives are imported.

## PTU / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing aid rather than a canon or mechanic grant. It points to movement/terrain, status, hazards, weather, campaign/session structure, encounter creation, recurring rivals, gyms and bosses in the supplied PTU/Kairos material. This pass does not infer any new PTU rule from those page references.

The reduced narrative pattern implemented here requires no battle engine. It relies on semantic time, private knowledge, delivered communication and durable world-agent state.

If later accepted replacement terms lead to structured conflict, each battle dependency must be admitted independently instead of treating one implemented representative mechanic as proof of a full category.

## Read-only engine evidence

AutoPTU-Java `main` was checked at `f859888213385e313df923678b62374ac6919b22`, PR #449. Current evidence freezes the side-effect order of one Quick Switch path. That is useful narrow evidence for that specific Trainer Feature/switching route, but it does not verify complete action economy/initiative, generic reactions/interrupts or the Trainer Features/perks family.

AutoPTU Python `main` was checked at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head explicitly describes a viewport-coordinate synchronization change as presentation-only and says no battle rules or outcomes change.

Current conservative capability posture for any mechanically rich follow-up:

- targeting/footprints/range/LoS — VERIFIED only in audited scopes;
- base movement legality — VERIFIED only in audited scopes;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED only in audited scopes;
- action economy/initiative — PARTIAL;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING by exact behavior;
- move-specific behavior — individually gated;
- abilities — PARTIAL and individually gated;
- items — individually gated;
- Trainer Features/perks — individually gated;
- AI legal-action infrastructure — specialized objective verbs require explicit admission;
- AI tactical policy — BLOCKING for specialized policies until verified;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL / BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

## Ouros design extraction

A replacement offer should preserve at least four independent facts:

1. the offer was authored;
2. the requester actually received the exact terms;
3. the requester accepted or rejected them, if they acted in time;
4. the offer expired unanswered, if its real deadline passed first.

Those facts should remain available to later relationship, accountability, scheduling and quest systems. A later consequence can distinguish `declined`, `timed out`, `never delivered`, `accepted but not yet communicated back`, and `accepted replacement commitment later failed` without inventing blame from missing information.

Pass 447 implements only the requester-side durable outcome. It deliberately stops before sending that answer back or creating a replacement commitment.
