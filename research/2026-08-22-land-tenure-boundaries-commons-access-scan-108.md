# Pass 108 Research — Land Tenure, Boundaries, Commons & Access

Status: RESEARCH / PROVENANCE ONLY. Nothing in this document is established Ouros canon. External material is used only for high-level structural inspiration. No protected prose, distinctive character, plot, legal regime or game mechanic is imported.

## Why this pass exists

The repository already has strong layers for homes, civic governance, conservation, agriculture, forestry, routes, public space, credentials, cartography, cases and agreements. Those documents repeatedly need concepts such as ownership claims, occupancy, access, stewardship and land-use coordination, but no single layer currently owns the relationship between a physical place and the different permissions or claims attached to it.

That missing layer matters because the same field can be:
- occupied by one household;
- farmed by another actor under a valid arrangement;
- crossed by a route used by the public;
- seasonally used by a herd;
- monitored by researchers;
- subject to a conservation buffer;
- crossed by a utility line;
- disputed on an old map;
- physically unchanged while its authorized uses change.

A persistent world needs to preserve those distinctions instead of collapsing them into `owner_id`.

## Existing Ouros boundaries reviewed

Before research, the current branch was inspected, including the full design tree and the most relevant systems.

`homes-housing-neighborhoods-layer.md` explicitly states that residence, household, access and ownership claims are distinct.

`civic-governance-public-works-layer.md` allows land-use coordination as a possible mandate but deliberately refuses to invent governance powers.

`conservation-protected-areas-stewardship-layer.md` separates ecological state, stewardship, visitor policy and enforcement capacity.

`cartography-survey-wayfinding-layer.md` already supports versioned maps and survey observations.

`case-authority-custody-layer.md`, `agreements-mediation-repair-layer.md`, `credentials-permissions-eligibility-layer.md`, `forest-management-silviculture-timber-layer.md`, `grasslands-grazing-rangeland-ecology-layer.md`, `food-agriculture-hospitality-layer.md`, `road-ecology-crossings-linear-infrastructure-layer.md` and `architecture-built-environment-adaptive-reuse-layer.md` all need a shared place-use contract but should keep authority over their own domains.

No dedicated land-tenure / parcel / common-use layer was present in the inspected design tree.

## Public Pokémon sources

### 1. Farm ownership can coexist with a wildlife-use problem

Source: Pokémon animation, “How Are You Gonna Keep ’Em Off of the Farm?”
https://www.pokemon.com/us/animation/seasons/24/episode-4-how-are-you-gonna-keep-em-off-of-the-farm

Reusable structure:
- a farm has a recognized human operator/owner;
- Diglett and Dugtrio begin using the farm after disturbance displaced them from another place;
- the conflict is resolved by investigating why they arrived instead of treating presence on the farm as proof of malicious trespass.

Ouros lesson:
A valid human claim to use a field and a valid ecological explanation for Pokémon presence can both be true. Land-use state should not determine wild-Pokémon intent or automatically authorize capture/removal.

### 2. A land sale, upstream access and water dependency are separate issues

Source: Pokémon animation, “The Young Flame Strikes Back!”
https://www.pokemon.com/us/animation/seasons/21/episode-26-the-young-flame-strikes-back

Reusable structure:
- a family farm is a persistent livelihood and place;
- a developer wants to acquire the site for another use;
- land upstream becomes relevant because control of one location affects water reaching another;
- the conflict contains sale pressure, infrastructure/resource dependency and misconduct as separate facts.

Ouros lesson:
A parcel boundary should not be treated as the boundary of every dependency. Water, roads, wildlife corridors, utility lines and public access may cross multiple land units. A dispute over one permission should not rewrite all others.

Copyright boundary:
No named characters, resort plot, battle wager, dialogue or episode sequence is reused.

### 3. Land can change purpose after ecological displacement becomes visible

Source: Pokémon animation, “Taming of the Shroomish”
https://www.pokemon.com/us/animation/seasons/6/episode-9-taming-of-the-shroomish

Reusable structure:
- urban development removed previous forest habitat;
- displaced Pokémon persist in a remaining structure;
- the human owner’s family changes the future use of the site after learning what happened.

Ouros lesson:
Land-use revisions should be versioned. A site can move from forest to mansion to demolition project to restoration area while remaining the same persistent place. Changing use should create history rather than replacing the old state.

### 4. Controlled access can exist without transferring ownership or permanent rights

Source: official Brilliant Diamond/Shining Pearl Trainer Guide — Great Marsh
https://diamondpearl.pokemon.com/en-au/trainersguide/fundamentals/

Reusable structure:
- visitors pay for scoped entry to a defined area;
- access has explicit limits and special activity rules;
- admission does not make the visitor an owner, resident or steward.

Ouros lesson:
Access permissions need scope, duration and activity limits. Physical entry, research access, harvest permission, building authority and transfer authority must stay separate.

### 5. A ranch can have an identified operator while Pokémon presence remains separate from land ownership

Source: official My Pokémon Ranch page
https://www.pokemon.com/us/pokemon-video-games/my-pokemon-ranch

Reusable structure:
- the ranch has a named owner/operator;
- Pokémon can be deposited there and interact in the space;
- the place’s identity persists as its population changes.

Ouros lesson:
Owning or operating land does not imply ownership of every Pokémon physically present there. Pokémon custody/party state continues to belong to Pokémon Agency and breeding/care systems.

### 6. A wealthy estate can deliberately be used as a public-facing Pokémon garden

Source: Pokémon animation, “Hungry for the Good Life!”
https://www.pokemon.com/us/animation/seasons/11/episode-32-hungry-for-the-good-life

