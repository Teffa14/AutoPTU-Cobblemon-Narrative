# Ouros Research — Fisheries, Aquatic Harvest, Landing & Stewardship — Pass 86

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is established Ouros canon.
Date: 2026-08-28

## Research purpose

The complete narrative repository tree was inspected before selecting this topic. Existing systems already cover maritime geography, sea lanes, harbors, aquatic habitats, food provenance, agriculture, conservation, wild collectives, seasonality, workplaces, Pokémon work, markets, equipment, found property and wildlife monitoring.

Two existing files deliberately expose the remaining gap:

- `design/maritime-coasts-depths-layer.md` says fishing may exist as food production, sport, research, culture, tourism, capture opportunity or stewardship, but does not define its operational lifecycle or mechanical resolution.
- `design/food-agriculture-hospitality-layer.md` includes `FISHERY` as an agricultural-site type and food batches as provenance objects, but does not model fishing effort, aquatic-harvest windows, release, landing or the handoff between water and downstream food/market systems.

Pass 86 investigates that gap without creating catch tables, quotas, yields, prices, capture rules or new aquatic battle mechanics.

## Source set

### Pokémon Tabletop United 1.05 Core — fishing procedure

Source:
- https://anyflip.com/tcye/paot/basic/201-250
- https://anyflip.com/tcye/paot/basic/251-300

PTU 1.05 already provides a concrete fishing procedure. It distinguishes rod class, bait/lure use, repeated bite checks, an Athletics check to reel the Pokémon in and subsequent choices around netting, Poké Ball capture or a possible attack by the hooked Pokémon. The GM is explicitly responsible for choosing locally plausible species or a suitable local randomization method.

Reusable lesson for Ouros:
- fishing mechanics already have a governing rules source;
- the world layer should provide location, ecological context, actor intent, equipment identity and persistent consequences;
- Minecraft/Cobblemon must not invent a second fishing-resolution rule when PTU legality matters;
- a hooked Pokémon, a reeled Pokémon, a captured Pokémon and a landed food/resource batch are separate outcomes;
- local ecology should constrain what may plausibly be encountered rather than a global narrative rarity table.

Important boundary:
The core book's example fresh/salt-water lists are examples for GMs, not Ouros canon encounter tables. Pass 86 does not copy them into a universal spawn list.

### Old Pokémon Tabletop community fishing tables — useful anti-pattern

Sources:
- https://www.tapatalk.com/groups/pokemon_tabletop/fishing-t1262.html
- https://www.tapatalk.com/groups/pokemon_tabletop/fishing-mechanics-and-fisherman-advanced-class-t2719.html

Older community discussions built detailed d100 fishing tables and homebrew angler progression before later PTU material standardized fishing more directly.

Reusable lesson:
Community tables demonstrate why a persistent game can easily overfit fishing into a parallel rules subsystem. Ouros should preserve the social, ecological and professional texture while refusing to import legacy/homebrew catch percentages, daily catch caps or custom classes as rules authority.

### Pokémon games — Hulbury as a mixed working waterfront

Sources:
- https://www.serebii.net/pokearth/galar/hulbury.shtml
- https://bulbapedia.bulbagarden.net/wiki/Hulbury

Hulbury combines docks, a market, restaurant, lighthouse, rail connection, Gym and fishing locations inside one compact coastal town.

Reusable lesson:
- a working waterfront can support food, transport, hospitality, recreation and institutions simultaneously;
- a fishing spot does not need to become a separate dungeon or isolated minigame location;
- repeated use of the same docks can reveal changing market supply, visitors, workers, route state and local ecology;
- the place remains legible even when one activity is disrupted.

No Hulbury NPCs, layout, catch rates or named businesses are imported.

### Pokémon games — Slateport and resource abundance becoming civic geography

Source:
- https://bulbapedia.bulbagarden.net/wiki/Slateport_Market

