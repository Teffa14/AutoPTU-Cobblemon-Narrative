# Global NPC AI Readiness Snapshot — Pass 402

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE

## Concrete change

Pass 402 adds an executable production call-site audit for `WorldResource.holder_actor_id` mutation paths.

The current low-level mutators are:

- `checkout_reserved_resource()`;
- `return_resource()`;
- `execute_authorized_handoff()`.

Within `tools/`, only `tools/global_npc_resource_holder_transitions.py` may call those functions directly. Higher-level runtimes must route accepted holder changes through journal-aware operations.

`tools/global_npc_holder_mutation_callsite_audit.py` parses the production tool tree and reports any direct or module-qualified bypass. `tests/test_global_npc_holder_mutation_callsite_audit.py` fails CI when such a caller appears.

This converts the manual Pass 399–401 call-site inspection into a continuing regression boundary.

## Holder-history confidence

The known current production Python call graph contains no holder mutation caller outside the admitted journal boundary.

This does not retroactively prove complete history for resources that existed before the journal. `complete_holder_history_resource_ids` must remain conservative until an authoritative baseline plus journal continuity can prove a bounded interval.

A future holder-mutating primitive with a different function name must be registered in the audit in the same change that introduces it.

## Narrative progress

Research added two previously unused anchors for this exact scan:

- Pokémon Opalo optional missions: independent public-board jobs, distributed objectives and disclosure consequences;
- Pokémon World Tour: United, `ReUnited 002`: ordinary work becoming the entry point to an investigation during a larger social event.

`Four Flags on the Board` converts those patterns into an original Ouros proposal where several minor field-recovery notices can be handled independently by the player or persistent NPCs. Provenance from one recovery may later matter without making every minor job part of a predetermined master plot.

Status remains PROPOSED / NON-CANON.

## PTU/Caelo/Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked as a router only. No Skill, Edge, Feature, class benefit, Item effect, carrying rule, hazard, weather effect or encounter rule is approved by Pass 402.

## Live engine evidence

AutoPTU-Java read-only head: `cf1e19c2ffb07ebd044d1d36348e88a67d5e413e`, merge #426, `Freeze authoritative switch transaction order`.

Verified only for the newly pinned switch-stage order and previously audited supporting seams. This does not complete the broader switching, lifecycle, movement, Ability or Trainer Feature families.

AutoPTU Python read-only head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Latest change remains presentation-only.

## Capability classification for the new encounter concept

Targeting/footprints/range/LoS: VERIFIED only inside previously audited scopes.

Base movement legality: VERIFIED only inside previously audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only inside previously audited scopes.

Action economy/initiative: PARTIAL overall; audited primitives exist.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: individually gated.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only inside ordinary audited scopes.

AI tactical policy: BLOCKING for recover-object-first, preserve-evidence, rescue-first, protect-object, objective-aware withdrawal and disengage-after-objective.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for persistent objective-object identity, pickup/return acknowledgement, environmental objective state and authoritative non-KO completion.

## Next highest-value seam

Create an authoritative holder-history coverage baseline for a resource at a known semantic cut. Combine that baseline with the CI-enforced mutation boundary and recovered `ResourceHolderTransitionLedger`. Then derive bounded complete coverage automatically instead of passing resource IDs manually.

In-flight AutoPTU recovery remains a separate high-impact seam: stable battle/session identity plus authoritative tactical result persistence are still required before the persistent world may recover through an unfinished battle.
