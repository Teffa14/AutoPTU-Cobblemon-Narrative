# Post-Restore Baseline and Conditional Access Scan — Pass 405

Status: RESEARCH / NON-CANON
Accessed: 2026-09-10
Canon effect: NONE

## Internal inspection and duplicate avoidance

The complete recursive repository tree on `main` at `50a4614f7952a509966af01d28aa1610c601252f` was inspected before writing. Relevant current-focus, canon-governance, research, proposal, design, implementation, test, tool and source-index material was reviewed, with particular attention to Passes 396–404, WorldResource checkpoints, holder transitions, bounded holder-history coverage, recovery reconciliation and the PTU/Caelo/Kairos routing index.

Repository searches were also used to reject resurfaced sources. Pokémon Burning Scales, Pokémon Odyssey and the PTU campaign-log pattern where prior treatment of wild Pokémon later explains local hostility are already represented in existing research and were not reused as primary sources.

## Implementation finding: a recovery baseline cannot validate its own cut

Pass 404 made `HolderHistoryCoverageBaseline` issuance deterministic from an exact `OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1` generation.

A naïve next step would feed a baseline emitted from the recovered catalog at semantic minute T back into reconciliation of that same catalog at T. That is circular. The current holder in the catalog would become the starting assertion used to prove the current holder in the same catalog. Worse, doing this could suppress visibility of incomplete or contradictory pre-T holder history.

Pass 405 therefore treats recovery-time baseline issuance as a post-validation handoff. Historical reconciliation runs first using only evidence that predates or independently constrains the current catalog. If activation is safe, the exact selected catalog checkpoint may then issue a baseline that begins a new bounded coverage interval after T.

This preserves the Pass 403 rule: a baseline can establish continuity from its own authoritative cut forward, never backward.

## New public source: Pokémon Rejuvenation — Prince from the Sands

Source: https://rejuvenation.wiki.gg/wiki/Prince_from_the_Sands

The public quest guide records a useful high-level consequence pattern. The same optional scene can resolve with different friction depending on an earlier outcome: under one previously established condition, an opposing group leaves rather than forcing the later battle.

Reusable structure for Ouros:

Earlier conduct or outcomes can change the set of later responses available to NPCs without changing the physical objective of the later scene. A later obstacle can become negotiation, cooperation, verification or combat depending on what relevant actors know and how they assess prior conduct.

Ouros transformation:

Do not encode this as a hidden omniscient morality flag. A changed response should arise from persisted relationship state, explicit institutional records, witnessed conduct, communicated evidence or another provenance-backed fact available to the deciding NPC. If the deciding actor never learned the earlier event, the event cannot silently change that actor's behavior.

No Rejuvenation character, faction, place, reward, dialogue, plot event or battle is imported.

## New public source: Pokémon Sacred Phoenix

Source: https://www.sacredphoenix.fr/

The public project page describes a Pokémon fan game built around a dedicated quest system, broader strategic choices and an alternate fantasy setting rather than merely replaying the standard badge structure.

Reusable structure for Ouros:

A Pokémon world can support multiple forms of obligation and advancement when quests are treated as first-class structures rather than disposable errands between battles. Access, trust, local responsibility and investigation can carry progression value without requiring every beat to resolve through combat.

Ouros transformation:

Optional and institutional work should alter future opportunity through world state and actor knowledge. It should not silently grant mechanical bonuses, species access, Trainer Features or supernatural permissions. Any PTU-facing benefit must still be checked against project-approved rules.

No Sacred Phoenix setting, mythology, mechanics, characters, quest text or plot is imported.

## New Ouros pattern extracted

A route closure, restricted work site, temporary checkpoint or controlled facility can present the same physical constraint to every party while producing different lawful options for different actors.

The deciding NPC should evaluate only evidence available to that actor. Prior reliable conduct may cause the NPC to explain a provisional detour, request assistance, offer supervised access or accept a narrower verification step. Missing evidence leaves the ordinary restriction in force. Contradictory evidence can justify additional supervision or refusal without making either side omniscient.

The useful consequence is option-shaping rather than binary reward/punishment. Earlier world history changes how a later problem can be approached while preserving the later problem itself.

## PTU/Caelo/Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked only as a router into supplied source material. Potentially relevant families include Skills/Edges/Features, Researcher, Chronicler, Survivalist, Topographer, movement/terrain, hazards, encounter construction, recurring rivals/villains and Items/Gear.

No Skill check, Edge, Trainer Feature, Item effect, access bonus, reputation modifier, movement exception, reaction, weather rule or encounter rule is approved by this research note.

## Live engine evidence

AutoPTU-Java read-only head inspected: `a27a27cb542f1b979b19abae4138261f322ca10e`, merge #428, `Freeze pinned switch post-entry call contract`.

The new evidence freezes the ordered post-entry semantic families observed in the pinned Python switch path: Ball Fetch, Curious Medicine, replacement initiative insertion, First Blood and Quick Switch. This is a staging/parity contract for that exact switch seam. It does not prove complete implementation of those Trainer Feature/Ability families, switching as a whole, action economy, initiative replacement semantics or full turn lifecycle.

AutoPTU Python read-only head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its latest change remains presentation-only and does not alter tactical rules or outcomes.

## Capability implications for the new proposal

A reduced conditional-access encounter can remain entirely in persistent-world systems: relationships, knowledge, institutional permissions, travel, communication, site state, obligations and evidence provenance.

A mechanically rich version that places the detour inside an unstable or contested tactical space requires exact capability gating. Targeting/footprints/range/LoS, base movement legality and core calculations remain verified only in audited scopes. Action economy/initiative remains partial overall. Complete movement, including push/pull/knockback/interception/forced movement, remains partial. Full turn/round lifecycle, full stateful damage pipeline and status lifecycle remain partial. Terrain/weather/hazards/zones/reactions remains mixed/partial/blocking by mechanism. Move-specific behavior, Abilities, Items and Trainer Features/perks remain individually gated. AI legal-action infrastructure is verified only in ordinary audited scopes. AI tactical policy and Minecraft/Cobblemon/Craftics objective playback remain blockers for several non-KO behaviors.
