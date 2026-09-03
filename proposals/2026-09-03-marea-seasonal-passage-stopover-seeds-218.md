# Marea seasonal passage and stopover seeds — pass 218

Status: PROPOSED / NON-CANON
Date: 2026-09-03

## Canon boundaries

This proposal reuses established Marea route, Sendero del Vidrio, seasonal-crossing and institutional roles without canonizing a new species, migration calendar, breeding ground, disaster, road closure or second wild population. It preserves the existing first persistent Sendero Fletchling identity and does not assume that individual participates in any future passage event.

The passage population remains deliberately unspecified until species provenance and local canon are approved.

## Narrative premise

A seasonal passage should alter how an existing route is used rather than replace the route with a temporary dungeon. People still need deliveries, fieldwork and ordinary travel while a population uses the same terrain for directional movement or a short stopover.

The useful conflict is operational: when to yield space, how to count what is happening, when a detour is justified, what evidence supports a restriction, and what happens if the animals change their route.

## Seed: The Crossing Becomes a Bottleneck

Nerea accumulates several observations suggesting directional movement through the Sendero seasonal crossing during a bounded period. The evidence can be direct passage, repeated traces, calls, camera/field observations or corroborated records from multiple points.

Mara must decide whether ordinary route use can continue, should be slowed, should temporarily yield during a passage pulse, or needs a stronger restriction. Lia's delivery responsibilities create a legitimate competing need without making her anti-wildlife.

The player can help establish whether the crossing is actually functioning as a bottleneck and whether a restriction would protect a real passage or merely respond to one unusually large local concentration.

No restriction is justified by headcount alone.

## Seed: Count Without Owning the Count

A field count at the crossing records more Pokémon than expected. The first temptation is to call that number the local population size.

The player can compare direction, timing, repeated sightings, recognizable individuals where identity is genuinely available, observation effort and a second checkpoint. The final record keeps raw observations separate from abundance estimates.

A good outcome can therefore be “we know at least this many passages occurred, but not how many unique individuals crossed.” That uncertainty remains useful data rather than a failed quest.

This seed gives Nerea a scientific role, Mara an operational one and the player a reason to revisit connected sites without creating another combat chain.

## Seed: The Stopover Moves

A site used during an earlier passage window receives much less use in the next one. A nearby site shows new evidence.

Possible explanations remain open: disturbance, food/water availability, changed route geometry, weather context, observation error, altered human activity or normal variation. The player can inspect both sites and reconstruct what changed without being promised a hidden culprit.

If human activity contributed, consequences can be practical. A delivery schedule might be adjusted, an observation position relocated, or a temporary buffer proposed. No universal distance or tolerance value is authored until species/population evidence supports it.

## Seed: A Familiar Individual Joins the Flow

This seed is gated and may never become canon.

If the authoritative state of the first persistent Sendero Fletchling eventually places that individual within a passage event, the player may recognize it among other wild actors. The recognition creates continuity, not ownership or a new species law.

Its participation proves only that this individual was observed moving with the passage at that time. It does not prove that the lower-shelf population is migratory, that all Fletchling use the corridor, or that the individual will follow the same route next season.

The generic Cobblemon population projection must not duplicate the persistent actor when this happens.

## Seed: Route Closure Has a Cost

Mara considers a temporary restriction during a narrow passage pulse. The ecological benefit may be real, but so are the costs to deliveries, inspections and residents who use the route.

The player can gather enough evidence to support a narrower window, a one-way human flow, a detour, observation-only access, no restriction, or a stronger closure if facts justify it. The final choice should persist in route/access records and affect later schedules.

A later migration shift can make last year's correct policy wrong this year. Institutions need revision history rather than eternal quest-state switches.

## Seed: Passage Without Battle

A visible group crosses while the player is nearby. Some individuals tolerate the Trainer, others increase distance, and another may warn or withdraw according to species/population context and individual state.

The player can stand clear, move out of the route, observe, follow at distance, attempt an authorized approach, or deliberately interfere. Each action becomes information for the behavioral policy.

A population moving together does not automatically become one combat unit. A Trainer that alarms one individual does not automatically aggro every visible Pokémon. Signal propagation, direct perception and individual legal options remain separate.

## Mechanically rich encounter: Seasonal Passage at the Narrow Shelf

Working title only. Species, exact window and group size remain unresolved.

### Intended full version

A passage pulse overlaps routine human use of the seasonal crossing. The party's primary objective is observational/operational: maintain a usable safe lane, avoid unnecessary escalation, gather reliable passage evidence and respond if one actor becomes blocked, injured, alarmed or intentionally interfered with.

The full version may use authoritative footprints/range/LoS; ordinary and special movement; independent wild behavior states; Trainer approach tactics; verified Stealth/handling/Features/Edges; capture or hindrance attempts; Status application; Moves/Abilities/Items that modify movement or perception; interception/forced movement when exact contracts permit; bounded hazards where actually authored; action economy and lifecycle if a structured encounter begins; AI legal actions plus tactical policy for autonomous participants; and semantic adapter events for Minecraft/Cobblemon/Craftics.