Reusable structure:
- a privately associated mansion/garden can still welcome visitors;
- public use is a policy layered over the underlying place relationship;
- wildlife can enter the site without automatically becoming property.

Ouros lesson:
Private use, public access and ecological permeability are separate axes.

## PTU / tabletop / roleplay material

### 7. Physical use of a landscape can trigger consequences without a formal land-law subsystem

Source: public PTU campaign log #24
https://www.reddit.com/r/PokemonTabletop/comments/wudfhz

Reusable structure:
- a Trainer cuts down a tree during exploration;
- a nearby Pokémon reacts because the action affected nesting context;
- restoration/replanting becomes part of the resolution.

Ouros lesson:
The world should remember physical interventions independently of whether anyone has authored legal ownership. A tree can be within a land unit, wildlife habitat, route context and resource-use claim at the same time.

This log has already informed ecological passes, so Pass 108 uses it narrowly for the new boundary between permission-to-use land and ecological consequence. No homebrew rule is imported.

### 8. Campaign settings become richer when land use affects livelihoods and institutions

Source: publicly accessible PTU Game of Throhs campaign-setting material, “Six Duchies” excerpts indexed online
https://www.scribd.com/document/785005535/Pokemon-Tabletop-United-Game-of-Throhs

Reusable high-level pattern:
- regions can be distinguished by agriculture, forestry, mining and settlement use;
- changing what land produces can affect residents for years;
- territorial administration, livelihoods and resource systems can intersect.

Ouros lesson:
Land-use change should be a world-state handoff to Agriculture, Forestry, Geology, Workplaces, Demography and Markets, not a cosmetic label.

Caution:
This source is PTU-adjacent setting material, not an Ouros rules authority. No political structure, duchy, economy, class, equipment or mechanic is imported.

## External systems research used only as abstraction

### 9. Tenure is a relationship about who can use a resource, for how long and under what conditions

Source: Food and Agriculture Organization of the United Nations — Governance of Tenure
https://www.fao.org/tenure/en/

FAO describes multiple forms of tenure and emphasizes that systems determine who can use resources, for how long and under what conditions.

Ouros adaptation:
Do not import real property law. Keep the abstract modeling insight: the relationship between actor and place should have explicit scope, duration, source and conditions.

### 10. Multiple actors can hold different rights over the same physical place

Source: FAO — “What is Land Tenure”
https://www.fao.org/4/Y4307E/y4307e05.htm

Source: FAO — “What is Access to Land”
https://www.fao.org/4/Y4308E/y4308e04.htm

Reusable abstraction:
One party may have use permission, another decision authority, another passage access and another transfer authority.

Ouros adaptation:
Model permissions as separate relationship records. Avoid a universal `owner_can_do_everything` rule.

### 11. Forest access, management and transfer can be held under different arrangements

Source: FAO Forest Tenure
https://www.fao.org/sustainable-forest-management-toolbox/modules/forest-tenure/en

Reusable abstraction:
Access, use, management and transfer can be separated; communal/open/public/private arrangements are not interchangeable.

Ouros adaptation:
A forest can support common gathering, restricted timber harvest, public transit and conservation management at the same time if canon explicitly establishes those relationships.

Cultural safeguard:
Real Indigenous/customary tenure systems are not templates to reskin into fictional peoples. Ouros should author its own institutions and practices. Real-world sources are used only to learn that tenure can be plural and layered.

## Design lessons extracted

1. Physical land identity should persist even when use changes.
2. Boundary geometry, a mapped boundary and an actor’s belief about the boundary are separate states.
3. Occupancy, residence, stewardship, access, use, management, exclusion and transfer authority must be independently representable.
4. A place can have overlapping valid uses.
5. A right to pass through a place does not imply a right to harvest, build or camp there.
6. Seasonal use should expire or pause without deleting history.
7. Commons/shared-use areas need explicit eligible groups and activity scopes; “public” and “common” are not synonyms.
8. Physical access in Minecraft does not prove narrative authorization.
9. A fence, sign or locked gate is evidence of an implemented control, not proof that the underlying claim is valid.
10. A map disagreement can arise from old surveys, physical change, different scopes or an unresolved claim; it does not automatically imply fraud.
11. Wild Pokémon presence does not create or erase human land claims and human tenure does not create Pokémon ownership.
12. Land-use change should propagate to the systems actually affected instead of directly spawning quests.
13. Land disputes should use Cases for evidence, Agreements for negotiated settlements, Governance for authored public decisions and Institutional Review only where a legitimate review body exists.
14. The generator must not invent a universal property code for Ouros.
15. Player-created structures need explicit authority to alter shared world space in multiplayer.

## PTU/Caelo mechanical boundary

No land-tenure mechanic should be inferred from PTU battle rules.

Potentially relevant PTU/Caelo topics that still require authoritative project-source extraction before mechanical use include:
- Survival and navigation where access depends on routefinding;
- Guile/Charm/Command/Intimidate if a social dispute reaches a Skill check;
- Groundshaper or terrain-changing capabilities when a player physically modifies land;
- Naturewalk when a legal battle occurs in a tagged environment;
- capture/release/custody rules when Pokémon are present on managed land;
- carrying/building/crafting Features where land-use projects become physical work.

None of these establish ownership, tenure, legal access or authority.

The full primary Caelo corpus was not reliably accessible during this run. Super PTU Online Helper was not exposed as an invokable capability. No output was invented from either source.

## Originality boundary for Pass 108

The proposed Ouros layer will use original schemas and original scenarios. External sources contribute only abstract patterns such as layered access, versioned land use, scoped admission, displaced wildlife, competing dependencies and long-term land-use change.
