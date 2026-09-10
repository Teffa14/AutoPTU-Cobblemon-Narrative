# AutoPTU Session Identity and Contested-Result Scan — Pass 411

Status: RESEARCH / PROVENANCE ONLY
Canon authority: NONE
Date: 2026-09-10

## Repository inspection and duplicate control

The recursive repository tree at narrative head `bda0f4b1426258fd614f9e3e7a66e83c364fe632` was inspected before writing. Relevant current files were re-read, including `CURRENT_FOCUS.md`, the complete `canon/` inventory, `canon/ouros-playable-foundation-v1.md`, the Pass 410 recovery implementation/tests/contracts, `design/battle-subject-binding-contract.md`, AutoPTU semantic ingress material, the global NPC AutoPTU binding state, prior research/proposal surfaces and `sources/kairos/KAIROS_SOURCE_INDEX.md`.

The current project already preserves `active_autoptu_binding` in persistent NPC state and already defines an opaque `battle_session_id` in the battle-subject binding contract. Existing recovery text explicitly leaves durable AutoPTU session-store reconciliation unresolved. This pass therefore targets session identity rather than adding another holder-history layer.

Repository searches were used to avoid recycling prior anchors. The PTU haunted-mansion campaign log had already been processed in Pass 282 and Pass 393. Reckless Rollers material including `Let's Solve A Moidah` had already been processed in Pass 394. Those sources were not counted as new research here.

Exact-title search found no prior repository occurrence for `Pokémon Crystal Inheritance` before this pass. Exact-title search also found no prior occurrence for `Infiltrating the Illumine Gym`, even though Pokémon Rollout! has appeared elsewhere in the broader research corpus. This pass uses only the newly inspected episode-specific structure.

## Public source 1 — Pokémon Crystal Inheritance

Public references inspected:

- release discussion: https://www.reddit.com/r/PokemonROMhacks/comments/1trhyhz/crystal_inheritance_10_release/
- feature summary: https://www.pokeharbor.com/2026/06/pokemon-crystal-inheritance/

Public descriptions present a completed Crystal ROM hack built around travel between historic and modern versions of Johto, overworld puzzles that depend on the relation between those states, and branching outcomes.

Reusable Ouros structures:

- the same geographic place can support different questions after its context changes;
- evidence collected in one state can alter how a later state is interpreted;
- revisiting a known place can be meaningful without respawning the same encounter;
- environmental investigation can carry progression without battle being the only gate;
- changed context can make earlier records newly useful while leaving the earlier observation historically valid.

Ouros transformation:

Ouros does not import time travel. A comparable structure can arise through ordinary semantic time, old surveys, repaired infrastructure, seasonal site revisions, changed access or new records. The playable value comes from comparing states with provenance rather than copying a supernatural mechanic.

Excluded protected/distinctive material:

No Johto plot, named character, Celebi use, villain, dialogue, exact puzzle, historic-map layout, fakemon, crafting item, gym structure, ending or scenario is imported.

## Public source 2 — Pokémon Rollout! episode 139

Source:

https://tapestryradio.org/pokemon-rollout/2026/6/1/episode-139-lie-or-cheat-part-four-or-awkward-little-babies

The official Tapestry Radio Network page identifies Pokémon Rollout! as a real-play Pokémon Tabletop United podcast. Episode 139, published 2026-06-01, publicly describes an already-running battle continuing before the group reaches the next larger destination.

Reusable Ouros structures:

- a tactical scene can begin before one episode/session boundary and remain part of a larger world obligation afterward;
- battle continuity needs an identity stronger than presentation continuity;
- the surrounding journey or institutional objective continues to matter after combat;
- witnesses and participants may remember what they saw while an institution still needs an authoritative result record for consequences that depend on the formal result.

Ouros transformation:

A Bruma Battle Yard training or exhibition bout can become a recovery test if world state survives while an AutoPTU tactical session is interrupted. Participant memories remain ordinary claims. The persistent world must keep the bout unresolved until authoritative tactical reconciliation or a separately authorized institutional decision resolves its administrative status.

Excluded protected/distinctive material:

