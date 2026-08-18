# Care, recovery and Pokémon welfare research — pass 14

Status: research and provenance only. Nothing in this file is Ouros canon.

## Why this pass exists

The repository already models crisis response, rescue operations, material supply, settlements, travel, social bonds and persistent Pokémon state. It did not yet have a dedicated research layer for what happens after damage or distress: medical access, convalescence, field care, rehabilitation, welfare, clinic capacity, wild-Pokémon treatment, caregiver workload and the narrative consequences of recovery.

This pass studies those structures without inventing new PTU healing rules.

## Source register

### Pokémon RPGs 101 — official Pokémon.com

Source: https://www.pokemon.com/us/strategy/pokemon-rpgs-101

Pokémon.com describes Pokémon Centers as common town/city services where Pokémon can be healed for free, NPCs can be consulted and other useful services may be available depending on the game.

Reusable structure:
- a care facility can also be a social and service hub;
- free baseline treatment changes travel planning and settlement value;
- the important narrative question is often access, distance, capacity or unusual conditions rather than routine healing itself.

Do not import main-series instant-healing timing into PTU. PTU has its own recovery rules.

### Pokémon Legends: Z-A adventure guide — official Pokémon site

Source: https://legends.pokemon.com/en-au/news/adventure

The official guide explicitly frames Pokémon Centers as places to heal Pokémon exhausted from battle and acquire useful supplies.

Reusable structure:
- treatment and resupply naturally form an expedition loop;
- settlement medical access can affect how far players safely range from infrastructure;
- a Center can connect care, inventory preparation and local information without becoming a quest vending machine.

### Pokémon Horizons: “The Pokémon Center Lady” — official Pokémon.com episode page

Source: https://www.pokemon.com/us/animation/horizons/3/the-pokemon-center-lady

The episode summary presents a Center worker treating wild Pokémon outside ordinary Trainer service and investigating a cluster of poisoned wildlife. A normally friendly wild Pokémon behaving aggressively becomes part of the same environmental-health problem.

Reusable structure:
- clinics can act as ecological sentinels because unusual injuries or symptoms arrive there first;
- a cluster of similar cases can become evidence of a larger environmental event;
- wild-Pokémon welfare can generate investigation, treatment and ecological content without requiring capture;
- observed behavior change should remain evidence, not proof of motive.

### “The Joy of Water Pokémon” — official Pokémon.com episode page

Source: https://www.pokemon.com/us/animation/seasons/4/episode-49-the-joy-of-water-pokemon

The episode summary describes generations of Center staff helping transform a toxic lake into a place where Water-type Pokémon can rest and recuperate.

Reusable structure:
- medical institutions can participate in long-term habitat stewardship;
- a clinic may develop species or environment expertise based on the local ecosystem;
- recovery infrastructure can leave visible historical changes in a settlement or habitat;
- expertise can become part of institutional identity across generations.

### Pokémon Concierge — official Pokémon.com

Sources:
- https://www.pokemon.com/uk/pokemon-news/soak-up-some-sun-with-the-pokemon-concierge-quiz
- https://www.pokemon.com/uk/pokemon-news/watch-new-episodes-of-pokemon-concierge-on-netflix

The official material centers a Pokémon resort around rest, recreation and a concierge whose work is helping Pokémon guests enjoy themselves.

Reusable structure:
- care is broader than injury treatment;
- rest, enrichment, calm spaces and species-appropriate activities can matter to Pokémon characterization;
- not every welfare interaction needs a mechanical buff or ailment;
- downtime locations can create roleplay and observation opportunities instead of functioning only as menus.

### PTU 1.05 Core — governing project source, externally corroborated

Project authority: supplied PTU Core Rulebook.

Public corroborating mirror for discoverability:
https://anyflip.com/tcye/paot/basic/251-300

Relevant rules boundary from PTU 1.05:
- rest restores Hit Points under defined limits;
- Injuries are separate from ordinary HP recovery;
- sufficiently injured characters cannot simply rest back to full usefulness;
- Pokémon Centers restore health/status/frequencies on a defined timetable and take longer when Injuries are present;
- the rules limit how many Injuries can be removed per day;
- the book recommends equivalent medical institutions even in settings without conventional Pokémon Centers.

Design consequence:
Ouros must not collapse `HP restored`, `Injury treated`, `status cleared`, `rest completed` and `medically ready` into one narrative flag.

### PTU Medicine Education — public rules reference, project Core remains authority

Sources:
- https://pturpg.wikidot.com/skills
- https://pokemontabletop.fandom.com/wiki/Trainer_Skills

Medicine Education covers first aid, biology, diagnosis and unusual ailments beyond ordinary battle wounds. These public references are useful for discovery, but final implementation must use the supplied Core/Caelo materials.

Reusable structure:
- medical expertise can create investigation and field-support roles;
- diagnosing a condition should be separate from curing it;
- remote expeditions can create meaningful care problems without fabricating new damage systems;
- unusual biological or environmental conditions can become research cases.

### PTU restorative items and bandages — public rules reference

Source: https://pturpg.wikidot.com/consumables

