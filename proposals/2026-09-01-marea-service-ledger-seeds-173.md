# Marea Interior Service Ledger Seeds — Pass 173

Status: PROPOSED / NON-CANON
Date: 2026-09-01

These are original Ouros candidates built on the fixed Marea Interior map and resident network. They are not canon until reviewed.

## Candidate: The Bruma Service Ledger

Puerto Bruma does not create a new adventurer guild. Existing institutions expose a shared service layer through several physical surfaces:
- Field Office dispatch board;
- Market Hall service ledger;
- ferry notice slate;
- Tideglass circulation desk;
- repair-row intake board.

Each surface shows only requests that plausibly reached that institution. The player can review them from the physical site. A future journal/UI may aggregate already-known requests, but the authoritative source remains the underlying world state and issuer knowledge.

Why this fits Marea:
The district already has actors whose jobs naturally generate small requests. Mara coordinates reports. Lia manages arrivals. Ivo buys supplies. Taro and Pia move documents. Teo handles equipment. Nerea and Ema rely on instruments and observations. Brin manages dispatch records. No new organization is needed.

## Seed 1 — The Wrong Crate at Bruma Market

Issuer: Ivo Serrat
Supporting actors: Brin Havel, Lia Morn
Sites: Bruma Market Hall, ferry landing, Loma storehouse
Questline tags: SETTLEMENT / FACTION / CHARACTER / ITEM

Premise:
A crate marked for Market Hall contains the correct general category of goods but carries a lot reference that does not match Brin's dispatch copy. Ivo refuses to treat a label mismatch as theft or sabotage.

Possible player work:
- inspect the visible crate label and market receiving note;
- ask Lia which consignment was physically unloaded;
- obtain Brin's dispatch copy;
- return with a reconciled account.

Durable outputs:
- corrected provenance chain;
- actor knowledge changes;
- possible later evidence for Thin Delivery Season;
- relationship history with Ivo/Lia/Brin.

No tactical dependency required.

## Seed 2 — Pia's Three Stops

Issuer: Pia Min
Supporting actors: Nerea Sol, Ema Rey, Teo Lark
Route: Tideglass -> Sendero -> Mirador -> return route
Questline tags: CLASS / EXPLORATION / EQUIPMENT / RELATIONSHIP

Premise:
Pia has archive copies for Mirador. Teo has already serviced one instrument that should return to the station. Ema has a field-note packet that belongs in Tideglass. If all three requests exist at the same time, the player's journal can present them as one compatible route bundle.

The story value is logistical coherence. The player experiences three residents as part of one working network rather than three quest markers.

No tactical dependency required unless an independent route encounter occurs.

## Seed 3 — The Crossing Report Nobody Agrees On

Issuer: Mara Veyra
Supporting actors: Mina Cors, Ema Rey
Sites: seasonal crossing, Estación Mirador
Questline tags: REGION / EXPLORATION / FACTION

Premise:
Mina says the crossing looked usable from the lower route. Ema's older observation says the upper shelf was unstable. Neither report is necessarily false because they were made at different times and from different positions.

Player work:
- revisit the crossing;
- record current observable conditions;
- identify which parts of the earlier reports remain valid;
- return without converting uncertainty into accusation.

Narrative purpose:
Teaches the Ouros evidence model through ordinary field work.

No tactical dependency required.

## Seed 4 — Jace Wants the Yard Ready

Issuer: Jace Orrin
Supporting actors: Sela Orrin, Teo Lark
Site: Bruma Battle Yard
Questline tags: RIVAL / COMPETITIVE / EQUIPMENT / RELATIONSHIP

Premise:
Jace wants an evening training slot, but one boundary fixture is visibly damaged. Sela will not open the marked lane until it is checked. Teo needs an inspection note before deciding what work is required.

Player work:
- inspect several physical yard anchors;
- identify the damaged fixture;
- bring the note to Teo;
- return later after repair state changes.

A later formal battle can happen, but battle victory is not the repair objective.

No tactical dependency for the service request. Any battle uses the ordinary audited battle contract separately.

## Seed 5 — Stranded Survey Crew

Issuer: Marea Field Office
Supporting actors: Nerea Sol, Ema Rey, Oren Vale
Site: upper Sendero/Mirador branch
Questline tags: CRISIS / EXPLORATION / CLASS / REGION

Premise:
A small survey team reports that a local wild group has become difficult to pass after a route disturbance. The immediate need is to create enough safe space for the crew to withdraw. The cause of the Pokémon behavior remains unknown.

Full tactical version:
Crew members are battlefield objectives moving through a withdrawal corridor while hostile/agitated Pokémon contest space.

Required capability families:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL when used;
- terrain/weather/hazards/zones/reactions — BLOCKING if route instability affects battle;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING as complete family.

Full version status: BLOCKED.

Reduced version:
The crew remains outside BattleSpec. The player reaches an authored encounter at the route edge. One ordinary battle is compiled only after every selected Move, Ability, Item and Feature is individually audited. An authoritative win can emit `IMMEDIATE_WITHDRAWAL_CORRIDOR_CLEAR`; the crew then withdraws through narrative world state.

Reduced version status: potentially READY after exact combat audit.

Important consequence:
Neither version proves why the wild group changed behavior. That remains a separate ecology/investigation thread.

## Seed 6 — The Clinic Has No Public Patient List

Issuer: Oren Vale
Supporting actor: Jo Venn
Sites: clinic, field school
Questline tags: SETTLEMENT / CARE / CHARACTER

Premise:
Oren needs routine prevention material delivered to Jo's field-school session. The public request describes quantities and destination but contains no patient names, diagnoses or private case history.

Purpose:
Builds clinic presence into ordinary life while preserving the repository's care/privacy boundary.

No tactical dependency.

## Seed 7 — Ferry Slate Changed Since Morning

Issuer: Lia Morn
Supporting actor: Mina Cors
Site: ferry landing
Questline tags: TRANSPORT / SETTLEMENT / SERVER_EVENT

Premise:
A ferry departure changes because of explicit service or route state. A previously available package request becomes superseded rather than failing the player arbitrarily.

Player-facing lesson:
The board is live world state. Requests can change because the world changed.

No invented weather penalties, speed math or transport capacities. Any reason for the schedule change must already exist in authoritative world state.

## Promotion criteria

Before any seed becomes canon:
- confirm it does not contradict the fixed Marea map/resident canon;
- connect every issuer/site to canonical IDs;
- decide which dispatch surfaces physically exist;
- define world-state records for posting/acceptance/supersession;
- validate any combat participant and exact PTU mechanic against current sources/runtime;
- keep rewards separate until economy/progression authority is explicitly mapped;
- ensure request completion writes at least one meaningful durable consequence beyond generic payout.
