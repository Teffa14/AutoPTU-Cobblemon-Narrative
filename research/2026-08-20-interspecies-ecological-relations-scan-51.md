# Interspecies Ecological Relations Research — Pass 51

Status: research/provenance only. Not Ouros canon. External material is used for high-level structural analysis. No protected prose, distinctive fan characters, dialogue or plots are imported.

Date: 2026-08-20

## Why this pass exists

The repository already models encounter ecology, wild populations, persistent collectives, migration, conservation, seasonal behavior, observation, habitat pressure and individual Pokémon agency.

It does not yet have a dedicated contract for persistent relationships between species or populations.

That missing layer matters because an ecosystem can change even when no population disappears. A food source can shift. A scavenger can begin following another species. A predator can concentrate around a seasonal route. A parasite can affect host behavior. Two species can share a resource without being allies. One species can create habitat that another later uses.

The design goal is to make those relationships observable and consequential without turning Pokémon into a deterministic food-chain simulator or inventing death, reproduction, fear, hunger, predation mechanics or species psychology.

## Existing Ouros boundaries inspected

This pass was checked against the repository tree and especially:

- `design/wild-collective-agency-layer.md`;
- `design/conservation-protected-areas-stewardship-layer.md`;
- `design/observation-settlement-time-layer.md`;
- `design/seasonality-calendar-phenology-layer.md`;
- `design/pokemon-agency-partnership-release-layer.md`;
- `design/crisis-rescue-recovery-layer.md`;
- `design/maritime-coasts-depths-layer.md`;
- `design/science-research-discovery-layer.md`;
- `design/encounter-implementation-contracts.md`;
- the engine-readiness snapshots through Pass 50.

Repository search found no dedicated predator/prey, trophic-network, scavenging, parasitism or interspecies-relation layer.

The new layer must therefore connect existing populations and collectives rather than replace them.

## Source findings

### Mantine and Remoraid — scavenging association

Official source:
https://www.pokemon.com/us/pokedex/mantine

The Pokédex describes Remoraid attaching to Mantine and scavenging leftovers while Mantine tolerates the association.

Reusable structure:

- two species can repeatedly co-occur for a concrete resource reason;
- one participant may gain a benefit without the source claiming a reciprocal benefit;
- association does not imply friendship, ownership, command or battle alliance;
- observed co-occurrence can become a research question before the relationship is understood.

Ouros should not automatically label every Mantine/Remoraid pairing as mutualism. The evidence supports a recurring association and scavenging behavior.

### Heatmor and Durant — direct predation plus defensive response

Official sources:
https://www.pokemon.com/us/pokedex/heatmor
https://www.pokemon.com/us/pokedex/durant

Heatmor is explicitly described consuming Durant. Durant is described retaliating against Heatmor and collectively protecting eggs from threats.

Reusable structure:

- predator/prey relationships can produce persistent spatial pressure;
- prey species may change nesting or defensive behavior in response;
- collective defense can be a world-state fact without granting a combat buff;
- predator presence can alter where another species is observed even before population counts change.

Do not infer a universal kill-on-contact rule. A specific tactical encounter still resolves through PTU/AutoPTU.

### Arrokuda — predator that is also prey

Official source:
https://www.pokemon.com/us/pokedex/arrokuda

Arrokuda is described hunting prey itself while slower individuals can become targets of Wattrel flocks.

Reusable structure:

- a species can occupy more than one ecological role;
- predator/prey should be represented as directed relations between actor and target contexts, not permanent species labels;
- condition, life stage, location or season may matter;
- food webs are more useful than a single linear food chain.

### Mandibuzz — opportunistic predation/scavenger-like behavior

Official source:
https://www.pokemon.com/us/pokedex/mandibuzz

Mandibuzz is described watching for weakened prey and carrying food back toward its nest.

Reusable structure:

- vulnerability state can change who interacts with whom;
- aftermath of another event can attract secondary species;
- a battle, storm or migration can therefore create ecological consequences without requiring a scripted villain.

Ouros must not infer that any mechanically Injured or low-HP Pokémon automatically becomes prey. Ecological observations and battle mechanics remain separate.

