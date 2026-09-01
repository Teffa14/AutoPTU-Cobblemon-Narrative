# Marea Language, Script & Interpretation Seeds — Pass 177

Status: PROPOSED / NON-CANON
Date: 2026-09-01
Depends on: `design/language-script-translation-interpretation-layer.md`

These seeds use only already-canonized Marea sites and residents unless explicitly marked otherwise. They do not canonize a new language, ancient civilization, Unown population, supernatural communication ability or family relationship.

## 1. The Margin Nobody Agrees On

Anchor: Tideglass Archive
Residents: Taro Min, Pia Min, Dr. Nerea Sol

A copied route survey contains a recurring margin symbol. One archive edition treats it as a warning marker. Another old copy places the same symbol beside routine measurements.

Player work:
- inspect two physical editions;
- distinguish original notation from later annotations;
- retrieve a third parallel example from Mirador records;
- document which interpretation is better supported.

Possible outcomes:
- `INTERPRETATION_WARNING_WEAKENED`
- `INTERPRETATION_SURVEY_SHORTHAND_SUPPORTED`
- `AMBIGUITY_REMAINS`

No single roll resolves the question.

Mechanical dependency: world/dialogue/archive only. No battle dependency.

## 2. Four Hands on One Marker

Anchor: Sendero del Vidrio
Residents: Mara Veyra, Taro Min, Ema Rey

A route marker has four visible layers: an older carved mark, a later survey notch, weathering, and a recent maintenance paint line.

The player must identify which physical layer each claim refers to before Mara can decide whether an operational warning is current.

Design value:
- teaches palimpsest/layer provenance;
- connects field observation to archive comparison;
- prevents an old warning from being mistaken for a present closure.

Mechanical dependency: base world interaction only.

## 3. Dock Signals in Bad Weather

Anchor: ferry landing
Residents: Lia Morn, Mina Cors, Pia Min

The ferry crew uses a small set of practical hand/flag/light signals during noisy unloading windows. A copied public guide omits one context qualifier, creating confusion between `WAIT` and `BERTH NOT READY`.

Player work:
- observe normal operations;
- compare the dock guide with Lia's current procedure;
- identify the missing context;
- deliver a corrected copy to Tideglass/public board if approved.

This does not canonize a formal sign language. It is an operational signal set.

Mechanical dependency: world-state and communications layer only.

## 4. Mirador Notation Drift

Anchor: Estación Mirador
Residents: Nerea Sol, Ema Rey, Jo Venn

Older field sheets and current field-school sheets use slightly different abbreviations. A student copied an old symbol literally and attached the wrong modern meaning.

The player can help build a crosswalk table while preserving both systems in the archive.

Consequences:
- selected old observations become easier to compare with current data;
- no historical measurements are rewritten;
- Jo can teach the distinction later.

Mechanical dependency: no battle.

## 5. Redline's Delivery Copy

Anchor: Tideglass Archive -> ferry landing -> Marea Field Office
Resident: Pia Min

Pia carries a corrected edition of a route notice. The old wording is still physically posted at one location because the replacement has not arrived yet.

The quest tests:
- edition identity;
- delivery state;
- supersession without history deletion;
- actor knowledge lag.

Player choice is operational: carry the corrected copy directly, confirm the old copy was removed, or let ordinary delivery complete later.

Mechanical dependency: no battle.

## 6. The Sound at the Crossing

Anchor: seasonal crossing
Residents: Mara Veyra, Nerea Sol, Ema Rey

Several people describe a recurring call/noise near the crossing with different written approximations. The proposal deliberately avoids deciding whether it is Pokémon vocalization, equipment resonance, water flow or another source.

Player work:
- record time/location/weather context;
- compare several observations;
- avoid merging different sounds into one phenomenon;
- place only supported claims into the evidence graph.

Possible escalation remains a separate proposal after source/mechanical review.

Mechanical dependency: world observation only in reduced form.

## 7. Companion Signal Notebook

Anchor: field school / selected resident workplaces
Residents: Jo Venn plus existing NPC/partner pairs

Jo proposes a teaching exercise in which residents record repeated, observable partner behaviors and the context in which they occur.

Guardrails:
- entries say `observed behavior` and `resident interpretation` separately;
- familiarity does not become perfect translation;
- no species-wide meaning is inferred from one partner;
- no Telepath/Channeler mechanics are assumed.

Examples of safe records:
- partner approaches a specific workstation before a routine task;
- partner repeats a posture when a familiar route is blocked;
- resident interprets a behavior as requesting attention, with confidence noted.

Mechanical dependency: relationship/world state only.

## 8. The Broken Copy

Anchor: Loma Clara field school / Tideglass
Residents: Jo Venn, Pia Min, Taro Min

A teaching copy of an older route document has a torn edge. Students have filled the missing phrase differently over the years.

The player can locate another edition and mark which letters are observed versus restored.

Narrative purpose:
- turns document criticism into ordinary local activity rather than ancient-prophecy spectacle;
- gives Tideglass practical social value;
- teaches the player the same provenance grammar used later for larger mysteries.

Mechanical dependency: no battle.

## 9. Signal Under Pressure

Anchor: future Sendero encounter space
Status: MECHANICALLY RICH / NOT READY FOR FULL VERSION

Premise:
A Pokémon group repeatedly produces a recognizable signal during a dangerous route incident. A qualified character may eventually interpret the signal as connected to a safe corridor or protective behavior.

Full intended version may include:
- active combat positions affecting signal visibility;
- interception or forced movement near a corridor;
- environmental hazard phases;
- an exact communication-related Trainer Feature or Pokémon capability;
- mid-round objective changes after a successful authoritative resolution;
- tactical AI responding to the same world state.

Required permanent capability families:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle if selected Moves require it;
- terrain/weather/hazards/zones/reactions;
- exact move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Current status: BLOCKED for full version.

Reduced executable version:
- signal observations happen before combat from safe observation points;
- Nerea/Mara can create a provisional claim from repeated observations;
- any combat is a separate ordinary audited BattleSpec on stable terrain;
- no signal changes legal actions mid-round;
- no dynamic hazard, escort or forced movement is required;
- victory may permit additional observation but cannot establish intent or translation.

## 10. Tideglass Interpretation Desk

Anchor: Tideglass Archive
Residents: Taro Min, Pia Min
Status: institutional candidate, not canon

Instead of creating a new faction, Tideglass can expose a small workflow surface for interpretation requests using its existing archive role.

Candidate workflow:
1. source object/copy registered;
2. transcription attached;
3. known parallels linked;
4. one or more interpretations recorded;
5. field verification request optionally created through existing dispatch;
6. corrected edition published through existing communications layer.

This is a workflow proposal inside the existing institution, not a new organization.

## Recommended first implementation

Best low-risk seed: `The Margin Nobody Agrees On`.

Why:
- uses only canon residents and locations;
- directly exercises archival editions, evidence provenance and actor-knowledge correction;
- requires no new battle capability;
- can be represented with physical quest objects now that the RPG adapter has proven persistent server-owned quest-object provisioning;
- teaches the player a system that later scales to larger ruins/mysteries.

Second choice: `Dock Signals in Bad Weather`, because it adds everyday nonverbal communication without supernatural assumptions.

## Canon boundary

None of these seeds establish:
- an ancient Ouros language;
- a Marea dialect;
- Unown presence;
- telepathic NPCs;
- a universal Pokémon language;
- new resident ancestry/family relations;
- hidden ruins at Marea;
- a finalized historical reading.

Promotion requires explicit canon review.