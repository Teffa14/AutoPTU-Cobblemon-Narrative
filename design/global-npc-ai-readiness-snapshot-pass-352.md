# Global NPC AI readiness snapshot — Pass 352

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-08

## Narrative repository baseline

Narrative main was inspected at `f29478826c2a8decc0bc694bf356e077e505d163` before writing. The full recursive repository tree was inventoried, then the current focus, canon governance, communication owner, deception runtime, allocation-notice owner, Pass 351 regressions, CI workflow and prior research index matches were inspected directly.

Pass 352 preserves terminal communication envelope provenance and allows a later resource-allocation notice audit to validate sender/receiver identity after delivery or restart.

No canon file is modified.

## AutoPTU-Java read-only evidence

Current main inspected: `4ed40a63b40cae0d13998a9997b774f99e1cc678`.

Commit message: `Merge #402: Resolve round-start ability holders from authoritative state`.

The inspected diff adds a server-owned `RoundStartAbilityExecutionContext` and `ActiveAbilityHolderResolver`. The resolver reads `BattleRuntimeState`, filters to active and conscious combatants, checks the exact Ability name, preserves battle insertion order, and is compared against a pinned Python oracle through `ActiveAbilityHolderResolverOracleParityTest`.

The parity workflow now exports active Ability holders from the Python oracle and includes the resolver test alongside round-start Ability dispatch, Arena Trap targeting/effect mutation and Trainer Feature lifecycle parity tests.

GitHub Actions for this head reported 77 workflow runs. Visible runs sampled from the head were completed with `success`.

This is positive evidence for server-owned round-start Ability-holder discovery. It does not establish every round-start Ability behavior, all Ability effects, full round lifecycle semantics, or adapter playback.

## AutoPTU Python read-only evidence

Current main remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its head is still the viewport-coordinate synchronization change whose commit message explicitly states that battle rules and outcomes do not change.

No capability family is promoted from the Python head.

## Permanent capability classification

Targeting/footprints/range/LoS: VERIFIED within ordinary audited contracts. Arena Trap retains additional authoritative candidate-projection evidence.

Base movement legality: VERIFIED within ordinary audited contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Existing movement and Burrow evidence does not establish carrying, physical interception, all forced-movement interactions or cargo behavior.

Core calculations: VERIFIED within audited deterministic arithmetic scope.

Action economy/initiative: VERIFIED for audited primitives. Objective-specific tactical actions such as message handoff, cargo pickup/drop or protected transfer remain individually gated.

Full turn/round lifecycle: PARTIAL. PR #402 strengthens one round-start discovery seam but does not establish the entire lifecycle family.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL. Arena Trap has authoritative status mutation evidence from PR #401, but complete expiration/cleanup and all status interactions remain unverified.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact family.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL. PR #402 adds authoritative active-holder discovery for named Abilities at round start. Arena Trap also has target projection, effect planning and authoritative status mutation evidence. These representative slices do not establish family completeness.

Items: PARTIAL and individually gated.

Trainer Features/perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED within ordinary audited action-generation scope.

AI tactical policy: BLOCKING for non-elimination escort, protect-carrier, preserve-resource, delivery-first, intercept-to-inform and disengage-after-objective goals.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING end-to-end.

## Pass 352 encounter dependency note

The reduced terminal-message audit case needs no AutoPTU battle.

A rich catch-up branch can use verified base movement for ordinary tactical displacement. Physical interception, carrying constraints, push/pull, knockback, rescue or forced movement remain dependent on complete movement. Round-based deadlines depend on full lifecycle. Persistent conditions depend on status lifecycle. Weather, hazards, zones and reactions remain gated by their exact families. Every Move, Ability, Item and Trainer Feature remains individually gated. Non-elimination escort/interception policy remains blocked. Minecraft playback remains separately gated.

## Unresolved engine questions

- Does a later Arena Trap slice prove one-round expiration and cleanup through the authoritative lifecycle owner?
- Are all authoritative movement paths consuming `Slowed` correctly?
- Which round-start Abilities are now wired through the new execution context and holder resolver, and which remain only discoverable?
- What contracts will own cargo, escort and intercept-to-inform objectives without embedding PTU rules in the Minecraft adapter?
- Is status and round-start semantic playback/acknowledgement complete through Minecraft/Cobblemon/Craftics?

## Unresolved narrative/runtime questions

- Should terminal envelope retention eventually have a bounded archival/compaction policy for very long simulations?
- Should the atomic world checkpoint explicitly version terminal transport provenance instead of relying only on the nested information queue snapshot?
- How should UI distinguish transport delivery, actor knowledge history, current recall accessibility and agreement?
- Which newer resource ledgers from Passes 339 and 342–352 should enter the coherent world checkpoint first?
