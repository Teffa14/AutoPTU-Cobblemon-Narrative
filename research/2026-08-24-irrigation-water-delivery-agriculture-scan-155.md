# Pass 155 Research — Irrigation, Water Delivery & Agricultural Water

Status: RESEARCH / PROVENANCE. Not Ouros canon.
Date: 2026-08-24

## Why this scan

The repository already has authorities for freshwater hydrology, groundwater, farms/cultivation, land access, drought, contaminated land and inland navigation. It did not have a dedicated model for the operational chain between an authorized water source and delivery to a managed field or orchard.

This scan therefore focuses on irrigation as an operational network: diversion, conveyance, delivery, application, tailwater/return flow, maintenance and changing delivery conditions. It does not define Ouros water law, crop yields or PTU environmental effects.

## Repository boundaries checked

- Freshwater remains authoritative for rivers, streams, reservoirs, flow and broad water-control state.
- Groundwater remains authoritative for aquifers, wells, pumping and drawdown.
- Food/Agriculture remains authoritative for farms, orchards, crops and cultivation cycles.
- Land Tenure remains authoritative for access/use permissions and authored rights over land.
- Inland Waterways remains authoritative for navigation reaches, locks, vessels and navigation restrictions.
- Toxicology / Food Safety remain authoritative if irrigation water later creates an exposure or food-safety investigation.

## Public-source findings

### Irrigation is a chain, not one quantity

USGS treats irrigation-water measurement as several separate quantities: withdrawals from surface or groundwater, deliveries through conveyance systems, conveyance losses, application, consumptive use and return flow. Surface return flow (tailwater) and subsurface return flow can behave differently and can reconnect agricultural fields to streams or groundwater later.

Sources:
- USGS, National Handbook chapter 11.H, irrigation measurement: https://pubs.usgs.gov/chapter11/chapter11H.html
- USGS irrigation glossary: https://pubs.usgs.gov/chapter11/chapter11M.html
- USGS Irrigation Water Use overview, current page retrieved 2026-08-24: https://www.usgs.gov/mission-areas/water-resources/science/irrigation-water-use
- Bern & Gidley 2024, agricultural return-flow dynamics: https://pubs.usgs.gov/publication/ofr20241075/full

Design lesson: Ouros should be able to say that a diversion occurred, a delivery reached a turnout, less water reached the field than expected, and some water later returned to a stream without collapsing those observations into `irrigation_success=true/false`.

### Turnouts are operational assets

The U.S. Bureau of Reclamation Water Measurement Manual describes irrigation turnouts as gate-controlled structures used to regulate and measure flow from a main canal or lateral into a smaller delivery channel. The useful abstraction is not the specific engineering standard but the operational role: a physical control point can have configuration, measurement and maintenance history independent of the source river.

Source:
- USBR Water Measurement Manual, Constant-Head Orifice Turnout: https://www.usbr.gov/tsc/techreferences/mands/wmm/chap09_11.html

Design lesson: an Ouros `IRRIGATION_TURNOUT` can remain the same persistent asset while its gate condition, calibration, operator notes, destination and delivery history change.

### Return flow can matter later and elsewhere

USGS documents both rapid surface tailwater and slower subsurface return flow. Irrigation can recharge shallow groundwater, alter later discharge to streams and, under some conditions, change water quality or stream temperature. These are delayed hydrologic handoffs, not immediate field effects.

Sources:
- USGS, Effects of Human Activities on the Interaction of Ground Water and Surface Water: https://pubs.usgs.gov/circ/1995/circ1139/htdocs/effects_of_human_activities_on_t.htm
- USGS 2024 return-flow study: https://pubs.usgs.gov/publication/ofr20241075/full
- USGS 2017 irrigation / groundwater / stream-temperature study: https://www.usgs.gov/publications/evaluating-impact-irrigation-surface-water-groundwater-interaction-and-stream

Design lesson: field application can later create a `RETURN_FLOW_OBSERVATION` handed to Freshwater or Groundwater. The irrigation layer should not itself rewrite regional hydrology.

## Pokémon and game-design findings

### The Lotad Lowdown — irrigation shortfall plus Pokémon assistance

