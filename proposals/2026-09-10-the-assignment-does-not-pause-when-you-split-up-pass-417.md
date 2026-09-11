# The Assignment Does Not Pause When You Split Up — Pass 417

Status: PROPOSED / NON-CANON

Research provenance: research/2026-09-10-shared-assignment-field-team-scan-417.md

Premise

A field assignment has one durable identity but more than one participant. The player follows one participant while another named NPC continues a different part of the same work off-screen.

The task does not clone into separate quest instances. Each participant keeps their own schedule, route, permissions, observations, obligations and knowledge.

Core structure

A practical assignment can be divided into two or more work fronts. Examples include checking two observation points, collecting one record while another person inspects a site, delivering equipment while another actor confirms access, or following two leads that must later be compared.

The participants may begin together and separate. They can also start in different places after receiving the same assignment through different channels.

The world records which actor actually performed each action. Being on the same assignment never creates automatic knowledge sharing.

Rejoining

When the actors meet again, they may exchange observations, documents or warnings. Only that exchange can make one participant know what the other learned.

If the NPC returns first, the player may arrive to find that some work was completed, another part failed, a route changed, or a new follow-up became necessary. The result must follow the NPC's real schedule, access, knowledge and actions rather than a hidden script that waits for the player.

If the player returns first, the NPC can still be in transit or working elsewhere. The quest UI should not silently mark that work complete until the corresponding world event exists.

Candidate Ouros surfaces

Existing institutions such as Marea Field Office, Estación Mirador, Tideglass Archive or Loma Clara Producers Cooperative can support this structure because they already create plausible observation, record, logistics and field-work obligations.

No new assignment, incident or institutional duty is canonized by this proposal.

Reduced implementation

The reduced version uses only world-level systems already present or explicitly modeled in Ouros:

semantic time; schedules; travel; obligations; permissions; private knowledge; durable memory; explicit communication; provenance; persistent observations; event-driven replanning.

The NPC's off-screen contribution stops at the normal AutoPTU handoff if structured mechanics become necessary.

Full encounter version

A richer version can split responsibilities during a dangerous retrieval, survey, escort or extraction. One actor may protect a specialist while another reaches an objective. The narrative premise does not require KO victory.

Mechanical dependency classification

Targeting/footprints/range/LoS is required if protection or interaction depends on exact tactical positioning.

Base movement legality is required for ordinary tactical pathing.

Complete movement including push/pull/knockback/interception/forced movement is required if actors can be displaced, dragged, intercepted or repositioned by rescue effects.

Core calculations are required for ordinary audited battle math.

Action economy/initiative is required when participants have distinct tactical turns or action budgets.

Full turn/round lifecycle is required for timed protection, staged extraction, delayed failure or multi-round objectives.

Full stateful damage pipeline is required if damage consequences must persist through the encounter or into world state.

Status lifecycle is required if ongoing conditions affect assignment completion or extraction.

Terrain/weather/hazards/zones/reactions is required for active environmental pressure, weather phases, triggered areas or reaction windows.

Move-specific behavior, Abilities, Items and Trainer Features/perks remain individually gated when a concept relies on them.

AI legal-action infrastructure is required for specialized actions such as protect, retrieve, escort, interact, carry or extract.

AI tactical policy is required for decisions such as objective-first movement, protecting the other participant, abandoning a secondary objective, or withdrawing after enough evidence has been secured.

Minecraft/Cobblemon/Craftics adapter/playback support is required to represent authoritative objective state, participant position, interaction and non-KO completion without duplicating PTU rules.

Fallback rule

If any full-version dependency is not verified, keep the same shared-assignment premise and run the reduced world-level version. Minecraft must not invent the missing tactical rule family.

Canon questions

No answer is proposed yet for whether any existing Ouros institution routinely assigns paired field work, how formal shared assignment ownership should be represented in canon, or which NPC pair should first demonstrate this structure.
