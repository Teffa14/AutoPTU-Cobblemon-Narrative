# Global NPC social relationship / faction contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-05
Scope: all persistent/recurring Ouros NPC world agents
Parent: `design/global-npc-world-agent-ai-contract.md`
Consumes: `design/global-npc-goal-need-schedule-contract.md`

## Purpose

Provide one region-neutral social state model that can alter the existing global NPC agenda without creating region scripts, omniscient faction members or automatic combat.

The social layer produces bounded world-intent pressure. The agenda planner remains the selector. AutoPTU remains owner of structured tactical resolution.

## Directional relationship state

Each persistent relationship record has an explicit source agent and target agent.

Core dimensions for the first executable seam:
- affinity;
- trust;
- respect;
- fear;
- rivalry;
- reciprocal obligation/debt;
- semantic update time;
- provenance references.

Each dimension is independently bounded. A content event changes only dimensions justified by the semantic event.

`RELATIONSHIP(A -> B) != RELATIONSHIP(B -> A)`

No relationship record grants access to the target's private memory, knowledge, inventory or hidden goals.

## Dimensions remain separate

Affinity can make social contact or assistance more attractive.
Trust can influence willingness to rely on information or cooperate.
Respect can strengthen mentorship, deference or rivalry without requiring affection.
Fear can increase avoidance or caution without creating hatred.
Rivalry can encourage comparison, training, challenge or investigation without requiring hostility.
Reciprocal obligation/debt can increase pressure to assist or repay a concrete prior benefit.

No dimension is a universal loyalty score.

`AFFINITY != TRUST`
`TRUST != AGREEMENT`
`RIVALRY != HOSTILITY`
`FEAR != HATRED`

## Provenance gate

Persistent relationship mutation requires a semantic event or authored starting-state record with provenance.

Allowed inputs can include:
- direct interaction observed by the agent;
- remembered interaction;
- communication the agent actually received;
- a world result whose social consequence is explicitly authored;
- canon starting relationship state.

The planner cannot mutate trust or affinity merely because an action candidate was selected.

A source event can update A toward B without updating B toward A.

## Faction / institution membership

Membership records are separate from interpersonal relationship state.

Minimum fields:
- agent ID;
- faction/institution ID;
- role ID;
- active/inactive state;
- role commitment strength;
- standing where content uses it;
- explicit obligation tags;
- explicit permission tags.

Shared membership does not create hive-mind knowledge.

`SAME_FACTION != SHARED_PRIVATE_KNOWLEDGE`

Membership does not imply unlimited obedience. Faction duties become agenda pressure that still competes with critical needs, hard external commitments, emergencies, relationships and other goals according to explicit priority.

`MEMBERSHIP != UNCONDITIONAL_OBEDIENCE`

A permission exists only when an active role explicitly grants it. A role cannot infer jurisdiction not represented by the relevant authority contract.

## Social intent adaptation

A social candidate is authored as a world-level purpose such as:
- assist;
- socialize;
- communicate;
- report;
- mentor;
- seek advice;
- avoid;
- reconcile;
- negotiate;
- investigate another actor;
- train because of rivalry;
- arrange a challenge;
- fulfill a faction duty.

The social layer can derive bounded `relationship_weight` and faction `obligation` values for the existing `NpcIntent` utility calculation.

It cannot bypass required knowledge, permission, locality or structured-mechanics gates.

The same relation can affect different intent kinds differently. High rivalry can increase an `ARRANGE_CHALLENGE` candidate while high trust can increase an `ASSIST` candidate. Neither creates an action unless the global agenda selects it.

## Knowledge boundary

Relationships and factions influence interpretation and motivation; they do not reveal facts.

A report intent requiring `claim:x` remains ineligible until the NPC knows `claim:x` through an allowed observation/communication path.

A trusted person can later affect belief revision once the memory/communication layer owns source reliability. Pass 280 does not add that inference yet.

## Agenda integration

Socially adapted candidates join the same pool as:
- durable goals;
- needs;
- commitments;
- ordinary situational intents.

The planner must not create a separate social scheduler.

A critical physiological/maintenance need can beat a weak faction duty. A hard duty can beat casual socializing. A known emergency affecting a close relationship can beat ordinary work. Exact balance is Ouros world-AI policy and remains versioned/tested.

## Rival and battle boundary

Rivalry is persistent narrative/social state.

Possible world intents include finding a rival, messaging them, training because of them, arranging a match, observing them or challenging them.

A selected intent that actually requires PTU mechanics emits `REQUEST_AUTOPTU`.

The social layer never selects tactical targets, legal Moves, positions, initiative, damage, statuses, reactions or Trainer Features.

`RIVALRY != AUTO_BATTLE`

## Minecraft/Cobblemon projection

Local presentation can express selected social actions through movement, facing, conversation, gestures, meeting locations or other supported surfaces.

Minecraft entity proximity alone does not create friendship, fear, faction membership or a relationship event. Entity unload does not erase social state.

## Capability dependency map for mechanically rich social encounters

Reduced world-only version:
- social state and agenda selection: Ouros world-agent AI only;
- messaging/reporting: future world communication layer;
- arranging a challenge: no tactical dependency until accepted structured resolution begins;
- off-screen social planning: no Minecraft entity required.

Full structured encounter can require, depending on authored content:
- targeting/footprints/range/LoS: when tactical targeting begins;
- base movement legality: ordinary structured movement;
- complete movement: interception, push/pull, knockback or forced movement;
- core calculations: adopted PTU arithmetic;
- action economy/initiative: structured turns/actions;
- full turn/round lifecycle: multi-turn encounter state;
- full stateful damage pipeline: actual damage consequences;
- status lifecycle: persistent battle afflictions;
- terrain/weather/hazards/zones/reactions: only when encounter uses them;
- move-specific behavior: for selected Moves;
- abilities: for Ability effects;
- items: for Item effects;
- Trainer Features/perks: for Trainer mechanics;
- AI legal-action infrastructure: generation of legal structured options;
- AI tactical policy: autonomous tactical choice during AutoPTU resolution;
- Minecraft/Cobblemon/Craftics adapter/playback: local presentation and semantic-result playback.

A social motive never promotes any of these capability families.

## Current implementation status

Pass 280 executable seam:
- `tools/global_npc_social.py`;
- `implementation/global-npc-social-relationship-faction-fixture-v1.json`;
- `tests/test_global_npc_social_relationships_factions.py`.

## Canon boundary

This contract is proposed implementation architecture. Fixture actors, factions, relationship scores, jobs, duties and disputes are synthetic and do not establish Ouros canon.
