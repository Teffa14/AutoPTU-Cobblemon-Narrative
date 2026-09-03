# Marea interspecies predation, competition and territory scan — Pass 226

Status: RESEARCH / PROVENANCE. Not canon by itself.
Date: 2026-09-03

## Question

What is the smallest source-backed set of species relationships that can seed a real ecological interaction network for Marea without inventing a food web from type matchups, visual resemblance or generic animal analogies?

The target questions are concrete:

- who hunts or eats whom;
- who treats whom as a predator or threat;
- who competes for a resource;
- who excludes whom from territory;
- when avoidance, hiding, withdrawal or combat are plausible responses;
- which relationship is official species evidence versus original Ouros ecology.

## Design conclusion

Species relationships must be directional and contextual.

A `PREDATES_ON` edge is not an instruction to attack every encountered prey individual. A `TERRITORIAL_AGAINST` edge is not a global hostility flag. A prey relationship can change distribution, visibility and refuge use without a kill. Competition can occur through resource use or displacement without combat.

This is consistent with community ecology: species sharing a habitat interact through predation, competition and other relationships, and competition is commonly driven by limited resources. Predator presence can also change prey behaviour and habitat use without consumption.

Sources:

- OpenStax Biology 2e, Community Ecology: https://openstax.org/books/biology-2e/pages/45-6-community-ecology
- Scientific Reports, habitat degradation and predator non-consumptive effects: https://www.nature.com/articles/s41598-019-51798-2

## Pokémon species evidence

### Fletchling

Official Pokémon Pokédex evidence:

- Fletchling occurs in rural and urban environments.
- Fletchling and Squawkabilly have had a large territorial dispute.
- Fletchling is normally calm but becomes aggressive when battle begins.

Source:
- https://www.pokemon.com/br/pokedex/fletchling

Use:
- strong evidence for `TERRITORIAL_AGAINST(fletchling, squawkabilly)` when the species actually overlap;
- strong evidence that territorial friction can escalate into fighting;
- explicit evidence against treating every Fletchling as permanently aggressive.

Local status:
- the lower-Sendero level-5 Big Pecks Fletchling is already CANON as a persistent individual;
- this evidence does not canonize Squawkabilly in Marea.

### Squawkabilly

Official Pokémon Pokédex evidence:

- Squawkabilly prefers populated/city environments;
- it forms flocks by plumage and fights over territory;
- green groups search for food in morning/evening periods;
- yellow-plumage Squawkabilly can drive other bird Pokémon from towns.

Source:
- https://www.pokemon.com/br/pokedex/squawkabilly

Use:
- explicit territorial pressure;
- explicit displacement pressure on bird Pokémon for at least one form;
- useful compatibility with Puerto Bruma / lower Sendero only as a PROPOSED local population, not automatic canon.

Important guardrail:
- form/plumage-specific evidence must stay form-specific. Do not give every Squawkabilly population the yellow-plumage displacement behaviour.

### Wurmple

Official Pokémon Pokédex evidence:

- Wurmple is explicitly targeted by Swellow as prey;
- it responds to the attacking predator with a defensive rear-spike/poison behaviour rather than being passive prey;
- it feeds on tree sap.

Source:
- https://www.pokemon.com/us/pokedex/wurmple

Use:
- `PREDATES_ON(swellow, wurmple)` is provenance-explicit;
- Wurmple needs an anti-predator response profile, not a generic `always_flee` rule;
- tree/sap resources can connect prey distribution to vegetation without inventing a second predator relationship.

Local status:
- PROPOSED candidate only. Marea presence is not established by this research.

### Taillow

Official Pokémon Pokédex evidence:

- Taillow feeds on Wurmple in forests;
- it is described as a recently fledged young bird in one entry;
- it may stand its ground against stronger foes.

Source:
- https://www.pokemon.com/us/pokedex/taillow

Use:
- `PREDATES_ON(taillow, wurmple)` is provenance-explicit but has a forest-context requirement;
- even a small predator does not imply automatic flight from conflict;
- local use requires an actually authored compatible wooded/forest microhabitat.

Local status:
- PROPOSED candidate only.

### Swellow

Official Pokémon Pokédex evidence:

- Swellow spots prey from above, dives and grasps prey;
- the Wurmple entry names Wurmple specifically as Swellow prey.

Sources:
- https://www.pokemon.com/us/pokedex/swellow
- https://www.pokemon.com/us/pokedex/wurmple

Use:
- predation has a credible aerial-search/pursuit shape in the overworld;
- exact capture, grapple, escape and chase mechanics must not be fabricated from prose. If structured mechanics are needed, AutoPTU owns legality and outcome.

Local status:
- PROPOSED candidate only.

### Scatterbug

Official Pokémon Pokédex evidence:

