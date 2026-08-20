# Evolution, Life Stage & Transformation Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros needs a persistent Evolution contract that preserves one Pokémon's identity while its authoritative species/form state changes.

Existing systems already cover Eggs, partnership, release, care, ecology and public memory. This layer owns the transition between those states and prevents the narrative generator from turning Evolution into an automatic reward, consent signal or unsupported mechanic.

## Core separation

```text
persistent Pokémon entity
        ↓
authoritative current species/form
        ↓
authoritative Evolution eligibility
        ↓
known candidate paths
        ↓
choice / intention only when explicitly authored or player-provided
        ↓
authoritative Evolution resolution
        ↓
mechanical refresh
        ↓
world-state consequences
        ↓
public memory / records
```

Eligibility does not imply intention. Intention does not perform the mechanic. A resolved Evolution does not replace the persistent entity.

## Persistent Evolution state

```yaml
evolution_state:
  pokemon_id: null
  current_species_ref: null
  current_form_ref: null
  authoritative_rules_ref: null
  eligibility_checked_at: null
  eligible_path_refs: []
  unresolved_condition_refs: []
  known_to_actor_path_refs: []
  decision_state: unresolved
  decision_provenance_ref: null
  last_evolution_event_id: null
  mechanics_review_required: true
```

`decision_state` is meaningful only where the rules/world model exposes a decision. Do not invent a psychological choice for an automatic biological process.

## Evolution event

```yaml
evolution_event:
  evolution_event_id: null
  pokemon_id: null
  from_species_ref: null
  from_form_ref: null
  to_species_ref: null
  to_form_ref: null
  authoritative_resolution_ref: null
  trigger_context_ref: null
  location_id: null
  world_time: null
  battle_ref: null
  witness_ids: []
  before_mechanical_snapshot_ref: null
  after_mechanical_snapshot_ref: null
  downstream_refresh_refs: []
  chronicle_event_ref: null
```

The same `pokemon_id` must exist before and after ordinary permanent Evolution.

## Evolution history

Keep a durable ordered history rather than only the current species.

This supports:

- old photographs correctly identifying the Pokémon's former species;
- historical battle records;
- research notes made before Evolution;
- former housing/equipment records;
- public misidentification after a change;
- released or wild individuals recognized later;
- family/lineage history without conflating Evolution with ancestry.

Historical records remain historically correct when they were correct at the time.

## Branching paths

For branching species, store separate concepts:

```yaml
evolution_path_status:
  pokemon_id: null
  path_ref: null
  rules_eligible: unknown
  conditions_satisfied: unknown
  actor_knows_path: false
  actor_intention: unknown
  resolution_state: unresolved
  provenance_refs: []
```

Never select a branch because it creates a better story, fills a team weakness or matches a faction aesthetic.

The current Python Career deterministic selector can remain useful for simulations or generated opponents where project policy authorizes it. It must not silently resolve an important persistent Pokémon's branch when a player-facing or authored decision is required.

## Delay and refusal

When the authoritative rules allow Evolution to be delayed, the world can preserve that state.

Possible factual records:

- Evolution became eligible at a known time;
- an Evolution attempt was cancelled under an authoritative mechanic;
- an Evolution item was offered but not used;
- the option was discussed;
- a later event reopened the same decision.

Do not infer:

- fear of Evolution;
- desire to stay small;
- rejection of the Trainer;
- lack of ambition;
- loyalty to a current form;
- consent or refusal from silence.

Those meanings require authored evidence.

## Evolution items and other resources

An Evolution item remains a persistent item instance governed by the material/item systems.

Possessing the item does not evolve the Pokémon.

Giving, lending, stealing, recovering or displaying the item changes custody/provenance. Actual use and resulting Evolution require authoritative mechanics.

## Place, time and environment-linked eligibility

Narrative generation may create reasons to visit a place or observe a season when an authoritative Evolution rule depends on those conditions.

It may not manufacture a new condition.

Keep these separate:

- physical location/time/weather state;
- actor knowledge of a possible condition;
- rule eligibility query;
- actual Evolution resolution.

A myth or local tradition that says a place causes Evolution is a claim until mechanics/canon establish it.

## Wild and institutional Pokémon

Evolution does not require player ownership.

A persistent wild Pokémon may:

- evolve within a collective;
- evolve during a seasonal gathering;
- evolve between research observations;
- evolve after release;
- evolve while living at a sanctuary;
- evolve while serving an institution when that relationship is canon-supported.

The event can change ecology or social state, but it cannot automatically make the Pokémon stronger in ways not present in the authoritative species data.

## Post-Evolution refresh contract

After a permanent Evolution, downstream systems should re-query authoritative state rather than copy assumptions from the previous species.

Potential refresh targets:

- battle species/stat profile;
- legal Moves and Abilities;
- footprint/size representation;
- movement/capabilities;
- held-item legality if relevant;
- care requirements;
- housing/space requirements;
- travel/mount assumptions;
- institutional work eligibility;
- habitat/collective role;
- visual identity and public records;
- Cobblemon model/entity representation.

Each target is independent. A change in one field never proves changes in all others.

## Temporary transformations

Permanent Evolution and temporary transformation must use separate records.

