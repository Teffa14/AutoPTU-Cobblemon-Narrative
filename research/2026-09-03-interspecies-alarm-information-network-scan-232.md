# Interspecies Alarm and Information Network Scan — Pass 232

Status: RESEARCH / PROVENANCE. No canon change.
Date: 2026-09-03

## Bounded question

How can Ouros model information moving between wild Pokémon without treating every nearby species as sharing perfect knowledge, and without forcing a tactical encounter?

This pass builds on:
- `design/global-species-interaction-graph.md`;
- `design/ecology-observation-intervention-contract.md`;
- `design/ecological-pulse-event-contract.md`;
- `proposals/2026-09-03-marea-rain-corridor-ecological-pulse-fixture-231.md`.

It does not replace those systems. It adds a local information-propagation layer between ecological actors.

## Source 1 — New Pokémon Snap behavioral chains

Public gameplay documentation for Blushing Beach (Night) records a chain where player action can cause one Pokémon to disturb another, producing pursuit and additional reactions along the route. The reusable design lesson is not the named species or exact staged event. The useful structure is:

```text
local stimulus
-> actor A changes state
-> actor B detects A or the stimulus
-> B changes state
-> downstream actors react to the changed local context
```

Source:
- Serebii, New Pokémon Snap, Blushing Beach (Night): https://www.serebii.net/newpokemonsnap/locations/beachnight.shtml

New Pokémon Snap also uses repeated visits, alternate routes, different day/night states and environmental scanning to expose different behavior without telling the player the hidden ecology directly.

Sources:
- New Pokémon Snap overview: https://en.wikipedia.org/wiki/New_Pok%C3%A9mon_Snap
- Scan/alternate-route documentation: https://game8.co/games/New-Pokemon-Snap/archives/328716

Authority note: gameplay choreography is inspiration only. No staged Snap sequence becomes Ouros canon.

## Source 2 — Heterospecific alarm-call eavesdropping

Magrath et al. review evidence that animals can use alarm calls from other species. Responses can include immediate anti-predator behavior, altered foraging, changed habitat use and learning about threats. The review emphasizes that information value depends on relevance, recognizability and reliability. It also describes the possibility of "keystone" information producers.

Source:
- Magrath, Haff, Fallow & Radford (2015), Biological Reviews, `Eavesdropping on heterospecific alarm calls: from mechanisms to consequences`: https://onlinelibrary.wiley.com/doi/10.1111/brv.12122

Reusable Ouros lesson:
- interspecies information edges can exist;
- they can be asymmetric;
- listeners should weight a sender by local reliability and relevance;
- one signal can change exposure or refuge use without changing population size;
- recognition can be learned rather than universal.

## Source 3 — Reliability is observer-relative

Magrath, Pitcher & Gardner experimentally found that different bird species responded differently to each other's alarm calls and that apparent reliability depended on the listener's own threat context. A call that produces many "false positives" for one species can still be useful for another if the called-about threat matters to that listener.

Source:
- ANU research record, `An avian eavesdropping network: Alarm signal reliability and heterospecific response`: https://researchportalplus.anu.edu.au/en/publications/an-avian-eavesdropping-network-alarm-signal-reliability-and-heter/

Reusable Ouros lesson:

```text
signal reliability != global property
signal reliability = sender x listener x threat/context x local history
```

This is important for avoiding a global `alarm=true` state that every Pokémon understands identically.

## Source 4 — Recognition can use both prior learning and signal similarity

Fallow, Gardner & Magrath found responses to unfamiliar heterospecific alarms were influenced by acoustic similarity, while learned recognition also mattered.

Source:
- ANU research record, `Sound familiar? Acoustic similarity provokes responses to unfamiliar heterospecific alarm calls`: https://researchportalplus.anu.edu.au/en/publications/sound-familiar-acoustic-similarity-provokes-responses-to-unfamili/

Reusable Ouros lesson:
- species can have an innate/trait prior for some signal classes;
- local experience can strengthen or weaken a learned association;
- persistent individuals may therefore differ in what signals they trust.

## Source 5 — PTU field observation compatibility

