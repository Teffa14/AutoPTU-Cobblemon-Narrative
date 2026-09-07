# Derelict Fishing Gear / Ghost-Fishing Research Scan — Pass 333

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-07
Canon effect: NONE

## Why this scan exists

The current Ouros foundation already establishes Puerto Bruma as a working bay town with a ferry landing, market, Field Office and Tideglass Archive branch. Repository-wide searches before authoring found no dedicated owner for abandoned/lost fishing gear, ghost fishing, gear entanglement or gear-recovery provenance.

This scan therefore looks for structures that can grow outward from existing Marea Interior canon without silently declaring a local fishing fleet, a new species population, a new authority or any PTU mechanic.

## Public sources reviewed

### NOAA Fisheries — Ghostfishing in Puget Sound

URL: https://www.fisheries.noaa.gov/feature-story/ghostfishing-puget-sound

High-level evidence:

- lost gillnets, pots, traps and other gear can continue capturing organisms after the original fishing operation has ended;
- older gear may remain biologically active for long periods;
- derelict gear can affect target and non-target organisms and create navigation/habitat problems;
- surveys can discover previously unreported gear in addition to known sites.

Reusable Ouros structure:

A hazard can outlive the action, owner intent and event that created it. The current biological consequence must therefore remain separate from the historical deployment event.

Do not import Puget Sound, species, mortality figures, fishing methods or legal rules.

### NOAA Fisheries — Marine Debris Research and Removal in the Northwestern Hawaiian Islands

URL: https://www.fisheries.noaa.gov/pacific-islands/habitat-conservation/marine-debris-research-and-removal-northwestern-hawaiian

High-level evidence:

- currents can transport lost gear far from its original source;
- reefs and shorelines can accumulate gear arriving from elsewhere;
- moving nets can entangle wildlife and damage habitat;
- removal missions combine survey, prioritization and cleanup rather than treating every observed object as an identical case.

Reusable Ouros structure:

`RECOVERY_LOCATION != LOSS_LOCATION`

Finding gear in Puerto Bruma would not by itself prove that it was deployed, lost or discarded there.

### NOAA Fisheries — Derelict Fishing Net Movement in the Northwestern Hawaiian Islands

URL: https://www.fisheries.noaa.gov/feature-story/derelict-fishing-net-movement-northwestern-hawaiian-islands

High-level evidence:

- derelict nets can move after they become debris;
- a net may alternately drift, snag, move again and damage different places;
- tracking an object over time can change the interpretation of which features it threatens.

Reusable Ouros structure:

Gear needs its own persistent identity and movement history. A later observation should not overwrite earlier positions.

### NOAA Fisheries — Large Whale Entanglement Response

URL: https://www.fisheries.noaa.gov/national/marine-life-distress/large-whale-entanglement-response

High-level evidence:

- entanglement consequences can persist after the initial contact with gear;
- authorized response networks separate observation/reporting from specialized intervention;
- a sighting of an entangled animal is useful evidence without automatically resolving gear origin, duration or outcome.

Reusable Ouros structure:

Observation, response authority, rescue state and provenance are separate concerns.

Safety boundary:

This source is not used as a real-world disentanglement manual. Ouros design must not teach players to imitate hazardous wildlife-rescue procedures.

### FAO — Abandoned, Lost or Otherwise Discarded Fishing Gear

URL: https://www.fao.org/responsible-fishing/marking-of-fishing-gear/en

### FAO — Voluntary Guidelines on the Marking of Fishing Gear

URL: https://www.fao.org/responsible-fishing/marking-of-fishing-gear/voluntary-guidelines-for-the-marking-of-fishing-gear/en

### FAO — proposed marking/recovery structure

URL: https://www.fao.org/4/w3591e/w3591e04.htm

High-level evidence:

- gear marking can support ownership identification, reporting, recovery and management;
- records can distinguish gear that was lost, found, recovered or disposed of;
- a mark may identify an owner or registered operator while other evidence is still required to establish what happened;
- recovery decisions can involve navigation, habitat and continuing ghost-fishing consequences.

Reusable Ouros structure:

`GEAR_MARK_IDENTIFIES_RECORD != CURRENT_CAUSAL_RESPONSIBILITY`

A faded mark can open an archive trail without becoming automatic proof of deliberate dumping, current ownership or liability.

