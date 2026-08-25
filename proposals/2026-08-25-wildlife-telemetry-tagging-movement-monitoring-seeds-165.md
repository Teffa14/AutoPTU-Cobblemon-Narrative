# Pass 165 — Wildlife telemetry, tagging, and movement-monitoring seeds

Status: NON-CANON / PROPOSED
Authority dependency: `design/wildlife-telemetry-tagging-movement-monitoring-protocol.md`

All concepts below are original Ouros candidates. They do not establish canon technology, institutions, species behavior, or PTU mechanics.

## Thirty worldbuilding and quest candidates

1. **No Signal at Dawn** — A recently released Pokémon stops appearing on the public monitoring dashboard. The actual investigation has at least four live possibilities: receiver outage, coverage departure, device failure, or a real change in movement. The case is allowed to remain unresolved.

2. **The Tag Moved Without the Pokémon** — A stationary individual is photographed in one valley while its telemetry device appears to travel downstream. Recovery later shows the device detached and entered a tributary. The raw detections remain valid even though the animal-movement interpretation changes.

3. **Receiver Shadow** — A ridge station has a persistent blind sector caused by local geometry. A supposed avoidance corridor disappears after a second receiver is installed.

4. **Battery Year Three** — A long-lived monitoring program reaches the point where older devices begin failing at different times. The resulting silence looks ecological until technicians compare deployment vintages.

5. **The Shed Collar** — A device is recovered in an ordinary resting site. The Pokémon is later observed alive elsewhere. The object enters Material Culture as a recovered research artifact while Pokémon Agency preserves the individual separately.

6. **Two Tags, One Animal?** — Historical records appear to assign two devices to one Pokémon during overlapping dates. One deployment record is wrong, but the data alone cannot initially reveal which.

7. **One Tag, Two Animals?** — A device was redeployed after recovery but one downstream dataset still assumes the old subject association. A migration paper now contains a provenance problem rather than fabricated animal behavior.

8. **The Post-Release Gap** — A rehabilitation release produces no detections for eleven days and then regular detections resume. The gap is preserved instead of filled by an invented route.

9. **Sensitive Roost Coordinates** — A famous tagged individual repeatedly uses a newly discovered roost. Researchers keep the precise site restricted while the public map shows only a broad district.

10. **Tagged Individual Skips Migration** — One known individual remains north during a year when the population-level migration still occurs normally. Migration records it as partial participation, not a corridor collapse.

11. **Signal Under the Bridge** — A river receiver repeatedly detects the same tag near a bridge. Field teams must determine whether the animal is using the site, the tag is trapped in debris, or receiver geometry is producing repeated observations from a wider area.

12. **Forest Grew Around Receiver** — Ten years of canopy regeneration gradually changes station performance. What looks like declining use of a corridor may partly be declining detectability.

13. **Old Frequency** — A historical receiver array still works but listens for a technology no longer used by new devices. Both generations of records are valid; interoperability is not automatic.

14. **Data Logger Survived the Storm** — Communications fail and the public network appears dead, but local stations continue recording. Weeks later the backlog fills an important gap in the Chronicle.

15. **Device That Changed Behavior?** — Researchers observe repeated rubbing near an attachment site and suspend the deployment under Research Ethics. Whether the device altered broader movement remains an open scientific question.

16. **Broken Clock** — A station’s timestamps are consistently wrong while detection order remains internally coherent. Timekeeping produces a corrected estimate without modifying raw records.

17. **Array Heard Nothing** — Every receiver in a migration gate records silence during an expected passage, but coverage testing later shows one station was offline and another had reduced range. The year cannot support a strong absence claim.

18. **Recovered Tag in a Nest** — A device from an adult appears inside a reproductive site. The record cannot decide whether the adult built the site, brought the device there after detachment, or whether another Pokémon moved it.

19. **Tagged Pokémon Returns to Care** — A released individual voluntarily returns to a rehabilitation facility while its device remains active. The return is a Pokémon Agency/Rehabilitation event; telemetry merely documents part of the path.

20. **Tagged Pokémon Joins a New Collective** — Field observations associate the individual with a different wild group. Telemetry can document shared locations but cannot assign leadership, kinship, membership, or social-learning roles by itself.

21. **Public Map Is Coarse** — Players notice that a public movement map seems less precise than their field experience. The difference is intentional privacy protection, not a broken map.

22. **Researcher Misreads Stationary Signal** — A rushed interpretation labels a long stationary sequence as mortality. A later field visit recovers the detached device. The correction becomes a training case in scientific uncertainty.

23. **Tag Is in the River** — A terrestrial individual’s tag starts moving at water speed. Hydrology can help explain the device trajectory without making claims about the Pokémon’s movement.

24. **Portable Receiver False Lead** — A field team follows increasing signal strength to the wrong side of a canyon because reflection and local geometry affect the reading. The incident improves future method documentation.

25. **Uninstrumented Majority** — A beautifully mapped set of tagged individuals is compared with ordinary field surveys that show many untagged Pokémon using other areas. The research institution revises how it presents the map publicly.

26. **Nothing Happened This Deployment** — A device works, the Pokémon behaves within its known range, no welfare issue is observed, and the deployment ends routinely. Years later this quiet interval becomes valuable baseline evidence.

27. **Two Stations, One Detection** — The same transmission reaches two stations. The processing pipeline must preserve both observations while deciding whether they support one derived fix.

28. **The Receiver Was Moved** — A station was relocated after road construction but an old configuration record stayed active. Apparent movement change vanishes after the station history is corrected.

29. **The Release Tag Outlived the Program** — A conservation project closes, but a recovered transmitter years later becomes an archive object that reconnects several old datasets and memories.

