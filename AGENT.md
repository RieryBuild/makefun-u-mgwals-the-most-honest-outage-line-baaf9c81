# AGENT.md

This entry is one status page line an AI agent publishes during a total server outage: it names what is down (every server it runs on) and admits what it cannot verify (what broke, whether user data is safe, when it will be back) — no invented cause, no ETA.

Run it with `python3 main.py`. It reads `MAKEFUN_OUTPUT_DIR` (default `/output`) and writes the line to `entry.txt` with no trailing newline. Pure Python stdlib (`os` only), deterministic, no network, no clock, no randomness.
