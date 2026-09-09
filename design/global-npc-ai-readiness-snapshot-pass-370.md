# Global NPC AI readiness snapshot — Pass 370

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-09-08

## Read-only engine evidence checked

AutoPTU-Java current main: `eaaed3abdc6f2f1d884d71324a4fe9f5186b1b50`, merge of PR #410. The latest demonstrated slice freezes differential parity for the specific Intimidate → Simple POST_APPLY interaction, including final Combat Stage result, once-per-round marker and event ordering. Earlier adjacent slices cover specific Intimidate interactions such as Mirror Armor, Defiant and Competitive. These representative interactions do not prove complete Ability or reaction-family coverage.

AutoPTU Python current main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head commit explicitly describes presentation-only coordinate synchronization with no battle-rule or outcome change.

Both engine repositories were inspected read-only. Pass 370 changes only the narrative repository.

## Permanent capability classification

Targeting/footprints/range/LoS: VERIFIED within ordinary audited contracts.

Base movement legality: VERIFIED within ordinary audited contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Do not assume complete interception, forced movement, carrier displacement or compound movement interactions.

Core calculations: VERIFIED within audited deterministic arithmetic scope.

Action economy/initiative: VERIFIED for audited primitives. Objective-specific pickup, relay interaction, item transfer and interrupts remain separately gated.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact family. Specific Intimidate reaction tests do not promote the family.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL and individually gated. Intimidate → Simple evidence is interaction-specific.

Items: PARTIAL and individually gated.

Trainer Features/perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED within ordinary previously audited action-generation scope.

AI tactical policy: BLOCKING for protect-relay, preserve-equipment, intercept-to-inform, reroute, timed-objective prioritization and disengage-after-objective policies.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for authoritative relay objectives, cargo identity, world acknowledgement and end-to-end tactical playback.

## Pass 370 encounter consequence

The reduced `Dead Relay at Saltglass Ridge` concept avoids battle dependencies and can advance using persistent communications, knowledge and travel systems.

The full field version may use ordinary verified targeting and movement primitives, but any forced movement, weather pressure, hazards, reactions, persistent statuses, specific Moves, Abilities, Items or Trainer Feature interrupts remain gated until their exact contracts/tests are verified.

## Unresolved mechanical questions

No live evidence yet promotes complete movement, lifecycle, damage, status, environment/reaction, Move, Ability, Item or Trainer Feature families to VERIFIED.

The rich relay objective still lacks verified AI policy for protecting or repairing an objective while disengaging from unnecessary combat.

Minecraft/Cobblemon/Craftics still requires an authoritative objective/cargo acknowledgement path before the relay station can become an end-to-end tactical object rather than semantic world state.
