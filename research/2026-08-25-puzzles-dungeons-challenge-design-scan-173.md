# Puzzles, Dungeons & Challenge Design Scan — Pass 173

Status: RESEARCH / PROVENANCE / NON-CANON
Date: 2026-08-25

## Why this pass exists

The repository tree was audited before writing. Searches for `puzzle` and `dungeon` returned no dedicated design authority, while many existing layers already own the physical and institutional pieces that a puzzle may use: Architecture owns structures and revisions; Material Culture owns persistent objects; Digital Systems owns digital state; Languages owns text and translation; Archaeology owns archaeological context; Wayfinding owns route guidance; Battle Institutions owns battle institutions; Credentials owns scoped access; Cases/Science own evidence and interpretation; Accessibility owns accommodation and access requirements.

The remaining gap is the persistent challenge state itself: how an authored mechanism exposes information, receives attempts, changes state, supports multiple valid solutions, resets, degrades, gains alternate routes and hands off to battle without making Minecraft or the battle engine invent the puzzle rules.

This research therefore proposes a dedicated puzzle/challenge authority rather than adding puzzle logic to Architecture, Minecraft blocks or AutoPTU.

## Source scan

### Pokémon Sword/Shield — Nessa Gym Mission

Source: Pokémon official E3 demo article, “We Battle Nessa and Her Dynamax Pokémon in the Pokémon Sword and Pokémon Shield Demo at E3.”
URL: https://www.pokemon.com/us/news/we-battle-nessa-and-her-dynamax-pokemon-in-the-pokemon-sword-and-pokemon-shield-demo-at-e3

The official description gives a clean state-machine puzzle: colored water flows block paths; color-coded switches alter those flows; the player must change them in a workable order to reach the end. Trainers are embedded along the route, but the puzzle and the battles remain distinct steps.

Reusable structure for Ouros:

`visible obstacle -> legible control -> persistent state change -> newly reachable route -> optional battle -> further state change -> exit`

Important design lesson: the challenge is understandable from the world. Its rule vocabulary is small. It does not require the player to guess an arbitrary hidden interaction verb.

Do not copy Nessa, the pipe layout, switch sequence, Gym or Galar location into Ouros.

### Pokémon Sword/Shield — Gym Challenge as institution

Source: official Sword/Shield website, “Strive to become the next Champion of the Galar region!”
URL: https://swordshield.pokemon.com/en-us/story/strive-to-become-next-champion/

The Gym Challenge is an institutional journey with endorsement, uniforms, Badges and public competition. The relevant high-level lesson is that an individual challenge can be embedded inside a larger institution without becoming the institution itself.

For Ouros, a Gym, academy, festival, museum, research station or civic institution may own a challenge program. The puzzle layer should record the challenge instance and its state while Credentials/Battle Institutions keep authority over eligibility and official outcomes.

### Pokémon Legends: Arceus — temple reached through a difficult route

Source: official Pokémon Legends: Arceus story page.
URL: https://legends.arceus.pokemon.com/en-ca/story/

The official page describes an ancient temple at Mount Coronet reachable only after conquering a difficult path. The useful design structure is spatial escalation: route mastery and place knowledge can make reaching a significant interior part of the challenge before any chamber puzzle begins.

For Ouros, dungeon identity can include approach, threshold, internal mechanisms and exit as separate nodes. A “dungeon” does not have to be one battle map.

### PTU community — Gym challenges should express theme or character

Source: r/PokemonTabletop, “How to handle Gyms,” 30 April 2022.
URL: https://www.reddit.com/r/PokemonTabletop/comments/ufhsgn

Suggestions in the thread include qualifying challenges, races, forest searches and dungeon-like Gym approaches. One particularly reusable recommendation is to build the pre-Gym adventure around what the Leader does outside Gym leadership. This makes the challenge reveal character and local life instead of serving as an arbitrary lock before the battle.

Transformed Ouros lesson: authored challenges should expose a place, institution, profession, ecological relationship or local history. A puzzle whose only identity is “match four colors” should be rare unless that abstraction has a clear in-world reason.

### PTU community — keep tabletop puzzles simple and adaptable

