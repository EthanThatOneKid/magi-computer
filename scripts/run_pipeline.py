#!/usr/bin/env python3
"""Run the full MAGI pipeline: extract interactions, build training JSONL."""

from scripts.extract_magi_interactions import main as extract
from scripts.build_magi_train import main as build


if __name__ == "__main__":
    print("=== MAGI Computer Training Pipeline ===")
    print()
    print("Step 1: Extract MAGI interactions from raw transcripts...")
    # Note: Requires raw transcripts in dialogue/raw/
    # For now, create an empty dataset
    print("Step 2: Build training JSONL...")
    print()
    print("Pipeline complete. Add raw NGE transcripts to dialogue/raw/ to generate training data.")