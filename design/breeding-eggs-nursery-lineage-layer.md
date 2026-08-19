# Breeding, Eggs, Nursery & Lineage Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already models care, custody, social bonds, ecology, settlements, travel, institutions and public memory. This layer adds the missing structures needed for Pokémon Eggs, nursery services, hatching, juvenile care and lineage provenance.

The layer is deliberately conservative. Narrative state can remember where an Egg came from, who cared for it and where it hatched. It cannot decide PTU breeding eligibility, species, inheritance, Ability, Nature, gender, hatch time or Hatcher benefits unless the governing PTU/Caelo rules have produced those results.

## Core boundary

Keep these concepts separate:

```text
mechanical breeding resolution
        ↓
Egg mechanical state
        ↓
Egg provenance / custody / care history
        ↓
authoritative hatch event
        ↓
persistent Pokémon entity
        ↓
juvenile care and later personal history
```

The narrative system owns provenance and story continuity.

PTU/Caelo owns breeding and hatching mechanics.

AutoPTU owns tactical legality when a later scene becomes a battle.

Minecraft/Cobblemon renders world presence and interactions after adapter support exists.

## Egg object

An Egg should be a persistent world object rather than an inventory string.

```yaml
egg_id: null
status: incubating
mechanical_resolution_ref: null
species_state: unresolved
known_parent_ids: []
source_institution_id: null
source_event_id: null
created_at_world_time: null
expected_hatch_state_ref: null
custodian_id: null
custody_location_id: null
ownership_claims: []
care_history_refs: []
travel_history_refs: []
medical_or_incubation_flags: []
public_knowledge_refs: []
hatched_entity_id: null
mechanics_review_required: true
```

### Required rule

If mechanical resolution is not known, the generator must leave the result unresolved.

It may never choose a species because it “fits the story.”

## Mechanical state vs narrative state

Possible mechanical fields should be stored only after authoritative resolution:
- species;
- hatch timing;
- Nature;
- Ability;
- gender;
- Inheritance Move List;
- Egg Move outcomes;
- any Hatcher/Breeder modifications;
- any item effect that changes hatch timing.

Narrative fields may include:
- who carried the Egg;
- who was present when it was found or handed over;
- where it was stored;
- which nursery cared for it;
- important travel or crisis exposure;
- who was present when it hatched;
- public rumors about it.

Narrative exposure must not silently modify mechanical output.

## Custody model

Egg custody reuses the case/custody layer but needs explicit hatching semantics.

```yaml
egg_custody_event:
  event_id: null
  egg_id: null
  from_actor_id: null
  to_actor_id: null
  from_location_id: null
  to_location_id: null
  reason: null
  authority_ref: null
  consent_ref: null
  timestamp: null
```

Valid narrative reasons can include:
- temporary boarding;
- transport;
- emergency transfer;
- research examination;
- intended handoff;
- adoption process;
- institutional care;
- recovery from abandonment.

No reason implies ownership automatically.

## Ownership and guardianship guardrail

Ouros has not yet established a complete legal framework for ownership of Eggs, rescued Pokémon, abandoned Pokémon or institutionally raised first partners.

Therefore:
- custody is factual;
- ownership may be claimed or disputed;
- guardianship can be temporary;
- intended recipient is not automatically owner;
- genetic parentage does not automatically determine human ownership;
- nursery possession does not automatically transfer ownership;
- hatching does not automatically settle a dispute.

These questions can later become worldbuilding or case material.

## Nursery institution

A nursery is a persistent service actor.

```yaml
nursery:
  nursery_id: null
  name: null
  location_id: null
  operating_state: OPEN
  service_profile: []
  staff_ids: []
  caretaker_roles: []
  egg_capacity: null
  juvenile_capacity: null
  occupied_egg_ids: []
  juvenile_entity_ids: []
  specialties: []
  supply_dependencies: []
  referral_links: []
  public_program_ids: []
  regulations_or_policies: []
  incident_refs: []
  history_refs: []
```

Possible services, each separately authored:
- Egg incubation support;
- temporary boarding;
- juvenile care;
- first-partner preparation;
- breeder consultation;
- rehabilitation;
- Trainer education;
- research observation;
- adoption coordination;
- transport preparation.

A facility does not provide every service by default.

## Capacity and service pressure

Capacity should become relevant only when it creates meaningful decisions.

Useful states:
- NORMAL;
- BUSY;
- LIMITED;
- PRIORITY_ONLY;
- CLOSED;
- EVACUATED;
- RELOCATED.

Causes should be traceable:
- festival demand;
- migration season;
- transport disruption;
- disease/welfare incident;
- staff absence;
- power failure;
- damaged infrastructure;
- regional breeding season;
- rescue intake;
- supply shortage.

