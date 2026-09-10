# The Expedition Log That Survived the Storm — Pass 397

Status: PROPOSED / NON-CANON
Date: 2026-09-10

## Premise

Several short survey teams visit a newly accessible field site over consecutive days. They share one instrument because the site is difficult to reach and the institution has limited equipment.

Each checkout, return and authorized handoff creates a holder-transition event. The teams also record measurements, route notes and observations through the ordinary persistent-world evidence and knowledge systems.

A severe infrastructure outage later forces recovery from a durable world checkpoint.

The recovered holder journal proves that the instrument passed from one named surveyor to another before the selected semantic cut. The current resource catalog also proves its holder and location at that cut. Reports describing events after that cut are incomplete.

The central problem is not deciding which NPC is lying. The player must separate three classes of fact:

- events durably proven before the recovery cut;
- current state durably proven at the cut;
- later events that remain unproven until another source establishes them.

A later anomalous reading makes that distinction important.

## Possible causes of the discrepancy

The proposal does not choose one explanation automatically. Candidates include:

- a legitimate post-checkpoint handoff whose journal generation was not recovered;
- a measurement copied under the wrong expedition identifier;
- calibration drift;
- a changed environmental condition;
- a route or location mismatch;
- a delayed report;
- an actual unauthorized transfer;
- a genuine environmental anomaly.

Each requires evidence. Recovery itself never selects one.

## NPC and faction pressure

The equipment coordinator wants an accountable chain of custody.

A field researcher wants the anomalous measurement preserved rather than dismissed as bad paperwork.

A later expedition wants access to the instrument now, not after the investigation finishes.

A cautious supervisor may suspend the site until the missing interval is reconstructed.

These are role pressures, not fixed canon factions or personalities.

## Reduced implementation

The full narrative premise works without AutoPTU.

Required persistent-world pieces:

- semantic time;
- persistent NPC identity and schedules;
- explicit private knowledge and communication;
- travel/replanning;
- current `WorldResource` state;
- reservation and custody history when relevant;
- `ResourceHolderTransitionLedger`;
- `OUROS_RESOURCE_HOLDER_TRANSITION_CHECKPOINT_V1`;
- observation/evidence records for the measurements and reports.

The site can be explored through travel and interaction scenes. The weather event may occur between scenes. The player can resolve the investigation through records, interviews, a repeat measurement and comparison of recovered generations.

## Mechanically rich implementation

A later return to the site may happen while conditions deteriorate. The objective is to complete or abort a measurement, recover personnel and preserve equipment. KO is not the implicit victory condition.

Capability dependencies:

Targeting/footprints/range/LoS: needed for any tactically targeted threat or ranged protection.

Base movement legality: needed for ordinary combat-grid navigation.

Complete movement: needed for dragging, push/pull, knockback, interception, rescue reposition or forced slides.

Core calculations: needed for ordinary tactical resolution.

Action economy/initiative: needed when the expedition is resolved inside tactical time.

Full turn/round lifecycle: needed for timed measurement windows, weather phases, delayed collapse, evacuation countdowns or round-bound objectives.

Full stateful damage pipeline: needed when damage has persistent tactical consequences.

Status lifecycle: needed for complex ongoing conditions.

Terrain/weather/hazards/zones/reactions: needed for flooding, unstable ground, high wind, visibility loss, triggered hazards or reactive environmental zones.

Move-specific behavior: individually gated.

Abilities: individually gated.

Items: individually gated if the instrument or safety equipment gains PTU mechanical effects.

Trainer Features/perks: individually gated for special actions, interrupts or bonuses.

AI legal-action infrastructure: usable only inside already audited ordinary scopes.

AI tactical policy: BLOCKING for survey-first, rescue-first, protect-equipment, escort-carrier, abort-measurement, objective-aware withdrawal and disengage-after-objective behavior.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for persistent instrument identity, authoritative pickup/handoff acknowledgement, environmental objective state, timed non-KO completion and end-to-end tactical playback.

## Current engine evidence

AutoPTU-Java inspected at `ca235409e6d317055ae4afd9008bd82156b739f7`, merge #423. The merge freezes a successful combatant switch transition plan against pinned Python behavior. That is evidence for the exact outgoing/replacement presence and destination seam. It does not verify complete switching, complete movement, full lifecycle or the other capability families required by the rich version.

AutoPTU Python remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its latest change is presentation-only.

## Long-term arc potential

If promoted later, repeated measurements from several temporary-access sites could reveal a regional pattern. Early missions would remain useful because their provenance, holder sequence and observation time are durable. New information can reinterpret old observations without rewriting them.

The player could eventually decide whether the pattern is environmental, institutional, technical, ecological or something else. This proposal does not establish that answer.

## Canon questions left open

No site identity is approved.

No institution or survey program is approved.

No instrument type is approved.

No weather event, anomaly, faction, NPC or species is approved.

No PTU Skill, Edge, Trainer Feature, Item or environmental rule is granted by this proposal.
