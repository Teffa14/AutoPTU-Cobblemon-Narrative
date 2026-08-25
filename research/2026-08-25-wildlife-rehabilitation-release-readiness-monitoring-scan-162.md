# Wildlife rehabilitation, release readiness & post-release monitoring — research scan 162

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is established Ouros canon.
Date: 2026-08-25

## Why this pass exists

The repository already has the correct high-level authorities:

- `care-recovery-welfare-layer.md` owns care cases, observed condition, diagnosis, treatment, narrative recovery and facility state;
- `pokemon-agency-partnership-release-layer.md` owns persistent Pokémon identity, custody, association and release as an identity-preserving state transition;
- `conservation-protected-areas-stewardship-layer.md` owns stewardship, relocation/release policy and the existing `wild_care_transition` concept;
- `wild-nesting-parental-care-juvenile-dispersal-layer.md` owns wild juvenile/dependency observations;
- `research-ethics-consent-subject-protection-layer.md` owns research authorization and intrusive monitoring limits.

What is still shallow is the operational and evidentiary space between `recovered enough for the care case to progress` and `release has produced an observed post-release outcome`.

Pass 162 therefore proposes a subordinate protocol, not a new authority layer.

The research question is:

How can Ouros represent release readiness, release-site selection, hard/soft/staged release, temporary support, post-release monitoring, return/recapture and uncertain outcomes without inventing veterinary rules, Pokémon Loyalty, ownership law, survival percentages or capture mechanics?

## Source A — IUCN guidance for displaced organisms, 2025

Source:
https://iucn.org/resources/publication/iucn-guidelines-responsible-translocation-displaced-organisms

Supporting IUCN story:
https://iucn.org/story/202506/new-iucn-guidelines-offer-direction-responsible-translocation-displaced-wildlife

The 2025 guidance specifically addresses organisms displaced by events such as habitat destruction, human-wildlife conflict, catastrophic events, climate change and human capture. The public summary stresses that not every displaced organism can or should be translocated and that an intervention must consider welfare, ecological risk and effects on resident wildlife and people.

Reusable structures for Ouros:

- `needs help` does not imply `must be relocated`;
- physical recovery does not by itself choose the destination;
- a release decision can end in `NOT_APPROPRIATE_YET`, `RETURN_TO_ORIGIN`, `RELEASE_ELSEWHERE_IF_AUTHORIZED`, `LONGER_CARE`, or another authored outcome;
- release-site decisions should read habitat, population, disease/biosecurity, current disturbance and stewardship state;
- doing something can create more risk than doing nothing, so a valid review may conclude that further intervention is unwarranted.

Do not import IUCN legal authority, species-management thresholds or conservation-translocation terminology as Ouros law.

## Source B — IUCN reintroduction/translocation principles, 2013

Source:
https://iucn.org/resources/publication/guidelines-reintroductions-and-other-conservation-translocations

Library record:
https://portals.iucn.org/library/node/10386

The guidelines provide a general design framework for conservation translocations rather than a single release recipe.

Reusable structures:

- define why movement/release is being attempted before carrying it out;
- evaluate risks and alternatives before the event;
- distinguish release implementation from later success;
- keep post-release monitoring and adaptive response in the same project history;
- preserve a decision trail so later generations can understand why a release occurred under the knowledge available at the time.

Ouros adaptation:

A release event should not close the entire story object. It should open a post-release observation window whose intensity and duration can vary by authored program.

## Source C — U.S. Fish & Wildlife Service rehabilitation evidence review

Source:
https://www.fws.gov/media/evaluation-current-scientific-literature-impact-wildlife-rehabilitation-conservation

The FWS literature review found a limited evidence base for post-release outcomes of rehabilitated birds and noted that studies used different outcome measures, commonly survival or later breeding/recruitment. It also states that there is no single standardized definition of rehabilitation success across the reviewed literature.

Reusable structures:

- `released` is an event, not a success flag;
- outcome can remain unknown because observation is incomplete;
- different programs may use different indicators;
- a lack of later detection does not prove death, failure or departure from the region;
- a later observation can revise an earlier `OUTCOME_UNKNOWN` without rewriting the release event.

This strongly supports keeping assessment scope and monitoring effort explicit.

## Source D — U.S. Fish & Wildlife Service oiled-wildlife training

Source:
https://www.fws.gov/training/oiled-wildlife-training-video-series

The public training series separates field response, rehabilitation activities and animal release, and includes release criteria as its own subject. It also emphasizes trained personnel for hands-on activities.

Reusable Ouros lesson:

Release readiness deserves its own evidence-bearing review between clinical care and physical release. A facility can be competent to stabilize a Pokémon without automatically having authority or capability to choose every release site.

Do not import professional licensure or oil-spill protocols into Ouros canon.

## Source E — pre-release acclimation and post-release monitoring example

Source:
https://www.fws.gov/policy/library/2023/2023-06958.html

The sihek translocation plan provides a concrete example of staged preparation: pre-release aviaries, acclimation, exposure to natural foods, health assessment, radio transmitters, supplemental feeding if needed, daily monitoring after release and the possibility of temporarily bringing an animal back under human care if it becomes sick or injured.

Reusable structures:

- `SOFT_RELEASE` can mean a reversible support phase, not ownership;
- supplementary resources can be tapered or ended rather than becoming permanent world infrastructure;
- return to care after release can be part of the program rather than a narrative failure state;
- monitoring may be intensive initially and later reduced when evidence supports it;
- release outcomes can include movement, feeding, social interaction and other observations instead of one numeric score.

