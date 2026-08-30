# Ritual, Tradition, Pilgrimage, and Site-Memory Continuity Extension

Status: PROPOSED ARCHITECTURE
Canon effect: NONE until individually approved
Pass: 153

## Purpose

Ouros needs to remember living traditions without making them omniscient history records or automatic supernatural mechanics. This extension tracks how communities transmit practices, attach meaning to routes and places, disagree about origins, interrupt or revive observances, and reinterpret inherited stories over time.

The layer is intentionally narrow. It records social-historical continuity and attributed meaning. It does not decide metaphysical truth.

## Authority boundaries

### This extension owns

- persistent identity for a tradition or named practice;
- named/local variants;
- relationships among variants where evidenced;
- practice elements and their version history;
- observance episodes;
- pilgrimage participation episodes as cultural participation records;
- tradition-linked route/site associations as attributed relationships;
- transmission events;
- reinterpretation and revival events;
- local cessation/dormancy;
- community disputes about meaning or continuity;
- historical attestations of practice;
- participant roles within a specific observance;
- explicit uncertainty and provenance around all of the above.

### Existing systems keep authority over

Travel/Expedition:
- physical departure, route traversal, delay, arrival, camp, vehicle, navigation, and travel outcome.

Material Culture / Heritage / Archaeology / Archives:
- object identity, construction, custody, physical dating evidence, archival documents, preservation, excavation, and material provenance.

Investigation / Claims / Testimony:
- hypotheses about what happened historically;
- testimony lineage;
- evidentiary support/conflict;
- unresolved questions;
- canonical-truth separation.

World Agency:
- actor knowledge, goals, motives, choices, participation decisions, and reactions.

Organizations / Civic / Credentials:
- organizational identity;
- offices and mandates;
- ownership;
- legal authority;
- access permission;
- credentials.

Ecology / Science:
- observed environmental facts;
- biological relationships;
- weather/ecological measurement;
- causal scientific interpretation.

AutoPTU:
- tactical combat facts explicitly covered by BattleSpec and verified mechanics.

Minecraft/Cobblemon/Craftics:
- rendering and playback of already-decided state only.

## Core identifiers

### `tradition_ref_id`

Persistent identity for the tradition as a historical-social continuity object.

Suggested fields:

```yaml
tradition_ref_id: trad:example
primary_name: Example Tradition
status: ACTIVE
first_attestation_ref: evidence:...
current_self_descriptions:
  - ...
associated_community_refs:
  - community:...
confidence: ATTRIBUTED
canon_status: PROPOSED
```

Identity must not be inferred from name alone. Two practices can share a label. One practice can have several names.

### `tradition_variant_id`

A distinguishable local, temporal, linguistic, organizational, household, route, or interpretive form.

Variant relationships are explicit:

- `DOCUMENTED_DESCENDANT`
- `DOCUMENTED_INFLUENCE`
- `SHARED_ORIGIN_CLAIM`
- `PARALLEL_VARIANT`
- `DISPUTED_RELATIONSHIP`
- `RELATIONSHIP_UNKNOWN`

A variant is not automatically a corrupted original.

### `practice_element_id`

A versionable unit inside a tradition, for example:

- walking a route segment;
- carrying an object;
- stopping at a location;
- reciting a text;
- wearing a color or garment;
- preparing food;
- performing music;
- maintaining silence;
- exchanging gifts;
- staging a contest or game;
- placing a non-mechanical offering;
- visiting a memorial;
- observing a date or season.

This is descriptive. It grants no combat effect.

## Tradition lifecycle

Recommended states:

- `ACTIVE`
- `SEASONAL`
- `DORMANT`
- `REVIVED`
- `CONTESTED`
- `TRANSFORMED`
- `LOCALLY_DISCONTINUED`
- `HISTORICALLY_ATTESTED`
- `UNKNOWN_CONTINUITY`

A single global state can be misleading, so locality/variant scope is required where relevant. One settlement may stop a practice while another continues it.

## Event model

### `tradition_transmission_event`

Records evidence that knowledge/practice moved between people or generations.