### Paras and Parasect — host/fungus relationship

Official sources:
https://www.pokemon.com/us/pokedex/paras
https://www.pokemon.com/us/pokedex/parasect

The Pokédex describes the mushrooms on Paras taking nutrition and Parasect being heavily controlled/drained by the mushroom.

Reusable structure:

- ecological relations can occur within what the game represents as one Pokémon entity;
- a parasite/host relationship does not always map cleanly to two separately spawned actors;
- biological interpretation can be established at species-lore level while exact mechanical consequences still come from the Pokémon's authoritative PTU sheet.

The narrative layer must not create extra status effects, damage, obedience rules or separate fungus combatants unless governing mechanics explicitly support them.

### Corsola — habitat quality as an ecological dependency

Official source:
https://www.pokemon.com/us/pokedex/corsola

Corsola is described as dependent on clean southern seas, and another form is associated with severe historical environmental change.

Reusable structure:

- habitat quality can mediate interspecies relations indirectly;
- loss of one habitat-forming or resource-linked species can have downstream effects;
- ecological investigation should distinguish direct predation from shared response to a third cause such as pollution or climate.

This supports a causal-network model instead of simplistic `predator increased -> prey decreased` logic.

### Cramorant — prey interaction tied to a specific Ability

Official source:
https://www.pokemon.com/us/pokedex/cramorant

Cramorant's prey interaction is connected to its Gulp Missile Ability and specific Move usage in the games.

Reusable design warning:

Some ecological-looking behavior is mechanically encoded in a Move or Ability. Narrative ecology must not recreate those effects independently.

If an encounter wants Cramorant to mechanically carry/spit prey, it depends on the exact PTU/Java implementation of the relevant behavior. A world-state observation that Cramorant hunt remains separate.

### PTU encounter design — wild behavior creates choices

Public PTU reference:
https://pokemontabletop.fandom.com/wiki/Encounter_Creation_Guide

The PTU encounter guidance includes wild groups protecting eggs or injured members, territorial encounters, external agitation, and predators pursuing vulnerable targets.

Reusable structure:

- encounter motivation should exist before initiative is rolled;
- protection, territory and pursuit can create choices other than total defeat;
- external causes can turn an ordinary ecological interaction into a larger plot hook;
- players may solve the situation by withdrawing, redirecting, investigating or changing the environment.

The supplied PTU Core Rulebook remains the project authority where this public reference overlaps it.

### PTU worldbuilding — sensible ecosystems

Public PTU reference:
https://pokemontabletop.fandom.com/wiki/Populating_Your_World

The PTU worldbuilding guidance explicitly balances game progression with sensible ecosystems and Pokémon behavior.

Reusable structure:

- encounter tables should have habitat logic;
- believable ecosystems still need to serve play rather than simulate every organism;
- regional ecology can change with story progression while retaining causal coherence.

This aligns with existing Ouros ecological-causality and observation layers.

### PTU campaign precedent — social ecology

Public campaign listing:
https://startplaying.games/adventure/clnt20u4d000208ma3ty01n49

A long-running PTU campaign publicly describes itself around the relationship between society and nature. The useful point is not its politics or plot; it is that a Pokémon tabletop campaign can sustain nature/society interactions as an ongoing campaign lens rather than isolated wilderness encounters.

No campaign characters or specific story events are imported.

### Fangame / systems reference — persistent ecosystem simulation

Source:
https://www.pokeliving.com/

Pokémon Living World publicly describes an ecosystem engine with population changes, weather and migration tied to trainer activity.

Reusable structure only:

- ecological change can continue across sessions;
- player activity can be one causal input among several;
- ecosystem state can generate future observations and opportunities.

Ouros should avoid copying its implementation or assuming that continuously simulating every predator/prey population is necessary. The stronger design is coarse state plus authored/observed causal edges.

## Research-derived interaction taxonomy

The following are useful narrative relation types. They are descriptive world-state categories, not PTU mechanics.

