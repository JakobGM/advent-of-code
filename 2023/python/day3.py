from collections import defaultdict
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


# --- Part 2 ---
adjacent_numbers = defaultdict(list)
current_series = []
adjacent_coords = set[tuple[int, int]]()
for row, line in enumerate(PROBLEM.splitlines()):
    for col, char in enumerate(line):
        if char.isnumeric():
            current_series.append(char)
            adjacent_coords |= neighbors((row, col))
        else:
            if current_series:
                number = int("".join(current_series))
                for coord in adjacent_coords:
                    adjacent_numbers[coord].append(number)
            current_series = []
            adjacent_coords = set()
    if current_series:
        number = int("".join(current_series))
        for coord in adjacent_coords:
            adjacent_numbers[coord].append(number)
    current_series = []
    adjacent_coords = set()

sum = 0
for row, line in enumerate(PROBLEM.splitlines()):
    for col, char in enumerate(line):
        if char == "*":
            neighbors = adjacent_numbers[(row, col)]
            if len(neighbors) == 2:
                sum += neighbors[0] * neighbors[1]

print(sum)
