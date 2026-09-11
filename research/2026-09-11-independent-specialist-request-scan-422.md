# Independent specialist request and assignment-cost scan — Pass 422

Status: RESEARCH / PROVENANCE ONLY. Nothing in this note is canon.

## Repository-first deduplication

The recursive main-branch repository tree at `ab17c2ad3109d7c31a76ff954793cf5cf8c8f916` was inventoried before writing. Current focus, canon governance, Marea resident/institution bindings, Pass 418–421 AutoPTU consequence/observation/delivery/replanning work, global NPC planner state, recent research/proposals and the Kairos/PTU source router were reviewed.

Frequently reused recent anchors were excluded. Repository search found no prior use of `Unavowed` under that title and no prior use of `Invisible, Inc.` under that title.

## New source: Unavowed

Public source: Wadjet Eye Games' 2018 adventure game, summarized in publicly accessible reference material.

https://en.wikipedia.org/wiki/Unavowed

Observed high-level structure:

At the beginning of missions, the player selects a limited companion group. Different companions expose different ways to investigate and solve the same broad mission problem because they bring different capabilities and perspectives.

Ouros-safe abstraction:

A world assignment can legitimately require a specialist without implying that one specific person must be teleported into the job. The useful state is the capability/request requirement plus the actual availability of named people who might satisfy it. A requester may ask one technician, medic, researcher, courier or field worker first, then adapt when that person cannot or will not join.

Do not import Unavowed's characters, supernatural premise, cases, dialogue, companion powers, puzzle solutions, locations or story outcomes.

## New source: Invisible, Inc.

Public source: Klei Entertainment's 2015 tactical stealth game, summarized in publicly accessible reference material.

https://en.wikipedia.org/wiki/Invisible%2C_Inc.

Observed high-level structure:

The campaign asks the player to choose missions and deploy a limited set of agents while travel consumes a finite global time budget. Personnel, equipment, location and time therefore interact: a useful agent can be unavailable in practice because putting that person on one task carries opportunity cost for another.

Ouros-safe abstraction:

Availability should be a world fact rather than an assumption attached to quest text. A specialist request can arrive while the target is travelling, working, resting, committed elsewhere or unable to reach the site before the useful window closes. The request still exists and remains reconstructable even if the answer is no or too late.

Do not import the espionage setting, corporations, agents, mission map, alarm system, procedural levels, plot or tactical rules.

## Combined design lesson

A request for another person should produce a causal chain rather than direct mutation of their schedule:

1. One NPC receives evidence and replans.
2. That NPC selects an intent to request help or a specific capability.
3. The requester's selected intent becomes a durable world-action intent.
4. A later communication event must actually reach the proposed specialist.
5. The proposed specialist independently evaluates the request against their knowledge, permissions, location, travel cost, needs, relationships and existing commitments.
6. Acceptance, delay, refusal, counter-proposal or silence are all valid outcomes.
7. Only an accepted durable commitment changes the specialist's future schedule.

This gives the player readable causal history. If two staff members appear to disagree, the world can explain whether the issue was missing information, travel time, conflicting duties, refusal or delayed communication instead of relying on a hidden quest flag.

## Canon-safe Ouros surfaces

Marea provides existing examples without requiring new canon:

- Mara Veyra coordinates field reports and practical assistance.
- Teo Lark maintains ordinary equipment and field instruments.
- Oren Vale handles routine care within verified mechanics.
- Dr. Nerea Sol performs ecological/weather observation.
- Lia Morn coordinates docks and unloading windows.

These existing roles are useful test surfaces for a request/availability pattern. This research does not create a new incident, relationship, duty, schedule or standing command chain among them.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` routes Trainer capabilities, Skills/Features, combat, movement/terrain, status, hazards/weather, encounters, Items and living-world structures to the supplied PTU/Kairos source material.

Pass 422 does not infer any new Trainer Feature, Skill check, action, movement permission, item effect or combat rule from the external game references above.

A world request for a specialist describes narrative/world-agent intent. If satisfying that request later requires structured mechanics, the normal explicit AutoPTU handoff remains mandatory.

## Capability impact

No permanent battle capability category is promoted.

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited paths.

Action economy/initiative: PARTIAL.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: PARTIAL and individually gated.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for audited ordinary world/tactical actions. Specialized rescue, escort, carry, retrieve, protect, interact or extract actions still require explicit admission when they become tactical.

AI tactical policy: BLOCKING for specialized rescue-first, escort, protect-carrier, objective-aware withdrawal and disengagement policies unless implemented.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative tactical objective state, specialized non-KO completion and in-flight battle recovery.

## Candidate unlocked by the scan

See `proposals/2026-09-11-the-person-you-ask-still-has-a-choice-422.md`.
