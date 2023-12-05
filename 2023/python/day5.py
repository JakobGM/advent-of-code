import itertools
import math
from pathlib import Path

PROBLEM = Path("input/5.txt").read_text().strip()
SEEDS, *SPECS = PROBLEM.split("\n\n")
SEEDS = list(map(int, SEEDS.partition(": ")[2].split()))


class Mapping:
    def __init__(self, line: str) -> None:
        self.destination_start, self.source_start, self.height = map(int, line.split())
        self.domain = range(self.source_start, self.source_start + self.height)

    def step(self, source: int) -> tuple[int, int]:
        target = self.destination_start + (source - self.source_start)
        remaining_height = self.height - (source - self.source_start)
        return (target, remaining_height)

    def applicable_for(self, source: int) -> bool:
        return source in self.domain


LAYERS = []
for spec in SPECS:
    header, *tables = spec.split("\n")
    layer = []
    for table in tables:
        mapping = Mapping(table)
        layer.append(mapping)
    LAYERS.append(layer)


def traverse(seed: int) -> tuple[int, int]:
    position = seed
    remaining_height = math.inf
    for layer in LAYERS:
        try:
            mapping = next(
                mapping for mapping in layer if mapping.applicable_for(position)
            )
            position, new_height = mapping.step(position)
            remaining_height = min(remaining_height, new_height)
        except StopIteration:
            pass
    return position, remaining_height


# --- Part One ---
min_position = math.inf
for seed in SEEDS:
    position, _ = traverse(seed=seed)
    min_position = min(min_position, position)
print(min_position)

# -- Part Two ---
min_position = math.inf
for seed_start, seed_length in itertools.batched(SEEDS, n=2):
    seed_range = range(seed_start, seed_start + seed_length)
    seed = seed_start
    while seed in seed_range:
        position, height = traverse(seed=seed)
        min_position = min(min_position, position)
        seed += height
print(min_position)
