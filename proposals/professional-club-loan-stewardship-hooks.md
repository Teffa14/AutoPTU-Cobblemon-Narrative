# Professional Club Loan Stewardship Hooks

Status: implementation-facing proposal. Not established canon.

## Purpose

AutoPTU Career already models club-supplied Pokémon as temporary loans with stable identities, club ownership, contract expiry, active-roster eligibility, temporary training and explicit return events. This proposal defines original Ouros narrative hooks that can sit on top of that authoritative state without turning a loan into a capture or inventing battle outcomes.

The core idea is stewardship. A trainer can become attached to a club Pokémon and can build a public history with it, but possession remains temporary unless a later authored system explicitly records a legal transfer. Returning a Pokémon should therefore feel like a career consequence instead of a silent roster deletion.

## Authority boundary

The narrative layer may read these Career facts when present:

- club identity and signed contract;
- loan Pokémon id, species and supplying club;
- season acquired and contract expiry;
- active-roster membership;
- recorded matches, wins, training and career-health values;
- `club.offer_signed` and `club.loans_returned` timeline events;
- completed season result and trainer reputation.

The narrative layer must not infer ownership transfer, hidden loyalty, injury, misconduct, tactical mistakes or club promises from absence alone. A loan Pokémon remains a loan until authoritative Career state says otherwise.

## Career-facing beats

### Arrival

When a club loan enters the roster, present it as a registered squad assignment. The trainer should see who supplied the Pokémon, how long the assignment lasts and that training gains are attached to the temporary individual rather than to a future permanent capture.

Useful tone: professional opportunity with emotional potential. Avoid treating the Pokémon as disposable equipment.

### Selection pressure

A loan can compete for one of the active six slots. If it is left in PC storage, the game may acknowledge that the player chose continuity with owned Pokémon. If it becomes a regular starter, the game may acknowledge that the club assignment became central to the season.

This is presentation only. The narrative should use recorded lineup and appearance data instead of generating a hidden approval score.

### Development story

Training a loan should create a visible season story because the player invests resources in an asset that may leave. The UI can surface a compact note such as “Club assignment — development returns with the Pokémon when the deal ends.” This gives training a real strategic tradeoff without changing training mechanics.

If future systems add club evaluation, they should calculate it from explicit recorded facts such as appearances, wins, training events and career health. They should not derive it from free-form dialogue.

### Renewal

When the same club renews and the same loan identity is retained, the narrative can recognize continuity. The Pokémon is the same individual, so prior season appearances and training remain meaningful. This supports a recurring teammate arc without pretending that the trainer owns it.

A renewal message can mention that the club kept the assignment together because the contract state actually retained that Pokémon. Do not claim the club was “impressed” unless a future evaluation event records that reason.

### Return

`club.loans_returned` should create a visible career-history beat. The return screen should identify the supplied Pokémon and the club, then separate three facts:

- the Pokémon leaves the usable roster;
- its recorded history remains in the career timeline;
- no capture or permanent ownership event occurred.

If the returned Pokémon had substantial recorded usage, the presentation can frame the departure as the end of a working partnership. If usage was low, keep the copy neutral rather than inventing conflict.

## Original Ouros event seeds

These seeds are optional narrative wrappers around existing state. They do not add mechanics by themselves.

### The borrowed ace

A club supplies a Pokémon that immediately becomes one of the trainer’s most-used team members. Near contract expiry, media questions focus on whether the trainer can reproduce results without it. The dramatic pressure comes from known roster dependence, not from a scripted betrayal.

### The development project

A lower-level loan receives repeated training and meaningful appearances. At return, the club records the Pokémon as developed during the assignment. A future reunion can reference its prior identity and history if the same Pokémon id is deliberately restored by an authored system.

### The crowded six

A strong loan arrives when the trainer already has six established Pokémon. The player must decide who loses an active place. Dialogue can acknowledge selection pressure, but relationship changes should only occur if a separate social system records them.

### The renewal core

A multi-season club relationship retains one or more loan identities. The next season opens with continuity rather than a reset. This gives rival clubs and commentators a factual basis to talk about squad stability.

### The clean goodbye

The trainer changes clubs. All previous club loans are returned before the new club’s assignments enter the roster. The timeline can frame this as administrative closure and preserve the history of both squads without mixing ownership.

## UI opportunities

A loan badge should remain visible anywhere ownership could be ambiguous: roster, PC, training, lineup and season summary. The badge should include the supplying club when space permits.

The season summary can show a small “Club assignments” section with appearances, wins and training investment for each loan. Only show values already stored by Career.

Before signing a different club, the confirmation screen should list which current loan Pokémon will return. This makes the consequence explicit before the player commits.

When a loan is returned, avoid presenting it in capture history or permanent Pokédex ownership totals.

## Acceptance rules for future implementation

- A narrative hook never changes `ownership="loan"` to permanent ownership.
- A return removes the Pokémon from active play while preserving its historical references.
- Renewal continuity uses the same stable Pokémon identity when Career state retains it.
- Club-change confirmation exposes the exact loan identities that will leave.
- Training copy communicates temporary stewardship without altering training math.
- Any future club approval or transfer system must write explicit authoritative events before narrative claims use them.
- Same authoritative Career state produces the same factual loan summary; flavor wording may vary only within those facts.

## Why this belongs in Ouros

Professional training in Ouros should create relationships that are shaped by institutions as well as captures. Club loans add a distinct kind of attachment: the trainer can care for, develop and rely on a Pokémon without owning it. That tension creates career stories from state AutoPTU already records, while preserving the engine’s ownership and battle authority.
