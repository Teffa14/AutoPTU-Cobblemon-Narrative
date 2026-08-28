# Ouros Narrative Research — Communications Network / Relay Service Continuity — Pass 105

Status: RESEARCH / PROVENANCE ONLY. This file establishes no Ouros canon and creates no PTU mechanics.
Date: 2026-08-28
Narrative baseline inspected before writing: `91b1774f26ae5841e4a04e4d67d9c40bfd8acbfb`.

## Repository gap check

The complete recursive `Teffa14/AutoPTU-Cobblemon-Narrative` tree was inspected before this pass and returned `truncated=false`.

Nearby ownership was reviewed before selecting this topic:

- `media-communications-information-layer.md` already owns information packets, publications, channels, coverage, message delivery and audience knowledge;
- `technology-energy-infrastructure-layer.md` already owns physical technical assets, communications backhaul as a network type, faults, maintenance, controls and redundancy;
- `infrastructure-outage-restoration-extension.md` already owns multi-service outage propagation, backup continuity and downstream restoration handoffs;
- `digital-systems-cyberspace-data-layer.md` already owns software, logical services, data, access and digital incidents.

The missing surface is narrower: persistent operational continuity of a communications network between its physical assets and the Media layer's delivery semantics. The useful objects are relay nodes, authored network links, service/coverage sectors, endpoint entitlement, reroutes, temporary relays, verification tests and restoration history. This pass does not create another message-delivery engine or another generic maintenance system.

## Public Pokémon source scan

### Goldenrod Radio Tower — production and technical operation are separable

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Goldenrod_City
- https://bulbapedia.bulbagarden.net/wiki/Goldenrod_City_Radio_Tower

Reusable structure:

Goldenrod Radio Tower contains studios, public-facing spaces, management space and a separate network of computers used for technical operations. Multiple programs can originate from one institution while sharing technical infrastructure.

Ouros transformation:

A communications institution can have several logical services whose editorial/content state is separate from network readiness. One program can stop while the carrier infrastructure remains usable. Conversely, an intact studio does not prove that transmission is reaching its intended area.

Excluded:

No Goldenrod characters, program names, takeover plot, floor layout, access items or broadcast schedules are copied into Ouros.

### Kanto/Lavender Radio Station — upstream restoration and endpoint entitlement are different gates

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Cion
- https://bulbapedia.bulbagarden.net/wiki/EXPN_Card
- https://bulbapedia.bulbagarden.net/wiki/Walkthrough%3APok%C3%A9mon_Crystal/Part_19

Reusable structure:

The Kanto station's normal operation is linked to restoration of the Power Plant, while a receiver may still need a separate expansion capability to tune particular broadcasts. Public access to the building is also restricted independently of whether the station broadcasts.

Ouros transformation:

Keep at least four facts separate:

1. upstream technical dependency available;
2. communications service transmitting;
3. signal/service available in a sector;
4. endpoint or actor authorized/equipped to receive that service.

Restoring power can release a communications dependency without automatically granting endpoint access, updating every receiver or proving every sector receives the service.

Excluded:

No Poké Flute effect, Snorlax interaction, EXPN Card item rule or Kanto security policy is generalized into Ouros.

### Pokémon Ranger: Guardian Signs — regional relay loss can persist after the initial incident

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Radio_Base
- https://pokemon.fandom.com/wiki/Wireless_Tower

Reusable structure:

The Wireless Tower supports long-range communication in Oblivia. Its antenna is disabled/destroyed during the story, preventing contact with the Ranger Union, and repair work continues as an ongoing objective rather than resolving automatically when the immediate confrontation ends.

Ouros transformation:

A communications node can be physically present yet unable to provide its authored role. An incident may produce separate phases: service loss, access secured, damage assessed, materials/tools obtained, repair performed, testing, limited restoration and normal service. The narrative can continue during those phases without requiring combat at every step.

The tower's game-specific exposed electricity and strong-wind traversal hazards are not imported as PTU battle mechanics.

### Radio interference — service disruption can be scoped rather than global

Source:
- https://bulbapedia.bulbagarden.net/wiki/Pokemusic

Reusable structure:

Pokémon games include a local radio transmission that interferes with ordinary tuning in a bounded area. The useful high-level lesson is scoped degradation: a network or receiver can behave differently by region/service without implying the entire world's communications are down.

