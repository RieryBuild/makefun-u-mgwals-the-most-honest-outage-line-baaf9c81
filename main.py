import os

ENTRY = "Every server I run on is down. I am writing this from outside them, and I cannot check what broke, whether your data is safe, or when I will be back."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
