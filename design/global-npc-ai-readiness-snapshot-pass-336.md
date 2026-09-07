# Global NPC AI readiness snapshot — Pass 336

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Scope

This snapshot records live mechanical evidence used by the conversational-grounding and `The Two Yards` work in Pass 336.

AutoPTU-Java and AutoPTU were inspected read-only. Only `Teffa14/AutoPTU-Cobblemon-Narrative` was modified.

No family-wide capability is promoted from one representative mechanic.

## Narrative repository inspection basis

Before authoring, Pass 336 inspected the complete recursive narrative tree at head `95a5a9daa268645bdc87e33e7ee8c813ae886217` and ran focused repository-wide searches for rival/rematch systems, deception/trust, dialogue, clarification, repair and common ground.

A proposed recurring-rival pass was rejected because the repository already contains dedicated recurring-rival agency/progression, battle-institution, scouting and rematch material.

Focused reads included:

- `CURRENT_FOCUS.md`;
- `README.md`;
- `canon/README.md`;
- `canon/marea-interior-map-resident-network-v2.md`;
- `research/2026-08-18-source-scan.md`;
- `design/global-npc-belief-aware-dialogue-projection-contract-pass-335.md`;
- `proposals/2026-09-01-marea-memorial-legacy-seeds-180.md` to avoid duplicating its name/provenance ambiguity cases;
- `sources/kairos/KAIROS_SOURCE_INDEX.md`;
- current AutoPTU-Java and AutoPTU heads.

The uncovered seam is pair-scoped conversational grounding and repair: the project can already project an NPC's belief-aware answer, but lacked an owner for whether two interlocutors established the same referent, requested clarification, repaired a misunderstanding or retained partner-specific shorthand.

## Live read-only heads

### AutoPTU-Java

Current `main` head observed during Pass 336:

`4dcaf7938b13606cf37761aae27727f51cf8a15e`

Commit:

`Wire round-start Trainer Features into lifecycle hooks (#394)`

This advances from Pass 335 head `f300626dfeb5a2e7bef9c46eeae1f746f00b45a6`.

Narrow evidence from the live commit:

- adds `RoundStartTrainerFeatureLifecycleHook`;
- registers Trainer Feature dispatch at `LifecycleHookPoint.ROUND_START_EFFECTS` through `BuiltinLifecycleHooks`;
- supplies authoritative Trainer Feature content/effects from core rather than an adapter;
- adds round-start lifecycle wiring tests;
- adds a Python differential and fixture for the round-start Trainer Feature lifecycle;
- gates the new seam against pinned Python oracle `16d228efa63aabecb67fa788959a359aac7f8f03`.

Workflow runs inspected for this exact head returned completed successful runs and no `failure` or `in_progress` match in the retrieved run set.

Boundary:

PR #394 proves another concrete round-start Trainer Feature lifecycle seam. It does not prove every Trainer Feature trigger, all Features/effects, every lifecycle phase, complete round semantics, every delayed effect, or family-wide adapter fidelity.

### AutoPTU Python

Current `main` head observed during Pass 336:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

The commit explicitly states that it is presentation-only and does not change battle rules or outcomes.

No rules promotion follows from this Python head.

## PTU / Caelo source state

The project README identifies PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List as mechanical authority when available.

The original project research records Caelo Social play as a roleplay/character-development activity container. That supports the existence of ordinary conversations but does not authorize invented social checks or bonuses.

The current repository tree still exposes comparative material under `sources/kairos`; its source index explicitly warns that page references are routing aids rather than automatic Ouros acceptance.

No ordinary `sources/caelo` directory was exposed in the inspected GitHub tree during this run. Pass 336 therefore adds no Persuasion/Guile/Intuition/Perception/Education DC, memory roll, lie-detection mechanic, communication bonus, Trainer Feature effect, Move effect, Ability effect or Item effect.

## Permanent capability audit

### targeting / footprints / range / LoS

Rating: VERIFIED for ordinary audited contracts.

The reduced conversation-repair case has no tactical targeting dependency.

An optional Battle Yard scene can use ordinary static targeting. Smoke, darkness, unusual concealment, dynamic obstruction or specialized visibility remain outside this general statement.

### base movement legality

Rating: VERIFIED for ordinary audited movement legality.

The reduced case uses world travel/location state rather than tactical movement.

A static optional battle may use ordinary movement. This does not prove mounts, swimming, climbing or special traversal.

### complete movement including push / pull / knockback / interception / forced movement

Rating: PARTIAL.

The reduced case avoids the family entirely.

Any rich Battle Yard version using ring-outs, interception, forced displacement or equipment protection via movement depends on exact verified support here.

### core calculations

Rating: VERIFIED for ordinary audited deterministic battle calculations.

Pass 336 creates no common-ground score, misunderstanding roll, conversation confidence formula or social arithmetic.

### action economy / initiative

Rating: VERIFIED for ordinary audited primitives.

Conversational acts such as `REQUEST_REFERENT_CLARIFICATION` or `CONFIRM_PARAPHRASE` are world-agent dialogue semantics, not tactical Actions.

If future combat permits communication as an initiative-consuming action, that requires a separate authoritative engine contract.

### full turn / round lifecycle

Rating: PARTIAL.

PR #394 adds meaningful evidence for one `ROUND_START_EFFECTS` Trainer Feature seam. It does not establish the complete family.

The reduced Pass 336 case needs no tactical lifecycle behavior.

A rich version where a corrected instruction arrives during battle or changes a round-timed objective depends on verified lifecycle support for that exact behavior.

### full stateful damage pipeline

Rating: PARTIAL.

Conversation repair creates no HP, Injury or damage rule.

