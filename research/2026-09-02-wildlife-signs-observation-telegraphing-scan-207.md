# Pass 207 Research — wildlife signs, observation telegraphing and peaceful encounter discovery

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-02

## Scope

This pass extends pass 206's Minecraft-visible wild encounter loop without selecting a canonical Sendero species table. The focus is what the player can learn before direct contact: tracks, calls, feeding traces, nesting evidence, disturbed vegetation, distant movement, repeated observation and visible social behavior.

The goal is to make wilderness exploration informative before combat and to reduce the pressure for every visible Pokemon to become an immediate capture battle.

No external plot, character, dialogue or species roster is imported as Ouros canon.

## Internal material inspected first

- `research/2026-09-02-minecraft-visible-wild-encounter-loop-scan-206.md`
- `design/engine-readiness-snapshot-pass-206.md`
- `design/ouros-source-authority-and-species-policy.md`
- `canon/marea-interior-map-resident-network-v2.md`
- current narrative head `2b550193b609f0635a75cbbdc828ecc7bde118df`
- current read-only AutoPTU-Java head `496f7e15dbc4bb547449727cd60cd397d8d9005a`
- current read-only AutoPTU evidence head `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
- current AutoPTU-Cobblemon-RPG main evidence including the visible wild request boundary and server-owned wild blueprint contracts

Pass 206 already established visible pre-provisioned actors, bounded encounter regions, deliberate tracking separation and behavior tags. This pass does not duplicate that architecture. It adds a diegetic observation layer before actor contact.

## Public research

### New Pokemon Snap — ecological survey and repeated observation

Official sources:

- https://newpokemonsnap.pokemon.com/en-au/
- https://newpokemonsnap.pokemon.com/en-au/explore/
- https://newpokemonsnap.pokemon.com/en-us/create-photodex/
- https://newpokemonsnap.pokemon.com/en-us/free-update/

Useful structures:

1. Exploration can be built around observing Pokemon in habitat rather than immediately fighting them.
2. Repeated visits can reveal different behavior while the physical area remains recognizable.
3. Pokemon can be partly hidden, visible only in unusual places, or discovered through environmental attention.
4. Plants, objects, sounds and habitat features can be investigation subjects alongside Pokemon bodies.
5. A research record can distinguish ordinary behavior from uncommon behavior without turning rarity into combat power.

Ouros transformation:

- a route can expose `observation clues` before a visible encounter actor is fully revealed;
- persistent route knowledge can remember what the Trainer has actually observed;
- repeated visits can unlock new authored observation surfaces when world conditions differ;
- no photography score, star system or Illumina mechanic is imported.

### Pokemon Legends: Arceus — species-specific disposition as presentation

Official examples reviewed:

- https://legends.arceus.pokemon.com/en-au/pokemon/cyndaquil/
- https://legends.arceus.pokemon.com/en-au/pokemon/zoroark/

The useful high-level pattern is that wild Pokemon presentation can communicate disposition before combat. Timid, defensive, hostile and protective behavior can produce different player expectations.

Ouros transformation:

Disposition tags may author Minecraft presentation such as hiding, warning, retreating, guarding or watching. These tags remain narrative/presentation facts. They do not grant PTU bonuses, choose tactical moves, determine capture legality or override authoritative encounter state.

### Pokemon Scarlet/Violet mass outbreaks — conspicuous temporary population events

Official example:

- https://www.pokemon.com/uk/news/seek-out-golden-shiny-pokemon-in-pokemon-scarlet-and-pokemon-violet-mass-outbreaks

Reusable structure:

A world can temporarily communicate that an unusual concentration of one species exists in a particular place. The event becomes a navigational/ecological signal rather than a generic random encounter roll.

Ouros transformation:

A future server-authored population event may increase visible signs, sightings or group presence in a bounded area. Exact species, abundance math, shiny probability, duration and rewards are not imported.

### PokemonTabletop community GM practice — narrative reasons and evidence before encounters

Sources:

- https://www.reddit.com/r/PokemonTabletop/comments/jivcud
- https://www.reddit.com/r/PokemonTabletop/comments/xzkco3
- https://www.reddit.com/r/PokemonTabletop/comments/11tn2q5
- https://www.reddit.com/r/PokemonTabletop/comments/xgemb5

Recurring community lessons, treated as anecdotal design evidence rather than rules authority:

- route encounters become more memorable when they have a visible ecological reason;
- territorial markings, nests, sounds and other evidence can precede direct contact;
- peaceful or observational encounters reduce table-time pressure and give Pokemon personality;
- a small authored route pool is easier to make meaningful than an enormous random table;
- individual capture scenes can stall multiplayer play when every sighting becomes a separate battle.

Ouros transformation:

The route should generate shared discoveries that the whole party can observe, then let individual intent branch from a common world state. A player who wants a capture can pursue it without forcing every nearby player into a private encounter scene.

## PTU / Caelo cross-check

Pass 206 already documented the relevant project-source findings:

- PTU Skills can support noncombat wild-Pokemon interaction rather than forcing every contact into battle.
- Caelo encounter records separate location/time/rarity/level from `Behavior` and `Details` fields.
- Caelo deliberate searching uses Survival/Perception patterns and remains distinct from ambient presence.

This pass keeps those mechanics behind the active Ouros rules profile. Minecraft observation clues may request an authoritative Skill interaction, but they do not decide the result or invent a new tracking subsystem.

No Caelo daily-search quota, DC, bait rule, species table or reward multiplier is adopted here.

## Derived Ouros design rule: clues before actors

A population profile may author one or more observation clues before a visible Pokemon actor is spawned or revealed.

Proposed clue categories:

- `TRACE`: tracks, scrape marks, shed material, disturbed soil;
- `FEEDING`: berries, shells, gnaw marks, stripped plants, leftovers;
- `NESTING`: nest material, burrow entrance, guarded resting site;
- `VOCAL`: calls, wingbeats, rustling, distant splashes;
- `MOVEMENT`: silhouette, wake, dust, canopy motion;
- `SOCIAL`: group formation, play, grooming, rivalry, guarding;
- `HABITAT_CHANGE`: locally disturbed vegetation, blocked path, moved stones;
- `DIRECT_SIGHTING`: visible Pokemon body at safe observation distance.

These are authored evidence surfaces. They must not claim species identity unless the source profile says the clue is diagnostically sufficient or an authoritative check succeeds.

## Observation knowledge state

Proposed non-canon data shape:

```text
ObservationRecord
  record_id
  observer_trainer_id
  route_or_site_id
  population_profile_id
  clue_type
  clue_instance_id
  observed_at_world_time
  observed_world_condition_id
  confidence_class
  identified_species_id?       // only if authoritative observation resolves it
  behavior_tag?                // only if actually observed
  provenance_version
