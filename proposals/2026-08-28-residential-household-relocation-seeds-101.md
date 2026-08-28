# Residential, Household & Relocation Seeds — Pass 101

Status: NON-CANON PROPOSALS. Every item requires continuity, originality, PTU/Caelo and implementation review before promotion.

## Design target

Use residences as persistent world-state anchors rather than disposable interiors. These seeds avoid assuming property law, rent, family structure, wealth, Pokémon ownership or recovery mechanics.

## The Repair Finished, the Family Did Not Return

A residence is physically repaired after a local incident, but only part of the household has returned. One actor still depends on a blocked route, care service or accessibility accommodation.

Playable work:
- compare repair completion with return prerequisites;
- identify the actual remaining blocker;
- update the household split state;
- avoid treating non-return as evidence of conflict.

Long callback: months later, the delayed return changes a school, workplace, shop or neighbor routine.

## The House Is Occupied, the Record Says Vacant

A public or institutional record still lists a residence as vacant while visible life has resumed.

Possible explanations:
- stale record;
- partial return;
- temporary resident;
- mistaken address identity;
- reuse of one portion of the structure;
- record revision still pending.

No fraud or trespass is inferred automatically.

## The Temporary Move Became a Year

A household left during repairs or a route closure. The temporary destination slowly became operationally normal while return remained possible.

The player can investigate:
- which original blocker still exists;
- whether a return is actually planned;
- which routines now depend on the temporary location;
- what happens to the original residence if nobody returns soon.

This supports ambiguity without forcing a permanent relocation outcome.

## The Old House Is Now the Clinic Annex

A former residence has been converted into a public or institutional use. An older resident returns and recognizes details that survived the conversion.

Content lanes:
- public memory;
- provenance of objects or renovations;
- accessibility changes;
- neighborhood adaptation;
- privacy boundaries around former residential records.

The old use does not create present ownership rights.

## Three Addresses, Two Homes

A recurring NPC appears in records at three addresses. Investigation reveals two actual residences across different periods plus one correspondence or temporary address.

The mystery is resolved through timestamps and provenance rather than a hidden deception score.

## The Pokémon Lives Here, Nobody Agrees What That Means

A Pokémon is repeatedly observed around a household and appears to sleep, eat and return there. Different witnesses call it a pet, partner, visitor, wild neighbor or family Pokémon.

Required boundary:
- preserve observations and claims;
- do not assign ownership, capture status, Loyalty, custody or combat participation without authoritative state.

Possible outcome: the ambiguity remains partially unresolved because social labels differ while mechanical ownership is clear or absent.

## The Lane Returned Before the Residents

A road or bridge reopens after a crisis, but a row of homes remains empty because utilities, sanitation, care access or habitability verification lag behind.

This visibly demonstrates that transport restoration and residential recovery are separate systems.

## The New Neighbor Knows the Old Route

A recently arrived household member recognizes a route, plant, Pokémon behavior or local practice from another region. Their knowledge creates a lead but not automatic truth.

Use to connect relocation history with observation/research without making migrant characters exposition devices only.

## The Empty House Became a Nesting Edge

A long-vacant property now has repeated Pokémon activity around its yard or structure. Reuse is proposed.

Potential lanes:
- residence provenance;
- conservation observation;
- maintenance inspection;
- public works/reuse decision;
- reduced tactical encounter only if explicit participants are selected.

Victory in battle cannot grant property, remove ecological significance or authorize demolition.

## The Child's Room Is Still Packed

A household moved temporarily, but one room remains packed and untouched because the move was always expected to reverse. Months later the return is uncertain.

Use for environmental storytelling about suspended decisions. Avoid inferring grief, estrangement or financial hardship unless authored evidence supports it.

## The Household Split Across Two Towns

Work, care, education or transport conditions cause one household to maintain two residences for a period.

The system should support:
- two valid residence links;
- different routine windows;
- travel dependence;
- changing public assumptions;
- eventual consolidation or continued dual residence.

No single `home` field should erase the other location.

## The Address Everyone Uses Is Wrong

A district was renumbered, renamed or rebuilt, but residents still use an older informal address.

Possible effects:
- deliveries go to the correct physical place despite stale labels;
- official notices appear inconsistent;
- travelers misread directions;
- older witnesses give useful but obsolete descriptions.

Cartography/communications own naming and publication. Residential continuity preserves which residence everyone actually means.

## Mystery — Five Occupancy Reports, Three Residents

Five reports suggest different people occupy a property. Reconciliation shows:
- one worker was repairing the building;
- one visitor stayed briefly;
- three actors are actual residents.

No actor is automatically lying.

## Mystery — Four Move Dates, One Relocation

Different sources cite packing day, departure day, destination check-in and address-change effective date. All four dates are correct for different stages.

Use this structure for provenance-heavy investigations where the apparent contradiction dissolves once event types are separated.

## Long arc — A Street Learns Its Residents

Phase 1: establish a compact street with recurring households, routines, Pokémon, deliveries and service dependencies.

Phase 2: one infrastructure or ecological problem affects only part of the street.

Phase 3: several households adapt differently. One stays, one relocates temporarily, one splits across locations, one closes part of the property.

Phase 4: repairs and service restoration happen on different timelines.

Phase 5: returns change local routines again. A temporary arrangement has acquired value of its own.

Phase 6: a later event reuses old address records, a vacant structure, a recurring neighbor or an altered Pokémon route as evidence.

The street accumulates history. There is no abstract `neighborhood_level`.

## Encounter — Residential Lane Withdrawal

Full intended version:
- multiple safe exits;
- residents withdrawing while explicit combatants protect lanes;
- Intercept/forced movement;
- reaction ordering;
- reviewed narrow terrain;
- tactical AI aware of withdrawal/nonparticipant spaces;
- adapter playback that keeps household actors distinct from combatants.

Dependency categories:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced version:
Residential/Crisis state evacuates all uninvolved actors before BattleSpec creation. The fight uses a static reviewed lane or courtyard. Private interiors and household goods are excluded. Victory secures only the immediate area and cannot update return, occupancy or ownership.

## Encounter — Repair-Site Perimeter Conflict

Full intended version:
- worker withdrawal;
- protected work access;
- obstacles or hazardous work zones;
- reactions/forced movement;
- objective-aware AI;
- playback.

Reduced version:
Maintenance suspends work before combat and removes workers/equipment. AutoPTU receives a static perimeter. The result may remove an immediate threat. Repair, verification and habitability remain separate later transitions.

## Encounter — Vacant House Boundary

Full intended version:
- territorial or escape-oriented AI;
- reviewed interior/exterior terrain;
- reactions;
- possible fragile-space hazards only if exact mechanics exist;
- explicit environmental interpretation outside battle.

Reduced version:
Conservation/Residential establishes observed use first. The tactical arena is a safe exterior or cleared interior. A battle result does not establish ownership, abandonment, capture entitlement, structural safety or reuse permission.

## Immediate noncombat utility

These seeds can run before tactical expansion:
- reconcile occupancy/address records;
- track temporary relocations;
- stage return reviews;
- preserve neighbor callbacks;
- represent partial residential recovery after crises;
- record reuse of former homes;
- connect residences to work, school, care, transport and service disruptions;
- maintain privacy-aware household knowledge;
- distinguish resident Pokémon observations from ownership/capture state.