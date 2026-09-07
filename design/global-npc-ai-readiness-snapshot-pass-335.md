# Global NPC AI Readiness Snapshot — Pass 335

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Scope

This snapshot records live mechanical evidence used by the belief-aware dialogue and `The Three Answers` work in Pass 335.

AutoPTU-Java and AutoPTU were inspected read-only. `Teffa14/AutoPTU-Cobblemon-Narrative` is the only writable repository in this task.

No category receives a family-wide promotion from one representative implementation.

## Narrative repository inspection basis

Before authoring, Pass 335 inventoried the complete recursive narrative-repository tree at the Pass 334 head and ran repository-wide content searches for proposed topics before selecting the final seam.

Topics rejected as duplicate or already owned included shift/project handover and warning credibility. Existing files showed prior owners for construction handover, institutional succession, shift-handover encounters and crisis warning credibility.

The selected uncovered seam was belief-aware dialogue projection. Focused reads included:

- `CURRENT_FOCUS.md`;
- `README.md` and its mechanical-source boundary;
- `canon/README.md`;
- `design/global-npc-world-agent-ai-contract.md`;
- `design/global-npc-goal-need-schedule-contract.md`;
- `design/global-npc-publication-revision-contract.md`;
- `design/global-npc-deception-source-attribution-contract.md`;
- `design/global-npc-ai-readiness-snapshot-pass-334.md`;
- `sources/kairos/KAIROS_SOURCE_INDEX.md`;
- current live heads of AutoPTU-Java and AutoPTU.

`CURRENT_FOCUS.md` explicitly names belief-aware dialogue as unfinished work. No dedicated dialogue-projection contract was found before Pass 335.

## Live read-only heads

### AutoPTU-Java

Current `main` head observed during Pass 335:

`f300626dfeb5a2e7bef9c46eeae1f746f00b45a6`

Commit / PR lineage:

`Compose authoritative Trainer Feature invocation execution (#393)`

This advances from Pass 334 head `257f58218204169ad8bd035772a4b4750ecc556e`.

Narrow evidence from the live commit:

- new `TrainerFeatureInvocationExecutor` composes the existing dispatch catalog, transactional `TrainerFeatureExecutionService` and effect batch/registry in invocation order;
- trainer state is required from authoritative `BattleRuntimeState`;
- context creation is explicit;
- effect application remains inside the transactional execution callback;
- the class states that traversal/content binding, transactional gates and concrete payload families remain separate frozen contracts;
- a round-start context factory is included for the already-supported `round_start` seam;
- tests were added for invocation composition.

Workflow evidence inspected for this exact head showed completed successful runs and no `failure` or `in_progress` match in the returned workflow-run set. The legacy combined commit-status endpoint still reports `pending` with zero legacy statuses, so this snapshot treats Actions evidence and legacy status reporting separately.

Boundary:

PR #393 improves composition of an already-narrow Trainer Feature execution path. It does not prove all Trainer Feature triggers, every Feature definition/effect, full battle lifecycle, dialogue mechanics, social checks, investigation actions or adapter support.

### AutoPTU Python

Current `main` head observed during Pass 335:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

The commit explicitly states that it is presentation-only and does not change battle rules or outcomes.

No rules promotion follows from this Python head.

## PTU / Caelo source state

The narrative repository still exposes comparative material under `sources/kairos`.

`KAIROS_SOURCE_INDEX.md` explicitly describes its page references as routing aids rather than automatic Ouros rules acceptance.

No adopted `sources/caelo` directory was found in the inspected narrative tree.

Pass 335 therefore creates no numeric/mechanical rules for:

- interrogation;
- lie detection;
- persuasion;
- social Skill checks;
- Perception or Education checks;
- confidence scores;
- message ranges;
- Trainer Feature social bonuses;
- Move, Ability or Item effects.

## Permanent capability audit

### targeting / footprints / range / LoS

Rating: VERIFIED for ordinary audited contracts.

Pass 335 dialogue itself does not require tactical targeting.

The optional rich encounter in `The Three Answers` may use ordinary static targeting. Smoke, darkness, unusual concealment, dynamic obstruction or specialized route visibility remain outside this general verification.

### base movement legality

Rating: VERIFIED for ordinary audited movement legality.

Ordinary movement can support a static route encounter. This does not establish mounts, climbing, swimming, unusual jumping or authored route-specific traversal.

### complete movement including push / pull / knockback / interception / forced movement

Rating: PARTIAL.

The reduced dialogue/investigation loop avoids this family.

A rich escort/rescue version would depend on interception, forced displacement, knockback near unsafe terrain and any moving hazard interaction it actually uses.

### core calculations

Rating: VERIFIED for ordinary audited deterministic battle calculations.

Pass 335 creates no dialogue-confidence formula, witness score, persuasion math, route certainty calculation or delivery probability.

### action economy / initiative

Rating: VERIFIED for ordinary audited primitives.

Normal battle actions may use the existing action economy. Narrative actions such as `present evidence`, `deliver correction`, `secure package`, `interview`, `signal` or `escort` are not automatically tactical Actions.

### full turn / round lifecycle

Rating: PARTIAL.

The reduced version needs no special turn/round behavior.

A rich scene with a route closing by round, delayed communication arriving during combat or staged environmental changes depends on this family.

