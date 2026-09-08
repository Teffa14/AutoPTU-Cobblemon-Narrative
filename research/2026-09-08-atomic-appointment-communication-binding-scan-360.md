# Atomic appointment / communication binding scan — Pass 360

Status: RESEARCH / PROVENANCE ONLY
Canon authority: NONE
Date: 2026-09-08

## Internal inspection before research

The recursive repository tree at narrative head `61e197e975a95ced7a72029c78048e3f7378d241` was inspected before writing. `CURRENT_FOCUS.md`, canon governance, Passes 339 and 342–359, the current world/resource checkpoint chain, communications provenance, appointment coordination, tests and workflow triggers were checked before selecting a new slice.

Existing research was searched for candidate source names before use. Previously processed sources including Pokemon Living World, Pokemon World Tour, The Reckless Rollers, Valoryn, Pokemon Terra Nova, Pokemon Lodestone, Pokemon Keishou, Pokemon Desolation, Pokemon Rainbow Wing, Radiant Heliodor and West Marches were not reused as primary sources.

## New public equipment-operations source — Barnard IMATS Equipment Room

Source: Barnard College IMATS, Equipment Room Policies.
URL: https://imats.barnard.edu/equipment-room
Accessed: 2026-09-08.

Observed high-level structure: the service sends separate confirmations for registration, reservation approval, equipment pickup and completed return. It also keeps pickup appointments distinct from the reservation itself and treats lateness/no-show as a separate operational condition.

Reusable Ouros abstraction: a resource request, an approved booking, a confirmation message, a physical handoff and a completed return are different facts. Persisting only the booking cannot prove that the correct participant received the message. Persisting only the later custody state cannot reconstruct which earlier communication was sent.

Not imported: Barnard-specific timing rules, account holds, staffing constraints, email addresses, institutional sanctions or equipment policy.

## New public appointment-message source — University College London Hospitals

Source: UCLH, SMS appointment reminder service.
URL: https://www.uclh.nhs.uk/patients-and-visitors/outpatients/sms-appointment-reminder-service
Accessed: 2026-09-08.

Observed high-level structure: a reminder contains appointment information and can support distinct responses for confirmation, rebooking or cancellation. Lack of reply does not itself cancel the appointment. Later reminders may have different response capabilities.

Reusable Ouros abstraction: authored notice kind, message delivery, recipient response and actual appointment state must stay separate. A confirmation addressed to the wrong actor cannot satisfy the intended coordination even if that communication event exists and was delivered successfully.

Not imported: medical context, response codes, exact reminder intervals, phone numbers, clinical consequences or patient policy.

## New living-world reference — Radiata Stories

Source: publicly accessible gameplay documentation for Radiata Stories.
URL: https://en.wikipedia.org/wiki/Radiata_Stories
Accessed: 2026-09-08.

This title had no exact repository match when checked before use.

Observed high-level structure: many NPCs have homes, jobs and day/night schedules; their presence and availability depend on the time and their routine rather than on the player's immediate need.

Reusable Ouros abstraction: appointment coordination becomes more useful when it binds into autonomous NPC schedules. A participant can be legitimately unavailable because another commitment still exists. The player may need to wait, reroute, contact someone else or gather evidence about what happened.

Not imported: Radiata characters, factions, combat, setting, dialogue, recruitment system or plot.

## New current PTU campaign reference — Putuland sandbox

Source: public StartPlaying listing, `Putuland - A Pokémon Sandbox [PTU][PTR 1e]`.
URL: https://startplaying.games/adventure/cmel0c8lm000dju04x52bfz7o
Accessed: 2026-09-08.

This campaign name had no repository match when checked before use.

Observed high-level structure: the campaign presents an original region as a sandbox whose mysteries and opportunities are not reduced to a single linear battle route.

Reusable Ouros lesson: logistical commitments and appointment failures can remain valid sandbox content while exploration, faction obligations and mysteries continue. A small missed pickup can become evidence in a larger pattern without forcing it into the main plot.

Not imported: Putuland region, mysteries, NPCs, factions, adventures, proprietary text or house rules.

## PTU / Caelo cross-check

The project source scan continues to identify PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List as governing sources for mechanical and setting claims.

Pass 360 does not add a PTU rule, Caelo location fact, Ability, Move, Item or Trainer Feature. It only strengthens persistence and provenance around an already existing world-agent appointment record. Public campaign and game references remain design inspiration only.

## Design synthesis

The durable causal chain should remain reconstructable as independent records:

request -> acceptance -> handoff authorization -> authored appointment notice -> concrete communication envelope -> delivery status -> receiver knowledge -> arrival/attempt -> physical custody transfer

Pass 359 persisted the authored notice. Pass 352 already made transport-envelope provenance queryable after delivery. Pass 360 can therefore validate the relationship between those two existing owners at coherent world restore without copying delivery state into the resource ledger.

Useful failure cases include a real notice linked to the wrong receiver, a real communication linked to the wrong sender, a resource notice pointing to a missing communication event, a claim mismatch between the authored record and transported envelope, or an older save that never persisted appointment history. All should remain distinguishable rather than being repaired through inference.

## Provenance boundary

Everything in this file is research or transformed design inference. It authorizes no Ouros institution, location, local penalty, named NPC, medical rule, equipment policy or canon event.
