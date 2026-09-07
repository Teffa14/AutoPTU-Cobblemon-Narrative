# Pollinator phenology observation contract — Pass 322

Status: DESIGN CONTRACT / NON-CANON
Date: 2026-09-06

## Purpose

Provide a reusable boundary for seasonal flowering, pollinator observations, management decisions, and delayed outcomes without allowing environmental presentation, incomplete surveys, or franchise flavor to become hidden mechanical authority.

## Authority chain

Authoritative narrative state should preserve this chain:

`feature identity -> authored phenological state -> observation event -> observer/receiver -> interpretation -> decision -> feature-scoped consequence -> later outcome evidence`

Pollinator presence or movement, when authored, remains its own state and does not collapse into the plant state.

## Required separations

### Phenological state versus rendering

A Minecraft flower block, particle, texture, or seasonal visual is presentation. It cannot assert `BLOOM_OPEN`, nectar availability, pollination success, or tactical terrain behavior unless authoritative state already says so.

### Observation versus absence

`VISITATION_NOT_OBSERVED` records a bounded survey result. It does not mean `POLLINATOR_ABSENT`.

Observations require feature, time or semantic time-window, observer/source, and provenance sufficient to distinguish repeated visits.

### Visitation versus outcome

Observed visitation does not prove adequate pollination. Lack of immediate fruit/seed evidence does not prove failure. Delayed outcomes need their own authored event and receipt path.

### Regional summaries versus local features

A district calendar or average cannot overwrite patch-specific state. Upper block, low pocket, margin, and other persistent features keep separate identities and histories.

### Knowledge versus world truth

NPCs know only observations, reports, decisions, or consequences they directly perceive or receive through an explicit information path. Hidden ecological state does not leak into dialogue or policy reasoning.

## Temporal revisit contract

A revisitable site must preserve feature identity between visits. New state can be authored through semantic time progression or explicit world events. A later observation may supersede an interpretation without deleting earlier provenance.

The same physical location can legitimately produce different observations at different times.

## Decision and consequence integration

Institutional action should target explicit features or practices. Examples include a monitoring plot, mowing strip, irrigation review, access rule, buyer forecast, or habitat margin.

A review or correction modifies only consequences supported by the new decision. It must not reset unrelated ecological, social, or economic effects.

## PTU / Caelo boundary

Franchise Pokédex material is ecological inspiration only. PTU mechanics for Perception, Survival, environmental traversal, Moves, Abilities, Items, Trainer Features, weather, or zones must be sourced from the project-authoritative rules before numeric checks or combat effects are authored.

Do not infer the implementation of Honey Gather from its videogame/Pokédex text. Do not infer Pollen Puff, Sweet Scent, Powder-family behavior, weather interactions, or custom pollen conditions from narrative flavor.

No adopted `sources/caelo` directory was found during Pass 322, so Caelo-specific phenology/pollination rules remain UNVERIFIED.

## Capability dependency contract

The reduced narrative version requires no dynamic battle environment. It can use ordinary routes, authored feature state, semantic time, explicit observations, NPC receipt, decisions, and consequences.

The mechanically rich version must declare exact dependencies:

- targeting/footprints/range/LoS: ordinary targeting may use verified contracts; vegetation, pollen or weather-dependent visibility requires dedicated evidence;
- base movement legality: verified standard traversal only;
- complete movement: required for forced movement, wind displacement, rescue, interception, pushes or pulls;
- core calculations: verified deterministic arithmetic only;
- action economy/initiative: verified ordinary action ordering only;
- full turn/round lifecycle: required for scheduled within-battle environmental transitions beyond specifically verified lifecycle seams;
- full stateful damage pipeline: required for any environmental damage interaction;
- status lifecycle: required for any persistent condition;
- terrain/weather/hazards/zones/reactions: required for dynamic pollen, wind/rain, vegetation or reactive environmental zones;
- move-specific behavior: each ecological/tactical Move independently verified;
- abilities: each Ability independently verified;
- items: each Item independently verified;
- Trainer Features/perks: each Feature independently verified;
- AI legal-action infrastructure: may enumerate verified legal actions;
- AI tactical policy: required before autonomous agents can reliably reason about changing phenological/environmental opportunities;
- Minecraft/Cobblemon/Craftics adapter/playback: presents authoritative state and semantic events but must not decide rules or hidden ecology.

## Fallback rule

If any rich dependency is unavailable, preserve the narrative premise through authored between-scene transitions and feature-scoped evidence. Do not recreate missing PTU rules in the Minecraft adapter.

## Acceptance tests for later implementation

A conforming implementation should be able to demonstrate that two surveys of the same block at different times can disagree without corrupting history; an unobserved pollinator does not become globally absent; a Minecraft visual change does not create authoritative phenological state; an NPC without receipt cannot cite another team’s survey; a corrected forecast does not erase the old forecast’s economic consequence; and a rich encounter falls back to the reduced world-state version when tactical dependencies are unsupported.