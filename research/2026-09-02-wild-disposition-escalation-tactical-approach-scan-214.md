# Wild disposition, escalation and tactical approach scan — Pass 214

Status: RESEARCH / PROVENANCE — NON-CANON
Date: 2026-09-02

## Research question

How can Ouros make a wild Pokémon react to a Trainer in a way that is grounded in species behavior, the actual individual, the local population context, and the Trainer's real actions/capabilities, while keeping all mechanical consequences under PTU/AutoPTU authority?

This pass extends the existing `design/wild-pokemon-behavior-tolerance-tactical-policy.md`. It does not replace the observation work from pass 207 or canonize new Fletchling behavior.

## Public sources reviewed

### Pokémon Legends: Arceus — official gameplay site

Source: https://legends.arceus.pokemon.com/en-gb/gameplay/

Useful structure: approach is gameplay. Smoke Bombs reduce visibility and help a Trainer approach without being noticed; Heavy Balls are more effective against Pokémon that have not noticed the Trainer. This supports separating awareness, approach posture and capture opportunity instead of treating every visible wild Pokémon as an immediate battle.

Ouros adaptation: visibility, approach and alarm can alter the set of legal/appropriate tactical responses, but Minecraft stealth presentation cannot itself grant a PTU modifier. Any mechanical effect must come from an audited rule contract.

### Pokémon Legends: Arceus — overworld capture documentation

Source: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Legends%3A_Arceus
Source: https://bulbapedia.bulbagarden.net/wiki/Caught_Pok%C3%A9mon

Useful structure: wild Pokémon differ in overworld behavior, Trainers can crouch and use items to alter detection/behavior, and an aggressive Pokémon targeting the player changes what capture attempts are possible. Berries and other thrown items can influence behavior. The reusable lesson is that capture is downstream of behavioral state and preparation.

Ouros adaptation: do not import Legends catch-rate arithmetic, alpha behavior or item effects. Preserve only the high-level structure: notice state + species/individual response + Trainer tactic + legal capture/control action.

### PTU GM community discussion — encounter pacing and capture

Source: https://www.reddit.com/r/PokemonTabletop/comments/xgemb5

Community reports describe several useful practices: sneaking or distraction can precede a capture attempt; failed capture may cause a wild Pokémon to flee; and some GMs choose behavior based on disposition rather than requiring combat. The strongest design lesson is that capture should not force a long isolated combat loop every time a species becomes visible.

Ouros adaptation: group/world exploration can remain continuous. A Trainer may observe, approach, disengage, prepare a capture, or provoke escalation. Exact PTU capture rolls and Skill effects remain subject to source verification.

### PTU GM community discussion — narrative reason for wildlife encounters

Source: https://www.reddit.com/r/PokemonTabletop/comments/xzkco3

The discussion recommends grounding forced encounters in a reason such as a protected nest, predation event, blocked road or herd behavior rather than anonymous random combat. This aligns with Ouros world-state-first ecology.

Ouros adaptation: a wild encounter should carry a behavior trigger or ecological purpose when one exists. The trigger can disappear during play, permitting withdrawal or de-escalation without requiring defeat.

### Urban wildlife research — flight initiation distance and human density

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC9925442/
Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11461048/
Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10119130/

These studies use flight initiation distance as a measure of how close an approaching human can get before a bird flees. Across multiple datasets, urban populations often tolerate closer human approaches than rural populations, while response also varies with species, population, season, flock size, body size and other conditions.

Ouros adaptation: `population/location tolerance` is justified as a contextual prior. It must not become a universal city bonus or deterministic threshold. A Fletchling population accustomed to ordinary Sendero traffic may eventually have a different authored tolerance band than a remote population of the same species, if canon establishes that exposure.

### Individual consistency and learned threat identity

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC6506441/
Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2690012/

Research on burrowing owls found strong individual consistency in fear-of-human response, while urban mockingbirds were able to distinguish and escalate against a repeatedly threatening individual human. Together these findings warn against treating population habituation as a complete explanation for every individual.

Ouros adaptation: persistent wild individuals may carry bounded interaction history. The world may record that a particular Trainer pursued, harmed, assisted or repeatedly approached that individual. The system must not infer human-style friendship, hatred or trauma from a counter alone.

## Derived design model

The behavior decision should consume four layers in order:

1. source-backed species/population prior;
2. authoritative individual state and mechanical capabilities;
3. observed Trainer behavior plus the Trainer's currently legal capabilities;
4. current local context, including population habituation, protected resources, dependents, escape geometry and recent disturbance.

The result is a behavioral intent and a set of preferred legal actions, not a fabricated PTU effect.

### Proposed behavior transition record

```yaml
wild_behavior_transition:
  pokemon_id: null
  previous_state: null
  next_state: null
  species_prior_ref: null
  population_context_ref: null
  individual_state_refs: []
  observed_actor_refs: []
  trigger_refs: []
  legal_action_snapshot_ref: null
  selected_action_ref: null
  mechanical_result_ref: null
  confidence: AUTHORED | VERIFIED_INPUTS | PARTIAL_INPUTS
```

The record supports debugging: the server can explain why the Pokémon shifted from tolerant to alert, warning, withdrawal, evasion, guarding or engagement without relying on opaque Minecraft AI.

## Trainer tactic families

A Trainer can affect the encounter through position and legal actions. Tactics include reducing alarm by slowing or stopping approach, preserving an escape lane, using cover/LoS appropriately, or using verified handling/Stealth-like options. Capture-oriented tactics can include funneling, blocking an exit, legal hindrance, trapping, restraint or Status Affliction. Those stronger tactics should themselves become observable threats and can cause escalation.

A capability is not an action. Merely owning a trapping Move or Feature does not alarm a Pokémon unless the behavior system has authoritative evidence that it was revealed, activated or otherwise perceived.

## PTU/Caelo/Kairos cross-check boundary

The project source index routes exact review to Kairos Core Chapter 3 for Skills/Edges/Features, Pokémon/capture around pp. 340–369, movement and tactical positioning around pp. 382+, status around pp. 397+, terrain/weather around pp. 404+, and encounter creation around pp. 470+. The supplied first-wild canon additionally cites PTU 1.05 Pokédex p. 95 for Fletchling and notes Caelo comparative evidence describing ordinary Fletchling as urban/route-capable and territorial/diurnal.

Those references are routing evidence only. This pass does not assign a Charm, Command, Intuition, Survival, Stealth, Feature, Edge, capture, trapping or status modifier until the exact source text is audited.

## Implementation implications

The behavior interpretation layer can advance before full tactical AI. Once a battle/control action begins, AutoPTU must generate legal actions and resolve every mechanical consequence. Minecraft/Cobblemon presents posture, warning, flight, attack animation and spatial playback; it does not decide legality, capture, status, trapping or movement prevention.

A reduced encounter can still use authored tolerance bands, server-observed approach, warning animation, explicit withdrawal and a normal audited BattleSpec if escalation reaches combat. Missing status, trap, reaction or forced-movement mechanics must remain unavailable rather than simulated narratively.

## Canon effect

None. No species threshold, personality, habituation value, Skill modifier, capture modifier or new Fletchling fact becomes canon in this research file.