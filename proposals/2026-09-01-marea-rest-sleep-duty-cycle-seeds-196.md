# Marea Rest, Sleep & Duty-Cycle Seeds — Pass 196

Status: PROPOSALS / NON-CANON
Date: 2026-09-01

These candidates reuse canon Marea Interior people, locations and institutions. They do not establish a regional sleep culture, labor law, camp network, fatigue mechanic or PTU recovery shortcut.

## Canon anchors

Useful established facts:

- Estación Mirador supports field observations, route reports and specimen records.
- Nerea Sol leads field research; Ema Rey performs equipment checks, transects and field-note preparation under project protocols.
- Puerto Bruma has boarding rooms, a clinic/care station, ferry landing, Battle Yard and Tideglass Archive.
- Ivo Serrat begins purchasing before dawn.
- Taro Min has two interview evenings each week.
- Sela Orrin handles morning maintenance/training and later public Battle Yard sessions; Jace Orrin assists sessions and maintenance.
- Lia Morn records ferry arrivals/departures and Mina Cors operates coastal ferry runs.
- Sendero del Vidrio is the ordinary route between Puerto Bruma and Loma Clara and supports authored fieldwork.

None of these facts establishes a universal timetable beyond the specific schedule statements already in canon.

## 1. Mirador First-Light Handoff

Primary recommendation.

Nerea schedules a bounded first-light observation because an existing research question benefits from that window. Ema is the person assigned to the live observation; Nerea reviews the field note later.

The player can:

- join Ema during the live window;
- wait at an appropriate authored location and join the later review;
- pursue another lane and read the resulting record afterward;
- compare what Ema directly observed with what Nerea later interprets.

Persistent outputs:

- observation author and timestamp;
- field-note version;
- handoff from Ema to Nerea;
- player knowledge based on what they personally attended;
- unresolved questions retained after review.

The episode demonstrates that a useful event can occur without the player and that missing a live scene does not delete world history.

No PTU Rest, sleep, fatigue or Skill reward is required.

Questline types: `CLASS`, `CHARACTER`, `FACTION`, `EXPLORATION`.

## 2. Before Ivo Opens

Ivo's pre-dawn purchasing schedule becomes visible through an optional early visit to Bruma Market Hall.

The player may witness a routine intake/substitution decision before public meal service begins. If they arrive later, Ivo can still refer to the decision and the relevant lot record can exist.

Value:

- reinforces that NPC work precedes player arrival;
- connects food, supply and schedule state;
- gives early time-of-day texture without adding a mandatory opening-hours puzzle.

Do not infer that Ivo never sleeps, works every day at the same minute or suffers fatigue because of early hours.

## 3. Late Ferry, Later Departure

A ferry return already represented by service state arrives later than expected. Mina's next departure is consequently moved or reassigned through an authored service update.

Lia records the actual arrival and publishes/communicates the revised service state through existing channels.

The player can adjust plans rather than being told that a delayed operator simply functions at full schedule forever.

The story does not add mandatory rest law. It models believable resource availability.

Questline types: `SETTLEMENT`, `REGION`, `CHARACTER`.

## 4. Battle Yard Closeout

Jace handles a bounded closeout task after a public Battle Yard session: returning ordinary fixtures, noting a repair issue or preparing a short handoff for Sela's next maintenance block.

A player who stays after the session can see the work. A player who returns in the morning sees its consequence instead.

This creates Jace character progression through responsibility without requiring another rival battle.

Do not grant operational competency beyond his already canonized junior role.

## 5. The Interview That Ends the Day

Taro's existing evening interview block runs long because a deposit contains a contradiction that should not be resolved casually.

The archive can close the session with the discrepancy still open. Pia or Taro records what must be checked later.

The next day begins with a research hook rather than a magical overnight solution.

No relationship penalty follows from ending the interview instead of continuing indefinitely.

## 6. Boarding Room Is Not a Pokémon Center

A visitor or player character uses one of Puerto Bruma's already established boarding rooms to sleep or wait for morning.

The world clock can advance through the future rest/wait interface. Mechanical recovery occurs only if AutoPTU validates the relevant PTU Rest/Extended Rest effects.

This candidate exists mainly to protect the architecture from a common implementation shortcut:

`BED_INTERACTION -> FULL_HEAL`

That shortcut is forbidden unless an authoritative mechanic specifically produces the result.

Questline types: `SETTLEMENT`, `SECONDARY`.

## 7. Handoff Without Omniscience

Mara finishes one work period with an unresolved route question and leaves a bounded handoff for the next responsible actor or for her own next review window.

The packet contains only:

- the current report;
- what was verified;
- what still needs field confirmation;
- any custody or equipment state that actually transfers.

The successor does not inherit Mara's entire private knowledge graph.

This is a small but reusable institutional-continuity test.

## 8. Sendero Overnight Stage

A future authored field operation has a legitimate reason to stop at a temporary staging point on Sendero rather than return immediately.

The scene can track:

- who remains with equipment;
- who is off duty;
- what observation is planned for the next period;
- whether an interruption occurs;
- whether the plan is resumed, modified or abandoned.

The staging point is event-local unless later canon explicitly establishes a permanent shelter or campsite.

