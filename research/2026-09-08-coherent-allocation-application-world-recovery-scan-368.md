# Coherent allocation-application world recovery scan — Pass 368

Status: RESEARCH / NON-CANON
Date: 2026-09-08

## Question

How should Ouros preserve the distinction between an institutional resource decision, its operational application, and later notification when a persistent world is saved and restored between those steps?

## Repository inspection

The repository was inspected before writing, including canon governance, CURRENT_FOCUS, the global NPC checkpoint chain, Passes 347–352, Pass 367 standalone V8 persistence, tests and CI paths.

Existing ownership remains:

Pass 347 owns historical conflict admission. Pass 348 owns allocation resolution and authority evidence. Pass 349 owns operational application. Pass 350 owns notice obligations. Pass 351 binds those obligations to actual communication recipients. Pass 352 archives terminal communication provenance. InformationEventQueue owns transport/delivery. Memory/belief owns private knowledge.

Pass 367 made Pass 349 durable in a standalone resource checkpoint but did not yet place it in the same global recovery instant as NPC state and communications.

## New public sources

### OpenInstrument shared-instrument workflow

Source: https://openinstrument.com/faq

Public documentation separates pending reservation approval, approval/rejection, cancellation, blackout periods and notifications. Admin cancellation produces a notification to the affected user, while calendar state and notification configuration remain distinct operational concerns.

Reusable structure for Ouros: a booking can change operationally before the affected person's knowledge catches up. Preserve the booking mutation and the notification path as separate facts. Do not infer delivery from the changed calendar.

No organization-specific policy, wording or software behavior is canonized.

### Pokémon Monomyth

Source: https://monomyth.jp/

The public project description emphasizes dangerous untamed exploration, sprawling environments, secrets and many sidequests alongside character-driven storytelling.

Reusable structure for Ouros: a logistical obligation can remain relevant while an expedition is physically far from the institution that created it. A resource decision made in town can become a field complication later because travel and side objectives continue while information propagates.

No region, characters, Pokémon variants, plot, mechanics or dialogue are imported.

### Pokémon Stalactite

Source: https://pokemon-stalactite.fr/

The public project describes an original semi-snowy region with mystery, regional adaptation, sidequests and environmental identity.

Reusable structure for Ouros: environmental conditions can justify scarce shared instruments and alternate observation windows. The narrative value comes from the changing field condition and human coordination around it, not from importing the project's region or plot.

No Citados lore, characters, antagonists, forms, story beats or dialogue are imported.

## Derived Ouros design lessons

1. Operational application must remain queryable independently from the decision that authorized it.
2. Application does not imply notification.
3. Notification does not imply delivery.
4. Delivery does not imply durable belief if later evidence changes the receiver's assessment.
5. A restart between any two of these stages must preserve the exact causal frontier.
6. Field travel can turn delayed knowledge into a playable consequence without requiring deception or incompetence.
7. Scarce scientific instruments work well as low-antagonism quest drivers because weather, habitat windows and competing legitimate projects naturally create pressure.

## PTU / Caelo cross-check

No new PTU rule, Move, Ability, Item, Trainer Feature, species fact or Caelo location is asserted by this research. PTU/Caelo source authority remains governed by the repository's existing source-priority files. The new encounter proposal therefore remains world-logic content and exposes any battle dependencies explicitly rather than treating narrative need as engine evidence.

## Provenance boundary

This file records public inspiration and transformed design lessons only. It is not Ouros canon. The associated proposal is also non-canon unless promoted through the repository's canon process.
