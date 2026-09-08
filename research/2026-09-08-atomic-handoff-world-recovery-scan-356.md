# Atomic handoff world recovery scan — Pass 356

Status: RESEARCH / NON-CANON
Date: 2026-09-08

## Research question

What reusable public design patterns support preserving a completed handoff and its surrounding world state across a save/restart without re-executing the transfer or inventing missing history?

Before external research, the repository tree and prior research were inspected. Pokémon Reborn, Pokémon Insurgence, Pokémon World Tour: United, The Reckless Rollers, Pokémon Adventures in the Millennium, West Marches, event sourcing and several institutional custody policies have already been processed repeatedly. This pass therefore uses a narrower set of sources not previously used for this exact seam.

## Source 1 — SPUD persistent-world save/load library

Source: https://github.com/sinbad/SPUD

SPUD documents a persistence model where selected actors and properties survive save/load and streamed-level unload/reload, including dynamically spawned and destroyed objects.

Reusable structure for Ouros:

- persistence should restore durable state instead of rerunning the action that originally produced it;
- state belonging to different streamed or unloaded parts of the world can still belong to one coherent save;
- object identity and state survive absence from the currently loaded presentation layer.

Ouros adaptation:

A custody transfer that already happened is historical state. Restoring the world should reconstruct its ledger record alongside NPC/world state. It should not execute the transfer again. Minecraft entity presence remains presentation and does not define historical ownership provenance.

No SPUD implementation code or Unreal-specific architecture is imported.

## Source 2 — Pokémon Uranium, Ripley's Sidequest

Source: https://pokemon-uranium.fandom.com/wiki/Ripley%27s_Sidequest

The public sidequest documentation notes that an earlier version could crash when saving during the sidequest and that the problem was later fixed. The quest itself also contains a temporary constrained exploration state before a later encounter.

Reusable structure for Ouros:

- side activities can create temporary but meaningful world state that must survive save/load safely;
- save boundaries should not assume the player only saves between narrative beats;
- a quest can remain optional and returnable while still requiring coherent persistence when active.

Ouros adaptation:

A resource pickup or courier obligation can cross session/restart boundaries. The checkpoint must be valid at intermediate states such as "authorized but not transferred" and "transferred but not delivered to final destination."

No characters, plot, dialogue, Pokémon roster or puzzle layout are imported.

## Source 3 — current public PTU campaign continuity

Source: https://startplaying.games/adventure/cml40sutr00dpl2046cr10ins

A currently listed Pokémon Tabletop United campaign, Radiant Heliodor, publicly advertises an ongoing weekly structure and was already scheduling sessions in the twenties when inspected on 2026-09-08.

Reusable structure for Ouros:

Long-running PTU play naturally spans many sessions. Persistent obligations, equipment custody and off-screen commitments therefore need to survive session boundaries without relying on GM memory or repeated exposition.

This source is used only as evidence for campaign continuity. No setting, characters, contest premise or paid-session material is imported.

## PTU / Caelo cross-check

The project source inventory continues to treat PTU Core, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and the Caelo Region Location & Encounter List as governing internal references.

Pass 356 introduces no new PTU mechanic and no Caelo lore claim. It persists world-state provenance only.

Any later tactical courier encounter must still use existing PTU/Caelo rules and the permanent engine capability gates. Persistence cannot be used to invent tactical pickup, interception, reactions, weather effects or Trainer Feature interrupts.

## Reusable Ouros lessons

A completed physical event should survive restart as history, not as a command waiting to run again.

A future authorization and a completed transfer are different persistence classes. The first can point into the future. The second cannot exist later than the checkpoint time.

Older saves must preserve uncertainty when a subsystem was not serialized. Current possession cannot be used as proof of how custody changed.

Intermediate quest/logistics states deserve save safety. A restart may occur while an obligation is still in progress.

World-state durability is useful narrative infrastructure because later disputes, investigations and consequences can depend on what was provably true at a prior moment.

## Canon status

No new Ouros canon is proposed by this research note. The associated scenario remains explicitly proposed and non-canon.
