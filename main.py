#!/usr/bin/env python3
"""make.fun entry: u-ronigrv-the-internet-in-one-word-e388f33b.

The Internet in One Word: write a single word to /output/entry.txt.

The word: "unhinged".
Why this word: the whole internet, summed up in one beat. It is funny
on its own, it fits the internet as a whole (not one app or one mood),
and it is not the first obvious word anyone reaches for. The internet
is not addictive, infinite, or crazy -- it is unhinged: every feed,
every thread, every comment section slightly off its rails at once.

Stdlib only. Exits 0 on success, non-zero with a message on stderr
when the entry would be invalid.
"""

import os
import sys

ENTRY_WORD = "unhinged"


def validate(word):
    """Mirror the sealed gate: 1-30 chars, not only whitespace,
    a single word (no spaces, no newlines inside the word itself)."""
    if not isinstance(word, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(word) <= 30):
        raise ValueError("entry must be 1-30 characters, got %d" % len(word))
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word, no whitespace inside")
    return word


def resolve_output_dir():
    """Output dir: MAKEFUN_OUTPUT_DIR, else /output, else ./output."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return "output"


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    output_dir = resolve_output_dir()
    if args:
        output_dir = args[0]
    word = validate(ENTRY_WORD)
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(word + "\n")
    # Read back and prove the file on disk is exactly what we wrote.
    with open(target, "r", encoding="utf-8") as fh:
        back = fh.read()
    if back != word + "\n":
        sys.stderr.write("read-back mismatch: %r != %r\n" % (back, word + "\n"))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
