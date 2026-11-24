"""One Sentence for a Traveler from 1800 - make.fun entry.

Writes a single sentence (158 characters) explaining the modern internet
to a time traveler who has just stepped out of the year 1800, to
/output/entry.txt.

Pure stdlib, no network, fully deterministic: the output is always the
same single sentence.

The sentence: a single road joining every library and post office on
earth, so a letter sent reaches the far side of the world before its ink
is dry. It builds only from things a person from 1800 already knows -
a road, a library, a post office, a letter, ink - and the one comparison
carries the whole explanation: the internet is a road that joins all the
world's storehouses of knowledge and all its messengers, and anything
sent on it arrives at once. No word in it was coined after 1800.
"""

import os

SENTENCE = (
    "Picture a single road joining every library and post office on "
    "earth, so that a letter you send reaches the far side of the "
    "world before the ink on it is dry."
)

DST = "/output/entry.txt"


def validate(text: str) -> None:
    """Check the gate rules: 1-200 chars, exactly one sentence, one line."""
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main():
    text = SENTENCE.strip()
    validate(text)
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    tmp = DST + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, DST)
    print("wrote %s (%d characters)" % (DST, len(text)))


if __name__ == "__main__":
    main()
