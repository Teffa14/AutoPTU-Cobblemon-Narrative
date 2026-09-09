# Portable Find Custody and Context Scan — Pass 388

Status: RESEARCH / PROVENANCE. Not Ouros canon.
Date: 2026-09-09

## Purpose

Close the research seam left by Passes 383–387: a `PORTABLE_FIND` may leave its discovery context, but its site provenance, physical custody, legal ownership, archival destination and interpretation must remain separate facts.

This pass does not add canon locations, cultures, institutions, species, artifacts or PTU mechanics.

## Internal inspection

The current site-evidence owner already records `PORTABLE_FIND` observations with site, revision, observer, semantic time, evidence reference and provenance root. It does not own possession.

The existing world-resource layer already owns stable resource identity, holder, location, reservation and availability. `ResourceHandoffLedger` separately records authorized custody transfers with provider, receiver, accountable actor, location, semantic time and optional condition reference.

Therefore the safe architecture is a bridge, not a second archaeology inventory.

Core separations:

`DISCOVERY_CONTEXT != CURRENT_CUSTODY`

`CURRENT_CUSTODY != LEGAL_OWNERSHIP`

`PHYSICAL_TRANSFER != CONTEXT_TRANSFER`

`POSSESSION != KNOWLEDGE`

`PORTABLE_FIND_OBSERVATION != WORLD_RESOURCE`

## Public sources

### Historic England Archaeological Recording Manual (2018)
Source: https://historicengland.org.uk/content/docs/research/historic-england-archaeological-recording-manual-2018

Reusable structure:
- finds are labelled with context/sample identifiers;
- fragile finds may be photographed in situ before lifting;
- processing preserves the relationship between recovered material and the context from which it came.

Ouros abstraction:
A portable find can move physically while retaining an immutable context link. Removal from a site must not replace the original observation or provenance root with the holder's current location.

### CIfA Standard and guidance: archaeological archives
Source: https://www.archaeologists.net/sites/default/files/2023-11/CIfA-SandG-Archaeological-Archives-2020.pdf

Reusable structure:
- recovered objects can have different ownership and deposition outcomes;
- finds that do not enter a repository should still be recorded, safely handled and have their later location/ownership documented where appropriate;
- archive integrity depends on linking material and documentary records.

Ouros abstraction:
Custody, ownership and archival destination are independent state. A find may be physically held by a field actor, legally controlled by another authority and destined for a repository without any of those facts changing the discovery context.

### CIfA / Historic England ownership toolkit announcement (2025)
Source: https://www.archaeologists.net/news/2025/new-draft-toolkit-resource

Reusable structure:
The management of recovered material explicitly distinguishes recovery, archiving and secure/legal transfer of ownership.

Ouros abstraction:
A custody handoff does not automatically transfer title. If Ouros later models ownership authority, it needs a separate owner or authority reference rather than overloading `holder_actor_id`.

### PTU Core 1.05 campaign guidance
Public reference: https://anyflip.com/qloz/xgfq/basic/451-500

Reusable structure only:
PTU explicitly presents ancient-ruin artifact retrieval as a possible campaign objective and demonstrates that the object can be a narrative trigger rather than merely loot.

Ouros abstraction:
Recovery of a find can satisfy an investigative or institutional objective without treating the object as a generic combat item. Any mechanical effect remains individually gated against PTU/Caelo and AutoPTU evidence.

No protected prose, named plot or distinctive trial structure is imported.

### PTU campaign log — Giant in the Playground
Source: https://forums.giantitp.com/archive/index.php/t-527075.html

Reusable structure:
Environmental exploration presents recoverable useful objects inside damaged locations while the physical state of the location itself remains relevant to risk and decision-making.

Ouros abstraction:
An actor can discover, assess and potentially remove an object from an unstable site while site condition and item custody progress on separate tracks.

No characters, incidents, dialogue or specific loot are imported.

### Pokémon Aragonite fan game
Public reference: https://www.ducumon.click/2024/11/pokemon-aragonite.html

Reusable structure:
Research rank, access to increasingly dangerous field areas, relic collection and investigation can coexist as a progression loop.

Ouros abstraction:
A recovered object can unlock institutional follow-up because of documented provenance and research value, not because possession itself grants authority or knowledge.

No region, organization, characters, relics, plot or custom Pokémon are imported.

## Design lessons for Ouros

1. A portable object needs one stable identity after recovery.
2. Its discovery context remains immutable historical evidence.
3. Current holder and current location belong to the resource/custody subsystem.
4. Authorization to transfer custody does not prove legal ownership transfer.
5. A transfer event may record condition, but later condition changes require new evidence rather than mutation of the historical transfer record.
6. NPC knowledge of the find still requires observation, report, archive access or explicit communication.
7. Removing a find can change a site revision, but that physical revision must be recorded independently from the object's custody transfer.
8. Loss, theft, loan, repository deposit, return and temporary examination can become distinct later lifecycle events without rewriting discovery provenance.

## Engine capability boundary

The reduced pattern requires no AutoPTU battle resolution.

If a recovery scene becomes tactical, capability dependencies must be admitted independently:
- targeting/footprints/range/LoS: required only for tactical interaction geometry;
- base movement legality: required for ordinary tactical approach/retreat;
- complete movement: required for push/pull/knockback/interception/forced movement, dragging or rescue reposition;
- core calculations: required for PTU calculations actually invoked;
- action economy/initiative: required for turn-ordered tactical recovery;
- full turn/round lifecycle: required for phased or delayed encounter behavior;
- full stateful damage pipeline: required for damage-driven consequences;
- status lifecycle: required for persistent statuses;
- terrain/weather/hazards/zones/reactions: required for unstable ground, collapse, flooding, dust, reaction hazards or timed environmental zones;
- move-specific behavior, abilities, items and Trainer Features/perks: each individually gated;
- AI legal-action infrastructure: required for legal tactical choices;
- AI tactical policy: required for protect-find, recover-object, escort, rescue-first, objective-aware withdrawal or disengage-after-objective behavior;
- Minecraft/Cobblemon/Craftics adapter/playback: required for stable find identity, pickup/handoff acknowledgement, site-revision projection and authoritative non-KO objective playback.

## Canon questions left open

- Which Ouros/Caelo authority, if any, regulates archaeological finds?
- Does legal ownership exist as a first-class world-state concept or only as institutional permissions/claims?
- Which sites permit removal, sampling or temporary examination?
- What evidence is required before an object may leave a site?
- Which PTU Skills/Features may support field recovery, documentation or conservation?
- What physical item classes can safely map to ordinary `WorldResource` without implying they are PTU battle Items?
