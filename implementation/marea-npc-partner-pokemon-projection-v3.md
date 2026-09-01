# Marea NPC Partner Pokemon Projection v3

Status: IMPLEMENTED / CANON-BACKED PLAYABLE SLICE
Date: 2026-09-01

This slice turns the named partner Pokemon already defined for every Marea Interior resident into visible Cobblemon actors without giving Cobblemon encounter or battle authority.

## Canonical identity

`AutoPTU-Cobblemon-RPG` now derives one stable partner identity for every entry in `CanonicalNpcCatalogue`:

`<npc_id>.partner`

Examples:

- `ouros.npc.mara_veyra.partner` -> Kite the Corviknight
- `ouros.npc.ivo_serrat.partner` -> Pepa the Greedent
- `ouros.npc.nerea_sol.partner` -> Lumen the Heliolisk
- `ouros.npc.taro_min.partner` -> Margin the Noctowl
- `ouros.npc.sela_orrin.partner` -> Rook the Falinks

The full 15-resident roster is derived from the NPC catalogue rather than manually duplicated. CI tests require one named partner identity for every canonical NPC and verify species/name parity with the NPC record.

## Minecraft/Cobblemon projection

`NpcPartnerPokemonProjectionRuntime` creates a Cobblemon `PokemonEntity` beside the resident's work anchor when Marea Interior is built.

The projection carries:

- rendered Cobblemon species;
- canonical partner tag `autoptu:npc-partner:<partner_id>`;
- visible canonical nickname;
- persistent Minecraft entity flag;
- generic `ouros:npc-partner` projection tag.

The entity is presentation only.

It is deliberately NOT registered through `VisibleWildPokemonEncounterRuntime`.

Therefore interacting with Kite, Pepa, Lumen, Margin, Rook or any other resident partner does not create a wild encounter reservation and does not make the partner capturable by implication.

## Authority boundaries

The following remain authoritative outside the Cobblemon entity:

- partner identity;
- NPC relationship;
- PTU battle sheet;
- level/stat derivation;
- Moves;
- Abilities;
- HP and status;
- capture legality;
- ownership transfers;
- injury/death/absence;
- battle participation;
- battle outcomes.

`COBBLEMON_ENTITY_EXISTS != CANONICAL_PARTNER_EXISTS`

`COBBLEMON_ENTITY_DESPAWNED != PARTNER_DEAD_OR_GONE`

`NPC_PARTNER_VISIBLE != WILD_POKEMON`

`NPC_PARTNER_SPECIES_MODEL != AUTHORITATIVE_BATTLE_SHEET`

## Player-visible result

Running:

`/ouros world marea_interior build`

now materializes the fixed Marea district, resident NPC presentation actors and named Pokemon partner projections.

The build result reports the number of partner Pokemon projected.

A player entering Puerto Bruma should now see residents accompanied by recognizable named Pokemon rather than only generic villager bodies.

## Correlation with resident network

This implementation closes the P1 item in `canon/marea-interior-map-resident-network-v2.md` for companion Pokemon presentation.

The next high-value P1 slice is server-owned NPC schedule state:

- canonical home anchor;
- canonical work anchor;
- schedule phase;
- projection target;
- safe movement/fallback when chunks or paths are unavailable;
- partner projection following the same presentation phase without making Minecraft pathfinding authoritative.

That schedule should make Puerto Bruma, Loma Clara and Estacion Mirador visibly change through the day while preserving permanent identity and relationship state independently of Minecraft entity movement.
