# Marea / Sendero wild nesting disturbance fixture — Pass 234

Status: PROPOSED FIXTURE. Not canon-approved.
Date: 2026-09-03

## Purpose

Exercise the wild nesting and parental-care contract in an already established Marea corridor without freezing species, biome or final coordinates before the global world substrate is validated.

This fixture is designed to remain narratively valid if Marea's legacy coordinate anchors require an explicit migration after worldgen lock.

## Existing canon reused

The fixture uses only established geographic relationships:
- Puerto Bruma connects toward Loma Clara through Sendero del Vidrio;
- Estación Mirador branches near the upper route;
- route traffic, residents and field observers already exist as plausible observation channels.

No new settlement, country, biome or canonical species population is created here.

## Scenario premise

During a seasonal dependence window, a persistent wild caregiver group establishes or reuses a nesting/dependent-young site close enough to a Sendero travel segment that ordinary human traffic becomes ecologically relevant.

The first visible symptom is not an attack. Repeated observations show:
- one or more adults carrying food/resource material along a repeatable route;
- increased vigilance near one section of trail;
- warning or shadowing behaviour when travellers linger;
- reduced attendance after repeated disturbances;
- changing wildlife use immediately around the site.

The actual cause must be discovered from evidence. NPCs do not begin with omniscient knowledge of an active nest.

## Species gate

`caregiver_species_id` and `dependent_species_id` remain null until all of these are satisfied:
- the global Ouros world is generated and its version/seed are frozen;
- the relevant Sendero segment has actual Minecraft biome IDs/tags and physical terrain inspected;
- the species is enabled for Ouros content;
- Cobblemon native spawn/habitat conditions are compatible;
- official/PTU evidence permits the proposed care behaviour or the relationship is explicitly authored with a provenance grade;
- persistent-individual reconciliation prevents generic duplication.

Example official species evidence such as Mandibuzz, Bombirdier, Leavanny or Kangaskhan is research provenance only. None is assigned to Marea by this fixture.

## Fixture state

```yaml
fixture_id: marea_sendero_nesting_disturbance_234
status: PROPOSED
region_id: marea
route_id: sendero_del_vidrio
site_ref: migration_sensitive_semantic_site
caregiver_species_id: null
dependent_species_id: null
nest_site_id: null
occupancy_state: ACTIVE
dependence_stage: dependent_young
disturbance_pressure: low
vigilance_state: baseline
relocation_pressure: low
human_route_overlap: true
worldgen_binding_status: PENDING
```

## Initial evidence packet

A traveller or field observer can plausibly notice:
- repeated movement toward the same concealed area;
- food or nesting material being transported;
- warning behaviour at a consistent distance;
- a shift in the caregiver's route when multiple people pass;
- fewer visible visits during periods of heavy traffic.

None of these facts alone proves:
- parentage;
- Egg presence;
- number of juveniles;
- nest success/failure;
- imminent attack;
- species aggression as a global trait.

## Hidden ecological state

The ecology service may know:
- persistent caregiver IDs;
- persistent dependent IDs if already materialized;
- actual nest-site occupancy;
- recent disturbance events;
- resource/provisioning demand;
- local predator pressure;
- current relocation pressure;
- whether the site remains active.

NPCs and players receive only observations available through their access and skills/institutions.

## Event progression

### Phase A — low disturbance

Route traffic is below the local tolerance threshold.

Expected world-state behaviour:
- provisioning continues;
- caregiver remains mostly concealed or neutral at distance;
- warning displays occur only on close approach;
- no battle handoff.

Useful player action:
- observe from farther away;
- avoid lingering;
- record evidence;
- choose an alternate side path if available.

### Phase B — repeated disturbance

Several world events accumulate under one recurrence key:
- repeated close approaches;
- harvesting near the site;
- high traffic during a short interval;
- sustained observation too close to the defended area.

Expected effects:
- vigilance rises;
- caregiver attendance pattern changes;
- warning boundary expands within ecological limits;
- provisioning route may shift;
- relocation pressure increases;
- observation packets become stronger but still non-omniscient.

No combat is required.

### Phase C — management choice

Once evidence is sufficient, local actors can propose an intervention.

Candidate interventions:
- temporary route marker or closure near the site;
- redirect foot traffic for a short world-time window;
- move a harvest activity away from the site;
- reduce field-observation frequency;
- create a quiet buffer using existing terrain/route controls;
- wait for the dependence window to advance before reopening normal access.

The intervention does not instantly set `success=true`.

### Phase D — delayed verification

