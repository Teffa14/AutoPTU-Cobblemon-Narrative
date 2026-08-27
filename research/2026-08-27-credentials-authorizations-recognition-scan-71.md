# Credentials, Authorizations & Recognition Research — Pass 71

Status: research/provenance only. Nothing in this file is Ouros canon.

## Scope

This pass looked for reusable structures around identification, institutional credentials, temporary authorization, qualification records, access proofs, recognition between organizations, expiry/replacement and the difference between carrying a document and actually possessing authority.

Repository review before research found no dedicated credential/permit lifecycle. Related state already exists in:

- `design/interregional-mobility-recognition-layer.md` for temporary access and recognition between institutions;
- `design/battle-institutions-challenge-circuits-layer.md` for qualification nodes and formal challenge eligibility;
- `design/education-academies-field-practice-layer.md` for completion records, competency evidence and supervised practice;
- `design/workplaces-professions-staffing-layer.md` for roles and assignments;
- `design/service-access-queues-appointments-extension.md` for access requests and allocations;
- `design/shared-equipment-lending-issued-assets-extension.md` for issued physical assets;
- `design/public-notices-signage-world-information-extension.md` for public projections of underlying state.

The missing layer is a common lifecycle for the credential/authorization itself.

## Source 1 — Trainer Card / Trainer Passport / Frontier Pass

Source: Bulbapedia, “Trainer Card (game)”
https://bulbapedia.bulbagarden.net/wiki/Trainer_Card_(game)

Reusable structure:

- one persistent identity surface can aggregate several records;
- the same franchise function appears under different regional forms;
- a credential can display identity and achievement without itself creating those achievements;
- a later context can wrap or extend an earlier credential, as with the Frontier Pass carrying the normal Trainer Card.

Ouros transformation:

Use a `credential_instance` that references authoritative identity/qualification records. The visible card, badge, token, paper, device or registry entry is a projection. Destroying or replacing the physical representation does not erase the underlying qualification unless the issuing system says so.

Do not import exact fields, Trainer IDs, money display, Badge display rules or a universal Trainer Card into Ouros.

## Source 2 — League Cards in Galar

Source: Bulbapedia, “League Card”
https://bulbapedia.bulbagarden.net/wiki/League_Card

Reusable structure:

- a regional competitive institution can issue a recognizable public-facing credential;
- a card can contain both current identity data and historical/public achievement data;
- registration and later achievements can change what the credential communicates;
- exchange of cards can be social/public without granting access to private records.

Ouros transformation:

Separate `public_credential_projection` from private institutional records. A battle organization may publish a credential containing only approved fields. A public card cannot expose hidden roster, private medical state, secret research access or private relationship data.

Do not import Galar stars, uniform numbers, Gym Challenge progression, League-card customization or achievement thresholds.

## Source 3 — Trainer Card as identification

Source: Bulbapedia, Trainer card disambiguation
https://bulbapedia.bulbagarden.net/wiki/Trainer_card

The page explicitly characterizes the game Trainer Card as an identification card used by Pokémon Trainers.

Reusable structure:

Identity proof and activity qualification can coexist on one artifact but remain logically separable.

Ouros transformation:

A credential record should contain independently sourced identity claims and authorization claims. Matching a name does not prove the holder has every authorization associated with that person; verification still checks the current issuer record.

## Source 4 — Formal progression as registration plus qualification

Source: League Card documentation above.

The League Card changes after Gym Challenge registration and later milestones. This supports a lifecycle where registration, participation, qualification and public display are separate events.

Ouros transformation:

An actor can be:

- registered but not qualified;
- qualified but not currently authorized for a specific site;
- historically qualified but expired/inactive;
- authorized temporarily for one task;
- publicly recognizable while lacking current access;
- locally authorized while their record is not recognized elsewhere.

## Source 5 — Public PTU campaign structures

Source: StartPlaying, “Pokémon | PTU | Kanto Adventures”
https://startplaying.games/adventure/cmnmfkamd002vkz04j3wcn1vm

