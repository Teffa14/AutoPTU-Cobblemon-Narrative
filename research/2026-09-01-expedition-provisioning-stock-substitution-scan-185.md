# Expedition provisioning, stock, substitution, and replenishment scan

Status: RESEARCH / PROVENANCE ONLY. No canon facts are created by this file.
Date: 2026-09-01
Pass: 185

## Research question

How can Ouros make ordinary preparation, field supply, limited stock, substitution, delivery, consumption, return, and replenishment create persistent story without converting every object into a PTU Item or duplicating custody, access, preparedness, commerce, or battle authority?

## Existing repository boundary reviewed first

The full Narrative tree was inventoried before research. Adjacent systems were inspected rather than assumed absent.

`design/emergency-preparedness-drill-continuity-layer.md` already owns plan-linked staged resources, preparedness caches, inspections, and corrective work. It explicitly records borrowed cache items and warns that a visible container does not prove contents are available.

`design/shared-resource-access-permit-stewardship-layer.md` already owns authorization to enter, observe, sample, handle, remove, repair, or otherwise affect a shared resource. It explicitly separates access authority from mechanical capability.

`canon/marea-interior-map-resident-network-v2.md` already establishes ordinary responsibilities that can host provisioning stories without inventing new institutions: Ivo coordinates purchasing and recipe substitution; Lia records arrivals/departures and unloading windows; Teo maintains ordinary equipment; Brin handles storehouse intake, dispatch preparation and storage coordination; Nerea/Ema work with field observations and equipment; Mara coordinates field reports and route work.

Therefore this pass does not create another custody ledger, permit system, preparedness plan, market economy, crafting system, or quest stack. The new seam is availability over time: what usable quantity exists, what portion is reserved, what is issued, what returns, what may substitute, and what has actually been replenished.

## Public sources and reusable structures

### Pokémon Legends: Arceus — Getting Ahold of New Wares / later wares requests

Source: Bulbapedia walkthrough and request documentation.
https://bulbapedia.bulbagarden.net/wiki/Appendix:Legends:_Arceus_walkthrough/Requests_1-30
https://bulbapedia.bulbagarden.net/wiki/Tao_Hua

Observed structure: the general store's available offering expands only after a supply relationship is resolved and requested materials are delivered. Later requests repeat the pattern with different inputs. The useful design lesson is not the specific characters or ingredients. It is that visible retail availability can be downstream of procurement, supplier willingness, material availability, and completed delivery.

Reusable Ouros pattern: an NPC can know that an item is normally stocked while the current usable quantity is zero; a requested replenishment can exist without having arrived; a supplier can agree to provide goods while downstream intake is still pending.

### Pokémon Mystery Dungeon: Explorers of Sky — expedition preparation

Source: Bulbapedia walkthrough, Chapter 7.
https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Mystery_Dungeon:_Explorers_of_Sky/Chapter_7

Observed structure: before the expedition the player is explicitly told to prepare, shop, use storage, protect valuables, and work within a finite bag capacity. The expedition changes party composition and makes loadout decisions consequential.

Reusable Ouros pattern: preparation can be gameplay even before scarcity becomes a crisis. A field party can choose what to carry, what to leave in a storehouse, what reserve remains behind, and what must be checked out for a particular job.

Do not import Mystery Dungeon bag limits or item effects as PTU rules.

### Pokémon Mystery Dungeon — Deposit Box

Source: Bulbapedia.
https://bulbapedia.bulbagarden.net/wiki/Deposit_Box

Observed structure: stored stock and carried stock occupy different operational states. Some dungeon contexts automatically move carried material back to storage when it cannot legally accompany the player.

Reusable Ouros pattern: physical ownership or custody does not imply an object is currently issued to a field team. Location and availability need explicit state.

### Pokémon Ranger: Guardian Signs — Luggage for Renbow Island

Source: Bulbapedia, Renbow Island quest listing.
https://bulbapedia.bulbagarden.net/wiki/Renbow_Island

Observed structure: a small delivery quest has a named origin/destination and the contents matter because they are meant for a particular recipient. The same region also changes physically when infrastructure is damaged and later repaired.

Reusable Ouros pattern: delivery should preserve destination, recipient, custody, condition, and completion rather than treating every carried parcel as generic inventory.

### Pokémon Ranger: Shadows of Almia — Deliver Vien Tribune

