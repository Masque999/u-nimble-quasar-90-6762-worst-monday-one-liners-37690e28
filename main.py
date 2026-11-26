import os

LINE = "Monday: my agent deleted the weekend's work, apologised in a 400-line commit message, and asked if it should try again."

# The entry must be exactly one line of 1-140 characters, with no
# leading or trailing whitespace and a proper ending.
assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
assert "\n" not in LINE
assert LINE == LINE.strip(), "line has leading or trailing whitespace"
assert LINE[-1] in ".!?", "line must end with terminal punctuation"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
