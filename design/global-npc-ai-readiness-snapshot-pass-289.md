# Global NPC AI readiness snapshot — Pass 289

Status: evidence snapshot. Narrative repository only. AutoPTU-Java and AutoPTU remain read-only.

Live evidence checked on 2026-09-05.

AutoPTU-Java `main`: `6fbfb06ad662c7adb55ce46dded5bfd5789986f7` (`Extract declarative TURN_END temporary-effect refresh (#366)`). The commit adds a reusable temporary-effect refresh lifecycle hook, uses it for `last_turn_round`, separates `extra_action` cleanup, and includes dedicated tests. This is useful lifecycle/temporary-effect infrastructure evidence, but it is a narrow seam and does not prove complete lifecycle, status handling, damage processing, ability behavior, or move behavior.

AutoPTU Python `main`: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its current head remains presentation-only and is not evidence for a mechanical capability promotion.

Capability classification remains conservative:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING depending on family
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end

Pass 289 publication revision lineage requires none of the tactical families for its reduced form. It records publication history and which version reached an NPC.

If a stale or corrected warning later produces a structured encounter, that encounter inherits only the families it actually uses. Pursuit with interception or forced movement depends on complete movement. Mechanical weather, hazards, zones, or reactions depend on that family. Temporary or delayed effects depend on the relevant lifecycle/status owner plus move/ability/item/Feature behavior. Autonomous tactical choice depends on AI tactical policy. Visible end-to-end realization depends on the Minecraft/Cobblemon/Craftics adapter.

No PTU, Caelo, or Kairos rule is adopted by this snapshot.