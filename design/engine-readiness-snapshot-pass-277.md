# Engine readiness snapshot — Pass 277

Status: evidence snapshot for narrative dependency gating. AutoPTU-Java and AutoPTU inspected read-only; this pass changes only the narrative repository.

Read-only heads inspected

AutoPTU-Java: `37fc6e5d3372130986c27b53f86a4178f7f97cb6`, merge PR #354 “Preserve move-special target transport through event composition”. No newer main-branch mechanical evidence was present during this pass.

AutoPTU Python: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, viewport synchronization explicitly described as presentation-only.

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

PR #354 remains narrow evidence that move-special target transport is preserved through event composition. Together with PRs #350–353, it strengthens a particular target-result/POST_DAMAGE transport seam. It does not establish full move-specific coverage, a complete stateful damage pipeline, complete turn/round lifecycle, complete movement, terrain/reaction coverage, tactical AI policy or a public typed semantic-result export adequate to promote an entire category.

Live Python evidence

No newer mechanical evidence exists at the inspected head. Its current main commit explicitly changes presentation coordinates after viewport resize and states that battle rules/outcomes are unchanged.

Pass 277 reduced profile

The delegated-stewardship loop requires no AutoPTU tactical capability. It consumes an already valid Pass 276 authority map and adds persistent Ouros governance records for delegated functions, retained powers, semantic term, explicit renewal, subdelegation limits, reporting/evidence obligations, corrective action, partial revocation and expiry.

Minecraft/Cobblemon may display the consequence through marker state, schedules, signs, camps, NPC roles or UI. Those surfaces do not create mechanical authority.

Pass 277 full-profile dependency gates

Tactical detection/selection uses targeting/footprints/range/LoS.

Ordinary traversal uses base movement legality.

Interception, push, pull, knockback or forced displacement require complete movement and therefore remain unavailable as a general assumption.

Adopted deterministic PTU arithmetic uses core calculations.

Structured sequencing uses action economy/initiative; phase-spanning behavior additionally depends on full turn/round lifecycle, still PARTIAL.

Persistent damage depends on the full stateful damage pipeline, still PARTIAL. Persistent conditions depend on status lifecycle, still PARTIAL.

Mechanical barriers, protected zones, weather interactions, hazards or reactions depend on terrain/weather/hazards/zones/reactions, still MIXED/PARTIAL/BLOCKING.

Exact Moves, Abilities, Items and Trainer Features/perks remain gated by their individual PARTIAL families.

AI legal-action infrastructure can enumerate legal actions. Autonomous patrol, enforcement, escort, withdrawal or confrontation policy requires AI tactical policy, still BLOCKING.

Live rendering and authoritative playback remain dependent on Minecraft/Cobblemon/Craftics adapter/playback support, still PARTIAL/BLOCKING end-to-end.

Governance boundary

Delegating authority to observe, maintain a marker, patrol or implement a world-state action cannot create PTU movement, collision, interception, reaction, damage, status, Move, Ability, Item or Feature semantics.

A delegate's competence does not prove authority. A badge or role title does not prove either one.

A partially revoked function does not reverse ecological outcomes already owned by another contract.

No capability promotion

Pass 277 promotes no engine family. Current evidence is unchanged and too narrow for a broader claim.

Caelo/Kairos boundary

No Caelo rule was found or adopted. Kairos remains comparative under `design/ouros-source-authority-and-species-policy.md`; no source-specific governance or tactical rule becomes active Ouros mechanics through this pass.
