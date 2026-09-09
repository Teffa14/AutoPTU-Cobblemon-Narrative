# The Wall That Was Recorded Twice

Status: PROPOSED / NON-CANON
Canon approval: NONE

## Premise

Two field teams produce records of the same stable site identity at different semantic times. The first record shows a continuous wall face. The second record, made after a physical intervention or natural exposure, shows an opening and a lower construction line that could not previously be seen.

Both records can be accurate.

The mystery is not resolved by choosing which team is trustworthy. The players must reconstruct which physical site revision each observation belongs to, what changed between visits and which later interpretations are actually justified by the available evidence.

No location, culture, institution, construction date, cause of the revision, species population or final explanation is canonized by this proposal.

## Reduced implementation

The reduced form requires no AutoPTU encounter.

It uses:
- stable site identity and sequential physical revisions;
- semantic time;
- site observations tied to exact revisions;
- observer-only private knowledge;
- inference materialization only from evidence the actor privately knows;
- `OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V1` for restart-safe coherence;
- existing travel and communication systems when different actors must compare records.

The player can solve the immediate contradiction by finding enough dated observations to demonstrate that the two teams saw different physical states. The larger meaning of the opening can remain unresolved.

## Rich implementation

A richer version can put the second documentation event under pressure. Possible objectives include keeping an observation point accessible long enough to document it, escorting a specialist, protecting measuring equipment, retrieving a context record before evacuation or leaving safely after enough evidence has been recorded.

Battle is optional pressure. Defeating every opponent is not the default success condition.

## Exact engine dependencies

targeting/footprints/range/LoS: VERIFIED within audited ordinary contracts if a tactical scene only needs ordinary targeting.

base movement legality: VERIFIED within audited ordinary movement contracts.

complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Any falling, dragging, forced slide, rescue reposition, push or interception version depends on this family.

core calculations: VERIFIED within audited deterministic contracts.

action economy/initiative: VERIFIED for audited primitives. New documentation, stabilization or evidence-protection actions are not automatically admitted.

full turn/round lifecycle: PARTIAL. Timed collapse windows, phased access loss or delayed environmental changes depend on exact lifecycle support.

full stateful damage pipeline: PARTIAL.

status lifecycle: PARTIAL.

terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by mechanism. Dust zones, unstable floors, flooding, debris, reaction cave-ins or delayed hazards require explicit verified support for each mechanism.

move-specific behavior: INDIVIDUALLY GATED.

abilities: INDIVIDUALLY GATED. Current Java evidence around Impostor does not generalize to environmental or objective interactions.

items: INDIVIDUALLY GATED. Measuring, stabilization or protection equipment needs explicit world or battle contracts before becoming mechanical.

Trainer Features/perks: INDIVIDUALLY GATED. Researcher/Paleontologist/Topographer references in supplied PTU/Kairos material are routing evidence, not automatic Ouros permissions.

AI legal-action infrastructure: VERIFIED for ordinary audited actions; documentation-first, stabilize-site and protect-evidence actions need explicit legal-action admission.

AI tactical policy: BLOCKING for documentation-first, escort, protect-evidence, rescue-first, stabilization-first, objective-aware withdrawal and disengage-after-objective.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING for stable site-feature identity, physical revision projection, non-KO objective acknowledgement, evidence interaction and authoritative end-to-end playback.

## Canon questions left open

The site location, responsible institution, reason for the physical change, permitted field methods, relevant species/habitat, available communications, exact PTU skill/Feature gates and final historical interpretation all require separate authority before promotion.
