# NPC Pokémon Dynamic Progression v1

Status: CANON-APPROVED FOUNDATION
Date: 2026-09-01

This rule applies globally to recurring Ouros NPC Pokémon unless a later canon profile explicitly opts out.

It supersedes earlier foundation language that left every recurring NPC Pokémon level and moveset unresolved.

## 1. Core rule

Recurring NPC Pokémon are persistent individuals but their combat level is not a fixed world fact.

Their identity, species, ownership/companionship history, personality, relationships and authored narrative history persist.

Their battle-ready level is generated from the player's current progression when an encounter is assembled.

This lets recurring rivals, mentors, professionals and faction members continue to develop alongside the player instead of becoming obsolete because they were introduced early.

## 2. Persistent identity versus generated combat state

Persistent:
- Pokémon persistent ID;
- nickname;
- species/form where canonized;
- Trainer or companion relationship;
- authored personality;
- authored history;
- major injuries or other governed persistent state;
- special authored TM knowledge when specifically canonized;
- generation seed;
- individual difficulty offset/profile.

Generated or derived for an encounter:
- effective level;
- level-legal move pool;
- selected active moveset;
- optional generated TM move eligibility;
- other level-derived battle values owned by AutoPTU.

`PERSISTENT_POKEMON_IDENTITY != STATIC_BATTLE_SHEET`.

## 3. Party reference level

Default NPC scaling uses the player's battle-eligible active party.

```text
party_reference_level = median(levels of battle-eligible active party Pokémon)
```

The median is preferred over the maximum so one overleveled Pokémon does not drag every recurring NPC upward.

If the party has an even number of eligible Pokémon, use the arithmetic mean of the two middle values and round to the nearest legal Pokémon level according to the implementation contract.

If no battle-eligible party exists, a battle cannot be assembled from this rule alone.

## 4. NPC difficulty offset

Each persistent NPC battle profile may define a small level offset relative to the party reference.

Default profiles:
- `supportive`: -2
- `ordinary`: 0
- `experienced`: +1
- `rival`: +2
- `boss`: encounter-specific; requires explicit authored contract rather than an unlimited generic offset

```text
effective_level = clamp_legal_level(party_reference_level + npc_level_offset)
```

The offset expresses encounter role, not permanent biological superiority.

## 5. Recurring progression

Recurring NPC Pokémon are expected to progress with the player's party.

A recurring individual therefore does not retain the numeric level it had in an earlier encounter.

Battle history may record the level used in each prior BattleSpec, but that historical snapshot does not freeze future level.

Example:
- Rook fought at effective level 14 in an early BattleSpec;
- the player later reaches a party reference near 27;
- a new Sela encounter may assemble Rook around level 29 because Sela uses a rival profile;
- the earlier battle record remains level 14.

`PRIOR_BATTLE_LEVEL != CURRENT_EFFECTIVE_LEVEL`.

## 6. No reroll-by-reentry

Random generation tied to a persistent NPC Pokémon must be deterministic from stored generation state.

Do not reroll a Pokémon's generated TM identity because the player:
- reloads;
- leaves and re-enters a chunk;
- starts dialogue again;
- forfeits and retries;
- changes active party order.

The world stores a stable random seed or resolved generated choices for that persistent Pokémon.

## 7. Level-up moveset rule

The authoritative PTU/Caelo/AutoPTU species learnset supplies the legal level-up move pool.

At encounter assembly:
1. resolve effective level;
2. resolve all level-up moves legally learned at or below that level;
3. construct the active moveset from that legal pool using the governing PTU move-slot rules;
4. prefer the most recently learned legal level-up moves by default unless an authored battle profile gives a legal alternative selection policy;
5. validate the final set through AutoPTU before BattleSpec creation.

Narrative code must never invent a move because it is thematically convenient.

## 8. Generated TM move rule

A recurring NPC Pokémon may have one or more generated TM-learned moves.

Each persistent Pokémon has:
- `tm_roll_probability`;
- a deterministic `tm_roll_seed` or stored roll result;
- a legal species-compatible TM candidate pool supplied by authoritative data;
- zero or more stored generated TM selections.

Baseline policy:

```text
if deterministic_roll(pokemon_seed, "tm-primary") < tm_roll_probability:
    generated_tm_move = deterministic_random_legal_tm(candidate_pool)
else:
    generated_tm_move = none
```

The selected TM must be legal for the species/form according to authoritative project data.

The generated TM selection persists for that individual once resolved.

The move may enter the active moveset only when the implementation can legally construct that moveset under PTU/Caelo rules.

## 9. TM probability profiles

Exact probabilities are content configuration, not PTU rules.

Ouros default narrative profiles are:
- ordinary civilian companion: 10%
- working professional partner: 20%
- experienced Trainer partner: 30%
- recurring rival partner: 40%
- specialist/boss partner: authored value, normally not greater than 60% without explicit reason

These probabilities control generated world variety only. They do not claim that PTU itself assigns those percentages.

A canon NPC may override the probability when their history supports formal training, limited resources, unusual specialization or deliberate lack of TM training.

## 10. More than one TM

The first implementation may support only one generated TM move per persistent Pokémon.

Later progression may permit additional TM rolls at authored progression bands, for example after major world-arc milestones or higher level bands.

Additional rolls must use distinct deterministic keys such as `tm-secondary` and must never replace an already established generated TM merely because a new encounter was assembled.

## 11. Evolution and form

Dynamic level scaling does not automatically evolve a persistent NPC Pokémon.

Evolution changes identity presentation and often narrative continuity, so it requires either:
- an authored progression rule;
- an explicit world event;
- or a later global evolution policy.

Level crossing an evolution threshold alone is insufficient to silently rewrite a canon persistent individual.

The same rule applies to form changes that are not purely temporary governed battle state.

## 12. Items, Abilities, Nature and Features

This policy does not randomize unsupported mechanics.

Ability, Nature, held Item, Trainer Features and other combat state must come from authoritative generation rules or explicit audited content.

They can receive separate generation policies later.

No Minecraft/Cobblemon random property may become battle authority.

## 13. Current Marea Interior application

The five foundation companions now use this global policy:
- `ouros.pokemon.kite` — Corviknight, Mara Veyra;
- `ouros.pokemon.pepa` — Greedent, Ivo Serrat;
- `ouros.pokemon.lumen` — Heliolisk, Nerea Sol;
- `ouros.pokemon.margin` — Noctowl, Taro Min;
- `ouros.pokemon.rook` — Falinks, Sela Orrin.

Initial difficulty/TM profiles:
- Kite: experienced, 30% TM roll;
- Pepa: working professional, 20%;
- Lumen: experienced, 30%;
- Margin: working professional, 20%;
- Rook: rival, 40%.

These values can be migrated later through explicit canon/version changes. They are not rerolled per encounter.

## 14. Battle authority boundary

Ouros selects the persistent NPC Pokémon and requests generation according to this policy.

AutoPTU remains authoritative for:
- legal level domain;
- learnset legality;
- TM compatibility;
- active move legality;
- derived stats;
- battle state;
- battle outcome.

Minecraft/Cobblemon may render the resulting Pokémon but cannot decide its level, moves, legality or battle result.
