# Pass 159 — Plant Pathology & Diagnostic Uncertainty Seeds

Status: NON-CANON proposals. Research provenance is in `research/2026-08-24-plant-pathology-disease-surveillance-scan-159.md`. Systems authority is `design/plant-disease-surveillance-diagnostics-protocol.md`.

These concepts are designed to create investigation, institutional memory and ecological consequences without turning every plant problem into a villain, plague or battle.

## 30 worldbuilding and quest candidates

1. **The Orchard With Two Symptoms** — two visually similar rows decline for different reasons. One traces to irrigation stress; the other remains a biological-disease case.

2. **The Blight That Was Drought** — a famous local label survives in public memory even after later evidence supports an abiotic explanation.

3. **Pathogen Without Symptoms** — a candidate organism is detected in apparently healthy plants. Researchers must decide what the result means before making a public claim.

4. **Symptoms Without Detection** — repeated tests fail to detect the leading biological hypothesis. Soil, roots, irrigation and chemical history become more important.

5. **Three Labs, One Sample** — three institutions analyze related material using different methods and produce results that are not directly comparable.

6. **The Wrong Fungus** — a conspicuous fruiting body near a dying tree dominates rumors, but the fungal occurrence may be secondary or unrelated.

7. **The Nursery Batch Under Hold** — a batch is temporarily withheld from distribution while diagnosis remains unresolved. Supply Chains and Markets feel the delay without implying contamination is confirmed.

8. **The Clean Sample** — one negative result becomes a political talking point even though the sampled area was tiny.

9. **The Pruning Tool Link** — cases appear along a maintenance route. The shared tool is a hypothesis, not a solved cause.

10. **Imported Rootstock Question** — symptoms appear after new plant material arrives, but the timing alone does not prove introduction through that shipment.

11. **The Wind Year** — unusual weather changes where symptoms appear, making an old map of affected plots misleading without making it fraudulent.

12. **The Irrigation Look-Alike** — leaf symptoms closely match a known disease, but the strongest pattern follows one lateral of the irrigation network.

13. **The Treatment Helped for the Wrong Reason** — an intervention improves the plants while leaving open which component of the intervention mattered.

14. **The Disease That Stayed Local** — a dramatic case affects one courtyard for years without spreading regionally. Its importance comes from continuity, not scale.

15. **The Famous Sick Tree** — a landmark tree becomes culturally important during a long diagnostic case. Public Memory persists after the plant recovers or dies.

16. **The New Method Revises the Old Outbreak** — archived samples are retested years later. Historical estimates change, but old decisions remain understandable in context.

17. **The Asymptomatic Row** — plants between two affected plots show no visible symptoms. Their role in the pattern remains uncertain.

18. **The Social-Media Blight Panic** — photographs of one symptom spread faster than diagnostic work. Communications and Public Memory must preserve the difference between report and conclusion.

19. **The Poison-Type Scapegoat, Again** — a Poison-type Pokémon is repeatedly photographed near declining vegetation. Timeline evidence later shows the decline began before its arrival.

20. **The Grass-Type Volunteer** — a companion Pokémon participates in a survey because it chooses to stay with the team. Its type gives no diagnostic ability by itself.

21. **The Greenhouse With Two Clocks** — symptom progression and sensor logs initially appear inconsistent because one monitoring system had time drift.

22. **The Wrong Locality Label** — a diagnostic sample was correctly tested but attached to the wrong plot during intake. Metrology/Identity-style provenance, not a new villain, resolves the discrepancy.

23. **The Closed Trail, Healthy Trees** — access is restricted as a precaution while nearby plants remain healthy. A closure is a management state, not evidence of infection.

24. **The Old Variety Problem** — only a historic cultivar appears affected. Botanical Gardens, Archives and Agriculture reconstruct its provenance before anyone claims unique susceptibility.

25. **The Secondary Invader** — a biological agent is genuinely present, but evidence suggests it colonized tissue already damaged by drought or roots.

26. **The Forest Edge Pattern** — dieback follows an edge that was created by road widening years earlier. The strongest explanation may involve microclimate rather than a transmissible agent.

27. **The Quarantine Ends** — an institution lifts a temporary material hold after evidence improves. Ending the precaution does not mean the original concern was foolish.

28. **The Case With No Single Cause** — soil compaction, irrigation timing and a biological agent all contribute. The final record explicitly supports mixed causation.

29. **The Diagnostic Atlas** — decades of maps show how symptom definitions, survey coverage and methods changed. Comparing raw maps without their legends creates false trends.

30. **Nothing Happened This Survey** — a routine plant-health survey detects no unusual condition. Years later it becomes a valuable baseline for a genuine change.

