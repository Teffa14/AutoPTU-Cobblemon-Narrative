# Research Scan 169 — Structural Inspection, Load Rating, Condition Monitoring, and Bridge Scour

Status: RESEARCH / PROVENANCE. Not Ouros canon.

Date: 2026-08-25

## Internal audit before research

The full repository tree was inspected before choosing this topic. The relevant existing authorities are:

- `design/architecture-built-environment-adaptive-reuse-layer.md`: persistent structure identity, physical versions, coarse condition, use history, access and adaptive reuse;
- `design/civic-governance-public-works-layer.md`: proposals, public-works projects, implementation phases and generic inspection events;
- `design/freshwater-watersheds-hydrology-layer.md`, `design/fluvial-geomorphology-channel-migration-layer.md` and related water layers: water regime and river/channel state;
- transport layers: service and route consequences when a connection is restricted;
- `design/metrology-calibration-measurement-standards-layer.md`: instrument/calibration provenance;
- `design/crisis-rescue-recovery-layer.md`: emergency closure, evacuation and recovery state.

The repo did not contain a dedicated structural-inspection/load-rating protocol. Architecture currently states that a visible crack does not automatically prove structural danger and stores `engineering_claim_refs`; Public Works records generic `inspection_events` but does not define the technical lifecycle between observation and operational restriction.

Pass 169 therefore extends those authorities. It does not create a second `structure_id`, bridge authority, public-works authority or hydrology authority.

## Research question

How can Ouros make bridges, halls, towers, stations, retaining structures and similar assets accumulate believable inspection history without turning every crack into a collapse quest or inventing an engineering simulator?

The useful design target is a persistent evidence workflow:

physical asset -> inspection event -> observations -> analysis -> condition/capacity assessment -> scoped operational decision -> repair/monitoring -> reinspection -> revised decision.

## FHWA: periodic inspection and asset history

The U.S. Federal Highway Administration describes bridge inspection as a recurring safety and asset-management process. The important reusable lesson is not any U.S. legal standard. It is that a structure has a continuing record and does not become either permanently safe or permanently unsafe after one visit.

Source:
https://www.fhwa.dot.gov/bridge/nbis.cfm

Reusable structure for Ouros:

- an asset has an inspection program separate from its physical identity;
- routine inspections and special inspections can coexist;
- condition records are dated observations/assessments, not immutable truth;
- later deterioration, repairs, changed loading or new evidence can require a new assessment;
- institutional decisions should preserve the evidence and version used at the time.

Do not import U.S. inspection intervals, legal qualifications, numerical condition codes or regulatory powers unless Ouros canon later authors equivalents.

## Load rating is separate from visible condition

FHWA maintains load-rating guidance separately from general bridge inspection and publishes bridge condition by posting status as different dimensions. A bridge can remain open under a restriction; a posting can change even when the physical structure itself has not suddenly transformed.

Sources:
https://www.fhwa.dot.gov/bridge/loadrating/
https://www.fhwa.dot.gov/bridge/nbi/posting.cfm
https://www.fhwa.dot.gov/bridge/nbi/no10/posting25.cfm

Reusable design lesson:

```text
physical condition != evaluated load capacity != operational posting != route availability for every user
```

This is valuable in Ouros because it allows consequences more interesting than OPEN/CLOSED:

- pedestrians and light service continue while freight reroutes;
- a historic bridge remains physically intact but a new bus type exceeds an authored restriction;
- a repair restores one element but a conservative restriction remains pending reinspection;
- the restriction changes because the assessment method or known loads changed, not because the bridge visibly worsened that day.

A load rating in Ouros should remain a scoped institutional engineering assessment. It must not become a PTU Power Capability, Weight Class calculation or Minecraft block-strength formula.

## Damage inspections after events

FHWA guidance distinguishes unscheduled damage inspection from routine inspection. Environmental or human-caused events can trigger a targeted review whose immediate output may be a restriction, closure, repair need or further in-depth inspection.

Source:
https://www.fhwa.dot.gov/bridge/nbis/t514021.cfm

Reusable Ouros pattern:

storm / impact / fire / earthquake / flood / construction incident
  -> physical event authority writes what occurred
  -> structure receives special-inspection trigger
  -> inspector records observations
  -> engineering assessment evaluates implications
  -> access/load decision is revised if warranted
  -> public works handles repair
  -> reinspection verifies what changed.

The incident does not author its own structural conclusion. Likewise, a battle near a bridge cannot write `bridge_unsafe=true` merely because attacks hit scenery.

## Scour: invisible or temporary evidence can matter

USGS and FHWA bridge-scour material is especially useful because it demonstrates a failure mode that may be difficult to infer from the visible deck. Flow can remove material around foundations; peak scour can also be missed if the hole later partially refills.

Sources:
https://www.usgs.gov/centers/oregon-water-science-center/science/bridge-scour-monitoring-oregon
https://www.usgs.gov/publications/ground-penetrating-radar-a-tool-monitoring-bridge-scour
https://water.usgs.gov/water-resources/memos/memo.php?id=696
https://www.fhwa.dot.gov/engineering/hydraulics/bridgehyd/poaform.cfm

Reusable structures:

