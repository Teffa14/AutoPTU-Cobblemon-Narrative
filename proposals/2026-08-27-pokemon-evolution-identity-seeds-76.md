# Pokémon Evolution & Identity Continuity Seeds — Pass 76

Status: PROPOSED / NON-CANON. Names, places, institutions and practices below are candidates only.

These seeds use the architecture in `design/pokemon-evolution-identity-continuity-extension.md`. None establishes Evolution legality, branch rules, custom species, custom forms, custom thresholds or mechanical benefits.

## Same Name, New Silhouette

A recurring local worker has known one of the party's Pokémon for months. On the next visit, the Pokémon has evolved. The worker initially hesitates because the silhouette is different, then recognizes a stable nickname, old routine or documented shared event.

Use:

- demonstrate identity continuity without exposition;
- create a callback to earlier visits;
- let actor knowledge update through observation rather than omniscience.

No inferred consequence:

Recognition does not create friendship, Loyalty, authority or a reward.

## The Expectation Board Was Wrong

A learning group has been informally recording predictions about a known Pokémon's future Evolution. The authoritative result later contradicts the most popular prediction.

Follow-up play:

- compare the old claims with the actual event;
- correct the board while preserving the earlier entries as history;
- investigate why the prediction became common;
- distinguish reasonable inference from hidden mechanical knowledge.

This seed works best with a canonically valid branch where observers genuinely cannot know the result in advance. The exact species cannot be chosen until source review.

## The Old Harness

A partner evolves and an issued harness, carrier or protective fitting may no longer be appropriate.

The quest is not "get a stronger harness because the Pokémon is stronger." It is an inspection and handoff problem:

- Shared Equipment checks the exact item instance;
- authoritative physical/capability data informs fit review;
- the old item may be adjusted, returned, reassigned or retired;
- Travel decides whether the Pokémon is actually legal for any mobility role.

The Evolution itself grants no mount permission.

## First Day Back at the Nursery

A Pokémon returns to a nursery or care site it used earlier in life, after Evolution.

Possible callbacks:

- staff records still point to the same `pokemon_id`;
- a room or routine once used by the Pokémon is physically different now;
- a caretaker remembers an earlier care episode;
- newer staff know only the current form and learn the history from records.

Do not infer adulthood, parenthood or reproductive eligibility from Evolution.

## The Wild Individual With the Old Mark

A previously observed wild Pokémon appears again after Evolution. A safe, already-established marker, scar pattern, tag, route history or observation chain may support the conclusion that it is the same individual.

The player can update the ecological record without claiming the entire local population evolved.

If the identity evidence is weak, preserve uncertainty.

## Two Witnesses, One Evolution

Two residents tell what sounds like a disappearance-and-arrival story: one familiar Pokémon stopped appearing, and a different Pokémon began using the same place shortly afterward.

The investigation can connect the two reports through:

- timestamps;
- stable routine;
- photograph provenance;
- care/registration history;
- direct witness evidence;
- a later authoritative identity record.

The answer does not need to be theft, capture or replacement.

## The Door Fits Differently Now

A persistent Pokémon's changed body shape makes an old route or fixture worth reviewing.

Examples:

- a narrow staff passage;
- a sleeping alcove;
- an issued enclosure;
- a service-counter gap;
- an old transport compartment.

Minecraft geometry can make the problem visible, but exact footprint/capability consequences must use authoritative data rather than render scale alone.

## The Team Role Everyone Assumes Changed

After Evolution, NPCs begin assuming the Pokémon should take a more prestigious, dangerous or visible role.

The actual decision remains with:

- player/actor intent;
- authoritative mechanical capability;
- workplace/institutional assignment rules;
- the Pokémon-agency layer.

This seed creates social pressure without converting species progression into a mandatory character arc.

## The Photograph Before the Change

A public display, archive or personal collection still uses an older image of a now-evolved Pokémon.

Questions can include:

- should the display be updated or preserve the historical image?
- should both images appear with dates?
- who has authority to revise the caption?
- does the current public know they are the same individual?

Public Memory/Archives own the publication decision. Pass 76 only provides the identity link.

## The Registration That Needs a Projection Update

An institutional record still contains an older species/form projection after a valid Evolution.

The underlying authorization may remain completely valid. The task is to reconcile presentation without treating the old credential as fraudulent.

This seed connects Pass 76 to Credentials without inventing a universal Trainer/Pokémon registration system.

## A Partner Changes Without Resetting History

