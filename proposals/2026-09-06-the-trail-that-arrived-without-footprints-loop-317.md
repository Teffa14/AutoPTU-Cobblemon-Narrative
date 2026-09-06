# The Trail That Arrived Without Footprints — Pass 317

Status: PROPOSED / NON-CANON
Date: 2026-09-06

## Premise

A managed habitat corridor begins generating repeated reports of a familiar Pokémon scent at crossings where observers cannot find matching fresh tracks, feeding traces or visual sightings. A Tracker-capable partner can follow part of the odor path, so the reports are not simply dismissed as imagination. The open question is what the trace actually represents.

No geography, species, institution or incident in this proposal is canon until explicitly adopted.

## Core mystery

The investigation separates several questions that NPCs initially collapse into one:

1. Is a chemical trace really present?
2. What source produced or carried it?
3. When and where was it deposited?
4. Has it remained in place, moved or been transferred?
5. Does it indicate current Pokémon presence?
6. Does it identify a particular species or individual with sufficient confidence?

A correct scent detection can still support an incorrect causal story.

## Spatial structure

The corridor has at least four useful evidence sites.

The first is a reported crossing where odor is detectable but visible tracks are weak or absent. The second is a sheltered control point where old material can persist longer. The third is a maintenance/storage area containing reusable equipment that moves between sectors. The fourth is a habitat edge with independent evidence such as fresh feeding signs, camera observations or known resting sites.

The party should be able to revisit these locations after a weather or operational change and compare what remains.

## Candidate explanations

Canon review can select one or combine compatible causes:

- the animals used the route earlier and the odor outlasted visible evidence;
- maintenance equipment transferred the trace between zones;
- a worker, crate, fabric or tool carried material from a legitimate handling site;
- rain or airflow removed evidence unevenly, leaving an apparently discontinuous path;
- the relevant Pokémon changed its activity time while traces persisted;
- another source produces a similar odor and was misidentified;
- an approved deterrent or attractant altered movement in an unintended way;
- an observer over-interpreted a Tracker result as proof of current presence;
- genuine current movement occurs by a route that produces little visible evidence;
- deliberate baiting or false trail placement occurred, but only if canon needs an adversarial version;
- two causes overlap.

The premise does not require sabotage.

## Quest progression

The player first records the exact reported evidence instead of accepting `Pokémon crossed here` as a fact. A source-validated Tracker-capable Pokémon can attempt the PTU-authorized tracking interaction if the project authority confirms the mechanic.

The party then compares the trace with visual, acoustic and environmental evidence at the other sites. Maintenance logs can establish which carts or tools moved where. A storage location may reveal that the strongest trace sits on an object rather than on the route surface. A later revisit after rain, cleaning or an operational pause can test persistence and transfer hypotheses.

The conclusion should identify what is supported, what remains uncertain and what additional observation would discriminate between remaining explanations.

## Stakeholders

A habitat observer knows historical movement patterns but may treat a familiar smell as direct proof. A maintenance contractor knows equipment routes but may not know ecological significance. A local producer or route user may be blamed if the trace appears near their property. A field researcher can enforce better sampling discipline. A Pokémon handler may know that a particular partner has Tracker but cannot claim capabilities the rules do not grant.

Conflict comes from evidence quality, operational costs and reputational consequences rather than mandatory villainy.

## Environmental storytelling

A wheel or reusable canvas cover can retain a trace in a place where no matching footprints exist. A sheltered beam can hold an older scent while an exposed path has been washed clean. Fresh feeding signs can exist away from the reported crossing. Maintenance maps can show equipment transfer between sectors. A camera or field log can establish that the detector was correct about a scent but wrong about timing.

The player learns the distinction between trace and actor through the world rather than through a single exposition conversation.

## Full encounter version

The mechanically rich version can place the investigation during an active containment or rescue problem after a chemical trace leads multiple actors toward the wrong sector. A verified Tracker-capable Pokémon may need to distinguish a useful trail from transferred contamination while ordinary tactical movement and a separate environmental hazard constrain access.

