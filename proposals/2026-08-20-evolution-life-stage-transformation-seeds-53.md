# Evolution, Life Stage & Transformation Seeds — Pass 53

Status: NON-CANON Ouros candidates. Original material derived from research structures. Mechanics remain subject to PTU/Caelo and implementation review.

## 1. The Pokémon Everyone Counted Twice

A research team has two years of records for a familiar wild individual. After it evolves, later observers create a new record because the appearance changed enough that nobody connects the two datasets. Players can resolve the continuity through photographs, location history and other evidence.

## 2. The Saddle That No Longer Fits

A long-serving transport Pokémon evolves. The institution pauses service while staff reassess equipment and physical suitability. Evolution does not automatically preserve or remove Mountable status; the actual capability must be re-queried.

## 3. A Rematch Everyone Expects

After a public defeat, spectators assume a Trainer will evolve their partner before the rematch. The actual Pokémon remains eligible but unresolved. The story focuses on outside expectations, preparation and what the player actually chooses.

## 4. The Moonlit Census

Researchers monitor a recurring wild gathering because prior years recorded Evolution events there. The gathering remains important even in a year when no Pokémon evolves.

## 5. Old Photo, New Name

A museum receives a photograph of a famous Pokémon taken before its Evolution. A newer cataloguer labels the old image with the current species name, creating a small but meaningful archival error.

## 6. The Transferred Partner

A Pokémon evolves shortly after changing custodians. Public discussion credits the new Trainer as the cause. The records only establish timing, not causation.

## 7. The Released Returnee

A former partner released years earlier is observed again after evolving in the wild. The same `pokemon_entity_id` preserves its earlier history without restoring command authority to the former Trainer.

## 8. Renovation After Evolution

A household discovers that a newly evolved resident needs different physical space. The result can create a small home-improvement project without inventing medical distress or a mechanical housing penalty.

## 9. Workshop Reassessment

An institutional Pokémon evolves and staff must re-evaluate which tasks remain appropriate. Species change does not automatically grant professional certification or work consent.

## 10. The Branch Nobody Chose Yet

An important branching Pokémon remains mechanically eligible for more than one path across several arcs. NPCs can have opinions, but the project keeps the decision unresolved until an authorized choice or rule resolves it.

## 11. The Stone in the Display Case

A historically significant Evolution item belongs to a museum collection while a Trainer has a legitimate reason to request its use. The conflict concerns custody, preservation and access; possession of the item never triggers Evolution by itself.

## 12. Mountain Research Station

A station exists near a location associated with a known Evolution condition. Researchers compare confirmed events across years and distinguish local folklore from actual mechanical evidence.

## 13. The Wrong Cause

A Pokémon evolves after a festival, and residents decide the ceremony caused it. Later records show the authoritative trigger may have been unrelated. The festival can remain culturally important even if the causal claim is wrong.

## 14. After the Change

A Pokémon that recently evolved spends several scenes adapting to a different body, reach or routine. The narrative records observable adjustment without inventing disobedience, Injury or emotional distress.

## 15. New Shape, Same Rival

A recurring rival's Pokémon evolves between meetings. The AI may only use information the rival has actually observed about the player's team; the evolved roster does not grant perfect knowledge.

## 16. The Habitat Shift Hypothesis

A known wild individual changes where it spends time after Evolution. Researchers test whether the new pattern follows species ecology, food availability, social position or another cause.

## 17. The Nursery Record Continues

A Pokémon first recorded as an Egg, then juvenile, later evolves. The same entity links Egg provenance, hatching history, care records and Evolution history without treating lineage as a power score.

## 18. The Evolution That Happened Offscreen

A non-player wild individual evolves during an offline period under a deterministic, fully represented trigger. The Chronicle records the event only if the system can authoritatively establish when/how it happened; otherwise the next observation records the changed state and leaves timing uncertain.

## 19. First Day Back at Work

An evolved service Pokémon returns to an institution after staff update procedures and equipment. The story can reveal that some duties remain valid while others need reassessment.

## 20. Misidentified Encounter Report

A case file treats an evolved recurring Pokémon as a second suspect/subject. Correcting the identity changes the investigation without changing what witnesses honestly saw.

## 21. The Team Slot Debate

A Trainer's partner evolves and public commentators assume the roster's tactical role will change. Actual team use remains a Trainer decision backed by legal Moves/Abilities rather than species stereotypes.

