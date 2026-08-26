# Ouros Narrative Research — Temporary Public Events & Operations — Pass 55

Status: Research only. Provenance and design evidence; not Ouros canon.

Date inspected: 2026-08-26

This pass looks at temporary public events as operational world state: setup, opening, stalls, activities, visitor pressure, service dependencies, disruptions, closure, teardown and aftermath. Ouros already has seasonality, public memory, tourism, material economy, staffing, accessibility, sanitation, travel and communications. The useful gap is the handoff between those systems during one event instance.

No external plot, character, dialogue, festival name, minigame, villain plan or distinctive sequence is imported. Sources are used only for reusable structures.

## 1. Official Pokémon game structure — a festival is a temporary service configuration

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Kitakami_Hall
- https://bulbapedia.bulbagarden.net/wiki/Festival_of_Masks

Kitakami Hall changes during the Festival of Masks. Food vendors and a dedicated activity appear in the same public place, and the event is tied to a recurring local tradition rather than being a permanent settlement configuration.

Reusable lessons for Ouros:
- one physical site can have a temporary event layout without becoming a second location identity;
- event-specific vendors and activities should have bounded operating windows;
- the event roster can combine stable local actors with temporary services;
- the event may have a historical edition chain, so present operations should be able to reference prior versions;
- a cultural activity can carry inherited interpretation without its story being automatically true.

The important abstraction is not the particular stalls or game. It is a temporary operational snapshot layered over an existing place.

## 2. Official Pokémon story structure — public ritual and historical truth can diverge

Source:
- https://bulbapedia.bulbagarden.net/wiki/Festival_of_Masks

The Festival of Masks has changed across generations because the community's interpretation of an old event changed. Present-day participation therefore exposes both current public practice and a historical claim that can later be questioned.

Reusable lessons:
- a recurring event should preserve edition history rather than overwrite its prior meaning;
- signage, performances, commemorative objects and activities may communicate a public interpretation, not canonical truth;
- archival or archaeological evidence can create a revision debate without invalidating the event's social importance;
- correcting a historical claim does not imply the community immediately changes every ritual or display.

This fits the existing Public Memory, Archives, Myth/Archaeology and Media layers. Pass 55 should only provide event-instance hooks for those systems.

## 3. Official Pokémon animation — a one-day festival concentrates professions, visitors and family expectations

Source:
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Street_Performer_Festival

The Pokémon Street Performer Festival is an annual one-day event with performers, Pokémon acts, food and merchandise stalls. Its story also uses the event as a point where a family/professional expectation becomes visible in public.

Reusable lessons:
- short events can justify temporary clustering of performers, vendors and visitors;
- a recurring event can expose personal or professional pressure because people who normally occupy different social graphs share one place;
- performers and vendors need operator identity and schedule state, not just decorative NPC placement;
- participation, refusal, cancellation or altered performance can remain meaningful even when no battle occurs.

Ouros should therefore allow event participation to create Chronicle and relationship state without inventing mechanical Contest, Performance or Trainer Feature rewards.

## 4. PTU campaign log — festival activity can expose an ecological dependency

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/ug8b7t

A public Pokémon Tabletop United campaign log describes a town festival whose offerings are connected to local Pokémon behavior. Investigation during the festival reveals that a significant tree is unhealthy and that the ecological problem is contributing to drought conditions.

Reusable lessons:
- a festival can reveal why people and wild Pokémon use the same resource or place;
- offerings, decorations or food distribution can have ecological consequences without becoming magical mechanics;
- a public celebration can transition into observation and investigation while preserving its social context;
- resolving the ecological issue can alter later town and event state.

Do not copy the saved-town sequence, species, drought cause, tree disease or festival origin. The reusable structure is `public event -> observed anomaly -> ecological dependency -> persistent operational consequence`.

## 5. PTU scenario evidence — a festival can contain several optional participation modes

Source:
- https://www.reddit.com/r/lfg/comments/v2suxf

A publicly advertised Pokémon Tabletop United one-shot uses a spring festival as a shared location for shopping, skill-oriented activities, catching-oriented competitions and combat, while also giving the party a separate safety responsibility.

Reusable lessons:
- one event can support multiple optional activities rather than forcing one linear quest;
- different experience levels can be served by different authored activities without changing the whole event;
- public safety or staff concerns can coexist with ordinary participation;
- the event should remain enjoyable even if the player declines the incident hook.

Ouros translation:
An event instance should publish an activity roster. Each activity owns its mechanics reference and availability state. Narrative code must not invent competition checks, catch rules, rewards or combat modifiers.

## 6. PTU actual-play evidence — leisure locations can sustain a full session

Source:
- The Reckless Rollers, `FTTC 7: Petey's Playland`, published 2026-02-15.
- https://creators.spotify.com/pod/show/reckless-rollers