```yaml
event_type: TRANSMISSION
from_actor_or_group_ref: ...
to_actor_or_group_ref: ...
variant_id: ...
medium:
  - ORAL
  - PARTICIPATORY
  - HOUSEHOLD
  - APPRENTICESHIP
  - SCHOOL
  - ARCHIVAL
  - INSTITUTIONAL
  - MEDIA
transmitted_elements:
  - ...
evidence_refs:
  - ...
uncertainty: ...
```

Transmission never implies perfect copying.

### `observance_episode`

A concrete occurrence.

```yaml
observance_id: obs:...
tradition_ref_id: trad:...
variant_id: var:...
start_time: ...
end_time: ...
site_refs:
  - ...
participant_refs:
  - ...
practice_elements_performed:
  - ...
practice_elements_omitted:
  - ...
interruptions:
  - ...
world_fact_refs:
  - ...
record_refs:
  - ...
```

A scheduled observance that was cancelled is different from one that occurred.

### `pilgrimage_episode`

Tracks cultural participation, not traversal physics.

```yaml
pilgrimage_id: pil:...
tradition_ref_id: trad:...
participant_refs:
  - ...
intended_route_ref: route:...
travel_episode_ref: travel:...
ritual_stops_completed:
  - ...
participant_declared_completion: true
community_recognition_state: ...
notes: ...
```

Travel still decides whether the participant physically reached places. This layer can record that those travel facts satisfied a locally defined practice element.

### `reinterpretation_event`

Records a change in publicly or locally expressed meaning.

Causes may include:

- newly found records;
- archaeology;
- political transition;
- ecological change;
- disaster;
- migration;
- generational disagreement;
- tourism;
- organizational sponsorship;
- contact with another community;
- direct observation of a relevant Pokémon;
- explicit decision to preserve a practice while changing its explanation.

A reinterpretation changes attributed meaning, not past facts.

### `revival_event`

Required when evidence shows a meaningful interruption followed by renewed practice. Revival must not silently rewrite an interrupted history as unbroken continuity.

### `route_change_event`

A pilgrimage/procession can keep continuity after landslide, construction, flooding, border closure, habitat protection, or local choice changes its physical course. Travel owns the new traversable path. Tradition continuity records how participants interpret the change.

## Site association model

A site can carry several simultaneous relationships:

```yaml
site_ref: place:...
tradition_associations:
  - tradition_ref_id: trad:a
    relation: VENERATED_SITE
    attributed_by: community:a
    start_attestation: ...
  - tradition_ref_id: trad:b
    relation: MEMORIAL_STOP
    attributed_by: community:b
    start_attestation: ...
  - tradition_ref_id: trad:c
    relation: DISPUTED_ORIGIN_SITE
    attributed_by: organization:c
    start_attestation: ...
```

These associations do not establish ownership, legal access, archaeology, ecology, or metaphysical status.

## Material anchors

Traditions often use objects: bells, masks, stones, standards, garments, books, plaques, tools, vessels, carvings, or ordinary household items.

This layer stores only the relationship:

```yaml
material_anchor_ref: object:...
tradition_ref_id: trad:...
role: PROCESSIONAL_STANDARD
role_start: ...
role_end: ...
claim_scope: ...
```

Material Culture owns the object's identity and provenance. A replacement object can inherit a ritual role without pretending to be physically ancient.

## Claim model

Tradition claims must identify claimant and scope.

Examples:

```yaml
claim_type: ORIGIN_STORY
claimant_ref: community:...
proposition: "The first observance began after event X"
confidence: COMMUNITY_TRADITION
source_refs:
  - testimony:...
  - archive:...
```

```yaml
claim_type: EXTRAORDINARY_POKEMON_ASSOCIATION
claimant_ref: household:...
proposition: "Species/entity X appeared here during the old winter"
confidence: HISTORICALLY_TRANSMITTED_CLAIM
canonical_truth_status: UNRESOLVED
```

The same claim can be important to characters while remaining unresolved in canonical truth.

## Extraordinary Pokémon evidence ladder

Do not collapse these states:

1. `NAMED_IN_TRADITION`
2. `REPRESENTED_IN_MATERIAL_CULTURE`
3. `INVOKED_IN_OBSERVANCE`
4. `HISTORICALLY_ASSOCIATED_BY_CLAIM`
5. `REPORTED_MODERN_SIGHTING`
6. `EVIDENCE_SUPPORTED_PRESENCE`
7. `DIRECT_CANON_OBSERVATION`

