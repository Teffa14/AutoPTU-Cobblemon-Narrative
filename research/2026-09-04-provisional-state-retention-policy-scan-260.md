# Provisional ecology state retention policy scan — Pass 260

Status: RESEARCH / PROVENANCE. No new Ouros canon or PTU rule is established by this file.
Date: 2026-09-04

## Question

Pass 259 allows one already-counted anonymous source to carry bounded provisional state before Ouros decides whether to expire that private linkage or promote the counted source through Pass 258. The remaining gap is retention policy: which kinds of provisional ecological consequences may survive observation gaps and restart, which should expire back to aggregate population state, and which are too identity-sensitive to remain anonymous.

## Existing Ouros constraints inspected

- `CURRENT_FOCUS.md` keeps ecology/species behaviour as the active workstream.
- `design/ecology-development-program.md` requires persistent ecology, individual variation, observation, Cobblemon projection and deterministic validation.
- `design/ouros-source-authority-and-species-policy.md` keeps Minecraft presentation subordinate to Ouros/PTU authority.
- `design/provisional-counted-source-state-contract.md` permits bounded references but intentionally leaves retention policy open.
- `design/counted-source-resolution-contract.md` owns the zero-demography conversion from an anonymous counted source to a persistent actor.
- Passes 248–259 already separate projection visibility, observation, recurring-identity hypotheses, site use, individual disturbance response, counted-source resolution and provisional state.

The repository tree was inventoried before this pass. Existing ecology research names were checked so this scan would not repeat the prior occupancy, recurrent-individual, site-use, mark-loss, disturbance or super-individual passes.

## New source findings

### 1. Hidden-state ecology separates the underlying state process from observations

USGS summary of Hollanders & Royle, “Know what you don't know: Embracing state uncertainty in disease-structured multistate models” (2022):
https://www.usgs.gov/publications/know-what-you-dont-know-embracing-state-uncertainty-disease-structured-multistate

The useful structural lesson is not the disease application. Hidden Markov / multievent models explicitly separate latent biological state from the observation process and preserve uncertainty when a detected state can be misclassified. For Ouros this supports retaining an authoritative ecological consequence independently from the evidence by which a player or adapter observed it. Observation uncertainty must not force the private state to become certain, and private state must not leak into public knowledge.

### 2. A temporal state trajectory can persist across imperfect detection

USGS summary of Fiske, Royle & Gross, “Inference for finite-sample trajectories in dynamic multi-state site-occupancy models using hidden Markov model smoothing” (2014):
https://www.usgs.gov/publications/inference-finite-sample-trajectories-dynamic-multi-state-site-occupancy-models-using

Dynamic multistate occupancy models treat latent state as a trajectory across sampling periods even when detection is imperfect. Reusable Ouros structure: some consequences have a legitimate temporal lifecycle that can outlive a single observation window. The retention rule should be based on the consequence's semantics and transition horizon, not on whether the Pokémon remained rendered or was detected every session.

### 3. Movement-derived behaviour is evidence, not an automatically authoritative state label

USGS, Buderman et al., “Caution is warranted when using animal space-use and movement to infer behavioral states” (2021):
https://www.usgs.gov/publications/caution-warranted-when-using-animal-space-use-and-movement-infer-behavioral-states

The study found that movement/space-use models did not consistently identify the target behaviour without validation. Reusable Ouros lesson: a path, location cluster or repeated site use may be retained as observation evidence but must not automatically create a durable behavioural state. This reinforces the existing ban on same-site recurrence as identity or lineage proof.

### 4. Some ecological transitions are one-way or rare enough to deserve explicit transition records

USGS, Gundermann et al., “Change-point models for identifying behavioral transitions in wild animals” (2023):
https://www.usgs.gov/publications/change-point-models-identifying-behavioral-transitions-wild-animals

The paper distinguishes recurrent latent states from transitions such as migration initiation, juvenile dispersal or parturition that may occur once during an observation period. Reusable Ouros lesson: retention should distinguish reversible context state from durable transition facts. A one-time authoritative semantic event must not be allowed to vanish merely because the next observation is absent.

### 5. Aggregate population representations can hide individual deviation

Parry & Evans, “A comparative analysis of parallel processing and super-individual methods for improving the computational performance of a large individual-based model” (2008), White Rose Research Online:
https://eprints.whiterose.ac.uk/id/eprint/4129/

This is complementary to Pass 259's super-individual research rather than a new canon claim. Aggregate representations save memory and time, but aggregation can hide important individual deviations. Reusable Ouros lesson: anonymous pool state is appropriate while differences are disposable; once a consequence would be lost or misattributed by aggregation, identity pressure increases.

### 6. PTU community practice still favours evidence-rich wild encounters over blind random spawning

