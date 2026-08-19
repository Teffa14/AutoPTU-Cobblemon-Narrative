# Language, translation & symbolic systems layer

Status: proposed systems design. Not canon.

## Purpose

Ouros needs to represent texts, inscriptions, symbols, translations, ciphers and interpretations without collapsing them into a single string of objective truth.

This layer connects archaeology, research, public memory, communications, dungeons and player knowledge while preserving uncertainty and provenance.

## Core separation

The system should keep these objects distinct:

- physical inscription or message
- encoded/transcribed representation
- segmentation and reading order
- proposed symbol values
- translation
- interpretation
- claim about history/world state
- actor knowledge of any of the above

A correct translation can still report a false belief. An incorrect translation can accidentally point toward a real fact. Neither should overwrite canonical truth automatically.

## Proposed data objects

### SYMBOLIC_SOURCE

Represents the physical or digital source.

Suggested fields:

```yaml
source_id: null
location_id: null
medium: inscription|tablet|book|mural|map|sign|recording|device|other
physical_state: intact|fragmentary|damaged|restored|copy
provenance_refs: []
script_system_id: null
known_reading_order: unknown
content_capture_refs: []
access_state: unknown
canon_status: proposed
```

### SCRIPT_SYSTEM

```yaml
script_system_id: null
name_status: unknown|provisional|canon
symbol_inventory_refs: []
directionality: unknown
segmentation_rules: unknown
numeric_system: unknown
logograms_present: unknown
historical_period_claims: []
known_regions: []
```

The script's existence may be canon while its age/origin remains disputed.

### TRANSCRIPTION

A transcription records what an actor believes is physically present before translation.

```yaml
transcription_id: null
source_id: null
author_id: null
created_at: null
symbol_sequence: []
uncertain_positions: []
method: visual_copy|rubbing|photo|scan|manual_other
confidence: null
```

This supports mistakes caused by damage, bad lighting or copied symbols without pretending those mistakes exist in the original source.

### DECIPHERMENT_MODEL

```yaml
model_id: null
script_system_id: null
author_ids: []
reading_order_hypothesis: null
symbol_mappings: []
segmentation_hypothesis: null
numeric_hypothesis: null
confidence: null
evidence_refs: []
contradictions: []
status: proposed|contested|superseded|accepted
```

### TRANSLATION

```yaml
translation_id: null
source_or_transcription_id: null
model_id: null
translator_ids: []
output_language_id: null
rendered_meaning: null
literal_or_interpretive: literal|interpretive|mixed
confidence: null
uncertain_segments: []
alternative_readings: []
created_at: null
```

### INTERPRETATION

Interpretation explains what an actor thinks the translated material means in context.

```yaml
interpretation_id: null
translation_refs: []
author_ids: []
claim_refs: []
confidence: null
assumptions: []
alternative_interpretations: []
```

## Knowledge boundaries

A player may know:

- that a tablet exists;
- that it uses an unfamiliar script;
- the complete transcription;
- only part of a symbol mapping;
- one scholar's translation;
- several conflicting interpretations.

These states must remain separate in multiplayer.

Public publication of a translation should flow through the existing media/communications system rather than grant universal knowledge.

## Translation confidence

Confidence should explain uncertainty, not function as a hidden truth meter.

Suggested components:

- source completeness
- transcription quality
- decipherment coverage
- independent parallels
- contextual consistency
- contradictory evidence

The engine should never expose a UI percentage that players can treat as omniscient proof unless that presentation is intentionally designed.

## Comparative decipherment

A powerful quest loop is comparison across sources.

Example structure:

1. Find an incomplete inscription at Site A.
2. Record repeated symbols but fail to determine their values.
3. Discover a bilingual or parallel phrase at Site B.
4. Update the decipherment model.
5. Revisit Site A.
6. A previously unreadable segment becomes interpretable.
7. The new meaning changes a hypothesis, not necessarily world truth.

This creates useful backtracking without arbitrary key items.

## Puzzle contract

Language/symbol puzzles should record three distinct challenge layers:

### Discovery
Can the player identify the relevant source, clue or repeated pattern?

### Interpretation
Can the player infer reading order, mapping, sequence or meaning?

### Manipulation
Can the player use that understanding to operate a mechanism, route or interface?

A puzzle can be difficult in one layer and easy in the others.

## Partial progress

Puzzles should support intermediate states such as:

- identified recurring glyph
- established reading direction
- decoded numerals
- translated proper noun
- translated action verb
- uncertain subject/object
- mechanism sequence partially known

Partial progress can unlock dialogue, research requests or safer experimentation before full solution.

## Recoverable failure

Default design should prevent experimentation from destroying the only route forward.

