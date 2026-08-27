# Engine Readiness Snapshot — Pass 81

Status: implementation evidence snapshot, not canon.

Date: 2026-08-27

## Scope

This snapshot supports `design/competitive-scouting-replay-analysis-extension.md` and the mechanically rich Pass 81 candidates.

Writable repository for this pass:
- `Teffa14/AutoPTU-Cobblemon-Narrative`

Read-only evidence repositories:
- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Binding authority boundary

The existing Ouros runtime rule remains unchanged:

- Ouros decides persistent world facts, encounter composition and which actors enter a tactical encounter;
- AutoPTU owns tactical combatants, legality, state transitions and outcomes;
- Minecraft/Cobblemon owns world embodiment, assets, interaction surfaces, networking and presentation;
- Cobblemon battle-state/participant/controller logic never becomes tactical authority.

Required flow:

`Ouros world/scouting state -> explicit BattleSpec + bounded knowledge input -> AutoPTU authoritative state/result -> adapter -> Minecraft/Cobblemon presentation`

For Pass 81 this means a Cobblemon replay screen, visual entity, battle callback or internal mod battle object cannot establish what an opponent legally knows. Competitive knowledge comes from Ouros provenance and authoritative AutoPTU reveal events.

## Current revisions inspected

AutoPTU-Java `main`:

`3177594f92df4c5a86023ba0cb5fbac3da195e4e`

Latest inspected commit:

`Freeze and port intercept eligibility contract (#242)`

Relevant immediately preceding commits:

`0706679f4540a0f2249ccfa95fdc86dff0fcf7ea` — forced displacement collision stop reasons.

`46b03107a566deba55b9f01d2bb571632870719b` — forced displacement collisions and Push/Pull execution with runtime position mutation.

AutoPTU Python `main`:

`95899537a72fb8c85330d7488c530316a8883884`

Latest inspected merge:

`Career: keep retirement ownership summary truthful`

Recent Python work concerns ownership summaries and temporary-loan accounting in Career. It does not establish a new tactical family.

## Live Java evidence added since Pass 80

Commit #242 creates a parity-gated `InterceptEligibilityResolution` contract.

It proves an authoritative eligibility slice shared by prepared interception-related behavior:
- fainted candidates are blocked;
- Paralyzed/Stuck/Tripped/Sleep/Flinch-family conditions are checked;
- trapped-family immobilization is checked;
- coaching-based intercept permission is represented;
- Loyalty thresholds and same-controller relationships are parity-tested against pinned Python behavior;
- candidate truth is derived from AutoPTU runtime state rather than Minecraft/Cobblemon.

The implementation documentation explicitly says Minecraft/Cobblemon must not supply status, coaching or controller values directly.

This is meaningful progress inside the complete-movement/interception family.

It is not end-to-end Intercept execution.

Current evidence does not yet establish all of:
- interception event triggering/execution across every legal call site;
- reaction timing and conflicts;
- target redirection consequences;
- complete knockback behavior;
- all forced-movement sources;
- Move/Ability/Item/Trainer Feature integrations;
- tactical AI decision-making around whether to intercept;
- semantic transcript completeness;
- Minecraft/Cobblemon authoritative-event playback.

Therefore the family remains PARTIAL.

## Permanent capability map

