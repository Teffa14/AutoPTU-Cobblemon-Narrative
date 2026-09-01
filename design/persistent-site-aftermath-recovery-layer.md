# Ouros Persistent Site Aftermath & Recovery Layer

Status: DESIGN / NON-CANON ARCHITECTURE
Date: 2026-09-01
Research basis: `research/2026-09-01-persistent-aftermath-site-recovery-scan-176.md`

## Purpose

Define how an authored incident can leave persistent physical consequences at an Ouros location, how custodians respond over time, and how later visits observe repair, recovery, repurposing or retained traces.

This layer does not create a second quest, dispatch, claim, public-memory, calendar, evidence or communications system. It supplies a physical-site continuity contract that those existing systems can reference.

## Existing ownership remains

- canonical location identity and anchors: existing world-map/location catalogues;
- incidents, observations, evidence, claims and hypotheses: existing investigation/world-agency layers;
- actor knowledge and claim posture: `design/local-knowledge-claim-propagation-layer.md`;
- information packets/publication/corrections: existing communications layer;
- work requests: existing mission/service-dispatch layers;
- calendar progression: existing calendar/world-time layer;
- public historical persistence: existing public-memory layer;
- battle outcome: AutoPTU authoritative battle result only;
- Minecraft/Cobblemon blocks/entities/particles: presentation projection only.

This layer owns the authored physical and operational condition of a canonical site across time.

## Core continuity model

`AUTHORED INCIDENT OR ORDINARY DEGRADATION`
`-> CANONICAL SITE-CONDITION FACTS`
`-> OBSERVABLE WORLD MARKERS`
`-> CUSTODIAN ASSESSMENT`
`-> RESTRICTION / WORK PLAN / NON-ACTION`
`-> INTERMEDIATE SITE CONDITION`
`-> REPAIR / RECOVERY / REPURPOSING`
`-> LATER OBSERVABLE STATE`
`-> ARCHIVE / PUBLIC MEMORY / NEW CLAIMS`

The player may influence several transitions, but quest completion is not itself the authority that changes every dimension.

## Site condition should be dimensional

Do not model a location with one scalar such as `site_health = 65`.

A site-condition record can reference independent dimensions such as:

```yaml
site_condition:
  site_id: null
  effective_from: null
  caused_by_event_ids: []
  accessibility: NORMAL
  operability: NORMAL
  physical_condition: SERVICEABLE
  ecological_condition: BASELINE_UNKNOWN
  custody_status: NORMAL_CUSTODY
  active_restriction_ids: []
  visible_marker_ids: []
  outstanding_work_ids: []
  supersedes_condition_id: null
  evidence_record_ids: []
```

The values above are illustrative design vocabulary, not canon enums.

Important separation:

- `physical_condition` answers what is materially true;
- `accessibility` answers where actors can currently go;
- `operability` answers what function can be performed;
- `ecological_condition` records ecology only when supported by observations/canon;
- `custody_status` answers who has authority/responsibility;
- claims/public memory answer what people think happened.

## Candidate presentation phases

A site may pass through some of these phases:

- disrupted;
- restricted;
- stabilized;
- under repair;
- recovering;
- reopened with retained trace;
- repurposed;
- decommissioned.

These are presentation/design phases, not a mandatory state machine. A site may skip phases or occupy different states on different dimensions.

## Observable markers

Persistent state needs concrete player-facing evidence. Examples:

- barrier, rope, sign or closed gate;
- temporary detour;
- patched roof or replaced boards;
- stacked removed material;
- numbered survey markers;
- instrument under calibration;
- empty berth or altered loading lane;
- scaffold/work table;
- replanted strip at an earlier disturbance;
- archived image or condition report;
- visibly mismatched replacement material;
- old fixture retained beside its replacement.

A marker is presentation. Its destruction or unload in Minecraft cannot silently mutate canonical recovery state.

## Custodian rule

Every non-trivial site transition requires an authored custodian, responsible institution or world process.

Examples already supported by Marea canon:

- Lia coordinates ferry landing operations;
- Mina operates ferry routes and supplies practical observations;
- Mara coordinates field reports and route checks;
- Teo maintains ordinary tools, lamps, carts and instruments;
- Nerea and Ema own scientific observation/field protocols at Mirador;
- Taro and Pia own archive handling/circulation responsibilities;
- Sela and Jace maintain ordinary Battle Yard fixtures;
- Brin manages cooperative storage records;
- Alba represents one producer voice rather than the whole cooperative.

The player can help. Assistance does not transfer institutional authority.

## Work progression

Recovery work should be decomposable into world facts rather than one completion flag.

Example:

`hazard reported`
`-> access restricted`
`-> assessment completed`
`-> temporary path marked`
`-> material delivered`
`-> stabilization work completed`
`-> inspection completed`
`-> route reopened`
`-> follow-up observation scheduled`

Any of these can create existing dispatch tasks, information packets or claims. The aftermath layer stores the site-facing consequence, not duplicate workflow objects.

## Autonomous world work

The player is not required to witness every labor step.

When ordinary work has:

- a responsible actor/institution;
- required inputs already available;
- no player-specific dependency;
- an authored duration or next-check time;

calendar progression may advance it while the player is elsewhere.

Return visits should read current canonical state and project it visibly.

## Retained-trace principle

Restoration should not imply amnesia.

When narratively useful, a recovered site can retain evidence through:

- patched construction;
- changed route alignment;
- permanent monitoring marker;
- retired component kept for teaching;
- archive record;
- revised operating procedure;
- NPC schedule change;
- new maintenance obligation;
- changed ecological use.

