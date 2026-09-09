# Site observation and private knowledge research — Pass 385

Date: 2026-09-09
Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE

## Repository inspection and deduplication

The recursive main-branch tree at `e4b56136acc9fae9986caa13dd2dd2b2cd4550cd` was inspected before external research, along with `CURRENT_FOCUS.md`, `canon/README.md`, Pass 383/384 archaeology research/design/proposal files, `tools/global_npc_site_evidence.py`, `tools/global_npc_memory.py`, the site-evidence regression, the global-NPC CI workflow and `sources/kairos/KAIROS_SOURCE_INDEX.md`.

The research corpus already contains W3C PROV, Pokémon Containment, Pokémon Desolation Ranger quests, Pokémon Gaia, Pokémon Wastelands, Pokémon Golurk Rising, PokéTaka, Pokémon Dreamstone Mysteries, Pokémon Infinity, Pokémon Bushido, Pokémon Odyssey, Pokémon Prisme, Pokémon Stalactite and other recent anchors. They were not reused as primary sources in this pass.

The immediate gap after Pass 384 is narrower than general archaeology: durable world observations exist, and private NPC claims exist, but there was no explicit owner proving when one direct site observation became private knowledge of the actor who actually observed it.

## Source 1 — CIDOC CRM / CRMsci

Sources:
- CIDOC CRM home: https://cidoc-crm.org/
- CRMsci Scientific Observation Model: https://cidoc-crm.org/crmsci/
- CRMba archaeological buildings extension: https://cidoc-crm.org/crmba

Accessed: 2026-09-09.

CIDOC CRM provides a formal structure for integrating cultural-heritage information from different sources without flattening all records into one mutable description. CRMsci specializes that approach for scientific observations, measurements and processed data, with emphasis on semantic and causal relationships. CRMba applies compatible modelling to archaeological buildings, physical phases, stratigraphic relationships and interpretation of material evidence.

Reusable Ouros lesson: the world evidence record, the act of observation and what a particular actor knows should remain separately identifiable. Integration should connect those records through explicit relationships rather than shared database visibility.

Transformation for Ouros: `OUROS_SITE_EVIDENCE_LEDGER_V1` remains the world-evidence owner. Pass 385 adds only a provenance-preserving bridge into the existing private knowledge ledger for the named observer. It does not claim CIDOC/CRMsci conformance and does not import ontology classes into canon.

## Source 2 — Pokémon Tabletop United campaign log on Giant in the Playground

Source: https://forums.giantitp.com/archive/index.php/t-527075.html
Accessed: 2026-09-09.

This public PTU campaign log repeatedly lets player knowledge emerge from physically entering locations, inspecting unstable or damaged structures and discovering what still works or what changed. One logged sequence has the party enter a damaged Pokémon Center, inspect a machine obstructed by rubble and discover usable supplies after interacting with the site.

Reusable Ouros lesson: access to a place can create actor-specific information and new choices. The important structure is not the specific ruined town or objects; it is that the people who were present acquire information because they directly encountered evidence.

Transformation for Ouros: a direct site observation can become knowledge for its observer at the same semantic time. Other NPCs do not gain the observation unless another explicit process carries it to them. No characters, locations, dialogue, accidents, combat events or plot from the campaign log are copied.

## Source 3 — Pokémon Frozen Spirit

Source: https://frozen-spirit.com/en/
Accessed: 2026-09-09.

The public project page presents an original region with varied environments, local legends and exploration framed through what the player encounters while travelling through those spaces.

Reusable Ouros lesson: environmental storytelling gains value when information is attached to actual places and encounters instead of appearing as universal exposition. Different actors may therefore know different parts of the same regional story because they visited different sites or visited the same site in different states.

Transformation for Ouros: site revisions and observations can support geographically distributed mysteries where knowledge spreads only after direct observation, records access or communication. No Essoria geography, characters, regional forms, legends, plot or artwork is imported.

## New synthesis

Pass 384 already protects four boundaries:

`SITE_REVISION != OBSERVATION`

`OBSERVATION != INTERPRETATION`

`CURRENT_SITE_STATE != HISTORICAL_OBSERVATION`

`REVISED_INTERPRETATION != MUTATED_OBSERVATION`

Pass 385 adds another:

`WORLD_OBSERVATION != UNIVERSAL_PRIVATE_KNOWLEDGE`

A durable observation can exist in world provenance without every managed NPC knowing it. A direct-observation materialization is valid only for the actor named as the observer. Institutional peers, later visitors and nearby actors require their own observation, archive access, report or communication event.

The materialized private claim uses a dedicated observation subject and the observation content as its value. Confidence 100 means the actor has a durable claim that this is what they directly recorded; it does not elevate a later interpretation or theory to world truth.

## PTU/Caelo cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing aid rather than a rules grant. It identifies the supplied Kairos/PTU material for Skills/Edges/Features, utility classes including Researcher, Paleontologist and Topographer, movement/terrain, campaign structure and encounter creation.

Pass 385 does not create a Perception check, Researcher Feature, Topographer bonus, excavation action, item rule, species distribution or automatic archaeological success rule. If a future authored observation requires a specific Trainer Feature, skill, Move, Ability, item, terrain interaction or tactical action, that exact rule must be verified against the supplied PTU/Caelo source and current engine contracts.

## Read-only engine evidence

AutoPTU-Java head inspected: `01a7787048ba92068f8c1340d80c9e9cb89c371d`, merge #419. The new parity evidence freezes Python-compatible Impostor random ability choice and the next RNG-stream value for a seeded scenario. This strengthens only the pinned Impostor RNG-consumption seam. It does not establish complete Ability coverage, target selection generally, lifecycle completeness or narrative observation behavior.

AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change remains presentation-only viewport synchronization.

Neither engine repository is modified by this pass.

## Narrative direction opened by the seam

A recurring investigator can truthfully remember a feature that later visitors cannot see because the physical site changed after the observation. That produces a mystery without requiring anyone to lie and without granting later actors access to the first observer's evidence automatically.

This structure supports testimony disputes, missing evidence, delayed corroboration, revisits, institutional skepticism and archive-driven investigation while preserving exact provenance.
