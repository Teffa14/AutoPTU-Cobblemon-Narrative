# Food, Agriculture & Hospitality Research — Pass 18

Status: research/provenance only. Nothing in this file is automatically Ouros canon.

## Why this pass exists

The repository already models material provenance, workshops, settlement services, ecology, crises, public events, care, breeding and social institutions. It does not yet model food as a distinct cultural and ecological system. Food is unusually cross-cutting in Pokémon: it can be a PTU mechanical item, a crop, a gathered resource, a profession, a social ritual, a business, a settlement service, a festival tradition, a care practice, a travel supply and an ecological pressure.

This pass separates those roles so future worldbuilding can use food without inventing new PTU rules or collapsing every meal into a combat bonus.

## Sources inspected

### Pokémon Tabletop United — Chef and food items

Public mirrors/reference pages for PTU 1.05 show that Chef is a Professional Class built around crafting food and requires access to a kitchen or Cooking Kit. The class explicitly supports culinary identity outside battle as well as combat-supporting recipes. PTU food items use Digestion Buffs; Berries are a major food category, and plant resources have their own harvesting/yield structure.

Sources:
- https://pturpg.wikidot.com/consumables
- https://anyflip.com/deia/psdg/basic/101-150

Reusable lesson:
Food already has mechanical authority in PTU. Ouros should model provenance, production context, cuisine, institutions and consequences around the mechanic while leaving actual recipe effects, Digestion Buffs, costs, prerequisites and yields to authoritative PTU/Caelo data.

### Existing Python AutoPTU evidence

The project-designated Python oracle currently contains explicit Food Buff state and logic, including Chef taste handling, Digestion Buff trades, Harvest interactions, Lunchbox interactions and item-derived food data. This is strong evidence that food is not merely flavor in the current engine lineage.

Project source inspected read-only:
- Teffa14/AutoPTU
- `battle_state.py` food-buff / Chef handling

Reusable lesson:
Any future Java food implementation belongs primarily to the permanent capability families `items`, `abilities`, `Trainer Features/perks`, `status lifecycle`, `full turn/round lifecycle`, `full stateful damage pipeline` and `move-specific behavior` where relevant. Minecraft should not reproduce Food Buff arithmetic itself.

### Pokémon Camp — cooking as team/social activity

Pokémon Sword/Shield's official Pokémon Camp material presents curry as a shared activity using ingredients and Berries, with the resulting dish depending on the chosen inputs.

Source:
- https://swordshield.pokemon.com/pt-pt/gameplay/pokemon-camps/

Reusable lesson:
A meal can be a social event and a record of who participated, where ingredients came from and what happened around it, even when the mechanical food result is resolved separately.

### Pokémon Café ReMix — service, menu and institutional growth

Official Pokémon Café ReMix material connects customer orders, Pokémon staff, menu development, friendship, new ingredients and physical café expansion. New menu items can attract new visitors, and milestones can change the café's tools or spaces.

Sources:
- https://www.pokemon.com/uk/pokemon-video-games/pokemon-cafe-remix
- https://support.pokemon.com/hc/en-us/articles/4409138427796-What-kind-of-game-is-Pok%C3%A9mon-Caf%C3%A9-ReMix

Reusable lessons:
- a food venue can be a persistent social institution rather than a static shop menu;
- menus can change who visits a location;
- staff identity and facility upgrades can become world state;
- service work can generate relationships and rumors without requiring combat.

Do not copy Café ReMix's puzzle mechanics or progression economy.

### Pokémon Pokopia — cultivation changes habitation

The official Pokémon Pokopia page describes growing vegetables, collecting materials and using Pokémon-linked abilities to alter the environment; a more developed settlement attracts Pokémon visitors. The February 2026 Pokémon Presents also identifies cooking and serving preferred dishes as part of settlement life.

Sources:
- https://www.pokemon.com/uk/pokemon-video-games/pokemon-pokopia
- https://www.pokemon.com/us/news/news-and-updates-from-the-pokemon-day-2026-pokemon-presents

Reusable lesson:
Agriculture and food can feed back into settlement ecology. A garden, orchard or kitchen can alter who visits, works or forages nearby. In Ouros, however, any Pokémon capability used to water, heat, harvest, carry or process materials must be validated from that individual Pokémon's authoritative capability state.

### Poké Pelago — cultivation as an infrastructure project

Official Pokémon material on Poké Pelago includes an island dedicated to Berry cultivation and connects expansion to Pokémon population and resource investment.

Source:
- https://www.pokemon.com/fr/articles/passez-a-la-vitesse-superieure-avec-poke-loisir

Reusable lesson:
Cultivation can be settlement infrastructure with capacity, development state and long-term outputs rather than a repetitive click-per-plant chore.

### Johto visitor guide — food and agriculture as regional texture

Pokémon's official Johto guide explicitly calls out Berry trees as part of travel and local life, and local shops change according to story state.

Source:
- https://www.pokemon.com/us/strategy/a-visitors-guide-to-johto

Reusable lesson:
Regional food sources, stores and roadside harvests help places feel materially distinct. Ouros can use food origin as geography and cultural identity without assigning invented stat bonuses.

