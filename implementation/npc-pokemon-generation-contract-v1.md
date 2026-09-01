# NPC Pokémon Generation Contract v1

Status: IMPLEMENTATION CONTRACT
Date: 2026-09-01
Depends on: `canon/npc-pokemon-dynamic-progression-v1.md`

## Purpose

This contract converts a persistent Ouros NPC Pokémon identity into a legal AutoPTU-ready battle request without freezing a static level or manually authored moveset.

## Inputs

```yaml
npc_pokemon_generation_request:
  pokemon_id: null
  owner_npc_id: null
  species_id: null
  form_id: null
  generation_seed: null
  difficulty_profile: ordinary
  level_offset_override: null
  tm_roll_probability: null
  authored_tm_moves: []
  authored_move_policy: null
  player_party:
    - pokemon_id: null
      level: null
      battle_eligible: true
  encounter_id: null
  world_event_id: null
```

## Party reference calculation

1. Filter to `battle_eligible == true`.
2. Sort levels ascending.
3. If count is odd, use middle value.
4. If count is even, average the two middle values and round to the nearest legal integer level.
5. If count is zero, return `NO_BATTLE_ELIGIBLE_PARTY`.

Default level offsets:

```yaml
supportive: -2
ordinary: 0
experienced: 1
rival: 2
```

Bosses require explicit encounter configuration.

## Effective level

```text
raw_level = party_reference_level + resolved_level_offset
effective_level = clamp_to_autoptu_legal_level(raw_level)
```

The generated BattleSpec records the effective level used for that specific encounter.

Do not write the effective level back as permanent biological canon.

## Persistent generated state

The world-state store must persist at minimum:

```yaml
npc_pokemon_generated_state:
  pokemon_id: null
  generation_seed: null
  primary_tm_roll_resolved: false
  primary_tm_roll_result: null
  primary_tm_move_id: null
  secondary_tm_rolls: []
  authored_overrides: []
```

Once a deterministic TM roll has resolved, retries reuse it.

## TM resolution

Pseudocode:

```text
function resolve_primary_tm(pokemon, authoritative_data):
    if pokemon.generated_state.primary_tm_roll_resolved:
        return pokemon.generated_state.primary_tm_move_id

    roll = deterministicRandom01(pokemon.generation_seed, "tm-primary")

    if roll >= pokemon.tm_roll_probability:
        persist resolved=true, result=false, move=null
        return null

    pool = authoritative_data.legal_tm_moves(
        species=pokemon.species,
        form=pokemon.form
    )

    if pool is empty:
        persist resolved=true, result=false, move=null
        return null

    move = deterministicChoice(pool, pokemon.generation_seed, "tm-primary-choice")
    persist resolved=true, result=true, move=move
    return move
```

The TM candidate pool must come from PTU/Caelo/AutoPTU data. Narrative or Minecraft code cannot construct it.

## Level-up move resolution

Pseudocode:

```text
level_pool = AutoPTU.levelUpMoves(species, form, effective_level)
ordered = sortByLearnLevelThenCanonicalOrder(level_pool)
active = selectLegalActiveMoves(ordered, governingMoveSlotRules)
```

Default selection prefers the most recently learned legal level-up moves.

If one persistent generated TM exists and is legal for the current build:

```text
active = integrateTM(active, tmMove, governingMoveSlotRules)
```

Default TM integration policy for v1:
- preserve the newest/highest-priority level-up options;
- replace the oldest currently selected level-up move when a slot must be freed;
- never create more active moves than AutoPTU permits;
- run final legality validation after integration.

If AutoPTU rejects the assembled set, battle generation fails closed and logs the legality reason. It must not silently substitute an arbitrary move.

## Battle snapshots

Each encounter stores a generated snapshot:

```yaml
npc_pokemon_battle_snapshot:
  pokemon_id: null
  battle_id: null
  effective_level: null
  level_reference: null
  level_offset: null
  active_move_ids: []
  generated_tm_move_ids: []
  autoptu_validation_version: null
```

Historical snapshots are immutable records.

## Anti-exploit behavior

The following do not reroll persistent generated choices:
- loading a save;
- reconnecting;
- respawning Minecraft entities;
- changing chunks;
- opening dialogue repeatedly;
- retrying the same encounter;
- changing party order.

Party composition can change the effective level because the level is intentionally encounter-derived.

Generated TM identity cannot change through those actions.

## NPC progression behavior

If the player's party reference rises, later encounters naturally produce higher effective NPC levels.

No separate XP simulation is required for recurring NPCs in v1.

This represents off-screen training and ordinary passage of campaign progression without having to simulate every NPC training session.

Narrative arcs may still record explicit training, injury, retirement, absence or decline. Those states can modify whether an NPC is available, but do not require a static level ledger.

## Current Marea profiles

```yaml
ouros.pokemon.kite:
  species: Corviknight
  difficulty_profile: experienced
  tm_roll_probability: 0.30

ouros.pokemon.pepa:
  species: Greedent
  difficulty_profile: ordinary
  tm_roll_probability: 0.20

ouros.pokemon.lumen:
  species: Heliolisk
  difficulty_profile: experienced
  tm_roll_probability: 0.30

ouros.pokemon.margin:
  species: Noctowl
  difficulty_profile: ordinary
  tm_roll_probability: 0.20

ouros.pokemon.rook:
  species: Falinks
  difficulty_profile: rival
  tm_roll_probability: 0.40
```

## Future extensions

Do not block v1 on these:
- weighted TM pools by Trainer class;
- authored signature moves;
- Nature generation;
- Ability generation;
- held-item generation;
- multiple TM bands;
- evolution events;
- team composition scaling;
- faction-specific training doctrine;
- difficulty-mode multipliers.

Each extension must remain deterministic for persistent NPC Pokémon and validated by AutoPTU before battle.

## Acceptance tests

1. Same NPC Pokémon + same saved generated state + same party reference produces same TM identity and same legal moveset.
2. Raising party median raises recurring NPC effective level according to profile.
3. Reordering party does not change reference level or TM roll.
4. Reloading does not reroll TM selection.
5. Illegal TM compatibility cannot enter BattleSpec.
6. A Pokémon with no successful TM roll uses only legal level-up moves unless authored legal overrides exist.
7. Historical battle snapshots retain old effective levels after future scaling.
8. Minecraft entity despawn/recreation cannot change generated combat state.
