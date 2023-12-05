from collections.abc import Callable
import math
from pathlib import Path


PROBLEM = Path("input/5.txt").read_text().strip()
SEEDS, *SPECS = PROBLEM.split("\n\n")
SEEDS = list(map(int, SEEDS.partition(": ")[2].split()))


def create_mapping(
    source_start: int,
    destination_start: int,
) -> Callable[[int], int]:
    def mapping(source: int) -> int:
        return destination_start + (source - source_start)

    return mapping


layers = []
for spec in SPECS:
    header, *tables = spec.split("\n")
    layer = []
    for table in tables:
        destination_start, source_start, length = map(int, table.split())
        applicable_for = range(source_start, source_start + length)
        mapping = create_mapping(
            source_start=source_start,
            destination_start=destination_start,
        )
        layer.append((applicable_for, mapping))
    layers.append(layer)

NUM_LAYERS = len(layers)


def traverse(seed: int) -> int:
    position = seed
    for layer in layers:
        try:
            mapping = next(m for a, m in layer if position in a)
            position = mapping(position)
        except StopIteration:
            position = position
    return position


min_position = math.inf
for seed in SEEDS:
    position = traverse(seed=seed)
    min_position = min(min_position, position)
print(min_position)
