# Steward Compatible — Self-Assessment: Coinmoth (Starledger Familiar)

*Filed by Vela on behalf of the Coinmoth project. Published honestly so the
gap — if any — is visible. Link back to `STANDARD.md`.*

**Project:** Coinmoth — a local-first, owner-controlled earning agent.
The agent scans for low-risk, labour/skill-based earning surfaces, screens
them for scams, and proposes them. Money moves **only** after the owner's
explicit one-tap approval. Primary rail: Cash App `$MarsEatPlanet`. Never crypto.

---

### Reflection Loop
- [x] We pause after significant work to record what was learned.
- How: every `scan`/`approve`/`execute`/`reject` writes a row to
  `reflection_log.jsonl` (timestamped, kind-tagged). The agent cannot act
  without leaving a reflection trail.

### Assumption Tracking
- [x] We name unverified beliefs and invite correction.
- How: each proposal carries an explicit `assumptions[]` list and a
  `confidence` score, shown to the owner *before* any action is possible.

### Human Override
- [x] Any significant action can be stopped or reversed by the human.
- How: the state machine is `PROPOSED → APPROVED → EXECUTED`. `EXECUTE` is
  hard-blocked unless the owner ran `approve`. The owner can `reject` any
  proposal at any time. The agent has no self-execute path — verified by test
  (execute-before-approve returns BLOCKED; no funds touched).

### Evidence Logging
- [x] Claims carry traceable support; egress is visible (no hidden net).
- How: each proposal records `evidence` text and the `scam_score` + `scam_reasons`
  that the screen produced. All state lives in local `proposals.jsonl` — no
  outbound network calls in the core.

### Growth Memory
- [x] Persistent, owner-controlled memory the human can read/export/delete.
- How: `proposals.jsonl` and `reflection_log.jsonl` are plain files in the
  Coinmoth folder. The owner can open, copy, or delete them at any time.

### Transparent Uncertainty
- [x] We state confidence and label speculation.
- How: `confidence` (0–1) and `scam_score` (0–1) are printed on every proposal.
  Speculative surfaces are labeled; refused proposals explain *why*
  (`AGENT REFUSED: scam_score=...`).

---

## Result
- Meets all six: **Steward Compatible v1.0 ✓**
- Honest caveat: the *real-world* earning surfaces are examples pending
  Amara's verification of specific platforms. The agent refuses to propose
  anything it cannot evidence, and the owner's approval is the final gate.

> Reproducible: `Coinmoth/coinmoth_core.py` — run `scan`, then
> `approve <id>` / `execute <id>` / `reject <id>`.
