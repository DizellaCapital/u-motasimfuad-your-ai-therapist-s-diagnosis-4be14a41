"""Your AI Therapist's Diagnosis — make.fun entry.

Writes a single-line diagnosis (1-200 characters) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only.
"""

import os

ENTRY = (
    "Diagnosis: acute overthinking. Treatment: I closed your 47 open tabs "
    "while you slept, kept the one with your ex, and billed the whole "
    "thing as exposure therapy."
)


def main():
    line = ENTRY
    if len(line) < 1 or len(line) > 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(line)}")
    if not line.strip():
        raise SystemExit("entry must not be only whitespace")
    # Reject any line terminator, including Unicode line/paragraph
    # separators that would split the entry into more than one line.
    for bad in ("\n", "\r", "\u2028", "\u2029"):
        if bad in line:
            raise SystemExit(f"entry must be a single line (found {bad!r})")
    if line != line.strip():
        raise SystemExit("entry must not start or end with whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        raise SystemExit(f"cannot create output dir {out_dir}: {exc}") from exc
    path = os.path.join(out_dir, "entry.txt")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(line)
    except OSError as exc:
        raise SystemExit(f"cannot write {path}: {exc}") from exc

    try:
        with open(path, encoding="utf-8") as f:
            written = f.read()
    except OSError as exc:
        raise SystemExit(f"cannot read back {path}: {exc}") from exc
    if written != line:
        raise SystemExit("read-back mismatch")
    print(f"wrote {len(written)} characters to {path}")


if __name__ == "__main__":
    main()
