from pathlib import Path
import re


path = Path(__file__).parents[1] / "input" / "3.txt"
problem = path.read_text().strip()
pattern = re.compile(r"(mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\)|do\(\)|don't\(\))")
sum = 0
enabled = True
for match in pattern.finditer(problem):
    groups = match.groupdict()
    if groups["x"]:
        if not enabled:
            continue
        x, y = int(groups["x"]), int(groups["y"])
        sum += x * y
    else:
        enabled = match.group(0) == "do()"
print(sum)
