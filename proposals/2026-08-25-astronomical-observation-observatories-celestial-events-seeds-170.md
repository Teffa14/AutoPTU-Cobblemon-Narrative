# Pass 170 — Astronomical Observation, Observatories & Celestial Events Seeds

Status: PROPOSED / NON-CANON. Nothing here establishes Ouros lore until explicitly approved.
Date: 2026-08-25

These seeds extend the proposed astronomical-observation layer while preserving Timekeeping, Lightscapes, Meteorology, Metrology, Science, Sacred Sites, Geology, Pokémon Agency and PTU rules as separate authorities.

## 30 worldbuilding and quest candidates

1. **The Comet Was Predicted, the Clouds Weren’t.** A rare observing window is scientifically well predicted, but the primary observatory is clouded out. A smaller community station may provide the only local record. The event remains real even if nobody in the capital sees it.

2. **Two Observatories, One Transient.** Two sites record a brief light at slightly different times. The first mystery is whether they saw the same event; a clock offset may matter more than the sky.

3. **The Clock Was Eleven Seconds Fast.** An old observation becomes newly useful after Timekeeping reconstructs an observatory clock’s drift. The raw plate remains unchanged; only its interpreted timestamp changes.

4. **The Old Star Chart Uses Another Epoch.** A century-old chart appears inaccurate until researchers reconstruct its coordinate convention and reference date.

5. **The Meteorite That Wasn’t Found.** A bright meteor is observed from several towns and a search area is estimated, but no physical object is recovered. The absence of a specimen does not invalidate the observation.

6. **The Rock Found Ten Years Later.** A museum receives an unusual stone from an old collection. Geology can test whether it plausibly links to a documented fall without allowing location alone to settle the question.

7. **The Festival Date Stayed Fixed.** A town’s celestial festival remains on the same civic date even though the astronomical event it originally referenced no longer peaks that night. Tradition and scientific timing diverge without either needing to disappear.

8. **Light From Meridian.** Urban growth slowly makes a historic observatory less useful. The institution debates relocation, filters, public outreach and preservation of the original site.

9. **The Instrument Saturated.** The brightest part of an unusual event overwhelms the detector. A technically “worse” amateur image preserves evidence the flagship instrument lost.

10. **Same Sky, Three Stories.** Scientists, a sacred-site caretaker and local families all describe the same recurring celestial event differently. The system preserves each claim without forcing a single metaphysical interpretation.

11. **Minior Fall Night.** Several Minior are observed descending during a night of unusual atmospheric conditions. The episode becomes ecological research, not proof that the astronomical event itself was made of Minior.

12. **Lunatone at Full Moon.** A local Lunatone population appears more active during a particular lunar phase. Researchers need repeated observations before deciding whether the regional pattern matches species lore.

13. **The False New Object.** A candidate transient produces excitement before follow-up shows it was an artifact or already-known target. The original notice stays in Chronicle as a reasonable provisional conclusion.

14. **The Object That Split in the Catalog.** Years of new observations reveal that records thought to describe one target actually belong to two.

15. **The Two Names Problem.** A historical observatory and a modern institute use different names for the same celestial target. Identity/Language work reconciles the archive without rewriting old publications.

16. **The Public Alert Went Viral.** A cautious follow-up request is interpreted online as a catastrophe warning. Media/Public Memory manage the social consequences while Astronomy keeps the scientific claim scoped.

17. **The Quiet Observatory.** Nothing unusual happens for an entire season. Years later that clean baseline helps identify when a variable pattern really began.

18. **The Missing Winter Series.** A roof mechanism failed for six weeks decades ago. A modern analysis must preserve the gap instead of interpolating a false uninterrupted series.

19. **Community Night Saves the Series.** The main station closes for maintenance, but distributed observers preserve enough coverage to continue a long-term record.

20. **The Plate in the Library.** An old photographic plate stored outside the observatory contains an unnoticed target. Visual Records, Archives and Astronomy reconstruct its provenance before using it scientifically.

21. **The Mountain Is Dark Again.** A former industrial corridor reduces nighttime lighting after redevelopment. Lightscapes records the change; Astronomy later discovers old observations can once again be repeated from the historic site.

22. **The Telescope Works, the Dome Does Not.** The instrument is functional but the building cannot safely expose it after structural damage. Public Works and Astronomy remain separate.

23. **The Wrong Horizon.** A new building blocks a narrow low-altitude observing window while leaving the observatory otherwise intact. Land Use/Public Space and Lightscapes become relevant without creating a battle mechanic.

24. **The School’s Better Measurement.** A student observing program produces one datum that improves a solution. Institutional prestige does not determine scientific validity.

25. **The Recovery Area Became a Park.** Decades after a meteor observation, the predicted fall area has become urban parkland. A new search proposal now needs access, archaeology/environmental safeguards and public communication.

26. **The Satellite Question.** An old document appears to describe an artificial object in the sky. Before importing modern assumptions, Archives/Technology must establish what the text actually means and whether Ouros even had that technology.

