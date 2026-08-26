# Infrastructure Interdependency, Outage & Restoration Research — Pass 64

Status: research/provenance only. Nothing in this file is established Ouros canon.
Date inspected: 2026-08-26

## Scope and repository-fit check

The complete repository tree was enumerated before this pass. The closest existing material was then read directly: `design/technology-energy-infrastructure-layer.md`, `research/2026-08-19-technology-energy-infrastructure-scan-29.md`, `proposals/2026-08-19-technology-energy-infrastructure-seeds-29.md`, `design/facility-maintenance-repair-inspection-extension.md`, `design/civic-governance-public-works-layer.md`, and `design/engine-readiness-snapshot-pass-63.md`.

Pass 29 already owns technical assets, utility networks, faults, maintenance, fallback plans, Pokémon-machine interaction and incident propagation. Pass 58 owns facility-level assessment, repair and reopening. Civic/Public Works owns major collective investment and construction decisions.

The remaining useful gap is narrower: how a multi-service outage is observed and bounded, how dependencies produce partial cascades, how temporary supply and backup states are represented, how restoration is sequenced, and how recovery is verified before downstream services are declared normal.

This pass therefore extends existing infrastructure design instead of creating another general utility system.

## New sources inspected

### Pokémon X/Y — Lumiose blackout and Kalos Power Plant

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Team_Flare
- https://bulbapedia.bulbagarden.net/wiki/Kalos_Power_Plant
- https://bulbapedia.bulbagarden.net/wiki/Lumiose_Gym
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_X_and_Y_Versions

Observed high-level structure:
- an upstream power-plant problem produces a downstream city outage;
- the outage changes route access and the availability of a major institution;
- restoration of the upstream source changes several downstream states at once;
- the player experiences the downstream consequences before resolving the source problem.

Reusable Ouros lesson:

An infrastructure incident should expose a dependency graph to the player through real consequences. A clinic, route gate, lift, communications room or public venue may become LIMITED or OFFLINE because of one upstream network state even when the dependent facility itself is undamaged.

Do not copy Team Flare, Lumiose, Prism Tower or the specific plot.

### New Mauville — shutdown can be the correct technical objective

Source:
- https://bulbapedia.bulbagarden.net/wiki/New_Mauville

Observed high-level structure:
- an underground technical site outlives its original urban-development purpose;
- wild Pokémon use the abandoned/repurposed environment;
- the requested intervention is to shut down a generator as a safety precaution rather than to maximize uptime.

Reusable Ouros lesson:

Restoration must not mean “turn everything back on.” Operators may isolate, de-energize, bypass or permanently retire a component because safe degraded service is better than nominal operation. The network state and the ecological state of an old technical site can also diverge over time.

Do not copy New Mauville, its access structure or reward sequence.

### Sunyshore City — distributed infrastructure and demand-side failure

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Sunyshore_City
- https://bulbapedia.bulbagarden.net/wiki/Sunyshore_Gym
- https://bulbapedia.bulbagarden.net/wiki/PS404

Observed high-level structure:
- roads and elevated walkways also collect solar energy;
- the city therefore embeds generation in ordinary public infrastructure rather than separating “power plant” from “street” completely;
- an unusually power-hungry local facility can contribute to a city-level blackout;
- investigation can trace a regional symptom to a specific downstream load rather than only to a broken generator.

Reusable Ouros lesson:

Dependency graphs need both supply-side and demand-side causes. An outage may arise from source loss, distribution failure, overload, configuration, competing demand or intentional diversion. A technically healthy source does not prove that downstream service is healthy.

Do not copy Sunyshore, Volkner, its Gym machinery or its solar-road implementation.

### Gringey City — cross-network cascade and recovery beyond restoration

Source:
- https://bulbapedia.bulbagarden.net/wiki/Gringey_City

Observed high-level structure:
- clogged waterways reduce flow to hydroelectric generators;
- the water-system problem becomes a power-system problem;
- the power outage then affects the wider city;
- restoring electricity does not end the longer cleanup problem.

Reusable Ouros lesson:

Cross-network dependencies matter. Water, waste/remediation, power, transport, communications and care can form chains. Restoring one service should emit handoffs to the systems that still own unresolved cleanup, ecology, repair or public-health state.

Do not copy Grimer/Muk infestation, the exact plant layout or episode plot.

### PTU community encounter design — utility problems as encounter premises

Source:
- https://www.tapatalk.com/groups/pokemon_tabletop/100-encounters-t2967-s10.html

Observed high-level structure:
- community encounter prompts include distressed Electric-type Pokémon disrupting technology and Pokémon drawing energy from a power plant;
- the prompts are deliberately compact and leave causal explanation and consequence to the GM.

Reusable Ouros lesson:

A utility incident is a useful encounter seed, but Ouros should add persistent before/after state around it. “Defeat the Pokémon and power returns” is too shallow unless the actual dependency, cause, isolation state, operator action and restoration verification support that outcome.

This source is inspiration only. It is not a rules source.

### PTU design discussion — capabilities require explicit grounding

Source:
- https://forums.giantitp.com/archive/index.php/t-331762.html

