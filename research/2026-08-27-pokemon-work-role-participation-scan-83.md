# Pokémon Work Roles, Assignment, Supervision & Participation Research — Pass 83

Status: research and provenance only. Nothing in this file is Ouros canon.

Date: 2026-08-27

## Research question

Ouros already has a broad workplace/staffing layer and a Pokémon agency/partnership layer. Both mention Pokémon participating in work. What remains under-specified is the operational lifecycle for one exact Pokémon taking part in one exact task: why that individual is assigned, which evidence supports the assignment, who supervises it, when it is active, what happens when the Pokémon pauses or withdraws, how a handoff works, and which system owns the resulting work product.

This pass asks how to make Pokémon visibly participate in ordinary institutions without reducing them to species/type resource slots and without turning Minecraft/Cobblemon presentation into PTU authority.

## Internal repository gap check

The full repository tree was inspected before external research.

Relevant existing boundaries:

- `design/workplaces-professions-staffing-layer.md` already models workplaces, roles, assignments, shifts, staffing, handoffs and ordinary careers. It explicitly says Pokémon participation should preserve individual identity, observed suitability and authoritative Capability/Move/Ability evidence when mechanics matter.
- `design/pokemon-agency-partnership-release-layer.md` already separates persistent identity, association, ownership/custody, active Trainer, temporary partnership, refusal, release and post-release continuity.
- `design/care-recovery-welfare-layer.md` already owns medical/welfare observations and recovery.
- `design/worksite-safety-near-miss-incident-learning-extension.md` already owns safety observations, restrictions and return-to-work decisions.
- `design/shared-equipment-lending-issued-assets-extension.md` already owns issued/shared equipment.
- `design/credentials-authorizations-recognition-extension.md` already owns human/institutional authorization evidence.
- `design/cobblemon-runtime-authority-boundary.md` is binding: Cobblemon may embody and present the Pokémon world, while Ouros chooses participants/world facts and AutoPTU owns tactical facts.

The missing object is therefore not another workplace or Pokémon relationship system. It is an assignment/participation extension linking those systems around one Pokémon's concrete work episode.

## Source 1 — Official Pokémon Sword/Shield: Poké Jobs

Source:
https://swordshield.pokemon.com/en-us/gameplay/pokejobs/

The official Sword/Shield site describes Galar as a region where people and Pokémon commonly work together. Companies and universities publish Poké Jobs, Trainers select Pokémon to send, and the assignment has a defined period and return/completion point.

Reusable structure:

- institutional demand can be explicit rather than improvised;
- Pokémon participation can have a start and end instead of being an indefinite background fact;
- different organizations can request different kinds of assistance;
- assignment can occur even when the Pokémon is not physically following the Trainer in the overworld.

Do not import:

- type-based suitability as an Ouros default;
- experience/base-point rewards;
- output bonuses from assignment duration;
- reward items;
- the Rotomi/Box workflow as universal technology.

Ouros implication:

The useful pattern is `posting/request -> selected individual -> bounded assignment -> observed completion/return`. Suitability should be derived from the individual Pokémon's authoritative and observed state, not a hidden species/type productivity table.

## Source 2 — Pokémon animated series: Bibarel Gnaws Best!

Sources:
https://bulbapedia.bulbagarden.net/wiki/Bibarel_Gnaws_Best%21
https://bulbapedia.bulbagarden.net/wiki/Isis

A bridge project stalls when a trained Bibarel refuses to cut more stone. Other Pokémon are able to cut material, but the resulting pieces are not made to the required specification. The later explanation is that the construction plan itself is unsafe; the Pokémon's refusal was not simply lack of cooperation.

Reusable structure:

- two actors capable of superficially similar actions need not be interchangeable workers;
- work quality can depend on training/history/context rather than species stereotype;
- refusal can be an observation that triggers review rather than an automatic morale/obedience conclusion;
- deadline pressure can conflict with technical/safety evidence;
- a work interruption can reveal a larger institutional problem.

Ouros implication:

An assignment record should preserve why a Pokémon was considered suitable, what task standard was expected, and what was actually observed. A refusal or unexpected pause should generate the smallest defensible event and may trigger a supervisor/safety review. It must not automatically lower Loyalty or invent an emotion.

## Source 3 — Expert stonecutter / Pokémon work crews

Sources:
https://bulbapedia.bulbagarden.net/wiki/Expert_stonecutter
https://bulbapedia.bulbagarden.net/wiki/Isis

The same story shows several distinct work relationships around Pokémon: a trained specialist Pokémon, a crew of Machoke/Machamp used for carrying stone, a temporary foreman, and an experienced stonecutter who possesses domain expertise humans around the site do not all share.

Reusable structure:

- work can have multiple roles with different capability requirements;
- supervision, planning, transport and execution are separate tasks;
- a workplace can have continuity even when the supervising human changes;
- a Pokémon's work history can remain meaningful across supervisors.

Do not import the species-role pairing as a rule. Ouros should model the exact individual and the evidence for that exact assignment.

## Source 4 — PTU community: Ranger as occupation rather than Trainer Class

Source:
https://www.reddit.com/r/PokemonTabletop/comments/izr3b3/

A public PTU discussion notes that a character can fictionally be a Ranger as a job even without a dedicated PTU Ranger class. The discussion also illustrates why homebrew attempts to force temporary wild-Pokémon control into PTU mechanics can become mechanically incompatible or difficult to balance.

Reusable structure:

