# Media, Communications & Information Flow Research — Pass 19

Status: research and provenance only. Nothing in this file is Ouros canon.

## Research gap

The repository already models canonical facts, witness reports, public memory, rumors, actor knowledge, cases, crisis forecasts, institutions and world-state changes. What it did not yet model was the infrastructure between those things: how information is published, transmitted, delayed, corrected, localized, interrupted or privately delivered.

This pass therefore studies communications as a world system rather than treating every known fact as instantly available to every player and NPC.

## Source 1 — New Valkenburg PTU campaign

Source: ElementalKnight, New Valkenburg campaign material.
URL: https://sites.google.com/site/ekautomuse/campaigns/new-valkenburg
Inspected: 2026-08-18.

Relevant high-level patterns:

- The setting explicitly includes local press, television and radio institutions.
- The New Valkenburg Daily Hyper Voice functions as a newspaper of record.
- Its daily headline tracks the campaign's in-game date, events and weather.
- The campaign treats media organizations as part of city geography rather than as abstract UI only.
- Player actions can therefore become part of an evolving public information environment.

Reusable lesson for Ouros:

A persistent-world campaign can use news as a digest of world state. The important design move is not the newspaper's name or exact content. It is the link between current simulation state and a diegetic information channel.

Copyright boundary: do not reuse New Valkenburg names, institutions, demographic setting, prose, NPCs or specific plots.

## Source 2 — Pokémon radio and regional broadcast infrastructure

Sources:
- Bulbapedia, Radio / Pokégear material: https://bulbapedia.bulbagarden.net/wiki/Radio
- Bulbapedia, Goldenrod City / Radio Tower: https://bulbapedia.bulbagarden.net/wiki/Goldenrod_City
- Bulbapedia, Kanto Radio Station / Pokémon Tower: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Tower

Relevant patterns:

- Johto has radio programming delivered through the Pokégear.
- Broadcast availability is regional and depends on infrastructure/access.
- Kanto radio access can depend on restored infrastructure and an expansion card.
- Broadcast towers are physical institutions with studios, staff, restricted areas and technical systems.

Reusable lesson for Ouros:

Communication should have coverage and infrastructure state. A message being true does not mean every region receives it immediately. Power loss, damaged relays, geography, equipment or institutional access can alter reach without changing the underlying fact.

## Source 3 — PokéNav Match Call

Source: Bulbapedia, PokéNav / Match Call.
URL: https://bulbapedia.bulbagarden.net/wiki/Match_Call
Inspected: 2026-08-18.

Relevant patterns:

- The PokéNav supports registered contacts rather than universal access to every person.
- Contacts can include Trainers and non-Trainers.
- Calls can create follow-up opportunities, including rematch availability.

Reusable lesson for Ouros:

Private communication should require a plausible contact relationship or channel. A recurring NPC can send a message because a contact method was exchanged or an institution knows how to reach the player; the narrative engine should not silently grant universal direct-message access.

No Match Call rematch mechanics are imported into Ouros.

## Source 4 — PokéNav Plus / BuzzNav and TV Mauville

Sources:
- Bulbapedia, PokéNav Plus / BuzzNav: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9Nav_Plus
- Bulbapedia, TV Mauville: https://bulbapedia.bulbagarden.net/wiki/TV_Mauville
- Bulbapedia, Gabby and Ty: https://bulbapedia.bulbagarden.net/wiki/Gabby_and_Ty
- Official Pokémon ORAS page: https://www.pokemon.com/us/pokemon-video-games/pokemon-omega-ruby-and-pokemon-alpha-sapphire/

Relevant patterns:

- BuzzNav displays reports about events and player exploits.
- TV Mauville has multiple program formats rather than one undifferentiated news feed.
- Reporters can physically encounter a Trainer, conduct an interview and later broadcast the result.
- Player-facing communication devices can aggregate navigation, social and broadcast functions.

Reusable lesson for Ouros:

