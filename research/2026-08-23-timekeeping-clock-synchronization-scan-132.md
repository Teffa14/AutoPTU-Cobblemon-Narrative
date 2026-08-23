# Narrative Research Scan — Pass 132: Timekeeping, Clocks & Synchronization

Status: RESEARCH / PROVENANCE ONLY. Not established canon.
Date: 2026-08-23

## Why this pass exists

The repository already has several systems that depend on time:

- `observation-settlement-time-layer.md` owns narrative escalation clocks and bounded action windows;
- `seasonality-calendar-phenology-layer.md` owns dates, recurring annual phases and phenology;
- `diel-activity-circadian-rhythms-layer.md` owns activity patterns across a day;
- `railways-stations-rail-operations-layer.md`, `postal-courier-parcel-logistics-layer.md`, `festivals-ceremonies-observances-layer.md`, `wildlife-migration-stopovers-corridors-layer.md` and other layers use schedules;
- `astronomy-celestial-observation-layer.md`, `meteorology-forecasting-weather-layer.md`, `metrology-calibration-measurement-standards-layer.md` and Science depend on reliable timestamps;
- `temporal-continuity-time-travel-layer.md` owns exceptional temporal contexts, loops and anomalous chronology.

What was still missing was an authority for ordinary civil/operational timekeeping:

- what clock or time standard an institution is using;
- how a local clock becomes synchronized to a reference;
- how much a clock has drifted;
- whether two timestamps are directly comparable;
- whether a published schedule uses the same time reference as a traveler’s device;
- how timestamp corrections are recorded without rewriting the original observation;
- how server-authoritative world time is projected into Minecraft without trusting a client device clock.

This pass researches that gap. It does not establish Ouros time zones, daylight-saving rules, atomic clocks or any other technology as canon.

## Repository overlap review

The full `design/`, `research/` and `proposals/` inventories were inspected before selecting this topic. Searches for `timekeeping`, `clock synchronization`, `time zone` and equivalent terms did not find a dedicated authority layer.

Important boundaries:

- Calendar/Seasonality remains authority for dates and recurring annual phases.
- Regional narrative clocks remain progress trackers, not physical clocks.
- Metrology remains authority for general calibration and measurement traceability.
- Temporal Continuity remains authority for actual time travel, loops and divergent temporal contexts.
- Digital Systems remains authority for software records and logs.
- Domain systems remain authority for schedules and events in their own operations.

The new layer should supply a shared time reference and timestamp provenance to those systems rather than replace them.

## Source 1 — Official Pokémon BDSP site: time and day alter the world

Source: The Pokémon Company, “Pokémon Brilliant Diamond and Pokémon Shining Pearl — Gameplay.”
URL: https://diamondpearl.pokemon.com/en-au/features/

The official site states that routes and towns differ depending on time and day. It also presents the Pokétch Digital Watch as a tool for tracking time.

Reusable structure:

Time can be visible to the player as ordinary infrastructure while also changing which world states are currently available. The useful design lesson is not to duplicate Sinnoh’s encounter tables. It is to make time an explicit input with a visible reference.

Ouros transformation:

- player-facing clocks can be real objects or interfaces;
- schedules can cite a specific time reference;
- time-dependent content should derive from authoritative world state rather than the client’s local operating-system clock;
- a displayed clock is a presentation of time, not the owner of time.

## Source 2 — Official BDSP Trainer Guide: game clock and local real-world settings are linked in that title

Source: The Pokémon Company, “Pokémon Brilliant Diamond and Pokémon Shining Pearl Trainers Guide — Pokémon Trainer Fundamentals.”
URL: https://diamondpearl.pokemon.com/en-au/trainersguide/fundamentals/

The guide explains that the game uses the Nintendo Switch system clock for its time-of-day categories and tracks days of the week.

Reusable structure:

A game can bind world timing to an external clock, but this is a title-specific implementation choice.

Ouros design lesson:

Do not inherit this behavior automatically. A persistent multiplayer world needs a server-authoritative chronology. Client clocks may be useful display inputs, but they cannot decide whether a migration started, a train departed, a permit expired, a timed observation occurred or a shop changed schedule.

## Source 3 — Pokétch watch/calendar/stopwatch: different temporal tools serve different jobs

Source: Bulbapedia, “Pokétch.”
URL: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9tch

The Pokétch includes separate watch, calendar, stopwatch and alarm concepts across its apps.

Reusable structure:

Time-of-day, elapsed duration, calendar date and alarms are different data products. A single `time` field should not silently stand for all of them.

Ouros implication:

Separate at minimum:

- timestamp / instant;
- local displayed time;
- elapsed duration;
- calendar date;
- scheduled deadline;
- countdown or narrative progress clock.

This is a secondary reference used only for design structure, not PTU rules.

## Source 4 — Pokémon Insurgence: visual daytime can be decoupled from time-dependent state

Source: Pokémon Insurgence Wiki, “Options.”
URL: https://wiki.p-insurgence.com/Options

The fangame exposes a `Constant Daytime` presentation option that changes daytime graphics without changing certain time-based events such as evolution requirements.

Reusable structure:

Presentation time and authoritative temporal state can be decoupled.

Ouros implication:

Minecraft sky rendering, accessibility presentation or a temporary visual override must never rewrite the authoritative world clock. Conversely, a server timestamp change must not require every visual system to expose the same representation.

Transformation rule:

Do not import Insurgence events, evolutions, options UI or custom mechanics. Reuse only the architectural distinction between presentation and underlying time state.

## Source 5 — Public Pokémon tabletop discussion: bounded in-world time can structure a location

Source: Pokémon Tabletop community forum, “Safari Zone,” 2012-08-04.
URL: https://www.tapatalk.com/groups/pokemon_tabletop/safari-zone-t1750.html

A GM discussion proposes using a bounded number of in-game hours for a Safari Zone visit.

Reusable structure:

In-world time can create understandable limits around an activity without requiring a real-time countdown.

Ouros implication:

A schedule can be expressed against authoritative world time while the UI compresses travel, downtime or routine actions. Time pressure and real-time player pressure should remain separate.

This is community practice, not a PTU rules source.

## Source 6 — NIST UTC time scale: reliable time is a maintained reference, not one perfect clock

Source: NIST, “How UTC(NIST) Works.”
URL: https://www.nist.gov/pml/time-and-frequency-division/time-services/utcnist-time-scale/how-utcnist-works

Source: NIST, “UTC(NIST) Time Scale.”
URL: https://www.nist.gov/pml/time-and-frequency-division/time-realization/utcnist-time-scale

NIST describes a maintained time scale produced from an ensemble of clocks, with adjustments that keep it aligned to UTC.

Reusable structure:

A trusted reference time can be an institutional product with provenance and revision history rather than a magical immutable clock object.

Ouros implication:

If Ouros eventually has regional or interregional standards, Chronicle should preserve:

- which authority maintained the reference;
- which standard/version was used;
- whether a local clock was synchronized;
- the estimated offset or uncertainty when relevant;
- any correction applied later.

Do not import atomic-clock technology or UTC itself into canon unless separately approved.

## Source 7 — NIST Internet Time Service: reference time, network transfer and local display are separate

Source: NIST, “NIST Internet Time Service (ITS).”
URL: https://www.nist.gov/pml/time-and-frequency-division/time-distribution/internet-time-service-its

NIST distinguishes the reference time from its transfer over a network. It also notes that local-time conversion is the client’s responsibility for one of the simpler protocols, and that observed accuracy depends partly on network conditions.

Reusable structure:

`authoritative reference -> transfer -> local clock -> displayed local time` is a useful chain for Ouros.

A correct upstream time source does not prove every downstream clock is synchronized. A device may also display local civil time while storing an absolute timestamp.