- underwater/foundation condition can require dedicated observations;
- one post-flood visual inspection need not reconstruct the maximum condition that occurred during the event;
- continuous or repeated monitoring can preserve transient evidence;
- sensor state and structural state must remain separate;
- streambed observations belong to hydrology/fluvial context while the engineering assessment belongs to this protocol;
- a high-flow event can trigger inspection without proving damage.

This connects cleanly to Ouros Metrology and Timekeeping. A sonar or other sensor, if such technology is canon-authored, needs its own calibration, clock and coverage provenance.

## Pokémon: Skyarrow Bridge as persistent infrastructure and social change

The official episode “The Lost World of Gothitelle!” uses Skyarrow Bridge as more than scenery. The story contrasts a period while the bridge was still under construction with the later completed connection; the completed bridge changes mobility enough that a prior Water Taxi service disappears.

Source:
https://www.pokemon.com/us/animation/seasons/14/episode-21-the-lost-world-of-gothitelle

Reusable high-level structure:

```text
infrastructure project
  -> new physical connection
  -> travel behavior changes
  -> older service loses role
  -> affected actors preserve memory of the earlier network
  -> the structure becomes a landmark with social history
```

For Ouros, structural inspection can produce similar long-lived consequences without copying the episode. A load restriction may temporarily revive an old ferry. A replacement bridge may preserve the old crossing name. A historic operator may remember how traffic patterns changed after reconstruction.

Do not copy Gothitelle, Sally, the time-memory plot or the specific Water Taxi story.

## Pokémon: a collapse is an event, not an engineering diagnosis

The official “Training Daze” recap includes a bridge collapsing beneath characters. It is useful only as a reminder that Pokémon stories can use infrastructure failure as an immediate scene transition.

Source:
https://www.pokemon.com/us/animation/seasons/chronicles/episode-13-training-daze

Ouros should add the missing persistent layer afterward:

collapse event -> closure -> rescue -> evidence preservation -> structural investigation -> temporary crossing -> repair/replacement decision -> later inspection history.

A cinematic collapse should never establish the cause automatically.

## PTU community lesson: encounters can create consequences without every physical object becoming a rule

Public PTU campaign logs repeatedly show that GMs use physical environment as narrative framing while keeping the actual battle manageable. One useful example from a campaign log has a player alter a tree, discover a Pokémon protecting eggs and solve the resulting problem by restoring the environment instead of converting every object into a combat subsystem.

Source:
https://www.reddit.com/r/PokemonTabletop/comments/wudfhz

This was processed previously for nesting research, so Pass 169 does not treat it as a new primary inspiration source. It is retained only as an internal cross-check on a broader design rule: structural stories should often resolve critical physical state outside the battle grid, then hand a static legal arena to AutoPTU if confrontation remains.

New PTU searches in this pass did not yield a sufficiently strong public bridge-inspection campaign log to justify importing a specific structure. No source is invented to fill that gap.

## PTU 1.05 cross-check

Public PTU 1.05 material defines Technology Education as governing machines/technology and explicitly includes examples such as repairing vehicles or machinery. It also defines Groundshaper/Mold the Earth as concrete tactical terrain-changing mechanics.

Sources:
https://pturpg.wikidot.com/skills
https://pturpg.wikidot.com/type-ace

Mechanical guardrails:

- Technology Education does not automatically define structural-engineering inspections, bridge capacity or universal repair DCs;
- Groundshaper is a PTU capability/feature interaction with specific terrain effects, not civil engineering;
- Mold the Earth cannot be used as an automatic bridge repair, foundation stabilization or scour countermeasure;
- Strength/Power-like capabilities, where present, must never be substituted for a load rating;
- Minecraft blocks cannot be summed into safe capacity.

The complete Caelo corpus was not recovered reliably in this pass. Super PTU Online Helper was not exposed as an invocable capability. No Caelo inspection rule, structural DC or helper output is invented.

## Design extraction for Ouros

The strongest reusable principles are:

1. Keep physical condition, engineering assessment, load/capacity assessment and operational restriction separate.
2. Treat inspection as a dated evidence-producing event, not an omniscient safety verdict.
3. Preserve special inspections after storms, impacts, earthquakes, fires or unusual observations.
4. Allow restrictions short of closure.
5. Require verification/reinspection after repairs rather than assuming completion equals restored capacity.
6. Keep sensor monitoring separate from the structure itself.
7. Allow hidden or transient foundation problems such as scour to create evidence gaps without procedural omniscience.
8. Let route restrictions create secondary travel, freight, emergency-service and public-memory consequences.
9. Preserve historical assessments. A bridge may have legitimately carried a different restriction ten years ago.
10. Let “nothing happened” inspections matter as baselines.

## Canon boundary

Nothing in this research establishes:

- which bridges or structures exist in Ouros;
- an Ouros engineering profession, regulator or inspection agency;
- inspection intervals;
- numerical load-rating formulas;
- legal vehicle weights;
- construction codes;
- universal repair methods;
- collapse probabilities;
- structural HP;
- environmental damage rules;
- Technology Education DCs;
- Groundshaper civil-engineering effects.

All proposed applications remain NON-CANON until separately approved.