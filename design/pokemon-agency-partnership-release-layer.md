# Pokémon Agency, Partnership & Release Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros needs one persistent model for an individual Pokémon that can survive capture, transfer, temporary cooperation, release, rehoming, institutional care, migration and retirement without flattening all of those states into one `owner_id` field.

Existing layers already handle social history, care, custody, breeding, conservation and wild collectives. This layer connects them around the Pokémon entity itself.

The design must support two boundaries at the same time:

1. Pokémon should remain characters with continuity outside battle.
2. The narrative generator must not invent emotions, consent, Loyalty values or obedience mechanics that belong to authored canon or PTU/Caelo rules.

## Core separation

Use separate records for separate facts.

```text
persistent Pokémon identity
        ↓
mechanical party / capture state
        ↓
custody and residence
        ↓
registration / ownership claims if canon defines them
        ↓
partnership history
        ↓
observed cooperation / refusal events
        ↓
mechanical Loyalty / Command state when authoritative
        ↓
public belief about the relationship
```

No arrow means that the lower state can be inferred from the higher state without evidence.

## 1. Persistent Pokémon entity

Important Pokémon should have durable identity even when they are not currently in a player party.

```yaml
pokemon_entity:
  pokemon_id: null
  authoritative_mechanical_ref: null
  species_ref: null
  current_location_id: null
  current_residence_id: null
  current_custodian_id: null
  active_trainer_id: null
  capture_or_ball_state_ref: null
  registration_claim_refs: []
  partnership_refs: []
  collective_membership_refs: []
  care_case_refs: []
  chronicle_event_refs: []
  public_identity_refs: []
  lifecycle_state: active
```

The narrative layer should never duplicate authoritative stats, Moves, Abilities, Loyalty, Injuries or battle state inside this record.

## 2. Association record

A Trainer/Pokémon association is historical state, not a synonym for ownership.

```yaml
pokemon_association:
  association_id: null
  pokemon_id: null
  actor_id: null
  association_kind: starter|captured_partner|temporary_partner|caretaker|research_contact|transport_partner|former_partner|other
  started_event_id: null
  ended_event_id: null
  current_status: active|dormant|ended|unknown
  custody_scope: null
  battle_control_scope: null
  residence_scope: null
  observed_cooperation_refs: []
  observed_refusal_refs: []
  shared_milestone_refs: []
  mechanical_relationship_ref: null
  provenance_refs: []
```

`association_kind` is descriptive metadata only. It does not create PTU bonuses.

## 3. Facts before feelings

Record observable Pokémon behavior precisely.

Good records:

- entered the battle after being called;
- refused one command;
- stayed beside an injured Trainer;
- returned to the same orchard on three mornings;
- accepted food from a caretaker;
- avoided one building;
- left with a migrating group;
- followed a Ranger during one rescue;
- returned to a former habitat after release;
- approached a former Trainer during a later encounter.

Do not automatically convert those facts into:

- loves Trainer;
- hates Trainer;
- feels abandoned;
- forgave Trainer;
- wants to be captured;
- wants to be released;
- is jealous;
- considers actor family;
- has trauma;
- consents to every future activity.

NPC/Pokémon internal states may exist when authored by canon. Procedural generation should prefer observable state.

## 4. Mechanical Loyalty belongs to PTU/Caelo

PTU has a formal Loyalty system.

Ouros narrative state may preserve events that could matter to Loyalty, such as care, neglect, recreation, mistreatment, long shared history or major rescues.

It must not:

- assign a Loyalty rank;
- change a Loyalty rank;
- decide a Command DC;
- decide whether a Pokémon obeys;
- create an obedience bonus;
- create a penalty from storage time;
- grant interception or other Loyalty effects;
- infer Loyalty from number of completed quests.

Those effects require the authoritative PTU/Caelo subsystem and its exact project rules.

## 5. Ownership, custody and active Trainer are separate

Ouros has not yet established one universal legal model for Pokémon ownership.

Therefore keep these separate:

- `current_custodian_id`: who physically has responsibility now;
- `active_trainer_id`: who is mechanically issuing Trainer-side battle commands when rules allow;
- `registration_claim`: what an institution or record says;
- `residence`: where the Pokémon normally lives;
- `ball_state`: authoritative capture/party storage state;
- `association`: historical relationship.

A clinic can be custodian without becoming owner.

A released Pokémon can still have a former Trainer association.

A temporary Ranger-like helper can cooperate without becoming a captured partner.

A Pokémon can live at a sanctuary while an ownership claim remains disputed.

## 6. Capture event

A capture should create a durable event with exact mechanical provenance.

