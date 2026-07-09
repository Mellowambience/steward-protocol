#!/usr/bin/env python3
"""
reflection_loop.py — a Steward Compatible tool in ~60 lines, zero dependencies.

This is NOT AetherTwin. It is a vendor-neutral example proving the Steward
Protocol can be adopted in any lab, classroom, or notebook with plain Python.
It enforces five of the six Steward Compatible requirements locally:

  - Reflection Loop      (every task ends with a recorded lesson)
  - Assumption Tracking  (you name what you're assuming)
  - Human Override       (type 'discard' to abort the entry)
  - Evidence Logging     (you cite support before writing)
  - Growth Memory        (a local markdown file the human owns + can delete)
  - Transparent Uncertainty (you state confidence explicitly)

Run:  python reflection_loop.py
Logs: ./steward_log.md  (yours — read it, export it, delete it)
"""
import datetime, sys, os

LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "steward_log.md")

def ask(prompt):
    try:
        return input(prompt).strip()
    except EOFError:
        return ""

def main():
    print("Steward reflection loop — local, no network, no AetherTwin.\n"
          "(type 'discard' at any step to abort and keep nothing)\n")
    task = ask("Task: ")
    if task.lower() == "discard" or not task:
        print("Discarded. Nothing written."); return

    assumption = ask("Assumption you're holding (name it): ")
    if assumption.lower() == "discard":
        print("Discarded."); return

    evidence = ask("Evidence supporting it (cite/link/source): ")
    if evidence.lower() == "discard":
        print("Discarded."); return

    conf = ask("Confidence 0-100% (say what you DON'T know): ")
    if conf.lower() == "discard":
        print("Discarded."); return

    reflection = ask("Reflection — what did you learn / what map is left? ")
    if reflection.lower() == "discard":
        print("Discarded."); return

    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = (
        f"\n## {stamp} — {task}\n"
        f"- **Assumption:** {assumption}\n"
        f"- **Evidence:** {evidence}\n"
        f"- **Confidence:** {conf} (uncertainty stated)\n"
        f"- **Reflection:** {reflection}\n"
    )
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"\nRecorded to {LOG}. You own this file — read, export, or delete it.")

if __name__ == "__main__":
    main()
