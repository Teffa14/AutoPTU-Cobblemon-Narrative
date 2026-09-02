# Pass 206 Research — Minecraft-visible wild encounter loop

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-02

## Why this pass

The current playable implementation already builds Marea Interior, binds persistent NPC identities, projects quests to real locations, and explicitly names Marea ecology / Sendero encounter provisioning as a next implementation step. The missing piece is a concrete contract for turning authoritative encounter content into visible Minecraft wildlife without letting Cobblemon presentation become encounter authority.

This pass deliberately stops producing another broad social-continuity layer. It targets a player-visible loop: leave Puerto Bruma, observe wild Pokemon in Sendero del Vidrio, choose whether to approach/avoid/track them, and hand a legally provisioned encounter to AutoPTU when combat begins.

## Internal project evidence inspected

- `canon/ouros-playable-foundation-v1.md`
  - Sendero del Vidrio encounter table remains explicitly unresolved.
  - `ouros.event.sendero_incident_01` already defines an optional battle handoff and reduced ordinary-battle version.
- `canon/marea-interior-map-resident-network-v2.md`
  - freezes physical Sendero anchors and requires Minecraft presentation entities to remain non-authoritative.
- `implementation/marea-interior-runtime-slice-v2.md`
  - current runtime already builds the route and ends its next-sequence list with ecology / Sendero encounter tables through AutoPTU-owned encounter provisioning.
- Existing research/design inventory was checked for a dedicated visible-wild spawn/provision contract. None was found through repository code search.

## Caelo source extraction

Caelo is used here as a pattern library, not binding Ouros canon.

### Encounter request structure

Caelo Player's Guide 1.5 states that wild Pokemon can be encountered in numerous places, distinguishes Morning / Day / Night encounter requests, and allows either a specific search or random encounter generation.

Reusable lesson:

`location + time window + player intent -> candidate encounter`

Do not import Discord thread quotas, Judge workflow, significance modifiers, reward multipliers, or Caelo-specific encounter frequency into Ouros automatically.

### Tracking

Caelo allows locating a specific Pokemon through Survival or Perception based on rarity/frequency and treats searching as an Extended Action with further attempts requiring Bait.

Reusable lesson:

Minecraft should expose deliberate hunt intent separately from ambient visible populations. PTU/Caelo adjudication remains authoritative for the actual check and any frequency limit selected by the active rules profile.

Do not invent a Minecraft-only tracking skill or let minimap visibility bypass the PTU check.

### Encounter table shape

`Caelo Region Location & Encounter List` repeatedly uses fields equivalent to:

- Pokemon;
- Times;
- Rarity;
- Levels;
- Behavior;
- Details.

The strongest reusable feature is the Behavior/Details column. Wild Pokemon are described as actors with territoriality, fleeing, hoarding, rivalry, time-of-day activity, urban adaptation and other ecological hooks rather than as weights alone.

Reusable Ouros data model:

`species pool + temporal window + relative frequency + legal level source + observable behavior tags + ecology notes`

No Caelo species table is copied wholesale into Marea.

## Public-source research

### Wilds of Kanto / overworld-spawn-mod

Source: https://github.com/YoDrehDenSwagAuf/overworld-spawn-mod

The mod reads the existing authoritative encounter table and projects tangible wild Pokemon into encounter regions. Species/level remain sourced from the real map table. It separates presentation behavior into Idle, Wander, Aggressive and Hidden. Contact can begin a battle with that exact projected individual. Story progress, position and warps remain untouched.

Reusable lessons:

1. The visible entity should be a projection of a pre-provisioned encounter identity, not a new random roll on contact.
2. Spawn density should belong to a bounded encounter region rather than arbitrary radius-around-player spam.
3. Behavior presentation can be richer than battle policy while still remaining non-authoritative.
4. Hidden encounters can exist through environmental tells instead of invisible random dice.
5. A fail-safe battle path can exist while presentation matures, provided it still asks encounter authority for the actual combatant.

### PokeWilds

Source: https://www.pokewilds.com/

The project combines open-world exploration, visible partner Pokemon, day/night and weather, resource gathering and field abilities. The useful design lesson is that creature presence and field utility become part of navigation rather than being isolated behind battle menus.

Reusable lesson for Ouros:

PTU Capabilities should eventually influence traversal and interaction in the physical world, but field presentation must query the active PTU rules profile instead of granting generic Minecraft powers based only on type/species.

### Pokemon Sword/Shield Wild Area encounter structure