- narrative profession and Trainer Class are separate;
- institutional role does not need a bespoke mechanical class;
- temporary cooperation should not be allowed to silently rewrite party/capture/battle rules.

This is community discussion, not governing PTU rules. Any mechanical consequence must be checked against the supplied PTU/Caelo corpus.

## Source 5 — Public PTU campaign: labor/construction organization as a persistent faction

Source:
https://www.reddit.com/r/PokemonTabletop/comments/xcgcx0/

A public Orre campaign write-up includes a former labor/construction group as one element in a wider regional political and corporate history. The particular names and plot are distinctive to that campaign and are not reusable.

Reusable structure:

- workforces and trade groups can have institutional history rather than existing only as anonymous background NPCs;
- development projects can connect labor, equipment suppliers, media, research and regional politics;
- a workplace story can persist after the original organization changes or disappears.

Ouros implication:

Pokémon work-participation history should be able to attach to institutions and projects that outlast one shift. It should not create a labor faction automatically; that remains a canon decision.

## Source 6 — Cobblemon Poser / animation surface

Source:
https://wiki.cobblemon.com/index.php/Poser

Current Cobblemon documentation describes data-driven Pokémon poses and named animations, including idle/movement states, cries and layered/primary animations. The documentation gives addon creators hooks for visual behavior without requiring that the animation system own gameplay semantics.

Reusable implementation lesson:

- work participation can be made visually rich using Cobblemon's existing model/pose/animation surfaces;
- Ouros can project an assignment state into an appropriate pose or authored animation;
- animation completion must never become proof that a PTU action, work output or tactical effect occurred.

This aligns with `design/cobblemon-runtime-authority-boundary.md`: safe presentation can be reused aggressively while mechanical truth stays upstream.

## Negative pattern — Pokémon as typed workforce tokens

Several Pokémon games and community proposals abstract labor as “send N Pokémon of a matching Type” or “donate a Type to maintain a facility.” This is useful for lightweight management games, but it is a poor fit for Ouros' persistent-actor goals.

Ouros should avoid:

- `fire_type_worker_count` as a substitute for actual Pokémon identity;
- assuming an Electric-type generates power;
- assuming a Fighting-type can lift a specific load;
- assuming a Water-type can operate a pump;
- replacing one trained individual with any same-species spawn;
- deleting work history when the entity leaves a chunk or party.

When the task has mechanical stakes, the requirement should resolve to exact authoritative evidence: a Move, Ability, Capability, Skill/Feature relationship, current movement profile, item/equipment interaction or other governing PTU/Caelo state. When no mechanical rule is needed, the contribution can remain authored world behavior with explicit observed history and no invented numeric output.

## Derived design lessons

### Assignment is an event, not a species property

The durable object should connect one Pokémon to one role/task in one time window.

### Eligibility must be explainable

A task may cite:

- observed prior performance;
- an authoritative Move/Ability/Capability relevant to the exact task;
- an institutional training record;
- a supervised trial;
- a temporary partnership scope;
- equipment compatibility that has actually been verified.

It should never cite only `species` or `type` when the task has meaningful mechanical or safety consequences.

### Refusal/withdrawal remains bounded

Record facts such as:

- did not begin the assigned task;
- stopped after a specific event;
- moved away from one work area;
- did not respond to one handler cue;
- returned after conditions changed.

Do not infer laziness, anger, fear, disloyalty, exploitation or consent to future work without evidence/canon.

### Work output belongs to the system that owns the work

Examples:

- Maintenance owns whether a repair is complete;
- Travel owns whether a transport service operated;
- Care owns whether treatment occurred;
- Construction/public works owns whether a project stage is complete;
- Courier owns whether a shipment advanced;
- Conservation owns a stewardship operation outcome.

The participation layer only records who contributed, under what scope, and what was observed.

### A Pokémon can be present and off duty

Physical presence at a worksite is not assignment state. This matters directly for Minecraft/Cobblemon: an entity loaded near a work area cannot be treated as a worker merely because it is nearby.

### A work role grants no battle bonus

A stonecutter, search partner, courier helper, clinic assistant or survey Pokémon does not receive Accuracy, movement, damage, initiative, Intercept, terrain or objective bonuses merely from the occupational label.

## PTU/Caelo review boundary

Before a work assignment has mechanical consequences, implementation must reopen the project-supplied PTU/Caelo sources for the exact claim involved. Potentially relevant families include:

- movement Capabilities and movement modes;
- weight/lifting/carrying rules if the project uses them;
- Skills and Command interactions;
- Loyalty/obedience rules;
- Moves that can legally affect objects/environment;
- Abilities that explicitly apply outside battle;
- Trainer Features that change cooperation, handling or field use;
- item/equipment rules;
- healing/care rules;
- capture/party/ownership rules where relevant.

No narrative occupational title can substitute for those rules.

## Research conclusion

The valuable addition is a Pokémon work-participation extension under the existing Workplaces + Pokémon Agency architecture. It should preserve individual identity, evidence-backed suitability, supervision scope, bounded assignment windows, withdrawal/handoff history and welfare/safety integrations.

It should use Cobblemon aggressively for embodiment and animation, while preserving the binding authority direction:

`Ouros work/world state -> explicit encounter decision when needed -> AutoPTU authoritative battle -> adapter -> Cobblemon presentation`.

No source in this pass establishes a new Ouros institution, labor law, universal employment norm, Pokémon-rights framework, species occupation, compensation policy or PTU mechanic.