Only the appropriate world authority can promote between evidentiary states. A festival, prayer, statue, shrine, Pokédex entry, rumor, battle story, or old book does not silently create level 7.

## Invariants

The implementation must preserve all of these:

`TRADITION_RECORDED != CANONICAL_COSMOLOGY`

`COMMUNITY_VENERATION != SUPERNATURAL_EFFECT`

`RITUAL_PERFORMED != BATTLE_EFFECT_GRANTED`

`PILGRIMAGE_COMPLETED != MORAL_OR_INSTITUTIONAL_AUTHORITY`

`SITE_VENERATED != SITE_OWNED`

`SITE_VENERATED != SITE_METAPHYSICALLY_SPECIAL`

`ORAL_TRADITION != UNRELIABLE`

`WRITTEN_RECORD != CANONICAL_TRUTH`

`OLDEST_ATTESTED_VERSION != ORIGINAL_VERSION_KNOWN`

`VARIANT_TRADITION != CORRUPTED_TRADITION`

`MODERN_REVIVAL != CONTINUOUS_ANCIENT_PRACTICE`

`SYMBOL_REUSED != SAME_ORGANIZATION`

`LEGENDARY_ASSOCIATION != LEGENDARY_PRESENCE`

`BATTLE_WON_AT_SITE != RITUAL_FULFILLED`

`FESTIVAL_REENACTMENT != HISTORIC_EVENT_RECONSTRUCTED_ACCURATELY`

`MATERIAL_ANCHOR_FOUND != MYTH_CONFIRMED`

`COMMUNITY_BELIEF != CANONICAL_TRUTH`

`DORMANT_PRACTICE != FORGOTTEN_PRACTICE`

`ROUTE_CHANGED != TRADITION_ENDED`

`OUTSIDER_DESCRIPTION != LOCAL_SELF_DESCRIPTION`

`ONE_VARIANT_DOMINANT != OTHER_VARIANTS_FALSE`

`SHARED_SITE != SHARED_INTERPRETATION`

`OBSERVANCE_INTERRUPTED != TRADITION_ENDED`

`TRADITIONAL_ROLE != LEGAL_AUTHORITY`

`HISTORIC_BATTLE_AT_SITE != CURRENT_BATTLE_REQUIRED`

## Player-facing presentation

Players may learn:

- locally used names;
- who says a story;
- which practices they personally witnessed;
- where a route traditionally goes;
- known variant differences;
- documented dates;
- material anchors they have inspected;
- which claims are disputed;
- whether a modern observance changed from an older recorded one.

Do not expose hidden truth flags, secret Legendary presence, universal authenticity scores, or invisible "correct tradition" labels.

## Battle boundary

Ritual and tradition are world-state contexts. BattleSpec receives only explicit combatants, static/dynamic geometry supported by current contracts, and individually verified PTU mechanics.

The following are forbidden shortcuts:

- starting a battle because a procession NPC came within Minecraft aggro distance;
- making all participants combatants;
- granting buffs because a ritual animation finished;
- applying Sacred Terrain because a location is called sacred;
- spawning a Legendary because a pilgrimage completed;
- deciding historical legitimacy from battle victory;
- treating a broken decorative object as PTU damage unless an object-combat contract explicitly exists;
- using Cobblemon BattleState to decide participants, phase, HP/status, legality, or consequences.

## Encounter contract A — Procession Route Evacuation Corridor

Narrative premise: an observance must pause because a hostile tactical situation blocks a segment of its route.

Full version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if crowd lanes, hazards, or reaction windows remain live
- move-specific behavior: PARTIAL; individual audit required
- abilities: PARTIAL; individual audit required
- items: PARTIAL; individual audit required
- Trainer Features/perks: PARTIAL; individual audit required
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

Full version: moving participants, contested withdrawal, route-control objectives, Intercept/forced movement where legal, and AI that understands evacuation rather than indiscriminate KO pursuit.

Reduced version: READY at narrative-contract level using basic verified families plus individually audited combat content. Pause the observance before initiative. Move participants and material anchors outside BattleSpec. Freeze the route as static geometry. AutoPTU may produce only `IMMEDIATE_PROCESSION_ROUTE_CLEAR`. Ouros separately decides whether and when the observance resumes.