## Source 8 — NTP design: distributed clocks drift and must be compared repeatedly

Source: Network Time Foundation/NTP reference library, “Computer Clock Modelling and Analysis.”
URL: https://www.ntp.org/reflib/reports/time/timeb.pdf

The NTP literature treats local computer clocks as oscillators that can drift and describes synchronization as repeated comparison and adjustment.

Reusable structure:

A clock can be healthy, drifting, isolated, recently corrected or using a fallback reference. This creates world state without needing dramatic sabotage.

Ouros implication:

A communications outage can produce later timestamp disagreement even after messages begin flowing again. The outage does not need to delete any records; it changes confidence in their temporal alignment.

## Cross-source design conclusions

### 1. Chronicle time and displayed clock time must be separate

The server needs an append-only authoritative chronology. A clock tower, Pokétch-like device, station display or Minecraft sun position is a projection of that chronology.

### 2. Raw timestamps must survive correction

If a camera was seven minutes slow, its original timestamp remains part of provenance. A later correction can map it to a better estimate without altering the raw record.

### 3. Different clocks can be internally consistent and mutually offset

Two institutions may each produce orderly logs while their clocks disagree. That is a temporal-linkage problem, not proof that either record was falsified.

### 4. Schedule reference must be explicit

A railway departure, observatory slot, clinic appointment, tournament registration deadline or migration survey window should cite the time standard or local schedule convention it uses.

### 5. Clock outage and event outage are different

A station clock stopping does not stop trains. A network time service failing does not stop time. An event can occur while every nearby clock is wrong.

### 6. Presentation can be accessible without mutating world truth

A player may display 12-hour time, 24-hour time, relative countdowns or local labels. Those are presentation choices. They must not alter event ordering.

### 7. Ordinary drift must not become a conspiracy generator

Most discrepancies should have mundane candidates first: unsynchronized device, manual setting, stale schedule, transport delay, power loss, network outage, reference revision or human transcription.

### 8. No direct timekeeping-to-battle shortcut

A clock discrepancy cannot create initiative changes, extra turns, delayed Move behavior, Trick Room, Speed stages or temporal rewinds. Battle time is owned by the battle engine.

### 9. Timekeeping and time travel remain distinct

An incorrect clock never creates a temporal anomaly. A temporal anomaly may cause confusing timestamps, but only Temporal Continuity can establish that world truth.

## Candidate data concepts emerging from research

- `TIME_STANDARD`
- `TIME_STANDARD_REVISION`
- `LOCAL_TIME_RULESET`
- `CLOCK_SOURCE`
- `CLOCK_INSTANCE`
- `CLOCK_SYNC_EVENT`
- `CLOCK_OFFSET_OBSERVATION`
- `TIME_REFERENCE_LINK`
- `RAW_TIMESTAMP`
- `CORRECTED_TIMESTAMP_ESTIMATE`
- `SCHEDULE_TIME_REFERENCE`
- `TIME_CORRECTION_EVENT`
- `TEMPORAL_DISCREPANCY_CASE`
- `CLOCK_OUTAGE`
- `TIME_DISPLAY_PROFILE`

## PTU/Caelo boundary

No external narrative source is treated as a PTU rules source.

The project’s complete named Caelo corpus was not recoverable as a reliable invocable source in this runtime. Super PTU Online Helper was also not exposed as a callable capability. Therefore this pass does not assert:

- time-based Skill DCs;
- clock or stopwatch item bonuses;
- initiative effects from accurate timing;
- Speed or Accuracy benefits;
- extra actions for deadlines;
- day/night combat modifiers;
- temporal Move effects;
- Trick Room behavior beyond the battle engine’s existing verified contracts;
- any Dialga, Celebi or other time-related Legendary capability.

## Canon safety

Everything in this file is research. Proposed Ouros institutions, standards, clocks and historical changes remain non-canon until reviewed.
