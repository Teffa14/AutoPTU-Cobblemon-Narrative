# Engine Readiness Snapshot — Pass 75

Status: implementation evidence snapshot. Not canon.

## Read-only sources inspected

AutoPTU-Java head: `cd67bdb8de7f53d376b7a4c8e8cbb0199095d55f`

AutoPTU Python head: `361cf8e6fa71285b95d91db8218a9cbc32792b3a`

Narrative repo pre-pass head: `25cff7b6598862a2e70279a9f84c28e3669545ef`

Live Java README inspected during Pass 75.

## Java evidence since Pass 74

AutoPTU-Java advanced one additional held-item slice after the Pass 74 snapshot:

- `cd67bdb8de7f53d376b7a4c8e8cbb0199095d55f` — ports held-item START rule-profile extraction/parsing, adds oracle fixtures and parity coverage, and gates the profile against Python.

Pass 74 already recorded the preceding held-item/lifecycle chain:

- `343ff74d068cf42a7db83ad706cff03117a9fbd5` — generic held-item START temporary effects;
- `6beb908f4246eb9f2e94161e3e28e4044be8fa92` — extended generic held-item START calculation-effect families;
- `95134b1d7089520f2e1aad917d38ce1940622318` — server-owned held-item rule catalog boundary;
- `84505214d4bca41610f36f0a178e675ef0ab26ba` — StatusController phase ordering;
- `b1dc29e3beae24f56d1106129cb1fa61db55b069` — phase-envelope dispatcher;
- `87ee4652b8d1d123f6b1180bf4f652053d40cb73` — live lifecycle wiring.

The new profile extraction is useful evidence that held-item START behavior is being decomposed into server-owned, parity-tested contracts rather than embedded ad hoc. It is still one bounded timing family. It does not prove full Item coverage, END/consumption behavior, complete battle state or complete hook registries.

The live Java README still explicitly lists as pending:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move, ability, item, perk and Trainer Feature hook registries;
- semantic battle-event emission and full `BattleSpec -> BattleTranscript` parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Python evidence since Pass 74

AutoPTU Python advanced to `361cf8e6fa71285b95d91db8218a9cbc32792b3a`.

The relevant recent Career work adds a squad-wide development floor so new/reserve Pokémon remain competitively usable, with regression coverage. The previous head already prevented a zero-roster browser softlock.

This is Career progression/robustness evidence. It does not establish a new Java tactical capability family and does not alter the classifications below.

## Permanent capability map

### targeting / footprints / range / LoS

Status: VERIFIED

Java explicitly supports range, areas, footprints, target anchors and line of sight in legal action generation.

### base movement legality

Status: VERIFIED

Shift/Jump legality, Overland/Swim/Sky, terrain costs, blockers, Wallrunner, sprint, water and landing-fit rules are implemented.

This excludes interception and forced displacement.

### complete movement including push / pull / knockback / interception / forced movement

Status: BLOCKING

Forced movement remains explicitly pending in the live Java README. No Pass 75 evidence closes interception or the complete movement family.

### core calculations

Status: VERIFIED

Damage Base, type-effectiveness steps, combat stages, accuracy stages, weather DB calculation primitive, crit probability, Burn, modifiers and rounding primitives remain implemented.

### action economy / initiative

Status: VERIFIED

Typed turn flow, phases, action budget, deterministic initiative, Trick Room/League ordering and declared-action ordering remain implemented.

### full turn / round lifecycle

Status: PARTIAL

The phase envelope is ordered, dispatched and connected to live lifecycle, and held-item START behavior now has multiple parity-tested slices plus profile extraction. Complete battle state, complete status behavior, full registries and transcript parity remain unfinished.

### full stateful damage pipeline

Status: PARTIAL

Calculation primitives exist, but full stateful damage resolution remains explicitly pending.

### status lifecycle

Status: PARTIAL

StatusController phase ownership and some live timing behavior are real. The live README still lists the StatusController as incomplete.

### terrain / weather / hazards / zones / reactions

Status: BLOCKING

Java has terrain-cost movement and a weather DB calculation primitive. It does not have a complete tactical terrain/weather/hazard/zone/reaction lifecycle. Pass 75 must not turn an overcrowded staging site, blocked exit, bad weather or unsafe surface into a PTU mechanical zone unless the exact governing rule/controller is verified.

### move-specific behavior

Status: PARTIAL

Representative rule infrastructure exists. Complete move hook registry coverage remains pending.

### abilities

Status: PARTIAL

Representative calculations do not establish complete Ability behavior. Ability hooks remain incomplete.

### items

Status: PARTIAL

Held-item START behavior has materially stronger live evidence: temporary effects, calculation-effect families, a server-owned rule catalog, and profile extraction/parity. Full item hook coverage, timing, consumption and stateful behavior are not complete.

### Trainer Features / perks

Status: PARTIAL

Previously verified Focused Training/Chronicler Accuracy slices remain bounded examples. The complete feature/perk registry remains pending.

### AI legal-action infrastructure

Status: VERIFIED

