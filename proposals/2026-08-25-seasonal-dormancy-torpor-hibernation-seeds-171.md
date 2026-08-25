# Seasonal Dormancy, Torpor and Hibernation Seeds — Pass 171

Status: NON-CANON PROPOSALS. Research-derived candidates only.
Date: 2026-08-25

1. The Den That Opens Late — a historically reliable emergence window passes with no activity; the mystery begins with monitoring gaps, not presumed mortality.
2. Arousal Is Not Awakening — a brief midwinter movement is mistaken publicly for the end of dormancy.
3. The Camera Missed Two Weeks — a sensor outage creates the exact uncertainty needed to prevent a false precise timeline.
4. The Same Den, Different Entrance — a storm changes access while the site identity persists.
5. The Road Was Built During Summer — a winter den later turns out to sit beside infrastructure that did not exist when the site was first used.
6. The Quiet Winter Was Normal — nothing unusual happens; the season becomes a valuable baseline years later.
7. Three Winters, Three Exit Dates — emergence varies enough to undermine a simplistic calendar rule.
8. The Tourist Cave Closes Early — a public attraction narrows access after monitoring detects repeated seasonal use.
9. The Famous Hibernator Stayed Active — a local population does not follow the popular species stereotype.
10. The Site Was Never Empty — non-invasive monitoring finds brief arousal events during a season assumed to be continuous inactivity.
11. The Alternate Exit — all visible signs at the known entrance stop, but tracks later reveal another route.
12. Snow Covered the Evidence — a survey says `NOT_DETECTED`; weather later explains why surface evidence was poor.
13. The Research Team Stops Visiting — the correct conservation response is less data, not more intrusion.
14. The Old Sign Is Too Specific — a trail marker gives an exact emergence date that was always only an estimate.
15. The Den Became a Landmark — local culture remembers a long-used site while exact current occupancy remains private.
16. The Warm Winter Question — entry occurs normally but exit shifts; Climate and Dormancy keep correlation separate from causation.
17. The Cold Spring Question — emergence occurs later even though winter itself was mild.
18. The Food Year — pre-dormancy foraging observations change while the den schedule does not.
19. The Former Partner's Winter Site — a released Pokémon may be re-observed at a recurring refuge without assuming ownership or guaranteed identity until evidence is sufficient.
20. The Den Nobody May Publish — the site is scientifically important but exact coordinates remain restricted.
21. The Midwinter Footprints — tracks outside a den support arousal, not permanent departure.
22. Two Sites, One Individual — telemetry suggests alternating seasonal refuges across years.
23. The Old Mine Becomes a Hibernaculum — an extraction site acquires ecological importance after closure.
24. The Hibernaculum Under the Festival Road — a recurring public event overlaps a sensitive seasonal site.
25. The Maintenance Window Was Wrong — infrastructure work was scheduled from an outdated activity guide.
26. The Winter Without Telemetry — the tag fails before dormancy begins; the season must remain partially unknown.
27. The Colony That Split — observations suggest two winter sites after a physical disturbance, but population identity remains shared.
28. The Public Calls It Sleeping — researchers use a more cautious term because the actual physiological state was never measured.
29. The Spring Survey Found Everyone — a poor winter dataset is later followed by normal activity, correcting a premature decline narrative.
30. Nothing Happened at Den Seven — the site remains quiet, equipment works, no quest appears, and the year improves the long-term record.

## Long arc: Five Winters at Cedar Hibernaculum

Year 1 establishes a coarse entry/exit window.

Year 2 adds a monitoring outage and uncertainty.

Year 3 road maintenance near the site triggers a temporary access restriction.

Year 4 a warm late winter produces an earlier candidate emergence, but coverage is imperfect.

Year 5 monitoring shows the earlier pattern again, enough to justify a timing revision but not a single-cause claim.

The arc can remain entirely ecological/institutional. It does not need a villain or Legendary explanation.

## Long arc: The Den With Three Histories

The same physical site is remembered first as a hunter shelter, later as a wildlife den, and eventually as a protected monitoring site.

Architecture preserves physical revisions.

Public Memory preserves social interpretations.

Dormancy preserves seasonal use.

Land Tenure/Conservation preserves access authority.

The site can accumulate decades of meaning without any layer overwriting the others.

## Long arc: From Winter Silence to First Route

A persistent individual is followed through several seasons from a winter refuge to spring activity and later migration/travel observations.

Dormancy owns the low-activity episode.

Telemetry/Tracking owns evidence between observations.

Migration owns corridor interpretation if the later movement is genuinely migratory.

Pokémon Agency preserves identity.

The arc is allowed to contain unknown intervals.

## Encounter contract: Hibernaculum Access Interruption

FULL version:
A research team must retrieve failed monitoring equipment near a protected chamber while an unrelated threat creates a tactical problem. Dormant wildlife remains noncombatant and protected.

Required categories:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL if needed;
- full stateful damage pipeline — PARTIAL if combat damage occurs;
- status lifecycle — PARTIAL for exact statuses;
- terrain/weather/hazards/zones/reactions — BLOCKING if protected chambers, cave hazards or unstable terrain affect tactics;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for `WITHDRAW`, `PROTECT_RESEARCHER`, `AVOID_PROTECTED_ZONE`, `REACH_EXIT`;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED version:
World state handles equipment recovery and site access. Researchers leave the sensitive area. Any independent confrontation uses a static arena outside the hibernaculum. Dormant occupants are never inserted into battle by default.

## Encounter contract: Early Emergence Road Closure

FULL version:
Wildlife movement and a temporary traffic closure coexist while players protect responders or clear an unrelated threat.

Major blockers:
- complete movement;
- tactical AI for `CROSS`, `WITHDRAW`, `CLEAR_ROUTE`;
- adapter/playback;
- environment family only if snow/ice/barriers have tactical effects.

REDUCED version:
Road Ecology/Wayfinding resolves the closure and crossing first. AutoPTU receives a static battle only afterward.

## Encounter contract: Den-Site Reconstruction After Storm

FULL version:
Debris, unstable surfaces, wildlife withdrawal and a changing route matter tactically.

Major blockers:
- complete movement;
- terrain/weather/hazards/zones/reactions;
- tactical AI;
- adapter/playback.

REDUCED version:
Architecture/Crisis/Cryosphere resolves the site revision and safe access. Battle, if any, occurs later on stable ground.

## Non-combat scenario: Midwinter Arousal Review

Researchers compare camera timestamps, tracks and environmental records after a brief midwinter activity event.

Valid outcomes include:
- `AROUSAL_SUPPORTED`;
- `FALSE_DETECTION`;
- `INSUFFICIENT_COVERAGE`;
- `UNRESOLVED`.

No battle capability is required.