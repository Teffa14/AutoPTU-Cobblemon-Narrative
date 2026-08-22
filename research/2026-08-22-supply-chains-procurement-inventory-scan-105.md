# Research Scan — Supply Chains, Procurement, Inventory & Warehousing — Pass 105

Status: external research and provenance only. Nothing in this file is established Ouros canon or a rules source.

Date: 2026-08-22

## Why this pass

The repository already has strong layers for material provenance, crafting, food/agriculture, workplaces, finance, transport, postal delivery, technical infrastructure, crisis response, rail, maritime freight and illicit diversion. The remaining gap is the connective tissue between them: how an institution decides what it needs, sources it, reserves it, stores it, routes it, substitutes it, receives it and reacts when supply no longer matches demand.

The gap matters because several prior layers already use concepts such as `supply_route_ids`, storage dependencies, backlogs, spare parts, food batches, clinic capacity and emergency reserves. Without a shared supply-chain authority, different systems could incorrectly infer that:

- material existing somewhere in the region means it is available to the actor who needs it;
- an announced purchase means goods were actually acquired;
- a shipment arriving means its contents were accepted for use;
- stock physically present in a warehouse is unreserved and usable;
- a delay means theft or sabotage;
- a visually refrigerated crate stayed within a valid storage condition;
- two batches with the same item type have the same provenance or suitability;
- a temporary shortage means the region does not produce the item;
- a warehouse count observed in Minecraft is inventory truth.

Pass 105 therefore focuses on logistics state rather than new PTU mechanics.

## Internal repository overlap reviewed

Before external research, the branch inventory and relevant existing systems were inspected.

Key overlap boundaries:

- `design/material-culture-economy-crafting-layer.md` owns physical item instances, material batches, provenance, production actions, workshops and commissions. It explicitly allows bulk supplies to remain aggregate inventory until an individual object becomes narratively significant.
- `design/food-agriculture-hospitality-layer.md` owns food batches, agricultural production, kitchens, menus and food-specific provenance. It already records storage and transport dependencies but does not own general warehousing or allocation.
- `design/workplaces-professions-staffing-layer.md` owns people, shifts, role coverage and work backlogs. It can say a procurement desk is understaffed; it should not calculate stock truth.
- `design/finance-sponsorship-risk-layer.md` owns funding authorization, payment commitments and receipt of money. A funded purchase is not automatically a delivered purchase.
- `design/travel-transport-expedition-layer.md` owns route/service availability and transport modes. It answers whether a freight leg can move, not whether the right stock was allocated to that leg.
- `design/postal-courier-parcel-logistics-layer.md` owns addressed postal items and last-mile mail routing. Pass 105 must not turn every freight movement into postal mail.
- `design/technology-energy-infrastructure-layer.md` owns machines, maintenance and service dependencies. It can request a replacement component, but Pass 105 should own sourcing and stock allocation for that component.
- `design/crisis-rescue-recovery-layer.md` owns emergency demand and recovery projects. Pass 105 can explain why emergency stock is reserved, depleted, rerouted or substituted.
- `design/illicit-networks-smuggling-diversion-layer.md` owns evidence-backed illicit diversion. A stock discrepancy must remain an inventory discrepancy until evidence supports theft or diversion.

The branch comparison before writing showed `agent/pass-53-evolution-life-stage` 208 commits ahead of `main` and 0 behind.

## Source 1 — Pokémon Sword/Shield: Poké Jobs

Source: Pokémon official Sword/Shield site, “Poké Jobs”.

URL: https://swordshield.pokemon.com/en-us/gameplay/pokejobs/

Observed structure:

- corporations and universities request help;
- requests are visible through an institutional interface;
- Pokémon are assigned to a job for a period;
- different jobs can prefer different capabilities/types in the game system;
- work has a requester, assignment and completion outcome.

Reusable Ouros pattern:

Institutions should be able to publish demand or work requirements rather than every shortage becoming an adventure hook personally authored by a quest NPC. A workshop can request parts; a clinic can request cold-storage capacity; a research program can request sample containers; a transport operator can request maintenance materials.

What is not imported:

- Poké Job EXP;
- EV/base-point rewards;
- type-based suitability formulas;
- job duration tables;
- item rewards;
- Box-based deployment behavior.

Those are game mechanics from Sword/Shield, not PTU/Caelo rules.

## Source 2 — Hoenn: Devon Parts / Devon Corporation

Sources:

- Pokémon.com, “Stairway to Devon”: https://www.pokemon.com/us/animation/seasons/6/episode-17-stairway-to-devon
- Bulbapedia, “Devon Parts”: https://bulbapedia.bulbagarden.net/wiki/Devon_Parts
- Bulbapedia, “Devon Corporation”: https://bulbapedia.bulbagarden.net/wiki/Devon_Corporation

Observed structure:

- Devon manufactures technical products;
- a specific package of mechanical parts is stolen, recovered and then physically delivered to a named recipient;
- the corporation can repair its own manufactured technology;
- transport and industrial projects can affect local Pokémon, as with the Rusturf Tunnel project being stopped when it disturbed the local Whismur population.

Reusable Ouros pattern:

A manufactured component can have a chain of identity and responsibility:

manufacturer -> batch/component -> holder -> route -> recipient -> project dependency.

The same company can also have production, repair and infrastructure roles without every employee or asset being interchangeable.

The Rusturf pattern is especially useful as a logistics/ecology guardrail: completing a supply or transport project is not automatically the correct outcome if the project damages another system. Procurement should consume environmental, civic and institutional constraints rather than override them.

What is not imported:

- Devon itself;
- its products as Ouros products;
- the stolen-goods plot;
- Hoenn characters;
- rewards for delivery;
- any assumption that corporate ownership grants public authority.

## Source 3 — PTU official campaign seed: The Road to Tomorrow / The Last Caravan

Source: official Pokémon Tabletop RPG blog, “Campaign Seeds: The Road to Tomorrow”.

URL: https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

Observed structure:

The Last Caravan explicitly links exploration and settlement rebuilding with shortages, recovered technology, supplies required to repair and maintain a city, merchant movement between settlements and trade connecting otherwise separated communities.

Reusable Ouros pattern:

Supply is most interesting when it is connected to a durable world dependency. A generator does not need to create random fetch quests. It can observe that:

- a settlement service depends on a component;
- the normal source is unavailable;
- an alternate source exists but has a cost or tradeoff;
- the choice changes future resilience or relationships.

The caravan pattern also supports moving distribution nodes. A mobile clinic, expedition vehicle, seasonal market or emergency convoy can temporarily become a regional stock point without becoming a permanent settlement.

What is not imported:

- apocalypse premise;
- specific settlements, factions or technology;
- resource mechanics;
- campaign antagonists.

## Source 4 — PTU adventure logistics: A Song of Ice and Ire

Sources:

- “A Song of Ice and Ire”: https://pokemontabletop.com/wiki/index.php/Quest%3AA_Song_of_Ice_and_Ire
- “ASOIAI Adventure Mechanics”: https://pokemontabletop.com/wiki/index.php/Quest%3AASOIAI_Adventure_Mechanics
- “ASOIAI Outline”: https://pokemontabletop.com/wiki/index.php/Quest%3AASOIAI_Outline

Observed structure:

This public PTU adventure makes supplies part of a bounded scenario:

- a scheduled shipment cannot arrive because of a storm;
- fuel consumption rises because the environment changes;
- emergency storage becomes relevant;
- medical supplies can run out;
- alternative local materials may support an improvised solution;
- wild Pokémon raids can reduce available supplies;
- side quests can extend how long a location remains operational.

Reusable Ouros pattern:

Shortage should be modeled as demand plus available stock plus replenishment timing, not as a binary story flag.

A location can have:

- normal stock;
- emergency reserve;
- inaccessible reserve;
- increased burn/usage rate;
- delayed replenishment;
- substitute source;
- loss event;
- recovery or conservation choice.

This is directly useful for clinics, remote stations, ferries, power systems, expeditions and crisis shelters.

What is not imported:

- the module’s custom Supply mechanics;
- Supply Point prices;
- attrition formulas;
- item quantities;
- the supernatural-storm plot;
- its NPCs, Pokémon encounters or side quests.

The module is a narrative-structure source only. PTU/Caelo mechanics still require project-source validation.

## Source 5 — PTU/Pokémon Odyssey planning and inventory abstraction

Sources:

- “Gameplay Structure”: https://pokemontabletop.com/wiki/index.php/Gameplay_Structure
- “Inventory”: https://pokemontabletop.com/wiki/index.php/Inventory

Observed structure:

Pokémon Odyssey deliberately abstracts routine supplies into preparation/downtime procedures instead of simulating every purchase. Travel basics are presumed available, while more consequential supplies are constrained by adventure planning and inventory.

Reusable Ouros pattern:

The supply-chain layer should compress routine procurement. A healthy settlement should not generate quests because a café ordered ordinary napkins or a clinic replenished common supplies. Detailed state becomes useful when:

- stock is strategic, restricted, scarce or perishable;
- availability changes a service;
- provenance matters;
- a shipment is disrupted;
- a substitute changes risk or quality;
- demand exceeds capacity;
- a player has deliberately entered a logistics/professional loop.

This is consistent with existing Ouros compression rules for travel, meals, care and ordinary work.

What is not imported:

Pokémon Odyssey is not the project’s governing PTU/Caelo rules source. Its Supply Points, inventory slots, Camp Supplies, Favor and item abstraction are not imported.

## Source 6 — NIST manufacturing supply-chain guidance

Source: National Institute of Standards and Technology, “Navigating Supply Chain Challenges in Food Manufacturing” (2025).

URL: https://www.nist.gov/system/files/documents/2025/01/15/MEP_WP%231%20SRM_Compliance%20Approved_Final.pdf

Observed high-level lessons:

- quality problems discovered operationally need to reach purchasing/inventory functions;
- low inventory is most useful when it triggers communication before stock reaches zero;
- a supplier issue can become a downstream production bottleneck;
- organizations track different measures of fulfillment and inventory performance.

Reusable Ouros pattern:

Information latency can create a shortage even when the material technically exists. A warehouse clerk noticing low stock, a mechanic discovering that the latest batch is incompatible, or a clinic finding a damaged container should produce a structured signal that can reach allocation/procurement.

The design should avoid importing real-world corporate KPI math. Ouros only needs coarse states and causal records.

## Source 7 — WHO cold-chain monitoring

Sources:

- WHO, “How to monitor temperatures in the vaccine supply chain”: https://iris.who.int/bitstream/handle/10665/183583/WHO_IVB_15.04_eng.pdf
- WHO, “COVID-19 vaccination: supply and logistics guidance”: https://hlh.who.int/docs/librariesprovider4/supply-chain/who-2019-ncov-vaccine_deployment-logistics-2021.1-eng.pdf

Observed high-level lessons:

- storage conditions can matter continuously across a chain;
- shipment condition should be checked at handoffs/receipt;
- monitoring devices can provide evidence of exposure;
- arrival is distinct from acceptance for use;
- lots/batches, quantities, source and timing matter when a product is sensitive.

Reusable Ouros pattern:

Some Ouros goods can have authored storage-condition requirements without turning the whole game into cold-chain simulation. The system can store a `condition_log_ref` and an acceptance state when a clinic, nursery, laboratory or food facility handles a sensitive batch.

No real vaccine temperatures or pharmaceutical rules are imported into Ouros. Specific thresholds must come from authored canon or PTU/Caelo implementation where relevant.

## Source 8 — FDA traceability and lot identity

Sources:

- FDA, “Tracking and Tracing of Food”: https://www.fda.gov/food/new-era-smarter-food-safety/tracking-and-tracing-food
- FDA, “Traceability Lot Code”: https://www.fda.gov/food/food-safety-modernization-act-fsma/traceability-lot-code
- FDA, June 10 2026 traceability readiness tabletop exercise update: https://www.fda.gov/food/hfp-constituent-updates/fda-releases-report-traceability-readiness-tabletop-exercises-and-updated-faqs

Observed high-level lessons:

- traceability depends on preserving identity through shipping and receiving events;
- transformation can create a new traceability identity while retaining a link to source lots;
- effective tracing requires coordination across separate participants rather than one perfect database;
- receiving records may legitimately differ from expected-shipment records when the actual delivered contents differ.

Reusable Ouros pattern:

Expected, shipped, received, accepted and consumed quantities/states should be separate. A warehouse can receive 20 units when the route manifest expected 24 without immediately creating theft evidence. A transformed batch can receive a new batch ID while preserving provenance to the input batches.

No FDA law, mandatory record fields, timelines or regulatory authority are imported into Ouros.

## Source 9 — fan-game reference: Pokémon Flux

Source: Eevee Expo, Pokémon Flux project page.

URL: https://eeveeexpo.com/flux/

Relevant high-level pattern:

Pokémon Flux ties a region’s economic growth and institutions to a regionally important energy resource. The reusable lesson is dependency: a resource can influence infrastructure, settlement growth, research and conflict at the same time.

Pass 105 does not import Flux energy, Alter Pokémon, its League structure, characters or story. Ouros should use its own authored materials and resources, with supply networks derived from existing world state.

## Cross-source synthesis

### A. Supply is a graph, not a quest item

The useful reusable structure is:

need -> demand/request -> source options -> allocation -> stock/batch -> storage -> transport legs -> receipt -> acceptance -> use/transformation -> replenishment/review.