Publication should be attributable. A public story may come from a reporter, official statement, eyewitness footage, institution, rumor desk or automated notice. The resulting report is a claim-bearing artifact, not canonical truth itself.

## Source 5 — Official Rotom Phone

Source: Pokémon Sword and Shield official website.
URL: https://swordshield.pokemon.com/en-gb/gameplay/about-pokedex-rotom-phone/
Inspected: 2026-08-18.

The official page establishes the Rotom Phone as a multifunction personal device integrated with Pokédex and mobility functions.

Reusable lesson for Ouros:

One player device can expose several world systems while authority stays server-side. A future Ouros UI could surface messages, public notices, map alerts, research reports and Chronicle-facing notifications without making the device itself the source of truth.

No Rotom-specific powers or hardware are assumed for Ouros canon.

## Source 6 — Living-World-News for Pokémon Essentials

Source: Eevee Expo, Living-World-News 1.1.0 by Eyebull21.
URL: https://eeveeexpo.com/resources/1883/
Published: 2026-03-04; update 2026-03-05.

Relevant patterns:

- Headlines can depend on story flags, player progress and time of day.
- The same information can appear through bulletin boards, TV and NPC gossip.
- Runtime events can post new news.
- The system tracks unread state.
- A later update exposes news through a PokéNav-style tab.

Reusable lesson for Ouros:

Separate the underlying information item from the presentation channel. One verified public notice can be rendered as a town board entry, a device notification, a radio segment and NPC chatter with channel-specific wording while preserving the same provenance ID.

Do not copy plugin code or text. This is a design-reference source only.

## Source 7 — Dynamic fame/news coupling

Source: Eevee Expo, Trainer-Fame-Reputation resource.
URL: https://eeveeexpo.com/resources/1884/
Published: 2026-03-04.

The plugin can automatically broadcast fame milestones through Living-World-News.

Reusable warning for Ouros:

Do not equate event occurrence, fame, public reporting and public belief. Ouros already separates public standing from canonical truth; this pass keeps that separation. A player's action should become public only through a plausible observation/publication path.

## Cross-check against existing Ouros architecture

The existing Public Memory layer already distinguishes canonical facts, public records and living memory. The World Agency layer already requires evidence and rumors to arise only when someone could plausibly observe an event. This pass extends those rules by modeling the transmission path between source and audience.

This avoids a duplication:

- Public Memory answers: what does a community remember?
- Actor Knowledge answers: what does this actor believe or know?
- Media/Communications answers: what packet of information moved through what channel, when, from whom, to whom and with what transformation?

## PTU/Caelo boundary

No new PTU combat rule is introduced by this research.

Communication equipment, supernatural communication, Pokémon capabilities, Trainer Features, Skill checks, interception effects or device mechanics must be validated against the project's PTU/Caelo source set before receiving mechanical effects.

The project-designated Python oracle contains many out-of-combat and capability structures, but presence in Python does not prove Java or Minecraft implementation. Narrative communication state should therefore remain ordinary world state unless an explicit PTU mechanic is invoked.

## Design conclusions

1. Information needs provenance, channel and audience.
2. Canonical truth must never be replaced by a headline.
3. Coverage and infrastructure should be persistent world state.
4. Private messages require plausible contact or institutional reach.
5. News should be versioned so corrections do not erase earlier misinformation.
6. Multiple channels can present one information object differently while preserving source identity.
7. Emergency alerts should degrade gracefully when infrastructure fails.
8. Delayed or incomplete information can create exploration and investigation without fabricating false world truth.
9. Players need a way to distinguish official notices, journalism, eyewitness claims, rumors and faction messaging.
10. Routine information delivery should compress; only communication failures, contested claims or meaningful choices need full scenes.

## New research directions

Future passes can inspect Pokémon mail/post systems, Ranger communication chains, public photography and documentation, archives/libraries, translation and multilingual communities, propaganda and counter-messaging, and multiplayer privacy/access-control patterns.