## Longer-term arcs

### Five Springs at Alder Orchard

Year 1 begins with scattered leaf symptoms and a provisional diagnosis. Year 2 adds irrigation data that weakens the first explanation. Year 3 introduces a positive biological detection in only one block. Year 4 changes pruning and water management while preserving several hypotheses. Year 5 shows recovery in some rows and persistence in others.

The arc can end with a supported mixed-cause assessment rather than a single culprit. The orchard becomes a Chronicle location whose maps, staff knowledge, plant lineages and survey methods improve over time.

### From Nursery to Valley

A nursery batch becomes the focus of a movement hold after a plant-health concern. Several settlements already received related material before the hold. Each site produces different observations because environment and cultivation differ.

The long arc follows provenance, distribution, sample comparison, public communication and institutional coordination. A later regional pattern may support, weaken or complicate the original nursery hypothesis. No malicious introduction is required.

### The Dieback Atlas

A forestry institution inherits thirty years of inconsistent records about a slow tree decline. Older surveys used visual maps; later ones used fixed plots and better diagnostics. Fires, road changes, drought and fungal observations overlap.

Players can help reconstruct which trends are real, which are artifacts of method and which remain unknowable. The payoff is a better regional evidence system and fewer false alarms, not necessarily a cure.

## Encounter contracts

### Orchard Diagnostic Survey

FULL premise: researchers need to inspect two symptom zones while wild Pokémon move through the orchard and may withdraw when disturbed.

Capability dependencies:

- VERIFIED baseline: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.
- BLOCKING: complete movement for dynamic crossing/withdrawal; AI tactical policy for `WITHDRAW`, `PROTECT_RESEARCHER`, `CLEAR_ROUTE`; Minecraft/Cobblemon/Craftics adapter/playback.
- BLOCKING only if tactically invoked: terrain/weather/hazards/zones/reactions for moving weather, debris, protected rows or environmental effects.
- PARTIAL if exact mechanics are invoked: status lifecycle, move-specific behavior, abilities, items, Trainer Features/perks.

REDUCED: survey and wildlife movement resolve in world state. Researchers leave the tactical area. Any independent confrontation uses a static legal arena and no plant-disease mechanic.

### Nursery Quarantine Transfer

FULL premise: staff move a documented batch from intake to an isolated greenhouse while a separate wildlife disturbance blocks the route.

Capability dependencies:

- BLOCKING: complete movement; AI tactical policy; adapter/playback.
- PARTIAL: items only if protective or handling gear needs battle semantics.
- No plant-health Status is created.

REDUCED: custody, plant movement and staff routing occur outside combat. AutoPTU resolves only the independent conflict after the transfer is paused.

### Forest Dieback Transect After Storm

FULL premise: technicians revisit monitoring plots after a storm while resident Pokémon attempt to leave and debris changes safe access.

Capability dependencies:

- BLOCKING: complete movement; terrain/weather/hazards/zones/reactions if debris or storm state affects the grid; AI tactical policy; adapter/playback.
- PARTIAL if an exact Move/Ability/Item is used by a combatant.

REDUCED: unsafe plots close before combat, wildlife/researchers relocate through world state and AutoPTU receives static safe geometry.

### Diagnostic Review Meeting

Non-combat. The group compares symptom maps, sample provenance, fungal records, irrigation history, toxicology, weather, soil and test methods. `UNRESOLVED`, `MIXED_CAUSATION_SUPPORTED` and `RULED_OUT_FOR_SCOPE` are valid outcomes.

## Factions and NPC archetypes

**The Field Diagnostician** values progression patterns and site history over dramatic single samples. They can be wrong without being incompetent.

**The Nursery Operations Lead** wants fast decisions because every day of a hold affects inventory and customers. Their pressure is structural, not automatically corrupt.

**The Archive Pathologist** works from old samples, labels and photographs and can revise historical interpretations without claiming the past was falsified.

**The Orchard Crew Observer** lacks formal laboratory authority but has years of repeated local observations that can expose when a pattern truly changed.

**The Biosecurity Reviewer** cares about movement risk even before causality is fully established. Their mandate can conflict with market or travel interests without creating a villain faction.

**The Public Communicator** must explain provisional findings without turning uncertainty into either panic or false reassurance.

## Non-inferences

None of these concepts authorizes plant disease as PTU Status, `Blight Condition`, Poisoned, ambient Spore, terrain, hazard, spawn modifier, capture modifier, regional form, evolution trigger or Minecraft block rule.

All plant-health conclusions remain evidence-scoped and NON-CANON until separately approved.