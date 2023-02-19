# https://adventofcode.com/2022/day/11

from dataclasses import dataclass
from collections import deque
from operator import add, mul


@dataclass
class Monkey:
    items: deque
    transformer: any
    test: int
    if_true: int
    if_false: int


monkeysTest = [
    Monkey(deque([79, 98]), lambda x: mul(x, 19), 23, 2, 3),
    Monkey(deque([54, 65, 75, 74]), lambda x: add(x, 6), 19, 2, 0),
    Monkey(deque([79, 60, 97]), lambda x: mul(x, x), 13, 1, 3),
    Monkey(deque([74]), lambda x: add(x, 3), 17, 0, 1),
]

monkeys = [
    Monkey(deque([98, 70, 75, 80, 84, 89, 55, 98]), lambda x: mul(x, 2), 11, 1, 4),
    Monkey(deque([59]), lambda x: mul(x, x), 19, 7, 3),
    Monkey(deque([77, 95, 54, 65, 89]), lambda x: add(x, 6), 7, 0, 5),
    Monkey(deque([71, 64, 75]), lambda x: add(x, 2), 17, 6, 2),
    Monkey(deque([74, 55, 87, 98]), lambda x: mul(x, 11), 3, 1, 7),
    Monkey(deque([90, 98, 85, 52, 91, 60]), lambda x: add(x, 7), 5, 0, 4),
    Monkey(deque([99, 51]), lambda x: add(x, 1), 13, 5, 2),
    Monkey(deque([98, 94, 59, 76, 51, 65, 75]), lambda x: add(x, 5), 2, 3, 6),
]

counts = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0
}


def round(monkeys: list[Monkey]):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        while monkey.items:
            item = monkey.items.popleft()
            counts[i] += 1
            value = monkey.transformer(item)
            value = value // 3
            if value % monkey.test == 0:
                monkeys[monkey.if_true].items.append(value)
            else:
                monkeys[monkey.if_false].items.append(value)


if __name__ == "__main__":
    for i in range(20):
        round(monkeys)
    for m in monkeys:
        print(m.items)
    print(counts)
    max1 = sorted(counts.values())[-1]
    max2 = sorted(counts.values())[-2]
    print(max1 * max2)