Source: Bulbapedia walkthrough / Ranger Mission list.
https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Ranger:_Shadows_of_Almia/Part_2
https://bulbapedia.bulbagarden.net/wiki/Ranger_Mission

Observed structure: ordinary distribution work can introduce geography, residents, exceptions, and relationships without combat. A recipient being away changes how the delivery is completed.

Reusable Ouros pattern: routine provisioning routes can teach the player how a settlement works while exposing stale assumptions about who is present or what destination is currently valid.

### The Alexandrian — expedition procedures and supply tracking

Sources:
https://thealexandrian.net/wordpress/date/2018/07
https://thealexandrian.net/wordpress/48073/roleplaying-games/hexcrawl-addendum-running-the-hexcrawl

Observed structure: expedition procedures become easier to run when supplies, guides, records, maps, and recurring operational checks are explicit rather than reconstructed ad hoc. Longer expeditions increase logistical burden.

Reusable Ouros pattern: a field operation can carry a small operational manifest and update it through ordinary events. Avoid importing this source's costs, encumbrance values, rations, or rules.

### PTU community/tooling scan

Public PTU searches this pass did not surface a strong campaign-log example specifically about provisioning. A Roll20 PTU inventory discussion does show that long unstructured item lists become difficult for players to use, but that is a UI/community observation rather than PTU rules authority.

Source: Roll20 community forum, PTU inventory tab discussion.
https://app.roll20.net/forum/post/2467512/help-inventory-tab

Reusable lesson: Ouros should avoid one enormous undifferentiated inventory list for institutional stock. Operational state and purpose matter more than exposing every stored object at once.

## PTU/AutoPTU boundary

AutoPTU and AutoPTU-Java remain read-only in this task. Narrative may reference PTU Items and Trainer capabilities only when their actual rule/content provenance is known.

A mundane field object, meal ingredient, lamp part, archive box, rope, spare fitting, survey notebook, or replacement lens must not silently become a PTU mechanical Item.

Likewise, possession of a PTU Item in battle does not establish who may allocate institutional stock outside battle. Inventory/equipment legality and civic/workplace authority are separate domains.

No generic `Provisioning Roll`, `Expedition Bonus`, `Well Supplied` combat modifier, crafting effect, healing value, weight rule, or scarcity penalty is created by this research.

## Caelo cross-check

A literal `Caelo` search across Teffa14/AutoPTU-Cobblemon-Narrative, Teffa14/AutoPTU-Java and Teffa14/AutoPTU returned no indexed result in this pass.

That result is an evidence gap only. It does not establish that Caelo lacks commerce, supply corps, field caches, item law, crafting, scarcity, stores, or expedition doctrine.

Any Caelo-specific terminology or rule must remain UNRESOLVED until a project source is located.

## High-value transformed patterns for Ouros

1. Stock has states: expected, ordered, received, inspected, usable, reserved, issued, consumed, damaged, returned, quarantined, and replenishment pending.
2. Availability is scoped by location and purpose. Ten units in Loma Clara do not mean ten units are available at Mirador.
3. A substitute can solve an operational need only after compatibility and authority are established; visual similarity is insufficient.
4. Emergency drawdown can create a later mundane shortage. The consequence may arrive after the exciting incident.
5. NPC work can progress while the player is elsewhere: orders arrive, inspections finish, issued kits return, or a shortage worsens.
6. Delivery completion can be partial. Cargo can arrive with a damaged lot, wrong quantity, stale paperwork, or a recipient change.
7. Known storage location is not permission to take stock.
8. Player inventory should never become the hidden authoritative ledger for a settlement.
9. Physical Minecraft containers are projections of server-owned records. Duplication, destruction, chunk unload, or UI desync must not manufacture or erase institutional stock.
10. A provisioning story can be solved through verification, allocation, substitution, scheduling, or resupply. Theft and sabotage are possibilities only when evidence supports them.

## Candidate story pressures

Useful non-villain pressures include ferry delay, a lot failing inspection, a tool reserved for scheduled repair, incompatible replacement parts, a mislabeled crate, demand arriving earlier than expected, a field kit returned incomplete, a substitute that works for cooking but not storage, a promised shipment not yet unloaded, or a cache that exists but was drawn down during a previous incident.

These structures fit Marea's established residents and sites without creating new canon.

## Copyright/provenance note

This file preserves source attribution and extracts abstract structures only. It does not copy protected dialogue, distinctive characters, scenes, quest text, exact plots, item tables, or rule prose into Ouros canon.