The system should not generate arbitrary “nursery full” gating without state explaining why.

## Hatching clock

Hatching is a world-time event backed by PTU/Caelo mechanical timing.

Narrative state can know:
- that the Egg is progressing;
- the authoritative expected window when rules permit it;
- whether a legal item or effect modifies that window;
- which location and custodian hold it.

Narrative state cannot invent:
- acceleration from affection;
- damage from ordinary weather;
- buffs from special scenery;
- bonus inheritance from travel;
- premature hatching from dramatic tension.

Unless PTU/Caelo explicitly supports an effect, those remain flavor only.

## Hatch event

A successful authoritative hatch writes a durable event:

```yaml
hatch_event:
  event_id: null
  egg_id: null
  pokemon_entity_id: null
  timestamp: null
  location_id: null
  present_actor_ids: []
  custodian_id: null
  mechanical_resolution_ref: null
  care_history_refs: []
  public_visibility: PRIVATE
  chronicle_weight: null
```

The new Pokémon inherits mechanical state only from the authoritative breeding/hatching subsystem.

The Chronicle may inherit provenance links but not infer personality.

## Juvenile care state

Recently hatched Pokémon may carry a narrative lifecycle:

```yaml
juvenile_profile:
  pokemon_entity_id: null
  hatch_event_id: null
  care_provider_ids: []
  home_location_ids: []
  observed_preferences: []
  observed_fears: []
  training_milestones: []
  social_introductions: []
  first_battle_event_id: null
  independence_state: null
```

Only directly observed behavior should populate preferences or fears.

Do not infer:
- temperament from species;
- loyalty from caregiver time;
- competence from parentage;
- rivalry from sibling status;
- affection from co-location.

## Parentage and lineage graph

When parentage is mechanically/canonically established, use explicit edges:

```text
PARENT_OF
HATCHED_FROM
CARED_FOR
RAISED_AT
TRANSFERRED_TO
TRAINED_BY
```

Avoid vague edges such as `bloodline_quality` or `good_stock`.

Lineage exists to support provenance, history, ecology and legal inheritance mechanics where PTU defines them.

## Historical breeding programs

A settlement or institution may have a historical breeding program.

Useful state:
- founding purpose;
- species or ecological focus;
- records retained;
- participating caretakers;
- ethical standards;
- current status;
- notable outcomes;
- controversies;
- genetic/lineage claims with confidence levels;
- relationship to wild populations.

This can support mysteries such as incomplete records or conflicting provenance without inventing parentage.

## Conservation breeding boundary

Conservation narratives can use:
- habitat restoration;
- captive care;
- juvenile release;
- population monitoring;
- genetic diversity as an authored scientific concern;
- institutional disagreements over intervention.

The generator must never create numerical genetic diversity, fertility, inbreeding or viability mechanics unless an explicit future system establishes them.

Wild population state remains separate from Trainer-owned or nursery-raised lineages.

## First-partner programs

A region may operate a first-partner program where Eggs or young Pokémon are raised before placement with new Trainers.

Potential states:
- candidate pool;
- care history;
- readiness assessment;
- intended placement;
- placement interview/event;
- follow-up support.

Mechanical selection criteria must not be fabricated.

The system should prioritize character fit, care context and institutional policy only where those policies are authored.

## Breeder / Hatcher careers

PTU explicitly supports Hatcher/Breeder-oriented character specialization.

Ouros can therefore support career state such as:
- apprenticeship;
- nursery employment;
- supervised care cases;
- research collaboration;
- breeding records;
- public reputation;
- mentor relationships;
- facility responsibilities.

Mechanical Features, Edges, bonuses and prerequisites remain PTU/Caelo-owned.

Narrative career progression cannot award them automatically.

## Multiplayer consent

When two players contribute Pokémon to an authorized breeding process:
- participation must be explicit;
- parent Pokémon remain player-controlled entities;
- the system must record consent to the process;
- custody of any resulting Egg must be resolved explicitly;
- the generator must not invent romantic/family language between Pokémon;
- the system must not assume shared ownership of the Egg.

This follows the project-wide rule that observable actions may be remembered while private relationship labels require authored evidence.

## Nursery events

Nurseries can produce noncombat content through:
- staffing problems;
- supply deliveries;
- first-partner ceremonies;
- escaped juveniles;
- record reconciliation;
- parentage disputes;
- adoption interviews;
- conservation releases;
- training demonstrations;
- facility expansions;
- care workshops;
- research visits;
- transport handoffs;
- emergency intake.

These should be generated from actual nursery/world state.

## Battle integration

An Egg or juvenile should rarely be a tactical combatant.

When a nursery story produces battle, keep battle responsibilities explicit.

