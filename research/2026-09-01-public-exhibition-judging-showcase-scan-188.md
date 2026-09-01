# Public Exhibition, Judging and Showcase Research Scan — Pass 188

Status: RESEARCH. NOT CANON.
Date: 2026-09-01

## Purpose

This pass investigates public exhibitions, contests, demonstrations, judging, audience response and persistent event records as reusable structures for Ouros.

The repository inventory was inspected before choosing this seam. Existing work already covers festivals, battle institutions, rivals, public memory, archives, schedules, governance, permissions, aftermath, emergency operations and material culture. The canon questline taxonomy already reserves `COMPETITIVE` for battle circuits, contests, tournaments, ladders, exhibitions and institutional competitive seasons. No additional top-level quest category is needed.

The missing layer is narrower: how a public event is announced, entered, evaluated, recorded, corrected and remembered without collapsing audience reaction, institutional judgment, PTU Contest rules and battle outcomes into one value.

## Existing project boundaries

Current canon supports Bruma Battle Yard as Marea's competitive hub. Sela Orrin runs training sessions and audited battles. Jace Orrin assists sessions and seeks stronger competition. Their canon roles are sufficient for proposed battle-yard exhibitions; this pass does not create a new arena, league, festival or judging authority.

The current AutoPTU source set contains explicit PTU Contest material. Searches at Python oracle head `729bae2d424963ff9bb3f4159c9a7ac9152128a7` found:

- Coordinator Features that trigger on Appeal Rolls;
- abilities usable once per Contest;
- Adaptable Performance and other Contest-specific effects;
- move records carrying Contest Type and Contest Effect;
- compiled useful-chart data for Contest effects.

Therefore Narrative must not invent a replacement scoring system for a real PTU Contest. A social demonstration may use ordinary world procedures, but a mechanically defined PTU Contest must eventually execute the appropriate authoritative PTU rules.

No indexed `Caelo` material was found in Narrative, AutoPTU-Java or AutoPTU during this pass. This is an evidence gap, not proof that Caelo lacks contests, exhibition circuits or regional judging practices.

## Public Pokémon sources

### Pokémon Contests

Source: Bulbapedia, Pokémon Contest
https://bulbapedia.bulbagarden.net/wiki/Pokemon_Contest

Reusable pattern:

Formal competition can combine distinct evaluation phases. The games separate presentation/condition from move-based appeals, then combine those results for the declared winner. Move use can also alter competitors, audience excitement and turn order.

Ouros lesson:

An event record should preserve which phase generated which result. A final placement should not erase the underlying observations or be treated as interchangeable with crowd reaction.

Do not import Pokémon game's numeric hearts, ribbons or exact scoring unless the governing PTU/Caelo rules explicitly require them.

### Appeal mechanics

Source: Bulbapedia, Appeal
https://bulbapedia.bulbagarden.net/wiki/Appeal

Reusable pattern:

Performance actions can have context-sensitive effects: order matters, audience state matters, move combinations matter and one participant can disrupt another. This is mechanically richer than a single Charisma roll.

Ouros lesson:

If an authored event is declared to be a PTU Contest, Narrative cannot approximate this kind of interaction with a generic score. Exact Contest effects and Features must remain an engine/source dependency.

### Super Contest Shows

Source: Bulbapedia, Super Contest Show
https://bulbapedia.bulbagarden.net/wiki/Super_Contest_Show

Reusable pattern:

A single public event can evaluate different competencies independently, then publish a combined result. Visual evaluation, timing/dance and a selected move all contribute, while the venue preserves pictures of notable winners.

Ouros lesson:

Separate event execution from institutional memory. A result can later produce a poster, photograph, archive entry or wall display without making the presentation artifact the authority for the original outcome.

### Pokémon Musical

Source: Bulbapedia, Pokémon Musical
https://bulbapedia.bulbagarden.net/wiki/Musical

Reusable pattern:

Audience response can be an important consequence even where formal judging is light. Spotlight, props, applause and followers create social aftermath, and the event produces a dated image of the performance.

Ouros lesson:

Audience response deserves its own observable record. It can affect future attendance, gossip or invitations, but it should not silently become a formal ranking, relationship score or PTU stat.

