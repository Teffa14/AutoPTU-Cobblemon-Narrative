# Antagonists, Defection, Escalation & Opposition Research — Pass 21

Status: research/provenance only. Nothing in this file is Ouros canon.

Date: 2026-08-19

## Why this pass

The repository already models factions, cases, public memory, rival history, crisis state, actor knowledge and world pulses. It did not yet have a dedicated research layer for persistent opposition: how adversarial actors pursue goals, how organizations split, how members defect, how escalation remains causal, how an enemy can become negotiable, and what happens after a leader is defeated.

This pass therefore studies antagonism as actor agency rather than as a fixed villain label.

## Source observations

### PTU: Tales of Visiwa retrospective

Source: https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

Useful structures:

- Two hostile organizations can pursue incompatible goals simultaneously instead of functioning as one monolithic enemy front.
- Personal PC hooks can pull characters into the same larger conflict from different directions.
- Opposition can exist at several scales: public-facing institutions, covert operations, agents, recurring mid-bosses and supernatural sponsors.
- A confrontation can be resolved partly through persuasion when an adversarial character is being manipulated. The retrospective explicitly describes a major fight whose trajectory changed after the PCs convinced an enemy clone she was being manipulated.
- Enemy attention can scale with player significance. Early mistakes did not trigger maximum retaliation because the PCs were not yet important enough to justify it.
- Environmental identity can coexist with antagonist identity; one remembered confrontation used shallow/heated water as part of the encounter rather than placing the opponent on a neutral arena.

Design lesson: opposition should have goals, knowledge, attention budgets and relationships. A combatant being hostile now does not prove they are permanently irreconcilable.

### PTU: Over There! retrospective

Source: https://pokemontabletop.com/over-there-a-world-war-one-pokemon-campaign-a-retrospective/

Useful structures:

- Two groups introduced as enemies can be forced into cooperation by a larger survival problem.
- Named antagonistic figures can have different alignments toward the same larger conflict: hostile, neutral, allied or persuadable.
- One enemy General was ultimately won over through repeated conversation rather than mandatory defeat.
- An apparent benefactor can later reveal incompatible goals, showing that ally/enemy status is contextual and can change without retconning prior help.
- Opposition can act on the map while ignored: flooding, territorial growth and nightly attacks create visible pressure.

Design lesson: allegiance should be stateful. The system needs room for enemy-mine alliances, changing loyalties and adversaries who remain ideologically distinct after cooperation.

### Official Pokémon: N and Team Plasma

Source: https://www.pokemon.com/us/pokemon-news/celebrate-25-years-of-pokemon-with-memorable-moments-from-the-unova-region

Useful structures:

- A public ideology can contain a legitimate concern while leadership exploits it for a separate hidden purpose.
- A visible leader may not be the real controlling actor.
- A central antagonist-adjacent character can learn that they were manipulated, leave the organization and later oppose the person who controlled it.
- Moral classification can remain ambiguous even when behavior and allegiances are concrete.

Design lesson: faction doctrine, leadership intent and member belief must be separate fields. Defection should update allegiance and knowledge rather than magically rewrite history.

### Official Pokémon animation: Team Plasma and former members

Sources:

- https://www.pokemon.com/us/animation/seasons/16/episode-21-secrets-from-out-of-the-fog
- https://www.pokemon.com/uk/animation/seasons/16/episode-17-saving-braviary

Useful structures:

- Former members can retain some beliefs while rejecting an organization's methods or leadership.
- An adversarial institution can use tracking, research subjects, pursuit and information infrastructure rather than only direct battles.
- A rescue can succeed through decoy, escape and protection objectives without defeating every pursuer.

Design lesson: leaving a faction does not require adopting the player's worldview. Opposition can narrow from ideological conflict to disagreement about methods, or vice versa.

### Fangame: Pokémon Conviction

Discovery source: https://www.eeveeexpo.com/released-games/

Public project description presents several competing groups inside one constrained location, including rival gangs, guards, rebels and state-aligned actors. It advertises reputation changes, optional side quests and multiple outcomes.

Reusable structure:

- A location can contain several adversarial networks with overlapping enemies and services.
- Cooperation with one actor should create opportunity costs or new suspicion elsewhere rather than a universal morality score.
- Constrained geography makes changing control, access and hidden routes legible to players.

