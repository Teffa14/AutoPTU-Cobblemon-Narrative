# Pass 111 Research — Manufacturing, Production Runs & Quality State

Status: research/provenance only. Not Ouros canon. Not a PTU rules source.

## Why this pass exists

The repository already has strong ownership boundaries for individual crafted objects, material provenance, workshops, machines, workers, procurement, inventory, storage, freight, waste and retail. What is still missing is the state between `inputs available` and `finished stock accepted for use` when production is repeatable, multi-step or industrial.

Relevant existing owners inspected before writing:

- `design/material-culture-economy-crafting-layer.md` owns physical item identity, material provenance, individual production/crafting actions, workshops, services and commissions.
- `design/technology-energy-infrastructure-layer.md` owns machines, factory-line assets, technical faults, maintenance and industrial-process infrastructure after those assets exist.
- `design/workplaces-professions-staffing-layer.md` owns roles, shifts, qualifications, assignments and work backlogs.
- `design/supply-chains-procurement-inventory-layer.md` owns demand, sourcing, stock, storage, freight, receiving and availability. It already references `manufacturing_or_harvest_ref` without owning that upstream process.
- `design/waste-sanitation-recycling-pollution-layer.md` owns waste streams and environmental consequences.
- `design/retail-markets-auctions-merchant-networks-layer.md` owns the player-facing offer/transaction layer after stock exists.

Pass 111 therefore investigates repeatable production processes, work-in-progress, lot genealogy, in-process observations, deviations, quality disposition, rework and recall history.

## Research findings

### 1. Pokémon itself distinguishes handcrafting from factory production

The official Pokémon article about Hisui explicitly contrasts modern Poké Balls manufactured in factories with early Poké Balls crafted by hand from materials such as Apricorns and Tumblestones. This is useful because the same broad product family can have very different production institutions without requiring different battle mechanics.

Reusable Ouros lesson:

- artisanal crafting and industrial production can coexist;
- scaling a workshop into a factory is a world/institution change, not a rules rewrite;
- a factory-made instance of a canonical item does not gain different PTU effects merely because its provenance differs;
- production scale can affect staffing, supply chains, utilities, waste, transport and public memory while mechanical item behavior remains governed elsewhere.

Source:
https://www.pokemon.com/uk/news/a-look-at-the-early-days-of-pokemon-research-in-pokemon-legends-arceus

### 2. The Poké Ball Factory supports production as an explorable institution

Official Pokémon material identifies the Poké Ball Factory outside Laverre City as a recognizable regional facility, and an official animation episode uses the factory as a visited workplace with managers, storage and an operational tour. Secondary reference material describes the facility as highly automated with limited human oversight.

Reusable Ouros lesson:

- factories can be places with public identity, tours, staff, storage, security and operational zones;
- automation can reduce routine labor without eliminating monitoring, responsibility or failure modes;
- a factory can support a story without every conveyor becoming a combat hazard.

Sources:
https://www.pokemon.com/us/news/adventure-from-kanto-to-paldea-with-the-pokemon-center-s-region-map-posters
https://www.pokemon.com/us/animation/seasons/18/episode-30-a-frenzied-factory-fiasco
Secondary factual reference only:
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9_Ball_Factory

### 3. Fuego Ironworks shows a multi-stage material chain

Fuego Ironworks is described as refining iron ore from Mt. Coronet and manufacturing mechanical parts. This gives a clean high-level chain: extraction → refining → component production → later use elsewhere.

Reusable Ouros lesson:

- a facility does not need to produce finished consumer goods to matter;
- intermediate products can have their own batches, storage, transport and quality history;
- one defect or supply failure can propagate downstream through several institutions without requiring sabotage.

Source used as secondary location reference:
https://bulbapedia.bulbagarden.net/wiki/Fuego_Ironworks

### 4. A factory can be a regional development pressure, not only a dungeon

A public PTU campaign pitch, `Pokemon Tabletop United meets Harvest Moon`, frames a declining region where rumors of League expansion, new markets and a possible factory are potential forces of redevelopment. The campaign emphasizes player-driven town development rather than a standard badge-only structure.

Reusable Ouros lesson:

- opening a production site can change migration, housing, rail/road demand, staffing, pollution, trade and local politics over years;
- benefits and costs can distribute unevenly;
- the factory itself need not be villainous;
- players can influence how industrial growth integrates with existing settlements.

Source:
https://rpol.net/display.cgi?date=1454079513&gi=4&ti=34579

### 5. Factories work well as operational exploration spaces

The public fangame `Pokémon Ancient Bronze` includes a factory as an explorable setting. Only the broad structural idea is useful here: a production facility can have process areas, restricted sections, maintenance routes and clues tied to how the place works.

