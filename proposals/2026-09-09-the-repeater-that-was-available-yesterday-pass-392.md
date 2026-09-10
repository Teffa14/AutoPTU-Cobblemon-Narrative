# The Repeater That Was Available Yesterday — Pass 392

Status: PROPOSED / NON-CANON.
Date: 2026-09-09

## Premise

Two field teams need the same communications capability during a period when routes and local infrastructure make substitutes difficult to obtain.

Team A checks an institutional resource record and learns that a portable field repeater is available at a remote depot.

Before Team A reaches it, another authorized mission checks the unit out. The repeater leaves the depot and becomes `IN_USE` under another holder.

Team A reaches the correct depot with correct older information and finds no usable repeater there.

No theft, sabotage or deception is required for the contradiction.

## Investigation and character pressure

The mystery begins as a practical failure rather than a crime accusation.

A dispatcher can truthfully state that the unit was available when the route was issued. The depot keeper can truthfully state that it was transferred later. The receiving team can truthfully state that they were authorized to take it. Team A can still suffer real consequences because their plan depended on stale state.

This creates several character directions without fixing a villain:

- a meticulous quartermaster who trusts recorded procedure but learns to distinguish record time from current state;
- a field leader who initially interprets the empty depot as institutional incompetence;
- a rival expedition whose legitimate priority competes with the player's objective;
- a coordinator forced to decide whether to reroute one team, negotiate a return window or locate a lower-capability substitute.

The relationship arc can change depending on whether the player verifies the timeline before accusing another actor.

## Reduced playable version

The reduced version needs no AutoPTU battle.

It uses:

- semantic time;
- `WorldResource` current state;
- `OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1` recovery;
- existing request/reservation/handoff owners when the scenario needs their histories;
- world travel and route planning;
- private knowledge and explicit communication;
- replanning when the expected capability is unavailable.

The objective can be completed by obtaining another communications path, negotiating access, waiting for the unit's authorized return, changing the expedition route or abandoning a time-sensitive sub-objective.

The narrative premise survives even if the actual capability is represented abstractly rather than as a Minecraft item.

## Rich encounter version

A mechanically richer version can stage the repeater's return during a hazardous field operation. The unit may need escort, extraction from an unstable location or protection while another actor finishes a task.

The tactical objective is resource recovery or safe transfer, not necessarily defeating every opponent.

### Permanent capability dependencies

Targeting/footprints/range/LoS: needed only if the rich version places combatants or interactable objective zones under tactical range/visibility rules. Use only verified audited scopes.

Base movement legality: needed for ordinary tactical movement to and around the resource. Verified only within audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: required if a carrier can be dragged, pushed, knocked away, intercepted or forcibly repositioned. PARTIAL based on current engine evidence.

Core calculations: required for ordinary audited combat calculations if combat occurs. Verified only within audited scopes.

Action economy/initiative: required if interacting with, securing or transferring the resource consumes tactical actions. Existing evidence verifies audited primitives only; any new objective interaction needs an explicit contract.

Full turn/round lifecycle: required for timed extraction windows, delayed shutdown, phased evacuation or end-of-round objective changes. PARTIAL.

Full stateful damage pipeline: required if damage to a carrier or objective changes persistent encounter state. PARTIAL.

Status lifecycle: required for lasting status effects that alter carrying, access or objective timing. PARTIAL.

Terrain/weather/hazards/zones/reactions: required for storm interference, unstable ground, hazard zones, reaction-triggered failures or visibility effects. MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated for every Move the encounter relies on.

Abilities: individually gated. No representative Ability implementation proves the family.

Items: individually gated. The field repeater is not automatically a PTU Item.

Trainer Features/perks: individually gated, especially interrupts or objective interactions.

AI legal-action infrastructure: ordinary audited legal-action scopes can be used where verified.

AI tactical policy: BLOCKING for protect-resource, escort-carrier, retrieve-object, transfer-object, objective-aware withdrawal and disengage-after-objective unless those policies gain live tests/contracts.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for stable resource projection, pickup/handoff acknowledgement, objective state and authoritative non-KO completion playback.

## Full version without rule duplication

If those tactical dependencies remain incomplete, the same story can stage hazardous portions between structured battles. The world layer decides current resource state and travel consequences. AutoPTU resolves only encounters it can authoritatively support. The adapter presents acknowledged outcomes rather than recreating missing PTU rules.

## Longer-term arc potential

Repeated resource-state conflicts can expose different institutional philosophies rather than one evil faction. One group may prioritize emergency response, another research continuity, another remote communities, and another infrastructure repair.

A season arc could make the player's reputation depend on whether they treat shared resources as common infrastructure, political leverage, personal property or evidence of institutional failure.

This remains a candidate pattern. No faction policy is canonized here.

## Canon questions

The following remain unresolved:

- which Ouros institution, if any, owns the catalog;
- whether a communications repeater exists in the setting at all;
- who can change operational state or approve reassignment;
- whether custody and legal ownership differ;
- which settlements or routes experience meaningful remoteness;
- which PTU/Caelo Skills, Features or Items could interact with communications/logistics;
- whether this incident belongs to a larger faction or infrastructure arc.
