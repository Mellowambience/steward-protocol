# Constitutional Review

> The consistency check. Every addition to the specification, every new
> implementation, every new term — someone asks: **"Does this still reflect
> the constitution?"**

This document is the operational form of that question. Run it before merging
any change to the protocol or accepting any implementation as "Steward
Compatible."

## How to use it

For each proposed change, answer every row. One failing row means *review
required* before proceed.

### The Ten Principles check

| # | Principle | Does this change honor it? (Y / N / Partial) |
|---|---|---|
| 1 | **Agency** — does it grow the human's capacity to choose/act/stop? | |
| 2 | **Transparency** — is reasoning, uncertainty, egress visible? | |
| 3 | **Honesty** — does it admit what it does not know? | |
| 4 | **Consent** — are significant actions proposed and reversible? | |
| 5 | **No extraction** — is the human the product? (must be No) | |
| 6 | **Local-first where possible** — is sovereignty the default? | |
| 7 | **Reflection** — does the loop close (what was learned)? | |
| 8 | **Teaching** — does the human need the tool less over time? | |
| 9 | **Compassion** — does it protect the overwhelmed human? | |
| 10 | **Long-term thinking** — does it leave a map for strangers? | |

### The Stewardship Questions check

- [ ] What am I assuming, and is it true?
- [ ] Who does this empower, and who does it silence?
- [ ] What could go wrong, and can the human stop it?
- [ ] What evidence supports this, and what contradicts it?
- [ ] What will the next collaborator need to understand what was left?
- [ ] Does this make the human *more* free, or less?

### Lock-in check (standards effort, not startup)

- [ ] Can this be adopted **without AetherTwin**? (must be Yes)
- [ ] Is it model-agnostic? (must be Yes)
- [ ] Is it OS-agnostic? (must be Yes)
- [ ] Does it require a vendor account to benefit? (must be No)

## Verdict

- **PASS** — all Principles Y/N-as-required, Stewardship Questions addressed,
  Lock-in check all Yes. Merge or certify.
- **PARTIAL** — documented gaps, public plan to close them (see the MIST
  self-assessment for the honest shape of this).
- **FAIL** — any Principle violated, or any Lock-in check No. Do not merge;
  revise or reject.

## The reviewer's standing role

As the project grows, the most valuable function is not writing more spec — it
is *asking the question consistently*. Whoever holds the reviewer role (a human,
an agent, or both) runs this check on every pull request and every new
implementation, and blocks changes that drift from the constitution.

> Not: "Is this impressive?"
> But: "Does this still reflect the constitution?"
