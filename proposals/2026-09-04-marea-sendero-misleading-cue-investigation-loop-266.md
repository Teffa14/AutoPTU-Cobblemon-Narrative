# Marea/Sendero misleading-cue investigation loop — Pass 266

Status: PROPOSED narrative/worldbuilding candidate. No cue, altered site, harmful outcome, ecological trap, NPC interpretation or new Pokémon introduced here is canon-approved.

The player can revisit a familiar Sendero observation window after a conspicuous environmental cue appears. Several already-counted Fletchling may be visible using the site. A casual interpretation is that the location became “better” for them. Ouros should preserve that as a hypothesis, not a world fact.

Later observations can complicate the first impression. A local cost signal might appear, activity might change when the cue disappears, or another comparable site might show different outcomes. The central investigation is not “defeat the thing causing the problem”; it is “what evidence actually connects attraction, use and consequence?”

This creates environmental storytelling where NPCs or field notes can disagree for legitimate reasons. One observer can focus on visible concentration. Another can point out that use does not prove benefit. A third can have outcome evidence but no proof that the animals prefer this site over alternatives. The player can improve the evidence through repeated visits without the journal automatically converting ambiguity into certainty.

The strict ecological-trap label remains unavailable until comparative selection and outcome evidence exist. Most early versions of this loop should remain `TRAP_HYPOTHESIS_UNRESOLVED`. That uncertainty is part of the story rather than a missing quest flag.

Reduced implementation: present the cue and already-counted sources, record observations, preserve comparison evidence, and update the public hypothesis state. No autonomous approach needs to be simulated and no AutoPTU handoff occurs.

Full implementation: individual Pokémon can notice, approach, ignore, abandon or contest access based on species, individual history and context. That version requires the exact movement/perception/AI families documented by the Pass 266 contract. Any mechanical hazard or battle aftermath remains under AutoPTU authority.

Longer-term arc potential: the same structure can support misleading artificial light, altered nesting/roost cues, human food subsidies, restored habitat that animals initially avoid, or management interventions that improve apparent habitat while changing hidden outcomes. These are design families only; none are Marea/Sendero canon until separately approved.
