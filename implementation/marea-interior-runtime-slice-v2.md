# Marea Interior Runtime Slice v2

Status: IMPLEMENTED / CANON-BACKED PLAYABLE SLICE
Date: 2026-09-01

This document maps the current Marea Interior canon to executable `Teffa14/AutoPTU-Cobblemon-RPG` surfaces.

## Implemented authority catalogues

The RPG repository now contains:

- `CanonicalWorldMapCatalogue` — fixed Marea coordinates and parent sites;
- `CanonicalNpcCatalogue` — 15 persistent resident identities, roles, class concepts and named Pokémon partners;
- `CanonicalQuestlineCatalogue` — composable questline graph metadata using the 16-family Ouros taxonomy;
- expanded `CanonicalQuestCatalogue` — first Marea quest episodes;
- expanded `CanonicalQuestObjectiveCatalogue` — server-observed location and Trainer-record objectives;
- expanded `CanonicalNpcDialogueCatalogue` — dialogue for all 15 Marea residents, with quest offers for the first five anchors;
- expanded `CanonicalLocationCatalogue` — discoverable Marea sites.

## Visible world runtime

`MareaInteriorBuilder` builds a fixed-coordinate first-pass physical district using vanilla Minecraft blocks.

Current physical sites:

- Puerto Bruma service hub;
- Bruma Market Hall;
- Marea Field Office;
- Tideglass Archive;
- Bruma Battle Yard;
- ferry landing;
- clinic;
- repair row;
- Sendero del Vidrio road;
- seasonal crossing;
- Loma Clara;
- cooperative storehouse;
- communal kitchen;
- field school;
- Estación Mirador;
- weather mast;
- Mirador transect trailhead.

The first visual pass is intentionally functional. It establishes coordinates, connectivity, facility silhouettes and interaction anchors. It is not the final art pass.

## Runtime commands

Admin build:

`/ouros world marea_interior build`

Player visit:

`/ouros world marea_interior visit`

Resident audit:

`/ouros world marea_interior residents`

The build command materializes the fixed district and spawns missing physical Villager presentation actors for all 15 canonical residents. Existing resident actors are detected by canonical NPC command tag near their work anchor so ordinary rebuilds do not duplicate them.

## Physical NPC interaction

Each resident actor is bound through `FabricNpcDialogueRuntime` to a server-owned `npc_id`.

Primary quest-giver surfaces:

- Ivo Serrat -> `marea-market-shortfall`
- Mara Veyra -> `marea-route-field-check`
- Dr. Nerea Sol -> `marea-mirador-observations`
- Taro Min -> `marea-tideglass-comparison`
- Sela Orrin -> `marea-battle-yard-introduction`

Secondary residents currently provide contextual dialogue and establish their role in the district graph. Later episodes can add quest actions without changing identity.

## First playable quest weave

### The Thin Delivery Season

Ivo starts a region/settlement thread.

The player must physically visit:
- Loma Clara;
- Estación Mirador.

Those visits are observed by the server and written to the player's canonical quest objective state.

### Reading the Sendero

Mara starts the Field Office route-evidence lane.

The player must physically visit:
- Sendero del Vidrio;
- its seasonal crossing.

### What the Station Can Actually Say

Nerea starts the Mirador evidence lane.

The player must physically visit:
- Mirador transect trailhead;
- Tideglass Archive.

### The Record Is Not the Cause

Taro starts an archive comparison lane.

The player must physically visit:
- Loma Clara cooperative storehouse;
- Estación Mirador.

### Measure the Change

Sela starts the first competitive/rival/relationship thread.

The player must:
- physically visit Bruma Battle Yard;
- run the existing canonical Trainer-record review surface.

`FabricTrainerRecordRuntime` emits the quest event only after it has loaded the player's server-owned Trainer record.

## Discovery integration

`FabricLocationDiscoveryRuntime` no longer assumes every authored location is centered on world spawn.

For Marea IDs it reads the fixed coordinate from `CanonicalWorldMapCatalogue`. Entering a location:

1. uses server-observed player coordinates;
2. persists canonical discovery through the existing discovery service;
3. emits `location:<location_id>` to `CanonicalQuestObjectiveService`;
4. updates only quests already accepted by the player;
5. remains idempotent through canonical objective persistence.

Legacy non-Marea test content retains the prior spawn-anchor fallback.

## Correlation gate

`CanonicalMareaContentTest` now fails CI if:

- a resident references a missing home site;
- a resident references a missing work site;
- a resident lacks a dialogue surface;
- a questline references a missing quest;
- a questline references a missing location or NPC;
- a child questline references a missing parent;
- a Marea discovery location lacks a fixed map anchor;
- a Marea questline quest has no server-authored objectives.

This is the first automatic anti-island rule. Future content should extend this gate instead of relying only on documentation review.

## Companion Pokémon status

The 15 named partner Pokémon are canon in `CanonicalNpcCatalogue`, but this slice does not yet spawn their Cobblemon entities.

Reason: a companion projection needs a dedicated persistent identity binding that prevents presentation entities from being interpreted as wild encounter authority. The project must not create visible companions by abusing the existing wild-encounter binder.

The next safe implementation should add:

`CanonicalNpcPokemonIdentity -> Cobblemon PokemonEntity projection`

with:
- stable NPC/Pokémon identity;
- dynamic party-relative battle sheet request only when a battle is authorized;
- no Cobblemon BattleState authority;
- no entity-despawn implication for canonical death/absence;
- no wild-capture interpretation for an NPC companion.

## Quest framework decision

The current native runtime already has durable canonical quest journals, objectives, NPC dialogue actions, location discovery, relationships, rivals, calendar state and world-story projection. Replacing it with an external quest mod would weaken authority separation.

External repositories are therefore references or optional UI adapters:

- Heracles: dependency/tree structure reference;
- FTB Quests: candidate chapter/graph UI projection;
- MCA: Quests: data-driven authoring and validation reference only; incompatible Forge/GPL implementation is not copied.

Long-term improvement: move hard-coded catalogue records into validated data files while keeping the same server-authoritative Java services. A data loader should reject broken graph references at server startup and CI.

## Next implementation sequence

1. verify Fabric build/server smoke CI for this slice;
2. add non-wild NPC Pokémon projection and dynamic loadout request;
3. add server-side NPC schedule state and safe work/home projection;
4. add first secondary resident quest episodes;
5. add richer map art/dressing without changing canonical anchors;
6. add a questline graph/journal UI projection that reads native canonical state;
7. expand Marea ecology and Sendero encounter tables through AutoPTU-owned encounter provisioning.
