# Pass 209 Research — field assistance, temporary cooperation and persistent wild identity

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-02

## Scope

This pass studies a gap not covered by passes 207–208: how Ouros can make helping a wild Pokémon, borrowing its field capability, solving a local service problem and returning it to ordinary life into a playable loop without implying ownership, capture, permanent recruitment or invented PTU mechanics.

The desired structure is useful for Marea Field Office work, Sendero del Vidrio maintenance and Pokémon-centered stories. It must coexist with the existing care/recovery layer rather than duplicate it.

## Internal project review

Before writing, the current recursive repository tree at narrative head `38ed9432b1401a11ecb41f6c89b16c075a0b4a21` was inspected and repository-wide searches were run for Ranger/field-move/request/rehabilitation/obstacle concepts. Targeted reads covered the current canon foundation, questline taxonomy, first visible wild population, care/recovery/welfare design and pass 208 research. The relevant boundaries are already explicit:

- Marea Field Office handles route observations, wildlife incidents, missing-person searches and practical assistance, but is not a police force and does not own rescued Pokémon;
- wild Pokémon may receive treatment without becoming owned;
- the first visible Sendero Fletchling is a persistent canonical wild identity/blueprint and cannot be silently repurposed;
- quest episodes reuse existing world entities and locations instead of creating isolated content islands;
- evidence and battle outcomes cannot manufacture ecological truth.

No prior indexed research in the repository uses Pokémon Ranger's quest/Field Move structure or Colosseum/XD's persistent Shadow Pokémon identity and progressive recovery as the source pattern developed here.

## Public research

### Pokémon Ranger: Shadows of Almia and Guardian Signs — local requests as field-service grammar

Sources:

- https://bulbapedia.bulbagarden.net/wiki/Ranger_Quest
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Ranger:_Shadows_of_Almia
- https://bulbapedia.bulbagarden.net/wiki/Obstacle
- https://bulbapedia.bulbagarden.net/wiki/Rain_Dance_(Field_Move)
- https://bulbapedia.bulbagarden.net/wiki/Psy_Power_(Field_Move)

Reusable structures:

Ranger Quests are optional requests from ordinary residents and can unlock as the world and prior work advance. Their useful structural range is broader than combat: investigate a report, obtain material, find or bring a Pokémon, open a path, calm a local problem or use a Pokémon's field capability in a specific place.

Ranger Field Moves also create an important separation between a Pokémon as an actor and an obstacle as a world object. The Pokémon supplies a capability for a bounded field task; the obstacle has a required interaction. In Ranger's own fiction, temporary Friend Pokémon can be released after assisting.

Ouros transformation:

- a citizen request should identify the practical problem before proposing a Pokémon solution;
- a wild Pokémon can cooperate for one bounded task without becoming captured, party-owned or permanently recruited;
- the world object and the actor remain separate records;
- species alone never grants permission to solve an obstacle: Ouros needs a verified capability/action contract;
- the same obstacle may have more than one legitimate solution when authored and mechanically supported;
- completion writes the result of the task, not ownership or loyalty.

Do not import Ranger capture-styler rules, friendship gauge math, exact Field Move levels, Ranger Points, mission ranks or specific quest plots.

### Pokémon Colosseum / XD — continuity before resolution

Sources:

- https://bulbapedia.bulbagarden.net/wiki/Shadow_Pok%C3%A9mon
- https://bulbapedia.bulbagarden.net/wiki/Purification
- https://bulbapedia.bulbagarden.net/wiki/Heart_Gauge
- https://bulbapedia.bulbagarden.net/wiki/Purify_Chamber

Reusable structures:

Colosseum/XD gives important identity continuity to Pokémon that remain unresolved over multiple encounters. Once a Shadow Pokémon has been encountered, its generated identity remains stable for later re-encounters. Its recovery also progresses through several kinds of interaction rather than one binary story beat, and final resolution is distinct from intermediate progress.

Ouros transformation:

- an authored wild individual involved in a rescue, disturbance or recurring observation should keep one persistent entity identity across escape, treatment, release and re-sighting;
- observed progress can accumulate as authored milestones without overwriting PTU health/status state;
- a care or assistance arc can end with release, continued observation or ordinary disappearance from player attention rather than capture;
- the final narrative state must be a world-state decision backed by actual events, never an inferred friendship meter.

Do not import Shadow Pokémon, snagging, corruption, purification, Heart Gauge values, locked moves, purification rewards or the Purify Chamber into Ouros canon.

## PTU / Caelo boundary

This pass does not establish a universal PTU field-move system. Pokémon capabilities, Moves, Skills, Features, movement modes, equipment and Trainer actions must be verified against the project's supplied PTU/Caelo/Kairos sources before any obstacle interaction becomes mechanical.

Narrative descriptions such as `can_help_move_debris`, `can_reach_high_marker` or `can_carry_line` are insufficient authority. A runtime action must point to a verified rule/capability contract or remain presentation-only.

Likewise, wild cooperation is a world-state relationship/event. It does not grant command legality, Trainer Features, capture rights, obedience, party membership or battle control.

## Derived candidate: FIELD_ASSISTANCE_CASE

Proposed, non-canon schema:

```yaml
field_assistance_case:
  case_id: null
  requester_entity_id: null
  owning_faction_id: null
  site_id: null
  problem_fact_refs: []
  affected_world_object_ids: []
  candidate_solution_contracts: []
  participating_pokemon_ids: []
  care_case_refs: []
  evidence_refs: []
  state: REPORTED | VERIFIED | ACTIVE | STABILIZED | RESOLVED | TRANSFORMED | CLOSED
  result_world_writes: []
  follow_up_refs: []
```

A solution contract should specify the actor, target object, authoritative action/capability reference, preconditions, result write, failure/transform behavior and exact engine capability families required.

## Derived candidate: TEMPORARY_COOPERATION_EVENT

```yaml
temporary_cooperation_event:
  event_id: null
  pokemon_entity_id: null
  initiating_context_ref: null
  bounded_task_ref: null
  observable_acceptance_refs: []
  authoritative_action_refs: []
  start_world_time: null
  end_world_time: null
  termination_reason: COMPLETED | DISENGAGED | UNSAFE | INTERRUPTED | OTHER
  ownership_write: NONE
  party_membership_write: NONE
```

This object records what happened. It never infers affection, obedience or ownership from assistance.

## Design lesson

Ouros gains more from Pokémon when they are allowed to participate in civic and ecological problems as persistent actors. A useful wild encounter can be remembered because the player helped, observed, cooperated, withdrew or later recognized the same individual. Capture and battle remain available where appropriate, but they do not need to consume every Pokémon-centered story.

## Rejected imports

Do not add Ranger organizations, Styler mechanics, Ranger ranks, specific Ranger quests, Shadow Pokémon, snagging, purification, Heart Gauges or Colosseum/XD institutions. Do not turn a species tag into a universal field key. Do not let Minecraft blocks decide PTU legality. Do not convert temporary cooperation into capture or loyalty. Do not make the existing Fletchling a required helper merely because it is the first implemented wild actor.