No project-specific characters, dialogue, plot sequence or faction names should be imported into Ouros.

### Fangame: Pokémon Supernova

Source: https://www.eeveeexpo.com/threads/8804/

Public description emphasizes school life, faction tension, branching outcomes, affinity, rumors and earlier choices changing later events.

Reusable structure:

- Antagonism may grow out of ordinary institutional relationships before becoming overt conflict.
- Earlier social choices can affect who shares information, who gives the player benefit of the doubt and who becomes an obstacle.

### Fangame: Pokémon Disintegration

Source: https://www.eeveeexpo.com/threads/9339/

Public description combines criminal pursuit, missing memory and choices that can affect regional outcomes.

Reusable structure:

- An antagonist may begin with a concrete grievance or pursuit before the player understands its larger context.
- A player's own incomplete knowledge can create conflict without requiring every opponent to lie.

### Procedural narrative research: CONAN

Source: https://www.sciencedirect.com/science/article/pii/S1875952121000197

The CONAN quest-generation work uses world facts plus character preferences/motivations to generate plans. It highlights a key problem: a causally valid plan can still feel unbelievable if it ignores character motivation.

Reusable principle for Ouros:

Adversarial action selection should require both executable world-state preconditions and an actor-specific reason. "This action would create drama" is not a sufficient motive.

### Interactive narrative: The Best Laid Plans

Source: https://ojs.aaai.org/index.php/AAAI/article/view/9780

The system generates conflict by letting NPCs act against player plans and replanning when circumstances change.

Reusable principle:

Opposition should thwart, adapt or abandon plans based on what actually happens. It should not endlessly repeat the same scripted obstacle after the world state makes that obstacle irrational.

### Continual multi-agent planning

Source: https://ojs.aaai.org/index.php/AAAI/article/view/7567

The research models agents whose beliefs, sentiments, goals and plans can change during a dynamic story world.

Reusable principle:

Antagonist state should distinguish goals, beliefs, knowledge and current plan. Changing one does not necessarily change the others.

### Adversarial planning agents

Source: https://scholars.duke.edu/publication/1681430

The Adversario work centers autonomous adversarial agents with goals that conflict with player goals and derives behavior from a broader social simulation.

Reusable principle:

An adversarial actor should remain embedded in social structure. Resources, obligations, allies, reputation and dependencies constrain what it can do.

## Patterns selected for Ouros design

1. Opposition is a relationship between goals, not a permanent moral type.
2. Faction doctrine, leadership intent, member belief and operational method remain separate.
3. Adversaries receive bounded attention and resources; they do not omnisciently counter every player action.
4. Escalation requires triggers and cost.
5. A defeated leader does not automatically dissolve an organization.
6. Defection updates allegiance, access, knowledge and relationships but does not erase prior actions.
7. Persuasion, surrender, withdrawal, exposure, rescue and temporary alliance are valid narrative resolutions when the mechanical layer supports them.
8. Former enemies may preserve ideological disagreement after ending active hostilities.
9. Internal factions and succession disputes can transform an organization rather than simply delete it.
10. Antagonists must operate from actor knowledge, never direct world truth.

## Copyright boundary

External sources are retained for provenance and abstract design lessons only. Ouros must not copy distinctive faction names, characters, dialogue, exact plots, bespoke mythologies, custom battle mechanics or authored prose from those works.

## PTU/Caelo boundary

The supplied PTU Core Rulebook already recommends weaving central plot and character-focused arcs into ordinary Trainer activity, while keeping meaningful player choice and self-contained session satisfaction. Caelo distinguishes Social, Encounter, Battle, Raid and Job activity, allowing antagonism to appear through several content forms instead of every conflict becoming the same combat.

This pass does not define new Skill DCs, persuasion mechanics, surrender rules, retreat rules, morale, capture legality, Trainer Feature effects, status effects or combat bonuses. Those require exact PTU/Caelo validation and implementation evidence.

## Research gaps for later passes

- Exact PTU/Caelo rules relevant to social conflict, Intimidate/Command/Guile use, surrender and withdrawal.
- Whether Ouros will define formal amnesty, parole, detention, restitution or restorative processes.
- How much off-screen action a hostile faction may take during offline world time.
- Whether players may join or infiltrate adversarial organizations.
- How private faction knowledge is protected in multiplayer.
- How NPC defections persist when the NPC is represented physically in Minecraft.
