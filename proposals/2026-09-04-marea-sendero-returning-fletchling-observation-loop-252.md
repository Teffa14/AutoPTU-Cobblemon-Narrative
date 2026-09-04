# Marea Sendero returning-Fletchling observation loop — Pass 252

Status: PROPOSED / NON-CANON
Canon effect: NONE until approved

## Premise

A wild Fletchling from the established lower-Sendero population can become narratively familiar through repeated encounters across real play sessions, chunk unloads and server restarts.

The premise does not require a special tagged bird, a unique cosmetic, a quest flag or a battle. The continuity comes from the same persistent Ouros actor being projected again and from observation history accumulating around it.

## Player-facing loop

First encounter: the player notices a Fletchling using a particular perch or retreat path. The observation is ordinary evidence with normal uncertainty.

Later encounter: after the entity has been unloaded and reconstructed, the same persistent actor can reappear. The notebook may surface a cautious relationship such as `possibly same individual observed previously` when the available evidence supports it.

Stronger longitudinal evidence may come from repeated route choice, temperament, timing, interaction history or an externally approved marker. The UI must not expose `persistent_actor_id` as player knowledge.

A later interaction can change the actor's individual history or avoidance/tolerance pressures while the local population remains 12 unless an explicit demographic event occurs.

## Useful consequences

The wild Pokemon can become a local character without being owned.

A player who repeatedly disturbs the same individual may encounter earlier warning or avoidance behaviour later.

A player who observes without escalating may learn a route, preferred time window or environmental relationship.

An NPC naturalist can compare independent observations without knowing the hidden Ouros ledger.

A disappearance after restart or unload has no narrative meaning by itself. Only world-state evidence can support conclusions such as relocation, injury, capture or emigration.

## Reduced implementation

Use the Pass 252 save/load reconciliation contract. The same persistent actor is restored or freshly rematerialized after release. Record a new observation against existing encounter history. No battle opens.

Mechanical dependency: Minecraft/Cobblemon/Craftics adapter/playback only. AutoPTU tactical categories are not required.

## Rich implementation

If a repeated sighting turns into pursuit or interception, add complete movement and tactical lifecycle dependencies. Autonomous escape choices require AI legal-action infrastructure and AI tactical policy. Terrain/weather/hazards/zones/reactions apply only when they mechanically shape the route. Damage/status, Moves, Abilities, Items and Trainer Features apply only if used.

## Canon questions

No visible physical tag is approved by this proposal.

No distinctive plumage, scar, nickname or guaranteed personality is approved by this proposal.

The exact evidence threshold for player-facing `possible same individual` recognition remains an implementation/design question.

The persistent Fletchling actor and population references are reused from existing repository evidence; this proposal does not create a new population member.
