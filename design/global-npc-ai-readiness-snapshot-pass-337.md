# Global NPC AI readiness snapshot — Pass 337

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Scope

This snapshot records live mechanical evidence used by the multiparty-audience, overhearing/privacy contract and `The Doorway Listener` case in Pass 337.

AutoPTU-Java and AutoPTU were inspected read-only. Only `Teffa14/AutoPTU-Cobblemon-Narrative` was modified.

No family-wide capability is promoted from one representative mechanic.

## Narrative inspection basis

Before authoring, Pass 337 inventoried the complete recursive narrative repository tree at head `a4517ad4f50b2f43e639b972b1ac6aeca116b8bc` and inspected current focus, canon governance, source authority, the Pass 336 contract/snapshot, existing communications seeds and repository-wide matches for overhearing and privacy.

The duplication check found prior narrow uses of overhearing:

- Pass 19 already stores a partially heard public broadcast as partial knowledge;
- Pass 151 contains a covert-operation seed where an alias may be overheard;
- multiple domain layers already carry privacy scopes;
- Pass 336 already states `OVERHEARD != GROUNDED_WITH_OVERHEARER`.

The uncovered seam is broader and architectural: multi-party audience assignment, per-listener reception, partial overhearing, participant-set grounding and disclosure/relay lineage.

## Live read-only heads

### AutoPTU-Java

Current `main` head observed during Pass 337:

`342399375c2053907c0951e41950073c1b5836d3`

Merge commit:

`Merge pull request #395 from Teffa14/parity/round-start-ability-dispatch-plan — Freeze Python round-start ability dispatch order`

This advances from Pass 336 head `4dcaf7938b13606cf37761aae27727f51cf8a15e`.

Narrow evidence from the live commit:

- adds `RoundStartAbilityDispatchPlan`;
- freezes orchestration order for the Python `start_round()` ability work after Trainer Features;
- models specific dispatch families for Air Lock, Arena Trap, Intimidate and Impostor;
- keeps ability effects outside this planner and explicitly states that registries/executors own them;
- adds a Python fixture exporter and differential parity test against pinned oracle `16d228efa63aabecb67fa788959a359aac7f8f03`;
- adds a dedicated GitHub Actions parity workflow;
- retains tests for the existing round-start Trainer Feature lifecycle seam in the new parity workflow.

The exact head exposed 77 check runs during inspection. Retrieved runs included completed success for trainer initiative speed, round-start Trainer Feature dispatch and parity. No `conclusion: failure` match was found in the retrieved check-run resource.

Boundary:

PR #395 proves ordering/orchestration for a narrow set of round-start Ability dispatch families. It does not prove each Ability effect, all Abilities, complete weather suppression, complete trapping, complete stat-change resolution, every trigger phase, full lifecycle semantics or adapter/playback behavior.

### AutoPTU Python

Current `main` head observed during Pass 337:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

The commit explicitly states that it is presentation-only and changes no battle rules or outcomes.

No rules promotion follows from this Python head.

## PTU / Caelo source state

The narrative README identifies the supplied PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List as the project's mechanical source set when mechanics are required.

The current GitHub tree exposes comparative Kairos material but no ordinary `sources/caelo` directory for direct inspection during this run. Existing project research records prior Caelo consultation, but Pass 337 does not infer a social mechanic from that history.

Therefore this pass adds no hearing radius, Perception/Intuition/Guile check, eavesdropping DC, communication Action, privacy mechanic, telepathy rule, sound-based Move effect, Trainer Feature benefit or Item behavior.

## Permanent capability audit

### targeting / footprints / range / LoS

Rating: VERIFIED for ordinary audited contracts.

The reduced Pass 337 case has no tactical targeting dependency. Conversational audience assignment is not derived from battle LoS.

A rich encounter can use ordinary audited targeting. Specialized hearing through walls, darkness, smoke, sound occlusion or line-of-effect for communication is not covered by this rating.

### base movement legality

Rating: VERIFIED for ordinary audited movement legality.