The public episode description places a full PTU actual-play session at an amusement park. The useful evidence is narrow: a leisure venue can be worthy of full table time without being reduced to a transition menu.

Reusable lesson:
Ouros should allow a temporary fair, park day, festival or market to become a playable social space when there are real choices, relationships, investigations or operational problems. It should still compress routine attendance when nothing meaningful is happening.

## 7. Long-running PTU actual play — recurring special events can become campaign memory

Source:
- Pokémon World Tour: United, a public PTU actual-play series active 2016–2026.
- https://podcasts.apple.com/us/podcast/pokemon-world-tour-united/id1154176782

Public listings include recurring special-event material such as `Candle Nights` alongside the main campaign and show a long-lived world with more than one hundred episodes.

Reusable lessons:
- a recurring event can gain meaning from earlier editions;
- an event can become a memory surface for characters who participated before their main journey or at different career stages;
- later editions can reference prior participants, incidents and traditions without replaying the same quest.

This reinforces the Edition Continuity rule already present in `design/seasonality-calendar-phenology-layer.md`; Pass 55 should consume that rule rather than duplicate it.

## 8. Existing Ouros ownership map

Repository inspection before writing found that most event-related concepts already have an owner:

- Seasonality/Calendar owns recurrence, world date and event windows.
- Public Memory owns remembered editions, controversies and legacy.
- Tourism owns visitor pressure and destination effects.
- Workplaces owns staffing and professional availability.
- Material Culture/Economy owns vendors, workshops, supply routes and market shortages.
- Accessibility owns participation accommodations and access barriers.
- Waste/Sanitation owns cleanup, refuse and pollution state.
- Travel/Transit owns route and service capacity.
- Media/Communications owns announcements, schedules and corrections.
- Civic Governance owns public works and institutional decisions where applicable.
- Contest/Performance and Battle Institutions own their formal mechanical event types.

The missing layer is operational coordination for one temporary event instance: which dependencies are required, which services are active now, which site zones are open, what phase the event is in, what incidents are affecting it and what must be handed back to the owning systems after closure.

## 9. Design rule — event mode does not clone the settlement

A festival, market day, exhibition, convention, tournament weekend or public ceremony should normally be a temporary state overlay on existing locations.

The event may add:
- temporary stalls;
- stages or activity areas;
- barriers/signage;
- staff-only work areas;
- temporary service desks;
- scheduled performances;
- visitor cohorts;
- closures or reroutes;
- cleanup state.

When the event ends, the underlying location remains the same location with an updated Chronicle and world state.

## 10. Design rule — crowds are aggregate state until individuals matter

Do not instantiate every visitor as a persistent actor.

Use:
- aggregate attendance/pressure bands;
- representative visitor cohorts;
- named staff, performers and vendors where recurring;
- named witnesses, specialists, rivals or contacts only when events promote them to persistent relevance.

A crowd description does not create difficult terrain, interception rules, panic movement or damage.

## 11. Design rule — setup and teardown create real story state

Temporary events should have before and after states.

Setup can expose:
- missing deliveries;
- unavailable staff;
- access problems;
- weather-driven relocation;
- signage errors;
- equipment custody;
- ecological restrictions;
- service conflicts.

Teardown can expose:
- lost property;
- damaged infrastructure;
- waste backlog;
- unreturned borrowed equipment;
- evidence or records left behind;
- route reopening;
- wildlife returning to a temporarily occupied space;
- disputes about what the next edition should change.

These consequences should write back to their owning systems instead of remaining trapped in an event script.

## 12. Mechanical boundary

An event can narratively contain dense crowds, temporary fencing, rain, loose equipment, queues, frightened Pokémon, blocked exits or moving performers.

Those facts do not automatically become PTU tactical rules.

Current AutoPTU-Java still explicitly leaves forced movement, terrain, hazards, reactions, full damage resolution, status-controller completion, full hook registries, AI scoring/policy and the Craftics/Cobblemon adapter unfinished. Rich event combats therefore need an executable reduced version whenever they depend on crowd displacement, reactive protection, dynamic hazards or objective-aware AI.

## 13. Originality boundary

Do not copy:
- Kitakami festival names, stories, stalls, minigames or characters;
- anime performers, family conflicts or incidents;
- PTU campaign-log towns, species, ecological problem or resolution;
- one-shot festival names, competitions or criminal scenario;
- actual-play characters, venues or episode plots.

Ouros may reuse only abstract structures: temporary service configurations, recurring editions, public interpretation drift, optional activity rosters, event-driven ecological observation, setup/teardown state and operational dependency handoffs.

## 14. Pass-55 conclusion

The useful addition is a temporary-event operations extension. It should coordinate existing Ouros systems for one bounded event instance without becoming a second calendar, economy, tourism, crowd-simulation or public-memory engine. The strongest gameplay value comes from making setup, live operation and aftermath persistent enough that the next edition remembers what actually happened.