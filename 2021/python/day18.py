from functools import reduce
import math
from operator import add
from pathlib import Path


def read_lists():
    string_content = Path("input/day18.txt").read_text()
    problem = []
    for line in string_content.strip().splitlines():
        problem.append(eval(line))
    return problem


class Number:
    def __init__(self, l, level=0, parent=None):
        self.level = level
        self.parent = parent
        if isinstance(l, list):
            self.left = Number(l[0], level=level + 1, parent=self)
            self.right = Number(l[1], level=level + 1, parent=self)
        else:
            self.number = l

    def explode(self) -> "Number":
        for number in self:
            if number.level == 4 and hasattr(number, "left"):
                left = number.left
                right = number.right
                del number.left
                del number.right
                number.number = 0

                right_of = number.right_of()
                if right_of:
                    right_of.number += right.number

                left_of = number.left_of()
                if left_of:
                    left_of.number += left.number

                return self

    def split(self):
        for number in self:
            if getattr(number, "number", 0) >= 10:
                value = number.number
                del number.number
                number.left = Number(value // 2, level=number.level + 1, parent=number)
                number.right = Number(
                    math.ceil(value / 2), level=number.level + 1, parent=number
                )
                return self

    def right_of(self):
        if self.parent is None:
            return None
        if self.parent.right is self:
            return self.parent.right_of()
        for x in self.parent.right:
            if hasattr(x, "number"):
                return x

    def left_of(self):
        if self.parent is None:
            return None
        if self.parent.left is self:
            return self.parent.left_of()
        for x in reversed(list(self.parent.left)):
            if hasattr(x, "number"):
                return x

    def __iter__(self):
        yield self
        if hasattr(self, "number"):
            return
        for x in self.left:
            yield x
        for y in self.right:
            yield y

    def __repr__(self) -> str:
        if hasattr(self, "number"):
            return f"{self.number}"
        else:
            return f"[{self.level}]<{self.left!r}, {self.right!r}>"

    def __str__(self) -> str:
        if hasattr(self, "number"):
            return f"{self.number}"
        else:
            return f"[{self.left}, {self.right}]"

    def to_list(self):
        return eval(str(self))

    def __eq__(self, other: "Number") -> bool:
        return repr(self) == repr(other)

    def __add__(self, other: "Number") -> "Number":
        result = Number([self.to_list(), other.to_list()])
        while True:
            exploded = result.explode()
            if exploded:
                result = exploded
                continue

            split = result.split()
            if split:
                result = split
                continue

            break
        return result

    def magnitude(self) -> int:
        if hasattr(self, "number"):
            return self.number
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()


def parse_input():
    lists = read_lists()

    numbers = []
    for l in lists:
        number = Number(l=l)
        numbers.append(number)
    return numbers


def sum_list(l):
    return reduce(lambda x, y: x + y, l)


assert sum_list(
    [
        Number([[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]]),
        Number([7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]),
        Number([[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]]),
        Number([[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]]),
        Number([7, [5, [[3, 8], [1, 4]]]]),
        Number([[2, [2, 2]], [8, [8, 1]]]),
        Number([2, 9]),
        Number([1, [[[9, 3], 9], [[9, 0], [0, 7]]]]),
        Number([[[5, [7, 4]], 7], 1]),
        Number([[[[4, 2], 2], 6], [8, 7]]),
    ]
) == Number([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]])


assert sum_list(
    [
        Number([1, 1]),
        Number([2, 2]),
        Number([3, 3]),
        Number([4, 4]),
    ]
) == Number([[[[1, 1], [2, 2]], [3, 3]], [4, 4]])

assert sum_list(
    [
        Number([1, 1]),
        Number([2, 2]),
        Number([3, 3]),
        Number([4, 4]),
        Number([5, 5]),
    ]
) == Number([[[[3, 0], [5, 3]], [4, 4]], [5, 5]])

assert sum_list(
    [
        Number([1, 1]),
        Number([2, 2]),
        Number([3, 3]),
        Number([4, 4]),
        Number([5, 5]),
        Number([6, 6]),
    ]
) == Number([[[[5, 0], [7, 4]], [5, 5]], [6, 6]])

assert Number([[[[[9, 8], 1], 2], 3], 4]).explode() == Number([[[[0, 9], 2], 3], 4])
assert Number([7, [6, [5, [4, [3, 2]]]]]).explode() == Number([7, [6, [5, [7, 0]]]])
assert Number([[6, [5, [4, [3, 2]]]], 1]).explode() == Number([[6, [5, [7, 0]]], 3])
assert Number([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]).explode() == Number(
    [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
)
assert Number([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]).explode() == Number(
    [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]
)

assert Number(10).split() == Number([5, 5])
assert Number(11).split() == Number([5, 6])
assert Number(12).split() == Number([6, 6])

assert (Number([[[[4, 3], 4], 4], [7, [[8, 4], 9]]]) + Number([1, 1])) == Number(
    [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
)

assert Number([9, 1]).magnitude() == 29
assert Number([[1, 2], [[3, 4], 5]]).magnitude() == 143
assert Number([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]).magnitude() == 1384
assert Number([[[[1, 1], [2, 2]], [3, 3]], [4, 4]]).magnitude() == 445
assert Number([[[[3, 0], [5, 3]], [4, 4]], [5, 5]]).magnitude() == 791
assert Number([[[[5, 0], [7, 4]], [5, 5]], [6, 6]]).magnitude() == 1137
assert (
    Number(
        [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]
    ).magnitude()
    == 3488
)

problem = parse_input()
print(sum_list(problem).magnitude())

from itertools import product

m = 0
for x, y in product(problem, problem):
    if x == y:
        continue
    m = max(m, (x + y).magnitude())
print(m)