## Fangame/community research

### Pokémon: The Slowpoke Shack

A completed fangame built around running a restaurant and slice-of-life problems.

Source:
- https://eeveeexpo.com/slowpoke-shack/

Reusable lesson:
A restaurant can sustain a compact narrative campaign through staff, customers, suppliers and daily operational problems rather than acting only as a vendor.

### Pokémon Family Restaurant

The player's struggling family restaurant is revitalized through an old cookbook and ingredients gathered across an island; the project advertises multiple endings depending on player actions.

Source:
- https://eeveeexpo.com/threads/8774/

Reusable lessons:
- recipe provenance can connect family/public memory to exploration;
- ingredient quests can reveal places instead of functioning as generic fetch tasks;
- a business can change because of choices, not only currency accumulation.

Do not copy its family, cookbook, island, recipes, endings or plot.

### Pokémon FarmVille

A completed Pokémon farming project focused on farming and taking care of Pokémon.

Source:
- https://eeveeexpo.com/threads/5169/

Reusable lesson:
Agriculture can itself be the play fantasy. Ouros should therefore support farm/ranch/orchard characters whose progression is meaningful even if they do not prioritize the League.

### Pokémon Beekeeper

A completed fangame centered on an apiary and honey gathering.

Source:
- https://eeveeexpo.com/beekeeper/

Reusable lesson:
A single resource ecology can support a location identity, profession and repeated local stories. Ouros should model apiaries, orchards and fisheries as world institutions with ecological dependencies rather than infinite resource nodes.

### Pokémon Berry Shake

An in-development fangame describes a shop/exploration loop with involved drink-making, quests and no battles.

Source:
- https://eeveeexpo.com/threads/9278/

Reusable lesson:
Food-production gameplay can remain meaningful without combat. That is valuable for Ouros because crafting/service/exploration careers should not require tactical battles merely to justify their existence.

### Pokémon Alexandrite

The project includes a player-owned Berry Farm and broad crafting/sidequest systems.

Source:
- https://eeveeexpo.com/threads/4087/

Reusable lesson:
A persistent agricultural holding can coexist with a conventional Pokémon journey as an optional home/project layer.

## PTU community warnings worth preserving

Community discussion around expanded cooking repeatedly demonstrates a danger: once a GM adds hunger, ingredient-unit accounting, custom flavors or expanded cooking effects, Chef can become entangled in large amounts of homebrew bookkeeping.

Source:
- https://www.tapatalk.com/groups/pokemon_tabletop/ptu-cooking-expanded-houserules-help-t3145.html

Design lesson:
Ouros must not add survival hunger, nutrition meters, starvation Injuries, custom food-combat math or ingredient-unit simulation by default. If such systems are ever desired, they need an explicit separate rules decision and implementation contract.

Another PTU discussion shows that Chef's effectiveness strongly depends on actual opportunities to rest, cook, access ingredients and use Food Buffs. That is useful narratively: world access matters, but the generator should not compensate by fabricating stronger food effects.

Source:
- https://www.tapatalk.com/groups/pokemon_tabletop/first-time-ptu-player-having-trouble-making-a-buil-t5795.html

## High-level structures extracted

1. Food has at least four separate identities: mechanical consumable, physical/provenance object, cultural practice, and social/service event.
2. Cuisine can make regions different without requiring unique combat rules.
3. Farms, orchards, fisheries, apiaries and kitchens should be service/infrastructure nodes with capacity and dependencies.
4. Ingredient scarcity should come from explicit ecology, season, crisis, transport or institutional state rather than random scarcity rolls.
5. Recipes can carry provenance, authorship and cultural ownership independently from mechanical item definitions.
6. Menus can affect visitors, markets and social activity without needing reputation points every time someone eats.
7. Pokémon may participate in agriculture or kitchens only through authored behavior plus authoritative capabilities; species flavor alone is insufficient.
8. Perishability should be modeled only where it creates a meaningful decision. It should not become constant inventory decay by default.
9. Routine meals and crop maintenance should compress. Playable scenes appear when a decision, discovery, relationship or failure state intersects them.
10. Community meals, markets and festivals are strong convergence points for unrelated arcs.

## Copyright / transformation boundary

The sources above are used only for high-level system and narrative structures. Ouros should not copy named fangame characters, restaurant names, recipes, dialogue, plot sequences, puzzle designs, endings or distinctive settings. Official Pokémon mechanics may be referenced for comparison but are not PTU rules authority.

## Questions for later passes

- Which exact Chef recipes and Food Buff rules from PTU/Caelo will Ouros use?
- Which food-related Python AutoPTU behaviors have parity-backed Java equivalents yet?
- How will Minecraft represent kitchens, farms and markets without requiring simulation of every plant or meal?
- Which wild-resource loops should affect Cobblemon spawning or only narrative world state?
- What privacy/ownership rules apply to culturally significant recipes?
- How should offline world time affect crops, fermentation, deliveries and restaurant schedules?
- Which forms of spoilage, if any, are worth implementing rather than abstracting?
