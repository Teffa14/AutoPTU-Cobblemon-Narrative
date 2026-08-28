# Research Scan — Manufacturing, Factories & Production Continuity — Pass 103

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. Not PTU rules.
Date: 2026-08-28
Baseline narrative head inspected before writing: `2726706fae57fe89637bfe70ac73a0547d98b76a`.

## Why this scan exists

The recursive repository inventory was inspected before writing and returned `truncated=false`. Existing layers already cover material provenance and validated crafting actions, workshops and commissions, procurement and supplier fulfillment, batch traceability/recall/quarantine, workplaces/staffing, logistics, infrastructure outages, worksite safety, science, pollution and storefront availability.

A remaining gap is organized production continuity: facilities that transform inputs into repeated outputs across lines, cells or production runs, with staged readiness, work-in-process, stoppages, quality holds, rework, release, capacity constraints and persistent operational history.

This scan therefore does not create a second crafting system. It researches how a narrative layer can preserve industrial operations while delegating actual recipes, PTU prerequisites, item mechanics, custody, finance, safety, pollution and distribution to their existing owners.

## Source 1 — Poké Ball Factory, Kalos

Public reference: Bulbapedia, “Poké Ball Factory”.
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9_Ball_Factory

Observed high-level structure:
- one specialized facility produces a regionally important family of goods;
- production is heavily automated but still requires human oversight;
- the same facility supports tours/public observation;
- conveyor systems and control interfaces visibly represent process flow;
- finished output leaves the plant through a distribution network rather than appearing directly in shops by magic.

Reusable Ouros lessons:
- separate `facility operational` from `line operational`;
- automation can reduce staffing requirements without eliminating operators, maintenance or verification;
- public-facing tours can coexist with restricted production areas;
- an upstream factory interruption can later appear as downstream availability pressure in Commercial Services without either layer inventing a price shock;
- conveyor direction, doors or machinery shown in Minecraft are presentation unless Ouros records an authoritative production-state transition.

Rejected imports:
- no assumption that Ouros has a single regional Poké Ball monopoly;
- no copied villain takeover plot;
- no copied floor plan or conveyor puzzle;
- no assumption that Poké Balls are manufactured by the same method in Ouros;
- no production quantity, timing or capacity numbers inferred from the game.

## Source 2 — Fuego Ironworks, Sinnoh

Public reference: Bulbapedia, “Fuego Ironworks”.
https://bulbapedia.bulbagarden.net/wiki/Fuego_Ironworks

Observed high-level structure:
- the facility receives an upstream raw material from another location;
- it refines that material and then manufactures mechanical parts;
- industrial production therefore contains at least two conceptually separate transformations;
- the plant is geographically embedded beside forest, river and neighboring settlements rather than existing in an abstract industrial menu.

Reusable Ouros lessons:
- a production chain should preserve input batch provenance through intermediate material and final output references;
- `refining complete` does not imply `component manufacturing complete`;
- a facility can create dependencies for Mining/Geology, Transport, Forestry/Conservation, Water, Pollution and Workplaces without taking authority over those systems;
- output shortages can have several causes: missing input, stopped process, failed verification, unavailable staff or blocked outbound logistics.

Rejected imports:
- no copied spin-tile dungeon logic;
- no universal molten-metal hazard mechanics;
- no assumption that proximity to fire or furnaces applies PTU Burn or damage;
- no inferred metallurgy checks or yields.

## Source 3 — Devon Corporation, Hoenn

Public reference: Bulbapedia, “Devon Corporation”.
https://bulbapedia.bulbagarden.net/wiki/Devon_Corporation

Observed high-level structure:
- an organization can evolve historically from extraction/smelting activity into a diversified technology producer;
- research, product development and released products are separate stages;
- several product families can coexist under one institution;
- not every experimental device becomes a released product.

Reusable Ouros lessons:
- preserve `prototype`, `pilot`, `approved product`, `production-ready` and `released` as different claims/states when canon later needs them;
- Science can own research evidence while Manufacturing owns operational production readiness;
- an old industrial identity can remain part of institutional history after the organization changes business model;
- production architecture should support a small workshop, a specialized plant and a diversified company without forcing all of them into one scale.

Rejected imports:
- no copied Devon inventions or corporate history;
- no assumption that Ouros corporations can revive fossils;
- no automatic conversion of research success into manufacturability.

## Source 4 — Silph Co., Kanto

Public reference: Bulbapedia, “Silph Co.”.
https://bulbapedia.bulbagarden.net/wiki/Silph_Co.

Observed high-level structure:
- a major technology company can manufacture multiple product families;
- its headquarters mixes research/administration with product identity;
- public knowledge about who develops or manufactures a product can be incomplete or overgeneralized.

Reusable Ouros lessons:
- separate manufacturer claims, developer claims, patent/invention claims and actual batch provenance;
- a brand name on an object or document is evidence, not automatic proof of the exact production site;
- institutional prominence can make facilities targets for espionage, sabotage or coercion, but those outcomes must be proposed separately rather than assumed.

