# Fashion, Clothing & Visual Culture Research — Pass 44

Status: research/provenance only. Not Ouros canon. External fiction and games are inspiration sources, not rules sources.

## Why this pass

The repository already has systems for material provenance, crafting, workplaces, contests, public memory, accessibility, infiltration, institutions and social identity. It did not yet have a dedicated layer for clothing, outfits, uniforms, fashion work, grooming, wardrobes or visual presentation.

That gap matters because clothing can connect several existing systems without needing to become a combat mechanic:

- personal self-expression;
- city and regional culture;
- occupational identity;
- institutional uniforms;
- performance and public events;
- material production and repair;
- disguise and mistaken identity;
- accessibility and protective equipment;
- photography and public memory;
- historical collections and inheritance.

Repository search before writing found no existing dedicated fashion/clothing/textile/uniform layer.

## Source 1 — Pokémon Legends: Z-A: Lumiose style and boutiques

Source: The Pokémon Company, “Adventuring in Your Own Style”, 22 July 2025.

URL: https://legends.pokemon.com/en-us/news/adventure-in-style

Useful structure:

- Lumiose is presented as a fashion center rather than fashion being only a character menu.
- boutiques provide different garments;
- salons provide hair and appearance services;
- appearance can be changed repeatedly during an ongoing adventure;
- Furfrou grooming exists as a specialized service;
- the grooming shop itself has a learning/progression idea, with more difficult trims becoming available through practice.

Reusable Ouros lesson:

Fashion can exist as a network of physical services, specialists, shops, local styles and personal choices. A wardrobe should be persistent world state and not only a one-time character-creation screen.

Do not copy exact outfits, shop names or Furfrou trim progression.

## Source 2 — Pokémon Legends: Z-A: Naveen as an aspiring designer

Sources:

https://legends.pokemon.com/en-us/news/team-mz
https://legends.pokemon.com/en-us/story-world/characters/naveen

Useful structure:

- a recurring adventure character can have a fashion career independent of battling;
- studio space is a meaningful resource;
- professional reputation can grow alongside the main adventure;
- a creative profession can give a character reasons to care about neighborhoods, materials, clients, events and workspace.

Reusable Ouros lesson:

A designer, tailor, stylist, dyer or groomer can be a persistent NPC profession with its own projects and career state. Their narrative value does not depend on giving clothing combat bonuses.

## Source 3 — Lumiose City: style as city culture

Source: Pokémon.com, “Illuminating Lumiose City”, 9 October 2025.

URL: https://www.pokemon.com/us/features/illuminating-lumiose-city

Useful structure:

Pokémon X/Y connected “style” with broader participation in city life, including restaurants, transport, grooming and other cultural activities. Boutique Couture also used a style-access gate.

Reusable Ouros lesson:

A city can have a recognizable visual culture and social expectations that emerge from many institutions, not merely clothing purchases.

Important adaptation boundary:

Ouros should not implement a hidden universal “fashion score” that determines human worth or city access. Access restrictions must come from authored institutions and explicit reasons. Public recognition can exist, but it stays separate from intrinsic character value.

## Source 4 — Galar boutiques and regional inventory

Source: official Pokémon Sword/Shield site, “Put on your favorite clothes, get a new hairdo, and set out on your adventure in style”.

URL: https://swordshield.pokemon.com/en-us/gameplay/clothes-hairdo-style/

Useful structure:

- different towns can offer different clothing;
- wardrobes can mix pieces rather than forcing full fixed outfits;
- appearance can connect to formal institutional presentation such as the Gym Challenge uniform.

Reusable Ouros lesson:

Regional and settlement-specific availability can make travel visually meaningful. A local textile, cut, badge placement, hat style or work garment can identify a place without granting mechanical power.

## Source 5 — Hearthome Collection and professional fashion ecosystem

Source: Pokémon.com animation episode page, “Arriving in Style!”, Season 11 Episode 34.

URL: https://www.pokemon.com/uk/animation/seasons/11/episode-34-arriving-in-style

Useful structure:

The episode combines designers, Pokémon/Trainer outfits, a public fashion show, judges, an editor-in-chief, celebrity participation and a commercial campaign opportunity.

Reusable Ouros lesson:

Fashion can create a professional ecosystem around:

- designers;
- models/performers;
- photographers;
- editors;
- venues;
- clients;
- ateliers;
- public showcases;
- press coverage;
- commissions.

This can connect naturally to the existing Contest, Media, Workplaces and Public Memory layers.

Do not copy the episode’s characters, designs, dialogue or competition.

## Source 6 — PTU Fashionista warning from the official developers

Source: Pokémon Tabletop RPG, “A Fresh Start! And PTU 1.05 News”.

URL: https://pokemontabletop.com/a-fresh-start-and-ptu-1-05-news/

The PTU developers explicitly noted that the Fashionista Class needed rework and that its update was being delayed until they could resolve larger Contest subsystem questions.

Reusable Ouros lesson:

Fashion-related PTU mechanics require especially careful source validation. Narrative systems must not infer that an outfit, accessory or designer career grants Appeal, Contest, Skill, Evasion, Defense or other bonuses.

This pass therefore treats clothing as world state until the exact governing PTU/Caelo rules are extracted and validated.

