# Death, Bereavement, Funerary and Memorial Seeds — Pass 165

Status: NON-CANON WORLDBUILDING CANDIDATES
Date: 2026-08-31

These concepts exercise the proposed mortality/funerary continuity layer without establishing any specific Ouros death, cemetery, religion, afterlife doctrine or cultural custom.

## The Marker With No Remains

A small settlement maintains a marker for someone whose body or remains were never recovered. Older residents call it a grave; the site record calls it a memorial marker. The discrepancy becomes important when a later infrastructure project assumes physical remains are present.

Design use:

- demonstrates `GRAVE_LANGUAGE_USED != REMAINS_PRESENT`;
- creates a records-and-memory problem rather than a supernatural mystery;
- can connect archives, planning, family testimony and material culture.

## Five Times Someone Said “They’re Gone”

Five witnesses use the same phrase for different states:

- one means the person left town;
- one means contact was lost;
- one means the person is missing;
- one means a preliminary death report circulated;
- one speaks after confirmed death.

The investigation is about resolving referents, dates and evidence rather than exposing a liar.

## The Cemetery That Outlived the Town

A once-busy settlement shrank or moved. Its cemetery remained because descendants, caretakers and travelers continued visiting it. Paths disappeared, local place names changed and nearby land acquired new uses.

Long-term payoff:

Players who knew the old town can return decades later and recognize continuity through markers, trees, paths and caretaker records even when almost nothing else remains.

## Two Memorials, One Death

Two communities preserve different memorials to the same deceased person or Pokémon. One focuses on public service; the other remembers a private relationship or local failure. Neither monument controls the underlying Chronicle fact.

The conflict can remain interpretive rather than requiring one memorial to be fraudulent.

## The Funeral Nobody Could Attend

Weather, transport disruption or another authored obstacle prevents many intended participants from reaching a funerary episode. The ceremony still occurs.

Later stories distinguish:

- intended attendance;
- actual attendance;
- messages sent;
- later private visits;
- public claims that “everyone was there.”

No attendance count is automatically a measure of affection.

## The Name That Moved Three Times

A marker is moved during redevelopment, then during consolidation of an old burial ground, then again after a preservation project. The physical object, resting-place record and remains-location record accumulate separate histories.

This concept exercises relocation provenance without requiring desecration or villainy.

## The Companion Nobody Buried

A beloved Pokémon dies, but the local custom chosen by its Trainer does not create a grave. Decades later, outsiders assume a missing marker means nobody cared.

The story tests cultural projection and the boundary between mourning evidence and universal funerary norms.

## The Keeper Who Refuses the Hero Story

A cemetery caretaker maintains a famous person's resting place but objects to the simplified heroic version repeated by visitors. The caretaker has direct memories and records, yet those too remain perspective-bound.

Public Memory owns the competing legacy. The mortality layer only links the person, site and funerary history.

## The Pokémon Who Returns to the Same Marker

A living Pokémon repeatedly visits the same memorial location at similar times of year. Ouros records the behavior.

It does not infer:

- understanding of death;
- supernatural communication;
- reincarnation;
- exact emotional state.

NPCs may hold different interpretations.

## The Memorial Built Before Confirmation

A dangerous disappearance lasts for years. A community establishes a memorial while official status remains missing or presumed dead. Later evidence changes the mortality record.

The memorial's existence remains a historical fact regardless of the eventual status.

## The Name Missing From the Public Monument

Private records establish a confirmed death and family mourning, but a large public monument omits the name because of the monument's authored scope, politics, incomplete records or a later design choice.

The absence does not erase the person from Chronicle.

## The Resting Place Nobody Can Prove

Tradition identifies a particular old marker as the resting place of a historic figure. Archival evidence is incomplete. Archaeology cannot currently confirm it.

Ouros stores:

- traditional identification;
- physical marker history;
- archaeological findings;
- uncertainty.

It does not choose spiritual or historical certainty merely to close the mystery.

## The Empty Grave That Became Important

A symbolic grave becomes the center of an annual observance. Generations later, many participants know the observance better than the original reason the grave was empty.

Ritual/Tradition owns the observance lineage. This layer only keeps the symbolic resting-place relationship and mortality provenance.

## The Public Hero and the Private Person

Long arc.

A respected public figure dies after decades of ordinary relationships, mistakes and service. Public Memory produces a compressed civic image. Family, former colleagues, rivals and old friends preserve different experiences. Years later, players can encounter all of these without any one perspective invalidating the others.

The arc should avoid a final “true version” reveal unless Chronicle genuinely contains decisive evidence.

## Three Generations, One Marker

Long arc.

A modest marker is maintained by three generations of different caretakers. The first knew the deceased personally. The second inherited the responsibility. The third knows the person only through stories and records.

Over time:

- the path changes;
- nearby buildings disappear;
- an inscription erodes;
- a copy enters an archive;
- the site's meaning broadens.

The payoff is accumulated continuity rather than escalation.

