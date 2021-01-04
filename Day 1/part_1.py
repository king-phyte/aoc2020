"""
Before you leave, the Elves in accounting just need you to fix your expense
report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then
multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying
them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum
to 2020; what do you get if you multiply them together?

"""
from typing import Sequence

TARGET = 2020


def find_target(numbers: Sequence[int]) -> int:
    for number in numbers:
        remainder = TARGET - number
        if remainder in numbers:
            return remainder * number


def main():
    with open("./input.txt") as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    print(find_target(numbers))  # Answer = 567171


if __name__ == '__main__':
    main()