## Source 7 — Fashion as user-created social activity

Source: PokeMMO community event, “urCute’s Fancy Fashion Contest”.

URL: https://forums.pokemmo.com/index.php?/topic/143597-unofficial-event-%E2%98%85%E2%98%86a%C3%AFr-urcutes-fancy-fashion-contest%E2%98%86%E2%98%85/

Useful structure:

The event explicitly valued creativity rather than rarity or price, and encouraged participants to use location and Pokémon companions as part of the composition.

Reusable Ouros lesson:

Player fashion events can emphasize composition, theme and community expression without becoming wealth contests. A rare garment should not automatically produce higher prestige than a cheap but meaningful or creative outfit.

This is a community example, not an authoritative Pokémon or PTU source.

## Source 8 — Fangame wardrobe implementation pattern

Source: Eevee Expo, DarrylBD99’s Wardrobe resource for Pokémon Essentials.

URL: https://eeveeexpo.com/resources/1117/

Useful implementation pattern:

The resource separates stored outfit choices from the presentation used to select them. That reinforces a useful architecture for Ouros: wardrobe state belongs in the game/world model, while Minecraft UI is only one presentation layer.

Do not copy code or assets from the resource.

## Source 9 — Avatar customization and identity research

Source: Fu et al., “Understanding Children’s Avatar Making in Social Online Games”, 2025.

URL: https://arxiv.org/abs/2502.18705

The study reports motivations including self-representation, alter-ego experimentation and social needs, and observes that participants may create multiple looks while repeatedly returning to a preferred one.

Reusable Ouros lesson:

Wardrobe history can support identity continuity without allowing the generator to infer private personality traits from clothing. A frequently worn outfit can become publicly recognizable; it must not become a claim about gender, class, beliefs, sexuality, morality or emotional state unless the player explicitly establishes that meaning.

## Cross-source patterns worth carrying forward

### Fashion belongs to places

Cities, neighborhoods and regions can have different ateliers, materials, cuts, grooming traditions, uniforms and public events. Visual culture can make travel recognizable before a quest begins.

### Clothing can have provenance

A garment may be commissioned, gifted, repaired, inherited, issued by an institution, used during a famous event or preserved in a collection. This connects directly to the existing material-provenance system.

### Appearance can be public information without being objective truth

People can recognize a uniform, famous coat or recurring color scheme. They can also misidentify someone from appearance. Clothing is evidence of appearance, not proof of membership, motive or identity.

### A visual career can exist outside combat

Tailors, designers, stylists, dyers, cobblers, groomers, photographers and models can have durable careers and projects.

### Clothing should not become a wealth ladder

Price, rarity, cultural meaning, craftsmanship, public fame and personal significance are different dimensions.

### Pokémon clothing needs a welfare boundary

A Pokémon wearing a garment or accessory should not imply consent, ownership, happiness or mechanical benefit. Species fit, behavior and welfare need explicit support when the design becomes more than cosmetic.

## Connections to existing Ouros systems

Material Culture & Crafting:
- textile/material provenance;
- commissions;
- repair;
- maker marks;
- heirloom garments.

Contest & Performance:
- stage outfits;
- rehearsal requirements;
- public shows;
- designers and photographers;
- formal Contest mechanics remain separate.

Workplaces:
- ateliers;
- laundries;
- salons;
- tailoring shops;
- costume departments;
- uniform suppliers.

Infiltration:
- presented identity;
- disguises;
- uniforms;
- observer belief;
- no automatic Guile/Stealth bonus.

Archives & Museums:
- historic clothing;
- provenance disputes;
- conservation;
- replicas.

Accessibility:
- adaptive clothing;
- mobility-compatible garments;
- sensory preferences;
- protective equipment;
- presentation options.

Public Memory & Media:
- iconic outfits;
- event photographs;
- public misidentification;
- changing style over a career.

## Copyright and originality boundary

The research may preserve source names, titles, URLs and high-level factual descriptions.

Ouros proposals must not copy:

- exact proprietary garment designs;
- named fashion brands from source fiction;
- distinctive character wardrobes wholesale;
- dialogue;
- event plots;
- source-specific fictional designers;
- proprietary artwork or sprites.

The implementation should create original Ouros designers, garment traditions, institutions, districts, events and visual motifs.

## PTU/Caelo questions requiring dedicated source extraction

Before any outfit affects mechanics, validate:

- whether the supplied PTU/Caelo corpus contains Fashionista or related Features;
- exact Contest accessory rules, if any;
- any equipment slots or worn-item rules relevant to garments;
- any disguising rules under Guile/Stealth;
- protective clothing or environmental gear rules;
- Pokémon accessory/equipment restrictions;
- whether Caelo modifies any of those systems.

Until then, fashion state is narrative/cosmetic only.

## Research directions for later passes

- textile and dye traditions in official Pokémon locations;
- Pokémon grooming professions and welfare;
- uniforms as institutional history;
- clothing repair and reuse after expeditions;
- adaptive clothing and accessibility;
- historical fashion as archaeological evidence;
- fashion journalism and photography;
- cosplay, ceremonial dress and performance costume boundaries;
- Minecraft/Cobblemon cosmetic-slot feasibility without moving PTU authority into the adapter.