```yaml
capture_event:
  event_id: null
  pokemon_id: null
  actor_id: null
  location_id: null
  timestamp: null
  mechanical_resolution_ref: null
  prior_wild_or_association_state: null
  resulting_ball_state_ref: null
  custody_change_ref: null
  registration_change_ref: null
  witness_ids: []
```

The capture event does not author personality or trust.

If PTU/Caelo allows befriending without combat, the resulting association should be generated from the authoritative resolution rather than rewritten as a fake capture battle.

## 7. Temporary partnership

Temporary cooperation needs first-class state.

```yaml
temporary_partnership:
  partnership_id: null
  pokemon_id: null
  actor_or_institution_id: null
  trigger_event_id: null
  purpose: rescue|survey|travel|habitat_defense|crisis_response|research|battle|other
  permitted_scope: []
  start_time: null
  expected_end_condition: null
  ended_event_id: null
  custody_changed: false
  ownership_changed: false
```

This structure supports Ranger-like assistance, local wildlife cooperation and crisis partnerships without making every helper a collectible roster asset.

## 8. Release event

Release is a state transition, never entity deletion.

```yaml
release_event:
  event_id: null
  pokemon_id: null
  releasing_actor_id: null
  mechanical_release_ref: null
  release_location_id: null
  release_reason_authored: null
  resulting_residence_state: null
  resulting_collective_state: null
  custody_end_ref: null
  registration_change_ref: null
  future_contact_policy: unknown
```

Unless explicitly authored, do not infer why the Pokémon or Trainer chose the separation.

The old association remains historical.

## 9. Post-release continuity

A released or rehomed Pokémon can later participate in the world graph.

Possible future state:

- joins or leaves a wild collective;
- becomes a recurring research observation;
- occupies a known home range;
- receives care from a sanctuary;
- temporarily assists former companions;
- becomes associated with another actor;
- migrates with a species group;
- becomes part of local public memory;
- disappears from observation without being declared dead.

This avoids the RPG pattern where release means deleting content.

## 10. Transfer and rehoming

Transfer should record at least:

- Pokémon identity;
- previous custodian;
- new custodian;
- mechanical party/registration result;
- reason if authored;
- consent/authorization evidence when project canon requires it;
- associated belongings or held-item custody;
- transition location;
- handoff witnesses when relevant.

A successful transfer does not guarantee immediate trust or tactical coordination.

Do not invent disobedience either. Leave cooperation mechanics to PTU/Caelo.

## 11. Refusal and hesitation events

If authored state or authoritative mechanics produce refusal, record the smallest defensible fact.

```yaml
pokemon_response_event:
  event_id: null
  pokemon_id: null
  actor_id: null
  requested_action_ref: null
  response: accepted|refused|hesitated|withdrew|unknown
  mechanical_resolution_ref: null
  observed_context: []
  interpretation_refs: []
```

One refusal should not become a permanent global tag.

## 12. Wild familiarity without capture

Ouros should support repeated relationships with wild Pokémon.

```yaml
wild_familiarity_record:
  pokemon_id: null
  actor_id: null
  encounter_count: 0
  observed_interaction_refs: []
  accepted_resources_refs: []
  followed_actor_refs: []
  approached_actor_refs: []
  avoided_actor_refs: []
  capture_state: wild
```

This is not a Friendship stat.

It simply preserves repeated observable contact.

## 13. Residence can outlast party membership

A Pokémon's home may be:

- with a Trainer household;
- a club or institution;
- a nursery;
- a sanctuary;
- a worksite;
- a research station;
- a transport service;
- a habitat;
- a mobile base;
- unknown.

Residence does not automatically establish owner, custodian or active battle Trainer.

## 14. Institutional Pokémon

Some Pokémon may be associated with institutions rather than one personal Trainer.

Possible examples:

- clinic helper;
- ferry partner;
- rescue-team Pokémon;
- nursery resident;
- research-station Pokémon;
- workshop helper;
- protected-area familiar;
- Gym staff Pokémon;
- farm or orchard resident.

The institution must define who can issue commands, who provides care and what happens when staff change.

Do not assume institutional service is permanent or involuntary.

## 15. Player authority boundary

A player's own mechanical Pokémon state remains authoritative through the game systems.

Procedural narrative must not silently:

- release a player's Pokémon;
- trade it;
- transfer custody;
- retire it;
- change its active Trainer;
- decide it refuses the player;
- decide it wants another Trainer;
- place it in permanent institutional service;
- establish a new owner;
- permanently remove it from the party.

Any irreversible player-facing transition requires explicit player action or authoritative game mechanics.

