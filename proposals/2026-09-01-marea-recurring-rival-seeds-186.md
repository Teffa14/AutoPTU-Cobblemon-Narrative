# Marea Recurring Rival Seeds — Pass 186

Status: PROPOSED / NON-CANON.
Date: 2026-09-01

These candidates use only established Marea people, locations and responsibilities unless explicitly marked uncertain. They do not canonize Jace Orrin as the player's rival. They provide ways that such a relationship could emerge from play.

## 1. The Yard Notices You

Primary NPC: Jace Orrin.
Location: Bruma Battle Yard.
Questline tags: RIVAL, COMPETITIVE, CHARACTER.

Premise:

Jace has seen enough public yard activity to consider the player worth testing. The first interaction is optional. If accepted, the battle exists to establish a shared competitive record, not to grant friendship or hostility.

World-state outputs:

- optional rival-candidate history edge;
- formal or exhibition battle record if the Yard contract supports it;
- public result visible at the Yard;
- revealed tactics only from what actually occurred.

Reduced implementation:

Use an audited stable-arena matchup with no unsupported terrain, hazards, reactions, forced movement, complex status interactions, Items or Trainer Feature interrupts.

## 2. Jace Is Working

Primary NPCs: Jace, Sela, Teo.
Location: Battle Yard.
Questline tags: CHARACTER, SETTLEMENT, RIVAL.

Premise:

The player arrives expecting a rematch. Jace is repairing or preparing fixtures under Sela's schedule and cannot battle now.

Purpose:

Show that a rival has responsibilities and can refuse a challenge without the system inferring fear or disinterest.

Possible follow-up:

A later exhibition window becomes available after the task is complete.

No BattleSpec required.

## 3. The Match Jace Misses

Primary NPC: Jace.
Questline tags: RIVAL, COMPETITIVE, CHARACTER.

Premise:

A local event proceeds while Jace is absent on another legitimate responsibility. The player's progress does not freeze his arc, and his absence does not generate a secret result.

World-state rule:

If no authoritative resolver exists, his unplayed match remains unresolved, is recorded as withdrawal/absence only when the event policy actually says so, or the bracket structure avoids fabricating a tactical outcome.

## 4. Public Tape, Private Team

Primary NPCs: Jace, Sela.
Questline tags: RIVAL, COMPETITIVE.

Premise:

A rematch is scheduled after both Trainers have public battle records. Jace may legally prepare from Moves and team members seen in public Yard records. He cannot read the player's current hidden loadout.

Purpose:

Exercise the scouting boundary and future AI-information contract.

Mechanical dependency:

Full intended version depends on AI tactical policy being able to consume only legally observed information. Until then, use a reduced policy that does not claim adaptive rival intelligence.

## 5. Rook Changes, But Not Silently

Primary NPCs: Jace, Sela, Rook only if canon relationship is later established appropriately.
Status note: UNCERTAIN because Rook is canonically Sela's companion, not Jace's.

Premise:

A public change in a recurring competitor's Pokémon should become an authored event with evidence instead of appearing because a scaled battle profile crossed a threshold.

Use:

This seed exists mainly as a guardrail. Do not evolve, transfer or alter Rook through rival-generation logic.

## 6. A Stronger Opponent, Different Reason

Primary NPC: Jace.
Questline tags: RIVAL, CHARACTER.

Premise:

Jace's desire for stronger competition becomes one reason to seek the player, but the encounter also intersects a responsibility Sela has delegated to him. Performance of the responsibility and result of the battle are evaluated separately.

Possible structure:

- Jace runs check-in correctly;
- Jace follows the approved match contract;
- battle occurs;
- post-match records are completed;
- Sela evaluates his procedural reliability independently of victory.

## 7. Help First, Battle Later

Primary NPCs: Jace, Teo, Mara.
Location: Puerto Bruma or Sendero del Vidrio.
Questline tags: RIVAL, CHARACTER, SETTLEMENT.

Premise:

The player and Jace cooperate on a mundane or field problem that has nothing to do with beating each other. Competition remains in their history, but the immediate objective is shared.

Rule:

`COOPERATION_EVENT != FRIENDSHIP_CONFIRMED`.

No battle is required.

## 8. The Rematch That Gets Postponed

Primary NPCs: Jace, Lia or Mara depending on cause.
Questline tags: RIVAL, SERVER_EVENT, COMPETITIVE.

Premise:

