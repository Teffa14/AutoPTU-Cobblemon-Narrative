# Global NPC AI readiness snapshot — Pass 292

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

Pass 292 records dependency evidence for atomic global-NPC checkpoint continuity. A representative hook never promotes a whole capability family.

AutoPTU-Java live head checked: `3913afb17430967f925179694693e6d6041b67c2`, `Add selective temporary-effect cleanup contract (#369)`. It adds declarative actor/all-combatant cleanup that selects metadata-matching entries inside one temporary-effect family and preserves unrelated entries, with dedicated tests. This is narrow lifecycle/status/Trainer-Feature infrastructure evidence, not full-family parity.

AutoPTU Python live head checked: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head remains presentation-only and explicitly does not change battle rules/outcomes.

Permanent capability status remains conservative:

| Capability family | Pass 292 status |
|---|---|
| targeting / footprints / range / LoS | VERIFIED |
| base movement legality | VERIFIED |
| complete movement: push / pull / knockback / interception / forced movement | PARTIAL |
| core calculations | VERIFIED |
| action economy / initiative | VERIFIED |
| full turn / round lifecycle | PARTIAL |
| full stateful damage pipeline | PARTIAL |
| status lifecycle | PARTIAL |
| terrain / weather / hazards / zones / reactions | MIXED / PARTIAL / BLOCKING |
| move-specific behavior | PARTIAL |
| abilities | PARTIAL |
| items | PARTIAL |
| Trainer Features / perks | PARTIAL |
| AI legal-action infrastructure | VERIFIED |
| AI tactical policy | BLOCKING |
| Minecraft / Cobblemon / Craftics adapter / playback | PARTIAL / BLOCKING end-to-end |

The logical checkpoint itself needs no tactical capability. It persists semantic causality only. The reduced Interrupted Dispatch loop therefore runs without AutoPTU.

A full danger scene inherits exact dependencies from selected mechanics. Interception/knockback requires complete movement. Mechanical weather/hazards/zones/reactions require that family. Delayed/phase-sensitive effects require relevant lifecycle/status and owner-family support. Moves, Abilities, Items and Trainer Features each require their own family. Autonomous combat remains blocked by AI tactical policy. Full visible execution remains dependent on Minecraft/Cobblemon/Craftics adapter/playback.

Open integration questions: what durable store owns the battle/session referenced by `active_autoptu_binding`; how an Ouros checkpoint reconciles atomically with that store; whether Minecraft local-ACK state survives restart without replay; which storage backend supplies the physical crash-safe transaction; and what parity tests promote each lifecycle/status/Feature family beyond representative hooks.
