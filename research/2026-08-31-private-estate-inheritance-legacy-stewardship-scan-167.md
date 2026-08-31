# Private Estate, Inheritance and Legacy Stewardship Scan

Status: RESEARCH ONLY — NON-CANON
Pass: 167
Date: 2026-08-31

## Research question

How can Ouros preserve posthumous private-asset continuity, inherited objects, instructions, claims, custody and long-term stewardship without importing a real-world probate code, treating kinship as automatic entitlement, or converting Pokémon companions and Minecraft inventories into property facts?

## Repository gap check

The repository tree was inspected recursively before writing. Searches for inheritance, probate and estate found no dedicated continuity layer. The adjacent mortality layer already owns death reports, confirmed mortality, remains, funerary episodes and resting places. Family/Kinship owns relationship history. Property/Ownership and Material Culture own title and physical-object history. Finance owns balances, debts and payments. Agreements owns commitments. Archives owns documentary provenance and preservation. Civic Office owns institutional succession.

This pass therefore addresses only the connective continuity between an authored death and later private-legacy handling. It does not replace those authorities.

## Pokémon-derived design evidence

### Luka's great-grandfather — intergenerational artifact plus documentary trail

Public Pokémon reference material describes a Silver Wing lost with a ship, repeated failed recovery attempts, and a diary/map later discovered among family heirlooms. The object and the documentary record cross generations before a descendant recovers the artifact.

Reusable lesson: an inherited mystery can be driven by provenance rather than destiny. Keep the ancestor, diary, map, object, wreck location, recovery episode and later custody as separate records. The descendant's relationship to the ancestor explains why the lead matters; it does not prove ownership or supernatural significance.

Source: Bulbapedia, “Luka's great-grandfather,” accessed 2026-08-31. Research reference only.

### Pokémon Ranger family property

Public material for Pokémon Ranger: Shadows of Almia describes the player's family as owning a home and nearby Partner Farm after moving to Chicole Village.

Reusable lesson: household residence, family membership and property ownership can overlap without becoming the same state. A future death or departure must not infer that the remaining household automatically owns every associated asset.

Source: Bulbapedia, “Player's Family,” accessed 2026-08-31. Research reference only.

### Community PTU campaign evidence

A publicly posted PTU campaign log uses a stolen family heirloom as an adventure objective tied to a Gym Leader's family and a broader legendary mystery. The session then becomes improvised around retrieval rather than a planned standard battle.

Reusable lesson: heirlooms work as relationship- and provenance-bearing objectives. Retrieval can produce negotiation, stealth, chase or combat, but possession after an encounter must not silently settle title, inheritance or legitimacy.

Source: r/PokemonTabletop campaign log #9, 2021. Community practice only; not PTU mechanical authority.

## Archival/probate-derived structural evidence

The UK National Archives research guides distinguish wills, administrators/executors, beneficiaries, probate or administration grants, inventories, disputed wills and later records. Historical inventories could separately itemize household contents, stock, agricultural equipment, assets and debts. The archive also emphasizes that not all wills or inventories survive, that copies can differ from originals, and that disputes generate their own records.

Reusable lessons for Ouros:

A stated instruction can exist before anyone establishes which instruction controls. An executor or administrator is a role of responsibility rather than an ownership shortcut. An inventory is a dated evidence snapshot, not omniscient truth. Missing archival material does not prove that no instruction or asset existed. A dispute preserves competing claims without requiring the generator to decide which party is morally correct. Distribution should be recorded as episodes so planned transfer, physical handoff, ownership update and financial settlement remain distinguishable.

Sources: The National Archives, “Wills 1384–1858,” “Wills and administrations before 1858,” “Wills and administrations after 1858,” and “Civil court cases: disputed wills,” accessed 2026-08-31.

## Transformation rules

No English, Welsh, Australian, American or other real-world inheritance law is imported into Ouros. Terms such as will, executor, administrator, beneficiary and inventory are used only as comparative research vocabulary. Canon must author the applicable succession institution, custom or rule for each culture or jurisdiction before the system can infer legal effect.

No source-specific character, plot, dialogue, treasure, legal threshold, court hierarchy, tax, waiting period or distribution formula is copied.

## Proposed Ouros abstractions

Useful records include an estate case, governing succession-rule reference, legacy instruction versions, dated inventory snapshots, asset and obligation links, custody episodes, claims, review episodes, distribution plans, transfer episodes, legacy stewardship episodes, disputes and later record revisions.

The architecture should support incomplete evidence. A case may remain open because an object is missing, an instruction is disputed, a creditor claim remains unresolved, or no canon-approved rule establishes who may decide.

Long-lived objects should preserve two timelines: physical/material history and stewardship/title history. A workshop can remain physically unchanged while its custodian, owner, user and symbolic meaning all change.

## Hard boundaries

`DEATH_CONFIRMED != ESTATE_OPENED`

`KINSHIP != AUTOMATIC_INHERITANCE`

`NAMED_IN_INSTRUCTION != PROPERTY_TRANSFERRED`

`BENEFICIARY != OWNER`

`ADMINISTRATOR != OWNER`

`CUSTODY != OWNERSHIP`

`POSSESSION != OWNERSHIP`

`DOCUMENT_EXISTS != CONTROLLING_DOCUMENT`

`LATEST_DOCUMENT != CONTROLLING_DOCUMENT_BY_DEFAULT`

`ASSET_LISTED != ASSET_PRESENT`

`CLAIM_FILED != CLAIM_ACCEPTED`

`DISTRIBUTION_PLANNED != DISTRIBUTION_COMPLETED`

`MEMORIAL_GIFT != ESTATE_TRANSFER`

`POKEMON_COMPANION != PROPERTY`

`MINECRAFT_CHEST_CONTENTS != CANONICAL_ESTATE_INVENTORY`

`DROPPED_ITEMS_AFTER_DEATH != INHERITANCE`

`BATTLE_LOOT != ESTATE_PROPERTY`

## PTU/Caelo cross-check

Repository and engine searches did not establish a universal PTU/Caelo inheritance, probate, heir, executor or estate mechanic. This means succession effects remain UNKNOWN until exact Core/Caelo authority is located.

An inherited ordinary object can exist narratively, but any object that functions as a PTU Item must use the verified Item implementation when it enters battle. A family story cannot grant an unimplemented mechanical bonus.

A Pokémon companion is an actor/creature with its own continuity. This pass never classifies a Pokémon as an estate asset merely because a deceased Trainer previously traveled with it.

## Design opportunities

The strongest adventure structures are provenance puzzles rather than treasure hunts: two inventories both correct at different dates; an object believed to be a gift but never physically handed over; an archive copy missing a page; a workshop whose tools belong to different people; a legacy instruction discovered after an initial distribution; or an heirloom whose cultural stewardship matters more than market value.

These structures create consequences across Family/Kinship, Material Culture, Property/Ownership, Finance, Archives and Public Memory while keeping each layer authoritative for its own state.

## Source ledger

New research used in this pass:

- Bulbapedia — Luka's great-grandfather.
- Bulbapedia — Player's Family.
- r/PokemonTabletop — campaign log #9 (community design evidence only).
- The National Archives — Wills 1384–1858.
- The National Archives — Wills and administrations before 1858.
- The National Archives — Wills and administrations after 1858.
- The National Archives — Civil court cases: disputed wills.

All provenance remains research-only until a separate canon approval promotes specific Ouros facts.