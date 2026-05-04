from __future__ import annotations
import hashlib
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def stable_id(*parts: str) -> str:
    """Generate a stable hex ID from parts."""
    h = hashlib.md5("|".join(parts).encode())
    return h.hexdigest()[:12]


def read_json(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_json(path: Path, data: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def write_jsonl(path: Path, data: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


def top_tokens(text: str, limit: int = 6) -> list[str]:
    """Extract top tokens from text (simple word frequency)."""
    words = text.lower().split()
    freq: dict[str, int] = {}
    for w in words:
        if len(w) > 4:
            freq[w] = freq.get(w, 0) + 1
    return sorted(freq, key=freq.get, reverse=True)[:limit]