Every arrow can fail or become delayed without implying wrongdoing.

### B. Physical presence, availability and suitability are separate

A warehouse can physically contain a part that is:

- reserved for another project;
- incompatible with the installed machine revision;
- awaiting inspection;
- damaged;
- held as emergency stock;
- subject to a case or recall;
- not authorized for the requesting institution;
- technically available but inaccessible because the only qualified staff member is absent.

That is much richer than `has_item=true`.

### C. Routine supply must compress

Healthy loops should advance silently. Expand them when a player-facing decision intersects:

- scarcity;
- substitution;
- provenance;
- custody;
- quality uncertainty;
- conflicting allocations;
- route disruption;
- crisis reserve use;
- institutional priority;
- player professional goals.

### D. Shortage should have a cause graph

Candidate cause families include:

- demand spike;
- production shortfall;
- transport disruption;
- warehouse capacity issue;
- inventory record mismatch;
- quality hold;
- incompatible revision/specification;
- staff/qualification shortage;
- funding or authorization delay;
- allocation choice;
- reserved/emergency stock;
- spoilage/condition failure when authored;
- illicit diversion only when evidence supports it.

### E. Resilience comes from remembered preparation

Useful long-term states include:

- alternate suppliers;
- compatible substitutions;
- spare-parts pools;
- emergency reserves;
- mutual-aid agreements;
- redundant routes;
- validated storage fallback;
- repairable legacy equipment;
- shared procurement;
- pre-positioned seasonal stock.

A choice made during calm play should be able to matter during a later disruption.

### F. Provenance survives aggregation

Routine inventory can remain aggregate. When a batch becomes relevant to a case, contamination investigation, historical object, specialized machine, breeding/care case or player-authored project, it can be promoted to persistent provenance state without retroactively inventing history.

## Guardrails for Ouros

The generator must not infer:

- stock physically present -> stock available;
- stock allocated -> stock shipped;
- stock shipped -> stock received;
- stock received -> stock accepted;
- stock accepted -> stock used;
- procurement approved -> payment made;
- payment made -> delivery occurred;
- warehouse mismatch -> theft;
- transport delay -> sabotage;
- damaged package -> damaged contents;
- visual refrigeration -> valid storage conditions;
- same item name -> same batch/specification;
- low stock -> regional scarcity;
- supplier identity -> manufacturer identity;
- substitute accepted -> mechanically equivalent item;
- Pokémon helping with logistics -> validated carrying, Mountable, movement or labor capability.

## PTU/Caelo boundary

This pass does not define:

- inventory slots;
- encumbrance;
- carrying capacity;
- item prices;
- crafting yields;
- repair times;
- Pokémon cargo capacities;
- storage-condition thresholds;
- spoilage rules;
- refrigeration bonuses;
- purchase checks;
- negotiation DCs;
- warehouse Skill checks;
- item substitution rules;
- item mechanical equivalence;
- healing-item effects;
- Trainer Feature procurement abilities.

The project’s supplied PTU Core, Pokédex and Caelo corpus remain the rules/canon basis. The complete primary Caelo corpus was not reliably exposed as a directly retrievable source in this runtime, so no new Caelo rule is asserted here.

Super PTU Online Helper was not exposed as an invocable capability in this runtime. No validation is attributed to it.

## AutoPTU boundary

Supply-chain world state belongs outside AutoPTU-Java. The battle core should receive only mechanically relevant, validated inventory/equipment/battle state.

A warehouse having ten Potions in world state does not put ten Potions into a Trainer’s battle inventory.

A convoy carrying a technical component does not make the component a combat Item.

A cold-storage alarm does not create Ice terrain, Hail/Snow Weather, damage or a Status.

A supply shortage cannot reduce HP, AP, Accuracy or damage unless a governing PTU/Caelo mechanic and implementation contract explicitly says so.

## Recommended next implementation-facing layer

Pass 105 should add a supply-chain systems layer with:

- persistent demand/request state;
- supply nodes and source offers;
- aggregate inventory pools;
- reservations/allocations;
- batch identity and specification refs;
- storage-condition evidence;
- procurement plans;
- inbound/outbound consignments;
- receiving and acceptance state;
- backorders/stockouts;
- substitutions;
- emergency reserves;
- bottleneck and resilience records;
- clear handoffs to Material Culture, Finance, Workplaces, Travel, Postal, Food, Care, Technology, Crisis and Cases.

Mechanically rich encounters should keep freight/civilians outside the grid in reduced versions until complete movement, hazards/zones, tactical AI and Minecraft playback are verified.