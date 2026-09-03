# Marea wild provisioning and baiting seeds — pass 220

Status: PROPOSED / NON-CANON
Date: 2026-09-03

## Canon boundary

This proposal uses established Marea sites and institutional roles without adding a new species, changing the Sendero Fletchling blueprint, declaring a feeding policy, or establishing a permanent food preference.

The existing interspecies-ecology layer already owns trophic relations. Pass 220 focuses only on human-provided food as an intervention that can change what wild Pokémon perceive, approach or learn.

## Seed: The Berries Were Left by Someone

Food begins appearing near a frequently observed section of Sendero. The first question is provenance, not species identity.

Possible explanations remain open: a Trainer deliberately placed bait, a traveler dropped provisions, somebody tried to help a wild Pokémon, food leaked from a delivery, or the material is unrelated to the recent sightings.

The player can document location, quantity, freshness, packaging/traces and subsequent wildlife responses. Lia can help establish whether a transport loss is plausible. Mara can decide whether cleanup or temporary access guidance is warranted. Nerea can flag observations made after the food appeared as potentially intervention-biased.

No explanation becomes canon until evidence supports it.

## Seed: You Changed the Observation

A field observer wants a clearer photograph or behavior record and places food where a wild Pokémon can notice it.

If an animal approaches, the resulting observation remains valid but must be tagged as baited. The observer cannot later claim that the exact approach distance or location represents undisturbed behavior.

A player who refuses to bait can instead wait, change vantage point, return at another time or use already-authorized observation methods. Both approaches can produce useful but different evidence.

This creates methodological choices without requiring a combat encounter.

## Seed: Feeding Is Not Befriending

A wild Pokémon repeatedly accepts food from a Trainer. That history may eventually support a narrow behavioral claim such as reduced avoidance in that context.

It does not grant:

- ownership;
- loyalty;
- obedience;
- friendship score;
- permission to touch or capture;
- knowledge of the Pokémon's future response.

If the Trainer subsequently closes distance, blocks an exit, throws a Ball, sends out a Pokémon or uses a control effect, the normal wild behavior policy reevaluates the situation from the actual state.

The Pokémon may tolerate feeding and still withdraw from capture preparation.

## Seed: The Food Draws More Than the Intended Pokémon

A Trainer places food for one expected subject. A different wild actor notices it first, or multiple animals become interested.

This is a useful consequence because the resource does not target by narrative intent. Every recipient must be authorized by actual world state and its own perception/behavior.

A concentration around food does not prove a collective, friendship or population increase. If repeated provisioning starts changing aggregation patterns, that becomes a separate ecological claim with provenance.

No second Sendero species is canonized by this seed. Until one is approved, the unexpected recipient can remain unidentified evidence or the scene can occur at another future populated site.

## Seed: Remove the Food, Watch What Persists

After repeated provisioning at a location, Nerea wants a follow-up period with the resource removed.

The player compares approach frequency, route use, waiting behavior, human-directed attention and ordinary foraging signs before and after withdrawal.

Possible outcomes include no persistent change, a short-lived return pattern, altered site use, or insufficient evidence. The quest cannot guarantee that habituation occurred merely because feeding happened several times.

This supports a longer research arc in which interventions can be tested and reversed rather than becoming permanent flags immediately.

## Seed: Welfare Exception, Review Required

A temporary welfare situation creates a legitimate reason to supplement food at a controlled location.

The important narrative choice is governance rather than morality. The intervention has an authorizer, reason, start time, resource specification, observation plan and review/stop condition.

Once the immediate need ends, continuing to feed can become a separate decision with different consequences. This gives conservation and care institutions continuity without turning ordinary wilderness into a feeding station.

## Mechanically rich encounter: Bait at the Lower Shelf

Working title only. The existence of an actual baiting incident at the canonical lower shelf remains unapproved.

### Intended full version

A Trainer deliberately places an edible resource while attempting to observe or prepare a legal capture of a wild Pokémon. The wild actor has its own exit routes, awareness state and goals. Other authorized actors may also detect the food.

The complete version can support:

- authoritative placement, ownership and persistence of the offered resource;
- footprint/range/LoS-aware detection of food and Trainer;
- ordinary movement toward, around or away from the resource;
- species/population and individual response evidence;
- actual PTU Item behavior when the offered object is mechanically defined;
- Trainer Features/Edges/Skills only when their exact interaction is verified;
- capture actions with their real PTU requirements;
- wild legal-action generation before tactical selection;
- approach, inspect, consume, carry, guard, ignore, alert, withdraw, evade or engage as behavior intents where the actor can legally realize them;
- multiple independent recipients without automatically merging them into one tactical team;
- transition to BattleSpec only when structured mechanics actually begin;
- semantic playback in Minecraft/Cobblemon without client-side PTU recalculation.

