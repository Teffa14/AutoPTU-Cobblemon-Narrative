# Active Replacement Viability Research — Pass 452

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-12

This note does not establish canon. It records transformed design lessons and source provenance for future Ouros work.

## Repository inspection and duplication check

The complete recursive repository tree at `1c4147ccf74b454335db8e520c1b16ba5d13ae61` was inventoried before writing. Current focus, canon surfaces, assistance/renegotiation Passes 422–451, checkpoint history, private knowledge, information delivery, replanning, world-event coordination, PTU/Kairos routing, prior research and proposals were checked before selecting sources.

Frequently processed references such as Rejuvenation, Desolation, Pokémon Unbound, Tales of Visiwa, the haunted-mansion PTU log, Stoneshard, Roadwarden and Citizen Sleeper were excluded from primary reuse.

The existing corpus had no match for the PTU campaign-log source below, no prior research hit for the `This Gym of Mine` stewardship structure selected here, and no prior hit for the PTR Evolved Interlude/End Trigger guidance.

## Public source A — Pokémon This Gym of Mine

Source: public project site.
URL: https://thisgymofmine.com/
Accessed: 2026-09-12.

The public description reverses the usual travelling-trainer premise by placing the player in charge of an institution. The player manages a Gym, receives challengers and deals with the place as an ongoing responsibility rather than as a location visited once and discarded.

Reusable structure for Ouros:

A long-lived duty can belong to a place and its steward. A scheduled survey, inspection, repair check or ecological review can recur against changing local conditions without becoming a new unrelated quest each time the calendar changes.

Transformation boundary:

Ouros does not import the fan game's city, characters, Gym progression, reputation values, field system, economy, puzzles, battles, dialogue or plot. The only retained idea is the abstract stewardship loop: persistent place plus recurring responsibility plus changing conditions.

## Public source B — PTU campaign log #15

Source: r/PokemonTabletop campaign log #15.
URL: https://www.reddit.com/r/PokemonTabletop/comments/oeddi8/
Reported session date: 2021-07-04.
Accessed: 2026-09-12.

The public session summary includes travel beside a river, discovery of a concealed way into a hostile site, several encounters, and opponents who eventually stop fighting and leave. The useful lesson is structural rather than plot-specific: local observation can change ingress, and an encounter sequence can de-escalate instead of requiring every prepared opponent to be defeated.

Reusable structure for Ouros:

A blocker on an already rescheduled obligation can be genuine without making the assignment impossible. New field evidence may reveal another entrance, a temporary crossing, a safe observation point, a cooperative local actor or a non-combat resolution. Such evidence should first alter viability/replanning. It must not silently grant route access or rewrite the accepted schedule.

Transformation boundary:

No river-base layout, faction, character, homebrew creature/item, combat sequence, reward, dialogue or distinctive event chain is copied.

This Reddit log is community play evidence, not PTU rules authority.

## Public source C — Pokémon Tabletop Reunited: Evolved GM Tips

Source: public GM Tips page, Interlude section.
URL: https://2e.ptr.wiki/en/rules/gm-tips
Accessed: 2026-09-12.

The guide describes Interludes as low-stakes spans that advance time or distance while retaining an explicit condition that returns play to a major scenario.

Reusable structure for Ouros:

Off-screen time can progress while a commitment remains meaningful. A later event can wake the relevant actor because conditions changed. The wake-up should point back to explicit evidence and the currently active obligation rather than reconstructing intent from elapsed time alone.

Transformation boundary:

No PTR mechanic is accepted as PTU/Ouros rules authority. The Interlude procedure, terminology, examples and downtime mechanics are not imported. Only the broad pacing lesson is retained.

## PTU / Caelo / Kairos cross-check

The project PTU/Kairos material remains reference material requiring rule-by-rule admission. Existing routing for travel, hazards, weather, encounters, rival/boss structures and campaign/session material does not grant a mechanic merely because a narrative scene mentions it.

Pass 452 does not add PTU battle rules. It only allows the current replacement commitment to receive the same kind of pre-start evidence already supported for an original commitment.

No Caelo/Kairos reference overrides authored Ouros canon in this pass.

## Engine evidence checked live

Read-only AutoPTU-Java head on 2026-09-12: `1ff22f2bb1495527ca6aea08d40ce87f38f4a9d5`, merged through PR #452. The current evidence adds server-authoritative guarded switch-trigger dispatch for specific Feature paths. This is meaningful evidence for those exact trigger contracts only.

Read-only AutoPTU Python remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its newest known change is presentation-only and does not alter battle rules or outcomes.

No family is promoted by this research pass.

Current conservative posture:

- targeting/footprints/range/LoS: VERIFIED only within audited scopes;
- base movement legality: VERIFIED only within audited scopes;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED only within audited scopes;
- action economy/initiative: PARTIAL;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING according to exact behavior;
- move-specific behavior: individually gated;
- abilities: PARTIAL and individually gated;
- items: individually gated;
- Trainer Features/perks: individually gated;
- AI legal-action infrastructure: specialized objective verbs require explicit admission;
- AI tactical policy: BLOCKING for specialized objective policies not already admitted;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

## Design conclusion

The next safe step toward multigenerational renegotiation is not another full negotiation owner. The current replacement first needs to be able to accumulate blocker evidence while proving that it is the active leaf. Pass 452 implements exactly that seam.
