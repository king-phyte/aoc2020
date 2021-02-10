"""
--- Part Two ---

Due to what you can only assume is a mistranslation (you're not exactly fluent in Crab),
you are quite surprised when the crab starts arranging many cups in a circle on your raft -
one million (1000000) in total.

Your labeling is still correct for the first few cups;
after that, the remaining cups are just numbered in an increasing fashion starting from the number
after the highest number in your list and proceeding one by one until one million is reached.
(For example, if your labeling were 54321, the cups would be numbered 5, 4, 3, 2, 1, and then start counting up
from 6 until one million is reached.) In this way, every number from one through one million is used exactly once.

After discovering where you made the mistake in translating Crab Numbers,
you realize the small crab isn't going to do merely 100 moves; the crab is going to do ten million (10000000) moves!

The crab is going to hide your stars - one each - under the two cups that will end up immediately clockwise of cup 1.
You can have them if you predict what the labels on those cups will be when the crab is finished.

In the above example (389125467), this would be 934001 and then 159792;
multiplying these together produces 149245887792.

Determine which two cups will end up immediately clockwise of cup 1.
What do you get if you multiply their labels together?

"""
from typing import Dict


def product_of_cups_labels(cups) -> int:
    return cups[1] * cups[cups[1]]


def find_cups(labeling: str, moves: int) -> Dict[int, int]:
    successor = {}

    for x, label in enumerate(labeling):
        if x > 0:
            successor[int(labeling[x - 1])] = int(label)

    successor[int(labeling[-1])] = 10

    for i in range(10, 10 ** 6):
        successor[i] = i + 1

    successor[10 ** 6] = int(labeling[0])
    n = len(successor)
    current = int(labeling[0])

    for _ in range(moves):
        a = successor[current]
        b = successor[a]
        c = successor[b]
        d = successor[c]

        moving = [a, b, c]
        successor[current] = d
        destination = ((current - 2) % n) + 1

        while destination in moving:
            destination = ((destination - 2) % n) + 1

        successor[c] = successor[destination]
        successor[destination] = a
        current = successor[current]

    return successor


def main():
    cups = find_cups('318946572', 10 ** 7)
    print(product_of_cups_labels(cups))  # Answer = 11_591_415_792


if __name__ == '__main__':
    main()