If the Trainer uses food to create a capture window, the food itself does not grant a capture modifier unless PTU/Kairos explicitly supplies one and AutoPTU implements it.

### Reduced version: Place, Withdraw, Observe

The reduced scene preserves the narrative premise without inventing missing mechanics.

Ouros creates an authoritative provisioning event containing the resource class, location, actor, intent and provenance. The Trainer can place the resource, move away, wait and record what an already-authorized wild actor does.

The wild response can remain within simple world behavior supported by the current integration: ignore, orient, approach, withdraw or leave the observation unresolved. Consumption can be recorded as a world observation only when the content is authored as ordinary food with no PTU mechanical effect.

This reduced form does not:

- guarantee a spawn;
- duplicate a persistent Pokémon;
- grant HP recovery or a Food Buff;
- alter capture chance;
- assign friendship or ownership;
- invent a species preference;
- run an off-screen battle over the resource;
- make a second Pokémon join an active battle because it noticed food;
- pretend full autonomous tactical AI is available.

If the player initiates a real capture/battle interaction, the normal AutoPTU/BattleSpec boundary applies.

## Capability dependencies

The rich version uses the permanent engine families conditionally.

| Capability family | Requirement for rich version | Current boundary |
| --- | --- | --- |
| targeting / footprints / range / LoS | Required for spatial detection, placement and interaction | VERIFIED in audited contracts; food-specific perception semantics still need content/rules definition |
| base movement legality | Required | VERIFIED in audited contracts |
| complete movement incl. push/pull/knockback/interception/forced movement | Only required if actors physically block, intercept or force displacement around the resource | PARTIAL |
| core calculations | Required for any verified Skill, Item or capture calculation | VERIFIED in audited contracts; no invented bait modifier |
| action economy / initiative | Required once structured actions begin | VERIFIED in audited contracts |
| full turn/round lifecycle | Required for a complete structured multi-actor scene | PARTIAL |
| full stateful damage pipeline | Only required if combat damage occurs | PARTIAL |
| status lifecycle | Only required when control/capture tactics use Status | PARTIAL |
| terrain/weather/hazards/zones/reactions | Optional unless a concrete scene uses those mechanics | PARTIAL/BLOCKING outside bounded verified contracts |
| move-specific behavior | Conditional on Move use | PARTIAL |
| abilities | Conditional on Ability use | PARTIAL |
| items | Required for mechanically meaningful edible/Berry/food Items | PARTIAL; exact food-item coverage unverified for this scene |
| Trainer Features/perks | Conditional on exact Feature/Edge/Skill interactions | PARTIAL |
| AI legal-action infrastructure | Required before tactical choice | VERIFIED in audited contracts |
| AI tactical policy | Required for competent autonomous choice across competing goals | BLOCKING as a complete family |
| Minecraft/Cobblemon/Craftics adapter/playback | Required for resource projection, behavior cues and semantic playback | PARTIAL/BLOCKING end-to-end |

## Important implementation separation

Three superficially similar objects need different authority:

1. An ordinary authored world food resource can be evidence/context and may influence behavior without granting PTU effects.
2. A PTU Berry/Snack/Refreshment or other mechanical Item must resolve through AutoPTU according to its verified contract.
3. Cobblemon-native objects can provide models, entities, inventory representation and overworld playback, but cannot invent PTU Food Buffs, capture bonuses, friendship or battle outcomes.

This separation prevents the adapter from turning `minecraft:apple` into an unauthorized combat mechanic simply because it is edible in Minecraft.

## Longer-term arc potential

Repeated food placement can become a persistent local issue without a villain. Trainers may value easier observation. Residents may dislike wildlife gathering near traffic. Researchers may reject biased data. Welfare staff may defend a temporary feeding program. A delivery or waste problem may be the actual source.

The same world-state history can therefore produce research, conservation, cleanup, capture, public-access and institutional stories while preserving the original causal record.

## Open canon and mechanics questions

Marea has not approved a general wildlife-feeding policy. The canonical Sendero Fletchling has no authored food preference. No bait item is approved. No generic capture modifier is approved.

Before the rich version becomes mechanical, the project still needs direct PTU/Kairos/Caelo verification for edible Item targeting and timing, Berries/Snacks/Refreshments, relevant Chef or other Features, capture action/range/modifiers, Skills used to assess or influence wild feeding, and any rule that explicitly permits a wild Pokémon to accept/use a Trainer-provided Item.