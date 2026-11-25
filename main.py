"""Describe Your Ex in One Word — the entry "Recalled".

One word, one verdict: an ex recalled like a defective product —
a factory recall. The script validates the word and writes it to
/output/entry.txt.
"""

from pathlib import Path

# The word itself: an ex recalled like a defective product.
WORD = "Recalled"

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 111


def validate(word: str) -> str:
    """Strip and sanity-check the word; raise ValueError on bad input.

    The gate allows 1-111 chars of UTF-8, not only whitespace; the
    entry itself must be exactly one word, so spaces and punctuation
    tricks are refused here too.
    """
    text = word.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"word must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if len(text) > 111:
        raise ValueError(f"word exceeds the 111-char gate, got {len(text)}")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be a single word (no spaces)")
    if not text.isalpha():
        raise ValueError("entry must be letters only (no punctuation tricks)")
    return text


def main() -> None:
    text = validate(WORD)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