After an authored verification interval, new observations test whether:
- caregiver attendance returns toward baseline;
- warning behaviour decreases;
- provisioning resumes;
- relocation pressure stabilizes or falls;
- the site remains active;
- dependents reach a later independence stage.

If evidence instead shows continuing decline, the cause remains open. Possible explanations include continuing disturbance, predator pressure, resource shortage, relocation in progress or another ecological event.

Absence alone never creates `FAILED_CONFIRMED`.

## Failure-forward consequences

Poor intervention can produce:
- temporary route restriction lasting longer;
- caregiver relocation to another compatible site;
- reduced field access;
- higher human/wildlife conflict pressure;
- a missed observation/research window;
- changed resource pressure along the provisioning route;
- institutional disagreement about access management.

Do not default to Egg/juvenile injury or death without evidence and governing mechanics.

## Optional structured escalation

### Trigger

Ouros may decide structured combat begins only if a caregiver or other actor actually engages after ecological warnings fail.

The trigger cannot be `player crossed Minecraft radius X` alone. It must come from persistent behaviour state plus current world facts.

### Full intended version

The caregiver attempts to keep intruders away from a defended area while preserving a path back toward dependents.

Potential rich mechanics:
- movement interception;
- forced displacement rather than KO-focused behaviour;
- defended-zone reactions;
- terrain-aware path control;
- escape/disengagement when separation is restored;
- objective-oriented tactical AI;
- weather or hazard interaction if the world context requires it.

Capability dependencies:
- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING outside verified slices;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING as a complete family;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING end-to-end.

Current AutoPTU-Java evidence from `21e0b02e5ff17132f3a7ed04007784884323df12` verifies a bounded movement-landing consequence executor and trap/status consequence seam. It does not verify this encounter's complete displacement, defended-zone or tactical-policy requirements.

### Reduced battle version

If escalation occurs before rich mechanics are ready:
- Ouros freezes the ecological scene at battle handoff;
- dependent young/Eggs remain outside tactical participation;
- AutoPTU runs an ordinary legal battle on static simple terrain using only reviewed mechanics available to the selected combatants;
- no custom escort, reaction zone, forced displacement, moving hazard or weather phase is invented;
- retreat/end-of-threat is mapped back to the ecological scene through a semantic result;
- after battle, the nest ledger updates disturbance and relocation pressure without inferring injury/death beyond authoritative outcomes.

The narrative premise remains unchanged: a caregiver escalated because the defended area stayed threatened.

## Noncombat reduced implementation

This fixture can ship before rich adapter behaviour exists.

Minimum implementation:
- persistent semantic nesting site;
- disturbance counter/history;
- caregiver/dependent persistent IDs;
- simple activity/visibility projection;
- observation packets;
- route-management world event;
- delayed verification event;
- no battle required.

Minecraft presentation may be limited to visible caregiver presence, route markers and changed spawn/activity projection. Missing animations do not prevent the ecological state from functioning.

## Interaction with previous ecology contracts

### Observation/intervention loop

This fixture uses evidence accumulation and delayed verification rather than instant quest completion.

### Ecological information propagation

A caregiver warning can alter nearby species behaviour if an approved information edge exists. The warning does not globally announce the nest location.

### Ecological pulse events

A rain/resource/disturbance pulse may temporarily raise traffic compression or provisioning pressure. Pulse state modifies context but does not replace the nesting lifecycle.

### Global interaction graph

Provisioning can temporarily strengthen approved `FORAGES_RESOURCE` or `PREDATES_ON` pressure. Nest defence remains local to the site/dependent context.

## Regression assertions

1. Repeated close approaches increase disturbance more than one isolated pass.
2. Withdrawal lowers immediate threat but does not erase disturbance history instantly.
3. Caregiver absence does not automatically mark the site abandoned.
4. Management intervention requires later evidence before being judged successful.
5. A species assignment cannot become executable until worldgen and native habitat gates pass.
6. No generic Cobblemon spawn duplicates a persistent caregiver or dependent.
7. No battle starts from vanilla aggression alone.
8. If battle begins, AutoPTU decides tactical facts.
9. Rich blocked mechanics are absent from the reduced version.
10. A route closure modifies human access pressure, not Pokémon HP/status or hidden battle state.

## Promotion questions

Before canon or implementation binding:
- Which generated Sendero site has suitable terrain and cover?
- Which official species naturally fits that site under the pinned Cobblemon spawn envelope?
- Is the caregiving behaviour explicit, inferred or Ouros-authored?
- What institution or local authority may temporarily alter trail access?
- What world-time interval counts as meaningful verification?
- How are persistent dependents represented before they are independently spawnable?
- How is relocation destination selected from compatible habitat rather than quest convenience?