Slateport's market is described as having grown in an area where clean water supported abundant food, with the market and later harbor becoming defining civic features.

Reusable lesson:
- resource conditions can shape settlement history rather than appearing only as inventory numbers;
- markets, harbors and food systems may have a common environmental origin while remaining separate operational systems;
- if ecological conditions later change, the consequences can propagate through food supply, labor, tourism, public memory and transport without requiring an immediate catastrophe.

### Pokémon Ranger: Shadows of Almia — lost fishing gear without forced capture

Sources:
- https://gamefaqs.gamespot.com/ds/944533-pokemon-ranger-shadows-of-almia/faqs/55434
- https://www.serebii.net/ranger2/quests.shtml

A public quest asks the player to recover a fisher's lost rod from the sea floor. The object is near a Pokémon, but the Pokémon does not need to be battled/captured to recover it.

Reusable lesson:
- fishing activity can create persistent equipment and recovery stories even when no catch occurs;
- an object, a nearby wild Pokémon and a quest objective should remain separate entities;
- proximity to a Pokémon does not make combat mandatory;
- Found Property, Equipment, Maritime access and local ecology can intersect in one small story without merging their authority.

### Slowpoke Well — extraction and welfare as different questions

Source:
- https://bulbapedia.bulbagarden.net/wiki/Appendix:Gold_and_Silver_walkthrough/Section_4

The Slowpoke Well storyline uses extraction of a Pokémon-derived commodity as an exploitative practice and ties it to local social value and welfare concern.

Reusable lesson:
- the fact that a biological resource can be obtained does not establish that extraction is acceptable, sustainable or institutionally authorized;
- regeneration, abundance or market demand cannot substitute for welfare and stewardship review;
- resource-use stories can involve disagreement over method, access and care without making every harvester a villain or every restriction objectively correct.

No Slowpoke-specific commodity or Team Rocket plot is imported.

### Cobblemon — Poké Rod and current fishing surface

Sources:
- https://wiki.cobblemon.com/index.php/Poke_Rod
- https://wiki.cobblemon.com/index.php/1.6.0

Cobblemon currently provides a rich fishing-facing implementation surface: Poké Rods, bobber interaction, bubbles/reel timing, Pokémon or item outcomes, bait, lure-related access, Luck of the Sea rarity handling, fishing statistics and audiovisual feedback.

Reusable implementation lesson:
- reuse this interaction/presentation surface aggressively where compatible;
- rod models/items, bobbers, animations, sounds, particles, bait UI, cast/reel events and statistics are strong candidates for safe reuse or adapter review;
- Cobblemon's internal selection/spawn result cannot automatically become an Ouros combatant or canonical ecological fact;
- when a PTU fishing interaction is mechanically authoritative, the adapter must collect intent/context and route the decisive rule through the approved Ouros/AutoPTU path;
- a Cobblemon-fished entity can only enter tactical resolution after Ouros explicitly selects that persistent/generated actor into the encounter manifest.

This preserves the binding rule in `design/cobblemon-runtime-authority-boundary.md`.

### Cobblemon — Fishing Boat mini-structure

Source:
- https://wiki.cobblemon.com/index.php/Mini_Dungeon

Base Cobblemon includes a Fishing Boat mini-structure that can connect exploration to a Shipwreck Cove map and Poké Rod upgrade material.

Reusable implementation lesson:
Existing world structures and props can help coastal regions feel materially connected. Ouros may reuse compatible structures/assets or treat them as presentation inspiration, but their generated loot and map semantics should only become persistent narrative facts through reviewed adapter/world-state handoff.

## Structural findings for Ouros

### 1. Fishing effort and ecological outcome must be separate

A light or empty return can result from many facts:
- short effort window;
- changed route;
- gear problem;
- weather/service interruption;
- deliberate release;
- unsuccessful PTU fishing checks;
- changed target practice;
- actual ecological change;
- incomplete reporting.

Therefore one poor landing cannot prove population decline.

