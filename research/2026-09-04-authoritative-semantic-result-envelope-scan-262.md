# Authoritative semantic-result envelope scan — Pass 262

Status: RESEARCH / PROVENANCE ONLY. Nothing in this note becomes Ouros canon or PTU rules by itself.

## Question

Pass 260 rejects Minecraft-only damage presentation as authority for persistent injury. Pass 261 requires a future typed AutoPTU semantic result before battle-authored consequences can enter ecological retention. This scan asks what a safe, replayable result boundary should preserve and which narrative structures become possible once aftermath can be trusted.

## Public sources reviewed

### CloudEvents specification

Source: CNCF CloudEvents specification 1.0.x, https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md

Reusable structure: event identity is separate from payload. CloudEvents requires `id`, `source`, `specversion` and `type`; the producer must make `source + id` unique for a distinct event, while a retransmitted duplicate may keep the same identity. This is a strong pattern for Ouros import idempotency.

Adaptation, not adoption: Ouros does not need to claim CloudEvents compliance. The useful lesson is to make result identity, producer identity, result type and schema version explicit instead of inferring them from transport or payload shape.

### W3C PROV data model

Source: W3C Provenance Working Group publications, https://www.w3.org/groups/wg/prov/publications/

Reusable structure: provenance distinguishes entities, activities and responsible agents, and explicitly represents derivation. An imported consequence therefore benefits from preserving the battle/session activity that generated it, the engine/rules profile responsible for adjudication and any antecedent semantic result it derives from.

Adaptation: Ouros can retain compact provenance references without implementing PROV-O or RDF.

### PTU injury and recovery semantics

Sources: PTU 1.05 material mirrored by the PTU community, including injury/healing text and Trainer Features; https://pturpg.wikidot.com/taskmaster and https://pturpg.wikidot.com/consumables . A public PTU 1.05 core mirror also describes daily injury-healing limits and recovery institutions: https://anyflip.com/qloz/xgfq/basic/251-300 .

Design lesson: an Injury is mechanically consequential state with its own creation, interaction and healing semantics. A visual hit, animation or Minecraft health event is therefore insufficient evidence for a PTU Injury. Any imported injury must come from the subsystem that actually adjudicated the relevant PTU path.

This note does not use community mirrors to silently amend the project's adopted PTU rules profile. The project-local PTU oracle remains authoritative for exact mechanics.

### Pokémon Mystery Dungeon environmental aftermath

Sources reviewed for high-level narrative structure: Pokémon Mystery Dungeon rescue-team stories repeatedly revisit places affected by wider disasters and let the state of an environment motivate later jobs, rescues and changed traversal. Public overview: https://en.wikipedia.org/wiki/Pok%C3%A9mon_Mystery_Dungeon%3A_Blue_Rescue_Team_and_Red_Rescue_Team . A review of Rescue Team DX highlights environments visibly altered by natural disasters: https://www.well-played.com.au/pokemon-mystery-dungeon-rescue-team-dx-review/ .

Reusable structure: a resolved encounter can leave legible aftermath that changes what the player sees on a return visit. Ouros can use the same high-level loop without copying locations, characters or plots: authoritative consequences from one scene become later environmental or individual-state evidence.

## Existing Ouros material cross-check

Pass 260 already establishes `REJECT_UNAUTHORIZED_STATE` for PTU state inferred from Minecraft/Cobblemon presentation. Pass 261 says a future battle consequence can open or close a semantic horizon only after the handoff proves it came from the authoritative battle path.

Pass 262 therefore must add the positive ingress contract rather than another presentation-rejection rule.

No existing research note found during the full repository tree inspection defines a complete typed semantic-result envelope with producer authority, actor lineage, capability provenance and replay identity together.

## Proposed reusable structure

A semantic result should carry four independently checkable dimensions:

1. Event identity: stable result ID, schema version and result type.
2. Producer authority: AutoPTU engine identity, engine revision/rules profile and battle/session provenance.
3. Subject binding: stable Ouros actor/source binding derived from the battle handoff, never a Minecraft entity UUID.
4. Capability provenance: the exact capability families needed by that result path and the verification status required before Ouros accepts a persistent consequence.

A fifth dimension, transport authenticity or cryptographic signing, remains unresolved. No current repository evidence proves a signing system exists, so Pass 262 must not fabricate one.

## Consequence mapping candidates

A validated authoritative result may create or update only the semantic classes explicitly mapped by its result type. Example candidates include an adjudicated injury, an adjudicated persistent status where PTU semantics permit persistence, or a battle end-state that changes a pre-existing ecological horizon.

Unknown result types, unsupported schema versions, actor-binding mismatches, missing authority provenance or capability paths below the required readiness threshold should enter a quarantine/rejection path. They cannot be downgraded into a best-effort PTU mutation.

## Narrative applications

A recurring wild individual can reappear after an earlier encounter with trustworthy aftermath attached to that same individual. A damaged roost or abandoned route can be shown later only when the environmental consequence has an authoritative owner. An NPC can react to a prior encounter outcome without the presentation layer inventing whether the Pokémon was injured, merely startled or unaffected.

The reduced form uses fixture-authored prevalidated semantic results and never runs a battle. The full form begins with a real AutoPTU encounter and imports its result envelope.

## Status classification

CANON-ALIGNED: AutoPTU owns PTU battle truth; Minecraft/Cobblemon/Craftics presents and plays back results; population and identity authority remain with Ouros ecology.

PROPOSED: typed semantic-result ingress contract and the fields described here.

UNCERTAIN: concrete transport, signing/authentication mechanism, production schema serialization, exact rules-profile identifier and adapter binding.

FIXTURE-ONLY: any Fletchling injury/status/result used in Pass 262 tests.

## Sources intentionally not promoted

Public PTU mirrors, community discussions and Mystery Dungeon summaries supply design patterns and cross-checks. They do not overwrite project-local PTU rules, Caelo/Kairos policy or established Ouros lore.