The official Pokémon episode page establishes the flower shop, berries, lake and Lotad context. A detailed public episode guide records that irrigation tubes were running dry and Lotad were used to carry water to the plants.

Sources:
- Pokémon.com, The Lotad Lowdown: https://www.pokemon.com/us/animation/seasons/6/episode-12-the-lotad-lowdown
- Serebii episode guide: https://www.serebii.net/anime/epiguide/houen/288.shtml

Reusable structure: infrastructure underperforms -> staff notice the shortfall -> Pokémon provide a local workaround -> the workaround remains distinct from repair of the infrastructure.

Ouros guardrail: a Water-type or Lotad does not become an infinite irrigation source. Any recurring institutional role must pass through Pokémon Agency / Working Pokémon, and no Water-type Move is converted into a crop-yield formula without PTU/Caelo authority.

### Legends: Arceus — irrigation as institutional capacity growth

The Jubilife Farm request `Help Wanted: Watering the Fields` explicitly frames additional irrigation as necessary to expand cultivated fields and asks for a Pokémon that can help with watering.

Sources:
- Serebii request page: https://www.serebii.net/legendsarceus/requests/helpwanted%3Awateringthefields.shtml
- Pokémon Database request listing: https://pokemondb.net/legends-arceus/missions-requests

Reusable structure: agricultural expansion -> new operational requirement -> institutional request -> persistent increase in service capacity.

Ouros transformation: expansion should create a new delivery requirement and infrastructure/workload history. It should not become `Water-type assigned -> farm permanently upgraded`.

### Pokopia community discussion — physical water routing as a puzzle pattern

Public 2026 player discussions around Pokémon Pokopia describe routing water through terrain to water wheels, including paths that stop short or require reshaping. These discussions are useful only as a design-pattern reference: visible water geometry can make a satisfying environmental puzzle, but player-edited Minecraft blocks must not become the authoritative irrigation ledger.

Source example:
- Reddit, Pokopia water-wheel discussion, 2026: https://www.reddit.com/r/Pokopia/comments/1rq5eb4/where_do_i_get_the_water_for_the_two_waterwheels/

Reusable structure: source visible but disconnected -> inspect elevation/path -> alter physical route -> test outcome. Ouros should only use this when world-state authorization and hydrologic handoff are explicit.

## Original Ouros design conclusions

1. Separate `source availability` from `delivery authorization`, `conveyance`, `field application` and `return flow`.
2. Preserve the same ditch, lateral, turnout and field-delivery identities across years of repairs and rerouting.
3. Store requested, scheduled, measured and actually delivered water separately.
4. A dry field does not prove the source is dry; a full canal does not prove the field received water.
5. A delivery shortfall can come from source conditions, gate configuration, obstruction, seepage/leakage, maintenance, timing, damaged measurement, downstream operations or incomplete records.
6. Tailwater can be a later input to Freshwater; seepage/deep percolation can become a Groundwater observation.
7. Agriculture consumes the delivered-water outcome but remains owner of crop response.
8. Drought can change delivery scheduling without inventing universal water-rights law.
9. Wildlife use of ditches and canals should be observed independently of the agricultural purpose of the asset.
10. Pokémon assistance is actor-specific and consent/workload-sensitive, never Type-derived automation.

## PTU / Caelo mechanical guardrails

The accessible project evidence does not establish a generic irrigation, crop-water, current, drowning, mud, canal or agricultural-hazard subsystem in AutoPTU-Java. Water-type Moves and Abilities remain battle mechanics unless a verified rule explicitly bridges them to overworld work.

Do not infer:
- Water Gun / Hydro Pump -> known irrigation volume;
- Rain Dance -> agricultural delivery entitlement or reservoir refill;
- Water Absorb / Storm Drain -> water-management capability;
- Swim -> canal-worker qualification;
- Grass-type presence -> crop health;
- mud -> Rough Terrain, Slowed or Tripped;
- moving water -> forced movement;
- ditch geometry -> battle Terrain;
- Pokémon helping once -> permanent institutional assignment.

Full Caelo primary material and Super PTU Online Helper were not reliably available in this runtime. No missing rule is filled by general memory.
