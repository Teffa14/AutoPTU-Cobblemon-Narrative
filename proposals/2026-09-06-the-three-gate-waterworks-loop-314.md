# The Three-Gate Waterworks

Status: PROPOSED / NON-CANON
Date: 2026-09-06
Pass: 314

## Premise

A water-distribution complex is producing contradictory downstream conditions. One branch is repeatedly starved while another overtops, yet the available operating record appears normal. The facility serves several legitimate needs, so the mystery is not designed around a mandatory villain.

The player must understand the physical system, establish what changed, decide which evidence is reliable and choose how to restore service without casually sacrificing another stakeholder's need.

No region, institution, settlement, species, historic incident or named NPC becomes canon through this proposal.

## Spatial structure

The facility is built around three connected control branches.

The intake/distribution branch governs ordinary delivery toward inhabited or productive areas.

The maintenance bypass exists to isolate parts of the system during repair or emergency operation.

The habitat side-channel preserves a lower-flow route used by wild Pokémon and surrounding ecology.

These labels describe functional roles only. Canon names and ownership are unresolved.

The player can enter from at least three directions: the public spillway path, a maintenance gallery, or a normally dry bypass culvert. Each route reveals different evidence and gives a different initial model of the problem.

## Environmental evidence

The dungeon should explain itself through physical traces before exposition.

Old mineral bands show historic water levels. Fresh debris lines indicate a recent high-flow episode. Tool wear around one mechanism can establish recent handling without identifying who handled it. An outdated maintenance diagram describes intended flow. Nesting or feeding traces may show that wild Pokémon used a branch before conditions changed, but species-specific interpretation remains unverified until source-backed.

A gate operation must provide local feedback. The player can hear flow change, see a gauge move, watch a downstream marker respond, or observe water retreat from a nearby threshold. Remote effects should later be confirmed through exploration rather than hidden behind trial-and-error.

## Mystery candidates

Several resolutions are intentionally compatible with the same premise.

A maintenance crew may have left the bypass in an emergency configuration and recorded the job incorrectly.

A legitimate safety response may have diverted flow while another department continued using an obsolete schedule.

A person may have opened the habitat branch to protect a vulnerable wild area during extreme conditions, creating real downstream costs without intending broader damage.

Mechanical deterioration can combine with deliberate operation, allowing concurrent causes rather than a false choice between accident and interference.

These are authoring candidates. A future canon pass should choose only one causal history after region, institutions and ecology are established.

## Stakeholder candidates

A veteran gatekeeper understands long-term operating patterns but may lack recent records.

A junior surveyor has precise current measurements but little historical context.

A habitat observer recognizes changes in wild activity but cannot automatically diagnose civil infrastructure.

A maintenance lead prioritizes safe isolation before any restart.

A downstream user representative wants predictable delivery and may have suffered real losses during the disruption.

Each perspective can be correct about part of the problem. None receives omniscient access to the full state.

## Exploration loop

The first pass establishes the contradiction and gives the player a partial map.

Exploration then produces a causal model: which gate states can physically create the observed marks and accessible routes?

The player compares that model with records and witness knowledge. The result can expose a bad record, a hidden bypass state, a physical fault, an intentional operation or a combination.

A repair choice changes the world. A branch may reopen, a bypass may be isolated, or the side-channel may receive a negotiated minimum flow. These outcomes remain proposed until the corresponding world-state adapters and canon institutions exist.

A later revisit should show consequences physically. Water lines change, previously flooded maintenance space becomes accessible, another corridor submerges, wild occupancy shifts, and different stakeholders remember the earlier decision.

## Puzzle philosophy

The puzzle is a network of causes, not three arbitrary switches.

Changing one gate should affect a bounded and predictable portion of the facility. The player should rarely need to traverse the entire site merely to learn whether a control had an effect.

At least two independent evidence paths should support the main deduction. A missing document or inaccessible room can make the answer harder without hard-locking the adventure.

## Reduced implementation version

The reduced version can run without dynamic water simulation or AutoPTU combat.

