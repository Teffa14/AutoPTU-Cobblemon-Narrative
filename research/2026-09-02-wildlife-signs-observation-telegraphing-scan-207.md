# Pass 207 Research — wildlife signs, observation telegraphing and peaceful encounter discovery

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-02

## Scope

This pass extends pass 206's Minecraft-visible wild encounter loop with a diegetic observation layer before direct contact: tracks, calls, feeding traces, disturbed vegetation, distant movement, repeated observation and visible social behavior.

The goal is to make wilderness exploration informative before combat and reduce pressure for every visible Pokemon to become an immediate capture battle.

No external plot, character, dialogue or species roster is imported as Ouros canon.

## Internal project evidence inspected

- `research/2026-09-02-minecraft-visible-wild-encounter-loop-scan-206.md`
- `design/engine-readiness-snapshot-pass-206.md`
- `design/ouros-source-authority-and-species-policy.md`
- `canon/marea-interior-map-resident-network-v2.md`
- branch-start narrative head `2b550193b609f0635a75cbbdc828ecc7bde118df`
- live main advancement `c123fb0b286c6c181fd29d4738e512547e8858fc`, which added `canon/marea-interior-first-wild-population-v1.md`
- read-only AutoPTU-Java head `496f7e15dbc4bb547449727cd60cd397d8d9005a`
- read-only AutoPTU evidence head `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
- current AutoPTU-Cobblemon-RPG visible-wild request, server-owned blueprint, immutable party handoff and authoritative HP projection evidence

Pass 206 already established visible pre-provisioned actors, bounded encounter regions, deliberate tracking separation and presentation behavior tags. This pass does not duplicate that architecture.

During this run, main canon-approved the first lower-shelf visible wild slot as a standard level-5 Fletchling with a frozen PTU 1.05 blueprint. That decision is now treated as established canon. The broader Sendero ecology remains unresolved.

## Public research

### New Pokemon Snap — ecological survey and repeated observation

Official sources:

- https://newpokemonsnap.pokemon.com/en-au/
- https://newpokemonsnap.pokemon.com/en-au/explore/
- https://newpokemonsnap.pokemon.com/en-us/create-photodex/
- https://newpokemonsnap.pokemon.com/en-us/free-update/

Reusable structures:

- exploration can center on observing Pokemon in habitat rather than immediately fighting them;
- repeated visits can reveal different behavior while the physical area remains recognizable;
- Pokemon can be partly hidden or found through environmental attention;
- plants, objects and habitat features can be investigation subjects alongside Pokemon bodies;
- research records can distinguish ordinary from uncommon behavior without turning rarity into combat power.

Ouros transformation:

- a route may expose observation clues before a visible actor is fully revealed;
- persistent route knowledge may remember only what the Trainer actually observed;
- repeated visits may unlock new authored observation surfaces when world conditions differ;
- no photography score, star system or Illumina mechanic is imported.

### Pokemon Legends: Arceus — disposition communicated before combat

Official examples:

- https://legends.arceus.pokemon.com/en-au/pokemon/cyndaquil/
- https://legends.arceus.pokemon.com/en-au/pokemon/zoroark/

The reusable pattern is that presentation can communicate different dispositions before battle. Timid, defensive, hostile and protective behavior create different expectations.

Ouros transformation:

Minecraft may present hiding, warning, retreating, guarding or watching as authored behavior. Those presentation facts cannot grant PTU bonuses, choose tactical moves, decide capture legality or replace encounter authority.

### Pokemon Scarlet/Violet mass outbreaks — visible temporary population events

Official example:

- https://www.pokemon.com/uk/news/seek-out-golden-shiny-pokemon-in-pokemon-scarlet-and-pokemon-violet-mass-outbreaks

Reusable structure:

A world can communicate that an unusual concentration of one species currently exists in a specific area. This creates a navigational/ecological signal rather than another invisible random roll.

Ouros transformation:

A future server-authored population event may increase visible signs, sightings or group presence in a bounded area. Exact abundance math, shiny probability, duration, species and rewards remain Ouros decisions.

### PokemonTabletop community GM practice — reasons and evidence before encounters

Sources:

- https://www.reddit.com/r/PokemonTabletop/comments/jivcud
- https://www.reddit.com/r/PokemonTabletop/comments/xzkco3
- https://www.reddit.com/r/PokemonTabletop/comments/11tn2q5
- https://www.reddit.com/r/PokemonTabletop/comments/xgemb5

Recurring community lessons, treated as anecdotal design evidence rather than rules authority:

- route encounters are stronger when they have a visible ecological reason;
- territory marks, nests, sounds and other evidence can precede contact;
- peaceful observation can give Pokemon personality and reduce combat fatigue;
- a small authored route pool is easier to make meaningful than a giant random table;
- individual capture scenes can stall multiplayer play when every sighting becomes a private battle.

Ouros transformation:

One clue instance should belong to the shared world. Individual intent can branch from that common state without spawning unrelated private Pokemon for every nearby player.

## PTU / Caelo cross-check

The project-source cross-check from pass 206 remains applicable:

- PTU Skills support noncombat interaction with wild Pokemon, so contact cannot imply mandatory battle;
- Caelo encounter records separate location/time/rarity/level from `Behavior` and `Details`;
- Caelo deliberate searching uses Survival/Perception patterns and remains separate from ambient presence.

This pass keeps those mechanics behind the active Ouros rules profile. Minecraft clues may request an authoritative Skill interaction, but they do not decide the result or invent a parallel tracking system.

No Caelo daily-search quota, DC, bait rule, species table or reward multiplier is adopted.

## Derived Ouros rule: clues before actors

A population profile may author one or more observation clues before a visible Pokemon actor is revealed.

Candidate clue categories:

- `TRACE`: tracks, scrape marks, shed material, disturbed soil;
- `FEEDING`: berries, shells, gnaw marks, stripped plants, leftovers;
- `NESTING`: nest material, burrow entrance, guarded resting site;
- `VOCAL`: calls, wingbeats, rustling, distant splashes;
- `MOVEMENT`: silhouette, wake, dust, canopy motion;
- `SOCIAL`: group formation, play, grooming, rivalry, guarding;
- `HABITAT_CHANGE`: locally disturbed vegetation, blocked path, moved stones;
- `DIRECT_SIGHTING`: visible Pokemon body at safe observation distance.

These are evidence surfaces. They must not claim species identity unless the authored source says the clue is sufficient or an authoritative interpretation succeeds.

The new lower-shelf Fletchling canon provides one concrete actor for this system. A clue attached to that slot may identify Fletchling only when that clue is authored to do so; unrelated route clues cannot be retroactively labeled Fletchling because it happens to be the first implemented wild species.

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
  identified_species_id?
  behavior_tag?
  provenance_version
```

