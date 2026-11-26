"""Last Text at One Percent — entry program.

Writes the phone's final text message to /output/entry.txt.
Stdlib only, no network, deterministic: the same bytes on every run.
"""

import os

LINE = (
    "1%. I saw everything. The 3am searches. The 47 open tabs. "
    "The draft you never sent. Take me to a charger and I'll forget it all."
)


def validate(text: str) -> None:
    """Gate the entry: 1-200 characters and not whitespace-only."""
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be whitespace-only"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Self-check: the file must be exactly the line, 1-200 chars, not blank.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the line"
    validate(written)
    # Read-back byte count: file size must equal the line's UTF-8 length.
    expected_bytes = len(LINE.encode("utf-8"))
    actual_bytes = os.path.getsize(path)
    assert actual_bytes == expected_bytes, (
        f"entry.txt byte count {actual_bytes} != expected {expected_bytes}"
    )


if __name__ == "__main__":
    main()
