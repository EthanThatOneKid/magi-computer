#!/usr/bin/env python3
"""Build MAGI training JSONL from interactions dataset."""

from __future__ import annotations
import json
from pathlib import Path


def build_magi_records(interactions: list[dict]) -> list[dict]:
    """Convert MAGI interactions into training records."""
    rows = []
    for interaction in interactions:
        if not interaction.get("response_text"):
            continue

        # Build context from preceding non-MAGI speakers
        context_parts = []
        if interaction.get("query_speaker") and interaction.get("query_text"):
            context_parts.append(f"{interaction['query_speaker']}: {interaction['query_text']}")

        # Include context lines if available
        for ctx in interaction.get("context", []):
            if ctx.get("speaker") and ctx.get("text") and not ctx.get("is_magi", False):
                context_parts.append(f"{ctx['speaker']}: {ctx['text']}")

        context_text = "\n".join(context_parts[-3:])  # Last 3 context lines

        # Format response with MAGI unit attribution
        response = interaction["response_text"]
        speaker = interaction.get("speaker", "MAGI")
        if speaker.upper() in ("MELCHIOR", "BALTHASAR", "CASPER"):
            response = f"{speaker}: {response}"

        row = {
            "id": interaction["id"],
            "messages": [
                {"role": "user", "content": context_text or "Query the MAGI system."},
                {"role": "assistant", "content": response},
            ],
            "metadata": {
                "speaker": speaker,
                "query_speaker": interaction.get("query_speaker", ""),
                "episode": interaction.get("episode", ""),
            },
        }
        rows.append(row)
    return rows


def main() -> None:
    import sys
    input_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent / "data" / "magi_interactions.json"
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).parent.parent / "data" / "magi_computer_train.jsonl"

    with open(input_file, "r", encoding="utf-8") as f:
        interactions = json.load(f)

    print(f"Loaded {len(interactions)} interactions from {input_file}")

    records = build_magi_records(interactions)
    print(f"Built {len(records)} training records")

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Wrote {output_file}")


if __name__ == "__main__":
    main()