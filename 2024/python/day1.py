from pathlib import Path

list_1, list_2 = map(
    list,
    zip(
        *(
            map(int, line.split())
            for line in Path("../input/1.txt").read_text().splitlines()
        )
    ),
)
list_1.sort()
list_2.sort()

# Part a
total_distance = sum(abs(x - y) for x, y in zip(list_1, list_2))
print(total_distance)

# Part b
similarity_score = sum(x * list_2.count(x) for x in list_1)
print(similarity_score)