Any optional battle still depends on authoritative handling of the exact damaging content selected.

### status lifecycle

Rating: PARTIAL.

Misunderstanding, ambiguity, disagreement and incomplete grounding are conversational/world-agent states. They are not PTU Status Afflictions.

No custom confusion, distraction or social status is created.

### terrain / weather / hazards / zones / reactions

Rating: MIXED / PARTIAL / BLOCKING by subfamily.

The reduced case uses fixed Puerto Bruma locations and no tactical environmental rules.

Any rich Battle Yard variant using arena zones, reactions, weather or changing hazards must gate each selected mechanic independently.

### move-specific behavior

Rating: PARTIAL.

No Move grants perfect communication, truth detection, translation, memory, referent resolution or task acceptance from flavor.

Every Move in an optional battle remains individually audited.

### abilities

Rating: PARTIAL.

No Ability creates shared knowledge, common ground, perfect hearing, truth detection or automatic repair.

Every selected Ability remains individually audited.

### items

Rating: PARTIAL.

The field lamp in `The Two Yards` is intentionally a narrative equipment instance unless a supplied source establishes a specific mechanical item. Its custody/destination can change without creating battle-item behavior.

Any combat Item remains individually audited.

### Trainer Features / perks

Rating: PARTIAL, with improved round-start evidence.

PR #394 is concrete progress: bound Trainer Feature execution is now wired into the authoritative round-start lifecycle seam and differential-tested against the pinned Python oracle.

Family-wide completion remains unverified. Pass 336 authors no social, communication, memory, investigation or clarification benefit from a Trainer Feature.

### AI legal-action infrastructure

Rating: VERIFIED for ordinary audited legal-action infrastructure.

This can support ordinary battle choice generation in the optional static fight.

It does not make dialogue repair, instruction confirmation, equipment retrieval or de-escalation into legal battle Actions.

### AI tactical policy

Rating: BLOCKING for rich non-defeat objectives.

Potential rich objectives that remain blocked without specific policy evidence include:

- pause or de-escalate when new information arrives;
- protect equipment instead of maximizing damage;
- allow safe retrieval;
- treat clarification/communication as more important than attacking;
- stop escalation after the operational misunderstanding is resolved.

The reduced Pass 336 loop has no dependency on tactical AI policy.

### Minecraft / Cobblemon / Craftics adapter and playback support

Rating: PARTIAL / BLOCKING end-to-end.

Minecraft can render canonical sites, named NPCs, the equipment instance, dialogue UI and corrected aftermath.

It cannot infer that a phrase was understood from NPC proximity, treat a nod animation as task acceptance, create common ground because two subtitles share a string, turn an overhearer into a participant, move custody merely because an item entity changed hands visually, or resolve a battle outside AutoPTU.

## Pass 336 reduced-version readiness

The recommended `The Two Yards` implementation can proceed at narrative/world-agent level without adding battle mechanics.

It uses existing or proposed world-system seams:

- canonical Puerto Bruma feature IDs and coordinates;
- persistent named NPC identity;
- communication delivery and semantic time;
- private knowledge/retrieval/source attribution;
- Pass 335 belief-aware dialogue projection;
- proposed Pass 336 semantic conversational acts;
- pair-scoped grounded referents;
- persistent equipment/custody state;
- commitments/pickup timing;
- selective replanning after a corrected instruction.

A deterministic menu/template implementation is enough to validate the architecture.

## Rich encounter dependency matrix

If an ordinary audited Battle Yard battle occurs alongside the delivery problem:

- targeting/footprints/range/LoS — required for ordinary battle; VERIFIED for audited ordinary contracts;
- base movement legality — required; VERIFIED for audited ordinary contracts;
- complete movement — only if ring-out/interception/forced movement selected; PARTIAL;
- core calculations — required; VERIFIED for audited ordinary contracts;
- action economy/initiative — required; VERIFIED for audited ordinary primitives;
- full turn/round lifecycle — required for round-timed communication/objective changes; PARTIAL despite new round-start evidence;
- full stateful damage pipeline — required for full ordinary battle consequences; PARTIAL as a complete family;
- status lifecycle — required for selected status content; PARTIAL;
- terrain/weather/hazards/zones/reactions — required only for selected arena complexity; MIXED/PARTIAL/BLOCKING;
- move-specific behavior — exact set audited; family PARTIAL;
- abilities — exact set audited; family PARTIAL;
- items — exact set audited; family PARTIAL;
- Trainer Features/perks — exact set audited; family PARTIAL with improved `round_start` seam;
- AI legal-action infrastructure — VERIFIED for ordinary audited infrastructure;
- AI tactical policy — BLOCKING for non-defeat communication/protection priorities;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL/BLOCKING end-to-end.

## Unresolved questions

Mechanical:

- whether/when communication may become a tactical action;
- whether any exact Item definition should back the field lamp or similar equipment;
- whether rich objective policy will eventually support de-escalation/protect-equipment behavior;
- which Trainer Feature triggers beyond round start are parity-safe;
- production acknowledgement and world/AutoPTU checkpoint reconciliation.

Canon/content:

- whether repair row has a distinct work-apron/storage subfeature;
- whether any local group uses `the yard` for that subfeature;
- who authors the ambiguous instruction;
- which equipment instance and downstream pickup are used;
- whether the incident produces a permanent naming/procedure change.

Dialogue implementation:

- exact persistent schema for `CommonGroundEntry`;
- how much low-stakes dialogue history is compressed;
- how multiplayer/multi-NPC grounding scopes participants;
- localization rules for partner-specific shorthand;
- privacy/overhearing hooks;
- how a future natural-language renderer maps wording into bounded semantic repair acts without acquiring state authority.