```yaml
transformation_event:
  transformation_event_id: null
  pokemon_id: null
  transformation_kind: null
  authoritative_mechanic_ref: null
  start_battle_or_event_ref: null
  started_at: null
  ended_at: null
  temporary_form_ref: null
  reverted_to_species_ref: null
```

Mega Evolution, Teracrystal/Terastallization, Dynamax-like state or other temporary mechanics cannot overwrite permanent Evolution history.

The exact allowed transformations in Ouros remain a canon/rules decision.

## Form changes

Not every form change is Evolution.

Regional forms, battle forms, seasonal forms, appliance states, stance changes and other transformations need their own authoritative classification.

The narrative system records what the rules engine says happened. It does not decide whether a form is permanent, inherited, reversible or species-changing from appearance alone.

## Evolution and public knowledge

Different actors may learn about an Evolution at different times.

Possible consequences:

- a Pokédex/research record updates;
- a club roster still lists the old species;
- a newspaper misidentifies the evolved individual as a new Pokémon;
- a former caretaker recognizes the individual through provenance/behavior;
- a battle institution updates a public roster;
- a photograph remains labelled with the old species because it predates the event.

Information spreads through the existing communications/public-memory systems.

## Offline advancement

Routine wild or NPC Evolution may advance offline only when:

- the authoritative trigger is deterministic and represented;
- no player-owned decision is required;
- the result does not consume a player-controlled item or irreversible choice without authorization;
- the resulting entity can persist safely.

Important partner branching choices should remain pending rather than being resolved while the player is offline.

## Battle implementation tiers

### Tier A — between-battle Evolution

Preferred first implementation.

1. Finish or pause the current tactical encounter under legal rules.
2. Resolve Evolution through an authoritative world/Career transition.
3. Refresh the persistent entity.
4. Load the evolved state into the next battle.

This preserves narrative continuity without requiring Java to rebuild a combatant mid-turn.

### Tier B — live mid-battle Evolution

Future capability requiring a dedicated Java contract.

A safe implementation must define at minimum:

- when during lifecycle the transition occurs;
- HP and Injury carry-over;
- status carry-over/clearing;
- combat-stage carry-over;
- new maximum HP handling;
- footprint and occupied-cell validation;
- legal Move/Ability refresh;
- initiative implications;
- queued/delayed effects referencing the old species state;
- AI legal-choice regeneration;
- ordered semantic battle events;
- Minecraft/Cobblemon visual swap and playback.

None of these rules may be guessed by the narrative adapter.

## Encounter contract — Mountain Threshold

Premise: a known Pokémon reaches a location associated with an authoritative Evolution condition while another conflict occurs.

REDUCED:

Run the tactical battle using the pre-Evolution state. After battle resolution, query the authoritative Evolution condition and process the permanent transition in world state if legal and authorized.

FULL:

Allow the Evolution event to occur during battle and continue with the evolved combatant.

Full dependency map:

- targeting/footprints/range/LoS — VERIFIED baseline, but footprint replacement needs dedicated transition validation;
- base movement legality — VERIFIED baseline;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if occupancy/forced movement interacts with the transition;
- core calculations — VERIFIED primitives, but species refresh contract still required;
- action economy/initiative — VERIFIED baseline, transition timing still needs contract;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if the condition or battlefield changes depend on them;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED baseline, but post-transition regeneration needs validation;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Additional blocker: no verified Java mid-battle Evolution transition contract.

## Encounter contract — Wild Ceremony Disturbance

Premise: researchers observe a recurring wild gathering where some individuals may become mechanically eligible to evolve.

REDUCED:

Keep the ceremony and Evolution checks in world state. If a separate hostile encounter occurs, battle only the immediate participants on a static map. Resolve any Evolution after the tactical encounter unless an existing authoritative mechanic says otherwise.

FULL:

Persistent wild actors can evolve during the event while groups reposition, withdraw or protect space.

Extra full dependencies include complete movement, broad terrain/zones if used, tactical AI and adapter playback. Wild collective membership remains narrative state and grants no combat bonus.

## Encounter contract — Mid-Match Breakthrough

Premise: an important battle reaches a legitimate Evolution trigger.

REDUCED:

Finish the current battle with the current species. Resolve Evolution immediately afterward and make the rematch/follow-up use the new state.

FULL:

Transform live and continue the same battle transcript.

This is blocked until the dedicated Java transition contract exists, even if every other listed capability eventually becomes verified.

## Canon boundary

Do not promote any Evolution event to canon from narrative convenience alone.

Required provenance includes the Pokémon entity, authoritative rule/result, time/location, consumed resources where relevant and resulting species/form state.

## Open implementation questions

- Exact PTU/Caelo Evolution rules and overrides.
- Whether an important Pokémon can have unresolved eligible branches indefinitely.
- How player consent/choice is represented for irreversible Evolution decisions.
- Cobblemon UUID/entity preservation across species change.
- Between-battle Java/Career integration path.
- Whether mid-battle Evolution is in the initial AutoPTU-Java scope.
- Exact carry-over semantics for HP, Injuries, stages, statuses and delayed effects if live Evolution is eventually implemented.