## 16. Pokémon agency without anthropomorphic overreach

The system can represent choices when they are actually observed or authored.

It should not force every Pokémon into human-like internal monologue, ethics or language.

Species intelligence, communication capability and individual characterization should come from canon, PTU/Caelo material or authored character design.

## 17. Partnership callbacks

Useful future callbacks can come from:

- first capture location;
- hatch location;
- first battle;
- first major defeat;
- rescue history;
- former home;
- former Trainer;
- old caretaker;
- migration site;
- favorite documented activity;
- old team members;
- institutional history;
- release location.

Callbacks should use verified history, not generated nostalgia.

## 18. World-state integration

This layer connects to existing systems.

Care:
- treatment does not change ownership;
- rehabilitation can end in release without deleting identity.

Breeding/nursery:
- hatching creates entity continuity;
- custody after hatching remains explicit.

Conservation:
- released Pokémon can enter protected-area and collective state;
- relocation is not the same as capture.

Wild collectives:
- an individual may join or leave a group;
- former Trainer history should not magically alter collective behavior.

Homes:
- residence can persist even when active roster changes.

Travel/workplaces:
- institutional Pokémon may have schedules and service roles.

Public memory/media:
- public stories about a famous partnership remain claims/public memory rather than private emotional truth.

## 19. Minecraft/Cobblemon representation

Desired adapter-facing state may include:

- stable Pokémon entity ID;
- current world representation ID;
- current residence/home anchor;
- current custodian/association metadata;
- former-partner reference where appropriate;
- spawn/despawn persistence policy;
- release-state persistence;
- institutional role tag;
- wild familiarity callbacks.

Minecraft must render this state. It must not independently decide ownership, Loyalty or obedience.

## 20. Encounter implementation contracts

### Temporary Ally at the Floodgate

Narrative premise:

A local wild Pokémon repeatedly observed around a damaged floodgate begins helping responders during a crisis. The players can coordinate around it for one scene. The Pokémon does not become a party member automatically.

Full version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING if route protection matters
- core calculations: VERIFIED for implemented primitives; exact temporary-partner/Command mechanics unverified
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if floodgate water or zones are tactical
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for an autonomous allied Pokémon pursuing a scene objective
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

The wild Pokémon's assistance resolves in overworld world state before combat. If a battle begins, it uses an ordinary legal static encounter and the helper remains outside the tactical grid unless current engine support can represent it safely.

### Former Partner at the Orchard

Narrative premise:

A Pokémon released or rehomed in a prior authored event is later observed around an orchard that has become part of its routine. A new problem affects the site.

Full version dependencies:

- ordinary static combat can use VERIFIED targeting/base movement/core/action infrastructure;
- any special command acceptance, former-Trainer control or loyalty callback is mechanically BLOCKING until exact PTU/Caelo rules and engine support exist;
- collective or habitat behavior stays world-state unless tactical AI is available;
- Minecraft persistence is BLOCKING.

Reduced version:

The former partner is an NPC Pokémon controlled only by authored scene logic outside battle. The player cannot issue battle commands merely because of historical association. A separate static AutoPTU encounter resolves any actual combat.

### Transfer Station Breakdown

Narrative premise:

A legitimate transfer/rehoming handoff is interrupted by a transport failure. The story focuses on keeping custody, records and Pokémon identities clear while solving the disruption.

Full version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception: BLOCKING if escort becomes tactical
- core calculations: VERIFIED generally; transfer/Loyalty rules unverified
- action economy/initiative: VERIFIED
- lifecycle/damage/status/move/ability/item/Feature families: use only validated slices
- terrain/weather/hazards/zones/reactions: BLOCKING for dynamic infrastructure failure
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for protection/escort goals
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Transfer records and Pokémon custody remain outside the grid. Players clear a normal legal encounter or repair problem, then the handoff continues through world state.

## 21. Promotion gate

No proposal from this layer can become mechanical canon until reviewers confirm:

1. exact PTU/Caelo Loyalty rules;
2. exact Command/obedience interactions;
3. capture/release/transfer rules used by Ouros;
4. ownership/registration canon where relevant;
5. stable Pokémon identity semantics in Cobblemon;
6. multiplayer authority for irreversible party changes;
7. AutoPTU ownership of any battle-level obedience resolution.

## 22. Design objective

The target experience is simple:

A Pokémon should remain the same meaningful individual before capture, during partnership, after transfer, after retirement or after release whenever the world has a reason to remember it.

The system should preserve what happened without deciding what the Pokémon privately feels unless canon or mechanics actually establish it.