## Encounter contract B — Venerated Site Threshold Perimeter

Narrative premise: combatants threaten immediate physical access to a culturally important site while participants withdraw.

Full version dependencies additionally include terrain/hazards/zones/reactions if the site has active environmental mechanics or protection zones. Tactical AI is required for differentiated protect/block/withdraw goals.

Reduced version: READY. Participants leave the tactical slice, culturally significant objects remain non-targetable scenery outside PTU object-state, terrain is fixed, and the battle can return only `IMMEDIATE_SITE_THRESHOLD_PERIMETER_CLEAR`.

Forbidden consequences include `RITE_VALIDATED`, `SITE_SANCTIFIED`, `TRADITION_AUTHENTIC`, `LEGENDARY_SUMMONED`, `CUSTODY_TRANSFERRED`, or `HISTORICAL_CLAIM_PROVEN`.

## Encounter contract C — Pilgrim Pass Chokepoint

Narrative premise: travelers participating in a pilgrimage cannot safely continue through an immediate hostile chokepoint.

Full version dependencies:

- complete movement: PARTIAL for escort/displacement cases;
- terrain/weather/hazards/zones/reactions: BLOCKING if weather or pass hazards remain tactically active;
- AI tactical policy: BLOCKING for protect/escape/deny-route objectives;
- adapter/playback: BLOCKING for authoritative realization.

Reduced version: READY. The traveling group waits outside BattleSpec. The pass uses static geometry. Explicit combatants resolve the immediate fight. AutoPTU may return `IMMEDIATE_PASS_APPROACH_CLEAR`. Travel/Expedition then determines whether the journey continues.

## Encounter contract D — Processional Standard Handoff Perimeter

Narrative premise: a material anchor is scheduled for handoff while hostile actors threaten the area.

Full version requires verified object interaction/carrying/escort semantics, complete movement, lifecycle, tactical policy, and possibly reactions. Those capabilities are not globally verified.

Reduced version: READY. Custody is frozen before initiative and owned by Material Culture/provenance state. The object does not enter BattleSpec. The battle only resolves `IMMEDIATE_HANDOFF_APPROACH_CLEAR`. Ouros performs or cancels the handoff afterward based on actor decisions and world state.

## Adapter contract

Minecraft/Cobblemon/Craftics may render:

- crowds and processions after Ouros decides membership and paths;
- route markers;
- decorations;
- material anchors;
- paused/resumed observances;
- NPC animations;
- site dressing;
- weather visuals when weather state is already authoritative elsewhere;
- Chronicle-visible aftermath.

The adapter must not decide:

- who believes a claim;
- whether a tradition is authentic;
- whether a ritual succeeded metaphysically;
- who joins BattleSpec;
- tactical legality;
- PTU HP/status;
- Legendary presence;
- custody;
- institutional authority;
- route completion;
- historical truth.

## PTU/Caelo guardrails

Until approved source evidence and tests establish otherwise, keep UNKNOWN:

- universal ritual subsystem;
- universal religion/pilgrimage rules;
- generic prayer/divine-favor mechanic;
- prophecy mechanics;
- automatic sacred-terrain effects;
- ritual-derived stat bonuses;
- universal Legendary/deity knowledge;
- automatic Legendary encounter or capture entitlement after pilgrimage;
- generic morality/alignment system;
- species/Type/Move/Ability-based sacred authority;
- generic Skill Check that proves ritual authenticity or cosmology;
- universal ritual interruption rules;
- shrine HP/Armor/DR;
- generic processional escort mechanics;
- ritual-based encounter tables.

Any actual Sage/Blessing/Occult/Move/Ability/Item/Trainer Feature behavior must be verified individually from project-approved PTU/Caelo material and current engine tests/contracts.

## Canonization gates

Before a concrete tradition becomes canon, specify at minimum:

- community/participants;
- locally used name;
- known practice elements;
- source/provenance for origin claims;
- whether extraordinary-Pokémon associations are claim, evidence, or direct canon observation;
- physical sites/routes involved;
- current legal/access owner where relevant;
- material anchors and their provenance owners;
- known variants;
- whether continuity is continuous, interrupted, revived, or uncertain;
- what remains deliberately unresolved.

This lets Ouros have old, meaningful, changing traditions without treating folklore as an engine command or a hidden truth database.