Ouros transformation:

Interference is stored only as observed service degradation or a technical claim until a cause is verified. No jamming mechanics, combat Accuracy effect or electromagnetic Pokémon rule is inferred.

## Public operational design sources

### FEMA continuity guidance — fallback paths are ordered, maintained and tested

Source:
- https://www.fema.gov/sites/default/files/documents/fema_continuity-guidance-circular_082024.pdf

Reusable structure:

Continuity planning distinguishes primary, alternate, contingency and emergency communication methods and emphasizes maintaining access/interoperability among fallback systems.

Ouros transformation:

A communications service may hold an authored ordered fallback plan. The plan does not create guaranteed connectivity. Each fallback has its own dependencies, readiness state and verification evidence. A fallback being available does not mean every actor knows how or is authorized to use it.

No United States institutions, priority programs, frequencies, legal requirements or emergency standards are imported into Ouros canon.

### FCC outage/availability material — reported availability and observed service can disagree

Sources:
- https://www3.fcc.gov/
- https://help.bdc.fcc.gov/hc/en-us/ (public Broadband Data Collection availability material; localized pages may redirect)

Reusable structure:

Operational communications reporting distinguishes service disruption records and evidence about whether a service is actually available at a location. Reported availability can require correction when observations contradict it.

Ouros transformation:

A coverage/service map is a versioned claim with provenance. A field test can contradict it without silently rewriting history. Sector state can move through UNKNOWN, EXPECTED_AVAILABLE, DEGRADED, UNAVAILABLE, RESTORING and VERIFIED_AVAILABLE with timestamps and evidence.

No FCC thresholds, deadlines, reporting law, broadband definitions or regulated-service assumptions are adopted.

## PTU / Caelo cross-check

Existing project source evidence identifies these governing internal sources:

- `CoreRulebook.pdf`;
- `Caelo Player's Guide 1.5.pdf`;
- `Caelo Region Location & Encounter List.pdf`;
- `character creation merged.pdf`;
- `Erratas and extra merged.pdf`;
- `Pokedex / pokedex merged.pdf`.

The existing Narrative source scan records that Caelo supports persistent activity/location state and that some authored locations can carry explicit mechanical environmental effects. That is not evidence for a universal telecommunications subsystem.

Nothing inspected for this pass establishes universal PTU/Caelo rules for:

- radio range;
- signal strength arithmetic;
- tower coverage geometry;
- frequency allocation;
- interference/jamming actions;
- hacking or network intrusion;
- antenna repair DCs;
- electrical exposure damage from communications equipment;
- Pokémon species automatically acting as repeaters, generators or operators;
- Move/Ability-based long-range communication;
- communication-derived initiative, Accuracy or tactical bonuses.

Any future concept using telepathy, Aura, an Electric Move, Porygon/Rotom interaction, a Technology Education check, an Item or a Trainer Feature must cite the exact PTU/Caelo rule and current AutoPTU support.

## Reusable Ouros design lessons

A communications network becomes narratively useful when its history is preserved at several levels:

- physical node condition;
- authored link/topology state;
- logical service state;
- sector availability;
- endpoint readiness/entitlement;
- fallback route state;
- verification evidence;
- public information about the service.

These facts should be able to disagree temporarily without automatically implying sabotage or corruption.

Strong quest structures include:

- a repaired relay that still fails a downstream verification test;
- a sector that has service through a temporary relay while the permanent route remains offline;
- an endpoint that cannot receive a healthy service because its authorization/configuration is stale;
- two field reports that are both correct because they tested different sectors or services;
- an old relay site that remains a landmark after network topology changes;
- a restoration that returns emergency dispatch before ordinary public channels;
- a temporary communications path that changes which settlement becomes an information hub;
- a wildlife or access issue discovered around a relay site without assuming the Pokémon caused the outage.

## Research exclusions

This pass does not copy protected dialogue, named original characters, distinctive quest sequences, dungeon layouts or complete plots.

It does not treat fan/community material as PTU 1.05 rules authority.

It does not infer Ouros technology level, radio ownership, licensing, frequencies, satellites, mobile networks, public safety institutions or universal device access.

It does not give Minecraft redstone, blocks, chunk state, Cobblemon BattleState or nearby entities authority over communications truth or battle truth.