Deterministic legal choices exist for Shift, direct targets, SELF/FIELD, tile-aimed AoE, footprints, LoS and action-budget filtering.

### AI tactical policy

Status: BLOCKING

AI scoring/policy remains explicitly pending. Legal actions do not imply policy for WITHDRAW, PROTECT, CLEAR_ROUTE, ESCAPE, territorial behavior or protecting civilians/supplies.

### Minecraft / Cobblemon / Craftics adapter and playback

Status: BLOCKING

AutoPTU-Java remains a rules library that a future adapter will consume. No parity-safe world-state/tactical-playback family is complete.

## Pass 75 encounter consequences

### Volunteer Staging-Site Evacuation

Intended full version requires:

- VERIFIED targeting/footprints/range/LoS;
- VERIFIED base movement;
- BLOCKING complete movement for interception/forced displacement and evacuation-lane interactions;
- VERIFIED core calculations;
- VERIFIED action economy/initiative;
- PARTIAL full turn/round lifecycle;
- PARTIAL full stateful damage;
- PARTIAL status lifecycle;
- BLOCKING terrain/weather/hazards/zones/reactions if unsafe areas change tactically;
- PARTIAL move-specific behavior;
- PARTIAL abilities;
- PARTIAL items;
- PARTIAL Trainer Features/perks;
- VERIFIED AI legal-action infrastructure;
- BLOCKING AI tactical policy for WITHDRAW/PROTECT/CLEAR_ROUTE;
- BLOCKING adapter/playback for helpers, closures, supplies and aid commitments.

Reduced version:

The site closes before battle. Helpers and recipients leave through world state. Community-aid commitments become PAUSED, RELEASED or HANDED_OFF. Exact goods remain with their owner/custodian system outside the tactical grid. AutoPTU resolves a conventional static encounter in the cleared perimeter. The specialist owner system decides reopening; victory does not reactivate the rota automatically.

### Community Cleanup Wildlife Conflict

Intended full version may require complete movement, protected-object/zone semantics, withdrawal or territorial tactical AI, dynamic access and adapter synchronization.

Reduced version:

Cleanup pauses. Helpers and collected materials leave the grid. Public Space/Ecology evaluates route/timing alternatives. If a battle remains necessary, AutoPTU receives a static arena containing only legal combatants. Victory does not establish historical causation for litter, damage or earlier incidents.

### Supply Table Interruption

Intended full version may require civilian withdrawal, protected-object objectives, interception, dynamic access and objective-aware AI.

Reduced version:

Distribution stops before combat. Recipients/helpers and exact batches are removed from tactical state while custody persists under the owning service. A conventional encounter resolves separately. Distribution resumes only after the service validates the site.

### Rota Reconciliation / Six Sign-Ups, Four Actual Helpers

No tactical capability is required.

These scenes use stable aid-need IDs, offers, role reviews, commitments, check-ins, handoffs, withdrawals, notices and communications. They can execute before the Minecraft battle adapter exists.

## Community-aid mechanical boundary

Pass 75 can persist:

- aid needs owned by another system;
- public/private calls for helpers;
- actor offers and availability windows;
- role slots and qualification requirements;
- role-review outcomes;
- temporary commitments;
- check-in and contribution history;
- handoffs;
- withdrawal/release;
- aggregate helper cohorts;
- in-kind contribution references;
- recurring participation history;
- pause/reopen state around tactical incidents.

It cannot itself define or alter:

- PTU Skills, Features, Edges or progression;
- Trainer Classes;
- occupational qualification;
- legal/emergency authority;
- PTU movement or forced movement;
- damage;
- statuses;
- tactical terrain/weather/hazards/zones/reactions;
- Moves or Abilities;
- Item effects;
- Trainer Feature timing;
- initiative/action budgets;
- tactical AI;
- Pokémon work/rescue capability from species/type alone;
- relationships or reputation rewards;
- ownership/custody of contributed goods;
- payment, wages, reimbursements or donation law.

## Promotion decision

No permanent capability category is promoted in Pass 75.

The held-item START profile extraction at `cd67bdb8` strengthens Items and full lifecycle/status evidence, but all three remain PARTIAL because the live README still lists broader state/controllers/hook registries as incomplete.

The Python Career development-floor work does not change battle-engine readiness.

## Open mechanical questions

- What held-item timing families follow the current START profile/rule-catalog work?
- When will item consumption, END timing and complete item hook coverage reach parity?
- When will complete StatusController behavior and full combatant/grid state land?
- When will full stateful damage be authoritative?
- When will interception and other forced movement become authoritative?
- How will PTU terrain, weather lifecycle, hazards, zones and reactions be represented?
- Will BattleSpec/BattleTranscript gain objective semantics such as WITHDRAW, PROTECT, CLEAR_ROUTE and ESCAPE?
- When will AI policy score those objectives?
- How will adapter/playback represent noncombatant withdrawal without Minecraft inventing PTU rules?
- How will world-state role restrictions guarantee that noncombat helpers never enter tactical state accidentally?

Until those questions are answered by contracts/tests, mechanically rich Pass 75 scenes retain reduced implementations.