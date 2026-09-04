# Projection arbitration and environmental signs scan — Pass 249

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Date: 2026-09-04

## Scope

This pass investigates the unresolved seam after Pass 248: an Ouros projection envelope can say that a population source is eligible for presentation, but the Minecraft/Cobblemon adapter still needs a safe decision between direct entity presentation, indirect environmental evidence, no presentation, and handling of an uncorrelated native entity.

The goal is to improve field exploration without allowing Minecraft spawn state to become ecological truth.

## Internal constraints preserved

Existing Ouros contracts already establish:

- population and persistent identity are authoritative Ouros state;
- Pass 248 derives projection eligibility from ecology pressure without changing abundance;
- Pass 239 requires a counted source and lease before a direct Cobblemon entity can represent that source;
- a Minecraft UUID is presentation correlation, not persistent identity;
- Pass 240 separates hidden world truth from observations, evidence and knowledge claims;
- accepting evidence or seeing an entity does not itself authorize AutoPTU handoff;
- PTU/Caelo/Kairos material remains evidence or comparison unless an Ouros canon file explicitly promotes it.

No species, population, resource, NPC, location fact, PTU rule or engine capability is promoted by this note.

## Public-source findings

### PTU community: evidence can precede the encounter

A 2020 PokemonTabletop GM discussion recommends replacing pure random encounter tables with evidence that Pokemon are nearby, including sounds or territorial markings, and resolving discovery with skills such as Perception, Pokemon Education and Survival. The reusable lesson is that field play can expose signs before it exposes an actor.

Source: Reddit r/PokemonTabletop, “How do you plan your wild encounters?”, 2020.
https://www.reddit.com/r/PokemonTabletop/comments/jivcud/

A 2024 exploration discussion describes wild Pokemon as active parts of the environment with small local stories rather than static capture targets. The reusable lesson is that a route can communicate behavior through environmental activity even when the player does not immediately engage a Pokemon.

Source: Reddit r/PokemonTabletop, “Question for Exploration”, 2024.
https://www.reddit.com/r/PokemonTabletop/comments/1gx1cz9/

These community examples are design evidence only. Their procedures and specific encounters are not Ouros canon.

### Acoustic monitoring: presence evidence does not require visual contact

Cornell Lab material describes acoustic monitoring as a way to document wildlife presence, seasonal patterns and vocal activity when direct observation is difficult. A separate Cornell overview notes that sound identification gives likely species suggestions that observers can compare and confirm.

Reusable lesson: an acoustic cue can support a presence claim while remaining weaker than direct individual identification. Ouros should preserve that distinction instead of turning every sound into a spawned Pokemon or exact count.

Sources:
- Cornell Lab of Ornithology, Acoustic Monitoring.
  https://www.birds.cornell.edu/landtrust/acoustic-monitoring/
- Cornell Lab of Ornithology, Merlin Bird ID.
  https://www.birds.cornell.edu/landtrust/merlin-bird-id/

### Mystery design: redundant evidence should use independent roots

Justin Alexander’s Three Clue Rule recommends multiple clues for conclusions so a scenario does not depend on one brittle clue. The important Ouros adaptation is not the literal number three as a rule of ecology. It is that exploration conclusions should be reachable through multiple independent evidence roots while provenance prevents one repeated rumor or duplicated sensor event from masquerading as corroboration.

Source: Justin Alexander, “Three Clue Rule”, 2008.
https://thealexandrian.net/wordpress/1118/roleplaying-games/three-clue-rule

This fits Pass 240 particularly well: several independent observations may strengthen a claim, while three relays of the same observation still count as one root.

## Reusable Ouros structures

### Presentation arbitration

After projection eligibility, Ouros should be able to request one of four presentation outcomes:

- DIRECT_ENTITY: a counted source is reserved and represented by a Cobblemon entity;
- INDIRECT_SIGN: the world presents evidence of ecological presence without creating an actor projection;
- NO_PRESENTATION: conditions are eligible but no player-visible manifestation is produced;
- QUARANTINE_UNCORRELATED_ENTITY: a Cobblemon entity exists without an approved Ouros source/lease and therefore cannot write ecological truth or enter AutoPTU automatically.

These are implementation candidates, not canon vocabulary.

### Indirect evidence as a first-class exploration surface

Useful fixture-only examples include an acoustic call, movement heard beyond line of sight, displaced generic perch debris, or another non-identifying environmental cue. A cue must not expose persistent actor IDs, exact population totals, hidden resource quantities or other secret ledger state.

Indirect evidence can feed Pass 240 observation and claim logic. It does not consume a population member, does not require a Minecraft entity UUID and cannot independently open AutoPTU.

### Independent evidence roots

An exploration node can offer several routes toward a conclusion such as “Fletchling are using this shelf during quieter periods”:

- direct visual observation during an eligible window;
- an acoustic observation from another window;
- a separately sourced NPC field note.

The sources should carry separate provenance roots. Repeating one root through several NPCs must not raise confidence as if several independent observations occurred.

## Original Ouros candidate

PROPOSED / FIXTURE-ONLY: during a high-disturbance period at lower Sendero, direct presentation may be suppressed while a non-identifying Fletchling acoustic sign remains eligible. The player can record that sign and later return during a quieter projection window for a direct sighting.

The premise does not require combat. It preserves the same ecology if the rich tactical version is unavailable.

No statement here canonizes a particular Fletchling call pattern, a physical forage resource, a new microhabitat, a new population, or a guaranteed individual source for the sound.

## Implementation consequences

A safe adapter seam needs to distinguish presentation from authority:

1. evaluate the current projection envelope;
2. choose a presentation mode;
3. for DIRECT_ENTITY, reserve an already-counted source before materialization;
4. for INDIRECT_SIGN, emit a sanitized observable event without a population lease or actor identity;
5. for an uncorrelated native entity, prevent demographic, knowledge or battle authority until explicit reconciliation succeeds;
6. feed only sanitized observation payloads into Pass 240;
7. keep AutoPTU handoff behind Pass 242 intent evaluation.

## Capability dependency classification

The reduced field-investigation version requires no AutoPTU battle capabilities. It depends on Ouros ecology/projection state and Minecraft/Cobblemon/Craftics adapter/playback support, which is currently PARTIAL/BLOCKING end-to-end.

A richer pursuit after direct sighting requires targeting/footprints/range/LoS only if tactical targeting enters the scene; base movement legality; complete movement when interception, forced movement or constrained pursuit matters; full turn/round lifecycle for tactical timing; AI legal-action infrastructure; AI tactical policy; and adapter/playback support. Terrain/weather/hazards/zones/reactions are required only when authored mechanics actually use them.

Damage, status lifecycle, move-specific behavior, abilities, items and Trainer Features/perks are dependencies only if the encounter invokes those exact mechanics.

## Open questions

- Should INDIRECT_SIGN have its own presentation budget so signs cannot spam a chunk when entity presentation is suppressed?
- Which signs are species-specific enough to require a validated ecological behavior profile rather than generic environmental evidence?
- Can an off-screen sign ever be attributed internally to a persistent individual, or should the first implementation remain population/habitat scoped to avoid accidental identity leaks?
- What exact adapter action should be taken with an uncorrelated native Cobblemon entity: hide, suppress, despawn, or hold outside authoritative interaction until reconciliation? This remains an implementation decision, not a narrative-rule assumption.
