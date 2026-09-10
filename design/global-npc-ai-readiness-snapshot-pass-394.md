# Global NPC AI Readiness Snapshot — Pass 394

Status: READINESS EVIDENCE. Not canon.
Date: 2026-09-09

## Slice completed

Pass 394 adds a conservative cross-owner recovery diagnostic for current `WorldResource` state versus known reservation and custody history.

Implementation:
- `tools/world_resource_history_reconciliation.py`;
- `tests/test_world_resource_history_reconciliation.py`;
- `design/world-resource-history-reconciliation-contract-pass-394.md`.

Research/content:
- `research/2026-09-09-layered-field-jobs-resource-reconciliation-scan-394.md`;
- `proposals/2026-09-09-three-jobs-on-the-same-road-pass-394.md`.

No canon file or engine repository is changed.

## Recovery boundary

`OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1` remains authoritative for current mutable resource state.

`ReservationLedger` remains authoritative for reservation history supplied to the selected recovery generation.

`ResourceHandoffLedger` remains authoritative for recorded authorized custody transfers.

The new reconciler owns no state. It reports `CONFIRMED`, `CONFLICT` or `INDETERMINATE` relations and never rewrites an owner to make records agree.

`LATEST_KNOWN_HANDOFF != NECESSARILY_CURRENT_HOLDER`

A later return, checkout or other legal mutation can make the current holder differ from the last custody transfer. Such a mismatch is deliberately indeterminate in V1.

An explicit active reservation for one actor and an explicit current reservation field naming another actor is a narrow proven conflict.

A report with indeterminate findings but no conflicts remains safe to restore; uncertainty stays visible.

## Public research contribution

The latest publicly indexed Reckless Rollers PTU episode descriptions add the pattern of one active job coexisting with unrelated obligations and a social location becoming an investigation site.

Pokémon Mystery Dungeon mission-board documentation contributes a high-level taxonomy in which rescue, escort, delivery and retrieval objectives can reuse exploration spaces while retaining different success conditions.

Pokémon Coral contributes optional-area/event density around ordinary regional progression.

Pokémon Reborn is used as a dependency warning: location-sensitive tactical environments can materially alter battle behavior, so Ouros must gate exact terrain/weather/zone/Move interactions against AutoPTU instead of treating them as cosmetic narrative facts.

No protected plot, characters, layouts, dialogue, custom species or proprietary mechanics are imported.

## New narrative candidate

`Three Jobs on the Same Road` is PROPOSED / NON-CANON.

A field team starts with one scheduled assignment, can accept an optional delivery along the same route, then receives credible information about a missing surveyor near the destination. Objectives may be combined, deferred, refused or delegated to persistent NPCs who actually know about them and have the required time/resources.

The reduced version is entirely world-state driven and requires no AutoPTU battle.

The rich version may stage rescue/contact under difficult terrain or wild pressure, but safety/contact/withdrawal remains the objective rather than a KO sweep.

## Read-only engine evidence

AutoPTU-Java advanced to `19dd2d9b99d81f8479c73e6ef4709a30f0794474`, merge #421.

That merge freezes additional Impostor negative-guard parity and touches lifecycle-hook registration. It is evidence for the exact tested seams only. It does not verify the complete Abilities family or complete turn/round lifecycle.

AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change is presentation-only viewport-coordinate synchronization.

Neither engine is modified.

## Permanent capability classification

Targeting/footprints/range/LoS: VERIFIED within audited scopes only.

Base movement legality: VERIFIED within audited scopes only.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED within audited scopes only.

Action economy/initiative: VERIFIED for audited primitives only.

Full turn/round lifecycle: PARTIAL. AutoPTU-Java #421 does not promote the whole family.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: individually gated. Impostor #421 is narrow evidence only.

Items: individually gated. `WorldResource` remains distinct from a PTU Item.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED within ordinary audited scopes only.

AI tactical policy: BLOCKING for rescue-first, escort-first, protect-cargo, split-task coordination, objective-aware withdrawal and disengage-after-objective until exact policies are verified.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative objective acknowledgement, persistent resource projection, escort/rescue state and non-KO completion playback.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked only as a routing aid. Pass 394 introduces no new Skill check, Edge, Trainer Feature, Item effect, environmental modifier, weather rule, Move effect or tactical interrupt.

Any later mechanically defined rescue, escort, delivery or environmental interaction must be checked against the actual supplied PTU/Caelo/Kairos source material and current AutoPTU implementation.

## Next implementation seams

Highest-value next work:

- run the global regression suite and merge Pass 394 only if it stays green;
- decide whether the reconciliation report should become an explicit post-restore validation stage downstream of `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V2`;
- add stronger holder reconciliation only after a complete authoritative holder-transition journal exists;
- define in-flight AutoPTU battle/session recovery using stable battle/session identity and authoritative tactical state/result;
- keep Minecraft/Cobblemon acknowledgement downstream of world and battle authority.

## Canon unresolved

Still open:

- whether the layered road assignment exists;
- region, road and institution;
- package and field-resource identity;
- surveyor identity and actual reason for delay;
- species or hazards present;
- assignment/delegation authority;
- PTU/Caelo Skills, Edges, Features or Items;
- whether any objective participates in a larger regional arc.

No answer is promoted by Pass 394.