### PTU Coordinator reference

Source: Pokémon Tabletop United Wiki, Coordinator
https://pturpg.wikidot.com/coordinator

Reusable rule evidence:

Coordinator explicitly interacts with Pokémon Contests, Appeal Rolls and Contest-specific Features. The class also contains mechanics that can matter in battle.

Ouros lesson:

`SOCIAL_PERFORMER`, `EVENT_PARTICIPANT`, `PTU_COORDINATOR_CLASS` and `FORMAL_CONTEST_ENTRY` are separate facts. A resident can give a public demonstration without gaining Coordinator Features. Conversely, a real Coordinator's Contest mechanics cannot be replaced by narrative flavor.

### Community Grand Festival discussion

Source: r/PokemonTabletop, “Has Anyone ran a Grand Festival? What rules did you use? (PTU)”
https://www.reddit.com/r/PokemonTabletop/comments/184p8tq

Reusable community evidence:

The discussion shows that GMs want large contest events to feel materially different from routine competitions, while also reporting friction when normal Contest procedures become repetitive or tedious. Participants describe homebrew modifications precisely because the base handling does not automatically solve pacing at larger scale.

Ouros lesson:

Do not expand significance by multiplying rounds. Larger public events should gain identity through changing stakes, rivals, records, access, venue consequences and social context. Any mechanical modification remains proposal/homebrew until separately approved.

## Cross-source design lessons

### Preserve multiple kinds of outcome

A public event can produce all of the following without treating them as synonyms:

- formal placement;
- evaluator notes;
- audience response;
- completion status;
- safety/operational outcome;
- public record;
- later correction;
- future invitation or eligibility consequence.

### Published procedure should precede adjudication

For institutional competitions or demonstrations, participants should be able to know the format that governs them. A rule sheet, challenge contract, posted order or briefing can be a physical world object.

If two versions conflict, the system should preserve provenance and resolve which version governed the event rather than retroactively pretending the conflict never existed.

### Judging can be fallible

An evaluator can make an attributed judgment. That does not turn the opinion into world truth. Documentary mistakes can be corrected while preserving the original publication and revision history.

### Audience reaction is valuable but bounded

Applause, attendance, comments and repeat interest can create world texture. They should remain observations or aggregates with provenance. They must not automatically grant friendship, fame, rank, class Features or mechanical bonuses.

### Demonstrations can be noncompetitive

A repair demonstration, field-method presentation or Pokémon skill exhibition can have observers and evaluation without declaring a winner. This broadens public-life content without turning every gathering into a tournament.

### Persistent displays create environmental storytelling

Photos, plaques, posted results, corrected notices and rotating displays let earlier events remain visible. The authoritative record must stay separate from the Minecraft projection so a broken block or missing entity cannot rewrite history.

## Proposed invariant set

- `ENTRY_ACCEPTED != PERFORMANCE_COMPLETE`
- `PUBLIC_APPLAUSE != FORMAL_SCORE`
- `JUDGE_OPINION != CANON_TRUTH`
- `DISPLAYED_SKILL != PTU_FEATURE_GRANTED`
- `CONTEST_RESULT != BATTLE_RESULT`
- `BATTLE_WIN != EXHIBITION_WIN`
- `AUDIENCE_REACTION != RELATIONSHIP_CHANGE`
- `EVENT_COMPLETED != EVENT_SUCCESSFUL`
- `RECORD_PUBLISHED != RECORD_IMMUTABLE`
- `MINECRAFT_PARTICLE_EFFECT != PTU_CONTEST_EFFECT`
- `VISIBLE_MOVE_ANIMATION != VALID_APPEAL_RESOLUTION`
- `SHOWCASE_ENTRY != PTU_COORDINATOR_CLASS`
- `EVENT_RULES_POSTED != CAELO_RULES_PROVEN`

## Provenance policy

Public Pokémon material in this note supplies structural inspiration only. No protected dialogue, distinctive character arc or exact plot is imported.

Community material is treated as evidence of play practice and pain points, not rules authority.

PTU source material is authoritative only within the project's accepted source hierarchy and must be cross-checked against the exact project source/version before implementation.

No proposal in this pass becomes canon automatically.