# Global NPC AI / engine readiness snapshot — Pass 280

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05
Narrative repo baseline before this pass: `106235725fdc8c64a3836647599b7cb7bdb3cc30`

## Read-only engine evidence

AutoPTU-Java live main inspected at:
`b4d46423ba657417f987f7432b49a5f81a268062`

Head is merge PR #357, `Add PTU/Kairos rulebook conformance baseline`. It strengthens the acceptance protocol by separating Python parity from selected-rule-profile conformance. This is valuable validation infrastructure but does not by itself prove a new tactical capability family complete.

AutoPTU Python live main inspected at:
`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Its head explicitly states presentation-only coordinate synchronization and no battle-rule/outcome change.

Neither repository was modified by Pass 280.

## Permanent capability classification

No category is promoted by this pass.

- targeting / footprints / range / LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy / initiative: VERIFIED within audited contracts;
- full turn / round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING;
- move-specific behavior: PARTIAL;
- Abilities: PARTIAL;
- Items: PARTIAL;
- Trainer Features / perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING;
- Minecraft / Cobblemon / Craftics adapter / playback: PARTIAL / BLOCKING end-to-end.

## Global NPC social layer distinction

`AI tactical policy: BLOCKING` does not block ordinary world-agent social decisions.

An NPC can decide to:
- help someone;
- report to an institution;
- seek or avoid another actor;
- train because of rivalry;
- arrange a challenge;
- negotiate or communicate;
without tactical AI.

When the selected purpose becomes a structured battle or other PTU-resolved interaction, the world agent emits `REQUEST_AUTOPTU`. Tactical autonomous selection then depends on the relevant AutoPTU categories.

## Encounter dependency examples

World-only friend assistance:
- world-agent social/agenda layer;
- future travel/communication systems as needed;
- Minecraft projection only if locally visible;
- no AutoPTU requirement unless a structured obstacle occurs.

Rival challenge arrangement:
- world-agent social state;
- knowledge/communication;
- schedule/travel once those layers are connected;
- no combat dependency merely to arrange the event.

Structured rival spar, intended full version:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- damage/status families if used;
- exact Move/Ability/Item/Trainer Feature families used by participants;
- terrain/reactions or complete movement only when the encounter actually calls for those mechanics;
- AI legal-action infrastructure;
- AI tactical policy for autonomous opponent tactical choice;
- adapter/playback for Minecraft presentation.

Reduced version while richer categories are incomplete:
- social AI selects `ARRANGE_CHALLENGE`;
- narrative scheduling and acceptance persist;
- structured battle starts only when the chosen encounter profile is supported;
- unsupported forced movement/reaction/weather/status gimmicks are omitted without changing the relationship premise.

## Canon/mechanics questions left open

- No PTU/Caelo/Kairos social relationship equation has been adopted.
- Relationship dimensions and utility weights remain Ouros world-simulation policy.
- A faction role cannot fabricate Trainer Features, Items, Abilities or tactical permissions.
- Battle outcome does not automatically imply friendship, trust loss, rivalry growth or faction consequences; those require explicit semantic/social consequence rules.
