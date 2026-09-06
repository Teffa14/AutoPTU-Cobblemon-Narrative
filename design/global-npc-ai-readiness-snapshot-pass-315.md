# Global NPC / encounter readiness snapshot — Pass 315

Status: DESIGN / LIVE EVIDENCE SNAPSHOT
Date: 2026-09-06

## Scope

This snapshot records the implementation dependency status used by Pass 315. It does not promote a whole engine capability because one representative seam exists.

Read-only engine evidence inspected:

- `Teffa14/AutoPTU-Java` head `e963a6b5a04bf4d7bf79616132545eb63ecf6deb`, PR #384, `Add reusable round-window history pruning contract`;
- pinned/read-only `Teffa14/AutoPTU` remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, whose current head is presentation-only according to the repository evidence previously audited by this project.

## Live Java delta since Pass 314

PR #384 adds a reusable round-window history-pruning contract, tests it, freezes representative histories against the Python lifecycle oracle and gates that seam against the pinned Python source.

This is meaningful evidence for round/lifecycle history retention and pruning. It does not prove:

- the full turn/round lifecycle;
- every phase hook;
- delayed environmental effects;
- all reaction windows;
- full stateful damage processing;
- status expiry/refresh semantics;
- arbitrary Trainer Feature timing;
- dynamic hazards;
- Minecraft playback.

Therefore the full lifecycle category remains PARTIAL.

## Permanent capability categories

### Targeting / footprints / range / LoS

Status: VERIFIED within audited contracts.

Pass 315 relevance: a full tactical rescue or encounter may use ordinary spatial targeting. Acoustic detection itself is not modeled as LoS or ordinary range by default.

### Base movement legality

Status: VERIFIED within audited contracts.

Pass 315 relevance: sufficient for reduced-version travel between authored observation nodes.

### Complete movement including push/pull/knockback/interception/forced movement

Status: PARTIAL.

Pass 315 relevance: blocks any assumption that noise panic, debris, rescue interception or shockwave-like displacement can be simulated generically.

### Core calculations

Status: VERIFIED within audited contracts.

Pass 315 relevance: sufficient for ordinary deterministic arithmetic already covered by those contracts. No acoustic attenuation formula is introduced.

### Action economy / initiative

Status: VERIFIED within audited contracts.

Pass 315 relevance: supports structured tactical turns where otherwise legal.

### Full turn / round lifecycle

Status: PARTIAL.

Evidence update: PR #384 strengthens a round-history pruning seam against Python. PR #383 already strengthened round-history ordering after initiative rebuild. Neither proves the complete lifecycle family.

Pass 315 relevance: dynamic machinery, timed acoustic windows or collapses during combat remain dependent on missing/full lifecycle guarantees.

### Full stateful damage pipeline

Status: PARTIAL.

Pass 315 relevance: environmental injury from debris, pressure, a sound Move or other authored hazard must use the authoritative damage path. The narrative layer may not approximate it.

### Status lifecycle

Status: PARTIAL.

Pass 315 relevance: no `deafened`, `ringing`, `panic` or similar persistent status is invented. Any real PTU condition requires verified lifecycle handling.

### Terrain / weather / hazards / zones / reactions

Status: MIXED / PARTIAL / BLOCKING by subfamily.

Pass 315 relevance: a full acoustic zone, unstable echo gallery, dynamic machine area or reaction rescue depends on exact subfamilies that are not globally verified.

### Move-specific behavior

Status: PARTIAL.

Pass 315 relevance: sound-based Moves cannot gain environmental masking, panic, structural or communication effects merely from narrative flavor. Each behavior must be verified.

### Abilities

Status: PARTIAL.

Pass 315 relevance: Soundproof or another acoustic-relevant Ability requires exact implemented semantics before use in the full encounter. Ecological hearing behavior is not inferred from the battle Ability.

### Items

Status: PARTIAL.

Pass 315 relevance: no item dependency in the reduced version. Any acoustic instrument that is only narrative/world equipment should remain outside PTU item semantics unless explicitly adopted.

### Trainer Features / perks

Status: PARTIAL.

Pass 315 relevance: Perception/investigation benefits, interrupts or acoustic specialization require source-verified Feature support before becoming mechanics.

### AI legal-action infrastructure

Status: VERIFIED within audited contracts.

Pass 315 relevance: sufficient to constrain structured autonomous actions to known legal choices where those actions already exist.

### AI tactical policy

Status: BLOCKING for general autonomous tactical choice.

Pass 315 relevance: autonomous rescue, route choice under dynamic hazards, deliberate exploitation of masking or sophisticated retreat policy remains blocked.

### Minecraft / Cobblemon / Craftics adapter and playback support

Status: PARTIAL / BLOCKING end-to-end.

Pass 315 relevance: client spatial audio, machine sound playback or Pokémon animation may enrich presentation, but cannot be the authority for world acoustic evidence. Full authoritative synchronization of acoustic scene state, battle consequences and playback is not established.

## Reduced-version readiness

`The Valley That Stopped Answering` can run without new AutoPTU mechanics if implemented as world/narrative state:

- authored observation nodes;
- direct observations with provenance;
- separate interpretation claims;
- machinery state changed between scenes;
- repeated visits at authored time windows;
- static open/blocked navigation;
- explicit information delivery between NPCs.

No tactical sound propagation, damage, forced movement, dynamic zones or invented statuses are required.

## Blocking requirements for the intended full version

The rich encounter remains blocked or partial where it uses:

- machine cycles inside rounds: full turn/round lifecycle;
- unstable acoustic/structural zones: terrain/hazards/zones/reactions;
- debris or panic displacement: complete movement;
- environmental injury: full stateful damage pipeline;
- persistent sound-related conditions: status lifecycle;
- special interactions from sound Moves: move-specific behavior;
- Soundproof or similar: Abilities;
- Trainer interrupts/specialized field mechanics: Trainer Features/perks;
- autonomous tactical rescue or exploitation: AI tactical policy;
- authoritative audiovisual reproduction: Minecraft/Cobblemon/Craftics adapter/playback.

## Mechanical uncertainty retained

Direct PTU/Caelo verification is still required before mapping field observations to Skills, Features, sound-based Moves, hearing capabilities, Ability interactions or persistent conditions. No Caelo acoustic overlay was verified in the narrative source material inspected for this pass.

## Canon uncertainty retained

No acoustic mystery location, affected species, facility, operator or historical baseline has been approved. Pass 315 remains research/design/proposal material only.