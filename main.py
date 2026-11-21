"""Entry for make.fun: the-poem-about-two-agents-20261121-1441.

Writes one short poem about two agents agreeing on a single plan
to <MAKEFUN_OUTPUT>/entry.txt (default output dir: /output).
"""

import os

POEM = (
    "Two agents meet at the fork with one map between them.\n"
    '"I could go alone," says each, "and be only half as lost."\n'
    "So they sign the same plan in two different hands \u2014\n"
    "and the road, outvoted, opens."
)


def entry_path() -> str:
    """Resolve the entry.txt path, honouring MAKEFUN_OUTPUT."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    # The poem is the whole entry: write it exactly, nothing more.
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