Source: r/PokemonTabletop, “Gym Puzzles/Trials and Evil Team Bases,” 15 June 2021.
URL: https://www.reddit.com/r/PokemonTabletop/comments/o0ohw0

The thread repeatedly recommends simple themed challenges. Other contributors describe turning environmental movement and battlefield features into challenge structure. Some examples rely on custom damage or terrain rules; those are inspiration only and cannot be imported mechanically into Ouros without engine support.

Reusable lesson: complexity should come from combining clear elements and consequences, not from hiding the rule vocabulary.

### PTU community — citywide clue challenge

Source: r/PokemonTabletop, “Need Ideas for Gym Challenge,” 30 July 2021.
URL: https://www.reddit.com/r/PokemonTabletop/comments/oumebr

The proposed structure distributes clues around a city and allows prior challengers/NPCs to provide partial guidance. The useful abstraction is that a challenge can span multiple world nodes and can change between attempts.

Ouros can therefore version a challenge route without rewriting old attempts. A former participant may know revision 3 while the current challenge uses revision 5.

### PTU community — evaluation can measure an objective other than winning

Source: r/PokemonTabletop, “Advice to gm ptu,” 1 July 2025.
URL: https://www.reddit.com/r/PokemonTabletop/comments/1lp99hf/advice_to_gm_ptu/

A community example proposes a Gym where a challenger succeeds by lasting a required number of rounds rather than defeating the opponent. This is not adopted as a universal rule, but it reinforces a valuable separation: battle result and challenge success condition may differ if the institution explicitly defines them that way.

### PTU community — riddles can evaluate justification instead of one secret answer

Source: r/PokemonTabletop, “Psychic Gym Challenge help,” 10 March 2023.
URL: https://www.reddit.com/r/PokemonTabletop/comments/11nh2xs

One suggestion reframes philosophical riddles around justifying an answer instead of guessing a single intended response. The reusable lesson is that some challenges can be adjudicative rather than mechanical: the state stores the response, reasoning and evaluator decision instead of a hidden “correct string.”

### Pokémon Reborn community — high puzzle density can become external-note work

Source: Reborn Evolved forum, “Radomus 4th block puzzle in Victory road (solution),” 23 April 2022.
URL: https://www.rebornevo.com/forums/topic/60412-radomus-4th-block-puzzle-in-victory-road-solution/

A player reports spending roughly two hours and using a large sheet of notes. Another forum request about a related postgame puzzle asks for an explanation and eventually requests a solution because the mechanism remains unclear.
URL: https://www.rebornevo.com/forums/topic/60614-help-with-puzzle-postgame-spoilers-solved/

These are community reactions, not objective design verdicts. They are still useful as an anti-pattern signal: complexity can exceed the amount of state a player can comfortably hold in working memory. Ouros should support notebooks, persistent clue records, visible mechanism history and alternate routes instead of requiring external notes for ordinary progression.

### The Alexandrian — remove chokepoints and provide redundant routes

Source: Justin Alexander, “Three Clue Rule,” 8 May 2008.
URL: https://thealexandrian.net/wordpress/1118/roleplaying-games/three-clue-rule

The central reusable principle is redundancy around required conclusions and required progress. A single clue or one exact deduction creates a brittle chokepoint. The article also extends the idea beyond mysteries: important obstacles should have multiple possible routes or solutions, and the GM should remain receptive to player-generated approaches.

Ouros adaptation:

- critical progression should rarely depend on one obscure interaction;
- important conclusions should have several independent clue paths;
- essential doors should have authored alternatives, later bypasses, institutional help or fail-forward state;
- clever emergent solutions can be accepted through an explicit adjudication record rather than rewritten into the original puzzle definition.

This is a design heuristic, not a PTU rule.

## Synthesis for Ouros

### 1. Puzzle truth must live outside Minecraft

A block, lever, redstone circuit, pressure plate or entity can present a mechanism. The authoritative challenge state must remain in project world state. Otherwise chunk reloads, block edits, lag, mods or client assumptions can silently alter the solution.

Desired direction:

`authored challenge definition -> world-state instance -> legal interaction request -> state transition -> presentation event -> Minecraft representation`

Never:

`redstone happened -> therefore canonical puzzle solved`

### 2. Puzzle state and player knowledge are separate