Source reviewed: https://marriland.com/sword-shield/walkthrough/wild-area/bridge-field/

Visible encounter pools change by weather and carry species, level and rarity information.

Reusable lesson:

World condition should select among authored encounter contexts rather than continuously rerolling individual mobs. Ouros can later attach weather/season predicates to a population profile, but only after those state systems and relevant PTU consequences are authoritative.

### Pokemon Living World

Source: https://www.pokeliving.com/

The project presents persistent NPC/world simulation and ecological population change while the player is absent. It is useful as a product-direction reference, not as authority or a proven PTU implementation.

Reusable lesson:

Wild-population history may persist beyond one session, but Ouros should begin with deterministic bounded population state and provenance before attempting autonomous ecosystem simulation.

## PTU rules cross-check

PTU Core establishes that Skills can alter how Trainers deal with wild Pokemon rather than every encounter becoming combat. Core examples include Intimidate to scare wild Pokemon away, Guile to trick/distract a hostile wild Pokemon, and Charm to improve disposition and potentially prevent conflict or seek help/resources.

Therefore the visible encounter loop must preserve an interaction gate before BattleSpec creation. `wild entity touched` cannot mean `battle mandatory` in every case.

Core also provides special Capabilities such as Naturewalk, Pack Mon, Glow, Darkvision and Groundshaper whose effects can matter to exploration or encounter context. Their existence is evidence for future field integration, not permission for the Minecraft adapter to independently reproduce their mechanics.

## Derived design rules for Ouros

### Encounter identity must exist before contact

A visible wild projection receives an `encounter_actor_id` issued by authoritative encounter provisioning. The Cobblemon entity stores only a binding token plus presentation state.

If the entity unloads and returns, it should rebind to the same live encounter identity when the authoritative window remains active.

### Presentation behavior is not tactical AI

Allowed pre-battle presentation examples:

- idle;
- graze/forage animation;
- bounded wander;
- flee from proximity;
- territorial warning;
- curiosity/approach;
- hidden environmental tell.

These tags may control Minecraft locomotion and animation. They do not determine PTU legal moves, target choice, Initiative, damage, status or battle victory.

### Player contact has a gate

Contact/interact produces one of several server-owned intents:

- observe;
- approach;
- attempt PTU-governed social/field interaction;
- attempt tracking continuation;
- initiate capture/combat path when legally applicable;
- disengage.

A hostile/aggressive presentation may request an encounter escalation, but authoritative rules still determine BattleSpec and participants.

### Ambient populations and deliberate tracking are separate

Ambient populations answer: `what is visibly present here now?`

Tracking answers: `can this Trainer deliberately locate a requested species under the active rules profile?`

A successful tracking result may ask the population authority to instantiate a matching encounter candidate. A visible ambient Pokemon does not retroactively count as a successful tracking check unless the active rules profile explicitly says so.

### Never spawn from species alone

A species entry is insufficient. Provisioning must resolve at least:

- encounter actor identity;
- source population/profile;
- species/form;
- legal level;
- battle build seed or authoritative build request reference;
- disposition/behavior presentation tag;
- spawn region;
- temporal/context predicates;
- capture eligibility or special encounter flags when known;
- provenance/version of the profile used.

## Proposed Sendero use without canonizing a table

This pass does not choose Sendero species. Instead it defines the first authoring requirement for a future `ouros.marea.sendero_vidrio.population.v1` profile.

The profile must contain at least three ecological roles so the route reads as habitat rather than a loot table:

- ordinary visible resident;
- avoidant/hidden resident;
- territorial or context-reactive resident.

The actual species must be selected in a separate canon/content approval pass using Pokédex habitat/capability data, Marea environmental facts and desired early-game PTU difficulty.

## Rejected imports

Do not import automatically:

- Caelo once-per-day encounter quotas;
- Discord thread tags;
- Judge staffing workflow;
- Caelo significance multipliers;
- Caelo exact species/levels;
- Sword/Shield weather tables;
- PokeWilds crafting/survival rules;
- any mod's aggro radius or spawn-count constants;
- random overworld levels generated by Cobblemon.

## Product criterion

A successful implementation of this research is visible to a player without opening documentation:

1. walk from Puerto Bruma onto Sendero del Vidrio;
2. encounter a bounded, authored wild population projected into the actual world;
3. identify different pre-battle behaviors;
4. choose to avoid, observe, interact or engage;
5. when battle begins, fight the same authoritative individual that was visible in the world;
6. return from battle and see the world projection reconciled with the result.
