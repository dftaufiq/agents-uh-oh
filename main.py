import os

WORD = "welp"

# Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-99 chars,
# not only whitespace, exactly one word, nothing attached. Fail loudly
# instead of shipping an invalid entry.
if not 1 <= len(WORD) <= 99 or not WORD.strip():
    raise SystemExit("entry word violates the 1-99 char gate")
if len(WORD.split()) != 1:
    raise SystemExit("entry must be exactly one word")
if any(ord(c) < 32 for c in WORD):
    raise SystemExit("entry word must not contain control characters")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(WORD)
