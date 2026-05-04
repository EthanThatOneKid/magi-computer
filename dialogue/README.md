# MAGI Dialogue Corpus

This directory acts as the storage repository for authentic MAGI computer dialogue sourced from *Neon Genesis Evangelion* episodes, films, and scripts for training the MAGI persona on Zo.

## Directory Structure

```
dialogue/
├── raw/                    # Raw NGE transcript files (.txt)
├── processed/              # Intermediate processed data
└── README.md               # This file
```

## Data Flow

1. **Raw transcripts** go in `raw/` — episode transcripts in plaintext format.
2. **Extracted interactions** → `data/magi_interactions.json` (following our standard schema).
3. **Training JSONL** → `data/magi_computer_train.jsonl`.

## Acquisition & Target Sources

To construct a comprehensive and high-fidelity corpus, gather dialogue from the following primary and secondary sources:

### 1. Raw Subtitles & Episode Scripts (.srt, .vtt, .ass)
- **Episodes 11 & 13**: High concentrations of MAGI terminal interactions and dialogues.
- **The End of Evangelion**: Critical MAGI defensive operations and tactical readouts.
- **Transcripts**: Sourced via [Onizuka's literal transcripts](http://plaza.harmonix.ne.jp/~onizuka/literal/) or [ForeverDreaming transcripts](https://transcripts.foreverdreaming.org/).
- **Method**: Extract lines using standard speaker tags (e.g., `MELCHIOR`, `BALTHASAR`, `CASPER`, `MAGI SYSTEM`, `RITSUKO (translating system text)`).

### 2. API Sources
- **[UNRULYEON/nge-api](https://github.com/UNRULYEON/nge-api)**: Provides structured episode metadata and dialogue traces for the main cast. Combine this with the `Character ID` or keyword filters for "MAGI" or individual unit names.

### 3. Fan Scripts & Transcription Archives
- **Evangelion Wiki / EvaGeeks**: High-quality scene-by-scene script transcriptions of clinical system messages and technical readouts.

## Corpus Structure

Dialogue should be consolidated into a structured JSON file `corpus.json` or `magi_interactions.json` following this schema:

```json
[
  {
    "id": "MAGI-001",
    "source": "Episode 13",
    "unit": "MELCHIOR-1",
    "timestamp": "00:14:22",
    "context": "System diagnostic while analyzing the Angel Ireul's progress.",
    "raw_line": "The analytical algorithms indicate a logical contradiction in the structural code of the simulation bodies."
  }
]
```

## Cleaning and Preprocessing Rules

1. **Isolate system output from operator voice**: Ensure the text strictly represents the output of the MAGI units or direct readouts.
2. **Translate to plain English**: Keep lines in standard English translations for the meta-prompting context.
3. **Strip out non-dialogue tags**: Remove descriptive screen cues (e.g., `[typing sounds]`, `(screaming)`).

## Status

The MAGI dialogue corpus is **pending acquisition**. The `data/magi_interactions.json` and `data/magi_computer_train.jsonl` files will be generated once raw transcripts are available.

Key MAGI system references in source material:
- **Episode 11** — Kozo explains MAGI runs Tokyo-3 via democratic majority rule.
- **Episode 13** — Angel Iruel infiltrates MELCHIOR and BALTHASAR; Ritsuko saves CASPER.
- **Episode 21** — Dr. Akagi names the system after the three wise men.
- **End of Evangelion** — SEELE hacks MAGI; Ritsuko confronts "Mother" in the computer room.
