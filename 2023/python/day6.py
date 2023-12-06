import math
from pathlib import Path


PROBLEM = Path("input/6.txt").read_text().strip()

times, _, distances = PROBLEM.partition("\n")
times = list(map(int, times.removeprefix("Time:").split()))
distances = list(map(int, distances.removeprefix("Distance:").split()))


def bounds(time, distance) -> tuple[float, float]:
    distance += 1e-10
    determinant = time**2 - 4 * distance
    sqrt_determinant = math.sqrt(determinant)
    upper = (time + sqrt_determinant) / 2
    lower = (time - sqrt_determinant) / 2
    return (lower, upper)


def winning_range(time, distenc) -> int:
    lower, upper = bounds(time, distance)
    return math.floor(upper) - math.ceil(lower) + 1


prod = 1
for time, distance in zip(times, distances, strict=True):
    band = winning_range(time, distance)
    prod *= band
print(prod)

prod = 1
time = int("".join(map(str, times)))
distance = int("".join(map(str, distances)))
print(winning_range(time, distance))