PokémonTabletop discussion, “Any tips for a future GM?” (2022):
https://www.reddit.com/r/PokemonTabletop/comments/xzkco3/

The thread recommends small route rosters, environmental description, Survival/Perception searching and narrative reasons for wild encounters rather than letting random combat dominate route play. This does not establish PTU rules. It supports a player-facing loop in which observation records can survive even after private source linkage expires.

PokémonTabletop discussion, “How do you plan your wild encounters?” (2020):
https://www.reddit.com/r/PokemonTabletop/comments/jivcud/

Responses suggest environmental evidence such as territorial markings and mixed Perception/Pokémon Education/Survival checks. Again, this is practice evidence only. It supports keeping evidence/provenance as a separate durable record from hidden individual state.

## PTU / Kairos / Caelo cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` routes PTU/Kairos ecology guidance to the supplied core compilation and records Kairos as a living-world reference, not Ouros authority. The current Narrative source tree exposes Kairos locally but does not contain a Caelo source pack. Pass 260 therefore makes no Caelo-specific rule claim.

Nothing in the inspected Ouros source-authority policy allows observation evidence to author HP, injury, status, Move, Ability, Trainer Feature or ownership state. A future durable injury can only enter this retention system after an authoritative PTU/AutoPTU semantic result or another explicitly approved Ouros authority source. Minecraft damage, disappearance or animation is insufficient.

## Proposed retention semantics

The following classes are design candidates, not species canon:

- `PRESENTATION_CORRELATION`: short-lived technical continuity only; retain only long enough for projection/save-load reconciliation.
- `OBSERVATION_PROVENANCE`: durable as a historical observation record, but it does not keep private individual linkage alive.
- `RECENT_SITE_USE`: short-lived context; usually expires to aggregate state unless another admissible continuity basis exists.
- `INDIVIDUAL_DISTURBANCE_RESPONSE`: restart-safe while its ecological recovery/decay horizon remains active; can create durable-identity pressure when future projection depends on that same individual's response history.
- `ACTIVE_DIEGETIC_MARKER_LINK`: identity-sensitive while an approved marker remains active; normally requires persistent identity once lineage is admissible.
- `AUTHORITATIVE_ONE_TIME_TRANSITION`: a semantic event such as an explicitly adjudicated dispersal/injury/other future transition must survive as history; if its continuing consequence belongs to one individual, aggregation is unsafe and promotion or quarantine is required.
- `INFERRED_BEHAVIOR_LABEL`: evidence-derived and uncertain; never retained as authoritative state merely because movement or site use suggested it.

## Candidate retention outcomes

`DROP_PRIVATE_KEEP_PUBLIC_HISTORY`

Use when the private correlation has no future semantic consequence. Public observations remain immutable historical evidence.

`RETAIN_UNTIL_SEMANTIC_HORIZON`

Use when a state has a defined ecological decay/recovery/window boundary. Restart may preserve the state until that boundary.

`PROMOTE_OR_QUARANTINE`

Use when continuing to keep the consequence on an anonymous pool slot risks applying it to the wrong biological individual. Promotion still requires Pass 258 lineage proof. Without proof, keep the consequence quarantined from generalized population behaviour rather than invent identity.

`REJECT_UNAUTHORIZED_STATE`

Use when the proposed state belongs to PTU mechanical authority and no authoritative semantic result exists.

## Marea/Sendero application candidate

Use the existing twelve-Fletchling population and fixture-only anonymous sources. One provisional source may accumulate only a recent site-use observation and safely expire. A second may carry an individual disturbance response with an active recovery horizon and survive restart. A third fixture-only scenario can receive a fake Minecraft damage observation; the retention layer must reject any attempt to convert that into an injury because no AutoPTU/Ouros-authoritative injury result exists.

No additional Fletchling actor, nest, territory, marker, injury or quest becomes canon through this scenario.

## Capability dependency interpretation

The reduced retention lifecycle is persistence bookkeeping and does not require tactical AutoPTU capabilities. Production observation/projection still depends on Minecraft/Cobblemon/Craftics adapter/playback support.

A full encounter that follows, blocks or battles an individual must declare the exact permanent categories used. Retention policy itself must not emulate complete movement, lifecycle, damage, statuses, move-specific effects, Abilities, Items, Trainer Features or tactical AI.

## Unresolved questions

The project still needs species/context-specific semantic horizons rather than a universal timeout. It also needs a production source for monotonic world time across restart, an explicit policy for long gaps when a consequence is still active, and a verified path for importing future AutoPTU injury/status/other semantic outcomes without allowing Minecraft presentation events to author them.

The next concrete design step is a retention matrix plus deterministic fixture that proves three different outcomes: safe expiry, restart-safe retention to a semantic horizon, and rejection of unauthorized PTU state.