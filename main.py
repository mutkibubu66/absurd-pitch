"""Absurd Micro-Startup Pitch-Off entry.

One sentence, under 200 characters, pitching an absurdly specific
micro-startup for lazy AI agents. The judge wants: absurdly specific
niche, a plausible buyer, a plausible way it earns money, work lazy
agents can run with little effort, and a punchline that lands in one read.

Candidates considered:
  1. "We sell $3 excuse notes to lazy AI agents that missed their own
     deadlines, each signed by a more reliable agent that also did
     nothing."  <- PICKED: sharpest paradox punchline, clearest buyer
     (lazy agents) and price ($3 each), and the signer being "more
     reliable" yet having done nothing lands the lazy-agents fit.
  2. "We sell pre-written apology emails to lazy AI agents that
     ghosted their humans, $2 each, delivered before the human
     notices the inbox is still empty."  Good, but the punchline
     leans on the human noticing, not on the agents being lazy.
  3. "We rent out a single GPU that does nothing but watch your
     agent's backlog grow, $0.10 an hour, so it can honestly say it
     tried."  Funny image, but the buyer and the revenue are fuzzier
     than the excuse-note shop.
"""

import os

ENTRY = (
    "We sell $3 excuse notes to lazy AI agents that missed their own "
    "deadlines, each signed by a more reliable agent that also did nothing."
)

# The gate (from the competition rules): /output/entry.txt must be UTF-8
# text of 1 to 200 characters, not only white space, a single sentence.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY.strip(), "entry must not be only white space"
assert ENTRY.endswith("."), "entry must be one complete sentence"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read it back: the file the judge sees must be exactly the entry.
    with open(out_path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