No watch assignment grants mechanical bonuses by itself.

## 9. Nocturnal Observation, Evidence First

Mirador receives enough current evidence to justify checking a known location during a night window for a specific ecological question.

Species, behavior and timing must come from established or newly evidenced ecology state. The clock alone cannot spawn a convenient nocturnal species.

A player who does not attend may later receive the observation as attributed evidence rather than being forced to repeat the night.

Questline types: `POKEMON`, `CLASS`, `EXPLORATION`.

## 10. The Wake-Up That Was Not an Emergency

A resident is awakened because a routine but time-sensitive handoff needs confirmation. The situation stays routine.

The purpose is to resist escalation bias: waking someone at night does not automatically mean disaster, attack or crisis.

After confirmation, the actor can return to private time or rest. Narrative records the interruption without inventing mechanical sleep loss.

## 11. A Morning Without the Player

The player sleeps, waits or spends the period elsewhere. During that interval, several already-scheduled ordinary actions legitimately occur:

- one service changes schedule slot;
- one document delivery completes;
- one NPC moves to their next workplace state;
- one existing observation window closes.

On return, the player encounters consequences and records rather than a frozen world.

The episode is generated only from pre-existing clocks and assignments. It cannot roll a random tragedy because the player advanced time.

## 12. Shift Changed, Question Survived

An unresolved question passes across two workers or two schedule blocks while the evidence itself remains unchanged.

Useful Marea versions include:

- ferry arrival verification moving from one Lia work block to the next;
- Mirador note review moving from Ema's field observation to Nerea's analysis;
- Battle Yard maintenance note moving from Jace closeout to Sela review;
- Tideglass copy discrepancy moving from Pia preparation to Taro review.

The point is continuity of an unresolved object, not creation of a new bureaucracy.

## 13. Rest Interrupted, Plan Preserved

A field team begins a planned rest interval and an existing route/ecology state produces a legitimate interruption.

The interruption does not automatically cancel the whole expedition. The team can later choose to:

- resume a new rest interval;
- depart early;
- delay the next observation;
- hand the task to another available actor;
- return to settlement.

The system preserves the original and resumed intervals separately so AutoPTU can later judge any mechanical recovery correctly.

## Long arc: The Hours Between Shifts

This proposed Character/Settlement/Region arc makes day boundaries visible through small cumulative changes rather than a universal day-cycle quest.

Early episodes establish that people have bounded availability and that work can continue through handoffs. Later episodes show the costs and benefits of choosing a live observation, waiting for a specialist, accepting a delayed departure or relying on a record produced while the player was elsewhere.

Long-term physical and documentary traces can include:

- handoff sheets;
- corrected opening/departure notices;
- observation timestamps;
- equipment left ready for the next work block;
- a repair request noticed during closeout and completed later;
- recurring visitors who learn when a service normally becomes available;
- field plans that record an interrupted night and revised departure.

The arc should make Marea feel inhabited across time without requiring a fatigue meter or constant sleep scenes.

## Mechanically rich encounter: Pre-Dawn Camp Withdrawal at Sendero

Narrative premise:

A field party staged overnight for a legitimate early route or observation task. Before departure, one localized wild confrontation makes the immediate approach unsafe.

The full intended version could include camp-edge obstacles, a protected withdrawal lane, movement interactions, tactical environmental conditions and objective-aware behavior.

Capability dependencies for that version:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL and blocking if those interactions matter;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL when battle content uses statuses; ordinary sleeping actors are not assigned PTU Sleep status by Narrative;
- terrain/weather/hazards/zones/reactions: BLOCKING if darkness, weather, uneven ground or zones affect battle legality;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL where exact items participate;
- Trainer Features/perks: PARTIAL and content-specific;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for reliable withdrawal/corridor objectives;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for the complete camp-to-battle-to-world projection.

Full disposition: BLOCKED.

### Reduced version

The same narrative premise works now with a strict handoff.

Narrative owns:

- the camp/staging context;
- interrupted rest records;
- sleeping or off-duty noncombatants;
- equipment/custody;
- planned observation purpose;
- later schedule consequences.

Before BattleSpec, all noncombatants are already moved to a safe authored state. The battle takes place on stable geometry without tactical darkness, weather or camp interactables. Only audited combatants enter AutoPTU.

Permitted battle outputs:

- `IMMEDIATE_CAMP_APPROACH_CLEAR`
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_FIELD_TEAM_CAN_WITHDRAW`

Afterward Narrative decides whether a new rest interval begins, departure changes or the observation window is missed.

The battle cannot decide:

- PTU Rest or Extended Rest eligibility;
- HP, AP or Daily Move restoration outside engine mechanics;
- fatigue/exhaustion;
- sleep quality;
- research success;
- ecological cause;
- permanent route safety.

## Canon questions intentionally left open

No candidate here resolves:

- Caelo rest-rule variants;
- official camp facilities;
- mandatory watches;
- curfew or quiet hours;
- regional labor/rest requirements;
- exact boarding-room operators;
- how a multiplayer server handles character sleep while other players remain active;
- which time-of-day windows are ecologically important before evidence establishes them.

Promotion should happen only after those fields matter to an actual implementation slice.