- PREDATION_OBSERVED
- PREDATION_PRESSURE_SUSPECTED
- SCAVENGING
- SHARED_RESOURCE_USE
- RESOURCE_COMPETITION
- HOST_PARASITE_RELATION
- HABITAT_ENGINEERING
- SHELTER_ASSOCIATION
- FOLLOWING_ASSOCIATION
- PROTECTIVE_ASSOCIATION
- MIXED_SPECIES_FORAGING
- TEMPORARY_AGGREGATION
- DISTURBANCE_RESPONSE_LINK
- UNKNOWN_ASSOCIATION

Terms such as MUTUALISM or COMMENSALISM may be used only when evidence supports the ecological claim. The generator should prefer an observed description over an overconfident scientific label.

## Core design lessons

### Relations are edges, not species identities

`Heatmor -> Durant predation` is an ecological relation.

`Heatmor = predator` is too broad.

The same species may hunt, be hunted, scavenge, compete, associate or ignore other species depending on context.

### Mechanical combat state is not ecological outcome

A KO in AutoPTU is not automatically death or consumption.

An Injury is not automatically vulnerability to predation.

Capture does not automatically remove a species from a local food web in a meaningful population-scale way.

Those consequences require explicit world-state logic.

### Absence is weak evidence

Fewer observations of one species may result from:

- actual population decline;
- migration;
- changed time of activity;
- altered survey coverage;
- avoidance of players;
- new shelter use;
- weather;
- resource movement;
- predator pressure;
- infrastructure disturbance.

The science/observation layers should preserve competing explanations.

### Interaction networks should stay sparse

Do not create a full food web for every route by default.

Persist a relation when it is:

- officially authored for the species;
- repeatedly observed;
- important to a current location;
- relevant to an ongoing ecological change;
- needed by a quest or research program;
- changed by a player-caused event.

### Encounter design should preserve agency

A predator/prey scene does not automatically require the player to save one side.

Valid outcomes may include:

- observe without intervention;
- withdraw;
- create distance;
- protect a specific actor;
- redirect a route;
- remove an artificial disturbance;
- rescue after an unrelated injury;
- document the event;
- allow ordinary ecological behavior to continue.

Conservation or moral framing should come from authored local context, not from the generator declaring one species good and another evil.

## PTU / Caelo boundary

The project's PTU/Caelo corpus remains authoritative for mechanics.

This pass intentionally does not invent:

- predation damage;
- morale;
- hunger;
- fear;
- pack bonuses;
- pursuit bonuses;
- species-specific initiative changes;
- automatic flee checks;
- death/consumption rules;
- injury-based targeting rules;
- capture restrictions;
- ecology-based stat modifiers.

Caelo encounter locations and behavior notes can inform which species occur together and how a local encounter is framed. They do not authorize new combat effects unless the governing rules text says so.

## Engine implications

World-state ecology can advance before tactical support is complete.

Mechanically rich ecological encounters may depend on:

- complete movement for pursuit, interception, knockback or forced retreat;
- terrain/weather/hazards/zones for habitat-driven battlefields;
- lifecycle for timed arrivals or withdrawals;
- status/damage only when exact legal effects are used;
- Ability/Move/Item/Feature families when species behavior depends on an actual mechanic;
- tactical AI for protect, hunt, withdraw, reach-zone or escape goals;
- Minecraft/Cobblemon playback for visible migration, pursuit, nesting and persistent individual identity.

Reduced versions should resolve the ecological event in world state before or after a conventional static battle rather than scripting missing PTU rules in Minecraft.

## Copyright and provenance rule

Official Pokémon and public community sources are used only to identify abstract ecological patterns. Ouros proposals must use original locations, institutions, conflicts and causal chains. Distinctive fan characters, prose and plots are not reused.

## Research conclusion

The strongest missing object is not a `food_chain` table. It is a versioned, evidence-backed ecological relationship edge.

That edge should answer:

- Which actors/populations are involved?
- What interaction has actually been observed?
- Where and when does it occur?
- What evidence supports the claim?
- Is the relation persistent, seasonal or situational?
- What changed recently?
- What other causes could explain the observation?
- What world-state consequences are allowed without inventing mechanics?

This gives Ouros living ecology without forcing every route into a continuous biological simulation.