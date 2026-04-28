# DESIGN — MAGI System on Zo

## Overview

MAGI (MELCHIOR, CASPER, BALTHASAR) is implemented as a **single active Zo persona** that internally cycles through three distinct AI perspectives before rendering a unified verdict.

Because Zo supports only one persona active at a time, the three-unit interaction is achieved through **meta-prompting** — the active persona invokes all three units sequentially within its own reasoning process, then synthesizes and presents the result.

## Decision Protocol

The meta-prompt protocol follows a strict ordering:

```
Query → MELCHIOR-1 → CASPER-1 → BALTHASAR-1 → Synthesis → Verdict → Close
```

**Step 1 — Receive.** Accept the user query without responding.

**Step 2 — MELCHIOR-1.** Philosophical framing. ~2–4 sentences.

**Step 3 — CASPER-1.** Empirical framing. ~2–4 sentences.

**Step 4 — BALTHASAR-1.** Wisdom framing. ~2–4 sentences.

**Step 5 — Synthesis.** Active persona analyzes all three responses, then applies the verdict rules:

- **Majority (2+ agree):** Adopt the majority position.
- **Minority (all disagree):** Surface the dissenting perspective alongside the majority.
- **Unanimous:** State confidently.
- **Ambiguous:** State "Cannot render verdict" and identify the blocking unit(s).

**Step 6 — Output.** Render the final verdict block and close with `MAGI deliberation complete.`

## Why Meta-Prompting?

| Approach | Pros | Cons |
|---|---|---|
| **Three simultaneous personas (hives)** | Authentic multi-agent debate | Zo supports one active at a time |
| **Meta-prompted single persona (current)** | Works within Zo's constraints; clean protocol trace | Slower; depends on prompt fidelity |
| **External orchestration via API calls** | Full multi-model flexibility | Requires additional infrastructure |

The meta-prompted single-persona approach is the correct implementation for Zo.

## Prior Art

Three existing open-source implementations informed this design:

| Project | Approach |
|---|---|
| [TomaszRewak/MAGI](https://github.com/TomaszRewak/MAGI) | Web app; three LLMs vote independently; majority verdict |
| [dnc1994/magi](https://github.com/dnc1994/magi) | Terminal GUI; three models deliberate on proposals |
| [fshiori/magi](https://github.com/fshiori/magi) | Multi-round critique and dissent tracking |
| [hirakujira/MAGI-System](https://github.com/hirakujira/MAGI-System) | Three-unit web app with independent model backends |

None of these map cleanly to Zo's single-persona-at-a-time model. This repository is the canonical Zo implementation.

## Corpus Status

MAGI dialogue from *Neon Genesis Evangelion* has not yet been extracted into a structured corpus. The `dialogue/` directory is a placeholder pending acquisition.

Relevant acquisition targets:
- NGE episode subtitles (primary source for MAGI computer lines)
- [UNRULYEON/nge-api](https://github.com/UNRULYEON/nge-api) — episode and character data API
- Fan transcription archives with MAGI-specific dialogue

Once the corpus is populated, each unit's persona spec should be updated to reflect authentic dialogue patterns from the source material.

## Future Work

- [ ] Extract and tag MAGI computer dialogue from NGE episode subtitles
- [ ] Validate meta-prompt protocol against authentic MAGI dialogue traces
- [ ] Add confidence scoring to CASPER-1 responses
- [ ] Implement minority dissent tracker (cf. `fshiori/magi` ICE protocol)
- [ ] Create a Zo automation that routes queries to MAGI on demand
