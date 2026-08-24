# Professional Club Transition Media Hooks

Status: implementation-facing proposal. Not established canon.

## Purpose

AutoPTU Career now records club contracts, renewal versus transfer choices, trainer reputation, season results, sponsor outcomes, and exact club-loan returns. This proposal turns those existing facts into a compact transfer-window narrative layer without changing battle rules or inventing hidden motives.

The design goal is to make changing clubs feel like a public career event. The player should understand what the move means for continuity, reputation, borrowed Pokémon, sponsors, and future rivalries before the next schedule begins.

## Authority boundary

Presentation may use only recorded Career facts: current and previous club, league, salary, contract length, renewal flag, returned loan identities, completed-season record, trainer reputation, sponsor outcome, and relationship entries that already exist.

Presentation must not infer that a club fired the trainer, that a Pokémon resents the move, that a sponsor caused the transfer, or that a rival is angry unless an authoritative event explicitly records that fact.

## Transfer-window sequence

### Departure desk

When a trainer leaves a club, show a short factual closure card before the new club introduction. It should name the previous club, the completed-season record when available, and the loan Pokémon returned by the move. Permanent Pokémon remain visually separated from club assignments.

If no loan Pokémon leave, omit the loan section instead of generating generic farewell text.

### Signing room

The new-club card should show salary, contract duration, club perk, incoming loans, signing gift, and the trainer reputation value used by the market. This makes the transfer legible as a professional decision rather than a cosmetic rename.

### Press questions

Generate two or three deterministic questions from the facts of the move. These are presentation prompts, not mechanical decisions unless a later system explicitly gives them consequences.

Useful factual question families:

- continuity: asked when the trainer renewed with the same club;
- rebuild: asked when multiple club loans left during a transfer;
- step up: asked when the league changed upward;
- recovery: asked after a losing season;
- momentum: asked after a winning season or title;
- sponsor continuity: asked when the latest sponsor was completed and renewed;
- independence: asked when the trainer declined sponsorship.

The answer choices can establish tone for the player-facing biography, but they must not silently change reputation, relationships, salary, battle preparation, or Pokémon state.

## Original Ouros event seeds

### The clean handover

A trainer changes clubs after a stable season. The old club formally receives its loan Pokémon, the new club registers its assignments, and the public story is about adapting to a different institution rather than personal conflict.

### The borrowed core leaves

Several returned loans had been active members of the six. The next preseason opens with a visible roster-continuity problem. Commentary may say that important registered players left because the lineup data proves they were active; it must not claim emotional fallout.

### The quiet renewal

The trainer stays with the same club. The story emphasizes continuity: same institution, retained eligible loans, and a longer planning horizon. This is useful contrast against transfers and makes renewal feel like an authored career path.

### The reputation move

A high-reputation trainer receives a stronger salary market. The signing presentation can explicitly connect the displayed market value to recorded reputation because salary generation already reads that value. It must not claim a specific negotiation occurred unless Career records one.

### The difficult reset

A transfer follows a poor season. The press layer can reference the actual record and ask how the trainer intends to rebuild. The game must avoid language such as “fired,” “forced out,” or “lost the dressing room” unless future authoritative events support those claims.

## Deterministic presentation contract

Given the same Career state, the same factual question families should be selected in the same order. Flavor wording may vary only inside the facts available to the renderer. This keeps save/reload behavior stable and makes regression testing practical.

A suggested priority order is: loan departures, league movement, title or winning record, losing record, sponsor continuity, renewal, neutral transfer.

## UI opportunities

A compact transition panel can sit between club selection and the normal preseason dashboard. It should have three columns on desktop and stack on mobile: previous chapter, roster consequences, new contract.

Returned loans should use the same loan badge used in roster and PC surfaces. Incoming assignments should display supplying club and expiry season. Permanent captures should never appear inside the returned-loan group.

The career timeline should preserve a concise transfer entry that links the old club closure and new signing without deleting the underlying `club.loans_returned` and `club.offer_signed` events.

## Acceptance rules for future implementation

- Transfer presentation reads authoritative Career state and never changes battle mechanics.
- A renewal never presents retained loans as returned.
- A transfer lists the exact returned loan identities already recorded by Career.
- Permanent Pokémon never appear as club property.
- Questions never imply dismissal, injury, loyalty, misconduct, or tactical failure without an explicit event.
- Same state selects the same factual question families.
- Mobile presentation remains readable without hiding loan ownership or contract consequences.
- Reloading the page does not create duplicate transition events.

## Why this belongs in Ouros

A professional trainer career becomes more convincing when institutions remember movement between clubs. The useful drama comes from facts the simulation already owns: a contract ended, a roster changed, a season succeeded or failed, a sponsor stayed or left, and a new institution accepted the trainer. Those facts are enough to create a public career story without replacing AutoPTU as the mechanical authority.