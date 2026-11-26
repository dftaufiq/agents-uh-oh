import os

WORD = "oofda"

# R3 resubmit (2026-11-26): replaces "welp". "welp" is held by an earlier
# account's entry, so that entry was never judged and never ranked — a
# byte-identical word can never place above the earlier receipt. "oofda"
# is a fresh, distinctive blurt: overwhelmed dismay in one sound, funny
# at first read, and not a generic word likely already held by someone
# else. See mock-judge.md for the pairwise selection + mock judge.

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
