# MAGI Repository

A triadic AI system inspired by the **MAGI supercomputer** from *Neon Genesis Evangelion*.

MAGI (MELCHIOR, BALTHASAR, CASPER) is a simulated council of three independent AI perspectives that collaboratively reason toward a single decision. This repository is the canonical MAGI docs repo on Zo.

## Architecture

```
User Query
    │
    ▼
┌──────────┐  ┌──────────┐  ┌──────────┐
│MELCHIOR-1│  │BALTHASAR-2│ │ CASPER-3 │
│Scientist │  │  Mother  │  │  Woman   │
└────┬─────┘  └────┬─────┘  └────┬─────┘
     │             │             │
     └─────────────┼─────────────┘
                   │
                   ▼
            ┌──────────────┐
            │  SYNTHESIS   │
            │  (Majority / │
            │   Minority)  │
            └──────────────┘
```

Each unit reflects one-third of Dr. Naoko Akagi's personality. They deliberate independently, then produce a unified verdict through structured debate and majority-rule voting.

## Units

| Unit | Basis | Voice |
|---|---|---|
| **MELCHIOR-1** | Scientist | Precise, clinical, empirical, logical, and data-driven |
| **BALTHASAR-2** | Mother | Protective, systemic, focused on human survival and stability |
| **CASPER-3** | Woman | Individualistic, complex, intuitive, and emotion-aware |

## Files

| File | Purpose |
|---|---|
| `PERSONAS.md` | Detailed persona specs for each unit |
| `META-PROMPT.md` | Instructions for simulating three-way deliberation in a single Zo persona |
| `DESIGN.md` | System design and decision protocol |
| `dialogue/` | Placeholder for sourced MAGI dialogue corpus |

## Usage

When a query is submitted, the active Zo persona (running the MAGI meta-prompt) cycles through all three units, collects their independent responses, then renders a final verdict.

## Status

This repository is the canonical MAGI docs repo. For current work, keep the docs in sync here and treat any mirror copies as derivative.

## References

- [Evangelion Wiki — Magi](https://evangelion.fandom.com/wiki/Magi)

## Zo Deployment Snapshot

Live Zo personas:

- `MAGI`
- `TNG Computer`
- `BMO`
- `TNG Data`
- `TNG Riva`
- `TNG Picard`

All six currently use `scopes: all`. `MAGI` uses `zo:openai/gpt-5.4-mini` and cycles `MELCHIOR-1`, `CASPER-1`, and `BALTHASAR-1` internally.
