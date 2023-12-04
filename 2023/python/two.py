import itertools
from pathlib import Path


problem = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip()


games = problem.splitlines(keepends=False)
games = Path("input/2.txt").read_text().strip().splitlines(keepends=False)

GAME = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

sum = 0
for game in games:
    index, game = game.split(":", maxsplit=1)
    _, index = index.split()
    index = int(index)

    low = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for round in game.split(";"):
        shown = {}
        for hand in round.split(","):
            num, col = hand.split()
            low[col] = max(low[col], int(num))
    prod = low["red"] * low["green"] * low["blue"]
    sum += prod
print(sum)
