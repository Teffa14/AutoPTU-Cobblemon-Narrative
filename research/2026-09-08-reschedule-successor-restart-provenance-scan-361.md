# Reschedule successor restart provenance scan — Pass 361

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-08

Purpose

Inspect the existing Ouros resource, appointment, communication and Pass 346 reschedule contracts before adding new narrative material. The narrow question is how a replaced handoff window can survive a restart while preserving both the superseded authorization and the successor that replaced it.

Repository boundary inspected before writing

The recursive repository inventory, canon governance, current resource/checkpoint sequence, Pass 345 appointment ownership, Pass 346 reschedule proposal/decision/replacement contract, Passes 347–352 downstream allocation work, Pass 359 appointment checkpoint, Pass 360 world/communication binding and current readiness snapshot were checked first. No canon file is modified by this pass.

Existing Ouros facts relevant to this scan

Pass 345 owns authored appointment notices. Communications owns whether the associated envelope was actually delivered. Pass 346 requires a delivered RESCHEDULE_REQUEST before the named responder can decide. Acceptance creates a distinct successor authorization and preserves the old authorization as superseded history. A physical handoff using the stale authorization must be rejected by the operational wrapper.

The remaining durability seam is therefore historical identity. A restart must not collapse the old and new windows into one record, infer that the new window was always the original arrangement, or lose the acceptance that explains why the successor exists.

New public sources

1. IETF RFC 5546, iCalendar Transport-Independent Interoperability Protocol (iTIP), section 3.2.2.1, Rescheduling an Event.
https://datatracker.ietf.org/doc/rfc5546/
Accessed 2026-09-08.

Reusable design lesson: rescheduling is represented as a later version of an already identifiable event rather than an unrelated replacement with no lineage. The earlier event identity and the newer sequence/version allow a consumer to distinguish reschedule from ordinary reconfirmation. Ouros should preserve equivalent lineage between old authorization, accepted proposal and successor authorization. No calendaring protocol is imported into canon or gameplay rules.

2. Uppsala University thesis, Majora's Mask Thesis, section discussing NPC schedules.
https://uu.diva-portal.org/smash/get/diva2:1664516/FULLTEXT01.pdf
Accessed 2026-09-08.

Reusable design lesson: NPC routines can be mechanically bound to world time while player intervention changes selected outcomes. Scheduled events continue to occur whether the player is present or absent. Ouros can use the same high-level principle without copying any Zelda characters, plots or dialogue: a provider, courier, researcher or ranger can continue following a revised appointment while another actor still acts on stale information.

3. StartPlaying public campaign listing, Roarin' Unova | The first Pokémon League challenge, circa 1920.
https://startplaying.games/adventure/cmtady2ew00kvl40402n96aaj
Accessed 2026-09-08.

This is a contemporary public Pokémon Tabletop United campaign listing. It describes a custom regional interpretation combining battle, lore, social play and mysteries in an ongoing campaign format. Reusable lesson: PTU play can support investigation and setting continuity alongside combat. The listing is research provenance only. Its version of Unova, characters, factions and campaign premise are not imported into Ouros.

4. AutoPTU-Java PR #408, read-only engine evidence.
https://github.com/Teffa14/AutoPTU-Java/pull/408
Inspected 2026-09-08.

The PR freezes differential parity for Intimidate interacting with Mirror Armor. The fixture compares both combatants' final Attack stages, the once-per-round Intimidate marker, and ordered reflection/combat-stage/Intimidate semantic events through the real Java pipelines. The PR explicitly adds no Minecraft/Cobblemon/Craftics rule logic.

Transformed Ouros structures

A rescheduled obligation should retain a lineage chain: original authorization -> delivered reschedule request -> proposal -> responder decision -> successor authorization. The successor can change location and time without rewriting what the parties were previously authorized to do.

Different NPCs can legitimately hold different schedule versions. One participant may know the successor window, another may retain the old one, and a third may only know that a reschedule request was sent. That disagreement can generate investigation, missed rendezvous, rerouting, social repair or resource-allocation pressure without requiring deception.

A restart should recover historical records, not replay the decision or reissue the authorization. The successor must already exist in the handoff ledger and must exactly match the accepted proposal. If the records disagree, restore should fail closed rather than silently choose one version.

Canon boundary

No source above establishes a Caelo fact. No PTU mechanic is inferred from a campaign listing. The new persistence codec is architectural support for already established Pass 346 behavior. Any location, faction, institution or NPC introduced in the companion proposal remains PROPOSED / NON-CANON until promoted through the repository's normal canon process.

Encounter dependency note

The reduced narrative version requires no AutoPTU battle implementation. A richer field interception remains separately gated by targeting/footprints/range/LoS, base movement legality, complete movement including interception/forced movement, action economy/initiative, full turn/round lifecycle, any exact terrain/weather/hazard/reaction mechanics used, AI legal-action infrastructure, AI tactical policy and Minecraft/Cobblemon/Craftics adapter/playback support. No representative Ability parity is treated as category-wide coverage.
