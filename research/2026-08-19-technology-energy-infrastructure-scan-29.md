# Technology, Energy & Infrastructure Research — Pass 29

Status: research/provenance only. Nothing in this file is established Ouros canon.

## Why this pass exists

The repository already has mature layers for public works, material culture/crafting, crisis response, communications, travel, science, conservation and settlements. What it did not yet model explicitly is the operational life of technology after construction: power generation, machine dependencies, maintenance, failures, repair history, technical operators, Pokémon-machine interaction and the difference between a civic project and the system that later has to keep running.

This pass studies that gap without inventing PTU mechanics or copying external plots.

## Sources inspected

### Pokémon Tabletop / PTU

1. Pokémon Tabletop RPG — Campaign Seeds: Mysterious Ruins, section "The Apparatus"
   - https://pokemontabletop.com/campaign-seeds-mysterious-ruins/
   - Reusable structure: a very large technological environment can function as settlement, dungeon, infrastructure network and mystery at once. Self-contained Pods, automated production and Administrator Porygons show how technology can become part of daily life rather than only a boss-room gimmick.
   - Do not copy the Apparatus, its Pods or Administrator Porygons into Ouros.

2. Pokémon Tabletop RPG — Gym Design: Unconventional Challenges
   - https://pokemontabletop.com/gym-design-unconventional-challenges/
   - Reusable structure: a technological institution can have laboratories, experimental equipment, a coherent engineering identity and a challenge space embedded inside a larger working facility.
   - Do not copy Sunny, her Gym or its specific technologies.

3. Pokémon Tabletop RPG — Tales of Visiwa retrospective
   - https://pokemontabletop.com/tales-of-visiwa-a-retrospective/
   - Reusable structure: technical expertise can matter across a long campaign through engineered Pokémon, Porygon use, scientific projects and opponents who themselves understand technology. Technology can support character identity instead of existing only as scenery.
   - Do not reproduce Genevieve, Turing, campaign inventions or distinctive incidents.

4. Pokémon Tabletop RPG — PTU resources / 1.05 status
   - https://pokemontabletop.com/downloads-and-resources/
   - Mechanical use: confirms PTU 1.05 remains the governing public rules family. Exact Technology Education, crafting, repair, Feature and Pokémon capability effects must still be checked against the supplied project rule corpus before implementation.

### Official Pokémon sources

5. Rotom Pokédex
   - https://www.pokemon.com/us/pokedex/rotom
   - Reusable structure: Pokémon can interact with machines in ways that are specific to the device. Machine state can also affect the Pokémon-machine relationship. This supports persistent machine/Pokémon associations, but it does not authorize a universal "Rotom can control any machine" rule.

6. To Catch a Rotom!
   - https://www.pokemon.com/uk/animation/seasons/16/episode-31-to-catch-a-rotom
   - Reusable structure: local infrastructure and wild Pokémon behavior can create recurring outages; communities can respond by redesigning the environment rather than simply removing the Pokémon. This is a strong coexistence pattern for Ouros.

7. Remember the Region: Sinnoh Spotlight
   - https://www.pokemon.com/us/features/remember-the-region-sinnoh-spotlight
   - Reusable structure: Valley Windworks ties a renewable power facility to local ecology, place identity and recurring Pokémon presence. Infrastructure can become an ecological landmark.

8. Current Events
   - https://www.pokemon.com/us/animation/seasons/4/episode-42-current-events
   - Reusable structure: a working energy facility can become an exploration problem through doors, security systems and the power source itself. Technical systems can create traversal and rescue situations without needing an evil mastermind.

9. The Future Is Now, Thanks to Determination!
   - https://www.pokemon.com/us/animation/seasons/18/episode-14-the-future-is-now-thanks-to-determination
   - Reusable structure: control of critical infrastructure can create city-scale consequences. A power plant incident matters because it affects a dependent settlement, not merely because the building is dangerous.

10. Gone with the Windworks!
    - https://www.pokemon.com/us/animation/seasons/12/episode-39-gone-with-the-windworks
    - Reusable structure: one circuit failure can change doors, containment and local access. Infrastructure should therefore be modeled through dependencies and failure modes rather than a single binary "powered" flag.

11. Stairway to Devon
    - https://www.pokemon.com/us/animation/seasons/6/episode-17-stairway-to-devon
    - Reusable structure: a technology company can combine manufacturing, repair, research and security in one institution. A broken personal device can naturally lead players into a larger institutional story.

12. A Frenzied Factory Fiasco!
    - https://www.pokemon.com/us/animation/seasons/18/episode-30-a-frenzied-factory-fiasco
    - Reusable structure: factories are operational systems with staff, production flow, controlled access and inventory custody. A factory quest can therefore be about continuity of operations, missing output, safety or access rather than only conveyor-belt puzzles.

13. Pokémon Sword/Shield — Rotom Phone
    - https://swordshield.pokemon.com/en-us/gameplay/about-pokedex-rotom-phone/
    - Reusable structure: a device can be a platform whose functions expand through attachments and integrations. Ouros can treat devices as service interfaces tied to actual infrastructure rather than magical universal menus.

14. Pokémon Legends: Z-A official gameplay
    - https://legends.pokemon.com/en-au/gameplay
    - Reusable structure: technology can deliberately create habitats inside a developed city. Technical infrastructure can mediate coexistence instead of opposing nature.

### Fan games / community projects

