# Example: The Steward Protocol in a Research Lab

This example proves the protocol travels. It uses **no AetherTwin, no cloud,
no account** — just standard Python any lab already has.

## The scenario

A researcher runs experiments. Before each significant result, they run a tiny
reflection loop that forces them to name assumptions, cite evidence, state
confidence, and record what was learned. The output is a local markdown file
they own.

## The tool

[`reflection_loop.py`](reflection_loop.py) — ~60 lines, zero dependencies.

Run it:

```bash
python reflection_loop.py
```

It walks through five prompts. At any step, typing `discard` aborts and writes
nothing — that is **Human Override** in practice.

### What it enforces (Steward Compatible map)

| Requirement | How this example meets it |
|---|---|
| Reflection Loop | Every task ends by appending a lesson to `steward_log.md` |
| Assumption Tracking | The "name your assumption" prompt, before action |
| Human Override | `discard` at any step; nothing is written without consent |
| Evidence Logging | The "cite your evidence" prompt, recorded with the entry |
| Growth Memory | `steward_log.md` is local, readable, exportable, deletable |
| Transparent Uncertainty | Explicit confidence prompt; speculation labeled |

## Why this matters

A lab can adopt the Steward Protocol **without buying anything or joining
anything**. The same shape works in a classroom (reflection on student work),
a nonprofit (decision logs), or a company (post-mortems). The protocol is the
part that spreads; the tools are local.

## The Constitutional Review on this example

Run against [`review/CONSTITUTIONAL_REVIEW.md`](../review/CONSTITUTIONAL_REVIEW.md):

- **Agency** — Y (human types every field; can discard)
- **Transparency** — Y (reasoning recorded in plain markdown)
- **Honesty** — Y (confidence prompt forces uncertainty out)
- **Consent** — Y (nothing written until the end; discard available)
- **No extraction** — Y (no network, no telemetry, file is yours)
- **Local-first** — Y (runs on the researcher's machine)
- **Reflection** — Y (that is the whole tool)
- **Teaching** — Y (the log makes the human reason better over time)
- **Compassion** — Partial (a CLI is not gentle UX — acceptable for a lab)
- **Long-term thinking** — Y (the log is a map for the next reader)

**Lock-in check:** adoptable without AetherTwin? **Yes.** Model-agnostic?
**Yes** (no model). OS-agnostic? **Yes** (stdlib Python). Vendor account?
**No.**

**Verdict: PASS** (one Partial on Compassion, which is honest and noted).
This is exactly the shape the MIST self-assessment took — gaps shown, not hidden.
