# Engine Readiness Snapshot — Pass 153

Status: LIVE EVIDENCE SNAPSHOT
Narrative head before pass: `992fe55758dc4222f6b92cbd9971a558d5f3352c`
Date: 2026-08-30

## Read-only engine heads inspected

AutoPTU-Java:

`c5b2a34ff23887770268bfe4108dfc86e9a796fb` — `Compose Intercept position from server-owned Shift legality (#288)`

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

No files in either engine repository were modified by Pass 153.

## Conservative interpretation of current evidence

The AutoPTU-Java head provides concrete evidence that Intercept-position composition uses server-owned Shift legality rather than allowing an adapter to supply arbitrary tactical destinations. This is positive evidence for a bounded part of Intercept and base movement authority.

It does not establish the complete movement family. In particular, Pass 153 does not infer global completeness for:

- Push;
- Pull;
- Knockback;
- every Intercept variant;
- arbitrary forced movement;
- escort movement;
- object carrying;
- moving platforms;
- environmental displacement;
- generalized reaction ordering;
- dynamic crowd movement;
- protect/capture/withdraw objective semantics.

The AutoPTU head remains presentation-side evidence only and does not justify promoting tactical capability families.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No category is promoted by Pass 153.

## Pass 153 encounter matrix

### Procession Route Evacuation Corridor — full version

Required families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when crowd lanes/hazards/reactions are active
- move-specific behavior — PARTIAL, individual audit required
- abilities — PARTIAL, individual audit required
- items — PARTIAL, individual audit required
- Trainer Features/perks — PARTIAL, individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Overall: BLOCKED for intended rich form.

Reduced form: READY at narrative-contract level if the BattleSpec uses only individually verified combat content. Participants and ritual objects are outside battle state; geometry is static; only immediate route clearance is returned.

### Venerated Site Threshold Perimeter — full version

Primary blockers:

- tactical policy for differentiated protect/block/withdraw behavior;
- terrain/weather/hazards/zones/reactions when site mechanics are active;
- incomplete lifecycle/state pipelines depending on selected combat content;
- adapter/playback for authoritative realization.

Overall: BLOCKED.

Reduced form: READY with fixed terrain and explicit roster. The battle cannot decide ritual validity, metaphysical status, ownership, historical authenticity, or extraordinary-Pokémon presence.

### Pilgrim Pass Chokepoint — full version

Primary blockers:

- complete movement for escort/displacement/rescue cases;
- weather/hazards/zones/reactions when pass conditions are tactically active;
- AI tactical policy for escape/protect/deny-route goals;
- adapter/playback.

Overall: BLOCKED.

Reduced form: READY. Travelers wait outside BattleSpec; the fight clears an immediate static approach; Travel/Expedition resumes afterward.

### Processional Standard Handoff Perimeter — full version

Primary blockers:

- generic object carry/handoff tactical semantics are not globally verified;
- complete movement remains PARTIAL;
- lifecycle depends on intended timing;
- AI tactical policy remains BLOCKING;
- reactions may be required by intended contest;
- adapter/playback remains BLOCKING.

Overall: BLOCKED.

Reduced form: READY. Material custody is frozen outside battle state and the fight can clear only the handoff approach.

## Narrative authority implications

Pass 153 introduces no tactical authority into Narrative.

Ouros remains authoritative for:

- tradition identity;
- practice history;
- observance scheduling and occurrence;
- attributed community meaning;
- route/site cultural association;
- extraordinary-Pokémon claims and their evidence status;
- world facts about participants before/after a battle;
- whether an interrupted observance resumes;
- canon truth about history or metaphysics.

AutoPTU remains authoritative only for tactical facts actually inside the BattleSpec and supported by verified/currently audited mechanics.

Minecraft/Cobblemon/Craftics can present the results but cannot decide participant roster, battle legality, PTU HP/status, ritual success, supernatural effects, historical truth, Legendary presence, or aftermath.

## PTU/Caelo unresolved mechanics

Keep UNKNOWN unless project-approved source evidence and current contracts verify them:

- universal religion system;
- universal ritual subsystem;
- pilgrimage completion rules;
- divine favor or prayer mechanics outside explicit Features/Moves/Abilities;
- prophecy mechanics;
- automatic sacred terrain;
- ritual-based stat bonuses;
- generic shrine defenses;
- universal Legendary knowledge;
- automatic Legendary encounter/capture entitlement;
- morality/alignment mechanics;
- ritual-authenticity Skill Checks;
- species/Type/Move/Ability conferring sacred authority by flavor alone;
- processional escort rules;
- generic object carry/handoff combat rules;
- ritual interruption/restart timing rules.

## Canon questions opened by Pass 153

- Which Ouros communities maintain living pilgrimage or processional traditions?
- Which traditions are seasonal, dormant, revived, or contested?
- Which sites have cultural importance without confirmed supernatural status?
- Which extraordinary Pokémon are only traditional associations, and which have direct canon evidence?
- Which material anchors have long continuity of role despite replacement of the physical object?
- Which regional traditions have multiple legitimate variants?
- Which public institutions document, sponsor, regulate, or commercialize traditions?
- Which routes changed because of ecology, disasters, transport, borders, or settlement growth?
- Which historical uncertainties should remain permanently unresolved?
- Which PTU occult mechanics, if any, are approved in Ouros and already supported by engine contracts?

## Pass conclusion

The new narrative concepts can progress today through reduced tactical contracts without duplicating missing PTU rules in Minecraft/Cobblemon. Rich escort, crowd-pressure, weather/hazard, reaction, object-handoff, and objective-aware versions remain explicitly gated by their actual capability families.