### 2. Hook, encounter, capture, release and landing are distinct events

A single fishing activity may produce:
- no contact;
- an item;
- a Pokémon contact that escapes;
- a reeled Pokémon that is released;
- a Pokémon that enters an explicitly composed tactical encounter;
- a legal capture event;
- a research observation/sample;
- a non-Pokémon food/resource batch where canon/rules support it.

Do not compress these into `catch=true`.

### 3. Landing site is a world-state node

The return from water to harbor/shore is where several systems meet:
- catch/release record;
- custody/provenance;
- food batch creation where valid;
- research observations;
- market handoff;
- sanitation/quality concerns;
- equipment return/repair;
- public knowledge and rumor;
- stewardship review.

The landing site should remain persistent even when no market sale occurs.

### 4. Managed use needs explicit evidence and authority

Conservation already permits a `managed harvest zone` as a descriptive use-zone concept. Pass 86 should link to that authority rather than invent quotas, seasons or enforcement powers.

A closure/restriction can exist only when a world-state actor/institution with approved mandate actually creates it. Ecological importance alone does not create law.

### 5. Market names are not biological identity

A local commercial or culinary name may refer to:
- one species;
- several species;
- a preparation category;
- a size/condition claim;
- a seasonal product label;
- a historical term that became imprecise.

Food provenance should keep the exact biological/material source separate from market language when the exact identity is known.

### 6. Fishing can be a profession without becoming compulsory combat

Playable scenes can include:
- route planning;
- gear preparation;
- observational surveys;
- release decisions;
- landing reconciliation;
- provenance disputes;
- gear recovery;
- market timing;
- stewardship meetings;
- seasonal practice change.

Combat should appear only when actual actors and circumstances justify it.

### 7. Cobblemon fishing should be treated as a deep presentation/integration opportunity

Candidate classifications for later code-level inspection:
- Poké Rod item/model/bobber/audio/particles: likely SAFE_REUSE;
- cast/reel interaction hooks and statistics: likely ADAPTER_REQUIRED;
- bait attachment UI/serialization: SAFE_REUSE or ADAPTER_REQUIRED depending on mechanical mapping;
- spawn-pool selection that decides which Pokémon appears: ADAPTER_REQUIRED for overworld ecology and BATTLE_AUTHORITY_FORBIDDEN if treated as tactical participant selection;
- any Cobblemon battle callback after a fished Pokémon appears: BATTLE_AUTHORITY_FORBIDDEN as an Ouros tactical authority.

Concrete APIs/classes still require source inspection before final classification.

## PTU/Caelo mechanical questions exposed

Before executable promotion, inspect authoritative project sources for:
- exact PTU fishing procedure chosen for Ouros;
- rod/bait/lure item mapping;
- Athletics interaction and time cost;
- legal capture/release sequence;
- whether a hooked Pokémon may initiate an attack and how that becomes a BattleSpec;
- any Caelo changes or encounter-location constraints;
- water movement and shore/boat positioning;
- any fishery/harvest rules beyond Pokémon capture;
- Trainer Features that modify fishing;
- equipment loss/custody implications when mechanically relevant.

Narrative design must not manufacture replacements for unresolved rules.

## Copyright / transformation boundary

Only high-level structures and publicly described mechanics are retained. No source dialogue, distinctive NPC, plot sequence, town layout, fan-made catch table or homebrew class is copied into Ouros.

## Recommended Pass 86 design direction

Create a fisheries/aquatic-harvest continuity extension that owns operational history and cross-system handoffs while leaving:
- tactical fishing/capture legality to PTU/Caelo/AutoPTU;
- habitats/populations to Ecology/Conservation/Wild Collectives/Science;
- food batches to Food;
- vessels/routes to Maritime/Travel;
- employment to Workplaces;
- sales/prices to Storefront/Finance;
- gear identity to Equipment/Material Culture;
- tactical battle truth entirely to AutoPTU.