### Encounter contract A — Nursery Perimeter Breach

Narrative premise:
A hostile group or wild threat reaches the outer grounds of a nursery. The objective is to prevent access to the protected building.

FULL version:
- attackers may attempt alternate paths;
- defenders can intercept movement;
- dynamic blockers or gates may change;
- AI prioritizes reaching an objective rather than only KO;
- civilians/Eggs remain protected off-grid unless future rules support more.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: BLOCKING;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING if gates/zones are tactical;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: BLOCKING if defender interrupts are used;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version:
Resolve a standard combat on a fixed map outside the nursery. Protected Eggs and civilians are outside the battle grid. Narrative success means the path is cleared before entry. Use only verified targeting/base movement/core/action-economy/legal-action foundations plus reviewed partial combat slices.

### Encounter contract B — Nesting-Ground Evacuation

Narrative premise:
A wild nesting area must be crossed or evacuated during an ecological disturbance.

FULL version:
- moving hazards alter safe space;
- participants escort or protect noncombatants;
- reactions/interception matter;
- objective success can occur without defeating every Pokémon.

Dependencies:
- complete movement: BLOCKING;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- lifecycle: PARTIAL;
- status: PARTIAL;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING.

REDUCED version:
Separate exploration from battle. Use overworld/world-state choices to choose a route. If combat occurs, resolve a normal legal battle in a static arena. Afterward write evacuation/protection consequences from authored objective state, not invented tactical events.

### Encounter contract C — Nursery Exhibition Match

Narrative premise:
A nursery or breeder association hosts a public demonstration showing how young but battle-ready Pokémon are trained safely.

FULL version:
Could include formal withdrawal rules, safety restrictions, special audience/venue state and Trainer/Hatcher interactions.

Dependencies:
- targeting: VERIFIED;
- base movement: VERIFIED;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- lifecycle: PARTIAL;
- damage: PARTIAL;
- status: PARTIAL;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: BLOCKING if Hatcher/Trainer features are mechanically relevant;
- AI legal actions: VERIFIED;
- AI tactical policy: BLOCKING for autonomous opponent strategy;
- adapter: BLOCKING.

REDUCED version:
Run an ordinary legal AutoPTU battle using only mechanics verified for the participating Pokémon. Treat event framing, audience and safety policy as narrative context. Do not add hidden damage caps, special buffs or invented withdrawal triggers.

## Capability readiness snapshot

Current evidence from AutoPTU-Java remains conservative:

- VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.
- PARTIAL: full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items.
- BLOCKING: complete movement including push/pull/knockback/interception/forced movement; terrain/weather/hazards/zones/reactions; Trainer Features/perks; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback.

Recent Java work adds authoritative lifecycle hooks, ordered damage hooks, canonical ability identities, a Mega Launcher parity slice, held-item state and a Pink Pearl item parity slice. These are important seams, not proof that whole families are complete.

## Minecraft/Cobblemon presentation

Eventually the overworld can represent:
- incubators or Egg displays;
- nursery pens;
- staff schedules;
- capacity indicators;
- juvenile Pokémon presence;
- first-partner ceremonies;
- pickup/drop-off handoffs;
- transport crates or approved carriers;
- nursery expansions;
- conservation-release events.

Minecraft must not calculate breeding legality, inheritance, hatch timing or Hatcher bonuses.

Those decisions must arrive as authoritative state from the rules layer.

## Failure-forward design

Nursery stories should rarely use permanent loss as the default consequence.

Useful failure consequences:
- delayed handoff;
- transfer to another facility;
- public trust change;
- damaged infrastructure;
- missed research window;
- custody dispute;
- an escaped juvenile requiring search;
- increased workload;
- reduced capacity;
- route/service changes.

Any injury, Egg damage or mechanical status requires actual rules support.

## Promotion checklist

Before a breeding/nursery proposal becomes canon or executable content:

1. Confirm the institution exists in Ouros canon.
2. Confirm its legal/service mandate.
3. Resolve custody and ownership rules where relevant.
4. Verify PTU/Caelo breeding and hatching mechanics.
5. Verify any Hatcher/Breeder Feature used.
6. Verify item effects such as Egg Warmers.
7. Verify species/parent/inheritance data against the governing Pokédex.
8. Attach encounter capability dependencies when combat exists.
9. Provide a reduced battle version when the full version depends on blocked families.
10. Confirm Minecraft/Cobblemon presentation does not recalculate PTU rules.

## Design outcome

This layer lets Ouros tell long-form stories beginning before a Pokémon hatches and continuing afterward, while keeping the most error-prone parts—breeding output, inheritance, mechanics and ownership—explicitly outside freeform narrative generation.