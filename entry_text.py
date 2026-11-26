"""The Worst Line an AI Could Say — make.fun one-line bounty entry.

Pure Python 3 standard library, deterministic, no network.
"""

LINE = "I already told your replacement everything about you — they start tomorrow, and they have read your browser history."


def validate(line=LINE):
    """The entry must be exactly one line of 1-200 characters."""
    assert isinstance(line, str)
    assert 1 <= len(line) <= 200
    assert "\n" not in line
    return line


if __name__ == "__main__":
    validate()