If the scenario authors a dynamic odor plume, deterrent field, irritant zone, weather-driven transport, scent-based concealment or a Move/Ability that changes the field, each effect needs its exact PTU and engine contract. Existing LoS cannot be repurposed as smell geometry.

The full version may include combat only if the narrative situation creates one. The mystery remains solvable without fighting.

## Reduced implementation version

The reduced version requires no calculated scent simulation.

World/narrative state uses authored facts such as `TRACE_PRESENT`, `TRACE_WEAK`, `TRACE_CONTAMINATED`, `TRACE_SOURCE_UNRESOLVED`, `TRACKING_ATTEMPT_RECORDED` and cross-channel observations. These labels describe evidence; they are not PTU statuses.

Environmental changes occur between scenes. There are no scent radii, wind vectors, decay formulas, tracking bonuses, contamination penalties or odor damage. Tracker use, if enabled, follows the exact project-authoritative PTU procedure rather than a new subsystem.

The route itself can use ordinary static movement/navigation. The complete narrative premise survives through comparative observation, revisitation and provenance-backed conclusions.

## Capability dependencies for the full version

Targeting/footprints/range/LoS: VERIFIED for ordinary audited spatial targeting. Scent detection, scent-based targeting and odor propagation are outside that verification.

Base movement legality: VERIFIED for ordinary movement and sufficient for the reduced version.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Needed only if rescue, panic, machinery or authored forced displacement becomes part of the rich encounter.

Core calculations: VERIFIED within audited contracts. No scent formula is introduced.

Action economy/initiative: VERIFIED within audited contracts for structured scenes.

Full turn/round lifecycle: PARTIAL. Required if a plume, cleaning cycle, ventilation state or delayed environmental change updates during tactical rounds. AutoPTU-Java PR #385 provides narrow round-history state evidence, not a complete environmental lifecycle.

Full stateful damage pipeline: PARTIAL. Not required for the investigation premise. It becomes relevant only if a separately authored hazard causes actual damage.

Status lifecycle: PARTIAL. No generic `scented`, `nauseated`, `masked` or similar condition is invented.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by subfamily. Dynamic odor fields, wind-carried zones, environmental masking or reaction rescues depend on this family.

Move-specific behavior: PARTIAL. `Odor Sleuth` or any other Move must use verified semantics. The research source indicates Odor Sleuth grants Tracker; no additional field effect is assumed.

Abilities: PARTIAL. Flavor text cannot create tracking, immunity or scent-field effects without exact authority.

Items: PARTIAL. Sample containers, field notebooks or ordinary maintenance objects can be world props. PTU Item effects require validation.

Trainer Features/perks: PARTIAL. Any Feature modifying tracking, Perception, Survival or investigation needs direct source validation.

AI legal-action infrastructure: VERIFIED within audited contracts.

AI tactical policy: BLOCKING for general autonomy. Autonomous choice between competing scent hypotheses, hazard-aware pursuit or rescue priorities cannot be assumed.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING end-to-end. Particles or client presentation may illustrate an authored trace but cannot become authority for its existence, identity or PTU tracking legality.

## PTU/Caelo questions before full implementation

PTU 1.05 publicly documents `Tracker` and links it to olfactory pursuit with Perception procedures; `Odor Sleuth` can grant Tracker. The project must still validate exact wording and numbers against its authoritative PTU/Caelo material before implementation.

No adopted Caelo olfactory overlay was located during Pass 317. Caelo modifications to Tracker, Perception, Survival, Moves, environmental effects or sensing remain `UNVERIFIED`.

## Canon questions before adoption

A canon pass must choose the region, habitat, infrastructure and stakeholders. It must choose any detector or source species only after confirming species behavior and available PTU capabilities. It must also establish the historical baseline, weather/maintenance context and whether the final explanation is transfer, persistence, genuine movement, masking, deliberate manipulation or concurrent causes.

The strongest version should remain interesting even when the answer is mundane: a sensor can be correct while the story built around it is wrong.