### FAO GFCM — Ghost gear

URL: https://www.fao.org/gfcm/activities/compliance/ghostgear/en/

High-level evidence:

- immediate retrieval can sometimes be unsafe or environmentally damaging;
- lost gear may gradually become incorporated into local habitat;
- monitoring and later reassessment can sometimes be preferable to an immediate removal attempt;
- reporting location and coordinating recovery are distinct operational steps.

Reusable Ouros structure:

A cleanup quest can contain a genuine decision rather than a single correct interact button. Removing an object can have consequences, and delaying removal can also have consequences.

### Pokémon Tabletop United community — Zenkari Living Server

URL: https://www.reddit.com/r/PokemonTabletop/comments/c2d3b4

Public description identifies Zenkari as a PTU living server with a persistent region, sessions that players can join independently and a more traditional Pokémon journey structure layered over living-world play.

Reusable lesson:

A local incident can remain persistent world state even when different player groups encounter different stages of it. Discovery, report, recovery and aftermath do not need to occur in one quest or with one party.

Do not import Zenkari geography, Gym structure, characters, server rules or homebrew.

## Cross-source design lessons

### 1. A tool can become an autonomous world problem after use ends

The original deployment event and present hazard state must be separate records. Intent does not remain attached to the object forever.

### 2. Object provenance needs time and movement

Useful fields include:

- stable gear/object ID;
- observed object type;
- mark/identifier evidence;
- known or claimed owner/operator record;
- last authorized deployment claim, if any;
- reported-loss event, if any;
- observed positions with timestamps;
- snag/transfer events;
- wildlife/habitat observations;
- recovery attempts;
- current custody/disposal state.

### 3. A mark is a lead, not a verdict

A registry match can justify contacting an actor or searching records. It does not prove when the gear was lost, whether a report was filed, whether another operator later possessed it or whether the current location resulted from deliberate disposal.

### 4. Rescue and investigation can diverge

The immediate obligation may be to protect a Pokémon or navigation route. Provenance can remain unresolved after the urgent problem is handled.

### 5. Removal can create a second decision

If gear is snagged into habitat, a removal action can itself disturb that feature. Ouros can support `REMOVE_NOW`, `STABILIZE_AND_MONITOR`, `RESTRICT_ACCESS`, `SPECIALIST_RECOVERY` or other authored decisions without making any of them universal rules.

### 6. Cleanup should leave aftermath

Recovered gear can enter custody, evidence review, repair/reuse, disposal or archive documentation. A cleared map tile should not erase the incident history.

## Ouros-specific candidate direction

Use the established Puerto Bruma bay as the receiving location while leaving gear origin unresolved. This avoids silently canonizing a Puerto Bruma commercial fishery.

Existing canon that can participate without revision:

- Puerto Bruma working bay and ferry landing;
- Marea Field Office for wildlife incidents and practical assistance;
- Tideglass Archive for route/market/local records;
- Mara Veyra as a practical coordinator who dislikes unsupported certainty;
- Dr. Nerea Sol as a researcher who can revise conclusions;
- Taro Min as an archive custodian who preserves contradictory testimony.

Candidate new facts remain PROPOSED until promoted through canon review.

## PTU / Kairos / Caelo boundary

The current repository source index routes the supplied Kairos compilation to:

- Fishing around p. 368;
- movement/terrain around p. 382+;
- status afflictions around p. 397+;
- hazards around p. 401;
- terrain/weather around p. 404+;
- ecosystem guidance around p. 437+;
- encounter construction around p. 470+;
- items/gear around p. 495+.

Those are routing aids, not Ouros authorization.

No adopted `sources/caelo` rules source was found during this pass.

Therefore this research authors no:

- net/rope item statistics;
- entanglement status;
- escape DC;
- underwater movement rule;
- current rule;
- cutting action;
- drowning rule;
- fishing check;
- rescue Feature;
- Pokémon Ability interaction;
- Move interaction;
- damage value;
- reaction timing.

## Copyright / transformation boundary

No protected plot, dialogue, named character, encounter map or campaign sequence is copied. Public sources contribute only high-level structures: persistent object hazards, provenance, reporting, movement, staged recovery, living-world continuity and institutional uncertainty.

## Research status

Research complete for Pass 333.
Canon promotion: NONE.
Primary reusable output: derelict-gear provenance and recovery decision architecture.