The central rule is that a passage objective remains distinct from battle victory. Defeating one Pokémon does not complete migration, clear a route, prove a count or authorize a closure. A passage can succeed narratively with zero combat.

### Reduced version: Watch, Yield, Record

The reduced version uses world/runtime capabilities that can arrive earlier.

Ouros holds a provenance-backed passage episode, site/route references, current access decision and observation records. Cobblemon handles ordinary generic world Pokémon availability where native spawn conditions can express the approved profile. The player traverses normally, receives observable passage cues, chooses whether to yield or withdraw, and creates field observations with timestamps/direction/count methodology.

If a persistent individual is present, only its authoritative identity state can project it. If an actual battle begins, participants enter through the normal frozen BattleSpec authority path.

This reduced form does not require group combat AI, forced movement, reaction attacks, status-based capture control, weather phases, migration bonuses, invented low-light rules or participant insertion into an already-running battle.

## Engine capability dependencies

| Permanent capability family | Need in intended full version | Current boundary |
| --- | --- | --- |
| targeting / footprints / range / LoS | Required for route occupancy, observation and spatial interaction | VERIFIED inside audited contracts; world-to-battle geometry mapping still needs adapter support |
| base movement legality | Required | VERIFIED inside audited contracts |
| complete movement incl. push/pull/knockback/interception/forced movement | Conditional when actors block, intercept or displace others | PARTIAL; bounded prevention cases do not complete the family |
| core calculations | Required for source-verified checks/capture/battle calculations | VERIFIED inside audited contracts; no invented migration modifier |
| action economy / initiative | Required once the scene becomes structured | VERIFIED inside audited contracts |
| full turn/round lifecycle | Required for a complete structured tactical encounter | PARTIAL |
| full stateful damage pipeline | Conditional if attacks/injury occur | PARTIAL |
| status lifecycle | Conditional if Status is used for control/capture | PARTIAL |
| terrain/weather/hazards/zones/reactions | Conditional for actual hazards, weather effects, zones or reactions | PARTIAL/BLOCKING outside bounded tile-entry trap contracts |
| move-specific behavior | Required for Move-based control, escape or support | PARTIAL |
| abilities | Required when an Ability affects movement/behavior/mechanics | PARTIAL |
| items | Required for Balls or other meaningful equipment | PARTIAL |
| Trainer Features/perks | Required for Feature/Edge changes to observation, approach, capture or control | PARTIAL |
| AI legal-action infrastructure | Required for autonomous actors | VERIFIED inside audited contracts |
| AI tactical policy | Required for competent independent decisions across a moving group | BLOCKING as a complete family |
| Minecraft/Cobblemon/Craftics adapter/playback | Required for population projection, movement cues, persistent identity and semantic playback | PARTIAL/BLOCKING end-to-end |

## World-runtime and spawn boundary

Migration state remains outside the 16 battle families. The runtime needs passage identity, route/stopover references, season/window provenance, observation timestamps, access policy, population projection rules and persistence across unload/reload/multiplayer.

Cobblemon should continue to own ordinary natural spawn eligibility and weighting wherever its native conditions can represent the approved availability. Ouros should not build a second spawn engine. Ouros supplies the authored passage semantics and may gate/provide persistent identities where generic spawning cannot represent them.

The deployed Cobblemon version must be checked before assuming a native calendar-season condition. Day/night support from pass 216 does not prove arbitrary seasonal scheduling.

## PTU/Caelo/Kairos audit queue

Before the full encounter is mechanically approved, freeze exact project-source authority for Trainer wild-interaction Skills/Edges/Features; perception/Stealth; capture action/range; movement capabilities; interception; trapping/restraint; Status effects relevant to capture/control; Moves/Abilities that alter position or terrain; weather if used; and any Caelo/Kairos overrides.

Do not infer `Pack Mon`, shared initiative, coordination bonuses or collective tactical actions from migratory grouping.

## Longer-term arc potential

Once one migration/passage is canon-approved, it can become a recurring regional clock with memory. A population can arrive earlier, bypass a damaged stopover, split between two routes, tolerate a human schedule that previously disturbed it, or stop using a corridor after persistent pressure. Institutions can compare years rather than repeat the same quest.

That also gives player decisions delayed consequences. Preserving a stopover, changing a delivery window or causing repeated disturbance can matter next passage without requiring a bespoke cutscene or villain.

## Open canon questions

Marea currently has no species approved by this pass as migratory. The project still needs to decide which population, if any, uses Sendero as a corridor; whether the seasonal crossing name reflects ecology, infrastructure or another established reason; what calendar/season model Ouros uses; whether Cobblemon can express the approved seasonal availability natively in the deployed version; how passage counts are stored; and which institution has final authority for temporary wildlife-related access restrictions.