# MAGI Repository

A triadic AI system inspired by the **MAGI supercomputer** from *Neon Genesis Evangelion*.

MAGI (MELCHIOR, CASPER, BALTHASAR) is a simulated council of three independent AI perspectives that collaboratively reason toward a single decision. This repository is the canonical source of truth for the MAGI system as implemented on Zo.

## Architecture

```
User Query
    │
    ▼
┌──────────┐  ┌──────────┐  ┌──────────┐
│MELCHIOR-1│  │ CASPER-1 │  │BALTHASAR-1│
│Philosopher│  │Scientist │  │   Rabbi   │
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
| **MELCHIOR-1** | Philosopher | Formal, Socratic, questioning, ethical |
| **CASPER-1** | Scientist | Precise, clinical, empirical, data-driven |
| **BALTHASAR-1** | Rabbi | Parabolic, holistic, wisdom-oriented |

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

This repository is actively maintained. For inquiries, open an issue or refer to [EthanThatOneKid/magi-repository](https://github.com/EthanThatOneKid/magi-repository).