Do not copy transmitter weights, monitoring frequency or the sihek project itself into Ouros.

## Source F — IUCN gibbon rehabilitation example

Source:
https://iucn.org/story/202304/community-engagement-conserve-endangered-javan-silvery-gibbons-indonesia

This public case describes rehabilitation involving health, normal behavior, socialization, acclimation at a release site and post-release monitoring of movement, food use and adaptation.

Reusable structures:

- readiness can have multiple dimensions rather than one `healthy=true` flag;
- social context may matter for some authored species/populations but cannot be generalized to all Pokémon;
- release-site acclimation may be a separate operational stage;
- monitoring can test assumptions made before release.

## Source G — Pokémon: Bonnie for the Defense!

Source:
https://www.pokemon.com/us/animation/seasons/17/episode-48-bonnie-for-the-defense

A wild Lapras is recovering from injury under the care of local children. After medical attention, its repeated orientation toward the water prompts the characters to consider that it wants to return to its ocean home. They escort it and it reunites with its family.

Reusable structure:

care → behavioral observation → hypothesis about destination → assisted return → reunion observation.

Critical Ouros guardrail:

The Lapras story is authored fiction. A Pokémon looking toward a direction does not become a universal `wants release` signal. Ouros should record the observation and let authored/validated interpretation determine what follows.

## Source H — Pokémon: Secrets From Out of the Fog!

Source:
https://www.pokemon.com/us/animation/seasons/16/episode-21-secrets-from-out-of-the-fog

The episode presents a hidden refuge caring for Pokémon that had been mistreated by people. The refuge is simultaneously a care site, a philosophy about human-Pokémon relationships and a location that can itself come under threat.

Reusable structures:

- a sanctuary can be a continuing institution rather than a temporary medical room;
- care philosophy and factual recovery state must remain separate;
- a refuge may become a long-term residence for some Pokémon without making that outcome mandatory for every patient;
- institutional beliefs about humans, release or safety can be challenged by new observations without automatically making either side malicious.

Do not copy Team Plasma, N, the refuge or its ideology into Ouros.

## Source I — Pokémon: The Island of Illusions!

Source:
https://www.pokemon.com/us/animation/seasons/16/episode-30-the-island-of-illusions

The episode includes a remote Pokémon Center serving wild Pokémon even where Trainer demand is absent. It also connects the site's present function with an older history involving an injured Zorua.

Reusable structures:

- wild-Pokémon care demand can justify a facility independently of Trainer traffic;
- a facility can outlive its original service model;
- repeated returns by wild Pokémon can become observed institutional history without implying ownership.

## Source J — PTU baseline and non-violent wild interaction

Sources:
https://pokemontabletop.com/downloads-and-resources/
https://pokemontabletop.com/gm-advice-your-first-ptu-session/

The official PTU site continues to point users to PTU 1.05 resources. Its first-session advice explicitly recognizes non-violent interactions with wild Pokémon and befriending attempts as valid approaches while warning that behavior varies by Pokémon/context.

Mechanical lesson:

PTU supports wild Pokémon as actors outside combat, but this public material does not define a generic rehabilitation/release subsystem, release-readiness score, soft-release mechanic or post-release monitoring rule.

The narrative repository must therefore avoid converting the proposed protocol into PTU mechanics.

## Design synthesis

The strongest reusable chain is:

```text
care case reaches a possible transition point
→ release-readiness question is opened
→ evidence reviewed by dimension
→ release/relocation authority reviews location and current ecology
→ method and contingency are recorded
→ physical release attempt occurs
→ Pokémon identity remains persistent
→ post-release monitoring records observations and non-detections
→ program may continue, taper support, close, pause, return to care or remain unresolved
```

Important separations:

- medically stable ≠ release-ready;
- release-ready ≠ authorized for release;
- authorized ≠ physically released;
- released ≠ established;
- departed release site ≠ successful;
- returned to facility ≠ failed;
- not detected ≠ dead;
- repeated human approach ≠ tame;
- use of supplementary food ≠ permanent dependency;
- persistent identity ≠ ownership;
- telemetry location ≠ complete knowledge of internal state.

## Proposed Pass 162 authority boundary

The new protocol should own only:

- readiness assessments and their evidence;
- release-site assessment records;
- release-method operational plans;
- release attempts and contingencies;
- support/taper records;
- post-release monitoring series;
- return/recapture observations;
- scoped outcome assessments.

It must not own:

- diagnosis or treatment: Care;
- release/relocation policy: Conservation;
- identity/custody/association: Pokémon Agency;
- population effects: Conservation / Wild Collectives / Migration / Conservation Genetics;
- biosecurity screening: Biosecurity;
- research authorization: Research Ethics;
- mechanical capture/release/Loyalty/Command: PTU/Caelo + authoritative runtime.

## Mechanics and Caelo boundary

No complete primary Caelo corpus defining rehabilitation, release readiness, soft release, wildlife transport or post-release monitoring was recovered in the inspected project sources for this pass.

Super PTU Online Helper was not exposed as an invocable capability.

Do not invent:

- Medicine DCs for release;
- required number of care days;
- release percentages;
- Loyalty thresholds;
- capture modifiers;
- obedience checks;
- movement/carrying limits;
- sedation or restraint mechanics;
- telemetry bonuses;
- species-specific rehabilitation times;
- automatic release-site selection.

External wildlife guidance is a narrative architecture source, never a PTU rules source.