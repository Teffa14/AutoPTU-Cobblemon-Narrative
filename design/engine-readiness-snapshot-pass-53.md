# Engine Readiness Snapshot — Pass 53

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.

Date inspected: 2026-08-20

## Repositories inspected

`Teffa14/AutoPTU-Java` was inspected read-only at `dc8cc6677dcfcf830fb176458b05ad08dba9b526`.

`Teffa14/AutoPTU` was inspected read-only at `e4bb0ca38b7018710af476ce365d515a387de4e7`.

The narrative repository is the only writable destination for this pass.

## New Java evidence since Pass 52

The previous narrative snapshot used Java head `260ca29699e34d56da8fb32d43d2b6de7dba6892`.

The live head now inspected is:

`dc8cc6677dcfcf830fb176458b05ad08dba9b526`

Newest inspected change:

`Wire live Aura Storm errata through canonical post-damage state`

The slice adds/wires:

- `Aura Storm [Errata]` into the ordered post-damage hook path;
- signed final-damage adjustments rather than positive-only bonuses;
- Aura Break [Errata] inversion/expiry behavior;
- use of canonical round and Injury history;
- authoritative HP/damage-history application;
- parity tests against the Python oracle for those exact interactions.

This strengthens evidence for selected Ability behavior, post-damage state and lifecycle coherence.

It does not prove:

- full damage parity;
- complete Ability coverage;
- complete status lifecycle;
- broad reactions;
- terrain or hazards;
- forced movement/interception;
- tactical AI;
- mid-battle species transition;
- Evolution mechanics;
- Minecraft/Cobblemon playback.

The Java README still states that Python AutoPTU remains authoritative while the port is incomplete and still lists full damage, status/terrain/hazards/forced movement/reactions, complete registries, AI policy and Minecraft/Cobblemon integration as unfinished.

## Python Evolution evidence

Python Career already has a useful between-battle Evolution slice.

At inspected head `e4bb0ca38b7018710af476ce365d515a387de4e7`:

`auto_ptu/career/evolutions.py`:

- reads compiled PTU Evolution minimum-level/lineage data;
- constructs immediate Evolution edges;
- filters candidates by region and level;
- selects a deterministic candidate using the persistent seed.

`auto_ptu/career/roster.py`:

- preserves the same `pokemon.id` through Evolution;
- replaces the current `species`;
- refreshes persistent identity/Abilities;
- appends `evolution_history`;
- emits a `pokemon.evolved` timeline event.

This is strong evidence for persistent identity across a Career Evolution event.

Do not infer:

- complete PTU/Caelo Evolution-condition support;
- player consent/choice semantics;
- trade/item/friendship/location trigger completeness;
- Java parity;
- mid-battle Evolution;
- correct branch policy for important persistent Pokémon.

The deterministic Career branch selector is implementation behavior, not automatically an Ouros canon rule.

## Permanent capability map

### VERIFIED

Targeting / footprints / range / LoS.

Base movement legality.

Core calculations.

Action economy / initiative.

AI legal-action infrastructure.

These verified families do not by themselves prove that a combatant can be replaced with a new species profile in the middle of a battle.

### PARTIAL

Full turn / round lifecycle.

Full stateful damage pipeline.

Status lifecycle.

Move-specific behavior.

Abilities.

Items.

Trainer Features / perks.

The new Aura Storm [Errata] slice strengthens stateful damage and Ability evidence but does not promote either category.

### BLOCKING

Complete movement including push / pull / knockback / interception / forced movement.

Terrain / weather / hazards / zones / broad reactions.

AI tactical policy.

Minecraft / Cobblemon / Craftics adapter and playback.

## Evolution-specific non-inference gate

Never infer that:

- a level threshold forces an important Pokémon to evolve;
- current Python deterministic branching is the desired player-facing rule;
- Evolution grants consent, Loyalty, friendship or obedience;
- Evolution heals HP or Injuries;
- Evolution clears or preserves statuses unless the exact rule says so;
- Evolution automatically preserves current footprint placement inside battle;
- Evolution automatically updates initiative without a lifecycle contract;
- a new species can legally keep every old Move/Ability without authoritative refresh;
- a regional/form change is a permanent Evolution;
- Mega Evolution or another temporary transformation overwrites permanent species history;
- a Cobblemon visual/model swap proves battle-state parity.

## Additional implementation blocker — species transition contract

The permanent capability categories do not currently include a dedicated Evolution category.

For live mid-battle Evolution, narrative design must therefore record an additional explicit blocker until Java proves a canonical species-transition contract.

That contract should define:

- same persistent combatant/Pokémon identity;
- from/to species/form;
- stat/max-HP rebuild;
- HP and Injury carry-over;
- stage/status/temporary-effect carry-over;
- new footprint validation;
- movement/capability refresh;
- Move and Ability refresh;
- initiative behavior;
- delayed/queued effect references;
- legal-action regeneration;
- event ordering;
- adapter playback.

## Encounter readiness — Mountain Threshold

REDUCED version:

Battle with the current species. After the encounter, perform an authoritative between-battle Evolution transition and refresh the persistent Pokémon before the next battle.

This reduced approach can use the existing verified battle baseline plus Python/Career-style world transition when the governing PTU/Caelo rule is validated.

FULL version:

Evolution occurs during the tactical encounter and play continues.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED baseline;
- base movement legality — VERIFIED baseline;
- complete movement/forced movement/interception — BLOCKING when footprint/occupancy changes interactively;
- core calculations — VERIFIED primitives;
- action economy/initiative — VERIFIED baseline;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if involved;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED baseline;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- dedicated Java species-transition contract — BLOCKING/unverified.

## Encounter readiness — Ceremony Perimeter

REDUCED version:

Treat the wild gathering and Evolution resolutions as world state. If a battle occurs, instantiate only current combatants on a static arena. Evolution happens outside the tactical transcript unless a verified mechanic requires otherwise.

FULL version:

Persistent wild Pokémon can evolve, change occupied space and alter available legal choices during the event.

This additionally depends on tactical AI, adapter playback and possibly broad terrain/zones/complete movement. Wild-collective state never grants automatic combat bonuses.

## Encounter readiness — Mid-Match Breakthrough

REDUCED version:

Finish the match with current state. Resolve Evolution immediately afterward. Use the evolved state in the rematch or next scene.

FULL version:

Continue one battle transcript through the species change.

This remains blocked by the missing species-transition contract regardless of the existing Python Career helper.

## Canon/mechanics questions still unresolved

- Exact PTU/Caelo Evolution rules and any Caelo overrides.
- How branch choice/authorization works for player-important Pokémon.
- Whether Evolution can be delayed under the project rules and how that is recorded.
- Whether wild Evolution advances offline.
- Which temporary transformations are in Ouros canon.
- How Cobblemon preserves entity identity across species/model changes.
- Whether AutoPTU-Java will support live Evolution or only between-battle refresh initially.
- Exact carry-over semantics for HP, Injuries, statuses, stages, temporary effects and delayed effects if live Evolution is implemented.
