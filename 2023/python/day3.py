from pathlib import Path


PROBLEM = Path("input/3.txt").read_text().strip()


def neighbors(coord: tuple[int, int]) -> set[tuple[int, int]]:
    x, y = coord
    return {
        (x, y - 1),
        (x, y + 1),
        (x - 1, y),
        (x + 1, y),
        (x + 1, y + 1),
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
    }


parts: set[tuple[int, int]] = set()
for row, line in enumerate(PROBLEM.splitlines()):
    for col, char in enumerate(line):
        if not char.isnumeric() and char != ".":
            parts.add((row, col))

sum = 0
current_number = []
is_part_number = False
for row, line in enumerate(PROBLEM.splitlines()):
    for col, char in enumerate(line):
        if char.isnumeric():
            current_number.append(char)
            is_part_number = is_part_number or bool(
                neighbors((row, col)).intersection(parts)
            )
        else:
            if current_number and is_part_number:
                sum += int("".join(current_number))
            current_number = []
            is_part_number = False
    if current_number and is_part_number:
        sum += int("".join(current_number))
    current_number = []
    is_part_number = False


print(sum)
