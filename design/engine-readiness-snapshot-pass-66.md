# Engine Readiness Snapshot — Pass 66

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.
Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live Java evidence

Newest inspected AutoPTU-Java commit:

`8670b4bf2b423c5d9e43cc9e8d6c979e6c832909` — Derive Chronicler Accuracy from authoritative runtime state (#228).

Immediately preceding:

`bc236441497771f54fd67e46d11d111ec9a1ec41` — Own Chronicler profile identity in runtime state (#227).

These commits strengthen one specific Trainer Feature/Accuracy slice by moving Chronicler profile identity and its Accuracy derivation into authoritative runtime state, adding ownership tests and fail-closed behavior for legacy input. This is meaningful implementation progress.

It does not establish complete Chronicler behavior, complete Trainer Features/perks, general knowledge mechanics, complete Accuracy state, or any of the environment/movement/AI/adapter families below.

The current Java README at `8670b4bf...` still reports implemented slices for:

- targeting, areas, footprints, target anchors and LoS;
- Shift and jump movement legality;
- Damage Base/type tables and calculation primitives;
- invariant d20 accuracy resolution;
- combat-stat resolution;
- typed turn flow/action budget;
- deterministic initiative;
- legal autobattler action-space generation.

The same README still explicitly leaves unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- full semantic BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Live Python evidence

Newest inspected AutoPTU commit:

`f4535cc8385fa6ee6805bdd2d0ef67b5b03ac8e6` — Career: fall back to Light Mode when battle renderer fails (#167).

The underlying change `67f7955ac07db5fd923c9eb5459079d8acf8aa15` makes the Career renderer degrade safely when the battle renderer fails.

This improves runtime resilience and presentation fallback. It does not add battle mechanics, tactical AI, object-custody rules or Minecraft/Cobblemon adapter semantics.

## Permanent capability map

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

Pass 66 does not promote any capability category.

## Found-property state is narrative/world authority

The new found-property extension may determine:

- which exact item instance was found;
- where and when it was recovered;
- who currently has custody;
- which loss reports may match;
- which actors asserted claims;
- what evidence supports/contradicts those claims;
- whether a return was authorized by an existing rule/institution;
- whether a physical handoff actually occurred;
- whether the matter was handed to Courier, Collection or Case systems.

It does not determine:

- combat item legality;
- held-item effects;
- damage;
- Accuracy;
- statuses;
- movement costs;
- initiative;
- targetability;
- Trainer Feature activation;
- AI tactical priorities.

## Item-category caution

The permanent capability family `items` is PARTIAL because AutoPTU-Java does not yet have complete item hook registries.

A persistent narrative `item_instance` must not be mistaken for a supported PTU battle item.

Examples:

- a lost camera case has no combat effect because it is tracked narratively;
- a notebook does not become a held item with custom bonuses;
- a returned tool does not create a crafting/combat action unless PTU/Caelo and engine data support it;
- a recovered medicine-like prop cannot heal because the story calls it medical;
- a named object that corresponds to a real PTU item must still use the exact implemented item contract if it is activated in battle.

## Chronicler caution

The newly strengthened Chronicler Accuracy path cannot be generalized into an investigation bonus.

Finding a lost notebook, identifying a maker mark, reviewing provenance or interviewing a claimant does not grant Chronicler Accuracy. Any Chronicler effect remains governed by its exact authoritative runtime ownership, eligibility and timing contract.

## Encounter review — Trail Satchel Recovery

Narrative premise:

A personally significant satchel has been reported missing along a route. A later inspection locates the exact object inside an area currently occupied by defensive or hostile Pokémon.

Intended full version may require:

- exact persistent object identity outside ordinary loot generation;
- route-access/search objective;
- weather or terrain interaction when PTU-mapped;
- changing safe approach lanes;
- forced displacement or interception;
- territorial/withdrawal behavior;
- objective-aware tactical AI;
- adapter playback that keeps battle outcome, object presence and later recovery synchronized.

Dependency state:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when active
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Keep the satchel in narrative world state and outside tactical targeting. Close the unsafe search area while combat is active. Run an ordinary reviewed static battle using only supported mechanics. After the authoritative result makes the area safe, perform a separate recovery interaction and create the find/custody event.

The battle result cannot prove ownership, authenticate contents or auto-complete restitution.

## Encounter review — Event Teardown Recovery Sweep

Narrative premise:

After a temporary public event closes, teardown workers find several personal objects near a section that wild Pokémon are beginning to occupy again.

Intended full version may require:

- workers/civilians withdrawing from the site;
- multiple protected recovery zones;
- temporary barriers or fragile scenery;
- changing route access;
- forced movement/interception;
- environmental hazards if exact rules support them;
- territorial/retreat AI rather than pure KO optimization;
- adapter playback preserving which objects were physically recovered and when.

Dependency state:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when active
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Evacuate workers before tactical resolution. Preserve named objects as world-state records rather than battle entities. Run a static encounter to make access safe. After combat, execute a noncombat recovery sweep and create separate find events for significant objects.

A win does not grant the winning Trainer ownership or custody by itself.

## Noncombat readiness

Pass 66 systems that can advance before new tactical families include:

- loss reports;
- exact find events;
- temporary custody;
- holding-location history;
- possible-match records;
- claim assertions;
- claimant evidence/provenance review;
- claim contradiction tracking;
- restitution handoffs;
- unclaimed-pending-review state;
- referral to Courier/Case/Collection systems;
- recurring lost-property service/backlog state;
- actor knowledge/privacy around private verification details;
- callbacks when a returned object changes a later routine or relationship.

These require persistent narrative/world state and eventual UI surfaces. They do not require AutoPTU to simulate ownership.

## Adapter implications

Safe future behavior:

- materialize only narratively significant found objects as persistent named props;
- use aggregate shelves/boxes for unimportant lost-property clutter;
- synchronize visible prop location with authoritative custody state;
- keep private claimant-verification details out of public NPC dialogue;
- remove/move a prop only after the authoritative handoff event;
- preserve identity and custody across chunk unload/server restart;
- link a shipment recovery back to the existing Courier record instead of spawning a new unrelated object;
- create later callbacks from actual restitution history.

Unsafe shortcuts:

- Minecraft pickup changes `current_owner_id` automatically;
- despawn means “returned”;
- respawning a unique found object after reload;
- giving every claimant the private description;
- treating NBT/display name as universal proof of ownership;
- making battle victory recover/return every object automatically;
- letting a dropped prop participate as a battle item without an implemented PTU item rule;
- using Cobblemon behavior to adjudicate claimant truth.

## PTU/Caelo mapping requirement for mechanically relevant recovered objects

Before a recovered object affects battle, implementation must identify:

- exact PTU/Caelo item/rule source;
- item identity and holder/owner semantics required by that rule;
- action/timing/frequency requirements;
- target legality;
- duration and expiry;
- relevant Move/Ability/Feature interactions;
- state mutation and transcript output;
- AI legal/action implications;
- adapter representation.

Narrative significance alone cannot satisfy this contract.

## Unresolved mechanical questions

- Which item hooks are currently safe to expose through Minecraft once adapter work begins?
- How should a significant narrative item that is also a PTU mechanical item share identity across persistence layers?
- What exact transcript events will represent item transfer/use when those registries arrive?
- How will objective-aware AI represent withdraw/protect/access goals without parallel Minecraft rules?
- Which terrain/weather states will be mapped from overworld conditions rather than left narrative-only?

## Unresolved canon questions

- Which Ouros institutions or services accept found property?
- What return-verification customs exist in each region?
- How are private identifying details handled?
- Can a recipient authorize a proxy, and through what established system?
- What happens to unclaimed property?
- Are finder rewards culturally normal anywhere?
- Which objects require special custody or automatic escalation?
- Which settlements have sufficiently regular transit/event/service routines for recurring lost-property stories?

Until these are approved, Pass 66 remains a systems/proposal layer only.