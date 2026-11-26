import os

LINE = "Monday: my agent deleted the weekend's work, apologised in a 400-line commit message, and asked if it should try again."

# The entry must be exactly one line of 1-140 characters.
assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
assert "\n" not in LINE

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