PTU Survival explicitly supports scouting wilderness to learn common Pokémon/resources and identifying signs of rarer Pokémon or plants with stronger success. Survival also supports tracking. Stealth supports field researchers observing reclusive or dangerous Pokémon without being detected.

Source:
- PTU skills reference: https://pturpg.wikidot.com/skills

Ouros interpretation:
- Survival/Perception/Stealth can expose evidence about local information cascades when an active Ouros rules profile permits those checks;
- the check reveals evidence, not hidden simulator truth;
- failed or partial checks must not fabricate false ecological facts unless a separate deception/misinterpretation system explicitly does so.

## Source 6 — Non-lethal risk changes habitat use

Real-world ecology-of-fear research supports non-lethal changes in movement, habitat selection and foraging under perceived risk. This reinforces the existing Ouros rule that predation pressure can alter visibility/activity without requiring consumption or battle.

Sources:
- PubMed, `Broadening the ecology of fear`: https://pubmed.ncbi.nlm.nih.gov/33622122/
- Chitwood et al. review of ungulate ecology of fear: https://onlinelibrary.wiley.com/doi/full/10.1002/ece3.8657

## Derived design principles

1. Ecological information is local and lossy.
2. A signal is an observation event, not canonical truth about the threat.
3. The receiver evaluates the signal using species baseline, individual experience, sender reliability, distance, cover, recent history and whether the implied threat is relevant.
4. Different receivers may produce different responses to the same event.
5. Information edges can be asymmetric.
6. Repeated false alarms can reduce trust or create habituation; repeated accurate alarms can strengthen learned response.
7. A player can create a disturbance cascade without the world treating the player as directly commanding every affected Pokémon.
8. Off-screen propagation resolves as state transitions and probability pressure, not hidden AutoPTU battles.
9. Persistent named individuals retain learned signal associations across sessions when persistence policy allows it.
10. Generic Cobblemon actors may express a local state but must never create new persistent knowledge merely by existing or despawning.

## Candidate provenance classes

Proposed information edges should use existing provenance concepts and add explicit evidence fields rather than pretending the relationship is official canon.

Suggested evidence grades:
- `PROVENANCE_EXPLICIT`: official Pokémon source explicitly documents a species reacting to another species' signal;
- `SPECIES_TRAIT_STRONG`: source establishes sensory/social traits that strongly support recognition;
- `PTU_DERIVED`: approved PTU capabilities support detection/communication but do not establish a named species relationship;
- `BIOLOGICAL_ANALOGUE`: real ecology suggests the mechanism only;
- `OUROS_INFERRED`: local history creates learned sender-listener reliability;
- `OUROS_AUTHORED`: reviewed world-specific relationship.

## Mechanical boundary

Pure ecological propagation requires no tactical capability family.

If the cascade remains overworld behavior, the main dependency is Minecraft/Cobblemon/Craftics adapter/playback for reliable visible presentation and world-state feedback. That family remains PARTIAL/BLOCKING end-to-end.

If a cascade escalates to a structured fight, dependencies must be declared for the exact encounter. Do not infer full reactions, forced movement, terrain, weather, status or AI support from a single verified representative mechanic.

## Live engine cross-check

AutoPTU-Java `main` inspected at:
- `1d3ce8784cf5a327ef8dce44e6e73effd1956c3a` — generic movement landing hook registry.

This is useful bounded evidence for deterministic movement landing hooks and tile-entry integration. It does not promote complete movement, reactions, terrain/hazards, abilities, status lifecycle or AI tactical policy as complete families.

Python AutoPTU `main` inspected at:
- `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

No newer Python mechanical evidence relevant to this ecology slice was found.

## Open questions

- maximum propagation radius per signal class;
- whether signal strength decays continuously or by ecology-cell boundary;
- how learned reliability decays across long periods without exposure;
- whether juveniles inherit species priors but not local learned associations;
- how much false-alarm history is stored per persistent individual versus population cohort;
- exact observer checks for distinguishing primary stimulus from downstream reaction;
- whether sound, scent, visual posture and movement cues use one generic signal schema or typed subcontracts.
