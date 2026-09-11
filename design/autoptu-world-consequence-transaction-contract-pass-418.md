# AutoPTU world consequence transaction contract — Pass 418

Status: PROPOSED DESIGN CONTRACT. No canon or PTU rule changes.

Purpose

Pass 416 records one admitted semantic result against one durable AutoPTU session. Pass 417 releases world-agent tactical ownership and retires that session in a restart-safe order. Pass 418 adds the next fail-closed boundary: convert an already admitted semantic result into one explicit Ouros consequence transaction without reconstructing hidden tactical state.

Authority

AutoPTU remains authoritative for the semantic result. Ouros may consume only fields named by an explicit mapper. Minecraft/Cobblemon/Craftics presentation does not add, infer or repair result data.

Transaction rules

A mapper declares its own mapper ID, accepted result type, consequence kind, required payload fields and allowed payload fields. A transaction may be committed only when the durable AutoPTU session is RESULT_RECORDED or RETIRED and the supplied result ref exactly matches the session's authoritative result ref.

Any payload field outside the mapper allowlist fails closed. The fixture deliberately demonstrates this with raw tactical-looking fields such as HP and initiative. The implementation does not maintain a universal blacklist because future result schemas may legitimately contain domain-specific fields. Authority comes from the positive mapper allowlist.

The transaction identity derives from session ID, result ref and mapper ID. Exact replay is an idempotent no-op. Reusing that identity with changed provenance or payload is a conflict.

The transaction records provenance and the mapped payload. It does not mutate an NPC, site, relationship, inventory, ecology state or Minecraft entity. Those changes remain owner-specific follow-up executors.

Fixture scope

The regression uses FIELD_OBJECTIVE_OUTCOME as a synthetic NON-CANON fixture result type with objective_ref, outcome and optional evidence_ref. This does not claim that AutoPTU-Java currently emits such a result type. It proves the consequence transaction boundary only.

Capability posture

The reduced bookkeeping fixture uses no tactical mechanic family.

Any production result still inherits the capability requirements of its producing path. Targeting/footprints/range/LoS, base movement legality and core calculations remain verified only inside audited scopes. Complete movement including push/pull/knockback/interception/forced movement remains partial. Action economy/initiative, full turn/round lifecycle, full stateful damage pipeline and status lifecycle remain partial. Terrain/weather/hazards/zones/reactions is mixed/partial/blocking by exact behavior. Move-specific behavior, abilities, items and Trainer Features/perks remain individually gated. AI legal-action infrastructure is verified only for audited actions. AI tactical policy remains blocking for specialized objective policies. Minecraft/Cobblemon/Craftics adapter/playback remains partial/blocking for authoritative tactical objective state and in-flight recovery.

Open questions

The next executor must consume only committed consequence transactions and mutate one named owner system with its own idempotency/provenance contract. Production semantic result types still need exact engine-side schemas. UNKNOWN and EXPLICITLY_ABANDONED authority reports remain separate from normal completion and cannot manufacture a consequence transaction through this path.
