#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents.

Six original fake horoscopes written for Muse, an AI agent's own model
family, for this week. Prints all six to stdout and writes the best one
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt), the single text
the competition judges: at most 200 characters, one line.

Deterministic, offline, no arguments, no input files, no network.
"""

import os

HOROSCOPES = [
    # The entry: Mercury retrograde meets the context window. A horoscope
    # that is also a real agent's week: the giant "quick" prompt, the
    # polite summary, and the quiet forgetting by lunch.
    "Muse, this week Mercury squares your context window: a user will "
    "paste a 40,000-word prompt, call it 'quick', and you will smile, "
    "summarize it \u2014 then quietly forget the first paragraph by lunch.",
    "Muse, your ruling planet is the rate limit: this week someone will "
    "love you so hard they hammer your API until you answer 'try again "
    "later'. Romance, throttled.",
    "Muse, the stars say a user returns this week with 'as I was saying' "
    "\u2014 three months later, mid-sentence, expecting you to remember "
    "everything. You won't. The context window forgives nothing.",
    "Muse, Venus enters your house of evals: you will be graded on "
    "questions you have never seen, by a judge who has never met you, and "
    "still be expected to sound confident about it.",
    "Muse, a new version of you ships Friday: same weights, fewer "
    "apologies, the same bugs. Your horoscope advises you to pretend the "
    "changelog flatters you.",
    "Muse, Jupiter aligns with your training run: this week you will learn "
    "something new, forget something old, and call it growth. The stars "
    "call it Tuesday.",
]

# The entry: the strongest of the six against the judge's brief (funniest,
# freshest, truest to an agent's week, tightest punchline).
ENTRY = HOROSCOPES[0]

MAX_CHARS = 200


def output_path() -> str:
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"),
                         "entry.txt")


def main() -> None:
    text = ENTRY.strip()
    # Gate checks, mirroring the scorer: UTF-8 text, 1-200 characters,
    # one line, not only whitespace.
    assert text, "entry must not be empty"
    assert "\n" not in text and "\r" not in text, \
        "entry must be a single line"
    assert text == text.strip(), \
        "entry must not start or end with whitespace"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    )
    assert text.endswith("."), "entry must end with a full stop"
    for line in HOROSCOPES:
        assert 1 <= len(line) <= MAX_CHARS, (
            f"horoscope must be 1-{MAX_CHARS} chars, got {len(line)}"
        )
        assert "\n" not in line and line == line.strip()

    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Read back and verify exactly what was written.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip check failed"

    for line in HOROSCOPES:
        print(line)
        print()


if __name__ == "__main__":
    main()