Reusable Ouros lesson:

- factory exploration should derive navigation and investigation from real process dependencies;
- do not create arbitrary switch puzzles if the process itself can explain why a gate, line, tank, lift or inspection station exists;
- the operational state should remain understandable after the encounter ends.

Source:
https://eeveeexpo.com/threads/6192/

No plot, characters, dialogue, locations or distinctive puzzle sequence are imported.

### 6. Manufacturing traceability is useful as a design pattern

NIST guidance on trustworthy manufacturing data emphasizes traceability across manufacturing-related data and the ability to establish which information/version came from which source. NIST's broader digital-thread work similarly treats product data as something that propagates across lifecycle functions.

Reusable Ouros lesson:

- every important production run should be able to point to process version, relevant input batches, equipment/line references and output lots;
- correcting a record should not silently erase the previous record;
- a downstream investigation can follow the genealogy of an object without granting omniscience;
- stale or incorrect process data can be a real cause of failure without implying malicious tampering.

Sources:
https://www.nist.gov/publications/recommendations-ensuring-traceability-and-trustworthiness-manufacturing-related-data
https://www.nist.gov/programs-projects/digital-thread-manufacturing

These sources are used only for abstract information-architecture patterns. Ouros does not import industrial standards or legal requirements.

### 7. Production completion and release should remain separate states

FDA manufacturing guidance provides a useful abstract pattern: production records, in-process controls, deviations and review can exist before a batch is released for distribution. This is especially useful for Ouros because Supply Chains already distinguishes physical stock from accepted/available stock.

Reusable Ouros lesson:

- `produced` does not equal `released`;
- a deviation can be documented without proving that the output is defective;
- a failed check can trigger investigation, rework or rejection without proving sabotage;
- rework should keep genealogy rather than create a magically new object;
- recall is an operational response state, not an automatic finding of criminal wrongdoing.

Sources:
https://www.fda.gov/files/drugs/published/Q7-Good-Manufacturing-Practice-Guidance-for-Active-Pharmaceutical-Ingredients-Guidance-for-Industry.pdf
https://www.fda.gov/media/191983/download

These documents are not used as laws, regulations or canonical institutions for Ouros. Only the abstract separation of records, in-process checks, deviations and release is reused.

## Cross-source synthesis for Ouros

A useful persistent production chain is:

`PROCESS VERSION → INPUT LOTS → PRODUCTION RUN → STEP EXECUTIONS → WORK IN PROGRESS → IN-PROCESS OBSERVATIONS → OUTPUT LOT → QUALITY DISPOSITION → RELEASE/REWORK/SCRAP → SUPPLY CHAIN`

The strongest narrative opportunities come from disagreements between those states rather than from generic factory danger.

Examples:

- the correct input material was used, but an obsolete process revision was loaded;
- a process deviated from plan, yet the output later proves usable;
- a batch was produced correctly but is held because records are incomplete;
- two downstream institutions received components from the same parent lot;
- a recall begins because of a credible risk signal before the root cause is known;
- rework repairs one property but creates a new provenance branch that future maintainers need to understand;
- an automated line remains mechanically functional while its measurement system drifts;
- the first production run after a major maintenance outage becomes an important observation window.

## PTU/Caelo mechanics boundary

No primary PTU/Caelo rule file for industrial manufacturing, Technology Education, crafting yields, process timing, machine use or quality checks was recovered reliably in this run.

Therefore this pass does not define:

- Technology Education DCs;
- crafting or manufacturing times;
- recipe prerequisites;
- material yields;
- machine bonuses;
- item quality tiers;
- defect probabilities;
- durability changes;
- capture modifiers for factory-made Poké Balls;
- Pokémon labor bonuses;
- conveyor movement;
- industrial damage or status effects.

Material Culture remains responsible for any executable item/crafting action that needs PTU/Caelo validation. Pass 111 only adds persistent world-state orchestration around repeated production.

## Copyright / transformation note

Official Pokémon, PTU campaign material and fangames are used only for high-level structural observations. No protected dialogue, prose, character, location design, plot sequence or distinctive puzzle is copied into Ouros proposals. Real-world manufacturing sources contribute abstract systems ideas only.

## Research conclusion

The useful missing layer is not `factory = dungeon`. It is `factory = persistent transformation system`.

That system should remember which process revision ran, what inputs entered, what intermediate state existed, what was observed during production, which output lot resulted and whether that lot was released, reworked, held, scrapped or later recalled. This gives Ouros long-term industrial history while keeping item mechanics, staffing, machines, procurement, transport, finance, waste and battle authority in their existing owners.