27. **The Observatory Changed Owners.** The building passes between institutions while the observing archive retains a continuous scientific identity.

28. **The Observation Nobody Believed.** A lone historical observer recorded something that did not fit contemporary models. A later dataset makes the record plausible without proving every detail of the original interpretation.

29. **The Forecast Was Right, the Crowd Was Wrong.** A public observing night accurately predicts the event, but visitors gather at the wrong side of the complex because an old sign still points to a former viewing terrace.

30. **Nothing Happened at Zenith Station.** The station operates normally, records expected targets and closes on time. The absence of drama is intentional baseline world history.

## Long arc A — Five Returns of Meridian Shower

Year 1 establishes a normal observing campaign and public viewing night. Year 2 suffers cloud loss at the main site but community observers preserve partial coverage. Year 3 a Minior descent overlaps the shower and causes public claims that the phenomena are identical. Year 4 improved timing and multi-site observations separate atmospheric Pokémon activity from the celestial series. Year 5 produces an ordinary return that confirms the value of the revised monitoring network. No villain is required.

## Long arc B — Observatory Through Three Generations

A mountain observatory begins as a small visual station, gains new instruments, loses dark-sky quality as a nearby settlement grows, relocates part of its science program and eventually turns the original dome into an education/archive site. Staff retire, methods change and older observations remain useful. The same institution can have scientific, public-memory and heritage identities at once.

## Long arc C — The Orbit That Kept Changing

A candidate small body is first detected under a short observation arc. Several solution revisions alter the predicted future path as new sites contribute data. Public concern rises and falls. The final story may be that nothing dangerous happens; the real Chronicle is how institutions, media and public observers learn to communicate uncertainty.

## Encounter contracts

### Observatory Dome Evacuation During Storm — FULL

Premise: a public observing night is interrupted by a separate threat while a storm closes safe routes through the observatory complex.

Required capability families:
- targeting/footprints/range/LoS: VERIFIED for ordinary combat;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: BLOCKING if visitors or staff move through threatened corridors;
- core calculations: VERIFIED for supported ordinary calculations;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL for any actual Status;
- terrain/weather/hazards/zones/reactions: BLOCKING if storm, damaged dome, falling equipment, exposed roof or protected corridors alter tactical legality;
- move-specific behavior: PARTIAL when an exact Move is essential;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for `EVACUATE`, `PROTECT_TECHNICIAN`, `WITHDRAW`, `CLEAR_ROUTE`;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED: end the observing session, evacuate visitors and secure the dome through world state. Freeze a safe adjacent arena. If an independent confrontation remains, resolve only that static battle. The storm never becomes custom Weather/hazard mechanics.

### Meteorite Recovery Perimeter — FULL

Premise: a search team investigates a predicted fall area while wildlife/crowd pressure creates a separate confrontation.

Complete movement: BLOCKING for moving search lines, civilians, wildlife withdrawal or interception.

Terrain/weather/hazards/zones/reactions: BLOCKING only if unstable ground, fire, debris or a protected evidence perimeter has tactical effects.

AI tactical policy: BLOCKING for `WITHDRAW`, `PROTECT_RESEARCHER`, `CLEAR_ROUTE`, `REACH_EXIT`.

Adapter/playback: BLOCKING.

REDUCED: search and evidence recovery happen outside combat. Geology/Material Culture decide whether any candidate rock is relevant. Run a static battle only after researchers and specimens are removed from the grid. Victory never proves a meteorite linkage.

### Stargazing Festival Crowd Surge — FULL

Premise: an accurate celestial prediction draws more visitors than a historic viewing site can safely hold, while a separate Pokémon disturbance develops nearby.

Complete movement: BLOCKING for crowd evacuation and non-hostile wildlife movement.

AI tactical policy: BLOCKING for `EVACUATE`, `WITHDRAW`, `PROTECT_VISITOR`, `CLEAR_ROUTE`.

Adapter/playback: BLOCKING.

Environment family: BLOCKING only if slopes, darkness, temporary barriers or weather need actual tactical consequences.

REDUCED: reroute/evacuate visitors in Public Events/Wayfinding world state and allow wildlife to withdraw. Use a static confrontation only if one remains. The celestial event continues independently of the battle outcome.

### Two Observatories Disagree — NON-COMBAT

Timekeeping, Metrology, Meteorology, Lightscapes, Astronomy and Science compare raw records, coverage and solution revisions. A valid resolution may be `UNRESOLVED`. No battle capability is required.

## Mechanical guardrails

Do not create environmental Gravity, Moonlight healing, lunar stat modifiers, meteor collision damage, comet zones, eclipse Status, cosmic Accuracy/Initiative changes, guaranteed Legendary appearances, Minior spawn schedules, telescope bonuses or automatic Psychic/Occult checks.

Minecraft sky rendering remains presentation only. A vanilla moon phase, shader, particle or client-side clock never becomes the authoritative astronomical event state.