The public reference distinguishes battle restoratives from longer-duration bandage care and notes that repeated/continuous treatment has constraints.

Reusable structure:
- field care can stabilize an expedition without making permanent infrastructure irrelevant;
- supply preparation matters more when players are far from a Center;
- treatment consumes time and supplies and can therefore interact with expedition planning.

Exact costs, healing values and action economy remain rules data, not narrative-generation values.

### Acclivity: Hoenn’s Advance — public tabletop campaign rules

Source: https://ahacampaign.wikidot.com/healing

This Pokémon tabletop campaign published its own healing assumptions and Center behavior.

Design lesson:
Campaigns frequently alter medical pacing. Therefore Ouros must never infer its healing economy from another campaign log. External campaign rules are inspiration for questions to ask, not authority.

### Pokécharms Pokémon RP — public roleplay examples

Sources:
- https://forums.pokecharms.com/threads/pokemon-role-play-thread.28798/page-66
- https://forums.pokecharms.com/threads/pokemon-role-play-thread.28798/page-67

Public RP scenes use Centers as places where Trainers and Pokémon may require different forms of treatment, where a patient may be distressed or resistant, and where an unfamiliar condition can exceed routine healing.

Reusable high-level patterns only:
- treatment scenes can create social decisions and follow-up investigation;
- the patient’s behavior and consent can matter narratively;
- an unusual ailment can force referral, research or specialist involvement;
- care spaces can connect PCs who otherwise arrived for unrelated reasons.

No prose, characters, diagnoses or events from these threads should be transplanted into Ouros.

## Cross-check against current AutoPTU implementation evidence

A recent Python AutoPTU snapshot available to the project contains explicit `injuries` state and a `QuickHealingAction` that removes a bounded number of Injuries from an eligible allied Pokémon and emits an `injury_recovery` battle event.

This is implementation evidence that Injury state is not merely prose in the current Python engine. It does not prove that all downtime healing, Pokémon Center recovery, Medicine checks or long-term convalescence are implemented outside combat.

## Patterns worth adopting

### Care encounter != combat encounter

A medical scene can revolve around:
- diagnosis;
- stabilization;
- transport;
- locating a specialist;
- finding safe rest;
- identifying exposure source;
- managing capacity;
- observing recovery;
- deciding when to resume activity;
- supporting a wild Pokémon without capturing it.

### Health state needs provenance

Narrative systems should know why an entity is in care.

Possible evidence sources:
- AutoPTU battle result;
- environmental hazard event;
- scripted world event;
- observed symptom;
- NPC report;
- player report;
- imported canonical event.

A rumor that a Pokémon is poisoned must not silently set the canonical Poisoned status.

### Treatment state and story state are different

The rules engine may say an Injury is removed. The narrative layer may still remember:
- who provided care;
- where treatment happened;
- what caused the incident;
- whether a specialist was involved;
- whether a facility became overloaded;
- whether an ecological pattern was discovered;
- whether the patient is still resting by authored choice.

Conversely, narrative text saying “the Pokémon looks better” must never mechanically remove an Injury.

### Clinics can be knowledge nodes

Aggregated, privacy-safe case patterns can reveal:
- repeated toxin exposure;
- route-specific injuries;
- seasonal disease clusters;
- harmful construction effects;
- new wild-population pressure;
- shortages of a treatment supply;
- a species appearing outside its expected habitat.

Individual medical details should not automatically become public rumors.

### Recovery can create downtime without dead time

While a primary Pokémon is resting, the player may:
- socialize;
- research the cause;
- help the clinic with non-medical errands;
- use another team member;
- prepare equipment;
- review field notes;
- pursue a low-risk local activity;
- visit the patient;
- contact a mentor or specialist.

The system should not force players into repetitive waiting gameplay merely because recovery takes time.

### Welfare state should be descriptive before numeric

Useful observations include:
- avoiding contact;
- seeking shade;
- refusing food;
- resting more than usual;
- engaging willingly with enrichment;
- repeatedly returning to a safe location;
- showing agitation around a specific stimulus.

Do not convert these directly into invented happiness, trauma or loyalty scores.

## Copyright and attribution boundary

External Pokémon episodes, fangame material, campaign logs and RP threads are research references only. Ouros may reuse structural lessons such as “clinic detects an ecological pattern” or “recovery creates a specialist referral,” but must not reproduce source scenes, dialogue, characters or distinctive plots.

## Questions for later mechanical review

- Which PTU/Caelo healing rules are already implemented by AutoPTU outside combat?
- Does current server state persist Injuries after a battle ends?
- What exact Caelo modifications apply to healing, Centers, restorative items and Injury limits?
- How should Trainer medical treatment differ from Pokémon medical treatment in Ouros?
- Can Minecraft represent a Pokémon as admitted/resting without losing its persistent identity?
- How should a clinic learn population-level trends without exposing private player information?
- Which conditions need specialist referral rather than standard Center handling?
- How should remote field care interact with fast travel and expedition abort decisions?
- What happens when a settlement loses access to its usual care facility?
