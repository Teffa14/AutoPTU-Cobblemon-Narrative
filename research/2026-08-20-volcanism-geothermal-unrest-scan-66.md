# Volcanism, Geothermal Systems & Unrest — Research Scan 66

Status: external research and provenance. Not canon. Not a rules source.

Date: 2026-08-20

## Why this pass exists

The existing Geology layer already recognizes `VOLCANIC_FIELD` and `GEOTHERMAL_SITE`, but it does not model volcanic unrest, vent history, geothermal circulation, ash/tephra footprints, eruption phases, monitoring networks or the long interval between eruptions as persistent world state.

This pass therefore extends Geology rather than replacing it. It also connects Meteorology, Freshwater, Crisis, Travel, Tourism, Infrastructure, Science, Conservation, Public Memory and battle encounter contracts.

## Source 1 — Pokémon: Fight for the Meteorite

Source: https://www.pokemon.com/us/animation/seasons/7/episode-14-fight-for-the-meteorite

Official Pokémon material places a scientific expedition, cable-car transport, rival organizations and an attempted artificial activation of Mt. Chimney in the same event.

Reusable structure:

- a volcano can be an infrastructure corridor and scientific site before it becomes a crisis;
- access systems such as cable cars can fail independently of the geological event;
- institutions may disagree about what should be done with material recovered near a volcano;
- a malicious plan and natural unrest must remain separate causal claims until evidence connects them.

Do not copy Team Magma, Team Aqua, Professor Cosmo or the meteorite plot.

## Source 2 — Pokémon: Volcanic Panic

Source: https://www.pokemon.com/us/animation/seasons/2/episode-4-volcanic-panic

The episode places a formal Gym battle directly above molten lava.

Reusable structure:

- settlements and institutions can normalize life around volcanic geography;
- a battle venue can have a strong volcanic identity without the narrative generator inventing lava damage;
- if the physical venue is damaged, the institution can move, adapt or rebuild rather than disappearing.

Mechanical caution:

A lava visual, volcanic arena or Fire-type theme does not create PTU terrain, environmental damage, immunity, movement permission or heat rules by itself.

## Source 3 — Pokémon: The Search for the Legend

Source: https://www.pokemon.com/us/animation/seasons/chronicles/episode-18-the-search-for-the-legend

The story combines an evacuated volcanic island, scientific interest, Legendary-related claims and an eruption threat.

Reusable structure:

- evacuation can precede certainty about the final event;
- scientific sampling, personal ambitions and conservation concerns can coexist around the same volcano;
- a Legendary association must remain separate from the actual geological mechanism unless canon explicitly connects them.

Do not import Moltres behavior, characters or plot.

## Source 4 — Lavaridge / Mt. Chimney hot-spring relationship

Discovery references:

- https://bulbapedia.bulbagarden.net/wiki/Lavaridge_Town
- https://bulbapedia.bulbagarden.net/wiki/Mt._Chimney

High-level structural observations:

- volcanic heat can support hot springs and a tourism/service economy;
- a change on the mountain can affect hot-water availability in town;
- later interpretation of a failed spring can be wrong before investigation identifies the cause;
- sudden reheating or release of hot water can create a separate hydrothermal risk.

Useful Ouros principle:

A geothermal service is a dependency graph, not decorative ambience.

`volcanic/geothermal state -> groundwater circulation -> spring output -> clinic/tourism/service state`

Each arrow requires its own evidence and implementation contract.

## Source 5 — One Island / Mt. Ember

Discovery reference:

https://bulbapedia.bulbagarden.net/wiki/One_Island

The island is described as benefiting from hot springs and volcanic climate even though the volcano has not erupted in years, while warm subterranean tunnels still attract Fire-type Pokémon.

Reusable structure:

- a volcano can shape ecology and settlement identity during long quiet periods;
- dormant or quiet does not mean geologically irrelevant;
- tourism can build around geothermal amenities long before any crisis occurs.

## Source 6 — Pokémon Conquest: Ignis

Discovery reference:

https://bulbapedia.bulbagarden.net/wiki/Ignis

Ignis uses a battlefield where volcanic features are mechanically active.

Reusable design lesson only:

- volcanic arenas can have telegraphed phase changes;
- battlefield geography can matter tactically;
- environmental state should be expressed through authoritative rules, not narration alone.

Do not import Ignis's magma-tile legality, healing hot springs, random fire strikes, turn limits or damage rules into PTU.

## Source 7 — USGS Volcano Alert Level System

Source: https://www.usgs.gov/programs/VHP/alert-level-system

