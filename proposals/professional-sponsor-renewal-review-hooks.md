# Professional Sponsor Renewal Review Hooks

Status: implementation-facing proposal. Not established canon.

## Purpose

AutoPTU Career already records sponsor offers, the up-front payment, a visible season objective, the objective target, the completion bonus, the end-of-season result, and whether a completed sponsor receives a renewal opportunity next season. This proposal turns those authoritative facts into a compact professional review sequence without inventing hidden pressure or changing mechanical money.

The goal is to make sponsorship feel like a relationship with memory. A sponsor should visibly remember whether the trainer met the agreement, while the player keeps a clear distinction between payment already received, a conditional bonus, and a future renewal decision.

## Authority boundary

Presentation may use only Career facts already recorded by the simulator: sponsor name, theme, up-front amount, objective type, target, actual result, bonus paid, completion or failure status, renewal flag, trainer reputation, league, and season number.

Narrative presentation must not create extra money, remove money already paid, alter reputation, force equipment use, change battle preparation, or claim misconduct. A failed objective means only that the recorded target was not met unless another authoritative event says more.

## End-of-season review sequence

### Agreement recap

Show the sponsor name, the original objective, the target and the guaranteed payment that was accepted at signing. Keep the guaranteed payment visually separate from the conditional bonus.

### Verified result

Use the authoritative season result that settled the objective. For a wins objective, show actual wins beside the target. The panel should state completed or missed and show the exact bonus paid, including zero when the condition was not met.

### Renewal outlook

If the sponsor completed successfully and Career marks the next offer as a renewal, label it as a continuation of the previous agreement. If the sponsor failed and therefore does not return immediately, the UI can state that no immediate renewal offer is available. It should not claim punishment, hostility or blacklisting.

### Market context

When a new sponsor market opens, show whether an offer is a returning relationship or a new relationship. The player should be able to compare continuity against a different sponsor without needing to inspect raw timeline events.

## Deterministic review contract

The same Career state must always produce the same review facts and the same review category. Suggested categories are:

- completed with bonus;
- completed with zero bonus only if a future objective type permits that state;
- missed objective;
- sponsor declined;
- renewal offered;
- new sponsor relationship.

Presentation can vary phrasing by locale, but the category and numeric facts must remain stable across reloads.

## Original Ouros event seeds

### The clean renewal

The trainer meets the objective and the same company returns next season. The story is continuity rather than escalation. The sponsor review emphasizes that both parties already have a completed agreement on record.

### The missed target

The trainer finishes below the objective threshold. The review shows the exact shortfall and the absence of the conditional bonus. The next market moves on without implying scandal or personal conflict.

### The better fit

A successful trainer receives a renewal but chooses another sponsor. The public story can frame the change as a different professional fit. It must not claim the previous sponsor withdrew support because Career records that a renewal was available.

### The sponsor-free season

The trainer declines all offers. The season review records independence from a primary sponsor for that year. The presentation should avoid describing this as financial hardship unless another system establishes that fact.

### The long relationship

The same sponsor is completed and renewed across multiple seasons. A future biography surface can count consecutive completed agreements as public career history. That count remains descriptive until Career explicitly gives it mechanical consequences.

## UI opportunities

A sponsor review card fits naturally beside the season-completed summary. On desktop it can show agreement, result and renewal outlook in three compact sections. On mobile it should stack vertically while keeping payment, target and outcome visible without opening another screen.

Use clear monetary labels such as guaranteed, conditional and paid. A player should never need to infer whether a displayed bonus was actually awarded.

The next preseason sponsor market can add a small renewal badge to returning sponsors and a previous-result line such as the recorded target and result. New sponsors should not inherit history from another company.

## Timeline and biography use

The underlying `sponsor.signed`, `sponsor.completed`, `sponsor.failed` and `sponsor.declined` events remain the authoritative record. A season-summary review should reference those events rather than replace them.

A later career biography can safely derive facts such as number of completed sponsor objectives, number of missed objectives, sponsor-free seasons and longest verified renewal streak. These remain presentation facts unless a separate mechanical system explicitly consumes them.

## Acceptance rules for future implementation

- The season summary shows the sponsor objective result when a sponsor was signed.
- Guaranteed payment and conditional bonus remain visually distinct.
- A failed objective never removes the guaranteed payment retroactively.
- Renewal status comes from the generated next-season sponsor market, not from narrative inference.
- A missed objective does not generate accusations, fines or relationship damage without an authoritative event.
- Declining sponsorship remains a valid explicit state.
- Same state produces the same review facts after reload.
- Mobile layout keeps sponsor name, objective, result and paid bonus visible.
- No sponsor presentation changes battle transcripts, money or reputation.

## Why this belongs in Ouros

Professional careers feel deeper when institutions remember agreements and results. AutoPTU already owns the hard facts required for that memory. The useful narrative layer is therefore not a new sponsorship simulator. It is a clear public record of what was promised, what happened, what was paid and whether the relationship continues.