No Rollout! character, Chandi-region fact, gym infiltration plot, dialogue, Pokémon team, battle sequence, joke, deception scene or encounter outcome is imported.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked as a routing surface. Relevant areas include campaign/session structure around pp. 449+, encounter creation around pp. 470+, ordinary battle and tactical rules in Chapter 7, movement/terrain around pp. 382+, status around pp. 397+, hazards around p. 401, terrain/weather around pp. 404+, and Items/Gear around pp. 495+.

The index explicitly does not grant those mechanics to Ouros. Pass 411 introduces no battle-result rule, replay rule, draw rule, rematch rule, Trainer Feature, Ability, Item, Move, status, terrain effect, hazard, victory condition or institutional PTU modifier.

The canon foundation confirms Bruma Battle Yard as a local battle/training institution supporting ordinary audited Trainer battles, practice and exhibitions. It is not canonically a Gym and grants no invented badge/progression reward. A contested-result proposal can therefore use the Yard as a regression site while keeping any formal receipt/void/rematch procedure PROPOSED.

## Read-only engine evidence

AutoPTU-Java head inspected during this pass:

`2e704f13f98ef8984f156bef4e6ec4e8924db87b`

Merge PR #434: `Freeze Ball Fetch AbilityEvent trace parity`, dated 2026-09-10.

The diff adds structured `AbilityEvent` materialization for the already-audited approach-Shift effect and extends Ball Fetch oracle parity to compare actor, ability, effect, target, target HP, from/to coordinates, phase and round against the pinned Python trace.

This is useful evidence for a specific semantic event seam. It does not provide a durable cross-process battle/session owner and does not establish general recovery of an in-flight battle.

AutoPTU Python head inspected during this pass:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Latest commit remains `Career: keep battle coordinates synced after viewport resize (#237)` from 2026-08-29. Its commit text explicitly classifies the change as presentation-only and says no battle rules or outcomes change.

Both engine repositories remained read-only.

## Capability classification for the new encounter candidate

Permanent categories retain the conservative live-evidence posture.

Targeting/footprints/range/LoS: VERIFIED only in audited scopes. The reduced contested-result investigation does not require tactical targeting.

Base movement legality: VERIFIED only in audited scopes. An ordinary audited battle can use only the movement paths already admitted.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Any rich bout using ring-out displacement, interception, escort or forced repositioning remains dependent on this family.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL as a complete family. Any exact continuation of a battle from a mid-turn state would require the precise action/initiative state, so Pass 411 does not claim in-flight tactical resume.

Full turn/round lifecycle: PARTIAL. Mid-round crash recovery, delayed battle effects or phase continuation remain blocked without stronger engine evidence.

Full stateful damage pipeline: PARTIAL. Persistent post-battle HP/injury consequences require admitted authoritative result paths rather than spectator recollection.

Status lifecycle: PARTIAL. Complex statuses cannot be reconstructed from presentation state.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism. A proposed exhibition with hazards, weather phases or reactive zones must declare those dependencies individually.

Move-specific behavior: individually gated.

Abilities: PARTIAL / individually gated. PR #434 strengthens one Ball Fetch event-trace seam only.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for audited ordinary scopes. A normal admitted battle may use those scopes; administrative actions such as request-rematch, preserve-result-dispute or wait-for-authoritative-recovery are world-agent actions rather than tactical legal actions.

AI tactical policy: BLOCKING for objective-aware non-KO policies not already audited. The reduced version avoids requiring special tactical policy.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative battle-session recovery. Presentation may display a battle and its correlation token, but disappearance of entities, animation completion, UI state, disconnect or restart cannot become an authoritative outcome.

## New reusable narrative structure

A persistent world should be able to distinguish four separate facts:

1. a bout was scheduled or initiated;
2. participants/witnesses remember claims about what happened;
3. an AutoPTU session identity exists and may remain unresolved after restart;
4. an authoritative tactical result was received and admitted.

Those facts can disagree temporarily without data corruption. That disagreement creates usable story: an institution can postpone a bracket, request a rematch, ask witnesses what they saw, or hold a later obligation while the result remains formally unresolved. Exact administrative policy remains a separate canon/design decision.

## Canon effect

None.

All new narrative material in this pass is PROPOSED / NON-CANON unless an existing foundation fact is quoted as such. No established cause, institutional procedure, NPC history, battle result or PTU mechanic is silently added.
