# Ecological facilitation cascade contract

Status: PROPOSED contract. Pass 268. No cascade edge or species behavior becomes Marea/Sendero canon through this document.

Record: `ECOLOGICAL_FACILITATION_CASCADE_V1`.

A cascade is a directed graph of modification/condition nodes connected by independently adjudicated dependency edges. Each edge requires edge id, upstream node, downstream node, relation class, evidence references, interpretation state, validity state, provenance and canon status.

Allowed interpretation states: `OBSERVED_ASSOCIATION`, `DEPENDENCY_HYPOTHESIS`, `DIRECT_DEPENDENCY_SUPPORTED`, `UNCERTAIN`, `REJECTED`. Allowed validity states: `ACTIVE`, `HISTORICAL`, `SUSPENDED`, `CLOSED`.

Core invariant: A -> B plus B -> C never creates A -> C. Transitive closure is forbidden unless A -> C has its own evidence and independently adjudicated edge.

Temporal order, co-occurrence, shared site, repeated recipient use, Minecraft adjacency, species identity or NPC belief cannot establish dependency. `DIRECT_DEPENDENCY_SUPPORTED` requires evidence that the downstream modification or ecological condition materially depends on the upstream node for substrate, shelter, retained material, access or another explicitly described ecological mechanism.

Dependency and benefit remain separate. A downstream structure can depend physically on an upstream feature without proving higher survival, fitness, abundance, ownership, nesting, territory or population growth. Pass 266 cue-quality rules continue to govern habitat-quality claims.

Node closure does not recursively delete descendants. When an upstream node degrades or closes, every direct downstream edge is re-evaluated. A downstream modification follows its own physical state and semantic horizon: it may persist autonomously, degrade, close, or become uncertain. The former edge remains in history as `HISTORICAL` when appropriate.

Cascade graph changes cannot create demographic events. All visible actors must already be counted unless a separate authoritative birth/immigration transaction exists.

Minecraft/Cobblemon geometry may present nodes and their spatial relationship but cannot author an ecological dependency edge. It also cannot infer PTU cover, blocker, difficult terrain, hazard, zone, reaction or movement cost.

Reduced encounter: persist two or more habitat modifications, record observations, expose dependency evidence gradually, and update edge validity on physical transitions. No AutoPTU handoff is required.

Full encounter dependencies: targeting/footprints/range/LoS applies when actors actively detect or target features/occupants. Base movement legality applies to ordinary approach, construction or traversal. Complete movement applies to push/pull/knockback/interception/forced movement or tactical blocking. Core calculations apply only when a mapped PTU rule requires them. Action economy/initiative and full turn/round lifecycle apply to tactical construction, destruction or interaction sequencing. Full stateful damage pipeline applies to destructive damage or persistent injury-producing consequences. Status lifecycle applies to persistent statuses. Terrain/weather/hazards/zones/reactions applies to any admitted battlefield semantics of the cascade. Move-specific behavior, abilities, items and Trainer Features/perks apply exactly when those mechanisms create, alter or exploit a node. AI legal-action infrastructure is required for legal autonomous choices; AI tactical policy is required for autonomous decisions to build, use, contest, maintain or abandon cascade features. Minecraft/Cobblemon/Craftics adapter/playback support is required for live persistence and presentation.

Fail closed: missing direct evidence leaves an edge hypothetical; upstream closure triggers re-evaluation rather than recursive deletion; no transitive edge is synthesized; no ecological edge becomes a PTU terrain rule without exact admission evidence.