# The Cache Was Empty for a Reason — Exploration Seed 410

Status: PROPOSED / NON-CANON
Canon authority: NONE
Date: 2026-09-10

## Premise

A field team reaches a known resupply point on a difficult route and finds less emergency material than its records led it to expect.

The missing stock is a problem because somebody now depends on it. The scene does not begin by declaring theft, sabotage or corruption.

Several explanations can remain simultaneously plausible until evidence narrows them: a prior team used supplies during an emergency; an authorized holder transferred material elsewhere; a scheduled replenishment was delayed; a reservation superseded an older plan; the inventory record is stale; a resource was returned to a different custodian; or material is genuinely missing.

None of these causes is canon-approved by this proposal.

## World-state structure

The cache is useful only if it is represented as persistent world state rather than a resettable loot container.

Relevant evidence can include a WorldResource identity, current holder or storage state, reservation lineage, custody transfers, holder-history transitions, delivery notices, route access, replenishment obligations and the private knowledge of people who actually handled the stock.

A party arriving later receives only information that is physically visible or actually communicated to them. A faction relationship does not create knowledge of the cache history by itself.

If an NPC team reached the cache earlier while the player was elsewhere, its legitimate actions can already have changed the state. If nobody visited, the simulation must not manufacture a prior use merely to create a mystery.

## Institutional pressure

More than one organization may depend on the same cache without sharing motives or authority.

One office may care about emergency readiness. A survey group may need specific equipment. A local maintenance crew may own the replenishment obligation. A route steward may control access. An independent traveler may have used supplies under a genuine emergency exception.

Their disagreement can concern responsibility, timing, evidence quality and future allocation rather than morality.

No global faction score decides who is trusted. Decisions use concrete relationships, permissions, records, communications and observed conduct already available to the deciding actor.

## Investigation outcomes

A complete resolution can establish a mundane authorized use, a delayed handoff, a documentation gap, a replenishment failure, a legitimate emergency consumption, unresolved provenance or actual loss.

Partial success is valid. The party can restore enough supply to make the route safe while leaving the historical question open. It can identify where the chain of evidence breaks. It can also discover that two records are both accurate but refer to different semantic cuts.

The important persistent consequence is the revised state and evidence, not a forced dramatic reveal.

## Reduced implementation version

This version requires no new AutoPTU battle mechanic.

Use existing world-agent systems for semantic time, travel, schedules, obligations, communications, permissions, WorldResource identity, reservation lineage, holder-aware handoffs, custody evidence and bounded holder history.

Any dangerous environmental change occurs between world-state revisions rather than as an unsupported tactical hazard. Carrying or consuming supplies remains ordinary narrative/world-state handling unless exact rules have been admitted.

The objective can end when the team has enough evidence to choose a safe next action, restores critical stock, communicates the shortage or leaves to obtain replacements.

## Mechanically rich version

A later implementation may place the cache inside a route where the party must reach it, protect a carrier, extract an injured actor, preserve scarce supplies or withdraw once the practical objective is complete.

This version must use only capabilities verified by engine tests/contracts. The adapter must not implement substitute PTU rules.

Targeting/footprints/range/LoS: VERIFIED only in audited scopes. Any unusual footprint, line-of-sight obstruction or range interaction remains individually gated.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Dragging, forced slides, interception, knockback or rescue reposition depend on this family.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL. Any special interaction that consumes, refunds, interrupts or reorders actions needs exact support.

Full turn/round lifecycle: PARTIAL. Timed extraction windows, delayed collapse, phased route closure or turn-count survival conditions depend on this family.

Full stateful damage pipeline: PARTIAL. Injury or damage that must survive tactical resolution into persistent-world consequences requires this pipeline.

Status lifecycle: PARTIAL. Complex or persistent conditions cannot be assumed.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism. Flooding, unstable ground, falling debris, reactive zones, wind, visibility shifts or weather phases require explicit evidence.

Move-specific behavior: individually gated.

Abilities: PARTIAL / individually gated. The current Java evidence covers a narrow Ability-triggered legal approach-Shift plus temporary-effect seam and nothing broader.

Items: individually gated. The cache contents do not acquire PTU Item effects merely because the narrative calls them supplies or equipment.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for audited ordinary scopes. Carry, interact, repair, rescue, use-cache and extraction actions require explicit legal-action admission if tactical.

AI tactical policy: BLOCKING for conserve-supplies, recover-cache, protect-carrier, rescue-first, objective-aware withdrawal and disengage-after-objective behavior.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative cache quantity/state, interaction acknowledgements, persistent environmental objective state and non-KO completion.

## Narrative fallback rule

If any rich encounter requires an unverified capability family, run the reduced version without changing the premise.

A shortage, disputed record and field decision remain narratively meaningful without simulated knockback, timed hazards, item activations or tactical carry rules.

## Provenance

High-level inspiration only:

Pokémon Emerald Enhanced public project material contributed the abstract structure of several organizations offering different work, relationships and access in an open world.

Pokémon Cave Escape public descriptions contributed the abstract structure of finite resources, route pressure and escape planning as the central challenge of a confined exploration space.

No protected prose, characters, plots, faction identities, maps, encounters, rewards or distinctive mechanics are copied.

## Canon questions before promotion

The route and cache location need a canon owner.

The organizations with legitimate access need to be selected from established Ouros institutions or proposed separately.

The stocked resources and replenishment responsibility need setting approval.

Any emergency-use exception needs a world-rule contract rather than an invented convenience for this quest.

Species, encounter composition, environmental danger and battle involvement remain open.

Any Skill, Edge, Feature, Move, Ability, Item or hazard mechanic requires PTU-source verification and engine admission before use.