```

`confidence_class` is narrative information provenance, not a fabricated PTU numerical bonus.

Suggested classes:

- `DIRECT`: clearly seen/heard physical fact;
- `INTERPRETED`: conclusion produced by an authoritative check or expert source;
- `RUMORED`: NPC/player report not independently verified.

The world must retain the difference between seeing claw marks and knowing which Pokemon made them.

## Shared expedition principle

For multiplayer, one clue instance belongs to the world. Multiple Trainers can inspect the same clue and may reach different authoritative conclusions because their knowledge/Skills differ.

This avoids spawning five unrelated private Pokemon merely because five players are walking together.

A successful observation can create shared party knowledge only through explicit communication or a shared institutional record; another Trainer's private check result is not automatically telepathic knowledge.

## Sendero del Vidrio candidate use

Status: PROPOSED, not canon.

Without selecting species, Sendero can support three first-route clue lanes:

1. `open resident lane`: obvious feeding/movement evidence leading to a common visible resident;
2. `avoidant lane`: faint trace or distant sound that rewards patient observation before the actor flees/reveals itself;
3. `territorial lane`: warning evidence near a bounded site that clearly gives the player a chance to withdraw before escalation.

This adds meaningful route exploration even before every battle mechanic is production-ready.

## Full encounter concept and reduced version

### Full intended version — The Fresh Marks

Players find fresh route damage and ambiguous tracks near the seasonal crossing. Observation can establish recency, direction and likely behavior. Following the trail reveals a protective or territorial wild group. The group may respond differently to distance, approach, noise and prior disturbance. If conflict begins, terrain around the crossing and group positioning matter.

Dependencies:

- targeting / footprints / range / LoS;
- base movement legality;
- complete movement if shoves, interception or displacement matter;
- core calculations;
- action economy / initiative;
- full turn / round lifecycle for multi-stage escalation;
- stateful damage if the encounter persists injury consequences;
- status lifecycle only if selected moves introduce persistent statuses;
- terrain/weather/hazards/zones/reactions if the crossing itself has tactical effects;
- move-specific behavior;
- abilities;
- items if bait/tools are mechanically active;
- Trainer Features/perks if field checks or interrupts depend on them;
- AI legal-action infrastructure;
- AI tactical policy for intended protective/group tactics;
- Minecraft/Cobblemon/Craftics adapter/playback support.

### Reduced implementable version

The same narrative premise can run with:

- authored static clue objects;
- one authoritative observation interaction;
- one pre-provisioned visible Pokemon actor;
- explicit approach/disengage choice;
- ordinary battle on a simple arena if engagement occurs;
- no tactical weather, hazard cells, forced movement objective, group tactics or delayed status objective.

Narrative premise remains: the player reads signs, chooses whether to investigate, then meets the same authoritative wild individual represented by the evidence trail.

## Capability implications from live evidence

Based on the latest read-only audit:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING as a complete family;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for complete intended behavior;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for full end-to-end target support.

AutoPTU-Java head `496f7e15...` adds project/rulebook sanity workflow on top of the forced-movement semantic-event head inspected in pass 206. It does not justify promoting any partial gameplay family to complete.

The RPG repository now has stronger presentation evidence, including authoritative PTU HP projection and the existing visible-wild request/blueprint boundaries, but normal ecology still requires trusted world-owned blueprint publication and complete end-to-end battle/reconciliation wiring before the full loop is playable.

## Rejected automatic imports

Do not import:

- New Pokemon Snap photo scoring/star ranks;
- Illumina mechanics;
- Legends: Arceus aggro/flee radii or catch formulas;
- Scarlet/Violet outbreak probabilities or shiny rates;
- Reddit homebrew encounter dice;
- community level formulas;
- a generic assumption that nests imply aggression;
- species identity from a generic visual clue without authored evidence;
- tactical buffs from observation knowledge.

## Product criterion

This layer succeeds when a player can walk Sendero and learn something before touching a Pokemon:

1. notice a world-authored clue;
2. inspect it without triggering battle;
3. retain exactly what was observed, with provenance;
4. optionally perform an authoritative PTU/Caelo-governed interpretation;
5. follow or ignore the evidence;
6. meet a visible Pokemon whose identity is already bound to authoritative encounter state;
7. keep peaceful observation valid when combat is unnecessary.
