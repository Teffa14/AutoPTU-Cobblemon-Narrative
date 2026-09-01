# Marea pilgrimage and sacred-route candidates — pass 182

Status: PROPOSED / NOT CANON
Date: 2026-09-01

These candidates use existing Marea geography, institutions and residents. They do not canonize a religion, shrine, Legendary association, supernatural effect or regional doctrine.

## 1. The Route People Walk Anyway

Premise:

A recurring community walk uses part of Sendero del Vidrio. Different participants describe it differently: commemorative walk, practical route check, inherited custom, family obligation, social outing.

Existing anchors:

- Sendero del Vidrio;
- Marea Field Office;
- Tideglass Archive;
- Mara Veyra;
- Taro Min;
- Pia Min.

Gameplay:

The player joins one edition, records who stops where, and notices that the route's public explanation is less uniform than expected.

Important boundary:

The event can be culturally important without proving any sacred origin.

Implementation readiness:

High. Requires schedules, location triggers, dialogue, calendar state and provenance records. No battle required.

## 2. Three Stones, Three Explanations

Premise:

Three old marker stones stand along an existing section of route. Residents offer incompatible explanations: old survey points, memorial markers, route-safety markers, or sites where travelers traditionally stop.

NPC weave:

- Taro preserves older records;
- Mara knows current route-use practice;
- Nerea cares about what can actually be inferred from placement;
- Teo may identify later repair work on the stones.

Quest outcome:

The player can establish which physical modifications belong to which period while leaving original purpose unresolved.

Strong lesson:

`MATERIAL_SEQUENCE_KNOWN != ORIGINAL_MEANING_KNOWN`

## 3. The Bell Before Crossing

Premise:

A small bell or sounding device near the seasonal crossing is used before some crossings. Several possible explanations circulate: warning downstream workers, checking audibility in fog, announcing a group, tradition, luck.

Status:

The bell itself is not canon yet.

Gameplay:

Compare current operational use, archive references and participant testimony. The player may discover that a practical signal and a later symbolic custom coexist.

No supernatural resolution is required.

## 4. Offerings That Became Litter

Premise:

People have begun leaving small objects at a route marker. Some are biodegradable, some are written notes, some are ribbons or packaged food. The practice creates maintenance and wildlife concerns.

NPC weave:

- Mara: route condition;
- Nerea/Ema: wildlife observations;
- Taro/Pia: preservation value of some written material;
- Teo: physical wear on the marker;
- Oren: care implications only if an actual case occurs.

Conflict:

Cleanup can be necessary without ridiculing participants or assuming every item belongs in an archive.

No battle needed.

## 5. The Closed Route Morning

Premise:

A scheduled traditional walk conflicts with a temporary Sendero closure after heavy weather or ecological evidence.

Choices:

- postpone;
- use a shortened safe section;
- hold only the opening gathering in Puerto Bruma;
- preserve the date but move the route action;
- cancel this edition.

Core consequence:

The practice acquires version history. The closure remains governed by existing authority, not by participant demand.

Implementation readiness:

High once route closure states and calendar events are projected.

## 6. Witness Walk at Tideglass

Premise:

Taro and Pia organize a small walk with several long-term residents to record how they remember the route's old stops.

Gameplay:

The player carries recording materials, checks names and locations, and later sees contradictory testimonies preserved side by side.

Relationship effect:

Accuracy, respectful correction and provenance matter more than choosing one story immediately.

## 7. The Marker That Moved

Premise:

An old route marker appears a few meters away from the position shown in an earlier survey.

Possible non-exclusive explanations:

- maintenance relocation;
- slope movement;
- later reconstruction;
- inaccurate old survey;
- deliberate repositioning for a public custom.

Gameplay:

Cross-reference Teo's repair knowledge, Tideglass copies and Mirador survey data.

Outcome may remain probabilistic.

## 8. One Morning, Two Calendars

Premise:

A recurring community route date overlaps with a phenology observation window at Mirador or Sendero.

Conflict:

Human traffic may affect detectability. Nerea does not own the route, and participants do not own ecological truth.

Possible solution:

Stagger departure times, establish observation-only sections or document disturbance explicitly.

This connects pass 178 ecology to the current social-practice layer.

## 9. Borrowed Ribbon

Premise:

A reusable decorative object belongs to Tideglass or another institution but has become associated with a recurring public walk.

Problem:

Someone treats it as an offering and leaves it outdoors after the event.

Gameplay:

Resolve custody without invalidating the person's intent. The object's provenance and condition remain tracked.

This candidate intentionally combines memorial/legacy custody and public practice.

## 10. Public Text, Private Doubt

Premise:

A route sign uses stronger wording than the archive evidence supports. Taro wants it corrected. Another resident worries that changing the sign will be read as attacking the tradition itself.

Gameplay:

Draft/review candidate wording using existing claim and publication architecture.

Success means accurate public language, not consensus on belief.

## 11. The Visitor Who Expects a Miracle

Premise:

An outside visitor arrives convinced that a local marker guarantees a rare Pokémon encounter, healing effect or blessing because of a story heard elsewhere.

Marea response:

Residents may disagree about the story but can still explain access rules, local custom and what has actually been observed.

Important boundary:

No encounter is spawned to reward the expectation.

`VISITOR_EXPECTATION != SPAWN_AUTHORITY`

## 12. Procession Under Pressure

Status: mechanically rich candidate.

Premise:

A recurring public walk is underway when a localized Pokémon confrontation or panic occurs near a narrow route section. Participants and route integrity matter, but the event's cultural meaning must remain outside BattleSpec.

### Intended full version

Tactical goals may include protecting an exit corridor, preventing involuntary displacement into unsafe cells, creating space for noncombatants and responding to objective-aware wild behavior.

Dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle when selected content needs it;
- terrain/weather/hazards/zones/reactions;
- exact move-specific behavior;
- exact Abilities;
- exact Items;
- exact Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Current classification: BLOCKED for the full objective-rich version.

### Reduced version

The public group reaches a safe world-state position before battle begins. The cultural event, route restrictions and physical objects remain outside BattleSpec. Any battle uses a stable clearing and audited participants only.

Allowed handoff:

`IMMEDIATE_ROUTE_THREAT_WITHDREW`

After the battle, the world layer separately determines whether the walk resumes, shortens, postpones or ends.

Forbidden automatic conclusions:

- practice validated;
- supernatural claim confirmed;
- route blessed;
- organizer authority expanded;
- closure lifted;
- historical origin proven.

## Recommended implementation order

First: The Closed Route Morning.

Reason: it directly composes calendar, route access, public practice and version history with no tactical dependency.

Second: Three Stones, Three Explanations.

Reason: it teaches material chronology versus interpretation using existing Tideglass/Mirador/Mara/Teo roles.

Third: Witness Walk at Tideglass.

Reason: it strengthens oral-history gameplay and makes contradictory testimony useful rather than a failure state.

Fourth: One Morning, Two Calendars.

Reason: it connects social life to the phenology layer and makes observation disturbance visible.

Do not implement Procession Under Pressure in full until the blocking capability families are verified for the exact battle content.