15. Pokémon Flux
    - https://eeveeexpo.com/flux/
    - Reusable structure: a valuable regional energy resource can drive prosperity, League institutions and ecological problems simultaneously. The useful lesson is the dependency graph between resource extraction, economy, infrastructure and Pokémon behavior.
    - Do not import Flux energy, Alter Pokémon, Altera, its League structure or story.

16. Pokémon Ancient Bronze
    - https://eeveeexpo.com/threads/6192/
    - Reusable structure: one factory can support exploration, machinery, hidden history and a personal narrative. The factory becomes a location with operational logic rather than a generic industrial backdrop.

17. Pokémon: Technology
    - https://eeveeexpo.com/threads/3551/
    - Reusable design caution: machine puzzles involving portals, switches, lasers and movable objects become prone to softlocks when state transitions are not recoverable. Ouros machinery puzzles need explicit reset/recovery states and should never require players to corrupt persistent world state to retry.

## Supplied PTU/Caelo grounding

The supplied Caelo Region material already provides a strong local precedent for technology having environmental consequences. Technopolis and the Toxic Ravine are connected to an industrialized part of the region, and the Toxic Ravine has an explicit environmental hazard rather than using industrial pollution as flavor text only.

The design implication is important: narrative documents may define that a facility pollutes, overheats, leaks, loses power or changes habitat only as world state. Exact Poison, damage, terrain, status or movement effects remain governed by the supplied Caelo/PTU rules and AutoPTU implementation.

The PTU corpus also includes Technology Education as a real Skill domain. Narrative technical competence should therefore point to authoritative character state where mechanical resolution is required. Do not create a parallel Engineering skill.

## Reusable design lessons

### Infrastructure should be a dependency graph

A power plant is interesting because clinics, workshops, transit, communications, lighting, refrigeration, pumps or habitat systems may depend on it.

A failure should therefore record:
- what component failed;
- which service lost capacity;
- which downstream systems were affected;
- who noticed first;
- whether the failure was total, intermittent or degraded;
- what temporary workaround exists;
- what permanent repair would require.

### Failure is different from sabotage

A blackout can come from overload, maintenance debt, weather, Pokémon behavior, operator error, aging equipment, damaged routes, a deliberate attack or an unknown cause.

The case/investigation layer should determine causation rather than the technology layer defaulting to villainy.

### Maintenance creates story without requiring collapse

Useful technical content can occur before disaster:
- scheduled inspection;
- calibration;
- replacement of an aging component;
- testing backup capacity;
- training an apprentice;
- validating a new route;
- auditing spare parts;
- wildlife mitigation around a facility.

This lets players prevent crises and later see that preparation matter.

### Pokémon-machine relationships should be individual and device-specific

Rotom provides a strong precedent for Pokémon inhabiting devices, but Ouros should not generalize this into an unrestricted possession mechanic.

A persistent relationship may track:
- individual Pokémon ID;
- device ID;
- first interaction;
- observed compatible functions;
- behavior around the machine;
- maintenance effects;
- operator practices;
- unresolved mechanical rules.

### Operators matter

Infrastructure should not function because "the city owns a generator." It functions because people/Pokémon inspect, repair, schedule, clean, monitor and replace parts.

Named operators, apprentices, contractors and institutional teams can become recurring NPCs without requiring every maintenance action to be simulated.

### Degraded operation is more interesting than binary state

Candidate service states:
- NORMAL
- DEGRADED
- INTERMITTENT
- EMERGENCY_ONLY
- OFFLINE_PLANNED
- OFFLINE_FAILURE
- BYPASSED
- ISOLATED
- UNDER_REPAIR
- TESTING

This creates choices about which services stay online when capacity is limited.

### Technical puzzles need recovery contracts

Every machine puzzle should have a defined recovery method:
- reset switch;
- safe rollback;
- alternate manual control;
- technician intervention;
- preserved last-known-good state;
- explicit failure state that remains solvable.

Avoid one-way puzzle actions that can permanently softlock a persistent Minecraft location.

## Research-derived Ouros opportunities

- power networks that influence settlement service capacity;
- maintenance teams as recurring NPC groups;
- technical apprenticeships tied to real institutions;
- habitat systems whose operation changes local Pokémon presence;
- old factories whose operational records matter to modern investigations;
- competing repair priorities after storms or sabotage;
- backup systems that were installed because of an older player action;
- Pokémon whose presence creates load, interference or stabilization without assuming malicious intent;
- infrastructure that can be modernized while preserving historical or ecological constraints;
- rotating shutdowns and temporary workarounds that alter routes/services;
- device provenance and maintenance history connected to the existing material-culture layer.

## Copyright / transformation boundary

Do not copy the Apparatus, Sunny, Valley Windworks story beats, Devon story beats, Flux energy, Alter Pokémon, fan-game factories, dialogue or distinctive puzzle sequences.

Only reuse abstract structures such as infrastructure dependencies, maintenance, degraded service, device-specific Pokémon interaction, recoverable machine puzzles and technology/environment tradeoffs.

## Questions for later passes

- Which technology level and regional differences will be canon for Ouros?
- Which services require continuous power, water, communications or staff?
- Which machines can exist physically in Minecraft and expose stable state?
- What does PTU/Caelo actually allow Technology Education to do mechanically?
- Which crafting/repair Features from PTU/Caelo will be retained?
- What Rotom/device interactions are rules-backed versus narrative-only?
- How should infrastructure advance while chunks are unloaded?
- How much maintenance should be simulated before it becomes repetitive?
