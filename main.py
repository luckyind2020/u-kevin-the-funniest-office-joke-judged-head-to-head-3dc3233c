"""One-line office joke entry.

Reads the joke from entry.txt (kept as a separate data file so the
line itself is the entry) and prints it to stdout.
"""

from pathlib import Path


def load_joke(path: Path) -> str:
    """Return the single joke line from *path*, stripped of whitespace."""
    return path.read_text(encoding="utf-8").strip()


def main() -> None:
    joke = load_joke(Path(__file__).with_name("entry.txt"))
    if not 1 <= len(joke) <= 200:
        raise ValueError(f"joke must be 1-200 chars, got {len(joke)}")
    if "\n" in joke:
        raise ValueError("joke must be a single line")
    print(joke)


if __name__ == "__main__":
    main()
