# MAGI Dialogue Corpus

This directory stores raw transcripts and extracted MAGI computer interactions for training the MAGI persona on Zo.

## Directory Structure

```
dialogue/
├── raw/                    # Raw NGE transcript files (.txt)
├── processed/              # Intermediate processed data
└── README.md               # This file
```

## Data Flow

1. **Raw transcripts** go in `raw/` — episode transcripts in plaintext format
2. **Extracted interactions** → `data/magi_interactions.json`
3. **Training JSONL** → `data/magi_computer_train.jsonl`

## Acquisition

Sources for NGE episode transcripts:
- http://plaza.harmonix.ne.jp/~onizuka/literal/ (individual episode scripts)
- https://transcripts.foreverdreaming.org/ (forum-based transcripts)
- https://github.com/UNRULYEON/nge-api (structured Evangelion data API)

## Status

The MAGI dialogue corpus is **pending acquisition**. The `data/magi_interactions.json` and `data/magi_computer_train.jsonl` files will be generated once raw transcripts are available.

Key MAGI system references in source material:
- **Episode 11** — Kozo explains MAGI runs Tokyo-3 via democratic majority rule
- **Episode 13** — Angel Iruel infiltrates MELCHIOR and BALTHASAR; Ritsuko saves CASPER
- **Episode 21** — Dr. Akagi names the system after the three wise men
- **End of Evangelion** — SEELE hacks MAGI; Ritsuko confronts "Mother" in the computer room