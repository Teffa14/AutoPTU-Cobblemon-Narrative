# Engine Readiness Snapshot — Pass 76

Status: implementation evidence snapshot, not canon.

Date: 2026-08-27

## Scope

This snapshot supports `design/pokemon-evolution-identity-continuity-extension.md` and the mechanically rich encounter candidates in Pass 76.

It also applies the runtime boundary in `design/cobblemon-runtime-authority-boundary.md`: Cobblemon is used aggressively for embodiment, assets, UI/networking and playback, while Ouros/AutoPTU retain authority over participants, battle state and mechanical outcomes.

## Inspected revisions

AutoPTU-Java `main`:

`c3b94bf4d4d5d0c3939bed027d3f9556b7c300e9`

Latest inspected change:

`Wire held-item START profiles into lifecycle (#238)`

The change wires parsed held-item START rule profiles into the live lifecycle, tests the path and respects Magic Room suppression.

AutoPTU Python `main`:

`69270e5e207774bac4a3f57b002d459efaafde1f`

Latest inspected change:

`Career: bring established rivals into featured battles`

That strengthens Career continuity but does not establish a new tactical capability family or Evolution runtime.

Cobblemon public source inspected:

- current evolution package and controllers/proxies;
- server-side `Evolution` abstraction;
- Evolution display/animation surfaces;
- tested/completed event surfaces;
- issue history demonstrating context-sensitive Evolution availability.

Cobblemon evidence is used to identify reusable adapter/presentation surfaces. It is never mechanical authority for Ouros.

## Permanent capability map

```yaml
capabilities:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: BLOCKING
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

No category is promoted in Pass 76.

## Why lifecycle remains PARTIAL

Java now has more real lifecycle ownership than in earlier passes:

- shared phase-envelope dispatch;
- live TURN_START/PHASE_CHANGE wiring;
- held-item START rule-profile parsing;
- live held-item START hook wiring;
- Magic Room suppression in that path;
- parity/tests around those slices.

This is meaningful implementation, but it does not prove complete lifecycle coverage for statuses, delayed effects, Abilities, Items, Trainer Features, terrain, reactions and every phase interaction.

## Why Items remain PARTIAL

Held-item identity, rule catalogs, START profile extraction and live START wiring now prove a broader authoritative path than one representative item hook.

Still missing for full-family verification:

- complete item registry coverage;
- all timing families;
- all consumption/replacement/suppression interactions;
- complete interaction with damage/status/Ability/Trainer Feature hooks;
- Evolution-specific item consumption where governing PTU/Caelo rules require it.

## Why Trainer Features/perks remain PARTIAL

Recent Java work has parity-backed slices such as Focused Training/Chronicler Accuracy behavior, but the complete family and all interrupt/timing interactions are not proven.

Evolution-specific Feature interactions have not been verified in this pass.

## Why adapter/playback remains BLOCKING

The project now has a strict architectural contract for how it must work, but evidence of a complete production adapter is still absent.

The required direction is:

`Ouros world state -> AutoPTU authoritative state/result -> adapter -> Minecraft/Cobblemon projection`

Forbidden:

`Cobblemon BattleState/participant/controller -> authoritative Ouros/AutoPTU fact`

For Evolution specifically, adapter readiness requires tests proving:

- stable `pokemon_id` survives projection;
- authoritative commit happens before visual species/form mutation;
- Cobblemon Evolution animation can be used without Cobblemon deciding PTU legality;
- reconnect/retry cannot duplicate mechanical effects;
- client playback failure does not rollback an already committed mechanical transition;
- Cobblemon-side spontaneous/queued Evolution cannot silently overwrite authoritative state;
- battle participant/state ownership never moves into Cobblemon.

None of that complete contract is verified yet, so the category remains BLOCKING.

## Evolution-specific readiness

Evolution is not one of the permanent battle capability categories, so Pass 76 tracks it as a cross-family implementation gate rather than inventing a seventeenth category.

```yaml
evolution_transition_readiness:
  PTU/Caelo source legality review: UNKNOWN
  branch selection ownership: UNKNOWN
  authoritative eligibility resolver: UNKNOWN
  authoritative persistent transition runtime: BLOCKING
  species/form identity revision persistence: DESIGN_READY
  stat recalculation transition: UNKNOWN
  current/max HP transition semantics: UNKNOWN
  Ability transition semantics: UNKNOWN
  Move transition semantics: UNKNOWN
  movement/capability transition semantics: UNKNOWN
  held-item consumption semantics: UNKNOWN
  Trainer Feature interactions: UNKNOWN
  mid-battle Evolution legality: UNKNOWN
  rollback/replay contract: BLOCKING
  Cobblemon presentation reuse: AVAILABLE_WITH_ADAPTER
  Cobblemon mechanical authority: FORBIDDEN
