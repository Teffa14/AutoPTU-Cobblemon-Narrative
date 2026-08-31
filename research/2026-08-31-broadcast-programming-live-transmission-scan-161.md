# Broadcast Programming, Live Transmission & Archive Research — Pass 161

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Date: 2026-08-31

## Research gap

The repository already has strong authority boundaries for information packets, publications, communication channels, network coverage, relay topology, audiovisual collection objects, public memory, performance productions and supporter communities.

Pass 19 already established that radio and television can be physical institutions, that programs may use different formats, that a reporter can gather an interview and later publish it, and that coverage/delivery are separate from truth. Communications Network continuity later added server-authored network nodes, service paths, sectors, temporary relays and verification tests. Performance continuity now owns staged works, production versions, casts, performances and reception. Archives owns preserved recordings and their custody/catalog state.

A remaining continuity gap sits between those systems: the persistent identity of a broadcast program and the concrete history of episodes, transmissions, live segments, scheduled slots, regional feeds, interruptions, rebroadcasts, presenter/crew tenures, production status and archived air copies.

This pass researches that gap. It does not create a universal technology level, ratings economy, broadcasting law, journalism mechanic, streaming platform or remote-combat mechanic.

## Source A — Jubilife TV and Sinnoh Now

Sources:
- Bulbapedia, Jubilife TV: https://bulbapedia.bulbagarden.net/wiki/Jubilife_TV
- Bulbapedia, Sinnoh Now: https://bulbapedia.bulbagarden.net/wiki/Sinnoh_Now
- Bulbapedia, TV programming in Sinnoh: https://bulbapedia.bulbagarden.net/wiki/TV_in_Sinnoh

Inspected: 2026-08-31.

Reusable high-level patterns:

- one broadcaster can maintain several recurring programs rather than one undifferentiated news feed;
- one program can contain different recurring segments;
- current events, local weather, Pokémon observations and player-related reports can coexist under the same broadcaster;
- specials and news flashes can coexist with regular programming;
- reporters encountered in the overworld can become part of later broadcasts;
- advertisements can occupy separate transmission space after a program.

Ouros lesson:

Model broadcaster, program, episode/edition, segment and transmission separately. A continuing show can survive a host change, a missed slot, a correction or a regional interruption. A concrete report inside one episode remains an attributable information packet governed by Media rather than becoming truth because it aired.

Originality boundary:

Do not reproduce Jubilife TV names, presenter identities, scripts, segment wording, advertisements or specific episode text. The reusable abstraction is program continuity and layered scheduling.

## Source B — televised Gym battles in Galar

Source:
- Official Pokémon Sword and Shield website, Gym Leaders: https://swordshield.pokemon.com/en-ca/people-galar-region/gym-leaders/

Inspected: 2026-08-31.

The official material states that spectators attend Gym stadium battles and that matches are broadcast on television.

Reusable lesson:

A battle and its broadcast are two linked events with different authorities. AutoPTU can resolve the battle. A broadcast system can then transmit or fail to transmit observations of that authoritative result. Camera loss, a regional feed interruption, commentary, replay editing or audience receipt cannot alter battle legality or outcome.

Ouros boundary:

`BATTLE_OCCURRED` and `BATTLE_TRANSMISSION_OCCURRED` need separate records. A spectator feed never supplies line of sight, targeting, initiative, combatant identity or tactical facts back into AutoPTU.

## Source C — Iono and livestream identity

Sources:
- Pokemon.com, Iono card feature: https://www.pokemon.com/us/news/a-look-at-pokemon-tcg-scarlet-violet-paldea-evolved-illustration-rare-cards
- Pokemon.com, “Dot and Nidothing”: https://www.pokemon.com/us/animation/horizons/2/dot-and-nidothing

Inspected: 2026-08-31.

Reusable high-level patterns:

- a public Trainer identity can include recurring online content independent of formal Gym duties;
- a battle can be rehearsed partly because a later event will be livestreamed;
- appearing on camera can create a social/character concern without changing the combat rules;
- a livestream has an audience-facing presentation layer around an underlying event.

Ouros lesson:

Broadcast participation can be a persistent social fact. Consent, identity, presenter role, rehearsal and public-facing framing can matter to story continuity while the tactical event remains under AutoPTU.

No Iono dialogue, visual identity, show format or plot is imported.

## Source D — real Pokémon competitive broadcasts

Sources:
- Pokemon.com, Grand Challenge Showcase broadcast: https://www.pokemon.com/uk/news/watch-the-grand-challenge-showcase-on-twitch-youtube-and-the-pokemon-broadcast-hub
- Pokémon Worlds 2024 virtual schedule: https://worlds.2024.pokemon.com/en-us/virtual/

Inspected: 2026-08-31.

Reusable patterns:

- one event can be distributed through multiple channels;
- a broadcast can have a declared time window and named hosts/commentators;
- commentators can discuss matches and strategy while the match itself remains governed by its competition rules;
- event scheduling and actual match duration can differ;
- a broadcast may contain additional discussion around the competitive event.

Ouros lesson:

A transmission should reference the authoritative event it covers rather than own that event. Distribution endpoints, hosts, pre/post segments and schedule state can vary without changing the underlying BattleSpec or result.

## Source E — recorded broadcast archives

Sources:
- Library of Congress, Audio-Visual Collections: https://wwws.loc.gov/avconservation/collections/
- Library of Congress, NBC Radio Broadcasts: https://guides.loc.gov/nbc/radio-collections/broadcasts
- Library of Congress, Public Broadcasting Web Archive: https://www.loc.gov/collections/public-broadcasting-web-archive/about-this-collection/

