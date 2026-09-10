# The Path Depends on Who Came With You — Exploration Seed 409

Status: PROPOSED / NON-CANON
Date: 2026-09-10
Canon effect: NONE unless separately promoted through canon review.

## Premise

A compact travel bottleneck has several legitimate ways through or around it. The routes are not a menu shown by an omniscient interface. Different travelers know, notice or qualify for different options because of their actual relationships, permissions, experience, equipment and companions.

The public way is slower but broadly usable. A maintenance path may be available only to actors who were told about it or have legitimate access. A less obvious field detour may be recognized only by someone who has previously traveled nearby, received a local description, studied a relevant record or is accompanied by an actor with an established applicable capability.

No specific Ouros location, faction, species, route or capability is established by this seed.

## World-agent behavior

An actor considers only routes represented in their knowledge or reasonably inferable from evidence they possess. The simulation does not query a hidden perfect route graph and then backfill an explanation.

A route fact can enter knowledge through direct travel, visible landmarks, a conversation, a work order, a map or record, an observed traveler, or another already admitted information source. Actors can disagree about whether a route is usable because their information may differ in age or provenance.

Traveling with another actor can therefore change planning without creating a party-wide omniscience rule. The companion must actually know, communicate or perform the relevant contribution.

## Consequences that distinguish routes

The routes should differ in world consequences as well as duration. A chosen path can change arrival time, resource use, who sees the travelers, which NPCs are encountered, what environmental evidence is observed, which institution records passage, or what future route knowledge becomes available.

A shortcut can also stop being preferable. A later closure, changed permission, damaged crossing, conflicting obligation or new information may make the ordinary route the rational choice again.

## Persistent NPC participation

NPCs can use the same structure off-screen. They do not wait for the player to discover every option first.

If an NPC knows only the public road, that is what the NPC plans around. If another actor was legitimately shown a maintenance path, that route can affect the second actor's schedule. If a route change is never communicated, other agents continue making decisions from older information until they observe evidence that challenges it.

This supports natural encounters where the player asks why one group arrived early, why another group never came through the expected checkpoint, or how a local worker reached a site the player believed was inaccessible.

## Adventure uses

The route knot can support a delivery, rescue, inspection, social visit, pursuit, return journey or ordinary travel day. The route itself creates the variation.

A later story can reuse the same place after circumstances change. The interesting question becomes whether the travelers' remembered route still applies, who knows about the change and how that information spreads.

## Reduced implementation version

The reduced version requires no AutoPTU battle mechanic. It uses persistent knowledge, communications, permissions, schedules, ordinary WorldResource state, current location and existing travel/replanning abstractions.

All paths use ordinary world navigation. Any difficult terrain or environmental change is represented as persistent route state between scenes rather than simulated as an unverified tactical rule.

This version preserves the central premise: party composition and real knowledge affect which routes are considered.

## Full mechanically rich version

A later version may let a verified Pokémon Move, Ability, Item or Trainer Feature create a route affordance, or may place the crossing inside a structured encounter where actors must traverse, protect someone, carry an object, rescue another actor or withdraw after reaching the objective.

Those mechanics are admitted individually. A narrative statement that a Pokémon can help does not create a mechanical permission.

## Permanent engine dependency classification

Targeting/footprints/range/LoS: VERIFIED only in audited scopes. Required if a tactical route interaction targets actors or spaces.

Base movement legality: VERIFIED only in audited scopes. Ordinary audited Shift legality can support simple tactical repositioning but does not prove every traversal form.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Blocking, rescue reposition, forced slides, knockback and interception remain dependent on this family.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL. Any route interaction performed during structured combat requires authoritative timing and action cost.

Full turn/round lifecycle: PARTIAL. Timed access windows, delayed collapse, staged evacuation or round-triggered changes depend on this family.

Full stateful damage pipeline: PARTIAL. Route hazards cannot invent persistent damage or injury outside the authoritative pipeline.

Status lifecycle: PARTIAL. Complex continuing traversal conditions remain gated.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by mechanism. Active weather, unstable surfaces, reactive obstacles and triggered zones need exact evidence.

Move-specific behavior: individually gated. Any Move-based route affordance requires verified implementation of that Move.

Abilities: PARTIAL / individually gated. Current Java evidence covers a narrow ability-triggered approach Shift plus temporary-effect seam only; it does not authorize environmental field use.

Items: individually gated. PTU Item effects require exact verification. Ordinary narrative equipment can use established WorldResource semantics when no PTU effect is claimed.

Trainer Features/perks: individually gated. No class Feature is granted route authority by this proposal.

AI legal-action infrastructure: VERIFIED only for audited ordinary legal actions. Specialized traversal/manipulation/rescue actions require explicit admission.

AI tactical policy: BLOCKING for bypass-first, escort-first, rescue-first, protect-resource, objective-aware withdrawal and disengage-after-objective behavior.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for authoritative route-affordance interaction, companion-specific field actions, persistent route changes and non-KO objective completion.

## Canon questions before promotion

A canon review would need to choose an actual location, determine why several routes exist, decide who legitimately controls any restricted access, identify how route knowledge is recorded or transmitted, and specify whether any Pokémon-specific capability is involved.

If a Pokémon Move, Ability, Item or Trainer Feature matters, the exact rule and engine contract must be verified before canon treats it as a dependable route solution.
