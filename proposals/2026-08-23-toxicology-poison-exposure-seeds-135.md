# Toxicology, Poison Exposure & Exposure-Route Seeds — Pass 135

Status: NON-CANON OUROS CANDIDATES. Requires review before promotion.

These concepts use the toxicology architecture without inventing PTU/Caelo poison mechanics.

## 30 candidates

1. The Empty Gas Alarm
A warehouse alarm triggers after a sensor detects a possible airborne hazard. Workers evacuate correctly. Later sampling cannot confirm a harmful exposure. The useful outcome is a better alarm/verification workflow, not a hidden villain.

2. The Poison-Type Scapegoat
A visible Poison-type Pokémon is blamed for workers feeling ill near an old loading yard. Timing evidence shows the symptoms began before that Pokémon started using the site.

3. One Spill, Three Routes
A damaged container creates inhalation risk near the break, dermal contact for a cleanup worker and possible ingestion exposure for a Pokémon that drinks from runoff later. Each record follows a different evidence chain.

4. The Bite With No Symptoms
A field researcher is bitten by a venomous Pokémon. The bite and probable exposure are recorded, but no harmful effect is observed. The incident still matters for future procedure.

5. The Symptoms Without the Bite
A subject develops concerning symptoms after a survey. Everyone focuses on a nearby venomous species, but no bite or sting evidence exists and several alternative sources remain open.

6. The Old Vial
A museum drawer contains a sealed historical sample labeled only “marsh toxin.” Modern analysis may refine the identity, but provenance questions make the result less simple than expected.

7. The Shared Canteen
Several expedition members report similar symptoms. The common water bottle looks suspicious, but route reconstruction shows only some affected people used it.

8. The Gas Mask Question
A responder wore PTU-authoritative protective equipment during an incident. The protection matters only within its exact source rules; investigators still preserve what agent and route were actually present.

9. The Clean Room Smell
Workers detect an unusual odor in a supposedly controlled laboratory. The odor is real, but smell alone cannot identify toxicity or source.

10. The Festival Batch
A food batch is temporarily held after several reports. The health cluster ultimately has mixed causes, while the batch itself remains safe. The hold becomes part of institutional memory.

11. The Toxic Stream Rumor
A creek is called “poisoned” by locals after wildlife behavior changes. Water-quality results show a real change, but toxicology and ecology still need to determine whether exposure explains the behavior.

12. The Wrong Source Drum
A leaking drum is found near an incident. Its contents are hazardous but chemically inconsistent with the evidence from affected subjects.

13. The Venom Archive
A regional clinic has decades of bite and sting records. The old files reveal that several species were historically blamed for incidents later attributed to different causes.

14. The Exposure Nobody Felt
Monitoring confirms a low-level exposure event in a maintenance crew, but no symptoms occur. The story centers on notification, follow-up and uncertainty rather than damage.

15. The Symptoms Came First
A clinic notices a repeated symptom pattern before any source is known. Toxicology joins the investigation only after Care and Outbreak systems have already opened cases.

16. The Source Was Fixed, the Case Stayed Open
A failed process is repaired quickly, but several exposure records remain unresolved because the dose and route cannot be reconstructed confidently.

17. The Public Map Is Too Broad
An advisory marks an entire industrial district while the source investigation is still narrow. Later revisions reduce the area. The original notice remains historically valid for the information available at the time.

18. The Former Partner at the Site
A released former partner is seen near a suspected toxic source. Its presence is logged without assuming ownership, distress, exposure or motive.

19. The Clean Sample, Dirty History
A site currently tests clean. Archived samples show that an exposure event did occur years ago. Current safety and historical truth coexist.

20. The Unopened Container
A container looks damaged after transport. Testing later shows the inner seal never failed. The precautionary shutdown was still reasonable.

21. The Missing Exposure Window
Three sensors agree on a release, but their clocks were out of sync during the event. Metrology and Timekeeping must reconstruct the window before toxicology can estimate who may have been present.

22. The Rain Changed the Route
A surface spill is washed toward a drainage system. Stormwater establishes the path; toxicology determines which subjects had plausible contact; neither system invents symptoms.

23. The Pokémon-Made Warning
A local species consistently avoids one part of a facility before human monitors register a problem. That behavior becomes evidence worth studying, not a magical toxin detector mechanic.

24. The Antidote Story
A public rumor claims that a common item cures “any poison.” The institution publishes a correction distinguishing PTU combat-item behavior from real-world-state toxicology cases.

25. The Reopened Case
A newly catalogued sample allows investigators to revisit an old exposure incident. The updated conclusion changes source attribution without rewriting the original symptoms or public reports.

26. The Decontaminated Room
A room completes cleanup and passes verification. One previously exposed subject still needs follow-up care. Decontamination and clinical recovery stay separate.

27. The Harmless Odor, Harmful Source
The strongest smell in an area comes from a harmless material, while the actual hazardous agent is difficult to detect. Smellscape and toxicology disagree without contradiction.

