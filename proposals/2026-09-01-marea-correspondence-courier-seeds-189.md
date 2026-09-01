# Marea Correspondence and Courier Seeds — Pass 189

Status: PROPOSED. NOT CANON.
Date: 2026-09-01

These seeds apply `design/correspondence-courier-message-continuity-layer.md` to existing Marea people and institutions. They do not create a postal service, courier guild, privacy code, literacy norm, regional communication technology or Caelo-wide delivery law.

## Tideglass Packet During Taro's Absence

A sealed packet reaches Tideglass while Taro is away from his normal review work.

Pia can receive the packet, record time and custody, and place it in the correct holding location if that action fits her established role. Receipt does not transfer Taro's interpretive or review authority.

The player can see three facts stay separate: delivery succeeded, custody is safe, substantive review is still pending.

Recommended first implementation slice. No BattleSpec dependency.

## The Notice That Outlived Its Revision

An older public instruction remains physically posted after the owning institution issued a revised version.

Residents who saw the old copy may have acted reasonably from stale information. The player can help identify which visible copies need replacement without rewriting the historical fact that the old notice was once valid.

Strong Minecraft persistence test: replacing a board projection does not create or alter institutional authority.

## Arrived After the Problem Ended

A practical request was issued and sent correctly. Before the message reaches its destination, another resident resolves the underlying problem through ordinary autonomous activity.

The delayed message still arrives and is logged. The recipient can acknowledge that no further action is required.

Purpose: prove that correspondence records history rather than freezing the world until the player delivers a quest item.

## Returned, Recipient Unavailable

An addressed message cannot be delivered at the expected location and returns to origin.

The correct next state is delivery failure or recipient unavailable. The system must not open a missing-person case unless separate evidence justifies that escalation.

This seed connects safely to the field-search layer without collapsing the two systems.

## Mirador Instruction Received by Ema

A written field instruction or request reaches Mirador while Nerea is occupied elsewhere.

Ema can accept the document and perform only actions already within her authority. If formal review or scientific approval belongs to Nerea, that state remains pending.

No generic Research roll, authority inheritance or Trainer Feature is created.

## Public Cargo Sheet, Private Note

A packet moving through Ferry Landing contains an ordinary public or operational cargo sheet plus a separately addressed private note.

The two records share transport but have different visibility scopes. Lia can coordinate the physical handoff without the system granting every nearby NPC knowledge of the private contents.

This tests mixed visibility inside one container.

## Two Copies, One Missing Line

Tideglass receives two copies of what appears to be the same earlier message. One transcription omits a line or date marker.

Taro and Pia can compare provenance, source marks and archive context. The goal is to establish which wording is better supported, not to treat the cleaner-looking copy as automatically authoritative.

Possible outcome: uncertainty remains documented if neither copy can be proven primary.

## The Reply Crossed the Courier

A reply is issued while the original courier is already returning by another route.

The two messages cross in transit. For a short period, sender and recipient each have incomplete knowledge of the other's latest position.

This creates believable asynchronous world state with no deception.

## Brin Holds the Packet, Not the Decision

A packet is temporarily stored with other protected goods because its intended office is closed or inaccessible.

Brin can hold custody when the authored episode supports that handoff. Storage does not grant permission to open, interpret, approve or dispose of the correspondence.

Useful connection to provisioning and custody systems.

## Wrong Desk, Correct Institution

A legitimate message reaches the correct institution but is initially placed at the wrong work surface or role queue.

The mistake should create a routing correction, not an invented disciplinary crisis. The timestamp of institutional receipt remains different from the later timestamp when the responsible reviewer actually reads it.

This is a practical test of role-based recipients.

## The Superseding Route Note

A route instruction is issued, then conditions change and a second valid message supersedes it.

One physical copy of the old instruction remains in circulation. The player may encounter a resident who has only that earlier information.

The episode can resolve by updating knowledge and copies. No character is automatically blamed for following the latest instruction they legitimately possessed.

This seed should reuse established closure/access authority rather than inventing a new route office.

## A Pokémon Brings Back the Satchel

A companion or local Pokémon appears with a message satchel or dropped packet associated with an existing delivery attempt.

Initial authoritative facts are limited to observable possession, location and the packet's persistent identity. The system does not infer that the Pokémon stole it, rescued it, understood the addressee or intentionally completed delivery.

Any Move, Ability, Capability or Trainer Feature needed for a more specific behavior must be audited before implementation.

## Letters That Outlive Their Errands

Longer-term arc concept.

Over several seasons, small correspondence chains accumulate around Marea. Some requests arrive on time. Others are superseded, returned, corrected, answered after the fact or preserved at Tideglass because later residents need to understand what people knew at the time.

Persistent traces can include dated packets, retired notice copies, receipt marks, reply references, corrected transcriptions and archived threads.

The arc makes institutional memory visible without creating a conspiracy, centralized bureaucracy or universal quest board.

## Mechanically rich candidate: Courier at the Glass Bend

A legitimate packet is being carried between existing institutions when wild activity makes part of the route unsafe.

The intended full version can involve corridor geometry, movement pressure, interception, displacement, environmental conditions and tactical protection. It therefore requires the permanent capability families listed in `design/correspondence-courier-message-continuity-layer.md`: targeting/footprints/range/LoS; base movement legality; complete movement including push/pull/knockback/interception/forced movement; core calculations; action economy/initiative; full turn/round lifecycle; full stateful damage pipeline; status lifecycle for chosen content; terrain/weather/hazards/zones/reactions when active; move-specific behavior; abilities; items; Trainer Features/perks when active; AI legal-action infrastructure; AI tactical policy; and Minecraft/Cobblemon/Craftics adapter/playback support.

Current full-version classification: BLOCKED.

The reduced version keeps the courier and packet outside BattleSpec, places the resident at an authored safe position, and runs only a separate audited battle if an immediate wild threat still blocks passage. AutoPTU may return `IMMEDIATE_ROUTE_THREAT_WITHDREW` or `IMMEDIATE_PASSAGE_CLEAR`. Narrative then decides whether delivery continues, custody transfers or delay is recorded.

Battle outcome cannot authenticate the packet, make an old instruction current, establish delivery, prove reading, accept the requested work or close the correspondence thread.

## Canon boundaries

These proposals do not canonize:

- a Marea postal institution;
- dedicated couriers;
- postage or mailboxes;
- a standard seal system;
- communication technology;
- literacy assumptions;
- privacy law;
- mandatory response times;
- a specific route used for every message;
- messenger Pokémon as a species role;
- new authority for Pia, Ema, Lia, Brin or any other resident;
- a Caelo correspondence system.

Every seed remains a candidate until explicitly promoted through the project's canon process.