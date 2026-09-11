# Negotiated Assistance and Counterproposal Scan — Pass 432

Status: RESEARCH / NON-CANON
Date: 2026-09-11

## Repository review before research

The complete recursive `main` tree at `a5e152294237e731debf57313cae46f04f40f135` was inventoried before writing. Current focus, canon governance, the fixed Marea resident network, questline taxonomy, Passes 422–431, world-action persistence, response delivery/replanning, commitments, deferrals, coherent assistance checkpoints, current tests/tools and the Kairos source index were checked.

Repository search was also run against candidate source names before selection. Frequently reused PTU actual plays, Pokémon World Tour: United, The Reckless Rollers, Pokémon Adventures in the Millennium, Kehalo, Rainbow Wing, Rejuvenation, Pentiment, Roadwarden, Citizen Sleeper, Six Ages, Heaven's Vault and other recent anchors were not reused as primary sources.

This pass selected sources that contribute a narrower lesson: an answer can alter the terms of cooperation without becoming acceptance.

## Source 1 — Supergiant's Pyre: outcomes remain history instead of being reset

Public source:
https://www.gadgets360.com/games/features/pyre-interview-supergiant-games-bastion-transistor-1721224

Additional design discussion:
https://www.gamedeveloper.com/design/making-a-multi-character-rpg-narrative-in-supergiant-s-i-pyre-i-

Observed high-level structure:

Pyre was designed so wins and losses can both remain part of the continuing story. Characters remember prior confrontation outcomes, later meetings can reflect those outcomes, and failure does not force a reset to the only approved branch.

Reusable Ouros lesson:

Assistance negotiation should preserve each answer as history. If a recipient cannot satisfy the original request but can offer a smaller, later or differently located contribution, the engine should not collapse that into ACCEPT or REJECT. The changed terms are themselves durable world state.

Transformation rule:

Do not copy Pyre's characters, rites, exile premise, liberation structure, dialogue, competition rules or plot. Only retain the abstract consequence pattern: prior outcomes persist and later interactions respond to them.

## Source 2 — public PTU campaign recruitment: roleplay/exploration can outrank combat

Public source:
https://www.reddit.com/r/lfg/comments/1l92gb7/

Observed high-level structure:

The campaign advertises an original-setting Pokémon Tabletop United game where roleplay and exploration take precedence over combat, with theatre-of-the-mind available when useful. This is a small but relevant community example that PTU play does not need every meaningful problem or agreement to terminate in tactical combat.

Reusable Ouros lesson:

A counterproposal can create useful gameplay entirely in world simulation. A changed meeting time, restricted work scope, remote observation offer or alternate helper can matter before any battle system is involved.

Transformation rule:

Do not copy the campaign's setting, characters, plot twists, table rules, tone or session structure. The only imported lesson is the viability of roleplay/exploration-first PTU play.

## Source 3 — AutoPTU-Java live evidence: replacement initiative runtime handoff

Read-only repository evidence:
`Teffa14/AutoPTU-Java` head `2f72abe6c0e2b58533856484a1cc954f9e6648e8`, merged PR #445 on 2026-09-11.

Observed implementation change:

The production switch-entry dispatcher now has a `ReplacementInitiativePostEntryHandler`. Caller policy carries `allowReplacementTurn` and `allowImmediate`; the handler derives the candidate from authoritative battle state and invokes the canonical initiative insertion mutation.

Capability interpretation:

This is stronger evidence than the previous oracle-only seam, but it verifies a replacement-switch initiative path, not the entire action economy/initiative family. It does not prove complete round lifecycle, arbitrary interrupts, reactions, Trainer Feature timing or every initiative transition.

Therefore `action economy / initiative` remains PARTIAL.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains the project routing aid for movement, combat, status, hazards/weather, encounters, Items, Abilities and Trainer mechanics. The index explicitly is not a replacement for the supplied source PDFs.

Pass 432 introduces no new PTU rule claim. Structured counterproposal terms are world-agent negotiation state. If accepted work later enters tactical resolution, the exact encounter must still declare and satisfy its mechanical dependencies.

## Extracted reusable structures

1. Response history should be durable even when it does not solve the original request.
2. A changed offer deserves its own structured terms instead of being encoded only in prose.
3. Time, place, scope and alternative course are separable negotiation dimensions.
4. Proposing terms does not reserve them.
5. The requester must learn the terms through explicit communication; durable global storage alone cannot create private knowledge.
6. A non-combat version should remain playable when the narrative premise is negotiation, scheduling, observation, repair, delivery or investigation.
7. If the negotiated job later becomes tactical, capability admission occurs at that later boundary.

## New Ouros candidate pattern

Working name: `The Help Comes With Different Terms`

Status: PROPOSED / NON-CANON.

A field coordinator asks a specialist for assistance. The specialist cannot satisfy the request exactly. Instead, the specialist proposes one or more changed terms: later timing, another site, narrower work, or a different way to contribute. The coordinator must receive those terms before reacting to them. Neither side is treated as having agreed until a later explicit decision creates that agreement.

The pattern can use existing Marea roles for regression without creating new canon. Mara Veyra can request practical assistance. Teo Lark can propose repair/inspection work. Nerea Sol can be relevant to observation or evidence quality. These are existing role surfaces only; no new incident or relationship fact is approved by this note.

## Encounter dependency classification

Reduced version:

No AutoPTU requirement. Uses semantic time, private knowledge, explicit communication, world-action intents, structured counterproposal terms, schedules, permissions, travel constraints and selective replanning.

Full tactical version, when the negotiated job becomes an encounter:

- targeting / footprints / range / LoS — VERIFIED only for audited scopes;
- base movement legality — VERIFIED only for audited scopes;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED only for audited scopes;
- action economy / initiative — PARTIAL;
- full turn / round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain / weather / hazards / zones / reactions — MIXED / PARTIAL / BLOCKING by exact behavior;
- move-specific behavior — individually gated;
- abilities — PARTIAL and individually gated;
- items — individually gated;
- Trainer Features / perks — individually gated;
- AI legal-action infrastructure — VERIFIED only for audited ordinary actions; specialized objectives need explicit admission;
- AI tactical policy — BLOCKING for specialized rescue/escort/protect/retrieve/extract behavior;
- Minecraft / Cobblemon / Craftics adapter/playback — PARTIAL / BLOCKING for specialized authoritative objective state, non-KO completion and in-flight recovery.

## Copyright boundary

No protected prose, dialogue, named fictional characters, encounter layouts, quests or plot sequences were imported from the external sources. All Ouros material in this pass is a transformed systems-level abstraction with source attribution retained here.
