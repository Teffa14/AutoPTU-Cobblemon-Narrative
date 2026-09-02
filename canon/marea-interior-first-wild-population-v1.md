# Marea Interior First Visible Wild Population v1

Status: CANON-APPROVED FOUNDATION
Date: 2026-09-02

This file freezes the first normal wild Pokémon population/encounter record that Ouros may project physically into Minecraft. It exists to unblock the Minecraft-first vertical slice without letting Cobblemon species/entity state invent PTU truth.

This is a bounded first population, not the final ecology system and not a global rules-profile decision.

## 1. Population identity

- `population_id`: `ouros.marea.wild.sendero_lower_shelf.fletchling.v1`
- `site_id`: `ouros.marea.sendero_vidrio`
- fixed site anchor inherited from Marea canon: lower shelf `(2056, 77, 2120)`
- `zone_id`: `ouros.marea.sendero_vidrio`
- `context_id`: `lower_shelf_first_slice_v1`
- first persistent encounter slot: `ouros.marea.encounter.sendero_lower_shelf.fletchling.0`
- species: **Fletchling**
- form: official standard Fletchling only
- species status: `OFFICIAL`
- Ouros authorization: `OUROS-CANON-APPROVED`
- fusion: `false`
- first presentation offset from the lower-shelf anchor: `(+3, +1, +3)`

This approval does not authorize any Fakemon, unofficial regional form, Type Sync/TOSIKI conversion, custom Mega/evolution, fusion, or unofficial stat/type/Ability/learnset mutation. The project-wide species/form gate remains in force.

Pia Min's named partner Redline is also a Fletchling. Redline remains a different persistent individual and is never part of this wild population.

## 2. First authored encounter blueprint

For the first vertical-slice actor only, Ouros freezes a complete PTU battle input before the Minecraft actor is revealed.

`mechanical_profile_id`: `ouros.vertical_slice.ptu_1_05.fletchling_v1`

The profile uses the supplied PTU 1.05 Pokédex Fletchling entry as the mechanical source for this individual. This does **not** globally choose PTU 1.05 over Caelo, Kairos or later Ouros rules-profile decisions.

### Identity and level

- species: `fletchling`
- level: `5`
- type: `normal / flying`
- Ability: `big-pecks`
- no Held Item
- no pre-existing Status Afflictions
- no pre-existing Injuries

The PTU 1.05 Pokédex lists Big Pecks and Tangled Feet as Basic Abilities for Fletchling. This first individual uses Big Pecks. Ability behavior remains AutoPTU-Java-owned; the narrative/runtime record only freezes the identity.

### Stats

PTU 1.05 Fletchling base stats are `HP 5 / ATK 5 / DEF 4 / SPATK 4 / SPDEF 4 / SPD 6`.

For this authored level-5 individual, a neutral Nature is already consumed into the frozen snapshot and the Level+10 stat points are distributed as follows while preserving Base Relations:

- HP: `8`
- Attack: `8`
- Defense: `6`
- Special Attack: `6`
- Special Defense: `6`
- Speed: `9`

Added points: `3 + 3 + 2 + 2 + 2 + 3 = 15`.

Using PTU's Pokémon HP formula, `Level + (HP x 3) + 10`, Max HP is `39`.

Baseline Accuracy/Evasion inputs:

- Accuracy Stage: `0`
- Physical Evasion: `1`
- Special Evasion: `1`
- Speed Evasion: `1`

### Moves

The PTU 1.05 entry gives Fletchling Tackle and Growl at level 1; Quick Attack is not learned until level 6.

The first level-5 encounter therefore freezes exactly:

- `tackle`
- `growl`

No TM, Tutor, Egg/Inheritance, custom or campaign-homebrew Move is added.

### Base movement and capabilities

From the supplied PTU 1.05 Fletchling entry:

- Overland: `3`
- Swim: `0`
- Sky: `5`
- Long Jump: `1`
- High Jump: `1`
- Power: `1`
- special capabilities: `guster`, `underdog`

Power remains descriptive/source provenance until the runtime has a dedicated canonical field that needs it. `CanonicalBaseMovement` receives only Overland/Swim/Sky/Long Jump/High Jump. `guster` and `underdog` may be transported as capability identities; their mechanical effects are not implemented by Minecraft.

## 3. Minecraft projection contract

Required order:

```text
Ouros canonical population record
  -> complete server-authored WILD blueprint
  -> publish create-only blueprint to active world registry
  -> spawn/render standard Cobblemon Fletchling actor
  -> bind actor UUID only as presentation correlation
  -> player interaction creates encounter request
  -> canonical party + exact frozen WILD blueprint hand off toward AutoPTU-Java
```

The actor may not be spawned as the authoritative first-slice wild until the complete blueprint is available and publishable.

Minecraft/Cobblemon may supply presentation facts such as the current actor UUID and observed world position. Minecraft/Cobblemon must never supply or overwrite the canonical species, level, stats, HP, moves, Ability, status, injuries, Held Item or battle result.

`COBBLEMON_FLETCHLING_ENTITY != CANONICAL_WILD_POKEMON_STATE`

`ENTITY_DESPAWN != CAPTURED_OR_DEAD`

`VISIBLE_ACTOR_LEVEL != TRUSTED_PTU_LEVEL`

## 4. Initial ecology scope

The first actor represents one ordinary Fletchling using the lower Sendero area. It is intentionally available as a deterministic first-slice encounter so the complete Minecraft -> Ouros -> AutoPTU path can be exercised repeatedly during development.

Do not infer from this single implementation slot that:

- Fletchling is the only species on Sendero del Vidrio;
- one visible actor equals local abundance;
- the actor is always aggressive;
- the population has a permanent level of 5;
- every future Fletchling uses the same Nature, stat allocation, Ability or moves;
- the lower shelf is a mechanically uniform battlefield;
- normal ecology should eventually be deterministic or single-species.

Later population work can introduce time/weather/ecology windows, multiple species, level bands, individual variation, recurring identities where useful and population state. Those additions must still select/freeze complete canonical state before presentation.

## 5. Source provenance

Mechanical source for this first blueprint:

- supplied **Pokémon Tabletop United Pokédex 1.05**, Fletchling entry, p. 95;
- supplied **PTU Core Rulebook**, Pokémon stat allocation / Base Relations / Pokémon HP formula / derived Evasion rules.

Comparative living-world/ecology inspiration only:

- supplied **Caelo Region Location & Encounter List** includes ordinary Fletchling as an urban/route-capable species and describes territorial/diurnal behavior;
- supplied **Caelo Player's Guide** and **Kairos New Player Doc/Core** remain comparative living-world sources, not automatic rules authority.

The supplied merged/edited Pokédex contains a different Fletchling Ability ordering and adds Swim 1. Those differences are preserved as source differences and are **not** silently merged into this PTU-1.05-bounded first blueprint.

## 6. Next implementation acceptance

This canon slice is successful when a player can enter the built Marea Interior world, physically see this wild Fletchling near the Sendero lower shelf, interact with it, and the server can prove that the already-published exact blueprint—not the Cobblemon Pokémon payload—is what enters the normal encounter handoff.

Battle completion/capture are separate downstream acceptance gates until their authoritative Java result contracts are ready.