Possible recovery tools:

- mechanism reset
- alternate access route
- surviving copy of the clue
- expert reconstruction
- later return after more evidence
- partial bypass at increased cost

Irreversible loss is allowed only when it creates a meaningful branch rather than a dead campaign.

## Expert assistance

Experts should not be universal puzzle-solvers.

They may provide:

- better transcription quality
- a known symbol correspondence
- historical context
- an alternative reading
- identification of a false assumption
- access to comparison material

They should still be limited by evidence and their own knowledge.

## Language communities

If Ouros eventually defines multiple living languages or dialects, the system should track social and geographic usage separately from mechanical translation rules.

Possible state:

```yaml
language_id: null
regions_used: []
institutions_used: []
registers: []
script_ids: []
historical_relations: []
```

The generator must not invent languages merely to manufacture friction. Basic player communication remains accessible unless canon explicitly establishes otherwise.

## Oral transmission

Songs, sayings, mnemonics and oral histories can preserve structure even when exact wording changes.

Record:

- performer/source
- date/place
- motif links
- known variants
- whether it claims to be historical
- whether a written parallel exists

Oral tradition belongs with public-memory/myth systems and should not be treated as degraded text by default.

## Unown and Pokémon-shaped symbols

The official franchise deliberately preserves uncertainty around Unown and writing. Ouros should do the same unless its own canon establishes a relationship.

Allowed states include:

- symbols resemble an Unown form;
- an Unown appears near a symbol-bearing site;
- researchers debate whether the relationship is historical, biological or coincidental.

Forbidden inference:

- resemblance automatically proves Unown authored the text;
- presence automatically makes the script readable;
- collecting Unown automatically decodes a language.

Any actual PTU Unown Capability must be validated separately.

## Dungeon integration

A symbolic puzzle may alter:

- door state
- route state
- machinery state
- safe/unsafe path knowledge
- optional chamber access
- historical interpretation

It should not silently alter PTU battle rules.

If manipulation occurs during combat, use an encounter implementation contract and declare exact capability dependencies.

## Encounter contracts

### Archive Lockdown

Narrative premise: players discover a translation dispute while a secure archive is being evacuated. A mechanism uses a symbol sequence and the team must choose whether to trust one of two incomplete decipherments.

Full version dependencies:
- targeting/footprints/range/LoS: VERIFIED baseline
- base movement legality: VERIFIED baseline
- complete movement including interception/forced movement: BLOCKING if guards physically intercept routes
- core calculations: VERIFIED baseline
- action economy/initiative: VERIFIED baseline
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if archive hazards change during combat
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: decipherment and mechanism choice occur in the overworld before or after a static legal battle. No timed console objective, interception or changing hazards are simulated on the grid.

### Glyph Chamber Defense

Narrative premise: researchers need time to capture inscriptions while territorial wild Pokémon occupy the chamber.

Full version dependencies:
- basic targeting/movement/calculations/action economy: VERIFIED baseline
- lifecycle/damage/status/moves/abilities/items: PARTIAL as applicable to chosen legal combatants
- PROTECT_ZONE or timed scan objective: not yet authoritative; treat as BLOCKING under tactical AI/objective support
- terrain/hazards if the chamber changes state: BLOCKING
- Minecraft playback: BLOCKING

Reduced version: the scan happens before/after a standard encounter; success in combat determines whether the party has enough uninterrupted time to continue research, without inventing combat actions for the scanner.

### Cipher Gate Pursuit

Narrative premise: an antagonist group has only part of a cipher. Both sides race toward a gate that neither fully understands.

Full version dependencies:
- REACH_TILE/BREAK_THROUGH objective: BLOCKING under tactical AI/objective support
- complete movement/interception/forced movement: BLOCKING
- remaining baseline categories as above

Reduced version: travel/decipherment determines who reaches the site first. If a battle occurs, it is a conventional static encounter; the gate remains overworld state.

## Engine boundary

The language layer does not define PTU Skills or checks. Any use of General Education, Occult Education, Perception, Intuition, Pokémon Capabilities, supernatural Features or items must come from the governing PTU/Caelo rules and authoritative AutoPTU implementation.

Text interpretation may affect world knowledge and quest state even while all language mechanics remain outside battle resolution.

## Canon promotion checklist

Before a script/language fact enters canon:

1. Confirm the source object and provenance.
2. Separate what is physically observed from what is translated.
3. Record whether the translation is accepted, contested or provisional.
4. Do not promote an interpretation as historical truth without evidence.
5. Confirm any PTU mechanic involved.
6. Confirm whether the fact is public, private or institution-limited knowledge.
7. Confirm the puzzle remains solvable/recoverable under expected player behavior.