28. The Toxic Agent With No Crime
A naturally occurring toxic agent enters a spring after unusual geology and weather. There is no responsible villain, only investigation, access decisions and recovery.

29. Three Clinics, Three Labels
Three facilities use different historical terminology for the same toxic agent. Language and Taxonomy/Metrology work is needed before old case counts can be compared.

30. Nothing Happened After the Alarm
A rare but important non-quest. An alarm triggers, evacuation works, verification finds no harmful exposure, everyone returns safely, and the event remains in preparedness history.

## Longer arcs

### Five Incidents at Southworks
Year 1: an odor complaint produces a precautionary evacuation with no confirmed exposure.
Year 2: a real dermal exposure occurs during maintenance and exposes gaps in handoff records.
Year 3: a public rumor blames a Poison-type population near the facility, but evidence weakens the claim.
Year 4: a process revision reduces one risk while creating a new monitoring requirement.
Year 5: a separate upstream source creates a superficially similar incident, and institutional memory prevents investigators from assuming the old explanation.

The arc builds competence rather than escalating toward a mastermind.

### The Venom Atlas
A long-term regional project compares bite/sting observations, retained samples, species behavior and treatment records. Over years, several famous “dangerous species” reputations are revised. Some remain legitimate hazards; others were historically over-attributed. Persistent individual Pokémon can appear repeatedly without becoming research property.

### What Was in the Water
A settlement experiences several episodes across a decade: one real contamination event, one distribution-system problem without toxic exposure, one seasonal ecological change that mimics the old symptoms, and one unresolved historical sample. The arc connects Drinking Water, Groundwater, Health Surveillance, Cases, Metrology and Public Memory.

## Encounter contracts

### Warehouse Exposure Alarm

Narrative premise:
An alarm activates while workers and Pokémon are still in a distribution building. The immediate goal is to clear people from the potentially affected area and secure an investigation perimeter.

FULL version:
- moving civilians/workers;
- protected evacuation route;
- possible wild/hostile Pokémon with WITHDRAW or BLOCK_ROUTE behavior;
- exact PTU toxic mechanics only if a validated Move/Ability/Item/field effect is actually present;
- semantic playback of exclusion zones and responder actions.

Capability dependencies:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including interception/forced movement for live evacuation objectives;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline if attacks occur;
- status lifecycle if exact PTU Status effects occur;
- terrain/weather/hazards/zones/reactions only for exact validated battlefield hazards;
- move-specific behavior;
- abilities;
- items, especially if exact protective equipment or antidotes are used;
- Trainer Features/perks if relevant;
- AI legal-action infrastructure;
- AI tactical policy for EVACUATE/WITHDRAW/CLEAR_ROUTE;
- Minecraft/Cobblemon/Craftics adapter/playback.

REDUCED version:
Resolve the alarm, evacuation and exposure opportunity entirely in world state. Move workers and noncombatants out before battle. Freeze a safe static arena. If confrontation remains, run a conventional battle. Afterward, toxicology sampling and exposure assessment continue separately. No custom poison zone is created.

### Venomous Bite Field Survey

Narrative premise:
A field team documents a bite/sting incident while attempting to leave a remote survey site.

FULL version:
The subject, support team and wild Pokémon may move toward separate exits; the encounter may include withdrawal rather than KO as the primary objective.

Dependencies:
- targeting/range/LoS — required for ordinary attacks;
- base movement — required;
- complete movement — needed for pursuit/interception/withdrawal behavior;
- lifecycle/damage/status — needed only for exact PTU effects actually invoked;
- move-specific behavior and abilities — PARTIAL family dependence;
- AI tactical policy — needed for withdrawal/escort goals;
- adapter/playback — needed for semantic field representation.

REDUCED version:
Record the bite/exposure before combat. Evacuate the affected subject in world state. If another Pokémon still confronts the party, run a static battle with remaining legal combatants. Care and toxicology proceed afterward. The transcript does not infer dose.

### Suspect Spring Closure

Narrative premise:
A spring used by travelers is temporarily closed after a toxicology signal. Investigators need to collect samples while visitors and wild Pokémon continue to approach the site.

FULL version:
Requires route control, protected sampling positions and objective-aware movement.

REDUCED version:
Travel/access state closes the spring before the encounter. Sampling is a non-combat world action. Any battle occurs on a nearby static approach and has no environmental Poisoned effect unless an exact authoritative mechanic applies.

## Canon questions carried forward

- Which Ouros institutions conduct toxicology testing?
- Which biological toxins are authored by species/region?
- Which industrial/environmental agents exist in setting technology?
- What environmental exposure rules exist in Caelo?
- Does Ouros need qualitative exposure bands or any numeric model outside PTU mechanics?
- What information from a toxicology case is private?
- Which samples can be retained and for how long?
- When can a public advisory name a suspected source?
- How are wild Pokémon treated after suspected exposure without creating ownership?
- Which PTU items/Features actually govern antidotes, protective equipment or environmental toxin response?