The reduced case uses persistent world locations and authored conversation participation.

A rich scene may use ordinary legal tactical movement. This does not prove swimming, climbing, squeezing, mounts or special traversal.

### complete movement including push / pull / knockback / interception / forced movement

Rating: PARTIAL.

The reduced case avoids this family.

A rich version involving escort, interception, rescue positioning, forced relocation of a listener or pursuit while a warning is delivered requires exact verified support.

### core calculations

Rating: VERIFIED for ordinary audited deterministic battle calculations.

Pass 337 creates no hearing probability, privacy score, gossip spread formula, trust roll or common-ground arithmetic.

### action economy / initiative

Rating: VERIFIED for ordinary audited primitives.

Audience assignment, listening, grounding and relay are world-agent semantics in the reduced version.

If warning, listening, interrupting, whispering or communicating becomes a tactical Action, that exact action requires a separate authoritative rule/engine contract.

### full turn / round lifecycle

Rating: PARTIAL, with additional round-start evidence.

PR #395 freezes another narrow `start_round()` orchestration seam, now for selected Ability dispatch after Trainer Features.

This does not establish complete turn/round lifecycle, delayed effects, every trigger phase or phase-safe communication.

A rich scene where a correction arrives mid-round or changes an objective during a precise phase remains dependent on verified lifecycle support for that behavior.

### full stateful damage pipeline

Rating: PARTIAL.

The reduced case creates no damage or Injury state.

Any optional tactical encounter depends on the exact selected damage behavior and the broader pipeline remains unpromoted.

### status lifecycle

Rating: PARTIAL.

`OVERHEARD`, `PARTIAL_RECEPTION`, `PRIVATE`, `UNCERTAIN_SOURCE` and `NOT_GROUNDED` are narrative/information states, not PTU Status Afflictions.

No custom distraction, confusion or secrecy status is authored.

### terrain / weather / hazards / zones / reactions

Rating: MIXED / PARTIAL / BLOCKING by subfamily.

The reduced case uses no tactical acoustic zone, weather penalty or hazard.

Any future system where doors, wind, machinery noise, walls or zones change hearing during battle requires exact contracts. Narrative code must not synthesize those effects from environmental flavor.

### move-specific behavior

Rating: PARTIAL.

No Move grants perfect hearing, private-channel access, truth detection, language understanding or common ground by flavor.

Every Move selected in a rich battle remains individually audited.

### abilities

Rating: PARTIAL, with improved round-start orchestration evidence.

PR #395 is meaningful but narrow. It freezes the order in which Air Lock, Arena Trap, Intimidate and Impostor families are dispatched at round start. The new planner explicitly does not implement their effects.

No family-wide Ability promotion is justified.

No Ability is allowed to create conversational knowledge or privacy behavior unless its exact sourced mechanic supports that effect and the engine verifies it.

### items

Rating: PARTIAL.

Pass 337 authors no listening device, radio, recorder, encrypted channel or sound amplifier.

Any future communication or surveillance Item requires an exact supplied definition and implementation evidence.

### Trainer Features / perks

Rating: PARTIAL, with the prior improved round-start seam retained.

PR #394 wired round-start Trainer Feature execution into lifecycle hooks. PR #395 runs selected Ability dispatch after that seam and keeps the parity workflow checking the Trainer Feature lifecycle oracle test.

This does not prove all Trainer Features, trigger families, prerequisites, resources or effects.

Pass 337 grants no Feature-based social, hearing, privacy, memory or relay benefit.

### AI legal-action infrastructure

Rating: VERIFIED for ordinary audited legal-action infrastructure.

This can support legal candidate generation in a conventional optional encounter.

It does not make `WARN_ACTOR`, `LISTEN`, `REQUEST_PRIVACY`, `RELAY_MESSAGE` or `DE_ESCALATE` battle Actions automatically legal.

### AI tactical policy

Rating: BLOCKING for rich non-defeat information objectives.

Potential rich objectives needing policy evidence include:

- warn an actor instead of maximizing damage;
- escort or protect an informed actor while withdrawing;
- stop attacking after a misunderstanding is resolved;
- preserve a confidential objective while choosing legal combat actions;
- prioritize communication or escape over damage;
- react correctly when some allies received a correction and others did not.

The reduced Pass 337 loop has no tactical-policy dependency.

### Minecraft / Cobblemon / Craftics adapter and playback support

Rating: PARTIAL / BLOCKING end-to-end.

Minecraft can render canonical locations, NPC positions, doorway presence, dialogue surfaces and later consequences.

It cannot infer addressee identity from gaze, grant knowledge by proximity, decide that a listener heard the entire line, create privacy scope, establish common ground, authorize relay, expose off-screen dialogue to the player character or treat subtitles/voice playback as authoritative receipt.

A future audio/spatial adapter may supply observation candidates. It must not own semantic audience state.

## Pass 337 reduced-version readiness

The recommended implementation of `The Doorway Listener` can proceed entirely at narrative/world-agent level.

Required seams are already conceptualized in the narrative architecture:

- persistent named NPC identity and canonical feature IDs;
- schedule/location state;
- message and semantic time;
- KnowledgeMemoryLedger and source attribution;
- belief revision;
- Pass 335 dialogue projection;
- Pass 336 repair/common ground;
- new Pass 337 audience/reception records;
- relay lineage and correction history;
- selective world-agent replanning.

No acoustic simulation, tactical hearing mechanic, PTU check or LLM inference is necessary. A deterministic fixture/template implementation is sufficient for first validation.

## Rich encounter dependency matrix

If the rumor eventually places an actor in an ordinary tactical encounter:

- targeting/footprints/range/LoS — required for battle; VERIFIED for ordinary audited contracts, not for acoustic inference;
- base movement legality — required; VERIFIED for ordinary audited contracts;
- complete movement — required only for escort/interception/forced-movement complexity; PARTIAL;
- core calculations — required for ordinary battle; VERIFIED for audited deterministic math;
- action economy/initiative — required for ordinary battle; VERIFIED for audited primitives, but communication Actions are not established;
- full turn/round lifecycle — required for exact mid-round information changes; PARTIAL despite additional round-start dispatch evidence;
- full stateful damage pipeline — required for full battle consequences; PARTIAL as a complete family;
- status lifecycle — required for selected PTU statuses; PARTIAL;
- terrain/weather/hazards/zones/reactions — required only for selected environmental complexity; MIXED/PARTIAL/BLOCKING;
- move-specific behavior — exact set individually audited; family PARTIAL;
- abilities — exact set individually audited; family PARTIAL with improved selected round-start dispatch evidence;
- items — exact set individually audited; family PARTIAL;
- Trainer Features/perks — exact set individually audited; family PARTIAL with prior round-start improvement;
- AI legal-action infrastructure — VERIFIED for ordinary audited infrastructure;
- AI tactical policy — BLOCKING for warning/escort/de-escalation/confidentiality objectives;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL/BLOCKING end-to-end.

## Unresolved questions

Mechanical:

- whether communication can ever consume tactical actions;
- whether any sourced hearing/listening mechanic should be exposed to the world-agent observation layer;
- how selected round-start Ability dispatch plans connect to fully verified effects;
- which Trainer Feature triggers beyond the current round-start seam are parity-safe;
- production world/AutoPTU acknowledgement and checkpoint reconciliation.

Narrative implementation:

- executable schema for `ConversationAudienceFrame` and `ConversationReception`;
- whether group common ground is stored or derived;
- compression rules for recipient-specific dialogue history;
- multi-player audience semantics;
- doorway/room/audio observation-candidate API;
- privacy/disclosure rules by domain;
- localization without addressee drift;
- debug/admin visibility without character-knowledge contamination.

Canon/content for `The Doorway Listener`:

- exact existing resident used as the doorway listener;
- field-service task and old route label;
- what portion of the conversation is participant-scoped;
- whether any resident changes plans because of the relay;
- whether a procedural change persists;
- whether the arc remains purely social/operational or later intersects a battle.