Observed high-level structure:
- PTU developers discuss why physical capabilities are assigned explicitly rather than inferred from generic combat stats or creature shape.

Reusable Ouros lesson:

Infrastructure work by Pokémon cannot be inferred from typing, body shape or combat stats. If a scene needs lifting, traversal, sensing, powering, operating or another mechanically consequential task, the individual Pokémon needs governing PTU/Caelo capability, Move, Ability, Feature or authored-world support.

## New synthesis: outage and restoration are separate timelines

A useful infrastructure story has at least four distinct state chains:

1. physical/technical cause;
2. current network availability;
3. downstream service consequence;
4. restoration and verification.

These chains should not collapse into one flag.

Example:

```text
pump intake blocked
  -> pumping capacity DEGRADED
  -> storage reserve begins supplying district
  -> clinic remains NORMAL for now
  -> market wash-water service becomes LIMITED
  -> reserve reaches review threshold
  -> bypass opened
  -> pumping returns PARTIAL
  -> water-quality/flow verification still pending
  -> clinic and market owners independently decide when their services normalize
```

The infrastructure layer records the network facts. Each dependent system owns its own service decision.

## Restoration principles derived from the sources

### Restoration is staged

Useful states include:
- INCIDENT_UNCONFIRMED
- OUTAGE_CONFIRMED
- BOUNDED
- ISOLATED
- BACKUP_ACTIVE
- PARTIAL_SUPPLY
- RESTORING
- TESTING
- SERVICE_AVAILABLE
- VERIFIED_NORMAL
- MONITORING

The exact vocabulary can remain implementation-facing until canon review.

### Backup power or reserve supply is not normal service

A backup can preserve a critical function while creating new dependencies:
- limited duration;
- reduced capacity;
- fuel/material dependence where canon supports it;
- manual staffing requirement;
- loss of nonessential functions;
- monitoring requirement.

Do not invent quantitative runtime or fuel consumption without canon/rules.

### Upstream restoration does not automatically reopen downstream services

Power returning to a building does not prove:
- refrigeration stayed within acceptable conditions;
- a lift is safe to use;
- pumps have adequate flow;
- communications hardware restarted correctly;
- a clinic can resume full service;
- a route controlled by the system is safe.

Owner systems must verify their own conditions.

### Cascades require explicit edges

Do not write “the whole region goes dark” for dramatic effect. The dependency graph must identify which nodes lost supply and why.

Similarly, two outages at the same time do not prove a shared cause.

### Restoration order is partly technical and partly institutional

A network may physically support several restoration sequences. Who receives priority can depend on civic authority, operator procedure, emergency state or local institution rules. This extension can expose the choices and constraints but must not invent who has legal authority.

## Pokémon ecology and infrastructure

Infrastructure corridors can become habitat, heat sources, shelter, feeding areas or barriers. New Mauville is a useful precedent for an engineered space becoming Pokémon habitat after its intended human use changes.

Ouros should therefore retain ecological observations through shutdown and restoration. Re-energizing or reopening a corridor may require a conservation handoff if current Pokémon use is materially affected.

No presence of Electric-, Water-, Ground- or other typed Pokémon automatically explains a network problem.

## Mechanical boundary

External stories do not define PTU mechanics.

Infrastructure incidents may create narrative/world-state facts such as a darkened district, disabled lift, closed door, low-flow notice or backup generator. These facts must not become combat damage, status, Accuracy/Evasion, forced movement, hazard zones, reaction windows or custom object HP without governing PTU/Caelo rules plus AutoPTU implementation evidence.

The latest inspected AutoPTU-Java commit is `c5ef1d72c8a997144d215423e2aab60d706905a9` (Port Chronicler Accuracy bonus resolution #226). It advances a specific Trainer Feature/Accuracy slice. The Java README still marks full battle state, damage, status controller, terrain, hazards, forced movement, reactions, complete hook registries, AI tactical policy and Craftics/Cobblemon integration as unfinished.

The latest inspected AutoPTU commit is `e9c4173e066da999046818d9ca066bd013f26431` (Career: keep ranked guard ahead of persistence reads #163). That is persistence/rollback hardening, not a new tactical family.

No capability category is promoted by Pass 64.

## Copyright/transformation boundary

Do not reproduce:
- Lumiose/Team Flare plot structure or characters;
- New Mauville access/reward sequence;
- Sunyshore/Volkner-specific machinery or city identity;
- Gringey City's exact Pokémon infestation;
- community encounter text verbatim.

Only the abstract structures are reused: dependency cascades, downstream consequences, safe shutdown, demand-side overload, cross-network coupling, staged restoration and post-restoration verification.

## Questions left open

- Which utility/service networks actually exist in each Ouros settlement?
- Which network edges are centralized, local or independent?
- Which facilities possess backup capacity?
- Which institution owns outage communication, switching, restoration and verification in each locality?
- Which services qualify for priority restoration, and under whose authority?
- Which old technical corridors have become meaningful Pokémon habitat?
- Which PTU/Caelo capabilities can legally support technical work by individual Pokémon?
- How should unloaded Minecraft chunks preserve outage and restoration progress without simulating every machine tick?
