#!/usr/bin/env python3
"""Extract MAGI computer interactions from NGE transcripts."""

from __future__ import annotations
import re
import json
from pathlib import Path

# Patterns for MAGI system interactions in NGE
MAGI_SPEAKER_RE = re.compile(
    r"^(MELCHIOR|BALTHASAR|CASPER|MAGI|Computer|voice from MAGI|machine)",
    re.IGNORECASE,
)

MAGI_CONTEXT_RE = re.compile(
    r"\b(magi|melchior|balthasar|casper|super computer|computer system)\b",
    re.IGNORECASE,
)

QUERY_RE = re.compile(
    r"\b(request|query|status|diagnostic|run|execute|access|search|find|locate|"
    r"compute|calculate|analyze|check|confirm|verify|what is|where is|who is|"
    r"how many|how much|what's|where's|who's)\b",
    re.IGNORECASE,
)


def looks_like_query(text: str) -> bool:
    return bool(QUERY_RE.search(text.strip())) or "?" in text


def is_magi_speaker(speaker: str) -> bool:
    return bool(MAGI_SPEAKER_RE.match(speaker.strip()))


def load_transcript_episodes(transcripts_dir: Path) -> dict[str, list[dict]]:
    """Load all transcript files grouped by episode."""
    episodes = {}
    for txt_file in sorted(transcripts_dir.glob("*.txt")):
        episode_id = txt_file.stem
        lines = []
        with open(txt_file, "r", encoding="utf-8", errors="replace") as f:
            for line_num, raw_line in enumerate(f, 1):
                # Try to parse "Speaker: dialogue" format
                match = re.match(r"^([A-Za-z][A-Za-z\s\-']+):\s+(.+)$", raw_line.strip())
                if match:
                    speaker = match.group(1).strip()
                    text = match.group(2).strip()
                    if speaker and text:
                        lines.append({
                            "line_num": line_num,
                            "speaker": speaker,
                            "text": text,
                            "is_magi": is_magi_speaker(speaker),
                        })
        if lines:
            episodes[episode_id] = lines
    return episodes


def extract_interactions(episodes: dict[str, list[dict]]) -> list[dict]:
    """Extract query-response pairs involving MAGI."""
    interactions = []
    for episode_id, lines in episodes.items():
        # Find all MAGI responses
        for i, line in enumerate(lines):
            if not line["is_magi"]:
                continue

            # Look for preceding context to find the query
            cluster = [line]
            j = i - 1
            while j >= 0 and i - j < 4:
                prev = lines[j]
                if prev["is_magi"]:
                    break
                # Include adjacent MAGI lines
                cluster.insert(0, prev)
                j -= 1

            # Find query - first non-MAGI line before the response cluster
            query_text = ""
            query_speaker = ""
            for k in range(i - 1, max(-1, i - 5), -1):
                if k < 0:
                    break
                if not lines[k]["is_magi"]:
                    query_text = lines[k]["text"]
                    query_speaker = lines[k]["speaker"]
                    break

            response_text = " ".join(l["text"] for l in cluster if l["is_magi"])

            interaction = {
                "id": f"magi_{episode_id}_{line['line_num']}",
                "episode": episode_id,
                "speaker": line["speaker"],
                "query_speaker": query_speaker,
                "query_text": query_text,
                "response_text": response_text,
                "response_lines": [l["line_num"] for l in cluster if l["is_magi"]],
                "context": [
                    {"speaker": l["speaker"], "text": l["text"], "line_num": l["line_num"]}
                    for l in cluster
                ],
            }
            interactions.append(interaction)

    return interactions


def main() -> None:
    import sys
    transcripts_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent / "dialogue" / "raw"
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).parent.parent / "data" / "magi_interactions.json"

    print(f"Loading transcripts from {transcripts_dir}...")
    episodes = load_transcript_episodes(transcripts_dir)
    print(f"Loaded {len(episodes)} episodes")

    print("Extracting MAGI interactions...")
    interactions = extract_interactions(episodes)
    print(f"Found {len(interactions)} interactions")

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(interactions, f, indent=2, ensure_ascii=False)

    print(f"Wrote {output_file}")


if __name__ == "__main__":
    main()