The trace can later fade if canon says it does. It should not vanish merely because a quest flag reached `COMPLETE`.

## Repurposing and succession

Recovery can produce a new use rather than restore the old one.

Possible design outcomes:

- former equipment space becomes observation storage;
- damaged route segment becomes a monitored no-through zone while a new path carries traffic;
- obsolete structure becomes habitat that institutions decide not to remove;
- replaced fixture becomes a field-school demonstration object;
- unused dock space becomes a temporary archive intake point during another disruption.

Any ecological claim requires evidence and canon review. The system must not infer habitat value from the presence of a Cobblemon entity.

## Information integration

Physical truth and public understanding remain separate.

Example:

- canonical fact: upper route section is restricted pending assessment;
- Lia knows only that deliveries are delayed;
- Mara has the route report;
- Nerea has measurements;
- a public notice says the route is closed;
- a rumor claims a Pokémon caused the damage.

The site-condition layer owns only the restriction and physical facts. Existing claim/communications layers own interpretations and dissemination.

## Quest and service-dispatch integration

A work request may point to:

- `site_id`;
- current condition record;
- required observation or work milestone;
- issuer/custodian;
- retirement condition.

Completing a request can submit evidence or a work result. The site transition occurs only through the authored world-state rule that consumes that result.

This prevents `QUEST_COMPLETE -> SITE_PERFECT` shortcuts.

## Battle handoff boundary

A battle result can change site aftermath only through a narrow, explicit handoff.

Allowed examples:

- `IMMEDIATE_THREAT_WITHDREW` permits assessment to resume;
- `WORK_CORRIDOR_TEMPORARILY_CLEAR` permits a crew to enter;
- an authoritative capture/removal result changes presence of the exact battle participant when canon allows it.

Disallowed automatic conclusions:

- victory repaired structural damage;
- defeating a Pokémon proves it caused an incident;
- winning authorizes reopening;
- battle damage becomes canonical building damage without an authored world-event bridge;
- Cobblemon knockback alters canonical terrain;
- entity despawn means threat resolved.

## Mechanically rich pattern: The Shelf After the Slide

Status: DESIGN EXAMPLE / NON-CANON

Narrative premise:
A section of an established route has fresh physical disruption. The player assists assessment and recovery while the route remains part of daily district life.

### Intended full version

Potential sequence:

1. route restriction is already canonical before entry;
2. player receives an evidence-preserving inspection task;
3. unstable cells, loose material or shifting access influence tactical positioning;
4. if a wild encounter occurs, player and Pokémon must maintain safe movement while preserving the exit corridor;
5. later stabilization, repair and reopening happen through custodial/world-state progression;
6. later visits show recovery markers rather than an instant reset.

Exact dependency families if those mechanics are used:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle when selected Moves/statuses require it;
- terrain/weather/hazards/zones/reactions for unstable cells, moving debris, slope zones, weather effects or reaction movement;
- move-specific behavior for every selected Move;
- abilities for every selected Ability;
- items for every battle-relevant Item;
- Trainer Features/perks for every selected interrupt/modifier;
- AI legal-action infrastructure;
- AI tactical policy if non-scripted opponents must choose safe/legal tactics;
- Minecraft/Cobblemon/Craftics adapter/playback support for faithful presentation.

Do not infer readiness of one family from a representative fixture in another.

### Reduced version

Keep the same narrative premise without tacticalizing the unstable slope.

- site restriction, debris and recovery remain server-authored world facts outside BattleSpec;
- inspection uses fixed authored observation points and safe route segments;
- no moving civilian/crew is a combat participant;
- no unstable-cell, falling-debris, weather, reaction or forced-movement objective is compiled;
- if a battle is required, it occurs on a bounded stable clearing as a separate encounter after exact Moves, Abilities, Items and Features are audited against current engine contracts;
- battle result may emit only `IMMEDIATE_WORK_CORRIDOR_CLEAR` or equivalent narrow handoff;
- slope cause, structural safety, reopening and long-term recovery are decided by non-battle world-state logic.

This reduced form allows the narrative arc to ship before the richer tactical families are complete.

## Current engine-readiness boundary

Read-only evidence checked in this pass:

AutoPTU-Java head: `7cbc5aafb50a5221d4493518297f24ff3e4a960a`.

Newest change freezes a composite forced-movement prevention guard, building on the prior Shadow Tag candidate-step constraint work. This strengthens one part of forced displacement. It does not prove all push, pull, knockback, interception, collision, partial-stop or arbitrary forced-movement behavior.

Conservative category classification for narrative gating:

VERIFIED for currently covered contracts:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING when a concept requires the complete family:
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

`Teffa14/AutoPTU` current visible head remains presentation/Career oriented (`729bae2d424963ff9bb3f4159c9a7ac9152128a7`) and supplies no new evidence that promotes these tactical categories.

## Validation targets

Future data/startup/CI validation should reject:

- site-condition records referencing missing sites;
- recovery transitions with no authorized trigger;
- work completion that silently mutates unrelated dimensions;
- presentation entities/blocks writing canonical site state directly;
- a battle outcome mapped to consequences broader than its explicit handoff;
- ecological recovery claims based only on spawned entity presence;
- reopening while an authored blocking restriction remains active;
- circular supersession of condition records.

## Canon boundary

This architecture can be implemented without canonizing any specific disruption. Marea's fixed coordinates, residents, relationships and current roles remain unchanged.