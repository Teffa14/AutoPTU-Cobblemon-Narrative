# Site interpretation and private inference research — Pass 386

Date: 2026-09-09
Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE

## Repository inspection and deduplication

The complete recursive repository tree on `main` at `3c0c64b03fcc986cfd1a29a01677ede70cd35d16` was inspected before writing. Relevant owners and contracts reviewed include `CURRENT_FOCUS.md`, canon governance, `OUROS_SITE_EVIDENCE_LEDGER_V1`, `OUROS_SITE_OBSERVATION_KNOWLEDGE_V1`, `KnowledgeLedgerStore`, Passes 383–385 archaeology/site evidence design and tests, global-NPC CI, and the Kairos/PTU source router.

The existing research corpus was searched before source selection. Frequently reused sources including The Alexandrian, Pokémon Rollout!, The Reckless Rollers, Pokémon Ashen Frost, Pokémon Gaia, Pokémon Wastelands, Pokémon Infinity, Pokémon Golurk Rising, PokéTaka, Pokémon Dreamstone Mysteries, CIDOC CRM/CRMsci/CRMba, CIfA and Historic England were not selected again as primary anchors.

Read-only engine evidence was refreshed. AutoPTU-Java remains `01a7787048ba92068f8c1340d80c9e9cb89c371d` (merge #419). AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Neither engine repository was modified.

## Research question

How should Ouros preserve a character's interpretation of physical evidence as private, revisable knowledge without treating that interpretation as direct observation, world truth or evidence known automatically by peers?

## Source 1 — archaeological inference is layered and increasingly interpretive

Christopher Evans, “Historicism, chronology and straw men: situating Hawkes' ‘Ladder of inference’,” Antiquity 72(276), 1998. Public abstract/metadata via Cambridge Core:
https://www.cambridge.org/core/journals/antiquity/article/abs/historicism-chronology-and-straw-men-situating-hawkes-ladder-of-inference/846706EC05465739D9D91BC3D09E224C

Hawkes' well-known ladder became a durable archaeological framework for discussing how claims can move from relatively direct material description toward increasingly abstract claims about past social systems or beliefs. Later archaeology debates and revises the limits of that framework, but the useful design lesson for Ouros is narrower: an observation and a higher-level explanation should remain distinguishable records.

Reusable Ouros structure:
- preserve the field observation even when an explanation changes;
- attach confidence to the explanation rather than retroactively strengthening the observation;
- allow later evidence to supersede an interpretation without deleting the earlier intellectual history;
- avoid turning a high-level claim into fact merely because it was authored by an expert NPC.

No real archaeological doctrine, chronology or culture is imported as Ouros canon.

## Source 2 — inference depends on transformations between past reality and surviving evidence

Richard A. Watson, “Inference in Archaeology,” American Antiquity. Public abstract via Cambridge Core:
https://www.cambridge.org/core/journals/american-antiquity/article/abs/inference-in-archaeology/42E641B2FD798C32F6C47B0636B8ADAF

The abstract frames archaeological reasoning as inference from surviving material remains through multiple processes and methodological assumptions. This reinforces a useful game-design boundary: the current visible site is evidence shaped by physical history, later alteration and methods of observation. The interpretation belongs to an actor and a moment in that evidence history.

Reusable Ouros structure:
- site revision, observation and interpretation remain separate causal layers;
- an interpreter needs an explicit provenance path to the observations used;
- two actors can produce different inferences from overlapping evidence without either receiving omniscient access to hidden site truth;
- future site revisions may change what can be observed but do not rewrite old claims.

## Source 3 — Pokémon Tectonic and region-spanning nonlinear character threads

Pokémon Tectonic official project page:
https://tectonic-game.com/

The public project description advertises a nonlinear region, multiple region-spanning character questlines, and a mystery tied to events years before the current adventure. The reusable structure is that a character thread can leave a location, acquire new context elsewhere, and later return with a different understanding of previously seen material.

Ouros transformation:
- an archaeological or ecological mystery may revisit the same persistent site several times;
- new evidence acquired elsewhere can alter an NPC's private inference when the actor actually learns that evidence;
- the original observation and earlier interpretation remain historical records;
- quest progression can be driven by changed understanding rather than by replacing every return visit with a stronger battle.

Do not import Makya, Team Chasm, named characters, regional forms, quests, dialogue, maps, bosses or plot resolutions.

## Derived Ouros design lesson

Pass 384 made site interpretation durable. Pass 385 made direct observation private to the observer. The missing boundary is actor eligibility for inference.

A world-level `SiteInterpretationRecord` must not automatically materialize in every NPC ledger. To create a private `INFERENCE` claim, the interpreting actor should already possess a valid private claim for every supporting observation. Those private claims may come from direct observation or an existing explicit communication/report path, but they must preserve the underlying observation content and provenance root.

Supersession should preserve both claims. The newer inference may point to the older private inference as its single parent lineage, while the interpretation bridge separately retains the complete set of supporting observation IDs and provenance roots. This avoids pretending the existing one-parent `Claim` field can encode a many-source evidence graph.

## PTU/Caelo boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` routes Researcher, Paleontologist, Topographer, Skills/Edges/Features, movement/terrain, campaign structure and encounter construction toward supplied PTU/Kairos sources. It explicitly remains a router, not a rules grant.

Pass 386 therefore defines no new Skill check, Feature bonus, excavation action, translation mechanic, Item, species distribution, damage rule or tactical permission.

## Encounter implementation boundary

Reduced version: persistent site evidence, private observation knowledge, private inference materialization, semantic time, world travel and explicit communications. No AutoPTU dependency.

Rich version may add unstable access, escort, rescue, evidence protection, time pressure, changing visibility or withdrawal after documentation. Such additions must be gated by exact engine capability families instead of assuming generic battle support.

Capability status from live read-only evidence:
- targeting/footprints/range/LoS — VERIFIED within audited ordinary scopes;
- base movement legality — VERIFIED within audited ordinary scopes;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED within audited deterministic scopes;
- action economy/initiative — VERIFIED for audited primitives; dedicated documentation/investigation actions remain separately gated;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism;
- move-specific behavior — INDIVIDUALLY GATED;
- abilities — INDIVIDUALLY GATED; Java #419 proves only seeded Impostor random Ability choice and subsequent RNG-stream parity for that scenario;
- items — INDIVIDUALLY GATED;
- Trainer Features/perks — INDIVIDUALLY GATED;
- AI legal-action infrastructure — VERIFIED for ordinary audited actions, not a blanket grant for new objective actions;
- AI tactical policy — BLOCKING for documentation-first, protect-evidence, rescue-first, escort, search, stabilization-first, objective-aware withdrawal and disengage-after-objective;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL/BLOCKING for persistent evidence identity, site revisions, inference acknowledgement, non-KO objectives and authoritative end-to-end playback.

No capability category is promoted by this research pass.