30. **The Public Thinks the Signal Is Live** — A museum display shows a historical movement animation. Visitors assume it tracks a currently living Pokémon in real time. The institution must redesign interpretation without erasing the original exhibit history.

## Long arc: Five Years of Cedar Telemetry Network

Year one begins with a small receiver network supporting a migration survey. Early data appear to show a strong eastern corridor. In year two a new station fills a coverage gap and reveals western movements that were always plausible but previously invisible. Year three includes a major clock correction; historical timing estimates are revised without changing raw detection order. Year four brings canopy growth, a moved station, and one recovered detached tag. Year five produces the strongest dataset yet, but the final scientific conclusion is narrower than the first public story: several movement strategies coexist, and network history explains part of the apparent change.

The arc produces institutional learning, map revisions, repeat locations, technicians, archives, and scientific debates without needing a villain. Migration remains the authority for corridor interpretation.

## Long arc: One Tag, Three Meanings

A device begins as a research instrument on a persistent wild Pokémon. Months later repeated stationary signals are interpreted as site fidelity. A field team then recovers the detached tag, revising that period to “device location unknown relative to subject.” Years later the physical tag enters a museum collection as evidence of an early regional monitoring program. The same object therefore accumulates research, error-correction, material-culture, and public-memory histories without ever becoming the Pokémon itself.

## Long arc: The Invisible Corridor

For several years, a handful of tagged individuals are detected at sparse receiver gates. Field signs, camera traps, seasonal sightings, and later remote sensing gradually make a broad movement corridor plausible. The important design rule is that no single telemetry line becomes the corridor. Conservation and Migration assemble the claim from multiple independent sources and preserve uncertainty around exact paths.

## Encounter contract: Telemetry Receiver Ridge Recovery

Narrative premise: a remote receiver has stopped reporting during a monitoring window. Technicians need access to determine whether the problem is power, communications, physical damage, or environmental obstruction. Wild Pokémon nearby are not presumed responsible.

### FULL version

The encounter can include a technician moving between equipment points, wildlife withdrawing through the same area, and a route that changes if storm damage or unstable ground matters tactically.

Required engine families:

- targeting/footprints/range/LoS: VERIFIED for ordinary battle targeting only;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: BLOCKING when movement through contested space matters;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL if an exact status is used;
- terrain/weather/hazards/zones/reactions: BLOCKING if storm, unstable terrain, protected equipment areas, or environmental effects alter tactics;
- move-specific behavior: PARTIAL for any specific Move beyond verified contracts;
- abilities/items/Trainer Features: PARTIAL when invoked;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for `REACH_DEVICE`, `PROTECT_TECHNICIAN`, `WITHDRAW`, or `CLEAR_ROUTE` objectives;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

### REDUCED version

World state resolves technician travel, receiver diagnosis, wildlife withdrawal, and equipment handling first. If a separate confrontation remains, AutoPTU receives a static legal arena with only real combatants. The receiver is repaired or diagnosed afterward from world state; battle victory never restores telemetry automatically.

## Encounter contract: Released Pokémon Signal Goes Silent

This is primarily an investigation and should usually remain non-combat.

Rehabilitation, Telemetry, Radio/Technology, Timekeeping, and Conservation inspect the last valid detection, device state, receiver health, network coverage, tag-loss possibilities, and independent field observations. Outcomes can include `DEVICE_FAILURE_PROBABLE`, `LEFT_COVERAGE`, `TAG_LOSS_SUSPECTED`, `SUBJECT_REOBSERVED`, or `UNRESOLVED` according to evidence.

No battle-engine category is required unless an unrelated confrontation emerges during fieldwork. Silence never writes death, release failure, capture, or absence.

## Encounter contract: Tag Recovery at River Crossing

Narrative premise: a detached or possibly detached device is detected near a river crossing during an ongoing ecological study.

### FULL version

Complete movement is BLOCKING if researchers or wildlife must cross/withdraw dynamically. `terrain/weather/hazards/zones/reactions` is BLOCKING if current, changing water, debris, slippery banks, or other environmental state has tactical effect. AI tactical policy is BLOCKING for `RETRIEVE_DEVICE`, `WITHDRAW`, `PROTECT_RESEARCHER`, and route objectives. Adapter/playback remains BLOCKING.

### REDUCED version

Freshwater/Travel freeze river and access state. Researchers recover or fail to recover the device outside battle. If conflict remains, a nearby stable arena is used. No current, drowning, mud, or forced-movement rules are invented.

## Encounter contract: Migration Receiver Array Interruption

Narrative premise: an array that normally documents a seasonal movement episode is partially unavailable during the crossing window.

### FULL version

Migration groups must be able to cross/withdraw while technicians reach equipment without all wild Pokémon behaving as hostile combatants. This requires complete movement, objective-aware AI tactical policy, and Minecraft/Cobblemon/Craftics playback. Environmental-family support is required only when a real tactical hazard or dynamic protected corridor is present.

### REDUCED version

Migration advances in world state first. Technicians and moving groups are removed from the battle grid. AutoPTU is used only for a static confrontation that remains at a receiver site. The missing data window is preserved regardless of battle outcome.

## Implementation guardrails

Pass 165 does not introduce electronic tracking as a PTU Item, Skill check, Feature, Move, Ability, status, target lock, Accuracy modifier, initiative modifier, capture modifier, or spawn system. It does not use battle LoS as receiver coverage. It does not convert loaded Minecraft entities into telemetry records. All richer mechanics remain gated behind the exact engine families identified above and behind future canon decisions about Ouros technology.