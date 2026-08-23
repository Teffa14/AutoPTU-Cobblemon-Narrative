# Ouros Museum, Collection & Exhibition Seeds — Pass 128

Status: NON-CANON PROPOSALS. Original Ouros candidates derived from high-level research patterns. No protected characters, plots, dialogue or distinctive museum scenarios copied from sources.

## 30 worldbuilding candidates

1. The Object That Never Reached the Gallery. A regional museum accessioned a river-survey instrument years ago, but it remains in storage because its condition is unstable. The public assumes it was lost.

2. Two Labels, One Fossil. A fossil was displayed for decades under one interpretation. New research changes the identification. The old label remains historically important because an entire generation learned from it.

3. The Famous Replica. A travelling replica became better known than the fragile original. When the original finally goes on display, visitors insist the real object “looks wrong.”

4. The Empty Case. A gallery case is empty because the object is on a legitimate outgoing loan. Rumors of theft spread faster than the museum's notice.

5. Storage Move Year. A museum relocates a collection because the old storage wing no longer meets its environmental needs. Hundreds of small location events become an institutional project rather than a quest for every box.

6. The Loan That Arrived Before Its Story. A visiting object reaches the host institution before translated labels and provenance notes are finished. It remains secured but not publicly installed.

7. The Museum That Has More Basement Than Gallery. Only a small fraction of the collection is visible. Researchers know the institution through storage rooms, study collections and preparation labs rather than iconic exhibits.

8. The Condition Photograph. A decades-old photograph shows a crack before a recent transport incident. The image prevents a false accusation while also revealing the object has been deteriorating longer than anyone realized.

9. The Uncatalogued Drawer. A box transferred from an older institution contains several objects with incomplete labels. Nothing is necessarily stolen; the problem is record linkage and provenance reconstruction.

10. The Cast With a Better History. A cast made for teaching survived a fire, moved between schools and museums, and became a public-memory object independent of the source fossil.

11. The Museum Closure That Wasn't a Shutdown. The public gallery closes for renovations while conservation, research and loans continue. Outsiders misread the closed doors as institutional failure.

12. The Borrowed Landmark. A small town receives a famous object for a six-week exhibit. Visitor numbers rise, transport schedules change and local businesses adapt, but the object still belongs elsewhere.

13. The Object With Three Owners in the Records. Old catalogues, family records and institutional files disagree about ownership history. Current custody is clear; historic title is not.

14. The Conservation Choice. Staff can stabilize an object in a way that preserves more original material but keeps visible damage, or restore its appearance more aggressively. Neither option produces a mechanical bonus.

15. The Exhibit Built Around Absence. A missing object becomes the center of an exhibition about provenance, loss and uncertainty rather than being silently replaced by a fake.

16. The Fossil That Cannot Be Restored. A scientifically valuable fossil remains a collection object because no authorized restoration pathway exists for it. Researchers still learn from it.

17. The Living Result. A restoration project produces a living Pokémon. The museum retains records, machine logs and the original material history, but the Pokémon becomes an actor under Pokémon Agency rather than a collection asset.

18. The Community Collection. A rural community maintains a small collection in a civic hall. It has fewer resources than a regional museum but stronger local knowledge about many objects.

19. The Specialist Who Retired. The only person who understood an old cataloguing system leaves. The records remain valid, but future staff need to reconstruct the conventions.

20. The Exhibition That Changed the Research Question. A public comparison exhibit causes a visitor to notice a pattern that researchers had not prioritized. The observation becomes a research lead, not instant truth.

21. The Object Too Fragile to Travel Again. A beloved exhibit stops touring after condition reports worsen. Future versions use a cast and archived recordings.

22. The Gallery Name Outlives the Collection. A hall keeps a historic name even after its contents and curatorial focus change completely.

23. The Restricted Shelf. An institution holds culturally sensitive objects whose records are partly visible but whose images, exact locations or access are restricted by authored stewardship rules.

24. The Deaccession Nobody Wanted to Discuss. An object no longer fits the institution's mission and another institution can care for it better. Transfer is administratively correct but emotionally controversial.

25. The Traveling Exhibit Splits. A multi-institution exhibit divides into two versions because some objects cannot make the next leg. Both versions remain legitimate descendants of the same project.

26. The Museum During the Storm. Staff relocate only the most vulnerable objects while others remain safely stored. Preparedness state determines what can be protected before the event.

27. The Security Video Is Right but the Conclusion Is Wrong. A person is correctly recorded near a missing object but had legitimate access and did not remove it. Case evidence and collection location history eventually reconcile.

28. The Misplaced Object That Was Never Missing. A catalog record points to an old storage code after shelving was renumbered. The object remained physically secure the whole time.

29. The Exhibit With Three Languages and Four Revisions. A travelling exhibit accumulates translations, terminology changes and updated scientific labels. All versions remain in Archives.

30. The Hundred-Year Collection Ledger. A museum's object-location history becomes a secondary history of floods, wars, renovations, railway openings, institutional mergers and changing scientific priorities.

## Three longer arcs

### Five Exhibitions of Meridian Natural History Hall

Year 1: a conventional regional exhibit opens using long-held specimens and casts.

Year 2: one attribution is challenged by new research. Labels are revised while the original gallery photographs remain archived.

Year 3: a travelling object arrives and draws larger crowds. Transport and public-space systems respond.

