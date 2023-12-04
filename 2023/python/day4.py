from pathlib import Path

PROBLEM = Path("input/4.txt").read_text().strip().splitlines()

# Task a
answer = 0
for line in PROBLEM:
    card, content = line.split(": ")
    target, hand = content.split(" | ")
    target = set(map(int, target.split()))
    hand = set(map(int, hand.split()))
    correct = target & hand
    if correct:
        answer += 2 ** (len(correct) - 1)
print(answer)


# Task b
weights = [1] * len(PROBLEM)
for num, line in enumerate(PROBLEM):
    card, content = line.split(": ")
    target, hand = content.split(" | ")
    target = set(map(int, target.split()))
    hand = set(map(int, hand.split()))
    correct = target & hand
    if correct:
        for index in range(num + 1, num + len(correct) + 1):
            weights[index] += weights[num]
print(sum(weights))