A scheduled exhibition is postponed because the venue, route or public-service situation changes. The postponement persists as state and may later be rescheduled.

Purpose:

Make world events affect rivalry without deleting the rivalry.

## 9. Jace Watches Someone Else

Primary NPCs: Jace, Sela, another approved Yard participant.
Questline tags: RIVAL, COMPETITIVE, CHARACTER.

Premise:

The player encounters Jace as spectator, maintenance hand or assistant rather than opponent. His knowledge gains come only from public observation.

Purpose:

Avoid making every Jace appearance a challenge prompt.

## 10. Parallel Training Week

Primary NPCs: Jace, Sela, Teo.
Questline tags: RIVAL, CHARACTER, EQUIPMENT.

Premise:

The player can see physical signs that Jace has been training while also helping maintain the Yard. The game records observable practice, not an automatic stat bonus.

Potential projections:

- scheduled drill board;
- repaired practice fixture;
- logged exhibition attendance;
- changed public style note after a real battle.

## 11. Rivalry Without a Ladder

Primary NPC: Jace.
Questline tags: RIVAL, RELATIONSHIP.

Premise:

The player repeatedly declines formal competition but still crosses paths with Jace. The relationship history continues through conversations, shared work and public events.

Purpose:

Prevent `RIVAL` from meaning mandatory combat content.

## 12. The Local Circuit Fork

Primary NPCs: Jace, Sela.
Questline tags: RIVAL, COMPETITIVE, CHARACTER.

Premise:

Jace receives an opportunity that competes with his Battle Yard responsibilities. The question is whether and how his schedule changes, not whether the player can defeat him.

Status:

PROPOSED only. No external circuit, job, title or promotion is canonized by this seed.

## Longer-term arc: The Measure Between Us

Status: PROPOSED.

A reusable arc for Jace if player history establishes reciprocal competitive interest.

Phase 1: Recognition

The player and Jace accumulate enough public overlap for a challenge to make sense.

Phase 2: First Record

An audited Yard match establishes a shared result.

Phase 3: Separate Work

Jace continues maintenance, training and delegated duties. The player continues unrelated questlines.

Phase 4: Reintersection

A world event, exhibition or shared task brings them together again.

Phase 5: Changed Evidence

Jace's role, style, schedule or public responsibilities visibly change through authored state.

Phase 6: Meaningful Rematch

Another battle occurs because the new state gives it purpose.

Phase 7: Parallel Standing

Either actor can advance elsewhere without forcing another match immediately.

Phase 8: Dormant or Mature Rivalry

The rivalry can remain active, become occasional, or go dormant while preserving history.

No phase automatically sets friendship, hostility, respect or career promotion.

## Rich encounter: Yard Circuit Test Under Pressure

Narrative premise:

Jace and the player are scheduled for a bounded Yard exhibition while an unrelated operational problem develops around the venue. The full version lets the world situation affect how the event proceeds without allowing the battle itself to solve the operational issue.

Full intended version dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement if any selected Move, Ability, Feature or arena interaction uses push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle when selected content requires it;
- terrain/weather/hazards/zones/reactions if the venue event is modeled tactically;
- exact move-specific behavior;
- exact abilities;
- exact items when permitted;
- exact Trainer Features/perks when Trainers participate;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

Current classification: BLOCKED for the full version.

Reduced version:

The operational problem is resolved or isolated through world state before BattleSpec creation. The exhibition then occurs on a stable audited court with a roster and contract deliberately restricted to currently verified behavior. If AI tactical policy is not parity-ready, the encounter should not claim that Jace adapts intelligently from historical scouting.

Allowed battle outputs:

- authoritative battle result;
- legally revealed information;
- supported mechanical aftermath;
- formal/exhibition record.

Forbidden automatic outputs:

- `JACE_RESPECTS_PLAYER`;
- `JACE_HATES_PLAYER`;
- `JACE_PROMOTED`;
- `JACE_BECOMES_PLAYER_RIVAL`;
- `SELA_APPROVES_JACE`;
- operational all-clear;
- venue repair completion.

## Canon questions preserved

- Whether Jace becomes a personal rival for a given player.
- Exact Yard challenge contracts.
- Whether the Yard has a recurring local circuit.
- Jace's long-term professional goal.
- Any future roster beyond his canon companion state.
- Exact family relation between Jace and Sela.
- Any Caelo-specific rivalry, ranking or rematch policy.
