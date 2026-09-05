# Proposal — Information Network Mystery Loop — Pass 283

Status: PROPOSED. NOT CANON.
Date: 2026-09-05

## Premise

A world event becomes interesting because different people learn about it at different times, through different channels and from different source roots.

The player may arrive somewhere where one NPC has direct evidence, another repeats a report, a third has not heard anything, and a fourth acts on stale information. The situation evolves even if the player is elsewhere because scheduled communication continues in semantic world time.

This structure is global. It is not tied to Marea, Sendero or any specific region.

## Example original loop

An unusual event occurs on a route between two communities. A worker directly observes a relevant fact and sends a warning. The first recipient changes plans after delivery. Another character hears the warning through a relay and forwards it. A later listener receives the same story from two people but both chains trace back to the original observer, so the evidence is still one-root hearsay.

A separate traveler later produces an independent observation. That second root materially changes the confidence landscape.

Meanwhile a communication channel fails. Some NPCs continue operating on old information and miss, delay or reroute commitments. The player can investigate the difference between what happened and who knew what when.

Nothing in this premise requires a villain or a false rumor. Delay and uneven access are enough to generate consequences.

## Player-facing structures enabled

- trace a circulating story back to its source;
- discover that several apparent witnesses share one original root;
- carry information manually when a channel is unavailable;
- decide whom to warn first when time matters;
- compare independent observations;
- encounter NPCs whose schedules changed because they received a message earlier;
- arrive before a warning and witness consequences of information lag;
- discover why a rival, faction or official acted rationally from stale information;
- use social relationships to reach a better-connected recipient without granting global knowledge.

## NPC arcs

A recurring NPC can become known as a reliable messenger because of authored/provenance-backed outcomes rather than a generic reputation stat. Another can be cautious about second-hand reports. A rival can reach a correct conclusion from a different information path. Friends can disagree because their ledgers contain different evidence.

Those tendencies should later integrate with Pass 280 relationships and future deception/source-confusion work. They are not canonized by this proposal.

## Reduced implementation version

The reduced version is entirely world-agent simulation:

1. world event creates an observation available to an NPC;
2. sender schedules a message;
3. semantic latency passes off-screen;
4. receiver ledger changes only at delivery;
5. recipient replans agenda/travel if the new belief makes another intent eligible;
6. provenance remains queryable by investigation/dialogue UI.

Required AutoPTU capability families: none.

Minecraft/Cobblemon presentation is optional for remote communication and required only for channels explicitly configured as local/projection-dependent.

## Full encounter version

A richer version may turn information pressure into a pursuit, confrontation, escort, ambush, rescue or battle. The narrative trigger is allowed before tactical completeness; the structured segment must declare its exact dependencies.

Examples:
- chase/interception: complete movement including interception/forced movement;
- battlefield geometry or LoS: targeting/footprints/range/LoS;
- weather or hazardous zone changing tactics: terrain/weather/hazards/zones/reactions;
- delayed or temporary combat effects: full turn/round lifecycle plus status lifecycle and the specific move/ability/item/feature family involved;
- autonomous enemy tactical choice: AI tactical policy;
- visible Minecraft/Cobblemon reproduction of authoritative results: adapter/playback support.

If those capabilities are not verified, run the reduced world-agent version or author a simpler structured encounter using only verified families. The information premise does not change.

## Consequence model

The useful consequences are not only combat outcomes. Information latency can affect:
- attendance;
- departures and arrival times;
- access to opportunities;
- who investigates;
- who prepares resources;
- who believes the player;
- which NPC is present when another event occurs;
- whether a faction appears coordinated or fragmented without implying hive-mind knowledge.

## Canon questions left open

- Which communication technologies exist in each part of Ouros?
- Which organizations operate formal dispatch/bulletin networks?
- What channels can fail and for what world-state reasons?
- When does a public announcement become accessible knowledge to a named NPC?
- How do literacy, language, devices, role permissions and distance affect access?
- Which persistent NPCs actively relay information versus merely retain it?

These require separate canon decisions. Synthetic fixture channels must not answer them implicitly.
