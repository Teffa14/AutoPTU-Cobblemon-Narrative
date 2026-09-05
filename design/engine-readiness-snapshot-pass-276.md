# Engine readiness snapshot — Pass 276

Status: evidence snapshot for narrative dependency gating. AutoPTU-Java and AutoPTU were inspected read-only; this pass changes only the narrative repository.

Read-only heads inspected

AutoPTU-Java: `37fc6e5d3372130986c27b53f86a4178f7f97cb6`, merge PR #354 “Preserve move-special target transport through event composition”.

AutoPTU Python: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, presentation-only viewport synchronization.

Capability classification

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING end-to-end.

Live Java evidence

PR #354 and its component commits preserve move-special target transport through event composition and freeze ordering with regression coverage. Combined with PRs #350–353, this strengthens one specific transport/composition seam around per-target move-special results and POST_DAMAGE snapshots.

It does not establish complete move-specific behavior, full damage semantics, full turn/round lifecycle, complete movement, terrain/reaction coverage, autonomous tactical policy or a public typed AutoPTU-to-Ouros semantic-result export.

Live Python evidence

No newer mechanical evidence exists at the inspected head. The current commit message explicitly says the viewport synchronization is presentation-only and changes no battle rules or outcomes.

Pass 276 reduced profile

The shared-jurisdiction coordination loop requires no AutoPTU tactical capability. It consumes authorized ecological evidence plus Pass 275 management-decision records and adds Ouros governance state: action-class mandates, approvals, consultations, implementation authority, capacity constraints, bounded emergency authority and semantic review horizons.

Minecraft/Cobblemon may present an approved world-state consequence such as changed schedules, signs, route markers, NPC placement or temporary visual barriers. Those surfaces remain non-authoritative for PTU mechanics.

Pass 276 full-profile dependency gates

Tactical detection/selection uses targeting/footprints/range/LoS.

Ordinary traversal uses base movement legality.

Interception, push, pull, knockback or forced displacement require complete movement and therefore remain unavailable as a general assumption.

Adopted deterministic PTU arithmetic uses core calculations.

Structured sequencing uses action economy/initiative; phase-spanning behavior additionally depends on the still-PARTIAL full turn/round lifecycle.

Persistent damage depends on the still-PARTIAL full stateful damage pipeline. Persistent conditions depend on the still-PARTIAL status lifecycle.

Mechanical environmental enforcement, protected zones, weather interactions or reactions depend on terrain/weather/hazards/zones/reactions, which remains mixed/partial/blocking.

Exact Moves, Abilities, Items and Trainer Features/perks remain gated by their individual PARTIAL families.

AI legal-action infrastructure can enumerate legal actions. Autonomous tactical enforcement, escort, withdrawal or protected-zone behavior requires AI tactical policy, which remains BLOCKING.

Live rendering/playback continues to require Minecraft/Cobblemon/Craftics adapter/playback support, still PARTIAL/BLOCKING end-to-end.

Governance boundary

A mandate can authorize an Ouros action. It cannot synthesize missing PTU semantics.

A closure notice does not create difficult terrain.

A Minecraft gate does not create a PTU blocker.

A guard does not gain interception from job title or pathing.

An emergency order does not create reactions, damage, statuses, Move effects, Ability triggers, Item effects or Trainer Feature interrupts.

No capability promotion

Pass 276 does not promote any engine family. The evidence remains too narrow for a broader claim.

Caelo/Kairos boundary

No new Caelo rule was found or adopted. Kairos remains a living-world/rules reference under the existing source-authority policy. No source-specific governance rule was promoted into Ouros.