### full stateful damage pipeline

Rating: PARTIAL.

Dialogue adds no damage behavior. Any rich encounter with falls, impacts, environmental hazards or other persistent HP/Injury consequences requires authoritative damage handling.

### status lifecycle

Rating: PARTIAL.

Uncertainty, confusion in testimony, stale knowledge, doubt and source ambiguity are world-agent information states, not PTU Status Afflictions.

Pass 335 creates no custom tactical `confused`, `panicked`, `burdened` or similar status.

### terrain / weather / hazards / zones / reactions

Rating: MIXED / PARTIAL / BLOCKING by subfamily.

The reduced version uses ordinary static routes and semantic world events.

A rich version using dynamic route closures, weather zones, unstable terrain, reaction windows or moving hazards must gate each used mechanic against verified engine contracts.

### move-specific behavior

Rating: PARTIAL.

No Move gains investigation, lie-detection, message delivery, tracking, signaling, escort or evidence-analysis behavior from flavor.

Every Move used in a rich encounter remains individually gated.

### abilities

Rating: PARTIAL.

No Ability grants truth detection, perfect memory, source identification, route knowledge, communication authority or investigation success from flavor.

### items

Rating: PARTIAL.

Notebooks, radios, route signs, packages, cameras, recorders, signal devices or investigation tools remain narrative objects unless an authoritative rules source and implementation establish tactical effects.

### Trainer Features / perks

Rating: PARTIAL.

PR #393 is meaningful narrow progress: Java now composes dispatch, transactional execution and effect batching for bound Trainer Feature invocations, including the existing round-start context seam.

Family-wide completion remains unverified. Pass 335 authors no Researcher, Chronicler, Investigator-like, social, interrogation or communication benefit.

### AI legal-action infrastructure

Rating: VERIFIED for ordinary audited legal-action infrastructure.

This supports ordinary legal battle choice generation.

It does not prove investigation dialogue, escort success conditions, evidence presentation or communication objectives as tactical actions.

### AI tactical policy

Rating: BLOCKING for the optional rich encounter's non-defeat priorities.

Examples include:

- protect or escort the carrier;
- prefer communication over attack;
- respond to a verified correction during the encounter;
- withdraw from a route that becomes unsafe;
- avoid escalating against actors who are operating from stale information;
- treat safe delivery or safe retreat as success rather than total defeat of opponents.

The reduced belief-aware dialogue loop is world-agent logic and does not depend on tactical AI policy.

### Minecraft / Cobblemon / Craftics adapter and playback support

Rating: PARTIAL / BLOCKING end-to-end.

The adapter may render NPCs, conversation UI, routes, public notices, packages and authored aftermath.

It may not infer:

- what an NPC knows from proximity;
- which statement is true from speaker animation;
- receipt of a message from visual playback alone;
- belief change from a dialogue line;
- source attribution from UI ordering;
- package recovery from a Minecraft pickup;
- battle or social outcomes outside authoritative owners.

## Pass 335 reduced-version readiness

The core of `The Three Answers` is usable without new battle mechanics because its meaningful state lives in existing world-agent information architecture plus the proposed dialogue-projection seam.

Use now at the design/content level:

- durable NPC identity;
- schedules and commitments;
- direct observations with semantic time;
- explicit communication delivery;
- per-agent claim ledgers;
- source/provenance lineage;
- current retrieval accessibility;
- subjective source attribution;
- contradictory evidence;
- belief assessment;
- individual publication-version receipt;
- deterministic dialogue semantic projection;
- archive/record evidence as separate external evidence;
- replanning after actual new information arrives;
- ordinary static AutoPTU battle only when independently justified.

Avoid claiming implemented production support until the new dialogue projection has an executable runtime and tests.

Avoid until separately verified/adopted:

- lie-detection mechanics;
- social DCs or persuasion math;
- dialogue-generated truth;
- dialogue-generated memories;
- automatic source recovery;
- global latest-publication knowledge;
- free-form LLM text writing into the evidence ledger;
- tactical communication/escort actions without contracts;
- rich dynamic route hazards;
- adapter-authored receipt, belief or evidence state.

## Category changes in Pass 335

No family-wide category rating changes.

AutoPTU-Java advances from PR #392 to PR #393 and provides stronger narrow evidence for the composition of Trainer Feature invocation execution. Trainer Features/perks remains PARTIAL because representative dispatch/execution composition does not prove full Feature coverage.

The main narrative contribution is orthogonal to battle mechanics: a new global dialogue-projection owner that can expose evidence, memory and belief distinctions without generating hidden truth or duplicating AutoPTU.

## Unresolved implementation questions

Before the dialogue seam becomes executable, the project still needs to choose:

- exact `DialogueProjection` schema and module owner;
- how current belief assessment maps to bounded stance classes;
- which retrieval states can expose source attribution;
- how privacy/permission filters enter projection;
- whether exact utterances are persisted only for consequential conversations or for all named-NPC dialogue;
- how localization/character voice consumes the semantic packet;
- how player free-text questions are normalized into safe dialogue intents if free-form input is supported;
- how a future generative renderer is prevented from adding facts;
- whether dialogue projection itself triggers no replanning and only resulting communication/evidence events do;
- production Minecraft acknowledgement semantics for conversations.

No canon answer is selected by this snapshot.