## The Missing Become Names

Long arc.

After a historical disaster, a memorial records both confirmed dead and still-missing people in deliberately different sections. Later retellings collapse the distinction.

Players reconstruct which names had which status at each date. Some statuses may remain unresolved indefinitely.

The memorial never upgrades missing people to confirmed dead by itself.

## Encounter Contract A — Resting-Site Approach Incident

Narrative premise:

A tactical threat blocks immediate access to an established resting or memorial site while visitors or caretakers are nearby.

Full version required capability families:

- targeting/footprints/range/LoS — VERIFIED baseline;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL as selected content requires;
- status lifecycle — PARTIAL as selected content requires;
- terrain/weather/hazards/zones/reactions — BLOCKING if graves, unstable ground, fog, fire, falling material or reaction windows have tactical effects;
- move-specific behavior — PARTIAL, individual audit required;
- abilities — PARTIAL, individual audit required;
- items — PARTIAL, individual audit required;
- Trainer Features/perks — PARTIAL, individual audit required;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for protect/withdraw/site-control behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic site playback.

Full status: BLOCKED.

Reduced version:

All visitors, caretakers, remains, markers and protected funerary objects are outside BattleSpec. Geometry is static and selected combat content is individually audited.

Permitted result:

`IMMEDIATE_RESTING_SITE_APPROACH_CLEAR`

Forbidden inferences:

`IMMEDIATE_RESTING_SITE_APPROACH_CLEAR != FUNERAL_COMPLETE`

`IMMEDIATE_RESTING_SITE_APPROACH_CLEAR != SITE_UNDAMAGED`

`BATTLE_WON != SPIRITS_APPEASED`

`BATTLE_WON != DEATH_CONFIRMED`

Reduced status: READY at narrative-contract level.

## Encounter Contract B — Memorial Procession Route Interruption

Narrative premise:

A procession pauses because a confrontation blocks the next route segment.

Full version requirements:

The full version additionally requires reliable escort/protection/withdrawal semantics, crowd or formation movement, protected-object carrying where relevant, lifecycle, tactical policy and any hazards/reactions active on the route.

Overall full status: BLOCKED.

Reduced version:

The procession stops before initiative. Participants, vehicles, coffin/urn/marker or other culturally authored objects remain outside BattleSpec. AutoPTU resolves a separate conventional engagement.

Permitted result:

`IMMEDIATE_PROCESSION_ROUTE_CLEAR`

Forbidden inferences:

`BATTLE_WON != PROCESSION_RESUMED`

`BATTLE_WON != FUNERARY_RITE_COMPLETED`

`BATTLE_WON != REMAINS_TRANSFERRED`

Reduced status: READY at narrative-contract level.

## Encounter Contract C — Search-Site Perimeter

Narrative premise:

A search for a missing person or Pokémon reaches a location whose immediate perimeter contains a tactical threat.

Full version requirements:

- complete movement including forced movement — PARTIAL;
- lifecycle — PARTIAL;
- hazards/weather/zones/reactions — BLOCKING when environmental search conditions are tactical;
- individual moves/abilities/items/features — PARTIAL and audited;
- AI tactical policy — BLOCKING for protect/search/withdraw semantics;
- adapter/playback — BLOCKING.

Overall full status: BLOCKED.

Reduced version:

Search activity pauses. Searchers, evidence objects and possible remains are outside BattleSpec. AutoPTU resolves only the local confrontation.

Permitted result:

`IMMEDIATE_SEARCH_SITE_APPROACH_CLEAR`

Forbidden inferences:

`BATTLE_WON != SUBJECT_FOUND`

`BATTLE_WON != REMAINS_FOUND`

`BATTLE_WON != DEATH_CONFIRMED`

`BATTLE_LOST != SEARCHER_DEAD`

Reduced status: READY.

## Encounter Contract D — Groundskeeper Record-Recovery Perimeter

Narrative premise:

A caretaker needs access to a records or maintenance area during an unrelated tactical incident.

Full version requirements:

Protection/escort/object-carrying semantics, lifecycle, tactical objective policy and any dynamic hazards remain incomplete or blocking. Individual combat content still needs parity audit.

Overall full status: BLOCKED.

Reduced version:

The caretaker and records are removed from the tactical slice before initiative. Static battle geometry protects the separation of authorities.

Permitted result:

`IMMEDIATE_CARETAKER_ACCESS_PERIMETER_CLEAR`

Forbidden inferences:

`BATTLE_WON != RECORDS_RECOVERED`

`BATTLE_WON != MARKER_IDENTITY_VERIFIED`

`BATTLE_WON != RESTING_PLACE_CONFIRMED`

Reduced status: READY.

## Authoring restraint

Death is a high-consequence continuity event. These seeds do not authorize automatic mortality for established characters or Pokémon.

A generator should not use death as the default explanation for absence, retirement, relationship change, institutional turnover or quest urgency. The project's authored canon and safety/continuity rules must explicitly permit the mortality event first.