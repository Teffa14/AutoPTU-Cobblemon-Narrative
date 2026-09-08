# Failed Handoff, No-Show & Replanning Research — Pass 344

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-07

Scope

This pass investigates what should happen when an already-authorized resource handoff is attempted but physical transfer does not occur. The target is the narrow seam after Pass 343 authorization and before custody transfer.

Repository duplicate guard

The full repository tree and existing shared-equipment owners were inspected first. Pass 69 already researches issue/return/overdue lifecycles and explicitly says that return is not the final verification step. Pass 343 already owns successful proxy pickup and append-only custody transfer. The remaining gap is failed physical attempt state and event-driven replanning.

Source 1 — Baylor HelpDesk+ loan policy

Source: https://helpdeskplus.web.baylor.edu/equipment-checkout-spaces/helpdesk-loan-policy

Observed structure

Reservations have explicit start/end times, may be cancelled for no-shows, and returns must be made to staff. Overdue equipment can suspend later borrowing until the equipment is returned and verified.

Reusable lesson

A scheduled entitlement can fail because the expected participant never appears. The failed appointment should remain a historical event instead of being silently treated as if the reservation never existed.

Transformation for Ouros

An authorized handoff may remain active after a non-terminal no-show until its authored window expires. The attempt becomes provenance for later replanning. No fine, suspension or institutional penalty is imported.

Source 2 — CSUSB Technology Lending

Source: https://www.csusb.edu/its/support/technology-support/its-technology-lending

Observed structure

Pickup location must match the reservation, early pickup is disallowed, and a missed pickup causes cancellation at the end of the allowed period rather than immediate physical transfer.

Reusable lesson

Place and time are part of fulfillment. Being eligible to receive a resource does not make an attempted pickup valid at another location or outside the allowed window.

Transformation for Ouros

Pass 344 validates handoff place and semantic time before recording an attempt. It does not create location-independent pickup or teleportation.

Source 3 — Elon University Media Services

Source: https://www.elon.edu/u/fa/technology/mediaservices/equipment-checkout/

Observed structure

A reservation can be cancelled after a missed pickup window, while renewals and delivery are separate policies. The equipment still physically remains at the checkout center unless a real checkout occurs.

Reusable lesson

Missed collection changes scheduling state but does not change custody.

Transformation for Ouros

`NO_SHOW != RESOURCE_TRANSFERRED`. A failed attempt does not mutate `WorldResource.holder_actor_id`.

Source 4 — official Pokémon Tabletop GM advice

Source: https://pokemontabletop.com/gm-advice-your-first-ptu-session/

Observed structure

Official PTU GM advice recommends simple early encounter situations and emphasizes explicit preparation around what a scenario actually requires. It also warns against overloading early encounters with mechanics that deny participation or add unnecessary complexity.

Reusable lesson

A mundane world-state complication can be a complete playable scene without forcing combat. When a richer encounter is added, its mechanics should be intentionally chosen and verified rather than assumed from narrative description.

Transformation for Ouros

A failed pickup can remain a noncombat scheduling/logistics incident. If a later field interruption becomes tactical, only the exact verified AutoPTU capability families may be used.

Cross-source structures

- appointment authorization and physical fulfillment are separate facts;
- the expected place and window matter;
- no-show can be recoverable while explicit refusal is terminal for the current authorization;
- failed fulfillment must not fabricate custody;
- the failure should wake only actors whose plans depend on it;
- institutional penalties are domain-specific and must not be invented globally.

PTU/Caelo boundary

Nothing in this research creates Skills, checks, Item effects, Features, communication Actions or social penalties. A mechanically active object remains individually gated by PTU/Caelo and current AutoPTU support.

Anti-copy rule

No university policy, fee schedule, identity system, disciplinary rule or exact operational wording is imported. The sources contribute only high-level state-machine structure.
