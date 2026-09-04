# Individual habituation and sensitization scan

Status: RESEARCH / PROVENANCE ONLY
Pass: 256
Canon effect: NONE
Date: 2026-09-04

## Question

How should repeated human disturbance change the future visible behavior of an individual wild Pokemon without treating all members of a species identically, changing population truth, or inventing tactical AI that AutoPTU-Java does not yet verify?

## New public-source findings

1. Ensminger and Westneat, Ethology 118 (2012), DOI 10.1111/eth.12009. House sparrows showed consistent individual differences in risk-taking and variation in neophobia; personality and behavioral plasticity should be treated as separate phenomena. Repeated disturbance can therefore change response while individuals remain distinguishable in baseline tendency.

2. Uchida, Blumstein and Candolin, Behavioral Ecology 32 (2021), DOI 10.1093/beheco/arab016. Fifteen years of yellow-bellied marmot evidence showed population-level habituation patterns together with individual divergence: some animals with greater flight distances became sensitized under repeated approaches. Reduced overt avoidance did not guarantee absence of longer-term cost.

3. Ellenberg, Mattern and Seddon, Animal Behaviour 77 (2009), DOI 10.1016/j.anbehav.2008.09.021. Yellow-eyed penguins differed in initial stress response and habituation potential according to prior experience and individual character; some did not habituate and some appeared to sensitize.

4. Vincze et al., Behavioral Ecology 27 (2016), DOI 10.1093/beheco/arw047. Urban and rural house sparrows differed in field tolerance, while controlled repeated exposure also demonstrated habituation dynamics. Context and exposure history matter separately from species identity.

5. Viblanc et al., BMC Ecology 12 (2012), DOI 10.1186/1472-6785-12-10. Responses to frequent low-intensity disturbance can attenuate while responses to infrequent, more noxious disturbance remain strong. Method intensity therefore belongs in the response model.

## Reusable Ouros lessons

A population pressure value is insufficient to decide one Pokemon's reaction. Evaluate species policy, individual baseline temperament, accumulated exposure history, disturbance method/intensity and immediate context.

Habituation and sensitization are state trajectories, not permanent personality labels. An individual can become more tolerant to one class of repeated low-risk stimulus while remaining strongly responsive to another.

Reduced visible flight is not proof that disturbance has no cost. Ouros should not convert a lower avoidance response into a blanket welfare-success flag.

Population pressure and individual response must remain separate ledgers. Shared local disturbance can affect projection policy while individuals inside that context still produce different exposure/withdrawal outcomes.

Response history should be reversible or revisable through later evidence. A single encounter cannot permanently label an individual as tame, fearful, aggressive or habituated.

## Proposed vocabulary

FIXTURE-ONLY implementation states for testing:

BASELINE
HABITUATING
SENSITIZING
CONTEXT_TOLERANT
CONTEXT_AVOIDANT

These are not canon Pokemon personality terms and are not PTU statuses.

## PTU/Caelo boundary

The canon first Sendero Fletchling freezes battle identity and PTU profile but explicitly does not state that every Fletchling is always aggressive or behaviorally identical. This research therefore extends an allowed ecology dimension without modifying its PTU stats, Ability, Moves or population count.

No source reviewed here grants a PTU mechanical modifier. Survival, Perception, Features, Moves, Abilities or status effects must use their own verified engine contracts before they change a tactical outcome.

## Design consequence

Pass 255 can write a local disturbance impact. Pass 256 should evaluate that shared pressure against an individual response profile and emit only an ecology/projection decision such as remain exposed, withdraw earlier, widen personal standoff distance or retain baseline presentation. It must not move the actor tactically during battle.

## Canon status

All numerical thresholds, temperament values, response slopes and Fletchling-specific trajectories remain PROPOSED/FIXTURE-ONLY. No individual habituation trait is canon-approved by this note.