- Scatterbug eats plants, with diet varying by where it lives;
- it emits poisonous powder to repel enemies;
- it can consume poisonous leaves/roots and convert the poison to its defensive powder.

Source:
- https://www.pokemon.com/us/pokedex/scatterbug

Use:
- good example of `FORAGES_RESOURCE` and anti-predator defense without inventing a named predator;
- candidate for future plant-resource and crop-edge interactions if Marea authors actually place it.

Local status:
- PROPOSED candidate only.

## First evidence-backed relationship table

| Actor | Target/resource | Edge | Evidence | Context | Marea status |
| --- | --- | --- | --- | --- | --- |
| Fletchling | Squawkabilly | `TERRITORIAL_AGAINST` | official explicit | rural/urban overlap; local contested resource required | Fletchling CANON, Squawkabilly PROPOSED |
| Squawkabilly | Fletchling | `TERRITORIAL_AGAINST` | official explicit reciprocal dispute | populated/route-edge overlap | PROPOSED local population |
| yellow Squawkabilly | other bird Pokémon | `DISPLACES` | official explicit form-specific | town/city | PROPOSED local population/form |
| Swellow | Wurmple | `PREDATES_ON` | official explicit | co-occurrence and compatible habitat | both PROPOSED locally |
| Taillow | Wurmple | `PREDATES_ON` | official explicit | forest microhabitat | both PROPOSED locally |
| Wurmple | tree sap | `FORAGES_RESOURCE` | official explicit | suitable trees | PROPOSED locally |
| Scatterbug | local plants | `FORAGES_RESOURCE` | official explicit category | suitable vegetation | PROPOSED locally |

## Avoidance / escape rule

Do not store `prey -> predator = always flees` as species canon unless a source supports that exact behaviour.

Instead:

```text
predator relationship
+ current individual state
+ relative capabilities
+ distance / cover / exits
+ young / nesting / feeding context
+ previous alarm state
+ human traffic / habituation
    -> candidate anti-predator responses
       [ignore, freeze, hide, withdraw, evade, warn, defend, fight]
```

The species edge creates a risk prior. The individual chooses or is assigned a plausible response from current state and capabilities. If the response enters structured combat, AutoPTU supplies legal actions and authoritative resolution.

Wurmple is the first useful example: official material gives both the predator and an active defensive response. It therefore must not be flattened into a helpless-prey script.

## Territory rule

Territory must name the contested resource or space. Examples:

- nest site;
- roost;
- feeding patch;
- shelter;
- water access;
- bounded settlement/structure space;
- breeding display site.

`TERRITORIAL_AGAINST` without a local resource/space is incomplete.

For Fletchling/Squawkabilly, the official relationship proves that territorial conflict exists at species level, but Marea still needs to establish what they would contest locally before the edge becomes active world truth.

## Competition rule

Do not derive `COMPETES_WITH` merely because two species have the same Diet category.

A competition candidate requires:

1. actual co-occurrence;
2. an identified resource or space both can use;
3. overlapping activity/access;
4. evidence or authored Ouros justification that the resource can be limiting enough to matter.

This allows competition to appear or disappear as resources change rather than being hard-coded permanently.

## Proposed first Marea ecological scope

Keep the first authored network small enough to observe and debug:

### Confirmed local anchor
- Fletchling — CANON persistent lower-Sendero individual/species presence.

### Candidate additions requiring explicit canon approval
- Squawkabilly — strongest candidate because it gives Fletchling a direct, official, interspecies territorial edge and is compatible with populated environments.
- Wurmple — gives a defensible low-trophic resource user and explicit prey relationship.
- Swellow — gives an explicit Wurmple predator.
- Taillow — optional second Wurmple predator only if a wooded/forest microhabitat is authored.
- Scatterbug — optional plant-resource species for future herbivory/defense interactions; no named local predator should be invented yet.

Do not canonize all five at once just to fill a graph. The graph can carry proposed candidates until the ecosystem roster is approved.

## Engine boundary

The species graph, local ecological pressure, off-screen demographic estimates and spawn-weight projections are Ouros world-state responsibilities.

AutoPTU is needed only when an ecological event becomes structured mechanics. It remains authoritative for legal actions, positions, HP/status and battle outcome.

Minecraft/Cobblemon can render presence, movement, natural spawn candidates and visible playback but cannot create the ecological truth merely because a Pokémon happened to spawn.

## Open questions

- Which exact Sendero/Loma Clara microhabitats are canonically wooded enough for the Wurmple/Taillow/Swellow evidence to apply?
- Do we want Squawkabilly as the first second wild species in the populated Marea edge, or reserve it for a later urban district?
- Which local resources should Fletchling and Squawkabilly contest in Marea: roost, feeding site, nesting site, or bounded settlement space?
- Which PTU/PTR species data source is the approved authority for Diet/Habitat and individual movement capabilities when Pokémon prose is silent?
