# Dad Joke Showdown — main.py
#
# Structure of the joke:
#   1. Stakes first: a son asks why dad brings a pencil to EVERY barbecue,
#      so the pencil sounds useless and the question sounds innocent.
#   2. Closing reversal: the punchline reframes the pencil as a tool with
#      one job at the grill — policing second helpings.
#   3. The pun "draw the line" does double duty: literally drawing with a
#      pencil, and idiomatically setting a limit on seconds.
#
# The program writes exactly one joke — no extra text, no trailing newline.

import os

JOKE = (
    "My son asked why I bring a pencil to every barbecue. "
    "I told him somebody has to draw the line at second helpings."
)


def main() -> None:
    # Competition gate: entry.txt must be 1-200 characters, so reject
    # anything outside that range instead of writing an invalid entry.
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(f"joke must be 1-200 characters, got {len(JOKE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