```yaml
capabilities:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: PARTIAL
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: PARTIAL
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

Pass 81 makes no category promotion.

## Why complete movement remains PARTIAL

Current verified slices now include:
- base Shift/Jump legality from earlier parity work;
- stepwise Push/Pull forced displacement;
- boundary/blocker/living-footprint collision stops;
- large-footprint support for the displacement slice;
- runtime position mutation;
- explicit displacement stop diagnostics;
- interception candidate eligibility guards with Python parity.

The broad family still lacks sufficient evidence for complete interception execution, reactions, all knockback/forced-movement sources and their integrations.

An encounter requiring only the exact implemented Push/Pull resolver may proceed against this PARTIAL family when its contract names that exact slice.

An encounter whose premise depends on full reactive Intercept remains dependent on unverified behavior even though candidate eligibility now exists.

## Why AI tactical policy remains BLOCKING

This category is central to the intended full version of Scouted Rematch.

AutoPTU-Java already has deterministic legal-action infrastructure. That establishes which candidate `BattleChoice` objects are legal.

Current live evidence still does not establish a general tactical scoring/policy layer that:
- chooses among legal actions strategically;
- consumes a bounded prior-knowledge packet;
- differentiates known, unknown and stale opponent information;
- updates its knowledge only after current-battle reveals;
- reasons about objectives beyond raw legality;
- avoids querying hidden server state.

Pass 81 therefore must not claim that rivals dynamically counter observed player patterns in battle.

The reduced design uses static reviewed preparation choices instead.

## Battle replay and reveal event readiness

The narrative design can represent replay provenance today.

Full tactical replay/analysis needs a stronger semantic event path than current broad evidence establishes.

The Java README still lists full `BattleSpec -> BattleTranscript` parity as pending. Existing individual semantic events and parity slices are useful, but they do not prove a complete replay-quality transcript for every Move, Ability, Item, Trainer Feature, status, displacement or reaction.

Pass 81 therefore distinguishes:
- historical/public battle result — can exist through narrative/institutional state when authoritative result data exists;
- visual replay record — can exist only when an actual presentation/capture path produces it;
- mechanically confirmed reveal — should require an authoritative event or explicit reviewed disclosure;
- analyst interpretation — can exist as a claim without mechanical certainty.

## PTU/Caelo boundary

Competitive scouting is primarily an information/provenance system.

No mechanical benefit is assumed from:
- watching a replay;
- recognizing a pattern;
- taking notes;
- receiving coaching;
- studying a rival;
- knowing that a Move appeared in an old battle;
- running a mock simulation.

If future content proposes an actual mechanical consequence such as training progression, a Feature interaction, tutoring, roster legality, item preparation or an in-battle modifier, that exact effect requires governing PTU/Caelo review plus current AutoPTU support.

No generic “Scouting bonus” is introduced.

## Cobblemon reuse profile for Pass 81

The binding architecture requires aggressive safe reuse without adopting Cobblemon battle authority.

SAFE_REUSE candidates:
- Pokémon models, forms and textures in replay/analysis presentation;
- animations, poses, cries, particles and sounds;
- NPC/Pokémon overworld entities in viewing rooms and competitive venues;
- menus, screens and UI surfaces for replay browsing and notes;
- networking/client synchronization;
- server/client lifecycle hooks;
- world display props and interaction hooks;
- storage/serialization hooks that retain references to Ouros-owned replay/source IDs;
- spectator positions and venue geometry as contextual observations;
- normal Cobblemon/Minecraft world presentation around an event.

ADAPTER_REQUIRED:
- rendering an AutoPTU semantic event sequence through Cobblemon entities;
- reconstructing playback after reconnect/chunk reload;
- mapping an authoritative reveal event to a player-visible replay annotation;
- preventing a replay UI from showing current hidden state instead of historical recorded state;
- converting review interaction into an Ouros `scouting_access_event` or analysis claim;
- feeding only the Ouros knowledge packet into future AutoPTU AI policy.

BATTLE_AUTHORITY_FORBIDDEN:
- Cobblemon battle state defining what a historical Move/Ability/Item/Feature was;
- Cobblemon choosing participants for a replay/rematch;
- Cobblemon HP/status/position being treated as the historical source of truth;
- Cobblemon tactical AI being treated as the real opponent's legal adaptation model;
- any Cobblemon internal roster leaking unused/private team members into a scouting packet;
- a Minecraft entity's loaded state determining whether a past participant existed.

## Encounter readiness — Scouted Rematch

Intended full version:

A recurring opponent has genuinely viewed selected public or legally accessible battle sources. Ouros compiles their bounded knowledge packet. AutoPTU tactical AI receives only that prior knowledge plus facts exposed during the current battle. The opponent makes legal strategic choices under an approved AI policy.

Dependency status:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL where selected roster mechanics require it;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if selected arena/roster depends on the family;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version:

Ouros still compiles the same legitimate source history. A static reviewed preparation profile is chosen before battle and may alter only things the actor can legally alter through authoritative current state, such as selecting from an approved roster profile. No claim is made that AI dynamically exploits scouting during combat. AutoPTU resolves a conventional approved battle.

## Encounter readiness — Analysis Between Rounds

Intended full version:

Several official matches occur in sequence. New replay/reveal data becomes accessible at explicit publication checkpoints. Later opponents may incorporate that information through tactical AI.

Key blockers:
- complete semantic replay/reveal coverage remains incomplete;
- move/ability/item/Trainer Feature families remain partial;
- AI tactical policy remains blocking;
- adapter/playback remains blocking;
- any selected reaction/environment behavior keeps its own blocking dependency.

Reduced version:

Treat each match as a separate authoritative battle. Between battles, Ouros records only confirmed public reveals. The next opponent receives a reviewed static preparation profile. No mid-battle learning is simulated.

## Encounter readiness — Film Review Disagreement

The scene itself requires no tactical capability family.

It can execute as narrative/world-state interaction using:
- visual record provenance;
- access events;
- public result refs;
- analyst claims;
- corrections;
- source comparison.

If the players launch a practice battle afterward, that battle receives its own normal encounter contract.

## Testing implications for future AI work

Pass 81 creates several acceptance tests for the eventual tactical AI adapter:

1. Opponent A watched replay X; opponent B did not. Their prebattle knowledge packets differ even if both server processes can read the same database.
2. A Move unused in public sources is absent from the packet even if it exists on the current hidden roster.
3. A current-battle Move becomes known only after its authoritative reveal event.
4. An old replay remains unchanged after the real Trainer edits or evolves their current team.
5. A commentary claim cannot override a conflicting authoritative reveal event.
6. An inaccessible/private source cannot enter the packet without an access event.
7. Cobblemon battle objects cannot populate or mutate prior knowledge.
8. A mock-opponent result cannot write to the real Trainer's battle history.
9. Reconnect/replay reconstruction cannot accidentally expose current private state.
10. Static reduced encounters remain executable without tactical AI or Cobblemon battle-state code.

## Current unresolved mechanics

- exact semantic event/reveal coverage needed to produce replay-quality records;
- final AI policy architecture and how bounded prior knowledge is injected;
- whether PTU/Caelo provides specific Trainer Features or Skills relevant to battle analysis and what their exact legal effects are;
- how formal roster selection and rematch preparation should expose information to AI without hidden counter-picking;
- complete Intercept execution beyond current eligibility parity;
- reactions and their ordering;
- complete forced movement/knockback coverage;
- complete Move/Ability/Item/Trainer Feature registries;
- adapter playback and persistence.

## Current unresolved canon

- whether Ouros has widespread battle-replay technology;
- which battle institutions record or publish matches;
- spectator recording norms;
- access/privacy policies;
- analyst/coaching professions;
- official result disclosure fields;
- replay retention and archival practices;
- whether mock-opponent simulations exist;
- what competitive information a formal opponent is allowed to use before a challenge.

No answer is promoted by this snapshot.