Year 4: a storm forces emergency relocation of some vulnerable holdings. Condition reports reveal older problems that predate the storm.

Year 5: the museum opens a new exhibit about how scientific interpretation changed across all four previous years. The institution becomes richer because it preserves its mistakes rather than hiding them.

### The Object With Six Locations

A single persistent item moves through excavation custody, university research, conservation treatment, museum accession, travelling exhibition and eventual return to a community collection. Every handoff preserves the same `item_instance_id` while ownership claims, custodians, interpretations and public meaning change.

The arc can connect Archaeology, Material Culture, Postal/Transport, Languages, Public Memory, Research Ethics and Institutional Review without requiring a villain.

### The Museum That Learned to Keep Less

A small institution begins by accepting nearly everything offered. Storage pressure, conservation backlog and unclear provenance accumulate. Over several years it develops collection scope, accession review, shared storage agreements, digitization, outgoing loans and carefully documented transfers to other institutions.

Success is better stewardship, not infinite collection growth.

## Encounter contracts

### Gallery Evacuation During a Collection Incident

Narrative premise:
A public gallery must be evacuated after a wild Pokémon enters through a damaged service area during installation of a temporary exhibit.

FULL version:
- civilians move toward exits;
- staff protect designated routes rather than objects as combat goals;
- wild Pokémon may attempt WITHDRAW rather than fight to KO;
- some gallery zones may become unavailable if an actual validated hazard exists;
- exhibit mounts remain physical scenery unless exact mechanics exist.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if gallery hazards are tactical
- move-specific behavior — PARTIAL, individually verify used Moves
- abilities — PARTIAL, individually verify
- items — PARTIAL if any battle item is used
- Trainer Features/perks — PARTIAL if any Feature is used
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for EVACUATE/WITHDRAW/PROTECT_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

REDUCED version:
Evacuate visitors and secure vulnerable objects in world state first. Freeze a safe gallery floorplan. AutoPTU receives only the actual combatants in a static arena. The wild Pokémon's post-battle custody/withdrawal is resolved separately according to valid rules and agency state.

### Travelling Exhibit Handoff Chokepoint

Narrative premise:
A shipment carrying a small travelling exhibition becomes stuck at a transport transfer site during a separate confrontation.

FULL version:
- cargo and staff have meaningful protected positions;
- opponents may attempt to reach or block an exit;
- the exhibit itself is not a combatant;
- custody remains with the authorized courier/institution.

Dependencies:
- complete movement/interception/forced movement — BLOCKING
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING
- targeting/range/LoS, base movement, core calculations, action economy — VERIFIED for the combat itself
- lifecycle/damage/status/move/ability/item/Feature families — PARTIAL as applicable

REDUCED version:
Keep the shipment outside the tactical grid under frozen custody state. Resolve the chokepoint fight as a conventional static battle. Afterward, Transport/Postal/Collection state determines whether the handoff can continue.

Battle victory does not transfer the objects.

### Conservation Lab Shutdown

Narrative premise:
A conservation lab suffers an equipment incident while a fragile object is under treatment. A Pokémon-related confrontation may occur nearby, but the conservation problem and combat remain distinct.

FULL version:
- technicians may need to reach safe stations;
- interactable machinery could matter only if Technology + engine contracts later support it;
- any fire, chemical, electrical or glass effect requires exact validated hazard mechanics.

Dependencies:
- complete movement/interception — BLOCKING if technicians move in-grid
- terrain/weather/hazards/zones/reactions — BLOCKING for any environmental lab hazard
- AI tactical policy — BLOCKING for CLEAR_ROUTE/PROTECT_TECHNICIAN
- adapter/playback — BLOCKING
- exact Move/Ability/Item/Feature effects — PARTIAL and individually verified

REDUCED version:
The lab performs emergency shutdown in world state, removes staff and fragile objects from the battle perimeter where plausible, and freezes a safe static arena. AutoPTU resolves only the confrontation. Conservation staff then create a new condition report; battle victory never means the object is undamaged.

## Additional quest hooks

A researcher asks players to locate the original field notebook for an accession whose modern catalogue lost excavation context.

A town wants to borrow an object for an anniversary, but the lending museum needs a condition assessment and secure transport plan first.

A community disputes an exhibit label, not the object's custody. The quest is evidence gathering and consultation rather than recovery.

A storage leak is discovered before anything is visibly damaged. Preventive maintenance becomes meaningful because preparedness state already exists.

A cast is mistaken for a stolen original after old photographs circulate without captions.

A collection object is scientifically reclassified, causing updated labels across three institutions without moving the object at all.

A closed museum receives a research request for an object that has never been exhibited.

A loan arrives during a regional transport disruption; the exhibition opening date changes rather than the world manufacturing a heist.

## Guardrails for future authors

No collection object becomes loot automatically.

No museum automatically owns what it holds.

No curator automatically knows the truth about an object.

No fossil automatically becomes a living Pokémon.

No living Pokémon becomes a museum asset.

No replica automatically deceives visitors.

No conservation treatment creates PTU bonuses.

No display case grants cover unless the battle engine explicitly models it.

No glass, hanging skeleton, mineral, fossil or machine creates a hazard by visual description alone.

No battle result settles provenance, ownership, authenticity or historical interpretation.