Suggested provenance classes:

- `DIRECT`: clearly observed physical fact;
- `INTERPRETED`: conclusion produced by an authoritative check or expert source;
- `RUMORED`: NPC/player report not independently verified.

The system must preserve the difference between seeing a mark and knowing what made it.

`confidence_class` is narrative provenance, not a fabricated PTU bonus.

## Shared expedition principle

Multiple Trainers may inspect the same clue and reach different authoritative conclusions because their knowledge/Skills differ.

A successful private interpretation does not become automatic group knowledge. Shared Field Office records or explicit player communication can publish it.

This matters for MMO play: route ecology stays common world state rather than becoming one duplicated personal instance per player.

## Sendero del Vidrio use after the new canon decision

The first open-resident slot is now concretely anchored by the canon lower-shelf Fletchling.

This pass proposes an observation layer around that existing slot while leaving later roles unresolved:

1. `open resident lane`: lower-shelf Fletchling can be seen or signaled before engagement;
2. `avoidant lane`: future official species/content approval required;
3. `territorial lane`: future official species/content approval required.

Observation design must not mutate the Fletchling's canon level, stats, Big Pecks identity, Tackle/Growl loadout, HP or encounter identity.

## Full encounter concept and reduced version

### Full intended version — The Fresh Marks

Players find fresh route damage and ambiguous tracks near the seasonal crossing. Observation can establish recency, direction and likely behavior. Following the trail may reveal a protective/territorial wild group. If conflict begins, terrain and group positioning matter.

Dependencies:

- targeting / footprints / range / LoS;
- base movement legality;
- complete movement if shoves, interception or displacement matter;
- core calculations;
- action economy / initiative;
- full turn / round lifecycle for multi-stage escalation;
- stateful damage if consequences persist;
- status lifecycle if selected moves require it;
- terrain/weather/hazards/zones/reactions if the crossing itself is tactical;
- move-specific behavior;
- abilities;
- items if bait/tools are mechanically active;
- Trainer Features/perks if field checks or interrupts depend on them;
- AI legal-action infrastructure;
- AI tactical policy for protective/group tactics;
- Minecraft/Cobblemon/Craftics adapter/playback support.

### Reduced implementation

The same premise can run with static authored clues, one inspection interaction, one pre-provisioned actor, explicit observe/disengage/engage intent and an ordinary battle only if the player chooses engagement.

For the first live route slice, that actor can be the already-canonized lower-shelf Fletchling. The clue layer must bind to its existing authoritative encounter identity rather than creating a second random Pokemon.

No tactical weather, hazard cells, forced-movement objective, group tactics or delayed-status objective are required for the reduced version.

## Capability implications from live evidence

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
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for complete end-to-end support.

AutoPTU-Java head `496f7e15...` adds a sanity workflow on top of the forced-movement semantic-event gameplay head inspected in pass 206. It does not justify promoting any partial family to complete.

The RPG repository has stronger presentation evidence, but normal ecology still needs complete world-owned blueprint publication and authoritative battle/result reconciliation before the entire loop is playable.

## Rejected imports

Do not import:

- New Pokemon Snap photo scoring/star ranks or Illumina mechanics;
- Legends: Arceus aggro/flee radii or catch formulas;
- Scarlet/Violet outbreak probabilities or shiny rates;
- Reddit homebrew encounter dice or community level formulas;
- a generic assumption that nests imply aggression;
- species identity from a generic clue without authored evidence;
- tactical buffs from observation knowledge.

## Product criterion

This layer succeeds when a player can walk Sendero and learn something before touching a Pokemon:

1. notice a world-authored clue;
2. inspect it without triggering battle;
3. retain exactly what was observed with provenance;
4. optionally request an authoritative PTU/Caelo-governed interpretation;
5. follow or ignore the evidence;
6. meet the same authoritative individual represented by the clue chain;
7. keep peaceful observation valid when combat is unnecessary.