Source: StartPlaying, “The Taygon region Pokémon adventure ‘Team Flow’”
https://startplaying.games/adventure/cl8got8ov000y09l73ppe3mfd

These public PTU campaign pitches use cohorts, sponsored starters, formal journey starts and League-style progression as persistent campaign framing.

Reusable structure:

- entry into a long campaign can begin with an institutional intake event;
- sponsorship, registration and legal/approved participation can be distinct narrative facts;
- formal progression can coexist with open-world personal goals.

Ouros transformation:

Use intake and credential issuance as world-state events when an institution actually requires them. Never assume every Trainer needs a universal license merely because some campaigns use formal journey frameworks.

These sources are inspiration only. Their setting rules and house rules do not govern Ouros.

## Source 6 — PTU campaign diversity as a guardrail

Source: official Pokémon Tabletop blog, “A Fresh Start! And PTU 1.05 News”
https://pokemontabletop.com/a-fresh-start-and-ptu-1-05-news/

The official PTU project emphasizes a broad Trainer-class ecosystem and continued subsystem revision rather than one universal campaign structure.

Reusable lesson:

Do not make a credential layer synonymous with Gym progression. Researchers, field workers, performers, couriers, care staff, event workers and conservation teams may have institution-specific authorizations when canon supports them.

## High-level design lessons

1. A credential is evidence issued by an authority; it is not the authority itself.
2. Qualification, role, access and identity must remain separate state families.
3. Physical possession of a card/token does not prove current validity.
4. Lost/replaced physical credentials should preserve history and invalidate superseded representations when policy says so.
5. Recognition is receiver-specific. One institution can authenticate a record but decline to treat it as locally sufficient.
6. Temporary authorization should carry scope and time boundaries.
7. Suspension, expiration, revocation and replacement require provenance and cannot appear from narrative convenience.
8. Public display should expose only explicitly publishable fields.
9. Access checks should verify underlying current state rather than simply inspect a Minecraft item.
10. No universal Trainer license, passport, visa, professional license or permit may be inferred for Ouros.

## New narrative structures enabled

### Credential mismatch mystery

A person presents a genuine older credential whose issuer record shows it was superseded. The interesting question is not automatically fraud. Possible explanations include replacement, administrative delay, duplicate issuance, changed scope, loss followed by recovery or a stale local cache.

### Temporary field authorization

A research or conservation institution grants time-limited access to one site and one task. Returning later with the same physical token does not guarantee continued access.

### Cross-institution recognition dispute

A host institution confirms that a visitor’s completion record is authentic but requires local orientation before granting site access. Neither side needs to be corrupt or incompetent.

### Emergency scope extension

During a crisis, an institution may issue a temporary role or access scope. The extension ends after the crisis unless an authored policy explicitly converts it.

### Replacement history

A lost credential is replaced. The old one later appears in found property. It remains historically authentic but may no longer be an active access token.

## Mechanical boundary

Credentials are primarily world-state objects. They must not grant PTU Skills, Edges, Features, Moves, combat stages, accuracy bonuses, initiative changes, action economy, item permissions or other combat effects unless a governing PTU/Caelo rule and current engine implementation explicitly support that effect.

A battle qualification may point to an authoritative AutoPTU result. The credential stores the institutional consequence; it cannot rewrite the battle result.

## Canon questions left open

- Does Ouros have any universal Trainer identity document?
- Which institutions issue credentials at launch?
- Which authorizations expire or require renewal?
- Are credentials physical, digital, registry-only or mixed?
- What information is public versus private?
- Which organizations recognize each other’s records?
- Can emergency scopes be issued, and by whom?
- Are there replacement fees, deposits or penalties?
- Are any credentials transferable? Default assumption: no, unless canon explicitly says otherwise.
- Which access rules belong to conservation, science, battle institutions, education, workplaces or civic systems?

No answer is promoted to canon in this pass.
