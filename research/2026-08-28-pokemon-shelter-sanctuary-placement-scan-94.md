# Pokémon Shelter, Sanctuary & Placement Research Scan — Pass 94

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is Ouros canon.

Date: 2026-08-28

## Why this pass exists

The repository already has strong neighboring systems:

- Care models treatment, welfare observations, rehabilitation and care-facility capacity.
- Pokémon Agency models durable individual identity, custody, residence, associations, transfer, rehoming and release.
- Conservation models wild-care transitions, release/relocation, habitat policy and post-release monitoring.
- Breeding/Nursery models Eggs, hatching, juvenile care, first-partner programs and lineage provenance.

The missing layer is operational continuity for a shelter or sanctuary program itself: intake, identity reconciliation, temporary residence, reunification, foster/temporary placement, rehoming, release, transfer to another facility, long-term sanctuary residence, capacity pressure, failed or reversed placements, and later callbacks.

This pass researches structures that can fill that gap without creating a second care system, a second ownership system, or a Pokémon vending interface.

## Source 1 — Lavender Volunteer Pokémon House

Source:
- Bulbapedia, Lavender Volunteer Pokémon House references in HeartGold/SoulSilver walkthrough: https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_HeartGold_and_SoulSilver/Part_19
- Bulbapedia, Mr. Fuji: https://bulbapedia.bulbagarden.net/wiki/Mr._Fuji

Observed structure:

The Volunteer Pokémon House is a community institution established to care for orphaned and abandoned Pokémon. Volunteers live at or use the same safe-house space while looking after resident Pokémon.

Reusable Ouros lessons:

1. Shelter care can be embedded in an ordinary neighborhood rather than isolated in a special dungeon or laboratory.
2. Resident Pokémon and human caretakers can share a persistent institution whose daily routine matters outside crisis scenes.
3. A facility can remain narratively important even when no placement or battle occurs; feeding, cleaning, visitor access, supply pressure and returning residents can all create continuity.
4. A shelter may know that a Pokémon was abandoned or orphaned while still having incomplete information about prior custody, ownership or exact history.

Not imported:

- Mr. Fuji, Lavender Town, Cubone, specific residents, Team Rocket events, Pokémon Tower plot or rewards.
- Any assumption that Ouros uses the same ownership law or volunteer model.

## Source 2 — Hidden Village

Source:
- Bulbapedia, Hidden Village: https://bulbapedia.bulbagarden.net/wiki/Hidden_Village

Observed structure:

The Hidden Village is run as a place for Pokémon abandoned by Trainers. The caretaker keeps them there until they are ready to return to the wild.

Reusable Ouros lessons:

1. Shelter residence can have an intended exit other than adoption or Trainer placement.
2. Rehabilitation and release can be different phases, with readiness reviewed before the transition.
3. Temporary human care does not require conversion of a wild or formerly trained Pokémon into a permanent collectible.
4. A release-oriented institution can create recurring content through follow-up sightings and post-release monitoring rather than deleting the individual from world state.

Not imported:

- Melanie, the specific village, Bulbasaur or the episode plot.
- Any universal claim that every abandoned Pokémon should be released.

## Source 3 — Pokémon Village, Kalos

Source:
- Bulbapedia, Pokémon Village: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Village

Observed structure:

Pokémon Village is a place where Pokémon live away from people for multiple reasons. Its value for this pass is the existence of refuge without a required human placement outcome.

Reusable Ouros lessons:

1. Long-term refuge can be a successful endpoint rather than a failed adoption case.
2. Some Pokémon may require or choose minimal-contact residence when canon/authored behavior supports that conclusion.
3. A sanctuary can be habitat-like rather than clinic-like, and its residents need not all be institutionally owned.
4. The system should support `LONG_TERM_SANCTUARY` or equivalent without applying a negative completion label.

Not imported:

- Kalos geography, specific species, Legendary associations or game progression.

## Source 4 — Aether Foundation / Aether House

Sources:
- Bulbapedia, Aether Foundation: https://bulbapedia.bulbagarden.net/wiki/Aether_Foundation
- Bulbapedia, Aether House: https://bulbapedia.bulbagarden.net/wiki/Aether_House

Observed structure:

Aether Paradise combines sanctuary and research functions, while Aether House has an orphanage purpose involving both people and Pokémon.

Reusable Ouros lessons:

1. One institution can legitimately hold several mandates, but the data model should keep those mandates explicit.
2. Sanctuary residence does not automatically authorize research, breeding, public display, battle training or transfer.
3. Mixed-purpose organizations create useful governance questions: who can access which records, who approves a transfer, which program owns a decision, and what happens when two mandates conflict.
4. Physical co-location should never collapse care, research and custody into one permission state.

Not imported:

- Aether Foundation characters, plot, technology, villainous actions, Ultra Beasts or Alola-specific institutional structure.

## Source 5 — PTU community discussion: rehabilitating Pokémon

Source:
- Reddit r/PokemonTabletop, “Rehabilitating Pokémon”: https://www.reddit.com/r/PokemonTabletop/comments/md80de

Observed structure:

The discussion identifies rescue and rehabilitation as rich roleplay material, especially for Pokémon coming from abandonment, abuse or hostile organizations. It also proposes custom mechanical penalties, altered movement and Ability replacement as possible representations.

Reusable Ouros lesson:

The narrative premise is useful; the proposed mechanical shortcut is not. Ouros can preserve observed behavior, care history, readiness reviews, repeated interactions and placement outcomes while leaving actual stats, Abilities, movement, statuses, Loyalty and Command effects to authoritative PTU/Caelo/AutoPTU state.