```

`DESIGN_READY` and `AVAILABLE_WITH_ADAPTER` are local implementation notes, not replacements for the permanent readiness states.

## Cobblemon reuse assessment

### Safe or desirable reuse

Public Cobblemon source demonstrates useful surfaces for:

- species/form metadata;
- Pokémon models/textures;
- cries;
- animation/display code;
- particles;
- entity identity/projection;
- UI/networking;
- Evolution tested/completed event observation;
- server/client Evolution display flow.

These can reduce duplicated Minecraft work.

### Adapter-only reuse

Cobblemon's current server-side Evolution API can determine results and perform side effects such as optional queueing and item handling. Those are exactly the portions that must sit behind the Ouros authority boundary.

The project may use those classes as reference or selectively reuse presentation/data surfaces, but it must not call them as the canonical PTU resolver unless a future adapter explicitly proves that the result has already been authorized and no duplicate mechanical side effect can occur.

### Explicitly forbidden

- Cobblemon Battle/BattleState ownership;
- Cobblemon participant selection;
- Cobblemon tactical HP/status/initiative legality as source of truth;
- Cobblemon battle AI deciding Ouros actions;
- Cobblemon Evolution resolution choosing canonical PTU branches;
- Cobblemon consuming authoritative battle/progression resources before AutoPTU commit.

## Encounter: Evolution During a Challenge

Intended full version depends on:

- targeting/footprints/range/LoS — VERIFIED, transition-specific footprint evidence still required;
- base movement legality — VERIFIED, transition-specific movement evidence still required;
- core calculations — VERIFIED, Evolution recalculation slice unverified;
- action economy/initiative — VERIFIED, transition timing unverified;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING if an autonomous actor must adapt;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Additional blockers outside the permanent categories:

- PTU/Caelo confirmation that mid-battle Evolution is legal;
- authoritative Evolution transition runtime;
- exact HP/status/Ability/Move continuity contract;
- rollback/replay semantics.

Reduced implementation now:

Resolve the current ordinary legal battle first. Apply Evolution afterward as a separate reviewed progression transaction once authoritative Evolution support exists. A later battle starts from the new state. No Minecraft script or Cobblemon battle object simulates mid-battle Evolution.

## Encounter: Protected Observation Window

Full version may depend on:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if route protection uses those mechanics;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING when active environmental mechanics matter;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced implementation now:

Withdraw observers in world state first, use a reviewed static ordinary battle if a confrontation is needed, then resume observation afterward. The battle result never causes Evolution.

## Read-only engine conclusion

AutoPTU-Java and AutoPTU were inspected only. No files were changed in either repository.

The Java head contains real incremental progress in Items/lifecycle. It does not justify promoting any permanent family, and it does not establish Evolution execution.

Python's latest Career-rival continuity change is relevant to persistence philosophy but does not change tactical readiness.

## Promotion evidence needed next

For Evolution runtime promotion:

1. exact PTU/Caelo rules extracted into a reviewed contract;
2. Python oracle behavior identified or added by its own engine project;
3. Java parity for eligibility/result and all changed mechanical state;
4. atomic persistent identity test using the same `pokemon_id`;
5. rollback/replay tests;
6. adapter tests proving Cobblemon is projection/playback only;
7. no dependency on Cobblemon BattleState or participant authority;
8. exact encounter-category dependencies verified separately.