Long-form callback arc.

Stage 1: establish the Pokémon's routines, known places, public contacts and persistent history before Evolution.

Stage 2: record expectations without promising a result.

Stage 3: the authoritative Evolution occurs through a mechanically valid process once implementation exists.

Stage 4: revisit earlier locations. Different actors update at different speeds because they have different knowledge.

Stage 5: secondary systems review only what actually changed: equipment fit, route geometry, public projection, care notes or work assignment.

Stage 6: months later, characters refer naturally to events from both stages of the same individual's life.

The arc has no hidden "bond reward" and no requirement that Evolution be framed as becoming better.

## Three Photos, One Pokémon

Noncombat mystery.

Three images show apparently different evolutionary stages at different dates. Records are incomplete and one caption is wrong.

Evidence sources:

- timestamp provenance;
- location history;
- stable nickname/registration reference;
- documented care event;
- visual marking only where reliably distinctive;
- witness claim lineage.

Possible outcomes:

- all three are the same individual;
- two are the same and one is unrelated;
- the evidence remains insufficient.

The mystery should never solve identity from species sequence alone.

## The Evolution Nobody Saw

A persistent wild individual disappears from its usual observation zone. Later, an evolved individual appears with evidence supporting continuity, but no one witnessed the transformation.

This tests the distinction between:

- authoritative world transition;
- direct observation;
- public belief;
- later retrospective inference.

The world does not need a cutscene for every important event.

## The Choice Is Still Open

A Pokémon is mechanically eligible for more than one reviewed outcome and the governing rules give a legitimate actor a choice. The narrative pressure around that choice can come from competing expectations, institutional assumptions or practical consequences.

The generator must not decide for convenience. It records the alternatives and the authorized decision owner.

Do not use this seed until PTU/Caelo source review establishes a compatible branch.

## Observation Day

A research or care institution schedules ordinary observation of known Pokémon undergoing life-stage changes. Evolution may be one possible subject, but the event is not a forced-evolution facility.

Useful structure:

- observation slots;
- historical records;
- before/after photographs;
- public education;
- uncertainty when no transition occurs.

This provides recurring world texture without turning Evolution into a guaranteed appointment.

## Encounter candidate — Evolution During a Challenge

Status: mechanically rich / REDUCED ONLY until source/runtime gates pass.

Full intention:

A partner undergoes a legal authoritative Evolution during an active challenge while preserving the same combatant identity and exact battle continuity.

Required capability families:

- targeting/footprints/range/LoS: VERIFIED, with specific post-transition footprint tests still required;
- base movement legality: VERIFIED, with transition-specific capability tests still required;
- core calculations: VERIFIED, but Evolution-specific recalculation unverified;
- action economy/initiative: VERIFIED, but transition timing unverified;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for autonomous adaptation;
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING.

Exact additional blocker:

Authoritative Evolution transition support and mid-battle legality remain unverified.

Reduced version:

Complete the ordinary battle first. Resolve Evolution afterward as a separate authoritative progression/world-state transaction. If another confrontation is needed, start a new ordinary encounter from the new state. Cobblemon plays the animation only after the transition commits.

## Encounter candidate — Protected Observation Window

Status: full version BLOCKED; reduced version viable as world-state + ordinary battle structure.

Premise:

Observers are studying a persistent wild individual around a possible Evolution window when a disturbance makes the site unsafe.

Full version wants:

- PROTECT/WITHDRAW/CLEAR_ROUTE intent;
- moving noncombatants;
- territorial/retreat AI;
- interception or forced movement where applicable;
- active environmental state only if mechanically authoritative;
- exact adapter playback.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING when used;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING when used;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING.

Reduced version:

Observers leave the tactical area first. The potential Evolution target stays outside battle unless it is itself a legal participant. AutoPTU runs a static ordinary encounter. Observation resumes afterward if conditions still support it. Victory cannot trigger Evolution.

## Canon questions raised by these seeds

- Does Ouros culturally treat Evolution differently across regions or institutions?
- Which kinds of Evolution choices belong to a Trainer, a Pokémon, a shared decision or a purely mechanical condition under the governing rules?
- What public records, if any, track a Pokémon's current species/form?
- How much historical species information is visible versus private?
- Which environments have institutions that study Evolution without manipulating it?
- How should known wild individuals be re-identified after major physical change?
- What physical accommodation reviews are meaningful in Minecraft without inventing PTU size/capability rules?

No answer is established here.