Inspected: 2026-08-31.

Reusable high-level patterns:

- broadcast programs can survive as recordings and related documents long after transmission;
- a preserved recording is a collection object with its own custody/access history;
- an institution can preserve program history, personnel information and recordings in multiple collections;
- recording practice may be incomplete across periods, so missing archive material does not prove a transmission never occurred.

Ouros lesson:

Separate transmission state from preservation state. `AIRED` does not imply `RECORDED`; `RECORDED` does not imply `ACCESSIBLE`; `ARCHIVED_COPY_EXISTS` does not imply it is the exact original air feed. Archives continues to own custody/catalog/condition of the recording object.

Real-world archival law, preservation standards, acquisition procedures and institutional policy are not imported.

## Source F — dynamic diegetic radio in Fallout 3

Source:
- Fallout Wiki, Galaxy News Radio / Three Dog pages, inspected for high-level design pattern only.

Inspected: 2026-08-31.

Reusable design pattern:

- a recurring radio identity can combine music, public-service material, serialized entertainment and news;
- presenter commentary can respond to player actions;
- most segments can be prerecorded while exceptional updates are framed as live;
- a station may continue to exist as a recognizable institution while individual content changes.

Ouros lesson:

A program can become a durable world object that reflects Chronicle state without becoming the Chronicle. Presenter commentary is an attributed interpretation. Recorded and live segments should have explicit provenance so the world can later know what was actually transmitted.

Copyright boundary:

Do not copy station names, hosts, scripts, quests, songs, setting details or story beats. This source contributes only the dynamic-radio structure.

## Source G — PTU actual-play publication continuity

Sources:
- Pokemon Rollout! public podcast listing / Tapestry Radio Network
- Pokemon World Tour: United public podcast listing

Inspected: 2026-08-31.

These are real PTU actual-play productions, not in-world rules authorities. Their usefulness here is structural: a long-running PTU narrative can be serialized into discrete published episodes, maintain a persistent production identity, include specials/intermissions, and continue across years.

Reusable lesson:

For Ouros, recurring in-world programs can similarly have episode identity, specials and hiatuses without forcing the campaign itself into episodic railroading. Publication cadence is world state only when authored for an in-world broadcaster.

No campaign plots, characters, dialogue or production branding are imported.

## Cross-check with existing Ouros authority

Media/Communications owns:

- information packets and claims;
- publication events;
- channel identity;
- delivery and audience receipt;
- editorial transforms;
- corrections and information revisions.

Communications Network owns:

- relay/network topology;
- service sectors;
- paths and reroutes;
- endpoint readiness;
- temporary relay operation;
- verification and restoration.

Performance continuity owns:

- staged works and production versions;
- ensembles, roles and rehearsals;
- actual artistic performance episodes;
- performance reception.

Archives owns:

- preserved recordings as collection objects;
- custody, catalog, condition, access and preservation history.

Public Memory owns later collective remembrance.

The new broadcast continuity layer should own only:

- persistent program identity;
- program format/version periods;
- presenters and broadcast-role tenure;
- scheduled slots;
- episode/edition production state;
- actual transmissions;
- live/recorded composition;
- regional/feed variants;
- interruption/override/resumption history;
- rebroadcast lineage;
- links to archived air/studio copies.

## PTU / Caelo source boundary

The project source scan identifies PTU Core, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List as mechanical authorities requiring exact validation.

Nothing inspected for this pass establishes a universal PTU/Caelo broadcast subsystem.

Remain UNKNOWN until exact project-source validation:

- a universal broadcasting Skill Check;
- camera or microphone equipment mechanics;
- remote Trainer command through television/radio/streaming;
- remote targeting or combat line of sight from camera feeds;
- a mass-audience morale, fame or reputation modifier;
- automatic Coordinator/Cheerleader effects from remote viewers;
- signal manipulation by Electric, Psychic or other Pokémon merely from Type/species flavor;
- Telepathy functioning as a broadcast channel beyond exact rules;
- jamming/interception rules;
- remote Contest judging;
- sponsorship or advertisement income formulas;
- a mechanic that treats a recording as authoritative evidence without provenance review.

## Design conclusions

1. Broadcast program identity needs continuity independent of channel and individual transmissions.
2. Schedule, production, transmission, receipt and archival survival need separate clocks.
3. Live status should be explicit; “live” does not mean unedited, universally received or mechanically authoritative.
4. Recorded segments can be combined into a transmission without pretending they occurred at airtime.
5. Regional feeds can diverge without creating contradictory world truth.
6. Corrections should link through Media rather than overwrite old air copies.
7. A rebroadcast points back to an earlier produced episode or segment; it is a new transmission event, not a new underlying event.
8. Missing archive material cannot prove a program never aired.
9. Presenter continuity and program continuity should be separate so shows can survive staff changes.
10. Broadcasts of AutoPTU battles are observers of authoritative tactical facts, never tactical authority.
11. Minecraft/Cobblemon may render studios, cameras, screens and live crowds only after Narrative establishes those facts.
12. Rich broadcast incidents should expose their exact engine dependencies and offer static reduced forms where possible.

## Canon status

All setting-specific examples that follow from this research remain PROPOSED until reviewed. No station, program, presenter, technology standard, media law, broadcast range or historical event is established as Ouros canon by Pass 161.