USGS separates background state, elevated unrest, heightened/escalating unrest and hazardous eruption states. It also uses a different color-code product for aviation ash hazards.

Reusable design structure:

- one volcano can have multiple public status products for different audiences;
- alert state is an institutional assessment, not the physical volcano itself;
- an alert can rise or fall as evidence changes;
- uncertainty about eruption timing can remain explicit.

Ouros should create original institutions and terminology rather than copying USGS levels verbatim into canon.

## Source 8 — USGS volcano notifications

Source: https://www.usgs.gov/programs/VHP/volcano-notifications-deliver-situational-information

USGS notifications are based on monitoring networks, direct observations and satellite data. Different products communicate ground hazards, aviation ash, routine updates and explanatory information.

Reusable structure:

`monitoring network -> observations -> analysis -> status assessment -> targeted notification -> actor decision`

This integrates naturally with Ouros Science and Communications layers.

## Source 9 — USGS volcano hazards

Sources:

- https://www.usgs.gov/volcano
- https://www.usgs.gov/mission-areas/natural-hazards/science/volcano-hazards

Relevant high-level hazard families include lava, ash, volcanic gases, lahars and landslides. Eruptions may have multiple phases, and volcanic landslides can occur even without an eruption.

Design lesson:

Do not represent a volcano with one generic `danger=true` flag.

A volcanic system may have separate footprints and clocks for:

- vent activity;
- ash/tephra;
- gas;
- lava;
- hydrothermal activity;
- lahar/debris flow;
- slope instability;
- geothermal output.

Exact hazard effects remain mechanically blocked until PTU/Caelo + AutoPTU support them.

## Source 10 — 2026 USGS notification history as a live-world pattern

Source: https://volcanoes.usgs.gov/hans-public/vonas/

The 2026 notification history shows an active volcano cycling repeatedly between heightened activity and quieter periods, while other volcanic systems produce steam explosions, ash resuspension or submarine-plume observations.

Reusable structure:

- volcanic activity can be episodic rather than one campaign-ending eruption;
- previously deposited ash can become a new problem later without a new eruption;
- submarine volcanic unrest can create maritime/scientific content without a visible lava flow;
- a system can return toward baseline and later escalate again.

Do not copy real volcano names, events or dates into Ouros canon.

## Source 11 — hydrothermal monitoring research

Reference:

https://arxiv.org/abs/1811.07183

The research studies hydrothermal activity using multiple sensor types and emphasizes that steam-driven hazards may operate on short timescales and benefit from combined monitoring.

Reusable structure:

- geothermal/hydrothermal unrest can differ from magma-driven eruption;
- multiple instruments can disagree or cover different parts of the system;
- a monitoring anomaly should produce a hypothesis, not an automatic eruption event.

## PTU / Caelo boundary

The project source corpus and existing narrative rules already establish a strict rule: environmental prose does not create combat mechanics.

Relevant narrow PTU evidence available to the project includes capabilities such as Groundshaper, Naturewalk and Firestarter, plus selected environment-dependent Python AutoPTU behaviors. Those examples do not prove a complete volcano subsystem.

Do not infer or invent:

- lava damage;
- magma-tile legality;
- ambient heat damage;
- volcanic-gas status effects;
- ash Accuracy penalties;
- lahar movement or damage;
- eruption timing rolls;
- falling-rock mechanics;
- pyroclastic-flow rules;
- steam-blast damage;
- hot-spring healing;
- Fire-type immunity to volcano hazards;
- Water-type suppression by heat;
- Ground/Rock bonuses on volcanic terrain;
- automatic Sunny Day or Harsh Sun;
- Legendary causation of eruptions;
- geothermal energy output formulas.

## Research-to-design conclusions

1. A volcano needs persistent identity through quiet, unrest, eruption and recovery periods.
2. Physical activity, observations, scientific interpretation, institutional alert level and public belief must remain separate.
3. Geothermal systems can generate ordinary settlement life: bathing, heating, research, tourism, agriculture, power and habitat.
4. Unrest can be episodic and reversible. Not every anomaly escalates.
5. Different hazard footprints can overlap but should not be collapsed.
6. Ash can create downstream Meteorology, Travel, Freshwater, Agriculture, Health and Aviation/transport effects after the eruptive phase.
7. Hydrothermal events deserve separate state from magma eruption.
8. Minecraft should render a validated world-state revision, not calculate whether a volcano erupts.
9. AutoPTU should receive only the exact tactical environmental mechanics that current rules and tests support.
10. A volcano is most useful when it creates years of connected stories rather than one boss fight.