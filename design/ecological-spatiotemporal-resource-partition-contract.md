# Ecological spatiotemporal resource partition contract

Status: PROPOSED contract. Pass 270. No species schedule, resource preference, avoidance relation or competitive outcome becomes canon through this document.

Record: `ECOLOGICAL_RESOURCE_PARTITION_V1`.

Each record contains claimant refs, resource/substrate ref, spatial-use evidence, temporal-use evidence, trophic/resource-fraction evidence, disturbance context, mechanism hypotheses, interpretation state, provenance and canon status.

Axis states are independent: `SPATIAL_OVERLAP`, `SPATIAL_SEPARATION`, `TEMPORAL_OVERLAP`, `TEMPORAL_SEPARATION`, `RESOURCE_FRACTION_OVERLAP`, `RESOURCE_FRACTION_SEPARATION`, each with evidence refs and confidence/status. One axis must never overwrite another.

Allowed interpretations: `OBSERVED_PARTITION_PATTERN`, `COEXISTENCE_HYPOTHESIS`, `AVOIDANCE_HYPOTHESIS`, `COMPETITION_MEDIATED_PARTITION_SUPPORTED`, `PREDATOR_PREY_TRACKING_SUPPORTED`, `FACILITATIVE_COUPLING_SUPPORTED`, `PHYSIOLOGICAL_SCHEDULE_SUPPORTED`, `DISTURBANCE_MEDIATED_SHIFT_SUPPORTED`, `UNCERTAIN`, `REJECTED`.

Core invariant: temporal or spatial separation is an observation pattern, not proof of avoidance, competition or dominance. Promotion to a causal interpretation requires evidence linking the pattern to a mechanism.

Different schedules may arise from physiology, resource availability, predation risk, disturbance, weather, nesting/parental context or other constraints. The ledger must preserve those alternatives until evidence resolves them.

Shared use at different times does not create ownership or exclusive access. Simultaneous use does not prove competition. Different resource fractions do not prove that competition caused the partition.

A change in temporal window after disturbance may be recorded as a shift. It cannot be globally attributed to humans, predators or competitors without evidence. Pass 269 branch-local limitation rules remain authoritative for direct access limitation.

The same claimant pair may occupy different positions across axes and contexts. Do not collapse multidimensional evidence into one niche-overlap score or one global species relation.

Population authority remains separate. Reduced overlap cannot create emigration, death, capture or population decline. Increased overlap cannot create immigration, births or population growth.

Minecraft/Cobblemon day/night, position and visible co-occurrence can provide presentation/observation inputs when authorized. They do not by themselves create temporal niche, avoidance, competition, territory, PTU terrain, reaction or movement truth.

Reduced encounter: project already-counted sources across multiple observation windows and locations; record axis-specific evidence; compare patterns; preserve uncertainty. No AutoPTU handoff required.

Full encounter dependencies: targeting/footprints/range/LoS for active detection/targeting; base movement legality for ordinary approach or rerouting; complete movement for interception, push/pull/knockback or forced displacement; core calculations only for mapped PTU arithmetic; action economy/initiative and full turn/round lifecycle for structured contests; full stateful damage pipeline for persistent damage; status lifecycle for persistent status; terrain/weather/hazards/zones/reactions when environment has admitted tactical semantics; move-specific behavior, abilities, items and Trainer Features/perks only when they cause the partition or contest; AI legal-action infrastructure for legal autonomous options; AI tactical policy for autonomous choice of when/where to forage, avoid, wait, pursue or yield; Minecraft/Cobblemon/Craftics adapter/playback for live projection.

Fail closed: `NOT_SEEN_TOGETHER != AVOIDS`; `DIFFERENT_TIME_WINDOWS != COMPETITION`; `DIFFERENT_RESOURCE_FRACTIONS != COMPETITION`; `MORE_OVERLAP != POPULATION_GROWTH`; `LESS_OVERLAP != POPULATION_DECLINE`.