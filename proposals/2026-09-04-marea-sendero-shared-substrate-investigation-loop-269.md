# Marea / Sendero shared-substrate investigation loop — Pass 269

Status: PROPOSED. No new species, site, resource, behavior or NPC is canonized here.

The player revisits a known microhabitat and sees two already-counted ecological branches using the same physical feature. The first readable layer is simple coexistence. Later observations reveal whether access is actually limited, whether use happens in different time windows, or whether one branch changes the substrate in a way that helps or hinders the other.

The narrative objective is causal interpretation rather than defeating an enemy. An observer can be wrong for plausible reasons: visible crowding can look like competition; earlier occupation can look like ownership; disappearance of one branch can look like recovery. The world ledger keeps those interpretations separate from adjudicated evidence.

A useful sequence is: baseline visit; shared use becomes visible; rumor or first impression assigns a winner; field evidence identifies the actual mechanism or leaves it unresolved; a disturbance or player intervention removes one branch; the player returns and discovers that the remaining branch still needs re-evaluation because neither habitat recovery nor population growth follows automatically.

This can support a conservation, ranger, researcher or resident-facing quest without requiring a new faction. Different NPC roles may expose different observations through the existing knowledge pipeline, but no NPC reads hidden branch state directly.

Reduced implementation: one persistent substrate presentation, two fixture/local branch records, observation packets, a branch closure event and a later revisit. No battle, no damage, no forced movement, no terrain semantics and no AutoPTU handoff.

Mechanically rich implementation: a live contest for access can use targeting/LoS and ordinary movement where verified. Interception, shove, knockback or forced displacement require complete movement. Structured sequencing requires action economy and full lifecycle. Any cover/blocker/hazard/zone/reaction behavior requires the terrain family. Move-, Ability-, Item- or Trainer Feature-driven access effects require those exact families. Autonomous decisions to contest, wait, reroute or yield require AI tactical policy. Persistent damage/status aftermath requires the corresponding stateful pipelines and semantic-result admission.

Design payoff: the same location can tell different stories over time without random spawn churn. One intervention can help one branch, leave another unchanged, or expose a third constraint. Because branch causality is explicit, later ecology can build on the result instead of rewriting the site with a single global score.