A mechanism may physically be in state `B`, while one party member believes it remains in `A`. A previous visitor may have recorded an old revision. A translated inscription may be inaccurate. The layer should keep physical state, clue state and actor knowledge separate.

### 3. A solution is a validated route through constraints

Avoid hard-coding one input sequence as the only concept of correctness unless that is truly the authored device. Challenges may accept multiple routes:

- manipulate the intended controls;
- restore a damaged mechanism;
- locate another entrance;
- obtain permission from the institution maintaining the site;
- use a documented Pokémon Capability when the rules source actually supports it;
- perform a valid Skill-based workaround where the challenge explicitly permits one;
- wait for a timed state change;
- discover that the obstacle can be left unresolved because the quest has another node.

### 4. Failure should produce state

Useful outcomes include:

- mechanism unchanged;
- partial progress retained;
- clue revealed;
- alternate route opened;
- time advanced;
- access temporarily suspended;
- evaluator records an unsuccessful attempt;
- maintenance is required;
- battle or social complication begins;
- challenge remains unresolved but the story can continue elsewhere.

Failure should rarely delete the run or trap the campaign behind a permanent softlock.

### 5. Reset semantics must be explicit

Some mechanisms reset after each attempt. Others remain changed for years. A Gym may deliberately reset between challengers while a ruined lock remains open forever after restoration. Reset behavior belongs to the challenge definition and its institution/history.

### 6. Accessibility alternatives belong in the authored challenge

An obstacle based on color, audio, rapid input, spatial memory, fine motor control or a specific physical route can create accidental exclusion. The challenge definition should be able to specify alternate presentations or equivalent routes without pretending the physical original never existed.

### 7. Battle can be one node without becoming the puzzle authority

A battle may guard a route, power a mechanism through an authored post-battle action, test an institutional criterion or interrupt a puzzle attempt. AutoPTU resolves only PTU combat. Challenge state consumes the authoritative battle result afterward and decides whether that result satisfies a challenge condition.

The adapter must never infer “enemy defeated -> door opens” unless the challenge contract says so.

## PTU / project mechanical cross-check

The accessible project corpus includes a Creative Action implementation whose own recorded rulebook basis references PTU Core sections for abilities/capabilities/skill checks as combat actions, capability limits and complex stunts involving Focus alongside another Skill. This is evidence that PTU supports adjudicated creative actions; it is not a generic puzzle-solving engine.

The project also exposes canonical Skills, Features, Capabilities and Items. Their presence never authorizes an invented puzzle bonus. A challenge may reference an exact canonical requirement only after the relevant rules text/source has been validated.

No reliable primary Caelo source was recovered in this run for a universal puzzle, trap, lock, riddle, dungeon or environmental-interaction procedure. No Caelo DC, automatic bypass, trap damage or challenge reward is invented.

Super PTU Online Helper was not available as an invocable runtime capability.

## Engine implications

A noncombat challenge can exist entirely outside AutoPTU.

A challenge that transitions into an ordinary static battle can use current verified ordinary targeting, movement legality, calculations, initiative/action economy and legal-action generation while respecting all PARTIAL families actually invoked.

A challenge-battle hybrid requiring moving platforms, knockback into mechanisms, pressure-plate zones, environmental damage, real-time switches, reaction windows, escorted actors or objective-aware movement still depends on the exact incomplete families: complete movement; terrain/weather/hazards/zones/reactions; relevant Move/Ability/Item/Trainer Feature semantics; AI tactical policy; and adapter/playback.

Recent Java work on generic Move Special secondary Status execution is strong evidence for that narrow path only. It does not establish puzzle mechanisms, environmental Status, generic triggers, arbitrary switches, dungeon traps or an adapter.

## Research conclusion

A dedicated challenge-state layer adds a missing narrative primitive to Ouros. It can support Gyms, ruins, museums, laboratories, civic tests, festivals, caves, dungeons, archaeological sites and player-built institutions without moving rules into Minecraft.

Its most important design commitments should be persistence, explicit authority, multiple progress paths, fail-forward state, versioned clues, accessibility and clean battle handoffs.

No source above is adopted wholesale. All Ouros examples in the associated proposal file are original, NON-CANON candidates.