# Research scan: global NPC audience / recipient resolution — Pass 285

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-05

This file records public-source inspiration. It does not create canon or PTU rules.

## Gap inspected

Pass 283 schedules information only after sender and receiver are explicit. Pass 284 can selectively wake the receiver. The unresolved seam was sender-side choice: who gets contacted, why, through which available connection, and under what fanout limit.

## Sources and reusable lessons

### Klaas, Southey & Cheung — Particle-Based Communication Among Game Agents, AIIDE 2005
Public source: AAAI AIIDE proceedings.

High-level lesson: agents operating without global knowledge need explicit communication mechanisms, and communication can be conditional rather than continuous. Ouros applies only that architecture-level lesson: world agents share bounded information through explicit paths instead of reading global state.

No particle-filter algorithm or paper-specific scenario is adopted.

### OASIS — Open Agent Social Interaction Simulations with One Million Agents
Public source: camel-ai/oasis GitHub project and associated paper.

High-level lesson: large social simulations require constrained action spaces and scalable interaction selection; agents do not interact uniformly with every other agent. Ouros uses this as support for explicit audience selection and bounded fanout before communication events enter the delivery queue.

Ouros does not adopt OASIS LLM behavior, social-media mechanics, recommendation algorithms or learned population assumptions.

### DASH / SocialSim work
Public source: DASH project, USC Information Sciences Institute.

High-level lesson: large distributed social simulations can model individualized actions from local environment, neighbors and history using discrete-event simulation. This supports keeping recipient choice agent-local and event-driven rather than broadcasting every meaningful event to every NPC.

No trained decision model is imported.

### Tabletop community practice
Public discussions about NPC/faction-heavy campaigns repeatedly emphasize tracking individual NPC state, faction role and specific information learned by each person rather than treating a faction as one character. This is useful as a game-master-facing validation of the same separation already required by Ouros.

The project uses only the general design pattern. No campaign NPC, faction, setting or protected text is imported.

## Transformed Ouros design lesson

Useful communication pressure can be represented as:

```text
relationship relevance
+ institutional reporting duty
+ semantic proximity/contact opportunity
+ topic relevance
+ role relevance
- reachability failure
- audience budget
= explicit recipient candidates
```

This ranking determines contact intent only. It does not establish truth, belief, trust change or automatic delivery.

## Authority notes

No PTU, Caelo or Kairos rule was adopted in this pass.

The weights and thresholds are versioned Ouros simulation policy.

`PUBLIC_SOURCE_PATTERN != OUROS_CANON`

## New narrative opportunities

- a witness tells a trusted friend before contacting officials;
- a professional duty routes a report to a responsible role while unrelated coworkers remain ignorant;
- a rival is deliberately excluded from a warning despite being reachable;
- a courier can contact only a small set of people before leaving;
- an emergency alert can later use a separate explicit broadcast subsystem rather than abusing person-to-person gossip;
- investigations can reconstruct not only who knew a fact, but why a sender chose those particular recipients.