## 22. The Evolution Item Supply Route

A legal Evolution path requires an item that is locally unavailable. The resulting adventure can concern sourcing, trade, provenance or borrowing. The game must never force use once the item is obtained.

## 23. The Ceremony Perimeter

A protected wild gathering attracts tourists after photos of past Evolutions circulate. Conservation staff must balance access, research and disturbance without assuming every attendee will evolve.

## 24. The Archive of Unchosen Paths

A research institution records branching Evolution possibilities and historical outcomes. It intentionally separates statistical patterns from claims about what any individual Pokémon should become.

## 25. The Gym Lesson After Evolution

A battle school runs a post-Evolution tactics workshop. It focuses on rechecking legal state, movement and team interactions rather than handing out free combat bonuses.

## 26. The Familiar Cry

Observers identify a recently evolved wild Pokémon as a previously known individual through a combination of location, recordings and behavior. The system treats this as an identity hypothesis until corroborated.

## 27. The Seasonal Form Confusion

Residents mistake a reversible/seasonal form change for permanent Evolution. The case teaches the difference between species history and form-state history.

## 28. The Temporary Power Question

A battler has access to a temporary transformation but does not use it in every match. Public speculation about why remains separate from actual mechanics and private intent.

## 29. Evolution During a Crisis

A Pokémon becomes eligible during an evacuation or rescue arc. The crisis does not override the normal authorization/rule boundary. If live tactical Evolution is unsupported, resolve it only between encounters.

## 30. The Old Uniform Problem

An institutional Pokémon evolves and its existing identification harness/uniform no longer fits visually. Reissuing equipment updates appearance and records but does not create mechanical armor.

## Long arc A — The Same Pokémon

Over several years, one wild Pokémon is first photographed as a juvenile, repeatedly observed, temporarily treated at a clinic, later evolves, joins a different local group and eventually becomes associated with a landmark. Different institutions accumulate partially inconsistent records. The arc is about establishing continuity and correcting the public archive rather than capturing the Pokémon.

## Long arc B — Paths Unchosen

A branching partner has several legal future paths. Travel, research, rivals and mentors expose the player to different possibilities over time, but none secretly locks the outcome unless the authoritative rules say so. The arc can end with an Evolution, a deliberate delay, or continued uncertainty.

## Long arc C — Season of Change

Researchers observe a regional pattern where multiple wild populations reach Evolution milestones during a recurring environmental window. Over several years the pattern shifts. The story connects seasonality, conservation, ecology and public memory while preserving uncertainty about causal mechanisms until evidence supports them.

## Encounter contract — Mountain Threshold

Premise: an important Pokémon enters a location tied to an authoritative Evolution condition while a battle occurs.

REDUCED version:

Complete the battle using the pre-Evolution state. After the battle, run the authoritative eligibility/resolution transition. The next encounter uses the refreshed evolved state.

FULL version:

Evolution occurs during battle and the same combatant continues in the new state.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED baseline;
- base movement legality — VERIFIED baseline;
- complete movement/forced movement/interception — BLOCKING if footprint/occupied cells change interactively;
- core calculations — VERIFIED primitives, with an additional unverified species-transition contract;
- action economy/initiative — VERIFIED baseline, transition timing still needs contract;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING when involved;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED baseline, regeneration after Evolution requires proof;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

## Encounter contract — Ceremony Perimeter

Premise: a wild Evolution gathering is disturbed by another actor or environmental problem.

REDUCED version:

Keep the gathering and any Evolution events in world state. If combat occurs, instantiate only the immediate combatants on a static legal arena and resolve Evolution after battle unless a verified mechanic explicitly requires otherwise.

FULL version:

Persistent wild actors may evolve, reposition, protect space or withdraw during the event.

Main additional blockers: complete movement, broad zones/reactions where used, AI tactical policy and adapter/playback. Wild collective state never grants invented bonuses.

## Encounter contract — Mid-Match Breakthrough

Premise: an authoritative trigger would allow an Evolution during a major match.

REDUCED version:

Finish the current match in the existing form. Resolve Evolution immediately afterward and let the follow-up/rematch use the evolved state.

FULL version:

Continue the same transcript after live Evolution.

This remains blocked by the missing dedicated Java mid-battle Evolution contract even if other capability families improve.