Source-quality caution:
A public community discussion has specifically challenged overbroad claims that Silph manufactures every TM merely because Silph material references TMs. This is a useful provenance lesson in itself: repeated fan assumptions must not be promoted to canon without primary support.

Rejected imports:
- no copied corporate takeover arc;
- no assumption about TM manufacturing;
- no universal large-corporation structure for Ouros.

## Source 5 — Pokémon Reborn, Blacksteam Factory / Peridot industrial continuity

Public references:
https://pokemon-reborn.fandom.com/wiki/Blacksteam_Factory
https://pokemon-reborn.fandom.com/wiki/Peridot_Ward

Observed high-level structure:
- an industrial facility can have environmental externalities that alter neighboring world state;
- a factory can later be repurposed into a different civic function, preserving place identity while changing use;
- an industrial location can support puzzles or encounters built from machinery and process concepts.

Reusable Ouros lessons:
- keep pollution evidence in Waste/Sanitation/Conservation/Science; Manufacturing only records the operating event or output that may be linked to that evidence;
- a closed facility can be mothballed, stripped, reused, converted or preserved instead of disappearing from the map;
- industrial architecture can produce exploration content through access, maintenance state and process history without requiring a combat encounter.

Rejected imports:
- no copied Team Meteor plot;
- no copied captive-Pokémon puzzle sequence;
- no copied facility conversion;
- no assumption that pollution implies deliberate wrongdoing.

## PTU 1.05 boundary

Public governing references inspected:
- official PTU 1.05 release page: https://pokemontabletop.com/pokemon-tabletop-united-1-05-release/
- PTU 1.05 Core mirrored text / rule references used to cross-check Health/Death and general action concepts.

The existing Ouros Material Culture layer already correctly requires every executable `production_action` to reference a governing recipe/rule and validate actor prerequisites, tools/facilities, inputs, action/frequency/time requirements and implementation support.

No inspected PTU 1.05 evidence establishes a universal industrial-production subsystem with:
- assembly-line throughput;
- generic machine speed;
- conveyor movement rules;
- factory capacity math;
- defect probability;
- machine HP;
- jam/overheat tables;
- generic worker productivity bonuses;
- industrial accident damage;
- automated crafting from Minecraft blocks;
- species-based manufacturing eligibility.

Therefore Pass 103 treats production continuity as world state. Actual PTU crafting or item creation remains mechanically governed by the existing rule references when a concrete recipe/action is executed.

## Caelo boundary

The project’s extracted Caelo material has previously been used for setting assumptions, locations, encounter content and character/rules cross-checks. No inspected governing evidence in the project establishes a universal factory, assembly-line, machine-capacity, industrial-safety or manufacturing-yield system.

Any Caelo-specific company, plant, craft tradition, production method or technology remains UNKNOWN until a governing source is located and reviewed. This scan creates no Caelo canon.

## Design lessons extracted

1. Production is a chain of evidence, not one boolean.
An order can exist before materials arrive. Materials can arrive before a line is ready. A run can start before it completes. Physical completion can precede quality release. Released goods can wait for distribution.

2. Work-in-process should persist.
If a line stops, partially transformed inputs should remain identifiable when narratively relevant. A restart should not recreate them from nothing.

3. Quality decisions need provenance.
A hold, rejection, rework instruction or release is a recorded decision tied to evidence and scope. A visual defect is not automatically a failed item.

4. Capacity is contextual.
Narrative state can record AVAILABLE, CONSTRAINED or UNAVAILABLE capacity and the reason. It should avoid speculative units-per-hour arithmetic unless canon or implementation data explicitly defines it.

5. Automation does not equal autonomy.
Minecraft machinery, redstone, conveyor animations or block movement can present operations. They do not authorize recipe execution, item creation, batch release or worker decisions.

6. Industrial sites accumulate history.
A line can be upgraded, idled, repurposed or removed. A building can remain after its original production role ends. Former supply relationships can continue to matter socially and economically.

7. Production problems do not imply sabotage.
Missing inputs, calibration, staffing, quality review, maintenance, utility outages, transport disruptions, ecological restrictions and normal variation are all valid causes.

## Candidate narrative structures

- a run completes physically but remains on quality hold;
- two workshops use the same input batch but have different output timing;
- a temporary production cell introduced during an outage becomes a permanent local specialty;
- a factory tour exposes a discrepancy between public process diagrams and current line configuration without implying conspiracy;
- a replacement component arrives but installation and verification remain separate;
- an old facility is repurposed while records from its former production era still affect present claims;
- a downstream shop reports scarcity although the upstream factory has resumed, because released goods have not yet cleared distribution;
- a production stoppage protects workers but creates secondary pressure on hospitals, farms, transit or expeditions;
- an individual Pokémon performs a production role only after explicit assignment and governing capability evidence, never from species/type alone.

## Canon status

Everything in this file is research or transformed design evidence.

No Ouros factory, corporation, product monopoly, production technology, industrial profession, Pokémon work role, output quantity, safety standard, labor rule or environmental impact becomes canon through Pass 103.
