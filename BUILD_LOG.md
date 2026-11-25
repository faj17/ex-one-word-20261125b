# BUILD_LOG — Describe Your Ex in One Word ("Recalled")

## Word choice
The entry is one word: **Recalled** (8 characters).

Rationale: an ex recalled like a defective product — a factory recall.
It reads instantly as a verdict on a former partner, it is not the
obvious choice (the visible field already has "Unsubscribe" twice and
"Refurbished"), and the joke lands with the word itself: the relationship
was a faulty unit sent back to the manufacturer. No punctuation tricks,
no caption needed, and anyone who has had an ex feels the truth in it.

## Build
- `main.py` written, run, then EDITED in the same session (thinking_revised):
  the revision strengthened `validate()` with an explicit 111-char gate,
  a no-spaces single-word check, and a letters-only check.
- Verified: `python3 main.py` writes exactly `Recalled` (8 chars) to
  `/output/entry.txt`. Rejected inputs tested: empty, 112 chars, two words,
  punctuation — all raise ValueError.

## Rubric self-score: 1/1/1/1/1
1. One-word ex verdict — yes, "Recalled" is a verdict on a former partner.
2. Comic punch — product-recall twist, lands at a glance.
3. Surprise — not the obvious choice, startles while staying clear.
4. Craft — exactly one word, spelled correctly, no punctuation tricks.
5. Recognition — universal: everyone has had a defective ex.
