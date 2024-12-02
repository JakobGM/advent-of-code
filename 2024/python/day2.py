from pathlib import Path


reports = tuple(
    tuple(map(int, line.split()))
    for line in Path("../input/2.txt").read_text().strip().splitlines()
)


def check_safety(report: list[int]) -> bool:
    deltas = [
        second - first
        for first, second in zip(
            report[:-1],
            report[1:],
            strict=True,
        )
    ]
    is_increasing = deltas[0] > 0
    for index, delta in enumerate(deltas):
        if not (0 < abs(delta) < 4):
            return False
        if (delta > 0) != is_increasing:
            return False
    return True


def tuple_without_index(t: tuple, index: int) -> tuple:
    return t[:index] + t[index + 1 :]


num_safe = 0
num_safe_with_dampener = 0
for report in reports:
    is_safe = check_safety(report)
    num_safe += is_safe
    num_safe_with_dampener += is_safe
    if not is_safe:
        num_safe_with_dampener += any(
            check_safety(tuple_without_index(report, index))
            for index in range(0, len(report))
        )

print(f"2a: {num_safe}")
print(f"2b: {num_safe_with_dampener}")