Represent each branch with authored states such as `OPEN`, `RESTRICTED`, `DRY`, `FLOODED` and `INSPECTION_ONLY`. Gate operations occur between scenes and update a deterministic route graph. A flooded edge is simply unavailable; a drained edge becomes traversable after the authored transition.

No current pushes actors. No water-level change happens mid-turn. No environmental damage, reaction rescue, delayed pulse, persistent status or dynamic hazard zone is required. Weather can remain presentation-only.

Investigation uses physical observations, private knowledge, records and world-state changes. The same stakeholder conflict and causal answer survive intact.

If a tactical scene occurs, place it on stable dry nodes and restrict it to verified basic spatial legality, movement, core calculations and initiative.

## Full mechanically rich version

A later implementation can allow water levels to change during an active encounter. Current can displace actors, narrow ledges can create rescue opportunities, gates can change tactical connectivity, and a sudden release can turn a dry route into a hazard zone.

Exact capability dependencies:

Targeting/footprints/range/LoS — required for combat or rescue across channels and platforms. Current audited status: VERIFIED within audited contracts.

Base movement legality — required for ordinary stable traversal. Current audited status: VERIFIED.

Complete movement including push/pull/knockback/interception/forced movement — required for current-driven displacement, interception and assisted rescue. Current audited status: PARTIAL.

Core calculations — required for deterministic tactical arithmetic. Current audited status: VERIFIED.

Action economy/initiative — required for structured contested actions. Current audited status: VERIFIED.

Full turn/round lifecycle — required if gate changes, surge timing or water-state updates occur at phase boundaries. Current audited status: PARTIAL.

Full stateful damage pipeline — required if current collision, falls or hydraulic hazards cause mechanical harm. Current audited status: PARTIAL.

Status lifecycle — required only if a persistent condition is explicitly authored and source-validated. Current audited status: PARTIAL. This proposal creates no custom water status.

Terrain/weather/hazards/zones/reactions — required for current zones, slick or flooded terrain, hydraulic surges and reactive rescues. Current audited status: MIXED / PARTIAL / BLOCKING by subfamily.

Move-specific behavior — required only for specifically authored Moves that alter traversal, water or rescue. Current audited status: PARTIAL.

Abilities — required only if an Ability changes terrain, movement, weather or interaction. Current audited status: PARTIAL.

Items — required only when equipment has mechanical effects. Current audited status: PARTIAL.

Trainer Features/perks — required only when a Feature changes legality, timing, inspection or rescue. Current audited status: PARTIAL.

AI legal-action infrastructure — required for autonomous actors to select only legal options. Current audited status: VERIFIED.

AI tactical policy — required for general autonomous positioning, rescue and hazard avoidance. Current audited status: BLOCKING for general autonomy.

Minecraft/Cobblemon/Craftics adapter/playback support — required for authoritative visible gate, water, movement and battle execution. Current audited status: PARTIAL / BLOCKING end-to-end.

## Full-version fallback

Keep water and gate state changes between tactical scenes. Convert moving current into presentation and fixed blocked edges. Remove forced movement, reactive rescue, mid-round water changes, environmental HP damage and persistent statuses.

The dungeon still contains multiple entrances, evidence, competing interests, a causal hydraulic puzzle and durable changes after repair.

## Long-term arc potential

A first visit establishes the facility and resolves the immediate contradiction.

A later seasonal visit can expose a previously submerged service chamber or close a route that was formerly dry. This creates environmental re-reading without requiring a retcon.

A subsequent institutional conflict can focus on how water is allocated, who maintains the bypass and how habitat needs are represented. Those questions should only become canon after regional governance and ecology are approved.

## Unresolved canon and mechanics questions

Which region can support this facility without contradicting established geography?

Which institution owns, operates and audits it?

Does an established Ouros habitat corridor already provide a suitable ecological stake, or should this remain a standalone location?

Which PTU skills or capabilities govern inspection, swimming, rescue and interpretation of environmental traces in the authoritative project source?

Does Caelo define any relevant water/current overlay? No Caelo source was found in the inspected narrative repository, so this remains UNVERIFIED.

Which Pokémon species can plausibly interact with the site? Species selection must follow approved ecology and behavior evidence, not type-theme convenience.