Anti-pattern recorded for Ouros:

Do not generate a hidden `trauma`, `abuse`, `rehabilitation_progress` or `trust` number and then modify combat statistics from it. Do not replace an Ability, reduce movement, add a status or change Command difficulty because narrative text says a Pokémon was rescued.

## Source 6 — PTU 1.05 Loyalty and Command

Sources:
- Pokémon Tabletop United 1.05 official release page: https://pokemontabletop.com/pokemon-tabletop-united-1-05-release/
- Public PTU 1.05 text mirror, Loyalty section around pages 209–211: https://anyflip.com/tcye/paot/basic/201-250
- PTU skill reference, Command: https://pturpg.wikidot.com/skills

Mechanical observations relevant to this pass:

PTU already has a Loyalty system. Low Loyalty can require Command checks in battle. The rules discuss mistreated or rescued Pokémon as examples that may affect the GM’s Loyalty determination, and the rules explicitly place changes in Loyalty under GM judgment. Command already covers ordering unruly or untamed Pokémon.

Ouros consequences:

1. Shelter history may provide provenance for events that a human GM or future authoritative subsystem could consider.
2. Narrative code must not assign or modify Loyalty ranks on its own.
3. Narrative code must not decide Command DCs or obedience.
4. A shelter resident’s willingness to approach, follow, accept handling, enter a carrier or interact with a prospective caretaker should be stored as observations unless an authoritative rule resolves something stronger.
5. A successful placement should not silently grant high Loyalty, commandability or battle readiness.

Caelo note:

No new Caelo-specific shelter, sanctuary, adoption or rehoming rule was located in the currently searchable project evidence during this pass. That absence is recorded as unresolved mechanical/canon scope, not permission to invent a replacement.

## Cross-source structures worth preserving

### Intake is an event, not a permanent label

The system should preserve how the Pokémon arrived, who supplied the information, what was directly observed, what belongings or identifiers were present, and which identity/custody claims remain unresolved.

“Abandoned” can be a supported fact, a report or an unresolved interpretation depending on evidence.

### Several exits can be legitimate

A case may end through:

- reunification with a prior legitimate caretaker;
- temporary foster/boarding;
- rehoming to another person or institution;
- release or relocation after appropriate review;
- transfer to a specialist facility;
- long-term sanctuary residence;
- continued open care when no safe transition exists yet.

No endpoint should be generated merely to clear capacity.

### Capacity pressure produces referrals, not automatic disposition

When a facility is full, valid consequences include waiting lists, temporary overflow space, transfer requests, volunteer/supply needs, delayed intake, emergency-only service, mobile support or negotiated assistance from another institution.

Capacity must never force an automatic release, capture transfer or player adoption.

### Matching needs evidence rather than a compatibility score

Prospective placement can consider authored requirements and observed interactions. The system should avoid a hidden universal match percentage. A trial may succeed, need adjustment, end early or remain unresolved without assigning emotions the game has not established.

### The Pokémon remains the same individual across the entire lifecycle

Intake, treatment, foster, return, release and later sighting should all point to the same persistent Pokémon entity whenever identity is known.

A transfer between facilities must not clone or regenerate the Pokémon.

## Useful narrative patterns for Ouros

### The intake mystery

A Pokémon arrives with incomplete or contradictory information. The playable problem is provenance reconstruction rather than combat.

### The placement that pauses

A trial placement begins successfully but a practical condition changes: housing, work schedule, transport, another resident, facility access, or the prospective caretaker’s capacity. The case returns to review without framing either party as morally at fault.

### Sanctuary as a destination

An individual with an established history can become a permanent resident whose routines, familiar caretakers and later callbacks make the sanctuary itself richer over time.

### Release with continuity

A release writes a durable event and can later generate sightings, monitoring, collective integration, seasonal absence or a return to the facility. Lack of later sightings remains absence of evidence, not proof of death or failure.

### Networked care

Different facilities can specialize. A local shelter may handle intake and ordinary residence, then refer medical care, juvenile care, rehabilitation, conservation release or disputed custody to the appropriate existing system.

## Originality and canon boundary

Everything derived here is structural inspiration only.

No source location, character, plot, species association, organization, law or technology is promoted to Ouros canon.

The proposed Ouros layer should remain compatible with future canon choices about:

- whether shelters and sanctuaries exist at all;
- who operates them;
- what legal categories exist for ownership, custody, guardianship or registration;
- what counts as abandonment;
- what privacy applies to prior-care histories;
- what release or rehoming approval requires;
- whether foster placement exists as a recognized practice;
- what records prospective caretakers may see.

## Implementation boundary

A shelter can create reasons for a battle without becoming a battle resolver.

Ouros owns intake, residence, custody references, placement workflow, facility capacity and encounter composition.

AutoPTU owns combatants once selected, legality, action economy, movement, HP, statuses, Moves, Abilities, Items, Features, AI legality and battle result.

Minecraft/Cobblemon can render facilities, enclosures, residents, caretakers, doors, gates, carriers, models, forms, poses, animations, cries, particles, UI, networking and synchronized state. Nearby shelter residents must never be inferred as combatants.

Binding direction:

`Ouros shelter/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

## Research outcome

The new design opportunity is not “an adoption center system.” It is persistent transition management around Pokémon who temporarily or permanently live under institutional care.

That distinction lets Ouros support rescue, rehabilitation, reunification, foster, rehoming, release and sanctuary life while preserving Pokémon identity, PTU mechanical authority and player consent.
